# Foundational Thinking DPF Suite Reference

> Find the mathematical, physical, computational, modeling or notational contribution your question needs, and understand how the contributions work together.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Date:** 19 September 2026
- **Status:** Eternal alpha. This edition gives working entries through all five member DPFs and FPF, with their methods, conditions and connections.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)
- **Suite:** [Purpose, membership and edition rules](./)

If you have a mathematical question already, start with [Mathematical Thinking](MATHEMATICAL-PRACTICE-DPF.md). If you need to turn a subject question into a mathematical one, start with [Mathematical Modeling](MATHEMATICAL-MODELING-PRACTICE-DPF.md). For a physical account, consequence or observation, start with [Physical Thinking](PHYSICAL-THINKING-DPF.md). For algorithm construction, interpretation or analysis, start with [Computational Thinking](COMPUTATIONAL-THINKING-DPF.md). For expressions whose rules, interpretation or changes need repair, start with [Notational Engineering](NOTATIONAL-ENGINEERING-DPF.md). When the difficulty lies between contributions, use the question index below.

The linked patterns describe methods; their results still have to be obtained or supplied for your situation. A small example shows what that use can produce. A missing result can require a specialist contribution or a further method; a reference alone does not supply it.

## Contents

| Section | What you can find there |
| --- | --- |
| [1. Start with a working question](#1-start-with-a-working-question) | Nine entries, including their available contributions and limits. |
| [2. What this Suite connects](#2-what-this-suite-connects) | Mathematical, physical, computational, modeling, notational and methodological work. |
| [3. Working combinations](#3-working-combinations) | Construction, changed methods, incomplete information, limits, continued inquiry, algorithms, coordinated expressions and an operating-flow application. |
| [4. Preparation and division of work](#4-preparation-and-division-of-work) | What a reader or collaborator needs to understand and supply. |
| [5. Current repertoire and its limits](#5-current-repertoire-and-its-limits) | What the five DPFs provide and when another contribution is needed. |
| [6. Architectural Rationale](#6-architectural-rationale) | Why these methods form separate languages, how they connect and when to change that arrangement. |
| [7. Sources and conceptual synthesis](#7-sources-and-conceptual-synthesis) | Contributions, alternatives and the limits of their use here. |
| [8. Using and revising an answer](#8-using-and-revising-an-answer) | Substantive checks, changed conditions, source return and citation. |

## 1. Start with a working question

| Your question | First useful answer | Open next |
| --- | --- | --- |
| I can solve familiar equations, but do not know which objects to use here. | State the needed consequence and choose objects by the operations or maps they must support. An observation or subject premise may still need its own inquiry. | [Construct an unfamiliar account](#31-construct-an-unfamiliar-account). |
| Several physical accounts fit what is known. Which difference matters for the work? | Derive their conditional consequences and construct an observation only when distinguishing them changes the next decision. | [Connect physical prediction and observation](PHYSICAL-THINKING-DPF.md#ph-predict-and-distinguish---develop-a-physical-prediction-and-the-test-it-needs). |
| Two ways of working look equivalent. Can I replace one with the other? | Identify what the replacement must preserve. Matching final values can hide a different observation, enabling condition or cost. | [Understand and change a construction](#32-understand-and-change-a-construction). |
| I must act before I know everything. What is worth finding out? | Formulate which information can reach the choice, compare the consequences still possible, and seek only information that can change the decision usefully. | [Choose with incomplete information](#33-choose-with-incomplete-information). |
| The full calculation is too expensive. What may I simplify? | Select the consequence to preserve, derive the contribution removed detail makes, and seek a replacement, approximation or sufficient bound. | [Obtain a result under limits](#34-obtain-a-result-under-limits). |
| A procedure gives a value, but I need a witness, every answer or a different error guarantee. | Reconstruct the required output, retain enough intermediate information and revise only the shortcuts that relied on the old request. | [Construct and change an algorithm](#36-construct-and-change-an-algorithm). |
| A formula, table or diagram is changed. What should its other expressions now say? | Recover the shared references, interpretation and intended edit; retain independent information and expose a loss or conflict. | [Carry meaning through different expressions](#37-carry-meaning-through-different-expressions). |
| A person or AI supplied an answer. Can we use, alter and extend the way it was obtained? | Recover the needed construction and its conditions, try the changed use, and identify the next useful question or missing capability. | [Continue and distribute thinking](#35-continue-and-distribute-thinking). |
| A local process is faster, but its recipient still waits. What should change? | Reconstruct resource occupancy, transfer and admission rules; compute the alternatives and retain the recipient's event boundary. | [Change an operating flow](#38-change-an-operating-flow-without-hiding-its-waiting). |

## 2. What this Suite connects

Knowing a formula can leave its use unresolved. A mathematically valid calculation can concern the wrong objects. A computation can return a value after the opportunity to act has passed. The Suite develops ways to locate and repair such difficulties while retaining the contributions that still work.

| Contribution | The work it does | What another contribution can use |
| --- | --- | --- |
| **Mathematical Thinking** | Construct objects and operations; establish consequences; compare and change constructions. | An object with usable maps, an interpreted expression, an argument, a witness, an obstruction or a qualified approximation. |
| **Physical Thinking** | Identify relevant phenomena, preparation, interactions and constraints; develop and challenge an account of what can happen. | Physical premises, possible changes, a distinguishing observation or a limit on realization. |
| **Computational Thinking** | Construct, understand, analyze and transform algorithms within computer science, including their semantics and interaction. | An algorithm, its representation and correctness, progress and resource conditions, or a limit that changes the requested answer or available operations. |
| **Mathematical Modeling** | Formulate how the subject question, supported relations, unknowns and observations enter mathematics. | A mathematical question whose answer has a stated use in the subject, with the conditions and losses of that use. |
| **Notational Engineering** | Develop expressions and interpretation through which participants can recognize and perform the needed operations. | A usable notation, correspondences between representations and the preparation their readers need. |

Section 5 describes the current repertoire. Choose a method by the contribution the working question needs; combining methods adds value when one result supplies what another requires.

**Methodology connects the contributions to ways of working.** A mathematical construction can describe how operations combine. A physical or computational result can make a different working arrangement possible. Method Engineering then helps construct or change that arrangement, including its observation, action and division of work.

There are two connected questions throughout. How is a claim obtained and warranted? How can its obtaining method and result be used, taught, distributed, changed and continued? Mathematical assumptions, physical premises and computational resource claims need their respective grounds. Their interaction makes a useful inquiry possible; none of the three is recovered merely by relabeling the others.

Here *foundational* means helping enter and develop problems across branches of these fields. A method's conditions still matter: a symmetry method needs a relevant transformation, for example. Further theoretical inquiry can itself be a useful continuation. A problem need not have an immediate commercial application to open a consequential new line of work.

## 3. Working combinations

Use a combination where its intermediate results are needed. Enter with a result already available, take an alternative branch when conditions require it, and stop when the question has a usable answer. The short sequences below explain possible uses; the linked pattern bodies supply the methods.

**Finding FPF and DPF bodies.** Open [FPF-Spec.md](../FPF-Spec.md) or a linked DPF, search for the full PatternID, and read its Problem frame and Solution. A DPF's own Table of Contents links to the bodies and practical entries. For a large file that GitHub cannot display, use View raw or Download raw file and search the downloaded text.

### 3.1. Construct an unfamiliar account

**Recover the question → choose objects and operations → formulate relations → obtain a consequence → interpret it or revise the failed contribution.**

Start with FPF B.5.FM when the mathematical question is missing. [MATH.16](MATHEMATICAL-PRACTICE-DPF.md#math16---choose-a-mathematical-construction-from-its-required-maps-universal-property) chooses a construction from the maps it must support. MATH.1 and MATH.5 can then construct and interpret composable expressions. [MMP.10](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp10---construct-and-revise-a-mathematical-constraint-formulation) expresses admissible subject cases; MMP.11 constructs an unknown relation inside supported conditions. Use FPF C.29 to interpret the consequence through the correspondence between the mathematical account and the working situation.

**Small use.** A cart log records two unit movements. Total distance is two both for forward-then-backward and forward-then-forward. If each entry records an actual signed displacement, assign +1 and -1 and use addition for composition: the final displacements are zero and two. MATH.1/.5 supplies that interpretation. If entries record commands and the cart can slip, the same sum answers a command question. Observation or a movement model must supply the relation to achieved position.

That missing physical account changes what can be concluded. [PHY.4](PHYSICAL-THINKING-DPF.md#phy4---constrain-an-unknown-physical-law-by-transforming-the-situation) develops physical grounds for restrictions on an unknown law. These restrictions can still leave a physical relation unresolved; use supported subject knowledge, observation or a collaborator for the needed premise. B.5.MPC connects the physical, mathematical and computational contributions. Stop with the qualified consequence, or with the particular relation still needed.

The [physical connected-use example](PHYSICAL-THINKING-DPF.md#ph-predict-and-distinguish---develop-a-physical-prediction-and-the-test-it-needs) follows an unknown response through a balance, a conditional prediction and a distinguishing observation. It shows when an experiment is unnecessary and which premise to revisit after conditions change.

### 3.2. Understand and change a construction

**Recover the operations → identify the result to preserve → compare their compositions → carry the consequence into the changed work.**

FPF B.5.RC and B.5.RA recover a construction or argument. MATH.1/.5 builds and interprets operation sequences; [MATH.2](MATHEMATICAL-PRACTICE-DPF.md#math2---treat-objects-as-the-same-while-preserving-operations-quotient) tests whether identifying descriptions preserves the required operations and answer. MATH.16 treats functions as objects with evaluation maps.

**Small use.** Let a stored quantity initially be 1. Operation R returns its present value; W doubles the stored quantity. Performing R then W and W then R both leaves 2 stored. The returned reading is respectively 1 and 2. If the next action uses that reading, equivalence based only on final storage loses the difference the action needs.

[Method Engineering](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md), especially ME.3 and ME.7, supplies the working-method account and composition question. Use FPF C.29 to establish what the mathematical elements and operations represent in that work, and which conclusions the correspondence supports. ME.12 checks claims about the description; it does not construct the replacement method.

[MATH.17](MATHEMATICAL-PRACTICE-DPF.md#math17---construct-mathematical-spaces-of-operations-and-operations-on-them) constructs transformations of rules and derives the laws their use needs. [MATH.18](MATHEMATICAL-PRACTICE-DPF.md#math18---compare-mathematical-accounts-through-interpretations) compares descriptions through interpretations and recoverable consequences. For example, preserving how operations compose can permit a calculation in the second description; recovering the first answer also needs a return that retains its required distinctions.

[CMP.14](COMPUTATIONAL-THINKING-DPF.md#cmp14---compose-interacting-computations-through-their-required-observations) develops the algorithmic interaction: expose shared state and allowed observations, construct coordination, and retain separate correctness and progress arguments. [CMP.12](COMPUTATIONAL-THINKING-DPF.md#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) supplies interpretation or translation when executable descriptions change.

[ME.6.MC](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6mc---compare-method-arrangements-through-a-mathematical-model) derives the consequences of proposed arrangements under a mathematical account of the work. [ME.25](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me25---transform-a-method-using-a-mathematical-construction) uses a mathematical transformation to construct a changed working procedure. The [connected ME example](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me-model-and-change---use-a-mathematical-construction-to-change-how-work-is-divided) develops local summaries for a distributed calculation, then changes those summaries when the recipient asks for another statistic. The mathematical preservation argument supplies one ground for the change; available performers, timing and practical benefit remain working questions.

For a longer construction, use [MP-COMBINE-RESULTS](MATHEMATICAL-PRACTICE-DPF.md#mp-combine-results---change-a-rule-so-that-separately-obtained-results-can-be-combined). It follows an unreliable aggregation rule through a counterexample, compatible summary, operation on summaries and proof, then reopens retained information when the answer changes. Each contribution supplies a result the next uses.

### 3.3. Choose with incomplete information

**Recover the available information → formulate the allowed choice → compare consequences → act, revise the requirement or obtain a useful missing indication.**

[MMP.8](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp8---formulate-information-dependent-choices-mathematically) formulates what may depend on information available at the time of choice. When a probabilistic recording question is needed, MMP.7 derives the record's law. FPF C.16.IR addresses what an observation relation distinguishes, including bounded indications. C.11.DUA compares the value and cost of further inquiry. The MMP Readme's observation-to-action entry connects these contributions with a usable instruction.

**Small use.** One resource must go to one of two requests. A report identifies the request that needs it with probability 0.8 in the first circumstance and 0.7 in the second. Following the report meets a requirement of at least 0.65 success in either circumstance, provided the report arrives before allocation. A zero-failure requirement remains unmet. If the first circumstance instead has probability 0.95 and the criterion is average success, always choosing it gives 0.95, while following the report gives 0.795.

The criterion, information and timing determine the next move. The mathematical comparison does not require further evidence when those inputs are already sufficient for the intended decision. A statistical fit is only one way to resolve an unknown. If unresolved alternatives all permit the same action, a bound may suffice. Observational agreement also leaves an intervention question open when it depends on an unestablished mechanism.

[MMP.12](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp12---formulate-an-inverse-problem-and-choose-whether-and-how-to-use-regularization) formulates recovery from records and makes any added restriction or penalty explicit. [MMP.13](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp13---infer-unknowns-statistically-under-a-stated-observation-model) constructs an inferential conclusion and propagates its uncertainty to the requested quantity. [MMP.14](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp14---find-and-repair-a-mathematical-models-failed-predictions) constructs a comparison for a consequential discrepancy, revises the implicated component and recalculates the receiving prediction. Use these contributions where the existing law or bound leaves that work unresolved.

[MMP.15](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp15---identify-an-intervention-effect-from-available-data) determines which intervention consequence follows from the available data and causal assumptions. [MMP.16](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp16---design-observations-to-separate-mathematical-model-alternatives) constructs an obtainable observation that separates a consequential ambiguity and compares its benefit with its burden. [MMP.8.SD](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp8sd---construct-a-sequential-decision-model-from-information-and-consequences) retains the information and change law needed for continuing choices.

For a question about the same observed case under another action, [MMP.19](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp19---construct-and-bound-a-mathematical-counterfactual-comparison-under-a-causal-model) connects factual inference with changed mechanisms through common underlying conditions. It constructs a joint or nested comparison, or bounds what remains ambiguous. An expected-outcome choice can still be settled by the intervention distributions alone.

The [intervention-and-information example](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-intervention-and-information---decide-whether-an-observation-will-improve-the-next-action) connects these methods: use the supported intervention losses, derive the possible reports, choose whether to observe, and make the later action depend on the received report. If the report no longer distinguishes the possibilities, the observation ceases to justify its cost.

### 3.4. Obtain a result under limits

**State the consequence to retain → derive what removed detail contributes → obtain a replacement or bound → interpret the result at its supported reach.**

[MMP.9](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp9---derive-a-reduced-mathematical-model-of-state-evolution) develops this operation for evolution laws. FPF C.29.2 connects a question with an obtaining process; C.29.3 connects that process to physical means. Use the MMP Readme's reduction entry when the removed detail is the difficulty.

**Small use.** Suppose two nonnegative populations satisfy x'=-x and y'=-2y, with x(0)+y(0)=1. Retain only z=x+y. Its derivative is -x-2y, which z alone does not determine: at z=1 it can be -1 or -2. Yet the source laws give e^(-2t) ≤ z(t) ≤ e^(-t) for t≥0. At t=3 the upper bound is below 0.05. A question asking whether the remaining total is below 0.1 is settled without recovering the initial split. At t=1, a changed threshold of 0.2 lies between the two bounds, so deciding whether the total is below that threshold requires more about the initial split.

A smaller model can therefore be sufficient for one decision while lacking a complete evolution law in the retained quantity. New interventions or a different time horizon can require the missing distinction again. FPF's ordinary comparison and improvement methods can retain several complementary models.

[MATH.20](MATHEMATICAL-PRACTICE-DPF.md#math20---bound-a-mathematical-unknown-by-comparable-constructions) now supplies the general bounding method: derive a comparison covering all admitted cases, carry it through the needed operation, and tighten it only if the answer needs more. [MATH.21](MATHEMATICAL-PRACTICE-DPF.md#math21---construct-an-object-through-convergent-approximations) constructs limits and justifies the operations performed on them. Physical Thinking supplies [PHY.3](PHYSICAL-THINKING-DPF.md#phy3---derive-a-physical-limit-from-permitted-transformations) for limits derived from permitted physical transformations, and [PHY.5](PHYSICAL-THINKING-DPF.md#phy5---choose-an-effective-physical-description-by-scales-and-couplings) for choosing which effects must be retained. [CMP.8](COMPUTATIONAL-THINKING-DPF.md#cmp8---construct-an-approximate-computation-with-controlled-error) constructs an effective approximation and finite return condition; [CMP.9](COMPUTATIONAL-THINKING-DPF.md#cmp9---construct-a-randomized-estimator-or-sampling-procedure) constructs sampling and estimation. Numerical procedures are one application of these algorithmic methods. [MMP.17](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp17---construct-a-surrogate-for-selected-model-responses) constructs a cheaper supplier of the responses the receiving operation needs. [MMP.18](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp18---couple-models-with-compatible-exchanges-and-scales) combines models through compatible exchanges and joint assumptions, retaining consequential approximation and dependence.

The [replacement-and-coupling example](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-replace-and-couple---use-cheaper-models-without-losing-the-combined-answer) sums two distinct amounts with their error bounds. A tighter decision threshold makes one coarse response insufficient; replacing that response can settle the decision without refining the other model. Asking when the threshold was crossed requires temporal information that the final amounts do not contain.

The full [MMP-SUFFICIENT-ANSWER example](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-sufficient-answer---answer-the-working-question-before-reconstructing-every-detail) works this connection across MMP, MATH and FPF. Its changed-time question derives the particular initial-state distinction worth recovering.

### 3.5. Continue and distribute thinking

**Expose the missing contribution → recover or obtain the method → use it under changed conditions → choose a worthwhile next question → retain the way of obtaining and using the result.**

FPF B.5.RC/RA recovers the needed construction or argument, B.5.RR follows changed premises, and B.5.QD develops a further question. C.40.CD connects developing problems with developing ways to address them; C.36.RP addresses retaining and renewing methods. MATH.19 constructs a missing argument, MATH.22 follows a change of axioms through its consequences, and MATH.23 develops a next conjecture from a changed construction. [MATH.4](MATHEMATICAL-PRACTICE-DPF.md#math4---construct-a-witness-by-induction) constructs a witness by induction; [MATH.12](MATHEMATICAL-PRACTICE-DPF.md#math12---extract-a-construction-from-a-proof) extracts a construction from a proof.

**Small use.** Ask for a rule that selects one member of an unordered two-element set and respects renaming. Swapping the elements leaves the set unchanged but moves either possible selection. Such a rule is impossible. MATH.13/.9 exposes the obstruction. Adding a distinguished member permits a choice; returning both members changes the requested answer. A program that takes the first stored element uses an ordering that the original question did not provide.

This obstruction opens useful next questions: may the representation introduce an order, does the intended work permit that extra structure, or does it need the whole set instead? A mathematical, computational and methodological discussion can now concern the same identified difference.

**Make the next contribution obtainable.** First locate what prevents its use: an unavailable input, an unexplained relation, an operation the recipient cannot yet perform, or a contributor they cannot reach. C.36.RP distinguishes these repairs. [DOCA.3](../Engineering%20DPF%20Suite/DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md#doca3---construct-a-worthwhile-problem-and-proposed-contribution) formulates what a development opportunity could supply; [DOCA.4](../Engineering%20DPF%20Suite/DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md#doca4---construct-development-directions-with-their-support-configurations) constructs prospective ways to obtain it, including help, access, learning and changed work, with the support each requires. Use an adequate existing arrangement when it already supplies the contribution.

For an explanation, [EXD.1](../Engineering%20DPF%20Suite/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd1---establish-and-revise-what-a-recipient-needs-explained) identifies the relation this recipient needs. [NOT.3](NOTATIONAL-ENGINEERING-DPF.md#not3---give-expressions-an-operative-interpretation) supplies the reading procedure; NOT.7 can repair an expression that makes the operation difficult. When a human needs practice in using the relation, [HCD.6](../Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd6---design-representative-practice-tasks) constructs a task from the later work and its permitted help. [EXD.5](../Engineering%20DPF%20Suite/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd5---guide-a-recipients-own-explanation) can guide the person's explanation and a revealing retry. Use the response to decide what help is still needed. Reading a worked answer supplies no observation of that person's learning. If later work requires retention or transfer, test performance in those conditions. Use the appropriate training or configuration method when an AI contributor needs a new capability.

**Connected use: develop a selection method that a team can change.** The following is a constructed design example, not an observed training result. A dispatcher must choose one of two equally eligible requests. Their identifiers are arbitrary: exchanging the identifiers must exchange which request a deterministic rule selects, while changing nothing else. The two-element obstruction above shows why those conditions cannot all hold. Choosing the first identifier introduces an ordering the requirement did not authorize. B.5.RA and MATH.13 recover the reason; EXD.1 makes that missing relation the explanation's target.

The team now has a consequential choice. It can supply a meaningful priority, request both items, or change the requirement to equal *probabilities* of selection. These changes answer different questions. Suppose the receiver permits the last option. [MATH.23](MATHEMATICAL-PRACTICE-DPF.md#math23---develop-a-conjecture-by-changing-a-construction) develops the changed claim: a uniform distribution on a finite eligible set is preserved by renaming, because renaming permutes equal probabilities. For two requests, an available unbiased random bit assigns probability one half to each. [CMP.9](COMPUTATIONAL-THINKING-DPF.md#cmp9---construct-a-randomized-estimator-or-sampling-procedure) supplies the construction and its randomness conditions. A temporary ordering can map the two bit values to the two requests; the distribution remains uniform after renaming even though a particular bit value need not select the corresponding renamed request. The resulting guarantee concerns the distribution.

This result permits a division of work. One contributor can establish the selection law, another obtain and implement the random choice, and the receiving dispatcher decide whether probability-based fairness serves the work. People, AI and tools may provide these contributions in different combinations. [ME.6.MC](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6mc---compare-method-arrangements-through-a-mathematical-model) and [ME.25](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me25---transform-a-method-using-a-mathematical-construction) connect the mathematical account to a changed working arrangement: the selected request has to reach the performer, and the permitted source of randomness has to be available. Choose which derivations each contributor needs for their part; the receiver must understand which guarantee the arrangement supplies.

If a human dispatcher can run the routine but says that one unlucky choice disproves equal probability, the explanation has a specific target. Show the two equally likely bit outcomes and their respective requests; ask which outcomes are possible under equal probabilities and what one selection can establish. For practice, change the condition to an available bit that returns 1 three quarters of the time. Directly mapping its values to the requests no longer gives equal selection probabilities. The learner can identify the failed assumption and return the need for another random-choice construction; they need not invent a randomness extractor to make that useful return. HCD.6 and EXD.5 supply the practice and assistance choices. An actual response would support a conclusion about that attempt under its stated help, not a claim of general competence.

**Changed working arrangement.** Two dispatchers now act simultaneously, and each eligible request may be assigned only once. Independent fair choices select the same request with probability one half: of the four equally likely pairs AA, AB, BA and BB, two repeat a request. The earlier marginal fairness calculation remains true for each dispatcher but does not meet the new joint requirement. [CMP.14](COMPUTATIONAL-THINKING-DPF.md#cmp14---compose-interacting-computations-through-their-required-observations) exposes the shared state and permitted histories. A single allocator can randomly permute the two requests and assign distinct entries, or coordinated dispatchers can use an available indivisible claim-and-remove operation. For the latter arrangement, a failed claim must lead to the remaining eligible request; its progress also depends on the service and communication conditions. ME then reconstructs the corresponding allocation and support arrangement. The mathematical calculation alone does not install that service or give a performer access to it.

The new problem is worth pursuing because its answer enables parallel assignment without duplicate work. C.40.CD connects that receiving need to the changed method; MATH.23 can investigate how the construction extends to larger sets. A first inquiry can compare allowed assignment histories with the two independent choices, before investing in a general implementation. If one dispatcher already meets the work's needs, this branch can remain a future opportunity; continuing research is not a condition for using the current result.

Keep what another contributor will need to renew the method: the chosen fairness meaning, the construction, its randomness and coordination assumptions, and a case exposing the difference between separate and joint guarantees. C.36.RP also retains access to the needed help or executor. This preserves a way to obtain, explain and change the answer. The same sequence can begin with a failed physical interpretation, an unfamiliar proof or a changed notation: recover the consequential relation, obtain the missing contribution, use it in the receiving work, and let the result open a justified next question.

### 3.6. Construct and change an algorithm

**Specify the required answer → construct its obtaining procedure → share or summarize only what the answer permits → bound cost and error → use the result → revise the changed dependency.**

[CMP.1](COMPUTATIONAL-THINKING-DPF.md#cmp1---solve-one-problem-through-another-or-transfer-a-limit-computational-reduction) builds effective conversions and answer recovery when another solver can help. [CMP.2](COMPUTATIONAL-THINKING-DPF.md#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) constructs a recurrence; CMP.3 chooses reuse and order. A mathematical construction or the formulation in MMP supplies their intended objects and answer conditions. It does not supply an algorithm merely by defining the answer.

The [connected CMP example](COMPUTATIONAL-THINKING-DPF.md#cp-answer-under-limits---obtain-the-answer-the-work-needs-within-available-resources) shows how a relaxed bound can finish a search for one best selection. Asking for every equally good selection changes which branches may be discarded and what a shared table must retain. CMP.4 supplies the exclusion rule, CMP.5 the bound and CMP.10 the representation comparison. The mathematical optimum can remain unchanged while its obtaining and output procedure changes.

If a weaker answer is acceptable, CMP.8 constructs an approximation and its error account. If the question concerns every possible algorithm under given access operations, CMP.11 constructs a lower bound rather than extrapolating the cost of one implementation. A changed input promise or tolerated error can reopen that limit. C.29.3 then connects the selected operations to physical execution where that contribution is needed.

These methods also support changing a way of working. A solver can move a contribution to another agent; a changed representation can make sharing possible; an interaction rule can prevent one contribution from invalidating another. C.29 and Method Engineering establish the correspondence to the actual working arrangement. They retain any physical or organizational requirement that the algorithmic argument did not address.

### 3.7. Carry meaning through different expressions

**Recover the operation → establish references and interpretation → preserve or expose translation loss → carry the intended change → revise the affected rule.**

[NOT.1–.3](NOTATIONAL-ENGINEERING-DPF.md#not1---choose-the-distinctions-and-operations-a-notation-must-support) connect the work requirement to formation and interpretation. NOT.4 constructs a transformation under its preservation conditions; NOT.5 exposes what a translation cannot recover; NOT.6 coordinates the useful remaining forms. NOT.7 repairs the resulting reading or editing burden. A single adequate expression can be used without this whole combination.

The [connected NOT example](NOTATIONAL-ENGINEERING-DPF.md#nt-change-together---carry-a-changed-request-through-several-representations) keeps a formula, operation graph and table usable through a parameter change. The table's sampled values do not determine the formula outside those inputs. A new parameter changes derived values while an independent observation remains a record of what was observed. Replacing a supplied variable by repeated sensor reads changes the interpretation again, so an arithmetic rewrite must be reconsidered.

MATH.18 supplies mathematical interpretation and its preservation arguments. CMP.12 constructs an effective interpreter when the expressions must be executed computationally. C.29 and the physical or modeling method supply the correspondence to the measured subject. A human reading a diagram can obtain a consequence without running software; a formal meaning alone does not supply an algorithm for every consequence.

When the expression is a score or gesture, NOT.8 adds the needed pulse, frame, segmentation and reading procedure. The direction a sign represents and the capability to perform that motion are different contributions. Method Engineering helps change the working method when the newly expressed or computed result makes another way of working possible.

### 3.8. Change an operating flow without hiding its waiting

A manager wants work to reach its recipient sooner. A local queue becomes shorter, yet the recipient waits just as long. Begin with the recipient's completion event and trace what a proposed change does to the work before, inside and after the measured operation. [Operations Management](../Engineering%20DPF%20Suite/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) supplies the operating subjects, policies and consequences; this Suite helps construct and interpret the model.

**Connect the question to the arrangement.** Use OPS.1/.3 to identify the requested result and participating work, then OPS.11 to recover consequential relations across resources and services. Distinguish a work route from the people or machines that perform it. Two stations in a diagram can need the same operator; one station can instead contain several interchangeable machines. Recover the intervals during which each resource is needed, including any unattended running time. B.5.MPC connects this account of the work with its mathematical description and computation. A changed physical arrangement can therefore change the answer even when the route diagram stays the same.

A constructed case has four orders available from time zero. Each needs one hour at A, then two hours at B. Each station has its own continuously available resource, jobs use each station in order, and there are no setups, failures or returns. Completion at B makes an order ready for its recipient. Compare transferring all four orders together, transferring each as soon as A finishes, and adding an internal limit of two unfinished orders to that second policy. For each policy, use the earliest permitted starts. When an internal place becomes free, admit the next waiting order immediately.

**Construct alternatives before selecting a sequence.** A.22.CGUS gives the ordinary operation: name the alternatives, their conditions and the facts that enable, block or leave them unresolved. For the unfolding work, ask whether A can start another admitted order and whether B can start a transferred order. E.18.3 gives the conditions for identifying a transformation-flow unfolding structure when the work needs that structural account. The ordinary continuation comparison is sufficient for this calculation.

[MMP.10](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp10---construct-and-revise-a-mathematical-constraint-formulation) turns the scheduling question into time variables and conditions. Let a_i be order i's internal admission, s_Ai and f_Ai its A start and finish, and s_Bi and f_Bi its B start and finish. For the given station order:

- s_Ai is at least a_i and the preceding A finish; f_Ai = s_Ai + 1.
- s_Bi is at least f_Ai and the preceding B finish; f_Bi = s_Bi + 2.
- Batch transfer additionally requires B to wait for every A finish.
- With two internal places and single-order transfer, orders 1 and 2 can enter at zero; each later admission waits for the B completion that frees its place.

Taking the maximum of the stated lower bounds constructs the earliest starts for each fixed policy. [CMP.2](COMPUTATIONAL-THINKING-DPF.md#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) and CMP.3 explain how to obtain these dependent results in order. A spreadsheet or a short program can execute the recurrence; four orders can also be calculated by hand. C.29.2 keeps the calculated schedule and the means of obtaining it distinguishable. If a resource is shared, its competing operations also need a chosen order. Construct feasible alternatives and compare their completion times; the order at each station alone may leave that resource conflict unresolved.

**Compare what actually changes.** The resulting times, in hours, are:

| Policy | B completions | Last completion | Mean from customer arrival | Mean from internal admission |
| --- | --- | ---: | ---: | ---: |
| All orders admitted at zero; batch transfer of four | 6, 8, 10, 12 | 12 | 9 | 9 |
| All orders admitted at zero; single-order transfer | 3, 5, 7, 9 | 9 | 6 | 6 |
| Single-order transfer; two internal places | 3, 5, 7, 9 | 9 | 6 | 4 |

The third policy admits orders at 0, 0, 3 and 5. Its internal residence times are 3, 5, 4 and 4; the excluded waits total eight order-hours. OPS.15 keeps both event pairs available, so OPS.10 compares service from the recipient's waiting origin. Smaller transfer batches improve service in this case. The additional internal limit relocates waiting without further improving those completion times. In another operation, a limit can change interference, returns or service duration; those effects need their own account.

The count-time relation makes the boundary visible. Over the nine-hour empty-to-empty interval, internal unfinished work occupies 16 order-hours. Its mean count is 16/9, equal to the completed-order rate 4/9 times mean internal residence 4. The customer-boundary area is 24 order-hours and mean residence 6. For an observation window that cuts through unfinished orders, count only each residence interval's overlap with that window; averaging the completed orders alone can omit the work occupying it. This finite-window reasoning follows the area construction in [Sigman's notes on Little's Law](https://www.columbia.edu/~ks20/stochastic-I/stochastic-I-LL.pdf), rather than assuming a steady regime or a delay distribution.

**Return to the changed premise.** Suppose one operator must now perform all A and B work, with no overlap. Add that shared occupancy to the model. The work needs twelve operator-hours, so the previous nine-hour finish is impossible. Performing A and B for each order in turn attains twelve hours under these conditions. If a decision requires completion within ten hours, this bound already settles the proposed arrangement. Choosing a remedy returns to the available ways of changing access, work or the commitment; further queue statistics cannot make twelve required hours fit into ten.

OPS.8 uses a chosen comparison to set release and protection, OPS.14 contributes the financial consequences when they matter, and ME.25 helps reconstruct a changed working method. Observation after implementation can reopen the resource occupancy, duration, transfer or completion premise. The example combines a subject account, mathematical constraints, an obtaining procedure, measurement and an operating decision; it is one application of foundational thinking. Its finite orders do not set the scope of the general methods.

### 3.9. Keep the vertical visible while doing the work

Contributions also meet within the same ongoing work. While constructing a model, you may interpret a notation to carry out a calculation that is part of testing a physical account. Ask what the calculation is doing in that inquiry, which constituent operations it needs and which whole conditions constrain them. [B.1.5.EW](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b15ew---recover-how-constituent-actions-enact-encompassing-work) gives that recovery Method.

For example, an engineer computes an average during the analysis of a response experiment. Adding samples constitutes part of computing the average, and that computation is part of the analysis currently under way. If the inquiry changes from average response to the first limit crossing, retaining only the sum and count no longer preserves the required answer. Mathematical Thinking helps identify the lost information and construction; Computational Thinking changes the calculation and its storage; Mathematical Modeling and Physical Thinking retain the observation conditions. Notational Engineering becomes relevant if the expressions hide which quantity or time each value denotes.

Knowing addition and knowing the experiment's purpose can leave the intermediate calculation or interpretation beyond a contributor's present capability. Obtain that contribution, explain or practise it, or change the arrangement. The result can depend on several people or AI agents, but their available contributions and communication must fit together. Successful separate operations do not establish that compatibility. Earlier observations remain earlier work; an ongoing analysis does not imply that the instrument is still observing.

A proposed faster constituent goes through [B.1.5.RS](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b15rs---evaluate-a-constituent-method-replacement-in-its-encompassing-uses): check what each relevant encompassing use needs, what survives and what adaptation is required. This vertical complements the longer result-to-use routes above. It does not prescribe a fixed number of levels or turn the five DPFs into five successive stages.

## 4. Preparation and division of work

The required preparation follows the selected operation. A finite path or set construction may need elementary sets and functions. Deriving a recording law uses probability; varying a curve uses calculus. A reader interpreting the result may need less technical preparation than the contributor constructing its proof, but must still understand the conditions and the consequence used next.

When dividing the work, state the contribution needed: a physical premise, a mathematical construction, an obtaining procedure, an interpretation or a changed working arrangement. Ask the contributor to return its inputs, conditions, useful result and consequential limits. That makes the division inspectable whether one person, several specialists or assisting AI agents provide the contributions.

For example, a cart investigation can divide observation and physical-account work, construction of a state model, calculation, and a controller change. A discrepancy can return to any of them. There is no requirement for four people or for one permanent role per DPF.

You may ask an assistant: “Use the relevant patterns, but explain the result in the language of my work. State any mathematical preparation I need, and explain unfamiliar terms where they affect the next step.” An explanation should let its reader recover the required structure and use it. FPF C.2.8 and Explanation Design address that question; a technically precise sentence can still leave the needed operation unexplained.

If a needed operation is unfamiliar, first decide whether you must learn it or can obtain its contribution from an available source, tool, specialist or AI. [HCD.1](../Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd-1) identifies the human contribution required by later work; HCD.2 and HCD.3 compare development and support from the preparation already available. A model's interpreter may need to understand its assumptions and limits while another contributor builds it. That division changes what the interpreter needs to learn.

For learning, choose a task that calls for the missing operation and the help available in the intended work. HCD.9 guides the attempt, feedback, correction and retry; [HCD.10](../Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd-10) varies practice. [HCD.12](../Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd-12) distinguishes evidence of transfer from evidence of learning a new method with a source. A correct answer supplied by a helper and the learner's own interpretation are separate contributions. Use the observed attempt to choose the next practice or support; claims about faster learning or broad transfer need the comparisons those claims entail. HCD.15 revisits the arrangement when the work or support changes. Reading all five DPFs is not a prerequisite for a useful first contribution.

## 5. Current repertoire and its limits

The Suite publishes **66 pattern bodies in five DPFs**: twenty in MATH, fourteen in MMP, ten in PHY, fourteen in CMP and eight in NOT. These methods form a selected repertoire; their number does not establish completeness of the fields.

| DPF | Published repertoire |
| --- | --- |
| [Mathematical Thinking](MATHEMATICAL-PRACTICE-DPF.md) - 20 patterns | Formation, operations and interpretations; proofs, witnesses, extraction and countermodels; bounds and convergent approximations; invariants, symmetry and variation; changed axioms and conjecture development. |
| [Mathematical Modeling](MATHEMATICAL-MODELING-PRACTICE-DPF.md) - 14 patterns | Admissible formulations, structured unknown relations, information-dependent and continuing choices, probabilistic recording, inverse recovery, statistical inference, model criticism, intervention effects, counterfactual comparisons, observation design, reduced evolution, surrogates and coupled models. |
| [Physical Thinking](PHYSICAL-THINKING-DPF.md) - 10 patterns | Physical similarity and analogues; limits from permitted transformations; restrictions on unknown laws; effective descriptions by scales and couplings; evolution from balances and response laws; motion from variational principles; macroscopic behavior and fluctuations from weighted microscopic alternatives; measuring interactions; and tests separating rival accounts. |
| [Computational Thinking](COMPUTATIONAL-THINKING-DPF.md) - 14 patterns | Reduction, recursive construction, sharing, search, relaxation, local updates and learning; approximation, sampling, representation and lower bounds; interpretation, abstraction and interacting composition. |
| [Notational Engineering](NOTATIONAL-ENGINEERING-DPF.md) - 8 patterns | Expression requirements, formation and binding, interpretation, transformation, translation with loss recovery, complementary representations, redesign around difficult operations, and temporal or embodied notation. |

The collaborating Method Engineering methods are outside these 66: ME.6.MC compares method arrangements mathematically, and ME.25 constructs a changed working method through a mathematical transformation. Their [publication](../Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) belongs to the Engineering DPF Suite.

A new difficulty, source contribution, medium or working condition can require further methods or a specialized profile. Use a suitable source or existing specialist method when it already supplies the needed operation. When the current language cannot provide a promised result, identify the missing operation and revise the affected method or its connections.

## 6. Architectural Rationale

**Separate languages preserve developed methods and their different grounds.** Mathematics has constructions and warrants that remain useful across many subjects. Physical premises concern phenomena and possible changes. Computational methods concern how an answer is obtained. Modeling constructs the relation between a question and its mathematical account; notation helps participants perform and interpret the operations. A single large language would make these fields harder to enter and revise independently.

**The Reference preserves connections that a catalogue loses.** A supplied mathematical object does not determine which observation refers to it. A physical law does not by itself supply an affordable calculation. An obtaining procedure must return something the receiving question can use. The entries therefore state intermediate results, conditions, failures and returns. FPF B.5 organizes reasoning and its revision; B.5.MPC and B.5.MPC.R develop coordination and repair for physical questions. This Reference explains selected uses of those contributions while retaining their respective scopes.

**Methods are organized by recurring difficulty and operation.** A thermal balance, optical arrangement, organizational flow or robot can demonstrate a method's use. Its Problem and Solution must still express the general operation when that example is removed. A specialist method belongs in a corresponding narrower body or profile; a broad title cannot enlarge what it teaches.

**Connected increments permit revision of the design.** A construction can reveal a missing operation, duplicated responsibility or incompatible result. The affected architecture then changes while still-useful explanations, proofs, examples and sources are retained. Counting headings or following numerical PatternID order cannot establish coverage. Stable addresses help existing users; Parts and the Table of Contents provide reading order.

**Profiles may overlap and have further refinements.** Specialization adds conditions and methods for a narrower situation. Composition connects contributions; reuse permits one pattern in several profiles; publication grouping organizes the text. These relations can produce a graph rather than one hierarchy. A question about shared generalizations and refinements can call for a further mathematical model. Give the profiles a partial order in which P ≤ Q means P refines Q. A least upper bound is then the most specific common generalization; a greatest lower bound is the most general common refinement. If both exist for every pair, that ordered model is a lattice. Construct it when these common bounds would help answer the question.

Direct use of a textbook or one FPF pattern can be sufficient. The Suite adds value when the work needs developed domain constructions and explicit connections among them. A single applied-engineering collection would instead narrow the promise: pure mathematical construction and development of a physical theory are also intended uses. Factory Physics and operations management are potential applications of the repertoire, not its defining scope.

## 7. Sources and conceptual synthesis

[Fong and Spivak's *Seven Sketches in Compositionality*](https://arxiv.org/abs/1803.05316) develops category-theoretic constructions through several applications. The available MATH bodies use particular constructions, including paths and interpretation; they retain direct finite calculation as an alternative when it suffices. The Suite uses composition across practices without requiring one mathematical foundation for every inquiry. The MATH Preface supplies further source comparisons for universal algebra, constructive proofs, symmetry and variation.

[Sussman and Wisdom's *Structure and Interpretation of Classical Mechanics*, Preface](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/9579/sicm_edition_2.zip/preface001.html), connects physical investigation, mathematical notation and executable procedures. Its functional notation exposes operations hidden by conventional expressions. This supports an important direction here: recover what each expression asks its interpreter to do. Mechanics and Scheme are the book's worked setting; they do not set the Suite's subject or language requirements.

[Frigg and Hartmann's *Models in Science*](https://plato.stanford.edu/entries/models-science/) distinguishes questions about what models are, how they represent and how they support knowledge. The MMP Preface develops its adopted source comparisons further, including Nguyen and Frigg, SIMULA history and equation-based modeling. The Suite consequently asks which use of a model is intended and how its result is obtained and interpreted, instead of prescribing one carrier for every model.

[Rodin's *Axiomatic Method and Category Theory*](https://link.springer.com/book/10.1007/978-3-319-00404-4) compares different ways of forming axiomatic theories, including constructive and categorical approaches. Its methodological question helps explain why this architecture includes operations as objects, comparison of interpretations and changes of axioms. A difference in permitted constructions or equality can itself be investigated. The selected methods let the reader examine such a difference while retaining the grounds specific to each mathematical account.

[Dutilh Novaes's *Formal Languages in Logic*](https://research.rug.nl/en/publications/formal-languages-in-logic-a-philosophical-and-cognitive-analysis) studies formal languages as tools used in human reasoning, including their historical and cognitive effects. This contributes a different question from whether a string is well formed: which reasoning operations does the notation make accessible, difficult or implicit? Notational Engineering therefore includes interpretation and reader-use changes, alongside expression rules. Extending these methods to AI or embodied carriers is part of this Suite's synthesis; claims about human cognition retain their own scope.

[Marletto, Deutsch and Vedral's *Tests of Constructor Theory*](https://arxiv.org/html/2606.07352v1), especially §§1.4 and 3.2, compares allowed evolution with repeatable performance of a transformation. This informs the separate attention to preparation, physical means, attainable transformations and their limits. Its new physical principles are proposals accompanied by tests. A physical method here must state the principles its consequence uses, so that a different physical account can be compared at the affected premise. This preserves the source's methodological contribution without making acceptance of its whole physical programme a prerequisite.

The organization here is a conceptual synthesis: retaining each contribution's conditions, connecting knowledge with its application, and making the methods themselves available for criticism and change. The small cross-practice cases explain this construction; they do not establish a general learning effect. A changed source matters when it changes an operation, premise, cost, interpretation or useful result. Return to that body's source discussion for the corresponding decision.

## 8. Using and revising an answer

Before relying on a combination, ask what can change the answer:

- Does each needed contribution exist and meet the next operation's conditions?
- Do the observation, information timing, physical preparation and mathematical interpretation describe the same intended situation?
- Does a simplification preserve the consequence now required?
- Can the result be obtained with the available means, or is a bound, reformulated question or different construction sufficient?
- When a premise changes, which contribution must be revised and which can remain?

These questions can be settled within the ordinary reasoning already needed for the work. Additional calculations, observations or records earn their place through the difference they can make; C.11.DUA helps when that trade-off is unresolved.

This Reference's availability statements concern the editions listed in the [Suite account](./). Later membership and edition decisions are recorded there. Reconsider an entry when its supplying edition changes the relevant method, its source becomes unavailable, a use fails at a named connection, or a new contribution changes the useful choice. Historical publication versions remain accessible through the repository.

Copyright © 2026 Anatoly Levenchuk. Licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), except separately attributed material; cited works retain their own licenses. Independent DPF and LPF authors choose their own licenses.

**Citation:** Anatoly Levenchuk. *Foundational Thinking DPF Suite Reference*. [FPF repository](https://github.com/ailev/FPF). Include the date shown at the start of this file. Cite a supplying DPF and PatternID when relying on its method.
