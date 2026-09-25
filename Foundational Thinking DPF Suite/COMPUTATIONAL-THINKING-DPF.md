# Computational Thinking DPF

> A pattern language for constructing, understanding, analyzing and transforming algorithms, including their interpretation and interaction.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 20 September 2026
- **Status:** Eternal alpha: a repertoire open to correction and extension.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF ecosystem repository](https://github.com/ailev/FPF)

Computational Thinking here means algorithmics within computer science. Begin with a question about how to obtain an answer, maintain a required behavior, or change a procedure. Use the Table of Contents to find a relevant method, then open its Problem frame, Solution, worked cases and checklist. The Readme follows worked connections between methods; the Preface explains their rationale, prerequisites and limits.

The reference code **CMP** names this DPF. Its numbers are stable pattern addresses; § shows position within a Part. Numerical algorithms are one application alongside symbolic, discrete, randomized and learning procedures. A computing device enters when its operations or physical limits matter to the algorithm or its realization.

This publication belongs to the [Foundational Thinking DPF Suite](https://github.com/ailev/FPF/tree/main/Foundational%20Thinking%20DPF%20Suite). Its [Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains the mathematical, physical, computational and methodological connections. References such as C.29.2 and B.5.MPC name patterns in [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). Open a supplier when its contribution is needed; revisit a receiving conclusion when that contribution changes.

To cite this edition: Anatoly Levenchuk, *Computational Thinking DPF*, [FPF ecosystem repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Computational Thinking - Readme](#computational-thinking---readme) | Follow worked connections between algorithmic methods. |
| Preface | [Computational Thinking - Preface](#computational-thinking---preface) | Understand the connected methods, their rationale, sources and limits. |

## Part A - Construct an algorithm

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.1 - Solve One Problem through Another or Transfer a Limit (Computational Reduction)](#cmp1---solve-one-problem-through-another-or-transfer-a-limit-computational-reduction) | Usable, evolving | reduction; solver reuse; input conversion; answer recovery; computability; complexity. Can this problem be solved through another one, and in which direction does a limit transfer? | C.29.2 for the required answer and computational model; MATH.17/.18 for composition and interpretation. |
| 2 | [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) | Usable, evolving | recursion; decomposition; induction; sufficient return; termination. What must smaller problems return so that their answers construct the required whole? | MATH.4/.12 for inductive or extracted constructions; C.29.2 for the computational formulation. |
| 3 | [CMP.3 - Share and Schedule Repeated Subcomputations](#cmp3---share-and-schedule-repeated-subcomputations) | Usable, evolving | memoization; dynamic programming; sharing; dependency order; effects; storage; recomputation. Which repeated subcomputations can share an answer, in what order, and what should be retained or recomputed within the memory limit? | CMP.2 for the recurrence; CMP.10 for representation and operation costs. |
| 4 | [CMP.4 - Construct Computational Search with Justified Exclusions](#cmp4---construct-computational-search-with-justified-exclusions) | Usable, evolving | search; branch and bound; pruning; witness; completeness; interruption. Which alternatives can be excluded while preserving the requested answer? | MATH.20 for bounds; CMP.5 for relaxation; MMP.10 for a subject constraint formulation when needed. |
| 5 | [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) | Usable, evolving | relaxation; feasible recovery; upper and lower bounds; approximation. How can an easier problem improve or bound an answer to the original problem? | MATH.20 for comparison; CMP.4 for bounded search; CMP.8 for controlled approximation. |
| 6 | [CMP.6 - Derive an Iterative Computational Update from Local Information](#cmp6---derive-an-iterative-computational-update-from-local-information) | Usable, evolving | local search; iterative update; neighborhood; step choice; noisy feedback; stopping. What does an admissible local change improve, and what follows on stopping? | MATH.10/.20/.21 for variation, bounds or convergence; CMP.7 for learning that needs an update. |
| 7 | [CMP.7 - Construct a Learner from Examples and Feedback](#cmp7---construct-a-learner-from-examples-and-feedback) | Usable, evolving | learning algorithm; rule class; inductive restriction; feedback; training fit; generalization. Which rule should examples select, and what supports its further use? | CMP.4/.6 for selection or updating; MMP.7 for a modeled data source; C.11.DUA for consequential additional inquiry. |

## Part B - Control error and computational cost

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.8 - Construct an Approximate Computation with Controlled Error](#cmp8---construct-an-approximate-computation-with-controlled-error) | Usable, evolving | approximation; scaling; discretization; finite stopping; rounding; conditioning. How can a permitted error reduce computation while retaining the answer quality needed next? | MATH.20/.21 for bounds and convergence; CMP.3/.10 for shared computation and representation. |
| 2 | [CMP.9 - Construct a Randomized Estimator or Sampling Procedure](#cmp9---construct-a-randomized-estimator-or-sampling-procedure) | Usable, evolving | randomized algorithm; sampling; estimator; proposal; dependence; stopping time. Which random procedure supplies the required law or finite-run estimate? | A supplied probability target, with MMP.7 where modeled; CMP.10 for access and storage. |
| 3 | [CMP.10 - Choose a Computational Representation for Its Access and Update Operations](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) | Usable, evolving | data structures; representation; queries; updates; conversion; arithmetic; memory. Which representation makes the required operations affordable? | CMP.2/.3 for compositional summaries and shared work; MATH for preserved structure. |
| 4 | [CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs](#cmp11---derive-a-computational-lower-bound-from-indistinguishable-inputs) | Usable, evolving | lower bound; adversary; indistinguishable inputs; decision tree; communication; error. What must every algorithm in this model observe or communicate? | MATH.19/.20 for argument and bound; CMP.1 for reduction; C.29.2 for the cost model. |

## Part C - Interpret, transform and compose computations

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) | Usable, evolving | interpreter; compiler; semantics; binding; environment; control; observable behavior. How does an expression execute, and what must its translation preserve? | MATH.5/.17/.18 for expression composition and interpretation; C.29.3 when realizing the primitives. |
| 2 | [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](#cmp13---construct-a-computational-abstraction-for-the-property-being-asked) | Usable, evolving | abstract interpretation; reachable states; sound approximation; fixed point; refinement. Which cheaper computation supports this property, and can its counterexample occur? | MATH.2/.18 for identification and interpretation; CMP.3/.4 for scheduling and exploration. |
| 3 | [CMP.14 - Compose Interacting Computations through Their Required Observations](#cmp14---compose-interacting-computations-through-their-required-observations) | Usable, evolving | concurrent algorithm; shared state; protocol; atomicity; interference; progress. Which interactions preserve the required whole behavior? | CMP.3/.10/.12 for dependencies, representation and semantics; C.29.3 for implementation assumptions. |

# Computational Thinking - Readme

## Practical entries

Bring an algorithmic difficulty: how to construct a procedure, preserve its meaning, or make its operations affordable. Computational Thinking concerns the methods of computer science used to answer those questions. Numerical computation is one application alongside symbolic processing, search, program analysis and interacting procedures.

The examples below show how one method's result makes another method usable, including where to branch or return when a condition changes. They are selected uses of the pattern language, not a catalogue or a prescribed workflow. Use the Table of Contents and the patterns' own `Use this when` and `Problem frame` for other questions. Open only the contributions the question needs; a sufficient existing answer does not require a new analysis.

For inexpensive direct help, [CMP.10 - Choose a Computational Representation for Its Access and Update Operations](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) can settle how to make one membership query in an existing unsorted list: a scan may suffice, with no new index to build. Many later queries or a different update workload can change that choice.

You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.” Ask it to follow an input through the proposed operations, retain the assumptions needed by the next method, and explain what the result permits.

### CP-TRANSLATION-SCOPE - A translation works on test inputs; which executions does it preserve?

- **Situation:** Expressions have been translated to a machine with different arithmetic, and a few successful tests do not settle the permitted input range.
- **Question:** Under which input conditions does the translated program preserve the required result?
- **First useful result or blocker:** A source-to-target correspondence with an established input condition, or a concrete mismatch or unresolved condition preventing that claim.
- **Start with:** [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation). If the correspondence depends on a property of possible executions, use [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](#cmp13---construct-a-computational-abstraction-for-the-property-being-asked) to obtain that premise.
- **Stop or return:** Use a sufficient correspondence on its established scope. Changed inputs or machine operations reopen the affected premise. An abstract warning alone is not a demonstrated failing execution.

For example, the source computes `(x + 1) * (x - 2)` with unbounded integers. The target uses unsigned 8-bit arithmetic, wrapping modulo 256. CMP.12 specifies evaluation and translation: evaluate each operand in order, pop the right operand before the left, and append the expression's result without changing an existing stack prefix. At `x = 5`, both executions produce 18. That test does not establish correspondence for other inputs.

Suppose the allowed integers satisfy `2 <= x <= 16`. CMP.13 can compute ranges at the expression's intermediate steps: `x + 1` lies in `[3,17]`, `x - 2` in `[0,14]`, and their product in `[0,238]`. These ranges cover every source execution under the stated input condition. No arithmetic intermediate overflows the target range. This discharges the arithmetic premise of CMP.12's correspondence argument; it does not replace the argument about operand order and preservation of the stack.

Now allow `x = 17`. The source returns 270 and the target 14. The changed range calculation warns that wrapping is possible; this concrete execution establishes an actual mismatch. Return to CMP.12 to choose wider arithmetic, retain a justified input restriction, or explicitly change the intended arithmetic. Do not “repair” the analyzer by removing a real input. For a different abstract warning, CMP.13 checks the proposed execution against the original computation. If reconstruction establishes that a lost distinction produced an impossible path, refine that distinction; failure to resolve a path is not proof that it is impossible.

The same connection can supply a premise about control, binding, errors or effects, but it needs an abstraction for that property and the actual execution rules. A range argument establishes none of those other properties by itself. The direct patterns give those constructions beyond this arithmetic example.

### CP-ANSWER-UNDER-LIMITS - Obtain the answer the work needs within available resources

- **Situation:** A finite selection problem is expensive; changing from one best selection to every best selection can invalidate a shortcut.
- **Question:** How can construction, sharing, bounds and retained information preserve the answer now required?
- **First useful result or blocker:** An answer-producing procedure with justified exclusions and sufficient reconstruction information, or the specific resource limit it cannot meet.
- **Start with:** [CMP.2](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition), then [CMP.3](#cmp3---share-and-schedule-repeated-subcomputations) when subproblems repeat. A useful bound from [CMP.5](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) can justify exclusions in [CMP.4](#cmp4---construct-computational-search-with-justified-exclusions).
- **Stop or return:** Stop at the answer sufficient for the work. Changed data, completeness or permitted error reopen the choices that depended on them; a faster value computation need not retain every witness.

First specify whether the result is a value, one selection attaining it, all such selections, or an allowed approximation. [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) constructs subproblems with enough returned information to assemble that answer. [CMP.3 - Share and Schedule Repeated Subcomputations](#cmp3---share-and-schedule-repeated-subcomputations) uses their identity and dependencies to decide what can be computed once, when it is needed, and what must remain available for reconstruction.

CMP.Preface:4 supplies a small connected case. Each distinct item may be selected at most once; costs and values add, and capacity is 5.

| Item | Cost | Value |
| --- | ---: | ---: |
| A | 4 | 7 |
| B | 3 | 5 |
| C | 2 | 3 |

Let `R(i,b)` be the best value using the first `i` items within capacity `b`. CMP.2 separates exclusion of the next item from its feasible inclusion. CMP.3 shares each resulting `(i,b)` subproblem. The final values for capacities 0 through 5 are `0, 0, 3, 5, 7, 8`; B+C attains 8. Keeping only two rows can save value-storage, but recovering a selection still needs choices or justified recomputation. CMP.10 chooses a representation for those actual accesses and retained distinctions. The table uses order `nW` updates for `n` items and integer capacity `W`; that is not a polynomial bound in the number of bits encoding `W`.

If exploring alternatives remains expensive, [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) permits fractional items to obtain an upper bound. A plus one third of B gives the fractional optimum `26/3`. Since original values are integers, they cannot exceed 8. B+C reaches 8, so the optimum is already settled. [CMP.4 - Construct Computational Search with Justified Exclusions](#cmp4---construct-computational-search-with-justified-exclusions) consumes such a bound to exclude alternatives; it does not treat an arbitrary relaxed candidate as an upper bound.

Now add D with cost 4 and value 8, and request **every** optimal selection. Both D and B+C must survive. The old bound concerned a different item set: D plus one quarter of A gives the new fractional optimum `39/4`, so its integer upper bound is 9 and does not alone settle optimality. The updated recurrence gives optimum 8. At its final state both the exclude-D and include-D branches attain 8; following both recovers the two selections.

The output change also changes pruning: for one optimum, an upper bound `U <= L`, where `L` is an attained value, excludes a branch that cannot improve it. For all optima, equality can hide another required selection, so this exclusion needs `U < L`. Storing only the cheapest selection for each value would keep D and discard B+C; following ties later cannot restore information already lost. Return to the recurrence and retain the required choices and item identities. Listing all answers can itself require much more work than computing their common value.

If a near-optimal answer would actually suffice, [CMP.8 - Construct an Approximate Computation with Controlled Error](#cmp8---construct-an-approximate-computation-with-controlled-error) changes the permitted error and construction; it does not answer the request for all exact optima. If the disputed question is what *any* algorithm must spend, [CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs](#cmp11---derive-a-computational-lower-bound-from-indistinguishable-inputs) requires a stated access and cost model. One slow implementation establishes no such limit. Other selection problems need their own sufficient subproblems and valid bounds; the item table is an example of the joins, not their scope.

### CP-RETRY-AND-RECOVER - Share calculations without merging requests or repeating their effects

- **Situation:** Requests repeat expensive calculations, replies can be lost, and a restart can erase some remembered results.
- **Question:** Which work may be shared while each logical request still has its required effect and reply?
- **First useful result or blocker:** Distinct reuse and request identities, a retention rule and a composed procedure, or the missing atomic operation or delivery condition.
- **Start with:** [CMP.14](#cmp14---compose-interacting-computations-through-their-required-observations) for required observations; [CMP.3](#cmp3---share-and-schedule-repeated-subcomputations) for reusable calculations; [CMP.10](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) for retained records. Return their results to CMP.14's interaction argument.
- **Stop or return:** Keep a sufficient existing procedure. Changed effects, record retention or failure conditions reopen the affected claim. At-most-once effects alone promise neither a reply nor a deadline.

Suppose a request runs a deterministic calculation `f(x)` and adds its result to a shared counter and returns the counter value immediately after that addition. For the input in this example, `f(x) = 5`, and the counter starts at 0. [CMP.14 - Compose Interacting Computations through Their Required Observations](#cmp14---compose-interacting-computations-through-their-required-observations) first distinguishes the intended observations: two independently intended requests must add twice; a retransmission of one request must not add again. A lost reply does not show whether the first addition occurred.

CMP.3 supplies a different distinction. A pure calculation of `f(x)` may be shared when its inputs and governing version make its returned result interchangeable. That reuse does not identify two independently intended additions. Give a logical request its own identifier `k`, reused only by its attempts, and keep its payload consistent. Two requests with the same `x` may reuse the calculated 5 while still adding 10 in total. If the calculation is cheap, there is no need to cache it.

These two identities determine what CMP.10 must represent: a cache for calculation results, when worthwhile, and a separate map from completed request identifiers to their payloads and returned results. Discarding a pure calculation's cache entry only causes recomputation under the same conditions. Discarding a request's completion record while an old attempt can still arrive can repeat an effect. The records' retention rules cannot be borrowed from one another merely because both look like tables.

CMP.14 uses those records in the actual interaction. After obtaining the amount, the receiver must atomically either find `k` completed and recover its original reply, or add the amount and record that reply as `k`'s completed result. Sending the reply may follow. For one request the counter becomes 5; loss of its reply followed by a retry returns the stored 5 without another addition. A genuinely new request adds another 5 and receives 10. A later retry of the first request still receives its original 5. An efficient lookup table by itself supplies no atomicity for this composite operation.

Now let a restart preserve the counter but lose completed-request records. Retrying the first request can raise 5 to 10: calculation reuse may remain correct while the composed effect is wrong. Return to CMP.14's failure model and CMP.10's retention choice. Effect and completion result must survive together if that guarantee is required. Persisting an identifier in one place and performing an external service's effect elsewhere does not close the crash interval between them; the missing operation or external guarantee remains a blocker.

Finally, keep the response question separate. Avoiding repeated effects does not require eventual message delivery. Eventual response does: it needs adequate retry, delivery, processing and retained-state conditions for both request and reply. Those conditions still provide no fixed deadline. Reopen only the affected assumption when it changes. The same separation applies to shared calculations, updates and message protocols beyond this counter example; the direct methods determine their actual identity, atomicity, storage and progress requirements.

# Computational Thinking - Preface

## CMP.Preface:1 - Problem frame and the algorithmic difficulty

Use this language when you need to construct, understand, analyze or change an algorithm. The work can concern a finite answer, a continuing response, a learning rule, or several processes whose interaction matters. A practitioner may be designing the procedure, reviewing one produced by an AI agent, explaining why it works, or deciding how to divide the work among implementations and performers.

A mathematical definition can specify the desired object while leaving its obtaining procedure unknown. An algorithm can compute the right value on a small input yet require unaffordable resources on the intended inputs. A program can work in isolation while changing its neighbors' observations when used in a larger computation. These are different difficulties; their remedies can need different mathematical constructions and execution assumptions.

The domain here is algorithmics within computer science. The methods concern effective operations, their composition, representations, meaning, correctness, termination, continuing progress and resource requirements. Symbolic manipulation, discrete search, numerical approximation, sampling and learning are branches in which those questions arise. Their worked cases show how to use a method; they supply no universal requirement to know a particular physical theory or programming technology.

Start with elementary algorithmic reasoning: inputs, operations, retained state, outputs and the ability to follow a short procedure. Individual bodies introduce their additional constructions. Recursion uses induction and a progress relation; randomized methods need the relevant probability account; a numerical update can require derivatives or an error bound. A concurrency question needs the proposed shared operations and scheduling assumptions. Obtain a missing contribution or learn it through a suitable example before relying on the result that uses it.

Use a known adequate algorithm directly when there is no construction or interpretation difficulty. If the unsettled question is what the subject model means, return to mathematical modeling. If it concerns whether a machine supplies the required operations, timing or physical resources, connect the algorithmic requirements to physical realization. These returns let the relevant specialist or agent work on the missing contribution.

## CMP.Preface:2 - Forces that shape the construction

| Requirement | Choice it creates |
| --- | --- |
| A useful answer | A decision, one witness, every witness, an approximation and a continuing response can require different procedures. |
| Feasible resources | Conversion, preprocessing, memory, communication and output can dominate the apparent main computation. |
| Sufficient retained information | Sharing or summarizing work saves resources while potentially discarding a later-required distinction. |
| A justified conclusion | Small executions help expose a failure; a general guarantee needs an argument covering its admitted inputs and operations. |
| Useful results under uncertainty | A conditional answer, bound or heuristic candidate can be enough; stronger assurance should change the receiving choice enough to repay its cost. |
| Reuse in a changed setting | A different primitive, observation, input promise or interaction can invalidate a formerly correct construction. |

C.29.2 in FPF supplies the computational formulation: what is represented, what answer is required and which operations and resources are available. C.11.DUA helps choose how much additional inquiry or assurance the work warrants. The CMP methods construct the algorithmic contribution needed under that formulation. They do not require a proof or benchmark that cannot change the next useful action.

## CMP.Preface:3 - The methods and their connections

### CMP.Preface:3.1 - Construct an algorithm

[CMP.1](#cmp1---solve-one-problem-through-another-or-transfer-a-limit-computational-reduction) connects a new computational problem to a solver for another one. Its conversion and answer recovery also determine the direction in which an impossibility or resource result can travel. [CMP.2](#cmp2---derive-a-recursive-procedure-from-a-problem-decomposition) constructs a recursive procedure by choosing smaller problems, sufficient returned information and a reason for progress. [CMP.3](#cmp3---share-and-schedule-repeated-subcomputations) turns repeated subcomputations into a shared dependency structure, choosing evaluation order and what to store or recompute.

[CMP.5](#cmp5---bound-an-optimum-or-recover-a-feasible-candidate-through-a-relaxed-problem) obtains a tractable relaxation and connects its bound or solution back to the original problem. [CMP.4](#cmp4---construct-computational-search-with-justified-exclusions) uses such bounds, or other justified conditions, to exclude search branches without losing the requested result. A feasible candidate can be useful before search finishes; its quality claim depends on the remaining alternatives and available bound.

[CMP.6](#cmp6---derive-an-iterative-computational-update-from-local-information) constructs an admissible iterative change from local information. The neighborhood and progress argument decide what stopping establishes. [CMP.7](#cmp7---construct-a-learner-from-examples-and-feedback) constructs the procedure that selects or updates a rule from examples and feedback. It separates that procedure from the resulting rule and separates successful optimization from what the rule supports on further cases. Search or iterative updating can supply its obtaining operation.

### CMP.Preface:3.2 - Control error and computational cost

[CMP.8](#cmp8---construct-an-approximate-computation-with-controlled-error) turns a permitted approximation into an effective computation with an error and stopping account. Mathematical convergence supplies part of the reasoning; the algorithm still needs usable operations and a finite return condition. [CMP.9](#cmp9---construct-a-randomized-estimator-or-sampling-procedure) constructs sampling and estimation, retaining the target law, dependence and stopping conditions. A random output, a sample distribution and an estimate have different uses.

[CMP.10](#cmp10---choose-a-computational-representation-for-its-access-and-update-operations) derives a data representation from the required access and update operations. It exposes costs moved into conversion, maintenance or output. [CMP.11](#cmp11---derive-a-computational-lower-bound-from-indistinguishable-inputs) proves a lower bound by finding inputs that remain indistinguishable under the allowed observations but require different answers. It constrains all procedures within that model; a changed access operation or tolerated error can reopen the conclusion.

These methods can change the construction in Part A. A prohibitive shared table can motivate scaling, another representation or a weaker answer. A lower bound can redirect the question rather than motivate another attempt at the same impossible guarantee. A randomized construction remains subject to the output conditions the receiving work needs.

### CMP.Preface:3.3 - Interpret, transform and compose computations

[CMP.12](#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) constructs an evaluator or a translation by specifying expression meaning, binding, primitive operations and control. The preservation relation follows what the receiving computation can observe. [CMP.13](#cmp13---construct-a-computational-abstraction-for-the-property-being-asked) constructs a cheaper abstract computation for a selected property, with operations that justify its conclusions and a way to reconstruct or refine an apparent counterexample. [CMP.14](#cmp14---compose-interacting-computations-through-their-required-observations) constructs the shared-state or communication behavior needed when computations interact, including the assumptions under which progress follows.

The returned operations can themselves become objects of further work: an algorithm can interpret another algorithm's description, a translator can transform it, and an abstract procedure can inspect its possible behavior. Mathematical Thinking supplies constructions of operations and interpretations. CMP adds effective execution and its consequences under the chosen computational model.

There is no compulsory fourteen-stage process. A reader with an adequate formulation can enter at a missing bound or representation. A representation failure can return to the recurrence; a semantic failure can return to interpretation; a communication failure can return to composition. Keep the required result and the assumptions of these connections visible when different agents supply the contributions.

### CMP.Preface:3.4 - Constituent actions in ongoing work

Updating a visited set can be part of executing a graph-search algorithm while a route-finding task is under way. Changing the required answer from any route to a route with the fewest edges changes which frontier-selection discipline suffices; a successful visited-set update alone does not establish the stronger result. The practitioner needs to connect the local update, the algorithm's invariant and the route requirement, while retaining its representation and memory conditions. Knowing set operations and the desired route can leave that intermediate algorithmic reasoning missing.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Use the parts of the vertical that can change the present result. A Method described here can require additional capability, available support and compatible resources at other grains.

## CMP.Preface:4 - Worked connection - One best selection becomes every best selection

Suppose a finite list contains individually identified options. Each may be chosen at most once. Costs are positive integers and values are nonnegative integers. A selection's cost and value are the respective sums for its chosen options; total cost must not exceed capacity W. The first request is the maximum value and one selection achieving it. These are stipulated model conditions; whether they describe an actual investment, experiment or production choice is a separate modeling question.

Use three options: A costs 4 and has value 7; B costs 3 and has value 5; C costs 2 and has value 3. Capacity is 5.

**Construct what a smaller problem must return.** CMP.2 defines R(i,b) as the best value using the first i options with remaining capacity b. The base is R(0,b)=0. If option i costs w_i and has value p_i, its recurrence is:

`R(i,b) = R(i-1,b)` when `w_i > b`;

`R(i,b) = max(R(i-1,b), p_i + R(i-1,b-w_i))` otherwise.

Every selection either excludes or includes option i, so these branches cover its possibilities. Both use a smaller i. Store a choice attaining the maximum when a witness is required. For A, B and C, the final values at capacities 0 through 5 are `0, 0, 3, 5, 7, 8`; recovering the choice at capacity 5 gives B and C.

**Share subproblems and compare cost.** CMP.3 computes each needed pair (i,b) once in dependency order. A full table has (n+1)(W+1) cells and O(nW) updates. This is a count of table operations; arithmetic cost depends on the size of the values. Since W is encoded with about log₂(W+1) bits, this procedure can still be expensive relative to input length. Keeping just two value rows reduces storage, but recovering the selection then requires retained decisions or recomputation. CMP.10 helps compare those operations for the actual workload.

**Use a cheaper bound when it settles the request.** CMP.5 allows fractional choices solely to obtain an upper bound. At capacity 5, take all of A and one third of B: the relaxed value is 26/3. The corresponding fractional optimum follows by considering value per unit cost, or by the bound derived in CMP.4's worked case. Original values are integers, so they are at most 8. The feasible B+C selection reaches 8. CMP.4 can therefore finish the optimality question without searching every remaining branch. When a bound does not settle it, the search retains the unresolved alternatives.

**Change the requested answer and a supplied option.** Add D, costing 4 with value 8, and request every optimal selection. The new final value row is `0, 0, 3, 5, 8, 8`. D and B+C both attain 8. D cannot be combined with another option within capacity; the earlier argument bounds all selections omitting D. The old fractional bound does not cover the changed list: the new relaxation can take D and one quarter of A, giving 39/4. That bound alone leaves the integer value 9 unresolved.

A search for one optimum can discard a branch whose best possible value equals the incumbent. A search for every optimum must retain a branch that may contain a different equal-valued witness. Similarly, a table storing only the minimum cost for each value keeps D at cost 4 for value 8 and can discard B+C at cost 5. Recovering all ties in that compressed table cannot recover a selection already discarded for being heavier.

Return to the original recurrence. After computing R, recover every optimal selection by following each branch whose value equals R(i,b), retaining the distinct choices. At (4,5), both exclusion, R(3,5)=8, and inclusion, 8+R(3,1)=8, qualify. They recover B+C and D. CMP.4 supplies the changed exclusion condition; CMP.3 supplies the retained dependencies or recomputation; CMP.10 exposes what a compressed representation lost. The value calculation survives, while the witness procedure changes. Enumerating all witnesses can require exponential output even if the value table is small.

If the work later permits a near-optimal value, CMP.8 can trade a quantified rounding loss for a smaller computation. That different request does not supply every optimizer of the unrounded problem. Select the answer the work needs before choosing the shortcut.

The same connected method can be used with other finite recurrences and search constructions. Independent additivity and integer capacity belong to this example. A different problem may require different state, recurrence and bounds while preserving the need to connect answer, construction, retained information and cost.

## CMP.Preface:5 - Use checks, assumptions and recurring failures

The worked cases use small inputs and explicit operations so that a reader can reconstruct the method and change a premise. A physical machine can provide different arithmetic, atomicity or memory behavior. An empirical data source can violate the probability or feedback assumptions used by an algorithmic argument. Carry those requirements to the appropriate implementation or subject inquiry when they matter to use.

For a combination of methods, check the following substantive questions:

- Does the original question require a value, a witness, complete enumeration, an approximation or a continuing behavior?
- Can each contribution actually obtain what the next one consumes, under the same input, meaning and resource conditions?
- What is retained or discarded by sharing, compression, relaxation, sampling, learning or translation, and can that change the requested answer?
- Which argument covers correctness and which covers termination or continuing progress? Are their operations and assumptions available in this setting?
- When a condition changes, which dependent conclusion must be revised and which earlier work remains useful?

Use the relevant body's checks where its operation enters; an unchanged supplier need not be rederived. Whole-computation costs can include simultaneously retained tables, repeated conversions or shared communication, even when each local operation is affordable.

| Failure invited by the construction | Practical correction |
| --- | --- |
| Memoization identifies calls by visible arguments while ignoring changing state or effects | Include the consequential context or avoid that reuse. |
| An optimum value is taken to supply every optimal witness | Preserve or reconstruct every required choice; account for output size. |
| Local improvement or training fit is treated as a guarantee about a different target | Recover the actual neighborhood, feedback and performance claim. |
| A stationary sampling law is treated as a finite-run independent sample | Establish the finite-run distribution or use an applicable dependence bound. |
| A translation or composition is checked only by its final value | Include the intermediate observations, failures and progress on which its context relies. |
| A model-specific limit is treated as an unrestricted impossibility | State the access and cost model, error and input promises, then examine which change escapes the bound. |

Being able to repeat a trace is useful preparation but leaves transfer to be tried. Ask the learner or assisting agent to change an input promise, required output or execution rule and recover the affected construction. Human learning, an AI agent's immediate performance and a learned rule's statistical generalization are different capability questions; their assessment should fit the intended work.

## CMP.Preface:6 - Consequences and Architectural Rationale

The repertoire makes a computational contribution discussable before a finished program exists. A practitioner can construct a recurrence, identify a missing return, derive a bound, change a representation or expose a failing interaction. These results support implementation, explanation, reuse and further inquiry. Their cost ranges from tracing a few states to constructing a substantial new algorithm or proof.

The organization follows recurring algorithmic work across branches. A catalogue arranged by familiar algorithms is useful when a reader already recognizes the problem and needs an implementation. A textbook organized by mathematical topics can develop deeper theory. This language serves the choice and construction between those points: what operation is missing, how its result will be obtained, and which downstream use it supports. Its fourteen methods are a selected repertoire; a specialized graph, geometric, cryptographic or other algorithm can require additional subject techniques.

Several apparent overlaps are useful distinctions of work. CMP.5 constructs a relaxation and recovery, while CMP.4 decides which search branches its bound can exclude. CMP.3 shares equivalent subcomputations, while CMP.13 deliberately summarizes possibilities for a selected conclusion. CMP.12 preserves the execution meaning needed by a translation, while CMP.14 supplies the interactions needed by the combined computation. Their outputs can be connected without making those methods interchangeable.

Mathematical Thinking supplies objects, operations, arguments and limits; Mathematical Modeling connects a subject question with those constructions. CMP develops effective obtaining procedures and their algorithmic consequences. Physical Thinking and C.29.3 connect required operations to physical interactions, preparation and readout. The computational and physical models must correspond where a claim about execution depends on both. A computational lower bound and a physical performance bound can therefore constrain different aspects of the same proposed system.

Notations and methods of work also matter. An expression can hide binding or evaluation rules that CMP.12 needs to expose. A mathematical model of a working method can use CMP.14 to compare orders and interactions, while the actual organizational roles and responsibilities still require a methodological account. FPF's B.5.MPC coordinates the mathematical, physical and computational contributions; ME develops the corresponding changes to ways of working.

This arrangement permits several routes and several performers. An AI agent can propose code, a specialist can supply a bound and another procedure can check a property. Their contribution remains usable only with the meaning and conditions its receiver needs. A new source or capability can change one construction and the affected connections without replacing the whole language. An unsupported operation becomes a useful next inquiry when resolving it could change what the work can do.

## CMP.Preface:7 - Shared sources, alternatives and relations

Erickson's [algorithm construction material](https://jeffe.cs.illinois.edu/teaching/algorithms/) and Morin's [Open Data Structures](https://opendatastructures.org/) support the connection between a problem, its representations, a constructed procedure and its argument. The bodies retain explicit conversions, recurrences and operation costs. Direct use of a known algorithm remains preferable when constructing another one adds no needed capability.

The approximation and learning sources cited in CMP.5-.9 connect a deliberately weakened or data-dependent answer to the procedure that obtains it. They also expose limits: a recovered relaxed solution needs feasibility and quality arguments; an optimized training criterion leaves generalization conditions to be established. CMP.8 compares its transparent scaling construction with a stronger recent knapsack scheme. CMP.7 compares historical assessment with adaptive assessment under temporal change. Those comparisons justify reopening the corresponding method when another construction changes cost or supported use.

[SICP's evaluator and compiler construction](https://sicp.sourceacademy.org/chapters/4.1.html) supplies an explicit historical demonstration of programs that interpret and transform programs. CMP.12 combines that construction with current behavior-preservation distinctions. Cousot's [Principles of Abstract Interpretation](https://mitpress.mit.edu/9780262044905/principles-of-abstract-interpretation/) develops computable summaries from the properties they must support; CMP.13 compares direct exploration, coarser abstractions and targeted refinement. These approaches answer different questions: a useful overapproximation can deliberately introduce behaviors that a meaning-preserving translation would have to treat differently.

Lamport's [A Science of Concurrent Programs](https://lamport.azurewebsites.net/tla/science-book.html) and the composition, memory and crash studies discussed in CMP.14 support its separation of observable behavior, permitted interaction and progress. Sequential composition is cheaper when interference is absent. More detailed composition arguments earn their place when shared observations or failures change what the whole computation can do. Each body gives the adopted contribution, serious alternative and conditions that would reopen its selection.

The [Suite Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) locates the related publications and explains their shared architecture. C.29.2 supplies computational formulation; C.29.3 physical realization; C.29.1 the transfer between mathematical accounts; C.29 the model-to-subject correspondence. B.5's inquiry methods support the next question when a limit or failure makes the old one insufficient. Notational Engineering supplies methods of expression design as those contributions become available; the operative rules stated in CMP remain usable without an unwritten supplier.

The three Parts group the presentation. The fourteen bodies form a repertoire of related Methods, usable individually or in combinations selected for the question. A particular connected use can describe a composite way of working, but membership in this publication alone does not make every method a mandatory step of that work.

## CMP.Preface:End

# Part A - Construct an algorithm

## CMP.1 - Solve One Problem through Another or Transfer a Limit (Computational Reduction)

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.1:1 - Problem frame

Use this pattern when an unfamiliar computational problem might be solved through another problem, or when you need to determine what an assumed solver would make possible. The useful connection must turn admitted inputs into usable queries and recover the answer required by the original question.

Start by naming the problem to be answered and the problem whose solver will be used. Construct a conversion on one revealing input and say how each possible solver answer returns to the first problem. A working conversion, a failed return condition or a correctly directed impossibility consequence is a useful first result.

A **computational reduction from A to B** is an effective way to solve A using a solver for B. The main route constructs a query and an answer-recovery procedure; a later branch covers several queries. The reader needs elementary algorithms, finite representations, function composition and arguments about termination. The graph example explains its representation and assumes a suitable shortest-path solver. The undecidability example uses the stated halting result as a mathematical premise.

Use an available solver directly when its admitted inputs and answers already fit the question. C.29.2 supplies ordinary computational formulation. The present method develops the missing reduction and what follows from it. Approximate, randomized or physically realized computations require the corresponding answer and resource guarantees when they enter this connection.

### CMP.1:2 - Problem

Two problems can have similar names or output shapes while admitting different inputs or requiring different guarantees. A conversion can lose the distinction that determines the answer, create a target input outside the solver's domain, or leave no effective way to recover the original output.

A reduction can also be used backwards. Solving A through B supplies an A-solver when B is solvable; a known impossibility for A then constrains B. Reversing that implication can rule out a useful algorithm without justification.

The task is to construct the connection, establish its answer relation and effective execution, and carry only the consequence that its direction and resource conditions support.

### CMP.1:3 - Forces

| Force | Tension |
| --- | --- |
| Reusing a solver and preserving the question | The solver may answer a translated problem while the original output or a negative case remains unresolved. |
| Mathematical definition and effective construction | A conversion can be well defined while computing it requires the answer being sought. |
| Computability and resource use | An effective reduction can create instances too large for the intended budget. |
| General limit and restricted use | A universal impossibility can coexist with algorithms for a narrower input class or a weaker answer. |

### CMP.1:4 - Solution

**Local mantra:** specify both answers; construct the queries; recover every relevant answer; establish direction and cost; use the consequence; revise the changed condition.

#### CMP.1:4.1 - Specify the two problems and the intended conclusion

Call A the problem to be answered through B. State each problem's admitted inputs and required outputs. An output might be a value, a satisfying witness, a decision including negative cases, or an approximation with a stated guarantee. Choose the forms actually needed.

For a decision problem, write `A(x)` for the proposition to be decided on input x. A solver must return a correct yes or no and terminate on every admitted input. If a proposed procedure only eventually confirms positive cases, retain that different capability in the problem statement.

For a witness problem, let `Ans_A(x,y)` mean that y is an acceptable answer for x. Specify what the procedure should do when no witness exists if that case is admitted. Use C.29.2 when the answer, representation or available elementary operations still need formulation.

Name the intended use of the reduction: build an algorithm from an available solver, transfer a known impossibility, or derive a resource consequence. This selects what effectiveness, return and cost arguments are needed.

#### CMP.1:4.2 - Construct a query without solving the original problem

Build a terminating procedure f that maps each admitted A-input x to an admitted B-input `f(x)`. Work from the information actually present in x and the operations available to the conversion.

A useful way to begin is to identify what a B-instance must represent about x. Construct its components and relations, then retain any additional information needed for answer recovery. When the input contains a program, a conversion can assemble a new program description with that program embedded in it. Constructing the description and executing the embedded program are different operations.

Check the solver's input conditions. A graph procedure accepting only nonnegative edge weights cannot be used unchanged when the conversion creates negative edges. A procedure specified for finite explicit inputs needs a suitable finite representation.

If producing `f(x)` already requires knowing A(x), the proposed conversion has not supplied the reduction. Replace that step with an effective construction from the available input, or retain it as the unresolved computational contribution.

#### CMP.1:4.3 - Construct answer recovery and establish correctness

For a single-query witness reduction, give a recovery procedure `r(x,z)`. For every admitted x and every answer z the B-solver is permitted to return, establish:

`Ans_B(f(x),z) implies Ans_A(x,r(x,z))`.

The recovery must terminate under those conditions. Include negative outcomes, failure reports or approximation bounds when the A-contract needs them. A single fortunate B-answer is insufficient if the solver may validly return another answer that the recovery cannot use.

For a yes/no-preserving decision reduction, establish both directions:

`A(x) iff B(f(x))`.

Then the B-answer is the A-answer. If recovery reverses or otherwise changes the returned answer, state that rule and prove the resulting correspondence. For example, one positive implication alone leaves the no branch undecided.

When several queries are needed, construct the calling algorithm. State how a returned answer determines the next query and retained state, why every query is admitted, and why correct target answers lead to termination with the required A-answer. An adaptive reduction is a procedure using the solver, rather than one fixed input map.

Compose reductions by composing their actual conversions and recovery procedures. Intermediate answers must satisfy the next procedure's conditions. MATH.17 and MATH.18 support the mathematical composition and interpretation questions; the present work additionally establishes effective execution under the selected computational model.

#### CMP.1:4.4 - Follow the direction of the consequence

For an established reduction from A to B:

- A suitable B-solver, together with the reduction, gives a suitable A-solver.
- If no such A-solver can exist under the stated model and guarantee, no B-solver with the assumed capability can exist.

Write the constructed A-procedure before using the second conclusion. It shows what the assumed B-solver would enable and where the contradiction arises.

Keep the scope of a limit. An impossibility for a total decision procedure on an unrestricted input class leaves other questions open: positive-case recognition, bounded execution, a restricted class, or a different computational model. Choose an alternative only when it supplies a useful answer for the work. The finite-state return in :5.2 shows such a change.

For a complexity consequence, use a reduction with the required resource bound. An unboundedly expensive input conversion supplies no efficient A-algorithm merely because B has one.

#### CMP.1:4.5 - Derive the cost that can change the choice

When cost matters, include input conversion, query size, solver calls and answer recovery under a named computational model. If conversion costs `T_f(n)`, its output has size at most `m(n)`, B costs `T_B(m(n))`, and recovery costs `T_r(n,m(n))` including the returned answer size relevant to it, the one-query construction has the corresponding total bound:

`T_A(n) <= T_f(n)+T_B(m(n))+T_r(n,m(n))`.

If the answer size is not bounded through these arguments, include it explicitly. For several queries, sum the costs of their construction, calls and recovery, including any adaptive work between calls. Analyze peak simultaneous storage separately from total work.

The representation matters. A quantity written with n bits can have a value exponential in n; enumerating that many states changes the cost claim. Exact rational operations also have costs depending on operand length when bit complexity is the model.

Use the result to choose or reject the reduction for the current resources. Another solver, a smaller representation or a different computational construction can preserve the answer while changing cost. C.29.2 supplies the surrounding resource and accuracy formulation.

#### CMP.1:4.6 - Return a usable construction or a bounded limit

For solver reuse, return the input construction, solver conditions, recovery and relevant cost. A user should be able to follow an input through to its original answer.

For a limit, return the reduction argument, its computational assumptions and the excluded guarantee. Use that result to revise the actual question or allocation of work. A failed implementation attempt supplies neither this limit nor a reason to stop searching for a valid reduction.

When the input class, answer guarantee, representation or available solver changes, revisit the affected connection. Retain the earlier consequence for the conditions under which it was established.

### CMP.1:5 - Archetypal Grounding

#### CMP.1:5.1 - Solve difference constraints through a graph problem

The input is a finite set of variables and inequalities of the form:

`x_v <= x_u+w(u,v)`,

with rational weights. The required answer is an assignment satisfying all inequalities or a correct infeasibility report.

Construct a directed graph with one vertex per variable and an edge u to v of weight `w(u,v)` for each inequality. Add a new source s with a zero-weight edge to every variable vertex. Use a solver that permits negative edge weights and returns either shortest-path distances from s or a reachable negative cycle.

A negative cycle proves infeasibility: sum its inequalities. Every variable cancels, leaving `0 <= sum of cycle weights`, which is false for a negative total.

If there is no negative cycle, all vertices are reachable from s and their shortest distances are finite. For every edge, the shortest-path condition gives:

`d(v) <= d(u)+w(u,v)`.

Thus `x_v=d(v)` recovers a satisfying assignment. This proves the required return for either solver outcome.

For example, take `x_b<=x_a+3`, `x_c<=x_b-2` and `x_a<=x_c+1`. Distances `(d(a),d(b),d(c))=(-1,0,-2)` satisfy all three. If the final bound changes to `x_a<=x_c-2`, the directed cycle has weight `3-2-2=-1` and proves infeasibility.

For n variables and m inequalities, construction adds n+1 vertices and m+n edges. Reading or assembling those lists and copying back an assignment takes O(n+m) operations under the explicit-graph model. Add the selected solver's cost on that graph and the rational-arithmetic costs appropriate to the representation.

The graph is a computational construction for the given inequalities. If those inequalities describe schedules, flows or another subject, their physical or organizational adequacy is a further modeling question. The reduction has established the answer for the supplied mathematical constraints.

#### CMP.1:5.2 - An event decider would decide halting

A team asks for a procedure that always decides whether an arbitrary deterministic program with unbounded working memory will eventually emit a designated event. The input is a finite program description, its finite initial data and the event to be recognized. The guarantee includes terminating with “no” for a program that never emits it.

Use the halting problem as A: given a program P and input x, decide whether P(x) terminates. Under the ordinary Turing-computable model, no total algorithm decides this for all programs and inputs.

Construct a program Q with x and P's description included. Q simulates P on x, suppresses the simulated program's output, and emits the designated event if and when the simulation halts. The description of Q is obtained by placing the supplied data inside this fixed wrapper; constructing it does not run P(x).

If P(x) halts, Q emits. If P(x) does not halt, Q never reaches its emitting step. A supposed total event-decider applied to Q would therefore decide A in both cases. This contradicts the halting result, so the requested universal event-decider is unavailable under these assumptions.

The direction matters: halting was reduced to event decision. The argument constructed a halting decider from the assumed event decider.

Now change the admitted system to a fully represented deterministic finite-state machine with effective transitions and a decidable emitted-event label on each transition. Starting from its initial state, follow transitions while remembering visited states. Return yes upon the event; return no if the machine halts without it or repeats a state before emitting it. At most the number of reachable states can be visited before such repetition or termination. Determinism and complete state make the future repeat as well.

This supplies a usable decision procedure for the changed class. If an environment can add unrepresented inputs or the “state” omits a changing counter, restore those inputs or state before applying this finite-state result. C.29.2 and A.3.3.TR supply that formulation work. The original universal impossibility and this restricted procedure remain compatible.

#### CMP.1:5.3 - A small description can create an expensive search

An input describes b Boolean state variables. A conversion that explicitly constructs every possible state may produce `2^b` vertices. Even a solver linear in the resulting graph size then gives an exponential dependence on b.

The construction may still be effective and useful for small b. For a larger budget-constrained use, keep the original answer condition and seek a representation or method that avoids explicit expansion, or derive a suitable restriction of reachable states. Calling the target solver efficient does not settle the cost of the whole reduction.

#### CMP.1:5.4 - Recover a witness through adaptive decision queries

The required answer is the lexicographically least satisfying assignment of a Boolean circuit C on n ordered input bits, or `UNSAT`. An available solver decides whether a supplied circuit has any satisfying assignment and terminates on either answer.

First query C. A negative answer gives `UNSAT`. After a positive answer, retain a prefix with a satisfying extension. Try its next bit as 0 and query the circuit with that prefix fixed. Keep 0 if the answer is yes; otherwise keep 1. The retained prefix still has a satisfying extension. After n bit choices it is a complete satisfying assignment; preferring 0 at each position makes it the least one.

For `C(a,b,c)=(a or b) and (not a or c)`, the answers are:

`C: yes -> prefix 0: yes -> prefix 00: no -> prefix 010: yes`.

The recovered answer is `010`. For circuit size N, copying each restricted circuit takes O(N) work. There are at most n+1 calls, giving total work bounded by `(n+1)T_B(O(N))+O(nN+n)` and sequential-call space `O(N+n+S_B(O(N)))`.

If the solver only recognizes satisfiable inputs and may diverge otherwise, the query at prefix `00` can fail to return. This construction then lacks its required guarantee. Obtain a total decider or use finite enumeration, whose worst-case work is `O(2^n N)`.

### CMP.1:6 - Bias-Annotation

The solver's familiar name can draw attention away from its admitted inputs and returned guarantees. Follow the actual conversion and recovery, including the negative branch the original problem requires.

An impossibility argument can also be overextended. Keep its input class, computational model and answer guarantee visible, then examine a changed useful question at those same points. A resource estimate is conditional on the representation used.

### CMP.1:7 - Conformance Checklist

For the reduction being used:

- Both problems have stated admitted inputs and required answers.
- The conversion is effective from the supplied input and produces admitted queries.
- Every solver outcome relied on by the construction has an effective recovery with the required guarantee.
- The correctness argument covers the needed directions and termination conditions.
- The consequence follows the direction of the constructed solver reuse.
- A resource claim includes conversion, calls, recovery and relevant representation sizes.
- The result supplies an algorithm, a useful restricted alternative or a limit with a specific effect on the next move.

### CMP.1:8 - Common Anti-Patterns and How to Avoid Them

**Requiring the answer to construct the query.** A wrapper program can be constructed without running the program it contains, as in :5.2. Identify that effective construction; treating a truth-dependent choice of wrapper as already computable would leave the original problem unsolved.

**Using only the successful branch.** Finding an emitted event confirms a positive case. The universal decision request also requires a terminating negative answer, which simulation alone leaves unresolved.

**Reversing the reduction.** Write the A-procedure using the B-solver before transferring an impossibility or an algorithm. Its actual calls determine the direction.

**Hiding conversion cost behind the solver's bound.** Explicit expansion of b bits into `2^b` states dominates the use in :5.3. Include the created instance and its storage in the resource argument.

### CMP.1:9 - Consequences

An unfamiliar problem can acquire a usable algorithm through a constructed connection to another. The same form of reasoning can establish a limit by showing what an assumed solver would imply.

The reduction retains responsibility for inputs, answers and resource effects at the connection. A new solver or representation can improve it; a changed answer guarantee or input class can invalidate only part of its earlier use.

### CMP.1:10 - Architectural Rationale

Effective conversion and answer recovery make reduction a computational method. Mathematical correspondence supplies the relevant implication, while computability and cost determine whether the connection can be used under the stated conditions.

Solver reuse and impossibility belong together because the latter follows by assuming and then constructing the former. Their guarantees and direction remain explicit. The shortest-path and program-wrapper cases demonstrate different uses of that shared method; neither application defines the scope of computational thinking.

C.29.2 already supplies the computational question, representation and ordinary progress account. This pattern develops a missing reduction, its answer relation and the consequence of an available or assumed solver. More specialized algorithm constructions can supply the conversion or the target solver.

### CMP.1:11 - SoTA-Echoing

Erickson's [Undecidability notes](https://jeffe.cs.illinois.edu/teaching/algorithms/models/07-undecidable.pdf), §§7.4-7.5 and 7.9-7.10, supplies a foundational account of effective program construction and the direction of reduction arguments. The adopted contribution is the explicit construction that turns an assumed solver into another solver. The event-wrapper example here uses the halting result under its stated computational model.

Erickson's [Shortest Paths](https://jeffe.cs.illinois.edu/teaching/algorithms/book/08-sssp.pdf) supplies the directed-graph and negative-cycle machinery used in the solver-reuse case. The recovered inequalities and their infeasibility argument explain what that machinery answers in the source problem.

A direct algorithm is preferable when conversion adds effort without improving the needed result. When a reduction is useful, the choice among ordinary computability, bounded-resource, approximate or randomized reductions follows the answer guarantee being transferred. A preserved decision alone leaves an approximation ratio, probability or practical runtime to its corresponding argument.

### CMP.1:12 - Relations

- **C.29.2** specifies computational answers, representation, progress, accuracy and resources.
- **C.29.1** establishes a subject correspondence when the computational problem describes something beyond the mathematical construction.
- **MATH.17 and MATH.18** develop operations on operations, interpretations and their preserved consequences.
- **MATH.4 and MATH.12** supply induction and constructive argument methods when the reduction needs them.
- **A.3.3.TR** recovers state and continuation distinctions, including those needed by finite-state restrictions.
- **C.39 and C.40** help develop a missing computational way or explore alternatives when a construction remains unresolved.

### CMP.1:End

## CMP.2 - Derive a Recursive Procedure from a Problem Decomposition

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.2:1 - Problem frame

**Use this when** you can state the answer required from a finite input, but a procedure for obtaining it is missing or unaffordable. Parts of the task resemble the whole, or a transformation produces another instance whose answer could help. You need to choose those subproblems and determine what they must return.

An engineer, researcher or AI agent may recognize a recursive formula yet be unable to turn an unfamiliar problem into one. A common difficulty appears at recombination: each part returns a correct answer to its own question, but those answers omit information needed for the whole. Another appears at progress: a call changes its input without bringing computation closer to a return.

The gain is a recursive procedure with usable base cases, a reason its calls return, a justified way of combining their results and an initial account of its cost. The reader needs to follow finite case distinctions, functions and a simple inductive argument. MATH.4 can supply that argument; C.29.2 supplies the relation between a computational answer and the question it is meant to settle.

Use a suitable existing procedure directly when it already answers the question within the available resources. This method develops recursion for obtaining a finite answer. A server, stream or other intentionally continuing process needs a progress condition appropriate to that behavior.

### CMP.2:2 - Problem

How can one discover a recursive algorithm whose subproblems are obtainable, whose answers suffice to reconstruct the requested result, and whose unfolding has an acceptable cost?

Choosing a familiar equation or writing a self-call does not settle those questions. The designer must connect the meaning of a subproblem to the operation that uses its answer.

### CMP.2:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Small subproblems and sufficient answers | A short returned value can omit the boundary information needed for recombination. |
| Natural structure and useful decomposition | Following input syntax makes some arguments easy; a different split may reduce work or expose the needed result. |
| Generality and effective choice | A mathematical existence argument can leave the next branch or object unavailable to computation. |
| Progress and branching | Every call may become smaller while their number grows too quickly. |
| Simple cost model and actual representation | Counting additions can hide copying, growing integers or expensive access. |
| Reuse and changed questions | A summary adequate for one result may discard information needed by a later result. |

### CMP.2:4 - Solution

**State the answer → propose smaller questions → derive the join → strengthen what must be returned → establish return → compare the work.**

#### CMP.2:4.1 - Fix the question and the available operations

Describe an input `x`, the information available about it, and what a returned answer must allow its recipient to do. Asking for an optimum value, one attaining object, or every attaining object gives different result requirements. State the empty and degenerate cases when they belong to the input family.

List the operations that can actually be performed on this input: inspect a constructor, split an interval, compare keys, compute a remainder, test a condition, or call a supplied procedure. A proposed step such as “choose the correct partition” remains a construction task until the partition can be obtained.

For example, maximum segment sum on a sequence of integers asks for a contiguous nonempty segment with largest sum. Returning its sum answers a value query; locating the segment also requires endpoints. Permitting the empty segment changes the base case and the answer on an all-negative input.

#### CMP.2:4.2 - Choose a decomposition by asking how answers would join

Take a representative input and suppose that selected smaller questions have been answered correctly. Try to construct the answer for this input from those returned values. This local design question avoids having to unfold the entire recursion while inventing it.

Useful proposals include removing one element, splitting into balanced parts, following the constructors of a structured input, or transforming the input while decreasing another measure. The last case includes Euclid's replacement of a pair by a divisor and remainder. Input size need not decrease in every component.

For each proposal, account for every form a valid answer can take. If a sequence is split into left and right parts, an optimal contiguous segment lies wholly on one side or crosses the boundary. The crossing case shows what the two recursive answers must supply.

Keep the proposal that makes the join both justified and obtainable. If the only available join searches the original problem again, change the subproblem question, retain more information, or try another decomposition.

#### CMP.2:4.3 - Strengthen the returned result when the join needs more

Write the join using named values. Each value must come from the input, a smaller answer or an available local operation. A missing value identifies a specific revision of the subproblem, rather than a reason to discard recursion as a whole.

For maximum segment sum, the best segment on each side is insufficient: a crossing segment uses a suffix of the left side and a prefix of the right. Let each nonempty part return four quantities:

- `T`: the sum of the whole part;
- `P`: the largest sum of a nonempty prefix;
- `S`: the largest sum of a nonempty suffix;
- `B`: the largest sum of a nonempty contiguous segment.

For a left summary `L` and right summary `R`, construct:

```text
T = L.T + R.T
P = max(L.P, L.T + R.P)
S = max(R.S, R.T + L.S)
B = max(L.B, R.B, L.S + R.P)
```

The alternatives in each maximum come from the possible locations of the corresponding segment. To return an actual segment, carry the endpoints attaining each selected prefix, suffix and best segment. Choose a consistent rule for ties when only one witness is wanted.

This is the algorithmic use of strengthening an inductive result in MATH.4. The additional design decision is what summary enables an affordable join for the chosen problem decomposition. Further questions may require a different summary.

#### CMP.2:4.4 - Supply base cases and a decreasing measure

Give a direct result for each case on which recursion stops. Then show that every recursive call reaches such a case after finitely many steps. A nonnegative integer that strictly decreases is often enough. A finite input constructor or a well-founded ordering can supply the same argument when one numerical size is awkward.

For the segment procedure, a singleton `v` returns `(v,v,v,v)`. Split every longer interval into two nonempty shorter intervals. Its length decreases along every call path. This also explains why an empty interval needs its own convention or must be excluded before calling the procedure.

For nonnegative integers with `b>0`, Euclid's call `(a,b) → (b,a mod b)` decreases the second component because `0≤a mod b<b`. The first component may increase relative to its old value; it is the selected measure that must decrease. At `b=0`, return `a`, with the intended convention for `(0,0)` fixed separately.

When a termination checker fails, inspect which decrease is absent from its account. A supplied difference, lexicographic measure or invariant may express the progress already present in the procedure. If progress is genuinely missing, repair the procedure or weaken its claimed result. A small successful run alone does not establish return on every allowed input.

#### CMP.2:4.5 - Establish the result and expose its computational cost

Use the base and smaller-call assumptions to establish the returned property. Recombination must work for every smaller answer allowed by its specification, including the selected tie behavior. When deriving a program from an existing proof, MATH.12 recovers the operations hidden in that proof.

Count the subcalls and local work. A recurrence for mathematical values and a recurrence for computational cost answer different questions. For balanced segment splitting with interval views, constant-cost arithmetic and the four-value join, the work satisfies `W(n)=W(floor(n/2))+W(ceil(n/2))+O(1)`, giving `O(n)` operations. Sequential depth-first evaluation retains `O(log n)` summaries on its call stack. Copying each subarray instead adds work at each level; growing integer values also change the cost per addition.

If equal subproblems recur, CMP.3 can identify and share them. If the decomposition generates alternatives that can be ruled out, CMP.4 can construct those exclusions. If representation dominates the cost, compare the access and update operations before replacing the mathematical construction.

#### CMP.2:4.6 - Use the result and revisit the assumption that changed

Run a small case through the complete procedure, including the use of its returned answer. Change one condition that stresses the construction: empty input, a boundary case, a different output request or a resource limit. Follow the affected base, join and progress arguments.

The result may be a working procedure, an unaffordable but informative construction, or a located missing operation. Use that difference to choose the next algorithmic move. Formal proof or additional testing is chosen for the uncertainty that matters to the receiving use.

### CMP.2:5 - Archetypal Grounding

#### CMP.2:5.1 - A join that initially loses the answer

For `[-2,3,-1,4,-5]`, split into `[-2,3,-1]` and `[4,-5]`. Their best sums are 3 and 4. Keeping only those values would miss the crossing segment `[3,-1,4]`, whose sum is 6.

The strengthened summaries are `L=(0,1,2,3)` and `R=(-1,4,-1,4)`, ordered as `(T,P,S,B)`. The join yields `(-1,4,1,6)`. With attaining endpoints retained, it returns the segment from the second through fourth element. The user can now obtain the segment rather than merely knowing its value.

**Changed condition:** suppose the wanted segment may contain at most two elements. The former crossing winner has length three. The four maxima have discarded the sums of shorter candidate suffixes and prefixes. Add prefix and suffix results indexed by permitted length, combine only lengths whose sum is at most two, and keep the same restriction on internal best segments. In this case the answer becomes 4, attained by `[4]`. For a general limit `k`, a straightforward join over length pairs costs `O(k²)`; the resource consequence can justify a different algorithm. Reusing the old four-value join would silently answer the earlier question.

#### CMP.2:5.2 - A subproblem obtained by a transformation

To compute `gcd(48,18)`, replace the pair by `(18,12)`, then `(12,6)`, then `(6,0)`, and return 6. The equality `gcd(a,b)=gcd(b,a mod b)` follows because a common divisor of either pair divides both entries of the other pair. The remainder operation and decreasing second component turn that equality into a returning procedure.

If the next use also needs coefficients `u,v` with `u*a+v*b=gcd(a,b)`, the returned number alone is insufficient. Suppose the smaller call supplies `d=u'*b+v'*r`, with `r=a-q*b`. Substitution gives `d=v'*a+(u'-q*v')*b`; return the updated coefficients too. For the original pair, `6=(-1)*48+3*18`. The same recursive decomposition supports a stronger output through a changed join.

### CMP.2:6 - Bias-Annotation

Familiar syntax can make one decomposition appear inevitable. Compare its join and cost with another plausible decomposition when those differences can change the choice. Conversely, an elegant asymptotic bound can hide operations that the actual representation makes expensive.

A successful example demonstrates the construction and can expose a missing case. The general result depends on the base, joining and progress arguments, with any additional assurance selected for the actual use.

### CMP.2:7 - Conformance Checklist

- The input and wanted result distinguish a value from any witness or continuation information that is needed.
- Each subproblem is constructible from available data, and its returned specification supplies the join.
- The base cases cover the stopping situations; every recursive path has the stated progress toward one of them.
- The join preserves the answer property, including boundaries and the chosen treatment of ties.
- The cost account includes branching, recombination and representation costs material to the decision.
- A changed requirement is followed through the returned information and affected clauses before the procedure is reused.

### CMP.2:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Return only the final scalar from each part | The segment example loses crossing answers. Derive the join and retain the boundary summaries it consumes. |
| Treat a changed input as a smaller input | Calls can continue indefinitely. State a well-founded decrease and check every recursive branch against it. |
| Treat termination as affordability | An exponential call tree can terminate correctly. Count calls and local work; share repeated subproblems when useful. |
| Keep the old summary after changing the question | A length constraint or witness request can be lost. Reconstruct what the new join needs and revise the affected result. |

### CMP.2:9 - Consequences

The method makes recursive algorithm design available as a sequence of inspectable choices. It exposes a useful link between mathematical construction and algorithmics: strengthening what a subproblem returns can make a previously unavailable or costly computation possible.

The resulting algorithm need not be the fastest one. Its explicit subproblem and join create opportunities for sharing, new representations, parallel execution or replacement by another algorithm. Those improvements retain their own correctness and resource questions.

### CMP.2:10 - Architectural Rationale

Subproblem meaning, recombination, progress and cost belong together because changing one can force a change in the others. Starting from a recursive syntax would obscure the discovery of the required question and summary. Starting from an induction proof alone can leave the effective decomposition and cost unresolved.

MATH.4 supplies witness construction by induction; MATH.12 supplies extraction from a proof. This pattern constructs and compares recursive obtaining procedures, including decompositions that do not follow the input's constructors. CMP.3 changes how repeated calls are evaluated without silently changing what they ask. C.29.2 retains the common computational formulation and its connection to the receiving question.

### CMP.2:11 - SoTA-Echoing

[Erickson, *Algorithms*, chapter 1](https://jeffe.web.engr.illinois.edu/teaching/algorithms/book/01-recursion.pdf) develops recursion through reductions to simpler instances and separate correctness and running-time arguments. This remains a useful foundational construction line. Adopt the local design question about a correct smaller answer; adapt it by making the information required at the join explicit and testing a changed output request. A remembered recurrence alone supplies less help when the decomposition itself is missing.

For the construction in :4.2–4.5, an available recurrence or input-structural split is the simpler alternative when it already returns enough information for the join and meets the cost requirement. Strengthening a subanswer is worth its extra work when that simpler return loses the requested result, as the four-value segment construction and coefficient-returning divisor procedure demonstrate. Reconsider this choice when a different output, representation or competing decomposition changes either sufficiency or total cost.

The current [Lean reference on recursive definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/) distinguishes structural recursion, well-founded measures and forms of partial or continuing behavior. Adopt the distinction between a missing syntactic decrease and an absent termination argument. Formal encoding can check a consequential or difficult construction; its additional work is unnecessary for simply exploring a decomposition. No particular proof assistant or finite-return account is imposed on every computational process.

### CMP.2:12 - Relations

- **C.29.2 - Computational Formulation:** supplies the requested computational result, elementary operations and connection to use.
- **CMP.1:** supplies reuse through an effective reduction; recursion constructs the repeated same-family reduction and its return.
- **MATH.4 and MATH.12:** supply inductive construction and the obtaining operations recoverable from proof.
- **CMP.3:** shares repeated calls and chooses their evaluation and storage; **CMP.4** handles exclusions among alternative extensions.
- **MATH.20:** supplies bounds used when comparing cost or consequences. The general resource and portfolio methods choose among the constructed alternatives.

### CMP.2:End

## CMP.3 - Share and Schedule Repeated Subcomputations

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.3:1 - Problem frame

**Use this when** a procedure repeatedly obtains the same intermediate answer, or retains so many intermediate values that it cannot finish within the available memory. You need to determine which work can be shared, when to perform it, and what to retain for later use.

The situation occurs in dynamic programming, symbolic evaluation, database computations, program analysis and differentiation of computational graphs. The repeated unit is a subcomputation with stated inputs and a needed result. Similar-looking calls may still require different answers because their data, assumptions or effects differ.

The gain is an evaluation procedure that performs less repeated work or fits the available storage while preserving the requested answer. The reader needs to understand a function call and a directed dependency graph; the graph is explained here as a set of intermediate results with arrows from each prerequisite to its consumer. CMP.2 can supply the original recursive procedure.

Direct recomputation is often best for a cheap, seldom-repeated operation. Apply this method when sharing or storage choices can change the feasibility or cost of the computation. A changing environment requires the meaning of reuse to be established before previous results are used.

### CMP.3:2 - Problem

How can repeated computations be identified and reorganized without merging cases that need different answers, using an evaluation order and storage policy that support the requested result?

“Cache the answer” leaves three questions open: what counts as the same question, which answers must already be available, and whether the retained information suffices for the eventual output.

### CMP.3:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Sharing and distinctions | A coarse reuse key saves work but can conflate different continuations. |
| Demand and predictable order | Computing only requested states avoids unused work; a regular order can simplify access and scheduling. |
| Time and storage | Retaining values avoids computation but can exhaust memory or increase data movement. |
| Value and witness | A small working table can retain the optimum value while losing the path attaining it. |
| Reuse and change | An answer remains usable only while the data and conditions on which it depends still apply. |
| Mathematical equality and execution effects | Repeating a pure calculation and repeating an observation or state change can produce different behavior. |

### CMP.3:4 - Solution

**Name the repeated question → retain its determining information → expose dependencies → choose evaluation order → choose retained values → recover the required output.**

#### CMP.3:4.1 - State what a subcomputation means

Describe the result of one subcomputation as a function of its inputs and fixed environment. Include every condition that can change the returned answer or its use. A pair of sequence indices identifies an edit-distance subproblem only within specified sequences, edit operations and costs.

For optimization, distinguish the best remaining value from accumulated cost already incurred. If two histories lead to the same remaining problem but have different past costs, share the remaining answer and combine it with each history's cost. Merging the complete histories may lose a better total. When history changes the allowed future choices, retain that history information in the state.

This question is also useful before an implementation exists: identify the small family of questions that many possible constructions would ask. A recursion tree can then be designed around those questions instead of optimized after the fact.

#### CMP.3:4.2 - Define reuse by the answer the continuation needs

Choose a representation of subproblem identity, often called a key. Equal keys must imply interchangeable answers for the intended continuation. The key can contain input values, an immutable object's identity, a data revision, parameters and relevant assumptions. A cache local to one fixed computation may keep some of these implicit in its scope.

MATH.2 supplies the reasoning behind an identification: the operation used after identification must give the same required result whichever representative was used. An implementation also needs an effective way to recognize the keys. A hash narrows candidates; resolve collisions before treating different data as identical.

Distinguish completed answers from computations that have merely begun. Reading an unfinished entry as a result can introduce circular reasoning. In parallel evaluation, decide whether repeated demand waits for one producer or safely computes another copy; preserve the meaning of completion in either case.

For an operation with effects, state what reuse preserves. Replacing two reads of a changing sensor by one stored reading changes the observation sequence. Repeating a random draw and reusing one sample changes dependence. Sharing a pure calculation on an already obtained reading or sample can be valid. Select the intended operation before choosing the reuse rule.

#### CMP.3:4.3 - Construct the dependency graph and an evaluation order

For each distinct subproblem, identify which other results are needed to obtain its answer. Draw an arrow from a prerequisite to its consumer. Count distinct states and the work needed to combine each state's prerequisites and alternatives; the number of states alone does not establish the total cost.

If dependencies are acyclic, two standard constructions are available:

| Construction | How it obtains results | Useful condition |
| --- | --- | --- |
| Memoized evaluation | On a call, return a completed stored answer if present; otherwise obtain prerequisites, compute the result and store it. | Only part of the possible graph is expected to be reached. |
| Ordered table evaluation | Obtain a topological order, in which prerequisites precede their consumers, and compute states in that order. | The needed state region and dependency order are known and regular access helps. |

These methods can be combined by regions. Independent ready states can also be evaluated concurrently, provided the sharing and combination operations preserve the result.

A directed cycle prevents this simple ordering. Determine whether it is an erroneous recursive dependency, a finite-horizon problem missing its horizon coordinate, or a genuine fixed-point problem. For a genuine cycle, provide the iteration, ordering or other solving method and its result conditions. Adding memoization alone does not solve mutually dependent equations.

#### CMP.3:4.4 - Retain what remains live, and recompute selectively

A value is live while a later operation will need it and cannot obtain it more cheaply by another means. Find its last planned consumer. After that use, the storage can be reused unless the requested final output needs the value for reconstruction.

Compare full retention, a moving set of recent values, and selected stored checkpoints from which intervening work is recomputed. Include key storage, lookup, copying, arithmetic size and transfer costs when they can change the choice. The mathematical dependency graph can be unchanged while these execution costs differ substantially.

Recomputation must reproduce the needed value from retained inputs and conditions. If it repeats an external effect or uses changed data, its meaning needs separate treatment. A stored checkpoint is useful only if it contains enough information to restart that part of the computation.

#### CMP.3:4.5 - Recover the value, witness or continuation actually requested

For each return, ask what the recipient must obtain. A dynamic program may return only an optimum value, one attaining sequence of choices, a count, or all attaining sequences. Store a selected predecessor when one witness is required, retain all relevant alternatives when their multiplicity matters, or provide an additional reconstruction procedure.

A small table is not automatically a complete answer. Sometimes an extra pass or a recursive split reconstructs a witness using less storage than retaining all predecessors. Include that work in the cost comparison.

When inputs or requirements change, identify the affected dependencies. Invalidate or recompute their consumers, or show that the changed information cannot alter those results. Choose the simplest reuse boundary that pays for itself; rebuilding a small calculation can be cheaper than maintaining fine-grained dependencies.

#### CMP.3:4.6 - Compare the resulting procedure with the original

Evaluate one complete use under both procedures and follow a changed condition that can break the proposed identification or storage policy. Check returned content as well as operation counts. The method's result is the changed computation and its resource consequence.

Use C.11.DUA when deciding whether another measurement, argument or experiment would change the choice. A theoretical bound can guide an initial implementation; actual resource observations can select among alternatives whose constant factors or memory behavior matter.

### CMP.3:5 - Archetypal Grounding

#### CMP.3:5.1 - Obtain a sequence-editing answer without expanding repeated calls

Let `D(i,j)` be the smallest number of unit-cost insertions, deletions and substitutions transforming the first `i` characters of fixed sequence `A` into the first `j` characters of fixed sequence `B`. Matching characters cost zero. Then:

```text
D(0,j) = j
D(i,0) = i
D(i,j) = min(D(i-1,j)+1,
             D(i,j-1)+1,
             D(i-1,j-1) + (0 if A[i]=B[j] else 1))
```

Here character positions start at 1. Each alternative identifies the last edit or match. Removing it leaves the corresponding smaller problem; adding it to a best smaller answer supplies a candidate for the whole prefix. Thus the minimum covers the possible last steps.

Naively unfolding this recurrence repeatedly requests the same prefix pairs. Within one fixed pair of sequences and one cost rule, use `(i,j)` as the key. Dependencies have smaller `i+j`, so increasing rows and then columns gives a valid order.

For `A=CAB` and `B=AB`, the complete table is:

| Prefix of A | Empty | A | AB |
| --- | --- | --- | --- |
| Empty | 0 | 1 | 2 |
| C | 1 | 1 | 2 |
| CA | 2 | 1 | 2 |
| CAB | 3 | 2 | 1 |

The result is 1; deleting the initial C attains it. There are `(m+1)(n+1)` states for lengths `m,n`, with constant work per interior state under constant-cost character comparison and small-integer arithmetic. Full retention uses `O(mn)` cells. If only the distance is required, the preceding and current row suffice, giving `O(n)` working cells.

**Changed output:** the recipient now needs an edit script. The final distance and two surviving rows do not supply the deleted path. One repair stores a minimizing predecessor for each cell and traces back from `(m,n)`. Another computes forward and backward costs to a middle row, chooses a column minimizing their sum, and recursively reconstructs the two halves. Every edit path crosses that row, which justifies the split. This second construction exchanges recomputation for storage; CMP.2 supplies the recursive decomposition. Neither choice alters the meaning of an allowed edit.

**Changed reuse scope:** for `A=CB`, `B=AB`, the value at `(2,2)` is 1; for `A=CA`, `B=AB`, it is 2. A global cache keyed only by `(i,j)` would conflate them. Restrict the cache to a fixed input pair or include the input identity and relevant conditions.

#### CMP.3:5.2 - Share an expression while preserving its interpretation

For `f(x,y)=(x+y)*(x+y)+(x+y)`, build one node `t=x+y` with three uses, then obtain `t*t+t`. With `x=2,y=3`, the result is 30. This replaces three additions of `x+y` by one and shares its stored value until the final addition.

If `y` changes to 4, `t` and its consumers must change; the result becomes 42. If each occurrence instead meant “read the next measurement and add x,” the shared expression would change the computation's meaning. The subproblem must be a fixed pure addition of supplied values for this identification to hold.

In differentiation of a longer expression graph, intermediate values may be needed again in reverse order. Keeping all of them can exceed memory. Retain selected restart values and recompute intervening pure operations when needed, comparing the extra work with reduced storage. This applies the same method to a different receiving algorithm.

### CMP.3:6 - Bias-Annotation

Visible repetition can encourage indiscriminate caching. The profitable unit may instead be a larger common subproblem, or no shared unit at all when lookup costs dominate. A small count of stored cells can also hide large objects, metadata and movement between memory levels.

Results obtained from fixed data invite overgeneralization to changing environments. State where a key's omitted parameters are held fixed, and revisit that boundary when the result is reused elsewhere.

### CMP.3:7 - Conformance Checklist

- The repeated question and its determining data are recoverable from the key and its stated scope.
- Equal keys justify the required reuse, including relevant effects, randomness and changed inputs.
- Dependencies determine an evaluation order, or a separate method resolves the genuine cycles.
- Completed results are distinguished from work still being evaluated.
- Storage and recomputation choices preserve the final value, witness or continuation that is required.
- The resource comparison counts relevant transitions, arithmetic, access and storage as well as states.
- The changed-condition use follows the dependency or output requirement that actually changed.

### CMP.3:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Key a subproblem by its position across changing inputs | The edit-distance example reuses an answer to another question. Bind the key to the input and conditions or narrow the cache's lifetime. |
| Treat an in-progress entry as an answer | A cyclic dependency can return unsupported content. Keep completion explicit and supply the appropriate cycle-solving method. |
| Discard predecessors while promising a witness | The optimum value remains but the attaining object cannot be returned. Retain choices or construct a reconstruction pass. |
| Share effects as if they were pure calculations | Observations, updates or random dependence can change. Identify the fixed data calculation that is actually interchangeable. |

### CMP.3:9 - Consequences

Many repeated call trees become a much smaller graph of distinct questions. Evaluation order and retention become design choices, making time, memory and output reconstruction comparable.

The transformation creates responsibilities for identity and change. Its benefit depends on repetition, graph size and access costs; a dependency graph can itself be enormous. A correct shared computation can still be unaffordable, which may call for a changed representation, approximation or problem formulation.

### CMP.3:10 - Architectural Rationale

Identity, dependencies, evaluation and lifetime form one method because changing the result being shared can alter all four. Separating “add a cache” from the required continuation would hide the main correctness question. Including selective recomputation prevents storage minimization and computation minimization from being treated as the same objective.

The mathematical identification is supplied by MATH.2, the subproblem construction by CMP.2, and common computational formulation by C.29.2. This pattern supplies the algorithmic reorganization. It can serve numerical, symbolic and learning procedures.

### CMP.3:11 - SoTA-Echoing

[Erickson, *Algorithms*, chapter 3](https://jeffe.web.engr.illinois.edu/teaching/algorithms/book/03-dynprog.pdf) develops memoization, deliberate evaluation order, space saving and reconstruction of sequence-editing answers. Adopt the progression from a meaningful recurrence to distinct subproblems and their evaluation. Extend the identity question explicitly to changing inputs and effectful operations. The CAB example is a small independent derivation of that general design approach.

[Hirschberg's linear-space reconstruction](https://ics.uci.edu/~dhirschb/pubs/p341-hirschberg.pdf) is a historical but still useful counterexample to the assumption that reconstructing a sequence requires retaining a complete table. Its middle-split method also applies to edit paths. Adopt reconstruction as a choice between storage and additional calculation; do not claim its cost is optimal for every input representation or modern machine.

Current [JAX checkpointing documentation](https://docs.jax.dev/en/latest/gradient-checkpointing.html) shows the same storage/recomputation choice in automatic differentiation. Adopt its substantive distinction between saved intermediates and recomputed pure operations. Compiler behavior and hardware costs affect the best schedule; a particular library interface is an example of realization rather than a prerequisite of this method.

The working choice in :4.3–4.5 is between retaining all needed intermediate answers, recomputing them when requested, and retaining selected answers from which others can be reconstructed. Full retention is simpler when memory is ample and reconstruction would dominate. Recalculation avoids maintaining entries whose results are cheap or rarely reused. Selective retention pays extra scheduling or reconstruction work when it preserves the required answer under a tighter memory limit; the edit-script construction supplies one such choice. Reconsider it when effects change which calls can be shared, the recipient needs a different witness, readout costs change, or a competing reconstruction method improves the same resource trade-off.

### CMP.3:12 - Relations

- **CMP.2:** constructs the subproblems and their combination; this method changes how repeated questions are evaluated.
- **MATH.2:** supplies identification under operations; **A.3.3** helps restore state information when equal retained states allow different continuations.
- **C.29.2:** supplies computational result and resource conditions. **C.29.3** applies when realization changes the relevant execution assumptions.
- **MMP.8:** supplies information restrictions for adaptive choices; a computation used to obtain such a policy must preserve the observations and history on which its choices depend.
- **C.11.DUA:** selects additional checking or measurement for a decision that could change, including the value of further optimization.

### CMP.3:End

## CMP.4 - Construct Computational Search with Justified Exclusions

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.4:1 - Problem frame

**Use this when** an answer must be constructed by choosing among alternatives, direct enumeration is too costly, and information about a partial choice can eliminate some of its completions. You need a search procedure that saves work while retaining the answers its recipient needs.

Examples include finding an assignment satisfying constraints, selecting a best combination, constructing a counterexample and exploring possible program states. The general difficulty is deciding which alternatives may be omitted. A promising search order can find an answer quickly while providing no reason to exclude the alternatives visited later.

The gain is a search with explicit coverage, useful exclusion rules and a result that remains interpretable if computation is interrupted. The reader needs finite sets, logical conditions and inequalities; MATH.20 supplies a more developed bound argument. C.29.2 supplies the wanted computational answer.

Use direct construction or enumeration when it already solves the problem at acceptable cost. Heuristic search is also useful when a good candidate is enough. Apply the exclusion method to the conclusions that must be retained, without requiring proof of global optimality for every candidate search.

### CMP.4:2 - Problem

How can a procedure omit whole sets of candidates and still return a valid witness, a justified optimum or a warranted statement that no required answer exists?

The exclusion must concern every relevant completion represented by the omitted branch. Failure of one attempted completion or poor predicted performance alone does not establish that result.

### CMP.4:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Coverage and early progress | Broad exploration retains alternatives; informed order may obtain a useful witness sooner. |
| Cheap and strong exclusions | A weak inexpensive bound can save more total work than a costly tight bound. |
| One answer and all answers | A rule preserving one optimum can discard other attaining objects. |
| Current candidate and remaining possibility | A feasible result establishes what can be done; a branch bound constrains what remains possible. |
| Reuse and assumptions | A learned conflict can remain useful across branches but fail after constraints change. |
| Return time and strength of conclusion | An interrupted search can still supply a candidate and a bound, while exhaustion supports a stronger conclusion. |

### CMP.4:4 - Solution

**Represent the alternatives → cover them by extensions → derive exclusions → choose exploration order → retain the remaining possibility → return the supported answer.**

#### CMP.4:4.1 - Define a partial choice and its completions

State what constitutes a complete candidate, when it is admissible, and which result is wanted: one witness, a best value and witness, every optimum, a count, or a counterexample. For optimization, state the criterion and its direction.

Choose a representation `s` of partial choices. Explain which complete candidates it represents and what information is still undecided. Include past choices when they change future feasibility or cost. If several histories have the same remaining question, CMP.3 can share that question while preserving the history-dependent contribution.

Construct extensions that cover the relevant completions. Binary inclusion/exclusion, a variable's remaining values and legal next transitions are common forms. Overlap is permitted for finding one witness but can duplicate results; counting and enumeration need a way to handle it. A symmetry reduction needs an account of which answers it identifies and whether the recipient accepts that identification.

#### CMP.4:4.2 - Derive an exclusion that applies to the entire branch

Select a reason for omitting `s` according to the result required:

| Reason | Required argument | What it allows |
| --- | --- | --- |
| Infeasibility | No completion of `s` can satisfy the original conditions. | Discard `s` when looking for admissible answers. |
| Bound | Every completion has a value no better than a bound compared with an already admissible answer. | Discard `s` for the corresponding optimization conclusion. |
| Dominance | Another retained choice supplies an admissible answer at least as good for every continuation that matters. | Omit dominated work while retaining the stated result. |
| Equivalent completions | A retained representative accounts for the answers required from `s`. | Share or omit duplicate work with the appropriate treatment of identity and multiplicity. |

Construct these arguments from the constraints and the partial state. Propagating a choice can shrink the permitted values of other variables; an empty remaining domain then excludes that branch. A bound may come from relaxing the remaining problem through CMP.5. Dominance must include future possibilities, not merely compare the current partial scores.

For a maximization problem, let `L` be the value of the best admissible candidate already obtained, often called the incumbent. Let `U(s)` be at least as large as the value of every admissible completion of `s`. If one optimum is required, `U(s)≤L` permits exclusion. If every attaining candidate is required, equality can still contain needed answers; use `U(s)<L` for this bound-based exclusion and preserve the attaining alternatives.

For minimization, reverse the bound directions: a lower bound on every completion is compared with the cost of a known feasible candidate. A candidate score and a bound on all completions have different roles even when their numerical values coincide.

#### CMP.4:4.3 - Reuse consequences within their conditions

When a conflict occurs, identify which partial assignments and original conditions imply it. A smaller conflicting subset can exclude the same combination elsewhere, saving repeated discovery. Apply the learned consequence only where those conditions hold.

Keep its scope simple enough to use. A consequence of the fixed problem can be retained throughout that search. A consequence relying on a temporary assumption applies only under that assumption, unless the assumption is retained in the learned condition. After a constraint or domain change, revisit consequences depending on it.

An observation that a branch was unpromising can guide ordering. Turning it into an exclusion requires the corresponding all-completions argument or an explicitly weaker heuristic conclusion. This is particularly relevant when a learned model proposes branches or estimates their value.

#### CMP.4:4.4 - Choose the exploration order for the next useful result

Maintain the unprocessed partial states. Depth-first exploration retains relatively little state; an order based on bounds can tighten the remaining optimum range; a feasibility heuristic can obtain an incumbent early. Choose according to the result and resources needed now.

At each selected state, propagate applicable conditions, apply a useful exclusion, return or improve a complete admissible candidate, or generate covering extensions. A finite search space and complete processing support eventual exhaustion. In an infinite space, eventual discovery additionally depends on how branches are scheduled; repeatedly expanding one branch can leave an existing witness unvisited.

Compare the cost of an exclusion with the work it is likely to avoid. It can be rational to skip a difficult bound and explore the branch.

#### CMP.4:4.5 - Preserve the meaning of bounds during computation

A mathematical bound must retain its direction in the arithmetic that computes it. For a maximizing search, an upper bound rounded downward without justification may exclude a better answer. Conservative rounding, interval bounds or a justified rational calculation can preserve the exclusion. A score predicted by a model is an estimate unless a suitable bound property has been established.

Use stronger arithmetic or independent checking where an erroneous exclusion could alter a consequential result. Ordinary exploratory search can instead keep a borderline branch or report a qualified result. C.11.DUA selects that extra work by its possible effect on the receiving decision.

Keep a bound for the unprocessed work, including a state whose expansion is interrupted. For maximization with an incumbent `L`, the whole optimum is at most `max(L, max U(s))` over the states still pending. The incumbent supplies a lower bound. If a pending state lacks an upper bound, a finite global upper bound is not yet supplied by this account.

#### CMP.4:4.6 - Return the strongest result actually obtained

On finding a witness, return it with the meaning of its admissibility. For optimization, include its objective value and any remaining bound that the recipient needs. On complete exhaustion, sound exclusions and covering extensions justify optimality if a feasible answer was found, or absence of a feasible answer if none was found.

On interruption, return the available candidate and unresolved possibility. “No witness found within this run” is useful information but does not establish that no witness exists. If only a satisfactory candidate was requested, its obtaining can complete the work without exhausting the search.

Use an initial and changed-condition case to check which conclusion the recipient can actually use. Changing an output from one optimum to all optima, or changing a domain, directly tests the exclusion's scope.

### CMP.4:5 - Archetypal Grounding

#### CMP.4:5.1 - Select a best subset and interpret an interrupted search

Choose a subset of three items within capacity 5. Their `(weight,value)` pairs are `A=(4,7)`, `B=(3,5)` and `C=(2,3)`. Values and weights are positive integers. A partial state fixes which items are included or excluded; the next undecided item supplies the two covering extensions.

An initial candidate `{A}` is admissible with value 7. To bound the root, allow fractions of items. Filling by value per weight takes A and one third of B, giving `7+5/3=26/3`. To establish that this is an upper bound, let a, b and c be the selected fractions. For `0≤a,b,c≤1` and `4a+3b+2c≤5`,

`7a+5b+3c=(5/3)*(4a+3b+2c)+a/3-c/3≤25/3+1/3=26/3`.

The displayed fill attains the bound. Every integral subset is included in this relaxed set, so it too has value at most `26/3`. Since integral subset values are integers, 8 is also a valid upper bound.

If the run is interrupted here, it has established `7≤optimum≤8`, together with candidate `{A}`. It has not established optimality of A.

In the include-A branch, neither B nor C can also fit, so its best completion is A with value 7. In the exclude-A branch, B and C fit together and give 8. This meets the global upper bound, establishing that `{B,C}` is optimal. The algorithm obtained both a usable subset and a stopping reason.

**Changed output:** add an item `D=(5,8)` and ask for all optimal subsets. Once `{B,C}` has value 8, pruning a branch with upper bound 8 could lose the distinct answer `{D}`. Retain equality branches, or use a separate enumeration phase constrained to the established optimum value. The former “one optimum” exclusion answers a different request.

#### CMP.4:5.2 - Use a conflict, then revise its assumptions

Three tasks A, B and C must occupy slots 0 or 1. Every pair conflicts, so conflicting tasks must use different slots. After choosing `A=0`, propagation forces `B=1` and leaves C with no allowed slot. The branch is infeasible. Choosing `A=1` gives the symmetric conflict. Exhausting these two A choices proves that no assignment exists under these constraints.

If a third slot 2 becomes available, the earlier impossibility no longer applies. The construction `A=0, B=1, C=2` is feasible. An implementation reusing conflicts learned under the two-slot domain must retain or reconsider that domain assumption. Searching faster with an obsolete conflict would prevent the useful new answer.

### CMP.4:6 - Bias-Annotation

An early good answer can make unvisited alternatives seem irrelevant. That is a valid stopping choice when the recipient needs only a satisfactory candidate; it does not itself justify an optimum claim. Conversely, insisting on exhaustion can waste resources after further improvement no longer matters.

Bounds deserve attention to their direction and scope rather than confidence-producing names. The relevant distinction is what the bound establishes about possible completions, including the arithmetic and assumptions used to obtain it.

### CMP.4:7 - Conformance Checklist

- Partial states have a stated meaning and their extensions cover the answers that must be retained.
- Each exclusion applies to every relevant completion represented by the omitted state.
- The use of equality, symmetry, dominance and duplicates matches the request for one answer, all answers or a count.
- The incumbent is admissible; each bound has the correct direction and computational support for its use.
- Learned consequences retain assumptions that limit their reuse.
- Interrupted work remains represented in the pending possibility, and the returned conclusion matches what was completed.
- Additional pruning or assurance work is chosen for its useful effect rather than required for its own sake.

### CMP.4:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Exclude a branch because one completion failed | Another completion may work. Derive a conflict applying to the entire represented set or continue branching. |
| Use a predicted score as a bound | A better answer may be discarded. Keep the prediction as an ordering heuristic unless its bound property is established. |
| Prune ties while enumerating all optima | Distinct attaining answers disappear, as in the added-D case. Retain equality branches or use a separate complete enumeration. |
| Report interruption as impossibility | Unvisited alternatives remain. Return the candidate, remaining bounds and the limit on the conclusion. |
| Reuse a conflict after its domain changes | A newly feasible answer can be excluded. Reconsider the consequence with its original conditions. |

### CMP.4:9 - Consequences

The search can avoid large parts of a combinatorial space and still support a precise result. It can also supply a useful answer before completion, with the remaining possibility described at the strength actually established.

The method does not guarantee affordable search. Exclusions may be weak, expensive or scarce; the remaining space may still grow exponentially. A changed formulation, relaxation, shared subproblem or weaker requested conclusion can then be the next useful move.

### CMP.4:10 - Architectural Rationale

Coverage and exclusion are complementary: a complete branching scheme loses its guarantee if an unsupported pruning rule is added, while sound pruning cannot recover alternatives that the branching never represented. Exploration order is kept separate because it can improve time to a witness without changing which branches are valid to omit.

MATH.20 supplies the mathematical bound. CMP.5 constructs a relaxed problem that can provide one; CMP.3 can share repeated remaining questions. This pattern combines such contributions into the algorithmic construction and interpretation of search. C.40 concerns broader exploration and further problem development; its interests and stepping stones need not be reducible to a fixed search objective.

### CMP.4:11 - SoTA-Echoing

[Erickson, *Algorithms*, chapter 2](https://jeffe.web.engr.illinois.edu/teaching/algorithms/book/02-backtracking.pdf) develops recursive exploration of choices. Adopt the separation between a partial choice, its extensions and the recursively obtained answer. The present synthesis adds the result-sensitive treatment of branch bounds, interrupted search and changed assumptions.

The primary report [*The SCIP Optimization Suite 10.0*](https://optimization-online.org/wp-content/uploads/2025/11/scipopt-100.pdf) describes current mathematical-programming search and a numerically rigorous mode combining rational and directed-rounding computation. Adopt its substantive lesson that a bound's mathematical direction must survive its computation. The additional cost and supported problem classes limit when that mode is appropriate. This pattern neither requires a solver certificate for ordinary search nor treats a floating-point estimate as an unconditional exclusion.

For :4.2–4.6, compare justified exclusions with simpler exhaustive exploration and heuristic ordering alone. A bound is useful when the branches it safely avoids repay the work of obtaining and maintaining it, or when its conclusion settles the task before exhaustion. If finding a satisfactory candidate is enough, cheap ordering can win without proving a stronger bound. Retain ordinary conservative arithmetic when it supports the required comparison; rational or directed-rounding machinery is useful only when its added cost buys a consequential warranted exclusion. Reopen this selection when the requested output, admitted assumptions, cost of bounds or evidence for their soundness changes. In particular, asking for every optimum changes the usefulness of equality bounds.

### CMP.4:12 - Relations

- **C.29.2:** states the wanted computational answer and its resource conditions.
- **CMP.2:** supplies recursive decomposition; **CMP.3** identifies repeated remaining subproblems and schedules their evaluation.
- **CMP.5 and MATH.20:** construct useful relaxed bounds and justify the corresponding inequalities.
- **MMP.10:** supplies the admissible problem when search serves a modeled subject question.
- **C.11.DUA:** guides the value of further exploration, stronger bounds or additional checking.
- **C.40:** supports the wider development of alternatives and problems, including situations in which the search space or objective itself is being changed.

### CMP.4:End

## CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.5:1 - Problem frame

**Use this when** an optimization problem is difficult to solve directly, but weakening some of its restrictions or costs gives a more accessible problem. Its solution may help construct a candidate for the original problem, or bound how much better the current candidate could become.

The situation occurs in combinatorial selection, scheduling, routing, program synthesis and continuous optimization. A relaxed solution can make an inaccessible search informative, but it may violate the original conditions. For example, fractional choices are useful for reasoning about an indivisible selection even though the fractions cannot be implemented as that selection.

The gain is a useful bound, a recovered admissible candidate, or both, together with a reason they apply to the original question. The reader needs feasible sets, an objective and inequalities. MATH.20 supplies further bound reasoning; a solver for the selected relaxed problem may be obtained as a separate contribution.

Use an available direct method when it already produces the needed result at acceptable cost. Approximation alone does not make a problem a relaxation: this method needs the correspondence and inequality that support its bound. A good heuristic can still be used without that bound, with its result stated accordingly.

### CMP.5:2 - Problem

How can solving an easier problem help obtain or assess an answer to the original one, without treating the easier problem's admissibility or optimum as the original result?

The designer must construct both directions of use: how original candidates are represented in the relaxed problem, and how the relaxed output yields a bound or a candidate that the original recipient can use.

### CMP.5:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Easy and informative relaxation | Removing many restrictions may simplify solution but leave a weak bound or hard recovery. |
| Relaxed value and admissible candidate | The easier optimum can be unobtainable under the original conditions. |
| Solver effort and useful improvement | Tightening a bound can cost more than exploring or using the current candidate. |
| Recovery and lost quality | Rounding or repair can restore feasibility while worsening the objective. |
| Mathematical and computed bounds | Approximate optimization and arithmetic can weaken or invalidate a claimed bound direction. |
| One criterion and several interests | A scalar optimization result answers its stated criterion; other objectives retain their own comparison. |

### CMP.5:4 - Solution

**State the original problem → construct the easier comparison → obtain its informative result → recover an admissible answer → bound the loss → choose the next use.**

#### CMP.5:4.1 - State what the original candidate must satisfy

Name the original feasible set `F`, objective `f`, and whether it is minimized or maximized. Include the conditions that make a candidate usable in the receiving activity. An abstract numerical optimum can leave implementation, uncertainty or other subject conditions outside this particular problem; keep that boundary visible through C.29 and MMP.10.

State what would change the present decision: a better candidate, an infeasibility conclusion, a bound on possible improvement, or an answer within a given tolerance. This selects how much work to spend on the relaxation and recovery.

If several criteria matter, use the existing characterization and Pareto methods to preserve their trade-offs. The scalar constructions below apply to the chosen optimization question. They do not replace that broader comparison with a model-specific score.

#### CMP.5:4.2 - Construct the relaxation and derive the bound direction

For minimization, give a relaxed feasible set `R`, objective `g`, and a way of representing each `x` in `F` by `i(x)` in `R`, such that `g(i(x))≤f(x)`. Where minima exist, this yields `min_R g≤min_F f`. For maximization, use the reversed objective inequality so that the relaxed optimum is an upper bound on the original optimum.

Common constructions include:

| Construction | Why the comparison can hold | Main design risk |
| --- | --- | --- |
| Drop a constraint or allow fractions instead of integral choices | Every original feasible point remains available with the same objective. | The relaxed optimum may be far from any original feasible candidate. |
| Make transitions or costs more permissive | Every original path remains represented at no greater cost in a minimizing problem. | The relaxed route may use operations forbidden in the original problem. |
| Replace a coupling constraint by a multiplier term | The signed term gives a bound on the objective for original feasible points, while the relaxed computation may separate into smaller problems. | A wrong sign or an unsupported minimizing step reverses or loses the bound. |

For the last construction, consider minimization with constraint `h(x)≤0`. For `λ≥0`, `f(x)+λ*h(x)≤f(x)` on original feasible points. Minimizing this expression over a larger, simpler set therefore supplies a lower bound if that minimum is obtained or bounded from below. The returned point can violate `h(x)≤0`; its usefulness as a bound does not make it an admissible answer.

Choose a relaxation by both its solving cost and its receiving use. A tighter mathematical description can be computationally worse, or make recovery harder. Existing portfolio and improvement methods can compare several candidate relaxations.

#### CMP.5:4.3 - Obtain a result with the strength its next use requires

Select an obtaining procedure for the relaxed problem. It may return an optimum, a candidate with a bound, a dual bound, or a heuristic estimate. Retain that distinction when using the result.

For minimization, a feasible relaxed point with value `P` gives an upper bound on the relaxed minimum. It does **not** by itself give a lower bound on the original minimum. To support such a lower bound, obtain the relaxed optimum or another justified lower bound `L`, for example from a feasible dual construction. MATH.20 supplies the bound argument; the relevant solver or proof supplies its computed value.

With an original feasible candidate of value `C`, the useful comparison is `L≤original optimum≤C`. A relaxed candidate's value `P` may lie on either side of the original optimum. Keep it separately when it guides recovery.

Check the computational bound direction when rounding, stopping tolerances or incomplete solving can change an exclusion or conclusion. A conservative weaker bound can be preferable to an expensive stronger one. C.11.DUA selects extra computation or assurance according to its possible effect.

#### CMP.5:4.4 - Construct an admissible original candidate

Give an effective recovery operation when a candidate is needed. Rounding, selecting a subset, scheduling fractional allocations, repairing violated conditions or searching near the relaxed answer can serve this role. Test the original conditions after recovery and explain why the operation preserves or restores them.

A generic instruction to “round the result” is insufficient. Rounding upward can violate a capacity limit, while rounding downward can leave coverage incomplete. Derive the direction and any subsequent repair from the constraints.

Track objective change through recovery. If every recovered candidate has cost at most `α` times an attained minimizing relaxation value `R*`, then `C≤α*R*≤α*original optimum` for nonnegative costs and the stated approximation factor. If the relaxed solver returns only a feasible value `P`, the first inequality may still hold with `P`, but the comparison to the original optimum needs a separate bound on `P` or a direct comparison of `C` with a justified lower bound.

Recovery can fail or produce no better candidate. Retain an already admissible better candidate. A useful bound alone can still guide search or show that further improvement is too small to matter.

#### CMP.5:4.5 - Return to the original problem and choose the next move

Return the recovered candidate under its original conditions and the bound that applies to the original objective. For minimization, an additive gap `C-L` bounds how much the candidate can still improve. A ratio uses additional conditions, such as a positive denominator; a zero or negative lower bound does not support a generic ratio claim.

Use the result to adopt the candidate, stop at an adequate gap, guide a branch of CMP.4, tighten the relaxation, revise recovery or choose a different algorithm. The stronger relaxation is worthwhile only if its expected contribution warrants the extra work.

When the question or allowed operations change, recheck the representation `i`, bound direction and recovery. A bound from a more restrictive former problem may cease to constrain the new one. A bound that remains valid may also become too weak to be useful.

### CMP.5:5 - Archetypal Grounding

#### CMP.5:5.1 - Recover indivisible choices from a fractional solution

In weighted vertex cover, a graph represents pairs that must be covered. Selecting a vertex covers its incident edges and incurs nonnegative cost `w(v)`. The original problem minimizes `sum w(v)*z(v)` with `z(v)` equal to 0 or 1 and `z(u)+z(v)≥1` on every edge.

Allow `0≤z(v)≤1` instead. Every integral cover remains feasible, so the fractional minimum is a lower bound. Obtain a fractional solution `x` and select every vertex with `x(v)≥1/2`. Each edge has an endpoint at least one half, so the selected vertices cover every edge. This derives feasibility of the rounding rule.

For each selected vertex, `w(v)≤2*w(v)*x(v)`. Summing over selected vertices, and using nonnegative weights for the remaining terms, gives `C≤2*sum w(v)*x(v)`. If `x` attains the fractional minimum, the recovered cover costs at most twice the original optimum. A merely feasible fractional point gives the displayed cost comparison but does not alone establish that approximation factor.

Consider a triangle with unit vertex costs. Setting every fractional value to one half gives value 1.5. Adding the three edge inequalities gives `2*sum x(v)≥3`, proving that 1.5 is the fractional minimum. Threshold rounding selects all three vertices with cost 3. Removing one vertex leaves a valid cover with cost 2, improving the initial candidate. Original costs are integers, so the lower bound 1.5 also implies an original cost of at least 2. The recovered cover is therefore optimal for this instance.

**Changed constraint:** add “select at most one vertex.” The fractional vector with all values one half violates this new constraint, and the recovered two-vertex cover is also inadmissible. If the cardinality constraint is deliberately dropped in the relaxation, 1.5 can remain a lower bound for feasible original solutions, but it provides no feasible cover. On a triangle one selected vertex always leaves the opposite edge uncovered, so the new original problem is infeasible. The previous recovery rule cannot be reused as a solution.

#### CMP.5:5.2 - Use a relaxed answer as a search bound

A robot moves on the finite grid with coordinates `0≤x≤2`, `0≤y≤1`. It can move one horizontal or vertical step at unit cost. The task is to go from `(0,0)` to `(2,0)`; cell `(1,0)` is blocked.

Ignore blocked cells in the relaxed problem. The distance is `abs(dx)+abs(dy)`, here 2. Every permitted original route is also a relaxed route with the same cost, so 2 is a lower bound. The straight relaxed route is unusable. An admissible detour through `(0,1),(1,1),(2,1)` costs 4, giving an initial comparison `2≤optimum≤4`.

CMP.4 can use the relaxed remaining distance at each partial route, together with the distance already traveled. Alternatively, the blocked direct row implies that a valid route must include an upward and a downward move in addition to two horizontal moves, proving a lower bound of 4. That stronger argument closes this small case. The relaxed result was useful without being mistaken for an executable original route.

**Changed operations:** allow diagonal moves at unit cost. The earlier Manhattan distance can overestimate: reaching `(1,1)` from `(0,0)` can cost 1 rather than 2. Relax the new movement problem instead. With unrestricted unit-cost horizontal, vertical and diagonal moves, `max(abs(dx),abs(dy))` is the distance and supplies the corresponding lower bound. The algorithmic thinking consists in rebuilding the comparison after the operations change.

### CMP.5:6 - Bias-Annotation

An elegant relaxed formulation can redirect effort toward solving the surrogate problem ever better while original feasibility remains unresolved. Keep the recipient's candidate or decision in view when choosing solver effort and recovery.

The word “bound” can also conceal a direction error. A convenient relaxed candidate is informative, but its objective value carries only the inequalities actually established. Calling a result approximate does not remove the need to state which conclusion the approximation supports.

### CMP.5:7 - Conformance Checklist

- The original feasible candidates, objective and useful next decision are stated.
- Every original candidate has the required representation in the relaxed problem, with the inequality in the needed direction.
- The relaxed solver's returned candidate, optimum, bound or estimate is used at its actual strength.
- Recovery is effective and its feasibility is established under the original conditions when an original candidate is promised.
- Loss through relaxation, incomplete solution and recovery is kept distinguishable where it affects the conclusion.
- Any additive or multiplicative comparison has its required sign and denominator conditions.
- A changed constraint or operation is followed through the relaxation and recovery before their result is reused.

### CMP.5:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Use a feasible relaxed objective as a minimizing lower bound | It can exceed the original optimum. Obtain an optimum, a dual lower bound or another justified bound. |
| Return the relaxed point as the original answer | Fractions or forbidden transitions can make it unusable. Construct and check recovery under the original conditions. |
| Round without examining the constraint | Coverage or capacity can fail. Derive the rounding direction and repair from the constraint's actual form. |
| Reuse the old relaxation after adding allowed operations | A former lower bound can become an overestimate, as with diagonal moves. Rebuild the problem comparison. |
| Tighten a bound after the decision is settled | Additional optimization consumes resources without changing the next action. Stop or redirect effort according to the receiving use. |

### CMP.5:9 - Consequences

A difficult problem can yield useful information and better candidates before it can be solved directly. Bounds can support early stopping, guide search and distinguish an unattained relaxed ideal from an original feasible result.

Weak relaxation or costly recovery can limit the gain. The method exposes these limitations as choices that can be changed: which conditions are relaxed, what result the easier solver supplies, and how the original candidate is reconstructed.

### CMP.5:10 - Architectural Rationale

The method joins two constructions that are often separated: making an easier problem informative and making its result usable in the original problem. Keeping recovery beside the bound prevents an easier optimum from replacing the task that motivated it.

MMP.10 supplies the formulated feasible problem when it arises from modeling; MATH.20 supplies mathematical inequalities. CMP.5 contributes the algorithmic construction of a relaxed obtaining problem and its recovery operation. CMP.4 can consume the bound without requiring a recovered candidate from every branch. Approximate subject models and general surrogate selection retain their own correspondence and portfolio methods.

### CMP.5:11 - SoTA-Echoing

[Williamson and Shmoys, *The Design of Approximation Algorithms*](https://designofapproxalgs.com/book.pdf), especially the introductory rounding constructions and later linear-programming methods, develops the link between relaxation, recovery and approximation bounds. Adopt the obligation to construct both feasibility and objective comparison. The triangle is a small worked instance of the familiar cover construction; its simple instance-specific optimality does not generalize to every graph.

The primary [SCIP 10.0 report](https://optimization-online.org/wp-content/uploads/2025/11/scipopt-100.pdf) adds a current computational consideration: relaxed bounds used in optimization can require rational or directed-rounding support to retain their direction. Adopt that consideration where the conclusion depends on it. A cheap conservative bound or direct candidate can be preferable to the additional solving and certification work.

The connection with relaxed path costs shows another use of the same construction. Here recovery is a separate route search, while the relaxed result supplies an optimistic cost.

For :4.2–4.5, compare relaxation and recovery with a direct algorithm, a cheaper feasible-candidate heuristic, and an already available valid bound. Prefer the lighter construction when it supplies the required candidate or comparison. Solving a relaxation more accurately is worthwhile when a tighter bound changes the search or when its recovered candidate improves the original result enough to repay the effort. Recovery can instead lose feasibility or too much objective value, as the changed cover case shows. Reconsider the selection when a new feasible-set relation, recovery guarantee, competing construction or resource limit changes that trade-off; an LP optimum is not a universal prerequisite.

### CMP.5:12 - Relations

- **MATH.20:** supplies the bound and inequality reasoning; **MMP.10** supplies the feasible problem in a modeled receiving use.
- **CMP.1:** transfers answers through effective problem reductions. The present relaxation can instead preserve a one-sided bound and require separate candidate recovery.
- **CMP.4:** uses relaxed bounds to exclude or prioritize search branches and to describe remaining improvement.
- **C.29 and C.29.2:** preserve the relation between the original subject question and the computational result being returned.
- **C.11.DUA and the general characterization, Pareto and improvement methods:** guide comparison of solver effort, candidate quality and further work.

### CMP.5:End

## CMP.6 - Derive an Iterative Computational Update from Local Information

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.6:1 - Problem frame

**Use this when** a desired result is hard to construct directly, but the current candidate reveals a computable improvement: a beneficial local replacement, a derivative, a violated condition or feedback about a proposed change. You need to turn that information into an update rule and determine what repeated updates can establish.

This is an algorithmic design problem. It occurs in discrete local search, iterative equation solving, optimization and learning procedures. The input need not be numerical: swapping two choices or changing one symbol can be the available operation. The difficulty is connecting an accessible local signal to a useful change of the whole candidate.

The gain is an executable update, an appropriate step or acceptance rule, and a stopping or progress account suited to the requested result. The reader needs to follow the candidate's admissible changes and comparisons. Differentiation is a prerequisite only for the derivative-based branch; MATH.10 supplies the corresponding mathematical variation.

Use a direct construction when it already gives the required result affordably. An existing iterative method can also be used directly when its hypotheses fit. This pattern is needed when the update or its justification must be constructed or changed.

### CMP.6:2 - Problem

How can local information generate an admissible sequence of computational changes with a justified improvement or termination claim, without confusing local progress, convergence and the original objective?

A direction that improves an infinitesimal model may fail at a finite step. A locally unchangeable candidate may still be globally poor. An indefinitely improving sequence may never return the finite answer its recipient needs.

### CMP.6:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Cheap information and useful direction | A local signal is accessible but can omit interactions determining the effect of a change. |
| Large progress and model validity | A large step may save iterations or leave the region where its prediction applies. |
| Feasibility and improvement | An improving unconstrained move can violate the original conditions. |
| Local and global conclusions | A local stopping test needs additional structure to establish a global optimum. |
| Iteration count and work per iteration | A stronger update may require more information or computation. |
| Computed and receiving criteria | Decreasing a surrogate or training loss can leave the intended use unchanged or worse. |

### CMP.6:4 - Solution

**Choose the comparison → construct the available changes → derive a useful update → control its extent → establish progress → return the result at its supported scope.**

#### CMP.6:4.1 - State the candidate, criterion and wanted conclusion

Describe the current candidate `x`, its admissible set and the result wanted. A criterion `J(x)` can measure an objective, a residual or a potential used to establish progress. State which it is. A potential that decreases helps analyze the algorithm; its relation to the recipient's requested answer still needs to be established.

Separate possible conclusions: one improved candidate, no improving change in a specified neighborhood, a point meeting a residual tolerance, a global optimum, or a sequence converging under stated conditions. Select the useful conclusion now rather than automatically pursuing the strongest one.

When the iteration serves a model or learner, retain its target through C.29.2 and the relevant modeling or learning method. Optimization error, error in the subject model and performance on later cases are different questions.

#### CMP.6:4.2 - Construct local changes and their obtainable consequences

Specify what may change at one step. Examples include flipping one binary choice, exchanging two assignments, updating a coordinate, adding a vector direction or replacing a violated part of a construction. MATH.10 supplies the comparison under admissible variation; the present task is to obtain a useful change by a finite computation.

Determine what information is available about a proposed change:

- a directly computed difference in `J`;
- a local approximation, such as a derivative or a small model of the objective;
- a response or estimate obtained from samples or feedback.

Choose a procedure that uses this information. A discrete local search can examine neighbor changes and select one with positive gain. A smooth minimization can use a negative gradient. A coordinate method can solve a smaller update problem while holding other coordinates fixed. A residual correction needs a relation showing how that correction changes the residual or another progress measure.

If obtaining the direction calls another hard problem, include its algorithm and cost or accept an approximate direction with an appropriate result condition. Writing an argmin expression identifies the desired update; it does not automatically supply an algorithm for obtaining it.

#### CMP.6:4.3 - Make the finite update admissible and useful

For discrete replacements, compute the whole finite difference when it is affordable. Apply only changes that retain the required constraints, or pair the change with a specified repair whose effect is included in the comparison.

For a direction `d`, construct `x'=x+η*d` with step size `η`. The local information must support that finite change. A known upper model can determine a suitable step; otherwise a trial-and-reduction rule can search for a step whose observed effect supports acceptance. Include every trial evaluation in the cost.

For example, suppose a differentiable minimizing objective satisfies

`J(x+s)≤J(x)+grad J(x)·s+(L/2)*||s||²`

on the relevant region, with known `L>0`. Choosing `s=-grad J(x)/L` gives

`J(x+s)≤J(x)-||grad J(x)||²/(2L)`.

This derives a finite descent step from a bound on the local model's error. When that bound is unavailable, an adaptive step rule needs its own termination or acceptance conditions. One unsuccessful trial can justify reducing or changing the step; it does not establish that the direction never helps.

For constrained problems, use an admissible parameterization, projection or other constraint-preserving update. Reestablish the progress account for that update. Simply clipping a coordinate can change the original unconstrained argument.

With noisy feedback, distinguish realized change from a conditional or expected improvement claim. Repeating a measurement or taking a larger sample is useful only when the additional information changes the step or its warranted use. A deterministic monotone-descent statement cannot be inferred from a noisy sign alone.

#### CMP.6:4.4 - Establish what repeated updates imply

Select a progress argument appropriate to the state space and update:

| Available structure | What can be established | What remains to be supplied |
| --- | --- | --- |
| A finite candidate set and strict improvement at every accepted change | No candidate repeats; the procedure reaches a state with no accepted improving change. | A feasible way to find or rule out such changes, and a useful bound on the amount of work. |
| A decreasing nonnegative integer potential | At most its initial value many decreases of at least one. | The potential's encoded magnitude can be large, and one iteration may be expensive. |
| A contraction or another quantitative convergence relation | A finite error bound after a chosen number of updates. | A way to compute the required update and connect that error to the requested result. |
| A descent estimate with a bounded-below objective | Bounds on accumulated improvement and, under appropriate assumptions, stationarity measures. | Convergence to one point or global optimality requires its own additional conditions. |

Use MATH.20 for the bound and MATH.21 for the convergence construction when needed. If each step improves but there is no useful stopping guarantee, return that limited procedure or change the method. Equal-value moves need their own cycle handling; strict-improvement reasoning does not cover them.

#### CMP.6:4.5 - Choose a stopping test that supports the receiving answer

Derive the test from the wanted conclusion. Exhausting a discrete neighborhood establishes local optimality for that neighborhood. A residual threshold answers a residual question; a condition or error bound is needed to convert it into distance from a solution. Small successive changes can result from a tiny step even while the candidate remains poor.

For a constrained optimum, the full gradient need not vanish. Use the absence of a feasible improving variation, a suitable projected update or the relevant constrained condition. Report that condition at the scope it establishes.

When time runs out, return the best admissible candidate or current approximation together with any supported bound. A tolerance or resource limit belongs to the use that needs the result.

#### CMP.6:4.6 - Revisit the source of a failed improvement

When the step fails, locate whether the direction, extent, feasibility repair, feedback or assumed relation to the objective changed. Revise that part. If local moves repeatedly stop at unsatisfactory candidates, enlarge or change the neighborhood, restart from another candidate, use CMP.4 to explore alternatives or obtain a bound through CMP.5.

Compare alternatives by the quality and cost relevant to the receiving use, using the existing characterization and improvement methods. Faster iteration is valuable only in relation to the result it obtains.

### CMP.6:5 - Archetypal Grounding

#### CMP.6:5.1 - Construct a discrete local-improvement algorithm

Partition the vertices of an undirected graph into two groups to maximize the total nonnegative weight of edges crossing between groups. Start with any partition. At a vertex v, let `I(v)` be the weight of its edges to vertices in the same group and `C(v)` the weight to vertices in the other group. Flipping v changes the cut value by `I(v)-C(v)`.

Compute these differences and flip a vertex whenever its difference is positive. Each flip is an admissible partition change and strictly increases the criterion. Because there are finitely many partitions, the algorithm eventually reaches one with `I(v)≤C(v)` at every vertex.

At this stopping state, `C(v)` is at least half the incident weight at v. Summing over vertices counts every cut edge twice, so the cut value is at least half the total graph weight. The total graph weight bounds any cut, giving a factor-two bound relative to the maximum cut. This is a property derived from the chosen neighborhood and nonnegative weights, rather than an assertion that every local optimum is globally optimal.

For a four-cycle with unit weights, start with all vertices in one group. Flipping vertex 1 produces a cut of value 2. Flipping the opposite vertex 3 produces value 4, which is optimal because all four edges cross. Only incident edges need updating after each flip. Finite termination alone does not make the general algorithm polynomial in the encoded input size; the number and cost of flips require a further account.

**Changed condition:** allow negative edge weights. Take four vertices with weights -3 on edges 1-2 and 3-4, and weight 1 on the four edges between those pairs. With all vertices in one group, each single flip changes the cut by -1, so the algorithm stops at value 0. Moving the pair {1,2} together to the other group produces value 4. Finite termination survives, but the former factor-two guarantee fails. A two-vertex neighborhood opens an improving move; its cost and eventual quality need their own comparison.

#### CMP.6:5.2 - Derive a step and change its constrained stopping condition

Minimize `J(x)=(x-3)²` over real x. Its derivative is `2(x-3)`. The update `x'=x-2η(x-3)` multiplies the error `x-3` by `1-2η`. Thus `0<η<1` contracts its magnitude; with `η=1`, the error oscillates without decreasing.

Choose `η=1/4`. From `x=0`, the iterates are `1.5, 2.25, 2.625, ...`; the objective values are `9/4, 9/16, 9/64, ...`. After k steps from the initial point, the distance to 3 is `3/2^k`. A requested distance at most epsilon therefore has a directly computable iteration bound. This example establishes the update through its algebra rather than through a generic instruction to repeat until the values seem stable.

**Changed constraint:** require `0≤x≤1`. Projection of the same proposed first step onto this interval gives `x=1`. Further projected steps remain at 1. The derivative there is -4, so a full-gradient-zero stopping test would never recognize the constrained optimum. Every feasible point in the interval has `J(x)≥4=J(1)`, establishing the result. The changed feasible set requires a changed stopping argument, even though a related update can still be used.

### CMP.6:6 - Bias-Annotation

A familiar update formula can displace the question of which local information is actually available. A gradient-based method, for example, needs a computable gradient or a justified estimate; a symbolic derivative on paper can still leave costly evaluation.

Visible improvement can also be mistaken for sufficient progress. Retain the relation between the improved criterion and the requested result, including the distinction between a finite-state termination argument and an affordable run.

### CMP.6:7 - Conformance Checklist

- The candidate, admissible changes, comparison criterion and requested conclusion are stated.
- The local information and the operation obtaining an update are available under the stated inputs.
- The finite step or replacement has the required feasibility and improvement account.
- Repetition has the claimed termination, convergence or limited progress conditions.
- The stopping test supports the wanted answer rather than merely detecting small changes.
- The cost comparison includes direction construction, trials, state updates and consequential arithmetic or information costs.
- A changed condition is followed through the update and its result claim before reuse.

### CMP.6:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Turn an improving direction into an arbitrary finite step | The quadratic example can oscillate or diverge. Derive step extent or supply an adaptive rule with stated conditions. |
| Stop solely because successive values barely change | A tiny step can hide a large unresolved error. Connect the stopping quantity to the result by a bound. |
| Demand zero full gradient at a constrained optimum | The interval example is optimal with a nonzero derivative. Use feasible variations or the appropriate projected condition. |
| Infer global optimality from a local stop | The neighborhood may miss a better distant candidate. Derive a global comparison or retain the local conclusion. |
| Treat finite termination as a useful runtime bound | The finite state space or potential may be enormous. Account for encoded magnitude and work per step. |

### CMP.6:9 - Consequences

The designer obtains a rule that makes a next computational change from available information and can explain what repeated use achieves. The method connects discrete improvement, continuous optimization and feedback-driven updates through their progress arguments without identifying their different guarantees.

It can also reveal that the available local information is insufficient. A new neighborhood, stronger model, additional observation or different algorithm may be required. The explicit failure locus makes that revision smaller than replacing the entire computational formulation.

### CMP.6:10 - Architectural Rationale

Update construction, finite-step control and stopping belong together because each changes what the algorithm can return. MATH.10 derives conditions from variations and MATH.21 constructs objects through convergence. CMP.6 supplies the effective rule, its repeated execution and the finite answer required from it.

CMP.5 can furnish a bound or an easier update subproblem; CMP.4 explores alternative candidates. CMP.7 can use the update to construct a learner, while keeping optimization progress distinct from performance on further cases. These are complementary algorithmic methods rather than one universal optimizer.

### CMP.6:11 - SoTA-Echoing

[Williamson and Shmoys, *The Design of Approximation Algorithms*](https://designofapproxalgs.com/book.pdf), chapter 2 and later local-search constructions, derives global comparisons from specified local neighborhoods. Adopt that style of argument rather than equating local improvement with global success. The cut example makes the neighborhood and nonnegative-weight assumption explicit; a more powerful neighborhood can require more work per update.

[Bottou, Curtis and Nocedal, *Optimization Methods for Large-Scale Machine Learning*](https://leon.bottou.org/publications/pdf/tr-optml-2016.pdf) develops obtaining procedures, step control and the distinction among optimization and statistical errors. Adopt the error-bound-to-update construction and the accounting for inexact information. Its smooth and stochastic analyses have stated assumptions; they do not govern every discrete or learned update.

For the smooth branch, compare a preset step with the upper-model or trial-controlled construction in :4.3 using the same available objective and derivative operations. A known useful L makes the derived step inexpensive; without that information, trial control spends extra evaluations to avoid an unsupported finite step. The quadratic case exhibits a concrete failure of a preset value. Retain a fixed step when its bound already supports the required result; choose trial control when its information gain warrants those evaluations. Under noisy feedback, that deterministic comparison must be replaced by the corresponding stochastic conditions.

For a finite discrete neighborhood, direct gain calculation may be simpler than fitting a continuous model. The cut example derives both update and guarantee from those discrete gains. Revisit the chosen direction, acceptance or stopping rule when feedback, admissible moves or a required progress bound changes, or when another construction obtains the same required result at lower total cost.

### CMP.6:12 - Relations

- **C.29.2:** states the obtaining task, operations and resource conditions.
- **MATH.10:** constructs admissible variations; **MATH.20** supplies bounds; **MATH.21** supplies convergence and finite-approximation reasoning.
- **CMP.4 and CMP.5:** can provide alternative exploration, a relaxed update problem or a useful comparison bound.
- **CMP.7:** uses updates in a learning algorithm while retaining a separate account of further-case performance.
- **C.11.DUA and the general improvement methods:** select the value of additional computation, information or a more costly update.

### CMP.6:End

## CMP.7 - Construct a Learner from Examples and Feedback

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.7:1 - Problem frame

**Use this when** examples or feedback are available and the required rule for further cases is missing, or an existing learning procedure must be changed for a different target, kind of feedback or resource limit. You need to construct the procedure that obtains the rule, rather than leave “learn the model” as an unexplained operation.

The situation occurs when learning a classifier, estimating a response, constructing a surrogate, discovering a program or updating a policy. The output may be a symbolic rule, a function represented by weights, a distribution or a retained set of candidate rules. Its required form follows from the intended use.

The gain is a learning procedure with explicit inputs, selection or update operations and a learned result that can be applied at its warranted scope. The reader needs functions, finite examples and a loss or another stated comparison. Probabilistic guarantees require the corresponding additional probability model; no one statistical sampling model is imposed on every learning problem.

Use an existing rule directly when it already serves the purpose. Use an established learner when its inputs, target, restrictions and costs fit. This pattern is needed when those choices or their connection to further use must be constructed or revised. Explaining a learned rule and teaching a person to apply it are distinct tasks, supplied by the explanation and development methods when required.

### CMP.7:2 - Problem

How can a computation turn examples and feedback into a useful rule for further cases, with a clear distinction between fitting the observed examples, obtaining the rule affordably and justifying its further use?

Many rules can agree on the available examples and disagree elsewhere. Faster optimization can obtain one of them more accurately while leaving that disagreement unresolved.

### CMP.7:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Expressive rules and learnability | A large rule family can represent more targets while requiring more information or search. |
| Available feedback and target use | Recorded labels or rewards may differ from the response the recipient actually needs. |
| Fit and generalization | Low loss on used examples leaves questions about unseen cases and changed conditions. |
| Statistical and computational efficiency | A class can be learnable in principle while obtaining its selected rule remains unaffordable. |
| Stability and adaptation | Retaining past information helps under stable conditions but can obstruct a changed target. |
| Point prediction and retained ambiguity | One chosen answer is convenient; unresolved alternatives can matter to the next action. |

### CMP.7:4 - Solution

**State the further use → identify available feedback → restrict the rule family → construct selection or update → establish its result → apply and revise.**

#### CMP.7:4.1 - State what a further application must obtain

Describe the input on which the learned rule will be used, the required response and the loss or gain that matters. Include the region, population, time or interaction conditions when they change that meaning. A rule predicting an observed label, a latent property and the consequence of an intervention answers different questions.

Separate the learning algorithm from the learned rule. In a batch setting, write `A(S)=h_S`: algorithm A consumes the examples S and returns rule `h_S`. A later application computes `h_S(x)` on a new input x. In an online setting, the learner also carries state and updates it as feedback arrives. The cost of obtaining a rule and the cost of applying it may favor different constructions.

State whether the recipient needs one rule, a set of alternatives, an uncertainty statement or an action selected from predictions. The output type changes what the learner must retain. A rule can be useful under a qualified assumption without an unconditional guarantee over all possible inputs.

#### CMP.7:4.2 - Recover the examples and feedback actually available

Identify the supplied inputs, labels, rewards, demonstrations or other observations and how they were obtained. For missing labels, delayed feedback, selection effects or dependence between examples, state what the learning procedure can actually observe. MMP.7 supplies the probability model of recorded data when such a model is needed.

Choose the feedback regime before deriving the update. In supervised learning, the supplied target response can evaluate a candidate prediction directly. In bandit feedback, only the consequence of a chosen action is observed; an update requiring all unchosen consequences is unavailable. A self-produced label remains the output of another rule and can propagate its errors.

State which conditions are fixed during the learning claim. Independent examples from one distribution, an arbitrary sequence generated by one stable target rule, and a changing target support different arguments. Data rows alone do not supply any of these assumptions.

#### CMP.7:4.3 - Construct the rule family and inductive restriction

Choose a family H of candidate rules and a representation in which they can be compared or updated. It may contain thresholds, programs, trees, parameterized functions or another suitable construction. Give the operations needed to apply a rule and obtain its response.

The restriction expresses which unobserved continuations the learner will consider plausible. It can come from subject structure, invariances, a simplicity preference, regularization or a previously learned representation. State the basis and the limit of the restriction. Choosing a rule family is an inference commitment, not merely a software parameter.

MMP.11 can supply a subject-grounded function family. For a surrogate, state the source responses and input region that the learned rule must serve. This pattern supplies the algorithmic way of obtaining a member or a supported collection of members from examples. If no candidate can serve the target, improve the family or representation rather than trying to optimize within it indefinitely.

#### CMP.7:4.4 - Give an effective selection or update procedure

Choose how data and feedback change the candidate:

| Construction | Effective operation | Principal condition |
| --- | --- | --- |
| Select from a finite family | Evaluate each rule on the relevant examples and select by the stated criterion, with an explicit treatment of ties. | The family and evaluations must be affordable. |
| Retain consistent candidates | Remove rules contradicted by newly observed feedback; use or combine the survivors. | Every observed label used for elimination must agree with one fixed target rule in the initial family. |
| Optimize a parameterized criterion | Construct updates or search using CMP.6 or CMP.4, including initialization, constraint handling and stopping. | Optimization progress and the meaning of the learning criterion both need their stated conditions. |

For empirical risk minimization, a typical criterion is the average loss `L_S(h)=(1/n)*sum loss(h(x_i),y_i)`. Regularization or another restriction can change the criterion. An argmin expression specifies the desired rule; the actual learner needs an obtaining procedure, including what it does when the minimum is not obtained or several rules tie.

Look for shared work and useful ordering. For thresholds, sorting examples once can let successive threshold scores be updated from counts rather than reevaluated on the whole dataset. CMP.3 supplies sharing when its identity conditions hold. For a parameterized learner, compare the work of one update, the updates needed and the later cost of applying the result.

#### CMP.7:4.5 - Establish the learning result at the strength available

Distinguish three results:

1. **Obtaining:** the algorithm returns the stated rule or collection under its inputs and computational limits.
2. **Fit or update performance:** the returned rule achieves the stated empirical criterion, or the online procedure has the stated behavior on feedback.
3. **Further-use performance:** a bound, comparison, assumption or observation supports the response on the receiving cases.

Prove or check only the result needed for the use, with additional work selected through C.11.DUA. For example, a finite fixed H with a realizable target and independent examples from the receiving distribution permits a sample-based generalization argument. A finite online candidate family can instead support a mistake bound for an arbitrary sequence under a stable realizable target; independent sampling is then unnecessary for that bound.

In a statistical argument, retain the class, loss range, dependence and selection conditions used by the theorem. Repeatedly choosing rules against the same assessment examples changes what that assessment supports. In a changed environment, all historical observations need not have the same relevance to the future query.

When available examples leave candidates disagreeing at a consequential input, return that ambiguity or choose a rule under an explicit selection basis. Obtaining an additional response is one possible move, not a default obligation. Compare its likely effect with the cost of asking, delaying or acting under the remaining uncertainty.

#### CMP.7:4.6 - Apply the result and revise the part that fails

Use the learned output on the intended further case. A discrepancy can come from the rule family, data law, target definition, optimization, representation or application. Follow the dependency that failed rather than reflexively requesting more training examples or more optimization steps.

If the target changes over time, choose a forgetting, reweighting, windowing or adaptation procedure together with the relation to the new target. C.11.DUA helps decide whether a discrepancy warrants more examples or a changed procedure; the common portfolio methods can retain several useful rules. This pattern constructs the learning operation used in that arrangement.

Return the learned rule, its application method, the conditions material to its use and the narrow reason for reopening it.

### CMP.7:5 - Archetypal Grounding

#### CMP.7:5.1 - Construct a batch selector and expose an unresolved continuation

On nonnegative integer inputs, consider the two rules `f(x)=x` and `g(x)=x mod 2`. The supplied examples are `(0,0)` and `(1,1)`. Both rules have zero squared loss on those examples.

A learner can evaluate both rules and return the minimizing set `{f,g}`. This is an effective obtained result with retained ambiguity. It can also return one rule under a declared preference, but the zero training loss alone gives no reason to prefer f over g at input 2. Their predictions there are 2 and 0.

Suppose the receiving task needs a prediction at 2 and an additional observed response is available for a cost that could be justified. If that response is 2, the same selection procedure prefers f; if it is 0, it prefers g. If the observation is not worth obtaining, use a selected rule under the remaining assumption or retain both possible responses for the downstream decision. Better minimization of the original two-example loss cannot distinguish them.

**Changed response:** suppose the response at 2 is 1. Neither rule fits all three observations. Revisit the two-rule family or the assumption of deterministic noiseless responses. Repeatedly fitting the original family more accurately cannot create the absent continuation.

#### CMP.7:5.2 - Construct an online learner and derive its mistake bound

Let H be a finite family of binary prediction rules and suppose one fixed rule in H gives every true label that will arrive. Retain the set V of rules consistent with all labels seen so far. On a new input, predict the majority label among rules in V, using a fixed tie rule. After receiving the true label, remove the rules that predicted otherwise.

On each mistaken prediction, at least half of V is removed. The true rule remains, so after M mistakes `1≤|H|/2^M`, giving `M≤log2|H|`. This establishes a bound on mistakes for an arbitrary input sequence under the stable-realizable-target assumption. It does not require independent random examples. Evaluating all survivors on each input costs up to `|H|` rule evaluations; the mistake guarantee alone does not make an enormous family affordable.

For a concrete instance, let inputs be integers 0 through 4 and let H contain six threshold rules `h_t(x)=1 if x≥t else 0`, for `t=0,...,5`. Break ties by predicting 1. At input 2, three rules predict each label, so predict 1. If the true label is 0, retain thresholds 3, 4 and 5. At input 3, the majority now predicts 0; if the true label is 1, retain only threshold 3. The two mistakes are within `floor(log2 6)=2`; subsequent predictions follow `h_3` correctly as long as the assumed target remains `h_3`.

**Changed feedback:** a later example gives label 1 at input 2. It contradicts the previously received label at 2. Eliminating the last rule would leave an empty set. The stable noiseless-target premise has failed: retain the discrepancy and choose a treatment for noise or change, such as weighting errors or using a recent-data learner. The earlier mistake proof cannot be carried through that change unchanged.

### CMP.7:6 - Bias-Annotation

Training loss and benchmark performance are visible and easy to optimize. The recipient may instead need a response in a different region or after an intervention. Keep that target explicit so that improving the visible criterion does not silently replace it.

A broad function class or large pretrained model can hide a strong inductive restriction in its representation, training history and obtaining procedure. The relevant question is which continuations it favors and how that choice fits the receiving use. Human-like explanations of a model's behavior do not by themselves supply its learning guarantee.

### CMP.7:7 - Conformance Checklist

- The future application, output type and relevant loss or gain are recoverable.
- Available examples and feedback match the operations the learner performs.
- The candidate family or other inductive restriction has a stated basis and boundary.
- Selection or update is effective, with tie, failure and stopping behavior specified.
- Obtaining, fit and further-use claims retain their distinct conditions.
- Statistical or online guarantees use the sampling, target and class assumptions they actually require.
- A contradictory or changed case leads to the relevant data, family, target or update revision rather than automatic extra training.

### CMP.7:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Use zero training error as a prediction argument | Identity and parity agree on the examples but disagree at 2. Retain the ambiguity or supply the selection basis relevant to further use. |
| Treat an optimization formula as the learning algorithm | The chosen rule can remain unobtainable. Supply effective selection or update with its computational cost. |
| Use feedback that the agent never receives | A bandit update can silently assume labels for unchosen actions. Match the operation to the actual observation regime. |
| Keep eliminating candidates after the fixed-target premise fails | The threshold example leaves no survivor. Revise the treatment of noise or change and its result conditions. |
| Assume more data or computation always resolves the failure | An inadequate family or wrong target can survive both. Locate the changed dependency before choosing more work. |

### CMP.7:9 - Consequences

Learning becomes an explicit algorithmic contribution: a reader can say what is supplied as feedback, how it changes a candidate, what rule is obtained and how that rule is used. The construction can be delegated or changed without leaving an unexplained “learn” step between modeling and computation.

The method can also expose a limit that further optimization cannot remove. New information, a better family, another target or a different receiving decision may be needed. The result remains useful when it identifies that choice without demanding unnecessary evidence.

### CMP.7:10 - Architectural Rationale

The learning algorithm and learned rule must remain distinct because their costs, inputs and failure modes differ. Inductive restriction belongs with the algorithm's construction: without it, agreement on examples leaves the future rule unspecified. The performance argument then follows the actual feedback and use rather than imposing one sampling theory everywhere.

MMP supplies data and subject-model accounts. CMP.4 and CMP.6 supply effective search or update; CMP.7 assembles those contributions into a learner. Further model assessment, explanation, development and portfolio choice use their existing methods.

### CMP.7:11 - SoTA-Echoing

[Shalev-Shwartz and Ben-David, *Understanding Machine Learning*](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf), chapters 2-5 and 21, supplies empirical selection, inductive restriction and online learning under different information assumptions. For a manageable finite family with a stable realizable target, adopt majority-and-elimination over choosing an arbitrary consistent rule when mistake reduction matters: one mistaken arbitrary choice may remove only one rule, while a mistaken majority removes at least half. The extra voting work is a real cost. When enumeration is unaffordable or feedback is noisy, this finite-family construction requires replacement or qualification.

For a large parameterized family, [Bottou, Curtis and Nocedal](https://leon.bottou.org/publications/pdf/tr-optml-2016.pdf) supplies optimization procedures and separates their error from statistical error. Adopt an affordable update through CMP.6 when direct rule enumeration fails; retain the unclosed generalization question after numerical progress.

For changing environments, [Han, Huang and Wang, *Model Assessment and Selection under Temporal Distribution Shift*](https://proceedings.mlr.press/v235/han24b.html) develops adaptive recent-history comparison instead of treating all historical assessment data as equally representative. Adopt reconsideration of data relevance and the selected assessment window when time changes the target. The benefit trades reduced historical mismatch against fewer effective observations and depends on the paper's assessment conditions; it is not a guarantee under arbitrary unobserved change.

Revisit the learning construction when the assumed feedback ceases to be available, the target or admissible family changes, or another obtaining procedure improves the required result at comparable resources. Revisit only the affected selection, update or performance argument.

### CMP.7:12 - Relations

- **C.29.2:** supplies computational formulation and application conditions; **C.11.DUA** selects worthwhile additional information or computation.
- **MMP.7:** supplies the law of recorded data when probabilistic inference is used; **MMP.11** can supply the subject response family.
- **CMP.4, CMP.6 and CMP.3:** supply search, updates and reusable intermediate work for obtaining the rule.
- **C.2.8, EXD and the development DPFs:** address what a reader or learner must understand or acquire when using and explaining the resulting method.

### CMP.7:End

# Part B - Control error and computational cost

## CMP.8 - Construct an Approximate Computation with Controlled Error

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.8:1 - Problem frame

**Use this when** computing the requested answer without approximation is unavailable or too expensive, and a cheaper computation can retain enough information for the receiving task. You need to construct that computation, determine what it loses, and control the loss through a parameter or a stopping rule.

This occurs in discrete optimization, compressed computation, function evaluation and numerical solution. Rounding item values to shorten a dynamic program and discretizing a continuous equation are different instances. The shared difficulty is obtaining a useful finite answer with a warranted relation to the original computational question.

The result is an algorithm, its approximation controls, and an answer accompanied by the error, bound or settled distinction it actually supports. The reader needs to follow the original problem and its comparisons; calculus is required only for a construction that uses it.

Use an existing adequate algorithm directly when no new approximation choice is needed. A faster procedure that preserves every requested answer may need only a representation or scheduling change. Choosing an approximate description of the subject itself belongs to modeling; this method starts from the computational question that description supplies. CMP.5 develops relaxation and recovery; the present method develops adjustable loss, finite arithmetic and stopping, including constructions that use no relaxation.

### CMP.8:2 - Problem

How can a finite computation be made affordable by discarding or approximating information while retaining the answer quality needed next?

A small internal change can produce a large output change. A small residual can coexist with a poor answer. Two refinements can agree because both omit the same contribution. Refining everything can spend the budget without reducing the error that matters.

### CMP.8:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Cheap computation and useful distinctions | Coarsening reduces work but can merge alternatives whose difference decides the answer. |
| Mathematical convergence and finite return | Eventual convergence may supply neither an affordable stage nor a recognizable stopping condition. |
| Local error and composed error | A small loss at every operation can accumulate or be amplified downstream. |
| Objective quality and admissibility | An excellent approximate objective value can accompany an infeasible returned object. |
| Precision and conditioning | More accurate arithmetic helps only the errors it controls. |
| Strong guarantees and obtaining cost | A computable conservative bound can be more useful than an inaccessible sharp one. |

### CMP.8:4 - Solution

**State the needed distinction → construct the cheaper computation → bound the lost contribution → include arithmetic and recovery → refine the limiting part → return the qualified answer.**

#### CMP.8:4.1 - Choose what approximation means for this answer

State the original input, admissible answers and receiving use. Select the comparison that use needs: absolute error in a value, relative error away from zero, distance between objects, an optimization ratio, or agreement on a named finite observation. An approximate optimum usually still needs an admissible witness.

For a threshold decision, an enclosure entirely on one side can settle the question even when it is wide. If the enclosure crosses the threshold, return the unresolved decision or refine it. Equality may require another method; do not promise that arbitrary refinement will decide every equality case.

Separate the computational target from any claim about a modeled subject. A result close to the solution of the supplied equations does not by itself establish that those equations answer the physical or organizational question. Preserve the subject interpretation through C.29 and the applicable modeling method.

#### CMP.8:4.2 - Construct a family of cheaper procedures

Choose what to simplify and provide the operations that obtain the simplified answer. Possibilities include rounding values to reduce the number of states, truncating a series with a bounded tail, evaluating on a finite grid, retaining a compressed summary, or stopping an iteration once a sufficient bound is reached.

Let a parameter control the discarded information. It can be a rounding interval, polynomial degree, mesh size, retained rank, iteration count or arithmetic precision. Describe how changing it alters both the algorithm and the information retained. One parameter need not control every source of error.

If the construction changes the feasible set, provide a recovery procedure and its feasibility argument. If it changes only the objective used to select an answer, establish how that selection compares under the original objective. CMP.2 and CMP.3 can construct and schedule the resulting subproblems.

Try the simplest family that can meet the receiving requirement. A parameterized approximation scheme is unnecessary when one cheap direct calculation or an already available bound settles the question.

#### CMP.8:4.3 - Carry error through the operations actually used

Relate the computed intermediate object to the original target. MATH.20 supplies comparison arguments; MATH.21 supplies approximation and convergence. The present task must make their sufficient stage obtainable.

For example, if an intermediate approximation has distance at most e from its target and the next operation G obeys `d(G(u),G(v))≤L*d(u,v)` on the relevant inputs, this contribution to final error is at most L*e. Add another error term only when it measures a comparable discrepancy and an argument, such as a triangle inequality, permits that addition. A probability of failure and a numerical error are different quantities.

For an optimization construction, compare the original objective of the recovered candidate with the original optimum. Follow every inequality in its proper direction. Rounding values can bound objective loss while leaving constraints unchanged; rounding constraint coefficients needs a separate admissibility argument.

When several approximations are composed, carry their bounds through the actual downstream operations. Allocate finer resolution where it changes the final bound most usefully. An unbounded sensitivity or a lost discontinuous distinction can require another formulation rather than further use of the same family.

#### CMP.8:4.4 - Include finite arithmetic and the sensitivity of the question

An algorithm implemented with finite representations performs approximations beyond those in its ideal construction. Identify consequential rounding, overflow, underflow, cancellation and approximate comparisons. Use integer or rational operations, higher precision, a stable reformulation or directed bounds where they improve the required answer affordably.

**Conditioning** describes how the mathematical answer responds to changes in the problem data. **Forward error** compares the returned value with the requested answer. **Backward error** asks how much the data would need to change to make the returned value an answer to the changed problem. Fix the permitted data changes and the measure of their size; those choices determine the claim.

A small backward error supports a small forward error only with suitable sensitivity control. A stable calculation cannot recover a distinction already absent from uncertain input data. Conversely, a well-conditioned question can be computed poorly by an unstable expression; :5.2 demonstrates a local repair.

Use a cheap bound or estimate of sensitivity when a stronger computation would not change the decision. When even the error bound is computed approximately, preserve the direction needed for its use.

#### CMP.8:4.5 - Derive refinement and stopping from the receiving requirement

Choose a stage from an a priori bound or use an observable enclosure with a justification that refinement reduces it. Include the work and storage needed to reach that stage. A bound polynomial in a numeric magnitude can still be exponential in that magnitude's encoded length.

Identify what currently limits the answer: approximation loss, arithmetic, insufficiently known input, or an unresolved subject assumption. Refine the responsible part. Comparing two resolutions can reveal failure or help estimate a rate, but their agreement alone is not a bound on the unresolved remainder.

Stop when the supported result is sufficient or when further refinement is not worth its expected effect. C.11.DUA helps compare additional computation with acting under the remaining uncertainty. Return a conditional or partial answer when that is what the available construction supports.

#### CMP.8:4.6 - Use the result and revise the affected construction

Return the value or witness together with the approximation meaning needed by its recipient. Distinguish a proved error bound, an empirically estimated error and an unbounded heuristic approximation.

A changed tolerance can require a different stage. A changed requested property can invalidate the error measure. A changed arithmetic format can invalidate an implementation argument while preserving the mathematical scheme. Reopen that part, retaining the constructions and comparisons that still hold.

### CMP.8:5 - Archetypal Grounding

#### CMP.8:5.1 - Round profits to construct a shorter discrete computation

Choose a subset of items within capacity W to maximize total profit. After removing items individually too heavy, suppose there are n items with positive integer weights and nonnegative integer profits `p_i`. If no positive profit remains, the empty subset is optimal. Otherwise let `P=max p_i`; at least that one item is feasible, so `P≤OPT`.

For `0<ε<1`, set `K=ε*P/n` and scaled profits `q_i=floor(p_i/K)`. Keep weights and capacity unchanged. Construct a dynamic program `D(j,q)` returning the minimum weight of a subset of the first j items with total scaled profit q:

```text
D(0,0) = 0; D(0,q) = infinity for q > 0
D(j,q) = min(D(j-1,q), w_j + D(j-1,q-q_j))
```

An out-of-range index is infeasible. Retain enough choices to recover a subset, and select the largest q with `D(n,q)≤W`. Including zero, there are at most `n*floor(n/ε)+1` scaled-profit positions. The straightforward table therefore takes `O(n³/ε)` arithmetic operations; weight arithmetic and witness storage have their own costs. Compute the rounding reliably when ε is supplied as a finite rational value.

Let A be the returned subset and O an original optimum. Because A maximizes the scaled profit among the same feasible subsets,

`p(A) ≥ K*q(A) ≥ K*q(O) > p(O)-n*K ≥ (1-ε)*OPT`.

The strict middle inequality follows from losing less than K on each of at most n selected items. Thus the returned object remains feasible and its loss is controlled, without knowing OPT in advance.

For A=(weight 5, profit 12), B=(3,7), C=(2,6), capacity 5 and `ε=1/2`, K=2 and scaled profits are 6,3,3. A and {B,C} tie under the scaled objective; a rule retaining A returns profit 12 although the optimum is 13. The approximation claim permits this. With `ε=1/4`, K=1 and the scaled objective distinguishes profit 13 from 12, returning {B,C}.

If the requested result changes to every optimal subset, the former error guarantee is insufficient. K=1 restores the original integer objective and lets this table obtain the optimal value, but can restore the large table the approximation was designed to avoid. Enumerating every optimum also requires reconstruction of every feasible subset attaining that value, including alternatives discarded by the minimum-weight entry. For example, with capacity 2 and two items of weights 1 and 2, each with profit 5, either singleton is optimal, although the minimum-weight entry retains only the first. The number of optimal subsets, and hence enumeration output, can be exponential. CMP.4 offers search with bounds; the cost and output requirement decide the choice.

#### CMP.8:5.2 - Repair an unstable evaluation without changing its target

Compute `f(x)=sqrt(1+x)-1` for a small positive x. Under binary64 round-to-nearest arithmetic, take `x=10^-16`. The addition can round `1+x` to 1, so the direct expression returns zero. The positive mathematical answer is about `5*10^-17`.

Rationalizing gives the same real-valued function:

`f(x)=x/(sqrt(1+x)+1)`.

Even when the computed square root is 1, this expression returns approximately `5*10^-17`, preserving the small contribution through the numerator. Near positive zero, the relative condition number is `(sqrt(1+x)+1)/(2*sqrt(1+x))`, which tends to 1. The failure of the direct expression therefore comes from its evaluation, not a large relative sensitivity to x.

This repair assumes the receiving requirement concerns f(x). If it instead asks for an accurate derivative obtained by subtracting nearby rounded function values, that is a new computation. The value repair alone supplies no error bound for that differentiation.

### CMP.8:6 - Bias-Annotation

Numerical language can conceal discrete approximation. The subset construction keeps feasible objects while coarsening selection values; the function construction changes arithmetic while preserving the real function. Neither branch makes calculus, floating-point arithmetic or an optimization objective mandatory for every approximate computation.

### CMP.8:7 - Conformance Checklist

- The receiving answer and approximation comparison are stated, including feasibility or a required witness.
- A finite procedure obtains each selected stage; its loss is related to the original computational target.
- Composed error follows the operations and comparisons actually used.
- Consequential arithmetic error is distinguished from sensitivity to input and from subject-model discrepancy.
- The stopping or refinement rule has an appropriate warrant and affordable execution.
- The returned qualification distinguishes a bound, an estimate and an unbounded heuristic.

### CMP.8:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Treat a good objective value as an admissible answer | Rounded constraints can admit an invalid object. | Preserve constraints or construct and justify recovery. |
| Stop because adjacent refinements agree | Both can omit the same contribution. | Bound the unresolved tail or use a justified enclosure. |
| Increase precision for every failure | Input uncertainty or subject-model error can dominate. | Identify the limiting contribution first. |
| Use a relative error at a zero target | The ratio is undefined or unstable. | Select an absolute or otherwise meaningful comparison. |
| Transfer an approximation guarantee to a changed output | Near-optimal value need not identify all optima or preserve derivatives. | Reconstruct the comparison for the new requested result. |

### CMP.8:9 - Consequences

Approximation becomes a controllable part of algorithm design. The reader can trade computation against a stated loss, distinguish a local implementation repair from a changed problem, and return a useful answer before exhausting every possible refinement.

Some requested distinctions remain too costly or are unsupported by the input. The construction exposes that limit and the specific stronger operation or premise needed to cross it.

### CMP.8:10 - Architectural Rationale

An adjustable approximation joins a mathematical comparison to an effective algorithm. Convergence alone supplies no running procedure; a fast procedure alone supplies no relation to the desired answer. Keeping obtaining, loss, representation and use together makes each approximation step inspectable and replaceable.

Feasibility, accuracy and the receiver's decision are separate obligations because one can survive while another fails. The same distinction permits composition with relaxation, iterative updates, probabilistic estimation and subject modeling without imposing one error measure on all of them.

### CMP.8:11 - SoTA-Echoing

How should an approximation become an affordable algorithm with a selected error? **Adopt** the scaling-and-bound construction illustrated in [MIT's advanced algorithms notes on approximation schemes](https://courses.csail.mit.edu/6.854/21/Notes/n20-approx.html): connect rounding loss to the original objective and to the size of the resulting dynamic program. Sections :4.2–4.5 and :5.1 make those connections explicit. A direct unrounded computation is preferable when its state range is already affordable; the scaled construction deliberately accepts a weaker answer in return for a range controlled by ε.

The simple table is not the strongest known knapsack complexity result. [Chen, Lian, Mao and Zhang, version 3](https://arxiv.org/html/2308.07821v3), combine proximity and approximate profit-function composition to obtain a substantially stronger bound. **Adapt** the comparison lesson: retain the transparent table for a small construction or a suitable workload, but reconsider its representation and composition when its `n³/ε` cost becomes limiting. The stronger asymptotic result does not establish an implementation advantage for every small input. A competing scheme meeting the same output requirement at lower total application effort reopens that choice.

For the numerical branch, **adopt** Higham's separation of [conditioning](https://nhigham.com/2020/03/19/what-is-a-condition-number/) and [backward error](https://nhigham.com/2020/03/25/what-is-backward-error/) in :4.4. Compared with increasing arithmetic precision without locating the error, a local stable reformulation can retain the answer with less work; :5.2 derives one such case. Backward error is useful only for the permitted perturbations and with the sensitivity needed by the output. A changed input uncertainty, output operation or arithmetic implementation reopens this numerical choice. These arguments do not rank the adequacy of the subject model.

### CMP.8:12 - Relations

- **MATH.20 and MATH.21:** supply bounds, convergence and sufficient finite observations; this method supplies the executable approximation and its cost.
- **CMP.3:** constructs shared computation and storage for finite stages; **CMP.5** supplies relaxation and recovery; **CMP.6** supplies iterative updates.
- **C.29.2:** fixes the computational answer, representation and resource conditions.
- **C.29 and MMP.9:** preserve the separate subject correspondence and model-reduction question when this algorithm computes a model's consequence.
- **C.11.DUA:** compares the value of further refinement with its cost and remaining uncertainty.

### CMP.8:End

## CMP.9 - Construct a Randomized Estimator or Sampling Procedure

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.9:1 - Problem frame

**Use this when** a computation needs a sample from a specified law, or an estimate that would be expensive to obtain by enumeration, and the sampling or estimation procedure must be constructed or changed. Available random bits, a stream, a convenient proposal distribution or local transitions can supply the starting operations.

The algorithm must connect those operations to the requested distribution or statistic. A random-looking output is insufficient: it may sample records in proportion to their multiplicity, favor high-degree states, or omit a rare but consequential contribution.

The gain is an effective sampler or estimator with its target, bias and dependence understood sufficiently for the receiving use. The reader needs elementary probability, expectations and the stated computational access. The method applies to discrete choices, data streams, simulation and learned procedures; a physical noise source is one possible realization.

Use a direct deterministic computation or an already suitable sampler when it meets the need affordably. Choosing a probability model for observations is a separate modeling task, supplied by MMP.7 when applicable. This method can also sample a mathematically specified set without making any empirical-population claim.

### CMP.9:2 - Problem

How can available random operations produce the desired law or an informative estimate under finite time and storage, and what conclusion remains warranted after changing the sampling or stopping procedure?

More samples reduce some variation but do not repair a wrong target or a missing region of support. Correct stationary probabilities do not establish rapid convergence from the chosen start. An interval valid for one fixed sample size may not remain valid when repeatedly inspected to decide when to stop.

### CMP.9:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Accessible randomness and target law | The easiest draws may have different probabilities from those the task needs. |
| Broad coverage and informative samples | Oversampling useful regions helps only with an appropriate correction and retained support. |
| Cheap transitions and useful information | Correlated steps may be inexpensive but add little information. |
| Unknown stream length and fixed storage | A representative sample must remain valid as unseen records arrive. |
| Adaptive effort and stated error | Stopping according to observed values changes some uncertainty guarantees. |
| Reproducibility and independent repetitions | Reusing a seed repeats a calculation; it does not create another independent draw. |

### CMP.9:4 - Solution

**Name the target law or quantity → choose obtainable random operations → derive the output law or correction → account for variation and dependence → choose effort and stopping → return and revise the qualified result.**

#### CMP.9:4.1 - Separate the target, access and output

State whether the result is a random object, a subset, an expectation, an event probability, or another statistic. For sampling, specify the target probabilities, item identity, replacement rule and any order requirement. For estimation, define the quantity, such as `μ=E_p[f(X)]`, before designing how X will be obtained.

Describe access: an indexed collection, a one-pass stream, evaluable weights, a generative operation, or neighbors of a current state. An evaluable probability density does not necessarily provide a cheap sampler. An unnormalized density does not supply its normalization constant.

If the inputs describe observations, MMP.7 supplies the relevant recording and inclusion law. Sampling uniformly from recorded rows remains different from sampling uniformly from the people, events or other objects those rows describe.

#### CMP.9:4.2 - Construct the random operation and its output law

Start with a random primitive whose assumptions are explicit, such as independent uniform bits or uniform integers in a bounded range. A finite generator supplies a particular implementation. Its period, correlations, state reuse or exposure to an adversary matter when the receiving claim depends on them.

For a finite categorical law with known probabilities, a cumulative-probability partition can transform a uniform draw. When generating a uniform integer from b bits for a range of size m, simply taking the remainder can bias the result unless m divides `2^b`. One repair accepts only bit values below `floor(2^b/m)*m`, then takes their remainder; rejected draws are repeated. Choosing `2^b≥m` makes this an effective rejection construction with acceptance greater than one half.

For a stream, maintain a distributional invariant that survives one new record; :5.1 derives such an update. For a proposal distribution q different from p, either correct the output distribution through an acceptance rule or correct the estimated contribution through weights. Derive which of those results the procedure actually returns.

When direct draws are unavailable, a transition rule can maintain a desired stationary law. Construct the transition probabilities and the condition that preserves that law. Reachability, convergence from the start and correlations remain additional algorithmic questions; :5.3 shows why an uncorrected neighbor walk can target the wrong distribution.

#### CMP.9:4.3 - Derive the estimator and its error sources

For independent draws from p, the mean of `f(X_i)` estimates `E_p[f(X)]`. Its expectation equals the target when the expectation exists. With finite variance σ², the mean's variance is `σ²/n`.

For independent draws from q, use contributions `Y_i=f(X_i)*p(X_i)/q(X_i)` when the ratio is computable and q is positive wherever `f*p` contributes. Then `E_q[Y_i]=E_p[f]`. Inspect the second moment under q: a poor proposal can greatly increase variance. If an unknown normalizing constant leads to a self-normalized ratio of sums, its finite-sample bias and uncertainty require their own account.

For dependent draws, the variance of a mean includes covariance terms:

`Var(mean Y_i)=(sum_i Var(Y_i)+2*sum_(i<j) Cov(Y_i,Y_j))/n²`.

This identity does not require stationarity. A chain's approximate equilibrium, correlation and initial transient cannot be assessed just by counting iterations. Use an applicable mixing argument, a justified dependence-aware uncertainty method, or retain a weaker empirical conclusion.

Keep computational variation distinct from uncertainty in the target model. Sampling an assumed distribution accurately improves its computed consequences; it does not by itself validate that distribution for the subject.

#### CMP.9:4.4 - Choose sample effort and a compatible stopping rule

Select the error statement that changes the receiving decision. For independent identically distributed contributions bounded in `[a,b]`, Hoeffding's bound gives

`P(|mean Y_i-μ|≥e)≤2*exp(-2*n*e²/(b-a)²)`

at a fixed n chosen independently of their observed values. Thus `n≥(b-a)²*log(2/δ)/(2*e²)` suffices for error at most e with failure probability at most δ. The range and independence assumptions belong to this particular bound.

If results are inspected to choose the stopping time, use a compatible sequential bound. A simple conservative construction assigns `δ_n=δ/(n*(n+1))` and applies a fixed-n bound at each n with that failure budget. Since the budgets sum to δ, all resulting intervals cover simultaneously with probability at least `1-δ`. Stop when the current interval settles the question. More efficient confidence-sequence methods can replace this construction under their stated hypotheses.

Generating more draws is one possible improvement. A better proposal, stratification, fewer redundant transitions or an affordable deterministic calculation can improve the answer more per unit work. Include the cost of drawing, evaluating, weighting and retaining the results. Use C.11.DUA when deciding whether further computation is worthwhile; exploratory sampling need not acquire a formal interval unless the intended claim needs one.

#### CMP.9:4.5 - Return the useful result and identify what a change invalidates

Return the sample or estimate with the target and qualification its recipient needs. Distinguish samples without replacement, independent repeated draws, correlated states and weighted observations. A retained seed can support replay; uncertainty across repetitions needs genuinely distinct random streams under the assumed generator model.

Check a finite case by deriving or enumerating its output probabilities. A frequency experiment can expose an implementation error, but agreement on a small run does not establish a claimed law for every input.

A changed inclusion rule, target statistic, proposal, random source or stopping rule can invalidate a different part of the construction. Revise that part. Preserve already useful samples only with the correction and dependence account that their new use requires.

### CMP.9:5 - Archetypal Grounding

#### CMP.9:5.1 - Keep one uniform record from a stream of unknown length

Store the first record. At record t, replace the stored record with probability `1/t`; otherwise retain it. Use a uniform integer in 1 through t to make this decision.

After t records, the new record has probability `1/t`. Every earlier record had probability `1/(t-1)` before this step and survives with probability `(t-1)/t`, giving `1/t` as well. This establishes the invariant inductively. The procedure needs one record, a counter, and one update decision per arrival; counter and record representation costs remain visible.

For the stream A, A, B, the resulting value is A with probability 2/3 and B with probability 1/3. This is correct uniform sampling of record positions. If the new request is uniform sampling of distinct values, the old invariant answers a different question. One construction keeps a set of already seen values and applies the same update only on a first occurrence. That requires storage for the distinct-value set or another algorithm with its own access and error assumptions.

#### CMP.9:5.2 - Concentrate draws without changing an expectation

The target is the mean of values 0,0,0,4 under the uniform law on four identifiable outcomes, so μ=1. Direct draws have variance 3 per contribution.

Choose proposal probabilities `q=(1/8,1/8,1/8,5/8)`, concentrating effort on the nonzero contribution. The corrected value on outcome 4 is `4*(1/4)/(5/8)=8/5`; the other corrected values are zero. Its expectation is `(5/8)*(8/5)=1`, and its variance is `(5/8)*(8/5)²-1=3/5`. At the same number of independent draws, this construction reduces variance by a factor of five; the proposal and weighting cost decide the actual work benefit.

Using the unweighted sample mean instead has expectation `(5/8)*4=5/2`, the wrong target. Increasing the sample count would concentrate that wrong answer. If the required statistic changes to a different function on the four outcomes, retain the proposal only after recomputing its support, corrections and variation for that function.

#### CMP.9:5.3 - Correct a local walk before using it as a sampler

Sample uniformly from three states connected in a path, `0—1—2`. A walk that chooses an adjacent state uniformly spends stationary probabilities `(1/4,1/2,1/4)`: the middle state has twice as many incident choices. Uniform selection among neighbors does not imply uniform selection among visited states.

Correct a proposed move x to y by accepting it with probability

`min(1, π(y)*q(x|y)/(π(x)*q(y|x)))`,

where π is the target and q the proposal probability. A rejection retains x. For positive target weights on connected states, the probability flow on either direction of an edge becomes the same minimum of the two proposed flows, so detailed balance holds. Normalizing constants cancel in the ratio.

For this uniform target, accept an end-to-middle move with probability 1/2 and a middle-to-end move with probability 1. The transition matrix, in state order 0,1,2, is

```text
1/2  1/2   0
1/2   0   1/2
 0   1/2  1/2
```

Its rows and columns each sum to one, so the uniform law is stationary. The finite chain is connected and has self-transitions, hence converges from any start. Its other eigenvalues are 1/2 and -1/2; for this small matrix, powers give an explicit decreasing transient. For instance, starting at 0 gives `(1/2,1/2,0)` after one step and `(1/2,1/4,1/4)` after two, still not uniform.

If the three target weights change to `(1,2,1)`, the original uncorrected neighbor walk has that stationary law. Reusing the former uniform-target acceptance probabilities would now be wrong. In either case, adjacent states are dependent observations; an independent-draw variance formula cannot be justified by the stationary law alone.

### CMP.9:6 - Bias-Annotation

A large sample count is an easy proxy for quality. The examples instead inspect the sampling unit, correction and transition law. Their small size permits direct derivation; a large state space may require stronger analysis or a more limited conclusion.

Randomness here is an algorithmic resource. Whether a physical source or pseudorandom generator adequately supplies it depends on the particular claim and environment, including adversarial use.

### CMP.9:7 - Conformance Checklist

- The target law or statistic, sampling unit and available access are explicit.
- Random primitives and the transformation, invariant or transition law determine the stated output.
- An estimator includes the needed correction and support condition.
- Bias, variance, dependence and target-model uncertainty are distinguished where they affect use.
- Sample effort and stopping support the error claim actually made.
- A changed target or sampling condition has a local consequence for the procedure and its qualification.

### CMP.9:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Sample a convenient law and average without correction | The estimate converges to another quantity. | Derive the weighting or acceptance operation. |
| Call repeated rows independent draws | Shared randomness or chain state can preserve dependence. | Model their joint generation and its error consequence. |
| Assume stationary means already equilibrated | The initial transient can remain large. | Establish sufficient mixing or qualify the finite result. |
| Inspect a fixed-n interval until it looks decisive | Its original coverage need not survive optional stopping. | Fix the sample size or use a compatible sequential bound. |
| Replace uniform records by uniform entities silently | Multiplicity changes inclusion probabilities. | Change the sampling unit and its obtaining algorithm. |

### CMP.9:9 - Consequences

An expensive enumeration can be replaced by a controlled random computation, and a sample can be maintained despite limited access or storage. The same derivation exposes a wrong target before more computation reinforces it.

A valid construction can still be inefficient. Support, weight variability, mixing and evaluation cost identify different routes to improvement; they do not all yield to a larger sample count.

### CMP.9:10 - Architectural Rationale

Sampling and estimation share the construction of an output law but return different things. An estimator can correct biased sampling without turning the retained draws into unweighted samples from the target. A transition can preserve a distribution without supplying independent draws. Keeping these results distinct makes their composition with learning, search and modeling reliable.

The general method derives probability statements from effective operations. Probability modeling supplies a target where needed; algorithmics supplies how to obtain, transform and use finite draws under resource limits.

### CMP.9:11 - SoTA-Echoing

How can a stream yield a uniform sample without knowing its length? **Adopt** the invariant-based construction in [Vitter, *Random Sampling with a Reservoir*, §2](https://www.cs.umd.edu/~samir/498/vitter.pdf), specialized to one stored record in :5.1. A two-pass method is simpler when counting and revisiting the input are cheap; reservoir updating removes that access requirement. Vitter also derives skip-based alternatives, so a per-record random decision is not asserted to be the fastest realization. Changed access costs, weighted sampling or a distinct-entity target reopen the choice.

When useful events are poorly represented by direct draws, **adopt** [Owen's importance-sampling construction, §§9.1–9.3](https://artowen.su.domains/mc/Ch-var-is.pdf), in :4.3 and :5.2: correct the contribution and compare variation together with drawing and weighting cost. Direct sampling remains preferable when a proposed correction costs more than the information it gains or produces unstable weights. A changed integrand, support, normalization or proposal can reverse the selection. The construction does not certify an empirical probability model.

For local state exploration, **adopt** the separation of stationary-law construction and mixing developed in [Levin and Peres, *Markov Chains and Mixing Times*, second edition, chapters 3–4](https://pages.uoregon.edu/dlevin/MARKOV/). Sections :4.2–4.3 and :5.3 retain that distinction instead of treating every random walk as a suitable sampler. Direct draws avoid a transient when available at comparable cost; local transitions are useful when direct generation is expensive and their finite-time behavior is adequate. A changed target, proposal, connectivity or mixing bound reopens that comparison.

When the stopping time follows the observations, **adapt** [Howard, Ramdas, McAuliffe and Sekhon's confidence-sequence framework](https://arxiv.org/abs/1810.08240) in :4.4. A fixed-n bound remains the lighter choice for a fixed-n claim; a simultaneous bound pays extra interval width to retain the claim under repeated inspection. The elementary failure-budget construction gives one transparent implementation, while the paper supplies sharper alternatives under explicit assumptions. Changed dependence, contribution bounds or stopping use requires a new compatible comparison.

### CMP.9:12 - Relations

- **MMP.7:** constructs the law of recorded data when the sampling target comes from observations.
- **C.29.2:** supplies the computational result, access and resource conditions; **MATH.20** supplies bounds used in the probability argument.
- **CMP.7:** uses generated examples or estimated feedback in a learning procedure; **CMP.6** uses stochastic feedback in an update.
- **CMP.3:** supplies storage and recomputation choices; shared draws must retain their dependence when reused.
- **C.29.3:** connects a computational procedure to its physical realization.
- **C.11.DUA:** chooses worthwhile additional sampling or a conditional result at the available effort.

### CMP.9:End

## CMP.10 - Choose a Computational Representation for Its Access and Update Operations

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.10:1 - Problem frame

**Use this when** a computation spends too much effort finding, updating, combining or storing information, and changing its representation could improve those operations. The mathematical objects may already be understood; the missing choice is how to obtain the needed answers from their stored form.

A sequence can be stored directly or through partial aggregates. A graph can be represented by a matrix or by lists of neighbors. The same relation can have very different computational consequences under those choices. Conversely, a compact representation can lose the multiplicity, ordering or state distinction needed after an update.

The result is a representation with effective read and update operations, a meaning-preservation argument, and a cost comparison for the intended workload. The reader needs the object's relevant operations and elementary algorithm analysis. No particular programming language or hardware is required.

Keep the existing representation when it already serves the work affordably. Choosing what the subject model should describe is a separate task. Here the target distinctions are sufficiently known to ask how different representations support their computation; a discovered missing distinction returns to that formulation.

### CMP.10:2 - Problem

How can a representation be constructed around the operations that matter, so that cheaper access or update retains the information and behavior required by the computation?

An encoding can be reversible yet expensive to query. A small stored summary can answer one question while making a later question impossible. An update can be cheap locally but invalidate a shared aggregate, index or cached interpretation.

### CMP.10:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Read cost and update cost | Precomputed answers accelerate queries but need maintenance when inputs change. |
| Compactness and accessible distinctions | Fewer stored bits can require expensive decoding or discard required identity. |
| Local operations and global invariants | A changed element can affect several summaries or indexes. |
| Initial conversion and repeated use | A better per-operation bound may never repay construction cost. |
| Abstract operation count and realization | Bit growth, memory transfer and output size can dominate a word-operation estimate. |
| Generality and workload fit | A versatile structure can cost more than a simpler one for the actual operation mix. |

### CMP.10:4 - Solution

**Name the operations → choose retained distinctions → construct representation and invariants → derive reads and updates → compare total work → use and revise the choice.**

#### CMP.10:4.1 - Start from the operations and their conditions

List the operations needed by the computation, including their inputs and returned results. Distinguish membership, enumeration, selection by order, aggregation, insertion, deletion and value replacement when their requirements differ. Include whether answers need original identities or only values.

Describe the anticipated operation sequence or range of workloads. A fixed dataset with many queries differs from a changing stream. If the mix is unknown, compare alternatives over the plausible range instead of inventing one universal average.

State which resources constrain the work: storage, worst-case response, total running time, memory transfers or communication. Include the required output size; listing k distinct items takes work to produce those k items under an ordinary explicit-output model.

#### CMP.10:4.2 - Choose what the representation must distinguish

Define how a stored state represents the abstract object or the observations required of it. State the invariants that make reads meaningful. A sorted array needs an order invariant; an aggregate tree needs each stored aggregate to agree with the segment it represents.

If two source states share one representation, check every required read and continuation. Their equality must preserve the requested answers after the allowed updates. MATH.2 supplies identification under operations. If the representation is deliberately lossy, CMP.8 supplies the approximate answer relation.

Keep consequential identity, multiplicity and ordering. A set removes duplicates; a sequence retains positions. A zero numeric value need not mean an absent relation. An object reference and a copied value respond differently to later mutation.

#### CMP.10:4.3 - Construct operations from the representation's structure

Choose a structure whose retained information makes the frequent operation cheaper. A sorted array supports binary search by repeatedly excluding one ordered half. A hierarchy of aggregates answers a range query by combining a small set of segments. Lists of actual neighbors avoid scanning absent graph edges.

Derive each read and update from the invariant. For an update, identify every stored part whose meaning depends on the changed input, and restore it. Include shared summaries and the operations used to recover an original witness. CMP.3 supplies reuse and dependency reasoning when values are cached across computations.

When summaries are combined, state the algebra the procedure needs. An associative operation permits regrouping; it need not permit reordering. An identity element can represent an empty segment. Inverses are required only for a method that subtracts or otherwise undoes an aggregate, not for every range-query construction.

For dynamic storage, include growth and rebuilding. Doubling an array's capacity gives occasional linear copying and bounded total copying over a sequence of appends. The resulting amortized append cost does not claim constant worst-case latency for every individual append. A latency requirement can select incremental rebuilding or another representation.

#### CMP.10:4.4 - Count the complete computation under an explicit cost model

Compare construction and conversion, the intended reads and updates, reconstruction or output, and peak storage. A useful first comparison is `construction cost + sum of operation costs` for the workload. Keep several resource dimensions separate when no accepted trade-off combines them.

State what one elementary operation costs. Arithmetic on a bounded machine word can be treated as constant in an appropriate model; multiplying or comparing integers whose encoded lengths grow needs the corresponding bit cost. A symbolic expression that shares subexpressions can be small while its fully expanded output is large.

If transfers between memory levels dominate, analyze blocks moved as well as abstract pointer or arithmetic operations. A representation with contiguous access can outperform one with fewer but scattered accesses. Realization measurements can distinguish close candidates; they need not precede a decision already settled by an adequate cost argument.

Include invalidation and synchronization when shared updates are part of the workload. An operation that is correct in sequential use does not acquire a concurrent guarantee merely because its representation is shared.

#### CMP.10:4.5 - Compare alternatives at the receiving use

Construct the simplest credible alternative, not only a slower version of the favored structure. Compare raw storage with a precomputed index, full retention with reconstruction, or a compact representation with an expanded one according to the actual operations.

Require preservation of the needed answers before treating reduced cost as improvement. For a deliberate approximation, retain its qualified result and the loss it buys. Use the existing characterization, Pareto and improvement methods when choices trade storage, latency, update work and precision; no single representation must dominate every workload.

Select conversion only when its cost and risk are justified by the expected subsequent use. A mixed strategy can keep a simple base representation and add one index for the consequential query. Its update obligations remain part of the choice.

#### CMP.10:4.6 - Return a usable representation and reopen it locally

Return the structure, its meaningful state, read and update procedures, and the resource consequence that motivated the change. A small worked operation should expose the invariant and a consequential change should test its maintenance.

Reconsider the choice when the query mix, update pattern, output identity, data magnitude or physical access cost changes. Preserve the abstract object and valid algorithms where they remain applicable. A newly required distinction that the old representation discarded may require returning to the source data, not merely rebuilding an index from the insufficient summary.

### CMP.10:5 - Archetypal Grounding

#### CMP.10:5.1 - Design stored aggregates for mixed queries and updates

Maintain a sequence of n integers with two operations: replace one element and return the sum of the first k elements. A raw array gives a constant number of word accesses for replacement and k additions for a prefix query. Precomputing every prefix sum makes queries constant-time, but a replacement can change all following prefix sums.

For frequent interleaved queries and updates, build a balanced binary tree over consecutive segments. A leaf stores one element; each internal node stores the sum of its children's segments. Padding to a power of two with zero-valued leaves gives fewer than 4n nodes for n>0 and logarithmic height. Build the sums from the leaves upward in linear many additions.

To replace an element, change its leaf and recompute every ancestor from its two children. To query a prefix, use a fully included segment's stored sum; ignore an excluded segment; at a partially included segment descend into its children. Only the boundary path is partially included, so at most a constant number of nodes per level are visited. Both operations take `O(log n)` additions/accesses, with integer bit costs counted separately.

For `[3,1,4,2]`, the two half sums are 4 and 6 and the root is 10. The prefix of length three combines the left half's 4 and the third leaf's 4, returning 8. Replace the second value by 5: its leaf becomes 5, the left sum 8 and the root 14. The same query now returns 12.

If updates disappear and many queries remain, the simpler prefix array may be preferable. If the aggregation changes to concatenation, retain left-to-right order. For leaves A,B,C,D, the prefix of length three must be ABC; regrouping into AB and C is valid, but combining them in reverse order returns CAB. The tree construction needs associativity, not commutativity. Its unit-cost sum analysis does not automatically apply to copying growing strings.

#### CMP.10:5.2 - Choose graph access by the question, retaining edge meaning

For a directed graph with n vertices and m edges, a Boolean adjacency matrix supports a membership test by one entry lookup. Enumerating a vertex's outgoing neighbors scans n entries. Adjacency lists store actual neighbors; enumeration examines its outgoing degree many entries, while a plain-list membership test can require the same scan. A hash index adds another storage/update trade-off.

A traversal that marks each vertex once and enumerates its outgoing edges therefore takes `O(n+m)` accesses with lists, and up to `O(n²)` with a matrix, excluding construction and output. Repeated pair-membership questions on a dense graph can favor the matrix. The graph's mathematical identity alone does not choose the computational representation.

Now attach numeric weights. If zero is used both for an absent edge and for an existing zero-weight edge, those two states become indistinguishable. For edges `0→1` with weight 0, `1→2` with weight 2 and `0→2` with weight 5, treating zero as absence deletes a path of cost 2 and leaves the apparent direct cost 5. Repair the representation with a separate presence indication or an absent value outside the admitted weights. Changing the shortest-path algorithm cannot recover an edge already discarded by its input representation.

### CMP.10:6 - Bias-Annotation

Familiar data-structure names can substitute for operation analysis. The examples instead derive the structure from mixed prefix operations or graph access. They assume a sequential computation and state their elementary costs; shared or unusual physical realizations require their corresponding conditions.

### CMP.10:7 - Conformance Checklist

- Required reads, updates, output identity and workload conditions are stated.
- Stored states have an interpretation and the invariants needed by those operations.
- Reads and updates are effective and preserve the required distinctions.
- Cost includes construction, maintenance, recovery, output and consequential representation growth.
- The chosen representation is compared with a credible simpler alternative on the intended workload.
- A changed operation or lost distinction leads to a specific reconstruction or source-return step.

### CMP.10:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Choose the smallest encoding | Decoding or updates dominate the computation. | Compare the required operations including conversion. |
| Treat all integers as constant-cost values | Operand lengths grow beyond the cost model. | Count bit operations or bound the admitted magnitudes. |
| Update only the changed leaf | Dependent aggregates or indexes retain obsolete answers. | Restore every affected invariant. |
| Reorder associative aggregates | Associativity alone does not permit exchanging operands. | Preserve order or establish commutativity for this operation. |
| Use one value for absence and a meaningful zero | The reader cannot reconstruct the discarded distinction. | Represent presence separately. |

### CMP.10:9 - Consequences

Algorithmic cost becomes changeable through a deliberate representation choice. A reader can replace an expensive access pattern, expose hidden maintenance or decoding work, and retain the original computational meaning through the change.

The best choice can vary with workload and realization. A new operation can reveal that a previously adequate summary is insufficient, opening a return to the richer source or a revised answer requirement.

### CMP.10:10 - Architectural Rationale

A computational representation is useful through what its operations obtain. Reversible encoding, mathematical equivalence and fast access are distinct properties; none implies all the others. Invariants connect them by explaining how stored states support the required observations and updates.

The method therefore places operation design and resource comparison together. It uses mathematical preservation and general portfolio comparison while retaining algorithmic responsibilities for effective conversion, access, maintenance and output.

### CMP.10:11 - SoTA-Echoing

Which representation serves a required mix of operations? **Adopt** the interface-to-implementation comparison in Morin's [*Open Data Structures*, chapters 2](https://opendatastructures.org/newhtml/ods/latex/arrays.html) and [12](https://opendatastructures.org/newhtml/ods/latex/graphs.html), for :4.1–4.5 and :5.2. It compares concrete operations rather than ranking structures by familiarity or compactness. Direct arrays or matrices remain serious alternatives to more elaborate indexing when their workload is favorable. Additional summaries deliberately trade maintenance and storage for cheaper queries; :5.1 derives a balanced aggregate construction with those obligations. A changed query/update mix or required identity reopens the comparison.

When memory transfers dominate, **adapt** the external-memory and cache-oblivious analysis developed in [Demaine's survey](https://people.csail.mit.edu/edemaine/papers/BRICS2002/paper.pdf), in :4.4. Its competing cost model exposes a limit of equal-cost memory accesses. A blocked or recursive layout can reduce transfers while adding construction complexity; choose it only when that saving matters for the receiving work. The historical survey supplies the analysis distinction, not a current hardware performance ranking. A changed memory hierarchy, data layout or measured bottleneck can reverse the practical selection without invalidating the abstract operation argument.

### CMP.10:12 - Relations

- **C.29.2:** supplies computational formulation and the elementary resource model.
- **MATH.2, MATH.17 and MATH.18:** supply identification under operations, operations as objects and preservation through interpretation.
- **CMP.2 and CMP.3:** construct recursive operations and shared intermediate results.
- **CMP.8:** supplies a controlled approximation when the representation intentionally loses information.
- **C.29.3:** establishes relevant physical realization conditions.
- **C.11.DUA and the general characterization, Pareto and improvement methods:** compare the useful effect of conversion, measurement and further optimization.

### CMP.10:End

## CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.11:1 - Problem frame

**Use this when** repeated attempts to accelerate a computation leave a question about what any algorithm could achieve under the available access. You can construct different admitted inputs that require different answers but remain indistinguishable before enough queries, comparisons, communication or stored information.

The gain is a lower bound tied to an explicit computational model, or a concrete change of access or requested answer that escapes that bound. This can stop fruitless optimization, reveal a needed index or observation, and separate an intrinsic restriction of the chosen model from a poor implementation.

The reader needs to follow the input family, allowed observations and the demanded answer. Counting, elementary probability or a mathematical adversary argument is used according to the branch. The adversary is a proof construction: it keeps several inputs consistent with what an algorithm has learned.

Use a known applicable bound directly when no new argument is needed. Timing one program establishes its performance, not a lower bound for every program. Undecidability through an effective reduction uses CMP.1; physical energy or transport limits use their physical formulation. The present method establishes computational information requirements under specified access.

### CMP.11:2 - Problem

How can one establish a minimum amount of computational work without enumerating every possible algorithm, and use the result without extending it beyond the model that made the proof valid?

An algorithm can make adaptive choices, preprocess data, exploit a promise or use randomization. A proof that ignores an allowed operation can forbid a procedure that actually works. A lower bound valid for a comparison model can disappear when keys have an accessible integer encoding.

### CMP.11:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Universal algorithm claim and bounded model | The proof must cover every admitted procedure without claiming more access restrictions than the task has. |
| Adaptive queries and remaining alternatives | Later queries depend on earlier answers, so the argument must survive that choice. |
| Strong answer and affordable observation | Exact identification can cost more than approximation or a promise-restricted decision. |
| Worst-case and expected cost | A hard input for each deterministic rule need not be one hard input distribution for randomization. |
| Preprocessing and online response | A cheap query can hide information acquired earlier. |
| Useful restriction and impossible-demand rhetoric | A bound should change construction or expectation, not merely declare the task hard. |

### CMP.11:4 - Solution

**Fix access and answer → construct indistinguishable alternatives → bound how fast observations separate them → respect the cost and error quantifiers → state the limit → change the assumption that constrains the work.**

#### CMP.11:4.1 - State the computational model and the claimed quantity

Specify the admitted inputs, promised structure, allowed queries or operations, prior information and required output. Count what the claim concerns: number of input probes, comparisons, transmitted bits, retained states, total time or another defined resource.

Include preprocessing and advice where they depend on the input. If preprocessing builds an index, distinguish its cost from a subsequent query's cost. An operation that reveals an entire vector is different from one that reads one bit, even if both are written as one function call.

State whether the bound concerns worst-case or expected cost, deterministic or randomized computation, and exact or error-tolerant answers. For randomization, say whether the error guarantee holds on every input and which randomness is available. These quantifiers determine the argument.

#### CMP.11:4.2 - Construct alternatives that the available observations have not separated

Describe a transcript: the sequence of queries and replies, or messages and observations, available to the procedure. Consider all inputs still consistent with it. If two of those inputs require incompatible answers, a deterministic procedure seeing that transcript cannot correctly finish on both.

Construct those alternatives rather than simply counting unknown data. For a bit query, place a decisive difference at an unread position. For a comparison algorithm, retain different orders compatible with the observed comparisons. For a communication or streaming algorithm, find different earlier inputs that lead to the same message or stored state but require different outputs after one common continuation.

Adapt the construction to the permitted answer. Distinct inputs do not need separate transcripts when the same answer is acceptable for both. A common approximation interval or permitted error can therefore weaken the lower bound.

#### CMP.11:4.3 - Turn indistinguishability into a resource bound

Use the form that fits the access:

- **Adversary:** answer queries while retaining incompatible possible inputs. Show how many queries are needed before no such pair remains.
- **Counting:** if each observation has at most b possible replies, q observations have at most `b^q` transcripts. If N input classes require mutually different outputs, then `b^q≥N`, giving `q≥log_b N` for a worst-case depth bound.
- **State or message collision:** with fewer than N distinguishable retained states or messages, two of N necessary input classes collide. A shared continuation then forces an error.

Establish that each constructed transcript is consistent with at least one admitted input. An adversary that combines incompatible answers proves nothing about the actual problem. A counting argument needs output-distinct classes, not merely many syntactically different inputs.

When an algorithm already provides an upper bound in the same model, compare the two. Matching orders of growth can establish asymptotic optimality for that model. A gap locates remaining room for a better construction or a stronger argument; it is not itself proof that the current algorithm is improvable.

#### CMP.11:4.4 - Handle randomization and average cost with their own argument

Fixing random choices gives a deterministic procedure, but its hard input may depend on those choices. That alone does not establish a bounded-error randomized lower bound on a fixed input.

One route chooses a distribution on inputs before the random choices. If every deterministic procedure within the allowed budget has error greater than δ under that distribution, averaging gives the same obstruction for any mixture of them. A randomized algorithm with error at most δ on every input would contradict it. Use the matching cost convention; a worst-case budget argument does not automatically establish a claim about expected budgets.

Another route couples runs on two inputs using the same random choices and bounds how often they see different observations. Section :5.1 applies this directly. A statistical or information inequality can supply a broader version when observation distributions overlap instead of agreeing exactly.

Keep quantum queries or stronger observation primitives outside a classical-query conclusion unless the proof actually covers them. Their admissibility is a model choice, not an implementation detail that can be ignored.

#### CMP.11:4.5 - Return the limit with a useful continuation

State the bound, input family, access, error and cost conditions together. Indicate whether it rules out the requested budget, establishes optimality within an order, or leaves a gap.

Identify a consequential escape: restrict the input by a defensible promise, allow a weaker answer or error probability, acquire an additional observation, preprocess and retain information, use a stronger primitive, or change the representation. Determine which premise of the lower-bound argument that change removes, then construct the new procedure. Renaming the same operations does not escape the bound.

Use C.11.DUA to decide whether proving a tighter bound or obtaining additional information would change the next move. A sufficient lower bound can already justify changing the task; there is no obligation to solve a harder open complexity question first.

### CMP.11:5 - Archetypal Grounding

#### CMP.11:5.1 - Determine whether any bit is one

An unknown n-bit input is accessed one bit at a time. Return whether it contains a one. For a deterministic always-correct algorithm, answer zero to every query. Before all n distinct positions have been read, both the all-zero input and an input with a one at an unread position remain possible. Their correct answers differ. Therefore some input requires n queries. A complete scan attains that bound.

Allow a randomized algorithm that uses at most q queries on every run and errs with probability at most `δ<1/2` on every input. Couple its runs on the all-zero input and on the input with just position j set to one, using the same random choices. Unless the zero-input run queries j, both runs have the same transcript and output. Let `p_j` be the probability it queries j on the zero input. Consequently,

`P(output 1 on singleton j) ≤ P(output 1 on zeros)+p_j ≤ δ+p_j`.

Correctness on the singleton requires the left side to be at least `1-δ`, so `p_j≥1-2δ`. Summing over j gives

`q ≥ sum_j p_j ≥ n*(1-2δ)`.

For `δ=1/3`, this gives `q≥n/3`. It is a lower bound under the stated maximum-query convention, not a claim that every randomized algorithm uses exactly that many queries.

Now change the promise: either all bits are zero or at least half are one. Query k independently chosen uniform positions, returning one if any query finds it. On a nonzero promised input, the probability of missing every one is at most `2^-k`; zero inputs always receive the correct answer. For `0<δ<1/2`, choosing `k=ceil(log2(1/δ))` therefore achieves the error requirement independently of n, subject to generating and accessing those positions. For n>2, the singleton inputs used in the earlier bound are excluded. This explains why the new algorithm escapes that growth in cost.

#### CMP.11:5.2 - Bound comparison sorting and identify its escape

Sort n distinct opaque keys, with their order available only through pairwise comparisons. A comparison has two possible outcomes. The `n!` possible input orders require different output permutations, so a correct decision tree needs at least `n!` leaves. A binary tree of height q has at most `2^q` leaves. Thus the worst case needs at least `ceil(log2(n!))` comparisons, which grows as `Ω(n log n)`.

This bound is about comparison sorting. If each key is an integer in `0..K-1` and direct array indexing is an allowed elementary operation, count occurrences in K counters and emit keys in index order. That construction uses `O(n+K)` counter/access operations and corresponding output work. It escapes the comparison bound by observing the encoding through indexing. Large K, long integers or a requirement to preserve distinct record identity can change its storage and reconstruction costs.

A practical consequence is to compare representations and access before spending effort trying to make an ordinary comparison procedure sort arbitrary distinct keys in fewer than order `n log n` comparisons. If comparisons themselves are expensive, a matching comparison count still leaves their internal cost to reduce.

#### CMP.11:5.3 - Expose information hidden in a message

One agent has an n-bit string x and sends one fixed-length binary message to another agent holding y. The receiver must decide whether x=y with no error. If two different strings x and x' produce the same message, take the common receiver input y=x. The receiver sees identical information in both cases but must answer differently. All `2^n` strings therefore need distinct messages, requiring at least n bits. Sending x achieves it.

If public independent random masks and an error probability are admitted, the task changes. For each mask r, send the parity of the positions where both x and r are one; the receiver compares with its parity from y. Equal strings always match. For unequal strings, choose one differing position: toggling its independent mask bit pairs masks with opposite comparison outcomes, so the parities match with probability 1/2. After k independent masks, falsely accepting equality has probability `2^-k` and the message has k bits. The shared random masks and local parity-computation cost are explicit resources, not information transmitted by the message.

### CMP.11:6 - Bias-Annotation

The word “impossible” can obscure the condition that makes a lower bound true. Each example states an access model and then changes a premise to construct a different result. These are algorithmic limits; interpreting a computed object as a subject property and realizing operations physically remain separate questions.

### CMP.11:7 - Conformance Checklist

- Inputs, promises, observations, preprocessing and required outputs are specified.
- The cost and error claim has explicit worst-case, expected or probabilistic quantifiers.
- Indistinguishable alternatives are admitted inputs requiring incompatible answers.
- The adversary, counting or collision argument covers adaptive behavior allowed by the model.
- Randomized claims use an argument valid for randomization and the stated cost convention.
- The conclusion names both its restriction and a useful continuation or unresolved gap.

### CMP.11:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Generalize from a slow implementation | Another algorithm may avoid its work. | Prove a requirement for every admitted transcript or procedure. |
| Count distinct inputs without considering acceptable answers | Several inputs may legitimately share one output. | Count output-distinct classes. |
| Supply an inconsistent adversary | No actual input could produce its replies. | Retain a nonempty compatible input family. |
| Fix randomness, then choose a different hard input for each seed | This can miss a successful randomized algorithm. | Use one prior input distribution or a valid coupled argument. |
| Ignore input-dependent preprocessing or stronger access | The algorithm already acquired the supposedly missing information. | Charge or expose that resource and restate the model. |

### CMP.11:9 - Consequences

A failed search for a faster algorithm can become a specific limit or a more promising problem. The bound identifies which observations, distinctions or access restrictions determine the remaining cost and helps decide whether to optimize, reformulate or change the requested answer.

The conclusion is conditional. It can remain correct while a new representation, promise or randomization changes what is achievable in the practical task.

### CMP.11:10 - Architectural Rationale

Lower bounds complement construction by studying what a successful construction must distinguish. Transcript-based reasoning handles entire classes of algorithms because identical observed information forces identical deterministic behavior, or bounds the separation of randomized behavior.

The access model belongs in the claim because it determines the observations available. This connects computational complexity to representation and mathematical argument while avoiding an unsupported claim about every possible physical or organizational realization.

### CMP.11:11 - SoTA-Echoing

How can a performance limit cover procedures not yet invented? **Adopt** the decision-tree construction in [Morin's comparison-sorting analysis](https://opendatastructures.org/newhtml/ods/latex/sorting.html), in :4.2–4.3 and :5.2. It overcomes the limit of timing or analyzing only the current algorithm by counting distinctions every comparison procedure must make. Direct performance analysis remains the cheaper sufficient method when the question concerns only that implementation. A new access primitive, key promise or output requirement reopens the universal comparison claim.

For randomized access, **adopt** the explicit separation of deterministic, zero-error, bounded-error and expected-cost models in [Blais's *Randomized Complexity*, query-complexity treatment](https://cs.uwaterloo.ca/~eblais/cs860/w25/queryseparations), for :4.1 and :4.4. The coupled proof in :5.1 supplies its own bound rather than transferring a deterministic adversary unchanged. A direct coupling is lighter than a general minimax argument when it settles the limit; an input-distribution or stronger information method is useful when the simple pair does not. Changed promises, error or cost quantifiers reopen that selection.

The same course's [communication-complexity treatment](https://cs.uwaterloo.ca/~eblais/cs860/w25/communication), following Rao and Yehudayoff's 2020 account, supplies the transcript and public-randomness distinction adapted in :5.3. A full string is the simple zero-error choice; random parity accepts bounded error to reduce communication while retaining local computation and shared randomness. A changed requirement for zero error, private randomness or adaptive adversarial inputs changes the comparison. This bounded choice does not claim that communication, query and physical limits are interchangeable.

### CMP.11:12 - Relations

- **MATH.19 and MATH.20:** supply argument construction and bounds.
- **CMP.1:** transfers algorithms or impossibility through effective reductions; this method derives a limit directly from available information.
- **CMP.9:** constructs random operations and their probability qualifications.
- **CMP.10:** changes representation, access and preprocessing while retaining the required answers.
- **C.29.2:** states the computational problem and cost model; **C.29.3 and PHY.3** address physical realization and physical limits separately.
- **C.11.DUA and C.40:** support choosing further argument, another resource or a changed problem when the bound changes the development direction.

### CMP.11:End

# Part C - Interpret, transform and compose computations

## CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.12:1 - Problem frame

**Use this when** a calculation, rule language or program description has an intended meaning, but an effective way to execute it is missing, too costly or must change. You need to construct evaluation rules, translate the description into another executable form, or repair a translation that changes the result or behavior on which its user relies.

The reader can distinguish the admitted expressions and the operations they describe. The task is to turn those distinctions into an algorithm for evaluation or translation. Programs become inputs and outputs of that algorithm: a reader can examine how a rule is executed and change the rule's representation without silently changing its use.

The result is an interpreter or effective translation, with the correspondence needed to use its output. Depending on the question, the preserved observation may include returned values, state changes, interaction, failure or termination. A compiler for a programming language, an evaluator for symbolic expressions and an interpreter for a decision language are different applications of this method.

Use an existing suitable evaluator or translator when it already provides the needed behavior affordably. Designing the notation's useful distinctions is a separate question when those distinctions are still unknown. Choosing a physical realization follows the computational construction and its actual resource requirements.

### CMP.12:2 - Problem

How can expression meaning be turned into effective evaluation and translation rules, so that the resulting computation preserves the observations needed by its user?

A mathematical interpretation can assign a meaning without providing an algorithm for obtaining it. A text substitution can preserve printed names while changing what they refer to. A translation can return the right value on a simple test while evaluating an unwanted branch, capturing another binding or failing to terminate on a previously terminating input.

### CMP.12:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Meaning and obtaining | Knowing what answer an expression denotes leaves the effective evaluation work to be constructed. |
| Local syntax and surrounding bindings | The same expression can refer to different values in different environments. |
| Equal final values and observable behavior | Order, effects, failure and termination can matter even when a returned number agrees. |
| Repeated interpretation and prior translation | Translation can save later dispatch work while adding construction time and retained code. |
| Compositional reasoning and execution context | A correct component must retain its meaning when combined with neighboring components. |
| Abstract operations and finite resources | Arithmetic range, stack capacity and foreign operations can change the admitted execution. |

### CMP.12:4 - Solution

**Recover expression structure and observations → construct evaluation rules → make control and binding effective → construct the translation → establish the needed correspondence → execute and revise the changed rule.**

#### CMP.12:4.1 - Recover the expression structure and the intended observations

Identify the constructors of admitted expressions and how their parts bind and compose. Work with a parsed structure when precedence, grouping or scope matters. A name occurrence must reach the declaration or external input intended by the language. If the supplied text admits different parses that change the answer, resolve that difference before constructing one evaluator.

Specify what evaluation receives and what its user can observe. Inputs can include the expression, name bindings, stored state and external responses. Outputs can include a value, changed state, a sequence of interactions or a failure. Distinguish a language-defined error from the absence of a defined operation; a translator can be required to preserve the former without being required to assign a meaning to the latter.

Choose the required relation between source and target observations. Equal returned values may suffice for a terminating pure expression. An interactive program may require the same ordered events. A source with several permitted behaviors may allow the target to choose among them; retaining every source possibility is a stronger requirement. Timing, memory use or a probability law belongs in this relation only when the receiving question uses it.

#### CMP.12:4.2 - Derive effective evaluation rules for each constructor

Construct the evaluator by cases on expression structure. For a literal, return its value. For a name, obtain its binding. For an operation, evaluate the required operands in the specified order and apply the available primitive. For a conditional, evaluate its test and then only the selected branch when that is the language's rule.

Give binding an explicit operation. In an immutable lexically scoped language, evaluating `let x=a in b` first obtains a's value in the current environment, then evaluates b in an environment extended with that binding. The extension's scope ends with b. Nested use of the same printed name need not change the earlier binding.

For a function expression, construct an applicable value containing the parameters, body and the bindings its later execution needs. Such a value is a **closure**. To apply it under lexical scope, extend its saved environment with the argument bindings and evaluate its body there. If variables can change, distinguish names, storage locations and current contents so that a captured reference continues to designate the intended location.

Expose the primitive's actual operation. An instruction to select an element satisfying a condition needs a search or other obtaining procedure. An unbounded search must retain its possible nontermination. If the implementation language has different arithmetic, truth values or evaluation order, translate those operations deliberately rather than inheriting its defaults.

#### CMP.12:4.3 - Make control, progress and resource use executable

Decide what remains to be done after the current subexpression returns. A recursive evaluator can retain that continuation in its own call stack. An explicit evaluator can instead store pending operations, environments and return destinations as data. Construct the transition that resumes the pending work with the obtained result.

Distinguish the termination of translation from the termination of the translated program. A compiler that traverses a finite syntax tree can terminate even when the generated program runs indefinitely. A step limit can return a suspended computation; reaching that limit does not establish divergence. CMP.1 supplies the limit on general termination decision when that question arises.

Count consequential dispatch, environment lookup, retained continuations, arithmetic and storage. Removing repeated syntax analysis may repay compilation for repeated execution. For a rarely used or frequently changing expression, direct interpretation may be the cheaper choice. Retain the existing algorithmic cost and comparison methods rather than assuming compilation always improves the work.

#### CMP.12:4.4 - Construct translation from the evaluation structure

Choose a target instruction or expression language with defined execution rules. For each source constructor, generate the target operations that perform its required evaluation. Construct the translation of subexpressions and then their combination, retaining temporary results until their consumers use them.

Preserve binding and control at this construction step. Allocate fresh temporary names or use addresses whose scopes cannot capture unrelated bindings. Place conditional branches behind the appropriate control transfer. Pass arguments and return results through agreed locations. An operator with effects requires the relevant order and number of executions; algebraic reassociation alone does not supply that permission.

State how source values, environments and observations correspond to target ones. A target representation may require encoding inputs and decoding outputs. Check that admitted values fit its arithmetic and storage operations. If one representation deliberately approximates another, use CMP.8 for the qualified relation instead of claiming unchanged values.

When several translation passes are used, connect their actual input and output relations. Each pass's output must satisfy the next one's premises. MATH.17 and MATH.18 supply composition and interpretation reasoning; the computational work additionally provides the terminating conversion and executable target operations.

#### CMP.12:4.5 - Establish the correspondence at the scope needed

For a structurally recursive translation of a terminating expression language, use induction on expression construction. Include the context that surrounding code can supply: an arbitrary admitted environment, earlier stored values and the continuation after the translated fragment. A claim that works only with an empty stack may fail as soon as two fragments are composed. Section :5.1 derives the stronger usable claim.

For stateful or interacting languages, relate source and target states and the observations their transitions produce. Explain how matching transitions reestablish the relation. If several internal steps implement one visible step, account for their completion; an infinite internal loop must not masquerade as successful preservation of a terminating computation. Choose the simulation direction or behavior relation that supports the requested conclusion. Showing that one source run has a target counterpart alone leaves other target behavior unresolved.

An alternative is to describe sets of terminating, diverging, failing or interacting behaviors and show that translation preserves the selected relation between them. Use this when the language's semantic operations and composition laws make the argument simpler. Preserve the distinctions that the use needs when choosing this mathematical representation.

Separate a general preservation claim from a check on selected translations. A small comparison can expose a defective rule or settle a bounded receiving case. A claim covering every admitted expression needs an argument covering that class. Use C.11.DUA to choose further testing, translation-specific validation or a general proof according to what the receiving decision requires.

#### CMP.12:4.6 - Run the construction and revise the failed correspondence

Evaluate or translate a meaningful input and use the resulting value or behavior. Return the construction together with the input, binding, execution and recovery conditions needed by its recipient. When comparison fails, locate the changed constructor, binding, primitive, control rule or value correspondence.

A changed language feature or execution context reopens its dependent translations. Preserve unaffected rules. Adding assignment requires revisiting captured bindings; changing integer arithmetic requires revisiting arithmetic correspondence; allowing externally supplied code requires examining the contexts with which translated components interact.

### CMP.12:5 - Archetypal Grounding

#### CMP.12:5.1 - Derive an arithmetic interpreter and stack translation

Expressions are integer literals, names and binary addition, subtraction or multiplication. An environment ρ supplies every free name. Both source and target use unbounded integers. The source evaluator returns a literal, looks up a name, or evaluates the left operand and then the right operand before applying the operator.

The target stack is written from bottom to top. `PUSH n` appends n; `LOAD x` appends ρ(x). For `ADD`, `SUB` or `MUL`, pop the right operand b and then the left operand a, and append respectively `a+b`, `a-b` or `a*b`.

Construct the compiler C:

- `C(n) = PUSH n`.
- `C(x) = LOAD x`.
- `C(a op b) = C(a); C(b); OP`, where OP is the matching target operation.

The useful induction claim is: for every admitted ρ and every initial stack S, running `C(e)` leaves `S · [eval(e,ρ)]`, with earlier entries unchanged. Literals and names append the required value. For a binary expression, the induction hypothesis for a gives `S · [eval(a,ρ)]`; applying the hypothesis for b to that whole stack appends `eval(b,ρ)`. OP replaces just those two entries by their required combination. This proves the claim and supplies the composition condition.

With ρ(x)=5, compile `(x+1)*(x-2)` to:

```text
LOAD x; PUSH 1; ADD; LOAD x; PUSH 2; SUB; MUL
```

Starting above an earlier stack value 99 gives successive added values 5, 1, then 6; next 5, 2, then 3; multiplication leaves `[99,18]`. Each syntax-tree node produces one instruction. Integer operation costs and peak live stack values still depend on the values and expression structure.

**Changed arithmetic:** suppose the target uses unsigned eight-bit wraparound. For `x+1` at x=255 it returns 0, while the source returns 256. Preserve the source by using a wider or multiword representation, restrict the admitted inputs by a valid range argument, or deliberately change the source meaning to modular arithmetic. A successful parse and a preserved instruction order do not fix the arithmetic mismatch.

#### CMP.12:5.2 - Preserve a function's binding when its call site changes

Extend the evaluator with immutable lexical bindings, function values and function application. Evaluate:

```text
let x = 2 in
  let f = (lambda y: x + y) in
    let x = 100 in f(3)
```

Creating f saves its body, parameter y and the environment in which x is 2. Calling f extends that saved environment with y=3, so the body returns 5. Looking up free x in the caller's environment would return 103 and implement a different binding rule.

The closure makes a rule available as a value without discarding its needed surroundings. A procedure can return it, receive it as an argument or construct a new closure that composes it with another rule. Each later application follows the saved bindings and the new arguments.

**Changed feature:** now permit assignment to the original captured x before calling f. If the language specifies capture of that variable's location, assigning it 7 makes `f(3)` return 10. Keeping a copied value 2 would instead return 5. Represent the environment as names mapped to locations and obtain current values from the store; a later shadowing declaration must allocate a different binding. Revise the capture and lookup rules without changing the arithmetic rule.

#### CMP.12:5.3 - Preserve which operation is executed

Let `ifzero(test,a,b)` evaluate test and then only a when the result is zero, otherwise only b. Let division by zero be a defined execution error. The expression `ifzero(x,0,10/x)` returns 0 at x=0 and 5 at x=2.

A translation that evaluates all three parts and then selects a value raises the unwanted division error at x=0. Instead generate fresh labels and conditional control:

```text
LOAD x
JZ zero
PUSH 10; LOAD x; DIV
JMP end
zero: PUSH 0
end:
```

`JZ` pops the test and jumps when it is zero; otherwise execution continues. `JMP` transfers control unconditionally. `DIV` pops right then left and divides left by right, using rational values here. Resolve each fresh label to its instruction position before execution. At x=0 the division instructions are skipped; at x=2 they append 5. Either path preserves earlier stack entries and appends one result.

If the branches instead emit commands, the same construction retains which command occurs. If the source is deliberately changed to evaluate both branches, the preservation claim and translation must change with it. The control rule, rather than a particular programming language's spelling, determines this choice.

#### CMP.12:5.4 - Preserve completion through internal steps

The source instruction is `return 7`; the receiving use requires that return. A target first takes k internal steps and then returns 7, where k is a supplied nonnegative integer. Use a remaining-step counter: each internal step reduces it by one, and at zero the target returns. For every finite k the counter proves that the internal phase finishes, so the target supplies the required result.

Change the target to `loop: goto loop`, leaving `return 7` after this loop. Each internal step goes back to `loop`, so the return is unreachable. A correspondence that allows arbitrarily many silent steps without a completion argument would hide this failure. Restore a finite internal phase to meet the required return.

### CMP.12:6 - Bias-Annotation

A familiar implementation language can silently supply truth tests, numeric limits, scope or evaluation order. Recover the intended operation before reusing that default. The arithmetic, closure and conditional cases each show a different observation lost by an apparently straightforward implementation.

### CMP.12:7 - Conformance Checklist

- Expression formation, binding and needed observations are recoverable.
- Every required evaluation step has an available operation and an explicit control rule.
- Translation terminates on its admitted descriptions; execution progress has its own stated scope.
- Source and target values, bindings, states and observations have the correspondence required by the use.
- The preservation argument includes the surrounding state or context needed for composition.
- Cost includes translation and execution under the actual arithmetic and storage assumptions.
- A changed rule or failed comparison leads to a specific reconstruction.

### CMP.12:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Copy the implementation language's defaults | The interpreted language acquires unintended arithmetic, scope or order. | Implement the source operation and its conditions explicitly. |
| Substitute names by spelling alone | A new binder captures an unrelated occurrence. | Preserve binding through fresh names, locations or scoped addresses. |
| Evaluate every child before choosing a branch | An unselected operation fails or produces an unwanted effect. | Compile the language's conditional control. |
| Prove a stack fragment only from an empty stack | The result cannot justify embedding after another fragment. | Establish its effect above any admitted earlier stack. |
| Treat a timeout as a divergence result | A terminating run may simply require more steps. | Return suspension or use an applicable termination argument. |

### CMP.12:9 - Consequences

Descriptions of computations become material for further computation. A reader can construct an evaluator, remove repeated interpretation work, combine translated fragments and diagnose a changed result through its binding, control or representation rule.

Preservation is relative to the observations and contexts selected. A useful translation may leave a reverse translation unavailable, select among allowed behaviors, or preserve values while having different resource costs.

### CMP.12:10 - Architectural Rationale

An expression, its mathematical meaning, an evaluator and one execution are different objects in this work. Keeping their correspondence visible lets operations themselves become inputs to constructive transformation. MATH.17 and MATH.18 provide the mathematical composition and interpretation; algorithmics supplies an effective evaluator or converter and explains its execution.

The preservation claim includes composition because translated fragments are normally used together. The arbitrary earlier stack, captured environment and selected branch are three forms of context that change what a local construction must retain. State-based and behavior-based descriptions offer different ways to carry that argument across a larger language.

### CMP.12:11 - SoTA-Echoing

How should expression meaning become executable? **Adopt** the constructor-based evaluation and saved-environment application in [SICP's evaluator](https://sicp.sourceacademy.org/chapters/4.1.1.html) for :4.2–4.3. Its historical contribution is exposing operations otherwise hidden in a host language. A direct evaluator is a serious cheaper choice for changing or infrequently executed expressions. **Adapt** [SICP's compilation construction](https://sicp.sourceacademy.org/chapters/5.5.html) when prior analysis repays its cost over subsequent runs: construct operations instead of repeatedly selecting them during execution. Keep binding and control semantics while comparing conversion, code storage and later execution. A changed execution frequency, primitive or language feature reopens that choice.

Which preservation claim supports actual reuse? **Adopt** the explicit behavioral scope in the current [CompCert manual, section 1.2](https://compcert.org/man/manual001.html), for :4.1 and :4.5. Matching final values is sufficient only for uses governed by those values; interaction and termination can require more. CompCert's theorem has its own language-defined behavior and undefined-behavior treatment, and excludes time and memory consumption from its observed trace. A translator for a language with a defined division error therefore needs the error policy chosen in :5.3, not an imported C-specific permission to remove it. A changed observation or admitted execution context reopens the relation.

For larger compositions, **adapt** the choice between operational simulation and denotational behavioral refinement examined in [*Denotation-based Compositional Compiler Verification*](https://arxiv.org/html/2404.17297v1). The latter uses algebraic composition of behavioral sets to reduce proof duplication, while retaining termination, divergence, failure and interaction distinctions that simpler final-state accounts can lose. Use it when those operations fit the language and simplify the actual preservation argument; a direct structural or state correspondence remains sufficient for the small constructions here. Neither proof representation automatically supplies a cheaper compiler. Changed control features, module interaction or proof-maintenance cost can reverse the selection.

### CMP.12:12 - Relations

- **MATH.5, MATH.17 and MATH.18:** supply extension through expression construction, operations on operations and interpretation/composition arguments.
- **CMP.1:** supplies effective conversion and answer recovery for computational reductions; interpretation here also retains the required execution behavior.
- **CMP.2, CMP.3 and CMP.10:** supply recursive construction, sharing and computational representation choices used by an evaluator or translator.
- **CMP.8:** qualifies deliberate approximation of represented values.
- **C.29.2 and C.29.3:** supply the surrounding computational formulation and physical realization questions.
- **C.11.DUA:** selects additional validation or proof by the conclusion it can change.

### CMP.12:End

## CMP.13 - Construct a Computational Abstraction for the Property Being Asked

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.13:1 - Problem frame

**Use this when** computing every relevant state or execution is unaffordable, but the question needs only some of their properties. You want to calculate with ranges, classes, relations or other summaries and determine what their answers establish about the original computation. Use it also when such a calculation reports an impossible path or loses a distinction needed for the answer.

The reader can describe the admitted inputs, elementary transitions and requested observation. Examples include asking which outcomes a rule system permits, whether a procedure can reach a failing state, or which dependencies can affect a returned value. The method constructs another computation over descriptions of possibilities, then relates its result to the question.

The first useful result is an effective abstract operation or small abstract execution with a justified conclusion about the original process. Extending that result across loops or interacting components requires the corresponding closure or composition argument. A finite reachability example can be done by hand; building an analyzer for a programming language requires its semantics and suitable algorithms for its representations.

Use direct computation when it already answers the question affordably. If the required change is a numerical error allowance, CMP.8 supplies that construction. If the problem is whether the original process describes the intended subject, return to that modeling question: a sound calculation about the process retains its subject assumptions.

### CMP.13:2 - Problem

How can a calculation discard detail yet retain a justified answer to the property being asked, and recover the distinctions that an inconclusive answer exposes?

A summary can combine possibilities that never occur together. A sequence of individually possible transitions can then appear to be an executable path. Conversely, retaining every distinction may make the supposedly cheaper calculation as difficult as the original. Loops add another difficulty: successive summaries can keep changing even when each update is easy.

### CMP.13:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Useful loss and needed distinctions | A small summary is useful only if it retains enough to answer the current question. |
| Possible and realizable | An overapproximation can exclude an outcome conclusively while leaving an included outcome unconfirmed. |
| Local operations and whole executions | Each transition must respect the interpretation, and loops require closure over repeated transitions. |
| Precision and completion | More detailed states and slower extrapolation may improve an answer while increasing the obtaining cost. |
| Separate summaries and correlation | Cheap independent properties may lose the relation that determines the result. |

### CMP.13:4 - Solution

**Local mantra:** choose the property; describe the represented possibilities; derive the abstract operations; compute a sufficient closure; interpret the answer; refine the distinction that blocks its use.

#### CMP.13:4.1 - Choose the observation and the direction of inference

Specify the original states, initial possibilities and transitions. Include the program location or phase when the same stored values permit different next steps there. Identify what the answer concerns: a reachable value, a path, termination, an interaction or another property. A set of reached states usually loses the order needed for a path question.

Choose what an abstract value represents. Write `gamma(a)` for the original possibilities represented by abstract value `a`. It can be a set of integer values, environments, graph states or complete traces. The concrete domain in this construction is the process being analyzed; it need not consist of physical objects.

For an overapproximation, every original possibility must remain among the represented ones. If the calculated possibilities exclude a bad outcome, that outcome is excluded from the original process. An included bad outcome may require reconstruction before it supports a counterexample. For an underapproximation, represented possibilities must be realizable: a retained witness can establish existence, while a missing witness leaves other executions unresolved. Choose the direction for the question and maintain it through the operations. The remaining steps develop the overapproximation branch.

#### CMP.13:4.2 - Derive computable operations on the summaries

For an original operation `f` and abstract input `a`, construct `f#(a)` so that it covers every allowed result of applying `f` to an input represented by `a`. If `post(X)` collects the one-step successors of states in `X`, the condition is:

`post(gamma(a)) ⊆ gamma(post#(a))`.

This is the soundness direction: the abstract step may add possibilities, but it must retain every original successor. Handle branch restrictions, failure and the actual arithmetic under the same interpretation. For example, an interval operation justified over unbounded integers needs revision for wraparound arithmetic.

Provide a way to combine incoming possibilities. An abstract join of `a` and `b` covers `gamma(a) ∪ gamma(b)`; it may include additional states. Implement the comparison used to recognize that a new result is already covered. Choose a representation whose operations and comparisons are affordable; an arbitrary logical formula may express the wanted property while making those operations difficult to compute.

A constructive starting point is to apply the original operation conceptually to the represented inputs, identify the property of all resulting outputs, and derive a formula for that property. The derived formula performs the abstract calculation without enumerating those inputs. Independent ranges, relations between variables and partitions by selected conditions provide different choices. Use the stronger choice where the receiving question needs the distinction it retains.

#### CMP.13:4.3 - Compute a result closed under the admitted transitions

For a finite graph of program points, associate an abstract state with each point. Initialize it from the admitted inputs. Recompute a successor when a predecessor summary changes and join its new contribution with the old one. CMP.3 supplies dependency scheduling and reuse. With finitely many points, monotone updates and an abstract order with no infinite increasing chain, a fair worklist reaches a stable result; the number and cost of updates still determine feasibility.

An infinite or very long increasing chain may need extrapolation. A **widening** combines successive approximations into a covering value and is chosen so the widening iteration stabilizes. For intervals, a bound that keeps moving outward can be replaced by an infinite bound. Apply such extrapolation where cyclic dependencies need it. Call context, retained relations and placement of widening can change precision, so a larger summary language alone does not guarantee a better computed answer.

Check the resulting closure. If `I` is the initial set and `a` the proposed result, the sufficient conditions are:

`I ⊆ gamma(a)` and `post(gamma(a)) ⊆ gamma(a)`.

Every reachable state is then represented: induction on execution length uses the first condition for the start and the second for each step. An implemented abstract transformer can establish the second condition by showing its result is covered by `a`. Such an `a` is often called a post-fixpoint. A prematurely interrupted growing approximation need not contain every reachable state.

If the closure is too broad, use restrictions from guards, a more discriminating representation, or a narrowing operation with its own soundness conditions. A proposed smaller set is useful only while retaining the initial possibilities and closure. Directly checking these two conditions is often enough for a small construction. An all-executions termination or response-time claim needs a corresponding argument; a closed set of reached states alone supplies neither.

#### CMP.13:4.4 - Recover the conclusion and examine a reported witness

Apply the requested observation to the closed result. If its represented states all satisfy the property, use that conclusion with its original input and transition assumptions. If the result overlaps an unwanted outcome, determine whether the overlap changes the next action. It may already be sufficient to retain the unresolved alternative.

When an actual path matters, reconstruct consecutive original states, starting from an admitted initial state. For abstract path `a0, a1, ..., ak`, propagate:

`X0 = I ∩ gamma(a0)`;

`X(i+1) = post(Xi) ∩ gamma(a(i+1))`.

If some `Xi` is empty, the abstract path is spurious: its steps cannot be joined into one original execution. If the last set is nonempty and these sets were computed without adding possibilities, retained predecessors can recover a concrete path. If this reconstruction is itself approximate, qualify its result with that approximation's direction; a nonempty overapproximation still leaves feasibility unresolved.

Loops and infinite-path properties require their own path and recurrence conditions. A finite prefix reaching a bad state settles finite reachability; repeating an abstract cycle does not by itself produce an infinite original execution.

#### CMP.13:4.5 - Refine the lost distinction and continue from the affected computation

Locate where the reported execution or answer became impossible. Restore the distinction responsible: separate a merged state, retain a relation, distinguish a calling context, or make an abstract operation more precise. A false path through one merged class can suggest splitting its reachable dead ends from the states that supply its outgoing edge.

Recompute affected dependencies and reuse results whose inputs and interpretation remain valid. Confirm that the revised construction removes the particular spurious result and still covers all original behavior. Removing one false path may leave others.

Choose further refinement by what it can change in the receiving work. A coarse result that already answers the question is sufficient. A real counterexample changes the original construction or its allowed use; improving the analyzer cannot make that execution disappear. When refinement remains too costly or inconclusive, return the unresolved property and the condition under which another calculation or direct execution would help. C.11.DUA governs the worth of that additional work.

### CMP.13:5 - Archetypal Grounding

#### CMP.13:5.1 - A graph summary invents a path

The original graph has vertices `a,b,c,d`, edges `a->b` and `c->d`, and initial vertex `a`. The question is whether `d` is reachable. Merge `b` and `c` into abstract vertex `q`, while keeping `a` and `d` separate. An abstract edge exists when any original edge connects the corresponding classes.

The abstract graph has `a->q` and `q->d`. Searching it returns the path `a,q,d`. Each edge has an original witness, yet the first edge arrives at `b` and the second leaves `c`.

Reconstruction gives `X0={a}`, `X1={b}` and `X2=empty`, since `b` has no successor. Split `q` into `{b}` and `{c}`. The recomputed reachable set is `{a,b}`, so `d` is unreachable. The useful result is both the answer and the reason the original summary could not establish it.

**Changed condition:** add edge `b->c`. The abstract path `a,q,q,d` now reconstructs to `a,b,c,d`; this is a real path. The shorter path `a,q,d` still has no consecutive realization, but its failure no longer excludes reachability. The transition change requires the affected search and reconstruction to be updated.

#### CMP.13:5.2 - Obtain a loop property without enumerating its iterations

Consider unbounded integers, positive integer `N`, and:

```text
x = 0
while x < N:
    x = x + 1
```

At the loop head, a set `X` of possible values is transformed by `F(X)={0} ∪ {x+1: x∈X and x<N}`. An interval hull supplies an abstract transformer. Starting at `[0,0]` produces `[0,1]`, `[0,2]` and so on until `[0,N]`; this takes a number of expansions proportional to `N` even though `N` can be written with logarithmically many bits.

Widen the increasing upper endpoint of `[0,0]` and `[0,1]` to obtain `[0,+infinity]`. It contains the initial value and is closed under the guarded update. It already establishes that `x` is never negative.

Suppose the receiving question instead asks for the value on exit. Apply the guard to `[0,+infinity]`: the integer inputs admitted by `x<N` are `[0,N-1]`; adding one and joining the initial value gives `[0,N]`. This smaller interval is itself closed under `F`, and contains 0. The exit condition `x>=N` then leaves `[N,N]`. Therefore every terminating execution exits with `x=N`.

For a termination conclusion, add a different argument: while the guard holds, the nonnegative integer `N-x` decreases by one, and the arithmetic is unbounded. This proves termination from 0 for the stated positive `N`. It explains why the exit value is obtained, rather than merely describing it if obtained.

**Changed condition:** replace the update by `x=x+2`, retaining `N=5`. The guarded interval calculation now gives `[0,6]`; exit intersection gives `[5,6]`. If that bound is sufficient, stop. If the final value is needed, retain the invariant that `x` is even as well. The exit result becomes `{6}`. The old answer 5 was tied to the former update.

#### CMP.13:5.3 - Independent ranges lose the determining relation

Let input `b` be either 0 or 1. Execute `x=b; y=b`, then test whether `x!=y`. Independent intervals give `x∈[0,1]` and `y∈[0,1]`. Their product contains `(0,1)`, so it cannot exclude the unequal branch.

Recover the construction: both assignments use the same `b`. Retain `x=y`, or keep the two input cases separate. Each choice excludes the unequal branch. The shared equality is the needed distinction; refining both independent endpoint ranges cannot recover it.

If the second assignment becomes `y=1-b`, both inputs take the unequal branch. A retained relation must be derived again from the changed operation. The earlier equality is an invalid assumption in the new computation.

### CMP.13:6 - Bias-Annotation

An alarming abstract result can draw attention away from whether its states form an executable case. Trace reconstruction tests that inference. A preference for simpler summaries can hide correlations; a preference for stronger analyses can spend resources recovering distinctions that the current answer does not need. Compare the actual result and cost under the requested observation.

### CMP.13:7 - Conformance Checklist

- The initial possibilities, transitions and requested observation identify the computation being analyzed.
- Each abstract value has an interpretation, and the inference direction supports the claimed conclusion.
- Abstract operations and joins cover their original counterparts; the obtaining algorithm has a justified completion or bounded-result condition.
- A whole-reachability conclusion uses initial containment and transition closure.
- A claimed concrete counterexample has a consecutive realization; a failed reconstruction identifies the lost distinction or remaining uncertainty.
- Refinement preserves the original possibilities and changes a result relevant to the receiving work.

### CMP.13:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Treat every abstract path as executable | Different steps can use incompatible representatives of one class. | Reconstruct the consecutive original states. |
| Return a growing partial result as all reachable states | Unprocessed transitions can add states. | Establish closure or report the limited exploration performed. |
| Strengthen independent ranges to recover a correlation | The relation is absent from the representation. | Retain a relational property or separate cases. |
| Widen at every combination | Extrapolation discards useful information where a finite join would suffice. | Locate the cyclic dependencies and choose a terminating update strategy there. |
| Keep an invariant after changing the transition | The invariant may exclude new executions. | Recalculate the affected operation and closure. |

### CMP.13:9 - Consequences

The reader obtains a computation over properties, together with the direction in which its answers apply. A false abstract counterexample becomes a constructive guide to a better representation. An already adequate coarse result can end the work.

The result depends on the original semantics and on the abstract operations, evaluation strategy and observation. A sound representation can still yield an answer too imprecise or expensive for use. Some properties remain undecidable or require a different form of reasoning.

### CMP.13:10 - Architectural Rationale

The construction combines two methods of thinking: choose a mathematical account of possible states, then build an effective algorithm on that account. MATH.2's quotient preserves specified operations independently of representative. Here a summary may deliberately combine different successors, so its justification is inclusion of possibilities rather than equality of returned classes. MATH.18 supplies the direction-sensitive comparison between accounts.

The examples expose three distinct causes of lost information: incompatible representatives in a path, extrapolation across iteration, and discarded correlation. Their repairs act on the abstraction and its algorithm. The physical or organizational interpretation of the original state system remains a separate subject correspondence.

### CMP.13:11 - SoTA-Echoing

How can a cheaper computation answer a selected question about executions? **Adopt** the calculational approach organized in Cousot's [*Principles of Abstract Interpretation*](https://mitpress.mit.edu/9780262044905/principles-of-abstract-interpretation/): choose the property semantics and derive effective abstract operations. Its scope includes dataflow, dependency and typing as well as numerical properties. This changes :4.1–4.3 from selecting a convenient picture to constructing a sound obtaining procedure. Direct finite exploration remains a serious cheaper alternative when its state space is manageable; a changed property or obtaining cost reopens the choice.

When independent summaries lose a needed relation, **adapt** the combination of algebraic and logical abstractions in [Cousot, Cousot and Mauborgne](https://www.di.ens.fr/~cousot/publications.www/CousotCousotMauborgne-JACM-59-6-32p-2012.pdf), especially their sound-transformer and reduced-product constructions. Combine complementary restrictions when that recovers the answer more cheaply than one uniformly rich domain. Solver-backed relations accept solver and representation costs; simple precomputed operations accept reduced expressiveness. The paper's implementation comparisons are historical, not a ranking of current tools. The choice changes :4.2 and :4.5 and is reopened by a relevant lost correlation or unsupported machine semantics.

For a reported abstract counterexample, **adopt** the reconstruct-and-refine step from [Clarke and colleagues](https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf), sections 4.3–4.4. Its finite-path construction motivates :4.4–4.5 and :5.1: split the distinction that prevents consecutive realization. Uniformly increasing precision is the rival; it can resolve more future questions but pays for distinctions this path may not need. Infinite-path properties require the additional loop conditions rather than reuse of the finite-path test alone.

How should cyclic abstract computations be scheduled? **Adapt** the question raised by [Yang and colleagues' 2025 interprocedural ordering method](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2025.34): distinguish actual recursive dependencies from spurious cycles introduced by merged call contexts, then choose where widening and narrowing operate. This strengthens :4.3's dependency-sensitive choice. A simple global worklist remains suitable when it produces an adequate result at lower construction cost. The reported advantages concern the paper's recursive-program analyses; they do not establish a universal schedule for every abstract domain. Lost call correlation or iteration cost can trigger reconsideration.

### CMP.13:12 - Relations

- **MATH.2 and MATH.18:** supply operation-preserving identification and interpretations between mathematical accounts; the overapproximation here has its stated one-way consequence.
- **CMP.3 and CMP.4:** supply dependency reuse and search; closure over cycles and reconstruction of abstract witnesses are developed here.
- **CMP.8:** supplies controlled numerical approximation; inclusion of possible executions answers a different question from numerical closeness.
- **CMP.12:** supplies effective interpretation of the original expressions and operations whose semantics this abstraction uses.
- **C.29.1 and C.29.2:** supply the surrounding interpretation and computational formulation; applying the result to its intended subject returns to C.29.
- **C.11.DUA:** selects further analysis by the receiving action or conclusion it could change.

### CMP.13:End

## CMP.14 - Compose Interacting Computations through Their Required Observations

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### CMP.14:1 - Problem frame

**Use this when** computations that work separately must run together, but shared state, communication or scheduling can change their results. You need to construct their interaction, repair a failing interleaving, or replace a component while retaining the behavior on which the rest relies.

The reader can describe each component's operations and the results expected from their combination. This method adds the shared state, communication and ordering rules needed to reason about the whole. It applies to concurrent algorithms and protocols, including computations performed by cooperating software agents. The implementation language and physical machine supply particular operations and failure conditions.

The first useful result is a composed procedure with a trace or invariant explaining how it obtains the required observation, or a counterexample that identifies the interaction to change. A small shared-state example needs only a few explicit steps. A general guarantee over an implementation needs the corresponding memory, scheduling and failure assumptions.

Use ordinary sequential composition or dependency scheduling when completed outputs suffice and no relevant interference remains. If the algorithms are already adequate and only their physical communication or timing is unresolved, take those requirements to the realization method. An organizational division of work needs its own account of actual roles, capabilities and authority; a computational model can help compare it once that correspondence is established.

### CMP.14:2 - Problem

How can separately useful computations be connected so that their possible interactions produce the required behavior, and what must change when one component's assumptions fail?

Two correct increments can lose an update. Retrying a request can repeat its effect. Individually finite operations can wait forever for one another. A replacement that returns the same final value can expose a different intermediate state to its neighbors. These failures concern the composition, so executing each component alone does not expose them.

### CMP.14:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Local reasoning and interference | A component's facts must survive the environment steps allowed between its own steps. |
| Independence and coordination cost | Isolation can simplify reasoning while synchronization, copying or serialization adds work. |
| Final result and observed history | Calls, replies and intermediate effects can distinguish executions with equal final values. |
| Excluding failure and ensuring progress | An execution can avoid every prohibited state yet never return a required answer. |
| Abstract operation and available primitive | A convenient atomic step requires an implementation or a justified coarser observation. |

### CMP.14:4 - Solution

**Local mantra:** choose the observations; expose the interactions; construct compatible steps; find the failing order or invariant; repair the protocol; establish progress under its actual assumptions.

#### CMP.14:4.1 - Specify what the combined computation must make observable

State the allowed inputs and required results. Include the observations a receiving component can make while work is in progress: returned values, shared-state reads, messages, failures or completed operations. Distinguish a request from each attempt to transmit or execute it when retries are possible.

Choose the required ordering. For a concurrent object, **linearizability** compares a history of calls and responses with legal sequential behavior. A finite history can contain pending calls. Append responses to any selected pending calls, then omit those still pending. Keep every originally completed operation, including its arguments and returned value. Seek a legal sequential order of the retained operations that respects every case where one operation returned before another was called. Each retained operation appears to take effect between its call and response in this extended history.

The appended responses belong to this comparison; they do not establish that the pending operations will actually return. Section :5.4 shows a pending call whose effect another operation has already observed. Other applications may accept weaker order, duplicate-tolerant combination or eventual agreement; use the property the receiving computation needs.

Also state required eventual events, such as a pending operation returning. An acceptable state or finite history does not alone settle that question. In concurrency theory, a **safety property** excludes a violation detectable in a finite execution prefix; a **liveness property** requires progress that no finite delay alone disproves. These meanings describe execution properties here.

#### CMP.14:4.2 - Expose steps, shared state and the environment

Give each component its local state and point of execution. Identify shared variables, owned data, channels and the operations that connect them. For each elementary action, specify when it is enabled, what it reads and changes, and which other values remain unchanged.

Choose the granularity supported by the computational model. A source statement that reads and then writes a value may allow another component's step in between. If a compare-and-swap or transaction is assumed atomic, its availability and scope are part of the construction.

Under an interleaving shared-memory model, form the combined state from the components and shared store, and let an enabled component take one step at a time. Message passing adds channel states and send/receive transitions; rendezvous requires the participating steps together. Include the admitted environment transitions, such as message loss, duplication, restart or input arrival, where the required claim depends on them.

A real language or memory model may permit observations absent from simple interleaving. Recover its ordering and visibility rules before transferring the argument. The method can then change the synchronization or the model instead of concealing the missing premise.

#### CMP.14:4.3 - Derive a compatible invariant or interaction rule

Construct the relation that must survive composition. For example, the shared counter must equal the number of committed increments, a request identifier must have at most one committed effect, or a waiting computation must request only a resource later in an acquisition order.

Establish that relation initially and inspect each allowed transition that can affect it. Local predicates must survive permitted environment steps. **Rely/guarantee reasoning** makes this explicit: a component assumes a stated interference relation from its environment and establishes a stated relation for its own steps. Its neighbors' possible steps must fit that assumption. Check the step-level conditions and their initial basis; mutually assuming that the other component eventually succeeds supplies no initial progress.

For a finite construction, explore enabled interleavings until a failure or the relevant closed state set is obtained. CMP.4 supplies search and CMP.13 supplies a qualified abstraction when the state space is too large. A counterexample should retain enough state and ordering to reproduce the offending interaction.

When operations commute under the observations of interest, exploit that property: some orders can be combined or avoided in exploration. Include intermediate observations in the comparison. Equality of the final store is insufficient if a neighboring read distinguishes the swapped operations.

#### CMP.14:4.4 - Change the interaction that causes the failure

Construct a repair from the failed premise. Common choices have different costs:

| Exposed difficulty | Constructive choice | Cost or condition to retain |
| --- | --- | --- |
| An intervening write invalidates a read | Use an atomic update, or validate the observed version and retry. | The primitive must cover the relevant state; retries have a progress cost. |
| Intermediate state is observed inconsistently | Serialize the affected operation, protect its critical region or publish an immutable result. | Waiting, ownership or retained copies replace the former interference. |
| A repeated message repeats an effect | Identify the logical request and combine effect application with remembering its result. | Identifier lifetime and failure recovery must preserve the relation. |
| Components wait in a resource cycle | Impose a shared acquisition order or another cycle-breaking protocol. | All participating acquisitions must follow the rule; starvation remains a separate question. |
| Coordination costs more than the required consistency is worth | Change the result specification to a weaker observation the receiver can use. | Revalidate the receiving algorithm under that weaker result. |

Execute the original failing trace against the repair, then inspect the transition family that caused it. This both explains the changed behavior and identifies what a more general argument must cover.

#### CMP.14:4.5 - Establish the progress actually promised

Identify what can enable and execute each required next step. A component may wait for another component, a message or a resource. A finite dependency with an available first move differs from a cycle in which every participant waits.

Choose only scheduling and delivery assumptions the intended use can support. **Weak fairness** excludes postponing an action forever once it remains continuously enabled. **Strong fairness** also excludes postponing an action forever when it becomes enabled infinitely often. Name the action or action family: fairness for an entire process does not make every branch of its code fair.

Use those assumptions with a progress measure or a dependency argument. Show why a required response eventually becomes possible and occurs. A bound on elapsed time additionally needs timing and resource bounds. A retry limit provides a finite failure return, not a guarantee that the requested effect happened or that it did not happen.

Test the relevant lost-progress case: an unavailable participant, an indefinitely lost reply, a stopped lock holder or an unfair scheduler. Return the supported result or the unresolved execution status. Do not preserve an eventual-response claim after removing its delivery or scheduling premise.

#### CMP.14:4.6 - Compare replacements through the composed observation

Relate the detailed execution to the promised higher-level operation. Some implementation steps may leave the chosen observation unchanged. That permits a coarser description, but hiding indefinitely many such steps can conceal lost progress; qualify the correspondence accordingly.

For replacement, ask whether the new component introduces an observation the allowed context could not obtain before. Include context interactions, failure and progress when they are part of the required behavior. A final-value comparison is sufficient only for a receiving use governed by that value.

Return the constructed coordination procedure, the result it supports and the assumptions the next user must retain. If a supplier changes its operation, memory rule, failure behavior or response promise, reopen the dependent composition. Use the common result-cost comparison and C.11.DUA when deciding whether another experiment, formal argument or alternative implementation would change the next move.

### CMP.14:5 - Archetypal Grounding

#### CMP.14:5.1 - Two increments need an operation that survives interference

Initially `x=0`. Two components each perform `r=x; x=r+1` once. Reads and writes are atomic, arithmetic uses unbounded integers, but the pair is not atomic. The required final result after both operations is 2.

One admitted execution is:

```text
A reads 0
B reads 0
A writes 1
B writes 1
```

The final value 1 violates the required result. Replace each increment by:

```text
repeat:
    v = read(x)
    if compare_and_swap(x, v, v+1) succeeds:
        return
```

Compare-and-swap tests the current value and, only if it equals `v`, changes it to `v+1` in one atomic action. A failed attempt leaves `x` unchanged.

The invariant is `x = number of successful compare-and-swap actions`. It holds initially; each success increases both sides by one, while reads and failed attempts change neither. Each component returns after its first success. Thus, when both return, `x=2`. A successful action supplies the point at which its increment takes effect in the sequential account.

If A and B both read 0, A can succeed first; B's stale attempt fails. B then reads 1 and succeeds with 2. For these two one-shot callers, each failed attempt is attributable to the other caller's success, so there can be at most one failed attempt before that caller completes. With both callers continuing to receive steps, both finish. A system with an unlimited stream of competing callers needs a different per-caller progress argument.

**Changed condition:** the environment supplies only a separate comparison and write. The old failing order is possible again. Use a primitive that really combines them or protect the read-modify-write region. Naming the pair “compare-and-swap” does not create that operation.

#### CMP.14:5.2 - A retry must refer to the same logical operation

A sender requests that a receiver add 5 to a stored counter. Initially the counter is 0. Messages may be lost or duplicated; the receiver continues running and retains its state. The receiver performs the addition, but the reply is lost. Blindly repeating the addition can leave 10 even though the sender requested one increment.

Give the logical request an identifier `k` that is not reused while an old request or reply with that identifier can still arrive. The sender retries the same pair `(k, add 5)`. At the receiver, process the following as one atomic state transition:

```text
if k is already in completed:
    result = completed[k]
else:
    counter = counter + 5
    result = counter
    completed[k] = result
send reply(k, result)
```

Only the state-changing conditional must be atomic; sending the reply can occur afterward. The first request changes the counter to 5 and stores `completed[k]=5`. Every duplicate returns 5 without another addition. The invariant relates a remembered identifier to its one committed effect. It depends on the same identifier denoting the same request payload.

At-most-once effect needs no promise that a message is eventually delivered. To promise a returned answer as well, suppose the sender keeps retrying, delivered requests are eventually processed, and each direction is a fair-loss channel: a message sent infinitely often is delivered infinitely often. The receiver answers each delivered request. These conditions ensure a reply eventually arrives. The result is a delivery-and-processing argument, not a deadline.

**Changed condition:** after applying the effect, the receiver can restart with the counter retained but `completed` lost. A later retry can again produce 10. Preserve the effect and its identifying result together across the admitted failure, for example through a durable atomic state update, or use an operation whose repetition is acceptable. An effect performed by another service needs that service's corresponding guarantee; persisting only the local identifier leaves the effect/record crash gap unresolved.

#### CMP.14:5.3 - An acquisition order removes a waiting cycle

Two computations need exclusive resources `L` and `R`. A obtains L and waits for R; B obtains R and waits for L. Both acquisitions were locally valid, but neither computation can proceed to release its first resource.

Choose one strict total order, `L<R`, and require both computations to acquire L before R. More generally, each computation acquires resources in strictly increasing order and releases them after its finite protected work. It waits only for these resource acquisitions.

A resource-wait cycle would require a strictly increasing sequence of resource positions to return to its starting position, which is impossible. The construction therefore excludes deadlock of this acquisition form. A waiting computation can still be postponed indefinitely by unfair grants. A starvation-freedom claim additionally needs a suitable grant policy and progress by holders; a bounded waiting time needs further bounds on their work and scheduling.

**Changed condition:** introduce a callback while holding R that tries to acquire L. This violates the shared order and can restore a cycle. Move the callback outside the protected region or redesign the acquisition protocol and its argument.

#### CMP.14:5.4 - Include an observed effect of a pending call

An initially empty FIFO queue has this history: A calls `enqueue(7)` at t=1; B calls `dequeue()` at t=2 and receives 7 at t=3; A has not returned by t=4. Comparing only completed operations would leave a dequeue from an empty queue.

For the comparison, append A's response at t=5. The sequential order `enqueue(7); dequeue() returns 7` is legal. For example, their effects can be placed at t=1.5 and t=2.5, within their call/response intervals. This is a witness for the finite history; it supplies no promise that A will eventually respond in the actual execution.

If there is no enqueue call at all, appending responses cannot invent one: a dequeue returning 7 from the empty queue remains invalid. If A instead returned at t=2 before B called at t=3, the sequential order must keep A before B. Pending-call completion thus preserves both the observed values and the order already imposed by completed calls.

### CMP.14:6 - Bias-Annotation

Sequential intuition can hide an interleaving between a read and its use. An atomic-looking API can hide a smaller implementation primitive. A successful retry demonstration can hide the uncertainty introduced by a lost reply or restart. Recover the actual transitions and observations before assigning the result of a simpler model to them.

### CMP.14:7 - Conformance Checklist

- The combined result includes the intermediate observations and eventual responses its user needs.
- The model states atomicity, visibility, communication and admitted environment changes where they affect the argument.
- Initial conditions and each relevant component or environment step support the shared invariant or protocol relation.
- A proposed repair changes the offending interaction and its general transition family.
- Progress uses named scheduling, delivery and failure assumptions; a finite timeout has its own qualified outcome.
- A replacement preserves the observations and progress required by its receiving context, with physical realization checked where that correspondence matters.

### CMP.14:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Compose isolated correctness results | Another component invalidates a locally established fact. | Test the permitted interference against that fact. |
| Treat a read-modify-write statement as indivisible | Interleaving can lose an update. | Construct or justify the required atomic operation. |
| Infer failure of the effect from a missing reply | The effect may have happened before the reply was lost. | Identify the logical request and recover its result. |
| Infer eventual response from absence of a bad state | All participants may keep waiting. | Establish an enabled progression and its fairness conditions. |
| Assume each component progresses because the other does | The circular assumptions may admit no first move. | Derive progress from initial enabling and justified dependencies. |
| Hide a changed memory or crash model in an implementation detail | The former permitted executions no longer cover the implementation. | Reconstruct the affected interaction and preservation argument. |

### CMP.14:9 - Consequences

The reader can construct an interaction protocol, locate a failed order, and explain which whole-computation property follows. An invariant, counterexample or progress argument supports division of algorithmic work while exposing the assumptions shared across components.

Coordination can add waiting, retries, retained state or stronger primitives. Sometimes changing the required observation admits a cheaper useful composition. The improvement is conditional on the receiving computation accepting that changed result.

### CMP.14:10 - Architectural Rationale

Mathematical composition supplies an operation for combining descriptions. Computational composition must also establish how the resulting process runs and what other processes can observe. Interference makes a component's admissible context part of its meaning.

The counter, retry and resource-order cases construct three different repairs: conditional atomic change, identity across repeated communication, and removal of cyclic acquisition. Their shared method is to expose the missing interaction, construct the coordinating steps and retain separate arguments for allowed histories and progress. Modeling a working Method with these operations can sharpen a methodological comparison, but the modeled operations still need a justified correspondence to the actual work.

### CMP.14:11 - SoTA-Echoing

How should local computations be combined without losing the required whole behavior? **Adopt** the separation of state/action description, refinement, progress and environment-dependent composition in Lamport's [*A Science of Concurrent Programs*](https://lamport.azurewebsites.net/tla/science-book.html), chapters 3, 4, 6 and section 8.2. It supports :4.2–4.6. Its composition discussion exposes the circularity of proving each component's eventual success by assuming the other's. A direct global invariant remains a serious simpler choice for small interacting systems; a component proof becomes useful when its explicit environment assumptions reduce repeated reasoning. The accepted cost is recovering those assumptions. Changes in observed behavior or progress premises reopen the choice.

When an abstract atomic object must replace a concurrent implementation, **adapt** the composition-sensitive account in [Oliveira Vale, Shao and Chen](https://flint.cs.yale.edu/flint/publications/ctlinear-jacm.html). It relates linearizability, locality and observational refinement through explicit composition operations. This sharpens :4.1 and :4.6: ask which context can observe the replacement, rather than checking final values alone. A short history/linearization-point argument is sufficient for :5.1; the richer algebra is useful when it reduces actual composition-proof work. It does not automatically preserve progress or supply an implementation. A new interaction context can reverse the choice.

Which interference may a component assume? **Adopt** the memory-model parameterization demonstrated by [Lahav and colleagues' rely/guarantee treatment of causally consistent shared memory](https://arxiv.org/abs/2305.08486) as a boundary on :4.2–4.3. Sequential interleaving is a convenient comparator, while weaker visibility needs a compatible semantics and reasoning rules. Retaining the simpler model is justified when the implementation supplies its conditions. Otherwise synchronization, the algorithm or the claimed observation must change; relabeling the old proof leaves the gap.

When restart is admitted, **adapt** the explicit crash-aware observation in [*Linearizability with Crashes*](https://flint.cs.yale.edu/flint/publications/crashlin.html) for :4.2 and :5.2. A no-crash history can omit the retained-state distinction that recovery needs. A durable coordination protocol accepts persistence and recovery costs; accepting an uncertain result or an idempotent effect may be a cheaper suitable rival. The framework distinguishes forms of crash-aware correctness, rather than making every retry protocol equivalent. Change the failure model or the effect's location and reconsider the corresponding claim.

### CMP.14:12 - Relations

- **MATH.17 and MATH.18:** supply composition of operations and interpretation between accounts; this method constructs their interacting computational execution.
- **CMP.3 and CMP.10:** supply dependency scheduling and data representations; interference can change the operations those representations must support.
- **CMP.4 and CMP.13:** supply exploration and qualified abstraction for the composed state or trace system.
- **CMP.12:** supplies interpretation and behavior-preserving translation when the component's executable description changes.
- **C.29.2 and C.29.3:** supply computational formulation and realization, including whether the modeled primitives and resource conditions are available.
- **C.11.DUA:** governs the worth of stronger analysis or testing for the proposed use.

### CMP.14:End
