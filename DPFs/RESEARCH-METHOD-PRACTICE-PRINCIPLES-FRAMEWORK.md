# Research Method Practice Principles Framework

**DocID:** `RMP` within **FPF Library**.

> Use these research methods to frame a question, choose and conduct an inquiry, assess what its results support and communicate the answer. You can also use them to assess or improve a research method.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Original edition:** 24 October 2026. For the version used, see [RMP.Sources:3](#rmpsources3---citation).
- **Status:** Eternal alpha. This working framework is open to correction as methods, sources and uses change. RMP.1–RMP.11 include ways to use an existing answer, stop an inquiry and improve a research method.
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content. Third-party material retains its own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Begin with your question and the results you have. You may need help interpreting a request, using a source that already answers it, choosing a design or specifying how to carry it out. Other entries help you reconstruct what researchers did, assess a claim or a threat to its credibility, synthesize disputed evidence, revise a knowledge account and return it to its users, or assess and improve a Method. Find the question or PatternID in the Table of Contents. The Readme gives worked introductions, the Architectural Reference explains connections among the eleven contributions, and the applications show how to use them together. To refer to this edition, use the [Citation](#rmpsources3---citation).


# Table of Contents

Find a pattern by question or PatternID. The Readme gives examples. Each pattern describes its Method, worked cases, evidence limits and conditions for stopping.

The PatternIDs RMP.1–RMP.11 give the methods stable addresses. The six Parts provide a reading order. Enter at any method whose inputs your question and existing records supply.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Research Method Practice Principles Framework Readme](#research-method-practice-principles-framework-readme) | Follow a research question through to a supported answer, a correction or a reason to stop. |
| [Research Method Practice Principles Framework Architectural Reference](#research-method-practice-principles-framework-architectural-reference) | Find how to use the eleven Methods separately or together, what each requires and how the repertoire compares with alternatives. |
| [RMP.Reference:1](#rmpreference1---the-practical-question-behind-research-and-engineering) | The practical question behind research and engineering |
| [RMP.Reference:2](#rmpreference2---forces-that-shape-the-first-result) | Forces that shape the first result |
| [RMP.Reference:3](#rmpreference3---research-membership-is-not-institutional-status) | Research membership is not institutional status |
| [RMP.Reference:4](#rmpreference4---question-frame-design-work-result-and-decision-remain-distinct) | Question, frame, design, Work, result, and decision remain distinct |
| [RMP.Reference:5](#rmpreference5---criticism-comes-before-method-prestige) | Criticism comes before method prestige |
| [RMP.Reference:6](#rmpreference6---pattern-relations-do-not-prescribe-a-research-lifecycle) | Pattern relations do not prescribe a research lifecycle |
| [RMP.Reference:7](#rmpreference7---use-question-qualification-and-design-selection-together) | Use question qualification and design selection together |
| [RMP.Reference:8](#rmpreference8---connect-operationalization-and-actual-trace) | Connect operationalization and actual trace |
| [RMP.Reference:9](#rmpreference9---connect-analysis-and-the-credibility-choice) | Connect analysis and the credibility choice |
| [RMP.Reference:10](#rmpreference10---connect-corpus-synthesis-and-exact-revision) | Connect corpus synthesis and exact revision |
| [RMP.Reference:11](#rmpreference11---connect-method-improvement-and-research-consequences) | Connect Method improvement and research consequences |
| [RMP.Reference:12](#rmpreference12---conditions-for-a-usable-combined-result) | Conditions for a usable combined result |
| [RMP.Reference:13](#rmpreference13---architectural-rationale) | Architectural Rationale |
| [RMP.Reference:14](#rmpreference14---what-the-repertoire-foregrounds-and-leaves-outside) | What the repertoire foregrounds and leaves outside |
| [RMP.Reference:15](#rmpreference15---intended-use-and-ordinary-non-use) | Intended use and ordinary non-use |
| [RMP.Reference:16](#rmpreference16---judge-the-connected-result) | Judge the connected result |
| [RMP.Reference:17](#rmpreference17---bias-and-the-reach-of-these-examples) | Bias and the reach of these examples |
| [RMP.Reference:18](#rmpreference18---failures-at-the-connection-between-the-patterns) | Failures at the connection between the patterns |
| [RMP.Reference:19](#rmpreference19---practical-consequences-and-revision) | Practical consequences and revision |
| [RMP.Reference:20](#rmpreference20---patternid-and-reader-order) | PatternID and reader order |
| [RMP.Reference:21](#rmpreference21---available-repertoire-and-scope) | Available repertoire and scope |
| [RMP.Reference:22](#rmpreference22---direct-result-relations-and-non-lifecycle-topology) | Direct result relations and non-lifecycle topology |
| [RMP.Reference:23](#rmpreference23---what-the-sources-contribute-to-the-shared-architecture) | What the sources contribute to the shared architecture |
| [RMP.Reference:24](#rmpreference24---using-fpf-for-the-source-answer) | Using FPF for the source answer |
| [RMP.Reference:25](#rmpreference25---external-result-and-authority-boundaries) | External result and authority boundaries |
| [RMP.Reference:26](#rmpreference26---public-returns-to-adjoining-practice) | Public returns to adjoining practice |
| [RMP.Reference:27](#rmpreference27---representative-case-coverage) | Representative case coverage |
| [RMP.Reference:28](#rmpreference28---publication-and-maintenance-boundary) | Publication and maintenance boundary |
| [RMP.Sources:1](#rmpsources1---source-use-and-currentness) | Source use and currentness |
| [RMP.Sources:2](#rmpsources2---edition-return) | Edition return |
| [RMP.Sources:3](#rmpsources3---citation) | Citation |
| [Cross-Pattern Application — RMP.Application](#cross-pattern-application) | Follow a pump seal, a stream anomaly, a historical claim, a calculation defect, a workplace experiment and a service restoration from the question to the finding and its use. |
| [Research Method Practice Principles Framework Sources and Edition Notes](#research-method-practice-principles-framework-sources-and-edition-notes) | Find what a source supports, the limits on its use, the contents of this edition and its citation. |

**Part I - Qualify the Question and Choose a Design or Stop**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [RMP.1 — Decide Whether a Question Needs Research and When to Stop](#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) | Stable | Does the question need research? Can an available source answer it, does another practice have the answer, or does some part remain open? | question and available sources, F.1, F.0.1 and A.10 for source use, E.8 for comparison with current practice, and relevant domain contributions |
| 2 | [RMP.2 — Choose a Criticism-Bearing Research Design or Stop](#rmp2--choose-a-criticism-bearing-research-design-or-stop) | Stable | What does existing evidence answer? If more is needed, is a suitable inquiry worth doing, does a missing condition prevent the choice, or can we finish with the limits of the evidence? | a ResearchQuestionBrief from RMP.1 or equivalent input, a qualified current frame, and relevant findings about the domain, measurement, access, ethics, safety and authority |

**Part II - Operationalization and Research Trace**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 3 | [RMP.3 - Operationalize the Research Design without Replacing the Question](#rmp3---operationalize-the-research-design-without-replacing-the-question) | Stable | How can we carry out the design so that the observations still answer the question and admit the intended criticism? Which failed premise needs attention? | a compatible brief and design from RMP.1/RMP.2 or another source, relevant domain results and conditions of practice, and RMP.4 for the record of actual work |
| 4 | [RMP.4 - Preserve a Criticism-Ready Research Trace](#rmp4---preserve-a-criticism-ready-research-trace) | Stable | Which claims or checks does the available material support, given what was recorded, reconstructed, changed, lost or kept under restricted access? | an ongoing or inherited inquiry and the intended examination, surviving plans and records, relevant findings from RMP.1/RMP.2 and plans from RMP.3 when available, and FPF A.10 and C.16 |

**Part III - Analyze Claims and Choose Credibility Work**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 5 | [RMP.5 - Analyze and Criticize the Research Claim under Its Method](#rmp5---analyze-and-criticize-the-research-claim-under-its-method) |  Stable  | What claim does the material support under the method used? How does a relevant criticism affect that conclusion? | material, analysis, claim and intended use, relevant plans from RMP.3 and actual history from RMP.4, returns to RMP.1/RMP.2 for identified questions, and RMP.6 if a credibility test warrants consideration |
| 6 | [RMP.6 - Choose a Credibility Test That Bears on the Research Claim, or Answer without New Testing](#rmp6---choose-a-credibility-test-that-bears-on-the-research-claim-or-answer-without-new-testing) |  Stable  | Does existing evidence answer this threat? If a test would help, can we obtain it at an acceptable cost? What can we conclude if we stop or if a necessary choice remains open? | claim, basis, use and threat from RMP.5 or an equivalent input, applicable methods and criteria, those responsible for the conditions of inquiry, and RMP.2/RMP.3/RMP.4 as needed |

**Part IV - Synthesize Evidence and Revise the Exact Contribution**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 7 | [RMP.7 - Synthesize a Research Evidence Corpus](#rmp7---synthesize-a-research-evidence-corpus) |  Stable  | What does this body of evidence establish? Where do shared evidence, different targets or missing material limit the conclusion? | a compatible question, synthesis design, operations and actual history, relevant returns to RMP.1–RMP.6, and RMP.8 when another claim or use depends on the result |
| 8 | [RMP.8 - Use Research Results to Retain or Revise an Episteme's Claims and Return Bounded Evidence](#rmp8---use-research-results-to-retain-or-revise-an-epistemes-claims-and-return-bounded-evidence) | Stable | Which claim or part of a model can we keep or revise? What evidence and limits does its user need? | analysis, criticism or synthesis from RMP.5–RMP.7 or another source, FPF accounts of epistemes and affected uses, and the criteria and authority for the intended use |

**Part V - Improve and Refresh Research Methods and Practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 9 | [RMP.9 — Decide Whether and How to Improve Research Methods and Practice](#rmp9--decide-whether-and-how-to-improve-research-methods-and-practice) |  Stable  | What should we retain or correct in this research method or practice? Would a further comparison justify the work and resources it requires? | a difficulty with an existing Method or a change in its research use, relevant Core Methods and field criteria, qualified existing evidence, and returns to affected RMP.1–RMP.8 contributions |

**Part VI - Reconstruct Practice and Explain Method History**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 10 | [RMP.10 - Reconstruct a Candidate Method Account from Practice Evidence](#rmp10---reconstruct-a-candidate-method-account-from-practice-evidence) | Stable | What account of the method does the surviving evidence support? What could an observation, critical-incident account or event log add? | ordinary recovery under A.3.1.MR, a research question and evidence strategy, RMP.2–4 where their results are missing, and A.3.1 for Method identity |
| 11 | [RMP.11 - Explain Method History with Discriminating Evidence](#rmp11---explain-method-history-with-discriminating-evidence) | Stable | How did methods or their relationships change? Which records distinguish the competing explanations, and how far do they support a descriptive or causal conclusion? | an identified Method or variant or an established family relation, source history from RMP.4 and corpus findings from RMP.7 when available, and C.28 for a causal claim |

# Research Method Practice Principles Framework Readme

## Practical entries

Start with the question that matters to the inquiry and the evidence you have. A design specifies what the observations must distinguish. The way you collect or recover material determines which comparisons you can make. Analysis, criticism and synthesis can support an answer, identify a limit or expose a premise of an earlier step that needs revision.

If the available results leave part of the research question open, use FPF B.5, **Choose the Next Reasoning Contribution**, to identify what another contribution would add. [RMP.Reference:6](#rmpreference6---pattern-relations-do-not-prescribe-a-research-lifecycle) explains how to connect the research methods and when a change warrants revisiting earlier work.

Start with the contribution whose inputs you have. The [Table of Contents](#table-of-contents) covers other questions. The [Architectural Reference](#research-method-practice-principles-framework-architectural-reference) explains why the methods belong here and what their combined use requires. When you seek help, ask for an explanation or a comment on your case in the language of your work.

Use [RMP.1 — Decide Whether a Question Needs Research and When to Stop](#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) to check whether an applicable source already answers the question. If it does, give the answer, its source and its relevant limits. If a knowledge question remains, explain what the inquiry seeks to establish, how another researcher can examine the connection from question to result, and the scope of the contribution. A suitable existing protocol can support an inquiry into a disputed claim. An established rule can also settle an ordinary case in its own practice.

For a manager considering a second approver, see [Should a second approver reduce customer waiting?](#rmpapplication5---app-rmp-05--should-a-second-approver-reduce-customer-waiting). Event records can support a delay forecast under stated conditions. To estimate the effect of adding an approver, establish how the queues operate. The application shows the comparison across branches with independent queues, how a shared queue changes its interpretation, and what a qualified analyst can supply.

The examples use constructed cases with stated professional premises. Research can change the evidence available for maintenance, environmental protection or another decision. The authority to make the decision belongs to its designated holder.

### RMP-SEAL — Separate routine qualification from a mechanism-validity inquiry

- **Situation:** A seal engineer needs to know whether an accelerated test supports a proposed use in pump maintenance, but the relation between laboratory degradation and service conditions may be unresolved.
- **Question:** What evidence can answer the engineer’s question? What happens to the conclusion if the comparison fails to distinguish the mechanisms or the laboratory result cannot be transferred to service?
- **First useful result or blocker:** An applicable source answer or a finding under the existing qualification procedure. If a knowledge question remains, state it and assess whether a feasible inquiry can answer it.
- **Start with:** RMP.1 for an unsettled question. Use [RMP.2 — Choose a Criticism-Bearing Research Design or Stop](#rmp2--choose-a-criticism-bearing-research-design-or-stop) directly when a compatible question, source account and useful stopping condition are already supplied.
- **Stop or return:** Give the answer the evidence supports. Use RMP.1 if the question has changed and RMP.2 if a design premise has failed. A decision about maintenance belongs to the authority responsible for it.

1. **Establish what is known about the mechanism.** In the [Pump-P4 application](#rmpapplication1---app-rmp-01--pump-p4-accelerated-seal-evidence), a qualified acceleration relation, test method and acceptance criteria may suffice for the engineering or assurance task. Evidence that the proposed acceleration changes the degradation mechanism may also answer the question directly. If plausible alternatives remain, use RMP.1 to specify what would support, narrow or defeat the proposed relation for the stated material and operating conditions.
2. **Construct a comparison that can distinguish the mechanisms.** In the [mechanism construction](#rmp2511---derive-and-repair-the-mechanism-comparison), two reference specimens have the same overall wear index and different degradation mechanisms. The index cannot tell the mechanisms apart. A qualified procedure for measuring a distinguishing signature lets the researcher compare accelerated and field-representative specimens under the required material and damage conditions. With RMP.2, the researcher can use sufficient evidence, select a feasible design, identify a missing result that blocks a needed selection, or give a reason to finish without a new study. Unknown marker discrimination blocks selection if the choice depends on it. Two necessary tasks of four to six non-overlapping investigator-days each could take eight to twelve days. A ten-day allocation covers some combinations, but does not ensure completion.
3. **Carry the intended comparison into specimen handling and measurement.** Once the marker, measurement procedure, material plan, safety conditions and access are suitable, use [RMP.3 - Operationalize the Research Design without Replacing the Question](#rmp3---operationalize-the-research-design-without-replacing-the-question) to specify specimen identity, allocation, observation timing and how the readings will enter the comparison. Three readings of one seal give information about that one specimen. If a specialist establishes that the marker cannot distinguish the mechanisms, return to RMP.2 with that result. Using a wear score instead would require evidence that it answers the mechanism question.
4. **Interpret the observations that survived.** With [RMP.4 - Preserve a Criticism-Ready Research Trace](#rmp4---preserve-a-criticism-ready-research-trace), trace the handling damage to specimen P4-07, its missing reading and the decision to exclude it. Use [RMP.5 - Analyze and Criticize the Research Claim under Its Method](#rmp5---analyze-and-criticize-the-research-claim-under-its-method) to examine what follows for the inference. The missing reading leaves the direction of bias open. Reproducing a simulated curve confirms its reproduction, while a claim about field performance needs evidence relating the model to field conditions. Use [RMP.6 - Choose a Credibility Test That Bears on the Research Claim, or Answer without New Testing](#rmp6---choose-a-credibility-test-that-bears-on-the-research-claim-or-answer-without-new-testing) to assess whether an attainable mechanism or field comparison would be worth its cost. A selected comparison still awaits results.
5. **Combine estimates of the same quantity.** In the corpus branch of the case, use [RMP.7 - Synthesize a Research Evidence Corpus](#rmp7---synthesize-a-research-evidence-corpus) to trace A and A2 to one test, B to an independent compatible test, and C to service replacement under different conditions. A2 adds detail about the first test. The two independent estimates of the laboratory mean-lifetime difference are 14 hours with standard error 4 and 8 hours with standard error 3. Under the justified common-effect model, inverse-variance weighting gives 10.16 hours with standard error 2.4. The normal approximation gives a 95% interval of about 5.46–14.86 hours. C can answer a separate service question.
6. **Revise the claims that rely on the result.** Use [RMP.8 - Use Research Results to Retain or Revise an Episteme's Claims and Return Bounded Evidence](#rmp8---use-research-results-to-retain-or-revise-an-epistemes-claims-and-return-bounded-evidence) to find the dependent claim. In the model example, a separate analysis supports a fitted wear relation for the dry laboratory. Its transfer to wet service remains unproved after the synthesis. Retain the dry-laboratory fit, withdraw the claim of demonstrated transfer and the service replacement-time prediction that depends on it, and tell the reliability practitioner which premise is missing. The engineering wear limit and any maintenance decision keep their own grounds.

A supplied result can support analysis, a credibility comparison or synthesis directly. If the common-effect premise fails, reconsider what the synthesis establishes. Qualified new field evidence can reopen the transfer question without repeating the laboratory calculation.

### RMP-CITIZEN — Investigate a stream anomaly without an affiliation gate

- **Situation:** Residents have downstream salinity records, a proposed explanation and material from other catchments. A comparison they intended to make becomes unavailable.
- **Question:** What do the surviving observations establish? How should the briefing reflect the loss of the intended comparison?
- **First useful result or blocker:** The observed pattern and the comparison or source relation still missing. If the question qualifies for research, identify a suitable inquiry or explain what can be concluded without a new study.
- **Start with:** RMP.1 if monitoring and research remain confused. With a selected field design, start at RMP.3; with inherited material, start at RMP.4.
- **Stop or return:** Report the supported observations and explain the limit on attribution. Use a qualified measurement result from the laboratory or another competent provider. Site access, use of community data and decisions about the environmental response depend on their respective permissions and responsibilities.

1. **Check what the monitoring rule answers.** In the [ResidentStream-S17 application](#rmpapplication2---app-rmp-02--residentstream-s17-salinity-anomaly), sampling under an established threshold and response rule can finish with the requested monitoring result. If the question concerns the cause, ask what would distinguish road-salt transport, seasonality and sensor drift. The question and the work establish whether this is research, whoever performs it.
2. **Relate the measurements to the design.** Given qualified measurement, safe access and suitable comparison periods, use RMP.3 to specify the site, period, hydrological conditions, sample and procedure. A laboratory can supply the measured value. The residents can then connect it to their site-period comparison.
3. **Account for the missing thaw observation.** Suppose the reference reach becomes inaccessible during the informative thaw and observations downstream continue. Use RMP.4 to record the downstream observations, the missing site-period and why it was missed. A later dry-weather reference reading concerns different conditions. If the design needs the paired thaw observation, return that loss to RMP.2. Use the surviving record for any narrower claim it supports.
4. **Report the pattern and the limit on its explanation.** With RMP.5, the residents may be able to describe the downstream pattern while its source remains open. They can finish with that finding. If a later matched observation could answer a remaining question, use RMP.6 to assess whether it is feasible and worth obtaining.
5. **Use other catchments for the questions they cover.** With RMP.7, compare the other studies under the conditions in which their observations were made. A similar chart elsewhere leaves the missed local event unobserved. Use RMP.8 to correct any unsupported local attribution in the briefing, keep the downstream finding and tell the recipient what is still unknown about the cause.

In the [historical application](#rmpapplication3---app-rmp-03--factory-closure-historical-transfer-probe), several histories repeat one memoir. An authenticated record dates the decision to close the factory before the protest said to have caused it. This chronology rules out that explanation for the decision. Its actual cause and the protest’s possible effect on later implementation remain open. With RMP.8 the researcher can give the museum editor the correction and its exact scope.

### RMP-CORRECTION — Repair an analysis and return its consequence without discarding a suitable method

- **Situation:** A completed analysis contains a calculation defect, and a later change in the observations may also challenge the method's fit.
- **Question:** Is the defect in the computation or the method? Under what conditions would a comparison of methods answer a further question?
- **First useful result or blocker:** A verified correction and any resulting change in the analysis or claim its users rely on. Under different conditions, the researcher may be able to select a method or explain which question about its suitability remains open.
- **Start with:** [RMP.9 — Decide Whether and How to Improve Research Methods and Practice](#rmp9--decide-whether-and-how-to-improve-research-methods-and-practice), using the actual difficulty and receiving conditions.
- **Stop or return:** Keep the suitable method after repairing the computation. If conditions have changed, report a proposed comparison as a plan until results are available.

1. **Locate the calculation error.** In the [calculation application](#rmpapplication4---app-rmp-04--retain-the-method-and-correct-its-research-consequence), the method for the independent observations 2, 4, 6 and 8 specifies sample variance with denominator `n−1`. The mean is 5 and the sum of squared deviations is 20. Dividing by `n` gives the reported 5. The specified denominator gives `20/3`. With RMP.4 the researcher can trace the computation and find the analyses that used it.
2. **Correct and verify the affected result.** Use RMP.9 to repair the denominator and retain the method. With RMP.5, recalculate the affected analysis. With RMP.8, return any changed uncertainty or conclusion to those who relied on it. The known-answer check settles this implementation defect. Earlier analyses that did not use the faulty calculation retain their support.
3. **Reassess the method for a different target.** Now the programme wants an equally weighted mean across independent sites. The numbers of dependent observations per site are unequal. Pooling all observations gives the sites different weights. Use RMP.9 to compare methods for the site-level quantity. A qualified statistician, existing simulation code and two investigator-days make it feasible to compare a t interval from independent site means with an interval obtained by resampling whole sites. The team has selected this comparison. Which procedure is suitable remains open until the comparison or other qualified evidence answers it. Restrict the unsupported uncertainty claim and reconsider the comparison if its cost, value, access or staffing changes.

# Research Method Practice Principles Framework Architectural Reference

**Edition:** The edition date appears at the beginning of the publication. The [source-use and currentness notes](#rmpsources1---source-use-and-currentness) give the dates and limits for the methodological sources.

Begin with the question and evidence available to you. An existing source may answer it. You may instead need to decide whether an inquiry is worthwhile, specify a design, recover what researchers did, assess a claim or its credibility, synthesize a body of evidence, revise a particular knowledge claim, assess a Method or explain how it developed.

Use RMP.1 to establish whether the question needs research. RMP.2 helps decide whether evidence suffices, a design is worth pursuing, a missing result prevents a needed choice or the work can finish with an evidence limit. RMP.3 turns the selected design into operations that preserve the question. RMP.4 keeps or recovers the records an examination needs. RMP.5 assesses the claim under its method, and RMP.6 considers further credibility work. RMP.7 synthesizes a body of evidence. RMP.8 helps retain or revise the particular claim or model contribution and return it to its users. RMP.9 distinguishes a defect in implementation from a question about the research Method and follows the consequences of any correction. RMP.10 reconstructs a candidate account of a Method when ordinary recovery leaves a question open. RMP.11 uses records and rival explanations to investigate Method history. Each contribution can enter where its inputs are available.

## RMP.Reference:1 - The practical question behind research and engineering

A reliability engineer may need to choose a pump maintenance interval. Residents may want to explain a stream anomaly. In either case, ask what the available sources or an established professional method can answer and whether an inquiry would add the knowledge still needed. RMP.1 and RMP.2 help establish a useful question, answer or limit before anyone commits to a study.

Engineering can change a system to produce an intended result. Research can change what is known about the system, its behavior, its causes or the conditions under which a claim holds. One practitioner or team can do both. In the seal case, the team may engineer a test rig and use the observations to assess how acceleration affects the degradation mechanism. The rig and the supported mechanism claim answer different questions. A maintenance decision can use that claim together with its engineering and operating criteria.

Science also names a social institution with organizations, occupations, careers, funding, journals and recognition. These can enable inquiry and impose obligations. To assess a particular case, ask what remains unknown, how the inquiry can change that knowledge and what criticism its answer must withstand. A university team may perform a routine qualification and a citizen group may investigate a disputed cause. RMP.1 gives working criteria for this repertoire. Each field still supplies its professional methods and criteria.

Use the methods to answer the part of the inquiry that matters now. A request to “prove that the change works” might become a question about whether a particular mechanism transfers. If that relation has already been qualified, ordinary engineering can use it. If an inquiry is needed, its operations must preserve the comparison that could reveal a failed transfer. A detailed record of a different comparison cannot supply the missing evidence. An existing result or an identified limit can also complete the work at any of the direct entries above.

## RMP.Reference:2 - Forces that shape the first result

| Working tension | How it changes use of this repertoire |
| --- | --- |
| A prompt answer can overlook a rival explanation or an important condition. | Use sources relevant to the question and identify when their answer is sufficient. Seek a stronger comparison if it could change the conclusion and its likely contribution justifies the work. |
| A familiar instrument or method may miss the error that matters. | Establish what criticism the answer must withstand. When a design choice is needed, compare how the feasible alternatives could reveal that error. |
| The team can sometimes choose a design before every detail is known. | Choose it if every remaining admissible combination preserves its design family, ability to withstand criticism and feasibility. If a missing result blocks a choice still needed, identify it. A decision to finish without a new study can leave that result unknown. |
| Combining methods may answer a richer question and create new demands. | Check shared resources and how the component results can be interpreted together, including disagreements. Some limits appear only when all the components are considered. |
| Research can take place in different institutional settings. | Apply the same membership criteria and establish the permissions, specialist contributions and constraints that matter in the setting. Use existing qualifications or permissions when they cover the work. |
| A sponsor’s intended action can bias the inquiry. | Keep the evidence capable of defeating or narrowing the favored claim. For a later decision, preserve the authority of its designated holder. |
| A protocol needs specific choices, while some methods develop through engagement with the material. | State which commitments were made in advance, allow justified changes under the method, and record when consequential choices changed and why. |
| Exhaustive recording can obscure a decisive choice or expose protected information. | Preserve what the intended examination needs. Identify the access available to its reader and which uses a loss or redaction prevents. |

## RMP.Reference:3 - Research membership is not institutional status

A company, public body, university, archive, community, independent practitioner or citizen group can conduct research. Ask whether the knowledge question remains open under the relevant sources, whether the inquiry as a whole faces a non-routine task of establishing knowledge under genuine uncertainty, whether a critic can follow the evidence from question to result, and what bounded contribution can be communicated. A routine operation or a previously justified protocol can be part of such an inquiry. Affiliation, publication plans and tool choice do not settle membership.

The same operations can serve different tasks. A seal test can qualify a product or test the relation that makes acceleration informative. A fully specified replication can examine a disputed claim. In [RMP.1’s paired assay case](#rmp157---one-supplied-protocol-two-different-epistemic-tasks), an established procedure also supplies a routine lot verdict under an accepted rule. Stream samples may support monitoring or an inquiry into rival causes. Reading sources can provide the answer directly or furnish material for historical source criticism.

## RMP.Reference:4 - Question, frame, design, Work, result, and decision remain distinct

The receiving question explains why the knowledge matters. A ResearchQuestionBrief specifies the intended change in knowledge, the current frame, the bounded question, the criticism an answer must withstand and the constraints. State both the evidence needed for an adequate answer and when the current work can finish with uncertainty, a justified refusal or a missing input. A design connects the question to observations or sources and suitable criticism. A protocol specifies what researchers intend to do. For a claim about conduct, records, analysis, publication, recognition or use, establish the relevant event or finding on its own grounds.

RMP.1 can supply a brief and RMP.2 a finding about the design. RMP.3 specifies operations or identifies the condition that prevents them. RMP.4 identifies the evidence available to the intended examiner. RMP.5 gives the supported claim and its criticism. RMP.6 identifies worthwhile credibility work and interprets a test result when one is available. RMP.7 gives an EvidenceSynthesis, RMP.8 an EpistemeChangeAndEvidenceReturn, and RMP.9 a ResearchMethodPracticeRevision, which can retain a suitable method or correct a particular defect. These results may share a document. Evidence of actual conduct, support for a domain claim, permission to study and authority for a later decision each come from the relevant source.

A Method pattern explains a recurring problem and its setting, the relevant forces, the solution, grounds, cases, limits, consequences and relations, including comparison with the best-known approaches under FPF. Language, notation, headings and file organization determine how readers encounter that content. A pattern language also relates its contributions to one another. One article can develop several contributions, and one Method can be presented in both an article and a pattern for different uses. [RMP.8:4.4.1](#rmp8441---make-a-research-method-contribution-recoverable-across-publication-forms) explains what a reader needs to repeat or adapt the work.

## RMP.Reference:5 - Criticism comes before method prestige
Explain how the design’s material could answer the question. Use a justified strategy when one is available. If a connection is missing, use C.39 with RMP.2. Work out what the answer must distinguish, recover a methodological operation that could distinguish it, follow it on available material and construct the missing connection. A failed comparison can show which observation, arrangement or question needs to change or which particular result is missing. When choosing whether to pursue a study, compare the resulting strategy with the real alternatives, including finishing on current evidence.

Experiments, field observations, qualitative and reflexive inquiries, historical source criticism, computational models, evidence synthesis and mixed designs expose different errors. Use RMP.2 to ask which could reveal a relevant rival explanation, source misuse, bias, dependence, loss of context or unsupported transfer. Specify which finding would defeat or narrow the claim.

Consider alternatives when their evidence would make a difference to the answer. A particular design choice remains on hold when plausible values of an unavailable input would change the design family, the criticism it can address or its feasibility. If the allocation finishes as QualifiedNoNewStudy, that unknown can remain a limitation. Obtaining it is a separate commitment. After selecting a design, treat an input as a PostSelectionNeed only if every admissible combination of remaining values preserves the selected relation.

## RMP.Reference:6 - Pattern relations do not prescribe a research lifecycle

Use FPF B.5 to see what the available results establish and what further contribution the inquiry needs. For a missing observation, RMP.4 helps identify the surviving material and RMP.5 the claim it can support. If a different use asks for a stronger claim, use RMP.1 to qualify that question and RMP.8 for any claims the evidence limit affects. Retain other adequate results.

`RMP.1 → RMP.2` expresses a dependency when design selection uses a qualified ResearchQuestionBrief and a compatible current frame. If those inputs are already available from a colleague or another source, start at RMP.2. Either method can answer the current request. Revisit RMP.1 when a change of question or frame matters and RMP.2 when a selection premise changes.

A compatible brief and selected design can supply RMP.3 directly. RMP.4 can start recording during an inquiry or work with inherited records. RMP.5 can examine a supplied analysis. RMP.6 can consider a threat to an identified claim before or after new work. RMP.7 can use a synthesis question, design and trace, and RMP.8 an analysis, criticism or synthesis result. Use RMP.9 for a question about Method performance, criticism or changed use. Revisit an earlier contribution when evidence, criticism or a Method finding changes its basis or warranted scope. The six reading Parts group different questions. A completed inquiry can stand without a Method-improvement project.

## RMP.Reference:7 - Use question qualification and design selection together

RMP.1 establishes whether research is needed and what knowledge would answer the question. RMP.2 determines what present evidence establishes and whether to select a feasible design, keep a needed selection open because a premise is missing, or finish without a new study while the evidence remains limited. Use both when the request leaves both questions open. Use either directly when its inputs are available.

For an ambiguous request, use [RMP.1:4.0](#rmp140---develop-the-question-from-available-material) if the distinction that would make the answer useful still has to be developed. Use the [qualification procedure](#rmp141---pattern-use-unfolding) to qualify the resulting question when needed. A source-based correction, an ordinary professional result or a specified gap can answer the current request. Where the inquiry meets the research conditions, the ResearchQuestionBrief gives RMP.2 the intended change in knowledge, the criticism to address and a useful point to finish. A colleague’s compatible brief can supply the same result.

With the brief and frame, use the [RMP.2 design comparison](#rmp244---compose-serious-design-or-stop-options). Compare alternatives against the same question while varying how evidence could answer it. For the seal, a mechanism experiment and a field-transfer comparison address different relations. Historical source criticism and corpus synthesis offer another possible contrast. Existing evidence may also suffice. For a selected design, identify the error it could reveal and the threats left open. The [four disposition branches](#rmp247---return-exactly-one-researchdesigndisposition) give the possible conclusions.

RMP.1 can finish when a source answers the question. RMP.2 can use that source work to compare the evidence with the brief’s answer condition. EvidenceSufficientStop means the evidence answers the question for this use. QualifiedNoNewStudy means no new study is selected and the evidence limit remains. Permission to finish the work can therefore coexist with an unresolved knowledge question.

If a design comparison changes the question, intended use or useful stopping point, revisit RMP.1. If it changes an instrument, access condition or another selection premise, revisit the affected RMP.2 comparison. An infeasible preferred design can leave the question sound. A supplied answer or an identified hold can finish the current request.

## RMP.Reference:8 - Connect operationalization and actual trace

With a selected design, use [RMP.3](#rmp3---operationalize-the-research-design-without-replacing-the-question) to follow an observation or source choice that matters to the answer. Specify its units, selection, comparison, timing, method and intended use. A qualified domain protocol may already specify much of this. Explain how these choices preserve the question and what change would undermine the comparison.

The ResearchProtocolAndOperationalizationMap identifies the operations that can be performed and any that remain blocked. A missing input may hold one operation while every admissible combination of values preserves the selected design. A measure, source or comparison that could defeat the intended criticism reopens RMP.2. A changed question or useful stopping point reopens RMP.1. Include joint access, resource and retention conditions in this assessment.

Use [RMP.4](#rmp4---preserve-a-criticism-ready-research-trace) to preserve evidence whose loss would prevent a relevant examination and to recover what earlier work can support. Distinguish plans, actual conduct, later reports and reconstructions. Trace how consequential selection and transformation connect observations, sources or computations to their use. Record what was known when a consequential choice changed and identify who or what contributed substantially, including any AI contribution.

An inquiry can preserve records for an intended criticism or analysis before it has a final claim. For inherited work, identify which plans survive, what was reconstructed later and what belongs to a new run. For each examination, establish what the intended critic can inspect. Controlled originals, public summaries and irrecoverable material provide different grounds.

One notebook may contain both the operational plan and the record of what was done. Distinguish those entries so readers can compare them. The result may be material that supports a particular analysis or a finding that the original comparison cannot be made. Use RMP.5 for the analysis and criticism, RMP.6 for a credibility question, or RMP.7 for synthesis when the question, design and surviving material support it.

## RMP.Reference:9 - Connect analysis and the credibility choice

Use [RMP.5](#rmp5---analyze-and-criticize-the-research-claim-under-its-method) to follow the connection from a consequential piece of evidence through the method to the proposed claim. Use an adequate existing analysis when available. Identify important planned and later choices, contrary evidence and uncertainty. State the claim the material supports and what a stronger claim would still require. A limited interpretation or finding that the answer remains open may be sufficient.

Use [RMP.6](#rmp6---choose-a-credibility-test-that-bears-on-the-research-claim-or-answer-without-new-testing) for a question about the credibility of an identified claim. Start with the claim, its basis, its use and the specific threat. Reproduction, replication, robustness, validation for a use, corroboration and transfer examine different relations. Compare what an attainable result could establish with the costs of access, preparation, performance, interpretation, protection, shared resources and displaced work.

A test can be chosen, specified, performed and interpreted at different times. Lack of access is evidence about feasibility. An inconclusive result leaves the tested proposition open. A decision to finish without a new test retains its uncertainty. If a feasible comparison later becomes worthwhile, revisit that choice. For a disputed requirement, distinguish the value of the function it protects from the authority to amend the rule.

## RMP.Reference:10 - Connect corpus synthesis and exact revision

Use [RMP.7](#rmp7---synthesize-a-research-evidence-corpus) when the question concerns what a body of evidence establishes. An adequate existing synthesis may answer it directly. Otherwise trace reports to their underlying studies or sources, including dependence, exclusions and missing contributions. Choose a synthesis appropriate to the question. It may pool estimates, compare without aggregation, develop an interpretation, reconcile historical accounts or relate findings of different kinds.

Two reports from one study can add detail about that study. Establish its dependence on other studies from their participants, data, comparisons and other relevant connections. A theme may describe a situated finding without giving its frequency in a population. When a common magnitude cannot be estimated, report what the corpus does establish and why the stronger estimate remains open.

Use [RMP.8](#rmp8---use-research-results-to-retain-or-revise-an-epistemes-claims-and-return-bounded-evidence) to establish whether an analysis or synthesis supports retaining or revising a wider claim, model or use. Match the subject and conditions on both sides and reconcile claims that rely on the result. Dating the factory decision leaves its later implementation open. Evidence for a laboratory wear relation can remain sound even when the transfer premise of a field prediction fails.

Give the answer, its basis, uncertainty and the limits on reliance. Where a correction affects a known use, reach the responsible party through a permitted route or apply it directly if your authority covers that use. A short linked explanation may suffice. If a further research opportunity arises, assess what it could establish and what obtaining it would cost.

For a result that includes a reusable Method, use [RMP.8's publication branch](#rmp8441---make-a-research-method-contribution-recoverable-across-publication-forms) to identify the knowledge conveyed in an article, pattern or framework. Reconstructing a derivation, rerunning a calculation, obtaining new measurements and transferring the Method need different inputs and criteria for agreement. The [calibration case](#rmp856---one-calibration-contribution-an-article-and-a-pattern) shows which steps and conditions must survive in a shortened account.

## RMP.Reference:11 - Connect Method improvement and research consequences

Use [RMP.9](#rmp9--decide-whether-and-how-to-improve-research-methods-and-practice) when the question concerns a research Method or its practice. Locate the difficulty in the method, its description or implementation, a particular execution, the performer’s capability or an affected claim. Retain an adequate method. For a determinate defect, a correction and the relevant verification can finish the task.

For an open choice, compare attainable alternatives for the same research purpose and the criticism the research must withstand. A new comparison is worth obtaining when its result could change the warranted answer and the full cost is justified. Otherwise retain the supported finding and restrict any unsupported use. Declining a comparison settles whether to undertake it. Method qualification requires evidence about the method.

A corrected analysis can be returned through RMP.5 and RMP.8 while a wider Method question remains open. If a Method change affects an operational choice, credibility claim or synthesis, trace the dependency and retain other supported results. To treat new work as research, apply the RMP.1 membership conditions. Use RMP.9 when there is a Method question to answer.

Core distinguishes Method identity, trial, fit, worth and variant. A.3.1.MI addresses introduction in practice. [RMP.9's source account](#rmp911---sota-echoing) connects these contributions to research. With C.11.MV, the present grounds may support a choice or a restricted set of candidates. Further inquiry depends on what can be obtained and whether its contribution justifies its cost. The research account can carry the choice and its grounds.

## RMP.Reference:12 - Conditions for a usable combined result

For a combination of methods, check that their contributions answer the same receiving question, intended change in knowledge and useful stopping condition. Compare their source basis, rival accounts, scope and specialist results. A design for another material or a different temperature mechanism may not answer a question about field seal degradation. Identify the missing relation. Requalify the question or obtain suitable evidence if the stronger answer is needed and attainable.

For a mixed design, [RMP.2's family comparison](#rmp245---preserve-design-family-differences) asks why each component is needed and how its result can be interpreted with the others. Check the participants’ shared workload, access windows, specialist time, resources and constraints over the same period. Explain what failure or disagreement in a component would mean for the claim. An additional method can resolve uncertainty, but agreement arising from shared data or assumptions cannot be counted as independent corroboration.

Consider a mixed inquiry into the stream anomaly with twelve investigator-days available. Field comparison requires six, archival comparison five and computational sensitivity analysis four. Suppose the three demands cannot overlap or share work. Each pair fits, but the three together need fifteen days. If all three results are necessary and all the work is still required, the proposed design exceeds capacity. An adequate existing result could reduce the work remaining. Otherwise compare a feasible arrangement when one is worth considering, or finish without a new study and state the evidence limit. Extra capacity requires its own decision. Dropping a component that supplies a necessary challenge changes the design. Lack of time leaves the adequacy of the evidence a separate question.

If different plausible capacity values prevent a needed selection, give the ResearchDesignHold under RMP.2. If the current allocation ends without a study, report the unresolved capacity as a limitation. Where multiple inputs are unknown, apply [RMP.2's joint-input test in RMP.2:4.3](#rmp243---expose-selection-changing-inputs) before treating them as PostSelectionNeed. The [RMP.2 result rule](#rmp247---return-exactly-one-researchdesigndisposition) identifies what to record and how to revisit the choice when an actual value falls outside the admitted range.

First establish that the selected design can answer the question, then use RMP.3 to examine the joint conditions of its proposed operations. RMP.4 records what was done and changed. A completed protocol or extensive trace can show how a comparison was lost, but cannot supply its missing evidence. Keep the supported question, design and unaffected material. Identify the failed relation and return it to the relevant work. RMP.5 can give a bounded claim and RMP.6 a credibility finding. Use RMP.7 or RMP.8 for synthesis or wider revision when needed, and RMP.9 for a distinct Method problem.

**Constituent actions in ongoing work.** Classifying an observation may be part of constructing an analytical comparison while an inquiry into an explanation is under way. If the question changes from describing cases to explaining their occurrence, a classification that ignores selection may no longer support the answer. Recording skill and statistical calculation can both be available while the operationalization between them fails. Use RMP.3 for that relation. B.1.5.EW helps explain which actions are part of the ongoing inquiry and what access, specialist capability and shared observation effort their combination requires. A later calculation can use earlier observations after collection has ended.

## RMP.Reference:13 - Architectural Rationale

Question qualification and design selection can be completed separately. Use them together when both an unresolved knowledge question and a strategy for answering it need work. A new source may settle the question directly. An invalid sensor may instead reopen the design while the question stays useful.

| Serious alternative | Why someone would choose it | Trade-off and when it is preferable |
| --- | --- | --- |
| Use FPF source and evidence methods with disciplinary sources directly. | Experienced practitioners can use original sources and familiar terms. | Prefer direct use when a source or domain method already answers the question. When both research membership and design remain open, RMP.1 and RMP.2 explain how to connect them, when to stop and which professional result a missing premise requires. |
| Start with the institution, occupation or familiar activity. | It helps place a case for staffing, administration or grant purposes. | Use this approach for an institutional classification. To distinguish routine qualification from inquiry into a disputed mechanism, examine what the work can establish. The same test applies to equivalent questions from citizen groups. |
| Use a standard design hierarchy or fixed research sequence. | A mature field may have an efficient rule for recurring questions. | Use that rule within its qualified scope. For different questions, examine whether the preferred design preserves source criticism, situated interpretation, transfer limits and useful stopping conditions. Use RMP.2 when that relation needs work. |
| Carry question and design in one template. | A single account reduces handoffs in a short stable inquiry. | Use it when convenient and keep the question distinguishable from the selected design. If the design quietly changes the question, readers need to be able to find that change. |
| Use question qualification by itself. | RMP.1 can use a sufficient answer or direct routine work to the relevant practice. | Finish there when that answers the request. If a seal or stream inquiry still needs to choose whether and how to study a qualified question, RMP.2 supplies the design decision, the reason for a hold or a justified stop. |
| Finish after question and design. | These may be the complete results needed before a study. | A selected design can settle the pre-study request. To specify detailed actions or preserve records of what researchers did, use RMP.3 or RMP.4 as appropriate. |
| Use one notebook for protocol and records of the work. | It can reduce paperwork in a small inquiry. | Mark what was intended, what occurred and what was reconstructed later. This lets a later reader assess changes and use inherited work. |
| Use a disciplinary handbook. | It can supply field-specific techniques, instruments and qualified procedures. | Use the source for the professional result it supports. The RMP methods connect that result to the research question, evidence and Method decision. |

Use qualified source, evidence and Method contributions for what they establish. RMP explains how their results enter a research question, design, operation, record of work, claim or credibility assessment. Use a professional result within the conditions its source establishes. State any missing relation between those conditions and the research use. Restating its method can save a reader a trip to the source, at the cost of preserving its qualifications in another account.


## RMP.Reference:14 - What the repertoire foregrounds and leaves outside

The repertoire helps researchers qualify a question against current knowledge, determine when present evidence is sufficient, identify a missing professional result, compare real design alternatives and decide whether a study is worth pursuing. It also addresses operational choices and records, criticism appropriate to the method, credibility and synthesis, revision of a particular claim, reconstruction and history of Methods, and retention or improvement of a research Method.

For general methods of using sources, measurement, inference, representation, uncertainty, comparison, value or decisions, use the applicable Core or domain contribution. Operating, monitoring, assurance and acceptance work retain their professional criteria and authority. The eleven research patterns rely on the relevant field’s competence, evidence and conditions of use.

## RMP.Reference:15 - Intended use and ordinary non-use

Use the method that fits the current question and the inputs available. You can qualify an unresolved research question, assess a design, specify an inquiry, recover actual material, examine a claim or its credibility, synthesize evidence, return a particular revision or assess and improve a research Method. RMP.10 and RMP.11 address questions about the reconstruction and history of Methods.

For routine literature searches, research administration, ethics or safety decisions, domain protocols, statistical methods, measurement, funding, publication requirements or an authorized operational decision, use the practice responsible for the result you need. Claims about what researchers did and what is true depend on relevant evidence.

## RMP.Reference:16 - Judge the connected result

Use the practical entries to find the relevant method. For each method you use, read its reasons and conditions with its checklist. When combining contributions, examine how they fit together using the questions below.

| Substantive question | A usable answer and its return when absent |
| --- | --- |
| Does the design address the brief’s question, intended use and stopping condition? | Identify the premises the comparison uses. Requalify a changed question. If compatibility of material, population, context or sources remains open, state the limit or obtain the missing evidence when needed. |
| Does the evidence answer the question, or has the allocation finished with limited evidence? | Give the adequate answer for EvidenceSufficientStop. For QualifiedNoNewStudy, give the bounded answer and the reason to finish without a study. Identify a missing result as a hold when it prevents a selection still needed. Those responsible for resources or permission keep those decisions. |
| Can the strategy expose the error or rival explanation that matters? | Identify what would defeat or narrow the claim, including the effect of shared assumptions or disagreement among components. Apply the [whole-combination conditions](#rmpreference12---conditions-for-a-usable-combined-result) when several methods contribute. |
| For a choice of design still needed, could remaining input values change its family, criticism, feasibility or a decision to decline it? | Consider each input and their jointly admissible combinations. Give ResearchDesignHold when an unknown prevents selection. After selecting a design, use PostSelectionNeed for an input whose full admissible range preserves that selection. A completed QualifiedNoNewStudy retains the evidence limit. |
| Do the proposed operations preserve the question and the criticism the design needs? | Follow a consequential observation or source choice through the arrangement. Use RMP.3 to identify a blocked operation or a premise that would change the design. |
| Does the receiving examination have the actual material and access it needs? | Use RMP.4 to distinguish plans, conduct, reconstruction, transformations and loss. State the particular examinations still supported and those prevented. |
| Does the analysis support the proposed claim under its method? | Use RMP.5 to trace material to claim, including consequential choices, contrary evidence, uncertainty and limits on stronger uses. |
| What does a suitable credibility examination establish, or what would conducting one cost? | Use RMP.6 to relate the threat to attainable results and the work needed. A current no-new-test answer may suffice. Report a chosen test and a result from a performed test under their respective conditions. |
| Does the synthesis preserve its question and the relations among its sources? | Use RMP.7 to assess source dependence, context, missing material and the grounds for combining results. If an aggregate is unwarranted, report the narrower finding. |
| Which assertion and use depend on the result? | Use RMP.8 to reconcile affected claims and preserve uncertainty. Return any correction to the use that needs it through a permitted route. |
| What has been established about this method and the research that relies on it? | Use RMP.9 to distinguish supported retention or correction, a justified comparison and a restriction on use. Return a changed result through RMP.5, RMP.8 or another affected contribution as appropriate. |
| What result has been supplied, and what can its user do with it now? | Identify the result, its evidence and limits, and the intended use it can support. Any later action remains subject to its own criteria and authority. |

Use the questions to examine the actual evidence and work. If a compatible brief already supports direct use of RMP.2, use it. When one premise changes, reconsider the conclusions and combinations that depend on it and retain the rest.

## RMP.Reference:17 - Bias and the reach of these examples

The constructed seal and stream cases emphasize engineering evidence and observable anomalies. The historical and interpretive contrasts show how different material can call for different criticism. The calculation case distinguishes an implementation defect from a Method question and from its consequence for a research claim. Use the examples to recognize choices and losses. For claims about performance in a field, use field evidence and the professional criteria of that tradition. RMP.2 compares design families, RMP.3 addresses their operations, RMP.4 their actual material and RMP.5/RMP.6 their claim-specific criticism and credibility work.

A sponsor may want a decision, while a researcher may need an explanation or a corpus finding for its own sake. Preserve alternatives capable of changing the answer, including one the sponsor favors. The [RMP.1 bias account](#rmp16---bias-annotation) and [RMP.2 bias account](#rmp26---bias-annotation) address assumptions about status, familiar activities, methods, tools and authority. [RMP.3](#rmp36---bias-annotation) examines operational selection and the researcher’s position. [RMP.4](#rmp46---bias-annotation) covers later reconstruction, unrecorded exclusions and limits on access. [RMP.5](#rmp56---bias-annotation) and [RMP.6](#rmp66---bias-annotation) address interpretive overreach, prestige, repetition and unnecessary acquisition. [RMP.7](#rmp76---bias-annotation) addresses corpus selection and dependence. [RMP.8](#rmp86---bias-annotation) addresses reliance on a wider model or receiving use. [RMP.9](#rmp96---bias-annotation) addresses novelty, easy-to-count indicators, unnecessary comparison and unsupported retention.

The same membership criteria can apply to groups with different access, skills, funding, archive rights and safe sampling windows. Those conditions affect which work is possible. Bounded communication requires enough evidence for a suitable critic to follow the reasoning. A permitted view of protected records can serve this purpose when it supports the intended examination.

## RMP.Reference:18 - Failures at the connection between the patterns

| Consequential misreading | Practical correction |
| --- | --- |
| Treat a qualified ResearchQuestionBrief as authorization to begin a favored test | The brief identifies the knowledge question. Use RMP.2 to justify the design if that choice remains open. Establish that the required permissions already apply or obtain them for the proposed work. |
| A detailed brief, design, protocol or trace concerns different material or a different question from its supposed input | Compare the question, source frame, material and intended use at the connection. Identify the changed question or missing evidence of compatibility. |
| Every component of a mixed design is feasible, so the combination is declared feasible. | Check shared capacity, burdens, access windows, and the integration claim for the whole set, as in the twelve-day example. |
| Keep a claim unchanged after losing the comparison on which it depends | Record what was lost, keep narrower uses of the surviving material and return the failed premise. Use independent evidence for the original claim if it exists. |
| Describe a protocol reconstructed after the event as a commitment made in advance | Establish the basis and date of the reconstruction. To claim an earlier commitment, use evidence that it was made at that time. |
| Treat a public summary as equivalent to its protected source for every criticism | Identify what each accessible view supports. For a stronger use, obtain permitted access when feasible or state the limit it leaves. |
| A repeated computation is treated as evidence that the model is adequate for any field use. | Preserve the computational result and examine the claimed model-to-field relation under RMP.5/RMP.6. |
| Treat a selected credibility test as a completed result | Identify what was selected, whether the test was conducted and what evidence it returned. |
| Count reports as independent corroboration or pool different quantities | Use RMP.7 to trace reports to underlying sources and establish the grounds for any transformation or synthesis. |
| Apply a correction to a different event or leave a dependent model claim unqualified | Use RMP.8 to match the assertion and reconcile the uses that rely on it. |
| Infer a Method improvement from a selected trial, or treat a costly test as evidence that present use is adequate | Use RMP.9 to assess the value of obtaining evidence separately from what any completed test supports. Restrict the unsupported use and preserve the limit on its dependent claim. |

## RMP.Reference:19 - Practical consequences and revision

A team can use an available source, recognize routine monitoring, develop a defensible inquiry or finish with an identified gap. Good operational choices and timely records preserve a comparison that could otherwise be lost. Analysis can narrow an explanation. Credibility work can strengthen or weaken its support. Synthesis can identify which sources add independent evidence and which concern a different question. A precise revision makes that finding usable without hiding its limits. A suitable Method can be retained after a local correction. If the Method or situation changes, decide whether a further comparison is worth the work and trace any consequence to the research result that depends on it.

Reconsider a use when a change in its question, recipient, source basis, rival explanations, mechanism, measurement, access, resources or authority affects the conclusion. Reconsider the repertoire when repeated cases expose a failure of its four research conditions, misroute a design, or need a missing or unqualified contribution to produce a promised result. Keep the case and identify what the method failed to supply. The [source-currentness account](#rmpsources1---source-use-and-currentness) identifies source changes that can reopen a relied-on methodological claim.

The examples show how to reach the bounded results described here. Wider disciplinary use requires the corresponding field methods and evidence. An empirical claim that the framework improves practice, or that a selected study produced its intended result, needs evidence of that outcome.

## RMP.Reference:20 - PatternID and reader order

`RMP.*` identifies Research Method Practice patterns. Their numbers provide stable addresses. The Table of Contents links the complete methods included in this edition.

| Available PatternID | Recurring practitioner difficulty | First useful result |
| --- | --- | --- |
| `RMP.1` | Does this request need research, an existing source answer or work under an established professional method? | `ResearchQuestionBrief` when research is warranted, or the supplied answer, professional contribution or source gap that answers the present request. |
| `RMP.2` | Decide whether evidence is sufficient, a useful feasible design is selected, a particular selection is held, or the current allocation closes with no new study. | One `ResearchDesignDisposition` |
| `RMP.3` | How can the selected design be carried out while preserving its question and intended criticism? | ResearchProtocolAndOperationalizationMap for the supported scope, or the specific blocked operation, design premise or question to revisit. |
| `RMP.4` | Preserve or recover actual research material for a named examination. | ResearchTracePackage with inspectable connections and explicit access, reconstruction and loss limits |
| `RMP.5` | Establish what the material supports under its Method and what criticism changes the claim. | Bounded ClaimCandidate with its CriticismRecord |
| `RMP.6` | What can resolve or qualify a threat to this claim, and what does an available test result establish? | CredibilityTestDecision, with any performed test and its result reported separately. |
| `RMP.7` | Establish what a contested corpus warrants under its synthesis question. | EvidenceSynthesis, adequate existing answer, useful refusal or exact input return |
| `RMP.8` | Which part of the knowledge account should be retained or revised, and what does its user need? | EpistemeChangeAndEvidenceReturn with the grounds and limits that matter to the affected use. |
| `RMP.9` | Is this research Method suitable for its use? What correction or comparison is warranted? | ResearchMethodPracticeRevision identifying supported retention, correction, change or restricted use. A proposed trial can remain unperformed. |
| `RMP.10` | What can observations of practice establish about a candidate reusable Method? | Candidate accounts with their scope, variants, evidence and uncertainty, or the narrower result the material supports. |
| `RMP.11` | How did Methods or their relationships change, and which records distinguish the historical explanations? | An account of the change, surviving rival explanations and evidence limits. Use C.28 for a claim that relies on causation. |

The six Parts group question and design (RMP.1–2), operational choices and records (RMP.3–4), analysis and credibility (RMP.5–6), synthesis and revision (RMP.7–8), Method improvement and retention (RMP.9), and practice reconstruction and Method history (RMP.10–11). Start where the relevant inputs are available. A supplied brief can support design selection, and a selected design can support operationalization. Record evidence during ongoing work or use inherited material before a final protocol or claim exists. Supplied analyses, threats to identified claims, evidence corpora or a changed research use can each provide their own point of entry. Use RMP.10 or RMP.11 directly when a practice or historical question and compatible materials are available.

## RMP.Reference:21 - Available repertoire and scope

| Contribution | PatternIDs | Available result and scope |
| --- | --- | --- |
| Question, current frame and design | `RMP.1`–`RMP.2` | A source or professional answer, a qualified research question or a specific gap. For design allocation, the result can be EvidenceSufficientStop, ResearchDesignDecision with any genuine PostSelectionNeed, ResearchDesignHold or QualifiedNoNewStudy. |
| Operationalization and trace | `RMP.3`–`RMP.4` | Operations that preserve the question or a specified obstacle, and an account of the surviving material and its limits for the intended examination. |
| Analysis, criticism, and credibility | `RMP.5`–`RMP.6` | A bounded claim with method-appropriate criticism, and a relevant credibility decision with interpretation of an actual test result when supplied. Either can finish the present question. |
| Synthesis, episteme revision and evidence return | `RMP.7`–`RMP.8` | A justified corpus finding, including a sufficient existing synthesis or a reason to decline a stronger inference. A finding about what to retain or revise, with grounds and limits for the user. |
| Research Method and practice improvement | `RMP.9` | Supported retention, correction or change for the named research use, or a restricted/stopped unsupported use. Relevant Core and field contributions retain their own scope. |
| Practice reconstruction | `RMP.10` | What can be recovered about a candidate Method from the evidence of practice. Ordinary recovery may suffice. A larger evidence programme addresses a remaining question when its contribution warrants the work. |
| Method history | `RMP.11` | Diagnostic historical comparison that preserves source dependence, surviving rivals and separate causal-use conditions. |

These eleven patterns explain how to obtain their results. A particular case also requires its own evidence, competence and authority. If a necessary external contribution is missing, state which part of the answer depends on it and what can still be established.

## RMP.Reference:22 - Direct result relations and non-lifecycle topology

- RMP.1:4.3 applies F.1, F.0.1 and A.10 to the receiving question and available source texts. The result is an answer with its source basis and limitations. A suitable supplied answer permits direct use.
- RMP.1:4.3.2 compares alternatives when their differences could change the answer. F.1 guides source selection; a claim about the best-known current answer also uses E.8's SoTA distinctions. The comparison can narrow the question, supply a sufficient answer or identify what remains to be investigated.
- Use a qualified question and its current frame from RMP.1 in RMP.2 when a design decision is needed. A supplied answer, a result from another practice or a specific source gap can finish the RMP.1 request.
- RMP.2 can finish with EvidenceSufficientStop or QualifiedNoNewStudy, or identify which missing result prevents a necessary selection. Use ResearchDesignDecision or a compatible selected design from elsewhere to begin RMP.3.
- Use RMP.3 to connect a selected design to operations and record needs. For a blocked operation, identify the particular input or professional result it needs. Return a failed design premise to RMP.2 and a changed question to RMP.1. Use any resulting correction in the operations that depend on it.
- With RMP.4, begin from ongoing work or inherited material. Trace the records and relevant changes to the examination they can support, even before a final claim exists.
- Operational choices can guide capture; actual loss or changed conduct can reopen the dependent design or question. Neither connection requires a fixed sequence.
- With RMP.5, examine the proposed claim against the surviving material and the method used. Give the supported answer or identify the specific premise the evidence defeats.
- Enter RMP.6 with a bounded claim, its basis, intended use and a specific threat. Use a sufficient existing result, select useful attainable testing, finish with a qualified answer without further tests, or identify the input that prevents a needed selection.
- Use RMP.7 to assess and synthesize a corpus under a compatible question, design and trace. Include source dependence, compatibility and missing material in the answer.
- With RMP.8, use available analysis, criticism or synthesis to establish which contribution to retain or revise. Return significant limits to the use that depends on it. An earlier answer can suffice where no wider claim needs attention.
- Use RMP.9 for a Method difficulty or changed research use. Trace the actual consequences for a question, operation, record, analysis, credibility finding, synthesis or knowledge account. A comparison can be proposed or selected before it has produced evidence.
- Use ordinary recovery under A.3.1.MR before undertaking additional investigation under RMP.10. If evidence of practice can answer a remaining question, return a candidate Method account with its scope. Admission of that Method has its own conditions. An adequate existing account can finish the reconstruction.
- Use RMP.11 to compare historical explanations against records and the relations among their sources. Use RMP.8 when a knowledge claim needs revision. A present architecture choice or causal attribution requires grounds appropriate to that use.
- Revisit RMP.1 if a change in the question, frame, recipient or stopping condition affects its result. Revisit RMP.2 if a premise of the design choice changes.

The corporate, citizen and historical applications illustrate different routes through these contributions. Use the route that fits the question, material and work already done.

## RMP.Reference:23 - What the sources contribute to the shared architecture

Frascati provides a cross-sector comparison for identifying research. UNESCO’s account of participation helps distinguish the inquiry from institutional affiliation. RMP.1 adapts those contributions to the knowledge task of the whole inquiry. The National Academies’ account of replication with new data explains how an existing protocol can examine disputed knowledge. Routine quality control can instead give a lot verdict under an accepted rule. A historical or citizen inquiry may address a particular event. The [Frascati comparison](#rmp146---frascati-criteria-mutated-for-this-boundary) explains these adaptations and their limits. Case evidence and permission to conduct a study have their own grounds.

For design, MRC/NIHR relates programme theory, context and key uncertainties to constructing and refining an inquiry. Cochrane uses conceptual models to connect intended intervention effects with assumptions and comparisons. RMP.2 adapts both accounts and uses C.39 to work backward from the question and forward through an actual operation to the resulting evidence. SRQR and AHA contribute criteria for situated and historical criticism. The National Academies distinguishes reproduction from replication. The [RMP.2 account](#rmp211---sota-echoing) describes what these sources support. Domain findings and a decision about action need their own grounds.

The pre-study arrangement combines these methodological contributions. PostSelectionNeed expresses a particular condition of this synthesis. For an unknown input that remains after selection, check that each admissible value and its combinations preserve the selected design. The worked choices and holds illustrate this rule. A reporting standard provides the requirements within its published scope. Empirical validation of the combined arrangement would require evidence about its use.

For operationalization and records, relate choices to the question and make significant changes and uses inspectable. Flake/Fried and Lakens explain which measurement and information choices can affect an inference. SPIRIT distinguishes details a protocol can specify in its scope, and TOP addresses the timing of commitments. Haven and the RTARG critique preserve justified evolution under a method and identify the limits of a generic checklist. RMP.3 uses these distinctions when specifying operations and deciding what a missing premise affects.

RMP.4 draws on source criticism and records of searches and computational runs to establish what material was used. CARE, FAIR and responsible-AI guidance contribute questions about rights, permitted access and substantial human or tool contributions. Apply the rules governing retention and disclosure to the particular material, and state which examination remains possible. Keeping everything can expose protected information and still omit a critical choice. A final narrative may omit the timing of that choice. Preserve the evidence that matters to the examination, using an adequate existing protocol and trace when available.

SCORE distinguishes examinations that depend on analytical choices, available computation and the criteria for comparing results. RTARG and AHA supply criteria for interpretive and historical claims. RMP.5 and RMP.6 use these contributions to connect the claim, its remaining threat and what a test could establish. A sufficient existing analysis or a reasoned finding without a new test may answer the question.

For synthesis, Cochrane addresses dependence, the grounds for quantitative models, alternatives and missing evidence. Its qualitative guidance and JBI distinguish integration for a common question from separate syntheses of different aspects. CERQual assesses confidence in a particular review finding. AHA source criticism helps distinguish independent historical evidence and event chronology from the number of narratives. With RMP.7, use the relevant contributions for the corpus question. RMP.8 connects the finding to the claims and uses that depend on it.

For Method improvement, statistical simulation design, transparency and failure handling help specify a comparison, its target, performance and limits. RTARG and AHA preserve interpretive and source-use criteria a generic benchmark can miss. RMP.9 uses these contributions to distinguish supported retention, a particular correction and a worthwhile decision to acquire more evidence. With C.11.MV, adequate present grounds can support a choice. Further inquiry requires an attainable gain worth its full cost.

These sources support a reasoned synthesis across several research families. An empirical claim about the effectiveness of that synthesis needs evidence of its use. A stronger comparison, changed question or observed failure can reopen the affected Method when it changes the warranted answer.

Frascati 2015 serves as a statistical-methodology comparator. The National Academies report supplies distinctions such as reproduction and replication. Reporting guidance specifies transparency obligations within its field. For their bibliographic bases, dates, qualifications and conditions of use, see the [source-use and currentness notes](#rmpsources1---source-use-and-currentness). Reconsider a methodological claim and the comparisons that depend on it when a stronger source or an observed misrouting changes its grounds.

## RMP.Reference:24 - Using FPF for the source answer

Begin with the question and available material in RMP.1:4.3. Use F.1 to find or select sources for the answer, F.0.1 to recover the source’s meaning of a consequential expression, and A.10 to relate evidence and provenance to a particular claim. For a claim about the best-known current answer, use E.8:11 to compare the relevant SoTA contributions. State what the sources answer and which question their conditions or omissions leave open.

Reuse an existing answer when its question, sources and conditions fit. For a conceptual synthesis in framework authoring, F.0.2 may supply the needed contribution. For a broader, refreshable SoTA collection, use G.2 within its declared frame. For appraisal and synthesis of a research corpus, use RMP.7.

Use FPF C.16 when specifying an observation under RMP.3 or distinguishing an instrument indication, measurement result and derived value under RMP.4. Use the field’s methods for the instrument, its validity and any case-specific measurement result.

## RMP.Reference:25 - External result and authority boundaries

Domain practice supplies qualified knowledge of phenomena and mechanisms, instruments, measurements, admissible observations, validity criteria, safety and the conditions under which a claim is true. Core supplies Methods for identity, repertoire, requirements, performance and provision, qualification, trial, fit, worth and variants. A.3.1.MI addresses introduction and revision in practice. Use the results of operations, audit, evaluation, assurance, acceptance, governance or administration for the questions they cover.

Establish the permissions or decisions that govern ethics, rights, confidentiality, privacy, security, community control, access and resources for the work in question. Use an existing permission within its scope or seek a needed decision from the responsible holder. These conditions may change the research question or design.

Research can return a bounded change in knowledge, its evidence and its relevance to the intended use. To choose a maintenance interval, remediation, policy, release, treatment, compliance response, employment action or personal course of action, use the applicable criteria and authority. One practitioner can perform both kinds of work if qualified and authorized for them.

## RMP.Reference:26 - Public returns to adjoining practice

Use a companion publication when the question belongs to an adjoining practice. Apply its method or use a qualified existing result for the case. Finding a reference identifies where the needed contribution is explained.

To read an FPF pattern, use the complete specification in a reader that can search for its full heading. If you need a local copy, [download the complete FPF-Spec.md](https://github.com/ailev/FPF/raw/refs/heads/main/FPF-Spec.md). The table gives the relevant headings and the result to bring back.

| Needed contribution | Where to continue and what to bring back |
| --- | --- |
| Develop a missing research strategy. | Start with RMP.2:4.4 and its worked seal construction. In the downloaded FPF specification, find `## C.39 - Find and Develop a Way to Obtain a Result` for the general recovery, construction and adaptation Method. Bring back an explained research evidence relation or the precise missing operation, with its conditions and useful stop. |
| Recover an answer from existing sources. | Start with RMP.1:4.3 in this publication. In the downloaded FPF specification, find `## F.1 - Find and Select Sources for a Current Question`, `## F.0.1 - Source-Local Meaning Recovery`, and `## A.10 - Evidence Graph Referring: Claim-Bound Evidence and Provenance Graph` for their contributing methods. Bring back the answer, sources, applicability and remaining uncertainty relevant to the research question. |
| Specify or examine the measurement account used by the inquiry. | In the downloaded FPF specification, find `## C.16 - Measurement & Metrics Characterization (MM‑CHR)`. Bring back the measurand, applicable method and model, qualification, value and uncertainty needed for the research use, together with the competent domain or laboratory result. |
| Identify or improve a reusable research Method, or assess its fit. | Use [FPF C.39.MF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c39mf---choose-and-reopen-a-method-development-focus) to establish which Method is under consideration, [FPF A.3.1.WT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31wt---design-and-interpret-a-method-work-trial) for a trial in representative work when needed, and [FPF A.3.1.FT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31ft---qualify-method-fit-and-transfer) for fit or transfer. Bring the research question, its criticism requirement and any observed difficulty. With [RMP.9](#rmp9--decide-whether-and-how-to-improve-research-methods-and-practice), assess suitability or decide whether a trial would add evidence the research needs. |
| Engineer a system or arrangement for obtaining a needed result. | Use [Systems Engineering](Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) for an apparatus, laboratory or organization. Use [SYSE.24](Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse24---choose-how-the-project-will-obtain-a-needed-engineering-result) when how to obtain the result needs assessment or choice, and [SYSE.1](Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse1---choose-and-reopen-the-project-system-of-interest) when the system of interest for a product undertaking needs clarification. Give the engineering work the relevant research requirements. Return the engineered contribution and its conditions to the inquiry. The research claim, including an independently useful knowledge finding, requires its own evidence. |
| Continue routine operating observation or response. | Use [Operations Management (OPS)](Management%20DPF%20Suite/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) with the variables, response conditions and operating authority that apply. If a question about mechanism, validity or transfer remains unresolved and research is warranted, return that question to RMP.1. |

Use qualified sources for field-specific instruments, admissible observations, authenticity and safety. Apply the rights, consent and decision authority governing the case. The companion publications explain reusable methods. An actual measurement, permission or professional finding requires its own basis.

## RMP.Reference:27 - Representative case coverage

| Case family | Available RMP coverage | Preserved outside result |
| --- | --- | --- |
| Corporate accelerated seal evidence | Routine qualification or a question about mechanism validity. Current evidence, competing designs and their joint inputs can determine whether to study it. The case tracks marker failure, repeated readings of one specimen, handling damage and the limits of a laboratory result for field use. Reproducing a calculation and validating it for maintenance answer different questions. | Failure evidence, instrument validity, safety and access, assurance and the maintenance decision. |
| Citizen stream salinity | Monitoring may settle the question under an accepted threshold, or the source of an anomaly may remain open. The case follows site-period sampling, a lost comparison during thaw, the surviving downstream finding and the limit of later observations for the missed event. Design can be selected, held open or declined on the relevant grounds. | Environmental evidence, sampling competence, safe and legal access, qualified laboratory results and the regulatory response. |
| Historical factory closure | An authenticated source can answer the question or lead to further source criticism. The case compares historical inquiry and corpus synthesis, examines provenance, access, contrary material and archival loss, and shows how a counter-source can defeat one explanation. Corroboration can address the surviving claim. | Archive rights, provenance facts, constraints protecting people and institutional or public action. |
| Computational model | The case distinguishes design and credibility, identifies the inputs, model and environment for a run, traces substantial human or AI contributions and explains the limits of replaying an inaccessible service. Model interpretation and sensitivity depend on their assumptions. Reproduction, replication and validation for a use examine different relations. | The domain account and validation target, access to computation, data and code, and the engineering decision. |
| Contested evidence corpus | Trace eligible reports to studies and common sources. The case covers justified quantitative combination, a reason to decline a common estimate, situated and mixed synthesis, and return of a precise revision with its uncertainty. | Domain appraisal and synthesis criteria, access rights and authority for the receiving use. |
| Research Method and its implementation | A corrected calculation can leave the Method suitable and change an analysis and its claim. A changed research use can justify a comparison before evidence establishes the fit of either procedure. Reflexive, historical and mixed cases retain their own criteria. | Field criteria, actual comparison evidence, competence, source access, Method qualification and authority for the receiving use. |

These constructed examples show how to use the methods and which conclusions their premises support. To report a completed study, field effectiveness, reader recognition or downstream use, seek evidence of that event or outcome.

## RMP.Reference:28 - Publication and maintenance boundary

Use the Readme and connected applications to find a working situation. The full pattern explains the method, its cases, sources, conditions and limits.

When relying on a copy or sharing a reference, establish which edition and pattern bodies it contains. Different folders can hold different editions.

This publication is a Research Method Practice practitioner reference.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#research-method-practice-principles-framework-sources-and-edition-notes). To compare real research options, see [the earlier RMP.2:4.6](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp246---compare-on-one-decision-bearing-canvas) and [the current RMP.2:4.6](#rmp246---compare-the-designs-and-the-option-of-no-new-study).

## RMP.Reference:End


# Part I - Qualify the Question and Choose a Design or Stop


## RMP.1 — Decide Whether a Question Needs Research and When to Stop

> **Type:** Research Method Practice practitioner method pattern
> **Status:** Stable


### RMP.1:0 - Use This When

Use this method when you need to establish what an available source or ordinary professional practice can answer and whether an unresolved question warrants research. Start with the intended use, the question as far as you can state it and the material you have. If the needed distinction is still unclear, develop it in §4.0. Use a suitable existing answer or recover one through §4.3. For routine professional work, §4.4 identifies the result needed and how to obtain or supply it. Prepare a **ResearchQuestionBrief** when the inquiry meets all four research-membership conditions.

A request for “more data,” a favored answer in search of support, a surprising observation, a disputed transfer from test to field or a literature search with a possible answer can all prompt this question. To determine membership, examine the inquiry itself. Affiliation, job title, grant, venue, publication plan, tool choice or data collection gives no verdict on the four conditions.

Give an answer from available knowledge, a particular gap or a research question that states what remains to learn and what evidence would suffice. Use `RMP.2` for an open design question when a compatible `ResearchQuestionBrief` and current frame are available.

For a design choice use RMP.2. For an instrument, access or risk decision, engineering or policy action, or repair to a reusable professional Method, use the practice and authority responsible for that result.

#### RMP.1:0.1 - Working Terms

| Name in this pattern | What it denotes |
| --- | --- |
| receiving question and use | The practical or knowledge question, who needs the answer and how they will use it. If it informs a decision, identify whose values and authority apply to that decision. |
| qualified current frame | An account of what the sources support for the receiving question, the conditions under which they apply, and which important alternatives or gaps remain. It may be supplied or prepared through §4.3. |
| unresolved knowledge question | A question about a specified claim or contribution to a body of knowledge. An answer or criticism could support retaining, revising, narrowing, rejecting or adding it for the intended use. Establish the gap against relevant knowledge available for that use. |
| criticism demand | The error, rival explanation, source misuse, dependence, bias, missing context or unsupported transfer a defensible answer must be able to reveal. More than one design may meet that requirement. |
| answer condition | What the evidence must establish to answer the bounded question for its intended use, with the uncertainty that use permits. |
| useful stop | The point at which the evidence gives an adequate answer, or the present work can finish with a reasoned refusal, uncertainty or an identified missing input. In the latter cases state what remains open and what could reopen the inquiry. |
| ResearchQuestionBrief | The bounded question, current frame, intended change in knowledge, criticism requirement, constraints, answer condition and conditions for stopping or reopening work when all four membership criteria hold. A brief can supply RMP.2. |
| exact supplied-result return | An existing result from sources, comparison, evidence assessment or retrieval that answers the question within a specified scope and limits. |
| exact non-research return | The precise question, available material, ordinary professional result needed and where it can be supplied or obtained. Include any condition that would reopen the research question. Examples include qualification, monitoring, troubleshooting, audit and evaluation. |
| research-boundary hold | The missing or stale source or result, the decision about research it prevents, its source or supplier when known, and the condition for reconsidering the question. |

Identify what each contribution changes and what evidence supports it. An inquiry may change the knowledge account. An operating, physical, social or administrative change needs the corresponding action, and an authorized decision when applicable. One may use the research result in making that decision.

### RMP.1:1 - Problem Frame

A laboratory can run a qualified engineering test or examine the mechanism that makes the test relevant. Stream measurements can implement monitoring or investigate rival explanations. Reading sources may return a sufficient answer or supply evidence for a synthesis. Interviews may evaluate a programme against stated criteria or examine competing interpretations and contrary cases. Identify the question the actual work is meant to answer.

Research membership depends on the knowledge unresolved for a particular use, the task of the whole inquiry, the criticism an answer must withstand, the evidence a critic can inspect and the bounded contribution to be returned. A fully specified protocol can serve such an inquiry. Institutional affiliation and originality of procedure do not determine membership.

Examine an ambiguous request far enough to identify what is needed. If an applicable source already answers it, return that answer and its conditions. Apply the research criteria when a knowledge question remains open.

### RMP.1:2 - Problem

Searching, measuring, experimenting, coding, surveying or publishing can apply an established method and give an ordinary result. Calling every such activity research misclassifies that work. Restricting research to named institutions can exclude an independent practitioner or a community group that has a genuine knowledge question and inspectable evidence.

A classification should help the work continue or finish. Give the ordinary result if available, identify the particular contribution still needed or state what would reopen the knowledge question. A general call for more research leaves these distinctions unresolved.

Define what would be sufficient for the use. Check the current knowledge before treating a personal surprise as a new question. Identify the claim the answer could change and the criticism that could defeat a favored explanation. Otherwise a topic or collection of data can grow without resolving the question.

### RMP.1:3 - Forces

- A broad topic becomes answerable when the use, subject, relevant unit or case, contrast, constraints and sufficient result are clear.
- A quick source answer saves Work, while a weak or stale source cut can create false closure.
- A familiar protocol feels systematic, while routine execution does not establish an unresolved knowledge question.
- A surprising observation can open inquiry, while surprise to one performer is not qualified novelty.
- A decision can motivate research, and a question about knowledge can stand on its own. A later decision keeps its applicable values and authority.
- Identify the criticism early enough to shape a design. Use RMP.2 when a design choice remains open.
- Traceability supports inspection, while a checklist or repeated measurement alone does not make Work research.
- A contribution is communicable when a suitable critic can examine its reasoning within the conditions of access. Publication, unrestricted access and institutional recognition address other questions.
- Apply the same research conditions to corporate, public, independent and citizen practice. Check the competence, ethics, safety, rights, confidentiality and access the particular inquiry requires.

### RMP.1:4 - Solution

Start with the question, or the material that could help formulate it. Use §4.0 when the distinction still needs to be developed. Look for a sufficient answer in existing material and apply the four membership conditions if a knowledge question remains. Give the result in the current exchange or work product. Use a ResearchQuestionBrief for an inquiry that meets all four conditions.

#### RMP.1:4.0 - Develop the question from available material

Use this branch when an observation, passage or other material is available but the claim or contrast that matters is still unclear. Examine what the material can reveal before judging the value or research status of the proposed inquiry.

Take a record, passage, attempted operation or observation. Recover what occurred or was asserted, how the material was obtained and the interpretation being used. Work through a consequence. You might contrast a case, change an assumption, or inspect a definition or intermediate operation whose contribution is unclear. For a reported count, establish what was counted before interpreting a change in the total. [FPF B.5:4.1.2](../FPF-Spec.md#b5412---find-useful-questions-and-possible-actions-from-incomplete-information) gives the general method. Use valid operations and evidence from the relevant field.

Use the difference you find to state a candidate question, what its answer could add and what remains open. A limited exploration can be worthwhile before its exact discovery is known when accessible material and an identifiable operation could reveal a useful distinction. Use C.11.DUA to compare that attainable gain with the full burden. Use an adequate existing answer and respect competence, access and resources. If another contribution is needed, show the material and where interpretation stops. Establish whether it can be obtained and continue with the questions the current material supports.

Return a question that remains open to §4.1 and the membership conditions in §4.2. A new distinction may instead support a sufficient source answer, an ordinary professional result or a precise gap. Give that answer. A better historical explanation, a narrowed claim or a newly expressible question can be useful even if no intervention changes.

#### RMP.1:4.1 - Pattern-Use Unfolding

1. **Establish who needs what answer and for what use.** Use §4.0 if the claim or distinction still needs to be developed. Identify the question, model, body of evidence or explanation that could change. The researcher may be its user. If another inquiry or an action depends on the answer, state that connection. For an action requiring permission or a decision, identify its holder and basis when known. If that authority is missing or unclear, state the limit on the action.
2. **Find what existing material can answer.** Use an applicable source answer directly. Otherwise follow §4.3 to locate relevant passages and establish their meaning, conditions and consequences for the question. Compare alternatives when their differences could change the answer or the need for a study.
3. **Finish with a sufficient source answer.** If the material answers the question for the intended use, give the answer, sources and limits and stop. Continue to the membership test when a knowledge question remains.
4. **Specify the possible change in knowledge.** Identify the claim or corpus contribution that could be retained, narrowed, rejected, qualified or added. State the phenomenon, case, population or corpus, relevant relation or contrast, constraints and smallest useful answer. A topic or collection plan can supply a starting point for forming this question.
5. **Apply the four conditions independently.** Establish the unresolved question, the whole inquiry’s non-routine knowledge task under genuine uncertainty, an inspectable path from question to evidence and criticism, and a bounded communicable contribution. The inquiry may use routine constituent actions or a justified supplied protocol. All four conditions must hold. Compare the inquiry with the nearest relevant ordinary use and identify what distinguishes them.
6. **Identify the criticism, adequate answer and conditions for stopping.** State the error or rival a useful answer must be able to expose. Specify the evidence needed for this use, which result would defeat or narrow the claim and what the inquiry leaves outside. Also state when the work can finish with uncertainty, refusal or a missing input, for example if further work lacks value or permission. Retain the unmet evidence condition in that result.
7. **Return one exact disposition.**
   - give the sufficient existing source answer and its limits.
   - give the ordinary professional result if available, or identify the work and who can supply it.
   - identify the source or professional result whose absence blocks a needed decision about research and the condition for reconsideration.
   - when the four conditions pass, give a ResearchQuestionBrief for the contribution still needed. Use RMP.2 for an open design choice.
8. **Keep later decisions with their holders.** The brief explains the knowledge question, its relevance and its criteria. A study design, authorization to act or later receiving decision each requires its own grounds.

#### RMP.1:4.2 - Four-Condition Research-Membership Test
Apply the test to the inquiry and the knowledge it aims to return. Running an assay, recruiting a participant or executing a specified analysis can be routine within research. The second condition concerns the knowledge task of the whole inquiry. Performers can use a design and interpretation criteria that are already justified.

For example, a justified protocol may specify how new data will challenge a disputed effect and how to recognize compatible, discrepant or inconclusive results. Until suitable evidence arrives, the relation remains disputed. In a quality-control case, a new measurement under an accepted rule may instead give a batch verdict. The first condition concerns a gap in current knowledge within the intended use. The second concerns examining or developing that knowledge. An unknown ordinary case value does not by itself supply either.

| Condition | Passing question | Does not pass | Reopen cue |
| --- | --- | --- | --- |
| Unresolved relative to a qualified frame and use | Could an answer or criticism change support for retaining, revising, rejecting, narrowing or adding a particular contribution to knowledge? | The question is new to this performer, or a qualified current source already answers it for the use. | A source gap, serious rival, material limit or changed use makes the contribution uncertain again. |
| Non-routine knowledge task of the whole inquiry under genuine uncertainty | Does the inquiry need to establish, criticize or develop a claim, explanation or applicability relation whose support remains open? | The accepted relation supplies an ordinary case result. The next measured value, verdict, schedule or execution remains to be observed. | A disputed explanation, validity or transfer relation needs examination. A suitable procedure may already exist. |
| Systematic and open to criticism | Can a critic trace the question to the sources, premises, intended moves, performed work, evidence, deviations, limits and conclusions relevant to the claim? | Stored records or repeated measurements leave a consequential link uninspectable. | The materials can now support a trace and a claim that criticism could narrow or defeat. |
| Bounded communicable knowledge contribution | Can a suitable critic examine the intended claim or corpus finding, its scope and limits? Who can use that result? | The sole intended result is an immediate control action, acceptance, compliance token, recognition, private belief or an unspecified increase in knowledge. | A bounded change in knowledge can be identified separately from an action or recognition. |

Use these four questions to establish membership. An experiment, review, laboratory, surprising graph or affiliation may suggest where to look. A qualifying inquiry can reuse an established design and criticism criterion. Use RMP.2 if selection remains open or RMP.6 for a replication or other credibility question with a compatible existing claim and basis.

#### RMP.1:4.3 - Answer from Existing Sources before Starting a Study

If a supplied answer fits the question, sources and conditions, use it. Otherwise use this route to establish what the sources answer and which part, if any, still needs investigation.

##### RMP.1:4.3.1 - Find and interpret the relevant material

1. **State the needed answer.** Explain the difficulty using the terms of the work and identify which understanding, claim, inquiry or action the answer could improve. If the distinction is not yet expressible, develop it from available material through §4.0. Use the available texts and search tools. Account for time or specialist input when they affect what can be resolved. Clarify an ambiguity that would send the inquiry in a different direction.
2. **Locate passages that can answer it.** Use the available texts, their contents and their terminology. Search the words of the question and useful alternatives. Follow a passage to definitions, conditions, examples or cited evidence when they change the interpretation. Use F.1 to find or select sources by what they contribute. One adequate identified source can answer the question.
3. **Resolve difficulties in the reading.** If the search misses expected material, try a different expression or source. Read enough of the surrounding passage to establish its meaning. F.0.1 can help with a consequential expression. If the passage concerns a different population, setting or use, identify the difference. Use another suitable source when available or report the limit. Give the corrected interpretation.
4. **Return what the sources support.** Give the answer with the passages, editions, uncertainties and omissions that affect its use. A.10 connects evidence and provenance to particular claims. Finish when the answer is sufficient. An existing explanation may contain the whole result. Record further search details when the question requires reproducing or diagnosing the search.

A missing text, unknown edition or unresolved applicability limits conclusions that rely on it. Preserve what can be answered and identify the source or competence needed for the remaining question. Further search is useful when what it might establish for the answer or its use justifies the cost. A remaining gap can stand as the result.

##### RMP.1:4.3.2 - Compare alternatives when their difference matters

Use this branch when existing sources offer materially different answers, or when the receiver needs the best-known current answer. Begin with the working question and the criteria that matter for its use.

Use F.1 to select sources that bear on the answer. For a best-known current answer, use F.1:4.2.1 and E.8:11 to compare serious alternatives, relevant failures and application effort. Date and adoption history can help identify sources. Prefer an approach on the grounds that matter to the present question.

Recover the assumptions, conditions and support for each proposed answer. For a claimed improvement, compare the earlier limitation with what the new approach repairs and what it leaves open. Consult the earlier source if the comparison depends on it. Historical influence and evidence that the current approach works answer different questions. State trade-offs where alternatives improve different characteristics or identify what would distinguish them.

Give the conclusion of the comparison and its consequences for the answer, applicability, remaining research question or stopping point. Use RMP.7 if a new corpus conclusion needs appraisal and synthesis. F.0.2 serves conceptual synthesis for framework authoring. G.2 serves a broader, repeatedly refreshed SoTA collection under its declared CG-Frame. A sufficient comparison can finish here.

#### RMP.1:4.4 - Nearest Non-Members and Exact Returns

| Nearest non-member | Exact return | Reopen RMP.1 only when |
| --- | --- | --- |
| Routine engineering qualification, verification or validation against supplied criteria | Give the test or qualification result for the engineering or assurance use. If a choice follows, its designated authority makes it. | Relevant sources leave a mechanism, validity, transfer or evidential relation open. A suitable examination may already exist or need construction. |
| Monitoring or measurement under established variables, thresholds and response rules | Use the observation or current-state finding in Operations or the domain monitoring practice. | A question about an unexplained pattern, rival causes, an invalid measure or transfer changes what the inquiry must establish. |
| Troubleshooting, incident response or fault isolation to restore an operating result | Give the supported diagnosis or restoration finding under the engineering, service or operations method. | A separate question about the episode, its mechanism or the suitability of the recovery method remains open and meets the four conditions. |
| Audit, compliance, programme evaluation or product acceptance under given criteria and authority | Give the required verdict, evaluation or acceptance result under the practice responsible for it. | The question now concerns the validity of the criteria, a causal explanation, transfer or another unsettled knowledge claim. |
| source retrieval, currentness checking, or bounded cross-source comparison sufficient for the use | Return the answer and the source, applicability and comparison limits needed by its receiver, using §4.3. | A material source gap or a new question changes what that answer can establish. |
| Ordinary application of a qualified professional Method | Use that method to produce the domain result, use a supplied result or seek the contribution from a qualified provider. | An unresolved question about fit, the underlying claim or a new case meets the four conditions. Use the corresponding Core Methods for Method identity, qualification, fit, trial, worth or variants, and A.3.1.MI for introduction. |

For adjacent work or a missing result, preserve the question, the usable material, the result needed and any condition for reopening the inquiry. Identify a supplier or responsible authority where the next work actually needs one. Give an adequate supplied answer to its user and finish.

#### RMP.1:4.5 - Record the Result

For an inquiry that passes the four conditions, include the following information in the ResearchQuestionBrief.

| Result position | Required content |
| --- | --- |
| receiver and use | Who needs the answer and what knowledge or practical use it serves. If the inquiry informs a decision, state that decision, any authority or permission already established and any gap that limits its use. |
| intended episteme change | Exact claim or corpus contribution that could be retained, narrowed, rejected, qualified, or added. |
| bounded question | Answerable question with phenomenon, unit, case, population or corpus, relation or contrast, constraints, and effective horizon where material. |
| qualified current frame | The source answer prepared through §4.3 or supplied for the same use, with its source editions, relevant alternatives, omissions and applicability limits. |
| membership account | Explain how each of the four conditions holds and how the inquiry differs from the nearest relevant ordinary use. State the knowledge task of the whole inquiry, including any routine actions or justified design it can reuse. |
| criticism demand | Principal error, rival, invalid source use, dependence, bias, missing context, or unsupported transfer that a defensible answer must expose. |
| constraints and professional results | Applicable domain criteria, measurement, instrument, safety, ethics, rights, confidentiality, access, resources or authority. Identify what is available and any missing condition the work depends on. |
| answer condition | What the evidence must establish for an adequate answer to the bounded question, including applicable uncertainty and scope. |
| work-stop and reopen conditions | When the present work can finish with an adequate answer, a refusal, retained uncertainty or a missing input. Identify any unmet evidence condition and what could reopen the inquiry. |
| source and result limits | What the supplied sources establish, the limits that matter to the use and which missing contribution cannot be inferred from them. |
| continuation | The brief and frame for an open RMP.2 choice, or other supplied inputs for the contribution needed. State separately any design selection, protocol, authorization or receiving decision already in place. |

If a supplied result answers the current question, give the answer with the source, scope and limits the user needs. The current exchange or existing work product may carry the complete result. Finish there.

For later reliance or another use, retain the source, scope, date or uncertainty that affects application of the answer. Use an adequate existing explanation and add a missing condition when the new use needs it.

For a non-research result or a research-boundary hold, identify the applicable relations in this table using the existing material or a short return.

| Return position | Required content |
| --- | --- |
| current question | The question as raised, or what the material allows you to clarify about it. Preserve the use that prompted it. |
| disposition basis | Supplied-answer sufficiency, nearest non-member, or named missing/stale source or owner result. |
| available material | Exact current results and limits worth carrying to the receiver or owner. |
| return target and expected result | What input or result is needed and who can supply it, if known. State any unresolved source or permission that limits further work. |
| effect and retry | What stops now, what can continue, and the condition that would reopen RMP.1. |

#### RMP.1:4.6 - Frascati Criteria Mutated for This Boundary

The OECD Frascati criteria provide a cross-sector comparison for research and development statistics. RMP.1 adapts them to inquiry that can be criticized on its evidence regardless of the performer’s institutional affiliation.

| Frascati criterion | RMP.1 use |
| --- | --- |
| novel | **Adapt.** Determine what remains unresolved in the relevant knowledge and use. Personal unfamiliarity is insufficient. The contribution need not claim patent novelty, publication priority or a global first. |
| creative | **Adapt.** Assess the non-routine task of the inquiry as a whole. It may construct or criticize an unsettled claim, explanation or applicability relation using a fully supplied design. The status of the particular procedure does not settle that of the inquiry. |
| uncertain | **Specify.** The defensible answer or route remains unsettled. Uncertainty about the schedule, process variability or execution risk can exist under fully accepted knowledge. |
| systematic | **Adopt.** Make the connection from question to result inspectable, including sources, premises, intended and performed actions, evidence, deviations, limits and stopping conditions relevant to that use. |
| transferable or reproducible | **Adapt.** Return a bounded contribution and enough evidence for a critic to examine or reuse the reasoning. The conditions for generalization, recurrence or replication with new data depend on the historical, qualitative, field, citizen or other inquiry. |

#### RMP.1:4.7 - First-Hour Qualification Card

If the question or useful distinction remains unclear, use §4.0 on the available material. Start the card with prompts 1–3. When prompt 3 gives a sufficient answer, return it under §4.5 and finish. Use prompts 4–8 when a question about research membership remains. Add a short statement or row where the necessary grounds are missing.

1. Who needs the answer, and for what use? If a later decision or permission is at issue, what authority has been established and what, if anything, remains open?
2. What do the available sources answer? Use §4.3 if the answer still needs to be recovered or compared. Retain the sources and limits that matter here.
3. Does that source answer resolve the receiving question? If yes, return it with the sources and limits needed for this use, and stop here.
4. What exact episteme could change, and what phenomenon, unit, case, corpus, relation, or contrast bounds it?
5. Why is the question unresolved relative to the frame rather than merely unfamiliar?
6. What knowledge claim or explanation must the whole inquiry establish, criticize or develop, beyond an ordinary case result under an accepted rule? What remains uncertain, and which suitable design or criticism choices can already be reused?
7. How could a critic inspect and defeat or narrow the claim?
8. What evidence would make the answer adequate? Separately, when can the current work finish with uncertainty or refusal, and what could reopen it?

If a missing source or professional result prevents a decision the current branch still needs, state the hold and what it affects. When the work belongs to another practice, give its supported result or identify the contribution needed. A sufficient answer finishes the corresponding branch.

#### RMP.1:4.8 - What Changes in Practice

A practitioner can start with a record whose significance is unclear and develop the question from its contents. Use a source answer or an ordinary measurement or acceptance result where it suffices. If an unresolved knowledge question remains, identify how the inquiry could change its support. A justified ready protocol can examine a disputed claim. When design selection is open, RMP.2 receives the bounded question and its criticism requirement. A specific supply gap can also be the current result.

### RMP.1:5 - Archetypal Grounding

These constructed cases use stipulated facts to illustrate how the research boundary changes with the question. Empirical claims about a pump, stream, archive, instrument or authority require evidence from the corresponding case.

#### RMP.1:5.1 - Corporate Seal-Test Case

A reliability engineer is asked whether an accelerated seal test justifies changing the maintenance interval for Pump-P4. In this case, designated authorities hold responsibility for maintenance, safety and engineering qualification. The inquiry concerns what the test establishes.

First check the current engineering account. If it supplies the field failure mechanism, applicable acceleration relation, qualified test method and instrument, acceptance criteria and evidence-to-use rule, the test can give an ordinary qualification or validation result. Give that result to its engineering or assurance user. The maintenance authority decides on the interval. A laboratory setting or possible publication changes neither question.

Suppose instead that high temperature may change the dominant degradation mechanism and that installation damage and fluid exposure are serious field alternatives. If these premises and the remaining membership conditions hold, the ResearchQuestionBrief can take the following form.

| Position | Constructed result |
| --- | --- |
| receiver and use | Reliability council needs evidence about whether the accelerated-test result can bear on the current seal-life claim. The maintenance authority retains the interval decision. |
| intended episteme change | Retain, narrow, or reject the claim that degradation observed under the selected accelerated condition is evidentially relevant to Pump-P4 field failure within the named operating envelope. |
| bounded question | Within the named Pump-P4 material, fluid, pressure, and temperature envelope, does the selected acceleration condition preserve the field failure-mechanism relation well enough for its degradation evidence to bear on the current seal-life claim? |
| current frame and rivals | Current sources support the field claim only provisionally. Acceleration-induced mechanism change, installation damage, batch/material variation, and field fluid exposure remain serious alternatives. |
| membership account | The mechanism relation is unresolved for this use and the inquiry must examine how evidence bears on it. Specimens, conditions, measurements, deviations and limits can be traced and criticized. The intended result is a bounded claim about the mechanism and its evidence. |
| criticism demand | The evidence must be able to reveal a mechanism change caused by acceleration and distinguish it from the named field alternatives. A design choice, if needed, concerns how to do so. |
| constraints and returns | Use qualified engineering results for admissible indicators and specimen identity, and suitable evidence for instrument feasibility and calibration. Observe the safety and access conditions set by their authorities. Identify a missing result and its supplier if the design depends on it. |
| answer condition | Establish whether the selected acceleration condition preserves the mechanism relation needed for the bounded seal-life claim. Qualified evidence can support, narrow or reject that relation; identifying a still-missing decisive result leaves it unresolved. |
| work-stop and reopen conditions | Finish with the supported answer or return the unresolved relation and its decisive missing result. RMP.2 distinguishes a still-needed selection from a completed allocation with no new study. A newly available result or worthwhile obtainable comparison can reopen that choice. The maintenance authority retains the interval decision. |

Use the brief and frame in RMP.2 if a choice of design is still needed. If existing evidence establishes that the acceleration relation is invalid for the proposed use, give that finding and its scope. It can settle the question directly.

#### RMP.1:5.2 - Citizen Stream-Salinity Transfer

Residents observe an increase in urban-stream salinity. If the task is to report current state under established sampling, threshold and response rules, use or supply the monitoring result. Repeated sampling and a public dashboard can serve that ordinary task.

Suppose instead that sensor drift, road-salt transport, groundwater contribution, a changed outfall and seasonal hydrology remain plausible explanations for a particular reach and period. The community wants an explanation. The question can satisfy all four conditions if the research must examine those unsettled alternatives, its sources and measurements are inspectable, and the team can return a bounded finding with its limits. A justified existing protocol may supply some of the operations.

The brief identifies the reach and period, observations and contrasts, relevant sources and dates, rival explanations, required criticism, sampling and access conditions, useful stop and intended user. Qualified measurement, site access, privacy, safety and official response each need their own basis. Membership depends on the inquiry. If the sensor is invalid, identify which claim loses its support. A qualified alternative measurement may be enough. If measurement repair or ordinary monitoring is needed, use that route and preserve any other supported finding.

#### RMP.1:5.3 - Historical Source-Critical Contrast

An archive group asks whether a change in maintenance followed one directive or appeared earlier in workshop records. Rival chronologies, source provenance and silences can call for genuine inquiry. If the four conditions hold, its result is a bounded historical claim. One authenticated dated record may already answer a narrower date question directly. Apply the relevant access, conservation, rights and interpretation conditions.

#### RMP.1:5.4 - Retrieval-Sufficient Stop

A product team asks whether the current standard still permits configuration X. The applicable edition and clause, their local meaning, jurisdiction and effective dates answer the question. Give the answer and its source conditions in the current exchange. The card finishes at prompt 3.

Another team proposes the same configuration in a different jurisdiction. The retained edition, clause and jurisdiction identify where the earlier answer applies. Use a competent existing result for the new jurisdiction or state the remaining gap. If the empirical adequacy of the clause in a materially new setting becomes a question, qualify that question and its current frame separately.

#### RMP.1:5.5 - Recover an Answer from the Texts

A product team asks to research whether instruction M still permits configuration X on housing V2. It has a 2021 instruction, the 2025 revision and a 2025 correction notice. All are stipulated source texts for this constructed case.

Searching the old instruction for "permitted configurations" returns X for V1. The new contents instead use "installation combinations"; its table lists X with V2. The adjacent note limits that row to dry service. The correction notice changes a different combination. Reading the table and its note changes the answer from "only V1" to "the 2025 instruction includes X with V2 for dry service." The answer identifies the edition, table and note. No experiment is needed to establish what that instruction says.

The team clarifies that the intended service is wet. Retain the established answer for dry service. An applicable instruction or qualified engineering judgment could supply the wet-service answer. If the team asks whether the instruction’s claim holds in a materially new setting, qualify the empirical question under the four conditions before choosing a study.

#### RMP.1:5.6 - Compare the Answers that Existing Reports Can Supply

In the seal case from §5.1, a report supports a temperature-acceleration relation for a stated material in water. A later report concerns another fluid and a different dominant degradation mechanism. Both can inform the question. Comparing their conclusions requires keeping the material, fluid and mechanism in scope. Publication date or test duration alone cannot rank them.

Retain the supported water relation and the evidence of a different mechanism in the other fluid. The useful question becomes whether the proposed test preserves the field mechanism for this material and fluid. An applicable existing study may answer it. If a mechanism question remains, apply the membership test with the criticism it requires. Undertaking a new study needs a justified design decision.


#### RMP.1:5.7 - One Supplied Protocol, Two Different Epistemic Tasks

Consider a two-condition assay of polymer stiffness after dry or humid storage. The case supplies and justifies the materials, allocation, conditioning, instrument, sample rationale, analysis and interpretation for the uses described. Competence, access, protection and resources are available. The procedure stays the same as the question and intended contribution change.

**Replication of a disputed claim.** Existing evidence disagrees about whether humidity changes the stiffness of a particular material under stated conditions. A new independent sample could change the support for that claim. The justified protocol specifies the comparison, treatment of uncertainty and what counts as a compatible, discrepant or inconclusive result. The inquiry meets the four conditions through its open knowledge question, examination of a disputed relation, inspectable evidence and bounded result. Its brief gives the claim, current knowledge, criticism requirement, proposed new-data contribution and limits. Use the design already selected. RMP.6 can help decide whether to obtain the replication at its full cost. Membership alone leaves that choice open. An inconclusive result can leave the relation disputed, and a discrepancy reopens the interpretations that depend on it.

**Routine quality control.** A production laboratory uses the same assay under an accepted material specification and acceptance rule. The question is whether this lot passes. Obtaining a new value supplies an ordinary case verdict while the humidity–stiffness relation stays an accepted premise. The trace and certificate can support that quality-assurance result. Production retains the release decision. For an out-of-range result, use the qualified investigation or recovery procedure. Revisit the need for research if a distinct claim about the relation, measure or applicability becomes unsettled.

A trainee may also run the assay to learn the procedure. Personal unfamiliarity can identify a learning need while the scientific relation is already established. Identify which result the work must supply in each case and preserve evidence for that contribution.

#### RMP.1:5.8 - An observation before a research question

An archive team sees district totals of 40 in one year and 80 in another. The headings and instructions show that the earlier table counts operating machines and the later one counts permits issued. A permit may precede installation or remain unused. The figures establish two counts with different meanings. Whether operating machines doubled remains open.

Reading the construction of the counts gave the team the distinction it needed. It can return that corrected interpretation directly. To investigate change in the number of operating machines, compare evidence of actual operation in the two periods. To explain a discrepancy between operating counts and permits, also establish how the two series relate. Check what existing records establish. If operating records are inaccessible and the necessary fact remains unknown, preserve the documentary correction and state the historical limit. Apply the four research conditions if a further inquiry needs qualification.

### RMP.1:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| institutional-status bias | Academic employment, a grant, or a journal is treated as necessary or sufficient. | Apply the same four conditions to corporate, public, independent, academic, and citizen holders. |
| activity-label bias | Searching, testing, measuring, interviewing, coding, or publishing is classified by appearance. | Recover the intended episteme change, uncertainty, criticism, trace, and return. |
| novelty to the researcher | Personal unfamiliarity is taken as a new research question. | Establish what relevant sources already answer before judging novelty or the need for research. |
| favored-answer bias | The desired conclusion sets the question and source cut. | State materially different answers and the criticism that could defeat or narrow the favored claim. |
| protocol bias | A standard protocol is treated as proof of research or proof that the whole inquiry is routine. | Identify the question, qualified frame and intended knowledge contribution. Reuse justified design choices. For a completed inquiry, trace what was done to the criticism it could address. |
| uncertainty about operations | Missing time, access or execution detail is treated as an unresolved knowledge claim. | Identify the knowledge question if one exists. Otherwise give the operating constraint or seek the ordinary result needed for the task. |
| data-volume bias | More observations are assumed to create a better question. | Define the answer-changing contrast and useful stop before requesting more data. |
| publication bias | Publication in a recognized venue is treated as proof that work was research or the claim is true. | Examine the inquiry and the grounds for its conclusion. Use evidence of publication or recognition for those distinct claims. |
| openness absolutism | Unrestricted release is made a membership condition. | Require a criticism-ready trace and bounded communicability while preserving ethics, rights, confidentiality, safety, security, and community governance. |
| authority inferred from research | The provider of evidence is assumed to decide on maintenance, policy, release or a personal action. | Identify the intended use. Where a decision follows, establish who may make it or state what authority is missing. The researcher can also make the decision when the applicable mandate permits it. |
| AI/tool bias | Tool sophistication or fluent synthesis substitutes for source verification and criticism. | Identify the sources and transformations used, who performed or supplied each contribution and which claims the evidence supports. State the limits of the resulting account. |

### RMP.1:7 - Conformance Checklist

Apply the questions relevant to the branch taken. Use the membership and knowledge-change questions for a ResearchQuestionBrief. A source answer, ordinary professional result or research-boundary hold has its own completion conditions.

- [ ] **RMP1-01:** The question, intended use and available material have been examined before any decision to start a new study.
- [ ] **RMP1-02:** The intended user and bounded use are clear. For a later decision or permission that matters, the account identifies the authority established or the specific gap.
- [ ] **RMP1-03:** The current frame is question-relative and records exact supplied results, source snapshot, omissions, and currentness limits.
- [ ] **RMP1-04:** Serious rivals or lineage are present when they can change the question; a source count is not used as coverage.
- [ ] **RMP1-05:** A sufficient source answer completes this use and the card. It includes the sources and limits the user needs.
- [ ] **RMP1-06:** The intended episteme change is exact enough to be retained, narrowed, rejected, qualified, or added.
- [ ] **RMP1-07:** The bounded question names the phenomenon, unit, case, population or corpus, relevant relation or contrast, constraints, and useful answer.
- [ ] **RMP1-08:** The unresolved question has been established against the relevant knowledge and intended use.
- [ ] **RMP1-09:** The inquiry as a whole has a non-routine knowledge task under genuine uncertainty. It can reuse a justified design. Uncertainty about an ordinary case value requires different grounds for research membership.
- [ ] **RMP1-10:** The intended trace can expose sources, premises, performed moves, evidence, deviations, limits, and stops to criticism.
- [ ] **RMP1-11:** The intended result includes a bounded knowledge contribution that a suitable critic can examine.
- [ ] **RMP1-12:** All four membership conditions pass independently before a ResearchQuestionBrief is returned.
- [ ] **RMP1-13:** The nearest plausible non-member is named and its difference is stated.
- [ ] **RMP1-14:** For an ordinary professional use, the relevant result is supplied or the work and required contribution are identified. State what would reopen the research question when that matters.
- [ ] **RMP1-15:** A missing or stale source or result is a hold when it blocks an answer still needed in the current branch. Identify the blocked question, the source or supplier if known, and what would permit reconsideration.
- [ ] **RMP1-16:** The source answer, comparison or named remaining gap follows from the question and available texts through §4.3. An identified search, interpretation or applicability failure has been addressed or retained as a limit.
- [ ] **RMP1-17:** FPF contributions keep their source meanings and conditions. A best-known current comparison meets F.1:4.2.1 and E.8:11. Use the narrower criteria appropriate to an ordinary source question.
- [ ] **RMP1-18:** The criticism demand names an error or rival to expose without selecting a design family.
- [ ] **RMP1-19:** The brief distinguishes evidence for an adequate answer from a reason to finish with refusal or uncertainty. It states any unmet condition and what would reopen the inquiry.
- [ ] **RMP1-20:** Use qualified field evidence for phenomena and instruments. Observe applicable safety, ethics, rights, access, assurance and decision authority.
- [ ] **RMP1-21:** For an open design choice, RMP.2 receives a compatible brief and frame. An existing design or later input can be reused at its supported scope. A brief alone establishes neither performed work nor its authorization.
- [ ] **RMP1-22:** Determine membership from the inquiry and its intended contribution. Apply the competence, access, rights and safety conditions of the actual setting.

### RMP.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| “Everything uncertain is research” | An operational uncertainty may concern only an ordinary case value. | Identify the knowledge claim that remains open, or give the operational finding or constraint. |
| “Research happens only in research institutions” | The same institution can conduct routine work and research. Community practitioners can also conduct research. | Apply the four conditions to the actual inquiry. |
| “A literature search is the study” | Retrieval may already answer the question, or it may be only one supplied input. | Return the exact source result or form a separate criticism-bearing question. |
| “Choose the method, then write the question” | A favored apparatus or design can manufacture its own problem. | Qualify the frame, episteme change, and criticism demand before RMP.2. |
| “Run the standard test to be safe” | Familiarity does not establish what the result would contribute to knowledge. | Use the existing test for routine qualification when it fits. To use it in research, establish the unresolved knowledge task and the other membership conditions for the whole inquiry. |
| “Systematic means a checklist exists” | Administrative regularity can leave the question-to-evidence relation unknown. | Preserve the premises, actions, evidence, deviations, limits and stops needed to assess the claim. |
| “No source result, so explore freely” | A missing source can prevent a particular answer or membership judgment. | Identify the specific source, date or comparison needed and what remains answerable. If the distinction still needs development, §4.0 gives a bounded way to explore the available material. |
| “One scientific method fits every question” | Historical, qualitative, observational, computational, experimental and synthesis questions can expose different errors. | State what criticism the answer must withstand. Use RMP.2 if the design still has to be selected. |
| “The research result decides the action” | Evidence about a subject does not allocate decision authority. | Give the supported knowledge contribution to its user. For a decision, apply the values, conditions and authority governing it. |
| “Not research” | The label leaves the useful work or available answer unspecified. | Give the relevant ordinary result, or identify the question, material and contribution needed. State what could reopen research membership when that is relevant. |
| “Apply Frascati as a legal or prestige gate” | Its R&D-statistics purpose and sector rules do not define all holder-neutral research practice. | Use the five criteria as explicitly adapted assurance questions with stated limits. |

### RMP.1:9 - Consequences

The user may receive a question ready for design selection, an adequate existing answer or a reason to stop. Routine engineering, monitoring, assurance, audit and evaluation can proceed on their own criteria and authority. The same research conditions apply to an independent practitioner, a citizen group or an institution.

Source qualification takes work. If an answer still needed depends on unavailable sources, rival accounts, measurements, domain criteria, access or permission, identify that particular hold. A task described as research may instead have an ordinary professional answer.

For an open RMP.2 choice, supply the criticism the design must address. Use a separately justified design if it is already adequate. Return the evidence for its intended use. Authority for a later decision, if any, remains with its holder.

### RMP.1:10 - Rationale

The four conditions distinguish the task of inquiry from its visible activities. Relevant sources establish what remains unknown for this use. The whole inquiry must construct or criticize knowledge under uncertainty. A fully supplied procedure can serve that task or an ordinary case under an accepted rule. Traceable evidence allows a critic to narrow or defeat a claim. A bounded, communicable finding can contribute to knowledge alongside any immediate use or later recognition.

A qualified source answer may resolve the request completely. A result from an adjacent practice, such as monitoring or qualification, remains useful in that practice. If it exposes a new question about mechanism, validity, transfer, measurement or evidence, revisit the affected research question.

Starting with the intended use helps establish relevance. Keeping the evidence open to a result the sponsor would dislike protects the inquiry. Defining the necessary criticism before choosing a design keeps a favored apparatus or method hierarchy from deciding the question in advance.

### RMP.1:11 - SoTA-Echoing

How can a practitioner recognize a research question that admits consequential criticism while preserving ordinary professional uses of the same techniques?

The OECD’s [Frascati Manual 2015](https://doi.org/10.1787/9789264239012-en), chapter 2, offers a cross-sector comparator for research and development statistics. RMP.1 adapts novelty and creativity to the unresolved knowledge and epistemic task of the whole inquiry. Section 4.6 describes its use of the other criteria. Frascati §2.16 recognizes the potential knowledge contribution of reproduction and discrepancies. To determine what a repeated procedure contributes here, examine its question and evidence.

The National Academies’ [replicability account](https://www.nationalacademies.org/read/25303/chapter/8) explains how a justified design and new data can change support for a claim. In §5.7 the replication can therefore earn research membership without a newly invented procedure. The same systematic measurement can give an ordinary quality-control verdict. RMP.1 distinguishes the cases through the whole inquiry’s knowledge task, qualified question, trace and bounded contribution. These four conditions combine and adapt the sources for the practitioner’s question.

UNESCO’s [Recommendation on Open Science](https://www.unesco.org/en/legal-affairs/recommendation-open-science) recognizes contributions by citizens and communities outside a particular research institution. This supports judging membership independently of affiliation. Ethics, safety, rights, confidentiality, security, access and community authority continue to govern conduct and disclosure.

An institutional or activity-based classification can help with staffing, funding or administration. Employer, venue and use of a laboratory can identify candidate work. They cannot distinguish routine testing from an investigation of a disputed mechanism. For that distinction examine the question, the task of the whole inquiry, the trace and the intended knowledge contribution.

Use field evidence for the truth of a claim, competent sources for its instruments and the governing authority for permission. Reconsider the affected membership criterion when a stronger cross-sector source changes it, evidence shows it misclassifies a design family or group, or a source rule changes what can be established about the relevant knowledge. Revisit prior uses that relied on the changed grounds.

### RMP.1:12 - Relations

- **`F.1` — Find and Select Sources for a Current Question.** Use it to find material a reader can inspect and identify limits on search or access. Its source-selection branch can supply a question-relative `SourceCutNote`.
- **`F.0.1` — Source-Local Meaning Recovery.** Use it to establish what a consequential expression means in its source.
- **`A.10` — Evidence Graph Referring.** Trace the evidence and provenance of the particular claim and state the limits on its use. Truth, assurance, permission and actual work need grounds appropriate to those claims.
- **`F.0.2` and `G.2`.** Use F.0.2 for conceptual synthesis in framework authoring and G.2 for a broader refreshable SoTA collection. Section 4.3 gives the ordinary source-answer route.
- **`E.8:11`.** Use its SoTA comparisons in §4.3.2 for a claim about the best-known current answer. Report what the comparison establishes about the answer, applicability, research question or stopping condition.
- **Core Method development and A.3.1.MI.** Use Core for Method identity, repertoire, requirements, qualification, trial, fit, worth, variants and provenance. A.3.1.MI addresses introduction and revision. RMP.1 addresses what makes this particular inquiry research and what knowledge question remains.
- **`RMP.6` — Choose the Credibility Test That Bears on the Research Claim, or Answer without New Testing.** With a bounded claim, basis and threat, consider a suitable examination, including replication with new data under a supplied design. The value of obtaining a test and a finding without another test depend on the threat and the attainable contribution.
- **`RMP.2` — Choose a Criticism-Bearing Research Design or Stop.** Use a compatible ResearchQuestionBrief and qualified current frame when the choice of design remains open.
- **Domain and institutional practices.** Engineering, Operations, assurance, audit and evaluation supply qualified results. For instruments, safety, ethics, rights, access, governance and subsequent decisions, use the evidence and authority applicable to each.
- **OECD Frascati Manual 2015.** Section 4.6 adapts its five criteria from research and development statistics to the inquiry examined here.
- **UNESCO Recommendation on Open Science.** It supports citizen and community participation under the applicable rights and legitimate restrictions.

### RMP.1:End


## RMP.2 — Choose a Criticism-Bearing Research Design or Stop

> **Type:** Research Method Practice practitioner method pattern
> **Status:** Stable


### RMP.2:0 - Use This When

Use this method when the research question, current evidence and answer conditions are sufficiently clear to ask whether further inquiry is worthwhile. First check whether the evidence already answers the question. If it does not, determine whether the current allocation already justifies undertaking no new study. When a selection remains open, use a suitable existing strategy or develop one through §4.4. Identify what evidence could distinguish the competing claims, recover an operation that could obtain it and follow its use on available material. Compare the actual options for their fit to the question, the error each can expose, their limitations and the full effort of obtaining an answer.

Return one **ResearchDesignDisposition** for the question about research effort now at issue. Use `EvidenceSufficientStop` when current evidence answers the qualified question. Use `ResearchDesignDecision` when a justified feasible strategy has been selected. Remaining `PostSelectionNeed` items must preserve the selection throughout their jointly admissible ranges. Use `ResearchDesignHold` when a specific missing result prevents a selection that is still needed. Use `QualifiedNoNewStudy` when the current allocation calls for no new study although the answer remains limited. For a selected design, check the construct, evidence, measurement, access, protections, permissions and resources on which its criticism and feasibility depend.

The result tells a researcher or commissioner what the current evidence supports and whether a particular study is worth pursuing. A selected design describes the proposed strategy. Its protocol, permission to proceed, actual work and findings have their own grounds.

If the research question or its current basis is unclear, use RMP.1 to qualify it. Use the appropriate professional method for operational definitions, study execution, analysis or development of a reusable Method. Obtain a required ethics, safety or access decision from its holder when the work depends on it, using an existing valid permission where applicable. The researcher may hold another role under its own mandate.

#### RMP.2:0.1 - Working Terms

| Name in this pattern | What it denotes |
| --- | --- |
| research design | A justified way to answer a qualified question. It relates the relevant cases, material or sources to observations, intended analysis, a challenge that could defeat or narrow the claim, significant threats and a useful stopping condition. |
| design family | A broad kind of relation between a question, its evidence, a comparison and a challenge to the inference. Options include intervention or assignment, field observation, situated interpretation, historical source criticism, computational modeling and corpus synthesis. A design may combine contributions from several families. |
| criticism logic | Which material error, rival explanation, source failure, dependence, bias or unjustified transfer the design could expose, how it could expose it and what result would defeat or narrow the claim. |
| serious design-or-stop option | A real way to stop or a feasible or conditionally feasible strategy for the same research question. It differs from the other options in what evidence could decide, what error could be exposed, what risk or cost would be incurred or what would prevent use. |
| EvidenceSufficientStop | Current evidence meets the answer condition for the intended use. Return the answer and the limitations that matter to reliance on it. |
| ResearchDesignDecision | A worthwhile feasible strategy has been selected, with an explanation of its distinguishing evidence, relevant alternatives including no new study, threats, required inputs, refusal conditions and useful stopping point. |
| PostSelectionNeed | An input still needed to instantiate, record, schedule or support the selected design. Every admissible value, including admissible combinations with other unresolved inputs, preserves its family, core contrast, criticism, feasibility and refusal conditions. The set can be empty. |
| ResearchDesignHold | A particular selection is still needed, but an unresolved result could change the approach, core comparison, admissible evidence, criticism, feasibility or reason for refusal. The hold identifies the result. Commissioning work to obtain it is a separate decision. |
| QualifiedNoNewStudy | No new study is selected for the current allocation. Return the bounded answer or still-open claim and the reason the attainable study does not justify its burden. A material uncertainty may remain a limitation or a condition for reconsidering the choice. |
| selection-changing uncertainty | A still-open fact or requirement whose plausible values support different strategies, ways of challenging the claim, stopping conditions or refusals. |
| expected information gain | What an option is expected to clarify or distinguish about the live question. Compare that contribution with the effort, risk and limits of obtaining the evidence. Use a numerical estimate when its assumptions are supportable. |

Recognize a design question when a qualified inquiry still has an open choice about further evidence. To justify a design, show how its evidence would address the same question, how it could reveal error and why the needed conditions can be met. Separately state what the current evidence already establishes and which research effort, if any, has been selected.

### RMP.2:1 - Problem Frame

Research questions do not determine one universal design. The same practical use can be served by a controlled comparison, a field observation, a qualitative account of situated mechanism, historical source criticism, a computational challenge, a synthesis of an existing corpus, a mixed composition, or no new study at all. Each exposes different errors and requires different observations, sources, access, and domain judgements.

A fact about the subject or available work may change the design. If acceleration changes the failure mechanism, evidence from an accelerated seal test may no longer support the field claim. An invalid salinity sensor or inaccessible site can eliminate a field comparison. Uncertain archival provenance can prevent a historical source from discriminating two chronologies. Settle such conditions when selection depends on them or identify the resulting limit.

Other details can remain open after selection. A particular filename, serialization or schedule within an established window may make no difference to the evidence, criticism or feasibility. Check the remaining values together before treating them as implementation details.

### RMP.2:2 - Problem

A familiar method can be chosen before anyone has identified the error the question requires the study to expose. Randomization, interviews, simulation or synthesis may each provide a suitable operation. A detailed implementation can still fail if the observations offer no relevant way to distinguish the rival accounts, including differences in their likelihood under the stated assumptions.

A design can fail when the construct has no suitable observable, the source cannot support the claim, the instrument lacks discrimination, safe access is unavailable or the required permission is missing. Identify such dependencies before committing effort to a protocol. They can change the strategy or make no new study the appropriate allocation.

An unresolved detail that cannot change the choice can wait. Assigning a record locator or a time inside a qualified window may be such a detail. Show why the admissible alternatives preserve the design and when a change would reopen it.

### RMP.2:3 - Forces

- Check whether the existing evidence answers the question. Residual uncertainty can be compatible with the answer condition.
- Compare the error each design can expose. A single numerical score can conceal important differences in what the evidence would establish.
- Compare real alternatives. If a single design is feasible, assess its contribution against the option of no new study.
- Domain knowledge, measurement, access and permissions can determine which design is possible. Use their proper grounds, whether they are already available or supplied by someone else.
- A design can guide later work once its consequential assumptions have been resolved or bounded.
- A detail can wait only if its admissible values preserve the selection.
- Weigh the information the work might supply against its whole burden. Some questions support a quantitative estimate and others a qualitative judgement.
- In a mixed design, explain how the different evidence will be brought to bear on the question and what disagreement would mean.
- If a reporting rule applies or supplies information the task needs, use it for that purpose. Justify a design by the relation between its evidence and the research question.
- Identify the intended use. If a later decision is required, establish its authority separately.

### RMP.2:4 - Solution

Keep the qualified question in view and test the current evidence against its answer condition. If the question remains open, determine what an obtainable study could distinguish and weigh that contribution against its full burden. Return the applicable result: sufficient existing evidence, a selected strategy, a particular choice held for a consequential input, or a completed allocation choosing no new study.

#### RMP.2:4.1 - Admit the Design Question

1. **Recover the question and its current basis.** Identify who needs the answer, what knowledge it should change, which rivals matter, what evidence could challenge the claim and what constraints apply. Distinguish the evidence required for an answer from conditions for ending work with uncertainty. A compatible supplied brief and current account allow direct entry.
2. **Check that the question still holds.** A material change to the use, question, evidence, rival accounts or useful stopping point may require a revised brief. Use RMP.1 for the missing qualification. If the revised question and its grounds are already available, use them directly.
3. **Establish the inputs and permissions this strategy needs.** Identify who can substantiate a domain or measurement claim, who can supply materials or resources and who holds any required ethics, safety, access or other permission. Use applicable evidence and permissions already established. If a receiving action requires a separate decision, state the authority or the specific gap.
4. **Define the present choice.** State what evidence strategy and challenge are at issue, which details may be chosen later and what result would justify stopping, refusing or reconsidering.

#### RMP.2:4.2 - Test the Evidence-Sufficient Stop

Compare qualified current evidence with what the ResearchQuestionBrief requires for an answer. Distinguish that requirement from a condition for ending work with an unresolved claim or a refusal.

- Does it answer the bounded question for the named receiver and use?
- Does the evidence cover the phenomenon, comparison, cases, population or corpus and time period to which the answer will apply?
- Does the evidence distinguish the principal live rival or address the relevant threat to validity?
- Are its source, evidence-use, provenance, uncertainty, and currentness limits compatible with the reliance proposed?

If the evidence meets the answer condition, return the answer with the source, scope and limitations its use requires. This is `EvidenceSufficientStop`. The answer may complete the assignment. Preserve any uncertainty that could change reliance on it.

If the evidence is insufficient, ask what an obtainable study could establish and whether its value warrants the full burden. Include preparation, access, measurement, execution, interpretation, work by participants, delay, displaced activity and joint resource limits where they apply. A contribution to knowledge or later inquiry can justify a study.

If the available facts justify choosing no new study for this allocation, return `QualifiedNoNewStudy` under §4.7 with the bounded answer or unresolved claim. Otherwise examine the inputs and options that could change the remaining selection. Budget, priority, availability and burden affect the allocation. Judge the adequacy of the evidence against the question.

#### RMP.2:4.3 - Expose Selection-Changing Inputs

While a choice remains open, identify the facts, requirements and permissions that can change the design, its criticism or its feasibility.

| Input | What could affect selection? | Typical source or responsible party |
| --- | --- | --- |
| construct or mechanism relation | Would a different relation between construct and observation change what needs to be measured, manipulated, compared or modeled? | Domain studies or a qualified domain investigator. |
| observation or source admissibility | Can the available observation or source support the claim, and under what interpretation or rights of use? | Observational specialist, archive, data steward or relevant rights holder. |
| instrument or measurement feasibility | Could sensitivity, specificity, calibration, disturbance, resolution or construct validity eliminate a required distinction? | A relevant instrument or laboratory result, or a qualified measurement specialist where needed. |
| case, population, material, corpus, or site access | Could access or sampling conditions make the selected contrast impossible or materially different? | Site, archive, data, participant, asset, or access owner |
| ethics, safety, rights, confidentiality, or community authority | Could a legitimate restriction prohibit the strategy or require a different evidence relation? | Applicable ethics, safety, rights, privacy, security, or community authority |
| intervention, exposure or comparison control | Can the relevant difference be produced or observed and attributed under the proposed conditions? | Domain or operational specialist, provider or applicable authority. |
| resource and provider feasibility | Could capacity, timing, specialist support, compute, laboratory, or field availability eliminate the family or core criticism? | Resource, provider, laboratory, platform, or programme owner |
| intended use and permission to use the result | Can the proposed recipient use the result for this purpose, or would that use require a different claim, different evidence or permission? | Recipient or relevant decision or assurance authority, where one is required. |

For an unresolved input that could affect selection, compare plausible values and their consequences. If the values support different families, core comparisons, criticism, feasibility or stopping conditions and this selection is still needed, return a hold. A remaining detail may qualify as a PostSelectionNeed if the admissible values jointly preserve the selection. Where no new study has been chosen on adequate allocation grounds, report the unknown as a limit or a reason to reconsider. Naming a dependency leaves any acquisition decision with its holder.


**Check the inputs together.** Examine combinations of the remaining values that are compatible with the evidence and constraints. Where a dependence among values is unknown, state how the outer bounds limit the feasibility claim. A set of PostSelectionNeed items is justified if every jointly admissible combination preserves the family, core contrast, criticism, feasibility and refusal conditions. Checking each value while fixing the others favourably can miss a joint failure.

Suppose two required tasks draw on the same ten investigator-days and their efforts cannot overlap. Each requires four to six days, and the supplied relations admit the pair six and six. Six plus four and four plus six fit. Six plus six requires twelve days. The whole strategy is therefore not assured feasible across the admitted demands. If the choice is still needed, return ResearchDesignHold with the two demands, their source, the combinations that fit or exceed the limit and the information that could settle selection. If an earlier part is already complete and its result is usable, count only the work still needed.

#### RMP.2:4.4 - Compose Serious Design-or-Stop Options


Use a supplied strategy directly when it fits the question, evidence, criticism and obtaining conditions. A justified replication can already have specified procedures. When the required evidence relation is missing, use C.39 to develop the operation for this question.

1. **Work backward from a useful answer.** Identify observations, relations among sources or interpretations that could support, narrow or defeat the claim. For each live account, ask what it permits or makes difficult to explain under the same conditions. An outcome can favor one account even when all permit it. Compare its likelihood under the accounts if suitable models are available. If they make the same predictions for the evidence being compared, that evidence cannot discriminate them. A dated record may distinguish two chronologies. A contrary case may challenge a situated interpretation.
2. **Find an operation that could obtain the distinction.** Use an adequate professional method, worked study, demonstration or source. Identify its inputs, what the investigator does, what it returns and why that result bears on the question. Carry its applicable conditions into the proposed use. A controlled comparison needs a defensible assignment and basis for comparability. A source comparison needs identifiable, admissible records. The families in §4.5 can help locate operations.
3. **Connect the material to the operation.** Identify the records, cases or specimens that could supply its inputs and how its output would bear on this question. Derive any needed comparison, transformation or combination from the domain premises. A lab that distinguishes mechanism signatures still needs comparable material and conditions to compare accelerated with field degradation. Identify what is already qualified, what the researcher has constructed and what remains assumed.
4. **Follow the proposed relation on concrete material.** A suitable record, specimen account or earlier analysis may show what enters, what the operation returns and how it would affect the claim. Try a small application if its contribution justifies the work and the needed authority is in place. Examine a consequential rival, such as two mechanisms that produce the same observation or two archival records that concern different events. Use the inspection to assess the proposed strategy. Evidence that the proposed study took place is a separate matter.
5. **Repair a failed connection if worthwhile.** Look for a more discriminating observation, a different comparison or another operation supported by the professional sources and domain premises. An analysis can recover an omitted distinction only with further observations or a justified relation that identifies it. If that relation remains unknown and selection depends on it, use §4.3 to state the gap and its consequences. If a narrower question would be useful, qualify that question explicitly through RMP.1 as needed. Section 4.7 also permits a bounded no-new-study result.

Explain how the material and operation would expose the relevant error, including any premise whose failure would defeat the comparison. One adequately developed strategy can suffice. Develop another when it could change the choice. Use available professional results directly where they fit. RMP.3 specifies the consequential operations of a selected strategy when that work is required.

For the same brief, compare strategies that differ in what the evidence could establish, their feasibility or cost. Include a current routine where it is a serious option and weigh further research against no new study when that choice is open. If an established source or constraint rules out a proposal, state that reason.

If a single research strategy remains, assess whether it can expose the relevant error, is feasible and contributes enough to justify the full burden compared with no new study. Consider another strategy when it offers a consequential difference in evidence, cost or constraints.

For each serious option, explain the following features as far as the choice requires. Use the brief and reliable inputs already available. A description is complete for this purpose when it shows how the evidence could answer or challenge the claim.

1. what could become known and when the result would be sufficient for its use,
2. which cases, units, materials, population or corpus the proposed comparison requires and which observations, sources or interventions would distinguish the claims,
3. the principal error or rival the inquiry could expose and what would defeat or narrow the claim,
4. which threats to validity it addresses, introduces or leaves unresolved,
5. what evidence, expertise, access, protections, rights, permissions, supplies or resources it requires and which are available, assumed or missing,
6. what useful information it could add and under which conditions it would add none,
7. the burden, timing, risk, reversibility and conditions for stopping or refusing, and
8. what would still have to be specified or recorded if the design were selected.

Differences in software, sample size, interview format or reporting can matter when they change the evidence, threats, cost or feasibility. Two descriptions with the same evidential and practical consequences can be treated as one strategy.

#### RMP.2:4.5 - Preserve Design-Family Differences

| Design family | How evidence bears on the question | Possible errors or rival explanations | Conditions that can affect selection |
| --- | --- | --- | --- |
| experimental — intervention or assignment | Deliberately vary or assign an intervention/exposure or comparison condition and estimate a bounded difference or relation. | Rival causes, allocation, baseline imbalance, measurement error, model dependence, missingness, intervention fidelity, and applicability. | Manipulability, admissible comparison, mechanism relation, instrument validity, safety, authority, sample/case feasibility, and effect/uncertainty use. |
| field or observational | Compare observed exposures, states, changes or contexts when the investigator did not assign the observed conditions. | Confounding, selection, measurement error, context and seasonal effects, missing observations, reverse causation and unsupported transfer. | Access to sites or usable records, valid measures, temporal and spatial coverage, available comparisons and the domain limits on causal inference. |
| qualitative or reflexive | Develop a situated account of meaning, experience, practice, process or mechanism from participants, records, interactions or cases. | Researcher position, rival interpretations, disconfirming cases, relevance of sampling, context, participant voice and unsupported transfer. | Appropriate participation or access to records, ethical use, a suitable account of the phenomenon, interpretive competence, and protection against harm or disclosure. |
| historical or source-critical | Use surviving records produced for particular purposes to investigate an occurrence, interpretation, change or lineage. | Provenance, chronology, source purpose, selective survival and silence, competing interpretations, anachronism and limited corroboration. | Access, rights, authenticity, date, archive coverage, the relation between record and claim and any missing evidence that could distinguish accounts. |
| computational/model | Challenge a mathematical, algorithmic, simulation, or code-mediated claim through derivation, implementation, calibration, sensitivity, reproduction, validation, or intended-use comparison. | Code/data/environment dependence, implementation defects, parameter and structural sensitivity, calibration, validation, identifiability, and intended-use fit. | Model-to-phenomenon relation, data and code access, environment identity, validation target, compute feasibility, and domain acceptance criteria. |
| synthesis | Use a defined body of evidence to answer a corpus question through eligibility, search, appraisal and suitable integration. | Eligibility bias, search omissions, dependence among sources, heterogeneity, incompatible measures or meanings, appraisal limits and selective publication or reporting. | A clear corpus question, traceable sources, eligibility and appraisal criteria, compatible results for any proposed pooling, access and currency. |
| mixed | Connect two or more component designs whose different evidence addresses the question. | Each component’s threats and any unsupported inference in combining the results, including disagreement, non-comparability or one component dominating the conclusion. | A reason for each contribution, feasibility of the components together, a justified relation among their results and a way to interpret disagreement or partial failure. |

These families illustrate different ways evidence can bear on a question. They can overlap and be combined. An observational study may estimate an effect under stated assumptions. An intervention study may examine situated experience. Enter with the available claim, corpus, model, field anomaly or proposed intervention. Stop or revise the strategy when the current evidence or a changed premise warrants it.

#### RMP.2:4.6 - Compare the designs and the option of no new study

Use the applicable questions below to compare real options on the same brief. State consequential differences and keep protected requirements in force. A short explanation may be sufficient.

| Comparison position | Required content |
| --- | --- |
| question and use | Which part of the brief could this option answer, for whom and under what conditions would the inquiry end? |
| evidence | Which material, observations, intervention or exposure, sources and comparisons would the investigator use, and what would be inferred from them? |
| criticism | Which error or rival could it expose? What result would narrow or defeat the claim, and what material threats would remain? |
| validity and transfer | Internal, measurement, source, construct, interpretive, contextual, external, or intended-use limits that matter to this claim. |
| inputs and permissions | What domain or measurement evidence, sources, access, protections, rights, capacity or supplier work does the strategy need? Which are established, assumed or missing? |
| expected information gain | What live question could the evidence resolve or distinguish? Under which conditions would the added work supply no useful information? |
| burden and refusal | What work, materials, time and capacity would be needed to obtain and interpret the evidence? What risk, irreversibility, delay, displacement or joint limit would matter? Under what conditions should the work stop or be refused? |
| continuation | What would need later specification or recording? What would close the inquiry or justify reopening selection? |

If a bounded decision rule combines several measures, establish their meanings and the rule’s scope. Keep protected constraints, materially different losses and consequential unknowns visible. A single feasible option must still justify its burden against no new study where that allocation remains open.

#### RMP.2:4.7 - Return Exactly One ResearchDesignDisposition

**Branch A — `EvidenceSufficientStop`.** Use this result when qualified current evidence meets the answer condition. Give the answer, the evidence and the limitations that matter to this use. If another party will act on it, identify any uncertainty or reason that could change their reliance. The answer completes this branch.

**Branch B — `ResearchDesignDecision` plus `PostSelectionNeed`.** Select a feasible research strategy when its evidence could expose the relevant error and its expected contribution justifies the full burden. Compare actual alternative strategies and the option of no new study. Identify the selected strategy, its core contrast, justification, threats, required inputs, resources, refusal conditions, useful stop and any later needs. Explain why a considered alternative was set aside. Apply the [joint-input test in RMP.2:4.3](#rmp243---expose-selection-changing-inputs) to all remaining inputs. For each PostSelectionNeed, show the following.

1. the value still needed and who can provide or establish it,
2. the admissible range or alternatives already constrained by supplied results;
3. why all admissible values, together with the other needs, preserve the selection, its criticism and feasibility, and
4. the action if the value arrives outside that range.

Write an empty set as `PostSelectionNeed: none`. If a plausible value or joint combination could change the family, core contrast, criticism, feasibility or refusal and the choice is still needed, use Branch C. Use Branch D when the available facts justify choosing no new study for the present allocation.

**Branch C — `ResearchDesignHold`.** Use a hold when a particular choice is still needed and a missing result prevents it. Identify the question, the affected strategies, plausible results with different consequences, what work cannot start on the present basis and what would reopen selection. Name a qualified source or holder for the missing result where known, or state the gap. The hold can complete the question about what prevents selection. Deciding to obtain the input requires its own justification, feasibility and any applicable permission.

**Branch D — `QualifiedNoNewStudy`.** Use this when no new study is selected for the present allocation and the evidence still falls short of the answer condition. Return the strongest bounded answer or name the unresolved claim. Explain why the obtainable study does not justify its burden or why the discriminating evidence is unavailable. Preserve material limits and any condition that could reopen the choice. This allocation leaves the evidential and permission requirements for a stronger use in force.

Use one branch for the present choice. The result may be part of the existing explanation. Reconsider the choice when new evidence or a changed use affects it. RMP.3 requires a selected design from Branch B or a compatible design already supplied. A sufficient answer, a hold and a no-study allocation can each conclude their own work.

#### RMP.2:4.8 - What Changes in Practice

A researcher can develop the comparison a question requires, expose a failure on available material and repair the relation or identify the gap. The resulting account shows what a strategy could establish and whether that gain warrants the work. The present task can finish with adequate existing evidence, a justified design, a specific hold or a bounded no-new-study decision.

### RMP.2:5 - Archetypal Grounding

The following examples stipulate the records, access, professional results and other conditions to show how the four dispositions differ.

#### RMP.2:5.1 - Accelerated Seal-Test: Different Supplied Values

The supplied ResearchQuestionBrief asks whether high temperature accelerates the same failure mechanism as the field conditions, so that accelerated degradation can inform the Pump-P4 seal-life claim. Choosing a maintenance interval is a separate operational decision.

##### RMP.2:5.1.1 - Derive and repair the mechanism comparison

**Start with the question and the domain evidence.** The higher temperature might accelerate the field mechanism or introduce a different dominant mechanism. Engineering supplies the material and operating envelope, the relevance of both accounts and the limits of a field-representative condition. In the laboratory method, a qualified practitioner prepares an identified specimen, observes its surface and chemistry and interprets the joint signature using mechanism references valid for the material and damage range. These results and the available laboratory competence and equipment are inputs to the research comparison.

**Examine the familiar operation.** A routine test returns an overall wear index. Suppose the proposed strategy compares that index under accelerated and field-representative conditions and takes matching values as evidence of the same mechanism. Examine the two reference records below.

| Supplied reference | Independently established mechanism | Overall wear index | Qualified surface/chemical signature |
| --- | --- | --- | --- |
| Reference A, within the named material and damage range | The field mechanism | 6 | A |
| Reference B, within the same qualified range | The rival heat-induced mechanism | 6 | B |

Both constructed references have wear index 6, although their mechanisms differ. Greater precision in that index alone would still permit both explanations of a matching value. The number may answer a wear question. It fails here as a discriminator of mechanism.

**Construct a comparison that can distinguish the mechanisms.** Within the supplied material and damage range, the laboratory operation can return a mechanism-sensitive signature. Compare the signatures in accelerated and field-representative conditions. Use comparable specimens, preserve batch identity and assign conditions so that batch differences can be distinguished from temperature effects. Compare at appropriate damage levels, since equal elapsed times can correspond to different degradation. Once the strategy is justified, RMP.3 can specify the allocation, observation schedule and handling procedures.

The proposed strategy obtains mechanism-sensitive observations under both conditions, preserves material and damage comparability and interprets the signatures against the qualified references. A discrepancy can challenge preservation within the stated envelope. Agreement can support the claim to the extent allowed by sensitivity, sampling and interpretation. A different field condition or a maintenance interval requires its own grounds.

**Test the proposed inference against the references.** A and B are distinguishable on the failure-analysis records despite their equal wear index. Their identities and qualified conditions allow their use as mechanism references. In the proposed study, a qualified rival signature would challenge preservation, a compatible signature could support it within the stated limits, and inadequate discrimination would leave the mechanism unresolved. Use the professional method’s relevant classification and uncertainty criteria when deciding whether the strategy is justified.

Check the material identity and qualified damage range of a proposed reference. A signature label on an unidentified specimen may leave the interpretation open. If the instrument cannot distinguish A from B under the study conditions, use an adequate alternative or field comparison when one is available and worthwhile. Otherwise state the missing measurement and how it affects the choice, or conclude that no new study is justified for the present allocation. The wear index still has its original limitation.

**Assess the proposed study.** Suppose matched specimens and a justified assignment are available. The laboratory supplies the signature relation, uncertainty criterion and qualified measurement range. Access, protections, qualified personnel and resources cover preparation, measurement and interpretation. The attainable mechanism answer warrants that burden. The available field records do not connect material to exposure as required. The available model admits both mechanisms and cannot independently distinguish them here. These facts favor the experimental comparison for this case. Its results remain to be observed.

The scenarios below vary the supplied facts for the same question. A suitable prior result can answer it directly. A missing discriminator can hold a choice that is still needed. If the comparison cannot be obtained at a justifiable cost, the present allocation may end without a new study and with the mechanism question open.

##### RMP.2:5.1.2 - Select the disposition under the supplied facts

Compare the following relations when their supplied conditions make them serious:

| Option | Evidence and criticism relation | Principal loss or dependency |
| --- | --- | --- |
| stop on current evidence | Use a result that already answers whether acceleration preserves the relevant mechanism within the specified conditions. | The conclusion is limited to that use. A stronger life or maintenance claim needs suitable further grounds, which may already exist elsewhere. |
| experimental mechanism comparison | Compare degradation under the candidate accelerated and field-representative conditions using the mechanism-sensitive relation derived in §5.1.1; challenge acceleration-induced mechanism change and alternative material effects. | Requires qualified indicator relation, instrument feasibility, specimen/material comparability, safety, and authority. |
| field or observational comparison | Relate field exposures, failures, material batches, installation histories and operating contexts to assess whether the laboratory relation transfers. | Confounding, selection, few failures, measurement limitations or lack of access may limit the distinction. |
| computational/model challenge | Test the proposed mechanism and acceleration relation through a domain-qualified model, sensitivity, calibration, and validation target. | Model-to-phenomenon relation, parameter identifiability, implementation, data, and validation can dominate. |

**EvidenceSufficientStop scenario.** Suppose an applicable result for compatible materials and the operating envelope shows that acceleration changes the dominant degradation mechanism. Return that finding and its scope. It answers whether evidence from this test can support the proposed mechanism-preserving inference. A stronger use would need a different basis.

**ResearchDesignDecision scenario.** Under the conditions in §5.1.1, the signature comparison is discriminating, obtainable and worth its burden compared with the field, model and no-new-study options. Select that strategy. The remaining PostSelectionNeed items concern the location and serialization of the required specimen, condition, observation and deviation records. Every admissible choice preserves the comparison and permits those records to be retrieved. If a required field cannot be recorded or retrieved, reconsider selection.

**ResearchDesignHold scenario.** The measurement result does not yet establish whether the indicator distinguishes the two degradation mechanisms. If it can, the experimental comparison may work. If it cannot, that comparison fails and a field or model strategy may be preferable. If the selection still matters, return this dependency and its consequences. The measurement specialist may already have suitable evidence. A decision to obtain a new result is a separate commitment.

**QualifiedNoNewStudy scenario.** The evidence leaves the Pump-P4 relation unresolved. The matched specimens have been lost and the available field and model material cannot distinguish the competing mechanisms for this case. Select no new study for the present allocation. Future specimens would belong to a different case. Newly released field records could make a relevant comparison attainable and justify reconsideration. A maintenance interval remains a separate decision.

#### RMP.2:5.2 - Citizen Stream Salinity: Dispositions without an Affiliation Gate

A resident team asks what explains the salinity increase in a specified reach and period. Possible accounts include road-salt transport, groundwater, a changed outfall, seasonal hydrology and sensor drift. Residents can frame and pursue this research in their own capacity. Available resources, measurement competence, safe access and applicable permissions still affect what they can do.

- Return `EvidenceSufficientStop` if validated monitoring and source results already distinguish the relevant explanation for this reach, period and use. State the scope and any remaining limits.
- Return a field or observational `ResearchDesignDecision` when the measurements, comparison reaches or periods, safe access and applicable permissions support a spatial or temporal contrast that can challenge the live rivals, and the contribution warrants its burden. A record locator may be chosen later if every admissible arrangement preserves the observations. Unknown calibration, access or comparison matters if it could change this selection.
- Return `ResearchDesignHold` if the field choice is still needed and sensor validity, site or record access, or a seasonal comparison could make the strategy work or fail. State which result could distinguish the options and who can establish it when known. The community may itself be able to answer.

The environmental finding can support a bounded explanation and identify evidence limits. If remediation is proposed, the applicable authority decides on that action.

#### RMP.2:5.3 - Historical Source-Critical Case

An archive group asks whether a maintenance-practice change followed Directive-D or began earlier. An authenticated dated record may already answer the chronology question. A source-critical study could compare the dates, provenance and purposes of workshop records, consider archival silences and examine rival interpretations. If the question concerns a contested corpus already traced, synthesis is another possible strategy.

If the discriminating records have suitable provenance and access, a historical design may be justified with only invariant transcription and locator conventions left to settle. If an open provenance or access question could make the comparison viable or impossible and a selection is still needed, return ResearchDesignHold. Use source criticism appropriate to the chronology rather than ranking the evidence solely by experimental criteria.

For the narrow chronology question, suppose one authenticated workshop series is the only accessible material that could distinguish practice before and after the directive. An index and another scan format expose the same records. Their content does not provide independent corroboration. If the source-critical examination fits the two available investigator-days and evidence of an earlier or later practice would alter the claim, this one strategy can warrant ResearchDesignDecision. If the work would instead take twenty days, only two are available and no feasible reduction preserves its discrimination, retain the open chronology and return QualifiedNoNewStudy for this allocation. A newly accessible independent ledger could change the comparison.

#### RMP.2:5.4 - PostSelectionNeed Counterfactual

Consider two questions about a proposed field design.

| Remaining value | Counterfactual test | Disposition |
| --- | --- | --- |
| directory and identifier syntax for required observations and deviations | Every admissible choice permits the required records to be retrieved and preserves the field comparison and its criticism. A syntax that loses a record falls outside this range. | PostSelectionNeed |
| whether the available sensor can discriminate salinity from temperature-dependent drift at the required scale | If it can, the field comparison remains possible. If it cannot, another instrument, a different evidence relation or no new study may be appropriate. | ResearchDesignHold when that selection remains necessary. |

Classify a remaining input by the effect its admissible values could have on the selection, including their effects together. The date on which the input is expected to be settled is a separate scheduling matter.

### RMP.2:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| favorite-method bias | The practitioner's familiar design defines the question and rivals. | Hold the brief fixed and compare actual answer-changing relations with the relevant no-new-study outcome. |
| hierarchy bias | One design family is presumed strongest regardless of claim and threat. | Compare the specific evidence relation and criticism each option enables. |
| novelty-of-tool bias | A new sensor, model, AI workflow, or platform is treated as an informative design. | State the answer-changing contrast, threats, and validation relation independently of the tool. |
| false-stop bias | Limited time, funds or willingness is reported as sufficient evidence. | Compare the evidence with the answer condition. An allowed return with uncertainty may end the work while the question remains open. |
| provisional-design bias | The proposal is called selected while a consequential input remains open. | Compare plausible results for that input. Return ResearchDesignHold if the needed selection depends on which occurs, or QualifiedNoNewStudy if no study has been selected on adequate grounds for this allocation. |
| hold-everything bias | A harmless record name or schedule choice prevents selection. | Check that the admissible values, including their combinations with other inputs, preserve the comparison, feasibility and refusal conditions. |
| reporting-as-design bias | A reporting guideline or protocol template is treated as design evidence. | Use it later for transparency where applicable; select the question-to-criticism relation here. |
| mixed-method accumulation | More methods are assumed to strengthen an inference automatically. | Explain each component’s evidence contribution and how to handle agreement, disagreement and partial failure. |
| unsupported information-gain estimate | A numerical gain is assigned without a defensible model of outcomes or use. | Identify the live uncertainty and what the possible answers could change. Use a qualitative comparison when the evidence supports that degree of precision. |
| authority inferred from design | Selection is treated as permission for access, safety, ethics, spending or an action by the recipient. | Identify the decision and the grounds for any applicable permission. Use an established decision or state the limit when the needed authority is absent. |

### RMP.2:7 - Conformance Checklist

Apply the following questions to the disposition being returned. For sufficient evidence, give the answer and limits. For no new study, explain the present allocation. For a hold, state the blocking dependency. The remaining design details apply to a selected strategy.

- [ ] **RMP2-01:** The question and its current basis are sufficiently qualified. Where a change leaves that qualification open, identify or obtain the contribution needed from RMP.1.
- [ ] **RMP2-02:** The intended use, answer condition and work-stop conditions are clear. Where a later action requires a decision, identify the applicable authority or the specific gap.
- [ ] **RMP2-03:** Before selecting work to obtain new evidence, determine whether the current evidence already answers the question.
- [ ] **RMP2-04:** A claim of evidence sufficiency accounts for the scope, relevant rivals, provenance, currency, uncertainty and reliance required in this case.
- [ ] **RMP2-05:** Constraint, cost, preference, or low priority is not mislabeled as evidence sufficiency.
- [ ] **RMP2-06:** The actual serious options address the same brief; a sole real research relation is judged against no new study without a quota of invented alternatives.
- [ ] **RMP2-07:** An applicable current practice or available routine remains in the comparison if it offers a serious option.
- [ ] **RMP2-08:** For each serious strategy, the account shows how the available material and operation could address the question, what would challenge the result and what obtaining it would require. If the connection had to be constructed, follow it on concrete material and repair or report a material failure.
- [ ] **RMP2-09:** Use the evidence and criticism appropriate to each family considered. When combining designs, explain how their contributions relate.
- [ ] **RMP2-10:** The selected option can expose the principal error or rival named in the brief.
- [ ] **RMP2-11:** For an alternative that was considered and rejected, state the reason for that decision.
- [ ] **RMP2-12:** Identify the construct, evidence, measurement, access, rights, capacity and other conditions that could change this strategy or its use.
- [ ] **RMP2-13:** Identify the grounds for inputs already established. Distinguish assumptions and missing results.
- [ ] **RMP2-14:** For an unresolved input that could still affect selection, explain how its plausible values or joint combinations could change the design or the decision to stop.
- [ ] **RMP2-15:** A value that prevents a still-needed selection by changing family, core contrast, criticism, feasibility or refusal produces ResearchDesignHold; an unknown does not create a pending investigation when the present allocation is already settled as QualifiedNoNewStudy.
- [ ] **RMP2-16:** A hold identifies the unresolved result, a qualified source or holder if known, the options affected, their plausible consequences and what would allow the choice to be completed. State which work the present basis cannot support.
- [ ] **RMP2-17:** In a hold, distinguish conditional strategies from a strategy already selected.
- [ ] **RMP2-18:** Across every admissible remaining value and their joint combinations, a PostSelectionNeed preserves the family, core contrast, criticism, feasibility and refusal conditions.
- [ ] **RMP2-19:** A PostSelectionNeed value outside the admitted range reopens selection.
- [ ] **RMP2-20:** An empty PostSelectionNeed set is written explicitly as `none`.
- [ ] **RMP2-21:** One of EvidenceSufficientStop, ResearchDesignDecision plus genuine PostSelectionNeed, ResearchDesignHold, or QualifiedNoNewStudy answers the present selection boundary. QualifiedNoNewStudy preserves insufficient evidence or a bounded answer and the reason no new study is selected.
- [ ] **RMP2-22:** Entry to RMP.3 requires a selected strategy or a compatible supplied equivalent. Its specification, execution, findings and permissions have their own grounds.
- [ ] **RMP2-23:** Expected information gain is tied to the uncertainty the strategy could reduce and the conditions under which the answer would be useful.
- [ ] **RMP2-24:** Where reporting guidance is used, identify what it supplies. Establish design selection and actual execution from evidence for the particular claim.
- [ ] **RMP2-25:** Domain and measurement conclusions have their professional grounds. Decisions about rights, access, safety, ethics, resources, assurance or further action stay with the applicable authority.


### RMP.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| “Use the gold-standard design” | A design suited to one question or threat can miss another. | Compare what each serious option could expose under the available conditions. |
| “List the ingredients and the design will follow” | A list of sources and measurements can leave unexplained how they could distinguish the claims. | Use §4.4 to connect the needed distinction to an obtainable operation and follow it on actual material. Repair a failure that matters or report the resulting limit. |
| “The protocol is the design” | A detailed procedure may leave its evidential rationale open. | Look for the basis of the question-to-evidence relation, relevant alternatives, threats and selection. A protocol that already explains them can supply this information. |
| “Evidence is incomplete, therefore study” | An unresolved claim does not select a useful obtainable acquisition. | Compare the whole burden and contribution; return QualifiedNoNewStudy when the current allocation closes without a new study. |
| “No budget, therefore evidence sufficient” | Resource refusal is not an epistemic conclusion. | Preserve the bounded answer or unresolved question in QualifiedNoNewStudy when no current study is selected; resource and receiving decisions remain with their owners. |
| “Select provisionally and validate later” | A missing mechanism, measure, access, protection or permission could overturn the selected strategy. | If the selection is still needed, return a hold and describe the missing result and its consequences. If the current allocation already justifies no study, return that decision and the evidence limit. |
| “Everything must be fixed before selection” | Some implementation details cannot change the justified strategy. | Check that jointly admissible values preserve the family, comparison, criticism, feasibility and refusal conditions. Record a remaining need as PostSelectionNeed when it passes that test. |
| “Two software packages are two research designs” | Different implementations may support the same evidential comparison. | Determine what differs. An eight-hour run and a two-hour run may realize the same research design at different costs. Compare practical alternatives where that difference matters, and distinguish a change of design when evidence, criticism or meaningful constraints change. |
| “Mixed means stronger” | Components may share a bias, disagree or lack a justified relationship between their results. | Identify what each contributes, how the results could be combined and what can still be concluded if one fails or the components disagree. |
| “A rerun is a replication” | Code/data/environment reproduction, new-data replication, validation, and robustness test different claims. | Name the live threat and select the credibility move that bears on it. |
| “The selected design authorizes the study” | Its justification establishes a strategy. Acting may require permission for access, safety, ethics, rights, resources or another use. | Identify any applicable authorization already in force or the decision still needed from its holder. |

### RMP.2:9 - Consequences

A researcher can use an adequate answer, justify a feasible design, hold a particular choice or close the present allocation with no new study. The account shows how the evidence bears on the question and what conditions protect the inference. A detail can be left to later work when its admissible values and combinations cannot change the selection.

To compare unlike strategies, establish what each could contribute and what it might miss. A change in access, measurement, the proposed mechanism, protections or authority can alter which strategy is feasible or worthwhile. Reconsider those parts of the comparison on which the use depends.

A later reader can distinguish a sufficient answer, a selected strategy, a choice still held open and a completed decision to undertake no new study on the available basis. Evidence of execution, findings, a commission or a subsequent decision must establish that particular occurrence.

### RMP.2:10 - Rationale

A design identifies how relevant material could be obtained and what its examination would establish. Following the proposed operation on concrete material can expose a gap that a family name or option list conceals. Both reference seals have wear score 6, so matching scores cannot establish matching mechanisms. The qualified signatures and comparability conditions support a different proposed test. When selection is still needed, weigh that contribution and its limitations against the alternatives and full burden.

A remaining detail belongs to PostSelectionNeed when all admissible values and joint combinations preserve the family, core comparison, criticism, feasibility and refusal. A selection still needed belongs on hold if plausible values support materially different outcomes. Where the present allocation has already selected no study, the same unknown can remain a limitation or a reason to reconsider.

Use EvidenceSufficientStop to return an already adequate answer. Use QualifiedNoNewStudy when a decision to undertake no new study is justified and the evidence is still insufficient. Substantiate domain facts, instrument capability and permissions on their proper grounds when the chosen strategy relies on them.

### RMP.2:11 - SoTA-Echoing

The methodological question is how to develop and choose a strategy that bears on the research question, or to finish without a new study, while making consequential missing information visible.

The MRC/NIHR [complex-intervention framework](https://doi.org/10.1136/bmj.n2061) uses programme theory, context and key uncertainties to guide inquiry, revision and stopping. Its phases concern complex health interventions. The transferable contribution here is the connection between explanatory premises and research choice. In [Cochrane Handbook chapter 2, §2.5](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-02), conceptual models identify assumptions, relate effects to required conditions and shape a review’s comparisons. Apply those operations to the question they serve. Review eligibility and synthesis retain their specific methods.

C.39 guides the construction in §4.4. Work backward from the required answer to an operation, follow its use on available material and repair a failure where worthwhile. A specialist may already have supplied an adequate strategy. When the evidence relation is missing, a list of candidate fields leaves the gap open. In the seal example the wear index admits both mechanisms. Professional premises allow a different comparison using the signatures. The example illustrates the reasoning and its additional design effort. An empirical claim about the method’s effectiveness would need evidence about actual use.

Different professional sources guide different inferences. The [Standards for Reporting Qualitative Research](https://doi.org/10.1097/ACM.0000000000000388) supports transparent reporting while allowing different qualitative paradigms and methods. The American Historical Association’s [Statement on Standards of Professional Conduct](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) addresses source use, assumptions, bias and alternative interpretations. The [Cochrane Handbook](https://training.cochrane.org/handbook/current/chapter-02) relates review eligibility, search, collection and synthesis to the question. The National Academies’ [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303) distinguishes computational reproduction from new-data replication. Use the contribution that bears on the current threat.

A domain ranking or a familiar sequence of studies can guide a recurring question when the applicable conditions justify it. Applied across all questions, a fixed ranking can conceal the error that historical source criticism, qualitative reflexivity, observational comparison, model validation or corpus synthesis could expose. Compare the actual evidence and losses. Existing evidence or a justified no-study allocation can also finish the work.

For domain claims, instrument validity, rights, access and protections, use the appropriate evidence and authority. If a professional source or local rule changes the feasible options or the error a design can expose, revisit the affected comparison. If the joint-input test repeatedly misclassifies a design, examine both the criterion and its application and repair the source of the error.

### RMP.2:12 - Relations

Use RMP.10 when ordinary A.3.1.MR recovery leaves a consequential question about a candidate account of how work was done. Use RMP.11 for a source-critical explanation of how an identified Method or its relationship to another Method changed. Either may supply an evidential distinction for design selection. Establish access, suitable sampling and a selected strategy separately when they are needed.

- **`RMP.1` — Decide Whether a Question Needs Research and When to Stop.** Use its qualified brief and current account to enter this method. Return there if a change in question, use, evidence or stopping conditions requires qualification that is still missing.
- **`RMP.1:4.3`.** Use F.1, F.0.1 and A.10 to compare available meanings and evidence where needed. A source comparison may already answer the question, reveal a different question or identify a material uncertainty requiring research.
- **`C.39` — Find and Develop a Way to Obtain a Result.** Use §4.4 to recover a relevant operation, reason backward from the needed distinction, follow the proposed connection on material and repair it where needed. Use professional competence and domain evidence for the underlying relations.
- **Core Method development and A.3.1.MI.** Use Method Engineering for the identity, repertoire, architecture, qualification, fit, worth or introduction of a reusable Method. RMP.2 selects a research strategy for one qualified question.
- **Operationalization and trace.** Enter RMP.3 with a selected design and any genuine PostSelectionNeed items, or their compatible equivalents. A stop, hold or no-new-study decision can complete the present work. To report that the research took place, use a trace or other suitable evidence of the actual work.
- **Professional evidence and authority.** Use domain research, measurement and instrument evidence, archives and other suppliers for the facts the strategy needs. For participation, rights, access, safety, confidentiality, resources or consequential use, rely on the applicable permissions and decisions. Identify a missing permission when it affects the choice.
- **MRC/NIHR complex-intervention framework:** supports perspective pluralism, uncertainty-led design, non-linear entry, reconsideration, and stopping for its declared intervention-research scope.
- **SRQR, AHA professional standards, Cochrane Handbook and the National Academies account.** Use the family-specific contributions to reporting, source criticism, synthesis, reproduction or replication described in §11.

### RMP.2:End

# Part II - Operationalization and Research Trace


## RMP.3 - Operationalize the Research Design without Replacing the Question

> **Type:** Research Method Practice practitioner method pattern
> **Status:** Stable

### RMP.3:1 - Problem Frame

Use this method to specify or assess the operations of a selected research design. Identify the consequential choice of specimen, encounter, source, observation or computation. Ask how it would help distinguish the alternatives in the qualified research question. A suitable existing protocol may already answer that question.

For example, a pump engineer has selected a comparison of accelerated and field-representative seal degradation. An easily measured wear score can answer a wear question. To assess preservation of the failure mechanism, the score or other evidence must distinguish the relevant mechanisms under the comparison conditions. A detailed schedule alone cannot establish that connection.

The operational specification connects one bounded design to the particular actions and records needed to carry it out. Depending on the question, it may specify a measurement, an interpretive encounter, a historical source comparison or a model experiment.

The **ResearchProtocolAndOperationalizationMap** is the protocol and the reasons its consequential choices address the question. A short protocol can state the reasons beside the relevant procedure. For a more complex design, use qualified instrument accounts, source descriptions or established procedures directly, identifying the conditions under which they apply.

Return the specification that is usable for the stated scope or identify the action or inference it cannot yet support. Reuse an adequate compatible protocol. If a gap concerns the research question, use RMP.1 as needed. If it could overturn the selected design, use RMP.2. Developing a reusable Method, obtaining a required permission, performing the study and interpreting the results each depend on their own tasks and evidence.

### RMP.3:2 - Problem

Some operational choices can change the question a study can answer. A replacement comparison site, different construct measure or convenience sample may remove the distinction that justified the design. Preserve both the intended arrangement and what actually happened when comparing the protocol with subsequent work.

Some confirmatory inquiries rely on choices fixed before the relevant outcome is seen. Qualitative, exploratory or source-critical inquiry may instead depend on justified development during the work. Specify what must be settled in advance, what may evolve and how a change will remain open to examination.

How can a practitioner make the design executable, preserve its criticism and allow appropriate adaptation without either hiding a defeated premise or imposing a universal research checklist?

### RMP.3:3 - Forces

| Force | Tension |
| --- | --- |
| Specificity | The specification should let its user recover what to do and why. Copying a full technical manual may obscure the consequential research choice. |
| Methodological fit | Instruments and templates can aid a question when their observation and interpretation fit it. Familiarity alone leaves that fit untested. |
| Advance commitment | Prior choices can protect criticism, while some inquiry depends on learning what to ask or inspect during engagement. |
| Feasibility | Access, timing, measurement and resources may each appear sufficient but fail in combination. |
| Records and protection | Later criticism needs consequential choices preserved, while indiscriminate recording can expose protected information or add unusable volume. |
| Supplied competence | A researcher can apply their own qualified procedure or use a suitable laboratory, statistical or archival contribution supplied by another practitioner or service. |
| Continuity | Most of a design may survive a local obstacle, while work depending on a defeated premise must stop or change. |

### RMP.3:4 - Solution

Keep the research question and the error the design must expose in view. Establish the reasons for consequential choices, check how they work together and identify what can be carried out under the present conditions. If a link is missing, state which action or claim depends on it.

#### RMP.3:4.1 - Recover the question and the selected design

Use the qualified question and its current basis from a **ResearchQuestionBrief** or equivalent information already available. Identify the use, population, setting, period or corpus that determines scope. State what the evidence would have to establish and when work can stop even if uncertainty remains. The inquiry may seek to revise an explanation, a model or another claim.

Use the **ResearchDesignDecision** or an equivalent selected design. Identify the evidence strategy, core contrast, relevant rivals, threats and appropriate criticism. Criticism here means an examination capable of exposing an important error or limiting the answer. Use an experiment or significance test only where it bears on that question.

A ResearchDesignHold identifies an unsettled choice. To proceed on that design, use evidence that resolves the consequential input or a subsequent justified selection. If neither is available, report what the hold prevents. A suitable design supplied independently can already give direct entry.

Examine a consequential operation. Explain its relation to the question in terms such as these.

> Examining this material in this way could distinguish the relevant alternatives because … . The inference applies under these conditions … .

For the seal inquiry, relate the observation to the possibility that acceleration changes the degradation mechanism. For a historical inquiry, relate an authenticated date to the possibility that a practice preceded the directive. If the required connection is missing, use an available subject account or identify the premise on which selection depends.

#### RMP.3:4.2 - Connect the question to particular material and actions

Specify the choices on which the inference depends. The table offers questions for the parts of this protocol that matter.

| Choice to settle | What makes the specification usable |
| --- | --- |
| Phenomenon, construct or meaning | State what the inquiry is trying to distinguish and why the proposed observation, source or encounter bears on it. A familiar variable name or cited scale does not establish that relation in the present use. |
| Units, cases and selection | Identify what is selected, what is changed or exposed, what is measured and what units the inference concerns. Give the source and grounds for choosing the attainable sample or corpus. Repeated readings can supply information about one specimen’s measurement variation. Its independent specimen count remains one. |
| Comparison or interpretive relation | Explain what will be compared, challenged or interpreted, which rival it can expose, and what differences must be controlled, described or acknowledged. |
| Timing and context | Specify the periods, sequence, exposure or engagement conditions that make the material comparable or interpretable. Retain the conditions that could make a later observation a different case. |
| Measurement, source or engagement Method | Identify the qualified procedure, source-critical technique, field or interview approach, computation or other operation and the conditions on which its use depends. Name the edition or configuration if it affects what can be done or inferred. |
| Information and uncertainty | State why the attainable material is useful for the intended criticism, what its limits are, and which supplied domain or statistical judgement supports that expectation. |
| Execution and access | Identify the capabilities, materials, facilities, permissions and access the proposed action needs. State which are available and which remain unknown. If another party supplies a result or controls access, identify that dependency where it matters. |

For a quantitative inference, establish the applicable basis for sampling or precision, dependence among observations and the measurement qualifications the question requires. An existing qualified result may supply them. To interpret an instrument indication as a measurement result, use the relevant measurement account, including its uncertainty and conditions. FPF C.16 guides measurement and characterization.

For a historical inquiry, identify relevant source series, dates, authenticity, provenance, transcription and the interpretation of silence where they matter. For qualitative inquiry, consider the theoretical orientation, researcher and participant positions, encounter conditions and how interpretation may develop. Specify the grounds appropriate to each source or encounter.

Use an adequate domain procedure directly. Explain its connection to the question and identify changes in application conditions that matter to the result.

#### RMP.3:4.3 - State the intended use of the material and the records it needs

Explain how the proposed material will be used in the analysis or interpretation. Identify the applicable method and any remaining consequential choices about exclusions, missingness, stopping or adaptation. State what the protocol specifies. An account of what was actually done or inferred requires the corresponding evidence.

Decide what a later critic would need to examine those choices. A specimen identifier may connect an exposure record to a measured value. A search version may explain why a source entered a review. A dated protocol may distinguish an advance commitment from a choice made after an outcome was seen.

For prospective work, arrange to preserve a consequential distinction before it can be lost. Use RMP.4 for a trace of actual decisions and work, including work begun while the specification evolves. For an inherited study, use what the existing records establish. Identify unresolved choices and lost evidence explicitly.

Identify applicable retention and access conditions. A public summary, a controlled original and a permitted independent inspection can support different examinations. Use existing rights and arrangements when they suffice. If necessary information cannot be retained or examined, identify the effect on the design and on claims that would rely on it.

#### RMP.3:4.4 - Preserve useful commitments and method-appropriate flexibility

Preserve the choice, its rationale and its timing relative to data access, exposure to outcomes or interpretive engagement. A registration, protocol and analysis plan may each record different commitments. Check what the dated content actually settled.

Commit in advance when a method or use depends on a choice preceding the evidence. Where the approach permits development during the inquiry, specify the limits of change and how it remains connected to the question. Apply an institutional registration or approval when required, using a valid existing result where it covers the work.

In a reflexive inquiry into former workers’ experiences of a factory closure, an encounter may reveal a meaning that warrants refining the interview prompt. Preserve the starting prompt, the reason for the change and the encounters affected. Estimating the proportion of all former workers who share a view requires a suitable question, population and design. Revising the prompt alone cannot establish that proportion.

Other design families require their own operational distinctions:

| Inquiry | Consequential detail and return |
| --- | --- |
| Historical or source-critical | Specify which documents could establish chronology, or identify those actually inspected for a claim about past work. State how contrary or inaccessible material bears on the inference. If a required series cannot be examined, distinguish missing evidence from the absence of an entry in an inspected record. Use RMP.2 where this defeats the selected comparison. |
| Computational or model-based | Specify the model–target relation, input and parameter choices, transformations, environment needs and intended sensitivity or analysis Method. A successful program run cannot supply a missing model–phenomenon justification. |
| Evidence synthesis | Relate the review question to eligibility, search, screening, extraction and intended appraisal. If a restriction could change the answer, assess its effect on the selected design and the warranted scope. Synthesis findings require evidence of the material actually obtained and combined. |
| Mixed inquiry | Explain the contribution of each component, shared inputs and how results would be related. Check joint access, participation, capacity and assumptions. If the design needs independent evidence of chronology, extra interviews based on the same retrospective account may leave that gap open. |

Choose the distinctions that fit the inquiry. Other study families or combinations can require different operational details.

#### RMP.3:4.5 - Test the whole arrangement and choose the exact return

For a proposed arrangement, ask whether its operations together can expose the error or distinguish the rival that justified the design. Check consequential interactions among selection, access, measurement, timing, resources and records. Include jointly admissible unresolved values. For an existing protocol, use established evidence of these conditions directly.

Apply the joint-input condition in RMP.2:4.3. Every admitted combination of PostSelectionNeed values must preserve the family, core contrast, criticism, feasibility and refusal conditions. A detail may safely wait when it passes this test in the combined specification.

| What the specification reveals | Action and result |
| --- | --- |
| The choices and their joint effects stay within the selected scope. | Complete or assess the protocol with its reasons. State the supported work, remaining bounded needs and conditions for change. Carry out the work when that is the task and any required permission is in force. |
| A result is still needed for an operation, but every admissible value preserves selection. | Identify the input, the action it blocks, any known source or holder and what would allow that action to proceed. Keep the justified design and usable parts of the specification. |
| A new value could defeat the family, comparison, criticism, feasibility or refusal condition. | Identify which values preserve the design and which could defeat it. If a new choice is needed, return the unresolved value and its consequences to RMP.2. Preserve the earlier decision and any actual work in the trace. |
| The question, intended knowledge, population, context or useful stop changes. | Qualify the changed question through RMP.1 where needed. Use its established answer to revise the dependent design or specification when that work is required. |
| Permission or resources are withheld independently of evidence sufficiency. | Identify the affected action and the actual limit on proceeding. If a decision is needed, use the applicable authority or state the missing authority. Preserve the research question and assess evidence sufficiency on its own grounds. |

A calibration value may be needed for a measurement even if every admissible value preserves the required discrimination. If the instrument might instead fail to distinguish the mechanisms, that uncertainty reopens selection where the comparison depends on it. The timing of the answer does not determine its scientific importance.

#### RMP.3:4.6 - Leave a usable operational result

A **ResearchProtocolAndOperationalizationMap** is usable for its stated purpose when a suitably competent user can recover the following.

- the brief and selected design being elaborated;
- the consequential operational choices and their question-relative reasons;
- the supplied Methods, qualifications and practical conditions on which those choices depend;
- the planned conduct, use of material and required records; and
- the remaining limitations and conditions for an amendment, return or stop.

A small inquiry can place the reasons beside the relevant procedures in an existing protocol. For a larger inquiry, identify the source and instrument accounts by the versions and uses on which the specification depends.

An incomplete specification can answer which action or inference is unsupported. Retain the supported work and name that limit. If further specification is needed, assess whether a missing input can be obtained or a design choice reconsidered with sufficient value, feasibility and authority. A protocol whose core comparison has failed needs a new basis before it can be used for that inference.

### RMP.3:5 - Archetypal Grounding

These constructed cases stipulate the domain premises. Their identifiers and counts illustrate how to relate records and repeated observations to one another. Sample size and scientific thresholds require justification for the intended study.

#### RMP.3:5.1 - Pump-P4: from a mechanism question to an executable comparison

The Pump-P4 question asks whether acceleration preserves the field seal-degradation mechanism within a specified material and fluid envelope. Suppose the selected design compares accelerated and field-representative conditions. The mechanism marker and measurement procedure are qualified, the conditions are safe for the proposed work and the specimen plan is adequate.

The team adds these entries to its existing protocol:

| Protocol choice | Question-relative reason and required record |
| --- | --- |
| Give each seal a specimen ID and retain its material batch and assigned condition. | The comparison concerns degradation under the two conditions; material and allocation must remain recoverable. |
| Measure the qualified mechanism marker at the specified exposure points. | Preserve the procedure version, calibration basis, time and uncertainty needed to interpret the marker. The observed distinction must bear on the degradation mechanism. Both mechanism references can exhibit the same total visible wear. |
| Treat three readings from one seal as repeated observations of that seal. | They may characterize measurement variation. The comparison still has one independent specimen here. |
| Preserve material deviations, missing observations and the conditions under which they occurred. | The available records should let a critic distinguish material behaviour from allocation, handling and selection effects as far as the evidence permits. |

Each choice relates an operation to the mechanism question and identifies material that could challenge the inference. The protocol specifies the proposed work. Permission to proceed and a decision about the maintenance interval require their own bases where applicable.

Suppose a qualified measurement result now shows that the marker cannot distinguish thermal degradation from the competing field mechanism under the proposed conditions. Return that result and its consequence for design selection through RMP.2 when selection remains open. An overall wear score needs a justified relation to mechanism before it can replace the marker. Keep the existing brief and specimen information where they remain applicable.

On the valid-marker branch, suppose P4-07 is damaged in handling before the observation. Consult the protocol’s stated treatment of missing material. Preserve what happened and any action taken through RMP.4. The remaining data and their conditions determine which inferences can be supported.

#### RMP.3:5.2 - ResidentStream-S17: a missing comparison is not a scheduling detail

The residents have a qualified question and a selected comparison of salinity observations across sites and times. Suppose the measurement procedure, calibration, uncertainty and permitted access are established and the plan fits the hydrological conditions of interest.

The specification identifies the reach and sampling point, the trigger for observation, the required time relation between reaches, the measurement result and the weather, access and calibration records needed for interpretation. The residents can use a qualified laboratory result or perform the measurement themselves if they have the required capability and access.

Suppose the reference reach becomes inaccessible during the informative thaw. Preserve the downstream observations and the reach, period and access conditions they describe. Check whether an adequate observation of the reference reach in that same event is already available. If the pair cannot be recovered, the downstream evidence can still support its own descriptive claim. Reconsider the paired design under RMP.2 if that question remains live. A reference observation in later dry weather concerns different conditions and needs its own justification.

### RMP.3:6 - Bias-Annotation

Examine how operational choices affect which cases, phenomena or voices are represented. Convenience sampling, uneven survival of records, access restrictions and exclusions can limit the answer. Documenting a restriction makes it inspectable. Assess its consequences separately.

Consider the researcher’s position when it can affect the encounter or interpretation. Prompt wording, relationships, competence and access may change what can be observed. Use criteria appropriate to the approach, including coder agreement only when the interpretation relies on it.

Ask whether the finished arrangement could expose the important rival or error, even when it is inconvenient to observe. Instrument familiarity and institutional pressure may favor easier observations. In mixed inquiry, check whether components share the same cases, records or assumptions and what that means for their relationship.

### RMP.3:7 - Conformance Checklist

Use the questions that apply to the operational specification. Use qualified domain procedures for the observations or actions themselves.

- The practitioner can recover a compatible question, current frame and selected design, with their criticism and useful-stop conditions.
- Each consequential operation has a recoverable question-relative reason and the units, context and timing needed to use its material.
- Identify relevant measurement, source, analysis and operational inputs with their conditions. Distinguish available results and permissions from proposals or unresolved needs.
- Distinguish planned analysis from work already performed. Identify which records are needed while the relevant information can still be preserved, or which have survived for a historical use.
- Commitment and amendment timing is recoverable relative to the information already available. Legitimate adaptation remains method-appropriate.
- Check the jointly admissible values of unresolved operational choices. Identify a blocked action even if the selected design remains justified.
- If the selection premise fails, identify its consequence for RMP.2. Qualify a changed question under RMP.1 when needed. For a decision about permission or resources, use the applicable authority or state the limit.
- State what the protocol supports. Identify any action or inference that remains unsupported and what, if anything, could make it available.

For a disputed or consequential use, follow a material observation from its specified unit and procedure through the proposed comparison to the error it could expose. Where unresolved inputs interact, check their adverse admissible combinations. A fully populated form can still leave either connection unsupported.

### RMP.3:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it fails | Repair |
| --- | --- | --- |
| “We use the standard scale.” | The scale may have been validated for a different construct, population or administration. | Use suitable qualification for the intended conditions. If the relation remains open, state which design premise depends on it. |
| Three readings become three specimens. | The information claim silently changes its unit and dependence. | Keep observation and inference units distinct and use the applicable sampling and analysis rationale. |
| A completed reporting checklist is treated as a justified protocol. | Reporting detail cannot select or validate the research relation. | Connect each consequential choice to the question and supplied Method. |
| Every adaptation is either forbidden or hidden. | The first suppresses legitimate inquiry; the second removes criticism of selection and timing. | State justified commitments and preserve actual reasons, timing and scope of change. |
| A lost comparison is recorded but its original inference is retained. | A transparent record of the loss may still leave the inference unsupported. | Use any adequate substitute evidence from the relevant condition. Otherwise state what remains supported and return the defeated selection premise to RMP.2 if a choice is still needed. |
| Each remaining need is tested with all others favourable. | The combined arrangement may be infeasible or incapable of criticism. | Apply the joint-input test to admissible combinations. |
| The protocol is cited as permission or as a scientific result. | Preparatory choices establish what is proposed. | For a permission or a finding, use the applicable decision or suitable evidence for that finding, such as a qualified observation, measurement or analysis. Where these are unavailable, preserve the supported protocol and state the limit. |

### RMP.3:9 - Consequences

The specification shows which operational choices implement the design and which could change the question it can answer. Arrange prospective records while important distinctions can still be preserved. Use qualified procedures and suitable records already available.

Explaining a consequential choice takes work. It may reveal that a study needs another design or an unavailable professional result. The effort is justified when it can prevent work that would not address the question. A sound specification still leaves study findings to the actual investigation.

### RMP.3:10 - Architectural Rationale

Use RMP.2 to select an evidence strategy and RMP.3 to specify its operations. During specification, check that every jointly admissible remaining choice still preserves the selected evidence relation, criticism and feasibility. When it does not, report the consequence for selection.

A protocol specifies intended work. A trace records what happened. Both may be kept in one notebook and may develop together. If what happened in an inherited study is unclear, use RMP.4 to examine its surviving trace. Available records may already answer the question even when its original protocol is lost.

Use a suitable domain protocol and adequate records directly. Examine the connection to the research question when a consequential operation, change or limitation remains unclear. A measurement problem, interpretive inquiry and historical source comparison may each need a different explanation of that connection.

### RMP.3:11 - SoTA-Echoing

**Practice question.** Which choices must be specified in advance to preserve the research question, and which may develop as evidence or interpretation changes?

Explain the reasons for consequential choices and make their timing and any amendments inspectable. Use an existing protocol when it already supplies them. Select advance commitments or permitted revisions according to the kind of inquiry and the threat being addressed.

| Source and scope | Operational contribution and limit |
| --- | --- |
| Flake and Fried’s [Measurement Schmeasurement](https://doi.org/10.1177/2515245920952393) addresses the basis for choosing a measure. The [2026 measurement study](https://doi.org/10.1371/journal.pone.0356070) by Goos et al. examines measurements used in Many Labs. | In §4.2, establish the relation between construct and measure and state consequential administration and scoring choices. A published replication and the Many Labs findings do not by themselves establish the validity of the local instrument or a general failure rate. |
| Lakens’s [Sample Size Justification](https://doi.org/10.1525/collabra.33267) compares quantitative rationales for sample size in relation to inferential aims and constraints. | In §4.2, justify the attainable sample for the question it must answer. A resource limit can determine the sample obtained while leaving the desired precision open. Use a relevant statistical procedure for quantitative adequacy and suitable criteria for historical or qualitative inquiry. |
| [SPIRIT 2025](https://www.bmj.com/content/389/bmj-2024-081477) gives reporting guidance for trial protocols. [TOP 2025](https://www.cos.io/initiatives/top-guidelines) distinguishes registration, protocol and analysis-plan practices. | In §§4.2–4.4, identify consequential choices and the information available when they were made. Trial-specific requirements apply where the inquiry uses that design. Inspect the contents and timing when judging what was committed in advance. |
| Haven et al.’s [qualitative preregistration study](https://doi.org/10.1177/1609406920976417) offers a starting account for qualitative preregistration. Braun and Clarke’s [RTARG argument and review](https://doi.org/10.1177/02692163241234800) challenges generic defaults for qualitative reporting and assessment. | In §4.4, make initial commitments explicit and preserve justified changes under the selected approach. The Delphi study and Braun and Clarke’s review of reporting in studies that used reflexive thematic analysis address particular methodological settings. Other qualitative approaches need their own grounds. |
| AHA’s [professional standards](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) and the [Cochrane Handbook, chapter 2](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-02) address source criticism and question-led selection. | In §§4.2 and 4.4, examine provenance, contrary material and which sources the question requires. A lost archival series limits the conclusion that can be drawn from it. A historical or synthesis finding requires actual relevant material. |

These methodological sources support the specified operations within their own conditions. If a change in construct, approach, corpus or access defeats a connection to the question, reassess that choice. Consider a different professional procedure when it preserves the required inference and criticism at lower cost. Claims about an improvement in actual research practice need evidence of that use.

### RMP.3:12 - Relations

For a practice-reconstruction question, RMP.10 relates candidate accounts to observations, critical-incident elicitation and log evidence. For a question about Method history, RMP.11 relates dated sequences to competing explanations and diagnostic observations. Include the operations the question requires and identify the limits of each source of evidence.

- **RMP.1** helps qualify the research question and stopping conditions, including a materially changed question or use whose qualification remains open.
- **RMP.2**, especially §4.3, gives the selected design and the condition for jointly admissible unresolved inputs. Return a defeated premise there when its consequences for selection need to be settled.
- **RMP.4** helps preserve evidence of conduct and changes as they occur, or assess what an existing trace supports. Capture may begin while the specification is being developed.
- **FPF C.16** supplies measurement and characterization discipline; **FPF A.10** supplies claim-bound evidence and provenance discipline. RMP.3 adds the particular research question and operational connection.
- Qualified domain, statistical, interpretive, source, ethics, safety, access and resource practices supply their own results. The Core Method-development family applies when the reusable Method itself needs design or repair.
- **RMP.5** helps connect actual material and analysis to a bounded claim. **RMP.6** helps assess the claim’s credibility using available evidence or a worthwhile test. A protocol supplies the relevant intentions and choices. Substantiate execution and conclusions from the actual work.

### RMP.3:End


## RMP.4 - Preserve a Criticism-Ready Research Trace

> **Type:** Research Method Practice practitioner method pattern
> **Status:** Stable

### RMP.4:1 - Problem Frame

Use this pattern to preserve the material for a particular examination of research or to establish how an earlier inquiry produced a reported result. Name the examination and locate the records it needs.

For example, residents measured downstream salinity during a thaw and missed their visit to the reference reach. Their chart preserves the downstream observations. Record which visit they missed, why, what can be established about the reference reach from other sources, and what the remaining observations support.

This pattern connects **the course of an inquiry and the material retained for a named examination**. Its **ResearchTracePackage** gives the reader the necessary records or reliable references and explains how plans, conduct and changes bear on the result. The records can reside in several places. Include limitations that affect the intended use.

A package is “criticism-ready” for an examination when the material that examination needs is inspectable under the stated conditions. A partial account can establish where inspection stops and how that limits the conclusion.

During planning or fieldwork, preserve at-risk records while they are available. For inherited work, start with the surviving material. Use RMP.1–RMP.3 if a needed question, design or protocol still has to be developed.

Use an existing notebook, laboratory record or repository when it supports the examination. Apply RMP.4 when a connection between conduct and material, a change or a limit of use needs explaining. Obtain a substantive assessment, computational reproduction, access decision or new research separately when the work calls for it.

### RMP.4:2 - Problem

An account written after the result is known can lose an earlier plan, record a missed observation as a blank cell or omit a failed computation. A step called “processing” may hide choices by researchers or AI systems. The reader needs the particular choices and events that bear on the result.

A large collection can omit the decisive exclusion or its timing, be inaccessible to its intended readers, or disclose material outside the authorized use. A public summary can be sufficient for one examination and lack the detail another requires.

What records will let a reader examine the course of an inquiry, and what can be established when material has to be reconstructed, has been lost or has restricted access?

### RMP.4:3 - Forces

| Force | Tension |
| --- | --- |
| Capture before loss | A later critic needs consequential detail that may disappear before a final claim is formulated. |
| Proportionate records | More detail can enable later questions, while indiscriminate capture increases burden and disclosure risk. |
| Plans and conduct | A dated plan can establish a commitment. A later methods account may also provide evidence of conduct. What happened depends on the grounds for that account. |
| Adaptive inquiry | Knowing when an interpretation changed and which outcomes the researcher had seen helps a reader evaluate the change. |
| Access | A protected original may support a permitted examination that its public rendering cannot support. |
| Reconstruction | Surviving records can establish part of a history and leave the rest open. A reader needs to know which claims the records support. |
| Reuse | Different examinations of the same records can require different detail, provenance or access. |

### RMP.4:4 - Solution

Specify the examination, preserve the material it needs while that is possible, and connect the records to the choices and results they support. Identify what the reader can inspect, what can be reconstructed, and how loss or limits on access affect the answer.

#### RMP.4:4.1 - Name the examination and choose the entry

State the question the examination should answer. For instance, the investigator may need to explain an exclusion, establish whether a comparison took place, inspect the basis for an interpretation or find the inputs to a calculation. Identify the relevant design and material where they are known.

During preparation, identify what will later show whether the comparison took place and what material the proposed analysis needs. If a result is reported later, connect it to the material used to obtain it. An examination of an earlier plan can finish before any result or ClaimCandidate exists.

Choose the entry that fits the work:

- **Planned or ongoing work.** Identify the question, design and operational choices that matter to the examination. Arrange to capture the needed records while their contents can still be established.
- **Existing or inherited work.** Start with the question, any claimed result and the surviving material. Recover the design, protocol and conduct to the extent supported by records, testimony or other evidence.

Use a compatible question, design or operational decision that is already available. RMP.1–RMP.3 can help develop a missing contribution. If an earlier design is uncertain, give the basis of any reconstruction and the date it was made.

Identify the part of the study, sources, encounters, specimens or computation in question and the relevant period or version. For a different examination, check whether the material still suffices.

#### RMP.4:4.2 - Preserve the smallest material whose loss would matter

Ask what the critic would be unable to distinguish if one record disappeared. Start with those distinctions. Examples include which specimen was measured, which document was inspected, why a source was excluded, or whether an outcome was already visible when a choice was made.

For ongoing work, capture the event or choice while it can be observed. If a suitable laboratory or data practice already preserves it, cite the record with its relevant qualifications.

Keep the versions and dates of the plans relevant to the examination, including amendments. A registration, protocol and intended analysis can record different commitments at different times. To establish a prospective commitment, check its contents and timing against the work.

Distinguish how each part of the account is supported.

| Basis for the account | How to report it |
| --- | --- |
| A contemporaneous record supports the event or choice. | Identify its scope and the particular claim it supports. Check the basis of recorded statements on which the examination depends. |
| A person reports the event later. | Identify it as a later report and retain what supports or limits that account. |
| Surviving sources support a reconstruction. | Mark the reconstructed part, its sources, reasoning and uncertainty. |
| The relevant conduct, reason or timing is unknown. | Say what is unknown and which examination depends on it. |

A single notebook can contain all four kinds of account. Date any reconstruction and identify the evidence that places an intention before or after access to the data. If its timing cannot be established, leave it open.

Apply the retention, access and destruction requirements that govern the material. Where permitted, preserve evidence of loss and explain its effect on the examination.

#### RMP.4:4.3 - Connect actual conduct, transformations and uses

Follow a consequential reported result back to the observations, sources, encounters or computations used to obtain it. For a planned comparison, identify the material it would require and what has been collected so far. Show how selection or transformation connects the material to its intended or actual use.

For observations, retain the identity of the specimen, case, participant, site or sample at the permitted level of detail and the conditions needed to interpret it. Distinguish instrument indications, qualified measurements and derived values. Use FPF C.16 when an examination depends on units, uncertainty or qualification that the recorded values alone leave unclear.

For documentary sources, specify whether the investigator used a catalogue description or inspected the document. Preserve the edition, locator, dating, provenance, reasons for selection and any relevant transcription or translation. Identify contrary evidence and unexamined collections where they affect the answer.

For transformations, show which operation produced the relevant output from which input. Record filtering, recoding, deduplication, aggregation, translation, corrections or computational steps that affect the examination, with versions and parameters where they matter. Use FPF A.10 when a claim needs its evidence and provenance made explicit.

For a reported computation, link the output to the particular run, its inputs, code and relevant environment, parameters and random seeds. Include failures and manual interventions that affect interpretation. A folder that contains several input versions may leave the version used in the run unknown.

For qualitative work, retain the material and interpretive choices on which the findings depend. Explain a change in the researcher’s position or questioning when it matters. Apply a coding-agreement criterion when the selected approach and examination warrant it.

For evidence synthesis, preserve the searches performed, including platforms or sources, dates, query versions and retrieved material. Trace screening, duplicate handling, exclusions and changes in extraction. These records can explain how the corpus was obtained. To establish appraisal or synthesis, locate evidence of the work performed.

In a mixed inquiry, preserve how each component contributed and how the investigators combined or interpreted their results. Identify shared data and assumptions. If two findings rely on the same participants or retrospective source, account for that dependence when assessing corroboration.

#### RMP.4:4.4 - Explain consequential changes and contributions

When a change from an earlier intention matters, identify the earlier plan, what changed, who made the choice, when it was made, and what material it affected. Give the supported reason and the data or results available at the time. Identify any part of that history that remains uncertain.

A missed observation, an excluded case, a failed run, an inaccessible source and a revised interpretation have different consequences. Identify the event. For example, an intact record may have been excluded from an analysis, whereas a missed observation has no recorded value to exclude.

If the outcome was known when a choice was made, retain that timing and the grounds for the choice under the method used. An advance commitment needs earlier evidence. Date any later sensitivity analysis or independent criticism separately.

Identify the people, teams, tools or services whose contributions affected the inquiry. For AI-assisted work, preserve the following details when they matter to the examination.

- The model or service, its known version or configuration, and the time it was used.
- The relevant input context and the output used, to the extent permitted by the applicable protection and access conditions.
- What was checked against which source, who or what performed the check, what was accepted, rejected or revised, and how that affected the work. Where the applicable research guidance assigns responsibility to a human researcher, identify that researcher’s verification and decisions.

Preserve the wording of a prompt when it can change how a reader understands the research choice. Routine spelling assistance usually contributes nothing to that question. If a service withholds its internal state, describe what can be examined from the inputs and outputs that survive.

If a service suggests a nonexistent source, preserve the suggestion, the check and the resulting decision when they affect the examination. These records can establish the service’s contribution and the response to it. Any scientific claim that relied on that citation still needs a source that exists and supports the claim.

#### RMP.4:4.5 - Determine actual access and the consequences of loss

Establish which material survives and which parts the intended reader can inspect under the applicable permissions. A repository locator identifies a location, a policy sets conditions, and a custodian can report what is available. Compare the detail in the accessible version with the detail the examination needs.

For the proposed examination, determine what each available source or view supports.

| Material available | What the material supports | Use or remaining need |
| --- | --- | --- |
| The intended reader can inspect the relevant originals in context. | The reader can examine the named connection when its necessary material is present. | Use or supply the available material. Undertake scientific analysis or criticism when its result is requested. |
| Originals survive under restricted access. A public version contains less detail. | State what the reader can examine in the accessible version. | Use that version if it suffices. If further detail matters, use authorized access or a qualified inspection result where available. Otherwise state the limit on the conclusion. |
| Surviving sources support a reconstruction. | The reconstruction can answer a historical question within the scope of its evidence. | Give the sources, reasoning and uncertainty. If an essential distinction is still open, use stronger evidence when available or withhold the dependent conclusion. |
| A needed record was never made, was lost or can no longer be retained. | Identify the affected examination, what can still be established and any narrower use of the remaining material. | Report the gap when that answers the question. If further work depends on missing evidence, identify what it would need. New observations or a new run have their own design and trace. |
| Loss of evidence or access defeats a design premise or changes the research question. | Identify the affected relation and what the remaining material supports. | Reconsider the design under RMP.2 or the question under RMP.1 when further work depends on it. Preserve what was established about the original inquiry. |

A custodian’s qualified inspection can answer a question within its stated scope. To establish that another reader has access, check that reader’s permission and ability to inspect the material.

#### RMP.4:4.6 - Return the trace with a truthful receiving scope

Give the reader enough information to locate the material and understand its connections and limits. For the examination at issue, identify the following.

- The examination, research question and study portion, with the design as far as it is known.
- The surviving plans and the grounds for claims about what took place.
- The material used and the selections or transformations that affected it.
- The timing of consequential changes and the contributions of people, tools or services.
- What can be inspected or reconstructed and which conclusions access restrictions or losses limit.

One record can support several parts of the account. Link to suitable records and specify their identities or versions where later changes could make a reference ambiguous.

Trace a connection that matters to the examination. For a reported value or interpretive excerpt, locate the source and the choices that shaped the result. For a planned comparison, identify what material it would need and what is already available. If a needed record or access is missing, explain which part of the examination remains possible.

A limited package can answer a question about the surviving record. For example, “The downstream measurements and handling decisions can be inspected. The reference reach was inaccessible, and we have found no comparable reference measurement for the same thaw.”

### RMP.4:5 - Archetypal Grounding

The following examples specify hypothetical events and records for examining research.

#### RMP.4:5.1 - ResidentStream-S17: preserve a useful trace after losing the comparison

The selected design would compare salinity-related observations at a downstream reach and a reference reach during an informative thaw event. Assume the measurement method, calibration basis, safe access and intended site-period relation were qualified when the design was chosen.

During the event, downstream observations are made, but the reference reach becomes inaccessible. The team retains the following linked account:

| Retained material | What the account says and permits |
| --- | --- |
| The design and the plan that existed before the event | The team planned to compare measurements from both reaches during the same thaw. The downstream record also permits a description of that reach. |
| Downstream sample and measurement records | Sample IDs connect time, reach, hydrological context, instrument indications and the qualified measurement results, including the relevant uncertainty. |
| The reference-visit record | The team missed the planned visit because it could not access the site. The record gives the basis for that explanation. |
| Preparation of a later chart | Each downstream value can be traced to its measurement record. The chart identifies the missing reference observation and the resulting limit on comparison. |
| Effect on the inquiry | With no comparable reference observation available, the planned comparison lacks one member. The downstream observations remain available for a narrower question. If the inquiry needs a different design, use RMP.2. |

The reader can inspect the downstream measurement and handling history. In this case the team’s visit was missed and no other comparable observation of the reference reach during the same thaw is available. If a suitably qualified measurement from that reach and event were found, the reader could reassess the original comparison.

A reference sample taken later in dry weather documents a different hydrological condition. To use it for a comparison, establish the particular relation that makes it comparable and state which question that comparison answers.

If volunteers started sampling before recording a protocol, their labels, instrument logs and later accounts may establish parts of the sampling procedure. Date the reconstruction, identify its grounds, and distinguish a reconstructed action from evidence that the volunteers had committed to it in advance.

Apply the existing permissions to private land-access details. The public account can identify what role those details played and which questions the published material supports.

#### RMP.4:5.2 - Pump-P4: distinguish absence, exclusion and interpretation

On the valid-marker branch of the seal study, specimen P4-07 is damaged during handling before one planned observation. The trace retains its allocation and material identity, the handling record, the time and basis of the reported damage, the absent observation, the applicable prior exclusion intention and the decision actually taken.

The comparison dataset links each remaining observation to its specimen and explains why P4-07 contributes no value at that point. Three readings from a second seal provide repeated measurements on that single specimen.

A critic can now assess the effect of the missing observation or exclusion on the comparison. Changing the pump’s maintenance interval would require grounds for that change and the applicable authority.

#### RMP.4:5.3 - A computation with a research-shaping AI suggestion

A researcher uses an AI service to suggest a preprocessing change for a model comparison. In this constructed case, the retained account identifies the supplied design, original data and code version, the relevant proposal and input context, and the researcher's decision to revise and use the change. The actual run connects the changed code, environment and parameters to its output.

The service also suggests a nonexistent article. The researcher checks the reference, rejects it and preserves the source actually used. This evidence can establish how the suggestion was handled. The scientific claim depends on what the source used supports.

When the original service version becomes unavailable, the retained suggestion, the researcher’s decision and the implemented change can still be inspected. A new run can test the retained implementation. Reproducing the original service response would need its own conditions and evidence.

#### RMP.4:5.4 - Historical and interpretive records support different criticisms

When asking whether a directive preceded a change in factory practice, preserve the identifiers, editions, dates and provenance of documents inspected, the relevant catalogue entries, contrary evidence and transcription choices. In this case the unavailable earlier series leaves the rival chronology open. An earlier decision could have occurred without leaving evidence in the surviving series.

To study how former workers understood the closure, retain the encounters, permitted excerpts, the researcher’s position and the grounds for changes to prompts or interpretation. A new prompt may still address the same question. Estimating population prevalence would require a different design. Judge the interpretation by the selected approach and its grounding, including a coding-agreement criterion only where it applies.

### RMP.4:6 - Bias-Annotation

Identify missing cases, sources, encounters or failed runs where their absence could affect the question. For example, a record restricted to successful runs cannot establish how often runs failed unless it can be linked to an adequate record of all attempts.

Later knowledge can influence a witness’s account of an earlier reason. Preserve the grounds for the reconstruction, including what contemporaneous records and later reports establish about timing.

Data holders, communities and participants may have authority over access and use. Apply the relevant conditions and report what the authorized view allows its reader to examine, including any material limit on the conclusion.

### RMP.4:7 - Conformance Checklist

Use this checklist for the package's declared receiving examination.

- The account identifies the inquiry, the portion covered and the examination. Claims about completed work have grounds in the surviving material.
- Plans, actual conduct, later reports, reconstructions and unknowns remain distinguishable.
- Consequential material can be followed through selection and transformations to its receiving use, at the granularity that examination requires.
- For a consequential change, the account identifies the earlier intention, timing, reason, effect and information available at the time to the extent supported.
- The account distinguishes the consequences of missing observations, exclusions, failed runs, inaccessible sources and revised interpretations where they occur.
- The account identifies significant contributions from people, teams, tools or services, the checks performed and the applicable responsibility, at the detail needed and permitted for the examination.
- The account distinguishes surviving material, actual permitted access, public views, reconstruction and loss.
- The material and permitted access support each examination described as criticism-ready. When an examination is prevented, the account identifies the limiting condition, any narrower supported use and a further source or change of design if one is needed and available.
- A rerun or a later observation is identified by its own date, inputs and conditions.

When relying on the trace, follow a consequential use back to its source or use a qualified inspection that establishes the necessary connection. Compare a prior commitment with conduct when that difference matters. If the examination requires the intended reader to inspect the material, confirm that reader’s access.

### RMP.4:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it fails | Repair |
| --- | --- | --- |
| The final methods account replaces every earlier plan. | The critic loses the timing and content of commitments. | Retain surviving versions and distinguish reconstruction from prospective intention. |
| Missing observations, exclusions and failed work are all recorded as “cleaning.” | Their causes and effects on the result can differ. | Identify the event, its supported reason and its effect on the examination. |
| A repository link is treated as criticism-ready access. | The material may not survive, be accessible or contain the needed detail. | Establish the actual material and access for the named examination. |
| A public summary is used for a claim that depends on redacted detail. | Its reader lacks the detail needed to examine that claim. | Identify what each view supports. Use an authorized source or a qualified inspection result if available, or report the limit. |
| The number of files is offered as support for a scientific claim. | The decisive record might be absent from a large collection. | Identify the connection the claim needs and examine the evidence that bears on it. |
| An AI suggestion or citation is used as evidence without establishing what supports it. | A saved output can show what was suggested. The source and the inference need their own grounds. | Identify the source, checks, decisions and responsible contributors. Where the applicable guidance assigns responsibility to a human researcher, record how the researcher exercised it. |
| A run with substituted inputs is reported as a replay of the original computation. | It tests a different set of inputs. | Identify the inputs, decisions and service state that can be recovered for the original run, then state what the new run tested. |

### RMP.4:9 - Consequences

A reader can see what was planned, what evidence supports the history of the work, how material reached a result and where examination stops. Capture during fieldwork can prevent loss. A later reconstruction can recover part of the history even when the original plan is missing.

Recording the relevant connections and maintaining suitable access take work. When decisive evidence is lost or inaccessible, state the conclusions that the remaining records support and the questions they leave open.

### RMP.4:10 - Architectural Rationale

A protocol states intended conduct. A trace supplies grounds for claims about what happened, including departures from the plan and work for which no prospective plan survives. One notebook or collection can serve both uses.

Use the named examination to judge when capture is sufficient. The same material can support one criticism and lack the detail for another. Additional capture and disclosure require justification for the use they would serve.

Use existing domain records or provenance information if they supply the connections the question needs. RMP.4 helps recover how choices, transformations and access affect examination of the particular inquiry.

### RMP.4:11 - SoTA-Echoing

**Practice question.** What does a reader need to inspect the conduct of this study, and which further claims need a replay or a scientific assessment?

**Selected approach.** Record the origin of the material, the timing of consequential changes and the access available to the intended reader at the detail required for the examination. When records are lost or restricted, establish which narrower questions can still be answered.

| Comparison and source role | Adopt, adapt or reject; effect on the Method and limit |
| --- | --- |
| [TOP 2025](https://www.cos.io/initiatives/top-guidelines) distinguishes research practices and records of commitments. | §§4.2 and 4.4 use contents and dates to establish what was specified in advance. A disclosure badge can identify a reported commitment. To verify it, use the relevant record or a qualified verification that covers the claim. |
| Miske et al.’s [Investigating reproducibility](https://doi.org/10.1038/s41586-026-10203-5) (2026) examined attempts to reproduce results in publications from 2009–2018 with obtainable datasets. [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) illustrates how to record particular workflow runs. | §4.3 connects reported outputs to the inputs, transformations and runs that produced them. The study documents difficulties recovering computations. The format is one way to preserve the connections needed for inspection. |
| [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z) gives reporting guidance for searches. | §4.3 retains the search as performed, including its query, platform, date, retrieved material and changes during retrieval. Those records can explain how a bibliography was obtained. Judging its adequacy for synthesis requires the relevant appraisal. |
| Braun and Clarke’s [RTARG argument and review](https://doi.org/10.1177/02692163241234800) examines how papers report reflexive thematic analysis. The AHA’s [professional standards](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) describe historians’ responsibilities for sources and interpretation. | §§4.2–4.4 use the approach being examined to decide which choices, contrary evidence and grounds for reconstruction to retain. A requirement for coder agreement needs a basis in that approach. |
| Carroll et al.’s [Operationalizing CARE and FAIR](https://doi.org/10.1038/s41597-021-00892-0) develops data-governance principles in the context of Indigenous peoples’ rights and interests. | §4.5 asks whose authority governs a particular use, what the permitted purpose is, and what the reader can inspect. A FAIR resource can have restricted access. |
| The European Commission’s [May 2026 revision](https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/updated-era-living-guidelines-responsible-use-generative-ai-research-2026-05-08_en) and its [Living guidelines on the responsible use of generative AI in research, fourth edition, October 2026](https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en) address researchers’ responsibility for AI-assisted scientific output and disclosure of substantial uses. | §4.4 applies that guidance to records of significant AI contributions and the responsible researcher’s verification and decisions. Routine editing calls for proportionate records. These recommendations are non-binding. Access to protected inputs and the ability to replay a service require separate grounds. |

Reconsider what to retain if a different examination needs different material, a source or service change affects a connection, or an existing practice can support the examination at lower cost. The cited guidance, research and implementation examples establish the specific contributions described above.

### RMP.4:12 - Relations

An issued instruction can establish what it prescribed. To reconstruct how work was performed, use the sources that bear on that question, such as an occurrence record, a participant’s account or an event log. Use RMP.10 when further reconstruction is needed. Dated sources may establish that a method changed. Use RMP.11 when the question asks why or how that change came about. In each case, account for relevant dependence and gaps in what survived.

- **RMP.3** supplies operational intentions and research-relative record needs. Capture can begin while those intentions develop.
- A lost comparison can be reported with the remaining findings. Use **RMP.2** if a revised design is needed. Use **RMP.1** to reconsider a question or intended use that has changed.
- Use a clear, qualified record directly. **FPF A.10** helps when the connection from a claim to its evidence needs to be recovered or made reproducible. **FPF C.16** helps establish the measurement basis when a distinction between an indication, a qualified result and a derived value matters.
- Use the relevant professional practice for recordkeeping, source criticism, statistics or interpretation. Apply the existing decisions and conditions governing retention and access. When a new decision is required, obtain it from the person or body with the applicable authority.
- Use an available analysis or credibility assessment within its scope. **RMP.5** helps analyze and criticize a claim when a substantive judgement is still needed. **RMP.6** helps select and interpret a credibility examination when the question warrants one. A report that a reproduction test took place needs evidence of the test performed and its result.

- Use **RMP.7** when the material, its relationships and its limits bear on a question about a corpus. A synthesis requires the appraisal and integration appropriate to that question.

### RMP.4:End

# Part III - Analyze Claims and Choose Credibility Work


## RMP.5 - Analyze and Criticize the Research Claim under Its Method

> **Status:** Stable

> **Type:** Research Method Practice practitioner method pattern

### RMP.5:1 - Problem Frame

Use this pattern to establish what claim a body of research material, an analysis or an emerging interpretation supports. Start from the proposed claim or the question the analysis is developing. Trace a consequential connection from the material through the analysis to the claim and examine which criticisms affect its support.

A simulation may reproduce a reported curve while its relation to field failures remains untested. Several valid downstream readings may establish a pattern while leaving its cause unresolved. In each case, identify the result obtained and the evidence needed for the stronger interpretation.

The **ClaimCandidate** states the bounded answer. Its **CriticismRecord** identifies the examinations performed, their bearing on the answer and any remaining uncertainty. An annotated analysis, an existing notebook or a concise qualified answer can carry both.

Use an adequate supplied analysis within its scope. For inherited material, establish the origin, method and limits needed for the present claim. The resulting answer can support a current use, narrow an earlier claim or identify the point open to challenge.

Use a qualified disciplinary method directly for a routine calculation, qualification or interpretation with adequate criteria. If an inference still needs a source, design premise or criterion, identify it and the affected claim. Access permissions and decisions about action have their own grounds. Use RMP.6 if a remaining credibility question warrants comparing ways to address it.

### RMP.5:2 - Problem

An association can be misread as a cause, or repeated readings as independent cases. A theme may be reported as a prevalence estimate, archival silence as proof that an event never happened, or a calculation as validation of a model for a new use. Each stronger conclusion needs a connection that the reported result alone may leave open.

Additional analysis is worthwhile when it can clarify the inference at issue. An adequate result can be reused. If a required comparison is missing, more detail about the surviving material may support a narrower claim while leaving that comparison open.

Identify the analytical choices and contrary material that bear on the claim. Judge exploratory, interpretive and source-critical work using criteria appropriate to the method employed.

### RMP.5:3 - Forces

| Force | Tension |
| --- | --- |
| A useful answer | The strongest requested claim may exceed the evidence while a narrower conclusion answers part or all of the question. |
| Method fit | Familiar analytical tools are accessible, while unlike questions require different forms of criticism. |
| Discovery and commitment | A relation noticed during analysis can justify a new question. A claim of advance commitment depends on what was recorded or otherwise established before the relevant results were known. |
| Reuse | Existing analysis can answer the question, while a changed input, assumption or use may invalidate part of it. |
| Contrary material | A coherent account is easier to communicate, while discordant cases and plausible rivals can change its scope. |
| Inspectability | Another critic needs the consequential reasoning, while indiscriminate recording can obscure it or expose protected material. |
| Completion | The available evidence can justify ending with a bounded or unresolved answer. A further examination may be worthwhile if its attainable results could change that answer or its use. |

### RMP.5:4 - Solution

Identify the claim, the material and the method it relies on. Use an adequate existing analysis or perform the analysis the question requires. Examine the assumptions, contrary evidence or alternative interpretations that could affect its support. Return the bounded answer, the criticisms examined and any remaining limits.

#### RMP.5:4.1 - Recover the claim and one consequential connection

Specify the phenomenon, cases, population, setting, period or corpus that the claim concerns, the proposed relation and the conditions for its use. Distinguish description, interpretation, comparison, causal explanation and prediction when they require different evidence. If the claim emerged during analysis, identify when and how.

Trace the connection needed to judge the claim.

| Connection | What to recover |
| --- | --- |
| Material to observation or source claim | Which records, specimens, encounters, documents or computations are available, what they represent, and their selection, transformation, loss and access limits. |
| Observation or source to analysis | The method and units used, the assumptions, consequential choices or departures, and when those choices were made relative to seeing the results. |
| Analysis to proposed answer | The reasoning that makes the result bear on the exact claim, including the comparison or interpretation and the scope it can support. |

Use the relevant RMP.3 plans and RMP.4 records when they supply part of that connection. A plan can establish an intention. Use evidence of conduct for a claim about what occurred, identifying later testimony or reconstruction as such. A missing record or unperformed comparison limits the inferences that depend on it.

Retain an existing analysis that answers the question for the relevant material, method, assumptions and use. If a premise has changed or a live criticism exposes a gap, reconsider the portion that depends on it. A new filename or the age of an otherwise applicable analysis supplies no such change by itself.

#### RMP.5:4.2 - Use the analysis that fits the question

Choose an analysis justified for the subject, material and inference. Use the criteria and assumptions appropriate to that discipline. The following examples show why a criticism that matters to one claim may be irrelevant to another.

| Research use | Practical analytical move | Criticism that can change the answer |
| --- | --- | --- |
| Quantitative or experimental estimate | Identify the target quantity, units of sampling or assignment and comparison. Report the estimated magnitude and its justified uncertainty, including relevant exclusions, multiple comparisons and choices made before or after seeing results. | Dependence, missing data, measurement and analytical choices can change the estimate or its interpretation. A significance label alone gives neither an estimate of effect size nor grounds for attributing a cause. |
| Observational or field account | Relate observations to the sites, periods, selection and measurement conditions. State the pattern established. | Examine confounding, seasonality, selection and any missing comparison when attributing a cause. Repeated measurements of one site can describe variation at that site. Inference across independent sites needs evidence from those units. |
| Qualitative or reflexive interpretation | Develop the interpretation under the selected approach and theoretical commitments. Connect it to the research material, the researcher’s contribution and relevant discordant cases. | A theme may omit a different account or extend beyond what its extracts support. In reflexive thematic analysis, judge the interpretation by its coherence with the approach and its grounding in the material. |
| Historical or source-critical account | Examine the dating, authenticity, provenance and purpose of the sources, their dependence and the sequence of events in question. | Copies may share one source. An archive’s survival and access conditions can explain a silence. A document may establish when a change occurred while leaving its cause open. Check material that could support a contrary chronology. |
| Computational or model claim | Identify the target, derivation or implementation, data, environment, fitted quantities and relevant assumptions. Interpret the output for the stated target. | Reproducing an output can support a claim about the implemented calculation. Calibration, verification, sensitivity and validation for a field use each examine a different connection. |
| Mixed inquiry | Analyze each component using its appropriate method and specify the relation claimed between the results. | Check dependence, meanings, targets and disagreements before combining results. Preserve a disagreement that changes what the components jointly support. |

Apply the kind of criticism the claim needs. A descriptive estimate can answer a descriptive question. In a qualitative inquiry, establish the sampling, saturation or reliability criterion from the approach and question where it is relevant. Historical claims can be examined through surviving evidence. If a disciplinary criterion is still needed, identify the claim it limits and a competent source where one is available.

#### RMP.5:4.3 - Criticize the consequential inference

Start with a threat that could affect the answer. Include other threats on which the claim depends. For each examination that matters, establish the following.

1. which claim or inference could fail;
2. which observations, alternative analysis or source comparison could distinguish the possible answers or their degree of support,
3. what was actually examined and what was found;
4. whether the finding sustains or changes the answer, its scope or its uncertainty.

Compare plausible rivals and defensible analytical choices, including contrary material, relevant exclusions and missing evidence. If a threat has not been examined, say which inference remains uncertain. Failure to obtain a record is evidence about the search or access. A conclusion about the proposed event needs grounds linking that absence to the event.

If an analysis chosen after seeing results reveals a relation, report the discovery, its connection to the original question and its present support. Record what was known when the choice was made so a critic can distinguish exploration from an advance commitment.

For a sensitivity analysis, identify the choices examined and their effects. Limit robustness claims to the scope the comparison supports. If a variant changes the target quantity or question, identify the separate claim each result answers.

#### RMP.5:4.4 - State the answer the examination supports

Give the answer warranted for the stated question and use. The following outcomes distinguish what the examination established.

- support the bounded claim to the extent established by the material and Method;
- narrow or qualify the claim because a condition, rival or limitation matters;
- defeat the proposed claim or one of its necessary premises;
- leave the named claim unresolved while preserving what is known.

State which part of the requested claim the answer supports. Downstream measurements may establish a descriptive pattern after a causal comparison is lost. A computational result can stand even when its proposed field interpretation has been rejected.

Interpret an estimate and its uncertainty interval under the method that produced them. An interval that includes zero can be compatible with zero and with nonzero effects. To assess practical sufficiency or equivalence, apply the relevant threshold or margin and the comparison rule.

Return the answer and the examinations on which it relies. A remaining limitation may justify a different conclusion or a proposal for further study. Time and resources affect what can be examined, not the strength of the available evidence.

#### RMP.5:4.5 - Retain the account needed for criticism and use

Keep the material, consequential choices, actual examinations, results and limitations accessible to the extent the use requires. A concise answer with its basis, a qualified notebook entry or a reference to the relevant calculation may suffice.

Provide the source, analytical choice or reason on which later reliance depends, within the permitted access conditions. A reconstruction can support claims about an earlier choice and its timing to the extent surviving evidence warrants them. Identify it as a reconstruction and state which conclusions remain open.

Apply the conditions protecting participants, confidentiality and rights. An authorized critic may examine material unavailable in a public summary. State which conclusion each can support and whether a qualified result from the authorized inspection answers the public reader’s question.

#### RMP.5:4.6 - Finish or return the specific missing premise

| Finding about the present use | Useful continuation |
| --- | --- |
| The analysis and its criticism already answer the bounded question | Return that answer and its material qualification. |
| The research question or proposed receiving use has changed | Recover the changed question with RMP.1 or compatible supplied inputs. |
| A needed comparison is unavailable or a premise of the selected design is defeated | State the consequence for the proposed conclusion. If the task requires a different design, use RMP.2. A justified decision to conduct no new study can finish the inquiry. |
| A specified operation cannot supply the intended contrast | State the resulting limit. Use RMP.3 to revise the operation when a workable specification is needed, keeping any change of research question explicit. |
| The examination needs a connection to material or a transformation that has not been recovered | Use an adequate existing record or inspection. Where the history still needs work, use RMP.4 to establish what survives, what can be reconstructed and the limit on the conclusion. |
| A needed disciplinary result, criterion or permission is still missing | Identify the dependent question. Obtain the contribution from a qualified or authorized source when it is needed and available, or state the remaining limit. |
| A remaining credibility question could change use of the claim | Use an existing qualified answer when available. Use RMP.6 if it is worthwhile to compare ways of examining the remaining threat. |

A research finding can change the grounds for an engineering, policy or management decision. When the task also calls for that decision, apply its criteria and identify or exercise the relevant authority.

#### RMP.5:4.7 - What changes in practice

The practitioner can show why a conclusion follows, what criticism was considered, and what that examination confirmed, changed or left open. This can be a complete answer to the present question.

### RMP.5:5 - Archetypal Grounding

The teaching cases use stipulated events, measurements and conditions.

#### RMP.5:5.1 - The seal model runs, but the field claim is still open

In a Pump-P4 analysis, investigators calibrate a model on accelerated-test observations. A run using the retained code, data and environment reproduces the reported degradation curve. The proposed field conclusion is that the maintenance interval can be extended.

The run supports the computational result under the stated inputs. Extending the field interval would also require evidence that the accelerated and field conditions preserve the mechanism relevant to that use. No qualified comparison establishes that relation in this case. Report the reproduced curve, its domain of calculation and the unresolved field-use claim.

If a qualifying parameter analysis shows that plausible material values reverse the comparison, include that sensitivity in the answer. Rerunning the same inputs examines computational repeatability. Use RMP.6 when a further sensitivity or field-validation question would affect use enough to warrant investigation. The present model result can stand, and the applicable authority makes any decision about the maintenance interval.

#### RMP.5:5.2 - Downstream salinity without the reference reach

The team’s RMP.3 specification calls for paired reference and downstream readings during the same thaw. Its RMP.4 trace supports the downstream readings, documents the missed reference visit and identifies no comparable reference measurement from that event. The thaw has ended.

Use the qualified measurements to describe downstream change, keeping repeated readings tied to site and time. Without the reference observations, the planned paired comparison is unavailable. The downstream series alone leaves the proposed outfall and the relevant hydrological alternatives unresolved as causes.

Return the observed pattern and the unresolved attribution. A qualified reference observation already made during that thaw, if found, could support the original comparison. Later authorized matched observations can address a new period using the conditions they actually cover.

#### RMP.5:5.3 - A directive date and an earlier practice

A historical claim says the practice first began after Directive-D and was caused by it. Authenticated records establish when the directive was issued. The earlier workshop series is inaccessible. Its catalogue identifies material to seek, but the evidence available here leaves the possible earlier practice open.

An authenticated earlier ledger then establishes that the practice occurred before issuance. This defeats the proposed chronology of its first occurrence. The cause of that earlier practice and any effect of the directive on later adoption remain separate questions.

#### RMP.5:5.4 - A situated theme is not a workforce percentage

A reflexive thematic analysis examines a small set of maintenance-team interviews under an explicit interpretive approach. A proposed theme presents record keeping as a means of blame. The supporting extracts describe defensive documentation, while another account treats the same records as useful protection during shift handover.

Examine how the investigator developed the theme and how their position shaped the reading. Include the discordant account. Here the extracts support a tension between blame and practical protection. State that interpretation and its grounds in the existing annotated material.

The interpretation concerns these accounts. Estimating a workforce percentage would need a suitable sampling and measurement design. Attributing change to a training programme would need a credible causal comparison. Coder agreement addresses neither question by itself.

#### RMP.5:5.5 - Repeated measurements and an uncertain contrast

Eight independent specimens are each measured three times under a supplied measurement method. The 24 readings can describe within-specimen variation. Use the eight specimens as the independent experimental units and account for the repeated readings in the analysis.

Suppose the estimated contrast is 2 scale units, with an uncertainty interval from −1 to 5 scale units. Report that estimate and interval with the comparison and methodological assumptions. If the supplied equivalence rule requires the entire interval to lie within (−6, 6) scale units, it meets the rule. It fails the same rule with a margin of (−2, 2). Without an applicable margin or practical threshold, these results alone leave equivalence and practical sufficiency open.

### RMP.5:6 - Bias-Annotation

| Recurring bias | Effect on the answer | Corrective move |
| --- | --- | --- |
| Desired-conclusion bias | Supportive material determines the story while contrary material disappears. | Follow the consequential inference and retain examinations that narrow or defeat it. |
| Technique prestige | A familiar statistic, code run or interview format is treated as universal assurance. | Recover the selected Method and the claim its result can support. |
| Retrospective certainty | An exploratory choice is described as though it preceded seeing the material. | Preserve its actual timing and the claim's resulting qualification. |
| Record-volume bias | Volume is taken as assurance of inspectability or support. | Identify which material the inference depends on and whether the intended reader can use it or a qualified examination of it. |
| Closure pressure | An unresolved claim is presented as settled or used to prescribe another study. | Give the bounded answer. Consider further acquisition when it could improve the answer enough to justify the work. |

### RMP.5:7 - Conformance Checklist

Use the questions below to assess the claim under the applicable research method.

- [ ] The proposed or emerging claim and a consequential connection to actual material can be identified.
- [ ] The target, relation, scope and use distinguish the descriptive, interpretive, causal or predictive claim actually made.
- [ ] Supplied analysis is reused when its material, Method, assumptions and use remain adequate.
- [ ] The account identifies consequential analytical choices, when they were made and any departure from the plan that affects the claim.
- [ ] The analysis addresses the units, dependence, missing evidence, source relations and uncertainty on which its conclusion depends.
- [ ] The conclusion accounts for relevant contrary material and defensible alternatives, including any that leave it unchanged.
- [ ] The account distinguishes inability to inspect a record from an observed absence in a source that was examined. When absence is used as evidence against a claim, the expected recording, survival and coverage have grounds.
- [ ] The result states the supported scope of the claim, any premise defeated and the remaining uncertainty.
- [ ] The criticism account describes examinations actually made and retains the limits needed for the receiving use.
- [ ] If a premise fails, the account identifies the affected claim. Where further work needs a correction or clarification, it identifies what would supply it (§4.6).
- [ ] Proposed credibility testing has grounds in its attainable contribution and the cost of obtaining it.
- [ ] When the finding informs an action, the applicable criteria, protections, access conditions and decision authority remain identifiable.

### RMP.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Practical correction |
| --- | --- | --- |
| “The graph proves the explanation” | The observations can support a pattern while leaving its cause open. | State what the comparison establishes and the further grounds for the proposed explanation, or the limit that remains. |
| “More readings give more independent cases” | Repeated measurements can share the same underlying unit and dependence. | Recover the unit and the justified uncertainty model. |
| “The model reruns, so it is valid in the field” | Execution and model-to-world adequacy are different relations. | Preserve the computational result and examine the proposed use separately. |
| “The archive is silent, so it did not happen” | Source purpose, selection, loss or access conditions can explain a silence. | Identify which records were examined and whether the event would be expected to leave an accessible record in that set. |
| “Every qualitative analysis needs coder agreement” | The criterion can contradict the selected qualitative approach. | Use its justified account of interpretation, researcher contribution and criticism. |
| “A limitation means the whole analysis failed” | A bounded finding may answer the question. | State the supported result and identify any further question on which the receiving work depends. |

### RMP.5:9 - Consequences

A reader can use the supported descriptive or computational result while limiting an unsupported extension. Existing suitable analysis can supply the answer directly, with enough of its basis to permit the examination required.

Judging the method and inference takes professional work. When a requested conclusion cannot be established, give the reason and any narrower finding the evidence supports. A specific evidential limit can itself answer the question. A separate decision may use that answer under its own criteria.

### RMP.5:10 - Rationale

Analysis transforms or interprets material. Inference relates the analytical result to a claim. A correct calculation can therefore be used to draw an unwarranted conclusion. Examining that connection can improve the answer with the data already available.

Choose criticisms that can expose error in the particular inference. A sampling unit matters to an experimental estimate, a source’s dependence matters to historical attribution, and an investigator’s interpretation matters to a reflexive theme. Each method can be criticized on grounds appropriate to its use.

A bounded answer can complete the present work. Consider further testing when its attainable findings and cost justify a separate investigation.

### RMP.5:11 - SoTA-Echoing

How can researchers relate an analytical result to a claim and examine the inference under the method that produced it?

The 2026 [SCORE analytical-robustness study](https://www.nature.com/articles/s41586-025-09844-9) examines defensible reanalyses of the same data in social and behavioural research. The findings give grounds to identify analytical choices that affect a result. A quantitative threshold for another use needs justification in its own setting.

[Braun and Clarke's 2024 RTARG discussion](https://doi.org/10.1177/02692163241234800) and their [author guidance](https://www.thematicanalysis.net/editor-checklist/) explain how methodological coherence and the researcher’s interpretive contribution bear on reflexive thematic analysis. Apply those criteria to the approach they address.

The [American Historical Association's professional standards](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) ground careful use of sources, inspectable interpretation and engagement with contrary evidence. They support distinguishing what an inspected record establishes from an inference about events on which the surviving archive is silent.

The [National Academies' 2019 account](https://doi.org/10.17226/25303) distinguishes computational reproducibility from replicability with new data. A successful rerun supports a claim about the computation under the conditions tested. A claim about transfer to the field needs evidence for that use.

Reconsider an analytical conclusion if new methodological evidence, changed material or a new intended use affects its grounds. Obtain a disciplinary measurement rule, causal evidence or permission from the source that supplies that particular contribution when needed.

### RMP.5:12 - Relations

- Use **RMP.3** to examine or develop operational choices when their relation to the research question needs work. A suitable existing protocol can supply those choices.
- Use **RMP.4** when conduct, transformations, loss or access need to be documented or recovered. Inspectable material permits an examination. Whether the claim follows depends on that examination and its findings.
- Use a compatible question and design already available, or **RMP.1** and **RMP.2** where the question changes or the selected design needs reconsideration.
- Use **RMP.6** when a remaining credibility question warrants comparing available responses. A new test requires a useful attainable result and a feasible arrangement.
- Use **FPF F.1** to find or select a source, **F.0.1** to recover a source-local meaning that matters, and **A.10** when the evidence for a claim or its provenance needs clarification or reproducible tracing. Use an adequate source result directly.
- Apply the disciplinary methods and criteria relevant to the inference. Use existing access and protection conditions. An action or change in those conditions needs the corresponding authority.

- A bounded RMP.5 answer may finish the inquiry. Use **RMP.7** if that answer is needed for a compatible corpus synthesis, or **RMP.8** when revisiting a broader claim or returning a change to its receiving use.

### RMP.5:End


## RMP.6 - Choose a Credibility Test That Bears on the Research Claim, or Answer without New Testing

> **Status:** Stable

> **Type:** Research Method Practice practitioner method pattern

### RMP.6:1 - Problem Frame

Use this pattern to assess which credibility examination bears on a research claim, whether a new examination is worth obtaining, or what an existing test establishes. Identify the claim, its current basis, the intended use and the particular uncertainty. Use an existing RMP.5 result or another source that supplies those inputs.

Ask what each possible result would establish. A successful rerun can establish computational reproducibility under its conditions. A question about field degradation also needs evidence relating the model to the field. Another interview may deepen an interpretation. Estimating the prevalence of that interpretation requires a suitable population basis.

A **CredibilityTestDecision** may use a qualified existing result, select a worthwhile new examination, close with a qualified answer or identify the input still needed to choose. The current research account can carry the conclusion. To rely on a test as performed, establish what was done and what it found.

Return the claim with the support the available evidence warrants. Leave a remaining uncertainty explicit when further testing is unavailable or its expected contribution does not justify the burden.

For routine execution of a qualified engineering or assurance test, use its domain method and criteria. RMP.6 addresses what such a test can establish about the research claim. Obtain any outstanding criteria, protection, permissions, funding or authority from the practice or holder responsible for that contribution when the task requires it.

### RMP.6:2 - Problem

“Repeat it,” “validate it” and “triangulate it” can name useful work or an expensive mismatch. The proposed test may target the implementation while the real concern is transfer, use copies of the same source as though they were independent, or reproduce a significance label without stating what agreement means.

Interpret the outcome of the examination. Lack of access can prevent a computation. An inconclusive replication can leave the effect open. A different result can reflect an error, changed population, changed method or another condition. Agreement may support a bounded claim while leaving a stronger interpretation unsettled.

Choose an examination by what its result can establish and whether the complete work of obtaining and interpreting it is feasible and worthwhile. A sufficient existing finding can close the question.

### RMP.6:3 - Forces

| Force | Tension |
| --- | --- |
| Relevant challenge | Repetition is recognizable, while the consequential threat may concern another relation entirely. |
| Comparability | A new examination needs a meaningful comparison, while changed materials, context or Methods may change the claim being tested. |
| Evidence and resources | Stronger support can be valuable, while preparation, access, interpretation and displaced work can dominate the benefit. |
| Existing results | A qualified prior examination can finish the question, while a changed premise or receiving use may limit its reuse. |
| Shared resources | Individual tests can be feasible while their combined programme is not. |
| Protection and authority | The merits of a requirement can be disputed while its current terms continue to govern conduct. Changing it requires the applicable authority. |
| Honest return | A receiver needs an answer, while a selected or attempted test may leave the claim unresolved. |

### RMP.6:4 - Solution

Identify the claim, the uncertainty and the question the answer must serve. Use an adequate existing examination. If further testing is at issue, compare its attainable contributions and costs, including the option to conclude with the present evidence. Report separately the decision to obtain a test, its performance and its result when those events occur.

#### RMP.6:4.1 - Name what could fail and what would change

Identify the claim and scope, the analysis or sources supporting it, the intended use and any consequential uncertainty. Use the relevant RMP.5 result or other suitable inputs already available.

Examples of questions that distinguish possible credibility contributions include the following.

- Is the reported computation obtainable from the identified data and analysis?
- Does a plausible analytical choice change the substantive interpretation?
- Does new corresponding material support the target relation?
- Does the model or measure have support for this intended use?
- Do apparently corroborating accounts have independent evidential contributions?
- Which difference between the original and receiving context can change the relation?

Select the question whose answer could affect the claim, its support or its use. Distinguish a possible threat from evidence that it has occurred. Whether to investigate it also depends on what can be learned and at what cost.

Use the method and criteria that make the proposed result interpretable. If a missing domain criterion, source relation or suitable comparison could change the selection, identify that gap. The success criterion needs subject or decision grounds independent of the outcome the investigator hopes to see.

#### RMP.6:4.2 - Reuse the examination that already answers

Use an existing examination whose material, method, criterion, assumptions and scope answer the present question. If a premise or receiving use changes, assess the affected part. Repeat or extend a test when the question remains consequential and the additional examination can justify its cost.

Check the dates and scope that matter to the particular examination. A record may establish when calibration, permission or a criterion expires. An earlier result whose relevant conditions still hold can remain usable.

When the existing basis answers the question, return that answer with the qualification needed to use it.

#### RMP.6:4.3 - Match the credibility move to the threat

| Examination | Comparison | Scope of the result |
| --- | --- | --- |
| Computational reproduction | Compare a computed output with the reported result using the identified data, analysis, relevant environment and justified tolerance. | Agreement supports reproducibility under the conditions tested. Claims about field adequacy, causation or transfer need their own evidence. If access or execution fails, no comparable output has been obtained. |
| New-data replication | Compare estimates for the target claim using new material and a corresponding design. Specify what was held comparable, what changed and the agreement criterion. | Use magnitude, uncertainty and the applicable criterion to assess the result. Agreement or disagreement between significance labels alone leaves equivalence and cause open. |
| Robustness or sensitivity | Examine plausible analytical choices, parameters, missingness or model assumptions under the declared question. | State what changed over the examined range. A different target quantity calls for a separate claim and comparison. |
| Validation for a use | Examine the empirical and conceptual relation between the model, measure or result and its intended use under supplied domain criteria. | Fitting to calibration material or checking implementation does not by itself establish adequacy for the intended use. Use challenging material separate from fitting where the claim requires it. |
| Triangulation or corroboration | Compare what different methods or sources establish, how their limitations are related and what agreement or disagreement would mean. | Copies may trace to one account. A discrepancy can reveal a serious difference in target or method that a single average would conceal. |
| Transfer examination | Identify differences in populations, settings, periods, materials or practices that affect the claimed relation. | Limit the transferred claim to conditions for which the relation has adequate grounds. |

Use the meaning and criterion of the examination in the relevant discipline. Select one or combine several when the question needs their distinct contributions and their results can be related meaningfully.

Match the test to the uncertainty. A simulation rerun can answer a computational question while leaving a mechanism-to-field relation open. Judge a reflexive interpretation by its grounding in the material. To establish historical chronology, examine the dates, origins and dependence of surviving sources.

#### RMP.6:4.4 - Compare contribution with the whole obtainable burden

Compare the attainable options, including adequate prior results and returning the present qualified answer. A single targeted examination can be sufficient.

For each serious option, identify what the attainable evidence could distinguish, what different results would imply, and what would remain open. Estimate the work of obtaining and interpreting it, including whichever of the following it requires.

- access to sources, participants, specimens, data and code;
- qualified personnel, instruments, preparation and computation;
- actual performance, interpretation and any independent examination required for the proposed use;
- participant effort, protection, legitimate restrictions and permissions;
- timing, delay, shared capacity, necessary records and displaced work.

Use the precision the choice requires. A qualitative comparison or supplied bound can settle it. Probabilities, costs and credibility scores need suitable grounds when they affect the choice. Include the contribution to knowledge, later inquiry and other receiving questions where relevant.

Check joint feasibility when tests draw on shared capacity. If each of two examinations can require four to six non-overlapping investigator-days and six plus six is possible, ten days do not assure both. State that result. For a requested plan, compare a sufficient subset, a different arrangement or ending with the present evidence. A shorter plan still needs a worthwhile contribution.

#### RMP.6:4.5 - Return the current decision and specify only selected work

Give the result warranted by the question and the available facts.

| Present condition | Result |
| --- | --- |
| An adequate existing examination answers the selected credibility question | Return that answer, its basis and the qualification needed for use. |
| An additional examination has a relevant contribution and a worthwhile feasible arrangement | For a proposal, identify the comparison, required inputs, criterion, possible results and remaining limits. Select or commission the examination within the applicable authority when that is the task. |
| The question can finish without additional testing | Return the supported claim, qualified or adverse finding, or precise uncertainty. Include the limit that matters to the recipient. |
| A missing input prevents this selection | Identify the input, the affected choice and what would permit reconsideration. Give its source if known. |

Use the existing research account or give the conclusion directly. An unknown can remain a limitation of a completed answer. Leave a selection open when the missing input prevents that particular decision.

Before undertaking selected new work, specify the target claim, material, design correspondence, method, criterion or tolerance, interpretation-changing differences and practical arrangements, including when to stop. Use RMP.2 or RMP.3 if the design or its operational choices need development. Preserve evidence of actual performance and deviations when the examination is conducted, using RMP.4 where needed.

A test selection or authorization can establish a plan. Report a performed test and a favorable or adverse result from evidence of the work and its findings.

#### RMP.6:4.6 - Interpret an actual return without changing its kind

To interpret a completed or attempted examination, identify what was done, how it relates to the intended claim and criterion, and the effects of any deviations. Qualify deviations by their evidence and justification.

| Actual return | Interpretation and continuation |
| --- | --- |
| The comparison was completed and supports the target relation under its criterion | State that bounded support and the limits left outside the comparison. |
| A completed comparison yields a consequential discrepancy | Confirm the target and assess whether the discrepancy reflects changed material, method, execution, context or a defect in the claim. State the result, leaving the cause open if the evidence does not distinguish it. |
| A completed comparison is inconclusive | Identify what remains unresolved and what the observations still support. |
| Access, execution or interpretation failed | Report what could not be obtained and why. Distinguish an absent output from a computed difference outside the comparison tolerance. |

For a replication, preserve the estimate, uncertainty, design correspondence and success criterion. Identify and justify a change of criterion, including when it was made. Apply agreement or discrepancy to the particular claim and scope for which the comparison provides evidence.

Return the credibility finding directly when it answers the question. For further work, use RMP.5 to reconsider the affected claim, RMP.2 for a defeated design premise, RMP.3 for an operational mismatch, or RMP.4 for a needed connection to the original work. Frame a materially different research question on its own grounds.

#### RMP.6:4.7 - When a protective requirement itself is disputed

If the necessity or proportionality of a record, independent check, evidence threshold or participation condition is disputed, consider two questions. What protection does it provide at what cost, and who can change the requirement under the applicable rules?

Identify what is protected, the unwanted outcome, the baseline and the time horizon. Compare the expected incremental protection, uncertainty, burden and any protective work displaced by the requirement. Where a change is under consideration, compare the practical options for retaining, revising, replacing or removing it. A label or cost estimate alone cannot establish the protection it provides.

Use research evidence for the causal, measurement and evidential questions. Apply the responsible practice’s protection duties, value criteria and authority to any amendment. A binding requirement governs conduct until it expires under its terms or a competent authority changes it.

#### RMP.6:4.8 - Preserve a useful answer for its receiver

Return the claim, the credibility question and the supported answer. Include the source, reason or limit needed for its intended use. An adequate existing research account or test report can carry the result.

When access is restricted, identify what the public material establishes, what the permitted critic could examine and what other recipients can use from a qualified inspection. A lost record or unperformed test limits the specific conclusions that depend on it.

### RMP.6:5 - Archetypal Grounding

These examples use stipulated data, tests and conditions.

#### RMP.6:5.1 - From a reproduced model to a relevant field comparison

A run of the Pump-P4 model with its identified data and code reproduces the reported accelerated-degradation curve. The computation is supported under those conditions. Its relevance to a longer field maintenance interval remains open. What would a further rerun establish about that use?

Another run with the same data and implementation could test repetition of the calculation. It would add no evidence about the missing relation between the accelerated and field mechanisms. Return the supported model result and state the field-use uncertainty if no worthwhile relevant examination is obtainable.

Now suppose a qualified independent field dataset becomes accessible in time and can distinguish the proposed degradation mechanisms. Assess a comparison under suitable domain criteria. If the whole comparison is feasible and its expected contribution warrants its cost, specify how it relates to the field use and how support, discrepancy or inconclusiveness would affect that use. A decision to obtain the comparison is prospective. The performed comparison supplies its finding. The maintenance interval remains a decision for the applicable authority.

#### RMP.6:5.2 - A blocked reproduction is not a contrary result

An analyst receives a published model claim and code, but the data needed to execute its reported analysis are not accessible under the available rights. The analyst cannot obtain the target computation.

The analyst can report the access restriction and what the code or description establishes. There is no computed output to compare and hence no observed discrepancy. If permitted access becomes available, reassess the need, feasibility and cost of reproduction. Perform a selected reproduction under its stated criterion when authorized to do so.

If a later run produces a different value, compare the target, inputs, environment and justified tolerance before judging the discrepancy and its implications for the reported claim.

#### RMP.6:5.3 - Historical corroboration and a qualitative receiving change

The directive’s date is established. In this case the earlier series is inaccessible and the available sources leave earlier practice unresolved. Three copies of one account add no independent evidence of earlier practice. Their shared origin can itself be established. The question can end with the remaining uncertainty.

If an authenticated earlier ledger becomes accessible, examine what it records when that would answer the chronology question. A qualified finding that the practice preceded the directive defeats the proposed sequence. The cause of the earlier practice and the directive’s effect on later adoption require different evidence.

A recipient asks whether most workers share a theme identified in a reflexive analysis of interviews. That is a new prevalence question. Agreement among coders would not supply a population basis. Give the warranted interpretation and identify the sampling and measurement the stronger claim needs. If the question concerns a discordant account that the interpretation may have omitted, examine that material under the selected qualitative approach.

#### RMP.6:5.4 - Two useful examinations and ten days

A research team has ten available investigator-days. Each of two proposed examinations needs four to six days of non-overlapping effort from that team. The conditions allow both to require six days in the same programme.

The arrangements 6 + 4 and 4 + 6 each fit ten days. The admissible 6 + 6 takes twelve. The pair is therefore not assured within ten days. If a programme is needed, consider a sufficient single examination, a changed arrangement or ending with the existing uncertainty.

A provider then supplies a qualified shared-preparation arrangement that bounds the combined effort by eight days and preserves both comparisons. The pair now fits ten days. To choose whether to undertake it, also consider the attainable credibility results, remaining limits and the work those eight days would displace.

#### RMP.6:5.5 - Two different merits answers, one authority boundary

A research protocol requires an additional independent check of a consequential record transformation. Its marginal protection is questioned.

In the first case, examination records show that the additional check detects a transformation error missed by the baseline controls. The error can change a protected exposure classification. The check fits the available window and displaces no more protective work. These findings support retaining the protection or an alternative that preserves it.

In the second case, the proposed check repeats the same source and procedure. The records show no additional ability to detect the protected failure under these conditions, and the extra check displaces an examination that can expose a consequential error. The comparison supports revising or replacing the requirement under the stated premises.

Report the evidence, uncertainty, burden and protection that led to each recommendation. The requirement continues to govern while it remains in force. A participant authorized to amend it can make the decision within that authority. Others seeking an amendment must obtain the appropriate decision.

### RMP.6:6 - Bias-Annotation

| Recurring bias | Likely drift | Corrective move |
| --- | --- | --- |
| Repetition bias | Any repeat is treated as a stronger test of the substantive claim. | Name the precise relation being challenged and the result that could change it. |
| Favorable-outcome bias | Criteria or tested variants are selected after seeing agreement. | Preserve the intended criterion, justified changes and unexamined range. |
| Counting methods | Each method or source is counted as independent support. | Identify the contribution and dependence of each, and what any disagreement would mean. |
| Acquisition bias | Every remaining uncertainty is treated as grounds for another study. | Compare what an attainable examination could add with its full cost. A bounded answer can finish the task. |
| Authority shortcut | A requirement is defended by its label or bypassed because it is costly. | Examine protection merits separately from the competent decision and current force. |

### RMP.6:7 - Conformance Checklist

Assess the credibility question, the decision if one was requested, and any actual test result under the conditions that apply.

- [ ] The account identifies the bounded claim, its current basis and the use or credibility question at issue. For a proposed new test, it identifies the uncertainty that test would examine.
- [ ] The selected question identifies a possible result that would matter to the support, interpretation or use of the claim.
- [ ] An adequate existing examination is used within its scope.
- [ ] Reproduction, replication, robustness, validation, corroboration and transfer retain their different comparisons and limits.
- [ ] The Method, relevant correspondence and criterion make the selected examination interpretable.
- [ ] For a requested choice, the comparison covers the realistic options and the criteria material to that choice.
- [ ] For proposed testing, its attainable contribution is weighed against the whole cost, including shared resources, necessary protection and displaced work.
- [ ] A no-new-test answer preserves insufficient evidence or uncertainty where it remains.
- [ ] A missing input is tied to the selection or conclusion that depends on it. Further acquisition is considered where the task requires it.
- [ ] The test decision, specification, actual performance and returned result remain distinct.
- [ ] The result distinguishes agreement, discrepancy, inconclusiveness and inability to obtain or interpret the comparison.
- [ ] A conclusion on the merits of a disputed requirement addresses its protected function and burden. Any decision to change it has the applicable authority.
- [ ] The receiving answer states the conclusion, conditions that affect its use and any consequential unresolved question.

### RMP.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Practical correction |
| --- | --- | --- |
| “The rerun validates the model” | Reproducing the computation can leave its intended field use open. | Use relevant independent grounds for the field relation, or report the limit if no adequate assessment is available. |
| “The replication was not significant, so the effect is absent” | The label omits magnitude, uncertainty and the chosen comparison. | Interpret the actual result under its design and criterion. |
| “Many copies corroborate the source” | Repeated carriers can preserve one dependent account. | Examine origin, dependence and the distinct evidential contribution. |
| “No data access means the claim failed” | An unattemptable comparison supplies no contrary output. | Return the access limit and the exact examination still unavailable. |
| “Each test fits, so the programme fits” | Combined demands on shared capacity may exceed what is available. | Check admissible joint combinations. Report the feasible or infeasible range, and select a useful set when a plan is requested. |
| “We selected the test, so credibility increased” | Selection establishes a plan. | Report what already supports the claim and identify the further evidence that would alter it. |
| “It is required, therefore it protects” | A binding rule can supply a duty while leaving its marginal protection unexamined. | Assess the protection where that is the question. Any change requires the applicable amendment authority. |

### RMP.6:9 - Consequences

An existing test can answer the stated credibility question. When relevant new evidence becomes obtainable, its expected contribution and cost may justify further work. An access failure can explain an incomplete examination, and an observed discrepancy can change the support for a particular claim.

Assessing credibility requires subject judgement about comparisons and criteria, and making a test feasible may consume scarce resources. If evidence is unavailable, identify which conclusion remains unsupported. An applicable protective requirement still governs conduct.

### RMP.6:10 - Rationale

A test is informative when its possible findings bear on the claim. One targeted comparison can resolve a question that several repetitions of an unrelated computation would leave open.

Assess separately what the available evidence supports and whether it is worthwhile to obtain more. A research plan can be justified while its result is still unknown.

For a protective requirement, consider its purpose, empirical effects, costs and current authority. Evidence of a costly procedure can bear on its merits. Changing that procedure also requires the applicable decision.

### RMP.6:11 - SoTA-Echoing

Which examination could change the support for the claim or clarify its limits, under which criterion and at what cost?

[National Academies' 2019 synthesis](https://doi.org/10.17226/25303) distinguishes repeating a computation on the same data from examining a claim with new data. Select the comparison that bears on the question.

The 2026 SCORE [reproducibility study](https://www.nature.com/articles/s41586-026-10203-5) distinguishes data availability from computational reproduction. The [replicability study](https://www.nature.com/articles/s41586-025-10078-y) examines how the criterion for success affects replication findings. The [analytical-robustness study](https://www.nature.com/articles/s41586-025-09844-9) considers defensible alternative analyses. Their results concern the sampled fields, comparisons and tolerances in social and behavioural research.

[Braun and Clarke's qualitative guidance](https://www.thematicanalysis.net/editor-checklist/) and their [2024 RTARG account](https://doi.org/10.1177/02692163241234800) explain methodological coherence in reflexive thematic analysis. The [American Historical Association's standards](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) guide criticism of sources and their integrity in historical inquiry. Apply each kind of examination to the claims it can assess.

[2021 MRC framework](https://www.bmj.com/content/374/bmj.n2061) relates perspective, context and resource consequences to the question in complex-intervention research. RMP.6 uses that contribution when comparing attainable examinations in context.

Reconsider a comparison when a new method, source, criterion, practical arrangement or proposed use changes what the test can establish or whether it is worth obtaining.

### RMP.6:12 - Relations

- Use **RMP.5** if the claim or the criticism it needs remains unclear, or if the test changes what that claim can support. Existing qualified inputs can be used directly.
- Use **RMP.2** when developing or reconsidering a research design is necessary. A justified finding that no new study is needed can finish the question.
- Use **RMP.3** when an examination needs an operational specification and **RMP.4** when the course of actual work or the material retained needs to be documented or recovered. An adequate protocol or trace can be used directly.
- Use an adequate ordinary-practice or source answer directly. **RMP.1** helps when a materially changed question needs framing or it remains unclear which practice or source could answer it.
- Use **FPF A.10** when the evidence for a claim needs clarification or reproducible tracing. Use **A.10.1** when a material change in a source or claim that earlier uses relied on calls for finding affected uses or revalidating several together. Use **C.11.DUA** to judge what new evidence could add at its full cost and **A.15.9** when obtaining a bounded contribution from another practice.
- Use applicable disciplinary methods, criteria, protections and permissions. For an action or amendment, apply the decision rules and authority of the receiving practice.

- A completed credibility examination can inform a compatible corpus appraisal under **RMP.7** or a claim or model revision under **RMP.8**. Use those results when the receiving work needs them. A bounded credibility answer can also finish the inquiry.

### RMP.6:End

# Part IV - Synthesize Evidence and Revise the Exact Contribution


## RMP.7 - Synthesize a Research Evidence Corpus

> **Status:** Stable

> **Type:** Research Method Practice practitioner method pattern

### RMP.7:1 - Problem Frame

Use this pattern to work out what several research reports or interpretations establish together, or what an existing synthesis already answers. State the question and identify the material the answer covers. Reuse a synthesis that answers it under the conditions at issue.

Four reports can cover two independent tests and material about a different outcome. Several histories can repeat one memoir. Studies can also appear to disagree because their questions or settings differ. Identify these relations before treating agreement or disagreement as evidence for the same claim.

The resulting **EvidenceSynthesis** states what the corpus warrants, how its sources contribute to that answer and which limits matter to criticism or reuse. A short answer citing an existing review may suffice. A new analysis may need a study map, a comparison or a calculation.

Start from the question, synthesis design, operations and record adequate for this use. They may come from RMP.1–RMP.4 or from work already available. When historical or qualitative material warrants refining the question, explain what changed and which evidence and criticism apply to the revised question.

When finding or comparing sources answers the question, use that result. RMP.5 examines an inference from particular material. Use RMP.7 when the question depends on how a corpus was appraised or its contributions combined. If a needed method, source or question is missing, say which conclusion this prevents. When that conclusion is still required, obtain the missing contribution from a suitable source where possible.

### RMP.7:2 - Problem

Several accounts can look like independent corroboration even when they draw on one study. A corpus may contain only favorable results. A pooled number can conceal different target quantities, and a common theme can conceal a consequential difference in setting or meaning.

Disagreement or incomplete coverage may still permit a numerical comparison, an interpretation or a precise conclusion about what the corpus cannot establish. If a previous review already answers the question, giving that review a new date adds no evidential support. A newly obtained observation may add support of its own.

Choose the form of the answer from the research question, the relations among the sources and the criticism that affects the conclusion.

### RMP.7:3 - Forces

| Force | Tension |
| --- | --- |
| Joint support | Distinct contributions can strengthen an inference. Several reports of one result can add detail while counting as one study. |
| A concise answer | A synthesis reduces reading effort, but an aggregate can hide a contrast needed to interpret the finding. |
| Different traditions | Quantitative, interpretive and historical inquiries can inform one question, while their transformations and confidence claims differ. |
| Coverage | Relevant omissions can change a finding, while a complete search may exceed what a bounded question needs or what access permits. |
| Reuse and change | An existing synthesis can supply the answer. A change to a source, the question or the intended use can affect the conclusion or its scope. |
| Completion | A qualified answer may settle the corpus question. Commissioning a further inquiry depends on what it could add and what it would cost. |

### RMP.7:4 - Solution

Start with the question and the material available. Establish what each distinct contribution supports and how it depends on other sources. Use the synthesis the question and material warrant. Give the answer, the transformations that affect it, its uncertainty and its scope.

#### RMP.7:4.1 - State the question and test the supplied answer

Specify the subject, the context and period that matter, and the conclusion sought. A mean difference needs a contrast. An account of participants’ experiences, a historical sequence and an explanation each ask for different evidence, even about the same subject.

For a supplied synthesis, check its question, coverage, method, findings and limits against the present use. Return its applicable findings with their source and qualifications. If a different population, changed premise or uncovered question matters to the task, reconsider the affected part or identify the limit.

If further synthesis is needed, establish what met the inclusion criteria, what was sought and obtained, and what was excluded or unavailable. Explain how this affects the answer. A claim of systematic coverage needs evidence of the relevant search and selection. A specified set of documents may be sufficient for a question about that set.

When further work requires a missing contribution, use RMP.1 for a changed question, RMP.2 for the synthesis design, RMP.3 for the operations and RMP.4 for what material was obtained or can be examined. Use adequate available inputs directly.

#### RMP.7:4.2 - Recover distinct contributions before counting support

Identify reports, the underlying studies and material, the authors’ interpretations and the finding you propose to draw across sources. One report can contain several studies, and one study can generate several reports.

| Source relation | Consequence for synthesis |
| --- | --- |
| Several reports concern one study | Use details and follow-up information from the reports, and resolve discrepancies where possible. Count this study once when estimating independent study contributions. |
| One report contains several studies | Identify the studies and establish whether their samples, controls or data are independent for the inference in question. |
| Samples, controls, records or data overlap | Account for the overlap in the analysis, group the contributions, or justify selecting among them. Establish independence from the underlying material. |
| Later accounts copy or interpret one earlier source | Identify their shared source and the interpretations each adds. Evidence of copying can establish transmission. Independent corroboration of the reported event needs evidence independent of that source. |
| A source adds context or a different outcome | Use it for the question it answers. Include it in an estimate of the target quantity only when its data support that estimate. |

Preserve contrary findings and disagreements between reports. If dependence remains uncertain, explain which combinations or narrower comparisons it permits and which conclusions it prevents.

#### RMP.7:4.3 - Appraise support for the proposed findings

Apply the appraisal criteria for the research approach and the finding. Consider limitations within a study, dependence across contributions, which results became available and whether the evidence applies to the question. Explain which findings each condition affects.

For consequential omissions, distinguish material never sought, an eligible result left unreported, a lost record and a source you cannot access. State which conclusion the gap limits. To infer absence of an event, effect or experience, establish how the available evidence bears on that absence.

Additional publications give no independent replication when they rely on the same observations. Appraise the connection between each source and the inference. Material too weak for one conclusion can still provide context or challenge a proposed interpretation.

Use RMP.5 when an individual inference needs reconsideration. RMP.6 can help interpret a credibility examination already performed or decide whether a further examination could improve the synthesis enough to justify its cost. For an empirical test result, establish what the test found.

#### RMP.7:4.4 - Perform the synthesis the question permits

Use a disciplinary method appropriate to the question. Explain any grouping, transformation, weighting or translation on which the finding depends so a reader can trace the contribution of the sources.

| Question and material | Positive move | What the result may claim |
| --- | --- | --- |
| Compatible quantitative estimates | Establish the target quantity, units, contrast, timing, dependence and uncertainty. Fit the justified statistical model and examine influential assumptions. | An estimate for that target with its warranted uncertainty and scope. A common-effect and a distributional-effect analysis have different assumptions and interpretations. |
| Quantitative findings without a justified common aggregate | Group and tabulate the relevant results and compare what the evidence permits. Identify the missing relation when it prevents a requested aggregate. | A narrower quantitative comparison or the conclusion that the corpus cannot establish the pooled magnitude. Significance counts do not estimate that magnitude. |
| Qualitative or interpretive findings | Compare, translate or develop interpretations under the selected tradition, retaining context, source concepts, disconfirming material and the synthesist's contribution. | A descriptive synthesis or explicitly developed explanatory construct with its grounding and applicable confidence account. |
| Historical sources and accounts | Examine provenance, dates, purposes, perspectives, dependence, gaps and rival interpretations that bear on the chronology or explanation. | The sequence or explanation the sources warrant, with any consequential alternatives still open. |
| Mixed evidence about one question | If a transformation makes the contributions comparable for this question, justify it. Keep the original values, meanings and context needed to examine what the transformation loses. | An integrated answer within the scope of the justified transformation. |
| Mixed evidence about different aspects | Synthesize the aspects on their own terms. Where the question requires their relation, compare the syntheses or use one finding to guide examination of the other. | An account of how the findings agree, complement one another or diverge, including any unresolved difference. |

Variation among studies can be compatible with a pooled estimate under a justified model. A random-effects model still needs a defensible relationship among the target quantities. A synthesis of effect directions alone does not estimate their magnitude.

For a qualitative synthesis, identify what the participants reported, how the source authors interpreted it and what interpretation the synthesis adds. When GRADE-CERQual fits, assess confidence in each finding from methodological limitations, coherence, adequacy and relevance. The resulting confidence judgement is qualitative and specific to that finding and approach.

If a required method or decisive premise is unavailable, identify the conclusion that this prevents and give any answer the available material supports.

#### RMP.7:4.5 - Return the useful corpus answer

Give the answer to the corpus question first. Identify the material and method used, source dependencies, transformations, uncertainty, omissions and transfer limits insofar as they affect interpretation.

Use existing notes, analysis output or a concise linked explanation when they suffice. Provide the evidence needed for the intended criticism within the applicable access conditions. If a qualified inspection of restricted material has established a finding, identify what others can conclude from it and what they can inspect for themselves.

Return the adequate existing synthesis, the new finding, a qualified answer, or the reason the requested result cannot be established. Identify a missing input if obtaining it matters to the work. A broader question may remain open. Select further inquiry only when the attainable contribution justifies the effort, cost and delay.

Use RMP.8 when reconciling the answer with a wider claim or model, or when its return to a receiving practice needs further judgement about reliance. Return an adequate corpus answer directly.

### RMP.7:5 - Archetypal Grounding

These examples use constructed studies and records.

#### RMP.7:5.1 - Two compatible tests among four reports

A seal engineer receives four reports. A and A2 describe one randomized accelerated test. A2 provides fuller outcome information. B reports an independent test of the same materials under compatible stress and measurement conditions. C describes in-service replacement decisions under different conditions.

The engineer wants the difference in mean time to a defined laboratory failure between the new seal and its comparator under specified accelerated conditions. Suppose all lifetimes were observed, the study estimates are approximately normal and independent, and a common underlying effect is justified for these conditions. A2 informs the first study estimate. C does not measure this laboratory contrast.

The two estimates are 14 hours for A/A2 (standard error 4 hours) and 8 hours for B (standard error 3 hours). The inverse-variance weights are 1/16 and 1/9. The weighted estimate is 10.16 hours, with a standard error of 2.4 hours and an approximate normal 95% interval from 5.46 to 14.86 hours.

Under the stated assumptions, the new seals have a longer estimated mean time to laboratory failure. Report the two study estimates as well as their combined estimate. Transfer to service and a change in the maintenance interval need separate grounds. C can inform a question about service use. If the common-effect premise fails, reconsider the interpretation of the combined estimate even when the arithmetic holds.

#### RMP.7:5.2 - A refusal with useful content

Another supplied corpus reports leakage after one hour, failure time under another stress and technicians' replacement decisions. The requested answer is a common percentage reduction in 500-hour failure risk.

Report the observed leakage, failure time and replacement choices with their contrasts, conditions and uncertainty. The supplied material gives no way to convert them to a common 500-hour failure risk. It supports the individual comparisons, but does not establish the requested percentage or show an absence of effect. This answers the question about what this corpus can establish.

#### RMP.7:5.3 - Situated participation and a mixed question

A resident group asks what impedes participation in water monitoring. One interview study links distrust to withheld feedback. Another interpretive study relates continued participation to community authority over the question. A survey reports stated reasons within its own sampled group.

For a mixed synthesis addressing this question, preserve the survey counts and denominator, the interview contexts and the authors’ interpretations. The synthesist proposes that control over the question and the information returned may both matter. The account supplies no population prevalence for that explanation. Continued participation in one case despite withheld feedback qualifies the proposed connection.

To estimate the intervention’s effect on water quality, use studies that measure that effect. If the question also concerns how participation relates to water quality, synthesize each kind of evidence appropriately and examine the connection.

#### RMP.7:5.4 - Shared memoir and contrary chronology

Several histories attribute a factory’s decision to close to a public protest. They cite one retrospective memoir. An authenticated record dates the decision before the protest.

The histories share a source, though their interpretations may differ. The dated record rules out the later protest as the cause of the earlier decision. The decision’s cause and the protest’s possible effect on implementation remain open. The historian can finish the chronology without counting the histories as independent corroboration.

### RMP.7:6 - Bias-Annotation

In the seal example the target quantities are compatible, independence is established and the common-effect premise is supplied. Other corpora may require domain expertise, further source recovery or a narrower answer. Historical chronology and accounts of participation illustrate different appraisal criteria.

Publication and access can favor certain institutions, languages and surviving sources. Interpret the coverage and silences of a corpus in that setting. Reuse a convenient synthesis to the extent that its question and qualifications apply.

### RMP.7:7 - Conformance Checklist

When examining a synthesis, check the following.

- Can the reader identify the question and determine what the existing work already answers or leaves open?
- Can the reader distinguish reports, underlying studies and material, source interpretations and synthesis findings, and identify dependence that affects the answer?
- Do inclusion criteria, exclusions, omissions and access conditions justify the stated scope of the corpus?
- Are the method and interpretation of each consequential transformation appropriate to the question it serves?
- Does each affected finding account for contrary evidence, uncertainty and limits on transfer?
- Does the answer give what the available material establishes, including a specific limit when it cannot support the requested finding? Is any proposed further work distinguished from evidence already obtained?

Use the evidence for the findings and source relationships to judge whether the synthesis answers its question.

### RMP.7:8 - Common Anti-Patterns and How to Avoid Them

| Failure | What changes in practice |
| --- | --- |
| Reports are counted as independent studies. | Identify the underlying material, account for dependence and retain any supplementary information. |
| Numerical results are pooled without a common target. | Establish their targets and any justified transformation. Give the narrower comparison or the specific limit if a common magnitude cannot be estimated. |
| Agreement is judged by counting significant results. | Compare the relevant estimates or other findings under a justified method, including uncertainty and missing evidence. |
| A theme is reported as a population percentage. | Preserve its interpretive basis. A prevalence estimate needs appropriate sampling and measurement. |
| A single confidence label is applied to every finding. | Appraise each finding under criteria suited to the research approach and the question. |
| Disagreement leads the reviewer to discard the corpus. | Give the distinctions the sources support or explain precisely which conclusion they cannot establish and why. |

### RMP.7:9 - Consequences

The resulting answer preserves the differences between sources that matter to the question. Compatible findings may strengthen an estimate. A dependent report may add follow-up detail, and a result about another outcome may help explain the scope of the comparison.

Appraisal and transformations take work. Reusing adequate earlier syntheses and documenting the decisions that affect interpretation can reduce that cost. The strength of the evidence still depends on what the sources establish.

### RMP.7:10 - Rationale

A synthesis draws an inference about how several contributions relate. Its design and criticism must support that inference. Use an established individual finding directly when it answers the question. Use RMP.5 when the inference from particular material still needs examination.

A finding that the requested conclusion is unsupported can settle the inquiry when it identifies the missing relation and shows what, if anything, the material does establish.

### RMP.7:11 - SoTA-Echoing

**What counts as independent support?** Cochrane [chapter 5](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-05) explains how to identify several reports of one study and combine the information they contribute. Counting repeat reports as additional studies inflates the number of independent studies. One report can also describe several studies. Discarding all repeated reports can lose follow-up observations. Section 4.2 preserves A2’s fuller outcomes in §5.1 and counts A/A2 as one study. Recover underlying relationships where they could change an inference. New evidence of overlap, provenance or additional outcomes can change it.

**Which numerical answer can this corpus support?** Cochrane [chapter 10](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10) guides combination for a defined quantity under an appropriate dependence model. [chapter 12](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-12) describes synthesis without meta-analysis. Sections 4.4 and 5.1–5.2 use the target and model to distinguish a justified combined estimate from a narrower comparison. Pooling all numerical results assumes they measure compatible quantities. Refusing every heterogeneous comparison would discard some useful estimates. Choosing groups and models takes judgement. Reconsider those choices if the target, dependence or a defensible alternative model changes. These chapters address intervention reviews.

**How should missing contributions affect a finding?** Cochrane [chapter 13](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-13) examines missing evidence in a synthesis and its potential effect on a finding. Its meta-analysis tools have that scope. Sections 4.1 and 4.3 distinguish material unavailable, unreported, never sought or lost. Assuming completeness can conceal selective reporting. Rejecting every incomplete corpus would also discard answers supported within a narrower scope. Reconsider the affected finding when new material, a selective omission or evidence of its effect becomes known.

**How can situated and mixed findings be related?** For a review of intervention effectiveness, [Harden and colleagues (2018)](https://discovery.ucl.ac.uk/id/eprint/10040031/) recommend synthesizing qualitative and quantitative evidence separately before integration. The archived [Cochrane Handbook v6.0, §21.13](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/archive/v6.0) gives that recommendation in its original setting. In [Sutcliffe and colleagues, Cochrane–Campbell Handbook, chapter 14 (February 2024 draft)](https://www.cochrane.org/authors/handbooks-and-manuals/cochrane-campbell-handbook-qualitative-evidence-synthesis/qeschapter14intv01140225), the authors describe transformation for a shared question, comparison of separate syntheses and using one synthesis to guide another. JBI [§8.3](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355829259/8.3%2BThe%2BJBI%2Bapproach%2Bto%2Bmixed%2Bmethod%2Bsystematic%2Breviews) distinguishes an integrated approach for evidence that answers the same question from separate syntheses of different aspects. Sections 4.4 and 5.3 use the question to choose among these operations, preserve context and show what a transformation loses. [GRADE-CERQual](https://www.cerqual.org/what-is-the-grade-cerqual-approach2/) assesses confidence in individual qualitative findings. Reconsider the choice if the question, research approach or evidence about those losses changes.

**What can agreement between historical accounts establish?** The AHA [professional standards](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) address the integrity and interpretation of source evidence. Sections 4.2–4.4 and 5.4 examine dependence, dates, purpose, contrary material and rival explanations. Counting the histories is quick, but they repeat one memoir. Source criticism establishes the chronology the dated decision record supports. It leaves the cause open. Reconsider that inference if new provenance, dating or a rival explanation affects its grounds.

These sources offer different ways to synthesize evidence. Choose the method appropriate to the research question and the relationships among the sources.

### RMP.7:12 - Relations

RMP.10 can distinguish candidate accounts of how a practice was performed when evidence supports different variants. RMP.11 compares explanations of an identified method’s history. The synthesis can establish how their sources contribute or depend on one another. Assess the explanations against the evidence that distinguishes them.

- **RMP.1–RMP.4** can supply the question, design, operations and record of actual work. Use existing inputs that answer those questions. Revisit a missing or changed premise when it limits the required synthesis.
- **RMP.5** examines individual source claims, including one that needs revision. **RMP.6** can interpret an existing credibility test or help decide whether another is worth obtaining.
- Use **RMP.8** when a wider claim or model needs reconsideration, or when a receiving practice needs a judgement about reliance. Return an adequate answer about this corpus directly.
- **FPF F.1, F.0.1 and A.10**, with a qualified F.0.2 contribution where applicable, help find, select and compare sources and establish how evidence bears on a claim. For a research synthesis, also establish what the contributions warrant together.
- Use the relevant **domain, access or receiving-practice method** for a disciplinary criterion, permission or decision when it is needed. Use **RMP.9** and the applicable FPF methods when the question is how to improve a research Method.

### RMP.7:End


## RMP.8 - Use Research Results to Retain or Revise an Episteme's Claims and Return Bounded Evidence

> **Type:** Research Method Practice practitioner method pattern
> **Status:** Stable

### RMP.8:1 - Problem Frame

Use this pattern to determine whether research results support, qualify or change a claim in a wider account, or to return evidence with the conditions its recipient needs. Identify the claim, model assumption or explanatory relation at issue and the finding that bears on it.

A synthesis can support a laboratory seal comparison while leaving its application to field conditions open. An archival record can rule out a proposed cause of a decision without establishing the cause or what happened during implementation. Match the earlier assertion and the supplied result to the subject, conditions and question of use.

The **EpistemeChangeAndEvidenceReturn** identifies what the account can now assert, its grounds and limits, and what the receiving work needs from it. A corrected sentence and a source reference may suffice. A model with dependent outputs or an assertion already used elsewhere may require a fuller correction.

An episteme here is a knowledge account such as a model, interpretation or pattern about a Method. Identify the particular claim in that account and what it means for the use at issue. A document’s name or publication status does not identify a change to its asserted content.

Use a compatible analysis, credibility result or synthesis already available. An answer from RMP.5, RMP.6 or RMP.7 may finish its task. Use RMP.8 when the result bears on a wider account or someone’s reliance needs examination. When a practical decision is required, establish its criteria and who has authority. The researcher can also be the decision-maker if they hold that authority.

### RMP.8:2 - Problem

A limited research finding can acquire an unsupported recommendation as it circulates. Criticism of one assumption can be read as rejection of the model, and a corrected decision date can be mistaken for a new account of the event’s cause. Someone using the earlier claim may also miss a correction made in the source.

An unresolved question can lead to an unnecessary new investigation even when a qualified answer already suffices. A proposal reports what a future examination could establish. Present credibility depends on the evidence available, even when no further inquiry is feasible.

Identify which assertion the evidence supports, carry the conclusion through the dependent parts of the account and return the limits relevant to its use.

### RMP.8:3 - Forces

| Force | Tension |
| --- | --- |
| Correcting the same claim | A short conclusion can suffice. A difference in subject, context or time can change what the evidence establishes. |
| Coherent models | A failed premise can affect several outputs, while unaffected claims should remain usable. |
| Receiving use | Evidence can change a practical choice, while the choice also depends on values, constraints and authority outside the research result. |
| Recoverability | A critic or earlier user may need both the earlier statement and its correction. A local draft edit may require only a source reference. |
| Disclosure | A recipient needs enough basis to judge reliance, while source rights, confidentiality and community authority constrain access. |
| Presentation and content | A familiar form may help a particular reader. It can also hide a missing problem, rationale, operation or condition of use. |
| Further inquiry | An open question may be worth investigating. The current answer can still suffice, or access and resources may place the investigation out of reach. |

### RMP.8:4 - Solution

Match the result to the assertion it bears on. Establish what should be retained, added or changed, follow its implications through the account and return the answer with the grounds, uncertainty and limits the receiving question requires.

#### RMP.8:4.1 - Locate the assertion and its receiving question

Identify the earlier statement or model relation, including its subject, comparison, conditions and time. Specify the supplied result, the examination that supports it and the part of the account it addresses.

Check whether the result bears on the same assertion. A factory’s decision to close and the subsequent closure are different events. A laboratory rate may refer to different conditions from a field rate. A finding about another population can extend an account without contradicting the original claim.

When developing a new account, identify the contribution and the material it would add to or qualify. If there is no earlier assertion to correct, treat the contribution as an addition.

Establish what the recipient needs to understand or do when it affects the explanation or evidence required. A scientific explanation or a reusable finding can answer the question, as can evidence for an engineering, public or personal decision.

If the source, its relation to the subject or the examination result is missing, say what conclusion this prevents. A plan can establish which test or synthesis was selected. A claim about its outcome needs evidence of what happened.

#### RMP.8:4.2 - State the warranted retention or change

State the contribution at the strength and scope its grounds warrant. Identify a stronger inference if a recipient could reasonably draw it from the wording or intended use.

| Warranted disposition | What to state |
| --- | --- |
| Retain | State why the assertion still holds under the conditions examined. Identify the basis and limits of that judgement. |
| Narrow | Restrict the population, context, time, relation or transfer to what the result supports, preserving the supported part. |
| Qualify | Keep the assertion and state the uncertainty, alternative explanation or condition of use that matters to it. |
| Reject | Remove the defeated claim or inference and explain what defeated it. Assess a proposed replacement from its own grounds. |
| Add | State the new contribution and its relation to the existing account, including whether it is supported information, an interpretation or a hypothesis for further inquiry. |

One model may need different conclusions about its premises and outputs. Give the grounds for each. To raise confidence, identify what adds support. Repetition of the assertion, a later document date or inability to inspect criticism adds none by itself.

Describe uncertainty under the method that produced the result. Give the quantity and assumptions for a numerical interval and the basis of a qualitative confidence judgement. Identify whether the open step is attribution, extrapolation, prevalence or another inference.

A result compatible with zero and nonzero effects can leave the effect unresolved. To establish equivalence, use the applicable margin and comparison rule. Limited access shows what could be examined. An inference from a missing record to the underlying event needs further grounds.

#### RMP.8:4.3 - Reconcile the affected account

Trace the premise to the conclusions and outputs that use it. Identify those that retain their support, those that change and any newly required relation.

In a model, distinguish the target, structure, parameter, assumption, calculation and interpretation when their grounds differ. An arithmetically correct output may rely on a failed transfer assumption for its field interpretation. The same parameter can remain useful within its calibration conditions.

If a conclusion’s warranted content or stated grounds change, revise the conclusion itself and correct any dependent outputs affected by that change. Preserve access to the earlier wording when a citation, correction or existing use requires it. An unused draft can often be edited in place with a source reference.

A replacement explanation needs grounds of its own. If the evidence rules out only the earlier explanation, retain the alternatives still possible. Use RMP.1 or RMP.2 when an unresolved question or design choice warrants further research.

Use existing records and source links when they let the intended reader examine the reasoning.

#### RMP.8:4.4 - Return evidence to the actual use

Give the answer to the receiving question first. For a change or retention, identify the earlier assertion it concerns. Cite the source or examination that supports the answer, with the conditions, uncertainty, dependence or access limits that affect reliance.

When a materially changed assertion was used elsewhere, provide the correction to any known affected use through its authorized route. Use FPF A.10.1 when affected uses need to be discovered or several known uses need revalidation together. A list of citations can locate possible uses. Establish which relied on the changed assertion.

The responsible editor, maintainer or practitioner can apply a correction to the account or decision they control. A correction that others rely on may also require notifying them. If communication or access is unavailable, identify the return still outstanding and what would enable it. The supported local correction can stand.

Observe applicable source rights, confidentiality, participant protection and community authority. Disclose only what the receiving question needs and permits. A qualified redacted account can convey a finding. If it lacks material needed for a particular inspection, say what cannot be checked. A reader’s own inspection requires their own access.

When a practical choice is required, the receiving practitioner weighs alternatives, values and constraints under the applicable authority. The research result supplies the evidential premise within its scope.



##### RMP.8:4.4.1 - Make a research Method contribution recoverable across publication forms

Use this branch when a publication presents a Method someone needs to understand, repeat, adapt or combine with other work. Identify the contribution and the intended use before choosing a publication form.

A practitioner pattern explains a Method and its use. It identifies a recurring problem, the conditions and competing demands that matter, the way of acting and its grounds, worked applications, limits, consequences and relations. Its SoTA comparison examines what the best available approaches and serious alternatives change in the Method. These elements give the operations their rationale and scope. If claiming that a particular episteme is a U.MethodDescription, establish under A.3.2 that it describes an admitted Method.

Choose a section structure, language, notation, reading order, medium and publication arrangement that give the reader access to that content. A translation or a change in file layout may preserve the contribution. Omitting a constraint that changes the choice of solution alters it. A short entry can direct readers to a developed explanation if that explanation is available.

An article may present several connected claims and Methods with their construction, evidence and limits. Its contributions may warrant one pattern, several related patterns, a change to an existing language or a different knowledge product. A pattern language connects recurring problems and ways to resolve them. A DPF serves a field of practice with a defined scope and maintenance boundary. Use E.4.DPF when deciding which framework contribution the material warrants.

Explain how to recognize another instance of the problem, the conditions that matter, which actions recur, what can vary, and the preparation, support and result required. Another qualified application can reproduce the intended effect while yielding a different object or number. Recomputing a reported number establishes that computation. Applying the Method to a new case tests a different claim. Correct recognition that the Method does not apply can answer a boundary question. Claiming its positive effect requires a case where that effect occurred.

For a reader to use the published Method, establish the following connections as the task requires.

1. **Explain how the Method works.** Identify the recurring problem, situation, objects and relations, the competing demands and how the way of acting addresses them. A construction may combine, adapt or reinterpret existing Methods. Show the sequence, alternatives, feedback and returns where they matter. For work performed together, show how its constituent actions realize the encompassing Method. E.4.CM helps establish compatible contributions and construct the connections a list of source methods leaves open.
2. **Specify the intended repetition.** Distinguish reconstructing a derivation, rerunning a computation on the same inputs, making new measurements and applying a Method under changed conditions. State what remains comparable, what changes, the result to compare and the criterion for agreement. Equality can be appropriate for a derivation or deterministic calculation. New measurements usually need a justified uncertainty or agreement criterion. RMP.6 helps choose an examination or interpret its observed result.
3. **Provide the means the examination needs.** Supply or locate the relevant definitions, assumptions, input preparation, reasoning, operations, material, comparison and interpretation. Give versions, environment, calibration, timing, randomization or required capability when a difference could change the result. For a reused Method, identify the usable instructions and their conditions. RMP.4 helps establish what surviving records show about conduct. State what they leave unknown.
4. **Connect the publication forms.** An empirical article often separates the question, methods, results and interpretation. A theoretical or methods article may develop a construction and its argument. A protocol or Stage 1 Registered Report specifies proposed work. A results report gives what was done and found. Apply the reporting requirements of the relevant venue and study type. A pattern explains the recurring problem, competing demands, solution, grounds, cases, boundaries and comparison with other approaches. Preserve the substance when changing section names or order.
5. **Explain what readers can examine.** Link each presentation to the source contribution and the material needed for the stated examination. Give access conditions and consequential omissions. A protocol supports a claim about intended work. An available artifact can permit a rerun. For a claim about an actual rerun, provide its result. A repeatable calculation needs an additional applicability basis for a different setting. When a claim on which others relied changes, correct affected presentations and uses through §§4.3–4.4.

Choose an explanation and access arrangement sufficient for the receiving use. A theoretical derivation may be reproducible from its premises without an empirical dataset. Respect restrictions on protected participant material. If they prevent the requested public inspection, identify the limit and any qualified finding available to that reader.

#### RMP.8:4.5 - Finish the answer and select further inquiry only when warranted

Finish when the account and its required recipients have the conclusion the evidence warrants, or when the specific missing input or delivery limit has been identified. Distinguish a supported local correction from an outstanding promised delivery. A broader open question can be reported separately.

If further inquiry could improve an explanation, reusable finding or receiving decision, compare its attainable contribution with the work it requires. Include preparation, access, execution, interpretation, protection, shared resources and displaced work. Keep the present conclusion within the evidence already obtained.

When a research design still needs choosing, RMP.2 helps compare designs. For a question about credibility, use an adequate existing result or use RMP.6 to assess the examination. Distinguish a supported decision to commission no further study from a choice that remains open because a needed input is missing. Revisit the choice if a useful investigation becomes feasible.

Repeated failures in selecting or performing research Methods can identify a question for RMP.9 or FPF Method development. State what needs improvement and which practice could address it, if known. The present research result can be returned while that work remains open.

### RMP.8:5 - Archetypal Grounding

The research results and communications in these cases are stipulated for illustration.

#### RMP.8:5.1 - Keep the laboratory result, withdraw the unsupported field prediction

In the example an engineer receives a synthesis supporting a positive mean difference in seal lifetime under specified accelerated laboratory conditions. The existing model makes the following three claims.

| Existing contribution | Supplied criticism and revision |
| --- | --- |
| The fitted wear relation describes the dry laboratory material over the tested range. | The analysis supports the relation within that range. Retain the parameter, fit and uncertainty for that scope. |
| The same wear rate applies in the wet service environment. | The synthesis covers dry accelerated tests. Withdraw the statement that this research demonstrated the wet-service rate. Its applicability there remains open. |
| A service replacement time follows from the laboratory rate and the engineering wear limit. | The arithmetic can still be correct. Its use for replacement time depends on the unestablished wet-service rate, so withdraw the prediction as an established field result. The engineering authority retains its wear-limit criterion. |

The engineer can report that the laboratory relation holds within the tested range. The synthesis supplies no basis for carrying the dry wear rate unchanged into wet service, so it cannot establish the derived replacement time there. Cite the laboratory result and identify the missing transfer premise.

Different dry and wet rates are one hypothesis. A suitable field comparison could examine it if the work is feasible and what it could establish warrants the cost. RMP.2 and RMP.6 can help make that choice. Give the reliability authority the bounded finding for its maintenance decision. The research return can finish with that correction even if the operational choice remains open.

#### RMP.8:5.2 - Correct the same historical event

Several later accounts claim that a public protest prompted the decision to close a factory. They share one retrospective memoir. An authenticated record dates that decision before the protest.

The dated record rules out the protest as the cause of the earlier decision. Retain the supported chronology and leave the cause open. Any effect on later implementation is a separate question.

A museum description attributes the decision to the protest. The editor responsible receives the corrected chronology, its source and the remaining causal limit. The correction concerns the decision to close. The timing and cause of the physical closure need their own evidence. Restrict protected detail to permitted uses and identify what an outside reader can authenticate from the public summary.

For the broader assertion that “the protest affected the closure,” distinguish the disproved cause of the decision from the unresolved influence on implementation. The same dated record has different consequences for those assertions.

#### RMP.8:5.3 - Return a situated finding without inventing prevalence

A community synthesis links distrust in monitoring to withheld feedback in its examined settings. An earlier briefing says that this is the principal reason most local residents do not participate.

The examined accounts link withheld feedback to distrust, with the stated exceptions and contexts. They supply neither a population denominator nor comparative frequencies for “most” or “principal.” Revise the briefing to report the connection attributed in those accounts. Distinguish the source authors’ interpretations from the broader explanation developed in the synthesis.

The group can use this finding to consider how it returns monitoring information. Predicting how many residents would participate after a change requires other evidence, and implementation requires the applicable authority. Consider a frequency survey if it can answer a question the group needs and its contribution justifies the work.

#### RMP.8:5.4 - An adequate answer and a later correction

A requester receives an existing synthesis that answers the specified comparison. A brief answer citing the synthesis, its applicability and uncertainty completes the return.

Later, an erratum reverses a result on which a finding relied. Recompute or reinterpret the affected finding, correct the claims whose grounds or content changed, and inform the people or services that relied on them through an authorized route. They can reconsider their conclusion or decision on the corrected basis. Retain unaffected results. A later date by itself supplies no reason for this reanalysis.

#### RMP.8:5.5 - Valuable uncertainty without an obtainable study

A synthesis establishes a chronology but leaves a historically important mechanism unexplained. The only study proposed would require access to records the historian cannot lawfully inspect. No worthwhile authorized alternative is available under the stated conditions.

The historian returns the chronology and identifies the mechanism that remains unexplained. No further study is selected under these conditions. If an archive later becomes available and could distinguish the explanations, weigh its contribution against the work required. The historical question has scientific value in its own right.



#### RMP.8:5.6 - One calibration contribution, an article and a pattern

Consider a temperature instrument with displayed value y and reference value x, both in degrees Celsius. Suppose a separate characterization supports the affine relation y = a + bx under the stated operating conditions over 0–20 °C. The two reference points below determine its coefficients under that premise.

The reference pairs are (0, 2) and (20, 24). They give b = (24 − 2)/(20 − 0) = 1.1 and a = 2, so x = (y − 2)/1.1. A display of 13 °C gives a corrected value of 10 °C. A reader can reconstruct the derivation and recompute the answer from these pairs. Observing the instrument again would be a separate examination.

An article can present the instrument problem, the independent characterization, the derivation, the observation procedure and data, and the scope of the result. A pattern for correcting readings would explain when offset and scale errors matter, what justifies the affine approximation, and how nonlinear response could defeat it. It would show how to obtain suitable references, apply the correction and respond to disagreement in an independent comparison. Its cases, consequences, relations and comparison with alternative methods help another practitioner use it. Giving the equation a section heading supplies none of the missing operations.

Now suppose the instrument displays 13.2 °C for a newly obtained reference of 10 °C. The corrected reading is 10.1818… °C. The difference of about 0.18 °C is within the prespecified allowance of ±0.3 °C, which includes reference uncertainty. This observation meets the agreement criterion at that point. Agreement at other points needs corresponding grounds. Use RMP.6 if the scope of the comparison is at issue.

The same correction Method accepts a different qualified input and can return a different value. Recomputing 10 °C from the earlier display of 13 °C repeats the reported calculation. Applying the rule to 13.2 °C returns 10.1818… °C. Copying 10 °C would give the wrong corrected value. In either case, establish that the calibration and affine approximation apply.

An English or Russian account may publish the pattern separately or as part of a framework. Its calculation and the conditions for using it can be preserved in either form. Removing the 0–20 °C condition changes the warranted scope. A proposed use at 40 °C needs a basis for extrapolation. Agreement at 10 °C cannot establish that. If a later investigation defeats the affine premise, retain the arithmetic and correct the calibration claim in affected articles, pattern accounts and uses that relied on it.

### RMP.8:6 - Bias-Annotation

One identifiable recipient makes a short correction easy to deliver. Distributed reliance, conflicting editions and protected material can require more investigation and communication. Determine that work from what used the affected claim and what requires correction.

The engineering examples show research informing a practical decision. Basic explanation, interpretation and reusable knowledge can also be valuable outcomes when considering further research.

### RMP.8:7 - Conformance Checklist

Check the account and its return against the following questions.

- Do the earlier assertion and new contribution address the same subject under comparable conditions? Where the comparison, time or context differs, has the account distinguished the claims?
- Is each retained, narrowed, qualified, rejected or added contribution supported to the extent stated?
- Have the affected outputs and explanations been reconsidered, and can the reader still use the conclusions that retain their support?
- Can the recipient recover the answer, its basis, uncertainty and any limits affecting reliance?
- Where someone relied on a materially changed claim, did the permitted correction reach the affected use, or can the reader identify the delivery that remains outstanding?
- Are the available evidence, any proposed inquiry and any authority needed for a practical decision identified on their own grounds?
- If the task is to repeat or adapt a Method, can the reader recover the problem, way of acting, grounds, scope and means of checking the intended result from the presentation available to them?

Use the working situation to recognize when this Method applies. Judge the resulting account from its evidence and the return required for its use.

### RMP.8:8 - Common Anti-Patterns and How to Avoid Them

| Failure | What changes in practice |
| --- | --- |
| A new label is taken as evidence that a claim changed. | Locate the assertion, assumption or explanatory relation and establish whether its content changed. Correct it when the evidence requires it. |
| Pattern headings are taken to establish that a Method can be repeated. | Preserve the problem, conditions, competing demands, construction, grounds and limits. Identify what a particular repetition needs, what is available and what an actual examination established. |
| The decision date is treated as the date of physical closure. | Identify which event the document dates and which event the causal explanation concerns. |
| Failure of one premise is taken to defeat the entire model. | Trace the conclusions that depend on it and retain supported parameters, observations and calculations within their scope. |
| An unrestricted conclusion survives beside a caveat. | Qualify the conclusion itself and reconsider outputs that use it. |
| Correcting the source is assumed to have corrected reliance elsewhere. | Establish which use relied on the changed assertion. Supply the correction through the permitted route, or explain which required delivery remains outstanding. |
| Every remaining uncertainty leads to a new study. | Compare the attainable contribution with access, cost and displaced work. Return the current conclusion and its limits when further inquiry is unnecessary or unobtainable. |

### RMP.8:9 - Consequences

The recipient can see which findings remain supported, which extrapolation or explanation has been defeated and which proposed alternative still needs evidence. The account can retain one claim while correcting another.

The effort depends on the account’s dependencies and who relied on it. A short answer may suffice. A change to a published model can require recovering the earlier meaning and notifying affected users.

### RMP.8:10 - Rationale

Research bears on a receiving use through an assertion, assumption or interpretation. Tracing that connection shows how far the result extends and which earlier conclusions continue to hold.

A research answer can settle an evidential question while a practical choice remains open. An account can also identify an important unexplained mechanism and finish its present task. Future studies can change that account when they provide evidence.

### RMP.8:11 - SoTA-Echoing

**What does the evidence establish for its recipient?** Cochrane [chapter 15](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-15) distinguishes interpretation of an observed effect, uncertainty about it and a recommendation about use. A positive finding can supply a premise for advice. An inconclusive result can leave the effect open. Sections 4.2 and 4.4 return the warranted finding and its conditions. A short qualified answer can avoid an unnecessary new study, but a consequential transfer limit needs explanation. Reconsider interpretation if the target, uncertainty, result or use changes. Criteria for a practical action come from the receiving practice.

**Which historical claim does the correction affect?** The AHA [professional standards](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) guide source integrity, interpretation, treatment of contrary material and confidentiality. Sections 4.1–4.4 and 5.2 use those distinctions to match the correction to its event. A dated decision can correct the museum’s account without establishing when physical closure occurred or why the decision was made. Comparing the events costs little and prevents an unsupported historical inference. Reconsider it if the asserted event, dating or provenance changes.

**Which accounts and uses need correction?** FPF C.2.1 identifies the knowledge account, A.10 relates evidence to a claim and A.10.1 helps recover affected uses or revalidate them together. Sections 4.1, 4.3, 4.4 and 5.1 trace the premise to the output, preserve the laboratory finding and correct its unsupported field interpretation. Discarding the whole model would lose the supported part. Editing only the source could leave an earlier user relying on the affected claim. Scale the work to that reliance and reconsider it when the relied-on content changes or another consequential use is discovered.

**When is further inquiry worth obtaining?** FPF C.11.DUA compares the epistemic or practical value of the attainable contribution with its full cost. RMP.2 and RMP.6 address research designs and credibility examinations. Sections 4.5 and 5.5 weigh scientific value, access, shared resources and protection. Insisting on immediate operating payoff would discard useful explanations. Commissioning every possible study can consume resources without resolving the question. Return the evidence already available and revisit the decision if a worthwhile study becomes feasible or the inputs to an open choice change.

**What would enable a reader to repeat the Method?** Nature Portfolio’s [reporting and availability policy](https://www.nature.com/ncomms/editorial-policies/reporting-standards) identifies the design information and access conditions for data, code, materials and protocols that readers need within the policy’s scope. The [Registered Reports description](https://www.cos.io/initiatives/registered-reports) distinguishes assessment of proposed methods from reporting obtained outcomes. Sections 4.4.1 and 5.6 connect these reporting questions to RMP.4 on the record of actual work, RMP.6 on the intended examination and FPF E.8 on the substance of a pattern. Publication and a filled template can leave the problem, grounds or means of repetition unexplained. Give the detail needed for the intended repetition or adaptation. If a consequential input is missing, a Method condition changes or an observed comparison fails, reconsider the affected claim.

These sources inform interpretation and reporting in their respective fields. Evidence about use of this Method across research traditions or a stronger methodological account can change how it should be applied.

### RMP.8:12 - Relations

- **RMP.5, RMP.6 and RMP.7** can supply an analysis, an examination result or a synthesis. Use an adequate result directly when it answers the question.
- Use **RMP.1** for a changed research question or **RMP.2** for a choice of design when needed. **RMP.3** and **RMP.4** help distinguish proposed operations from the evidence of conduct.
- Use **FPF C.2.1** for the knowledge account and **A.10** for its link to the evidence. When materially changed source content requires discovery of affected uses or joint revalidation, use **A.10.1**. **C.11.DUA** helps compare further inquiry with its attainable benefit and burden.
- The **receiving domain or practice** establishes any action alternatives, values, safety conditions, access, confidentiality and authority needed for the intended use. A bounded research finding can supply evidence for a decision.
- Use **RMP.9** or applicable FPF Method-development guidance when the issue concerns how research Methods are selected, improved or used.
- **FPF E.8** explains a pattern’s substantive functions and publication conventions. **E.4.CM** guides the construction of a composite Method. Use **E.4.DPF** when deciding whether the contributions warrant a new or revised DPF.

### RMP.8:End

# Part V - Improve and Refresh Research Methods and Practice


## RMP.9 — Decide Whether and How to Improve Research Methods and Practice

> **Status:** Stable

> **Type:** Research Method Practice practitioner method pattern

### RMP.9:0 - Use This When

Use this method when research work, criticism, a change in tools or a new use raises a question about the suitability of a research Method or the way researchers practise it. State the use and the difficulty or opportunity. Determine what the available evidence says about the Method, its description, its implementation or the conditions in which it was used.

The result can explain what happened, support retaining a Method, identify a correction or show where a use lacks support. If the task includes introducing a change, establish what its users need. A specified calculation error can be corrected directly. A new comparison is worth considering when its attainable results matter enough to justify the full effort.

Research-Method improvement connects a knowledge question, criteria of validity and criticism, field-specific interpretation, research material and the claims that depend on the Method. FPF Core supplies methods for identifying, trying and comparing Methods, assessing fit and worth, and distinguishing variants. Use A.3.1.MI when introducing a Method into practice.

A disappointing finding, an unfamiliar technique, reviewer disagreement or a software release can prompt an inquiry. Establish which part of the work is affected. Use RMP.5 to examine a particular analysis or RMP.8 to revise a knowledge claim. Use the relevant operations or institutional practice for equipment recovery, administration and permissions. Apply the four RMP.1 conditions when asking whether the inquiry into a Method qualifies as new research.

#### RMP.9:0.1 - Working Terms

| Term | Meaning for this use |
| --- | --- |
| research Method | A repeatable way of investigating, analysing, interpreting or criticizing a research question. Its suitability depends on the question and conditions of use. |
| Method description | Instructions or an account of how to use a Method. A correction can clarify the account while preserving what practitioners are to do. |
| implementation or support | Software, an instrument, procedural support or another means of applying the Method. A defect in it can explain the failure of an otherwise suitable Method. |
| semantic Method change | A change in what practitioners are to do that can alter the Method’s applicability or the claims it supports. Determine whether this introduces a variant and which qualifications carry over. |
| supported retention | Keeping a Method or practice for conditions in which adequate evidence supports its use. Examine its fit separately when those conditions change. |
| ResearchMethodPracticeRevision | An account of the supported outcome. It can identify a retained Method, a correction, a changed Method, a restriction or a discontinued use. |

### RMP.9:1 - Problem Frame

The same error in an uncertainty estimate can have different explanations. The implementation may calculate the wrong formula, the observations may violate its assumptions, or the quantity of interest may have changed. Check a faulty implementation against the specified formula, examine the assumptions against the observations, and settle the target before ranking estimators for it.

Professional traditions also differ in what improvement means. A statistical comparison can examine coverage under relevant generating conditions. Reflexive qualitative analysis can need a more coherent interpretation, while a historical argument can need correction of a source transcription. A criterion useful for one purpose can distort another.

Compare the alternatives that bear on the question. Available evidence may support keeping the present practice, making a limited correction, adopting a different Method, using variants in distinguishable situations or stopping an unsupported use. Further inquiry can supply evidence when the choice is open.

### RMP.9:2 - Problem

Teams can replace a useful Method after a criticism of its implementation, or excuse a genuine Method defect as poor execution. Speed, agreement or novelty can improve while the research result deteriorates. Check the indicator against the research purpose before using it to judge improvement.

An unresolved comparison can cost time for design, execution and reporting. Estimate what its results could establish and whether the comparison is attainable. If the cost rules it out, judge the present Method from the evidence available. An untested use can remain unsupported.

### RMP.9:3 - Forces

| Force | Tension |
| --- | --- |
| Preserve useful practice | A familiar Method may merit retention. Judge its fit from evidence about the use in question. |
| Locate the defect | A similar symptom can arise from the Method, its description or implementation, the practitioner’s capability or the claim made from the result. Each calls for a different repair. |
| Criticism within the research purpose | Shared demands for inspectability coexist with different statistical, interpretive and historical criteria. |
| Evidence and whole burden | A discriminating comparison can improve many later studies, while its design, conduct and uptake consume real research capacity. |
| Change and continuity | Users introducing a revision need access to the change, its provenance and the conditions for reusing earlier qualifications. |

### RMP.9:4 - Solution

#### RMP.9:4.1 - Locate the question and try the supported present answer

Identify the research use, the question about the Method and the evidence that could affect the answer. Establish the relevant Method, its description, how it was or would be applied, and the receiving conditions as needed to distinguish the object at issue. For a proposed change, identify what its introduction would alter in practice.

Use available evidence to distinguish the reusable Method from its interpretation or implementation, a local deviation, a gap in capability or support, and an affected analysis or claim. If several explanations fit an observed failure, say which remain possible and what each implies.

Use an adequate existing result within its conditions. It may settle a question about a past application, warrant retention or specify a correction. If a correction is commissioned, check it at the affected object and give the users of its result the conditions on which it depends.

**First useful example.** Suppose a suitable Method specifies the sample variance with denominator n−1 and the implementation uses n. If the error is still present, correct it and check the calculation against the formula. A saved check of the repaired calculation may already support an account of the earlier correction. When correcting dependent work, identify the results that relied on the wrong value and reanalyse those whose conclusion or basis is affected. Section 5.1 works through the numbers.

#### RMP.9:4.2 - Compare alternatives for the same research use

For an open decision, compare the attainable courses that address the difficulty. They may include retaining the practice, repairing its description or support, changing the Method, keeping variants for distinguishable situations or stopping a use that lacks a defensible basis. A supported conclusion on one course can answer a question about that course.

Compare alternatives for the same quantity, interpretation or research purpose. If they answer different questions, state the difference. Examine their resistance to the relevant criticism, their fit to the material and receiving conditions, and the implications for users.

Compare material burdens and identify who bears them. Include relevant demands on access, participant time or exposure, equipment, competence, software, design, computation, reading, interpretation, documentation, transition, maintenance and recovery. Account for displaced research and for the work of proposing and explaining the comparison.

Exclude alternatives that violate binding validity, ethical or access conditions. Count long-term scientific value where it matters. Where the accepted criteria leave alternatives incomparable, explain the trade-offs.

#### RMP.9:4.3 - Decide whether further evidence is worth obtaining

Before designing a new trial or study, ask:

- What could the new evidence establish or change about the claim, its support or the decision?
- Could a discriminating comparison be obtained under the actual access, capability, material and time constraints?
- Would that contribution justify the full effort of obtaining and using the evidence?

Use sufficient existing evidence for retention, a specific correction or a conclusion about an earlier use. If an important question remains, select a comparison that can answer it within the available conditions and whose contribution warrants the work.

If a further comparison is out of reach or costs more than its result warrants, state what the relevant evidence supports and where its support ends. That can finish an account of an earlier use. If advice or a restriction is called for, identify the unsupported use and act within the authority for that work. Declining a new study leaves its possible result open.

For a selected comparison, choose a research or Core Method-development method that can obtain the needed evidence. State which existing or proposed methods or uses are being compared and what evidence could distinguish them in the selected comparison. For a completed trial, establish what was done and observed, the inference those observations support and any resulting Method decision.

For a simulation, define its aim, generating situations, common estimand, candidate procedures and performance measures. Account for Monte Carlo uncertainty and for missing or non-convergent outputs. An analysis restricted to successful runs can favour a procedure that often fails. Report what happened across the runs and limit the performance claim to the conditions examined.

Use the standards of criticism appropriate to a qualitative, historical or mixed inquiry. For example, improved reporting may make an interpretation inspectable. Judge the interpretation itself against the research question and its evidence.

#### RMP.9:4.4 - Retain or introduce the supported change

State what practitioners retain or change and the conditions that support that conclusion. Distinguish a revision of what the Method requires from a correction to its description or software and from a local deviation. For a changed Method, assess whether it forms a variant and which earlier evidence still applies.

When introducing a selected change, supply the missing instructions, capability, tools or other support. Introduce it under the supported conditions and keep the provenance and means of recovery needed by users. Distinguish notification, actual use and observed effects.

A team with the necessary capability can make a small correction directly. A wider change may call for preparation or follow-up. Select a later observation when its attainable result could reveal an important failure, clarify an effect or affect a decision.

When two variants serve different situations, give the feature that distinguishes those situations and the evidence supporting each use. To qualify a local adaptation, establish what changed and where the evidence applies.

#### RMP.9:4.5 - Return the actual consequence and finish

Identify any results that relied on the affected part of the Method. If the change alters their basis or warranted scope, reassess that part of each result and retain the work that still holds. A revised measurement relation can affect operationalization and analysis, a corrected extraction can affect a historical claim, and a changed synthesis procedure can affect a corpus finding. Section 12 gives the corresponding methods.

In a ResearchMethodPracticeRevision, give the research use, the object examined, the supported outcome and its basis and limits. Include the change to practice and consequences for receiving work when present. If the decision is to obtain further evidence, identify the selected work and the open qualification question it addresses.

If investigating the Method becomes a research question, test the whole inquiry against the four conditions in RMP.1:4.2. A fully specified protocol can investigate a disputed knowledge claim. A check of a known correction against an accepted rule can finish as ordinary Method work.

A failure, a dispute or a changed tool can raise the question. Use evidence of fit for retention, a check against the applicable criterion for a correction, evidence of applicability for transfer, and grounds for attributing an improvement to the change when making a causal claim.

### RMP.9:5 - Archetypal Grounding

The following cases use stated assumptions to show when different answers are warranted.

#### RMP.9:5.1 - Correct the calculation and retain the Method

A team's accepted Method estimates sample variance for independent observations by dividing the squared-deviation sum by n−1. The receiving conditions still fit this Method. A software default instead divides by n.

For observations 2, 4, 6 and 8, the mean is 5 and the squared-deviation sum is 9 + 1 + 1 + 9 = 20. The specified sample variance is 20/3; the implementation reports 5. The difference is a determinate implementation defect under the case premises.

Correct the denominator and check both the sample variance and any dependent uncertainty calculation. For these observations, the correction changes 5 to 20/3. Retain the Method for the stated conditions. Trace the analyses that used the wrong denominator on any dataset and return consequential corrections through RMP.5 and RMP.8.

The known-answer check can establish that the implementation now produces the specified value for these observations. Qualifying another estimator or using this Method under different conditions requires evidence for that question.

#### RMP.9:5.2 - Select a worthwhile comparison without inventing its result

Suppose a programme now needs an equally weighted mean across independent sites. Site sample sizes differ, and observations within a site are dependent. Pooling observations weights sites by sample size. Under these conditions the former analysis does not provide the required weighting or uncertainty calculation.

Both candidate procedures use the mean of the site means. One constructs a t interval from the independent site means. The other resamples whole sites to construct an interval. For few sites, skewed outcomes and plausible heterogeneity, compare how the intervals perform under conditions relevant to their intended use.

Suppose a qualified statistician and existing code put the comparison within a two-day allocation, including design, code checks, computation, investigation of failed runs, Monte Carlo uncertainty and interpretation. Include the cost of introducing a chosen procedure in the decision. The programme would reuse the analysis across several studies whose uncertainty claims matter.

Select a simulation that compares performance for the shared estimand across the relevant generating situations. Include adverse and inconclusive results. If neither procedure meets the requirement, consider a narrower supported claim or stop the proposed use.

These premises justify obtaining the comparison. Decide which procedures fit the proposed use when adequate performance evidence is available. Reconsider the investigation if its access, capability, cost or expected contribution changes.

#### RMP.9:5.3 - Repair interpretation within reflexive thematic analysis

A reflexive thematic analysis team is asked to maximize agreement among coders. Suppose its topic list gives little interpretation and the research question calls for a coherent thematic account. Examine how the team developed the themes. Coder disagreement alone has yet to explain the interpretive weakness.

Develop the themes through interpretation and reflexive discussion, then judge them against the research purpose. If the question requires repeatable fixed-category counts, select and qualify a Method and criteria for that purpose. Agreement among coders can be relevant to the latter task.

#### RMP.9:5.4 - Correct source extraction without certifying a new tool

An OCR tool repeatedly omits marginal dates from a historical collection. Compare the extraction with the available source images, correct the affected transcription and chronology, and retain the supporting source for the interpretation. The team can retain its historical Method while correcting the extraction.

For a replacement tool and a different handwriting collection, ask whether evidence of extraction fidelity already covers the intended use. If fidelity remains uncertain, compare the tools when access, expertise and effort justify the test. Speed measures throughput. When adequate evidence of the marginal dates is unavailable, qualify the affected part of the argument.

#### RMP.9:5.5 - Preserve the distinct contributions in mixed research

A project combines fixed-category counts with an interpretive account. A coding revision changes both the counting rule and the meaning of the categories. Reassess the affected count by its measurement criteria and the interpretation by its evidence and purpose, then examine what the two findings can support together.

Use RMP.3, RMP.5 or RMP.7 for the affected operationalization, analysis or synthesis. Retain still-applicable material and inform the users of any claim whose content or basis has changed. Explain how the two contributions bear on the common question.

### RMP.9:6 - Bias-Annotation

Numerical examples make some errors and comparison criteria easy to display. Interpretive, historical and community research have other forms of criticism. Use their own professional knowledge to judge an improvement for their purposes.

Novelty and countable gains can attract attention that a suitable practice or a small correction deserves. Saving the cost of a study can also leave an important weakness unexamined. Compare alternatives by the research use, the strength of the evidence and the full cost of obtaining more.

### RMP.9:7 - Conformance Checklist

Check the conclusion against the question and conditions it covers.

- Have you identified the Method, description, implementation, capability or claim at issue, and the research use for which it matters?
- Does existing evidence settle the question, support retaining the Method or specify a correction?
- If further evidence is needed, what could it establish, is it attainable, and does its contribution warrant the full effort?
- If a needed basis is missing, is the limit clear to the person or service considering that use?
- Does the conclusion distinguish proposed change, actual performance, qualification and observed consequence?
- Does a changed Method retain the necessary variant, provenance, receiving-condition and recovery distinctions?
- Do the people or services relying on the result have the information they need about its scope and consequences?

### RMP.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Every criticism becomes a new trial | The team starts acquiring evidence despite a determinate correction or an adequate answer. | Use sufficient evidence first. For a remaining question, compare the attainable contribution of a new study with its full cost. |
| No affordable comparison means the Method is adequate | Acquisition cost is taken as evidence of suitability. | State which uses are supported and where qualification remains open. Restrict an unsupported use when that is within the remit. |
| Every software change creates a new Method | An implementation or description correction is mistaken for a change in what the Method requires. | Identify what changed and reassess the qualifications that depended on it. |
| One metric improves every research tradition | The chosen indicator changes the research purpose or overlooks its criticism. | Compare alternatives under the actual estimand, interpretation or source-use question. |
| Only successful trials enter the comparison | Failures and non-convergence disappear from the evidence used for the Method decision. | Preserve them and choose their treatment by the comparison's aim. |
| New description means successful adoption | Announcing a revision is taken as evidence of its use or effects. | Establish what support was provided, where the Method was used and what the observations show about its effects, as the claim requires. |
| Every Method revision restarts the research repertoire | Independent questions, material and claims are reopened together. | Trace uses of the changed part and reassess the results whose content or basis depends on it. |

### RMP.9:9 - Consequences

A team can retain a suitable Method, verify a small correction, or investigate a consequential weakness when attainable evidence justifies the effort. Users can see the conditions supporting the decision and which research results depend on it.

Diagnosis, qualification, introduction and maintenance of a major revision can require specialist capability and substantial work. Include those demands when comparing the alternatives.

Reassess the relevant decision when criticism, instruments, tools, receiving conditions, sources, costs or observed use materially affect its grounds. Trace the particular analyses that rely on the change.

### RMP.9:10 - Rationale

Research practice connects a Method difficulty to the standards of criticism for that research and the claims that rely on it. Use Core methods for trials, fit, worth and variants and A.3.1.MI for introduction into practice when one of those contributions is needed.

Identify what needs attention and check the current evidence before commissioning more work. A decision about the value of obtaining evidence can be sound even while a claim about the Method remains unresolved.

### RMP.9:11 - SoTA-Echoing

For a question of research-Method improvement, [Core Method development (FPF C.39.MF)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c39mf---choose-and-reopen-a-method-development-focus) distinguishes identity, trials, fit, worth and variants. [FPF A.3.1.MI](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31mi---introduce-a-method-into-practice-and-decide-what-to-keep-or-change) addresses introduction into practice. C.11.MV:4.1–4.2 compares attainable courses and their full burdens, including retaining a set of alternatives when the evidence does not distinguish them. Section 4.3 **adopts** its stopping and acquisition conditions and **adapts** the comparison to the knowledge question, its standards of criticism and the affected result. In §5.1 the specified denominator makes correction and verification sufficient. If qualification remains open, state which uses lack support. Reconsider further inquiry when the contribution it can supply warrants its cost. Reassess this use of Core if a relied-on condition changes.

For a selected simulation, §§4.3 and 5.2 **adopt** the common-target design in [Morris, White and Crowther (2019)](https://doi.org/10.1002/sim.8086), with inspectable planning and reporting from [Williams et al. (2024)](https://doi.org/10.1111/2041-210X.14415) and treatment of missing or non-convergent outputs from [Pawel et al.](https://doi.org/10.1080/00031305.2025.2540002). Specify the estimand, generating situations, performance criteria and Monte Carlo uncertainty. Investigate failures and interpret them in light of the aim. Comparing only successful runs can obscure unequal failure rates. Include this work in the acquisition cost. These sources guide the conduct and interpretation of a simulation once it has been selected. Reconsider the comparison if the target changes, a new failure appears or better treatment of missing outputs becomes available.

For reflexive thematic analysis, §5.3 **adopts** the methodological coherence discussed in [Braun and Clarke's RTARG contribution (2024)](https://doi.org/10.1177/02692163241234800) and their [quality guidance](https://www.thematicanalysis.net/quality-in-ta/). Developing an interpretation and examining it reflexively addresses the weakness of the topic list. Increasing agreement among coders can leave that weakness in place. For repeatable fixed-category counts, choose a Method and criteria for that task. Depending on the coding arrangement, the criterion might concern agreement among coders or the fidelity of an instrument to a reference classification. Judge the quality of the interpretive work from the analysis as well as its reporting.

Section 5.4 **adapts** the [AHA professional statement's](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) requirements for source integrity and a recoverable trail. Checking the original images grounds a correction to the marginal dates and the chronology that used them. A speed comparison would answer a question about extraction time. A comparison of fidelity for another handwriting collection requires evidence for that collection. Assess available substitutes when access to the originals changes.

The cases apply different standards to statistical, interpretive and historical work. They illustrate how the purpose and cost of an inquiry can change the practical choice. A claim about the effect of using RMP.9 in actual research would require evidence from its use.

### RMP.9:12 - Relations

Use A.3.1.MR to recover a candidate way of working from practice. Use RMP.10 when a material reconstruction question needs a larger evidence programme. RMP.11 can explain differentiation among Methods. Use that explanation for a present choice where it bears on the choice, and examine present fit under the relevant conditions.

| Contribution | Actual relation |
| --- | --- |
| RMP.1 and RMP.2 | Use RMP.1 to establish whether a newly opened question qualifies as research and RMP.2 for a needed design comparison or a justified stop. |
| RMP.3 and RMP.4 | Use RMP.3 to develop or assess a changed operational choice. Use RMP.4 to establish which records, deviations, transformations and provenance matter for the claim. |
| RMP.5 and RMP.6 | RMP.5 examines affected analysis or inference. RMP.6 can establish what an earlier credibility examination showed or help choose a further one. |
| RMP.7 and RMP.8 | RMP.7 can reassess an affected synthesis. RMP.8 revises the claim or model and traces the uses of what changed. A difficulty with either Method can enter RMP.9 directly. |
| Core Method development and A.3.1.MI | Use the Core method for identity, repertoire, trial, fit, worth, variants or practice culture when it supplies a needed result. A.3.1.MI supports introduction. |
| Domain practice and institutional authorities | Use research evidence in engineering, operational, policy, access or adoption decisions under the criteria and authority governing each decision. |

### RMP.9:End

# Part VI - Reconstruct Practice and Explain Method History

## RMP.10 - Reconstruct a Candidate Method Account from Practice Evidence

> **Status:** Stable

> **Type:** Method pattern
>
> **Primary working result:** a **claim-to-evidence dossier** that connects each proposed account of a reusable practice to the evidence for it. Include significant contradictions, rival explanations, limits and the results of any further checks performed. Sometimes the evidence establishes only an occurrence, a local workaround or tool behavior, or leaves the grouping unresolved.

### RMP.10:0 - Use This When

Use this method when ordinary recovery through `A.3.1.MR`, or a usable result of that work, leaves a material reconstruction question and answering it warrants a larger evidence programme. You may need to distinguish settings, disputed variants, tacit cues or judgements, gaps in the records, or the reach of an account under changed conditions. A question about past practice can warrant the work in its own right.

Identify what the recipient needs to know about a possible reusable practice. Select the claims whose content, scope or support matters to that use and the forms of evidence that can distinguish the plausible answers.

A first result connects each claim to the observations that could support it, contradict it, distinguish variants or justify a narrower statement. Use this claim-to-evidence matrix to select cases or sources and to estimate the specialist work still needed.

Use an existing account or a description of the observed work directly when it answers the question. When making a stronger reconstruction, distinguish what occurred from the later hypothesis about a reusable Method. Use an instruction as evidence of what it prescribed and event records according to what they recorded. `A.3.1` governs identification of a Method.

#### RMP.10:0.1 - Working Distinctions

| Evidence or result | Contribution retained here | Boundary |
| --- | --- | --- |
| occurrence observations and artifacts | Overt actions, results, versions, coordination and traces for a particular Work occurrence. | Recurrence supports a claim about observed behavior. Identifying a Method requires the applicable identification grounds. |
| Critical Decision Method (CDM) probe | A participant’s recalled cues, options, judgements and counterfactual reflections on a critical incident. | Account for recall and interviewer effects. Establish logged events from their records. |
| event-log analysis | Recorded recurrence, sequence, deviation and conformance under the declared meanings of the log fields. | To infer intent or tacit contribution, establish what evidence bears on it. A recording of events and an instruction can serve different claims. |
| contextual observation or protocol elicitation | Evidence of coordination, workarounds or reasoning that the other selected sources leave open. | Choose and qualify each operation for its own purpose and risks. Cite the source that supports it. |
| expert synthesis | The matrix, sampling for relevant variation, comparison of apparent contradictions by scope, and choice of checks and stopping conditions. | Attribute these choices to the practitioners combining the evidence. |
| candidate Method account | a scoped episteme about a possible reusable way of doing | Method identification remains with `A.3.1` |

### RMP.10:1 - Problem Frame

Logs capture events visible to the instrument. Instructions describe intended action. Interviews can favour memorable episodes. Records of success can overlook recovery work or practices used by a minority. For an unresolved claim, identify which information is missing and which source could provide it.

Compare the contribution a specialist inquiry could make to the content, scope or grounds of the candidate account with the work it would require. If ordinary recovery answers the receiving question, use its result.

### RMP.10:2 - Problem

A recurring log entry can be mistaken for a reusable Method and a vivid recollection for a common practice. Counting accounts can conceal a variant used in a few settings or an important failure. Identify what evidence would distinguish the alternatives and when enough has been established.

For each consequential claim, identify its supporting evidence, what could count against it and which uncertainties affect the intended use.

### RMP.10:3 - Forces

| Force | Tension |
| --- | --- |
| Tacit contribution | Important cues and judgments may be absent from records, while elicitation can distort them. |
| Heterogeneity | Differences among performers and settings can distinguish variants. Sampling further examples of the same conditions may add little relative to its cost. |
| Contradiction | Variants may be real, while some disagreement is error or incomplete evidence. |
| Tool visibility | An event log can identify the events and fields it captured. Coordination or intent may require evidence beyond those fields. |
| Further discrimination | A case withheld from account development can test a prediction under new conditions. Record the predictions before examining the case and weigh the expected contribution against the cost of obtaining it. |
| Specialist burden | A consequential reconstruction may justify sampling and analysis across several sources. Ordinary recovery can be sufficient for a narrower use. |

### RMP.10:4 - Solution

If the evidence strategy remains open, RMP.2 helps choose a design or a justified stop. Use an adequate supplied design or trace directly. RMP.3 addresses operational choices and RMP.4 the actual observations, elicitation records and logs with their access conditions. Here connect each uncertainty about a reusable practice to evidence capable of resolving it. Keep a variant tied to its setting when the evidence supports the difference, and report the account the combined material warrants.

Arrange the evidence by the claims that matter to the receiving question. Identify each source’s contribution, examine disagreements in their settings, and select a further check when the result it can provide warrants the effort. Return the scoped accounts or the narrower conclusion that the material supports.

#### RMP.10:4.1 - Pattern-Use Unfolding

1. **Identify the use and the unresolved claims.** What matters about the intended result, entry conditions, reusable operations or invariants, cues and judgements, participants, capabilities, information, artifacts, support, variation, recovery or stopping conditions? Include the aspects needed for the question.
2. **Connect each claim to evidence.** State which observations could support or contradict the claim, distinguish variants or justify a narrower conclusion. Explain how the proposed evidence could discriminate among those outcomes.
3. **Sample for relevant variation.** Select cases that could discriminate among accounts. Relevant differences may include success or failure, routine or exceptional work, performer, setting, tool or provider. Look for cases that could challenge an account developed on a convenient sample. If access prevents that comparison, limit conclusions accordingly.
4. **Use each form of evidence for its claim.** Observations and artifacts can establish overt actions and results, CDM can recover recalled critical-incident judgements, and event-log analysis can establish recorded recurrence and deviation. Use contextual observation or protocol elicitation for a specified gap, allowing for the risks of that method.
5. **Trace claims to occurrences.** Identify the occurrence behind each consequential observation, using existing records where adequate. Preserve important missing fields, observer effects, limits of recall, tool coverage and source access. Then determine what can be generalized across occurrences.
6. **Examine contradictions in context.** Compare performer, setting, outcome and evidence form. Correct an established error. Where the conditions account for the difference, state the supported variants and their scope. Where its explanation remains open, retain plausible rivals, narrow the claim or describe the observed events.
7. **Decide whether to obtain more evidence.** Identify what remains unresolved and which attainable result could matter. Include access, practitioner capacity, delay and the whole cost of acquisition. If a check of prediction or transfer justifies a held-out case, state each serious rival’s predictions about cues, decisions, variation and result before inspecting it. To interpret a completed check, compare the observations with predictions documented before the case was seen. For another claim, a source comparison or targeted elicitation may be more informative. Use sufficient existing evidence or state the limit if the needed check is out of reach.
8. **Finish at the supported scope.** Return the accounts and the uncertainties that bear on their use. Rivals can remain when choosing between them would add nothing material to the question. If an important uncertainty remains, state the resulting limit and, where a use is proposed, whether it needs narrowing or deferral. The supported result may be a Work description, a local workaround, tool behavior, or an unresolved grouping of events.

#### RMP.10:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| receiving question | The situation and intended use, the candidate accounts and what remains unresolved. For a decision, include its consequences. |
| claim-to-evidence matrix | For each material claim, identify what observations could support, contradict or narrow it, distinguish variants, and show when the evidence will answer the question. |
| sample and occurrences | Relevant variation, the occurrences examined, source access, missing fields and limits of the evidence. |
| synthesis | Report the accounts and their scope, the variants or rivals retained, how the evidence explains any disagreements and what remains unresolved. Attribute the steps that combined the sources. |
| further checks, when relevant | The open claim, the contribution a check could make and its cost. For a completed check, give the result and remaining uncertainty. For a held-out case, distinguish predictions made before inspection from what was observed and revised. |
| return | The scoped accounts or narrower result, its evidence and limits, and the conditions for reconsidering it where relevant to use. |

#### RMP.10:4.3 - What Changes in Practice

Teams can distinguish what a sequence records from a candidate explanation of the practice, and what an interviewee recalls from what recurred. A comparison across settings can yield two supported variants. The receiving practitioner can use that result without having to infer a universal rule.

### RMP.10:5 - Archetypal Grounding

#### RMP.10:5.1 - Ordinary `A.3.1.MR` Stop

Suppose a maintenance team has six calibration Work records linked to their sources. They use the same released instruction, input schema, equipment configuration, decision authority and meaning of the result. One failed record shows the missing-input stop described by the candidate account. The team needs a source-traceable account to compare two instructions. No unresolved cue, variant or question about transfer bears on that comparison.

`A.3.1.MR` returns the provisional candidate account for this use, its sources, any substantive rivals and significant limits. That result suffices for the instruction comparison. Interviews, process mining or a held-out prediction would add effort without resolving a relevant uncertainty here.

#### RMP.10:5.2 - Genuine Escalation: EC-417 Evidence Reconciliation

In this constructed case, ordinary records leave open whether internal and supplier-originated evidence reconciliation follow the same rule or require different branches. The distinction matters to evidence closure on EC-417. Case access and practitioner capacity make a larger inquiry worthwhile. The team uses twelve cases to develop accounts and reserves a thirteenth to discriminate among them.

- four firmware-only and four internal harness-plus-firmware releases accepted versioned provisional pinout evidence before safety closure;
- four supplier-originated releases required signed evidence at closure;
- four reconciliation boards were observed;
- CDM probes involved two supplier, two software, one hardware, and one safety practitioner; and
- a thirteenth supplier-originated change was reserved unseen for the held-out discriminator.

| Evidence move | Scenario contribution | Limit retained |
| --- | --- | --- |
| observation and artifacts | Observed evidence versions, board records, integration bundles, approval states and closure results. | These establish what was visible in the cases examined. Population rates and unrecorded judgements require other grounds. |
| CDM probes | cues, considered options, judgments about provisional versus signed evidence, and counterfactual reflections in critical incidents | retrospective recall and interviewer effects remain |
| event-log analysis | Recorded recurrence and deviations in evidence-version, integration, approval and closure events. | Interpret the fields by their event semantics. Inferring intent or a reusable rule needs appropriate evidence. |
| expert synthesis | Choice of twelve development cases and one held-out case, an internal/supplier split, the contradiction rule, the test of rivals and the stopping judgement. | These are the reconstruction team’s choices in this example. |

Before inspecting the thirteenth case, the team recorded three rival predictions:

| Account or rival | Cues and decision predicted | Variation and result predicted |
| --- | --- | --- |
| `C-Evidence-Reconcile-Internal` applied beyond its observed scope | internally controlled versioned evidence would be the decisive cue; the internal reconciliation role could decide the branch without a distinct supplier approval | supplier origin would not change the branch; closure could proceed from the internal reconciliation result without signed supplier approval |
| `C-Evidence-Reconcile-Supplier` | supplier-owned configuration and restricted geometry would be decisive; supplier responsibility and signed approval would remain required for closure | reversible early integration could occur, but a signed-delta comparison and affected verification would precede either closure or an explicit missing-approval stop |
| `R-Rig-Capacity-Only` | Lack of rig capacity would trigger the hold and the decision to wait for the next slot. | The same branch would apply to internal and supplier changes, and the hold would clear when rig access returned. |

In the held-out case the team found supplier-owned geometry, restricted provider access and available rig capacity. The team allowed reversible early integration and withheld closure pending signed supplier approval. It required a signed-delta comparison and one affected verification, then closed after approval arrived. Those observations fit the supplier-scoped predictions. The hold despite available rig capacity contradicts the capacity-only rival for this case. The requirement for supplier approval contradicts extrapolating the internal account to this case.

Retain `C-Evidence-Reconcile-Internal` for the eight internal cases and `C-Evidence-Reconcile-Supplier` for the supplier-owned configuration with the signed-evidence branch. Rig availability remains a support condition. Evidence about the approval requirement distinguishes the accounts even though internal cases were more numerous. The one held-out supplier case leaves transfer to other suppliers, other configuration classes and cases of missing approval uncertain. The result is a pair of candidate accounts. Identification of a Method, effectiveness and population frequency would each need further grounds.

#### RMP.10:5.3 - A Specialist Programme Can Finish without a New Case

A retired repair service used two routing practices. Ordinary `A.3.1.MR` recovery from mixed logs and instruction editions leaves two possibilities for an urgent route, a repeatable cue-based branch and a supervisor override. A museum archive wants a qualified comparison of these accounts for the final year of the service.

Distinguishing the missing cue would change the archive’s comparison enough to justify the source work. The team selects dated routing sheets and critical-incident interviews with two available former dispatchers. The sheets record whether replacement stock was present. The logs record the chosen route. Linking both to the same occurrences shows that the disputed route accompanied absent stock in the accessible cases. Both dispatchers recall using the stock cue, and each describes an exception that required a supervisor. The sheets and logs support the recorded association. Attribute the recalled reasons and exceptions to the interviewees, within the limits of recall.

The archive can compare a stock-conditioned candidate branch and a reported supervisor exception with the earlier instruction. Return the source links, limits of recall and gaps outside the accessible cases. The service has closed. A new simulation would examine present performance under changed conditions. It could not supply an observation of the disputed historical occurrences.

The reconstruction answers the archive’s question at the supported scope. If a later operator proposes reusing the branch, examine its fit for the new conditions and what the earlier evidence can support there.

### RMP.10:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| trace bias | A recorded sequence is treated as a complete description of the Method. | Establish what the log recorded and identify any further grounds the claim requires. |
| interview bias | A memorable explanation is treated as sufficient proof of a general practice or its cause. | Establish which incidents the interviewee reports and what their account can support given its scope and the limitations of recall. For a stronger recurrence or causal claim, identify any further evidence it needs. |
| majority bias | The largest variant erases a competent minority or setting-specific branch. | Resolve contradictions by performer, setting, outcome, and evidence form. |
| method-brand bias | The name of one evidence method is taken as authority for the whole synthesis. | Attribute each sourced operation and identify the reconstruction team’s contribution. |
| programme bias | The team keeps collecting cases after the question has an adequate answer. | Tie sampling and stopping to the receiving question and the consequential claims still open. |

### RMP.10:7 - Conformance Checklist

- [ ] Ordinary recovery or its supplied result leaves a reconstruction question important enough to warrant the specialist work.
- [ ] The matrix shows what evidence could distinguish the consequential claims and why the selected cases or sources cover the relevant variation.
- [ ] Each selected form of observation, artifact, elicitation, log analysis or synthesis contributes within its evidential limits.
- [ ] Claims of actual performance can be traced to the corresponding occurrences.
- [ ] The treatment of contradictions reflects their scope, evidence and remaining uncertainty.
- [ ] Any further check addresses an uncertainty that matters to the question and has an attainable contribution worth its cost.
- [ ] For a completed held-out check, the record distinguishes the predictions made before inspection from observations, surprises and revisions.
- [ ] Material variants and rivals have an identifiable scope and evidential basis.
- [ ] If the evidence establishes only an occurrence, local workaround or tool behavior, the result says so. If the observed activities cannot yet be grouped into a candidate Method account, the grouping remains open.
- [ ] The conclusion distinguishes occurrence evidence, a proposed reusable account, a MethodDescription, identification of a Method and any claim about causes.

### RMP.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Mine the log and recover the Method.” | Establish the events and declarations actually recorded. Use the matrix for any unresolved question about intent, tacit work or context. |
| “Interview experts until their stories converge.” | Sample for variation relevant to the receiving question. Retain consequential disagreements, limits of recall and supported minority variants. |
| “Use every evidence form.” | Choose the sources that can establish or discriminate among the material claims at a justified cost. |
| “A specialist programme must always obtain another unseen case.” | Select a further check for a material unresolved claim. Finish on sufficient evidence or report the limit on the conclusion. If a proposed use depends on missing evidence, narrow or defer it as appropriate. |
| “The held-out case fits after we revised the account.” | Record predictions before inspection. Report departures from them and identify any post-inspection revision. A fresh prediction test requires evidence withheld from that revision. |
| “The reconstructed account is now an admitted Method.” | Report the account at its supported scope. Use `A.3.1` if the work also requires Method identification. |

### RMP.10:9 - Consequences

The receiver gets candidate accounts tied to the evidence for each claim. The reconstruction can preserve distinct variants or establish that the sources support only a record of local work. Either can answer a consequential question about practice.

Specialist sampling, access and analysis take effort. Even a well-conducted inquiry may establish only a local observation or a limit on what can be recovered.

### RMP.10:10 - Rationale

Overt action, logged recurrence, recalled judgement, tacit coordination and variation across settings present different evidential questions. Match each consequential claim to sources that can answer it. The matrix, comparison by scope and stopping conditions make a combination inspectable where several sources are needed.

### RMP.10:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.3.1.MR` | Recover a provisional account from occurrences, with its sources, substantive rivals, useful distinguishing questions and limits. A narrower result can be sufficient. | Enter RMP.10 when the receiving question still needs a larger programme and its attainable contribution warrants the effort. |
| Klein, Calderwood and MacGregor, [Critical Decision Method](https://doi.org/10.1109/21.31053) | Retrospective critical-incident probes for recalled cues, options, judgements and counterfactual reflections. | Use these for the experience and reasoning reported by the participant. Logged events, recurrence, population rates and causes each require evidence bearing on that claim. |
| IEEE Task Force, [Process Mining Manifesto](https://www.tf-pm.org/resources/manifesto) | Discovery, monitoring and conformance analysis over recorded event logs. | Use the semantics and coverage of the fields. Intent, tacit contribution, Method identity and causal explanation each need their own grounds. |
| Ordinary observation and artifacts | Evidence of overt occurrences and their results. | Identify what the observation or artifact covers, including its access, observation scheme and time window. |

RMP.10 combines the claim matrix, sampling for relevant variation, comparison of contradictions by scope, selection of further checks and a stopping judgement. Reconsider the combination if a source method changes an operation it supplies, or if a representative use shows that the specialist work adds too little to the account or its intended use for its cost.

### RMP.10:12 - Relations

- Use RMP.2 for an open design choice, RMP.3 to develop or assess its operationalization, RMP.4 for the material actually available, and RMP.5 for an unresolved question about the inference. Use adequate supplied results directly. RMP.9 addresses a difficulty with the research Method itself.
- Use the ordinary recovery supplied by `A.3.1.MR` directly when it answers the question. Its remaining evidential limits help define a possible specialist inquiry.
- `A.15.1` governs any claimed Work occurrence; `A.10` governs evidence paths and provenance; `A.3.1` alone governs Method identification.
- C.39.RP can retain a candidate account provisionally in a repertoire and keep other material in its appropriate role. A.3.1.QM can qualify an identified Method or a candidate Method account while preserving that status.
- For later description, support, trial or architecture work, use the account and evidence within the conditions they cover. Identify the additional contribution needed for a stronger use.
- RMP.11 addresses how and why a Method architecture differentiated. Use historical sources for what changed and appropriate discriminating evidence for a proposed cause. A candidate account from RMP.10 may contribute to that inquiry.

### RMP.10:End


## RMP.11 - Explain Method History with Discriminating Evidence

> **Status:** Stable

> **Type:** Method pattern
>
> **Primary working result:** a **differentiation account** of a dated change in a Method, family or relation among Methods. For an explanatory question, identify the proposed links, serious rivals, diagnostic observations and degree of support. If a use requires causal reliance, give a separate `C.28` causal-use support result. A present architecture decision requires its own criteria and authority.

### RMP.11:0 - Use This When

Use this method to investigate how an identified Method, an independently established family or a named relation among Methods changed. You may want to know when a variant appeared, why a contribution separated, why a provider or profession retained a form, or how an environmental change affected practice. Establish what happened before deciding how well the evidence explains it.

Identify the Method, established family inclusion or relation at issue, the change and the period. Ask whether the recipient needs its chronology, evidence comparing explanations, or support for a specified causal claim. If a current decision uses that history, identify which conclusion it needs.

A first useful result may be a dated sequence with its sources and limits. For causal reliance, specify the question, claim kind, rung of the causality ladder and support required.

A local name can identify candidates for investigation. Establish professional family membership from independent evidence. If ordinary chronology answers the question, use it directly. Use RMP.11 to determine what the documented changes or competing accounts support. Popularity can help locate a diffusion question. When a present architecture choice also needs the history, assess that choice by its own criteria and authority.

#### RMP.11:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| explanandum | The differentiation to explain in an identified Method, an independently established family inclusion or a named relation among Methods. |
| differentiation account | A dated account of the change and its evidence. For an explanatory inquiry it includes link claims, rivals, diagnostic observations, support grades, limits and conditions for reconsideration. |
| descriptive sequence | Dated editions, evidence of Work, variants, disappearances and decision points for the period in question. |
| link claim | A proposed connection among a pressure or change, an affected actor or carrier, a response or variation, its selection or retention, and the resulting change in a Method or its relations. |
| rival | A materially different account such as constraint, provider/tool availability, regulation, authority, diffusion/fashion, recording artifact, redesign, or survivorship bias. Rivals may coincide. |
| causal-use support result | A separate `C.28` result naming the question, claim kind and rung, with references to the findings that supply the required support and to the assessment of common threats. Its verdict identifies supported and unsupported uses, limits, time window and grounds for reconsideration. |
| non-causal observation or hypothesis | An observation or proposed association reported at its supported scope. It may help design a bounded probe. |
| downstream architecture decision | A separate authorized choice with its own criteria, conditions for stopping and resource burden. Any causal premise it uses must fall within the causal-use verdict. |

### RMP.11:1 - Problem Frame

An account of professional Method change relates variants recorded in successive sources to changes in institutions, tools, regulation and local Work. It examines deliberate redesign, diffusion, fashion, retention and loss. Questions about variants and selection help develop competing accounts. Process-tracing research supplies methods for examining the sequence within a case, rival explanations and diagnostic observations.

Use C.28 when an inquiry or decision relies on a causal part of the historical explanation. An established sequence can support description and a hypothesis. To claim what an intervention would do, establish the required support for the interventional use.

### RMP.11:2 - Problem

A pressure can precede a change for several reasons. Search frequency can measure attention, and institutional promotion can document publicity. Where the question concerns adoption, seek evidence of use. In an account of historical alternatives, look for abandoned variants that surviving editions omit. A claim of professional family membership needs grounds beyond a local grouping.

A historian can report an established change while its cause remains unresolved. If a decision needs the cause, identify and assess the evidence for that stronger claim.

### RMP.11:3 - Forces

| Force | Tension |
| --- | --- |
| Useful history | A dated account can answer when a change occurred or expose an alternative that matters to a present use. Select the chronology for the historical question. |
| Diagnostic depth | An observation can favour one account within a case. Identification and estimation require grounds specific to the causal use. |
| Evolutionary language | Variation, selection, retention and loss suggest questions. Establish a proposed causal link from the relevant evidence. |
| Causal cost | Description or a hypothesis can answer some questions. A use that depends on an effect can require substantially more work. |
| Present authority | History can inform a choice. A decision about today’s architecture also needs its own criteria and an authorized decision-maker. |

### RMP.11:4 - Solution

Use surviving records and their access or loss conditions from RMP.4, and an applicable corpus and account of source dependence from RMP.7 when needed. To explain differentiation, identify competing accounts, determine what observations could distinguish them, and weigh findings in light of the sources already used. A dated sequence may answer when the change happened. For causal reliance use the separate C.28 assessment.

Establish the dated changes. For an explanatory question, compare plausible accounts using observations that can distinguish them. Apply `C.28` when a claim or decision calls for causal reliance, and identify the scope of each result.

#### RMP.11:4.1 - Pattern-Use Unfolding

1. **Bound the explanandum.** Identify the Method under `A.3.1`, an independently established family inclusion or a named relation among Methods, and the change at issue. Use a local grouping to locate candidates. For a claim about professional membership, establish it separately.
2. **Identify the historical use.** State whether the question is when the change occurred, what the evidence suggests about the reasons, or which causal claim it supports. For causal reliance, specify the `CausalUseClaimKind`, target `CausalityLadderRung`, relevant comparator or intervention and proposed links. Return a dated account when it supplies the requested result.
3. **Establish the dated sequence.** Recover the source editions, Work evidence, appearances, disappearances, abandoned variants and decision points pertinent to the change. Use the resulting timeline for chronology or as an index to evidence for an explanation.
4. **Propose explanatory links where needed.** Identify the pressure or environmental change, the affected actor or carrier, response or variation, selection or retention, and resulting Method or relation change. Use *mechanism* in the cited source’s sense unless a distinct `A.6.1` `U.Mechanism` has been identified.
5. **Identify serious rivals.** Consider demand, constraints, tool or provider availability, regulation, authority, fashion, diffusion, recording changes, deliberate redesign and survival of the records where they fit the case. State which accounts compete and which contributions could coexist.
6. **Derive diagnostic observations.** What dated records, version differences, decisions, Work evidence, interviews, abandoned variants, negative cases or cross-setting contrasts would be more expected under one account than another? Use existing material or obtain additional evidence when warranted. Preserve provenance and source dependence. Before grading the link claims, compare the evidence as described in :4.4.
7. **Assess a named causal use through `C.28`.** Identify the question, claim kind, rung, applicable evidence paths and data regimes, specialist findings, common threat screen, verdict, supported and unsupported uses, limits, evidence window and conditions for reconsideration. Use the results that actually supply the required support. An unresolved relevant threat or missing required identification, bound or estimate limits the verdict for that particular use.
8. **Return the results at their supported scope.** Mark differentiation claims as observed, source-supported, inferred, expert-estimated, contradicted or missing, and retain material rivals. Identify any causal-use result separately. For a present choice, the authorized decision-maker may rely on causal conclusions within the verdict. If the verdict is `unsupported` or `undecided`, a separate non-causal observation or hypothesis may still justify considering a bounded trial.

#### RMP.11:4.2 - Record the Results

| Result | Required content |
| --- | --- |
| differentiation account | The change and dated sequence, with source editions, Work evidence, grades and limits. For an explanation, include the proposed links, rivals and diagnostic comparisons with their assumptions and source dependencies. Identify evidence that could materially revise the result. |
| causal-use support result, when needed | Identify the question, claim kind and rung. Cite the findings supporting its components and the common-threat assessment. Give the verdict, the causal uses it supports or rules out, its limits and evidence window, and the changes that would warrant reconsideration. |
| non-causal observation or hypothesis, when needed | Identify it separately, state its descriptive grounds, any bounded use in a design, the inferences it cannot support and any changes that would warrant reconsideration. |
| use by a downstream decision, when applicable | The result and the reliance it supports. Authority and criteria for the decision belong to the party making it. |

#### RMP.11:4.3 - What Changes in Practice

A dated account can recover forgotten variants and identify competing explanations. A limited causal verdict tells a decision-maker which reliance lacks support. A separate non-causal observation can still inform an authorized reversible probe.

#### RMP.11:4.4 - Weigh Historical Evidence between the Actual Accounts

Distinguish the reliability of a source from the diagnostic weight of its contents. A reliable fact expected equally under all serious accounts can establish the sequence while leaving their relative support unchanged. A potentially discriminating statement may carry little weight if its date, authorship or relation to the events is uncertain. Use these judgements when grading claims in :4.1.

1. **Compare the actual accounts.** For the same finding, ask how expected it would be under each serious account given the evidence already used. Explain the difference. If two causes can operate together, compare their proposed contributions or consider a combined account.
2. **Examine how the finding became available.** Distinguish the event from a later assertion. Ask what the source could observe, what would be recorded and how records were selected and preserved. Absence can weigh against a proposed event when that event should have left a record in the material actually examined.
3. **Identify new information and its origin.** A brochure, an interview repeating it and an article citing the interview can transmit one assertion. Assess what each adds given the earlier evidence. A new source date or an independent Work observation can add information even within the same archive.
4. **Return a conditional comparison.** State which findings favour which accounts and under what assumptions. Report unresolved rivals when the relevant observations are equally expected or source uncertainty defeats discrimination. Examine whether the preference survives plausible changes in coding, selection, dependence or weight of a finding. If it does not, describe that sensitivity. If the question needs a numerical comparison and the observation model and assumptions warrant it, use a quantitative analysis.
5. **Reconsider earlier findings when the account changes.** A new actor, date or proposed mechanism can change what earlier evidence implies. Compare the revised account with the relevant prior corpus and the new item, accounting for dependence.
6. **Identify the use the evidence supports.** A comparison can yield a scoped historical hypothesis or identify a worthwhile further inquiry. For causal reliance, supply the relevant findings and limits to `C.28`. If a revised premise mattered to an existing repertoire or decision, trace that reliance in C.39.RP, A.3.1.QM or C.32.MWA.PP. A current Method can retain a qualification that rests on independent evidence.

### RMP.11:5 - Archetypal Grounding

#### RMP.11:5.1 - Descriptive Stop

Suppose a design office needs to reconcile names and source editions after drawing signoff differentiated. For this example, A.3.1 identification and A.3.1.MV variant qualification already establish `M-Signoff-0` and local variants `M-Signoff-E` and `M-Signoff-M`. All return approve or reject for a drawing. The electrical variant requires clearance and harness-revision checks, the mechanical variant load-case and fit checks. Each withholds approval when its required check is absent. These are independently established differences in the local Methods. The question here concerns the timing of their documentation and use.

The office needs to establish when the different checks were approved and used in the surviving records, and when separate electronic forms represented them. Dated instructions and Work records can answer those questions even if the first-ever use is unknown.

The case also identifies `ElectricalReviewer-E` and `MechanicalReviewer-M` as Agents for the respective checks under A.13, and their 9 and 18 April occurrences `WE7` and `WM4` as Work under A.15.1. They enacted `M-Signoff-E` and `M-Signoff-M` using the respective E1 and M1 instructions. The following records form the source set.

| Date and source | Recoverable fact and limit |
| --- | --- |
| 15 January 2024, signoff instruction S3 | A common instruction covers both drawing types and requires the presence of evidence. Neither local variant’s distinct test-and-withhold rule appears in S3. Whether somebody used either check earlier remains open. |
| 4 March, exception log X2, and 11 March, proposal P1 | X2 records two returned drawings, one lacking electrical-clearance evidence and one lacking the mechanical load case. P1 cites these exceptions, proposes the two domain-specific rules and retains common signoff with expert escalation as an alternative. This establishes a stated reason for the proposal. |
| 2 April, approval A14 and instructions E1/M1 | A14 approves the two local variants for the respective drawings. E1 and M1 specify different checks and returns for failure. A14 leaves the common-with-escalation proposal unselected. The deliberation minutes are missing. |
| 9 and 18 April, signoff Work WE7/WM4 and their annotated results | In WE7, ElectricalReviewer-E followed E1 and withheld approval for missing clearance evidence. In WM4, MechanicalReviewer-M followed M1 and withheld it for a missing load case. These records establish two enactments before the forms separated. Earlier occurrences and the extent of uptake remain open. |
| 6 May, PLM migration note T2 and form edition F2 | F2 introduces separate electronic forms and names for approval records. T2 states that they carry the E1/M1 rules already in use. The change documented here concerns how those rules are represented. |

Before examining the April records, the office considers two accounts. **R-demand** attributes the proposal and selection to domain-specific omissions. It predicts a problem record, a response proposal and distinct checks before migration. **R-carrier** attributes the apparent split to the May change in recording or naming. It predicts unchanged checks under the new forms. The March returns and proposal make R-demand plausible. The searchable PLM history begins with F2, which makes a recording change plausible until the earlier instructions and Work are examined.

E1/M1 specify distinct checks and WE7/WM4 record their enactment in April, before F2. That contradicts the strong R-carrier claim of a naming-only change in May. The records fit R-demand. They leave open why the office chose separate rules over common signoff with escalation and what other pressures contributed. The deliberations are missing. A within-case inquiry might investigate the missing link through further sources. A possible contribution of the carrier to later retention also remains open.

`DA-Signoff-Differentiation-1` returns these grades and limits:

| Claim | Grade and allowed use |
| --- | --- |
| The common and domain-specific instructions differ in the named required checks and stops. | **Source-supported** by S3/E1/M1; Method identity and variant qualification remain the separate case premises. |
| Separate rules were approved by 2 April and enacted in the named April occurrences. | **Source-supported** by A14 and WE7/WM4. The dates bound the documented approval and two uses. The first-ever use and extent of uptake remain open. |
| The March exceptions were a stated reason for proposing the variants. | **Source-supported** by P1. The effect of those exceptions on selection needs its own evidence. |
| The split was merely a May renaming with no earlier semantic difference. | **Contradicted** by the April instructions and Work records. |
| Demand caused selection over common signoff with escalation, or the carrier contributed to later retention. | **Missing causal support** for these links. The deliberation evidence and evidence of later continuation are incomplete. |

In `DA-Signoff-Differentiation-1`, retain S3 as the common predecessor account, E1 and M1 as different variant descriptions and F2 as their later forms. The dates and observed signoffs answer the reconciliation question. The first occurrences and reasons for selection remain unresolved. An earlier instruction, a deliberation record or contrary Work evidence could revise the relevant claim. A request to choose a present architecture would introduce a different decision.

#### RMP.11:5.2 - Causal-Use Branch and Non-Causal C.32.MWA.PP Consumption

Suppose a team considers release alternative B2 from C.32.MWA.PP:5.3 for EC-417. B2 starts integration from a specified provisional supplier-evidence edition and reconciles it with signed evidence at the safety-closure checkpoint thirteen days later. Supplier preparation shares the reconciliation workload. Signed evidence, separate safety and release decisions, and the provisional evidence history are required. The supplying comparison gives capacity, confidentiality, assignments, permissions, recovery and trial-entry conditions. Here the question concerns the possible relationship of checkpoint timing to later reopenings. The four results below serve different uses.

- `DA-EC417-CadenceDifferentiation-1` records the observed co-occurrences. The dates, variants and selection history needed for a full differentiation account remain incomplete.
- `CUR-EC417-CadenceEffect-1` is the causal-use support result;
- `DC-EC417-CadenceMismatch-1` is a non-causal timing/co-occurrence hypothesis; and
- `AD-EC417-B2-Trial-1` is the receiving C.32.MWA.PP architecture decision.

The question in `CUQ-EC417-CadenceEffect-1` is whether starting provisional-evidence reconciliation in the early integration slot would reduce mismatch-related reopenings compared with starting at the signed-evidence checkpoint thirteen days later, for EC-417-like releases under the stated team, supplier and change class. Its `causalUseClaimKind` is `causalEffectClaim` and the target rung is `interventionalActionRung`.

The support components are `evidencePathRefs=[EP-EC417-BundleSequence-20, EP-EC417-RigAvailability-20, EP-EC417-QuarterlyCadence-2]` and `empiricalDataRegimeRefs=[EDR-EC417-NaturalReleaseHistory]`. Identification and an estimate for the named effect are missing.

Common threat screen `CTS-EC417-CadenceEffect-1` records:

| Threat-screen field | Result |
| --- | --- |
| `causalUseQuestionRef` | `CUQ-EC417-CadenceEffect-1` |
| `interventionWellDefinedOrConsistency` | `liveThreat` |
| `temporalOrdering` | `clear` |
| `exchangeabilityOrConfounding` | `liveThreat` |
| `positivityOrOverlap` | `liveThreat` |
| `interferenceOrSpillover` | `liveThreat` |
| `selectionCensoringOrMissingness` | `liveThreat` |
| `measurementErrorOrConstructShift` | `liveThreat` |
| `transportToTarget` | `liveThreat` |
| `routedThreatRefs` | `[]` |
| `resultingSupportBoundary` | `unsupported` |

The screen leaves the named threats unresolved, and the C.28 verdict is `unsupported`. The `supportedUse` is to flag the limit on interventional reliance. The `unsupportedUse` includes attributing the reopenings to cadence mismatch and claiming B2 will reduce them. The evidence window covers the named twenty releases and two earlier cases for this team, supplier and change class. Reconsider the verdict if a governed comparison, replayable identification or supported bound distinguishes reconciliation timing while controlling or explicitly modelling rig availability, approver capacity, outcome definition and evidence access.

`DC-EC417-CadenceMismatch-1` retains the observed timing and co-occurrence as a trial hypothesis and design constraint. With evidence of capacity, confidentiality, authority and reversibility, `AD-EC417-B2-Trial-1` selects a bounded B2 trial. `SafetyReviewer-17` performs `W-SafetyEvidenceDecision-17` under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17` for the evidence condition. `ReleaseDecider-17` performs `W-ReleaseDecision-17` separately under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17` for branch entry and release disposition. The causal verdict marks a limit on the decision’s interpretation.

#### RMP.11:5.3 - A Dated Proposal Has More Weight than Repeated Promotion

Extend the constructed signoff history from :5.1, keeping the independently identified Method and variants. **H-response** says repeated domain-specific omissions contributed to selecting separate rules. **H-tool-only** says a provider’s form package induced the split and the omissions were cited afterward. Compare their support. Tool support may also have helped retain rules initially selected for other reasons.

An authenticated internal memo dated March compares separate rules with common escalation. It recommends separation because the named specialist would be unavailable. Its date precedes the earliest documented provider contact. A problem-specific recommendation at that point is more expected under H-response than H-tool-only. Its weight depends on the memo’s authenticity and role in the decision, and on the possibility of earlier provider influence outside the recovered records.

A budget approval cites the memo and establishes that resources were authorized. Its repeated rationale adds no independent account of the reason. A later brochure and three interviews repeat the launch narrative, showing that it circulated. Trial records were not routinely preserved. Even a well-documented trial might therefore leave no surviving record. Failure to find one adds little evidence against a trial.

Under these assumptions, H-response receives more support than H-tool-only. Provider influence and a mixed account remain plausible. That relative comparison can finish the historical inquiry. If the remaining question warrants more work, records of earlier contact and of the actual decision could distinguish the accounts further. A numerical probability or an effect of imposing the rules today would require evidence and assumptions for that use.

Now suppose an authenticated February provider proposal comes to light. The March memo is no longer earlier than all known provider opportunities. Reassess the memo and budget under the revised chronology, comparing a mixed account with tool-only influence and response to omissions. The memo still establishes its stated reason. Reassess a current repertoire or decision where it relied on the changed attribution. Retain the independently supported qualification of a local variant.

### RMP.11:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| chronology bias | Earlier and later events are described as cause and effect. | Establish the dated sequence. Assess explanatory links and use C.28 for a named causal use when one is at issue. |
| survival bias | The surviving materials omit abandoned or excluded variants. | Consider sources that could reveal those variants and state any consequential limits on coverage. |
| fashion-metric bias | Publication counts, search frequency or promotion are taken as direct measures of adoption or effectiveness. | Establish which attention or diffusion claim the indicator supports and what else could account for it. |
| family-label bias | A local grouping becomes a professional family explanandum. | Require independent family membership or explain named Methods and relations instead. |
| history-authority bias | A historical explanation is used as authority to implement a change. | For a current architecture decision, identify its criteria, authority, causal premises and conditions for stopping a trial where applicable. |

### RMP.11:7 - Conformance Checklist

- [ ] The explanandum is an identified Method, established family inclusion, or named Method relation change.
- [ ] The historical question and required scope of description, explanatory comparison or causal reliance are clear.
- [ ] The dated sequence preserves the source editions, Work evidence, variants, appearances, disappearances and decisions on which the account relies.
- [ ] Each proposed explanatory link identifies the relevant change or pressure, affected actor or carrier, response, selection or retention, and resulting change to a Method or relation.
- [ ] For an explanatory comparison, serious rivals and their expected observations guide the use or selection of evidence.
- [ ] Diagnostic weight reflects what each rival predicts given the existing evidence, how the sources arose and whether they repeat an earlier assertion.
- [ ] Differentiation claims carry grades and limits, and changed accounts prompt reconsideration of the relevant earlier evidence.
- [ ] Any causal-use result contains the complete current `C.28` identity, support, threat, verdict, use, window, and reopen fields.
- [ ] The causal-use result identifies which evidence or specialist findings support each component it relies on.
- [ ] The historical account, any causal-use verdict or non-causal hypothesis, and any subsequent architecture decision have identifiable grounds and scope.
- [ ] An `unsupported` or `undecided` result supplies no positive causal premise.

### RMP.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The pressure came first, so it caused the Method change.” | Establish what the dated sequence supports. For the proposed explanation compare link claims and rivals using diagnostic observations. Apply C.28 when the receiving use requires causal support. |
| “The timeline is the explanation.” | Use the timeline for the chronology. For a question about reasons, compare the expected evidence under the proposed links and their rivals. |
| “Process tracing proves the causal effect.” | Use process tracing for within-case diagnosis. For a causal use, apply C.28 and limit the verdict where required identification, a bound or an estimate is missing. |
| “Unsupported means the history is useless.” | Return the established sequence. If a distinct non-causal hypothesis is supported or useful to investigate, state it within its scope. |
| “The history tells us what to implement.” | Use the historical conclusion within its scope. Refer a current implementation choice to the party with the relevant authority when such a choice is needed. |

### RMP.11:9 - Consequences

The historical account can establish when a Method changed and restore forgotten variants. Evidence can favour some explanations over others or leave rivals unresolved. In a current decision, an authorized reversible probe may be justified from non-causal observations even when the proposed effect lacks support.

Comparing explanations requires source criticism. Assessing a causal use also requires examining the relevant threats. The best supported answer can be a dated account, a partial explanation or a stated limit on causal reliance.

### RMP.11:10 - Rationale

A dated sequence, support for a causal explanation and authority for a present choice have different grounds. A chronology can be established while attribution remains open. A non-causal observation can still identify a design constraint.

Variation, transmission, fashion, retention and loss can suggest hypotheses about Method change. Compare the observations each hypothesis predicts using process-tracing methods. Apply C.28 to identify the evidence required for a causal use, including identification or estimation when that particular question calls for it.

### RMP.11:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Stacey et al., [Methods as a form of engineering knowledge](https://doi.org/10.1017/dsj.2025.9) | Method knowledge, variation and loss in engineering contexts. | Use the conceptual history to frame a question. Specific causal attribution and authority for a current choice have their own grounds. |
| Collier, [Understanding Process Tracing, with 2019 addendum](https://polisci.berkeley.edu/sites/default/files/people/u3827/2011%20Collier-Understanding%20Process%20Tracing%20with%20Addendum.pdf) | The 2011 treatment supplies within-case sequencing and diagnostic observations. The addendum develops relations among rivals and examines the limits of rigid necessity/sufficiency test classes. | Use this historical foundation with later work on inference and C.28 when a causal use is at issue. |
| Fairfield and Charman, [Explicit Bayesian Analysis for Process Tracing](https://researchonline.lse.ac.uk/id/eprint/69203/2/Fairfield_Explicit%20bayesian%20analysis_author_2017%20LSERO.pdf) and [A Dialogue with the Data](https://doi.org/10.1017/S1537592718002177) | Compare specified alternatives conditional on prior evidence, account for source dependence and reconsider existing evidence as hypotheses change. | These operations support qualitative comparison. Numerical probabilities require their own justified assumptions. Judge causal support and a present architecture choice separately. |
| [Fully specified Bayes factors for hypothesis testing and sensitivity analysis in process tracing, v2](https://arxiv.org/abs/2606.16683v2), 2026 preprint | Model-based evidence weights and sensitivity analysis can show how coding, selection and weighting affect a conclusion. | The binomial observation model and comparisons to one rival require substantive justification. Clustered dependence among sources limits the guarantees. Use the numerical procedure where these conditions fit. |
| Mahoney, [The Logic of Process Tracing Tests](https://doi.org/10.1177/0049124112437709) | Logic of weak, necessary-condition and strongly discriminating tests. | Use the test logic to assess particular observations, then compare the support for the links across the chain. |
| Current FPF `C.28` | The causal-use question, rung, support components, common threat screen, verdict, permissible reliance, limits and conditions for reconsideration. | Use the verdict within its specified scope. A downstream decision also requires its own criteria and authority. |

Reconsider the historical or causal account when a relied-on source changes the diagnostic comparison, an observed case exposes a consequential gap between historical and causal claims, or an intended use needs evidence the present account does not supply.

### RMP.11:12 - Relations

- Use RMP.4 for source relations and limits and RMP.7 for a corpus that accounts for dependent reports. RMP.5 can examine the inference from historical evidence. RMP.8 helps revise a changed knowledge claim and trace the uses that rely on it.
- Use `A.3.1` for Method identity and `G.5` for an established family or selector claim. A local name may help locate the candidates to examine.
- Use `A.10` for sources and evidence paths. When a relied-on premise changes materially, correct a known use directly if that resolves the issue. Use `A.10.1` when locating other affected uses or requalifying dependent claims together is needed. `C.27` addresses temporal claims, and `C.28` and `C.28.CM` causal support and the construction of a causal inquiry.
- C.39.RP can retain variants and lineages with the historical and causal support appropriate to each claim.
- C.32.MWA.PP can use the differentiation account, a causal-use verdict or a separately identified non-causal observation within its scope. The authority for the architecture choice belongs to its decision-maker.
- Cultural continuation and professional-history questions can have their own supported answers. Use those answers for a project decision where they bear on that decision.

### RMP.11:End


# Cross-Pattern Application



## RMP.Application:1 - APP-RMP-01 — Pump-P4 accelerated seal evidence

This constructed case follows a question about an accelerated seal test through RMP.1–RMP.8. Its stated conditions illustrate how the research result changes as different information becomes available.

Pump-P4’s reliability council asks whether a high-temperature accelerated seal test supplies grounds for changing the maintenance interval. The maintenance authority makes the interval decision. Use qualified engineering and assurance results for the failure relation, test Method and criteria, and the applicable sources or authorities for the instrument, laboratory, safety, access and material.



### RMP.Application:1.1 - First fork — routine qualification, supplied answer, or research question

With RMP.1, identify what the council needs and what the available engineering, laboratory and field results already establish.

| Supplied situation | RMP.1 result |
| --- | --- |
| A qualified field failure mechanism, applicable acceleration relation, qualified test Method and instrument, criteria, and evidence-use rule are current. | Return routine qualification/validation to engineering or assurance and the interval choice to the maintenance authority. |
| Qualified existing evidence shows that the accelerated condition changes the dominant degradation mechanism for the stated use. | Report that finding and its scope. It answers whether the same mechanism can be assumed under those conditions. |
| Acceleration-induced mechanism change, installation damage, variation in material and exposure to field fluid remain serious rivals. Investigating their relation is the epistemic task. | If the research conditions hold, return a ResearchQuestionBrief asking whether the accelerated condition preserves the field mechanism-to-evidence relation within the stated envelope. Use an adequate comparison if one is already supplied. |
| A necessary source result, domain relation or condition of access is unavailable. | Identify the particular conclusion that remains open and what information or authority would settle it. Return that limit, or locate the appropriate source if resolving it is part of the task. |

For the research branch, state the receiving use, the proposed revision to the mechanism-to-evidence claim, materials and operating conditions, sources and rivals, required criticism, constraints and applicable specialist results. Distinguish what would answer the question from what warrants finishing with uncertainty. The maintenance authority retains the interval decision.



### RMP.Application:1.2 - Construct a comparison that can answer the mechanism question

The RMP.2 case begins with the rival mechanisms and an overall wear index. Two qualified references have the same index but different mechanisms. Matching index values therefore fails to identify a matching mechanism. The test can still measure wear for its ordinary purpose.

The laboratory has a mechanism-sensitive surface or chemical signature with a qualified interpretation. Compare accelerated and field-representative conditions while preserving material identity, assignment and the qualified damage range. Follow the operation on the reference records. State what agreement, discrepancy or an uninterpretable signature would establish. If material correspondence or signature discrimination is missing, identify the affected inference. Select the design when its informative result is attainable and warrants the work.



### RMP.Application:1.3 - Second fork — answer the current research-allocation question

For the question in the brief, use an adequate existing finding. If further research remains under consideration, compare attainable experimental, observational or model-based approaches with the course of commissioning no new study. Judge each by what it could resolve under the actual conditions.

| Changed supplied value | RMP.2 disposition |
| --- | --- |
| Applicable evidence meets the brief’s answer condition by supporting, narrowing or rejecting the proposed acceleration relation within the scope of the brief. | `EvidenceSufficientStop`. State the supported answer and any consequential limits or evidence that would revise it. |
| Domain engineering supplies the indicator relation, measurement feasibility, material identity, safe operating envelope and necessary authority. An experiment best distinguishes acceleration-induced mechanism change. | A `ResearchDesignDecision` selects the comparison and its criticism. Retain as a `PostSelectionNeed` a missing record locator or serialization detail only when its possible values leave that selection unchanged. |
| Two plausible results about the indicator’s discrimination would lead to different designs. | A `ResearchDesignHold` identifies the needed measurement finding, its source, the alternatives it affects, the outcome under each possible value, the work that must wait and what would permit it to proceed. |
| Evidence remains insufficient, and material, access or cost rules out any worthwhile attainable new study for this case. | `QualifiedNoNewStudy`. Give the allocation decision and its grounds, the remaining uncertainty or narrower answer, and any change that would warrant reconsideration. |

A hold identifies a missing value that can alter a design selection still needed. A decision against a new study can stand while the mechanism question remains unresolved. For a selected design, retain its comparison and limits. Use RMP.3 to specify any consequential operations that the design leaves open or to assess a supplied protocol.



### RMP.Application:1.4 - From the selected design to operational choices and actual trace

Suppose the team has the mechanism marker, measurement qualification, specimen plan, safe conditions and access. With RMP.3 it connects the comparison to the mechanism question. The protocol identifies each seal and material batch, assigned condition, measurement time and procedure, and the records needed to examine selection and missingness. Three readings of one seal give repeated measurements of one specimen.

Suppose the marker cannot distinguish thermal degradation from the competing field mechanism under the chosen conditions. Report the limit on the intended comparison. If a design for that distinction is still needed, return the result to RMP.2. A convenient wear score would need a justified relation to the mechanism question.

On the viable-marker branch, specimen P4-07 is damaged in handling before a planned observation. With RMP.4 trace its identity, allocation, available handling history, missing observation, intended exclusion rule and actual decision. Link the remaining measurements to their specimens. These records support examination of selection and missingness. Judge the scientific inference against the resulting data and its assumptions.

The protocol specifies the operations and scope of the comparison. The trace identifies what happened and which criticisms the available records permit. With RMP.5 examine the specimens, measurements and exclusion history under the qualified Method. Estimate or bound the effect of missingness when the evidence and analysis support that inference.



### RMP.Application:1.5 - From analysis to a relevant credibility examination

Suppose the available data and code reproduce the reported curve of a calibrated simulation. RMP.5 can establish the computational result and the missing inference from mechanism to field use. Repeating the calculation checks the computation. A claim about field behavior needs evidence of field applicability.

Use RMP.6 to establish what an earlier relevant examination showed, or to select a further one if worthwhile. If no informative examination is attainable, report the supported computational finding and the field limit. If independent qualified field material becomes available, compare the contribution and cost of a mechanism or validation study. A later result may support, narrow or defeat the field use. The maintenance authority makes the interval decision.



### RMP.Application:1.6 - From a corpus answer to the exact model return

Suppose four reports comprise two accounts of one accelerated study, an independent compatible test and a service-use account from different conditions. With RMP.7 retain extra detail from the second account and count two independent laboratory test contributions. Combine the compatible estimates when the statistical model and conditions justify it. Use the service account for the question it addresses. RMP.7 gives the numerical example and assumptions.

With RMP.8 compare the synthesis to the model’s claims. In this case the laboratory relation remains supported, transfer to service remains unestablished and a replacement-time prediction that relied on transfer loses its warrant. Identify the precise correction and retain the supplied engineering criterion. The RMP.8 model case develops these different outcomes.

The reliability council can use the bounded result. A qualified source answer, a limited synthesis or a precise correction can finish the research question. The council can consider a future field study on its own merits, and the maintenance authority retains the interval decision.



## RMP.Application:2 - APP-RMP-02 — ResidentStream-S17 salinity anomaly

In this constructed application, residents investigate a change in a stream. The same research criteria apply across institutional settings.

Residents observe increased salinity in urban stream reach S17. A public environmental or operational body needs an account of the anomaly. Use the applicable site, safety, measurement and data permissions, the laboratory’s qualified measurements, and the regulator’s authority for any regulatory response.

RMP.1 first distinguishes:

- established sampling against a supplied threshold, which can answer the monitoring question about current state. Apply a response rule if a further response is part of the task.
- a validated source or monitoring result that already answers the question about the specified anomaly, which can be reported directly.
- an unresolved question about road-salt transport, groundwater, an outfall change, seasonality or sensor drift. If the inquiry satisfies all four research conditions, frame it in a ResearchQuestionBrief.
- a missing measurement, source, site condition or permission that prevents a research-boundary judgement still needed. State which judgement remains open and what would settle it.

For a qualifying brief, use sufficient existing evidence. If the explanatory question remains open, compare an attainable field study across places and times, a synthesis of sources or a justified combination with the course of commissioning no new study. Apply a routine monitoring or instrument-repair method directly when it supplies the needed result.

| Changed supplied value | RMP.2 disposition |
| --- | --- |
| Current validated monitoring and source results already discriminate the bounded anomaly. | `EvidenceSufficientStop`. |
| The proposed space–time comparison distinguishes the serious rivals. Measurement validity, safe and lawful site access and suitable comparison reaches and periods are established. | Select the field or observational design. Defer only record-locator details whose possible values cannot change that selection. |
| Sensor validity, safe access, outfall records, or seasonal comparison availability can still eliminate or replace the field relation in a selection still needed. | `ResearchDesignHold` identifying the exact measurement, site, record or authority result. |
| The bounded evidence remains insufficient and the informative comparison is no longer obtainable, with no worthwhile current substitute. | `QualifiedNoNewStudy` preserves the observed account and unresolved explanation without commissioning a replacement study. |

Citizen researchers can use any of these branches. Obtain permission for site entry or sampling where required. The regulator or another responsible holder decides whether to order remediation using the applicable evidence and criteria.



### RMP.Application:2.1 - Preserve the comparison when the field situation changes

For the selected field design, RMP.3 specifies the reach and sample location, hydrological condition and time, requirements for the measurement and records of access, weather and calibration. Use a qualified existing measurement that fits those requirements, or define the operation needed to obtain one. The residents can use an applicable laboratory result directly.

Suppose the reference reach becomes inaccessible during an informative thaw while a downstream observation remains possible. Check whether an existing measurement covers the needed reference site, time and conditions. If none does, the original pair is incomplete. Preserve the downstream observation and the reason the reference is missing. If a new design is needed, use RMP.2. A dry-weather sample requires its own comparability grounds.

With RMP.4 trace raw indications, qualified measurements and chart values through sample identities, calibration, context and actual transformations. Distinguish a missed observation from an excluded value. On the branch with a missing reference, the downstream result and handling history remain available while the original pair is incomplete. Those data may already answer a narrower descriptive question.

If volunteers began before recording a protocol, use dated materials to establish what choices they made and when. Identify the basis of the reconstruction and any consequential gaps. To claim a prospective commitment, look for evidence of what was fixed at the time. Protect access details under the applicable conditions and identify which examinations the public summary supports.

RMP.5 can establish the downstream pattern while attribution to the proposed source remains unresolved. Without a qualified reference at the relevant time, more downstream readings cannot supply the original paired comparison. A matched observation in a later period can address a new question. Use RMP.6 to weigh that contribution and its cost if needed. A limited historical answer can finish without a new study. Responsibility for a response remains with the authorized body.



### RMP.Application:2.2 - Relate unlike contributions and return the limitation

For other catchment studies and accounts of participation, use RMP.7 to identify which questions each can answer. A similar chart from another catchment does not supply the missing local observation. A qualified cross-catchment comparison can support a transferable finding or a narrower shared pattern. Retain differences in contexts, source dependence and missing premises.

If a briefing attributes the anomaly to one source without sufficient support, use RMP.8 to correct that claim and retain the observed downstream pattern. Give the environmental recipient the resulting uncertainty. A synthesis of participation experiences can document participants’ accounts of distrust. Prevalence or effects of remediation require evidence for those claims. Data use and regulatory action remain subject to their respective authorities.



## RMP.Application:3 - APP-RMP-03 — Factory-closure historical transfer probe

Suppose a public narrative attributes a factory closure to one executive directive. An independent historian identifies the specific claim, available archives and testimony, source provenance and silences, rival chronology, access and harm constraints, and what would answer the historical question.

RMP.1 can yield an authenticated source answer, a historical ResearchQuestionBrief or a precise source or access limit. With RMP.2 use sufficient evidence directly, or compare historical source criticism and corpus synthesis with commissioning no new study. For a selected design, identify the discriminating sources and provenance it requires. If access or provenance could change a selection still needed, state the condition. If no worthwhile study is attainable, give that allocation result and what can be established from the surviving evidence.

For the chosen historical comparison, specify the document series and testimony, provenance, dates, access and transcription that can test the directive account against an earlier chronology. With RMP.4 distinguish personally inspected sources from catalogue descriptions. A qualified finding from an authorized custodian may establish specified contents or dates despite restricted personal access. Give the source and scope of that finding and what the recipient can examine. Preserve contrary material and explain transformations and source selection. If an earlier archive is inaccessible and no adequate result supplies its contents, its silence cannot show that no earlier decision occurred. State what the available material establishes and the limit on the intended comparison.

A different question asks how former workers experienced closure. A reflexive qualitative approach can refine a prompt after an encounter. Retain the change and its grounds. A population prevalence estimate would need a question and design for that quantity. Preserve the researcher’s contribution, permitted excerpts and discordant material, and use RMP.5 to examine the situated interpretation. For the earlier historical question, an authenticated pre-directive record of the same change can defeat the claim that the change first occurred after the directive. Its cause needs separate grounds. Use RMP.6 for a further corroboration or transfer test when the question warrants the effort.

Suppose several accounts attribute the closure decision to a public protest. With RMP.7 trace them to one retrospective memoir. An authenticated record dates that decision before the protest, ruling out that protest as the cause of that decision. The cause and any effect of the protest on later implementation remain open. With RMP.8 return the correction to the museum description that relied on the claim, via its responsible editor and under the source-access terms. The protest and earlier executive directive are distinct events.




## RMP.Application:4 - APP-RMP-04 — Retain the Method and correct its research consequence

Suppose a team completed an analysis under a suitable Method and found an error in its variance calculation. Start with the recorded computation and the applicable specification.

For the observations 2, 4, 6 and 8 in RMP.9, the specified sample variance is 20/3. The software used the denominator n and returned 5. The stipulated Method and receiving conditions still fit.

Use RMP.4 to locate the computation and its dependent material. A historical inquiry can report which denominator the implementation used and what any saved check of its repair established. If correction is commissioned, use RMP.9 to retain the suitable Method and correct its implementation. Use adequate prior checks or verify what is still untested. With RMP.5 recalculate affected analyses and with RMP.8 return any change to the content or grounds of a claim. An analysis record may suffice. Retain unaffected work.

If the programme now uses dependent observations or a different site-level quantity, assess the Method for those conditions. In RMP.9’s distinct site example, the expected contribution warrants a feasible comparison of interval procedures for the same estimand. Selection of the comparison leaves their performance open. Give the receiver the qualification the existing evidence supports and the remaining limit.




## RMP.Application:5 - APP-RMP-05 — Should a second approver reduce customer waiting?

Use this application when a workflow change raises a question about customer outcomes. Distinguish the outcome customers need from the indicator the organization records. The example shows how a manager can use process knowledge and arithmetic to frame the question and inspect a comparison. Use a qualified statistical design or analysis where that contribution is needed.

The branches, professional findings and numbers below are assumptions of a constructed case. They show what a manager can obtain and check in a specialist’s result. For another workplace, establish the design, sample and capability appropriate to that task.



### RMP.Application:5.1 - Find the question that matters

A quotations manager sees overdue offers and proposes a second approver. The manager distinguishes meeting the promised date from reducing the customer’s actual wait. Extending the promise can improve the first indicator with no change in the second. The manager chooses actual waiting time and specifies an acceptable limit for any increase in quotation errors.

The question is **whether a specified additional-approver arrangement would shorten the time from a customer’s request to sending the quotation.** Missing input and difficult calculations are other possible sources of delay. Existing evidence can identify an adequate repair, such as restoring a failed forwarding rule. [RMP.1](#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) can return that answer for a repair question. Here the causal effect of additional approval capacity remains open and matters to recurring staffing.

Keep three questions separate:

- **Where did these quotations wait?** Use event records or another adequate source for the actual intervals.
- **Which mechanisms explain the waits?** Consider approval delay, missing input, or both, with initial complexity and workload affecting them.
- **What would the additional-approver arrangement change?** This needs a justified comparison of intervention versions and outcomes.

[Constructing and challenging a causal model (FPF C.28.CM)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28cm---construct-and-challenge-a-causal-model) helps specify the proposed mechanisms and their observable implications. Use the evidence to judge the connections drawn in a diagram.



### RMP.Application:5.2 - Obtain records that preserve the needed distinction

The CRM date labelled “status updated” may refer to an administrative edit after the quotation was sent. Establish what the field recorded. A suitable prior validation can answer, or compare retained messages and approval records with their CRM entries. The comparison can establish when the field was updated and whether that time is suitable for measuring customer waiting. Estimating the effect of a second approver requires an intervention comparison.

For one constructed request, the retained records show:

| Event | Recorded time | Working time since the preceding event |
| --- | --- | ---: |
| Customer request received | Monday 09:00 | — |
| Sufficient customer input received | Tuesday 10:00 | 9 hours |
| Calculation completed and submitted for approval | Tuesday 14:00 | 4 hours |
| Approval completed | Wednesday 16:00 | 10 hours |
| Quotation actually sent | Thursday 10:00 | 2 hours |

The office counts weekdays from 09:00 to 17:00. The four intervals add up to 25 working hours, or 3.125 eight-hour days. Of that time, nine hours elapsed before sufficient input, four before submission, ten between submission and approval, and two between approval and sending. A CRM edit on Thursday at 11:00 would be another event.

Assess missing events, clock consistency, retrospective estimates, duplicate requests and the effort of recording. Use an existing validation or try the recording method where needed. If the history is missing, state the limit. Prospective recording can serve later cases when worthwhile. When both seven and eight hours have been stored as “one day”, more copies of the rounded values cannot recover the missing distinction.

[RMP.3](#rmp3---operationalize-the-research-design-without-replacing-the-question) connects the specification to the question, and [RMP.4](#rmp4---preserve-a-criticism-ready-research-trace) preserves what happened and what the evidence permits a recipient to examine. Compare intended recording with consequential departures. Stage durations can locate waits. The intervention question concerns the total time until sending.



### RMP.Application:5.3 - Separate a delay forecast from an intervention effect

Suppose a separate set of 30 old quotations contains 20 late and 10 on-time quotations. The head approver was absent for 13 of the late quotations and three of the on-time quotations. The odds of lateness are initially 20/10 = 2. On learning that the approver was absent, the likelihood ratio is (13/20)/(3/10) = 13/6. Updated odds are 13/3, corresponding to probability 13/16.

Under the stated table model, absence raises the predicted probability of lateness in those records. High workload or complex cases could coincide with absence, and a substitute could behave differently. Estimating an effect of the proposed staffing arrangement requires a suitable intervention comparison. For a forecast about later quotations, establish that the earlier table is an appropriate basis.

To compare approval delay, missing input and their combined contribution, identify which observations differ in expectedness under the accounts. Use likelihoods when the model supports them or a weaker contrast the available records permit. Two accounts can allow the same finding with different probabilities. When their expected findings coincide, report the unresolved distinction. Include plausible coexisting mechanisms and give any mixture of alternatives a justified composition.

Use [statistical inference under an observation model (MMP.13)](Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp13---infer-unknowns-statistically-under-a-stated-observation-model) for the probability model and update, [observations that distinguish model alternatives (MMP.16)](Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp16---design-observations-to-separate-mathematical-model-alternatives) for the alternatives an obtainable observation can distinguish, and [intervention-effect identification (MMP.15)](Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp15---identify-an-intervention-effect-from-available-data) for identification of the stated intervention effect. The manager can use the result relevant to the staffing question. The decision owner with authority to commit the resources decides under the applicable criteria.



### RMP.Application:5.4 - Ask for a comparison the organization can obtain and run

The manager gives a qualified analyst a concrete request:

> We need to decide whether to fund an additional hour of approval capacity per working day in each participating branch. The new arrangement adds a trained approver during that hour using the existing rules. The current arrangement has no additional approver. We need working time from an eligible request to sending the quotation, including waits for missing input, and the change in the proportion of quotations requiring a customer-facing correction. Specify the eligible cases and branches, assignment, treatment of unfinished or missing cases, comparison and uncertainty calculation.

The manager supplies workload and complexity records, staffing, queues, expected volumes, the reporting deadline and who can keep the records. Before seeing intervention results, the manager and decision owner set two criteria. The lower limit of the specified two-sided 95% interval for mean time reduction must exceed **one working day**. The upper limit of the corresponding interval for increased correction rate must be below **0.5 percentage points**. These criteria govern the case’s operating decision.

The analyst explains how assignment, outcomes, dependence, expected precision, observation period, analysis and stopping rule answer the question. [RMP.2](#rmp2--choose-a-criticism-bearing-research-design-or-stop) uses that construction to choose an obtainable design or finish with no new study. [RMP.3](#rmp3---operationalize-the-research-design-without-replacing-the-question) specifies or assesses the consequential operations. A worked branch and request can show the staff what the plan asks them to do. Use the qualified design and its grounds, including a sufficient existing explanation when available.

For the study branch, assume the analyst justifies the following arrangement for this workplace.

- Sixteen branches have separate customer populations, queues and approvers, with no shared reserve staff or transferred requests. Form eight pairs from prior workload, complexity and waiting records. Randomly assign one branch in each pair to each arrangement for the same calendar period. Admit requests for four weeks and continue the assigned staffing for six to cover follow-up. Specify how an unobserved sending or correction outcome would limit the conclusion.
- Estimate the average across these branches at the specified workload, weighting each branch equally. Calculate each branch’s mean for eligible requests arriving during the four weeks, then the eight paired branch contrasts. More requests can improve information on a branch. The eight assignments are drawn independently across pairs. Within a pair, assigning one branch to the new arrangement determines the other branch’s assignment.
- Determine eligibility at arrival. Include time spent obtaining missing input in total wait and keep approval time in the total effect. Follow each eligible request through sending and the agreed five-working-day correction window. Apply a specified rule to unsent, withdrawn or untraceable requests and disclose their numbers and treatment.
- Use the same recording and notification practice under both arrangements. Take times from their respective events. An assessor who can inspect quotations with assignment labels hidden applies the correction rule. Retain evidence of actual staffing, other changes and departures from the plan.
- The analyst uses historical variation and expected volume to qualify the proposed precision under stated assumptions. For this case the analyst supplies a paired-contrast model and interval calculation for eight pairs and four weeks of incoming requests. Assess design and precision afresh where the conditions differ.
- Set the primary outcome, weighting, interval calculation and analysis before inspecting outcomes. This workplace’s rule stops the trial for serious customer harm and returns the issue to the responsible decision-maker. Report missing records and staffing departures. Continue to the planned end under this stopping rule even if an interim result looks favourable. Retain the specified primary outcome and identify any additional exploratory analysis as such.

Pairing uses known background characteristics to improve comparability. Random assignment determines which branch within a pair receives the additional approver. Inspect the achieved balance and any shared queue. The [NIST account of randomized blocks](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) explains the distinction between the factor under study and background variation controlled by blocking. Qualify the specific workplace design from its own conditions.

Before relying on the workplace analysis, use the complete protocol and its grounds for unfinished cases, precision and analysis. The summary identifies what the manager needs to inspect and operate. If a required part is missing, obtain it from the analyst or another qualified source.



### RMP.Application:5.5 - Decide whether the study is worth obtaining

Suppose the comparison fits eight calendar weeks, with four for incoming requests, two more under assigned staffing to complete follow-up, and time for analysis and return. The eight assigned branches need 240 additional approval hours across six five-day weeks. Recording setup and checks take 24 staff-hours, analysis 32 and management 16. The total is **312 staff-hours**, within the allowance of 340. The decision owner also considers which work the approval hours displace, customer disruption and the cost of delaying a staffing decision.

In this case the owner judges the expected answer worth the effort. A supported reduction could inform recurring staffing, and inconclusive or adverse evidence could prevent an unwarranted commitment. If the answer would arrive too late, a sufficient result already exists, or the choice is settled on other grounds, the same study could have less value.

If the comparison cannot be obtained on useful terms and no adequate design or result is already available, the manager can report the observed stage intervals and the unresolved staffing effect. The authorized decision-maker can decline the new expenditure. A limited improvement to recording can prepare later work if its contribution warrants the effort. State what new evidence, availability or consequence would matter to reconsideration.



### RMP.Application:5.6 - Use the returned analysis at the strength it supports

Now suppose the work was completed as specified. Every eligible request has sending and correction follow-up. The case records show no lost cases, cross-branch assistance or changes to approval rules. The analyst checks assignment, workload and conduct against the planned analysis.

The returned time reductions, current arrangement minus new arrangement, are **1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6 and 2.8 working days** for the eight branch pairs. Their mean is 2.10 days. The analyst's qualified paired model uses the standard deviation of those eight contrasts divided by √8, giving standard error 0.173 days. With the stipulated t interval and seven degrees of freedom, the 95% interval is approximately **1.69 to 2.51 days**.

For correction rate, the paired changes, new minus current, are **−0.4, −0.2, 0, 0.1, 0.1, 0.2, 0.4 and 0.6 percentage points**. The mean change is +0.10 percentage points, standard error 0.112, with an interval of approximately **−0.16 to +0.36 percentage points**. The analyst qualifies the approximation for these branch rates. Low event counts or different dependence could require another analysis. The [paired-mean interval formula](https://www.itl.nist.gov/div898/handbook/prc/section3/prc312.htm) supports checking the arithmetic. Examine assignment, model adequacy and recording against their own evidence.

| Predeclared condition | Returned result | Consequence for this use |
| --- | --- | --- |
| Lower time-reduction limit exceeds one working day. | 1.69 days exceeds 1 day. | The supplied analysis clears the case's meaningful-improvement criterion. |
| Upper limit of the mean increase in correction rate is below 0.5 percentage points. | +0.36 is below +0.5 percentage points. | The average meets the quality criterion. The limit for an individual branch or branch pair is a different question. |
| Conduct and resources preserve the agreed comparison. | The stipulated trace supports the protocol conditions; the burden remains within the authorized allowance. | Return the bounded result for a staffing decision. A defeated condition would restrict that return even with the same numbers. |

The intervals express uncertainty about the average under the qualified analysis. One pair’s observed correction-rate increase is 0.6 percentage points. The predeclared criterion concerns the average. These data do not establish that every branch or pair remained below 0.5 percentage points.

[RMP.5](#rmp5---analyze-and-criticize-the-research-claim-under-its-method) connects the observations, analysis and criticism to the claim. [RMP.8](#rmp8---use-research-results-to-retain-or-revise-an-epistemes-claims-and-return-bounded-evidence) returns the supported change to the knowledge account. **Under these branch, workload and monitoring conditions, the specified additional-approver arrangement reduced average customer waiting, with the stated uncertainty and average quality bound.** Input and other stages can still contribute to delay. Assess differently specified staffing arrangements under their own conditions.

The decision owner compares the recurring benefit with staffing costs and alternative uses of staff. At one hour each working day, eight branches need 160 approval hours per four-week period and sixteen need 320. Suppose 160 hours are available without displacing a more valuable commitment. The authorized owner may continue in branches that can be staffed within those hours and observe the relevant outcomes. The choice of branches and the capacity to serve them require their own grounds.



### RMP.Application:5.7 - Change the shared-queue condition

Suppose hard requests from apparently separate branches actually go to the same reserve approver. Additional capacity in one branch can change waiting in both assigned groups. The earlier contrast for independent queues no longer has its assumed interpretation. Increasing the number of requests within this shared queue preserves that dependence.

Give the analyst the actual queue, staffing and transfer relations for any design still needed through RMP.2 and RMP.3. Alternatives include assigning independent queues, studying a whole-network intervention or making a time comparison that accounts for trends, learning and carryover. A next-day switch in one office can retain learning from the previous condition.

With one shared queue and no worthwhile attainable design for the causal question, report the supported description and the unresolved effect. The original intervals apply to their own arrangement. A proposed study of the network can supply a design before the observations needed for any finding have been made.



### RMP.Application:5.8 - Keep the threats connected to actual decisions

When inspecting a plan or its execution, identify which conditions affect the comparison and what their presence would do to the proposed inference.

| Threat | What it changes in this application |
| --- | --- |
| Initial differences between groups | Pairing and random assignment address the comparison; inspect actual workload and complexity. Selecting only the worst branch for treatment and comparing it with an easier branch needs a different justification. |
| Reaction to being observed | Common recording makes the comparison refer to monitored work. Withdrawing that practice changes the conditions for transferring the answer. |
| Several changes introduced together | Record the treatment bundle. A valid contrast that changes both the priority rule and the number of approvers estimates their joint effect. Distinguishing the individual contributions requires a comparison that can do so. |
| Time, learning or carryover | The concurrent branch comparison and the changed shared-queue case require different dependence models. A later result may depend on earlier training or a seasonal workload change. |
| A convenient indicator replaces the goal | Keep actual sending time distinct from a changed promise or CRM update. Restore the event-to-measure relation before using the number. |
| Judgement affected by the observer | Use suitable event records and an applicable correction rule. Where feasible, conceal assignment from the assessor. If the assessor knows it, examine what bias that could introduce and how it affects the claim. |
| Repeated records mistaken for independent units | Analyze the assigned branches and matched pairs. Several records from one request, approver or branch do not supply additional independent assignments. |
| Inadequate recording resolution or precision | Inspect the recording operation and the planned uncertainty. More rounded rows may add no distinction; more genuinely informative units may still be too costly to obtain. |
| Selecting outcomes, analyses or stopping after seeing results | Preserve what was fixed beforehand and why later choices changed. An exploratory favorable subgroup can suggest another question; it does not retrospectively become the planned confirmatory answer. |

Before extending the finding, examine the workload, staffing and interactions in the receiving setting. Re-running the same data can expose a computational error. For a question requiring new workplace cases, use suitable existing evidence or assess a further check through [RMP.6](#rmp6---choose-a-credibility-test-that-bears-on-the-research-claim-or-answer-without-new-testing). Finish with the supported answer or its precise limit. Where a decision is part of the task, state what the result can inform.

## RMP.Application:6 - Restore a service while investigating an unresolved mechanism

This constructed case distinguishes an immediate service task from a research question about its mechanism.

Suppose response times rise after a cache is enabled. An applicable operating procedure and current observations support restoring the previous configuration for today’s service. The authorized operator can act under that procedure. The general explanation of the delay may remain open.

A separate inquiry asks when contention for the cache’s shared lock can worsen response time even as remote requests decline. Suppose the sources leave this relation unsettled for the implementation and concurrency range. A scoped, criticizable explanation could change the model and later design guidance. This inquiry remains useful with today’s operating decision settled.

Use [the distinction between model, explanation, research and advice (PSDA.Reference:2.1)](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psdareference21---do-we-need-a-model-an-explanation-research-or-advice) to identify each needed contribution. Suppose one simulation reproduces the delay through lock contention and another through the mix of requests. The aggregate delay alone does not distinguish the explanations. Other observations may already do so. [PSDA.3](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda3---construct-complementary-situation-and-option-models) identifies what each model assumes and supports. [RMP.2](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp2--choose-a-criticism-bearing-research-design-or-stop) helps choose observations that could distinguish their mechanism claims.

One candidate design observes lock waiting and request classes during a replay that preserves the relevant concurrency. Check measurement, access and the correspondence between replay and target workload. Serializing the requests would change the interaction being investigated. Choose a design that can discriminate where the answer is important enough to warrant the work.

For a chosen investigation, use [RMP.3](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp3---operationalize-the-research-design-without-replacing-the-question) for consequential operational choices, the qualified domain Method to carry it out, and [RMP.4](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp4---preserve-a-criticism-ready-research-trace) for the actual trace. Use [RMP.5](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp5---analyze-and-criticize-the-research-claim-under-its-method) to interpret the material, with [RMP.6](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp6---choose-a-credibility-test-that-bears-on-the-research-claim-or-answer-without-new-testing) for a further credibility question when needed. An adequate existing result can supply a contribution directly. If no informative observation is attainable at worthwhile cost, the allocation question can finish with no new study and the mechanism unresolved. Today’s supported service restoration remains available.

Suppose later evidence supports the locking explanation within the tested concurrency range. Give model and design users that range and its grounds. For a new configuration, the service owner needs evidence of fit and the required deployment authority. [EXD.4](https://github.com/ailev/FPF/blob/main/DPFs/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd4---co-construct-and-repair-an-explanation-in-dialogue) helps explain the relation between understanding a mechanism and qualifying a particular design for use. A workload outside the supported range requires another applicability judgement. Retain the result for conditions it covers.

## RMP.Application:End

# Research Method Practice Principles Framework Sources and Edition Notes

## RMP.Sources:1 - Source use and currentness

The following sources inform research membership, the choice of investigation, operationalization and records, inference, credibility testing, synthesis, knowledge revision and Method improvement. RMP.10 and RMP.11 describe their specialist reconstruction and historical sources in their own source sections.

| Source | Role in the available patterns | Limit preserved |
| --- | --- | --- |
| OECD, [Frascati Manual 2015](https://doi.org/10.1787/9789264239012-en) | A five-criterion, cross-sector account of R&D used in RMP.1. | The manual addresses statistical methodology. RMP.1 adapts all five criteria to its research-membership question. Truth and institutional authorization require their own grounds. |
| UNESCO, [Recommendation on Open Science](https://www.unesco.org/en/legal-affairs/recommendation-open-science) | Research across institutional, citizen and community settings. | Apply ethics, safety, rights, confidentiality, security, access and community authority to the relevant participation and data use. |
| MRC/NIHR, [framework for complex interventions](https://doi.org/10.1136/bmj.n2061) | In RMP.2, compare perspectives around the important uncertainty, revisit earlier choices when needed and stop when further work lacks value. | Apply the intervention and health-research guidance within its scope. Other inquiries have their own applicable design and sequence. |
| O’Brien et al., [Standards for Reporting Qualitative Research](https://doi.org/10.1097/ACM.0000000000000388) | Transparency and flexibility in reporting qualitative work. | Use it for appropriate reporting. Choose a design from the question and evidence, and establish actual conduct from its records. |
| American Historical Association, [Statement on Standards of Professional Conduct](https://www.historians.org/resource/statement-on-standards-of-professional-conduct/) | Careful source use, declared methods and assumptions, relations between evidence and interpretation, bias awareness and alternatives. | Use the professional standards for the historical work they cover. A specific finding, archive access and any required authority need their own grounds. |
| Cochrane, [Handbook for Systematic Reviews of Interventions](https://training.cochrane.org/handbook/current/chapter-02) | Question-led eligibility, search, appraisal and synthesis for intervention reviews. | Judge the applicability of that guidance to the review question and use an actual qualified corpus. |
| National Academies, [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303) | Computational reproduction uses the original inputs and analytical steps. Replication examines whether studies addressing the same scientific question obtain consistent results with data each collected. | Select a move for the question it can answer. Qualification for a different setting, robustness and an authorized decision have their own conditions. |
| SCORE 2026 [analytical robustness](https://www.nature.com/articles/s41586-025-09844-9) and [replicability](https://www.nature.com/articles/s41586-025-10078-y) studies | Consequential analytical alternatives and comparison criteria in RMP.5 and RMP.6. | Retain the sampled social and behavioural fields, rates and tolerance conventions when interpreting the findings. Establish criteria for another use separately. |
| Flake and Fried, [Measurement Schmeasurement](https://doi.org/10.1177/2515245920952393), and Goos et al., [measurement reliability, validity and reporting](https://doi.org/10.1371/journal.pone.0356070), 2026 | Connect construct, measure, administration and context in RMP.3, and locate the actual measurement in RMP.4. | Assess validity for the receiving context. The Many Labs observations apply to their examined material and measurement conditions. |
| Lakens, [Sample Size Justification](https://doi.org/10.1525/collabra.33267) | Rationale for sample size tied to the question, precision and dependence. | Judge whether an attainable sample can support the required conclusion. Qualitative and source-critical adequacy use their appropriate methods. |
| [SPIRIT 2025](https://www.bmj.com/content/389/bmj-2024-081477) and COS [TOP 2025](https://www.cos.io/initiatives/top-guidelines) | Consequential protocol detail and the time at which registration, protocol and analysis intentions were fixed. | Establish what was committed prospectively from dated evidence. Appraise the design separately and allow method-appropriate changes with their grounds. |
| Haven et al., [qualitative preregistration Delphi study](https://doi.org/10.1177/1609406920976417), and Braun and Clarke, [RTARG and review](https://doi.org/10.1177/02692163241234800) | Informative starting commitments, method-appropriate evolution and reporting suited to reflexive thematic analysis. | Use the contribution for the qualitative approach in question. A consensus or reporting review supports its stated scope. |
| Rethlefsen et al., [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z) | Search versions, sources, platforms, dates and retrieval records. | The actual search, appraisal and synthesis must serve the supplied review question under their qualified methods. |
| Miske et al., [Investigating reproducibility](https://doi.org/10.1038/s41586-026-10203-5), 2026, and [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) | Observed problems and an implementation approach for connecting inputs, transformations, runs and outputs. | The study covers its 2009–2018 papers and obtainable datasets. A provenance format can document a run. Qualification of the finding and actual reproduction of it require their own evidence. |
| Carroll et al., [Operationalizing CARE and FAIR](https://doi.org/10.1038/s41597-021-00892-0) | Data authority, purpose and access, and what criticism each available view permits. | CARE has an Indigenous data-governance basis. FAIR principles address findability, accessibility, interoperability and reusability under stated conditions. Establish which material the recipient can examine. |
| European Commission, [Living guidelines on the responsible use of generative AI in research, fourth edition, October 2026](https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en), with the separately dated [May 2026 revision](https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/updated-era-living-guidelines-responsible-use-generative-ai-research-2026-05-08_en) | Records of research-shaping AI contributions, verification by the responsible researcher and applicable accountability for research decisions. | The non-binding guidance distinguishes substantial contribution from routine editing. Apply its named responsibility to the research it covers. Retained outputs support examination of what was received, while replay and disclosure depend on their own conditions. |
| Cochrane [chapters 5](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-05), [10](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10), [12](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-12), [13](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-13) and [15](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-15) | Reports and studies, quantitative combination and alternatives, missing contributions and bounded interpretation in RMP.7 and RMP.8. | Match the model to the quantity and dependencies. Use the intervention-review guidance within its scope and the synthesized finding under its conditions. |
| [Harden and colleagues (2018)](https://discovery.ucl.ac.uk/id/eprint/10040031/), [Cochrane Handbook v6.0, §21.13](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/archive/v6.0), [Sutcliffe and colleagues, Cochrane–Campbell Handbook, chapter 14 (February 2024 draft)](https://www.cochrane.org/authors/handbooks-and-manuals/cochrane-campbell-handbook-qualitative-evidence-synthesis/qeschapter14intv01140225), [GRADE-CERQual](https://www.cerqual.org/what-is-the-grade-cerqual-approach2/) and JBI [mixed synthesis §8.3](https://jbi-global.atlassian.net/wiki/spaces/MANUAL/pages/355829259/8.3%2BThe%2BJBI%2Bapproach%2Bto%2Bmixed%2Bmethod%2Bsystematic%2Breviews) | For intervention-effectiveness reviews, Harden and the historical handbook describe separate syntheses followed by integration. The newer chapter distinguishes transformation for a common question, comparison of separate syntheses and use of one synthesis to inform another. CERQual assesses confidence in qualitative findings, and JBI relates integration to the review question. | Select the operation for the question. Retain context and the meaning or information lost in a transformation. An interpretive finding and a population prevalence estimate have different grounds. |
| Morris, White and Crowther, [simulation-study design](https://doi.org/10.1002/sim.8086), Williams et al., [simulation transparency](https://doi.org/10.1111/2041-210X.14415), and Pawel et al., [failures and non-convergence](https://doi.org/10.1080/00031305.2025.2540002) | Aim, estimand, generating situations, performance, Monte Carlo uncertainty and failures for a selected RMP.9 comparison. | Use these operations to design and interpret the study. Judge whether to commission it from its attainable contribution and cost. Claims of performance require the actual results within their scope. |

The question and design uses were examined on 3 October 2026, operationalization and trace on 6 September 2026, and analysis, credibility, synthesis, revision and Method improvement on 8 September 2026. The stopping and acquisition contribution from Method Engineering was reconsidered on 9 September 2026. The European Commission and mixed-synthesis entries distinguish the editions cited above where the content at their former current addresses changed. Reconsider a source use when a relied-on criterion, field-specific criticism, participation condition or limit changes, or when an omitted alternative could alter the answer.

RMP.10 uses Critical Decision Method for recalled critical-incident cues and process mining for recorded event relations. Its combination of evidence is a separate synthesis. RMP.11 uses process-tracing and historical-evidence methods for diagnostic comparisons, with C.28 governing the evidence required for a causal use. Their source sections describe the contributions, alternatives and limits.

Use the source that supplies the needed operation or evidence. Each pattern’s source discussion explains the adopted contributions and alternatives. Domain methods and evidence govern the failure mechanism, salinity measure, historical source, instrument, safety condition or other subject-specific claim.

The [shared-architecture account](#rmpreference23---what-the-sources-contribute-to-the-shared-architecture) explains what the sources contribute to the connected research Methods.

## RMP.Sources:2 - Edition return

**Research Method Practice Principles Framework — First Edition** comprises the Readme, Table of Contents, Architectural Reference, eleven pattern bodies in six reading Parts, practical entries, connected applications and source and edition accounts. Use the Table of Contents to locate a method.

Enter the eleven-method repertoire where a contribution fits the question. Use disciplinary methods and case-specific findings for the subject in hand, and the relevant authority for a receiving decision. A sufficient finding from one method can finish the inquiry.

## RMP.Sources:3 - Citation

Levenchuk, Anatoly. *Research Method Practice Principles Framework — First Edition*. Original edition, 24 October 2026. Developed and reviewed with AI assistance. [Publication](https://github.com/ailev/FPF).

To identify the version you used, cite a permanent link to this file at the specific repository commit. For a particular method, include its PatternID and title.

The [Architectural Reference](#research-method-practice-principles-framework-architectural-reference) explains the connected language and the consequences of these sources for its use.

## RMP.Sources:End
