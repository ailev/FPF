# Mathematical Modeling DPF

> Methods for constructing mathematical representations of a question, connecting unknown relations, observations and available actions, and revising the resulting models.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 22 September 2026
- **Status:** Eternal alpha: a growing language of general modeling methods.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF ecosystem repository](https://github.com/ailev/FPF)

Begin with the question your model must answer. Use the Table of Contents to find a relevant pattern, then open its Problem frame, Solution, worked cases and checklist. Readme shows how results connect the methods; Preface explains their rationale and limits.

The code **MMP** names this DPF. Its numbers are stable pattern addresses; § shows position in this edition. References beginning MATH name patterns in [Mathematical Thinking](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md). References such as C.29 name patterns in [FPF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). ME references name patterns in [Method Engineering](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md). Open the cited publication when that contribution is needed. When using another version, revisit a conclusion if its cited operation or condition has changed.

To cite this edition: Anatoly Levenchuk, *Mathematical Modeling DPF*, [FPF ecosystem repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Mathematical Modeling - Readme](#mathematical-modeling---readme) | Follow worked connections between modeling methods. |
| Preface | [Mathematical Modeling - Preface](#mathematical-modeling---preface) | Understand the connected methods, their rationale, sources and limits. |

## A. Formulate the subject question

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.10 - Construct and Revise a Mathematical Constraint Formulation](#mmp10---construct-and-revise-a-mathematical-constraint-formulation) | Usable, evolving | objects; representation; domains; constraints; recovery; multiplicity; optimization. How can the objects and conditions of a working question be expressed so that mathematical answers still refer to the intended possibilities? | B.5.FM for initial formulation; MATH.1/.5 for construction and representation; C.29.1 for transferring results; MMP.11 for unknown relations. |
| 2 | [MMP.11 - Construct a Mathematical Model Family from Known Relations](#mmp11---construct-a-mathematical-model-family-from-known-relations) | Usable, evolving | unknown relation; family; grounded structure; parameterization; completeness; identifiability. How can an unknown contribution vary without losing known relations, and which remaining ambiguity changes the requested consequence? | MMP.10 for admissible representation; A.3.3.TR for state; C.16.IR for observation-based inference; C.28.MR for intervention; MMP.9 for reduction. |
| 3 | [MMP.8 - Formulate Information-Dependent Choices Mathematically](#mmp8---formulate-information-dependent-choices-mathematically) | Usable, evolving | available information; action; policy; decision timing; objective; conditional requirement; average performance. What can be chosen with information available in time, and which conditions must that choice satisfy? | MMP.7 for reports; A.3.3.TR for change; MMP.10 for constraints; ME for changing the corresponding way of working. |
| 4 | [MMP.8.SD - Construct a Sequential Decision Model from Information and Consequences](#mmp8sd---construct-a-sequential-decision-model-from-information-and-consequences) | Usable, evolving | sequential decision; sufficient state; belief; policy; transition; accumulated consequence; continuation. What information must a continuing instruction retain, and how do present choices affect later possibilities and results? | MMP.8 for available choices; A.3.3.PI for predictive state and belief; MMP.7 for records; CMP.3/.5/.9 for policy computation. |

## B. Infer, distinguish and revise

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.7 - Construct a Probability Model of the Recorded Data](#mmp7---construct-a-probability-model-of-the-recorded-data) | Usable, evolving | observation; recorded data; selection; missing records; censoring; noise; probability law. What distribution does the recording procedure produce from the modeled possibilities? | C.16.IR for interpretation and inference; MMP.11 for unknown relations; MMP.8 when the record informs a choice. |
| 2 | [MMP.12 - Formulate an Inverse Problem and Choose Whether and How to Use Regularization](#mmp12---formulate-an-inverse-problem-and-choose-whether-and-how-to-use-regularization) | Usable, evolving | inverse problem; identifiability; conditioning; regularization; restriction; penalty; target. Which unknowns can the records resolve, and what improvement and loss does a stable reconstruction introduce? | C.16.IR for compatible cases; MMP.11/.7 for the forward and recording relations; MMP.13 for inferential uncertainty; CMP for solving the formulated problem. |
| 3 | [MMP.13 - Infer Unknowns Statistically under a Stated Observation Model](#mmp13---infer-unknowns-statistically-under-a-stated-observation-model) | Usable, evolving | estimator; confidence coverage; prior; posterior; predictive uncertainty; dependence; target propagation. Which inferential construction supports the statement the receiver needs? | MMP.7 for the record law; MMP.12/C.16.IR for ambiguity; CMP.8/.9 for numerical computation; MMP.14/.8 for prediction checks and decisions. |
| 4 | [MMP.14 - Find and Repair a Mathematical Model's Failed Predictions](#mmp14---find-and-repair-a-mathematical-models-failed-predictions) | Usable, evolving | model criticism; predictive comparison; residual; conditional response; selection; repair; held-out prediction. Which discrepancy changes the use, what assumption can repair it, and what consequence must be recalculated? | MMP.7/.11/.13 for comparable predictions; B.5.RR for affected revision; CMP.8/.9 for numerical error; C.11.DUA for worthwhile further checking. |
| 5 | [MMP.15 - Identify an Intervention Effect from Available Data](#mmp15---identify-an-intervention-effect-from-available-data) | Usable, evolving | causal identification; intervention; adjustment; mediation; population transfer; support; partial identification. Which intervention consequence follows from the available laws and causal assumptions? | C.28.MR for intervention meaning; MMP.7/.13 for recording and estimation; C.16.IR for compatible possibilities; MMP.16 for worthwhile distinguishing observations. |
| 6 | [MMP.19 - Construct and Bound a Mathematical Counterfactual Comparison under a Causal Model](#mmp19---construct-and-bound-a-mathematical-counterfactual-comparison-under-a-causal-model) | Stable | counterfactual; same case; factual inference; common input; joint response; pathway; bounds. What would happen to the same case under another action, and what does the available information determine? | C.28.MR for changed mechanisms; MMP.7/.13 for factual records and inference; MMP.15 for identification; MMP.10/.16 for bounds and useful observations. |
| 7 | [MMP.16 - Design Observations to Separate Mathematical Model Alternatives](#mmp16---design-observations-to-separate-mathematical-model-alternatives) | Usable, evolving | observation design; discrimination; nuisance; recording law; value of information; feasible design. Which obtainable observation separates a consequential ambiguity, and can its benefit repay its burden? | MMP.7/.11/.12/.13 for predicted record laws; MMP.8/.8.SD for decisions; C.11.DUA for worthwhile further work; subject methods for realization. |

## C. Change the model while retaining its use

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MMP.9 - Derive a Reduced Mathematical Model of State Evolution](#mmp9---derive-a-reduced-mathematical-model-of-state-evolution) | Usable, evolving | reduction; hidden state; closure; memory; approximation; error; sufficient bound. What contribution is left by eliminated detail, and which replacement preserves the consequence needed? | A.3.3.TR for evolution; C.29.1 for preserved structure; MMP.11 for a replacement family; B.5.RR for affected revision. |
| 2 | [MMP.17 - Construct a Surrogate for Selected Model Responses](#mmp17---construct-a-surrogate-for-selected-model-responses) | Usable, evolving | surrogate; selected response; input region; approximation; correction; tail; refinement. Which cheaper construction can supply the model response the next operation actually needs? | MMP.11 for retained structure; CMP.7/.6 for learning and updates; MMP.14 for consequential mismatch; MMP.18 for coupled use. |
| 3 | [MMP.18 - Couple Models with Compatible Exchanges and Scales](#mmp18---couple-models-with-compatible-exchanges-and-scales) | Usable, evolving | coupling; interface; scale; conservation; closure; shared uncertainty; double counting. How can component models exchange quantities and information without changing the required joint answer? | A.3.3.TR and MMP.10 for joint conditions; MATH.18 for retained consequences; MMP.9/.17 for missing contributions; CMP.8/.14 for interacting computation. |

# Mathematical Modeling - Readme

## Practical entries

Bring the question you need a model to answer. It may concern an unexplained observation, a proposed intervention, a design, a prediction or the way work is performed. A useful result can be a relation that makes calculation possible, a conditional answer, a reason to reject a proposal or a more precise question.

The methods in this language work together through the results they produce. A formulation says which possibilities the model admits. An observation model says which records those possibilities can produce. Recovery and inference determine what can be learned from those records. An information-dependent choice uses the resulting distinctions only when they are available in time. A failed prediction can send the work back to the observing procedure, a model relation or the calculation.

Enter where the difficulty occurs and reuse results you already have. If the question is not yet mathematical, FPF B.5.FM helps choose participants and propose relations; B.5.TU helps interpret an unfamiliar theory. C.29 connects the construction with what it represents. For example, a cart's total distance does not determine its final position. Signed displacements and a starting position answer that question on a straight path; a question about visits along the way needs further information. Once the needed objects are recognizable, MMP.10 expresses their constraints; MMP.11 constructs a family when a relation remains unknown.

The worked connections below show how an intermediate result changes the next operation. They are selected examples, not a catalogue or a prescribed modeling process. Use the Table of Contents for other questions and the pattern bodies for the methods, prerequisites and further examples. FPF supplies shared reasoning methods; Mathematical Thinking supplies reusable mathematical constructions.

You can ask an assisting agent: “Explain the result and give feedback in the language of my work, without framework jargon.”

A contribution already available can supply its result without being reconstructed.

### MMP-OBSERVATION-TO-ACTION - Turn an observing model into a workable instruction

- **Situation:** A proposed way of working includes an observation followed by a decision, but their combined benefit is unclear.
- **Question:** What instruction can use that report, and which change to the work is worth making?
- **First useful result or blocker:** An instruction with its required information, timing and supported performance, or a contribution still needed before it can be used.
- **Start with:** [MMP.8](#mmp8---formulate-information-dependent-choices-mathematically) to formulate the choice; [MMP.7](#mmp7---construct-a-probability-model-of-the-recorded-data) when its reporting law is missing; ME.7 when the observing and acting methods must be combined or changed.
- **Stop or return:** Use a sufficient instruction. A changed recording procedure reopens the observation model; changed timing, allowed choices or success requirements reopen the decision. Use C.11.DUA when the benefit of further inquiry is uncertain.

#### Worked connection for MMP-OBSERVATION-TO-ACTION

**A noisy report and a changed success requirement.** The observing and acting methods are examined together through ME.7 in [Method Engineering](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md).

Start with what successful work means. In MMP.8:5.2, one of two requests needs a scarce resource, and allocation must follow a report. With perfect timely information, an instruction can follow the report. Without a distinguishing report, each fixed allocation fails in one admitted circumstance.

For the noisy procedure, MMP.7 supplies a necessary intermediate result. Two channels may produce the report, but the record does not identify the channel. Sum over that unrecorded choice to obtain the reporting law for each actual circumstance. MMP.8:5.2 performs this calculation: following the report succeeds with probabilities 0.8 and 0.7 in the two circumstances. No prior probability for which circumstance is actual is needed for those conditional results.

Now construct what can be done with that report. MMP.8 compares the four deterministic instructions on a two-valued report. A requirement of at least 0.65 success in each circumstance admits following it. A zero-failure requirement does not. Changing the requirement to average success, with one circumstance occurring with probability 0.95, makes always allocating to that request preferable among the four instructions. The preferred instruction changed because the question changed; the observing procedure stayed the same.

Return this answer to the proposed work. The report must be produced before allocation, and the receiving participant must be able to follow the instruction. If obtaining a better report costs more than the improvement is worth, C.11.DUA can support a sufficient existing choice or acceptance of the remaining risk. If the observation itself changes the situation, first represent that intervention through C.28.MR and derive the reporting and outcome laws for the changed situation.

ME.7:4.1 helps examine the proposed composition: what each method contributes, how the report reaches the acting participant, and which timing and support conditions the whole needs. Its result can be a supported composition or a proposal with unresolved conditions. Retain the resource demands and timing when revising the mathematical question. The useful result is a change the work can perform, a supported explanation of why the present method suffices, or the specific contribution still needed to choose.

### MMP-RECORDS-TO-ANSWER - Reach a usable conclusion from incomplete and noisy records

- **Situation:** A fitted model produces an answer, but ambiguity in the unknowns or in the observing procedure may change what that answer supports.
- **Question:** Which conclusion do the records warrant, and what must be revised when a consequential assumption fails?
- **First useful result or blocker:** An identifiable target and an inferential result with a stated meaning, or the unresolved difference that still changes its use.
- **Start with:** [MMP.7](#mmp7---construct-a-probability-model-of-the-recorded-data) for the record law, [MMP.12](#mmp12---formulate-an-inverse-problem-and-choose-whether-and-how-to-use-regularization) for recovery and ambiguity, [MMP.13](#mmp13---infer-unknowns-statistically-under-a-stated-observation-model) for inference, and [MMP.14](#mmp14---find-and-repair-a-mathematical-models-failed-predictions) when a prediction needs repair.
- **Stop or return:** Use a sufficient result under its stated assumptions. Additional diagnostics or observations are needed only when they can change the warranted use. A changed target, recording rule or dependence returns to the contribution it affects.

#### Worked connection for MMP-RECORDS-TO-ANSWER

**1. Construct what can be observed.** Suppose two nonnegative contributions, u and v, produce only a total T=u+v in a measuring procedure. The task is to determine whether T is below 10.5 in the stated units. Initially the measuring practice supplies the model y_i=T+e_i for nine complete readings, with independent normally distributed errors of mean zero and known standard deviation 3. Their observed mean is 8.

MMP.7 turns that account into the joint law of the records. If a procedure instead discards readings outside a reporting range, its probability law must condition on that selection before the same inference can be attempted. MMP.11 is needed earlier if the relation between the unknowns and the observations has yet to be constructed.

**2. Ask what the law can distinguish.** MMP.12 examines changes that leave the records unchanged. Replacing (u,v) by (u+h,v-h), while both remain nonnegative, leaves T and the record law unchanged. No increase in the number of these total readings identifies the two contributions separately. The present target T remains identifiable, so its estimation need not wait for that unresolved decomposition. A question about u alone would require a restriction, another observation relation or a sufficient bound.

**3. Construct the claim needed for the decision.** Under the supplied law, MMP.13 gives the sample mean standard deviation 3/sqrt(9)=1. The rule “mean plus or minus 2” has about 95.45% repeated-sampling coverage for T. Applied here it gives [6,10]. Its upper end is below 10.5. Whether this is sufficient for the intended action depends on the consequence of a wrong answer and the accepted uncertainty; the interval itself supplies no permission to act. The confidence level describes the rule across repetitions, not a posterior probability for this realized interval.

This inference uses the total that MMP.12 found recoverable and the dependence assumptions that MMP.7 made explicit. A different requested claim, such as a posterior probability or the distribution of the next reading, needs the corresponding MMP.13 construction. A regularized split of u and v supplies neither of those claims.

**4. Recalculate after the observation premise changes.** An existing calibration investigation now establishes that all nine readings can share an unknown offset b, with |b|≤2. The measuring practice supplies this bound; a residual plot alone would not establish it. This changes the relation used by MMP.7 to y_i=T+b+e_i.

MMP.12 now exposes ambiguity between T and b. MMP.13 retains the interval for T+b and expands it over the admitted b values, giving [4,12] for T with at least the earlier coverage for each fixed admissible offset. The former threshold conclusion no longer follows. More repeated readings reduce the independent noise but do not determine b. A useful next move is a sufficient existing calibration bound, a qualified narrower answer or a different observation when its benefit warrants the work.

**5. Return to the question that will consume the result.** If an action must be selected despite the remaining uncertainty, MMP.8 formulates that choice using the information and timing actually available. If the question concerns changing the mechanism, FPF C.28 and C.28.MR identify the causal question and replacement: observing a variable at a value differs from forcing it to that value. MMP.15 then determines whether the available laws and causal assumptions identify the requested intervention consequence. An observational fit alone cannot supply that inference. If the original inferential answer is sufficient, the connection ends there.

If instead a consequential difference between predicted and observed records is the unresolved difficulty, MMP.14 compares them under the modeled conditions and helps locate the contribution to repair. A supplied change of premise, as in step 4, can return to the affected construction without that additional diagnosis.

The same joins support other observing procedures. Their general contribution is carrying a model's remaining ambiguity into the inference and its receiving use, then revising only the affected construction when an assumption changes.

### MMP-SUFFICIENT-ANSWER - Answer the working question before reconstructing every detail

- **Situation:** A model omits internal distinctions, and reconstructing them may cost more than the requested answer needs.
- **Question:** Which consequences are shared by the remaining possibilities, and do they already decide the question?
- **First useful result or blocker:** A bound that settles the stated threshold, or the distinction whose unresolved value still changes the answer.
- **Start with:** [MMP.9](#mmp9---derive-a-reduced-mathematical-model-of-state-evolution) for lost evolution information; [MATH.20](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md#math20---bound-a-mathematical-unknown-by-comparable-constructions) for bounds; FPF C.29 for subject interpretation and C.11.DUA when further inquiry is a live choice.
- **Stop or return:** Use a settled answer under the supplied premises. A changed threshold, observation, law or time horizon returns to the affected comparison.

#### Worked connection for MMP-SUFFICIENT-ANSWER

**1. Make the receiving question specific.** A supplied account has two nonnegative populations with laws x'=-x and y'=-2y, where time uses the unit in which these rates are stated. The initial total is 1, but its split is unknown. Is the total remaining at time 3 below 0.1? This case starts with those laws; establishing a physical or other subject law is a different contribution.

**2. Recover the omitted contribution.** With z=x+y, MMP.9 gives z'=-x-2y. The same z=1 can have derivative -1 or -2, so the current total alone does not determine its rate of change. This result identifies the missing distinction and supplies alternatives for a bounding calculation.

**3. Derive an answer shared by those alternatives.** Put x(0)=a and y(0)=1-a, with 0≤a≤1. The equations give `z(t)=a*exp(-t)+(1-a)*exp(-2t)`. MATH.20 uses this convex combination to derive exp(-2t)≤z(t)≤exp(-t) for t≥0. At time 3, exp(-3)<0.05<0.1. The upper bound settles the question for every initial split. No estimate of a is needed for this answer.

**4. Return the consequence to the work.** C.29 asks what the populations, rates, total and threshold represent and which assumptions permit the interpretation. Under the supplied account, the condition is satisfied at time 3. Using that consequence in a real decision also uses the subject premises that made these equations applicable.

**5. Reopen what changes the answer.** Suppose the next question is whether z(1)<0.2. The bounds straddle 0.2. The same formula reduces the decision to a<(0.2-exp(-2))/(exp(-1)-exp(-2)), approximately 0.278. An available bound on a may settle this. Obtaining more about a is useful when it can change the decision enough to justify its cost; C.11.DUA helps make that choice. Changed evolution laws instead return to step 2, since the old enclosure may fail.

A different population or physical decay process can use this example when it supplies the stated laws and interpretation. The reusable connection is broader: reduction exposes a lost distinction, a mathematical comparison bounds its effects, and the receiving question decides whether those effects need further work.

### MMP-INTERVENTION-AND-INFORMATION - Decide whether an observation will improve the next action

- **Situation:** Several actions have different consequences in circumstances that the current record does not fully distinguish.
- **Question:** What can the available data establish about those actions, and is another observation worth obtaining before acting?
- **First useful result or blocker:** A justified action comparison and a contingent instruction, or an assumption, distinction or timing condition still needed.
- **Start with:** [MMP.15](#mmp15---identify-an-intervention-effect-from-available-data) to identify the intervention consequences; [MMP.16](#mmp16---design-observations-to-separate-mathematical-model-alternatives) to compare obtainable information; [MMP.8.SD](#mmp8sd---construct-a-sequential-decision-model-from-information-and-consequences) when observing and acting form successive choices.
- **Stop or return:** Use the sufficient existing instruction when further information cannot repay its burden. A changed recording law, effect of observing or available action reopens the affected construction.

#### Worked connection for MMP-INTERVENTION-AND-INFORMATION

**1. Establish what the actions would do.** A service must choose response A or B. Its current circumstance is H0 or H1, each with supplied probability 0.5. Earlier randomized work recorded the circumstance and supplies the following population mean losses:

| Circumstance | Response A | Response B |
| --- | ---: | ---: |
| H0 | 0 | 4 |
| H1 | 10 | 0 |

MMP.15 makes the use of these records explicit. The case assumes consistent response versions, no interference, positive assignment probability for each response in each recorded circumstance, and transfer of the conditional intervention means to the current service. Under those assumptions, randomization identifies the means in the table. They are stipulated population quantities here; estimates from finite records would also need MMP.13's uncertainty.

Without another indication, A has expected loss 5 and B has expected loss 2. This supplies the comparison that any proposed observation must improve.

**2. Construct the record the proposed observation would supply.** A diagnostic report is positive with probability 0.8 in H1 and 0.2 in H0. It does not change the circumstance or the subsequent action losses. Within each circumstance, the report supplies no further information about response loss. Its cost is 0.2 in the same loss units, and the report arrives before the response is chosen. MMP.7 retains this reporting law, rather than treating a positive report as certain knowledge of H1.

**3. Compare information through its consequence.** MMP.16 obtains a posterior probability of H1 equal to 0.8 after a positive report and 0.2 after a negative one. Choose B after positive: its conditional expected loss is 0.8. Choose A after negative: its conditional expected loss is 2. Each report has probability 0.5, so expected action loss is 1.4. The information reduces that loss by 0.6; including its 0.2 cost gives 1.6 rather than 2.

**4. Construct the continuing instruction.** MMP.8.SD represents the first choice, whether to obtain the report, and the later response choice. For the response choice after the report, the posterior belief is sufficient: the conditional mean losses depend only on H and there are no later choices. The resulting instruction is to obtain the report, then use the branch above. Subject and Method Engineering work supply the actual observing and acting capabilities. If the report cannot arrive in time, formulate the response choice from the information that will actually be available.

**5. Revise only what changed.** Suppose the available diagnostic now has the same positive probability, 0.5, in both circumstances. MMP.7's new law leaves the belief at 0.5 after either report. MMP.16 returns zero information benefit for the response decision; MMP.8.SD chooses B without the diagnostic and avoids its cost. If observing instead changes the circumstance, include that transition and the changed intervention consequences before reusing the former calculation.

**6. Recover the comparison if the question changes.** A later inquiry may ask which cases would have benefited from the other response, rather than which response minimizes future expected loss. [MMP.19](#mmp19---construct-and-bound-a-mathematical-counterfactual-comparison-under-a-causal-model) constructs the relation between a case's alternative responses. For an observed case, MMP.7/.13 first recover what its factual record implies about the underlying conditions; C.28.MR then changes the mechanism while retaining that case information.

Check what the available laws actually determine. In MMP.19:5.2, two models have identical action-specific success probabilities and identical randomized records, but give different answers about the same observed case under the other action. MMP.19 returns that ambiguity; a feasible observation is considered through MMP.16 only if it could resolve a useful distinction. Returning to the future expected-outcome criterion can make the unresolved same-case relation irrelevant. The earlier choice is then usable without that extra inquiry.

The connection can stop at a sufficient existing choice. The needed comparison determines whether to construct a report, a continuing instruction or a same-case counterfactual.

### MMP-REPLACE-AND-COUPLE - Use cheaper models without losing the combined answer

- **Situation:** A required answer combines expensive model contributions, and cheaper replacements are available.
- **Question:** What must each replacement supply, and which errors or shared dependencies can change the combined result?
- **First useful result or blocker:** A sufficient coupled answer with propagated approximation limits, or the component contribution that still needs refinement.
- **Start with:** [MMP.17](#mmp17---construct-a-surrogate-for-selected-model-responses) for the replacement's target and use region; [MMP.18](#mmp18---couple-models-with-compatible-exchanges-and-scales) for the exchanged quantities and dependencies; MATH.20 for the needed bound.
- **Stop or return:** Keep a sufficient approximation. Return to the affected source model or interface when the bound no longer settles the question, or to MMP.14 when an observed discrepancy needs diagnosis.

#### Worked connection for MMP-REPLACE-AND-COUPLE

Two components contribute distinct amounts u and v to a total, in the same units and over the same interval. MMP.18 establishes that the required combination is u+v and that neither contribution already contains the other. MMP.17 selects surrogates for these two amounts on the input region being used.

For the present input, suppose their estimates are 0.42 and 0.48, with supported absolute error bounds 0.03 and 0.04. The resulting total is in [0.83,0.97]. It is below a threshold of 1 throughout that interval. No independence assumption is needed for this worst-case sum bound. Errors measured only on a few training cases would not, by themselves, supply the stipulated bounds.

Now lower the threshold to 0.94. The interval no longer settles whether the total is below it. If obtaining the second component from its source model is worthwhile, and that calculation returns 0.46 with absolute error at most 0.001, retaining the first surrogate gives [0.849,0.911]. That narrower combination settles the new question without replacing both surrogates.

A different question can instead change what the interface must carry. A time of threshold crossing needs information about evolution within the interval; two final amounts do not supply it. MMP.18 then returns the missing temporal contribution, and MMP.17 changes the response that a replacement must preserve. More accurate final amounts alone would answer the wrong question.

### MMP-REPRESENT - Why does counting the records overcount the assignments?

- **Situation:** A request can be left unassigned or assigned option 0 or 1. The data format uses a presence bit and an option bit.
- **Question:** Does counting the records count the intended assignments?
- **First useful result or blocker:** A representation with three possibilities per request, or weights that correct duplicate representations. When the presence bit is zero, either option bit denotes the same absent assignment.
- **Start with:** [MMP.10 - Construct and Revise a Mathematical Constraint Formulation](#mmp10---construct-and-revise-a-mathematical-constraint-formulation), especially :5.2. Construct a valid representation, then determine whether its multiplicities preserve the requested count or sampling law.
- **Stop or return:** Use a sufficient count or representation. Reopen the translation when requirements or the requested operation change; a representation adequate for finding an assignment can still distort counting.

# Mathematical Modeling - Preface

## MMP.Preface:1 - Problem frame - Make a mathematical question useful

You may know the relevant formulas and still be unable to build a model for the question in front of you. The candidate objects may be unclear. A recorded value may hide part of the observing procedure. A proposed decision may use information that arrives too late. A detailed model may become affordable only after removing something its answer depends on.

Mathematical Modeling develops methods for constructing and revising such mathematical questions. Its subject can be a physical situation, a working method, a computational process or another mathematical construction. The useful result may be a prediction, an explanation, an admissible arrangement, an instruction, a bound or a question that directs further inquiry. Start with what that result would let you understand or do.

This language belongs to the Foundational Thinking DPF Suite alongside Mathematical Thinking, Physical Thinking, Computational Thinking and Notational Engineering. Its three parts address formulation, inference and model revision, and changes that preserve a needed use. The Table of Contents identifies the methods available here; obtaining a contribution outside them still needs another source or collaborator.

The mathematical account and the subject supply different parts of the reasoning. A relation describing a material, an observing procedure or a permitted action needs its corresponding subject knowledge. A mathematical construction then helps express the relation and derive consequences. The answer returns to the original question with the conditions under which that interpretation holds. The [First Principles Framework (FPF)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) develops this connection in B.5.FM and the C.29 family; the bodies here develop particular model-forming operations within it. Find a named FPF pattern by its full code in FPF-Spec.md and open its Problem frame and Solution. If GitHub cannot display the large file, use its View raw or Download raw file action, then search that copy.

The needed preparation depends on the operation. Finite arrangements can use sets, functions and elementary counting. Probabilistic recording needs conditional probability and sums or integrals. Evolution and reduction can require differential equations. Each body states its prerequisites and works small cases. When a collaborator or assisting agent supplies the mathematics, ask for the meaning of its inputs, its conditions and the result the next part of your work can use. You can ask for that explanation in the language of your work.

Begin with the [Readme](#mathematical-modeling---readme) when the useful entry is unclear. Enter a body directly when its Problem frame matches the difficulty.

## MMP.Preface:2 - Problem and forces - Choose what the model must retain

A model can answer a mathematically well-formed question that differs from the one the work needs. This often happens before calculation: a convenient variable excludes an allowed arrangement, a mean hides a distinction needed for action, or a fitted relation describes observation while the question concerns an intervention.

Several choices therefore shape the construction:

| Working tension | Consequential choice |
| --- | --- |
| A familiar representation and the intended objects | Which distinctions must variables, domains and conditions preserve? |
| Supported structure and an unknown relation | What may vary, and what must remain true throughout that variation? |
| An event and its recorded description | Which unobserved, selected or combined alternatives can produce this record? |
| Knowing a circumstance and choosing before it is known | Which information may the instruction actually use? |
| A detailed account and an affordable answer | Which eliminated contribution needs reconstruction, approximation or a bound? |
| Resolving every unknown and settling the present question | Which remaining differences can change the required consequence? |
| Stable recovery and added assumptions | What variation does a restriction suppress, and could the requested target depend on it? |
| An uncertainty label and the claim it supports | Is the needed result a coverage guarantee, a posterior probability or a prediction for a new outcome? |
| Agreement in one use and a changed use | Which premise, mechanism or interpretation must be reconsidered? |

The requested answer determines how far to develop the model. A bound can settle a threshold question while leaving parameters unresolved. A proposal for a new working method can instead require distinctions that an earlier prediction ignored. C.11.DUA helps decide whether another calculation, observation or refinement is worth its possible contribution.

## MMP.Preface:3 - Solution - Connect the contributions the question needs

### MMP.Preface:3.1 - Form the first account and recover its interpretation

If there is no mathematical question yet, use B.5.FM: identify the participants, propose the relations relevant to the difficulty, work a small consequence and return it to the question. B.5.TU helps when an available theory supplies those relations. Mathematical Thinking provides constructions of objects, operations, representations and arguments when the needed mathematics itself must be developed.

Recover what a request to use a model means in this situation. A structure satisfying stated axioms answers a different question from a representation used to predict an observed process. Both can be useful mathematical work. E.10 clarifies the intended use when the word *model* conceals it; keep the subject's established vocabulary when it is already clear.

A drawing, formula, program or learned representation also needs an operation that obtains the requested answer. A person may reason from a diagram; software may solve equations; an experimental arrangement may exhibit a behavior. Make the required interpretation available when another participant must continue the work. A.6.3.RT.OE helps make an expression usable for that operation, and C.29.2 develops a computational formulation when computation is needed. The obtaining procedure can itself become a subject of mathematical investigation.

### MMP.Preface:3.2 - Represent admissible objects and construct missing relations

[MMP.10](#mmp10---construct-and-revise-a-mathematical-constraint-formulation) starts from intended candidate objects and their requirements. It chooses a representation, derives the conditions that make the representation valid and expresses the required answer. These steps matter for sets, sequences, functions and quantitative objects alike. If several records describe one object, a count or probability over records can require correction before it answers the subject question.

[MMP.11](#mmp11---construct-a-mathematical-model-family-from-known-relations) starts with supported relations and an unknown contribution among them. It constructs adjustable families that retain the needed properties and inserts that contribution into the connected model. A known total, a monotone response and a normalized probability law require different mathematical constructions. Their common modeling question is how to permit the unknown variation while retaining what is supported.

Choose the form from the next operation. Direct constraints may already describe all useful candidates. A parameterization can make changes preserve the constraints automatically, but may introduce duplicate descriptions or omit parts of the allowed family. Retain that difference when interpreting a fitted value, an impossibility result or an observed agreement.

### MMP.Preface:3.3 - Construct change and observation together when they interact

For an evolving situation, A.3.3.TR constructs a state-change rule from the contributing relations, including simultaneous constraints, alternatives and events. If situations assigned the same state need different continuations under the same modeled inputs, revise the state or retain the alternatives. The computation's chosen solution order need not be the represented order of physical change.

[MMP.7](#mmp7---construct-a-probability-model-of-the-recorded-data) derives a probability law for the record produced by an observing procedure. Compose the source and recording laws, retain shared unknowns, sum or integrate unrecorded alternatives, and account for selection. The resulting law can supply a statistical inference or prediction method. C.16.IR addresses what a supplied observation relation resolves, including bounds and consequential ambiguity.

[MMP.12](#mmp12---formulate-an-inverse-problem-and-choose-whether-and-how-to-use-regularization) constructs recovery from a forward relation. Find which changes to the unknown leave the records unchanged or change them too little for stable recovery. A restriction or penalty can make a useful reconstruction possible; derive both the error it suppresses and the target detail it may remove. A bound that already settles the question can end the work before regularization.

[MMP.13](#mmp13---infer-unknowns-statistically-under-a-stated-observation-model) constructs the inferential claim. Choose whether the use needs a repeated-sampling guarantee, a posterior probability or a prediction for a new outcome; derive that result under the record law and the additional assumptions it requires. Propagate joint uncertainty to the quantity the receiver actually needs. A regularized optimum alone supplies neither a posterior distribution nor a coverage guarantee.

Observation can also change the situation. C.28 and C.28.MR help formulate that intervention and replace the affected mechanism. [MMP.15](#mmp15---identify-an-intervention-effect-from-available-data) asks whether its requested consequence is determined by the available laws and causal assumptions. It derives an identifying expression, a sufficient bound or an unresolved difference between compatible causal accounts. MMP.13 can then estimate an identified quantity from finite records; an observational fit alone does not identify it.

A question about the same case under another action needs a further connection. [MMP.19](#mmp19---construct-and-bound-a-mathematical-counterfactual-comparison-under-a-causal-model) constructs the underlying conditions shared by its alternatives, uses MMP.7/.13 to recover what the factual record says about them, then applies the changed mechanisms. Separately known intervention distributions can leave their same-case relation ambiguous. The result can be a conditional response or a bound; a choice based only on expected outcomes can remain settled without resolving that ambiguity.

### MMP.Preface:3.4 - Turn uncertainty into a question about available action

[MMP.8](#mmp8---formulate-information-dependent-choices-mathematically) separates circumstances from choices and specifies when information arrives. It then formulates whether the work needs a fixed decision or an instruction depending on an available report, and whether performance is required for each admitted circumstance or on average under a stated probability law.

This formulation can expose a change needed in the work itself: observe earlier, distinguish another circumstance, permit another action or revise the requirement. [Method Engineering (ME)](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) develops the observing and acting methods and their composition. Their timing and resource demands return as premises of the mathematical question.

An information-dependent instruction needs both an obtainable report and a participant able to act on it at the stated time. Check this condition for the combined method. A correct reporting law and a correct decision calculation can still describe an instruction that the proposed work cannot perform.

[MMP.16](#mmp16---design-observations-to-separate-mathematical-model-alternatives) constructs the records that alternatives would produce under feasible designs. Compare the distinction an observation could resolve with its contribution to the receiving question and its burden. An informative report can still leave the preferred action unchanged.

[MMP.8.SD](#mmp8sd---construct-a-sequential-decision-model-from-information-and-consequences) develops continuing choice: retain a state or belief sufficient for the proposed decisions, construct transitions and observations, and derive how a present choice and its continuation determine the accumulated consequence. This joins observation design to action when timing, information or changes caused by observing matter.

### MMP.Preface:3.5 - Simplify, diagnose and revise for the required consequence

[MMP.9](#mmp9---derive-a-reduced-mathematical-model-of-state-evolution) starts with a source evolution law and quantities to retain. It derives their change, identifies the contribution that depends on removed detail and constructs a replacement through elimination, memory, added state, approximation or a sufficient bound. Initial conditions, inputs and the requested horizon determine whether the replacement serves the question. MMP.11 can supply a family for a still-unknown replacement relation.

[MMP.17](#mmp17---construct-a-surrogate-for-selected-model-responses) constructs a cheaper supplier for selected source-model responses. Choose the responses and input region from their intended use, build the replacement, and refine or return to the source where approximation changes the answer. Retaining a value can be insufficient when the receiver needs a derivative, tail event or explanation.

[MMP.18](#mmp18---couple-models-with-compatible-exchanges-and-scales) connects models through the quantities and conditions they exchange. Translate between their quantities and scales, supply any omitted influence needed by the connection, and retain shared information. Preserving a total amount, a constant field or a joint probability law requires different conditions on that connection. Matching software inputs and outputs does not establish those conditions.

[MMP.14](#mmp14---find-and-repair-a-mathematical-models-failed-predictions) helps when available observations reveal a consequential prediction failure, or a proposed use makes a comparison worth performing. Choose a discrepancy relevant to that use, derive predictions for comparable records, locate the mismatch and change the implicated relation or assumption. Recalculate the receiving consequence. Several repairs may explain one discrepancy; predictive improvement alone does not identify its cause. Existing records, an algebraic comparison or a restricted use can be sufficient.

When a premise or question changes, B.5.RR identifies the reasoning that depends on it and derives the revised consequence. If the argument must first be recovered, use B.5.RA. B.5.MPC.R develops the comparison when the difficulty concerns a connection among physical, mathematical and computational accounts. The repair may belong to subject assumptions, observation, mathematical formulation or computation.

These contributions admit several entry points and returns. A changed reporting procedure can require a new probability law while leaving the choice criterion intact. A changed criterion can require another instruction while leaving the reporting law intact. A changed intervention can require revising the model's mechanisms. Preserve each still-useful result and reconsider the part whose conditions changed.

### MMP.Preface:3.6 - Use the model-forming result across the Suite

The [Foundational Thinking Suite Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains the shared architecture and worked combinations. Mathematical Thinking constructs the objects and arguments a formulation needs. Physical or other subject methods supply the supported relations. Computational methods obtain the consequence, and the subject interpretation determines what that consequence lets the work do. Notational methods make these operations recoverable by their participants.

A particularly useful boundary concerns an unknown relation. MMP.11 can construct a family respecting supported conditions without selecting one fitted member. MMP.7 supplies a probabilistic recording law when that is the question, while C.16.IR can expose what a supplied indication or bound resolves. The appropriate next step can therefore be inference, a discriminating observation, an already sufficient bound, or action under the remaining uncertainty.

The Readme illustrates two further connections: carrying intervention consequences through a diagnostic report into a continuing instruction, and using cheaper components while retaining a sufficient combined answer. The needed intermediate result chooses the next method. General portfolio comparison and improvement remain with the existing FPF methods.

### MMP.Preface:3.7 - Constituent actions in ongoing work

While constructing a model of recorded observations, summing over unrecorded alternatives can be part of forming the observation law, within the modeling inquiry already under way. If the observing procedure changes from recording a below-threshold result to omitting the case entirely, that local operation must follow the changed selection rule. Mathematical calculation and knowledge of the subject may both be available while the intermediate description of observation is missing. MMP.7 helps construct the recorded-data law; obtaining the procedure's actual conditions still requires the appropriate source or contributor.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Use the parts of the vertical that can change the present result. A Method described here can require additional capability, available support and compatible resources at other grains.

## MMP.Preface:4 - Archetypal Grounding - A report, an instruction and a changed question

The Readme's [observation-to-action entry](#mmp-observation-to-action---turn-an-observing-model-into-a-workable-instruction) works the connection between MMP.7, MMP.8 and Method Engineering. One of two requests needs a scarce resource. Allocation follows a report produced through an unrecorded choice of channel.

MMP.7's operation first sums over the channel to obtain the reporting law. In the worked case, following the report succeeds with conditional probabilities 0.8 and 0.7 in the two circumstances. MMP.8 then asks what performance the instruction must supply. At least 0.65 success in each circumstance permits following the report. Zero failure does not. An average-success criterion with one circumstance occurring with probability 0.95 instead favours a fixed allocation among the four deterministic instructions considered.

The calculation changes the proposed way of working: whether to obtain and follow the report depends on the requirement, the circumstances it distinguishes and its cost. The receiving participant must get it before allocation. The complete elementary comparison is in [MMP.8:5.2 - Decide which participant gets a scarce resource](#mmp852---decide-which-participant-gets-a-scarce-resource). The Readme explains the return to the work when observation itself changes the situation. Each changed condition selects the contribution to revise.

### MMP.Preface:4.1 - A total is sufficient until the question changes

Suppose material passes through two cycles in two intermediate buffers. Each incoming portion retains 80% of its amount. Its fractions going to each buffer are unknown but constant across the cycles and independent of the portion's amount. Initially the amounts are `(10, 0)`. Both buffers have sufficient capacity; the material remains there until a receiver is selected and the later transfer begins. Transfer losses are neglected. How much capacity does that receiver need for all the material?

MMP.10 represents one cycle by `x_next = A*x`, where the two components of x are the amounts in the buffers. Nonnegative entries of A express the fractions received; each column sums to 0.8. MMP.11 retains the family defined by those conditions. Direct constraints suffice: choosing one fitted matrix would add information the situation has not supplied.

MMP.9 derives a simpler relation for the total `S = x_1 + x_2`: `S_next = 0.8*S`. After two cycles the total is 6.4, so capacity 7 suffices. The unknown distribution does not need to be resolved for this answer.

Now transfer only from the first buffer. One admissible model, `A = 0.8*I`, leaves 6.4 there. Another, `A = 0.8*[[0,0],[1,1]]`, leaves none there. Both give the same total. Capacity 7 still suffices, but the total alone cannot justify using a cheaper receiver of capacity 4. Return to the retained model family to ask which differences can affect the local amount. A further observation is useful if resolving those differences can change the receiver choice enough to justify its cost; C.16.IR and C.11.DUA support that question. The revised use changes what the model must preserve while leaving the total calculation valid for its original question.

Other bodies show different mathematical work: representing partial functions without distorting the requested count, deriving a bound after removing population detail, and constructing an unknown response while preserving its shape. Use their worked cases to learn the corresponding operations and their limits. The choice among those operations follows the difficulty, not the example's subject.

## MMP.Preface:5 - Conformance Checklist - Can the result do its intended work?

For the combination being used, ask:

- What question does the result answer, and how will that answer be interpreted or used?
- What do the chosen mathematical objects represent? Which cases, operations and distinctions are retained or excluded?
- Which relations come from the subject, which follow mathematically, and which remain hypotheses or adjustable contributions?
- What operation obtains the answer, and what information or capability does its performer need?
- Do the connected contributions agree on the situation, timing, admissible variation and required consequence?
- Does a restriction, ambiguity or approximation still permit the proposed use? If the question changes, which part must be reconsidered?

A small use may already have these answers in one body and its worked argument. Carry that answer forward. Seek an additional check or observation when its result can change the decision enough to justify the cost, using C.11.DUA.

## MMP.Preface:6 - Common Anti-Patterns and How to Avoid Them

The methods address consequential failures visible in their constructions. An encoding with ignored fields can give several records for one object; MMP.10 shows how that affects counting and interpretation. A probability law for the source event can omit the procedure that selected the available records; MMP.7 reconstructs that procedure's contribution. A decision rule can accidentally depend on information unavailable at the time of action; MMP.8 constructs the allowed dependence.

Recovering one best-fitting unknown can also hide a distinction the observations never resolved; MMP.12 separates recovery from the restriction that selects it. MMP.13 distinguishes the meaning of a confidence interval, a posterior probability and a prediction. MMP.14 shows why fitting an overall mean can leave the conditional prediction wrong, and why matching the data used to design a repair is not an untouched test of that repair.

Two further failures concern changing a model. Removing variables can leave a missing contribution in the retained evolution; MMP.9 derives that contribution before choosing its replacement. A flexible fitted function can violate a property known about the modeled relation; MMP.11 constructs the variation within that property and exposes any additional restriction.

Their repairs are specific. More numerical accuracy will not recover an excluded candidate object or an omitted relation. A different equation solver can help when the obtaining operation is the actual difficulty. Locate the consequential discrepancy before deciding what to change.

## MMP.Preface:7 - Consequences, biases and limits

The language makes intermediate modeling results available for subsequent work: an admissible representation, a reporting law, a recoverable target, an inferential conclusion, a repaired prediction, a feasible instruction, a reduced evolution law or a family retaining known relations. Their explicit conditions help collaborators divide the work and change one contribution while retaining others.

Construction costs time and mathematical effort. A familiar adequate model or direct calculation can be sufficient. A reusable model family or derivation becomes valuable when the work needs several cases, revisions or explanations. A remaining ambiguity can also be useful if it tells the team which proposed consequence is unresolved.

The worked cases favour small constructions whose reasoning is inspectable. Larger instances can require specialist mathematics, computational resources and subject knowledge. A proof of existence, a practical obtaining procedure and a reliable implementation have different requirements. Questions involving additional causal structures or specialist statistical constructions can require further methods and subject knowledge.

Prediction, explanation and intervention can also favour different accounts. Use C.2.8 and Explanation Design (EXD) when the recipient's recoverable understanding is at issue. A predictive success supplies the performance it demonstrates; explaining a phenomenon or changing a mechanism requires the corresponding content. Several models can contribute to the same project, with comparison and improvement supplied by the existing FPF methods.

## MMP.Preface:8 - Architectural Rationale - Organize by model-forming operations

The organization follows difficulties that arise before and during the construction of a mathematical question. An arrangement, a recorded observation and a changing quantity can require different operations. A solver catalogue begins after many of these choices; a universal modeling cycle usually leaves their detailed construction to the reader. Addressable methods preserve that detail while allowing different combinations.

The formulation part constructs admissible cases (MMP.10), a varying relation inside supported structure (MMP.11), and choices under available information (MMP.8 and its sequential refinement MMP.8.SD). The inference and revision part derives the recording law (MMP.7), formulates inverse recovery and regularization (MMP.12), constructs an inferential conclusion (MMP.13), repairs failed predictions (MMP.14), identifies intervention consequences (MMP.15), and designs discriminating observations (MMP.16). The model-change part derives reduced evolution (MMP.9), constructs a surrogate (MMP.17), and couples models through their exchanges (MMP.18). These parts help find a needed operation; they prescribe no fixed sequence.

Common reasoning remains in FPF: constructing a first account, applying a theory, connecting a mathematical result to its subject, describing change, replacing a mechanism and revising an argument. Mathematical Thinking develops the mathematical constructions. MMP develops the model-forming operation that uses those contributions; it keeps the actual subject premises visible. This division allows mathematical, physical and computational thinking to support one another while retaining their different questions.

The same division applies to modeling a working method. A function, path or state rule can describe an aspect of that method. Its mathematical properties become useful only through the correspondence with the work: what counts as input, which operations are available, what state can change and what result is returned. Method Engineering uses the consequence to retain, compose or change the working methods. A mathematical transformation may preserve returned values while changing time, information or execution demands; include the demands relevant to the proposed use.

A more detailed construction can need its own pattern and further refinements. A profile can combine several methods with additional conditions for a narrower practice, and one method can participate in several profiles. Specialization, composition and reuse describe different relations.

Reconsider a boundary when a recurring difficulty requires an unavailable operation, when two bodies develop the same operation, or when their combination leaves a needed contribution implicit. Preserve still-useful arguments, examples and source qualifications while changing the organization.

## MMP.Preface:9 - Source use and currentness

[Nguyen and Frigg's Scientific Representation](https://www.cambridge.org/core/elements/scientific-representation/A5C2A74998C15C36D4B204E4B3E70B1C), especially its comparison of inference and representation, helps separate deriving a consequence within a model from using it about a subject. This is a useful philosophical account of representation; the language's practical operations do not require adopting it as the only account of models.

The historical [SIMULA account by Nygaard and Dahl](https://www.cs.tufts.edu/comp/150FP/archive/kristen-nygaard/hopl-simula.pdf), printed pages 457-458, connects system description with simulation programming and reasoning from a description. [Modelica's equations and initialization](https://specification.modelica.org/maint/3.7/equations.html) provide a maintained example in which simultaneous relations and their computational treatment are distinct. These contributions support recovering the interpretation and obtaining operation rather than imposing one representation medium or execution order.

The individual bodies keep the operative sources for their mathematical construction. MMP.10 compares direct constraints with representation and refinement work in MiniZinc and Conjure. MMP.7 uses statistical workflow and observation/selection constructions. MMP.8 compares fixed and information-dependent choices. MMP.9 uses closure and reduction research. MMP.11 compares constrained construction with data-driven discovery and hybrid known/unknown relations. MMP.12 compares regularization constructions with unregularized recovery and learned restrictions. MMP.13 and MMP.14 use statistical workflow to connect inference, consequential prediction checks and localized revision; they distinguish mathematical calibration from agreement with the modeled subject. MMP.15 distinguishes identification from estimation using causal identification and population-transfer constructions. MMP.16 combines discrimination and decision-valued observation design. MMP.8.SD develops decision-sufficient state and continuation; MMP.17 compares surrogate and correction constructions; MMP.18 connects interface-preserving maps with coherent shared information. Their bodies give the operative sources and limits. Each source contributes at its stated scope; the resulting organization and elementary cross-practice examples are conceptual synthesis.

Source changes matter when they alter an operation, its assumptions, its practical cost or the conclusion it supports. Return to the affected body's comparison in that case. A new implementation can change how cheaply a result is obtained while leaving the mathematical relation intact; a newly recognized observation or intervention effect can instead require a different model.

## MMP.Preface:10 - Relations to continued inquiry and work

B.5.QD helps turn a result, obstruction or unresolved difference into a further question. A model can therefore contribute before it supplies a final numerical answer: it may expose a new distinction, make a comparison possible or suggest a different way of working. Choose further inquiry in relation to the work it could enable.

When the difficulty is acquiring or transferring the ability to use such constructions, Human Capability Development (HCD), Explanation Design (EXD) and the relevant development methods address that learning and use. Their question differs from whether one displayed calculation is correct. Retain the preparation and support a participant needs when dividing work among people and AI agents.

For evaluating alternatives and improving them, reuse FPF's characteristic, comparison and development methods. Define the consequences that matter for the question, including approximation, explanatory use, effort and ability to revise the model when relevant. Different models may supply different contributions. The next modeling operation follows the deficiency or opportunity that comparison identifies.

## MMP.Preface:End

# A. Formulate the subject question

## MMP.10 - Construct and Revise a Mathematical Constraint Formulation

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.10:1 - Problem frame

Use this pattern when you know conditions that a possible object or situation must satisfy, but still need to express its possibilities mathematically. You may be looking for an arrangement, a quantity, a shape or a rule of action. Choosing variables already makes decisions: a number can express an amount, but an ordered list, a set of members and an unknown function permit different operations and different possible answers.

Start by describing one candidate object and what would make it admissible. Choose a way to represent it, then distinguish two kinds of condition: those needed for the representation to denote such an object, and those expressing the requirements on that object. This produces a mathematical problem that can be reasoned about or handed to an appropriate computational method.

The result consists of variables with their domains, joint conditions, the requested operation on their solutions and a way to interpret the answer. It can be enough to find one feasible case; another question may require all possible values, a preferred case or a count. The chosen representation must support that particular result.

You need to understand the objects and requirements in the original question, elementary logical conditions and the mathematics used to express them. A mathematical collaborator can construct the expressions while you resolve their intended meaning. When a suitable formulation already exists, use it. When the missing contribution is a physical relation, an observation law or a rule of change, obtain that relation through the relevant method before translating it. B.5.FM supplies the broader first-model construction; MMP.7 and MMP.9 develop observation and reduced-evolution constructions.

### MMP.10:2 - Problem

A convenient variable can leave out the possibility that matters. A single interval cannot represent an activity that may pause. A membership bit cannot record repeated membership. Coefficients of a straight line cannot describe every continuous curve. These restrictions may be useful, but they change which cases the formulation can answer for.

Representation can also add possibilities. A table intended to describe a function can allow two values for one argument unless its conditions exclude that case. Extra fields can create several records of the same object. A calculation over those records can then answer a different counting or probability question.

The difficulty is to construct the mathematical expression of the intended possibilities, including their joint restrictions and the requested result. Solving the resulting equations addresses the problem only after that construction has been made.

### MMP.10:3 - Forces

| Force | Consequence for the construction |
| --- | --- |
| Faithful possibilities and useful operations | A familiar representation may make calculation easy while excluding an intended case or hiding a useful relation. |
| Structured objects and scalar tools | A function, set or sequence may need several scalar variables and additional conditions to represent its structure. |
| Shared restrictions and local descriptions | Separate bounds on individual variables can lose a condition on their combination. |
| Simple answer and rich solution set | A single witness needs less from the representation than counting, sampling or claiming that no witness exists. |
| Reuse and changed requirements | A derived constraint that helped an earlier formulation may exclude valid cases after the requirement changes. |

### MMP.10:4 - Solution

**Describe the possible object → choose its representation → derive the representation conditions → express the requirements and question → obtain and interpret a result → revise the affected construction.**

#### MMP.10:4.1 - Recover what varies and what the question asks

Describe a candidate before choosing scalar variables. Is it an amount, a collection, a sequence, an assignment, a function or another mathematical object? Which distinctions can change the answer? A set retains membership; a multiset also retains multiplicity; a sequence retains positions. Choose among them from the question.

Separate supplied quantities from unknowns. Among unknowns, distinguish what is to be inferred, what can be chosen and what can vary independently of that choice. If a choice uses an observation, specify when the observation becomes available; MMP.8 constructs the resulting information-dependent requirement. An unknown value does not become a freely selectable design variable merely by appearing in the same equation.

State the requested result. Existence asks whether at least one admissible object can be constructed. Inference asks what a quantity can be across admissible objects. Selection adds a preference among them. Counting and sampling depend on how individual objects are distinguished. Keep those requests separate while choosing the representation.

#### MMP.10:4.2 - Construct variables that represent the object

Choose an expression from which a candidate can be recovered. Give each variable a domain and any unit or reference point needed by its operations. A machine label ranges over names; arithmetic on the label requires a separate meaning. A count ranges over nonnegative integers; an amount may be divisible. State a finite bound when the task supplies one. Adding a bound solely to finish a search restricts the question to that bound.

For a structured object, compare representations by the operations you need. A function on a finite set can use one output variable for each input. Alternatively, a table of Boolean indicators can say which input-output pairs belong to its graph. The first expression makes function evaluation easy to state. The second makes some relations among pairs visible, but needs conditions to make the table a function. For a partial function, represent undefinedness as well as defined values.

Keep a shared quantity shared. If several equations use the same unknown offset, one offset variable must occur in all of them. Introducing a separate offset in each equation creates additional possibilities. Conversely, equating genuinely separate values can remove possibilities.

For a function or shape over an infinite domain, choosing finitely many coefficients also chooses a family. Identify that family and whether it expresses the intended possibilities or is a deliberate restriction. For example, the conditions on a continuous function may allow curved solutions even when no affine function satisfies them. A useful restricted family can be sufficient for finding a witness; failure inside it leaves the larger family unresolved.

#### MMP.10:4.3 - Derive structural conditions and translate requirements

Ask what must hold for a variable assignment to describe one candidate of the intended kind. With Boolean entries `r_ij` describing the graph of a total function, require `sum_j r_ij = 1` for every input i. For a partial function, replace this with `sum_j r_ij <= 1`; an all-zero row then means undefined at that input. For an injective function, additional conditions on columns express the extra requirement.

These conditions have different reasons. One value per input comes from choosing a total function. Injectivity comes from the particular problem, if it requires injectivity. Keep their reasons recoverable so that a later change from total to partial or from injective to unrestricted has a local repair.

Express the original requirements using the represented objects. Conjoin conditions that must hold for the same assignment. Use disjunction for allowed alternatives and implication when choosing an option imposes a condition. An implication alone supplies no timing; use time quantities or an explicit sequence when order matters. Preserve a coupled condition such as `x+y=1` rather than replacing it by separate bounds on x and y.

When a bijection between representations is established, MATH.7 supplies transport of operations, relations and compound expressions. For a representation with several records per object, C.29.1 supplies the more general correspondence. Use the decoding of a record to express the requirement on its object. If a condition is rewritten to fit the receiving notation, derive that expression from the original relation and the structural conditions. This is where a missing index, an undefined value or a lost alternative can change the formulation.

Additional constraints can expose consequences and help the obtaining method. Derive them from the retained requirements, and preserve that dependence. Fewer variables or more constraints do not alone establish a faster method; compare the actual resulting work when efficiency matters.

#### MMP.10:4.4 - Make the answer correspond to the question

Define how to recover the requested object or quantity from a satisfying assignment. Then work in both directions: represent an intended admissible case, and interpret an allowed assignment. Use the construction and its conditions to establish the reach of this correspondence. A small case can expose a mistake; a claim about every case needs the corresponding argument.

Match that reach to the requested result:

- To use a witness, its recovered object must satisfy the original requirements.
- To conclude that no intended object exists from inconsistency of the formulation, every intended object must have a representation in it.
- To infer all possible values, translate the quantity as well as the admissible cases; C.16.IR supplies the projection question.
- To optimize, translate the objective and preference as well as feasibility. Distinguish a bound from a value attained by an object.
- To count or sample objects, account for multiple representations of the same object. One representation per object is one solution; weighting or grouping representations can be another.

Auxiliary variables can change what a returned number means. Suppose a finite nonempty set of finish times `f_i` is determined by the other variables. Introduce a real auxiliary T used only in `T >= f_i` and the objective of minimizing T. Lowering T to `max_i f_i` then preserves feasibility, so at an attained optimum T equals the latest finish. If T must instead be an integer and the latest finish is 1/2, its minimum is 1. A merely feasible intermediate T can also exceed the latest finish. Recover the actual latest finish as `max_i f_i`; infer equality with T only when its domain and other conditions permit that lowering.

Choose an obtaining method for the constructed question. Manual substitution may suffice; another problem needs a numerical method, symbolic derivation or search. C.29.2 separates the required mathematical result from the procedure and its execution. Use that method's actual conclusion: finding no case within a time budget differs from establishing inconsistency. Preserve any restriction or approximation when returning the result to the original question through C.29.1.

#### MMP.10:4.5 - Revise the formulation from the changed requirement

Locate the changed participant, domain, relation or requested result. Changing a supplied amount can retain the same representation. Allowing interruptions changes what an activity description must express. Changing a total function to a partial one changes structural conditions. Changing existence to counting can make duplicate records material.

Revisit constraints derived from the old requirement as well as the original formula. Reconstruct the affected expressions and answer interpretation, retaining the unaffected ones. If a solving tool cannot support the needed object, construct a suitable representation or choose another obtaining method; keep any deliberate restriction visible in the returned conclusion.

Stop with a usable formulation and interpretation, an adequate answer, or a named missing relation or operation. Choose further derivation, observation or computation according to what it can change in the work and its cost; C.11.DUA supplies that decision. When the formulated object is itself a working method, return its proposed change to ME for interpretation and use. The mathematical model supplies a reason for the change; the working method still has to be performed under its stated conditions.

### MMP.10:5 - Archetypal Grounding

#### MMP.10:5.1 - Construct an unknown rule from requirements on its repetitions

A device has three labeled modes A, B and C. The required rule changes the mode on every use and returns to the starting mode after three uses. The question is to construct a deterministic rule, with no additional internal state. The rule itself is the unknown object.

Let `S={A,B,C}`. Choose one output variable `p_i in S` for each input i. The requirements become `p_i != i` and `p_(p_(p_i)) = i` for every i. Function composition gives the meaning of the repeated application. MATH.1 constructs composable paths; MATH.5 extends an interpretation of their elementary steps to the compounds.

To express the rule by selected pairs instead, choose `r_ij in {0,1}`. Add `sum_j r_ij=1` for each row, `r_ii=0`, and, for all i,j,k, `(r_ij=1 AND r_jk=1) implies r_ki=1`. The row condition makes a function. The implication expresses the return after three uses: the first two selected transitions determine a required third.

Recover p by taking the unique selected column in each row. Conversely, p creates the table by selecting exactly its output pair in each row. These constructions are inverse. The triple-application requirement is therefore the same in both formulations, with MATH.7 carrying that relation. A rule A→B→C→A and its reverse both satisfy it.

There are precisely two such rules. From `p^3=id`, p is invertible with inverse `p^2`. Its cycles have lengths dividing three. Since a one-element cycle is forbidden, the three modes form one three-element cycle, with two possible orientations. This reasoning proves completeness; listing two examples alone would not.

Change the device to four modes, retaining the three-use return and no unchanged mode. A permutation of four elements cannot partition them into cycles all of length three, so no rule exists under these conditions. Change instead to a return after two uses. The conditions become `p_(p_i)=i` and `p_i!=i`; the indicator formulation requires symmetry `r_ij=r_ji`. It admits three pairings of four modes. Remove the former three-use implication: leaving it in the formulation would make the new, feasible requirement appear impossible.

The result is a rule that can be implemented and its stated scope: deterministic changes of the visible mode without hidden state. A proposal with additional state describes a different device and needs a new account of its operation.

#### MMP.10:5.2 - Preserve existence while repairing a count

An optional assignment gives each of two named requests either no selected option or one of options 0 and 1. Different requests may select the same option. This is a partial function from the two requests to `{0,1}`. Each request has three possibilities, so there are nine assignments.

Suppose the storage format gives each request two bits: d says whether an option is defined, and q gives its value when defined. When `d=0`, q is ignored. All sixteen four-bit records denote valid partial assignments. Every assignment has a record, so the representation can support an existence query with translated requirements.

It does not preserve the count. The empty assignment has four records, each of the four assignments defined on exactly one request has two records, and each of the four total assignments has one record. Thus `4 + 4*2 + 4 = 16`. Uniform selection among records gives probability `4/16` to the empty assignment and `1/16` to each total assignment, rather than the `1/9` obtained by uniform selection among assignments.

For a count or uniform assignment sample, one repair is the structural condition `d=0 implies q=0` for each request. There are now three admissible bit pairs per request and nine records, one per assignment. Another is a single variable with domain `{absent,0,1}` per request. If the sixteen-record storage representation must remain, group or weight its records using the multiplicities instead. To sample the nine assignments uniformly, give each record of an assignment with m records probability `1/(9*m)`. The probabilities of all m records then sum to `1/9` for that assignment. Thus each record of the empty assignment receives `1/36`, each record of a one-request assignment `1/18`, and each total-assignment record `1/9`. C.29.1 supplies the required correspondence; MMP.7 supplies a probability law when sampling is the intended operation.

The original existence use can remain sufficient. The new count or sampling question exposes the need for the additional construction. No change in the underlying possible assignments is intended.

#### MMP.10:5.3 - Keep quantities and domain restrictions together

A preparation requires one litre containing 35 percent solute by volume, using solutions A and B at 20 and 80 percent. Assume solute is conserved and component volumes add in this preparation. Those subject assumptions supply the relations. Let x and y be the respective volumes in litres; choose nonnegative real domains because the amounts can initially be divided freely.

The joint conditions are `x+y=1` and `0.2*x+0.8*y=0.35`. Substitution gives `x=0.75`, `y=0.25`. Both the total and solute requirements hold for those amounts. Separate bounds `0<=x<=1` and `0<=y<=1` would lose their required total.

Now only whole half-litre doses may be used. Change the representation to `x=m/2`, `y=n/2`, with nonnegative integers m and n. The volume equation becomes `m+n=2`. Its possibilities `(m,n)=(2,0),(1,1),(0,2)` give solute amounts 0.2, 0.5 and 0.8 litre. None supplies 0.35 litre. Rounding the former solution changes the preparation; it does not satisfy its original condition.

If the required concentration changes to 50 percent, one dose of each solution works. The subject relations and unit remain, while the requirement and feasible assignment change. If mixing changes volume or solute, obtain the replacement subject relation before revising its mathematical expression.

### MMP.10:6 - Bias-Annotation

Tool familiarity can make scalar variables appear inevitable and conceal a different object or useful operation. Begin with the candidate object and its requirements. Compare representations when that comparison can change the answer or obtaining effort.

Compactness can hide duplicate records or omitted possibilities. Judge the representation by the requested result and the work needed to obtain it.

### MMP.10:7 - Conformance Checklist

- Can the reader identify a candidate object before interpreting the variables, including what is supplied, unknown or selectable?
- Do domains, units, shared quantities and definedness express the intended possibilities?
- Which conditions make the representation denote an object, and which express requirements on it?
- Do conditions that must hold together refer to the same assignment? Are alternatives and conditional restrictions preserved?
- Can intended cases be represented and satisfying assignments be interpreted at the reach required by the question?
- Does the requested value, preference, count or probability survive the representation, including auxiliary values and duplicate records?
- What does the obtaining method actually establish, and which changed requirement reopens which construction?

### MMP.10:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it changes the result | Repair |
| --- | --- | --- |
| Use separate bounds in place of a joint relation. | The same assignment can violate the lost total or coupling. | Retain the relation with its shared variables. |
| Number labels and use their arithmetic as a subject law. | Addition or order on the labels may describe no operation on the labeled objects. | Supply the intended operation or use names as names. |
| Read an empty restricted search as absence in the original problem. | Intended cases may lie outside the chosen bound or family. | Return the restricted conclusion or extend the representation. |
| Count records as objects after adding auxiliary fields. | Multiple records can describe one object and alter the count or sampling law. | Canonicalize, group or weight by the needed correspondence. |
| Keep a consequence of a replaced requirement. | It can remove the newly allowed cases, as in the changed rule in :5.1. | Re-derive the affected constraints. |

### MMP.10:9 - Consequences

The mathematical problem becomes available for reasoning, computation and revision without leaving the interpretation of its variables implicit. A solver result can be returned as the arrangement, quantity or unresolved distinction that the work needs.

Constructing and maintaining a second representation has a cost. Direct formulation is often sufficient when the objects and their restrictions already have a clear expression. A structured intermediate formulation becomes useful when it preserves meaning across several receiving notations, helps revise requirements or exposes a calculation that the first representation hid. Any efficiency advantage depends on the resulting obtaining method.

### MMP.10:10 - Architectural Rationale

Mathematical modeling often starts with choosing how possible objects will be expressed. The choice determines which restrictions must be added and which results can be recovered. Separating representation conditions, subject requirements and the operation on solutions makes revisions local: a changed requirement need not replace the representation, and a new representation need not change the intended possibilities.

An operation can itself be the unknown object. The finite-rule case therefore treats repeated action as a requirement on a function and uses composition to express it. The same organization applies to other structured objects, while their mathematics supplies the needed constructions and proofs. MATH.7 explains reversible transport after the maps are available; this pattern develops the modeling choice and construction of those expressions, including cases that need a many-to-one correspondence.

The connection to computation runs in both directions. A mathematical formulation supplies the problem a procedure must answer. The operations supported by a procedure can suggest a different expression of that problem. Meaning is retained through the representation conditions and answer interpretation, while performance is judged on the resulting work.

### MMP.10:11 - SoTA-Echoing

The [MiniZinc Handbook 2.10.1, modeling and efficiency sections](https://docs.minizinc.org/en/stable/efficient.html) develops alternative models, derived constraints and interactions with solving methods. Adopt comparison of the resulting work; a smaller variable count alone does not settle it. A direct scalar formulation remains economical when its meaning is already clear.

[Akgun and colleagues, Conjure (2023), sections 2-4](https://www.ijcai.org/proceedings/2023/0765.pdf) separates representation selection from expression refinement and introduces structural constraints during refinement. Adopt this construction when structured objects would otherwise disappear into unexplained scalar choices. Conjure's finite combinatorial scope and model-selection heuristic remain specific to that approach. They do not establish a general best representation or performance guarantee.

The [Essence language reference, function and relation domains](https://conjure.readthedocs.io/en/latest/essence.html) makes such choices as partiality and cardinality explicit. This informs :4.2-4.3; its particular syntax is optional. The ordinary alternative is to express those conditions directly in a familiar mathematical notation.

For infinitely many possible objects, a finite parameterization needs its own coverage or approximation argument. Consider continuous nonnegative functions f on `[0,1]`, with `f(0)=f(1)=0` and integral one. An affine parameterization permits only the zero function after the endpoint conditions, so it fails. The quadratic `f(t)=6*t*(1-t)` satisfies every requirement. This authored countercase explains why the finite structured-model sources do not settle general parameterization. C.29.1 supplies the interpretation of a restriction; the relevant mathematical method supplies a suitable larger family or approximation.

To apply the formulation in another subject, obtain the relations and mathematical operations needed to express its requirements. Reconsider the representation when a new requirement, result kind or obtaining method changes what it needs to preserve or make affordable.

### MMP.10:12 - Relations

- **B.5.FM and B.5.TU:** construct a first account and connect a subject theory to the encountered problem. This pattern translates its candidate objects and conditions into a mathematical formulation.
- **MATH.1 and MATH.5:** construct composable paths and extend an assignment on elementary steps to compounds while preserving operations and equations. MATH.16 chooses a mathematical construction from the maps it must support. MATH.7 transports structure when the required bijections have been constructed.
- **C.29.1 and C.29.2:** supply correspondence, answer recovery and the separation of a mathematical result from its obtaining procedure and execution.
- **C.16.IR:** determines what a compatible set permits one to infer through projection and constancy of the requested quantity.
- **MMP.7 and MMP.8:** construct observation probabilities and information-dependent choices. A formulation's variables retain those probabilistic and temporal meanings.
- **MMP.9:** derives a reduced evolution law when retained quantities depend on eliminated contributions. The resulting law can supply relations used here.
- **C.11.DUA and E.22/E.23:** choose worthwhile further inquiry and organize evaluation and improvement of a formulation or its obtaining work.
- **ME:** uses the mathematical result when constructing or changing a working method. Its performance in the subject remains distinct from the formal properties of its description.

### MMP.10:End

## MMP.11 - Construct a Mathematical Model Family from Known Relations

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.11:1 - Problem frame

Use this pattern when part of a model is supported, but a function or other relation is still unknown. You may know which quantities interact, what must be conserved, or how a response begins and ends, while lacking its form between those conditions. You need candidate models that retain this knowledge while allowing the missing contribution to vary.

Begin by locating the unknown contribution in the relations needed for the question. Say what it takes as input, what it supplies and which properties its variation must preserve. Construct a family for that contribution, then put it back into the model. For a response that rises from zero to one, a family of curves constrained by those properties gives a different starting point from an unrestricted fitted curve.

The first useful result is a family of models, its remaining adjustable parts and the restrictions introduced by its construction. It may already give a sufficient bound. When observations are available, the same construction lets you ask which functions, parameters or consequences those observations can distinguish.

You need the subject grounds for the retained relations and enough mathematics to construct and use the family, or access to that mathematical contribution. A known adequate relation can be used directly. An unknown numerical parameter inside a suitable family normally needs its estimation method. Use this pattern when the family itself needs construction or revision. B.5.FM and B.5.TU help when the missing contribution is the subject account or theory from which a relation should come.

### MMP.11:2 - Problem

A familiar formula can exclude the response being sought. Giving a learner unrestricted freedom can create the opposite problem: the fitted response may violate a known relation. Fitting two interacting contributions independently can also destroy a property that depends on their connection.

Agreement with recorded outputs leaves another difficulty. Several parameter settings may define the same function, and several functions may produce the same observations. Some receiving questions distinguish those alternatives; others need only a consequence on which they agree. Choosing one fitted instance can conceal this difference.

The modeling work is to construct the adjustable contribution in a form that retains the supported relations, then determine what that family can establish for the present question. The construction itself may impose additional restrictions, so its expressive limits belong to the answer.

### MMP.11:3 - Forces

| Force | Tension |
| --- | --- |
| Retained knowledge and flexibility | A structural relation can rule out impossible candidates; an unsupported restriction can remove the needed one. |
| Local fitting and coupled behavior | A contribution can fit its own samples while disrupting the model in which it is used. |
| Simple representation and family coverage | A small parameterization is easier to fit but can omit admissible functions. |
| Parameter recovery and useful inference | Parameters may remain ambiguous while a required consequence is determined. |
| Prediction and intervention | Two accounts can agree during observation and differ after one mechanism is changed. |

### MMP.11:4 - Solution

Locate the missing relation, separate what is retained from what may vary, construct the adjustable family, and derive its contribution to the receiving question. Observation or computation is then selected for what remains unresolved.

#### MMP.11:4.1 - Locate the contribution that may change

State the result wanted from the model. Identify the unknown relation and the quantities it connects. Keep its inputs, output, domain, units and permitted dependence explicit enough to substitute a candidate into the surrounding relations. A function of present state, a function of its history and a random response law admit different constructions. If equal proposed inputs require different deterministic outputs in the admitted circumstances, revise the inputs or retain those alternatives. Greater flexibility of a single-valued function cannot supply both outputs. For a dynamic model, A.3.3.TR supplies the corresponding reconsideration of state.

Recover the grounds and application range of the relations you retain. A balance may be required by the chosen boundary; monotonicity may hold only over one operating range; a shape assumption may be provisional. Keep an allowed discrepancy when the subject account supplies one. A convenient property is not automatically a property of the subject.

Use the smallest part that can be varied without silently changing another retained claim. If an adjustable term can absorb a known contribution, include that possibility in the inference question. Section :5.2 shows an ambiguity between two gross transfers even when their net effect is known.

#### MMP.11:4.2 - Construct the permitted variation

Translate each retained property into a mathematical condition, then choose a construction that satisfies it. MMP.10 supplies the general work of representing candidate objects and their conditions. Here the object being constructed is a family of relations to insert into the model. Direct conditions may already give a workable representation of that family. Constructing through free elements is useful when their variation should preserve the conditions; compare its obtaining and revision operations with those of the direct representation.

A useful construction separates a fixed part from free variation. If a linear operator L must satisfy `L(g)=b`, find one particular solution g0 and choose a correction h with `L(h)=0`. Then `g=g0+h` retains the condition. This describes every solution only if the admitted corrections cover the whole null space in the chosen function domain. Restricting h to a few basis functions supplies a smaller family. Establish the linearity and domain before using this construction.

For a sign, bound or shape condition, construct through a map whose output has that property. Nonnegative weights can be normalized to probabilities. Integrating a nonnegative function can produce a nondecreasing response. Work out the domain and boundary of the resulting family: strict positivity excludes zeros, and an integral of an ordinary integrable function produces an absolutely continuous curve. Section :5.1 develops one such construction and its restriction.

When a property depends on coupling, construct the coupled contribution. Using the same transfer with opposite signs in two balance equations preserves their total. Two separately fitted right-hand sides have no such identity unless their joint conditions supply it. Use A.3.3.TR to assemble a change rule from the interacting relations.

A penalty during fitting offers a different construction: it discourages violations while allowing them. Use it when that allowance fits the question. If the account requires an identity, either build it into the representation or use an obtaining method that enforces it. The size of a training penalty does not by itself establish the identity.

#### MMP.11:4.3 - Choose the representation and its range

Choose a representation whose operations fit the required use and available resources. A table can represent a finite function. A basis expansion or program can retain a useful structure. A neural representation can supply a flexible adjustable function. The meaning of its inputs and outputs, and the retained relations, remain part of the model.

Check two different questions. Does every admitted parameter setting produce a relation allowed by the construction? Does the construction cover all relations needed for the present conclusion? A witness may need only one candidate; an impossibility claim over all admissible models needs coverage of that whole family or another sufficient argument.

State restrictions introduced by knots, basis functions, regularity, network architecture or domain truncation when they can change the answer. A numerical fit inside the restricted family answers for that family. If its consequence is sufficient, a more flexible family may add only cost. If the missing case matters, change the representation.

Different parameters can denote the same function. Recover the function or consequence needed by the receiving use rather than demanding unique parameters by default. Section :5.3 gives a normalization redundancy. Use MATH.7 when a change of representation has constructed inverse maps; use C.29.1 when correspondence is more general.

#### MMP.11:4.4 - Put the family into the model before using its fit

Substitute the adjustable contribution into the relations that consume it. Derive the resulting observable or answer condition with shared quantities kept shared. An error measured on an isolated contribution and an error in the coupled output are different fitting questions.

Choose the insertion point from what must remain meaningful. In a component model, inserting an unknown relation before algebraic elimination can retain a named component's inputs, outputs and connections. Adding a correction after elimination can be simpler, but the correction then acts on the transformed relations. Recover how it affects the properties needed by the original question. A reduced model may use MMP.9 to derive the contribution its simplification leaves open.

Represent how observations are produced. MMP.7 derives a probability law for records when probability is needed; C.16.IR uses the supplied indication relation to obtain compatible cases or bounds. Fitting an unobserved internal term as if it were measured supplies an extra premise. If that premise is unavailable, fit or constrain through the observable relation instead.

For a dynamic or implicitly defined model, obtain the consequence through its coupled equations and conditions. A good component fit does not settle whether the resulting evolution, initialization or constraints are usable. Apply the mathematical and computational method appropriate to the stated consequence; C.29.2 helps formulate its obtaining operation.

#### MMP.11:4.5 - Determine which remaining differences matter

Ask what the available observations constrain: the adjustable parameters, the unknown function over a stated domain, or a particular consequence. Use C.16.IR on the resulting observation relation. The function can remain undetermined away from the observed inputs even when its recorded values are fixed.

When ambiguity could change the answer, construct two admitted candidates with the same relevant observations and different receiving consequences. Such candidates show what further information must distinguish. If all compatible candidates or a sufficient bound give the same answer to the present question, use that answer without resolving unrelated differences.

Repeated numerical fits can discover alternatives. Agreement of finitely many fitted instances leaves unsearched alternatives possible. A claim of uniqueness needs its mathematical or statistical grounds; a sufficient decision can require much less. Numerical search failure also differs from a proof that the family is inconsistent with the observations.

Change the question explicitly when a new use requires it. An intervention may distinguish models with the same observational behavior. C.28.MR supplies the replacement of the affected mechanism under its causal premises. Explanation or modification of a working method can require structure beyond that needed for prediction; characterize the required explanatory use through C.2.8 and Explanation Design (EXD).

#### MMP.11:4.6 - Use the consequence or revise the family

Return the result with the family, input range and conditions that affect its use. It may be a candidate relation, a bound, a conditional prediction, a supported instruction or a located missing contribution. When the model is used to change a working method, Method Engineering receives the consequence and the relations the proposed change must preserve.

Revise the part whose restriction prevents the needed result: the subject premise, permitted dependence, representation, observation relation or obtaining method. Use B.5.RR to carry a changed premise or question through the reasoning. General comparison, portfolios and improvement use the existing C.16, C.11 and E.22/E.23 methods when those questions arise.

Stop when the receiving use has a sufficient answer or the missing contribution is clear enough to obtain. Use C.11.DUA when deciding whether another observation, a richer family or further computation can improve that use enough to warrant its cost. A more detailed family is valuable only through what it enables.

### MMP.11:5 - Archetypal Grounding

#### MMP.11:5.1 - Construct a response from its known shape

A normalized input u lies in [0,1]. The subject account supports a nondecreasing response r with `r(0)=0` and `r(1)=1`. Its intermediate shape is unknown. Begin with these properties, rather than choosing a straight line as the only candidate.

Choose an integrable h with `h(u)>=0` almost everywhere and `H=integral_0^1 h(v) dv>0`. Define

`r(u)=integral_0^u h(v) dv / H`.

The endpoints follow by substitution. For `u2>=u1`, the difference is the nonnegative integral of h over [u1,u2], divided by H. Thus every member is nondecreasing. These curves are absolutely continuous. Every absolutely continuous nondecreasing response with these endpoints has such a representation using its almost-everywhere derivative, but a jump response is outside this family. The needed regularity must come from the question or remain a declared restriction.

For a small calculable family, use linear segments through (0,0), (1/4,q), (1/2,1/2) and (1,1). Their slopes are `4*q`, `2-4*q` and 1. They are nonnegative exactly when `0<=q<=1/2`. This is a construction of admissible candidates, not a conclusion from measurements alone.

Suppose observations establish only the three values at 0, 1/2 and 1. Every q in that interval agrees with them. The consequence `r(1/4)<=0.6` follows for this whole family; it also follows for every nondecreasing response with the given midpoint. There is no need to identify q for that question.

Now the receiving use asks whether `r(1/4)>0.3`. Candidates q=0.2 and q=0.4 satisfy the same observations and give opposite answers. Another repetition at the three old input values does not distinguish these ideal candidates. An observation near the disputed input may help; its precision and cost belong to that new question. Alternatively, a supported additional shape relation could narrow the family.

#### MMP.11:5.2 - Retain an exchange balance without inventing its mechanism

Two nonnegative amounts x and y exchange a conserved total N. The forward and reverse rates are unknown. Use locally Lipschitz nonnegative rate functions a(x,y) and b(x,y), defined on a neighborhood of the nonnegative states being used, and construct

`q=x*a(x,y)-y*b(x,y)`,

`x_dot=-q`, `y_dot=q`.

Adding the two equations gives zero change in x+y for every admitted a and b. At x=0, `x_dot=y*b(0,y)>=0`; at y=0, `y_dot=x*a(x,0)>=0`. With these regularity conditions the continuous-time solution preserves nonnegativity. These are properties of the coupled construction. The applicability of conserved exchange to the subject remains a premise.

Even complete knowledge of q need not identify the gross transfers. For any nonnegative locally Lipschitz h, define

`a_new=a+y*h`, `b_new=b+x*h`.

The two added contributions to q are `x*y*h` and `-y*x*h`, which cancel. The whole observed evolution is unchanged. This is an algebraic family of alternatives, not merely several successful numerical fits.

For a dimensionless instance, take a=b=1. The alternative h=1 gives `a_new=1+y` and `b_new=1+x`, yet both models have `q=x-y`. At x=2, y=1 they both predict `x_dot=-1`.

Change the question: a proposed intervention suppresses only the reverse transfer while leaving the forward rate law applicable. Under that causal premise, C.28.MR replaces the reverse contribution by zero. The first model gives `x_dot=-2`; the second gives `x_dot=-4` at the same state. Ordinary observations of x and y under the unchanged mechanisms cannot choose between these accounts. A prediction under the old operation can still be useful; the proposed intervention needs a contribution that distinguishes the mechanisms or a sufficient bound covering them.

For dimensional quantities, a and b have inverse-time units, while h has inverse-amount-inverse-time units. Restoring units prevents treating the added terms as arbitrary dimensionless corrections.

#### MMP.11:5.3 - Construct probabilities while keeping boundary outcomes

A report has three possible outcomes. Let `w_i>=0` and let their sum W be positive. Set `p_i=w_i/W`. Every candidate has nonnegative probabilities summing to one. Conversely, every probability vector on these outcomes is represented by choosing w=p. Thus this construction includes zero-probability outcomes.

The weights (0,1,3) and (0,2,6) both give probabilities (0,1/4,3/4). The parameter vector is redundant even if the probability vector becomes fully determined. There is no need to distinguish those weights when the receiving question uses only the law.

A strictly positive parameterization, such as exponentiating every finite unconstrained parameter before normalization, excludes zero probabilities. It can approximate a zero closely but cannot express it with finite parameters. If the subject account rules out the first outcome, retain that zero in the construction and normalize weights for the remaining outcomes. Whether a very small nonzero value would suffice depends on the receiving question.

The constructed p is a family member, not yet an estimate from data. MMP.7 composes it with selection, rounding or other recording behavior. The appropriate statistical method then determines what the observations support. Changing the recording procedure can change that inference without changing the underlying outcome family.

### MMP.11:6 - Bias-Annotation

Familiar formulas can turn an assumed shape into an unnoticed restriction. Flexible fitting can conceal a different commitment: the selected inputs, architecture and loss still determine which functions can be obtained. Recover those choices when they affect the receiving result.

A respected subject law can also be applied outside its range or boundary. Preserve its grounds and allowed discrepancy. If no supported structural restriction is available, an unrestricted family can be a reasonable candidate for a bounded use; further structure must earn its place through the subject question.

### MMP.11:7 - Conformance Checklist

- The unknown contribution has interpretable arguments, result, domain and permitted dependence.
- The retained relations have subject grounds and an application range.
- The construction shows why admitted adjustable values preserve the required properties.
- Restrictions introduced by representation are carried into conclusions that depend on family coverage.
- Coupled effects and the actual observation relation determine the fitting or inference question.
- Remaining parameter, function and consequence ambiguities are distinguished when they change use.
- A changed intervention or receiving question reopens the relevant contribution.
- The result can be used, qualified or passed to a named next method without requiring unrelated identification work.

### MMP.11:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Consequence | Repair |
| --- | --- | --- |
| Fit each contribution independently despite a shared identity | The fitted whole can violate the identity. | Build the shared quantity or joint condition into the family. |
| Treat a penalty as an enforced relation | A small fitting loss can conceal a consequential violation. | Match the construction and obtaining method to the allowed discrepancy. |
| Treat a finite fitted family as all admissible relations | A failure inside it becomes an unsupported impossibility claim. | State its restrictions and widen or bound the family when the question needs it. |
| Identify parameters when only a consequence is needed | Work is spent resolving distinctions that do not change use. | Apply the observation relation to the receiving consequence. |
| Transfer an observational fit to an intervention without modeling the mechanism change | Models agreeing on observed behavior can imply different intervention effects. | Construct the mechanism replacement and the alternatives it can distinguish. |

### MMP.11:9 - Consequences

The family carries usable knowledge through variation and fitting. It can supply a bound before a particular model is selected, or reveal why more observations of the same kind will leave the important ambiguity intact.

The cost is constructing and checking the representation. Strong restrictions reduce the search but can exclude useful candidates. A flexible family can retain more possibilities while increasing inference cost and leaving more uncertainty. Compare these costs against the result the work actually needs.

### MMP.11:10 - Architectural Rationale

Constructing the free part through the retained relations makes the reason for a property inspectable. A shared transfer preserves a total because the same quantity enters with opposite signs. A shape-constrained response preserves monotonicity because its increments are integrals of nonnegative values. Those reasons remain available when coefficients or learned functions change.

Separating function, representation and receiving consequence also permits economical inference. Many representations of the same function need not be distinguished. Functions that agree on the needed consequence may remain as alternatives. A new intervention can make a formerly irrelevant difference decisive.

The insertion point is therefore an architectural choice in the model. It determines what the adjustable contribution can change, which relations constrain it and which results still have the interpretation the work needs. A symbolic expression and a trained network can each participate in this construction when their mathematical role is recoverable.

### MMP.11:11 - SoTA-Echoing

**How much of the relation should be left free?** The historical [SINDy work, Brunton, Proctor and Kutz (2016), Discussion and Appendix B](https://robotics.caltech.edu/wiki/images/a/a3/BPK_PNAS.pdf), binds sparse discovery to the chosen coordinates and function library. The [universal differential equations construction, section 2.3](https://arxiv.org/html/2001.04385v4), combines retained mechanisms with an adjustable function. Sections :4.1-4.3 adopt this choice of where freedom belongs. A small fixed family can be sufficient when its restrictions fit the question. The flexible construction trades additional representation and inference work for retaining variations the small family omits.

**How should a required relation survive fitting?** For the conservation question in :5.2, :4.2 selects a shared transfer with opposite signs over independently fitted change laws for x and y with only a finite conservation penalty. The latter can fit observations while violating the required total elsewhere. The shared construction preserves that total for every admitted choice of its rate functions. Accept the extra derivation and restriction to conserved exchange in return for that identity; obtain the subject grounds for conservation first. When the question allows a specified discrepancy, a penalty or simpler approximate relation can be sufficient at lower construction cost. Carry its discrepancy into the requested consequence rather than requiring the identity anyway. Direct constraints enforcing the relation remain another option under MMP.10.

**Where does the adjustable part enter?** [Dyad's model-discovery documentation](https://help.juliahub.com/dyad/stable/analyses/udes.html) supports component-level insertion before structural simplification. [Micluta-Campeanu and colleagues (2026), sections 2.1-2.2](https://arxiv.org/html/2603.15943v1), demonstrate post-simplification correction followed by optional reduction and symbolic replacement. Section :4.4 retains both placements, chosen by their effect on the needed relations. Their thermal application supplies one use, not the scope of this method.

**What does fitting resolve?** [Loman and Baker (2025), sections 3.1, 3.3, 3.5 and B.5](https://arxiv.org/html/2510.14140), distinguish functions, parameters and predictions. Section 3.1 also constructs an algebraic compensation between an unknown function and a mechanistic parameter that preserves observed dynamics. Adopt that construction of indistinguishable alternatives in :4.5; :5.2 adapts it to coupled directional rates. Their finite fitted-ensemble comparisons in :2.4 and Appendix B can reveal alternatives, but agreement of sampled fits does not prove uniqueness over the admitted family. Constructing two admissible alternatives with different receiving consequences already establishes the consequential ambiguity, without fitting an ensemble.

Revisit the chosen family when new subject knowledge changes its restrictions, a different observation changes what is distinguishable, a new use needs a formerly discarded difference, or another construction supplies the needed result at lower cost.

### MMP.11:12 - Relations

- **MMP.10** constructs representations and the conditions making them admissible. **MMP.9** derives an unknown contribution caused by reduction and can use a constructed family to replace it.
- **A.3.3.TR** composes a rule of change; **C.29.1** relates model consequences to their receiving use; **C.29.2** constructs the needed computation.
- **MMP.7** supplies the recording probability law. **C.16.IR** determines what the resulting indication relation resolves. **MMP.8** uses the available information in a choice question.
- **C.28.MR** constructs the changed mechanism for an intervention. **B.5.RR** revises reasoning after a changed premise or question.
- **C.2.8 and Explanation Design (EXD)** characterize the explanatory contribution needed by a reader. **Method Engineering (ME)** uses a model consequence to develop or revise the corresponding way of working.
- **C.11.DUA** compares a further modeling contribution with its cost; general model comparison and improvement use the existing framework methods.

### MMP.11:End

## MMP.8 - Formulate Information-Dependent Choices Mathematically

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.8:1 - Problem frame

Use this pattern when a mathematical problem mixes quantities you may choose with quantities you do not control, or when a proposed solution depends on information that arrives too late. A solver can find a configuration for each possible circumstance while leaving you unable to select one in advance. A simulation can show a successful continuation because it chose an environmental value that the acting system cannot choose.

Begin with one proposed action. Ask what will be known when it must be chosen, which quantities remain outside that choice, and what result the action must achieve. Construct two possible circumstances that look the same at that moment. If the proposal assigns different actions to them, it needs another observation, a different decision time or a different policy.

The result is a mathematical formulation of the available choices and the requirement they must satisfy, including their dependence on information. It can establish a feasible fixed choice, a policy, a counterexample to the proposal or the missing contribution. This is a general modeling method for design, prediction and control questions. It develops the formulation before a solver or a control algorithm is selected.

The finite examples need elementary sets, inequalities and the meanings of 'there exists' and 'for every'. More demanding cases can require optimization, stochastic processes or control theory. If the answer condition and available information are already correctly formulated, use C.29.2 or the applicable computational method to obtain the result.

### MMP.8:2 - Problem

A mathematical unknown can represent a decision, an unobserved state, an external input or a quantity constrained by other relations. Treating every unknown as a free decision lets the solution change the problem's circumstances to make the requested result possible.

Timing introduces another error. A family of solutions indexed by the true circumstance can be mathematically valid while requiring an observation that the acting system never receives. Separately optimizing every future case then grants foresight that the described method lacks.

The difficulty is to translate the work's choices, information and requirements into a mathematical question with the corresponding dependencies and quantifiers.

### MMP.8:3 - Forces

| Choice | Consequence |
| --- | --- |
| One decision or an adaptive rule | An adaptive rule can use later observations but needs a realizable way to receive and act on them. |
| Possible success or required success | A successful case can support possibility while leaving a guarantee unresolved. |
| Unknown state and random state | An uncertainty set permits several values; probabilities require an additional model. |
| Strong requirement and useful feasibility | A guarantee across an oversized circumstance set can reject useful choices; changing the set changes the claim. |
| Mathematical existence and an obtainable rule | A policy's existence can matter before an affordable construction is known. |

### MMP.8:4 - Solution

Separate choices from circumstances, express the relations that must hold, and state which information each choice may use. Formulate the requested result over those objects, then test the formulation against a small contrasting pair of circumstances. Preserve any useful conditional answer when a stronger requirement is unavailable.

#### MMP.8:4.1 - Name choices, circumstances and consequences

Start from the question in the work. Identify what a participant can change and what is supplied by the subject or environment. Let a denote the choice and w the circumstance. Give both their domains and meanings. A choice can be an arrangement, an input, a rule for later actions or another object the work can construct.

Use the subject relations to connect them to a result. For a deterministic model, a consequence may be written y=f(a,w). An implicit relation R(a,w,y) can retain several possible consequences. Additional unknowns can describe forces, flows, internal states or other quantities jointly constrained by the model. Acausal equations can constrain these quantities without making them free controls.

State what the question requires of the result. If it asks whether every permitted behavior meets a condition, a solver's ability to find one favorable y does not settle it. If the work can select among the permitted consequences, represent the mechanism that gives it that choice. A.3.3.TR supplies the relevant state-change or interaction rule.

#### MMP.8:4.2 - Recover the order and availability of information

Describe what is observed before each decision and what arrives afterward. Express the available observation as h(w) when it is a deterministic description of the circumstance. It may reveal only part of w. For a random or noisy observation, specify its probability law for each admitted w. An unknown fixed w can index a family P_w of observation laws without having a probability distribution itself. A joint law is needed when the question also treats w as random and averages over it. MMP.7 constructs the recording law.

A policy pi selects an action from the information available: `a=pi(h(w))`. Two circumstances with the same h(w) must therefore receive the same action. This uses MATH.2's condition that an answer remains constant on cases identified by a description. Here the observation determines those groups. The information restriction is often called nonanticipativity: the policy does not use distinctions the decision-maker has yet to observe.

For repeated interaction, use the observation history available at each decision. A policy may remember earlier observations or actions. Omitting that memory is a substantive model choice. Global termination is unnecessary when the question concerns a continuing response; specify the response or progress condition that matters under the admitted inputs.

If an earlier action changes what can be observed, make h depend on that action and describe the cost and timing of observation. If action also changes the circumstance distribution or evolution, include that relation. C.28 supplies the causal-use question and the policy's permitted pre-action information; C.28.MR constructs the mechanism replacement. A changed distribution cannot be inferred from a favorable selection of historical cases alone.

#### MMP.8:4.3 - State the required quantifiers and performance criterion

For a deterministic success condition G(a,w), these are different questions:

| Working question | Mathematical statement |
| --- | --- |
| Is there some successful combination? | There exist a and w with G(a,w). |
| Does every circumstance have a successful action, if it were known? | For every w, there exists a with G(a,w). |
| Can one action be selected now that succeeds throughout the admitted circumstances? | There exists a such that, for every w, G(a,w). |
| Can an observation-dependent rule succeed throughout those circumstances? | There exists an allowed policy pi such that, for every w, G(pi(h(w)),w). |

Choose the statement from the work's requirement. The first two can expose possibilities or limits even when the latter two fail. A stronger claim can require a different action or information source.

When the receiving use permits failures with a stated probability, name the event and the randomness over which that probability is calculated. For unknown fixed w and random observation O, the question may require `P_w(failure of pi(O)) <= epsilon` for every admitted w. If w itself is modeled as random and the question concerns performance averaged over circumstances, use the joint law of w and O. An expected cost needs the same choice of what is averaged. Neither a probability nor an objective follows just from listing possible circumstances. Feasibility, expected performance, tail risk and worst-case performance are alternative questions with different consequences. Use the common choice and characterization methods to decide which matters to the work.

Preserve dependence within the circumstance set. Independently combining several ranges can create impossible circumstances and overstate a requirement. Conversely, excluding an inconvenient circumstance changes the range of the conclusion and needs a subject reason or an agreed narrower use.

#### MMP.8:4.4 - Construct or refute a usable choice

For each circumstance w, let A(w) be the actions satisfying the requirement under the modeled relations. For a fixed robust choice, seek an action in the intersection of A(w) over the admitted circumstances. An empty intersection refutes that fixed-choice requirement.

For an observation-dependent choice, group circumstances by the observation they produce. For each obtainable observation o, intersect A(w) over the circumstances with h(w)=o. An action in this intersection works throughout that observationally indistinguishable group. In a finite problem, choosing one such action for each observation constructs a policy. One empty intersection proves that this observation cannot support the required policy.

For a noisy observation and an all-cases guarantee, construct the allowed pairs (w,o) from the observation mechanism's admitted realizations. This relation, rather than a positive probability for each individual report, determines compatibility. For example, if O=w+E with E uniform on [-1,1] and all errors in that closed interval are admitted, the boundary error E=1 remains in an all-cases guarantee despite having probability zero. An almost-sure or specified-probability requirement is a different claim; state that choice.

For a received report o, first check that at least one circumstance is compatible with it. If none is compatible, return the conflict between the report and the observation model under C.16.IR:4.4. A universal statement over an empty set supplies no guarantee for the situation that produced the report. With a nonempty compatible set, intersect A(w) over its members. For a probability-of-success requirement, instead calculate the event under the conditional family or joint law chosen in :4.3; the set of allowed pairs alone supplies no probability weights.

For infinite spaces or long-running interaction, these relations still specify the question, but a usable policy requires the corresponding mathematical and computational construction. A pointwise existence argument does not automatically provide an effective rule. C.29.2 addresses that obtaining work; the present method retains the information restrictions in what it asks the computation to produce.

When several outcomes remain possible for one action and circumstance, apply the required quantifier to those outcomes as well. Derive or inspect a violating outcome when refuting a guarantee. If the missing factor is an unmodeled selection mechanism, obtain it or retain the conditional answer rather than allowing the solver to invent a favorable mechanism.

#### MMP.8:4.5 - Interpret the result and change the working method

Follow the resulting action or policy through one modeled case and a consequential change. Return the consequence to the original requirement. If a planned response depends on a distinction absent from the available observation, revise the observation, defer the decision, choose a more tolerant action or change the stated goal with the responsible party.

Compare these options by what they change and cost. A more informative observation can enlarge the feasible policy set, but it may arrive too late or cost more than a sufficient fixed choice. C.11.DUA supplies that comparison. An infeasible guarantee can still leave a useful bounded, conditional or risk-qualified proposal.

For a working-method change, explain who or what supplies the observation, what result it provides, when it becomes available and what the receiving action does with it. ME supplies the composition and change of those methods. The mathematical policy then describes an obtainable contribution, rather than relying on an unstated observer or decision-maker.

### MMP.8:5 - Archetypal Grounding

#### MMP.8:5.1 - Choose a preload before or after learning an external load

An ideal static arrangement has a downward load w, an adjustable upward preload a and a residual y=w-a. A later use requires `abs(y)<=1/4`. The load is either 1 or 2, and a can be any value from 0 to 2. The relation is a supplied illustrative mechanical model; the pattern's work is to formulate the choice and its information.

If w=1, acceptable choices form `[3/4,5/4]`; if w=2, they form `[7/4,2]` after the actuator limit is applied. Both sets are nonempty, so each known load has a feasible choice. Their intersection is empty. No one preload chosen before distinguishing the loads can meet the requirement for both.

Suppose a reading available before adjustment reports which of the two loads is present. The policy `a=w` then meets the requirement. A reading received only after the preload is locked cannot support that policy at the relevant decision.

Now the tolerance is relaxed to 3/5. The acceptable intervals overlap from 7/5 to 8/5, so `a=3/2` works before any reading. Additional measurement is unnecessary for this revised requirement. The change is in the required result, not the sophistication of the computation.

#### MMP.8:5.2 - Decide which participant gets a scarce resource

Two work requests, L and R, may need the only available resource. Exactly one needs it. Allocation succeeds when the resource goes to that request. The instruction must choose L or R deterministically from one report received before allocation.

With no distinguishing report, there are two constant instructions: always allocate to L or always allocate to R. Each fails in one circumstance. A truthful timely report permits an instruction that follows it and succeeds in both. A report arriving after allocation cannot supply that choice.

Now the timely report is noisy. The observing procedure independently chooses one of two channels with equal probability, then sends its L/R report without naming the channel. The model supplies these conditional reporting probabilities; the remaining probability in each row produces the opposite report:

| Channel | Actual request needing the resource | Probability of a correct report |
| --- | --- | ---: |
| 1 | L | 0.9 |
| 1 | R | 0.5 |
| 2 | L | 0.7 |
| 2 | R | 0.9 |

Use MMP.7 to remove the unrecorded channel by summing over it. For fixed circumstance L, `P(report L)=0.5*0.9+0.5*0.7=0.8`. For fixed R, `P(report R)=0.5*0.5+0.5*0.9=0.7`. No probability for which request actually needs the resource was needed for this construction.

There are four deterministic instructions from one two-valued report:

| Instruction | Success probability in fixed L | Success probability in fixed R |
| --- | ---: | ---: |
| Always allocate to L | 1 | 0 |
| Always allocate to R | 0 | 1 |
| Follow the report | 0.8 | 0.7 |
| Choose opposite to the report | 0.2 | 0.3 |

If the requirement is success probability at least 0.65 in each admitted circumstance, following the report satisfies it. None of these instructions gives a zero-failure guarantee. The conditional laws are sufficient to make both statements while the circumstance remains unknown and fixed.

Change the question to average success in a stream of requests modeled as L with probability 0.95 and R with probability 0.05, retaining the channel procedure. Following the report gives `0.95*0.8+0.05*0.7=0.795`. Always allocating to L gives 0.95; always allocating to R gives 0.05, and choosing opposite to the report gives 0.205. The instruction with greatest average success among the four is now always L. It still fails in fixed R.

Choose the performance requirement from the work's purpose before adopting an instruction. The observing model supplies conditional probabilities; the decision about the work determines whether performance in each circumstance or an average matters.

To retain the zero-failure requirement, the work could obtain a truthful report in time or provide enough resource to serve both requests. Compare the cost of those changes with the consequences of accepting a mistaken allocation, using C.11.DUA. A changed channel, recorded channel identity or permission to randomize the instruction changes the information or choice set; formulate the revised question accordingly.

#### MMP.8:5.3 - Find a strategy, rather than an answer chosen with future knowledge

A program repeatedly receives a bit b and emits a bit a. A requirement asks it to emit the same bit. If receipt precedes emission, the rule `a=b` works on every round. If emission must precede receipt, each possible future bit has a matching answer, but no deterministic rule using only the earlier history can guarantee a match against every admitted next bit.

To see the failure, hold the earlier history fixed. The rule chooses either 0 or 1. Both next input bits are still admitted, including the opposite one. That continuation refutes the guarantee for this history. Inspecting more successful traces cannot remove it.

A changed requirement may ask for success probability under independent fair input bits. Any earlier choice then matches with probability 1/2 in one round, including a randomized earlier choice independent of the next bit. Success in every one of N such rounds has probability 2^(-N). These probabilistic claims use the new input assumption. They do not establish success against every input stream.

This is a continuing computational interaction. The construction determines how each response may depend on incoming information. The same observation-order construction identifies what a distributed team or controller would need to know before acting.

### MMP.8:6 - Bias-Annotation

Optimization tools encourage viewing every variable they can assign as an available choice. Recover the subject meaning of each unknown before interpreting a solution. A second bias is to make robustness the default goal. State the receiving requirement first; a conditional answer or an explicitly accepted risk may be more useful than an infeasible all-circumstances guarantee.

### MMP.8:7 - Conformance Checklist

- Are choices, circumstances and consequences distinguished by what the acting system can actually change?
- Does each choice depend only on information available at its decision time?
- Do the quantifiers express the intended possibility, guarantee, policy or probabilistic question?
- Are dependent circumstances and remaining possible outcomes preserved in the formulation?
- Does a witness, empty intersection, policy or bound have the claimed meaning?
- Does the interpreted result support an action, a changed method or a specific unresolved contribution?

### MMP.8:8 - Common Anti-Patterns and How to Avoid Them

| Failure in this work | Repair |
| --- | --- |
| A solver changes an external load or unknown state to satisfy the goal. | Treat it as a circumstance and apply the required quantifier. |
| A separately optimal action for every future is presented as one available strategy. | Group cases by the information available at the decision; require a common action within each group. |
| An existentially chosen consequence stands in for all allowed behavior. | Retain the behavior relation and test the quantifier required by the goal. |
| A larger uncertainty set is called safer without examining its subject meaning or cost. | Check the joint possible circumstances and choose the requirement for the actual use. |
| Better observation is required after a sufficient common action is already available. | Compare what the additional information can change before commissioning it. |

### MMP.8:9 - Consequences

The formulation prevents computation from supplying unavailable control or foresight. It can expose a useful change to observation, timing or the requirement before optimization begins. It can also be harder to solve than its scenario-wise surrogate; that extra difficulty reflects the question the work actually asked.

### MMP.8:10 - Architectural Rationale

Quantifier order and permitted dependence express different aspects of the working problem. 'For each circumstance there is an action' concerns a family of possible solutions. An executable policy also needs a way to select its action from obtainable information. Grouping indistinguishable circumstances makes that additional condition visible and gives a constructive test for finite cases.

This mathematical formulation can describe physical adjustment, resource allocation or computational interaction. Its source premises and available actions differ across those practices. The method keeps those differences explicit while reusing the same reasoning about choices and information. It complements FPF's continuation and computation methods by constructing the mathematical answer condition they consume.

### MMP.8:11 - SoTA-Echoing

[Boyd and Vandenberghe, Convex Optimization, section 4.1](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), distinguish the feasible set from the objective and transformations of a problem. Adopt that separation in :4.1 and :4.3. The present finite constructions do not require convexity; the book's convex solution guarantees apply only under their conditions.

[Ben-Tal, Goryashko, Guslitzer and Nemirovski, Adjustable robust solutions of uncertain linear programs (2004)](https://doi.org/10.1007/s10107-003-0454-y), develop adjustable decisions alongside choices fixed before uncertainty is revealed. Adapt this distinction into the information-dependent formulation; do not transfer linear-program tractability to unrestricted policies.

[Duchi, Optimization with uncertain data (2018), sections 1 and 6](https://web.stanford.edu/class/ee364b/lectures/robust_notes.pdf), compares uncertainty-set requirements with probabilistic ones and makes choosing the uncertainty set a modeling question. Adopt that choice explicitly; no worst-case objective is imposed by this pattern.

[Vayanos, Georghiou and Yu, Robust Optimization with Decision-Dependent Information Discovery, version 3 (2022)](https://arxiv.org/abs/2004.08490v3), treats actions that affect when uncertainty can be observed. Carry that extension into :4.2 and the return to method design. Its specialized algorithms are further methods, not assumed capabilities of every reader.

The interval, allocation and bit-response examples are constructed demonstrations of the method under their stated assumptions.

### MMP.8:12 - Relations

B.5.FM and C.29 connect the work's question to its mathematical formulation. A.22.CGUS exposes allowed continuations; A.3.3.TR constructs the behavior relation. MMP.7 supplies a missing observation law for probabilistic uses. MATH.2 explains the identification of cases that preserve a requested answer; here grouping by available information determines which actions a policy can distinguish. C.29.2 obtains a computation for the formulated question and C.29.3 examines realization. C.28 governs causal claims when acting changes the represented world. ME uses the result to compose observation, decision and action methods with their needed contributions and timing.

MMP.8.SD refines this formulation for continuing decisions. It constructs a decision-sufficient state or belief, transitions and observations, and the relation between a present choice and its later consequences. Use that refinement when the one-step formulation leaves a consequential continuation unresolved.

### MMP.8:End

## MMP.8.SD - Construct a Sequential Decision Model from Information and Consequences

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use.

### MMP.8.SD:1 - Problem frame

**Use this when a choice changes what can be done or learned later, and comparing its immediate result does not settle the useful course of action.** You might reserve a resource for a later request, inspect an unfamiliar document before choosing how to process it, or pursue a target whose attainment depends on several moves.

Start with two possible first actions. For each, write what becomes available before the next choice and what the next choice can change. This small decision tree often reveals the missing resource, remembered event or uncertainty that a proposed “current state” has discarded.

The object being constructed is a **sequential decision model**: a mathematical account connecting available information, allowed actions, subsequent observations and accumulated consequences. Its result lets a reader compare a present action together with an admissible continuation. A continuation is the later policy: a rule for choosing actions from the information available then.

This is the sequential refinement of **MMP.8 - Formulate Information-Dependent Choices Mathematically**. It retains that pattern's separation of chosen quantities, uncontrolled circumstances and information available at each choice. It adds the construction of a state sufficient for the selected decision problem and the relation between current action and remaining consequence. A short history tree is a valid starting model; a compact state becomes useful when the tree repeats questions or grows too large.

A reader can work the finite cases with conditional probability, finite sums and maxima, or with sets of possible outcomes. For continuous, constrained or indefinitely continuing models, the person supplying the mathematical argument needs the relevant preparation in stochastic control, decision theory or the applicable field. This can be the reader or an available specialist. Give a specialist the actual timing, allowable actions and consequence criterion; ask for the resulting model and its limitations.

**Not this pattern when** the useful comparison is already a single choice with no consequential continuation. Use MMP.8 directly. If the decision model is adequate and only its solution is expensive, the next work is computational. If the difficulty is deciding whose interests or which consequences should count, obtain that choice from the responsible people and the applicable decision or strategy practice.

### MMP.8.SD:2 - Problem

A record of the present can omit information that changes a later action's availability or value. A forecast can predict the next reading correctly while omitting an accumulated loss that matters at the end. A plan can also give its future decision maker information that will arrive too late.

These defects can survive accurate computation. Optimizing a model of the latest observation, a guessed hidden state or immediate payoff may return the best answer to a different problem. Conversely, retaining every observation and solving for every possible future can cost more than the decision warrants.

The modeling question is: **what information and consequence account make the present choice and its continuation comparable, under the actual conditions of use?**

### MMP.8.SD:3 - Forces

| Force | Tension |
| --- | --- |
| Useful memory | A compact state saves work, but merging histories can remove an allowed action or change its consequences. |
| Information timing | Later observations support conditional action, while a plan chosen now cannot depend on their unrealized values. |
| Present and later consequences | A locally attractive move may consume a resource, remove an option or change what can be learned. |
| Criterion choice | Expected total gain, probability of meeting a target and worst possible loss can prefer different policies. |
| Affordable adequacy | Exact reconstruction of the hidden state may be unnecessary; an adequate comparison or bound can already settle the use. |
| Model and computation | A correct solver can answer a deficient model, and an adequate model can remain computationally difficult. |

### MMP.8.SD:4 - Solution

Construct the information available at each choice, retain what determines the relevant continuation, and derive the accumulated consequence of a policy. Use that derivation to locate the premise responsible when a changed condition alters the answer.

#### MMP.8.SD:4.1 - Fix the decision times and the consequence being compared

Recover from MMP.8 the choices, uncontrolled circumstances and information available before each choice. Mark the order of observation, action, transition and consequence. Include delays, commitments and stopping opportunities when they change what can be done.

For decisions at times `t=1,…,T`, let `H_t` be the available history immediately before action `A_t`. It contains received observations and known previous actions. Include a realized gain or cost in this history only if the decision maker can know it then. A policy `π_t(H_t)` selects an allowed action from that history; randomization is an additional allowed operation when the problem permits it.

State the consequence criterion supplied by the receiving use. One common finite model maximizes

    J(π) = E^π[R_1 + R_2 + … + R_T + G].

Here `R_t` is the gain at decision step t, `G` is a terminal contribution, and the expectation uses the trajectory law induced by policy π and the model. Gains can be negative costs. Their addition presupposes a common meaning and scale. Specify the initial information or distribution under which policies are compared.

An expected sum is one choice of criterion. For a target such as “finish with at least k points,” the consequence can instead be the terminal indicator, equal to 1 when the target is met and 0 otherwise. Its expectation is the attainment probability. For several criteria, retain their comparison or trade-offs until an applicable choice method supplies a selection rule. A scalar “reward” does not decide that rule.

Use a horizon or stopping condition appropriate to the work. Assign the consequences left at the horizon, such as unused stock or unfinished obligations. A discounted sum gives later gains smaller weights; choose that meaning deliberately. Shortening a computational planning window does not make omitted consequences disappear.

#### MMP.8.SD:4.2 - Construct how an action changes the world and the available information

Write the transition and observation account for each allowed action. For a finite stochastic model, choose an underlying state X that retains the information needed for the transition account. One possible representation is the joint law

    K_t(x', y, r | x, a)
      = modeled probability of next state x',
        next observation y and current gain r
        when action a is applied in state x.

This representation assumes that, given x and the applied action a, the omitted history does not further change the law. Retain a missing historical distinction when that assumption fails. Using a joint law permits dependence between the transition, observation and gain. Factor it into simpler laws only when the model supports the corresponding conditional independence. A deterministic rule or a relation of possible successors can replace probabilities when that is what the available knowledge warrants.

Identify the source of these relations. A subject model supplies the consequences of applying the action; MMP.7 supplies how observations are recorded and become available. An intervention model through C.28.MR can supply the changed mechanism. A conditional association among logged actions and outcomes is not automatically the law under a new policy.

An action can change both the subject and what the next decision maker will know. An inspection might consume time, disturb an object and produce a reading. Include each effect that changes the policy comparison. If two participants receive different observations, preserve their separate information; a policy using all their private information would require a means of sharing it before the choice.

For a small problem, enumerate the allowed actions and possible next observations at each history. Label branches with probabilities or allowed circumstances and gains. This tree supplies a reference calculation before any compression.

#### MMP.8.SD:4.3 - Retain a state sufficient for the selected continuation

Propose `Z_t=s_t(H_t)`, a summary obtainable from the information available at time t. It may be an observed state, a history window, a set of possibilities or a belief: a probability distribution over the hidden state conditional on the available history.

When the retained state is a belief, A.3.3.PI:4.4 supplies its prediction and observation update under a specified model. Use that distribution and update here. Include uncertain fixed parameters or other remembered quantities when they affect future consequences. A point estimate can discard differences that change an action's value. A posterior over physical coordinates alone can also be insufficient when a resource budget or terminal target depends on the past.

For the expected additive criterion in :4.1, a constructive sufficient test compares any two admitted histories at the same decision time having the same proposed Z. For every action covered by the model, determine whether those histories give:

- the same allowed actions;
- the same conditional expected current gain;
- the same conditional law of the next retained state after the action.

At the terminal time, the conditional expected terminal contribution must also depend only on the retained state. Supply an initialization and an update from retained information, the action taken and the next received observation. These conditions let the continuation calculation use Z in place of the full history. They are sufficient conditions for this reduction, not a claim that every useful decision requires this much information.

The comparison covers the actions and histories for which the policy is to be used, including alternatives to the former policy. A match only along recorded behavior can hide distinctions that another action makes consequential. Predicting irrelevant observations is unnecessary when their differences affect neither the criterion nor future choices.

When the test fails, identify the missing distinction and repair the state. An unspent resource, elapsed time, accumulated amount or belief over an unknown mode can be the needed addition. If the repair is expensive, retain the history tree, restrict the claimed use, or use a bound sufficient for the present comparison. Two histories with different forecasts can still support the same action when that action dominates under both.

For an approximate summary, determine how its errors can change the action comparison. Carry errors in current gains and in expected continuation through the selected horizon, using an applicable bound or model criticism. If computed action values each have justified absolute error at most e relative to the intended model and criterion, a largest value more than `2e` above every rival has the same maximizing action. Without such separation, preserve the unresolved comparison or improve only the approximation that can change it. A small prediction error on a training sample alone does not supply this guarantee.

#### MMP.8.SD:4.4 - Derive current gain plus continuation

First evaluate a policy that selects its actions from the retained state. With a sufficient state, let `V_t^π(z)` mean expected gain from time t onward when the policy is followed, conditional on current retained state z. For a deterministic policy, the finite model gives

    V_(T+1)^π(z) = g(z)
    V_t^π(z) = r_t(z, π_t(z))
               + sum_z' P_t(z' | z, π_t(z)) V_(t+1)^π(z').

Here `g(z)` is the conditional expected terminal contribution, `r_t(z,a)` the expected current gain, and `P_t` the next retained state's law derived from :4.2–:4.3. A randomized rule averages the right-hand side over its action probabilities.

The equation follows by splitting the accumulated gain into the current term and the remaining terms, then conditioning on the next information state. Thus each action is compared with what can follow it, including the information then available.

For a finite state and action problem with nonempty allowed action sets, whose only policy restrictions are those local sets, the best attainable value satisfies

    V_(T+1)(z) = g(z)
    Q_t(z,a) = r_t(z,a) + sum_z' P_t(z' | z,a) V_(t+1)(z')
    V_t(z) = max over a in A_t(z) of Q_t(z,a).

An attaining action at each reached state defines an optimal policy for this model and criterion. Finite sets make these maxima attainable. For more general spaces, determine the relevant existence, measurability and integrability conditions. When a maximum is not attained, distinguish the supremum from any obtained approximate policy.

The order of choice and averaging matters. When a later observation is available before the next action, its branch can use its own continuation. A fixed action sequence cannot use that observation. At a common decision node, selecting a different action for each still hidden state would add unavailable information.

Retain restrictions coupling choices across histories or times. A total resource limit can often be represented by remaining resource in Z; a constraint on the whole policy may instead require a constrained formulation. Independently maximizing every node can violate a coupling that the state has omitted.

These equations define the mathematical continuation problem. CMP.3 supplies sharing and scheduling of repeated subcomputations; CMP.9 supplies a sampling procedure and the error of estimated expectations; CMP.5 can supply a relaxation, a usable policy and an improvement bound when its recovery conditions hold. C.29.2 supplies the wider computational formulation, including a continuing response rather than a terminating answer.

For indefinitely continuing use, first select a finite total, discounted sum, average rate or other well-defined criterion. For example, bounded per-step gains and a discount factor γ with `0≤γ<1` make the infinite discounted sum finite. A fixed-point or limiting equation then needs conditions appropriate to that criterion. A solver's convergence and a policy's consequences remain separate questions.

#### MMP.8.SD:4.5 - Match the continuation to the uncertainty and objective

When the available information is a set of possible circumstances, evaluate a policy over the permitted complete trajectories. Compare its worst consequence, an interval or another requested result without inventing a probability distribution.

A stage-by-stage worst-case calculation is justified only if the retained description preserves which continuations remain possible. In particular, one unknown parameter fixed throughout a run cannot silently take a different worst value at each stage. Carry that parameter's compatible set and any information learned about it, or keep the coupled trajectories. :5.4 shows a choice reversed by losing this dependence.

Likewise, a terminal threshold depends on the accumulated amount. Retain that amount if it is observed; otherwise retain the uncertainty about it together with the other relevant state. In :5.3, current expected gain is enough to compare one objective but insufficient for another.

For a compressed or learned state, separate three possible claims: performance of a specified restricted policy; an optimum within that policy class; and an optimum among all policies allowed by the available history. Neither a convenient memory representation nor a converged learning algorithm makes those claims interchangeable. Evaluate the returned policy under the original information and consequence account, with the uncertainty or approximation relevant to its intended use.

#### MMP.8.SD:4.6 - Return the model and propagate a consequential change

Return the state or belief and its update, admissible policy information, action-dependent relations, consequence criterion and continuation relation. Include a computed policy comparison or bound when it is already useful, and state the assumptions that make it applicable. A formula alone can be the right input to a computational specialist; a two-branch calculation can already settle an ordinary choice.

Work through an available case from initial information to the result that the receiving activity uses. If a state reduction was needed, include the histories it would otherwise merge. Compare with a serious simpler option: a fixed plan, immediate-gain choice, full history tree or an existing policy with an adequate bound. Added state and computation earn their cost by changing the answer, making it obtainable or preserving a needed qualification.

When an actual premise changes, follow the affected dependency. A delayed observation changes allowable conditioning; changed resource availability changes actions and transitions; a new target changes the consequence account and may change the state. Recalculate the affected continuations. Use MMP.14 when observations reveal systematic mismatch in the proposed model, and the subject method when its action consequences need repair.

Use C.11.DUA to decide whether additional observation, modeling or computation can improve the receiving use enough to warrant its cost. An existing bound can settle the question. A hypothetical sensitivity exercise is useful when it can expose a consequential assumption; it is not an additional task when it cannot change use.

A human or AI participant can construct or calculate this model. Applying a policy in the subject still requires the observations, permitted actions and performing method that the model assumes. Methodological work uses the model to decide, for example, whether to observe before acting, retain a resource or change a method after an informative result; it also supplies the practical conditions under which that sequence can be performed.

### MMP.8.SD:5 - Archetypal Grounding

The following are constructed finite models. Their numbers show what follows from the stated assumptions; they are not measured effects or recommendations for a particular organization.

#### MMP.8.SD:5.1 - Reserve a resource for an observed later request

A portable power unit has enough energy to serve one task in either of two slots, with no recharge. Serving the current task in slot 1 yields 4 units on an already selected gain scale. In slot 2 a different task arrives with probability 0.6 and yields 10 if served. Arrival is observed before the slot-2 decision. Unused energy has terminal value zero; the current task cannot be deferred. Serving consumes the whole unit.

Let b be remaining energy, either 0 or 1, and d indicate the later arrival. At slot 2,

    V_2(b,d) = 10*b*d.

Use the retained state `(time, remaining energy, current request)`. The slot-1 comparison is

    serve now: 4 + 0 = 4
    reserve:   0 + 0.6*10 + 0.4*0 = 6.

The resulting policy reserves energy, then serves if the request arrives. It has larger expected gain than immediate service, although it yields zero when no request arrives. If the requirement is a gain of at least 4 in every admitted case, serving now meets it and reservation does not.

Two histories can show the same later request but differ in whether the energy was already used. Merging them would make the slot-2 service appear available after both histories. Retaining b prevents that error.

Suppose the arrival probability changes to 0.3, with the other premises unchanged. Reservation now gives 3 and immediate service gives 4, so the first action changes. If instead the only available probability statement is `0.55≤p≤0.65`, reservation gives expected gain between 5.5 and 6.5 and exceeds 4 throughout. Refining p is unnecessary for that comparison.

#### MMP.8.SD:5.2 - Pay for information only when a later choice can use it

An unfamiliar encoded document uses format A or B, initially with equal probabilities. Two supplied decoders are available: the matching decoder gives a usable output worth 10, and the other gives 0. The model permits one final decoder application. An optional diagnostic costs 1 on the same gain scale and leaves the format unchanged.

The diagnostic returns + with probability 0.8 in format A and 0.2 in format B; the complementary probabilities give −. Its result arrives before decoder selection. The supplied observation model and A.3.3.PI's conditioning give:

| Information before decoder choice | Probability of format A | Best decoder | Expected final gain |
| --- | --- | --- | --- |
| No diagnostic | 0.5 | A or B | 5 |
| Diagnostic + | 0.8 | A | 8 |
| Diagnostic − | 0.2 | B | 8 |

The decision state can be `(stage, p)`, where p is the current probability of A. At the final stage,

    V_2(p) = max(10*p, 10*(1-p)).

Each diagnostic result has probability 0.5 under the initial model. Thus

    skip diagnostic:  V_2(0.5) = 5
    use diagnostic:  -1 + 0.5*V_2(0.8) + 0.5*V_2(0.2) = 7.

The continuation's choice changes with the observation. Fixing one decoder in advance gives 5 before the diagnostic cost, or 4 after it. This is why the extra information has value here.

Now the diagnostic result is delayed until after the final decoder choice. The decoder choice can no longer depend on that result. Using the diagnostic then has net expected gain 4, so skipping it gives the better value 5. This repair changes the information timing rather than the arithmetic of conditioning.

A different changed condition also reverses the comparison: with a timely but weaker symmetric diagnostic that is correct with probability 0.55, using its result gives `-1+10*0.55=4.5`. Skipping still gives 5 and is preferable.

The decoder and diagnostic behavior are premises of this example. A real use requires the applicable processing and observation methods to supply those consequences.

#### MMP.8.SD:5.3 - Retain accumulated progress when the terminal goal changes

In a two-round game, all awarded points are observed immediately. The first move is either A, giving 2 points with probability 0.5 and 0 otherwise, or B, giving 1 point certainly. In the last round, the player chooses Safe, adding 1 point certainly, or Gamble, adding 3 with probability 0.4 and 0 otherwise. The gamble's outcome is independent of the first round.

The objective is initially to maximize the probability of finishing with at least 3 points. Let c be points already earned. The terminal contribution is `g(c)=1` when `c≥3` and 0 otherwise. With zero intermediate contribution, the continuation compares terminal attainment:

| Points before last round | Safe: attainment probability | Gamble: attainment probability | Best continuation |
| --- | --- | --- | --- |
| 0 | 0 | 0.4 | Gamble |
| 1 | 0 | 0.4 | Gamble |
| 2 | 1 | 0.4 | Safe |

Therefore first move A gives `0.5*1+0.5*0.4=0.7`, while B gives 0.4. Choose A and condition the last move on earned points. Retain the state `(round, c)`. The round number alone is insufficient: histories with c=0 and c=2 require different continuations.

If the objective were expected final points, Gamble's expected increment 1.2 exceeds Safe's 1 at every c. Both first moves have expected increment 1, so both then give 2.2 expected final points. That calculation answers a different question from attainment probability.

Now change the requested terminal target from 3 to 4 points. From c=2, Gamble attains it with probability 0.4 and Safe fails. From c=0, neither last move can attain it. Thus A gives `0.5*0.4+0.5*0=0.2`. B followed by Gamble gives 0.4 and becomes preferable. The transition probabilities remain unchanged; the changed terminal criterion alters both the continuation and the first choice.

#### MMP.8.SD:5.4 - Preserve one unknown condition across stages

A two-stage processing route incurs costs w and `1-w`, where an unknown w is fixed for the whole run and belongs to `{0,1}`. Choosing that route commits to both stages. A supplied alternative has total cost 1.5. The question is to minimize worst total cost, with no probability model.

The two possible cost sequences for the route are `(0,1)` and `(1,0)`; both total 1. The route therefore beats the alternative. Adding the worst first-stage cost 1 to the worst second-stage cost 1 gives 2, but combines different possible runs.

For the first choice, the common total 1 already suffices. If the remaining cost is later needed and the first-stage cost is observed, that observation identifies w and determines the remaining cost.

Now the operating condition is allowed to change between stages: costs are `w_1` and `1-w_2`, with all four pairs `(w_1,w_2)` allowed. The pair `(1,0)` gives total cost 2. The route's worst total is now 2, so the fixed-cost alternative 1.5 is preferable. The old conclusion fails because the admitted dependence changed.

### MMP.8.SD:6 - Bias-Annotation

Finite stochastic examples make expectations and recursion easy to inspect, but may encourage a probability model or scalar gain where neither is supplied. Keep non-probabilistic possibilities and multiple criteria when that is what the work supports.

A model with one decision maker can also conceal separate information held by different people or systems. Represent communication and its timing when the proposed continuation depends on shared knowledge. Learned memory is attractive in large problems; its convenience does not establish sufficiency for a changed action set or criterion.

### MMP.8.SD:7 - Conformance Checklist

- The model states the decision order, information available before each action and allowed policy class.
- Transition and observation relations distinguish applied actions from uncontrolled circumstances and retain consequential dependence.
- The proposed state has an obtainable initialization and update. Its sufficiency or approximation is tied to the selected actions, criterion and horizon.
- The accumulated consequence includes the relevant terminal contribution, resource constraint or remembered progress.
- The continuation relation preserves the order of observation, choice and aggregation over uncertainty.
- A worked comparison returns a useful policy consequence, bound or unresolved distinction; any real changed premise is propagated to its affected use.
- Additional data or computation is selected for its possible effect on the decision. An already sufficient result remains usable.
- The mathematical model, computed policy and subject performance have distinct claims and required contributions.

### MMP.8.SD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Latest reading called the state | Histories with different resources or beliefs become indistinguishable. | Compare the histories' allowed actions and continuation, then retain the missing distinction. |
| Future knowledge used now | A policy selects a branch before its observation arrives. | Place observations and commitments on the same decision timeline. |
| Immediate score treated as total value | Resource use or information acquisition changes the future comparison. | Include the continuation under each current action. |
| Every objective written as a sum of immediate rewards | A terminal target or policy constraint changes meaning. | Preserve the criterion and augment the state or formulation where it needs history. |
| Independent worst values substituted for one fixed unknown | The calculation creates a trajectory excluded by the model. | Preserve coupling across stages or explicitly adopt the enlarged uncertainty set. |
| Convergence treated as decision sufficiency | A solver can converge for a representation that loses relevant history. | Identify the solved problem and evaluate the returned policy under the intended model. |

### MMP.8.SD:9 - Consequences

The reader obtains a model that explains why a present action is useful together with what can follow it. It can reveal that a resource should be retained, that a reading is worth obtaining only before a commitment, or that a changed target requires remembering different information.

The construction also locates missing contributions: an observation law, an action consequence, a criterion, a retained distinction or a computational procedure. A small bound may close the comparison before any large policy computation.

A sufficient state can greatly reduce repeated reasoning, but constructing it and solving the resulting problem can still be costly. More detailed modeling can worsen the work when it cannot change the receiving decision.

### MMP.8.SD:10 - Architectural Rationale

The construction begins with available histories because they expose the actual information constraint. A state is then a justified reduction of the decision problem. Starting from a convenient list of current features reverses that order and can hide lost memory.

Prediction contributes the distribution or set needed to describe a continuation. Decision modeling additionally specifies allowable actions and how consequences are accumulated and compared. In :5.3, identical transition knowledge supports different policies after a change of goal. In :5.2, identical diagnostic accuracy has different value after a change of timing.

A full history tree is a serious alternative to state compression. For a small problem it is often the clearest and cheapest model. A fixed plan is adequate when future information cannot improve the selected comparison; the delayed diagnostic shows such a boundary. For larger problems, a justified compact state makes repeated questions reusable by computational methods.

The continuation relation describes the mathematical problem consumed by those methods. It does not prescribe a solver or the worth criterion. This keeps model construction usable in physical operations, investigation, computational work and method design without replacing their subject methods.

### MMP.8.SD:11 - SoTA-Echoing

The practice question is how to retain enough information for a useful sequential choice without demanding an unnecessarily complete reconstruction.

| Question and comparison | Adopted or adapted contribution and limit |
| --- | --- |
| Can a compact summary replace the full history tree? | **Adopt** the information-state line of Subramanian, Sinha, Seraj and Mahajan, [*Approximate Information State for Approximate Planning and Reinforcement Learning in Partially Observed Systems*](https://jmlr.org/papers/volume23/20-1165/20-1165.pdf), JMLR 23 (2022), §§2.2–2.3 and 3.2, especially Theorems 5 and 9. Preservation of expected gain and the next summary's law supports the reduction in :4.3–:4.4; approximate preservation needs a consequence bound. A full history tree remains preferable when small. This line saves representation and computation only when its conditions are obtainable; prediction fit alone supplies less. Reopen when a newly relevant action, history or criterion changes the equivalence between merged histories. |
| What if compact memory is useful but not sufficient? | **Adapt** Sinha and Mahajan, [*Agent-state based policies in POMDPs: Beyond belief-state MDPs*](https://arxiv.org/html/2409.15703v1), arXiv v1, 24 September 2024, §§II-C–II-D and III. Its comparison of policy classes supports :4.5: evaluate a restricted controller as such, rather than assuming an arbitrary recurrent memory admits the continuation equation in :4.4. Direct policy search is a serious alternative when sufficient-state construction is too costly. Preserve whether its result is locally optimal or best within a restricted policy class. Reopen when memory, available computation or required policy class changes. |
| Does convergence of a modern learning algorithm close the state question? | **Reject that inference**, using Sinha, Geist and Mahajan, [*Convergence of regularized agent-state-based Q-learning in POMDPs*](https://arxiv.org/html/2508.21314v2), arXiv v2, 2 September 2025, §§II-B–IV and Theorem 1. Under its learning-rate and visitation assumptions, the limit is for a regularized model that depends on the behavior policy's limiting distribution. The result sharpens :4.5's separation of numerical convergence from the intended policy comparison. Regularized learning remains a computational option; it brings its objective and representation conditions. Reopen when a proposed solver claims a stronger use than its result supports. |
| What if probabilities are unavailable and the criterion is worst consequence? | **Adapt** Dave, Venkatesh and Malikopoulos, [*Approximate Information States for Worst-Case Control and Learning in Uncertain Systems*](https://arxiv.org/html/2301.05089v2), arXiv v2, 6 April 2024, §§II–III. Conditional ranges and a criterion-specific continuation are a serious alternative to expected gain. The paper derives continuations for maximum instantaneous and terminal cost. For accumulated costs, :4.5 and :5.4 preserve the allowed complete trajectories. The trade-off is a worst-case comparison in place of a probabilistic average; reopen when the uncertainty set or its cross-stage dependence changes. |

### MMP.8.SD:12 - Relations

- **MMP.8 - Formulate Information-Dependent Choices Mathematically** supplies choices, uncertainty, information timing and admissible policies. This nested refinement constructs their sequential state and continuation.
- **A.3.3.PI - Retain the Information Needed for Prediction**, especially :4.4, supplies prediction and hidden-state belief updates. This method consumes them in action and accumulated-consequence comparisons.
- **MMP.7** supplies the recording law and available observations. **MMP.13** can supply inferred model quantities with their uncertainty; neither contribution alone establishes the effect of a new action policy.
- **C.28.MR** supplies intervention through a changed mechanism. A subject method supplies or justifies the resulting action and observation relations used here.
- **MMP.14** supplies criticism and repair when comparable predictions fail. A detected failure here identifies which state, information or consequence premise must return to modeling.
- **C.29.2 - Computational Formulation** specifies the computational answer or continuing response and the procedure needed to obtain it.
- **CMP.3 - Share and Schedule Repeated Subcomputations** organizes repeated evaluations of the continuation. **CMP.9 - Construct a Randomized Estimator or Sampling Procedure** estimates expectations with a computational error account. **CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem** supplies relaxation, candidate recovery and improvement bounds for the chosen formulation.
- **C.11.DUA** helps decide whether further information or computation is worth obtaining. FPF choice and portfolio methods and the applicable DOCA, Strategy or Method Engineering practice supply criteria, compare the returned alternatives and organize their practical use.

### MMP.8.SD:End

# B. Infer, distinguish and revise

## MMP.7 - Construct a Probability Model of the Recorded Data

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.7:1 - Problem frame

Use this pattern when inference depends on how events, responses or quantities become records, and that procedure has not yet been expressed in the probability model. A feedback log may contain successes more often than failures. A timed trial can end before its event occurs. Several readings can share one calibration error. In each case, fitting a familiar distribution to the visible numbers can answer a different question from the one you intended.

Start with one possible event and follow what the observing procedure would record. Include the possibility that it leaves no record, reports an interval or shares an influence with another observation. Repeat for a contrasting event. These cases reveal what the mathematical outcome must contain before you choose its distribution.

The result is a probability law for the recorded outcome under stated assumptions, together with its relation to the quantity being inferred. It can supply a likelihood, a distribution of future records or a reason the intended inference remains ambiguous. This pattern develops probabilistic formulation within mathematical modeling. The subject practice supplies the meaning of the event, the observation procedure and plausible relations among quantities.

You need conditional probability and sums over alternatives; continuous cases also use densities and integration. A collaborator can supply those operations when you can describe the observation procedure and interpret the returned law. If an existing model already represents that procedure and answers the question, use it. When only compatible ranges are needed, C.16.IR can provide a sufficient answer without probabilities.

### MMP.7:2 - Problem

The distribution of a subject property and the distribution of its records can differ. Selection changes which cases appear. Coarsening combines several possible values into one report. A common influence makes observations dependent. These transformations remain part of the inference even when a dataset presents every row in the same format.

A formula such as independent errors around a predicted value already makes choices about those transformations. If the choices are left implicit, more data and more accurate computation can reinforce a mistaken interpretation.

The difficulty is to construct the law of the observations from the modeled subject and its recording procedure, preserving the dependencies that matter to the question.

### MMP.7:3 - Forces

| Choice | What changes in the inference |
| --- | --- |
| Target population and included cases | A result about reported cases may require a selection model before it describes the target population. |
| Retain or remove unobserved quantities | Keeping them can clarify construction; summing or integrating them out can simplify computation. |
| Separate and shared influences | Conditional independence can hold while observations remain dependent after a shared influence is removed. |
| Rich observation model and obtainable information | Extra parameters can represent real effects while leaving the desired answer less identifiable. |
| Probabilistic answer and sufficient conditional answer | A likelihood can be useful before choosing an estimator or a prior. A bound may already settle the action. |

### MMP.7:4 - Solution

Construct the possible recorded outcomes from the observation procedure. Combine the subject and recording laws, remove the unobserved alternatives by the appropriate probability operation, and inspect what the resulting law permits you to infer. Return to the procedure or assumptions when its output does not answer the working question.

#### MMP.7:4.1 - Choose the target and the recorded outcome separately

State what the answer concerns: a rate in a population, a property before measurement, a future response, or another quantity selected by the work. Specify the population, conditions and time range when they change its meaning. Use C.16 for the characteristic being measured and C.16.MR for the relation from the property to an indication.

Describe one complete outcome of the observing procedure. It may contain a value and an inclusion flag, a duration and a timeout flag, or several related readings. The mathematical outcome space must distinguish every report the procedure can produce that affects the inference.

State what the observation plan fixes. Following a known cohort produces information about excluded cases that a sample drawn only from submitted reports may lack. Stopping after a specified time, after a specified number of records, or after an event can produce different data laws. Recover the actual plan before treating any count as fixed.

#### MMP.7:4.2 - Construct the joint law from the modeled dependencies

Introduce variables for the quantities used by that procedure. Explain their domains and meanings before assigning distributions. Let Z denote an underlying event or value and O its recorded outcome. Parameters theta describe quantities held fixed in the proposed probability model. When these laws are represented by probability masses or by densities under an appropriate reference measure, write the subject law as p_theta(z) and the conditional recording law as k_theta(o given z). Their joint expression is:

`p_theta(z,o) = p_theta(z) k_theta(o given z).`

Each factor needs an interpretation. The first describes variation in the subject under the stated conditions; the second describes how the procedure records it. A deterministic recorder assigns probability one to its specified output and zero to the other outputs. This accommodates rounding and threshold reports as well as random response or selection.

Use a sequence of conditional laws when more stages matter. Multiplication follows the chain rule. Omitting a variable from a conditional law asserts that, given the retained variables, it does not change that law. Make that assumption from the modeled relation; separate rows in a file provide no independence argument.

Keep an unknown fixed parameter as unknown. Give it a probability distribution only when that additional modeling choice is justified for the intended inference. A shared but unknown calibration offset can remain a parameter in a joint likelihood. A distribution over possible offsets supports a different, explicitly extended model.

#### MMP.7:4.3 - Obtain the law for what was actually recorded

The general operation averages the chance of an observed event over the underlying cases. Let K_theta(B given z) be the chance that the report falls in a set B, given underlying value z. Then:

`P_theta(O in B) = integral K_theta(B given z) P_theta(dz).`

Here P_theta(dz) means averaging with the probability law of Z: a weighted sum for discrete cases or an integral for continuous ones. A deterministic recorder O=g(Z) has K equal to one when g(z) lies in B and zero otherwise. This constructs its output law even when the joint pair (Z,O) has no ordinary joint density, as with O=Z for a continuously varying Z.

When the masses or densities used in :4.2 are available, the same averaging operation gives the law of a particular report. For discrete unobserved alternatives, sum:

`p_theta(o) = sum_z p_theta(z) k_theta(o given z).`

For continuous alternatives, integrate the product of the subject density and the recording factor. A report produced exactly when Z lies in a fixed set A has recording factor one inside A and zero outside; its probability reduces to the integral of the density over A. If the procedure chooses which set to report, retain that choice in k_theta(A given z).

For example, let Z be equally likely to be 0 or 1. A truthful recorder reports {0,1} always when Z=0 and with probability 1/2 when Z=1; otherwise it reports {1}. The probability of receiving {0,1} is `1/2 + (1/2)(1/2) = 3/4`, although the probability that Z lies in {0,1} is one. The recording factor makes the difference.

For an individually observed continuous value, use a density with respect to the stated measurement convention. A point density and the probability of an interval have different meanings.

When inclusion in the dataset is itself a condition of sampling, retain its normalization. If Z has density or mass p_theta(z), and s_theta(z) is its probability of inclusion, the included-case law is:

`p_theta(z given included) = p_theta(z) s_theta(z) / P_theta(included).`

The denominator is obtained by summing or integrating the numerator over all admitted z and must be positive. If it depends on theta, dropping it changes the inference. When the counts or identities of excluded cases are also observed, include that information in the joint outcome instead of silently discarding it by conditioning. Section :5.1 shows the change.

Keep shared influences shared during elimination. For observations conditionally independent given an unknown B, integrating one joint product over B generally differs from multiplying separately integrated factors. The latter construction assigns a fresh B to each observation. Use it only when that is the observing arrangement.

#### MMP.7:4.4 - Connect the law to inference and prediction

When the observation laws have a common probability-mass or density representation, insert the recorded outcome o into p_theta(o). As a function of theta, this gives a likelihood, up to a factor independent of theta. It need not sum or integrate to one over theta. Estimation or a posterior distribution requires the chosen inferential method and its assumptions; the observation law is the input to that work.

Before drawing an inference, check whether the recording rule admits the received report for any parameter value. A continuous reading can be admitted even though its single-point probability is zero; determine admissibility from the modeled observation mechanism and the cases it permits. If no admitted case produces the report, return the conflict and locate which assumptions or recording steps need reconsideration, using C.16.IR:4.4. For example, a fixed signal with one fixed additive offset and one unchanged threshold must produce identical bits on repetition. A mixed sequence contradicts that joint account. It cannot be repaired by fitting a different signal within the same family.

Identify how the requested quantity depends on theta or on a future outcome. Two parameter settings can induce the same law for every possible record while assigning different values to the target. Constructing such a pair shows that this observation model cannot identify that distinction. C.16.IR supplies the corresponding compatible-case reasoning; numerical fitting alone cannot resolve it.

For a future record, specify whether its recording procedure is the same. For the underlying population quantity, return through the subject law rather than interpreting a selected-case rate as the population rate. A proposed intervention requires its changed relations under C.28; changing a predictor value in a fitted association is insufficient when the intervention changes how the data arise.

#### MMP.7:4.5 - Test a consequence and revise the construction

Check normalization and a small case that follows the procedure. Enumerate a finite outcome space or generate subject cases and pass them through the recorder. Compare that construction with the probabilities or summaries derived from the observation law. C.29.2 supplies a computational construction when enumeration or integration needs further work.

When the inclusion rule, timeout, shared calibration or receiving question actually changes, revise the affected relation and carry its consequence through the calculation. Compare a plausible alternative condition when the comparison can change the intended use or returned claim; this can expose the observation mechanism beyond one fixed formula. An already sufficient construction under unchanged conditions needs no invented variation.

A simulation agreeing with the formula checks their agreement under the modeled assumptions. An available observation can challenge those assumptions; selected domain assurance determines which empirical comparison is worth performing. C.11.DUA helps choose between further observation, a conditional answer and acting with remaining uncertainty. Preserve a sufficient result without demanding another dataset merely because an influence remains unknown.

### MMP.7:5 - Archetypal Grounding

#### MMP.7:5.1 - Infer a success rate from a selectively submitted log

A team asks what fraction of attempts succeed. In a proposed model, each attempt succeeds with probability p. Every success is logged; each failure is logged independently with probability 1/4. Initially the team has a fixed-size sample of independently drawn log entries, with no information about how many attempts produced the source log.

The event variable Y is success or failure. The recording flag R says whether the attempt enters the log. Their joint probabilities are:

| Outcome | Probability |
| --- | --- |
| Success, logged | p |
| Failure, logged | (1-p)/4 |
| Failure, unlogged | 3(1-p)/4 |

The included-case success probability is `q = p / [p + (1-p)/4] = 4p/(1+3p)`. If the observed fraction of successes is 1/2, the likelihood estimate of q is 1/2, and transforming it gives `p_hat = q_hat/(4-3q_hat) = 1/5`. Sampling uncertainty remains; this calculation corrects which rate is being estimated.

The first useful result is the distinction between a 50% rate among reports and the estimated 20% rate among attempts under the supplied reporting assumptions. If the failure-reporting probability is unknown, several combinations of that probability and p can produce the same q. The log alone then leaves the population rate unresolved.

Now the procedure changes: a register names a fixed cohort of N attempts and links each submitted report to its attempt. Model those attempts as independent, each with the same success probability p, retaining the stated reporting rule. Since every success is reported, an unreported attempt is a failure. If there are k success reports, the likelihood for p is proportional to `p^k (1-p)^(N-k)`; the failure-reporting factors do not depend on p. The estimate becomes k/N. Conditioning only on reported entries would throw away information the revised procedure provides.

This is a change in the team's observing method. ME can describe the linked-attempt register and responsibility for recording it. Whether to introduce it depends on what resolving the population rate would change in the team's work.

#### MMP.7:5.2 - Preserve a common influence across readings

Two sensors measure quantities x1 and x2 with one shared calibration offset b. Their readings are `Y1=x1+b+E1` and `Y2=x2+b+E2`, with independent zero-mean errors of variance sigma squared. Begin by retaining b as a common parameter. The joint conditional density factors given b; each factor uses that same value.

For the difference, `Y1-Y2=x1-x2+E1-E2`: the offset cancels. Its error variance is `2 sigma^2`. A measurement of the difference can therefore be useful while either absolute value remains uncertain.

For repeated measurements of one x, suppose an additional justified model describes the common offset as a zero-mean random variable B with variance tau squared, independent of the errors. The average of n readings has variance `tau^2 + sigma^2/n`. Integrating a separate offset for every reading would incorrectly produce `(tau^2+sigma^2)/n`. Repetition reduces independent noise but leaves this common calibration contribution.

If the instrument is independently recalibrated before every reading, the arrangement changes. A separate-offset model can then be appropriate. The governing operation is to trace which influences are shared and preserve that sharing in the probability construction.

#### MMP.7:5.3 - Use a timed-out trial as an interval report

A test asks how long an event takes. Each independent trial is observed until its event or a fixed timeout c. Record both `V=min(T,c)` and a flag D indicating whether the event occurred before timeout. As an illustrative subject assumption, let T have exponential density `lambda exp(-lambda t)` for t at least zero, with lambda positive.

An event at time t before c contributes the density `lambda exp(-lambda t)`. A timeout contributes `P(T>=c)=exp(-lambda c)`, obtained by integrating the density over the unobserved tail. For m completed trials and total observed time S, including the timeout durations, the likelihood is proportional to `lambda^m exp(-lambda S)`.

With completions at times 1 and 2 and one timeout at 4, `S=7` and `m=2`. Maximizing this illustrative likelihood gives `lambda_hat=2/7`. Treating the timeout as a third event instead gives 3/7; dropping it gives 2/3. The flag determines which operation is correct.

If only completed trials enter a database and neither the number nor identities of timed-out trials are available, the observed-time density instead conditions on completion: divide the event density by `1-exp(-lambda c)` on the interval before c. A changed recording rule changes the model even when the stored times look the same. The exponential assumption is dispensable: a different duration law supplies its own event density and tail probability.

### MMP.7:6 - Bias-Annotation

The visible dataset invites treating its rows as the whole observation procedure. Begin from how a row, absence or interval report is produced. A second temptation is to add one independent error to every row; trace shared influences before factorizing. More detailed modeling can also conceal missing knowledge, so retain uncertainty in the recording mechanism when the available information does not determine it.

### MMP.7:7 - Conformance Checklist

- Can a reader identify the target and all possible reports that affect the inference?
- Do the subject and recording factors describe the stated procedure, including what it fixes and what it reveals?
- Are unobserved alternatives removed by a justified sum, integral or conditioning operation?
- Does the joint law preserve common influences and any information about excluded cases?
- Is the first result interpreted as a likelihood, estimate, prediction, bound or unresolved distinction with its respective conditions?
- Can the formulation be changed when the observing procedure or receiving question changes?

### MMP.7:8 - Common Anti-Patterns and How to Avoid Them

| Failure in this work | Repair |
| --- | --- |
| Reported-case frequency is substituted for population frequency despite selective reporting. | Derive the included-case law and the relation to the target rate. |
| An interval report is replaced by an event at its endpoint. | Sum or integrate the joint subject-and-recording law over the underlying values that can produce the report. |
| A common influence is independently removed from every observation. | Keep it in the joint law before elimination. |
| A likelihood is read as a probability distribution over the unknown parameter. | Supply the inferential method that turns it into the requested result. |
| A fitted model is trusted because its simulator reproduces its own assumptions. | Separate computational agreement from the subject comparison needed for the use. |

### MMP.7:9 - Consequences

The constructed law allows computation to answer the intended observation question and can expose an ambiguity before expensive fitting. A changed reporting procedure becomes a model change that can be analyzed. The work may also show that the target needs assumptions or information absent from the records; a narrower conditional answer can remain useful.

### MMP.7:10 - Architectural Rationale

The observation procedure connects the subject to the data used in inference. Keeping that connection explicit makes deterministic coarsening, random selection and shared uncertainty instances of one construction. It also separates modeling choices from the later choice of an inference algorithm.

The factors are chosen for the procedure and question. Their order as a probability factorization does not establish a causal direction in the represented world. Several factorizations can describe one joint law; the subject account and intervention question determine any causal interpretation.

This method uses C.16's measurement and resolvability work while supplying the probability operations those patterns leave to statistical modeling. Its examples require different transformations: conditioning after selection, joint elimination and tail integration. The transferable operation survives replacing the logged activity, sensor or timed event.

### MMP.7:11 - SoTA-Echoing

[Gelman, Vehtari and McElreath, Statistical Workflow (2025), sections 1.1-1.7](https://sites.stat.columbia.edu/gelman/research/published/Statistical_Workflow_article.pdf), emphasize measurement, assumptions, shared information and the distinction between model parameters and inferential targets. Adopt the connection of those decisions to model construction and revision. Their comparison of Bayesian and other workflows supports leaving the inference method explicit; it does not select one estimator for every observation law.

[Rubin, Inference and missing data (1976)](https://doi.org/10.1093/biomet/63.3.581), is a historical foundation for specifying when a missing-data mechanism can be ignored. Adopt the requirement to establish the applicable conditions rather than assuming that absence is harmless. Its qualifications depend on the inferential method. The examples here derive their recording laws directly and require no blanket ignorability claim.

The [Stan User's Guide 2.39 treatment of truncation and censoring](https://mc-stan.org/docs/stan-users-guide/truncation-censoring.html) provides executable constructions for restricted observations and tail reports. Adapt those probability operations to :4.3 and :5.3. The guide's programming and inference conventions are useful implementations, not prerequisites of the method. A direct finite calculation or another suitable implementation can supply the same law.

The three demonstrations are elementary constructions for this pattern. They explain the modeling operations under stated assumptions; they are not empirical reports about the activities or devices used as examples.

### MMP.7:12 - Relations

C.16.MR constructs the relation from a sought property to its indication; this pattern makes its probability law usable for inference. C.16.IR identifies what the resulting observations can resolve. C.29.2 constructs a computation for marginalization, estimation or prediction when needed, and C.29.3 addresses its realization. C.28 governs a causal use of the result. MMP.8 uses the observation model to determine the information available to a decision. B.5.MPC.R coordinates a repair spanning subject interpretation, mathematical formulation and computation. ME uses the result when the observing procedure itself is being changed.

### MMP.7:End

## MMP.12 - Formulate an Inverse Problem and Choose Whether and How to Use Regularization

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.12:1 - Problem frame

Use this pattern when you can predict records from a proposed state or model, but recovering the needed unknown from the records is ambiguous or too sensitive to their errors. A mixture can reveal its total while scarcely distinguishing its components. Accumulated activity can be known much more reliably than its instantaneous rate. You need to decide what can be recovered and what additional structure a usable reconstruction would impose.

Begin with the quantity the next use needs. Write how a candidate unknown would produce the recorded result, then vary the unknown in a direction that changes that quantity. If the records remain unchanged, that distinction is unidentified. If they change only slightly, calculate how their uncertainty affects recovery. Introduce regularization only when the remaining task warrants its extra assumptions.

**Regularization** constructs a controlled reconstruction by restricting candidates or discouraging selected variations. Its practical gain is a usable answer whose dependence on that restriction is visible. It can suppress error amplification while also suppressing real detail. The result may be a conditional estimate, a sufficient target bound, or a reason the requested reconstruction needs another contribution.

This is the inverse-formulation branch of mathematical modeling. It constructs the reconstruction problem and the added structure that shapes its answer. Statistical inference supplies probability claims when needed; computational methods obtain solutions to the stated problem. The examples use linear equations, norms and elementary differentiation. More difficult operators require suitable mathematical preparation or a collaborator who can supply their inverse and stability analysis. A person or AI participant still needs the subject grounds for the forward relation and the proposed restriction.

Use an adequate direct inverse when its propagated error is acceptable. If an available range or comparison already settles the receiving question, return it through C.16.IR without reconstructing every unknown. Solver implementation alone calls for the corresponding computational method.

### MMP.12:2 - Problem

Matching the data can select the wrong kind of answer. Several unknowns may produce the same records, or the best fit may follow noise in a direction the observations barely constrain. More accurate solution of those fitting equations can make the reconstruction more extreme.

Additional structure can help, but it changes the grounds of the answer. A small norm favors small unknowns in a chosen representation. A smoothness penalty favors slow variation. A learned penalty favors features represented by its training and construction. Each can remove a feature the receiving question needs.

The problem is to formulate recovery so that the required target, observation relation, error account and added selection are distinguishable, and then to determine which improvement and loss the regularization produces.

### MMP.12:3 - Forces

| Force | Tension |
| --- | --- |
| Needed target and full reconstruction | A stable total or comparison can be sufficient even when individual components are unresolved. |
| Fit and sensitivity | Exact fitting retains recorded detail, including errors amplified by inversion. |
| Additional structure and lost alternatives | A restriction can make recovery usable while excluding a consequential subject case. |
| Strong regularization and bias | Suppressing weakly observed variation reduces sensitivity but can systematically displace the target. |
| Mathematical recovery and computation | Solving the selected objective accurately does not establish that it recovers the subject quantity accurately. |

### MMP.12:4 - Solution

Construct the forward relation for the requested target, locate the consequential loss of distinction or amplification, and choose the smallest justified restriction that changes that difficulty. Formulate its strength together with the error account. Return the target with the dependence and loss introduced by that choice.

#### MMP.12:4.1 - Construct the forward relation from the modeled situation

Name the unknown x, the target q=T(x), and the records y. The unknown may be a parameter vector, a function or a collection of relations. State its domain and the units and scales used to compare changes. A target can be a total, a value at one time or a threshold; it need not be x itself.

Follow a candidate x through the modeled process and recording operation. Write the resulting ideal record as F(x,z), where z contains influential unknowns that are not the target. Keep known inputs fixed and retain shared unknowns across records. MMP.11 constructs a missing model family; C.16.MR supplies a missing measurement relation. If probabilities matter, MMP.7 constructs the recording law.

For an additive bounded-error account, one possible formulation is

`y_delta = F(x,z) + e, with ||e||_Y <= delta.`

Here delta bounds error in the chosen record norm. Use this form only when the recording procedure supports additive error. For an implicit forward relation, retain its equations and jointly unknown outputs rather than forcing it into a single-valued map. A likelihood from MMP.7 can instead supply the data discrepancy appropriate to a probabilistic account.

Include consequential uncertainty in calibration and in the forward approximation. A fixed but unknown offset remains an unknown; setting it to zero can make recovery appear better determined. A noise bound and a standard deviation have different meanings and support different conclusions.

#### MMP.12:4.2 - Locate the part that needs regularization

Use C.16.IR's compatible cases or sufficient bounds to establish what the current records and premises resolve. Reuse that result. This pattern adds the construction of a recovery rule and analysis of the rule's sensitivity.

For a linear relation y=A*x, a change h with A*h=0 is invisible to the records. If both x and x+h are admitted and T(x+h) differs from T(x), full recovery of that target needs another premise. If T is unchanged, the invisible direction may be irrelevant to the current use. For unknown influences, vary x and z jointly.

Next examine changes that are visible but weak. In finite dimensions, after meaningful scaling, singular values of A describe the response to orthogonal input directions. A small nonzero singular value sigma means that direct inversion multiplies the corresponding record error by 1/sigma. Estimate the effect on T, not merely on an unnecessarily detailed reconstruction. For nonlinear models, a derivative can reveal local weak directions; it does not establish global uniqueness or exclude another branch.

Distinguish poor conditioning from a discontinuous inverse. An invertible finite matrix has a continuous inverse, although its error amplification may be unacceptable. In a function-space problem, data changes tending to zero can produce target changes that do not tend to zero. The spaces and norms determine this claim; :5.3 gives an explicit example. Refining a finite discretization can expose progressively larger amplification.

If the supported target bound is already sufficient, stop. If the premises are inconsistent, return to their diagnosis through C.16.IR. A penalty cannot make an incompatible observation account true.

#### MMP.12:4.3 - Turn the added structure into a reconstruction problem

State why particular alternatives should be excluded or discouraged. A known nonnegative quantity can justify a hard domain restriction. A supported slowly varying response can justify discouraging rapid changes. A reference state can justify penalizing departure from it. When the structure is only a preference for selecting one nominal model, say so; the selected model then remains one conditional representative.

A useful variational formulation is

`(x_lambda,z_lambda) in argmin over (x,z) in C of D(F(x,z),y_delta) + lambda*R(x,z).`

C contains the hard conditions. D measures discrepancy in records. R is the regularizer: the quantity whose increase discourages a candidate. The parameter lambda controls its weight. Explain each term's subject meaning and scaling. Adding squared errors with different units, or changing units without changing the weights, changes the problem.

Choose R by deriving which variations it penalizes. For a quadratic example,

`R(x) = ||L*(x-x0)||^2.`

The reference x0 and operator L determine the preference. L=I penalizes distance from x0; a difference operator penalizes changes between neighboring values. The latter permits constant shifts unless another condition fixes them. A sparsity penalty is appropriate only when concentrating the unknown in relatively few components fits the intended representation and subject question.

For a finite, unconstrained real linear problem with scaled squared discrepancy, differentiating the quadratic objective gives

`(A^T*A + lambda*L^T*L)*x = A^T*y_delta + lambda*L^T*L*x0.`

For lambda>0 this has a unique minimizer when the null spaces of A and L intersect only at zero. Thus adding a penalty does not by itself guarantee unique recovery. Constraints and nonlinear or nonconvex choices require their own existence, uniqueness and obtaining arguments.

An alternative is to minimize R subject to a justified discrepancy ceiling. This makes the acceptable fit explicit. It can agree with a penalized formulation for suitable parameters, but the correspondence must be established for the problem being used.

A learned regularizer is another way to construct R. Its training examples and training objective supply additional structure, whose relevance to the current subject and observation conditions must be justified. Compare it with the simpler available restriction on the same required target and with its training and obtaining costs included. A visually plausible or numerically precise reconstruction can still lose the feature the target asks for.

#### MMP.12:4.4 - Select strength from the required sensitivity and tolerated loss

Work out how the added structure changes recovery before choosing its numerical strength. For L=I, x0=0 and one nonzero singular direction, quadratic regularization replaces division by sigma with multiplication by

`sigma/(sigma^2 + lambda).`

This reduces noise amplification. With exact data, it also multiplies the true component by `sigma^2/(sigma^2+lambda)`, shrinking it toward zero. A component invisible to A is selected through the regularizer, not recovered from the records.

Choose lambda using the error account and the receiving use. A bound on acceptable noise amplification, together with a bound on tolerated shrinkage, can determine an interval of useful values. Section :5.1 computes such a choice. A supported discrepancy level can instead guide a parameter search: compare each candidate's residual with the level warranted by the observation and model errors. An empirical choice rule needs evidence appropriate to its own claim; fitting the available records best is not a general parameter-selection argument.

Evaluate both sides of the trade-off. Compare the changed target when the data are perturbed within their error account and when the reference, penalty or strength changes within its justified range. Return consequential dependence rather than hiding it behind one selected value. A few numerical trials can reveal a failure; they establish a bound only when an argument covers the claimed variation.

If no supported strength gives the needed sensitivity and tolerable loss, narrow the target or return the missing contribution. A stronger penalty can make outputs nearly constant while leaving them useless for the question.

#### MMP.12:4.5 - Separate recovery error from solving error

For a linear reconstruction rule H_lambda and exact data y, the triangle inequality separates two contributions:

`||H_lambda*y_delta - x_target|| <= ||H_lambda*(y_delta-y)|| + ||H_lambda*y - x_target||.`

The first is propagated data error; the second is the displacement caused by the reconstruction rule even with exact data. Choose x_target explicitly: an identified true unknown, a specified minimum-norm solution, or another admitted target. Those are different claims. Numerical approximation adds its own contribution, which MATH.20 and CMP.8 can bound.

For a fixed regularization strength, establish only the stability supported by the formulation. A unique minimizer in a general nonlinear problem is not automatically a quantitative stability bound. If the claim concerns recovery as noise tends to zero, specify how strength and any discretization change with that noise. Fixed-strength bias may persist. Classical regularization analysis supplies conditions for this limit; the existence of a penalty is insufficient.

Keep that limit separate from iterations of a solver converging at fixed data and strength. The solver can converge to the exact minimizer of a biased problem. Conversely, early stopping can itself be a regularization choice when its stopping rule has an appropriate noise-dependent justification. Additional iterations then need not improve the subject reconstruction.

For ordinary finite use, obtain only the error or settled distinction the receiver needs. A limiting theorem need not be proved anew when an applicable result and a sufficient finite bound are available.

#### MMP.12:4.6 - Return the useful target and the choice it depends on

Return T(x_lambda) with the forward relation, consequential error assumptions and added restriction needed to interpret it. State what remains unresolved and how much the target changes under the relevant data and regularization variations. Preserve a compatible range when it is needed alongside a nominal reconstruction. A penalty-selected point alone supplies neither a confidence interval nor a posterior distribution.

Regularization changes the grounds for selecting an answer; it creates no new observation from the old records. When a different premise, observation relation or target would remove the difficulty, name that contribution. Further computation helps only if the remaining problem is computational.

A person or AI can propose the formulation, calculate the example and compare alternatives. The needed subject relation and mathematical argument must still be available from a competent participant or established result. When they are missing, return the precise question they must answer. B.5.RR carries a changed premise through the reasoning; B.5.MPC.R helps coordinate a revision spanning subject, mathematical and computational contributions.

A methodological use can take the same result back to a working method: for example, replace an unstable instantaneous-rate target by a sufficient interval total, or revise how records are obtained when a needed distinction remains invisible. Such a change is selected for the original use, not made compulsory by the presence of an inverse problem.

### MMP.12:5 - Archetypal Grounding

#### MMP.12:5.1 - Recover a split whose contrast is weakly observed

Suppose two nonnegative loads x1 and x2 have exactly known total s=3. A second channel measures a small contrast:

`d=x1-x2; z=0.01*d+e; |e|<=0.02.`

All values are expressed in fixed normalized units. The recorded z is 0.03. The inverse relations are `x1=(3+d)/2` and `x2=(3-d)/2`, so nonnegativity gives -3<=d<=3. The error account gives 1<=d<=5; jointly, the compatible contrasts are 1<=d<=3.

If the question concerns the total or whether d is positive, this already answers it. A simulation that needs one nominal split must introduce a selection. Suppose its stated reconstruction requirement is to limit the contribution of channel error to at most 1 contrast unit, while accepting at most one-half shrinkage toward balanced loads. This is a modeling preference for the nominal input, not additional evidence that the loads are equal.

Use the objective

`J_lambda(d)=(0.01*d-0.03)^2 + lambda*d^2; -3<=d<=3.`

Its unconstrained minimizer, whenever it lies in that interval, is

`d_lambda=0.01*z/(0.0001+lambda).`

The data-error contribution is bounded by `0.01*0.02/(0.0001+lambda)`. Making it at most 1 requires lambda>=0.0001. The exact-data shrinkage fraction is `lambda/(0.0001+lambda)`; making it at most one-half requires lambda<=0.0001. These two declared requirements select lambda=0.0001.

The nominal result is d_lambda=1.5, hence (x1,x2)=(2.25,0.75). Its predicted contrast record is 0.015, leaving residual 0.015 within the supplied error bound. For this fixed strength, the interior reconstruction gain is 50, compared with 100 for direct inversion. Projection onto the admitted interval cannot increase that gain.

The bias matters. If the underlying contrast were d=1 and the error e=0.02, direct inversion would return 3 and this regularized rule would return 1.5. If the underlying contrast were d=3 with e=0, the same observed record would make direct inversion correct and the regularized rule would understate the contrast by 1.5. These are two constructed compatible cases, not an empirical accuracy comparison.

For a worst-case guarantee from these records, retain [1,3]. Its midpoint 2 has maximum absolute error 1 over that interval, while the selected nominal value 1.5 has maximum error 1.5. The midpoint is the better choice for that different criterion. Regularization is justified here by the declared response and shrinkage requirements, not by a claim that it improves every error criterion.

**Changed condition.** A new acquisition reports the same z=0.03 with supported error bound 0.002. The compatible interval is now [2.8,3]. Direct inversion has data-error contribution at most 0.2, already below the allowed 1. Choose the weakest penalty meeting that requirement: lambda=0 now suffices and introduces no shrinkage. It returns d=3 with the interval [2.8,3]; a receiver minimizing worst-case absolute error could instead use 2.9.

Keeping the old strength would return d=1.5 and residual 0.015, incompatible with the new error bound. The changed observation condition, not more accurate minimization of the old objective, changes the useful formulation.

#### MMP.12:5.2 - A circulation selected away by minimum norm

Three stores exchange material around a directed cycle. Let the nonnegative transfers be a from the first to the second, b from the second to the third, and c from the third to the first. Their stock changes are

`F(a,b,c)=(c-a, a-b, b-c).`

Observed zero stock changes allow every (a,b,c)=(t,t,t) with t>=0. Minimizing a^2+b^2+c^2 selects t=0. The minimizer is unique, yet a circulation of one unit gives exactly the same records. Minimum norm has supplied a nominal no-circulation choice, not evidence that no transfer occurred.

A question about net stock change is already settled. A question about gross transported amount 3*t remains unresolved unless the subject account supplies another restriction or observation. If the stores can circulate material during unchanged stocks, using the minimum-norm answer as measured throughput would erase the quantity being sought.

#### MMP.12:5.3 - An accumulated quantity with an unstable derivative

In a continuous model on the normalized time interval [0,2*pi], accumulated activity is N(t), and its rate is r(t)=N'(t). Consider

`N(t)=2*t; N_k(t)=2*t + sin(k*t)/k`

for positive integers k. Their maximum difference is 1/k, tending to zero. Their rates are 2 and `2+cos(k*t)`, whose maximum difference remains 1. Both accumulated curves are nondecreasing. Thus nonnegativity of the rate does not remove this instability in the maximum norm.

A justified bound on rapid rate variation, or a penalty on changes in the rate, can suppress the oscillatory alternative. It also risks suppressing a real short surge. Specify which temporal detail the receiving use needs before selecting that structure.

If the use needs only the total over this interval, both curves give 4*pi. Recover that target from the endpoints without differentiating. For a fixed sampling interval a finite-difference inverse is continuous, but its error amplification grows as the interval shrinks; this differs from the discontinuity of the function-space inverse just exhibited.

### MMP.12:6 - Bias-Annotation

The quadratic case makes sensitivity and shrinkage calculable. It does not make quadratic penalties appropriate for every unknown. A smoothness preference can remove discontinuities; a sparsity preference depends on the representation; a learned preference can lose features absent from its construction cases.

The method treats the subject grounds of additional structure as a separate contribution. Its mathematical examples establish consequences of stated premises, not the suitability of those premises for a particular physical or organizational situation. More consequential use can require stronger subject evidence or a validated target bound; ordinary use can stop at an already sufficient comparison.

### MMP.12:7 - Conformance Checklist

- The target and forward relation are recoverable, including consequential unknown influences, units and record-error assumptions.
- Indistinguishable alternatives and error amplification are distinguished; a sufficient target is used without demanding full recovery.
- Each hard restriction or penalty has a subject justification or an explicit nominal-selection purpose. Its excluded or discouraged variation is identifiable.
- The strength choice exposes both sensitivity reduction and target loss. A changed observation condition is carried through that choice.
- Existence, uniqueness, stability, vanishing-noise recovery and solver convergence are claimed only at the scope established for the formulation.
- The returned target retains consequential dependence on added structure and the uncertainty needed for its receiving use.

### MMP.12:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A unique penalized minimizer is reported as an identified subject value. | Show which data-indistinguishable alternatives the penalty selected among; retain the selection premise. |
| A smaller residual is treated as a better reconstruction. | Compare propagated error and regularization bias for the required target, as in :5.1. |
| An old penalty is retained after the noise or forward relation changes. | Recalculate its discrepancy, sensitivity and lost target detail under the changed condition. |
| A smooth or learned reconstruction is used for a feature its construction suppresses. | Change the restriction or return the feature as unresolved; the rate surge in :5.3 shows the relevant loss. |
| A solver's convergence is offered as stability of recovery. | State the fixed computational problem solved and separately establish sensitivity or the noise-dependent limit. |

### MMP.12:9 - Consequences

The practitioner obtains a reconstruction problem with visible reasons for its additional structure. Some questions become cheaper because a stable total or bound replaces full reconstruction. Others gain a useful nominal estimate at the cost of explicitly accepted bias.

The formulation also locates a failed use: unsupported regularity, an unresolved invisible direction, an inadequate forward relation or insufficient numerical control call for different contributions. Increasing regularization or computation indiscriminately does not resolve them.

### MMP.12:10 - Architectural Rationale

The forward relation determines what the records respond to. The target determines which unresolved variations matter. Regularization determines which remaining variations the reconstruction discourages. Keeping these three contributions separate explains why one fitted answer can be useful for a nominal simulation yet inadequate as evidence about the subject.

This method extends compatible-case interpretation by constructing the recovery rule, choosing its strength and analyzing its induced loss. The distinction from computational approximation preserves the ability to solve the chosen equations accurately while still revising their recovery assumptions.

### MMP.12:11 - SoTA-Echoing

**How should a needed reconstruction be stabilized at the available accuracy?** The selected line separates propagated error from regularization bias and chooses strength for their receiving use. The serious defaults are direct inversion or least-squares fitting, and the sufficient-bound route of C.16.IR. In :5.1, elementary calculations expose the direct gain of 100 and the selected gain of 50 at comparable effort, with shrinkage as the accepted cost. The bound wins when it settles the question; direct inversion wins after the tighter observation. **Adopt** this conditional choice in :4.2–4.5 rather than a default penalty. [Clason, *Regularization of Inverse Problems*, arXiv:2001.00617v2, Chapter 4, equation (26), and Chapters 6–7](https://arxiv.org/html/2001.00617v2) supplies the mathematical error decomposition and parameter-dependent recovery line, including iterative regularization. Its operator assumptions delimit those results; it does not justify a subject penalty. Reopen the choice when a simpler recovery or bound meets the same target conditions, or when changed error or model structure defeats the selected strength.

**When can newer learned reconstruction change that choice?** **Adapt** the distinction between reconstruction fit and recovery guarantees from [Bednarski and Roith, *Introduction to Regularization and Learning Methods for Inverse Problems*, arXiv:2508.18178v1, §§1.3–1.4, 2.3 and 3.2–3.3](https://arxiv.org/html/2508.18178v1). Its mathematical treatment is a best-known-line candidate for comparing classical and data-dependent regularization: training distributions and parameter rules matter to the resulting guarantee. This changes :4.3–4.5 by retaining the added structure and its recovery conditions when R is learned. A trained replacement is a serious alternative when a simple penalty loses important structure, but requires a target-specific comparison including its extra preparation cost.

[Hertrich et al., *Learning Regularization Functionals for Inverse Problems: A Comparative Study*, arXiv:2510.01755v1, §§5.1–5.5](https://arxiv.org/html/2510.01755v1) supplies bounded rival and failure evidence: its imaging comparisons show dependence on training, task and cost, and report attractive reconstructed geometry that differs from ground truth. **Reject** transferring an imaging ranking into a general reconstruction rule. Retain its action-changing lesson in :4.3: compare the actual required feature under applicable conditions. Reopen when a learned alternative preserves that feature better at justified total effort, or when a changed observation model or subject domain invalidates the comparison.

### MMP.12:12 - Relations

- **Uses MMP.11** to construct the model family from which the forward relation is assembled, and **MMP.7** when a probability law of records is needed.
- **Uses C.16.MR** for a missing measurement relation and **C.16.IR** for compatible alternatives and sufficient target bounds. Adds regularized formulation, strength selection and analysis of induced sensitivity and loss.
- **Uses MATH.20** for error and target bounds. **CMP.6 and CMP.8** supply an iterative obtaining method or controlled approximate computation for the selected problem.
- **Supplies statistical inference** with the target, observation account and unresolved dependence on added assumptions when an estimate's probability or uncertainty is needed. **Supplies observation design** with the distinctions an additional observation would need to resolve.
- **Returns to B.5.RR and B.5.MPC.R** when the required result changes the mathematical, subject or computational contribution. Method Engineering can use that result when revising how a working method obtains or uses observations.

### MMP.12:End

## MMP.13 - Infer Unknowns Statistically under a Stated Observation Model

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.13:1 - Problem frame

Use this pattern when a probability model describes how records arise, and the work needs an estimate, an interval or a probability about something not directly known. The wanted quantity may be a failure probability, a mean before measurement error, a response for a different mix of cases, or a future outcome.

Start by writing the sentence the result must support. “This procedure covers the fixed unknown in at least 95% of its modeled repetitions” differs from “the unknown lies here with 95% posterior probability under these assumptions.” A probability about the next observation is another question. Choose the inferential construction that supports the required sentence.

The result is an estimator or posterior and its consequence for the requested target, with an interpretable account of uncertainty. It exposes which assumptions make the conclusion possible and which change would require recalculation. Reporting a fitted coefficient and a number labeled “error” can otherwise leave the actual question unanswered.

This is statistical inference within mathematical modeling. MMP.7 supplies the law of the records; MMP.12 supplies unresolved recovery ambiguities and any regularization choices. The present method constructs what may be concluded under that law and additional inferential assumptions. Selecting an action also needs its consequences and preferences, supplied by a decision method such as MMP.8.

The reader needs conditional probability, expectations and quantiles; continuous models also use integration. A mathematically qualified collaborator can supply those operations when the practitioner can specify the observation process and interpret the target.

Use an existing sufficient inference directly. If a compatible range already settles the question, C.16.IR can end the work without a probability model. A missing observation law returns to MMP.7; constructing a numerical sampler for an already specified posterior belongs to CMP.9.

### MMP.13:2 - Problem

The distribution of the observed records does not itself choose an estimator, an uncertainty statement or a prior. Those additions can produce different useful conclusions from the same data.

The inferential target may also differ from the fitted parameters. A nonlinear function of parameter estimates can give a different answer from averaging that function over a posterior. Shared uncertainty can remain after many repeated readings. A narrow interval for an expected response can coexist with a wide distribution for the next response.

The problem is to construct the inference needed by the receiving use while preserving its sampling, conditioning and approximation assumptions. Changing one of those assumptions must change the relevant calculation, rather than only the qualification attached to an unchanged number.

### MMP.13:3 - Forces

| Force | Tension |
| --- | --- |
| Target and parameterization | The model can contain many unknowns while the use needs only one function of them. |
| Conditional probability and repeated-use performance | A posterior probability and confidence coverage answer different questions. |
| Convenient defaults and supported assumptions | Independence, a prior or a normal approximation can simplify the calculation while changing its meaning. |
| Joint uncertainty and simple summaries | Separate standard errors can lose covariance needed by the target. |
| Inferential precision and computational precision | More accurate integration can leave the subject uncertainty unchanged. |

### MMP.13:4 - Solution

Specify the target and the intended uncertainty claim. Combine the record law with the inferential assumptions needed for that claim, derive the estimator or posterior, and propagate it to the target. Carry any actual consequential revision through the affected calculation. Compare a plausible alternative assumption only when doing so can change the use or returned claim. Return the sufficient result at the scope the calculation supports.

#### MMP.13:4.1 - Fix the target before choosing a fitting routine

Write q=g(theta), where theta denotes the unknowns in the observation model. It can index a distribution or unknown function, not just a finite vector. State the population, conditions and time range that make q meaningful. Distinguish unknowns needed only to explain the records from the target being returned.

For prediction, instead name the new outcome Y_new and its observing conditions. A conditional mean of Y_new is a function of theta; the realized Y_new also varies under the model. A proposed intervention requires a supplied causal identification argument before a fitted association can be interpreted as its effect.

Select the smallest result that changes the next use. It may be a point estimate with a stated error property, an upper confidence bound, a posterior probability of a threshold, or a predictive distribution. A threshold action still needs its loss or decision rule; a probability or confidence level does not choose that action by itself.

#### MMP.13:4.2 - Recover the law and the assumptions being added

Take the joint law P_theta of the records Y from MMP.7. Retain its inclusion, censoring, dependence and stopping conditions. Where a common probability-mass or density representation exists, inserting the observed y gives the likelihood L(theta;y)=p_theta(y).

The likelihood compares how parameter values account for the same records. It is not a probability distribution over theta merely because it can be plotted or maximized. Likewise, records in separate rows are not necessarily independent observations.

Use the existing ambiguity result from MMP.12 or C.16.IR. If two parameter values give the same observation law and different q, the records cannot distinguish that target. A prior or restriction may support a conditional answer, whose dependence on that addition remains visible.

Choose the inferential branch by the claim required. Frequentist construction assesses a data-to-answer rule across the specified observation law at fixed unknown values. Bayesian construction adds a prior law and conditions their joint model on the observed records. Neither branch removes the need for a justified observation model.

If the same data choose a model, tuning value or prior hyperparameter, include that adaptation in the inference being claimed. Treating an estimated quantity as externally known can understate uncertainty. A sensitivity comparison can instead hold the data fixed and show the consequence of several explicitly conditional assumptions.

#### MMP.13:4.3 - Construct an estimator and its frequentist uncertainty when needed

An estimator is a rule q_hat=T(Y), chosen before its repeated-use properties are assessed. Derive it from the target and observation law: for example, invert an observable expectation, solve an estimating equation, or maximize a likelihood and obtain the required function of the fitted values. State the selected property, such as a controlled error probability or mean squared error. Likelihood maximization alone supplies no interval.

One general confidence construction chooses, for each admitted theta, an acceptance region A_theta of possible records such that

`P_theta(Y in A_theta) >= 1-alpha.`

After observing y, retain those theta for which y lies in A_theta, and map them through g. The resulting set C(y) has coverage

`P_theta(g(theta) in C(Y)) >= 1-alpha`

under the stated law. A target-specific statistic can make this much cheaper than constructing a set for every nuisance parameter. The binomial inversion in :5.1 is a small example.

Coverage describes the procedure across repetitions allowed by the model, at fixed theta. It does not assign posterior probability to the parameter in the one observed interval. Nor is a confidence set the set of all logically possible values: a value outside it may still assign a small positive probability to these records.

Use an exact distribution or justified pivot when available. An asymptotic approximation needs its sample-size, regularity and boundary conditions. A bootstrap needs a resampling unit and mechanism that represent the dependence and the fitted procedure; resampling individual readings cannot reproduce an omitted common calibration error. Retain approximate coverage as approximate unless a stronger result is available.

The observation plan belongs to the guarantee. An interval justified at a fixed sample size need not preserve its coverage when repeatedly inspected until it looks favorable. Use a method valid for the actual stopping plan. For countably many looks, one conservative construction allocates error probabilities alpha_j with sum at most alpha to valid per-look intervals; the union bound gives simultaneous coverage. An applicable confidence-sequence method can provide a less conservative construction. This is a choice of inferential guarantee, not a requirement to collect more data.

#### MMP.13:4.4 - Construct a posterior when conditional probability is needed

Supply a prior probability law Pi with its subject meaning. Reweight that law by the observed likelihood and normalize, preserving any point masses and continuous parts. For a set A to which the prior assigns a probability,

`Pi_y(A) = integral_A L(theta;y) Pi(dtheta) / integral L(u;y) Pi(du).`

Pi_y denotes the posterior law. Integration against Pi means combining values under the actual prior: a sum for discrete unknowns, integration against a density where one exists, and both contributions for a mixture. A function-valued unknown requires a specified prior law and likelihood on that space, not an assumed ordinary density.

The denominator must be finite and positive; an unnormalized expression alone does not establish a posterior probability law. For a real vector theta whose prior has a density pi(theta) with respect to ordinary volume dtheta, the posterior density is

`pi(theta | y) = L(theta;y)*pi(theta) / integral L(u;y)*pi(u) du.`

This density formula is a representation of the preceding law construction under that condition. A uniform prior depends on the parameterization, and an improper prior requires a separate argument that the posterior exists.

For example, give a failure probability p prior mass 1/2 at p=0 and a uniform distribution on [0,1] for the remaining 1/2. One failure-free Bernoulli observation has likelihood 1-p. The unnormalized atom has mass 1/2; the weighted continuous part has mass 1/4. Normalizing by 3/4 leaves posterior mass 2/3 at zero. The remaining 1/3 has conditional density 2*(1-p) on [0,1]. Using only the ordinary density would lose the atom.

Retain joint dependence when removing nuisance unknowns. Sum or integrate the joint posterior over them, or calculate g(theta) from joint posterior draws. Independently combining draws from marginal distributions changes the joint law unless independence is established.

Derive the posterior of q through that transformation. For a set B,

`P(q in B | y) = integral 1{g(theta) in B} Pi_y(dtheta).`

A credible set has its stated posterior probability under this model and prior. A posterior mean, median or quantile is a chosen summary of that law. In general, `E[g(theta)|y]` differs from `g(E[theta|y])`; :5.1 computes the difference.

A penalized optimum from MMP.12 can coincide with a posterior mode when its objective represents the chosen likelihood and prior. That optimum still does not supply the posterior spread. If a prior resolves an otherwise unidentified difference, preserve that source of the resolution in the returned result.


#### MMP.13:4.5 - Propagate uncertainty to the actual receiving quantity

For a posterior predictive result, construct the law of the new observation under its specified conditions and average it over the posterior law:

`P(Y_new in B | y) = integral P(Y_new in B | theta,y) Pi_y(dtheta).`

In the density case of :4.4, Pi_y(dtheta) is pi(theta | y) dtheta. For a mixed posterior, include its atoms as well as its continuous contribution.

This includes both uncertainty in unknowns and the modeled variation of a new outcome. Where variances exist, the decomposition is

`Var(Y_new|y) = E[Var(Y_new|theta,y)|y] + Var(E[Y_new|theta,y]|y).`

The second term alone concerns uncertainty in the conditional mean. It is not the full predictive variance.

A frequentist prediction interval also needs the joint law of the original and future records. Derive a prediction error or another statistic with the needed coverage. Sharing a calibration influence with the old readings and using a fresh calibration produce different prediction problems, as in :5.2.

For a posterior of a real parameter vector theta with covariance V, the linear target q=a^T*theta has posterior variance a^T*V*a. A frequentist covariance calculation instead uses the sampling covariance of the joint estimator, retaining its repeated-use interpretation. For a nonlinear target, propagate the joint posterior or derive uncertainty from the estimator's sampling law; an approximation needs its own conditions. A confidence set for theta can be mapped through g to obtain a confidence set for q; projecting a large joint set can be conservative. A marginal interval for each coordinate does not automatically give simultaneous coverage for a function of them.

Then obtain the numerical answer with the needed accuracy. CMP.8 supplies controlled approximate computation; CMP.9 supplies a sampler or randomized computational estimator. The posterior distribution, a confidence procedure and the algorithm approximating their consequences are different results. More posterior draws can reduce Monte Carlo error in a computed mean while leaving the posterior uncertainty about q unchanged.

#### MMP.13:4.6 - Test the claimed consequence and revise the assumption that matters

Check the derivation at the level needed for its use. In a finite model, normalization, enumeration or an exact calculation may suffice. For an approximate frequentist procedure, simulation at fixed parameter values can expose bias or coverage failures under the assumed law. For a posterior computation, a suitable simulation-based calibration check draws parameters and data from their joint model and tests the inference computation. These are different checks. Agreement under a model does not establish that the model describes the subject.

Select such work for an unresolved claim. A routine use of an applicable exact result need not become a new simulation study, and simulated datasets are not additional subject observations.

When a premise or target actually changes, recalculate the affected target and uncertainty; reuse unaffected results. Compare a plausible alternative dependence, prior scale, inclusion probability or target-population weight only when that comparison can change the intended use or returned claim. State whether an altered result comes from changed records, changed assumptions or a changed target, and keep a material disagreement visible. A sufficient inference under unchanged grounds needs no invented alternative.

If observed failures call for a richer model, return the model-criticism and revision question to the relevant subject method and MMP.11. If the desired effect is not causally identified, return that identification question. Designing a new observation is a further choice when the existing result is insufficient; it is not part of every inference.

#### MMP.13:4.7 - Return the conclusion at its established meaning

Return the target, the estimate or distribution, the meaning of its uncertainty, and the assumptions whose variation changes its use. Identify a numerical approximation limit separately. Give the receiver enough to distinguish a frequentist coverage claim, a posterior probability and a predictive claim without consulting the fitting software.

Use the sufficient result. C.11.DUA helps compare another observation, a changed formulation, more computation or action with remaining uncertainty when that choice is live. B.5.RR carries a changed premise through the reasoning; MMP.8 receives inference when an actual choice needs its consequences and preferences.

A methodological use can revise how a working method treats uncertainty: retain a shared influence, compute the requested derived quantity, or stop demanding an unidentified parameter when a sufficient consequence is available.

### MMP.13:5 - Archetypal Grounding

#### MMP.13:5.1 - Zero recorded failures: two different uncertainty claims

A device is tested for a fixed four operations. All failures are recorded, and the supplied model gives independent Bernoulli outcomes with one unchanged failure probability p. No failures occur, so K=0 and the likelihood is proportional to (1-p)^4.

Suppose the requested target is the probability of at least one failure in two further operations under the same condition:

`q=1-(1-p)^2.`

The future operations are assumed independent conditional on the same p. The question concerns q, rather than every detail of an operating model.

**Frequentist construction.** The likelihood estimate is p_hat=K/4=0. Inserting it into the familiar normal standard-error expression gives zero estimated standard error and the interval [0,0]. At p=0.2, zero failures occur with probability 0.8^4=0.4096, and [0,0] excludes the true p on every such occurrence. This alone rules out 95% coverage.

For a one-sided 95% binomial upper confidence procedure, invert the lower-tail probability: for k<4 choose U(k) satisfying

`P_(p=U(k))(K<=k)=0.05,`

and set U(4)=1. Binomial test inversion gives coverage at least 95%, allowing conservatism from discreteness. At k=0,

`(1-U)^4=0.05; U=1-0.05^(1/4)=0.5271.`

Since q increases with p, its upper confidence limit is

`1-(1-U)^2=1-sqrt(0.05)=0.7764.`

This is the result of a covering procedure, not a statement that q has a 95% probability of being below 0.7764 after these records.

**Bayesian construction.** Choose a uniform prior for p on [0,1]. Multiplying and normalizing gives posterior density

`pi(p|K=0)=5*(1-p)^4; 0<=p<=1.`

Thus E[p|K=0]=1/6, and the posterior 95% upper quantile of p is `1-0.05^(1/5)=0.4507`. Transforming that quantile gives a posterior 95% upper quantile of q of `1-0.05^(2/5)=0.6983`. Its smaller value does not make it a uniformly better confidence limit; it expresses a different conditional claim with a prior.

To obtain the probability of a failure in the next pair, average q itself:

`E[q|K=0] = 1 - integral_0^1 (1-p)^2*5*(1-p)^4 dp = 2/7.`

Using the posterior mean of p first would give `1-(5/6)^2=11/36`, a different value. The posterior predictive probability is 2/7; the event of a failure in that pair remains a binary future outcome.

**Changed assumption.** Hold the four records fixed but replace the uniform prior with density `9*(1-p)^8`, favoring lower failure probabilities. The posterior becomes `13*(1-p)^12`. The posterior probability of p<0.2 changes from `1-0.8^5=0.67232` to `1-0.8^13=0.94502`; the predictive probability for a failure in the next pair becomes 2/15.

These changes come entirely from the prior. They neither add operations to the observed test nor establish that the new prior is appropriate. If its relevance is unresolved, return the conditional results and their difference. The frequentist bound remains available without that prior under the original fixed-sample observation model.

#### MMP.13:5.2 - A common calibration error survives averaging

Four readings in fixed units are 9, 10, 10 and 11, giving mean 10. Initially suppose

`Y_i=mu+epsilon_i; epsilon_i independently Normal(0,1).`

The noise variance 1 is supplied, not estimated from these four values. The sample mean is an estimator of mu with variance 1/4. An exact normal 95% confidence procedure uses `mean(Y) +/- c/2`, where c is the 0.975 standard-normal quantile, approximately 1.96. The realized interval is approximately [9.020,10.980].

A prediction interval for one independent future reading uses the error `Y_new-mean(Y)`, whose variance is `1+1/4`. Its realized 95% interval is approximately [7.809,12.191]. Uncertainty about the mean and variation of the future reading require different intervals even before any model revision.

Now revise the calibration account:

`Y_i=mu+B+epsilon_i; B~Normal(0,1).`

B is independent of the individual errors, shared by all readings in one setup, and drawn afresh across the repeated setups used to define the coverage claim. Then

`Var(mean(Y))=1+1/4.`

The confidence interval for mu widens to [7.809,12.191]. Treating B as a fresh independent error on each row would instead give variance 2/4 and understate the uncertainty. More readings in this same setup reduce the individual-noise term but leave the calibration term.

Prediction also depends on what stays shared. A new reading in the same setup has the same B, which cancels in `Y_new-mean(Y)`; the prediction-error variance remains 1+1/4. A reading in a new setup with independent B_new has variance `1+1+1+1/4=3.25` for that error, giving approximately [6.467,13.533].

These are coverage statements over the stated repeated-observation law. If B is only an unknown fixed offset with no bound or probability law, these normal intervals for mu do not follow. MMP.12 then retains the unresolved separation of mu and B; assigning B a distribution is an additional modeling contribution.

#### MMP.13:5.3 - Infer the rate for the receiving workload

Two classes of requests have different probabilities of finishing by a deadline. For class A, seven of eight observed requests finish; for class B, one of eight finishes. Assume fixed sample counts, independent Bernoulli outcomes within each class, independent class data, and independent uniform priors for p_A and p_B.

The posterior densities are proportional to `p_A^7*(1-p_A)` and `p_B*(1-p_B)^7`: Beta(8,2) and Beta(2,8). Their means are 0.8 and 0.2, and each variance is 4/275. The posteriors are independent under the stated construction.

For a future workload selecting the two classes equally, the conditional completion probability is `q_old=(p_A+p_B)/2`, with posterior mean 0.5. Now change only the receiving workload: its known class proportions are one-quarter A and three-quarters B. The target becomes

`q_new=p_A/4+3*p_B/4.`

Its posterior mean is 0.35 and its posterior variance is

`(1/4)^2*(4/275)+(3/4)^2*(4/275)=1/110.`

No new fitting is needed for this changed target. Carrying forward 0.5 would answer for the old mixture. If the target were an individual future completion indicator, its posterior predictive probability would be 0.35 and its variance 0.35*0.65, rather than 1/110.

The transfer assumes that the within-class probabilities remain applicable. Changed operating conditions require their own relation. Uncertain class proportions or a shared influence on the two probabilities require joint uncertainty, rather than the independent weighted-variance calculation above.

### MMP.13:6 - Bias-Annotation

The worked laws are simple enough for exact calculations. Real records can have selection, dependence, weak identification or model mismatch that a convenient binomial or normal family conceals. The resulting uncertainty is conditional on the assumptions represented; it does not automatically include an omitted mechanism.

Bayesian and frequentist results are compared by the conclusions they support. A narrower interval alone cannot rank different probability meanings. The choice of prior, coverage domain and receiving target is part of the inference, even when software supplies defaults.

### MMP.13:7 - Conformance Checklist

- The inferential target and its subject conditions are stated separately from nuisance unknowns and the subsequent decision.
- The observation law retains consequential recording, dependence and stopping assumptions.
- The estimator's repeated-use claim or the posterior's conditioning assumptions are recoverable; normalization or coverage has an applicable basis.
- Joint uncertainty is propagated to the actual target. Parameter uncertainty, future-observation variation and numerical error are distinguished.
- Any actual consequential revision is propagated through the affected target and uncertainty calculation. A sensitivity comparison addresses a live alternative that can change the use or returned claim; an unchanged sufficient inference needs none.
- The returned conclusion is sufficient for its use or names the missing contribution without requiring an automatic new experiment.

### MMP.13:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A confidence interval is read as posterior probability for the observed interval. | State which object varies under the probability law and which claim the construction supports. |
| A likelihood curve or penalized optimum is treated as a posterior distribution. | Supply and normalize the prior-likelihood construction before using posterior probabilities. |
| A derived result is computed only from parameter means or separate standard errors. | Transform the joint inference; retain nonlinear effects and covariance. |
| More readings are assumed to remove a shared uncertainty. | Derive the variance under the actual dependence, as in :5.2. |
| Smaller Monte Carlo error is reported as less subject uncertainty. | Qualify the computed summary separately from the distribution it summarizes. |
| The prior or fitted model is changed without recalculating the receiving conclusion. | Carry the revised assumption through the target and uncertainty calculation. |

### MMP.13:9 - Consequences

The receiver gets an estimate or distribution with a usable meaning for its uncertainty. A needed probability, bound or prediction can be obtained without recovering every parameter, and a changed target can sometimes reuse the existing joint inference.

The method also makes the cost of assumptions visible. Another record, another prior and another numerical approximation change different parts of the answer. A sufficient inference can be used while a stronger claim remains unresolved.

### MMP.13:10 - Architectural Rationale

The observation model describes how records vary. The inferential construction determines how those records support conclusions about unknowns. Target propagation determines which consequence reaches the receiving use. Their separation permits a computation to be correct while its prior, target or observation assumption is still reconsidered.

This preserves the distinction from inverse-problem regularization, numerical computation, causal identification, model criticism and decision making. Those methods supply or receive particular contributions; none is obtained merely by fitting a statistical model.

### MMP.13:11 - SoTA-Echoing

**Carrying fitting into the required conclusion.** **Adopt** target-specific propagation of joint uncertainty rather than reporting a coefficient table or substituting parameter means. [Gelman, Vehtari and McElreath, *Statistical Workflow*, §§1.3–1.6 and 1.10, author manuscript dated 5 December 2025 for the 2026 article](https://sites.stat.columbia.edu/gelman/research/published/Statistical_Workflow_article.pdf) explains how dependencies, derived quantities and calibration affect both Bayesian and non-Bayesian workflows. This changes :4.1 and :4.5–4.6. In :5.1 and :5.3 the extra calculation is small and corrects the actual requested probability or workload target. The source does not rank one inferential philosophy above the other, nor validate a particular subject model. Reopen when another construction gives the same target meaning and uncertainty at lower effort, or when changed dependencies defeat the propagation.

**Uncertainty near a parameter boundary.** The serious default is the normal standard-error interval, which collapses in :5.1. **Adopt** binomial tail inversion when its fixed-sample coverage is the requirement; **retain** a posterior alternative when its prior-conditional probability is wanted. [NIST/SEMATECH e-Handbook, §7.2.4.1](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) supplies the explicit comparator and small-sample construction. The few tail calculations cost little here and repair the degenerate result; discreteness can make coverage conservative. A posterior requires the additional prior and can change materially with it. This comparison governs :4.3–4.4 and :5.1, not a universal preference for exact intervals. Reopen for a changed sampling law or a justified approximation that meets the same coverage need more efficiently.

**Inference when observations determine stopping.** **Adapt** simultaneous coverage as a conditional alternative to fixed-time intervals in :4.3. [Howard et al., *Time-uniform, nonparametric, nonasymptotic confidence sequences*, §1 and equation (1), arXiv:1810.08240v9](https://arxiv.org/html/1810.08240v9) supplies the stronger guarantee and its cost in interval width. Its stated stochastic conditions still apply. A fixed-time method remains sufficient for its own observation plan; sequential machinery is unnecessary there. Reopen when the actual stopping rule changes or a narrower valid construction improves the needed inference at comparable effort.

### MMP.13:12 - Relations

- **Uses MMP.7** for the law of recorded outcomes and **MMP.11** for the model family when that family needs construction.
- **Uses MMP.12 and C.16.IR** for unresolved recovery distinctions and sufficient target bounds. Adds estimator or posterior construction and the meaning of inferential uncertainty.
- **Uses CMP.8 and CMP.9** to obtain numerical consequences of the selected inference, with computational error separate from inferential uncertainty.
- **Supplies prediction and model criticism** with conditional consequences that can be compared with relevant observations. A causal interpretation additionally needs its identification argument under C.28.
- **Supplies MMP.8** with estimates or distributions used in a decision; **C.11.DUA** compares the value of further information or computation when needed.
- **Uses B.5.RR** to propagate a changed premise. Method Engineering can use the resulting inference when revising how a working method obtains or interprets records.

### MMP.13:End

## MMP.14 - Find and Repair a Mathematical Model's Failed Predictions

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.14:1 - Problem frame

Use this pattern when a mathematical model's predictions leave a consequential feature of the available observations unexplained, or when a proposed use makes such a discrepancy worth examining. A model may reproduce an overall average while missing conditional responses, bursts, extremes or the records that a selection rule actually permits.

Start with one needed prediction and a feature whose failure would change its use. For overload, compare relevant tails or sequences, not only the fitted mean. Construct that feature under the model on comparable records. The first result can be a localized discrepancy, a repaired calculation, or a sufficient reason to retain a narrower use.

The principal result is a changed model, the assumption changed, and the consequence that must be recalculated. A supported restriction of use or an unresolved choice between repairs can also be the useful result. A small residual is not a certificate of adequacy; a nonzero residual is not automatically a model failure.

This is model criticism within mathematical modeling. MMP.7 supplies the recording law, MMP.11 the available model family, and MMP.13 inference within a stated model. Here the work constructs and interprets comparisons that can change that model. A physical, biological, economic or other subject method supplies the meaning and admissibility of the proposed repair. Predictive improvement alone identifies neither a causal mechanism nor an intervention effect.

Do not reopen an adequate application merely to run a standard collection of diagnostics. An established calculation, bound or checked prediction may already suffice under unchanged conditions. C.11.DUA selects further checking when its possible outcomes can change the answer, claim or warranted use. New observations, model enlargement and simulation are not routine prerequisites.

### MMP.14:2 - Problem

An optimizer can improve fit without repairing the needed prediction. A model can fail a broad diagnostic while retaining a sufficient narrower answer. Apparent disagreement can also come from comparing latent quantities with selected records, numerical approximation, or ordinary model-permitted variation.

Even a real discrepancy rarely names its cause. Large residuals might reflect a missing predictor, varying noise, dependence, selection or an erroneous observation. Wholesale replacement hides the changed assumption; making every observed feature look ordinary can fit chance patterns.

The working problem is to construct a comparison that can expose the relevant mismatch, trace it to a revisable part of the model, and establish what the revision changes without treating reused data or simulated agreement as new external evidence.

### MMP.14:3 - Forces

| Force | Consequence for the method |
| --- | --- |
| Intended use versus overall fit | The discrepancy must retain distinctions on which the receiving prediction depends. |
| Sensitivity versus ordinary variation | A useful diagnostic can reveal systematic failure without declaring every unusual observation erroneous. |
| Localization versus ambiguity | A pattern of failure narrows repairs but often does not uniquely identify the defective assumption. |
| Adaptation versus evaluation | Data used to choose a repair cannot also supply an untouched assessment of that choice. |
| Flexibility versus retained structure | A repair must preserve needed constraints and account for the additional estimation or regularization it introduces. |
| Assurance versus effort | Use available comparisons first; acquire more evidence only for a consequential unresolved claim. |

### MMP.14:4 - Solution

**Choose a consequential discrepancy → construct comparable predictions → locate the mismatch → change the implicated assumption → recalculate and compare the consequence → return the warranted use.**

#### MMP.14:4.1 - Choose the prediction and the discrepancy together

State the receiving quantity and conditions: a response at specified inputs, a probability of exceeding a limit, a distribution of recorded counts, or a forecast for a given horizon and group. Name the relevant observational unit. A message, a batch of messages and a whole operating period support different comparisons.

Recover the model and its observation law. Retain units, inputs, initial conditions, exposure, recording rules and material dependence. Separate unknown parameters from assumptions such as constant response, independent errors or complete recording.

Choose a discrepancy \(D\) that responds to a failure relevant to this use. For example:

- Conditional bias can be exposed by mean residuals within relevant input ranges, rather than a mean over all inputs.
- A tail count \(D(y)=\sum_i 1\{y_i>u\}\) asks whether the model accounts for excursions beyond the consequential level \(u\).
- A run length or \(D(r)=\sum_{i=2}^n r_i r_{i-1}\), with residuals in their actual order, can expose dependence hidden by a histogram.
- A distribution of recorded categories can reveal that predictions concern unfiltered events while observations concern selected records.

A conditional plot, a few statistics or a direct bound can suffice. Explain which repair would change the feature. A statistic that fitting nearly forces to agree, such as the mean in a fitted constant-mean model, usually contributes little to detecting omitted structure.

The user needs the target, conditional distributions or bounds, and the comparison's construction. Obtain a missing calculation from a mathematically qualified collaborator: for example, a record generator and a discrepancy's reference distribution. A human or AI participant may supply it; recover the subject assumptions and interpretation before using its output.

#### MMP.14:4.2 - Generate the comparison the question requires

Compare quantities with the same meaning. Replicated physical states are not yet rounded, censored or selected records. Carry them through MMP.7's recording law.

For a **posterior predictive comparison**, obtain joint parameter draws from MMP.13 and generate records conditionally:
\[
 \theta^{(s)}\sim\pi_M(\theta\mid y,x),\qquad
 y^{\mathrm{rep},(s)}\sim p_M(y^{\mathrm{rep}}\mid x,\theta^{(s)}).
\]
Here \(M\) names the model and \(x\) the retained input and recording conditions. Compare \(D(y)\) with \(D(y^{\mathrm{rep},(s)})\). If the discrepancy depends on parameters, calculate \(D(y,\theta^{(s)})\) and \(D(y^{\mathrm{rep},(s)},\theta^{(s)})\) at the same draw.

Decide what repeats. New observations for existing groups with their inferred effects differ from new groups with regenerated effects. Retain or regenerate effects according to the questioned prediction. Do not independently redraw an effect that should be common to an entire batch.

A **non-Bayesian comparison** can use a specified parameter value, an exact conditional reference distribution that eliminates a nuisance parameter, or a fitted-model simulation. State which is used. When the reference concerns a statistic of a fitted procedure, reproduce the fitting step on each simulated dataset; a simulation that holds its fitted coefficients fixed generally answers a different question. A parametric bootstrap may approximate a reference distribution, not make its calibration exact.

For a **held-out comparison**, construct the forecast without using the records being predicted to fit, tune or select that forecast. Keep preprocessing inside the corresponding training operation. Choose the withheld unit and allowed information for the receiving prediction: new observations in an existing group, a whole new group, or a future block with a specified horizon. A convenient random split does not by itself establish future or new-group performance. An alternative split needs an argument that its bias and variability suffice for the intended conclusion.

Write a held-out predictive law as \(Q_M(y_H\mid y_T,x)\), where \(T\) is the available training information and \(H\) the withheld portion. Compare the models on the same \(H\), target and scoring convention. Use a joint block prediction when the question depends on within-block dependence. Pointwise scores can still answer a declared marginal prediction question; they do not test all joint behavior.

Exact enumeration or algebra may replace simulation. If a deterministic prediction and an observation each have established error bounds, compare their admissible ranges. Disjoint ranges expose an incompatibility under those bounds; overlapping ranges do not prove the model.

#### MMP.14:4.3 - Interpret the difference at the comparison's actual strength

Inspect where discrepancies occur, not just whether one aggregate score changes. Compare direction, size, input region and persistence with the variations that the reference construction permits.

A posterior predictive tail fraction describes a conditional comparison under the fitted model. It is not generally a frequentist p-value with a uniform null distribution. An exact conditional tail probability, a fitted bootstrap approximation and a held-out loss have different interpretations. None is the probability that the model is false.

Account for the construction's resolution when it can change the result. Zero exceedances in finitely many simulations does not establish a zero tail probability. Approximation error, poor sampling or an inaccurate held-out calculation can create an apparent discrepancy. CMP.8/.9 supply the relevant numerical error account. Checking recovery on data generated by the model can expose computational faults; success there does not establish the model's correspondence with the subject.

A pattern found after searching many views remains a useful clue, but its nominal tail area is not automatically calibrated for that search. If a repeated-error guarantee matters, account for the selection or use a suitable untouched comparison. Exploratory diagnosis need not claim that guarantee.

A discrepancy can warrant restricted use, examination of one component, or rejection of a prediction. Failure to expose one means only that this check, at this resolution, has not exposed it.

#### MMP.14:4.4 - Change the part that explains the consequential mismatch

First trace the disputed prediction through its calculation and observation meaning. A wrong unit, event label, numerical solution or censoring convention can require correction without changing the underlying subject relation.

Then formulate a small number of plausible revisions. Show the changed mathematical component and why it can affect the discrepancy:

| Located feature | Possible construction to examine |
| --- | --- |
| Residual means vary with an omitted input | Replace \(m_0(x)\) by \(m_0(x)+b\,h(x)\), with a subject-admissible function \(h\); estimate \(b\) and recalculate the relevant conditional response. |
| Dispersion varies by input while the mean remains adequate | Replace constant error scale by a positive function \(s(x)\); compare conditional spread and the receiving tail probability. |
| Residual sequences have dependence absent from the model | Replace independent errors by a specified covariance or a recurrence such as \(e_t=\rho e_{t-1}+\eta_t\); derive the resulting block or horizon prediction. |
| Available records exclude outcomes the prediction includes | Change the recording or selection component using the established inclusion rule; predict the retained records, keeping the latent law separately visible. |

These are candidates, not conclusions from the symptom alone. Do not delete observations or inflate noise until everything passes. Several changes can reproduce the feature; use subject knowledge and existing discriminating observations to choose, retain conditional alternatives, or return the missing distinction.

Use MMP.11 to preserve support, constraints and known relations when extending the family. Use MMP.13 to infer the revised unknowns; MMP.12 supplies a justified restriction when added flexibility makes recovery unstable. Changed priors, constraints or noise laws can change the answer without adding information to the records.

If the remaining difference is worth a new observation, return the distinguishing prediction and feasible-design question to the applicable observation-design and subject methods. A predictive repair does not identify an intervention effect; obtain the required causal assumptions and identification separately when that is the receiving question. A narrower supported use can finish without either continuation.

#### MMP.14:4.5 - Recalculate the consequence and examine the repair

Recalculate the original discrepancy and the receiving quantity under the revision. Adding a term to an equation leaves both questions unfinished. Show what changes and what remains unchanged.

Compare with the previous model and a serious sufficient alternative on the same available basis. A simpler model can be preferable when its retained result suffices and the added component contributes only estimation noise or cost. A better average score can coexist with a worse consequential tail or subgroup prediction; inspect that conflict directly.

Distinguish **repair construction** from **assessment of the repaired prediction**. Reproducing the data that motivated the revision shows what the revision accommodates. An untouched set of suitable existing records can assess a forecast fixed before those records are inspected. When repeated tuning consumes that set, it becomes part of development. If the needed performance claim concerns the whole adaptive procedure, its assessment must include that adaptation, for example through a suitable outer split; it is not a test of one retrospectively selected fit.

Fresh observations are not the only useful continuation. Recalculate with available held-out records, derive the affected consequence, retain a conditional result or restrict use. C.11.DUA determines whether resolving the remaining limitation is worth its cost. Do not describe an unperformed comparison as successful.

#### MMP.14:4.6 - Return the model and its changed use

Return the changed relation or distribution, retained assumptions, relevant comparison, and consequence to use or recalculate. Include ambiguity where it affects use. A short explained calculation can suffice.

For a methodological use, return which discrepancy reveals the omitted distinction, how to produce comparable predictions, and which component to reconsider. For an unresolved subject use, identify the missing contribution instead of a generic demand for more data.

Recognition starts with a consequential disagreement. Assurance depends on the claim: algebra establishes a recalculated consequence; a computational check establishes its numerical execution; an appropriate comparison with observations supports the bounded subject use. Reopen when the target, regime, recording law, relevant evidence or consequential error requirement changes.

### MMP.14:5 - Archetypal Grounding

The following are constructed cases. Their arithmetic demonstrates the method; the stated observations are example inputs, not reports of empirical studies.

#### MMP.14:5.1 - A correct overall mean conceals failed conditional predictions

Two message routes, A and B, are used under ordinary load. The target is the chance of timely delivery for each known route. In this small example every message has a complete binary record, the deadline is unchanged, and outcomes are assumed independent with a stable probability within each route and load regime.

The supplied records are partitioned before fitting. Only the fitting and diagnostic portions are opened during model construction; the assessment portion remains withheld until the revised forecasts are fixed.

| Portion | A: timely / total | B: timely / total |
| --- | --- | --- |
| Fitting | 8 / 10 | 2 / 10 |
| Diagnostic | 9 / 10 | 1 / 10 |
| Withheld assessment | 8 / 10 | 2 / 10 |

The original model \(M_0\) ignores route: \(Y_i\sim\mathrm{Bernoulli}(p)\). Its maximum-likelihood estimate from the fitting portion is \(\hat p=1/2\). Its expected diagnostic total equals the observed total: 10 timely deliveries out of 20. That agreement does not answer the route-specific question.

Choose \(D=|K_A/10-K_B/10|\), where \(K_A,K_B\) are the timely counts in the diagnostic portion. Observed \(D=0.8\). Under the common-probability model, condition on the observed total \(K_A+K_B=10\). Then
\[
 P(K_A=k\mid K_A+K_B=10,M_0)
   =\frac{\binom{10}{k}\binom{10}{10-k}}{\binom{20}{10}}.
\]
This reference retains the two sample sizes and removes the unknown common \(p\). The exact two-sided tail for \(D\ge0.8\) is
\[
 \frac{2(1+100)}{184756}
 =\frac{101}{92378}\approx0.001093.
\]
It exposes a discrepancy in the common-probability account under its independence and stability assumptions. It does not identify a causal route effect. A shared disturbance confounded with route could demand a different repair.

Suppose the subject account permits route-specific response probabilities. Construct \(M_1\): \(Y_i\mid g_i\sim\mathrm{Bernoulli}(p_{g_i})\). Using the same fitting records gives \(\hat p_A=0.8,\hat p_B=0.2\). The changed component is the relation between the known route and the response probability, not the binary recording rule.

Recalculate the original discrepancy under the fitted \(M_1\), retaining the same total of 10. Conditional replicate counts have weights
\[
 w_k=\binom{10}{k}^{2}16^k,\qquad
 P(K_A=k\mid K_A+K_B=10,\hat M_1)=w_k/\sum_{j=0}^{10}w_j,
\]
where \(16=(0.8/0.2)/(0.2/0.8)\) is the fitted odds ratio. Summing \(k=0,1,9,10\) gives \(P(D\ge0.8)=0.37348\). The revised point model accommodates the diagnostic contrast. This calculation is conditional on its fitted probabilities; it neither calibrates a test of the estimated family nor independently confirms the repair.

Fix these point-probability forecasts and open the assessment portion. The sum of log probabilities of its 20 individual outcomes, using natural logarithms, is
\[
 L_0=20\log(0.5)=-13.86294,\qquad
 L_1=16\log(0.8)+4\log(0.2)=-10.00805.
\]
Thus \(M_1\)'s fixed forecasts gain \(3.85490\) on this portion. This is an observed paired comparison, not a guaranteed future gain or a parameter-uncertainty interval. The diagnostic portion was used to propose the repair; it was not counted as untouched assessment.

For three future independent A messages under the same regime, the point forecast of at least one late delivery changes from \(1-0.5^3=0.875\) to \(1-0.8^3=0.488\). That receiving calculation must change. If uncertainty about the probabilities matters, MMP.13 must propagate it; the point calculation does not already do so.

**Changed condition.** The supplied operating condition now specifies high load. Before any refitting, a supplied high-load batch has 5/10 timely outcomes on each route. The ordinary-load forecasts give
\[
 L_1^{H}=10\log(0.8)+10\log(0.2)=-18.32581,
\]
whereas the common \(0.5\) forecast still gives \(-13.86294\). Carrying over the repaired forecast loses \(4.46287\) on this batch. The earlier assessment concerned ordinary load and does not establish transfer. Keep that use boundary and examine invariance if a high-load forecast is needed. A high-load common-rate fit of \(0.5\) is a possible new model; its fit here is not an untouched assessment. Its three-message late-delivery forecast would again be \(0.875\), conditional on that rate and independence.

For the narrower question of expected timely deliveries with equal numbers of A and B under ordinary load, both fitted models give one half of the total. If only that expectation is needed and its basis suffices, this case does not require adopting the richer model or obtaining new observations. It does not make the two models' conditional or joint predictions equivalent.

#### MMP.14:5.2 - Repair the law of the exported records

A candidate latency model assigns \(X\) uniformly to the integer values 1 through 6. An export contains only values 1, 2 and 3. Comparing these records with unconditional replications of \(X\) suggests too few large values.

The documented export rule, supplied independently of that discrepancy, retains a record only when \(X\le3\). The failed comparison omitted selection. Compose the candidate event law with the actual rule:
\[
 P(R=j\mid\mathrm{retained})
 =\frac{P(X=j)}{P(X\le3)}=\frac13,\quad j=1,2,3.
\]
The predicted mean of exported values is 2, not 3.5. Their probability of exceeding 2 is \(1/3\), not \(2/3\). Construct comparable replications by applying the same filter, or draw directly from this conditional law. Do not reduce the latent model's tail merely to make the unfiltered comparison agree.

If the documented export cutoff changes to 4, the corresponding mean becomes 2.5 and the probability of an exported value exceeding 2 becomes \(1/2\), with no alteration to the candidate uniform latent law. These are recalculated consequences of the changed recording rule, not new empirical confirmation of that law.

Agreement within the retained range does not establish the distribution among unrecorded values. If the target is only the distribution of exported records, that unresolved tail may be irrelevant. If the target needs latent large-latency probabilities, return the missing information or assumption through MMP.12/C.16.IR; the selection correction has not recovered it.

#### MMP.14:5.3 - A failed numerical prediction need not require a new subject model

A normalized quantity is modeled by \(u'(t)=-u(t)\), \(u(0)=1\). A record at \(t=1\) is \(0.370\), with an established absolute recording error at most \(0.005\). A forward-Euler computation with step \(h=1\) predicts 0.

Before replacing the decay law, compare the numerical result with the model's exact consequence \(u(1)=e^{-1}\approx0.367879\). Euler steps \(h=1/2\) and \(h=1/4\) give \(0.25\) and \(0.316406\); the sequence of approximations exposes a material computational error. The exact value lies in the observed admissible interval \([0.365,0.375]\). Here the repair belongs to CMP.8, while this observation supplies no reason to change the decay relation.

That interval overlap establishes compatibility for this record under the error bound, not the correctness of the decay model at every time. If a relevant observation instead excludes the accurately computed consequence, the subject relation or observation account becomes live again. Numerically precise evaluation and adequate subject prediction remain separate achievements.

### MMP.14:6 - Bias-Annotation

Familiar diagnostics favor failures that are easy to display. Aggregate scores can hide sparse but consequential regimes; selecting the most striking plot can exaggerate ordinary variation. A preferred causal story can make one repair appear uniquely compelled when several produce the same records.

Preserve the intended use, the role of each data portion and the compatible alternatives. Do not transfer support to unrepresented conditions.

### MMP.14:7 - Conformance Checklist

- The questioned prediction and a discrepancy that can change its use are recoverable.
- Observed and predicted quantities share the relevant inputs, recording meaning, unit and dependence conditions.
- The replication, conditioning or withholding construction supports the interpretation actually claimed.
- Computational error and ordinary model-permitted variation have not been silently treated as subject-model failure.
- A proposed repair names the changed mathematical component and its subject basis; unresolved alternatives remain visible where consequential.
- The receiving consequence has been recalculated, and the role of data reused during repair is stated where it limits assessment.
- The result gives a warranted use, restriction or missing contribution, without imposing new evidence acquisition on a sufficient existing answer.

### MMP.14:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Fit the overall mean and infer adequacy for every conditional forecast | Compare the feature on which the receiving use depends. |
| Call every residual an error in the model | Compare with the model's permitted variation and relevant numerical or recording error. |
| Simulate latent states and compare them with selected records | Pass replications through the actual recording law. |
| Treat a predictive tail fraction as the probability that the model is wrong | Retain the reference distribution and its actual probability statement. |
| Tune repeatedly on a “test” set and report an untouched test result | Treat that set as development data; qualify or separately assess the adaptive procedure. |
| Replace an inconvenient observation or inflate noise until a check passes | Examine the observation basis and competing model components; preserve legitimate unusual outcomes. |
| Improve prediction and claim the causal explanation is established | Retain the predictive claim; obtain identification and subject grounds for the causal claim. |
| Require a new experiment after every mismatch | Use C.11.DUA to choose among available repair, narrower use, conditional continuation and worthwhile inquiry. |

### MMP.14:9 - Consequences

The practitioner can replace “the model fits badly” with a calculable failed prediction and an explicit revised assumption. Downstream users can see which consequence changes, which remains sufficient, and which use is unsupported.

Comparable predictions cost work. Adaptive repair consumes assessment information, and extra parameters can weaken estimation. Improving one feature can leave another failure unresolved. Retain the use boundary without demanding exhaustive criticism of every model.

### MMP.14:10 - Architectural Rationale

B.5.TC aligns competing accounts; B.5.RR carries a changed premise into its consequences. Neither alone constructs a conditional discrepancy distribution, a predictive replication or a withholding scheme. Those mathematical operations provide the contribution here.

MMP.13 determines inference under a model. This method examines where that model fails a needed prediction and changes a component before inference is repeated. MMP.7 prevents a change in recording from being mistaken for a change in the subject. MMP.11 supplies admissible replacement relations, while the subject method determines what those relations purport to represent.

The cases separate a missing conditional relation, a missing selection rule and an inaccurate computation.

### MMP.14:11 - SoTA-Echoing

**Working question.** How can a practitioner find the model component that spoils a needed prediction and repair it without confusing better fit, statistical surprise and external confirmation?

**Selected line.** Combine discrepancy-directed predictive criticism with evaluation appropriate to the intended prediction. Use an exact conditional comparison, fitted simulation, posterior replication or held-out prediction according to the claim. No inferential framework wins independently of the question.

- Gelman, Vehtari and McElreath, [*Statistical Workflow*](https://sites.stat.columbia.edu/gelman/research/published/Statistical_Workflow_article.pdf), §§1.7–1.8 and 1.10–1.11. The text used is the author manuscript dated 5 December 2025 for the 2026 article, not the publisher's typeset version. Its operative contributions here are localizing misfit through predictive comparisons, understanding changes through related models, and separating computational calibration from subject adequacy. Adopt those in :4.3–:4.5. Adapt the wider workflow to a consequential local question; fitting increasingly flexible models until no anomaly remains can absorb legitimate rare patterns.
- [Stan User's Guide 2.39, “Posterior and Prior Predictive Checks”](https://mc-stan.org/docs/stan-users-guide/posterior-predictive-checks.html), posterior checks, discrepancy statistics and mixed hierarchical replication. Adopt the explicit replicated-data construction and the choice of what is regenerated in :4.2. Retain the limitation that a posterior predictive tail fraction is not generally a classically calibrated p-value. A statistic largely determined by fitting can miss the omitted structure. The Bayesian construction is one available comparison, not a requirement to replace an exact conditional or sufficient deterministic argument.
- Aki Vehtari, [*Cross-validation FAQ*](https://avehtari.github.io/modelselection/CV-FAQ.html), online version consulted 16 September 2026, §§3, 5 and 7–11. Adopt its separation of the prediction task, partition and loss in :4.2/:4.5, and its treatment of selection-induced bias. The closest task-matching split is a useful starting point, not an unconditional optimum: alternative partitions can trade bias for variance. Held-out performance can compare predictions without identifying the component that needs revision.

**Serious alternatives on the same question.** In :5.1, optimizing and checking the pooled fit costs less and answers the expected-total question. It fails to expose the conditional discrepancy relevant to forecasting an A message. A held-out log-score comparison of the two fixed forecasts supplies useful performance evidence on the supplied assessment portion, but the score alone does not explain what relation to change. The chosen construction adds the route contrast and a conditional reference, then compares the explicit repair on that same predictive question. It costs an additional fitted probability and leaves uncertainty and regime transfer unresolved; it is not superior for a target already supplied by the pooled expectation.

Reopen the choice when the target becomes a new group, a different horizon, a tail or an intervention; when dependence or selection changes; or when the error requirement makes an approximate comparison insufficient. A more elaborate model or checking scheme earns its place through the new question, not through its recency.

### MMP.14:12 - Relations

- **B.5.TC / B.5.RR:** align accounts and revise dependent reasoning; this method supplies the model-criticism constructions.
- **MMP.7:** constructs the law of recorded data used for comparable predictions and repairs to selection or measurement assumptions.
- **MMP.11 / MMP.10:** supply admissible model families and constraint formulations when the failed prediction requires a changed relation.
- **MMP.13 / MMP.12 / C.16.IR:** supply inference, regularized recovery and the limits of what records resolve; a repaired fit does not remove those limits.
- **CMP.8 / CMP.9 / MATH.20:** obtain predictions and discrepancy calculations with the relevant numerical error or bound.
- **Causal-identification and observation-design methods:** receive the unresolved causal effect or distinguishing-observation question when it matters. Obtain these contributions from a suitable subject source or collaborator.
- **C.11.DUA and the subject method:** select worthwhile checking and establish the subject meaning of a repair. The receiving practice uses the revised prediction or restriction.

### MMP.14:End

## MMP.15 - Identify an Intervention Effect from Available Data

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.15:1 - Problem frame

**Use this when** the work asks what changing an action, operating condition or working method would do, and available observations or experiments might already determine the answer. A fitted association, even a precise one, does not by itself say what would happen under that change. Start by writing the intervention and the quantity needed, then ask which available probability laws and causal assumptions can determine it.

The practical gain is an expression that can be estimated from the available records, a useful bound, or an explanation of the remaining ambiguity. Identification can spare an unnecessary experiment or prevent an unsupported intervention claim.

This is a method of mathematical modeling within causal reasoning. It constructs the connection from available laws to an intervention target. C.28.MR supplies the meaning and consequences of replacing a mechanism in a given causal model; here the model's relevant mechanisms may remain unknown. Subject methods must justify what the intervention changes, which influences may be shared, and which relations remain applicable. The method applies to physical, biological and computational systems and to human or AI working methods.

Preparation requires conditional probability, expectation and the ability to follow a mathematical argument about assumed causal relations. For graphical derivations, the practitioner or an available specialist must be able to check which paths remain open under conditioning and intervention. A specialist contribution must return the target, assumptions, required observable quantities and derivation or obstruction; a software answer alone is insufficient.

Do not reconstruct identification when an applicable result already answers the unchanged question. Use MMP.13 for estimation under an already identified expression, and C.28.MR for a consequence inside a fully supplied causal model. Design another experiment only when the existing result is insufficient and further evidence is worth obtaining. For a question about the same observed case under another action, or a joint or nested comparison of its responses, MMP.19 constructs the common-case relation and determines what the available information fixes.

### MMP.15:2 - Problem

Several causal models can produce the same observable distribution and different intervention consequences. Selection adds another limitation: an experiment can identify an effect among its participants without identifying the effect in the receiving population.

The task is to determine whether the requested causal quantity follows from the available laws and stated assumptions. Failure to find an adjustment set is not failure of identification. Fitting, choosing a prior or simulating one compatible mechanism does not prove that all compatible models give the same answer.

### MMP.15:3 - Forces

- **The requested effect versus an unnecessarily complete model.** An average contrast may be determined while individual responses or the full intervention distribution remain unknown.
- **Usable assumptions versus attractive fit.** Temporal ordering, excluded pathways and invariance across populations carry causal meaning that goodness of fit cannot supply.
- **Available information versus convenient information.** Separate experimental, selected and population laws cannot be treated as one complete joint distribution without a derivation.
- **Simple sufficient construction versus broader search.** Adjustment is often enough. Mediated identification or a general identification algorithm can succeed where adjustment does not, at the cost of additional structural reasoning.
- **A conditional answer versus another investigation.** An explicit bound or assumption-dependent result may already suffice. New observations must answer an unresolved consequential question.

### MMP.15:4 - Solution

Define the target, recover the available laws and describe the admitted causal models. Derive a common expression for their intervention consequence, or demonstrate how they disagree. Limit the returned conclusion to what that argument establishes.

#### MMP.15:4.1 - Specify the causal quantity and what counts as the same intervention

For an action level \(a\), let \(Y(a)\) denote the outcome under the specified intervention setting the action to \(a\). For a target population \(T\), a common request is

\[
\mu_a=E_T[Y(a)], \qquad \Delta=\mu_1-\mu_0.
\]

Define the action, comparator, outcome, population and time horizon far enough to distinguish the actual question. A contrast of average outcomes differs from the chance that a particular unit would benefit. Identifying both marginal laws of \(Y(1)\) and \(Y(0)\) does not ordinarily identify their joint law or the distribution of individual differences.

Establish consistency: for a unit actually receiving the specified version of action \(a\), its observed outcome agrees with \(Y(a)\). Different doses, implementations or accompanying actions may give the same label different meanings. If one unit's outcome depends on other units' actions, represent the relevant joint assignment or policy; the notation \(Y(a)\) must not silently discard that dependence.

For static interventions, \(P(Y\mid do(A=a))\) denotes the corresponding intervention law. C.28.MR defines the change of mechanism that gives this notation its meaning. Identification below seeks that law or its required function without assuming all the changed model's numerical mechanisms are already known.

#### MMP.15:4.2 - Recover the available laws and the admissible causal models

Use MMP.7 to recover how records arise. With inclusion indicator \(S\), selected records supply a law such as \(P(A,Y,L\mid S=1)\), not automatically \(P(A,Y,L)\). Keep assignment, actual action, measurement and inclusion distinct when those distinctions affect the target. State which variables were jointly observed, which interventions were performed, and which population each source concerns.

For identification, provisionally treat these population laws as known. This asks what unlimited data of those kinds could determine. MMP.13 handles finite-sample estimation.

Describe the admitted causal relations. An acyclic causal graph is a useful representation: directed arrows allow direct causal influence, and a shared unobserved cause can be represented explicitly or by a bidirected edge. The absence of an arrow excludes a possible influence relative to the represented variables. A good observational fit does not justify that exclusion. Time-indexed variables can express feedback across time; a theorem for acyclic graphs must not be applied unchanged to an equilibrium model with unresolved cycles.

The operative identification test is this: whenever two admitted causal models induce the same available laws, must they give the same requested quantity? If the assumptions themselves conflict with the available laws, return that conflict rather than declaring a result identified through an empty model class.

#### MMP.15:4.3 - Derive an expression, using the simplest sufficient route

Begin with a relation that replaces an unobserved intervention quantity by available quantities under an explicit assumption. Then combine it with ordinary conditioning, multiplication and averaging. Every final factor must come from an available law or an earlier justified step. Displayed sums concern discrete variables; for continuous or mixed variables, average against their actual probability laws.

For example, let \(L\) be measured before action. For a mean effect in the same population as the data, suppose that within each relevant \(L=l\), action assignment does not select a different mean potential outcome:

\[
E[Y(a)\mid L=l]=E[Y(a)\mid A=a,L=l].
\]

This mean exchangeability assumption, consistency and positive probability of each required action in the relevant strata give

\[
\mu_a
=\sum_l E[Y(a)\mid L=l]P(L=l)
=\sum_l E[Y\mid A=a,L=l]P(L=l).
\]

The first equality averages over the target strata. The second uses exchangeability to compare the same potential outcome, then consistency to replace it by an observed outcome. Average both actions with the same target weights. The different distributions \(P(L\mid A=a)\) generally answer an association question instead.

A common graphical justification is the back-door criterion: choose pretreatment variables that block every path into \(A\) capable of linking it to \(Y\) through other causes. In checking a path, conditioning on an intermediate non-collider blocks it; a collider, where two arrowheads meet, blocks it unless that collider or a descendant is conditioned on. Thus adding every available covariate can open a path rather than remove bias. This criterion is sufficient, not the only way to justify adjustment or identify an effect.

When adjustment of \(A\)'s effect is unavailable, derive other observable intermediate quantities. In a simple front-door construction, a measured mediator \(M\) carries every directed path from \(A\) to \(Y\); \(A\) to \(M\) has no open back-door path; and conditioning on \(A\) blocks all back-door paths from \(M\) to \(Y\). Under these conditions and the required support,

\[
P(Y=y\mid do(A=a))
=\sum_m P(M=m\mid A=a)
   \sum_{a'} P(Y=y\mid M=m,A=a')P(A=a').
\]

The outer factor identifies the effect of action on the mediator. The inner adjustment identifies the outcome law under intervention on the mediator. The pathway restrictions license combining them for the action's total effect. Merely including a post-action measurement in a regression does not perform this construction. These classical conditions are sufficient; their failure does not establish that this functional or another identifying expression is impossible. [Front-door criteria and their extension](https://arxiv.org/html/2604.15288v1), §§2.1.5–3.

For a more involved graph or several input laws, derive a sequence of intermediate distributions using the rules of do-calculus and probability. Each exchange between observation and intervention needs the corresponding separation condition in the modified graph. A suitable identification implementation can carry out that search: provide the graph, the target and the actual input laws, then recover the returned derivation and check its required factors. The historical ID algorithm covers a specified acyclic model class with latent common causes and an observed joint law; generalized search can use several incomplete or experimental laws. Do not replace those inputs by a joint law that the records never supplied. [ID algorithm](https://ftp.cs.ucla.edu/pub/stat_ser/r327.pdf), Figure 3; [generalized search](https://arxiv.org/html/1902.01073v5), §§2–3.

#### MMP.15:4.4 - Carry selection, transport and support through the expression

Identify which population supplies every average. For example, an experiment in \(S=1\) may supply action-specific outcome means by pretreatment \(L\), while an existing inventory supplies the target distribution \(P_T(L)\). If the intervention has the same meaning, assignment in the experiment is exchangeable, and the conditional potential-outcome means agree between the experimental and target populations, then

\[
\mu_a=\sum_l E[Y\mid A=a,L=l,S=1]P_T(L=l).
\]

This is a transport assumption followed by trial identification and target averaging. It requires trial coverage and both action levels wherever the target gives relevant weight. Equal variable names, similar marginal distributions, or randomization within the experiment do not establish the transport assumption. Selection after action or outcome requires its own recording and causal argument; it cannot automatically use this pretreatment bridge. [Generalizing trial results](https://arxiv.org/html/1709.04589v2), §§3–4.

Inspect the support needed by the chosen expression. Positivity means that a required conditional law is defined on the relevant target support; in the discrete adjustment example, \(P(A=a\mid L=l)>0\) whenever the target weights that stratum. For continuous variables, use the corresponding support condition. A fixed intervention value in a continuous action space may also need a continuity or other structural restriction: the observed law determines conditional responses only almost everywhere. An empty cell in a small sample does not prove a population probability is zero. A known structural exclusion is different: the missing conditional response cannot be learned there from that source.

Failure of support invalidates that expression at the excluded values. Another source, another identifying argument or an explicit structural restriction may still answer the question. Extrapolation through a response model can produce an assumption-dependent answer, but fitting or regularizing that model does not create observations at the missing support.

#### MMP.15:4.5 - Distinguish a proof of ambiguity from an unfinished search

To demonstrate nonidentifiability, construct two causal models satisfying the stated assumptions, reproducing all the available laws, and giving different values of the requested target. C.28.MR can calculate each model's intervention consequence. Show both the observational agreement and the difference after intervention, as in :5.2.

A complete identification algorithm can also return an obstruction; check its class and query. A time limit or exhausted search without an applicable completeness result leaves the derivation unresolved. Failure to identify a full intervention distribution also does not by itself prove failure to identify a particular mean or contrast. [ID completeness](https://ftp.cs.ucla.edu/pub/stat_ser/r327.pdf); [scope of search completeness](https://arxiv.org/html/1902.01073v5), §3.4.

When a point is not identified, use the assumptions to bound the requested quantity. Optimize it over compatible models, or derive an inequality valid for all of them. One compatible example establishes possibility; it does not establish a bound. If a bound is claimed sharp, show that compatible models attain or approach its endpoints. A bound that already settles the receiving question needs no complete reconstruction of unknown mechanisms.

A prior or added restriction may select among compatible answers; retain that dependence. It is not new evidence.

#### MMP.15:4.6 - Return the sufficient result and propagate consequential changes

Return the target and the assumptions under which its identifying expression, bound or ambiguity result holds. Make the data factors recoverable for estimation and uncertainty under MMP.13. Numerical evaluation belongs to an appropriate computational method; a completed optimization or simulation is not an identification proof.

Check the derivation as needed: verify a finite case, inspect a disputed graph condition, or calculate a countermodel's observational and intervention laws. These checks establish the mathematical consequence of assumptions. Assurance that the assumptions describe the subject requires relevant subject evidence; successful fitting or self-consistent simulation does not provide it by itself.

When an actual change admits a direct pathway, changes an intervention's version, alters selection, or changes the target population, propagate it through the affected derivation and calculation. Compare an alternative assumption when that comparison can change the intended use. Do not invent a sensitivity exercise for an already sufficient result under unchanged conditions.

C.11.DUA selects whether remaining uncertainty warrants more evidence, an explicitly conditional answer, a narrower agreed question or no further work. MMP.16 can design an observation if that further work is chosen. A mathematical identification result does not authorize or physically carry out the intervention.

### MMP.15:5 - Archetypal Grounding

These constructed population probabilities make the calculations inspectable; they are not empirical results. Each case assumes fixed intervention meanings and no interference between its units. Finite records add estimation uncertainty to the assumption dependence shown here.

#### MMP.15:5.1 - Separate a production action from the batches receiving it

A production team asks whether enabling a stabilization mode \(A=1\), rather than \(A=0\), increases the probability of a conforming item \(Y=1\). Incoming batch condition \(L\) is recorded before mode selection. Half the target batches have \(L=0\), half \(L=1\). Mode 1 is used on 80% of \(L=0\) batches and 20% of \(L=1\) batches.

| Batch condition | \(P(Y=1\mid A=0,L)\) | \(P(Y=1\mid A=1,L)\) |
| --- | --- | --- |
| \(L=0\) | 0.10 | 0.20 |
| \(L=1\) | 0.70 | 0.80 |

The subject account asserts consistency and mean exchangeability given \(L\); both modes occur in both strata. Adjustment therefore gives \(\mu_0=0.5(0.10)+0.5(0.70)=0.40\), \(\mu_1=0.5(0.20)+0.5(0.80)=0.50\), and \(\Delta=0.10\).

The selected groups instead give \(E[Y\mid A=1]=0.8(0.20)+0.2(0.80)=0.32\) and \(E[Y\mid A=0]=0.2(0.10)+0.8(0.70)=0.58\): an association of \(-0.26\). Its sign differs because the two modes receive different batch mixtures.

This positive average effect is conditional on the causal account; the table does not prove exchangeability. An already supported account and sufficient estimate need no new experiment.

#### MMP.15:5.2 - Use a mediator, then withdraw a pathway exclusion

A service's command \(A\) can activate a retry mechanism \(M\), which affects successful completion \(Y\). Unrecorded load can affect both command selection and completion. The initial causal account permits \(A\to M\to Y\) and an unobserved common cause of \(A,Y\), but no other arrows: in particular, no direct effect of \(A\) on \(Y\) and no hidden common cause of \(A,M\) or \(M,Y\).

All three variables are binary. The available joint law has \(P(A=1)=0.5\), \(P(M=1\mid A=0)=0.25\), \(P(M=1\mid A=1)=0.75\), and:

| Mediator and command | \(P(Y=1\mid M,A)\) |
| --- | --- |
| \(M=0,A=0\) | 0.10 |
| \(M=1,A=0\) | 0.70 |
| \(M=0,A=1\) | 0.30 |
| \(M=1,A=1\) | 0.90 |

There is no observed pretreatment adjustment variable for the shared load. The front-door conditions nevertheless hold. First adjust the mediator's effect over \(A\): the inner means are \(h(0)=0.5(0.10)+0.5(0.30)=0.20\) and \(h(1)=0.5(0.70)+0.5(0.90)=0.80\). Then average over the mediator law induced by each command:

\[
\mu_0=0.75(0.20)+0.25(0.80)=0.35,\qquad
\mu_1=0.25(0.20)+0.75(0.80)=0.65.
\]

Thus \(\Delta=0.30\). Directly comparing observed commands instead gives \(0.75-0.25=0.50\).

**Changed condition.** Inspection of the service reveals that the command can also change completion through a path bypassing retry. The revised account permits a direct \(A\to Y\) arrow. Retaining the previous formula is no longer justified.

The same full observational law now admits at least two answers. To demonstrate this, let unobserved \(U\) be a fair binary variable, let observational command selection be \(A=U\), and generate \(M\) with probability \(0.25+0.50A\) using independent random variation. In two alternative models, generate completion with respective probabilities

\[
\text{Model I: }0.10+0.60M+0.20U,\qquad
\text{Model II: }0.10+0.60M+0.20A,
\]

using a further independent random draw. Every probability lies between zero and one. Because \(A=U\) observationally, both models give every cell of the supplied joint law.

Under \(do(A=a)\), \(U\) remains fair. Model I gives \(\mu_0=0.35,\mu_1=0.65\); Model II gives \(\mu_0=0.25,\mu_1=0.75\). Their effects are 0.30 and 0.50. Both satisfy the revised account, which permits the listed influences without requiring every permitted influence to be nonzero. Model II was excluded by the original no-direct-effect premise.

This is a proof that the revised assumptions and available law do not identify the average effect. These are ambiguity witnesses, not discovered service mechanisms. More precise estimation of the same law cannot distinguish them. A substantive restriction might; further evidence is chosen by its value for the use.

#### MMP.15:5.3 - Transfer an experiment to another mixture of sites

An ecological model asks for the effect of a specified irrigation change \(A\) on establishment of a seedling \(Y\), averaged across a target collection of sites. Soil stratum \(L\) is known from an existing inventory. A selected experiment randomized both irrigation levels within each stratum, recorded every outcome, and used the same irrigation implementations as the target question.

Suppose the subject account supports equality of conditional potential-outcome means between experimental and target sites. Experimental sites are 80% \(L=0\) and 20% \(L=1\); the target inventory is 25% \(L=0\) and 75% \(L=1\).

| Soil stratum | Experimental mean under \(A=0\) | Experimental mean under \(A=1\) | Difference |
| --- | --- | --- | --- |
| \(L=0\) | 0.20 | 0.50 | 0.30 |
| \(L=1\) | 0.60 | 0.70 | 0.10 |

The experimental average effect is \(0.8(0.30)+0.2(0.10)=0.26\). The target means are \(\mu_0=0.25(0.20)+0.75(0.60)=0.50\) and \(\mu_1=0.25(0.50)+0.75(0.70)=0.65\). The requested effect is 0.15. Randomization identifies the comparisons inside the experiment; the transport assumption and target inventory justify the different outer average.

Now suppose the source is found to contain experimental outcomes only for \(L=0\); the supplied \(L=1\) values were extrapolations, with no justified response relation supporting them. Retain the target inventory and transport within the covered stratum. With no outcome restriction for \(L=1\) beyond binary outcomes, its mean effect \(\delta_1\) lies in \([-1,1]\). Therefore

\[
\Delta=0.25(0.30)+0.75\delta_1\in[-0.675,0.825].
\]

The endpoints are attainable by making every uncovered site respectively harmed or helped: \((Y(0),Y(1))=(1,0)\) or \((0,1)\). Those choices do not alter any available experimental outcome. The bound is sharp under these assumptions, and the sign of the target effect is not identified. The effect 0.30 remains available for the covered stratum if that is the agreed receiving question; it must not silently replace the original population target.

### MMP.15:6 - Bias-Annotation

Predictive success invites reading inputs as controls. Readily measured variables invite unjustified adjustment, while unmeasured common causes disappear for lack of a data column. Construct the causal account from the subject process.

Failure of a familiar criterion can instead encourage unnecessary data collection. Search more broadly when the answer matters, preserving unresolved search as unresolved. Check that calculation has not substituted a convenient population or intervention version for the requested one.

### MMP.15:7 - Conformance Checklist

- The intervention, comparator and receiving quantity are defined, with consistency and interference handled where relevant.
- The derivation uses the laws actually supplied by the recording and selection procedures.
- Every causal substitution has an assumption or applicable graphical argument; every final data factor is available on its required support.
- A nonidentifiability claim has a target-matched witness or applicable complete-method obstruction. An unfinished search is reported separately.
- A returned bound is justified for all compatible cases; sharpness is claimed only with an attainability argument.
- Estimation uncertainty, causal assumption dependence and computational approximation retain their different meanings.
- Actual consequential changes are propagated. A sufficient existing result does not trigger an obligatory new study.

These conditions recognize a constructed identification result. They do not establish the subject truth of its causal assumptions or authorize an intervention.

### MMP.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Consequence | Repair |
| --- | --- | --- |
| Change a predictor value and call the prediction an effect | Conditions on naturally selected cases rather than specifying an intervention | Define the intervention target and derive its relation to the available law |
| Adjust for every recorded variable | Can block part of the requested effect or open a collider path | Justify the selected variables for that target |
| Treat no adjustment set as nonidentifiability | Misses mediated or other identifying constructions | Seek a justified broader derivation or a real obstruction |
| Pool experimental, selected and target records as one population | Changes the probability law behind the expression | Retain source conditions and derive the transport or selection correction |
| Fill unsupported cells by regression and claim data-only identification | Hides extrapolation assumptions | State the additional response restriction or return a bound |
| Treat a prior, fitted mechanism or simulation as fresh causal evidence | Conceals disagreement among compatible causal models | Show which assumption selected the answer and what the records distinguish |

### MMP.15:9 - Consequences

Estimation concentrates on the required observable quantities. Nonidentifiability becomes an explicit limitation of assumptions and information, not an unexplained numerical failure.

The causal argument may demand subject knowledge unavailable in the dataset. More elaborate identification does not strengthen an unjustified premise. A conditional answer or bound can be useful without recovering every mechanism.

In methodology, this changes how a proposed improvement to a working method is assessed. Define the method change and relevant outcome, recover how cases and results were recorded, and distinguish its effect from differences in which cases received it. The same reasoning can govern a human procedure, an automated procedure or their combination, without making a population experiment mandatory for every use of the method.

### MMP.15:10 - Architectural Rationale

Mechanism replacement gives intervention semantics within a model. Identification adds a different construction: showing that the needed intervention consequence is common to the causal models compatible with available laws and assumptions, or exposing where it is not.

The target-first construction avoids demanding a complete causal model when a mean, contrast or bound suffices. Separating derivation from estimation lets one identifying expression support different appropriate inferential methods. Separating source laws prevents mathematical convenience from turning selected records into information about an unobserved population.

### MMP.15:11 - SoTA-Echoing

The governing question is whether the available laws and defensible causal assumptions determine the requested intervention quantity. A serious default is justified covariate adjustment; another is to fit a response model and predict after changing its action input. Adjustment is retained when it supplies a valid, economical derivation. Prediction under a fitted response model is accepted as an intervention answer only when its structural assumptions identify that meaning.

**Historical completeness anchor.** Shpitser and Pearl, *Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models* (AAAI 2006, UCLA report R-327), Figure 3 and the soundness/completeness argument, supply an algorithm that can return an expression or a graphical obstruction in its specified model class. This supports :4.3 and :4.5: failure of adjustment is not the general stopping rule, and a negative algorithmic result requires the matching completeness conditions. The result is not a universal certificate for cyclic, selected or otherwise differently specified models. [Source](https://ftp.cs.ucla.edu/pub/stat_ser/r327.pdf).

**Several available laws rather than an invented joint law.** Tikka, Hyttinen and Karvanen, *Causal Effect Identification from Multiple Incomplete Data Sources: A General Search-based Approach* (2021; arXiv v5, 27 August 2021), §§2–3.4, develops do-search by retaining known distributions and deriving new ones with justified rules. This is adopted in :4.2–:4.3 when one adjustment formula or one complete observational law does not fit the information actually available. Its broader search costs more than a sufficient specialized derivation; its negative output has only the completeness scope established for the problem being solved. [Read version](https://arxiv.org/html/1902.01073v5).

**Current extension of a familiar sufficient criterion.** Wu and Robeva, *Generalization of Pearl's Front-Door Criterion* (arXiv v1, 16 April 2026), §3, gives weaker sufficient graphical conditions for the same front-door functional and worked derivations outside the classical criterion. This reinforces the broader derivation route in :4.3 instead of rejecting an effect merely because a familiar criterion fails. The simple case in :5.2 needs only the classical sufficient conditions. The newer result concerns a particular functional in its stated graphical setting; it neither removes the need for subject justification nor supplies a complete test for every causal target. [Read version](https://arxiv.org/html/2604.15288v1).

**Population scope is part of identification.** Dahabreh and colleagues, *Generalizing causal inferences from individuals in randomized trials to all trial-eligible individuals* (2019; arXiv v2, 29 October 2019), §§2–4, separates within-trial exchangeability from the conditional-mean and participation assumptions required for generalization. That distinction is adapted in :4.4 and :5.3: the target mixture can differ even when the experimental comparisons are valid. Its particular nested-trial setup is not presumed for arbitrary selected records. [Read version](https://arxiv.org/html/1709.04589v2).

Reopen the chosen derivation when the target, available laws, causal exclusions, population bridge or support changes. Consider a different identification method when it answers the same question under more defensible assumptions or with materially less effort; source recency alone does not require replacing an already sufficient argument.

### MMP.15:12 - Relations

- **C.28** supplies the causal-use question and the distinction between identification, estimation and realizability. **C.28.MR** supplies intervention semantics and calculations within a specified causal model.
- **C.16.IR** supplies compatible-case and sufficient-target reasoning; this pattern constructs the causal identification expressions and ambiguity witnesses.
- **MMP.7** supplies the observation law, including selection and missingness. **MMP.11** supplies an explicit model family when its restrictions are needed.
- **MMP.12** handles inverse ambiguity and justified regularization. A restriction used here remains an added causal or response assumption, not new evidence.
- **MMP.13** constructs inference for the identified expression or explicitly assumption-dependent target. **MMP.14** investigates failed model predictions; observational checks alone need not distinguish observationally equivalent causal models.
- **MMP.19** constructs and bounds history-conditioned, joint and nested counterfactual comparisons; an intervention mean can remain sufficient for a choice based on expected outcome.
- **MMP.16** addresses a chosen need for additional observation design. **C.11.DUA** governs whether that work is worthwhile.
- **Computational Thinking**, including **CMP.8/CMP.9** where their numerical methods apply, obtains numerical values without supplying the missing causal argument. Subject methods justify and realize the intervention and the asserted invariances.

### MMP.15:End

## MMP.19 - Construct and Bound a Mathematical Counterfactual Comparison under a Causal Model

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MMP.19:1 - Problem frame

Use this pattern when the question concerns the same case under another action, a joint comparison of its possible responses, or a specified pathway through which a change would act. A population average may be available while the case-specific or pathway question remains unanswered.

Start with the intended use, the observations about the case or population, and a causal account of the relevant mechanisms. Construct what remains common across the alternatives, carry factual information into that construction and calculate the consequence or range it supports. A useful first result can be two compatible models that give different answers: the supplied information then leaves this distinction unresolved.

The mathematical prerequisites are function evaluation and the probability operations used in the chosen construction. A qualified contributor can supply them. The meaning of the variables, observations and interventions still needs subject knowledge. Small finite cases can be calculated by hand.

For a population intervention effect, use MMP.15 and C.28.MR directly. A choice maximizing expected realized outcome under each action can also need only those intervention distributions, conditional on the information available before acting. Constructing a joint counterfactual law is useful when the receiving question actually depends on it.

### MMP.19:2 - Problem

An intervention distribution describes results across the selected population. Information about an observed case can select different underlying conditions. Reusing the population distribution then answers another question.

There is also a difference between knowing each alternative's distribution and knowing how their results correspond for the same unit. Two causal accounts can agree on every available observation and intervention yet disagree about whether this unit would have succeeded under both actions. Independent simulation of the two distributions silently chooses one such correspondence.

A pathway question adds another dependency: a variable may be set to the value it would have had under a different action. Substituting its population mean can erase the case relation that the question needs.

### MMP.19:3 - Forces

| Force | Consequence for construction |
| --- | --- |
| Case information and population variation | Infer the case's conditions under the factual account before changing its mechanisms. |
| Marginal agreement and joint ambiguity | Recover or bound the dependence across alternatives when the target uses it. |
| Mechanistic detail and obtainable information | A supplied model can determine a conditional consequence that the data alone do not identify. |
| Pathway meaning and interactions | State which nested comparison is intended; different decompositions can answer different questions. |
| Useful decisions and unresolved counterfactuals | A sufficient action comparison may finish without recovering the whole joint law. |

### MMP.19:4 - Solution

**Specify the comparison → construct the common case → use its factual information → evaluate the alternative mechanisms → identify or bound the target → return the consequence to use.**

#### MMP.19:4.1 - State what the comparison must answer

Name the unit, relevant time and population. State the action or mechanism alternatives and what would count as their outcomes. C.28 distinguishes the causal-use question; C.28.MR supplies the meaning of mechanism replacement.

Distinguish the targets that the question could need. Common examples are a mean under an intervention, the response under another action given what happened to this case, and a joint property such as succeeding under one action while failing under another. For a pathway question, name which mechanism's input is to be changed and which other route remains as specified.

Recover what the recipient will do with the answer. A future choice based on expected outcome and action cost can depend only on each action's marginal distribution. A probability of benefit, an explanation of an observed result or a nested pathway contrast can depend on more. C.11 and MMP.8 retain the decision criterion; the mathematical construction must answer that criterion rather than substituting another one.

#### MMP.19:4.2 - Construct one common basis for the alternatives

In a structural model, write the relevant variables as functions of their parents and underlying inputs U. Recover the joint law p(u), given input values, or a set of admissible input laws and mechanisms. U can include shared disturbances and persistent characteristics; its meaning depends on the subject account.

For each action a, let Y_a(u) denote the output of the modified model at the same underlying input u. A response-type representation can instead give a joint vector such as (Y_0,Y_1) directly. Its joint distribution states which responses belong to the same modeled unit. Having the two marginal distributions alone does not supply this dependence.

Keep common conditions common, and identify which changes the action itself causes. Two runs with independently drawn U describe different modeled cases. Reusing a random seed is a numerical way to implement a specified coupling; the seed does not justify that coupling in the subject. Repeating work later with changed conditions likewise needs an account of which inputs persist and which are newly drawn.

Use a model with well-defined responses for the requested inputs. In the finite acyclic case, evaluation in dependency order suffices. Continuous, cyclic or multiple-solution models require their own existence and solution-selection conditions; a solver's returned trace does not settle an unspecified response relation.

#### MMP.19:4.3 - Infer case conditions from the factual observations

Let e denote the available factual record. Use the model and recording procedure that produced it, including the actual action regime. MMP.7 constructs the recording law; MMP.13 supplies the needed conditioning.

For a finite supplied input law and record likelihood k(e given u), form

```text
w(u given e) = k(e given u) p(u) / sum_v k(e given v) p(v).
```

The denominator must be positive. An exact deterministic record has a likelihood of one for compatible inputs and zero for incompatible ones. A noisy or selected record needs its actual likelihood. An individually observed continuous value uses the appropriate conditional distribution or density, not division by the probability of a zero-probability point.

This operation uses the factual mechanisms. Conditioning after replacing them can select a different set of cases. If the supplied account cannot produce the record, return the conflict; changing an assumed mechanism or observation model is a separate justified repair.

A probability law need not be invented when only possible inputs are supported. Retain the inputs compatible with the record and derive the range of responses they permit. If there is no factual conditioning in the query, use the selected population law or set directly.

#### MMP.19:4.4 - Evaluate the compared responses with that common basis

Replace the selected mechanisms using C.28.MR. At each retained u, evaluate all the responses needed by the question before averaging. For a finite conditional comparison,

```text
P(Y_a=y, Y_b=z given e)
    = sum_u w(u given e) 1[Y_a(u)=y and Y_b(u)=z].
```

Here the indicator is one when both conditions hold. A single response or expected difference uses the corresponding function inside the same sum. The shared u preserves the modeled relation between alternatives. Use integration when the model supports a continuous version of this operation.

For a nested response Y_(a,M_b)(u), first compute the intermediate value M_b(u) under b. In the second model set A to a and M to that computed value for the same u, then evaluate Y. Averaging M_b before this replacement generally changes the target. The construction defines a model consequence even when no available physical procedure can jointly realize every term; C.28:4.5 governs a separate claim about obtaining samples.

For a pathway decomposition, state both component contrasts and verify that their sum is the intended total. Interactions can make another choice of reference mechanism give different components. A component's numerical size does not by itself establish the adequacy of the explanation or the feasibility of a proposed physical intervention.

#### MMP.19:4.5 - Determine what the available information fixes

A fully supplied model gives a consequence conditional on that model. Identification asks whether all admissible models agreeing with the available information give the same target. Use MMP.15's distinction between a proof of ambiguity and an unfinished search on the counterfactual construction now specified.

Two compatible models with different target values prove non-identification under their shared assumptions and available laws. More samples from those same laws cannot distinguish them. A narrower quantity can nevertheless be identified.

For a finite response-type construction, assign a nonnegative mass to each admitted type, with total mass one. Express the known marginal, joint and regime laws as constraints on those masses. Add a structural restriction only when the causal account supports it. Minimize and maximize the target over the compatible masses; for a conditional probability retain its conditioning denominator. MMP.10 helps formulate the constraints and an appropriate computational method can solve them.

Call the resulting bounds tight only when the construction establishes that no smaller range follows and that its extremes are attainable, or specifies unattained limiting extremes. A numerical search that finds two values supplies witnesses, not necessarily the full range. Uncertainty from estimating an input law with finite data is another layer, handled by MMP.13; it is not the same as ambiguity remaining even when that law is known.

#### MMP.19:4.6 - Use a sufficient consequence and reopen the affected assumption

Return the target's meaning, the supported value or range, and the assumptions that determine its use. The calculation can already carry these facts; a separate record is needed only by a receiving use.

If every compatible answer supports the same sufficient action or explanation, use that result. If the distinction matters, identify what would change it: a defensible restriction on mechanisms, informative existing records, a feasible different observation, or a different question. MMP.16 and C.11.DUA compare the value and burden of obtaining that contribution. Unavailable evidence can leave a bounded answer and a choice under uncertainty.

A revised recording rule changes the factual conditioning. A revised intervention changes the response functions. A changed criterion can make joint dependence irrelevant. Recalculate the affected contribution while retaining the rest.

During an investigation, this construction can perform its mathematical-modeling contribution while conditioning and mechanism evaluation supply constituent Methods. The investigator or subject specialist supplies the case and causal interpretation; a mathematical or AI collaborator may supply the calculation. Availability of one contribution leaves the others to be obtained where the work needs them.

### MMP.19:5 - Archetypal Grounding

These are constructed cases with supplied mechanisms or exact probability laws. They demonstrate the mathematical operations and limits, not empirical effectiveness.

#### MMP.19:5.1 - Change the route for an already observed processing case

A routing model gives latency in ticks as Y=2A+U. Route A=1 adds two ticks; residual latency U is 0 or 1 with equal probability. The recorded case used A=1 and had Y=3.

Under the factual equation only U=1 is compatible. Keeping that input and replacing the route by A=0 gives Y_0=1. Drawing a fresh U from the population instead gives mean latency 1/2. That is a new-case mean, not the requested alternative for the observed case.

If the record is noisy, use its likelihood rather than selecting U with certainty. If an exact Y=4 is reported under the unchanged model, neither admitted U is compatible; return the conflict instead of calculating a posterior with zero denominator. Whether the same residual condition would persist under a real route change is a subject premise of this model.

#### MMP.19:5.2 - Expose a coupling that experiments do not determine

Let a randomized binary action A be independent of the response type U=(Y_0,Y_1). Consider two possible type distributions:

| Type (Y_0,Y_1) | Model S | Model T |
| --- | ---: | ---: |
| (0,0) | 3/8 | 1/8 |
| (0,1) | 1/8 | 3/8 |
| (1,0) | 1/8 | 3/8 |
| (1,1) | 3/8 | 1/8 |

Each action succeeds with probability 1/2 in both models. With a fair random assignment, all four observed (A,Y) combinations have probability 1/4 in each model.

For a case observed with A=1,Y=1, only types (0,1) and (1,1) remain. In S, the probability that it would also succeed under A=0 is (3/8)/(1/2)=3/4. In T it is (1/8)/(1/2)=1/4. Both models fit the supplied observational and intervention laws, so these laws do not identify the answer.

For a future choice scored only by expected success, the actions tie at 1/2 under both models. If A=1 adds a positive cost and no other consequence, A=0 is sufficient for that criterion. Resolving the counterfactual ambiguity would not improve this choice.

#### MMP.19:5.3 - Bound benefit without inventing a joint law

Suppose binary success probabilities under actions 1 and 0 are p1=7/10 and p0=2/5. Let b=P(Y_0=0,Y_1=1), the probability of succeeding only under action 1. The four type masses must be

```text
P(0,1)=b                 P(1,1)=p1-b
P(1,0)=p0-p1+b           P(0,0)=1-p0-b.
```

Nonnegativity gives max(0,p1-p0) <= b <= min(p1,1-p0), hence 3/10 <= b <= 3/5. At b=3/10 the masses in order (00,01,10,11) are (3/10,3/10,0,2/5); at b=3/5 they are (0,3/5,3/10,1/10). Both attain the supplied marginals, establishing the bounds for this unrestricted response-type class.

Now suppose assignment A is independent of the response pair (Y_0,Y_1), P(A=1)>0, and a case is observed with A=1,Y=1. The probability that this case would fail under action 0 is P(Y_0=0 given A=1,Y=1)=b/p1, hence between 3/7 and 6/7. Conditioning retains the types with Y_1=1; the independent assignment probability cancels from numerator and denominator. The same endpoint distributions attain these conditional bounds, since their denominator is the fixed positive p1=7/10.

The mean effect is p1-p0=3/10 in every compatible model. An expected-success criterion with an action-1 cost of 1/10 therefore has net gain 1/5 without identifying b. A criterion that explicitly requires b to exceed 2/5 remains unsettled by these bounds.

If subject knowledge warrants that action 1 never changes a success into failure, P(1,0)=0 fixes b=3/10. That is an additional monotonicity assumption; it was not learned from the two marginal probabilities.

#### MMP.19:5.4 - State which mediated contrast is being calculated

Take the supplied mechanisms M=A+U and Y=3A+2M+AM, with U=0 or 1. Compare actions 0 and 1 for the same u. The total change is 6+u.

First retain the mediator at M_0=u while changing A: Y_(1,M_0)-Y_(0,M_0)=3+u. Then change the mediator to M_1=1+u while retaining A=1: Y_(1,M_1)-Y_(1,M_0)=3. The components sum to 6+u.

Reversing that decomposition gives mediator change 2 at A=0, followed by direct change 4+u at M_1. These components also sum to 6+u. The interaction AM makes the two decompositions different. A request for “the part caused through M” must select its intended contrast. Knowing the total effect alone supplies neither decomposition; observing data that identify it is a further question.

### MMP.19:6 - Bias-Annotation

The explicit examples use finite inputs and simple structural functions. Their transparency helps inspect a comparison but does not show that such a causal account is obtainable for every subject. Subject ambiguity can remain after a numerical method computes a definite answer.

The same-unit relation is part of the model. Its appropriateness in a physical, organizational or human setting depends on what is held common and what each action changes. A purely numerical pairing can be useful for variance reduction while lacking the interpretation required by the causal question.

### MMP.19:7 - Conformance Checklist

- The target states the unit, alternatives, relevant factual information and receiving use.
- Common conditions and changed mechanisms have a subject interpretation.
- Factual conditioning uses the factual mechanism and recording law.
- Joint or nested responses use the specified common-case dependence.
- A model-conditional calculation is distinguished from identification across admissible models.
- An ambiguity or bound is returned at its proved scope, with estimation uncertainty kept distinct.
- A sufficient action can finish without recovering an irrelevant joint law.

### MMP.19:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Use the population input law after receiving information about the case. | Condition under the factual account before evaluating its alternative response. |
| Independently simulate two marginals and interpret the pairs as the same units. | Construct or bound the joint response law the interpretation needs. |
| Replace a nested intermediate value by its population mean. | Compute the intermediate response for each common input before evaluating the outer mechanism. |
| Report a uniquely identified answer because one chosen model yields a number. | Examine the target across the admissible models, or report the result as conditional on that model. |
| Demand a benefit probability for a choice determined by expected outcomes. | Recover the criterion and use the sufficient marginal comparison. |

### MMP.19:9 - Consequences

The recipient obtains a comparison whose case relation and assumptions can be inspected, changed and used. A proved range exposes what remains unresolved without replacing the result by a generic request for more data.

Constructing a common causal account and solving its constraints has a cost. Its value depends on whether the joint, conditional or pathway distinction changes the explanation or decision. An intervention mean or conditional outcome prediction can remain the sufficient result.

### MMP.19:10 - Architectural Rationale

The hard step is often the relation between calculations, rather than each calculation separately. Ordinary conditioning recovers case information; mechanism replacement constructs an alternative; the common input or response-type law connects them. Maintaining that relation permits a joint question and exposes assumptions invisible in separate marginal fits.

The same construction supports historical explanation, probabilities of benefit and nested pathways. Their targets remain distinct. In particular, a decision based on realized outcomes can use less structure than a question about how those outcomes would differ for the same unit.

### MMP.19:11 - SoTA-Echoing

[Correa and Bareinboim (2025)](https://proceedings.mlr.press/v267/correa25a.html), Definitions 1.1–1.3 and §2.1.1, supply the shared-input and nested-response semantics used in :4.2–:4.4. The finite examples here use those definitions; the richer graphical calculus has further conditions and operations.

[Mueller and Pearl (2023)](https://ftp.cs.ucla.edu/pub/stat_ser/r513.pdf) separate average effects from probabilities of benefit or harm. [Dawid and Senn (2025, v2)](https://arxiv.org/pdf/2301.11976), §§2–4, supply a serious alternative: intervention distributions suffice for maximizing expected realized outcomes under the stated information and constraints. Adopt the target distinction in :4.1/:4.6. In :5.2 the same two models require a joint account for the historical question but no such recovery for the stated future choice. The changed question justifies the more elaborate construction.

[Raghavan and Bareinboim (2026, preprint)](https://arxiv.org/html/2602.23541v1), §§2 and 4–5, distinguish identification, partial identification and physically realizable counterfactual sampling. Adapt those distinctions in :4.4–:4.5. Their available-action, finite recursive and positivity assumptions limit the algorithmic results. Establishing a model consequence leaves its physical sampling conditions to be established separately when sampling is needed.

Reopen the selected construction when a supported additional mechanism or information source changes the compatible comparisons, or when another method obtains the required answer with less unsupported structure or burden. The worked finite constructions establish their stated mathematical consequences; practical validity still depends on the subject account.

### MMP.19:12 - Relations

- **C.28** governs causal-use questions and support; **C.28.MR** constructs mechanism replacements and their consequences.
- **MMP.7/.13** supplies the recording and inferential operations used to recover factual case information. **MMP.15** identifies intervention effects from available laws and supplies the identification/ambiguity distinction reused here.
- **MMP.10** formulates compatible response-type constraints. **MMP.16** constructs a worthwhile distinguishing observation; **MMP.14** repairs an account contradicted by appropriate records.
- **MMP.8/.8.SD**, **C.11** and **C.11.DUA** connect the consequence to choice, continuation and proportionate further inquiry. **EXD.1** recovers what connection an explanation must supply.

### MMP.19:End

## MMP.16 - Design Observations to Separate Mathematical Model Alternatives

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.16:1 - Problem frame

Use this pattern when several mathematical accounts remain possible and the next useful answer depends on a difference between them. You can choose which cases to observe, under which conditions, or how to record them. The difficulty is to find an attainable observation that exposes the relevant difference.

The desired result may be a better decision, a supported prediction, a distinction between proposed mechanisms, or a new research direction. For example, two response laws agree at all previously tried inputs but imply different behavior in the intended use. Repeating those inputs more accurately may leave the disagreement untouched.

This pattern constructs the mathematical design of an observation. It returns what to observe, what records the alternatives would produce, and how those records would change the answer. It can instead return a useful limitation: the available observation choices leave the needed distinction unresolved. The subject practice supplies feasible access and performs the observation; PHY.9 and PHY.10 do that work for a physical readout and test.

Start with the receiving question, the alternative models and the observation law from MMP.7. Set-valued reasoning needs functions and sets. Probabilistic design also needs conditional probability and the inferential meaning chosen in MMP.13. An analyst can supply that mathematics while another participant supplies the observing conditions and interprets the result.

Use the present answer directly when the remaining alternatives make no consequential difference. A new observation is only one possible response to uncertainty. C.11.DUA supplies the comparison with using what is already known, changing the claim or taking another feasible step. A routine prescribed measurement with an already sufficient design needs no new design study.

### MMP.16:2 - Problem

A model can predict a large difference that the actual record cannot show. An instrument may saturate, a log may aggregate away timing, or an unknown offset may account for the apparent difference. Conversely, overlapping distributions can still support a useful distinction; requiring one observation to identify the model without error can reject worthwhile designs.

An observation can also be highly informative about something irrelevant to the requested result. Choosing a design by parameter uncertainty, fit or model label can therefore direct effort away from the question that made the modeling useful.

The problem is to construct a feasible observation whose possible records support a consequential comparison, with the uncertainty and cost that this use can tolerate.

### MMP.16:3 - Forces

| Force | Tension |
| --- | --- |
| Visible contrast and recorded contrast | Models can disagree about an unobserved quantity while predicting the same available record. |
| Model identity and receiving result | Different models may support the same answer; a single model family may contain the important disagreement. |
| Discrimination and uncertainty | One certain separating observation is attractive, but useful statistical distinctions often retain error. |
| Informative design and model adequacy | A design can be excellent within an inadequate model family. |
| Learning and available work | A better distinction can cost more time, access or computation than its contribution warrants. |
| Immediate gain and continued inquiry | One observation may prepare a later useful test without answering the final question itself. |

### MMP.16:4 - Solution

State the disagreement that matters. Derive the records each alternative can produce under feasible observation choices. Construct a comparison of those records that improves the receiving answer, and compare the attainable benefit with the work involved. Obtain the selected observation only when that comparison supports it; otherwise use the present result or change the question or access.

#### MMP.16:4.1 - Locate the consequential disagreement

Write the answer that would differ. It may be a threshold response, a predicted event, an intervention consequence or which conjecture to develop next. For a numerical target, write it as q(h,theta), where h selects a model and theta contains its remaining unknowns. Different theta within one model can matter as much as different model labels.

Recover what the present observations and assumptions leave possible. MMP.11 constructs the family of models; MMP.12 exposes a recovery ambiguity; MMP.13 supplies probabilistic conclusions when used. Group equivalent parameterizations by the behavior relevant to this question.

Ask which remaining disagreements change the intended answer or a worthwhile later inquiry. If all retained alternatives already support the same sufficient answer, return it.

#### MMP.16:4.2 - Construct the law of the obtainable records

Let d denote a feasible design: the selected inputs or cases, preparation, observing times and recording procedure. For each alternative derive either:

- a set R(h,theta,d) of possible records under its bounded uncertainties; or
- a probability law P(Y | h,theta,d) for the records Y.

The record includes what the procedure would actually retain. Compose the modeled response with the selection, measurement, censoring, rounding or aggregation operation. If an intervention changes the subject, derive its response under that intervention; an observational association alone supplies no such law.

Keep unknowns shared across readings shared. An unknown calibration offset cannot take one arbitrary value for the first reading and an unrelated value for the next if the same offset governs both. A repeated observation can reduce independent noise while leaving that common ambiguity intact.

A probabilistic comparison integrates unknowns only under a supplied probability law. Otherwise retain them as conditional possibilities or compare performance across their admitted range. Choosing a convenient nuisance value separately for each model can make a design look more discriminating than it is.

For an adaptive design, later observation choices are functions of records already available. Derive their joint law with that dependence. A sequence of fixed-design calculations does not by itself describe an outcome-dependent stopping or sampling rule.

#### MMP.16:4.3 - Find what a design can distinguish

First seek a simple consequential contrast. For a set-valued model, take the union of R(h,theta,d) over the remaining possible theta. Disjoint unions for two alternatives give a separating observation under those assumptions. If the unions overlap, identify records that would settle the needed distinction and records that would leave it open.

Equal sets alone do not establish equal statistical information: probability laws can weight the same possible records differently. In a probabilistic model, compare the full record laws or a statistic whose retained information suffices for the requested result. Distinct means are one possible contrast, not a universal criterion.

An impossibility conclusion needs its scope. Two alternatives that give the same record law under every currently feasible design, yet different required answers, demonstrate a distinction unavailable through those designs. More repetitions under the same uninformative access do not resolve it. Changing the observation type, access or target may do so. Failure of a numerical search to find a good design establishes only that search result.

A narrower target can remain obtainable. Suppose all feasible records leave the individual parameters unresolved, but every compatible parameter pair gives the same total response. Return the total when it answers the work question. Recovering each parameter is then unnecessary.

#### MMP.16:4.4 - Construct the design criterion from the receiving use

For a required distinction with controlled statistical error, construct a rule T(Y) that returns the answer or an unresolved result. For example, let two specified hypotheses have record densities p0(y;d) and p1(y;d) relative to the same measure. For a chosen threshold c, the rule selects H1 on the region A={y: p1(y;d)>c*p0(y;d)} and H0 otherwise. Calculate P0(A), the chance of selecting H1 under H0, and P1(A-complement), the opposite error. Compare designs and thresholds that meet the required error bound. For a composite hypothesis, the claimed protection across its parameter range requires controlling the error across that range, rather than only at a fitted value.

Other decision rules can retain an unresolved answer when that is useful. Their comparison likewise follows from their record laws and the error consequences the use requires.

When probability, actions and losses are appropriate, let pi be the current joint law of the unknowns, a an available action, and L(a,h,theta) its loss. For a finite set of action choices and an observation that changes information alone, compare:

~~~
R0 = min_a E_pi[L(a,h,theta)]

R(d) = E_Y[min_a E[L(a,h,theta) | Y,d]]

value of sample information = R0 - R(d).
~~~

The inner choice uses the observed record; the outer expectation averages records that are still unknown when the design is chosen. In this formulation the recipient can ignore the record and retain the old action, so R(d) cannot exceed R0 under the same model. Subtracting the full cost of obtaining and using the information can still make the proposal unattractive. :5.2 carries out the calculation.

If the experiment itself changes the state, available actions or their consequences, include those effects in the decision model. The simple information-only comparison above is then insufficient. MMP.8.SD constructs the continuing state, information and consequence model.

An information criterion is another branch. For a selected unknown Q, expected information gain is the mutual information I(Q;Y | d) under the supplied joint law. Choosing Q as the model label, all parameters or a wanted prediction defines different design problems. Use this criterion when resolving that uncertainty serves the stated inquiry. It does not measure every practical consequence of the observation.

The comparison need not be a probability calculation. A guaranteed separation, an ordinal improvement, or a change in attainable answers can suffice. Use the existing FPF choice and portfolio methods when several gains and burdens remain incomparable. This pattern supplies the modeled observation consequences, not a new general system for valuing research.

#### MMP.16:4.5 - Construct and compare attainable designs

Use the contrast to generate alternatives: observe where responses differ, resolve an omitted component, vary an input independently, measure at a different scale or time, or change how the record is made. Derive the resulting record laws before optimizing a convenient proxy.

For a small set of designs, calculate the selected criterion directly. For a large set, use the applicable search or numerical method from Computational Thinking. Count the cost of evaluating a design as part of the work. If approximate criteria cannot reliably order close candidates, return that uncertainty, retain several designs, or refine the calculation where a changed ranking matters.

Compare against using current information. C.11.DUA governs the attainable contribution, delay, displaced work and any disputed evidence demand. When an information-only design has a bound on its possible benefit below its cost, that bound can end the comparison without computing its criterion more accurately.

For a sequence of observations, decide whether the immediate comparison represents the intended horizon. An apparently uninformative first step may enable a later separating observation. Construct that continuation with MMP.8.SD when it changes the choice; do not require a full sequential optimization for a sufficient one-step design.

#### MMP.16:4.6 - Use the result and reopen the implicated assumption

Return enough for the observation to be performed and interpreted: the selected conditions, records to retain, comparison rule, and the consequence of an unresolved or conflicting result. A design calculation remains a prediction about possible records; it is not an observation already obtained.

After observing, use the inference and comparison that match the actual procedure. If access, stopping or recording changed, revise the affected law before interpreting the result. For example, replacing a numerical readout by a threshold alarm changes the available distinction.

Model discrimination compares the alternatives supplied. If every alternative fails to explain an important record, MMP.14 returns to the relevant subject or observation assumption. Selecting the least poor alternative can support a limited approximation, but its winning score alone does not establish adequacy.

Where the intended use covers different conditions from the selected observations, carry that difference into the receiving prediction. Recent work on active learning under model misspecification shows why concentrating observations for parameter information can worsen prediction elsewhere. Compare alternative observation regions or model families when this vulnerability can change the design or receiving prediction.

### MMP.16:5 - Archetypal Grounding

The cases use stipulated models and costs so that the design can be reconstructed. They demonstrate the method, not reports of performed experiments.

#### MMP.16:5.1 - The largest response difference disappears in the readout

A team has two candidate response laws for a calibrated device assumed valid over the input range 0 to 2:

- H1: y=x;
- H2: y=x^2.

Both agree at the previously inspected inputs 0 and 1. The team needs to know whether the modeled response at x=2 is below or above 3. The laws answer differently: 2 and 4. Their applicability across the range is an assumption supplied for this case.

With a numerical readout r=y+e and a known error bound -0.1 <= e <= 0.1, the design x=2 gives:

| Design | H1 records | H2 records | Consequence |
| --- | --- | --- | --- |
| x=2, numerical readout | [1.9,2.1] | [3.9,4.1] | Disjoint intervals separate the alternatives. |

Now recover a missed feature of the actual instrument: it saturates at 1. Its record is r=min(1,y+e). At x=2 both alternatives always record 1. The large latent response difference gives no distinction at all.

Changing the input to x=0.5 yields:

| Design | H1 records | H2 records | Consequence |
| --- | --- | --- | --- |
| x=0.5, saturating readout | [0.4,0.6] | [0.15,0.35] | Both ranges lie below saturation and are disjoint. |

This design separates the supplied alternatives without replacing the instrument. A record 0.27 retains H2; a record 0.52 retains H1. A record 0.37 fits neither under the given error bound, so it reopens the response or observing assumptions rather than forcing a label.

The result at x=0.5 supports the answer at x=2 through the supplied response families. If those families were justified only up to x=1, this design would not establish the requested extrapolation. The next work would concern that range extension or access to a suitable direct observation.

If the only available inputs were 0 and 1 and the record error law were the same under both accounts, the available designs would not separate them. That conclusion concerns the stated access; it does not say the response question is unanswerable under every possible instrument.

#### MMP.16:5.2 - A useful signal is still too costly

A service team must choose one of two recovery procedures. It models two possible failure modes H0 and H1 with current probabilities 0.5 each. The loss is remaining recovery time, in hours:

| Procedure | H0 | H1 |
| --- | --- | --- |
| A | 0 | 10 |
| B | 4 | 0 |

With current information, expected losses are 5 for A and 2 for B. The team chooses B.

A proposed diagnostic produces either "+" or "-". Its supplied law is P(+ | H1)=0.8 and P(+ | H0)=0.2. Each signal has marginal probability 0.5. Bayes conditioning gives P(H1 | +)=0.8 and P(H1 | -)=0.2.

After "+", A has expected loss 8 and B has 0.8, so the team chooses B. After "-", A has expected loss 2 and B has 3.2, so it chooses A. Expected loss with the signal, excluding diagnostic cost, is therefore:

~~~
R(d) = 0.5*0.8 + 0.5*2 = 1.4 hours.
R0 - R(d) = 2 - 1.4 = 0.6 hours.
~~~

If obtaining, interpreting and waiting for the diagnostic adds 0.7 hours to recovery, its total expected loss is 2.1 hours; using current information is better under these conditions. At an all-inclusive cost of 0.2 hours, the diagnostic gives 1.6 hours and improves the choice. The example assumes the diagnostic does not change the failure mode or the two procedures.

A different test might reveal a device identifier perfectly. If that identifier is independent of the failure mode and losses in this model, its information gain about the identifier does not reduce this recovery loss. Selecting all available uncertainty as the target would misdirect the design.

Now change the current probability of H1 to 0.95. The "-" posterior is 0.19/(0.19+0.04), approximately 0.826, and the "+" posterior is 0.76/(0.76+0.01), approximately 0.987. B remains the better procedure after either result. The diagnostic still changes beliefs about the mode, but its sample-information value for this particular choice is zero.

A later method-development investigation could use the same signal for another target, such as learning how failure modes arise. That research value needs its own question and horizon; the zero above applies to the specified recovery choice.

### MMP.16:6 - Bias-Annotation

The worked cases make the candidate models and observing conditions unusually explicit. In practice, deriving the record law can be the hardest contribution. The mathematical design must retain uncertainty about that law rather than quietly treating a convenient simulator as the subject.

A small named model set also favors choosing a winner. Keep the possibility that all proposed accounts fail the receiving use. Conversely, do not turn that possibility into a demand for an unlimited search for alternatives: pursue it when a discrepancy or consequential vulnerability makes it useful.

### MMP.16:7 - Conformance Checklist

A constructed design supports its intended use when:

- the remaining disagreement and the answer it could change are identifiable;
- its predicted records follow from the alternatives and the actual selection and recording procedure;
- shared unknowns and adaptive choices retain their dependencies;
- the claimed separation, error property or expected improvement follows from a reconstructible comparison;
- any criterion based on information names the unknown being learned and its receiving use;
- feasibility and burden are compared at the scope needed for the decision, using present information as an available alternative;
- the result explains how the selected records change the answer and when an incompatible record returns to the model or observation assumptions.

These conditions concern the mathematical design and its stated assumptions. They do not establish that the observation was performed, that its subject assumptions hold, or that access is authorized. Stronger assurance belongs to the actual intended use.

### MMP.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Maximize a difference before deriving the record | Saturation, selection or aggregation can erase it | Compare the obtainable records, as in :5.1 |
| Demand disjoint supports for every useful test | Discards informative but uncertain observations | Construct the required error or decision comparison |
| Average away an unknown without a probability basis | Hides the assumption deciding which design looks best | Retain conditional cases or supply the probability law |
| Maximize information about every model parameter | Can favor learning that leaves the receiving question unchanged | Select the target or consequences that matter |
| Treat the best candidate as an adequate account | A closed comparison can select a poor explanation of the subject | Use a consequential mismatch to reopen the family |
| Require new data whenever models disagree | Spends effort even when the answer is already sufficient | Compare with the attainable use of current information |
| Interpret an adaptive sample as if it were fixed in advance | Can invalidate the claimed uncertainty or error property | Derive the law for the actual choices and stopping rule |

### MMP.16:9 - Consequences

The next observation becomes a constructed part of modeling: a specified change in available information with a stated consequence. A no-separation result can redirect effort from repeated measurement to a different readout, access route or question.

Good designs depend on assumptions about records and their use. A computed optimum can change when the observer, cost, model family or research horizon changes. For expensive searches, a sufficient feasible design may be more useful than a more precisely optimized proposal.

In methodology, the same construction helps compare alternative accounts of a working method. Choose a case or observation that makes their consequential disagreement visible. Human and automated procedures can both be studied this way; the subject method supplies what can be changed and observed.

### MMP.16:10 - Architectural Rationale

The general contribution is the construction of discriminating observations from models and their receiving use. It is separate from performing a physical test, deriving an estimator after observations, or choosing among all possible projects.

Separating the predicted response from its recording prevents a mathematical contrast from being mistaken for an observable one. Separating information from decision consequence lets exploratory research retain its own value while avoiding an automatic demand for more evidence in ordinary work.

The deterministic and probabilistic branches share that construction. Their guarantees differ, so the pattern does not reduce every use to one statistical test or one information metric. Existing FPF choice, resource and improvement methods receive the consequences produced here.

### MMP.16:11 - SoTA-Echoing

**Design according to its goal.** Huan, Jagalur and Marzouk, *Optimal experimental design: Formulations and computations* (Acta Numerica, 2024), §2.2 and the goal-oriented and model-discrimination formulations, distinguish information targets and decision utilities. The adopted contribution is the explicit selection of what an observation should improve in :4.4. A design maximizing information about every parameter is a serious default when that is the actual aim; it is replaced when the receiving target differs. Numerical optimization methods are delegated to the applicable computational construction. [Source](https://arxiv.org/html/2407.16212v1).

**Information that can change a decision.** Heath and colleagues, *Simulating Study Data to Support Expected Value of Sample Information Calculations: A Tutorial* (2022), “Background and Notation,” gives the pre-observation comparison of decisions after possible records. Its loss-form equivalent is used in :4.4 and the original recovery example in :5.2. The model's costs and consequences must describe the receiving work; the source's health-economic conventions are not generalized into mandatory monetary valuation. [Source](https://journals.sagepub.com/doi/10.1177/0272989X211026292).

**An informative design can misdirect learning.** Tang, Sloman and Kaski, *Representative, Informative, and De-Amplifying: Requirements for Robust Bayesian Active Learning under Model Misspecification* (arXiv v2, 2026), §§2–4, studies prediction under a fixed, potentially inadequate model family. Its analysis separates approximation error, estimation error and their interaction under the intended input distribution. This motivates the explicit receiving conditions in :4.6. Their proposed acquisition rule is not a universal remedy: its assumptions and quantities need their own justification before use. The adopted general move is to compare consequential model inadequacy and observation placement, rather than assuming that higher information gain implies better prediction. [Read version](https://arxiv.org/html/2506.07805v2).

These sources develop statistical branches. The bounded-error construction in :5.1 is an elementary set-valued derivation; it needs no prior distribution. Reopen the selected design when the target, record law, feasible access, receiving population or substantive model alternatives change. A newer optimization technique matters when it improves that same construction at worthwhile effort.

### MMP.16:12 - Relations

- **MMP.7** constructs the law of what is recorded; **MMP.11** constructs the admitted model family.
- **MMP.12** exposes recovery ambiguities; **MMP.13** supplies inference and uncertainty claims that match the chosen observation procedure.
- **MMP.14** investigates failed predictions and returns to the implicated subject or observation assumption.
- **MMP.15** supplies causal identification when the target is an intervention effect. A new association does not by itself identify that effect.
- **MMP.8** formulates the receiving choice; **MMP.8.SD** constructs a longer observation-and-action sequence when continuation changes the design.
- **C.11.DUA** appraises an evidence demand and its attainable contribution; **C.11** and the applicable portfolio methods compare attainable gains with resources and other consequences.
- **C.16.IR** supports a sufficient answer despite unresolved distinctions. **B.5.TC** relates a test to the theoretical comparison it is meant to change.
- **PHY.9** constructs a physical readout and **PHY.10** a physical test. Other subject practices realize the corresponding access and observation.
- **Computational Thinking** supplies the selected search, sampling or approximation procedure. **MMP.17** consumes an informative-case design when constructing a surrogate.

### MMP.16:End

# C. Change the model while retaining its use

## MMP.9 - Derive a Reduced Mathematical Model of State Evolution

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.9:1 - Problem frame

Use this pattern when a supplied model describes how a state changes, but predicting the quantities you need would be easier with less state, shorter memory or a simpler update. After removing detail, the proposed update still depends on something you removed. You need to derive what can replace that contribution while retaining a useful answer.

Start with the quantity you want to keep and compute its change from the supplied model. Circle the part that cannot be obtained from the proposed smaller state. For an average, this may be the variance of the underlying values. For one observed component, it may be the effect of unobserved components. That expression identifies the construction needed next.

The result can be a smaller evolution law, a history-dependent rule, an approximation with a stated error, or bounds sufficient for the question. Keep the initial information, inputs and time range on which it depends. A model that is already affordable and sufficient can be used directly. If the original change law is missing, recover or construct it in the subject practice before using this reduction method.

You need the mathematics used by the supplied law: substitution and recurrence for discrete changes; differentiation and integration for differential equations; expectations when reducing a probability distribution. A mathematical collaborator may perform those operations from your stated question and model. This is reduction within mathematical modeling. A.3.3.PI supplies the general test of which information a prediction needs; C.29.1 supplies the comparison that transfers the reduced result back to the source question.

### MMP.9:2 - Problem

A description can retain today's quantity while losing what determines tomorrow's. Differentiating a mean can introduce higher moments. Solving for an unobserved component can make its past influence explicit. Dropping a quickly decaying component can retain a lasting change it caused before decaying.

The missing contribution is often called an **unclosed term**: the proposed retained state does not determine it. A **closure** supplies a way to obtain or approximate that contribution from the information the reduced model carries. Its choice changes the resulting evolution.

Finding the unclosed term locates the difficulty. The remaining work is to derive a usable replacement and determine what that replacement permits the model to answer.

### MMP.9:3 - Forces

| Choice | Consequence for the construction |
| --- | --- |
| Smaller state and longer memory | Eliminating coordinates can replace present-state work with a history calculation. |
| Detailed trajectory and selected result | A bound on one output can be cheaper than a replacement for the whole trajectory. |
| Additional moments and finite closure | Deriving another moment can expose yet another missing moment. |
| Short-lived component and lasting effect | A small or fast component can make a consequential accumulated contribution. |
| Fit to supplied trajectories and use inside a new evolution | Once the replacement supplies the next state, its errors can change the states it later receives. |
| Several adequate replacements and available effort | An existing bound or larger model can cost less than developing a new closure. |

### MMP.9:4 - Solution

**Choose the retained result → derive its change → expose the unclosed contribution → construct a replacement or bound → use it over the required horizon → revise the part that changes the answer.**

The work may end at a useful bound. It may also show that the smaller description would cost more than continuing with the source model.

#### MMP.9:4.1 - Express the retained result and its change

Name the source state z, its initial possibilities and the admitted inputs u. Specify the answer and horizon: a quantity at time T, a threshold crossing, a response to an input, or a distributional feature. Construct the retained description x=r(z) from those needs. A.3.3.PI:4.1-4.2 tests whether merged source states can still answer that question; use an already sufficient result from that test.

For a discrete source update z_next=F(z,u), substitute it into the retained description:

`x_next = r(F(z,u)).`

For a differentiable r and a differential law z_dot=F(z,u), the chain rule gives:

`x_dot = Dr(z) F(z,u).`

Dr is the derivative of r. If r also depends explicitly on time, include its time derivative. A discontinuous readout or event needs its own change relation rather than this differentiable formula. A.3.3.TR supplies composition of the relevant changes.

Rewrite the result using x, the admitted inputs and whatever other information the smaller model proposes to carry. The part still depending on discarded quantities is the unclosed contribution. One convenient decomposition is `x_dot=f0(x,u)+c(z,u)`, where f0 is the part you will compute directly and c is the remaining contribution. Another decomposition can be useful; what matters is the complete retained law and what information obtains each term.

If every term is obtainable from the retained information, construct the closed update through A.3.3.PI and compare it through C.29.1. Continue here when the replacement itself still needs construction.

#### MMP.9:4.2 - Derive the discarded contribution before approximating it

Try to express the discarded variables through their own evolution, initial conditions and the retained history. In a discrete law, iterate the discarded update and substitute each earlier term until the dependence has a usable form. In a differential law, solve or integrate the discarded equation under the supplied retained history, then substitute the result into the retained equation.

For constant compatible matrices and supplied initial values, consider:

`x_dot=A*x+B*y`, `y_dot=C*x+D*y`.

Solving the second equation while treating x(s) as its input gives:

`y(t)=exp(D*t)*y0 + integral_0^t exp(D*(t-s))*C*x(s) ds`.

Substitution gives the retained law:

`x_dot(t)=A*x(t)+B*exp(D*t)*y0 + integral_0^t B*exp(D*(t-s))*C*x(s) ds`.

The first added term carries the discarded initial condition. The integral carries the past influence of x through y. With a forcing term in the discarded equation, its propagated contribution also appears in the integral. These terms identify what a proposed memory approximation would replace. Unknown y0 remains an initial uncertainty; it cannot be set to zero solely because y is being removed.

Look for a less costly way to compute the derived expression. Equal decay modes can be combined; a sum of exponentials can be updated through a few auxiliary variables. For example, `v(t)=integral_0^t exp(-lambda*(t-s))*x(s) ds` satisfies `v_dot=x-lambda*v`, v(0)=0. This replaces storage of the whole history with an evolving value. Carry a nonzero initial contribution separately or incorporate its matching initial condition. Count the required auxiliary values and update work before claiming a computational saving.

For nonlinear discarded dynamics the same elimination question remains, but the response to retained history may require solving a nonlinear problem. Use the derived dependence to select an approximation, retained variable or bound; an implicit formula that still requires the original computation has not yet supplied a cheaper model.

#### MMP.9:4.3 - Choose and construct a useful replacement

Use the expression just derived to decide which information or calculation earns its cost.

**Retain a quantity that obtains the missing contribution.** If c depends on a small additional observable v, derive v's update from the source law and repeat the closure test for the pair (x,v). This operation can reveal a useful finite system or a growing hierarchy. For members obeying `Z_dot=-Z^2`, the mean m has `m_dot=-mean(Z^2)`. Retaining `q=mean(Z^2)` gives `q_dot=-2*mean(Z^3)`. The new equation exposes the next assumption needed; adding q alone does not finish the closure.

**Compute the effect through memory.** Use the history expression from :4.2. To truncate old history, bound its omitted contribution for the admitted histories. To replace the memory kernel by a simpler one, bound or estimate the resulting difference on those histories, then propagate that difference through the retained evolution. A slowly decaying kernel can make distant history consequential. An auxiliary-state representation can be cheaper than truncation when a few modes express that kernel.

**Bound the requested output.** If the use asks for a threshold or interval, derive bounds directly from the source law and available initial information. For a population, solve or bound the member response as a function of its initial value, then average using known ranges or moments. Monotonicity, convexity or conservation can give a bound without choosing a complete distribution. The nonlinear example in :5.2 constructs such bounds. Use C.29.1:4.5 to turn them into the corresponding decision, or to expose the still-unresolved range.

**Approximate a contribution whose accumulated effect is small.** Identify the parameter and the class over which smallness is claimed: initial values, inputs, horizon and required error. Derive or bound the contribution integrated over that horizon. A small coefficient can multiply a large hidden value, and a fast transient can shift the later state. If a transient only matters near the start, retain its effect in an adjusted initial value and state when the later approximation begins. :5.3 shows both constructions.

A learned closure is another possible approximation to the missing contribution. Specify what its inputs contain and how its output enters the retained update. Pairs of retained inputs and source contributions can support fitting, but different hidden states can give different contributions at the same retained input. A fitted conditional mean then answers a distribution-dependent question; it is not an all-cases replacement of those contributions. When probability is needed, MMP.7 helps construct the law of the sampled or recorded training cases. Use the resulting closure at its intended inputs and horizon before drawing the corresponding predictive conclusion.

Compare the candidates through the existing characterization and choice methods: the required output or bound, obtaining cost, initial information and conditions. There is no need to develop every alternative. C.11.DUA helps choose whether more derivation, data or computation can change the decision.

#### MMP.9:4.4 - Evaluate the replacement inside the retained evolution

Write the model that will actually be used, including its initial values, any auxiliary variables, input rule and observation interpretation. Construct the requested output from that model. Substituting the closure into known source trajectories tests a different computation from letting it generate successive retained states.

Compare the retained source result and the reduced result for the same admitted initial case and input. For an identity, use the derivation to establish the covered equality. For an approximation, propagate the discrepancy to the requested output and horizon through C.29.1:4.5. A numerical scheme adds its own approximation; include it when it can change the answer. A.3.3.PI:4.5 supplies the repeated-use and changed-condition questions.

For a probabilistic model, choose the distributional feature the work needs. Agreement of a mean can coexist with different variance, correlations or event probabilities. A further observable is worth checking when it can change the planned use. State which result the comparison supports rather than extending one fitted statistic to the whole model.

When inputs are chosen from observations, retain the information the choice rule uses. If reduction removes that information, formulate the revised choice under MMP.8 before claiming that the same intervention or control method remains available. A changed intervention also requires the corresponding source law or mechanism under C.28.MR.

#### MMP.9:4.5 - Return the result and revise the construction when needed

Return the reduced law, sufficient bound or located obstacle with the assumptions that affect its use. An existing derivation and calculation can carry this information. Explain which discarded contribution was replaced, how to initialize and run the replacement, and which question it answers.

If a bound settles the working question, use it. If the result is too weak, locate why: uncertain initial influence, unresolved higher moment, long memory, error amplification, or information unavailable to an action. Improve that contribution or retain more of the source model. A mathematical construction can also show that the proposed simplification offers no saving.

Reopen the affected construction when the source law, initial class, inputs, observation, horizon or required output changes. Keep conclusions whose conditions still hold. In a model of a working method, ME can use the comparison to design a different method or representation; the actual work must still provide the quantities and relations assumed in the model.

### MMP.9:5 - Archetypal Grounding

#### MMP.9:5.1 - Replace many response components by two evolving quantities

Suppose a dimensionless model has an observed x and n hidden response components:

`x_dot=-x+sum_i y_i+u(t)`, `y_i_dot=c_i*x-2*y_i`,

where the nonnegative c_i sum to one. Initial values and a prescribed input u(t) are supplied. The question asks for x over a finite horizon; each y_i separately is irrelevant to that result.

Retaining x alone leaves the unclosed contribution sum_i y_i. Solve each hidden equation and sum:

`sum_i y_i(t)=exp(-2*t)*sum_i y_i(0)+integral_0^t exp(-2*(t-s))*x(s) ds`.

All hidden contributions have the same decay kernel. Define v=sum_i y_i. Differentiating the sum gives the two-variable model:

`x_dot=-x+v+u(t)`, `v_dot=x-2*v`, `v(0)=sum_i y_i(0)`.

The derived equations and initial sum preserve x for every supplied input for which these linear equations have their solution. For n>1 this uses two evolving quantities instead of n+1. The required hidden initial information is their sum. Arbitrarily setting v(0)=0 would already change x_dot(0) when the actual sum is nonzero.

The initial sum requires n terms once. Each subsequent evaluation of the reduced right-hand side uses x, v and u(t); it no longer recomputes n component contributions. This saves repeated arithmetic when those components would otherwise be advanced separately.

Now one component has decay rate 3 instead of 2. Summing produces `v_dot=x-2*v-y_1`; the old two-variable model has lost a contribution. Retain y_1 separately and update it by `y_1_dot=c_1*x-3*y_1`, or separate the two decay groups. The change determines which added state is needed. The same grouping can combine any components that share their response kernel; different kernels remain distinct until another justified approximation combines them.

#### MMP.9:5.2 - Answer about a nonlinear population without a closed mean equation

A finite population has nonnegative member values X_i with `X_i_dot=-X_i^2`. The available initial information is 0<=X_i(0)<=M and mean m0. The requested output is the mean m(t).

Differentiating the mean gives:

`m_dot=-mean(X_i^2)=-m^2-Var(X_i)`.

Replacing this by m_dot=-m^2 sets the variance contribution to zero. Populations with the same mean can have different variance, so first ask whether a bound already answers the question.

Each member has `X_i(t)=X_i(0)/(1+t*X_i(0))` for t>=0. Since X_i(0)<=M, averaging gives the lower bound `m0/(1+M*t)`. The response `a/(1+t*a)` is concave for nonnegative a and t>=0; the mean of the responses is at most the response of the mean. Thus:

`m0/(1+M*t) <= m(t) <= m0/(1+m0*t)`.

With M=2, m0=1 and t=1, the mean lies between 1/3 and 1/2. A requirement m(1)<=0.55 is established without a variance model or a complete initial distribution.

Change the requirement to m(1)<=0.4. A population whose members all start at 1 has m(1)=1/2. An equally divided population starting at 0 and 2 has m(1)=1/3. Both fit the supplied initial information, so it cannot settle the changed requirement. Information about the initial population or a different acceptable requirement would change the next move. Treating the zero-variance closure as the whole population would conceal this distinction.

#### MMP.9:5.3 - Decide whether a fast transient can be omitted

For a dimensionless model with epsilon>0,

`x_dot=y`, `epsilon*y_dot=-y`,

the solutions for t>=0 are `y(t)=y0*exp(-t/epsilon)` and `x(t)=x0+epsilon*y0*(1-exp(-t/epsilon))`.

Suppose the admitted initial values satisfy abs(y0)<=Y. Replacing the model by constant x0 gives an error at most epsilon*Y for every t>=0. With epsilon=0.01 and Y=1, that is 0.01. It can meet a tolerance 0.02 while failing to establish tolerance 0.001. The coefficient alone is insufficient if the initial class changes: y0=1/epsilon leaves a later change approaching one.

When y0 is known and the use concerns only later times, a different approximation is constant `x0+epsilon*y0`. Its error is at most `epsilon*Y*exp(-t/epsilon)`. For tolerance `0<eta<epsilon*Y`, it meets that tolerance at all times starting from `t_start=epsilon*log(epsilon*Y/eta)`. With eta=0.001 in the preceding case, t_start is about 0.0231. The adjusted initial value has retained the transient's later effect; it does not reproduce the initial interval.

If y0 is unknown, the adjusted value is also unknown. Its stated range can still yield a useful interval for x. The choice between an early transient calculation, a later approximation and a bound follows the requested result and available initial information.

### MMP.9:6 - Bias-Annotation

Compact equations can conceal transferred effort. Removing variables may require a history integral, extra initial information or an expensive closure. Compare the work needed to obtain the requested result. A familiar equilibrium substitution or learned fit is a candidate construction whose lost contribution must remain visible in that comparison.

### MMP.9:7 - Conformance Checklist

- Can the retained quantity's change be derived from the supplied law, with its initial and input conditions?
- Which contribution is unavailable from the proposed retained information, and how does the replacement obtain, approximate or bound it?
- Does an added variable have its own usable update and initialization? If a hierarchy remains, where is the closing assumption?
- For a memory or small-parameter approximation, what bounds the omitted effect on the requested output over the stated horizon?
- Is the comparison made in the model's intended repeated use, with the relevant numerical and observation conditions?
- Does the resulting law or bound settle the working question? If not, which changed contribution could do so at worthwhile cost?

### MMP.9:8 - Common Anti-Patterns and How to Avoid Them

| Observed difficulty in the construction | Repair |
| --- | --- |
| Replacing the mean of a nonlinear response by the response at the mean loses heterogeneity. | Derive the missing moment term, then retain, model or bound its effect; :5.2 may already settle the output question. |
| Hidden state is eliminated together with its initial effect. | Carry the initial-condition term in the memory formula or initialize the corresponding auxiliary value. |
| A small coefficient is used as the entire error argument. | Bound the multiplied state, accumulated contribution and admitted initial class, as in :5.3. |
| A closure is judged only on inputs from the source trajectory. | Insert it into the retained evolution and compare the requested result at its intended horizon. |
| Adding a moment is presented as completing a model although its equation needs another moment. | Continue the derivation until a usable closure or sufficient bound is obtained; otherwise retain the unresolved contribution. |

### MMP.9:9 - Consequences

A reduced model can expose which information determines the answer and make repeated calculation cheaper. Bounds can support a decision before a full reduced trajectory is available. Derivation also identifies a reusable limitation: which initial conditions, inputs or new questions require restoring discarded content.

The cost can move into initialization, memory, closure construction or verification at the required horizon. Where that cost exceeds using the source model, the larger account remains a useful option.

### MMP.9:10 - Architectural Rationale

Reduction is organized around the requested result and the source law's unclosed contribution. This makes the choice between retained state, memory, approximation and bounds depend on what each construction obtains. Beginning with one favored approximation would select what to discard before establishing its effect.

A.3.3.PI supplies the question-relative information test. This method develops the subsequent mathematical construction of a replacement contribution. C.29.1 supplies the common exact-or-bounded transfer and error propagation; those rules also apply to constructions outside model reduction.

Linear response, nonlinear aggregation and fast transients require different constructions. A new source law requires deriving its own discarded contribution; it need not resemble one of these examples. When the deriving operation itself requires a further subject method, retain that mathematical dependency rather than presenting a technique's name as an already obtained closure.

### MMP.9:11 - SoTA-Echoing

The practice question is how to replace unresolved dynamics economically while retaining the needed result. **Adopt** construction from the source law and evaluation within the reduced evolution, including memory, initial information and question-relative outputs. A serious alternative fits an instantaneous missing term on source trajectories and judges primarily that fit. It can be cheaper and adequate for a limited use, but it can miss errors generated when the closure supplies its own future inputs.

[Sanderse, Stinis, Maulik and Ahmed, Scientific machine learning for closure models in multiscale problems, version 2 (2024), sections 2.1-2.2, 3.2 and 7.1](https://arxiv.org/html/2403.02913v2), is a comparative synthesis of closure constructions. It distinguishes an unclosed term from its replacement, and fitting the term from testing the evolving reduced model. **Adapt** these distinctions in :4.1-4.4. Its memory discussion supports preserving initial and historical effects during elimination. An exact elimination identity still needs an affordable way of obtaining its result; :4.2 makes that cost question explicit. The linear elimination, population bounds and transient estimates above are elementary derivations developed here, not empirical validation claims.

[Freitas, Um, Desbrun, Buzzicotti and Biferale, A posteriori closure of turbulence models: are symmetries preserved? (2026 preprint), sections 3-5](https://www.geometry.caltech.edu/pubs/FUDBB26.pdf), provides a current countercase. A learned shell-model closure reproduces selected statistics while missing other correlations and scale-invariance properties. **Adopt** its consequence in :4.4: select the observables that the receiving use needs instead of extending fit of one statistic to all requested behavior. Missing memory is a proposed explanation in that case; it does not establish a universal cause or require every reduced model to carry the same memory construction.

The selected method spends effort on the omitted contribution and the use it can change; it need not reproduce every property of the detailed model. A sufficient analytic bound can be cheaper than training or testing another closure. Reopen the comparison when changed inputs, initial conditions, horizon or requested observables expose a consequential error, or when another construction obtains the same needed result at lower cost.

### MMP.9:12 - Relations

- **A.3.3.TR and A.3.3.PI:** compose source changes, determine the information needed for the future question and update the retained account. MMP.9 constructs a remaining closure or bound after those operations expose the gap.
- **C.29.1 and MATH.2:** compare the retained construction with the source and determine which answers survive identification; use their exact or bounded transfer where applicable.
- **MMP.7 and MMP.8:** construct observation laws and information-limited choices when a learned or controlled reduced model uses them. Their conditions determine which data law or action rule is actually being compared.
- **C.28.MR and B.5.MPC.R:** reconsider the relevant mechanism or connected accounts when an intervention or model change alters the source law.
- **C.11.DUA:** decide whether further derivation, observation or comparison is worth its cost for the receiving decision.
- **E.22 and E.23:** frame the question for evaluating a candidate, then organize repeated improvement under that evaluation when needed.
- **EXD and C.2.8:** EXD develops an explanation for the recipient's question; C.2.8 compares what structure that recipient can recover from its expression under stated conditions. Prediction and explanation can require different retained results.
- **ME:** use the mathematical result to construct or change the working method it describes.

### MMP.9:End

## MMP.17 - Construct a Surrogate for Selected Model Responses

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.17:1 - Problem frame

**Use this when** repeated use of a model is too costly or cumbersome, and the next calculation needs only some of its responses. You may need values at many inputs, a probability of exceeding a limit, a field over a region, or a response used inside an inverse problem. Begin with one receiving question: which response must the replacement supply, over which inputs, and what error would change the answer?

A **surrogate** is a replacement constructed to reproduce selected responses of a source model. It may be an interpolation table, a constrained formula, a reduced representation of outputs, a learned function, or a correction to a cheaper model. The practical gain is a less costly response with a usable account of where substitution holds and where to return to the source.

This is a method of mathematical modeling. It applies to computational, physical, biological and organizational models; a differential equation or a neural network is one possible case. It governs the construction and use of a replacement, while the subject practice supplies the meaning and grounds of the source model. Agreement with that model and agreement with the world remain different questions.

Preparation requires functions, interpolation and an error comparison suited to the receiving calculation. The derivative branch uses elementary differentiation; the output-basis branch uses orthogonal projection and singular value decomposition. The stochastic branch requires expectation, variance and the meaning of interval coverage. For a learned replacement, CMP.7 supplies the learning rule and its further-use conditions, with CMP.6 supplying iterative computation when needed. A specialist can construct a harder approximation, but must return an evaluable replacement and the conditions under which its response can be substituted.

For a few inexpensive queries, evaluate the source or reuse already computed answers. If a prescribed numerical approximation already supplies the response and sufficient error control, CMP.8 may finish the work. Surrogate construction becomes useful when selecting the responses, cases and retained structure changes what can be obtained at affordable cost.

### MMP.17:2 - Problem

A replacement can fit its construction cases and fail at the inputs or operations that matter next. Average accuracy can conceal a wrong threshold crossing, a lost dependence between outputs, or a derivative with the wrong sign. A source model can also be wrong in a way that its accurate surrogate faithfully reproduces.

The modeling problem is to construct a useful substitution without silently enlarging its promise: choose what to reproduce, obtain informative cases, build the replacement, and act on consequential discrepancies or lost structure.

### MMP.17:3 - Forces

| Force | Tension |
| --- | --- |
| Selected response | Reproducing less can save work, while a later question may need something discarded. |
| Construction cost | More source evaluations can improve the replacement, but may consume the saving it was meant to provide. |
| Known structure | Conservation, bounds and symmetries restrict useful candidates; a convenient restriction can also exclude the needed response. |
| Local and broad use | Concentrating cases near a decision can improve that answer while leaving other inputs poorly represented. |
| Several error sources | Source computation, surrogate approximation and uncertain source premises can each limit use and require different repairs. |
| Continued use | Reuse makes construction worthwhile, but changed inputs or questions can invalidate the substitution. |

### MMP.17:4 - Solution

Construct the replacement around the response that another calculation or person will use. Carry the source conditions into that substitution, and refine only where the remaining difference matters.

#### MMP.17:4.1 - Select the response and the input region

Let \(M\) be the source model and let \(Q\) extract the required response. Write the target as

\[
r(x)=Q(M(x)),\qquad x\in D,
\]

where \(x\) contains the inputs and \(D\) is the intended region of use. The input may be a number, a vector, a history, a function or a discrete configuration. State enough of its meaning to distinguish materially different conditions. If the same listed input gives different deterministic responses because a regime or previous state was omitted, restore that input before fitting a function.

Choose \(Q\) from the receiving operation. A mean, a tail probability and an entire probability law are different targets. So are a field value, its spatial derivative and a quantity integrated over that field. For a random source output \(Y_x\), a mean surrogate targets \(\mathbb E[Y_x]\); reproducing individual draws or their distribution requires another construction.

Determine how response error affects the receiving result. For a comparison with a limit, the distance to the limit matters. For a ranking, the gap between alternatives matters. If the receiver will differentiate, iterate or invert the response, include the corresponding sensitivity or structural requirement. A low average value error does not select these requirements for the practitioner.

#### MMP.17:4.2 - Obtain construction cases that can distinguish useful replacements

Reuse source results whose inputs, output meanings and computation are compatible with the target. Choose further cases to expose consequential variation: the region the receiver will visit, boundaries or changes of regime, and places where plausible replacements disagree about the receiving answer.

For a scalar interval, an initial set of endpoints and interior points may suffice. For many inputs, a full grid can be unaffordable; use known structure to reduce the varying inputs, or distribute a finite set across the relevant region before concentrating additional cases. A design concentrated near one operating point supports a local construction unless another argument supports wider use.

Each case supplies an input and the selected source response. If the source response is itself approximate, carry its error into the construction. For a stochastic source, use MMP.7 to identify how the runs were obtained: repetitions, dependence, shared random inputs and selection can change what their averages or fitted probabilities estimate. MMP.13 supplies the uncertainty result needed from those runs.

Choose case placement and assessment together. Cases used to fit, select or repeatedly tune the replacement are construction cases. If the further-use claim depends on held-out performance, retain assessment cases suited to that use and do not count their later reuse for tuning as untouched assessment. For trajectories, repeated runs or grouped inputs, the unit that must be held out follows the claim; randomly separating nearby points does not by itself test a new trajectory or regime.

A query to the source model adds information about that model's response. An observation of the world may also challenge the model. Keep those contributions separate. Use existing bounds or observations when they already answer the question; another experiment is not an entry condition for constructing a surrogate.

#### MMP.17:4.3 - Construct an evaluable replacement with the needed structure

Start with a representation that can express the required response at the available construction cost. Use MMP.11 to preserve justified relations and to expose what remains adjustable.

For ordered scalar cases \((x_i,r_i)\), one complete construction is piecewise linear interpolation:

\[
\widehat r(x)
=\frac{x_{i+1}-x}{x_{i+1}-x_i}r_i
+\frac{x-x_i}{x_{i+1}-x_i}r_{i+1},
\qquad x_i\leq x\leq x_{i+1}.
\]

The rule supplies a response between distinct neighboring inputs. It needs no iterative training. Its adequacy between the cases still depends on the response's variation and the receiving tolerance.

For a field or a large output vector, one can instead construct

\[
\widehat y(x)=y_0+\sum_{j=1}^{k} a_j(x)\phi_j.
\]

Here \(y_0\) and the retained output shapes \(\phi_j\) come from known structure or computed cases. For example, take \(y_0\) as the mean case vector, stack the centered case vectors as columns, retain selected left singular vectors of that matrix, and project each centered case onto those orthonormal vectors. Then interpolate or learn the coefficient functions \(a_j(x)\) from the inputs and the computed coefficients. A small reconstruction error over sampled fields can still discard a localized feature that controls the receiver's maximum or threshold. If only \(Q(y)\) is needed, compare approximating that response directly with reconstructing the full field.

When a cheap model \(L\) already follows much of the response, construct a correction from paired cases:

\[
d_i=r(x_i)-L(x_i),\qquad
\widehat r(x)=L(x)+\widehat d(x).
\]

Pair the same inputs and corresponding outputs. This construction still evaluates \(L\) at each new input. It is useful when the discrepancy is easier to approximate than the whole response; if the cheap model misses the consequential regime, adding many cheap cases may help little.

For a learned function, supply CMP.7 with the target, construction cases, function family and loss that reflects the required response. Obtain its effective fitting procedure through CMP.6 or another suitable computation. Writing an objective without a way to obtain and evaluate its candidate leaves the replacement unfinished. Optimization progress, fit on construction cases and accuracy at further inputs are separate results.

Preserve a justified relation by construction when possible. If two delivered quantities must sum to an input \(d\), construct one and define the other as \(d-\widehat q_1\), while also enforcing any required nonnegativity or capacity limits. A small penalty for violating a relation permits violations; it does not implement the relation as an identity.

#### MMP.17:4.4 - Locate errors and losses that change the receiving use

Compare the replacement with the source in the quantities the receiver consumes. A deterministic bound, an empirical error on selected cases and a statistical interval support different conclusions.

When bounds are available in the same response metric, propagate them. For example, if interpolation of accurate case values differs from \(r\) by at most \(e_{\mathrm{int}}\), and each supplied case value has error at most \(e_{\mathrm{case}}\), convex linear interpolation has error at most \(e_{\mathrm{int}}+e_{\mathrm{case}}\). Other fitting rules need their own propagation: a poorly conditioned fit can amplify errors in its cases. CMP.8 supplies that numerical approximation and conditioning work.

For a scalar test \(r(x)\leq b\), a justified bound \(e(x)\) gives an immediate rule:

- if \(\widehat r(x)+e(x)\leq b\), the bound supports the test;
- if \(\widehat r(x)-e(x)>b\), the bound rules it out;
- otherwise the replacement leaves this test unresolved.

An observed maximum error at finitely many cases is not automatically a bound over \(D\). A statistical coverage result retains its sampling and calibration conditions and its pointwise, marginal or simultaneous meaning. A fitted uncertainty indicator can guide the next query without supplying such a result.

Test lost operations as well as values. On \([0,1]\), \(r(x)=x\) and \(\widehat r(x)=x+0.01\sin(1000x)\) differ in value by at most \(0.01\). Yet \(r'(x)=1\), while \(\widehat r'(\pi/1000)=-9\). If a receiver follows the derivative, this substitution can reverse the proposed direction. Include derivative information or a justified monotone family when that operation matters, or keep the source calculation for it.

A discrepancy with the source calls for examination of case coverage, representation or fitting. A discrepancy with observations can instead require MMP.14 to revise the source or its observation model. Agreement with the source cannot close that second question.

#### MMP.17:4.5 - Refine, combine or return where the difference matters

Choose the next change from the unresolved receiving result. With piecewise interpolation and a bound on curvature, subdivide intervals whose error bound can change that result. With an empirical construction, inspect informative new source cases, a different family or a local correction. Adding cases everywhere can cost more than repairing the affected region.

For adaptive case selection, make a finite candidate set in the allowed region, compare its points by the expected relevance of their unresolved responses and an error or disagreement indicator, and query the chosen source cases. Retain coverage of plausible unexplored regimes; a confident but misspecified replacement can otherwise prevent its own correction. Refit after adding the cases and assess the changed replacement under the conditions needed for the claim. The indicator is a reason to investigate a point, not evidence that the source response there has already been obtained.

A useful combination may keep the source near a threshold or regime boundary and use the surrogate elsewhere. It may keep a cheap model with a learned correction, or different replacements for different response questions. Make the selection condition usable by the caller. When a query is outside the supported region or the needed error control is unavailable, call the source if it can answer, restrict the claim, or return the unresolved response.

Compare total effort: case generation, fitting, checking, each later evaluation, and repairs after relevant changes. A source call can finish a single difficult query more cheaply than improving a reusable approximation. Stop when the receiving question has sufficient support at acceptable cost. Use the existing FPF choice and improvement methods when several worthwhile replacements or refinements remain; this construction does not require one universal best surrogate.

#### MMP.17:4.6 - Carry the substitution into continued use

Make the evaluation rule, input meanings and region, selected responses, and consequential limits available with the replacement. The receiver must be able to obtain its response and recognize when the fallback applies. A function with its conditions in the surrounding model may suffice.

When the surrogate enters an inverse problem or an uncertainty calculation, propagate its approximation in the observation metric and into the requested conclusion. A small forward-response error can matter greatly along a poorly resolved direction. MMP.12 supplies the ambiguity and regularization analysis; MMP.13 supplies the qualified inference and uncertainty. Treating the replacement as an exact likelihood or forward relation can give a tighter answer than its construction supports.

Reopen the construction when the input region, source assumptions or receiving operation changes. A new question about an intervention may need causal identification or a mechanism supplied by the subject practice, even if the old predictions remain accurate. A new request for explanation needs the relevant relations, not only the same output number. Use C.2.8 to distinguish the structure a reader can recover and EXD to construct an explanation from a supplied subject account. A compact surrogate may expose useful structure, but compactness and predictive fit do not establish that contribution.

### MMP.17:5 - Archetypal Grounding

#### MMP.17:5.1 - Refine an interpolation only until it settles the comparison

A repeated calculation needs the response \(r(x)\) of a costly reference model for \(0\leq x\leq1\). The present question is whether \(r(0.4)\leq0.3\). Available analysis of the reference model gives \(|r''(x)|\leq2\). Its accurate case values are \(r(0)=0\) and \(r(1)=1\).

The first surrogate is the line \(\widehat r(x)=x\). For linear interpolation on an interval of width \(h\), the curvature bound gives an error at most \(2h^2/8\). With \(h=1\), the response at \(0.4\) is therefore enclosed by \(0.4\pm0.25\). This interval crosses \(0.3\); the replacement has not answered the question.

Query the reference model at \(x=0.5\), obtaining \(r(0.5)=0.25\), and use the two half-intervals. In the first half, \(\widehat r(x)=0.5x\), so \(\widehat r(0.4)=0.2\). The bound is now \(2(0.5)^2/8=0.0625\), giving

\[
r(0.4)\in[0.1375,\,0.2625].
\]

The upper endpoint is below \(0.3\). One added case and a specified interpolation rule settle the comparison under the curvature premise. The three values alone would not justify the bound.

Now the receiving limit changes to \(0.18\). The same enclosure crosses that limit. For this one query, the practitioner returns to the reference model at \(0.4\), which gives \(0.16\), and can answer the stricter comparison. If many similar queries are expected, further subdivision may instead be worthwhile. There is no need to improve the surrogate over the entire interval to finish the single question.

These calculations establish agreement with the reference model under its stated smoothness and case-accuracy conditions. Whether that model's response represents the subject phenomenon remains a separate modeling question.

#### MMP.17:5.2 - Correct a cheap allocation model, then change its regime

A network model returns delivered quantities \(q_1(d)\) and \(q_2(d)\) through two channels for demand \(2\leq d\leq4\). In the normal regime all demand is served, so \(q_1+q_2=d\). A cheap approximation splits it equally: \(L(d)=(d/2,d/2)\).

The source supplies \(q(2)=(1.2,0.8)\) and \(q(4)=(3,1)\). The first-channel discrepancies from \(L\) are \(0.2\) and \(1\). Linear interpolation of that discrepancy gives

\[
\widehat d_1(d)=0.4d-0.6,\qquad
\widehat q_1(d)=0.9d-0.6,\qquad
\widehat q_2(d)=d-\widehat q_1(d).
\]

At demand \(3\), the replacement returns \((2.1,0.9)\). It preserves total delivery and nonnegativity throughout the declared interval. Those properties follow from the construction; agreement between the cases has not yet been established.

The receiving question is whether the first delivery stays at or below \(2.25\) at demand \(3\). The provisional value \(2.1\) is only \(0.15\) below the limit, and there is no supported error bound for this interpolation. A source query at \(3\) returns \((2.4,0.6)\), ruling out the proposed limit. Add its discrepancy \(0.9\) and interpolate separately over \([2,3]\) and \([3,4]\). The new surrogate matches all three cases and preserves the balance. Further-input accuracy remains an empirical question or requires a separate bound.

Now channel 2 becomes unavailable. The normal-regime fit does not describe this input. Suppose the changed source account states that channel 1 serves all demand up to \(3\) units and any excess remains unserved. The needed output now includes unserved demand \(u\):

\[
q_1=\min(d,3),\qquad q_2=0,\qquad u=d-q_1.
\]

At demand \(4\), the result is \((3,0,1)\). The balance has become \(q_1+q_2+u=d\). This branch follows from the newly supplied operating rule, not from extrapolating the normal-regime cases. Its formula is already cheap enough to use; training another replacement adds no benefit here. The caller can retain the normal-regime surrogate for its supported questions and use this formula for the stated unavailable-channel regime.

#### MMP.17:5.3 - Reuse stochastic cases when the requested response changes

A stochastic loss model returns either \(0\) or \(5\). Its source structure states that the probability \(p(x)\) of loss \(5\) is affine for \(0\leq x\leq1\); the two endpoint probabilities are unknown. All 2,000 runs in the construction are independent: 1,000 runs give 100 losses of \(5\) at \(x=0\), and another 1,000 give 300 at \(x=1\).

Fit the endpoint proportions and interpolate:

\[
\widehat p(x)=0.1+0.2x,\qquad
\widehat\mu(x)=5\widehat p(x)=0.5+x.
\]

The affine premise comes from the source structure, not from the two observed proportions. The mean surrogate is evaluable without rerunning the stochastic source.

At \(x=0.5\), the estimated mean is \(1\). A simple uncertainty calculation illustrates what must accompany that value. Each endpoint proportion has variance at most \(1/(4{,}000)\). Independence gives variance at most \(1/(8{,}000)\) for their average, an unbiased estimator of \(p(0.5)\) under the affine premise. Chebyshev's inequality therefore gives coverage of at least 95% for a half-width of \(0.05\) around that average. The resulting probability interval is \([0.15,0.25]\), and the corresponding mean interval is \([0.75,1.25]\). For a receiver using this 95% confidence procedure, the upper endpoint supports the mean-at-most-\(1.4\) comparison; it is not a deterministic bound. MMP.13 permits sharper uncertainty calculations when the receiving use needs them.

The receiver now asks whether \(\Pr(Y_{0.5}>4)\leq0.18\). The mean alone cannot answer: a constant loss of \(1\) has the same mean but a different tail. Here the retained two-point support supplies the relation \(\Pr(Y_x>4)=p(x)=\mu(x)/5\). Reuse the same cases and the probability surrogate; no new fit is needed. The interval \([0.15,0.25]\) crosses \(0.18\), so this uncertainty result leaves the new comparison unresolved.

The interval concerns the fixed input \(0.5\) under independent runs, the stated support and the affine probability law. It is not a simultaneous guarantee for all inputs, and it does not cover error in those source premises. A sharper inference, a useful bound, more runs or a qualified unresolved answer are different possible continuations; choose among them for the receiving question.

### MMP.17:6 - Bias-Annotation

Convenient source cases can overrepresent smooth central behavior and miss a boundary, rare response or minority regime. Begin with the receiving consequence, then check whether the construction and assessment actually expose it.

A family with a smooth uncertainty indicator can understate error where all its members share the same missing structure. Source comparisons outside the currently attractive region can reveal that failure. The indicator's numerical precision does not strengthen its grounds.

Construction cost can be hidden by reporting only evaluation speed. Compare the reuse expected in this work, including source queries and repair, before attributing a practical saving.

### MMP.17:7 - Conformance Checklist

Use these questions when relying on or passing on the replacement. The answers can remain in the model and its explanation.

| Check | Required content |
| --- | --- |
| Target | The source, selected responses, receiving operation and input region are recoverable. |
| Cases | Their obtaining conditions and any source-computation or sampling uncertainty fit the construction. |
| Construction | The representation and obtaining rule produce an evaluable replacement; justified coupled constraints are retained. |
| Consequential error | The error comparison addresses the receiving result and states whether its grounds are a bound, empirical comparison or statistical result. |
| Lost structure | A required derivative, dependence, regime or explanatory relation has not been inferred from value fit alone. |
| Continued use | The caller can identify unresolved queries and use the supported refinement, restriction or source return. |
| Effort | Construction and continued-use costs justify the substitution for the intended work. |

### MMP.17:8 - Common Anti-Patterns and How to Avoid Them

| Invited mistake | Repair |
| --- | --- |
| Declare success from small average error while a limit crossing is wrong. | Compare the response and error in the receiving operation, including the affected input region. |
| Treat an optimization objective as the constructed surrogate. | Supply the fitting procedure and the evaluator; inspect computational failure separately from inadequate cases or family. |
| Add cheap cases whose model misses the needed regime. | Examine the cheap-to-source discrepancy and compare correction with source-only construction at the same total effort. |
| Differentiate or invert a value surrogate without carrying its approximation. | Include the required operation in construction and error analysis, or keep the source for that operation. |
| Use the same cases repeatedly for tuning and claim untouched assessment. | Treat them as construction information and qualify the remaining further-use result. |
| Read a fitted interval as a guarantee against missing source structure. | Retain its conditions and return to source-model criticism or the subject account when those conditions change. |

### MMP.17:9 - Consequences

Selected responses can become cheap enough for repeated comparison, simulation or inference. Known constraints can remain usable even when most of the source calculation is replaced, and a local source return can resolve the few queries that remain difficult.

The saving comes with a narrower promise and construction cost. Different responses may need different replacements. A changed question can reuse the cases while changing the response construction, as in the tail-probability example, or require a changed source account, as in the unavailable-channel example.

### MMP.17:10 - Architectural Rationale

The response and the receiver's operation are chosen before the representation because they determine which differences matter. Reconstructing an entire model can waste effort; reproducing only a convenient summary can remove what the next operation needs. Selecting \(Q\) and \(D\) makes that trade-off actionable.

MMP.11 constructs families from known relations. MMP.17 adds the substitution question: which source responses to retain, which cases make their replacement informative, and where to refine or return when the replacement changes a receiving answer. CMP.7 and CMP.6 supply learning and computation when those are the chosen construction, while CMP.8 supplies numerical approximation control. The interpolation branch shows why a surrogate need not require a learner.

The source remains distinguishable from its replacement because a source call can repair approximation without repairing the model's account of the world. MMP.14 governs the latter discrepancy. Likewise, fast predictive use can coexist with a separate explanatory model; neither role earns the other's conclusions by sharing outputs.

### MMP.17:11 - SoTA-Echoing

The practice question is how to obtain a reusable response at lower total effort without losing what the receiver must do with it. The selected answer is a response-specific construction with informative cases, retained structure, and refinement or source return where the receiving consequence remains unresolved. It does not select one model family for every input dimension, data budget and error claim.

**Adaptive construction versus a fixed case budget.** [Winovich et al., *Active operator learning with predictive uncertainty quantification for partial differential equations*, v4 (2026), §§2 and 5](https://arxiv.org/html/2503.03178v4) compares uncertainty-guided construction with alternatives that differ in accuracy and training cost. **Adapt** this experimental line in :4.2 and :4.5: target informative queries while counting the guidance cost. Fixed distributed cases remain a serious alternative when guidance is unreliable or expensive. The PDE experiments establish neither general superiority nor error bounds at arbitrary inputs. Reopen the choice when consequential errors escape the indicator or the cost balance changes.

**Combined models versus a single replacement.** [Brunel et al., *A survey on multi-fidelity surrogates for simulators with functional outputs: unified framework and benchmark* (2025), §§3 and 6.6](https://arxiv.org/html/2408.17075v2) compares correction, mapping and fusion; its benchmark has no universal winner. **Adopt** paired correction in :4.3 and **adapt** the comparison in :4.5: retain the cheap model when its discrepancy is easier to represent than the whole response at comparable total effort. Interpolation or single-source construction can otherwise win. The functional-output results inform this branch, not the method's domain boundary. Lost features or weak correspondence reopen the choice.

**Structural restriction versus expressive universality.** [Kovachki, Lanthaler and Mhaskar, *Data Complexity Estimates for Operator Learning*, v2, introduction and main results](https://arxiv.org/html/2405.15992v2) supplies a theoretical counterweight to choosing an expressive learner first. Their general operator classes can require exponentially many examples, while more restricted approximation classes permit better rates under their assumptions. **Reject** expressive capacity as sufficient grounds for affordable construction; **adapt** the consequence in :4.1–:4.3 by reducing the target and using justified structure before expanding the learner. The results concern specified classes and access models, not the sample count for an arbitrary engineering model. Reopen the restriction when it excludes a consequential response.

For the scalar bounded case in :5.1, interpolation already answers the needed comparison with one added case and a supplied curvature bound. An operator learner or statistical uncertainty model would add assumptions and construction work without improving that answer. For coupled outputs or large response families, the retained contemporary branches can instead justify their extra cost. That difference, rather than a universal ranking of algorithms, selects the branch.

### MMP.17:12 - Relations

- **MMP.11** supplies families constrained by known relations; MMP.17 consumes them to reproduce selected source responses.
- **MMP.7 and MMP.13** supply the obtaining law and qualified inference for stochastic construction cases. **MMP.12** supplies ambiguity, stability and regularization when the replacement enters an inverse problem.
- **MMP.14** finds and repairs predictive discrepancies that can require a changed source model; a surrogate-to-source discrepancy can often be repaired within the present construction.
- **CMP.7, CMP.6 and CMP.8** supply, respectively, a learning rule with further-use conditions, iterative computation where needed, and numerical approximation or error propagation. None selects the receiving model response on behalf of the practitioner.
- **C.2.8 and EXD** distinguish recoverable structure and explanatory work from predictive agreement. **C.28.MR** supplies intervention consequences inside a stated causal model; agreement of surrogate outputs does not identify that model.
- **C.11/C.11.CRC** compare worthwhile choices and contributions; **C.18** governs retention and Pareto-front claims; **G.5** declares a selected set when that is the needed result. **E.22/E.23** frame and conduct improvement. MMP.17 supplies the candidate replacements and their response/error/cost consequences, not another portfolio or improvement method.

### MMP.17:End

## MMP.18 - Couple Models with Compatible Exchanges and Scales

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### MMP.18:1 - Problem frame

Use this pattern when the required answer combines models whose shared quantities, representations or scales differ. One model may return an average while another needs a distribution. Two simulations may exchange a flow at different times. Two statistical analyses may reuse the same prior or observations.

Begin at one exchange that affects the answer. Identify what the supplying model returns, what the receiving model uses it to mean, and the relation needed to connect them. A matching variable name or software interface leaves that relation to be constructed.

The result is a joint formulation: component models with their shared quantities, interface relations and the assumptions needed to use their combined answer. It may expose a missing closure, incompatible conditions or a dependency that an available simulator cannot realize. The first useful result can be that obstruction, or a restricted coupled answer sufficient for the work.

This is mathematical coupling across models. A.3.3.TR supplies joint relations and change rules; MMP.10 supplies their constraint formulation. The additional work here constructs exchanges between representations, preserves the quantities the use depends on, and accounts for shared information. Subject methods supply the meaning and applicability of those exchanges.

The reader needs the mathematics used by the components and their connection. Algebra suffices for the first coupling steps; time-dependent, spatial or probabilistic branches require the corresponding integration, mapping or probability knowledge. A collaborator can construct the mathematics from supplied models and a recoverable subject question.

Use an already adequate joint model directly. Merely keeping several alternative models in a portfolio does not require coupling them into one model. Use portfolio and improvement methods when the alternatives serve complementary questions without exchanging modeled quantities or information.

### MMP.18:2 - Problem

Locally useful models can give an unusable combination. An exchange may be counted twice or disappear between different time steps. Components may share an unknown while their combined calculation treats its values as independent. An average may conceal a variation needed by a nonlinear response. A sequential software call may insert a delay into relations intended to hold together.

The difficulty is to construct the joint model without silently changing what the components mean or the answer they are meant to support. Compatibility at the interface and adequacy in the subject remain separate questions.

### MMP.18:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse and joint meaning | Existing components save work but may describe their common quantity differently. |
| Local accuracy and combined behavior | Accurate component calculations can lose a balance or destabilize feedback through their exchange. |
| Different scales and required detail | A coarse result can omit the variation, timing or dependence another component needs. |
| Separate uncertainty and common information | Independent treatment can count shared evidence twice or remove correlation. |
| One joint solve and separate execution | Separate solvers retain existing tools but introduce exchange approximations and synchronization work. |
| More coupling and sufficient use | Recovering every interaction can cost more than the question warrants. |

### MMP.18:4 - Solution

Choose the combined answer. Recover the meaning and conditions of each consequential exchange. Construct interface relations that preserve what the receiving use needs, then impose them with the component models. Obtain and interpret a joint result, distinguishing a formulation defect from an approximation in its computation. Reopen only the exchange or component whose changed assumption affects that result.

#### MMP.18:4.1 - Identify what the models share and what they exchange

Start from the required result and trace which component supplies each quantity it uses. Recover the quantity's referent, unit and reference point, as well as any time interval, spatial region or probability conditioning that changes its meaning.

Distinguish a shared quantity from a transferred result. If both models describe the same unknown offset, retain one common offset or a justified relation between their coordinates. If one supplies an estimated offset to the other, specify whether the receiving calculation uses its uncertainty or only an approximation by a point value.

Locate overlapping subject effects. If both component laws already include the same interaction, composing them may count it twice. Decide from the subject model which contribution is being retained and which is a second description of it. A.3.3.TR and C.29.BB supply the resulting joint change and balance relations.

Also recover the operating conditions. A component calibrated for one boundary condition may cease to apply when connected to a responsive neighbor. Replacing a supplied input by another model's output can therefore require a changed component law, even when the variable types match.

#### MMP.18:4.2 - Construct the interface relation

Express the exchange as a relation between the component descriptions. A deterministic map is appropriate when the supplied result determines the needed input. Use a broader relation or conditional law when several inputs remain possible.

For a conversion, translate the quantity and its reference point. For an aggregate, state the operation over the specified region or interval. For example, an amount over [t0,t1] is the integral of a rate over that interval; a rate at t0 alone determines that amount only under an additional evolution assumption.

Let x range over values expressed by the supplying model and y over those used by the receiving model. A relation H(x,y) states the compatible pairs. A.3.3.TR supplies composition with other relations, and MMP.10 expresses the joint possibilities. MATH.18 helps determine which operations and consequences the interpretation preserves. Equality of numerical values is one possible relation, not the default.

Derive the property the map must preserve. For amounts at locations, a linear map b=W*a preserves their total for every a when every column of W sums to one. For values of an intensive field, a map preserving a constant field instead has every row sum to one. If amounts must remain nonnegative, nonnegative weights are an additional sufficient condition. The needed property chooses the map; a convenient interpolation routine does not choose the property.

The two conditions solve different problems. A common field value should remain that value on another discretization. The total amount distributed among cells should remain the same total. When both requirements matter, construct a map with the appropriate geometry or integration weights rather than substituting one condition for the other.

#### MMP.18:4.3 - Restore what the receiving scale needs

Apply the receiving operation to the proposed supplied description. If the result still depends on discarded detail, identify that dependency before choosing a closure.

For example, a component supplies only the mean of x over a region, while a neighboring response requires the mean of x^2. The missing contribution is the variance:

~~~
mean(x^2) = mean(x)^2 + variance(x).
~~~

Two fields with the same mean can therefore yield different received responses. Supplying the squared mean silently sets the variance to zero. Retain the needed statistic, obtain it from the finer model, supply a justified closure or return bounds sufficient for the question. MMP.9 derives reduced evolution and closures; MMP.17 constructs a surrogate when that is the chosen supplier.

A time-scale change can create memory. An interval average need not determine a response at an intermediate instant. A rapidly changing component can also leave an accumulated effect after its local state has relaxed. Recover the information needed by the receiving answer instead of assuming that a small or fast component has no relevant contribution.

Use a coupled approximation only within the conditions supporting it. If feedback drives a surrogate or closure into a different regime, revise that contribution or return to a suitable supplier. Good behavior on isolated component inputs does not establish behavior on inputs generated by the coupled system.

#### MMP.18:4.4 - Impose the joint conditions before choosing execution order

Combine the component relations and interface conditions for the same modeled situation. Shared boundary values and initial conditions must satisfy that joint formulation. Redundant equations can express a useful invariant; contradictory equations expose incompatible assumptions or a failed identification of the shared quantities.

Feedback can require a joint solve. Suppose the selected same-instant relations are x=1+y and y=x/2. Substitution gives x=2 and y=1. Starting from y=0 and calling the first model once, then the second, returns x=1 and y=0.5; those values fail x=1+y. That call order is only one unfinished computation of the joint relation.

Choose between a common solve and separate interacting computations from the available capabilities and error needed by the answer. For time-dependent components, specify which inputs are held, interpolated or extrapolated between communication times, how events are synchronized, and whether a proposed step can be repeated. These are computation assumptions unless the actual subject has that delay or sampling behavior.

Compare the obtained exchange against the joint conditions and the required result. A residual can reveal a mismatch. Turning a small residual into an error bound needs the relevant conditioning or stability argument; CMP.8 supplies that approximate-computation work. CMP.14 supplies interaction between computations. More iterations cannot repair an incompatible physical or statistical premise.

#### MMP.18:4.5 - Combine uncertainty without duplicating information

When components are probabilistic, construct a joint law for the common quantities and the component-specific quantities. Marginal distributions alone generally leave dependence unspecified. Obtain the needed dependence from the modeled mechanism, a conditional law or an explicit additional assumption.

For components sharing z, one possible factorization is:

~~~
p(z,u1,u2) = p(z) * p(u1 | z) * p(u2 | z).
~~~

It assumes conditional independence of u1 and u2 given z. If that assumption is unavailable, construct their joint conditional law or retain the unresolved dependence. A common random quantity is sampled or integrated once as that same quantity; two independent draws would describe a different model.

For two analyses using the same positive prior pi(z) and conditionally independent data D1,D2, their posteriors satisfy q1(z) proportional to pi(z)*L1(z) and q2(z) proportional to pi(z)*L2(z). The combined posterior is proportional to q1(z)*q2(z)/pi(z) on the common prior support. Multiplication without the division counts the prior twice.

If the analyses use overlapping records, first recover which observations and likelihood factors are shared. Dividing out a prior does not remove a duplicated observation. If component priors disagree, selecting a common prior or a pooling rule changes the model and needs a stated basis. MMP.7 supplies the record law and MMP.13 the resulting inference; a computational sampler obtains values from that law.

Point estimates can still be sufficient for a particular receiving use. To replace a distribution by a point, establish that the omitted uncertainty does not alter the required result at its chosen tolerance. Keep a consequential dependence when a nonlinear operation or tail probability needs it.

#### MMP.18:4.6 - Return the coupled result and localize a failure

Return the combined formulation with the exchanged quantities and assumptions needed to reproduce the required result. The subject recipient must be able to interpret that result, including any approximation or unresolved interface contribution that changes its use.

Check the consequence at the scope actually claimed. An interval balance establishes the amount transferred over that interval, not the time of a threshold crossing within it. A joint posterior accounts for the supplied data under its dependence assumptions; it does not establish that those assumptions describe the subject.

If a result fails, locate whether the problem lies in the quantity identification, map, closure, component law, dependence or computation. Repair that contribution and its affected consumers. For a physical question, B.5.MPC.R coordinates a change crossing the physical, mathematical and computational accounts.

Stop with the sufficient coupled answer or the missing contribution that prevents it. C.11.DUA governs whether obtaining that contribution is preferable to a restricted answer or a different method. More detailed coupling is useful when its difference matters to the work.

### MMP.18:5 - Archetypal Grounding

These constructed cases keep the model assumptions visible so that the reader can change the exchange and recompute its consequence.

#### MMP.18:5.1 - Preserve a transfer across different time resolutions

Two components model stores A and B. Material flows from A to B with the supplied rate q(t)=k*t, where t is time since the interval's start and k=1 unit per minute squared. The stores have enough material and capacity for the stipulated transfer over T=1 minute. Initially A=10 units and B=0.

The donor computes the interval amount:

~~~
Q = integral from 0 to T of k*t dt = k*T^2/2 = 0.5 units.
A(T) = 10 - 0.5 = 9.5 units.
~~~

The receiving simulator takes the initial rate q(0)=0 and holds it throughout the minute. It obtains B(T)=0. The combined stores now total 9.5 units, although the model contains no external removal.

The error is in the exchange. Both components must use the same transferred amount over the same interval. Sending Q=0.5 units and applying A(T)=10-Q, B(T)=Q gives a total of 10 units. C.29.BB supplies the balance; this construction makes the exchange between the two component representations satisfy it.

Now change the requested result: when does B first reach 0.125 units? Under the supplied continuous rate, B(t)=k*t^2/2, so it reaches the threshold at t=0.5 minutes. A receiver that inserts the entire amount only at T=1 minute reports a different crossing time despite preserving the final balance.

For that question, send or reconstruct the cumulative transfer Q(t)=k*t^2/2 over the interval, or use a computation with adequate intermediate and event resolution. Exchanging only the interval amount is sufficient for the final stores but insufficient for the crossing. The changed question reopens the temporal representation, not the already correct conservation argument.

A nonlinear receiver can likewise need more than an averaged input. Suppose two equally weighted fine cells supply x values (0,2), and the receiver requires the average of x^2. The mean input is 1, but the required response is (0+4)/2=2. Sending only the mean and squaring it gives 1. Supplying variance 1 restores 1^2+1=2; a justified closure could supply the same missing contribution in a larger model.

#### MMP.18:5.2 - Join two analyses without counting their prior twice

Two analyses concern the same binary condition z. Both start from P(z=1)=0.2 and P(z=0)=0.8. Each has one positive observation with the supplied law:

~~~
P(positive | z=1) = 0.75
P(positive | z=0) = 0.25.
~~~

The two observations are distinct and conditionally independent given z. Each separate posterior gives:

~~~
P(z=1 | one positive) = (0.2*0.75)/(0.2*0.75 + 0.8*0.25) = 3/7.
~~~

Multiplying the two posterior mass functions and normalizing gives 9/(9+16)=9/25=0.36. This has counted the shared prior twice.

Construct the joint model from one prior and the two likelihood factors:

~~~
P(z=1 | two positives)
 = (0.2*0.75^2)/(0.2*0.75^2 + 0.8*0.25^2)
 = 9/13, approximately 0.692.
~~~

The same result is recoverable from the separate posteriors by dividing their product by the common prior before normalizing. That operation preserves their intended contributions under the supplied conditional independence.

Now discover that the two reports contain the same observation, copied into two analyses. There is only one likelihood factor. The correct result under the original observation model is again 3/7; the 9/13 calculation is no longer supported. If there are two dependent observations instead, their joint conditional law is needed.

The exchange therefore includes the identity and dependence of the contributing information, not just two numbers labeled “probability.” In a method assessment, the same problem appears when two models of performance use overlapping case records.

### MMP.18:6 - Bias-Annotation

Coupling is often presented through physical simulations, which can suggest that every interface carries a conserved flow. Statistical components instead require coherent shared distributions and dependence. Both cases need an explicit relation between components; the relation's governing property comes from the modeled quantity.

The examples use small equations with known solutions. A large coupled formulation may be well defined but expensive to compute, or locally accurate but poor for the receiving use. Preserve that distinction when choosing a simpler interface or component.

### MMP.18:7 - Conformance Checklist

The coupled construction supports its stated use when:

- the requested combined result and the component contributions needed for it are recoverable;
- shared quantities retain their subject meanings and relevant units, reference points and conditions;
- each consequential exchange has a relation that connects what is supplied to what is used;
- aggregation or scale change retains, obtains or bounds the information the receiving operation needs;
- jointly applicable component and interface conditions hold for the claimed solution;
- computational exchange approximations are distinguished from actual subject delays or events;
- shared uncertainty and evidence have the dependence and multiplicity asserted by the joint model;
- the result retains a consequential limit and a usable return to the contribution that failed.

These conditions recognize the coupled model. Establishing its subject applicability or a numerical error guarantee needs the corresponding subject or computational argument when the use requires it.

### MMP.18:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Connect equal names as equal quantities | Different intervals, references or populations become silently identified | Construct the quantity correspondence before exchanging values |
| Use an interpolation because the tool offers it | A total or constant field may be altered | Derive the preservation condition from the receiving use |
| Pass an average into an arbitrary nonlinear operation | Lost variation changes the result | Derive and supply the missing statistic or closure |
| Treat software call order as the subject law | Inserts a delay or leaves same-instant relations unsatisfied | Formulate the joint conditions, then choose their computation |
| Preserve the final balance and claim the trajectory | Intermediate timing remains unresolved | Retain the temporal information required by the question |
| Multiply fitted component distributions | Can duplicate a prior or shared records | Recover and combine the actual likelihood and dependence contributions |
| Reuse an isolated closure under changed feedback | The coupled system can leave the closure's supported regime | Revise its supply conditions or use a suitable richer component |

### MMP.18:9 - Consequences

A component can be replaced without rebuilding the entire model when its replacement supplies the same required exchange under the same conditions. MATH.18 gives the mathematical comparison; the present method identifies what the neighboring models actually require.

Coupling may reveal that a previously useful component is insufficient or incompatible. The resulting repair can add a shared state, a closure or a joint solve. It can also remove unnecessary detail when the receiving answer depends only on an aggregate already preserved.

For working methods, this helps model the interaction of distinct procedures: a scheduling account may consume a resource or duration distribution supplied elsewhere. The coupling explains that mathematical dependence. ME retains the interpretation and change of the working procedures.

### MMP.18:10 - Architectural Rationale

The general relation-composition method supplies the way to impose conditions together. Model coupling adds the construction needed when those conditions use different representations, scales or overlapping information. It makes the supplier's result usable by the receiver.

A separate interface relation keeps three possible repairs distinguishable: change a component, change how its contribution is represented, or change the computation of their joint conditions. Without that distinction, solver adjustments can conceal a subject-model error, while a harmless numerical approximation can provoke an unnecessary redesign of the subject account.

Conservation and probabilistic coherence are different preservation questions. Their coexistence here reflects a common modeling task, not an assertion that a probability distribution is a physical flow. The appropriate mathematics remains with its governing pattern or specialist method.

### MMP.18:11 - SoTA-Echoing

**Interoperable components still need a coupling construction.** The Modelica Association's *Functional Mock-up Interface* 3.0.2, §§3–4, distinguishes exchanging model equations from co-simulation and leaves the coordinating solver to the importer. This supports :4.4: an interface format does not select the numerical interaction or establish its error. Reusing existing simulators remains valuable when their exchange capabilities support the required result; a joint solve is the alternative when independently advanced components do not. [Specification](https://fmi-standard.org/docs/3.0.2/).

**Choose a map by what it preserves.** The current preCICE documentation, “Mapping configuration,” distinguishes sum-preserving maps, constant-field interpolation and weighted integral preservation. The adopted move in :4.2 is to derive the required map property from the exchanged quantity. The documentation's mesh algorithms are useful specialized realizations, not universal choices for every representation. A cheap nearest-neighbor map can suffice when its error and preserved quantities fit the use. [Source](https://precice.org/configuration-mapping).

**A common unknown needs a coherent joint distribution.** Goudie and colleagues, *Joining and splitting models with Markov melding* (2019; arXiv v3), §3, constructs combinations through shared variables and addresses inconsistent marginal priors. This supplies a serious alternative to informal transfer of fitted summaries. The simple common-prior case in :4.5 and :5.2 is adopted here; more general pooling requires its additional assumptions. [Read version](https://arxiv.org/html/1607.06779v3). Manderson and Goudie, *Combining chains of Bayesian models with Markov melding* (2023), extends the construction to distinct shared quantities along a chain while retaining their dependence. That extension matters when one shared variable cannot represent all interfaces; an arbitrary network or dependent evidence still requires its own joint construction. [Source](https://arxiv.org/html/2111.11566v2).

**Scale interfaces can need learned or derived closures.** Sanderse and colleagues, *Scientific machine learning for closure models in multiscale problems: a review* (2024), §2, locates the missing contribution when reduction and evolution do not commute. That result supports :4.3's return to MMP.9 or a suitable surrogate. A learned closure is one candidate alongside derived memory, retained state and sufficient bounds; its isolated fit does not settle its coupled use. [Source](https://arxiv.org/html/2403.02913v2).

Revisit the coupling when a component, exchange representation, shared data, scale or receiving result changes. A new numerical or learned method is useful when it improves that same coupling under its applicability conditions and available resources.

### MMP.18:12 - Relations

- **A.3.3.TR** constructs joint change rules and **A.3.3.PI** tests whether retained information suffices for the needed continuation.
- **C.29.1** transfers a result between mathematical accounts. **C.29.BB** constructs a balance whose exchange this pattern may need to preserve.
- **MATH.18** compares mathematical accounts and the consequences their interpretations carry.
- **MMP.10** formulates constraints on the combined possibilities; **MMP.9** derives reduced evolution and closures.
- **MMP.7** supplies the observation law and **MMP.13** the inference under the combined probabilistic assumptions. **MMP.14** investigates a failed model prediction.
- **MMP.17** constructs a surrogate for a needed contribution. Its approximation conditions remain relevant inside the coupling.
- **CMP.8** controls numerical approximation, while **CMP.14** constructs interactions between computations. These obtain a result from the formulation rather than supplying its subject meaning.
- **PHY.5** selects effective physical descriptions by scales and couplings; **PHY.6** supplies physical evolution from balances and response laws.
- **B.5.MPC.R** coordinates repairs across physical, mathematical and computational accounts when the receiving question is physical; **C.11.DUA** compares further coupling work with an adequate restricted answer.
- **ME** consumes the construction when mathematical models of working procedures are combined or changed.

### MMP.18:End
