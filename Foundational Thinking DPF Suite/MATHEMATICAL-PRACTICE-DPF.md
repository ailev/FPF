# Mathematical Thinking DPF

> A pattern language for constructing mathematical objects, operations and arguments, using their results, and developing the next useful question.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 20 September 2026
- **Status:** Eternal alpha: a growing repertoire of methods for mathematical work.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF ecosystem repository](https://github.com/ailev/FPF)

Begin with the working question. If you have not yet identified its mathematical contribution, use Readme entry MP-FRAME. Use the Table of Contents to find a relevant pattern, then open its Problem frame, Solution, worked cases and checklist. Readme follows connected mathematical work; Preface explains the methods and when to revise a construction.

The reference code **MATH** names this DPF. Its numbers are stable pattern addresses; § shows position in this edition. References such as B.5.RA and C.29.1 name patterns in [FPF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). Use those patterns when the cited question arises.

When a mathematical result changes a working method, [Method Engineering DPF](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) provides two further methods: ME.7 helps resolve a proposed composition of methods; ME.12 helps locate an inconsistency between a method, its descriptions, the work performed and its supporting means.

Open the cited publications for those pattern bodies. When using another edition, revisit your conclusion if a cited operation or condition has changed.

To cite this edition: Anatoly Levenchuk, *Mathematical Thinking DPF*, [FPF ecosystem repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Mathematical Thinking - Readme](#mathematical-thinking---readme) | Follow connected mathematical work. |
| Preface | [Mathematical Thinking - Preface](#mathematical-thinking---preface) | Understand the connected methods, their rationale, sources and limits. |

## Part A - Choose and relate constructions

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MATH.16 - Choose a Mathematical Construction from Its Required Maps (Universal Property)](#math16---choose-a-mathematical-construction-from-its-required-maps-universal-property) | Usable, evolving | universal property; product; coproduct; pullback; function object; currying. What maps should a new object support, and how can that requirement select a construction? | MATH.2 for quotients; MATH.5 for generator extensions; MATH.7 for reversible representations; C.29 for interpretation in another subject. |
| 2 | [MATH.17 - Construct Mathematical Spaces of Operations and Operations on Them](#math17---construct-mathematical-spaces-of-operations-and-operations-on-them) | Usable, evolving | operations as objects; admissible functions; closure; higher-order operation; transformation law. How can a rule be constructed, combined or changed while retaining the consequence its use needs? | MATH.16 for function objects; MATH.1/.2 for retained steps or identification; MATH.18 for interpretation between accounts; C.29 for a working-method application. |
| 3 | [MATH.1 - Build a Mathematical Structure of Composable Paths](#math1---build-a-mathematical-structure-of-composable-paths) | Usable, evolving | generators; paths; endpoints; identity; associativity. Which elementary steps can be composed? When do different sequences need to remain distinct? | MATH.2 when paths will be identified; C.29 when the construction represents another subject. |
| 4 | [MATH.2 - Treat Objects as the Same While Preserving Operations (Quotient)](#math2---treat-objects-as-the-same-while-preserving-operations-quotient) | Usable, evolving | quotient; congruence; equivalence; partial operation; refinement. Can these objects be treated as the same without losing a later operation or result? | MATH.1 when paths first need construction; MATH.6 for a counterexample to the proposed identification. |
| 5 | [MATH.5 - Extend a Generator Assignment While Preserving Operations (Homomorphism)](#math5---extend-a-generator-assignment-while-preserving-operations-homomorphism) | Usable, evolving | generators; relations; homomorphism; free structure; extension. How can a choice on generators determine an operation-preserving map on everything they generate? | MATH.1 for paths; MATH.2 when an extension must descend to a quotient. |
| 6 | [MATH.7 - Transport a Mathematical Structure Through a Bijection](#math7---transport-a-mathematical-structure-through-a-bijection) | Usable, evolving | bijection; transport; inverse map; isomorphism; domain of operation. How can a useful operation, law and answer be carried through a change of representation? | MATH.2 when identification is proposed instead of a bijection; C.29 for interpretation in another subject. |
| 7 | [MATH.18 - Compare Mathematical Accounts through Interpretations](#math18---compare-mathematical-accounts-through-interpretations) | Usable, evolving | interpretation; primitive operation; preservation; reflection; round trip; equivalence. Which constructions, equations and maps transfer between two mathematical descriptions, and what can be recovered? | MATH.5 for generated interpretations; MATH.7 for bijective transport; MATH.2 for quotients; MATH.17 for transformations of operations. |

## Part B - Construct and criticize arguments

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MATH.19 - Construct a Proof through Intermediate Claims](#math19---construct-a-proof-through-intermediate-claims) | Stable | lemma; backward and forward reasoning; generalization; proof dependency. Which intermediate claim connects the available premises to the desired conclusion? | B.5.RA for recovery of a supplied argument; MATH.4 for induction; MATH.6 for a separating case; MATH.12 for obtaining an object from the proof. |
| 2 | [MATH.4 - Construct a Witness by Induction](#math4---construct-a-witness-by-induction) | Usable, evolving | induction; recursive witness; base and step; representation. How can a proof supply an object for every finite input? Does the construction respect equivalent representations? | MATH.2 when a recursive construction must respect identification; MATH.12 for extracting constructions from other proof rules. |
| 3 | [MATH.12 - Extract a Construction from a Proof](#math12---extract-a-construction-from-a-proof) | Usable, evolving | constructive proof; witness; function; pair; branch; finite search; computation. Which data-producing operation does a proof supply, and what is needed to execute it? | B.5.RA for an unfamiliar argument; MATH.4 for induction; C.29.2/.3 for formulation or execution questions. |
| 4 | [MATH.6 - Refute a Mathematical Claim with a Countermodel](#math6---refute-a-mathematical-claim-with-a-countermodel) | Usable, evolving | counterexample; countermodel; quantifiers; finite scope; encoding. What concrete structure refutes the claim? What does an unsuccessful bounded search leave unresolved? | B.5.RA if the claim's argument needs recovery; MATH.2 when the counterexample defeats an identification. |
| 5 | [MATH.20 - Bound a Mathematical Unknown by Comparable Constructions](#math20---bound-a-mathematical-unknown-by-comparable-constructions) | Stable | bound; inequality; enclosure; relaxation; attainability; residual and error. Which comparison can answer the question before the whole unknown is obtained? | MATH.19 for an intermediate inequality; MATH.6 for a failed bound; MATH.21 for convergent approximation; FPF for choosing further work. |

## Part C - Change a construction and develop its theory

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MATH.11 - Construct an Invariant from Transformation Rules](#math11---construct-an-invariant-from-transformation-rules) | Usable, evolving | invariant; transformation rule; preservation equation; coefficient; reachability. How can a preserved expression be constructed and used to obtain a formula or exclude a target? | MATH.2 for identification; MATH.7 for transport; C.29 for a consequence about the modeled subject. |
| 2 | [MATH.13 - Derive a Consequence from a Symmetry](#math13---derive-a-consequence-from-a-symmetry) | Usable, evolving | symmetry; uniqueness; fixed point; orbit; conservation; numerical update. What does a transformation preserve, and which conclusion actually follows from that symmetry? | MATH.8 for the full orbit construction; MATH.9 for compatible choice; MATH.10 for admissible variation. |
| 3 | [MATH.8 - Generate a Solution Family by Symmetry](#math8---generate-a-solution-family-by-symmetry) | Usable, evolving | group action; solution orbit; stabilizer; repetitions; representatives. Which solutions can be generated from one solution, and how much of the solution set does this cover? | MATH.13 for an unresolved symmetry consequence; MATH.9 when one compatible representative is required. |
| 4 | [MATH.9 - Determine Whether and How a Choice Rule Can Respect Symmetry](#math9---determine-whether-and-how-a-choice-rule-can-respect-symmetry) | Usable, evolving | equivariant choice; stabilizer; symmetry obstruction; additional data. Can one allowed answer be chosen consistently with symmetry? What can replace an impossible choice? | MATH.8 for solution orbits; MATH.13 for an earlier consequence or uniqueness question. |
| 5 | [MATH.10 - Improve a Mathematical Candidate or Derive a Necessary Condition by Admissible Variation](#math10---improve-a-mathematical-candidate-or-derive-a-necessary-condition-by-admissible-variation) | Usable, evolving | admissible variation; improving change; stationary point; boundary minimum; constraint; first variation. Which change is allowed, can it improve the candidate, and what condition follows? Does that condition establish an optimum? | B.5.RA if the variational argument needs recovery; C.29 when a mathematical variation represents a subject change. |
| 6 | [MATH.21 - Construct an Object through Convergent Approximations](#math21---construct-an-object-through-convergent-approximations) | Stable | limit; completeness; compatible approximation; uniform convergence; error control. How can finite approximations construct an object while retaining the next operation? | MATH.20 for bounds; MATH.19 for convergence and interchange arguments; MATH.2 for classes of representations; computational methods for effective obtaining. |
| 7 | [MATH.22 - Change Axioms and Trace Their Consequences](#math22---change-axioms-and-trace-their-consequences) | Stable | axiom change; theory; interpretation; model; independence; proof repair. Which constructions and consequences survive when assumptions change? | MATH.18 for interpretations; MATH.19 for replacement proofs; MATH.6 for countermodels; MATH.23 for a further conjecture. |
| 8 | [MATH.23 - Develop a Conjecture by Changing a Construction](#math23---develop-a-conjecture-by-changing-a-construction) | Stable | conjecture; construction variation; proof and refutation; generalization; next problem. How can a change or obstruction yield a precise useful claim and an attainable next operation? | MATH.19 for proof construction; MATH.6 for refutation; MATH.22 for theory change; B.5.QD/C.40.CD for continued inquiry. |

# Mathematical Thinking - Readme

## Practical entries

A mathematical result often becomes an input to further work: a construction supplies the objects for a proof, a failed implication changes the question, and a changed rule requires an argument that its useful properties survive. The patterns in this language help make and connect those contributions.

The two worked connections below start at different places. The first turns a working difficulty into a mathematical question and returns the answer to its subject. The second changes a rule so that independently obtained results can be combined, proves the new rule and revisits it when the requested answer changes. Enter with the results already available; a settled contribution need not be reconstructed.

These examples do not enumerate the language. Use the Table of Contents to find other questions and the actual pattern titles. Each body states its prerequisites, method, examples and limits. A construction can serve mathematics itself or describe another subject; FPF C.29 helps establish what its result says about that subject.

You can ask an assisting agent: “Explain this and comment on my proposal without FPF jargon; use the language of my work.”

### MP-FRAME - Find the mathematical contribution in an unfamiliar problem

- **Situation:** Something in the work is unexplained or fails, and you do not yet know whether another observation, a new model, a mathematical construction or a different computation is needed.
- **Question:** What must become distinguishable or possible for the next answer to be useful?
- **First useful result or blocker:** A mathematical task with a stated use. For example, a cart's travel log gives total distance, but that total cannot tell whether the cart returned to its start. Identify the position question first. With straight-line motion and known displacements, a sequence of signed displacements supplies an account that can answer it. MATH.1 constructs the sequences and their composition; MATH.5 derives the accumulated displacement from the elementary displacements. A sensor report must first be interpreted as the movement it measures.
- **Start with:** FPF B.5.FM. State the working question, identify the participants and relations that may change its answer, and build a small account that yields a consequence. If an unfamiliar theory supplies the account, B.5.TU helps construct its application. B.5.MPC connects the physical, mathematical and computational contributions when the difficulty lies between them. Their bodies are in the FPF publication linked above. If the problem is deciding what an object must let you form or recover, use MATH.16. If it is deciding which distinctions can be forgotten, use MATH.2. If an implication is doubtful, use MATH.6. The question determines the construction; an available formula may settle only part of it. C.29 supplies the interpretation through which a mathematical result answers the original question. C.29.2/.3 develop a needed procedure and its execution.
- **Stop or return:** After the question changes, test whether the summary still determines the answer. If two runs have the same final position but differ in a requested visit, recover the information that separates them. MATH.2 helps locate the failed identification; B.5.QD develops the next useful question. For a working method changed by the result, ME.7 helps describe the proposed operations and their relations; ME.12 checks the claims in that account and its description. The Preface's worked use follows these choices in detail.

### MP-COMBINE-RESULTS - Change a rule so that separately obtained results can be combined

- **Situation:** A rule works for one input, but splitting the work or combining its results changes the answer.
- **Question:** What must each contribution retain, how should contributions combine, and why will the result still answer the original question?
- **First useful result or blocker:** A composable summary with a stated use. For an arithmetic mean of finitely many real values, return each group's sum and count; add these pairs and divide the total sum by the total count.
- **Start with:** [MATH.23](#math23---develop-a-conjecture-by-changing-a-construction) to develop the question; [MATH.2](#math2---treat-objects-as-the-same-while-preserving-operations-quotient) to choose compatible identification; [MATH.17](#math17---construct-mathematical-spaces-of-operations-and-operations-on-them) to work on the combining operation; [MATH.19](#math19---construct-a-proof-through-intermediate-claims) for the argument.
- **Stop or return:** Use the proved rule within its assumptions. A new statistic, allowed transformation or arithmetic implementation can invalidate a retained-information or proof step; return to that step.

#### Worked connection for MP-COMBINE-RESULTS


**1. Recover the failure and intended result.** Averaging the means of [0] and [2,4] gives 1.5, while the mean of the combined list is 2. MATH.23 turns this difference into a question: which summary recovers the mean of every nonempty combined finite list, for every partition into nonempty groups? The result is a claim and its range of cases for the identification step.

**2. Decide what may be forgotten.** MATH.2 tests identification against the operations still needed. Equal means are insufficient: [0] and [0,0] both have mean 0, but adjoining [2] gives means 1 and 2/3. Instead identify lists with equal sum and count. Concatenation respects that identification because both components add. Empty lists can have summary (0,0); division is defined only after the combined count is positive.

**3. Make the rule itself available for work.** Combine (s,n) and (t,m) as (s+t,n+m). MATH.17 asks whether the operation stays within the chosen space and which laws the use needs. The pair summarizes an input; the binary operation is another mathematical object, which can be compared with a replacement. Associativity permits regrouping; commutativity permits reordering. These laws become premises needed by the proof.

**4. Connect the local calculation to all allowed combinations.** MATH.19 separates two claims: summarizing a concatenation equals combining its summaries, and extracting s/n at positive n returns the list's arithmetic mean. The first follows from addition of sums and lengths. Repeated combination follows by induction over the finite grouping, using [MATH.4](#math4---construct-a-witness-by-induction) if that induction needs construction. The argument thus covers every stated partition.

**5. Use the result with its conditions.** Contributors can now return pairs to combine. FPF C.29 connects the mathematics to actual records: which values belong to the population and whether any are duplicated remain subject questions. Real addition supplies the laws above; floating-point regrouping needs its numerical account when rounding can change the use.

**6. Develop the next question.** If the answer becomes a median, sum and count no longer suffice: [0,0,6] and [0,3,3] share both but have medians 0 and 3. Return to step 2 and use MATH.23 to construct the new question. A quantile method or a different summary can supply the next contribution.

# Mathematical Thinking - Preface

## MATH.Preface:1 - Problem frame - Construct mathematics for the question

You may know a formula, a programming technique or a useful physical law and still be unable to formulate the next problem. The objects may have been chosen too coarsely. Two operations may work separately but fail when combined. A plausible statement may need a proof, or a proof may leave you without a way to obtain its promised object.

Mathematical Thinking helps construct and develop the mathematics needed in such situations. Its starting repertoire forms objects and operations, tests identifications, builds arguments and witnesses, changes representations, and obtains consequences from transformations and constraints. Work can begin in mathematics itself, a physical investigation or the design of another working method.

This edition contains twenty patterns. Mathematical Thinking belongs to the Foundational Thinking DPF Suite alongside Mathematical Modeling, Physical Thinking, Computational Thinking and Notational Engineering. Together they connect these inquiries with the development of methods of work. Use the present Table of Contents to find an available method; a planned contribution still requires another source or collaborator. Pattern IDs remain stable across editions, including gaps left by withdrawn bodies; Parts group the available methods by the work they support.

Begin with the question that is blocked. If its mathematical form is still unclear, the Readme MP-FRAME entry uses FPF B.5.FM, B.5.TU and B.5.MPC to obtain the first account and locate the missing contribution. Once a mathematical operation is needed, a body here develops that operation. The worked use in :4 begins before a representation has been selected. Use the Table of Contents for other questions; each pattern states its prerequisites and conditions.

The common starting preparation is elementary sets, relations, functions and the ability to follow a short proof. Several examples need only integer arithmetic. Variation of a curve additionally uses differentiation and integration; the relevant pattern states those requirements. A collaborator can provide a mathematical contribution that you cannot yet construct yourself. Retain the inputs, conditions and result of that contribution so that the next part of the work can use it.

## MATH.Preface:2 - Problem and forces - Make a usable construction

A mathematical description earns its place by making an operation, argument or question possible. Choosing names for objects is often the beginning of that work. The harder part is deciding how the objects can be formed, transformed, compared and used in a subsequent construction.

Several tensions recur:

| Working tension | What must be decided |
| --- | --- |
| Retaining detail and obtaining a manageable calculation | Which distinctions does the next operation need, and which can be forgotten? |
| A general statement and an obtainable answer | Is existence enough, or must the work return a witness, path, function or procedure? |
| A simple representation and preserved meaning | Which operations and conditions must travel with the representation? |
| A local calculation and a general consequence | What carries the result from the worked input to the claimed family? |
| Reusable machinery and the cost of constructing it | Will a general structure help further work, or will a direct calculation settle the question? |
| A solved problem and development of the repertoire | Which failure, remaining limit or new construction makes a worthwhile next question possible? |

The same question can have several satisfactory mathematical descriptions. A list of movement steps can show each change; a displacement summary can answer a final-position question with less information. A later question about visiting an intermediate position can require a distinction that the summary discarded. Choose a representation from the answer needed, its further use and the effort available.

## MATH.Preface:3 - Solution - Connect constructions through what they supply

### MATH.Preface:3.1 - Form objects, operations and representations

[MATH.16](#math16---choose-a-mathematical-construction-from-its-required-maps-universal-property) starts one step earlier, when several constructions seem plausible. Describe the maps the new object must support, then compare arbitrary allowed ways of supplying or processing its data. The resulting universal property distinguishes, for example, carrying both components from accepting either input, and arbitrary pairs from compatible pairs. It can also specify an object that represents a prepared function. A known construction can then supply the object and its maps.

[MATH.1](#math1---build-a-mathematical-structure-of-composable-paths) starts with permitted elementary connections and constructs finite paths, identities and composition. Retaining a path can preserve the order and history that its final effect forgets. [MATH.5](#math5---extend-a-generator-assignment-while-preserving-operations-homomorphism) starts with assigned values for generators and obtains values for their composites while preserving the operations.

When several descriptions should count as the same input, [MATH.2](#math2---treat-objects-as-the-same-while-preserving-operations-quotient) tests whether the required operation is independent of the representative. For a partially available operation, its availability can matter as much as its output. A failed test supplies a distinction to restore.

[MATH.7](#math7---transport-a-mathematical-structure-through-a-bijection) addresses a reversible change of representation. It constructs the operations in the new representation and carries results back. Renaming the elements while keeping an unsuitable operation can change the problem; the transported operation supplies the repair.

[MATH.17](#math17---construct-mathematical-spaces-of-operations-and-operations-on-them) makes the rules themselves available for construction and change. Select allowable operations, determine whether their composition stays allowable, then construct an operation that transforms them. Its required law follows the intended use: repeating a composite and repeating its stages separately can yield different answers.

[MATH.18](#math18---compare-mathematical-accounts-through-interpretations) compares descriptions with different primitives, allowed maps or equality. Construct the needed interpretations, establish what transfers, and inspect the return. A partial interpretation can be enough for one consequence; equivalence requires the corresponding comparisons in both directions.

These methods can be used separately. They also connect: form expressions from generators, interpret their operations, identify descriptions that preserve the desired answer, then choose a convenient representation for calculation. When the rule or the whole account changes, use MATH.17 or MATH.18 to construct and examine that change.

### MATH.Preface:3.2 - Obtain an argument and the object it supports

[MATH.19](#math19---construct-a-proof-through-intermediate-claims) constructs an argument when the premises and conclusion are known but the connecting steps are missing. Work backward to a sufficient claim and forward to available consequences, then prove a lemma joining them. An unsuccessful induction can require an extra parameter or a stronger intermediate statement. B.5.RA instead helps recover an argument already supplied in another description.


[MATH.4](#math4---construct-a-witness-by-induction) obtains a witness by following the construction of a finite input. A step may require a stronger intermediate result or another parameter. [MATH.12](#math12---extract-a-construction-from-a-proof) recovers functions, pairs, projections and branch information from proof steps, including non-inductive steps. It distinguishes the operations that produce data from a proof that some suitable data exists.

[MATH.6](#math6---refute-a-mathematical-claim-with-a-countermodel) constructs a case in which the assumptions hold and the proposed conclusion fails. Such a case can reveal a missing premise, a misplaced quantifier or an overly narrow search. [MATH.11](#math11---construct-an-invariant-from-transformation-rules) instead solves for a function preserved by the allowed transformations. Its value can exclude a target or determine an accumulated quantity. Equal values leave any required reachability construction to be supplied.

[MATH.20](#math20---bound-a-mathematical-unknown-by-comparable-constructions) obtains a useful comparison before the whole unknown is available. A feasible path bounds a shortest length from above; inequalities covering all paths can bound it from below. The method constructs the comparison, propagates its direction through the needed operations and tightens the part that leaves a consequential gap. It can return enough for the next decision without completing an optimization.

An argument and an obtaining procedure can support each other. Given a finite list, a terminating test and a proof that some listed element passes, testing the entries obtains a witness. If the searched range becomes infinite, the finite-search argument must be reconsidered. The available result may remain a logical conclusion or a procedure for each finite portion.

### MATH.Preface:3.3 - Change a construction and develop its theory

[MATH.13](#math13---derive-a-consequence-from-a-symmetry) establishes how a transformation of the data relates to transformations of admissible candidates and answers. That relation can transfer a solution, constrain a unique answer or expose an impossible choice requirement. [MATH.8](#math8---generate-a-solution-family-by-symmetry) constructs the resulting orbit, removes repetitions and separates one orbit from all solutions. [MATH.9](#math9---determine-whether-and-how-a-choice-rule-can-respect-symmetry) constructs a choice compatible with the transformations when the input's own symmetries permit one.

When candidates satisfy constraints, [MATH.10](#math10---improve-a-mathematical-candidate-or-derive-a-necessary-condition-by-admissible-variation) constructs changes that stay within them and calculates what those changes do to a criterion. The result may be an improving candidate or a necessary condition. A minimum requires the corresponding additional argument. In a physical-action calculation the requested condition can be stationarity.

Symmetry and variation can simplify the same problem while answering different questions. One establishes a relation among transformed problems and solutions; the other investigates admissible changes and their effect on a criterion. Preserve the conclusion supplied by each.

[MATH.21](#math21---construct-an-object-through-convergent-approximations) constructs an object through converging or compatible approximations. The intended use selects what convergence must preserve: a finite prefix, function values, an integral or another observation. MATH.20 can provide the necessary error bound; MATH.19 can supply a missing limit or interchange argument. A limit's existence and an effective way to obtain the requested finite information require their respective constructions.

[MATH.22](#math22---change-axioms-and-trace-their-consequences) changes the permitted objects or reasoning by changing assumptions. Follow the affected proof steps and constructions, retaining a conclusion when its justification survives or can be repaired. MATH.18 supplies interpretations between accounts; MATH.6 can separate a claimed consequence from what the new assumptions allow.

[MATH.23](#math23---develop-a-conjecture-by-changing-a-construction) turns a variation, obstruction or unexplained regularity into a next mathematical claim and a proving or refuting operation. If equal weighting of group means fails for unequal groups, restricting all groups to equal size abandons the original need. Retaining sums and counts repairs the construction and opens a general question about combinable summaries. Proof construction, countermodels and changed axioms then provide different continuations.

### MATH.Preface:3.4 - Return a construction to further work

The connecting rule is simple: name what one construction returns and what the next one uses. A set of solutions, one chosen solution, a proof of existence and an executable selection support different continuations. Enter at a contribution already available and stop when the requested mathematical result has been supplied.

For a question about another subject, use FPF C.29 to establish the correspondence through which the mathematical result answers that question. C.29.2 develops a missing computational formulation; C.29.3 connects a computation with the arrangement that prepares its inputs, performs it and exposes an interpretable result. B.5.MPC coordinates mathematical, physical and computational reasoning when their contributions must be developed together.

### MATH.Preface:3.5 - Use this contribution within the wider repertoire

The [Foundational Thinking Suite Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains where this mathematical contribution connects with model formulation, physical premises, computation, notation and Method Engineering. A result such as a function object or an interpreted path becomes useful through what the next operation can do with it. Its mathematical laws alone leave the subject interpretation and execution conditions to their respective methods.

The twenty bodies connect formation and interpretation with proof, comparison and continued theory development. MATH.17 makes operations available for change, MATH.18 compares interpretations, MATH.19 builds a missing proof, and MATH.20/.21 connect justified bounds with approximation. MATH.22/.23 develop changed theories and useful conjectures. Start with the contribution needed next and read the methods that supply its missing inputs.

For example, changing the order of a read and an update can preserve the final stored value but change the reading used by a later decision. MATH.1/.5 supply sequences and their interpretation, and MATH.2 tests the proposed identification. Method Engineering uses that distinction when deciding how work may be rearranged. The mathematical construction and its use in the working method remain separately inspectable.


### MATH.Preface:3.6 - Constituent actions in ongoing work

A symbolic rewrite can be part of proving a lemma while that lemma's proof is part of proving a larger claim. The required domain constrains the rewrite at that same moment: cancelling a factor is permissible only under the relevant algebraic conditions, and excluding zero would change a claim that is meant to include it. Knowing the symbols and the theorem goal can leave the intermediate reasoning unavailable. Recover or obtain that reasoning rather than treat the smaller calculation as proof of the whole.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Use the parts of the vertical that can change the present result. A Method described here can require additional capability, available support and compatible resources at other grains.

## MATH.Preface:4 - Worked use - Choose a representation after the question changes

A team receives travel logs from a cart moving along a straight line. Two runs have the same recorded distance, yet one ends at the starting point and the other does not. The immediate question is which runs returned to their start. Starting with a familiar distance formula leaves the missing information unresolved.

**Recover the subject account.** B.5.FM asks what can change the answer. Total distance has forgotten direction. Establish where the line's origin and positive direction are, and what a recorded movement denotes. For this small case, each observed movement is a monotone step of one unit, either forward or backward; the cart starts at zero. This is the supplied physical account. If the log only records a commanded movement, the actual displacement remains a question for observation or a supported movement model. B.5.MPC keeps that physical contribution distinct from the subsequent calculation.

**Construct and interpret the mathematics.** Use MATH.1 to form finite sequences of forward and backward steps. MATH.5 constructs their displacement map by assigning +1 to a forward step, -1 to a backward step, and addition to concatenation. The empty sequence has displacement zero. Forward-then-backward and forward-then-forward both have total distance two, but their displacements are zero and two. Thus the first run returns to its starting point and the second does not, under the stated account.

The method needed an operation on sequences, not just names for two kinds of movement. MATH.5's extension explains why adding the elementary displacements evaluates any finite sequence and respects concatenation. C.29 connects the resulting number back to the cart's position. If a program performs the calculation, C.29.2/.3 connect that rule to its input interpretation and implementation. For example, adding absolute distances would compute a different quantity from the one now requested.

**Decide what can be forgotten.** For the return-to-start question, sequences with the same displacement have the same answer. Concatenating another movement sequence adds the same further displacement. MATH.2 therefore permits identification by displacement for these operations and this answer. The compact representation is useful because its retained information has been matched to the continuation.

**Change the requested result.** Now ask whether a run visited position +1. Forward-then-backward visits +1; backward-then-forward does not. Both end at zero. The two histories could be identified for the former question, but their equivalence no longer preserves this new answer. Return through MATH.2 to the forgotten distinction. Retain the path and compute its successive positions; compare each with the queried location. In this unit-step example the recorded endpoints and monotone steps suffice. For a longer continuous movement from 0 to 2, the endpoints already imply a visit to +1. Use the recorded positions and known conditions of movement to answer the visit question. Recover further information only when those conditions leave the answer undetermined: a run that starts and ends at 0, for example, may or may not have reached +1 in between.

**Change the working method.** The team can now revise its logging and analysis method: retain the movement information needed by the questions it actually asks, specify how a calculation interprets it, and return a result with that meaning. An observer can supply displacements, a mathematical contributor can define the representation and its operations, and a programmer can implement them. ME.7 helps describe those proposed contributions and their relations. ME.12 checks the method claims and the description used by their recipients. Each contributor must understand the conditions at the join where another uses the result.

**Develop the next question.** The failure suggests a further mathematical problem: what smaller summary, if any, preserves both displacement and the requested visit information under concatenation? B.5.QD helps turn that question into a first construction or counterexample. MATH.16 can help specify what a proposed summary must let the next operation recover; the required maps and laws still need to be established. The cart is the worked example. Selecting distinctions by their use, constructing operations, justifying a compression and restoring information after a changed question are the reusable moves.

## MATH.Preface:5 - Worked use - Construct a choice after finding an obstruction

Four positions form a cycle, with costs (1,3,1,3). The required result is one cheapest position. Changing the numbering origin must rotate the selected position along with the input.

MATH.13 first establishes the transformation relation: rotation preserves the cost-minimization question. MATH.8 identifies the relevant transformed cases. A half-turn leaves this particular input unchanged but swaps its two cheapest positions.

Apply MATH.9's choice condition. An input-preserving transformation must also preserve the answer chosen from that input. Neither cheapest position is fixed by the half-turn, so the requested deterministic rule cannot choose one of them while meeting the rotation requirement.

This obstruction gives useful ways to change the problem. If the receiver can use all minimizers, return the set of the two cheapest positions. If one position is needed and a meaningful mark is available, include that mark in the input and choose the first cheapest position clockwise from it. A joint rotation preserves distances from the mark, so the selected position rotates as required. MATH.9 gives the construction and its reason.

A chosen lowest numeral would introduce a preferred origin. It is appropriate only when that added distinction belongs to the problem. A later request for continuity of the choice raises another condition; an equivariance argument alone has not addressed it.

The result identifies the missing input distinction or output change that permits a construction. The same pattern of work appears in mathematics used for geometric learning, cyclic schedules and other settings, with each setting supplying its own acceptable outputs and additional conditions.

## MATH.Preface:6 - Checks and common failures - Preserve what the next construction needs

For a use spanning several patterns, check the following relations at the joins:

1. The next operation receives objects in its domain, with every enabling condition it uses.
2. An identification retains the operation or answer that will be applied to the classes.
3. A change of representation carries the relevant operations and quantities, including the rule for returning the answer.
4. A consequence has the scope supplied by its argument: for example, impossibility, a necessary condition, a constructed witness or a minimum.
5. A computation has the data, branch decisions and termination properties claimed for its use.
6. A changed premise is followed through the constructions that depend on it.

Use the corresponding local pattern's argument where it already answers the question. A small direct use needs only its relevant conditions. A larger claim can require more: obtaining a minimum over one orbit does not by itself settle a minimum over every solution, and a physical conservation statement requires the dynamics under which the quantity is conserved.

The movement example shows why a representation must be judged against the question it answers. Accumulated displacement answers the final-position question; it loses information needed for some visit questions. MATH.2 supplies the test for retaining an answer when cases are identified. In symmetry-dependent choice, MATH.8 and MATH.9 ask how the answer must change with the data; an invariant quantity and a choice that transforms with the input need different constructions.

Another failure arises when mathematical equality is used to reorganize work without examining execution. MATH.12's split-and-join example returns equal values for a fixed function, while repeated evaluation can cost more. If a call changes hidden state, repeated calls can also return different values. Restore the relevant state and use C.29.3 for the execution correspondence before transferring that mathematical transformation.

## MATH.Preface:7 - Consequences, biases and limits

The language makes useful intermediate results available for reuse: composable paths, valid classes, interpreted expressions, witnesses, countermodels, invariant equations, solution families and qualified improvements. Their conditions help divide a larger problem among contributors and locate the part that needs revision.

This arrangement adds the cost of constructing the mathematical account. A reusable proof or operation can repay that cost across many cases. For a small question, direct calculation or an existing result can be more economical. A failed construction remains useful when it exposes the premise or operation that must change.

The examples favour small, inspectable constructions. They make dependence and failure visible, but do not establish that every larger instance will be computationally affordable. Existence of an answer, an efficient algorithm and an implementable calculation have different requirements.

The starting repertoire concentrates on formation, proof, representation and transformations. Numerical analysis, statistical inference, signal processing and specialized algorithm design supply substantial further methods. Use those contributions when the question reaches their conditions. The present patterns can help formulate that question and carry the resulting mathematical contribution into a larger argument.

An assisting agent can propose objects, examples or proofs and execute calculations. Its contribution must be understandable at the join where another contributor uses it. The mathematical statement and its justification remain available for criticism and revision, including when a person delegates the detailed calculation.

## MATH.Preface:8 - Architectural Rationale - Organize by reusable constructions

A single mathematical construction can serve many subjects. A quotient can retain the information used by a later operation; symmetry can organize solutions of a theoretical problem or constrain a learning system. This reuse makes the mathematics valuable across disciplines while leaving its specialized construction methods with mathematical practice.

The organization therefore separates three relations. Mathematical methods form objects, perform operations and establish consequences under stated assumptions. A modeling correspondence interprets an object or result in another subject. An executing arrangement performs the selected computation. These relations can be developed together, but each supplies conditions that the others need. FPF's C.29 family makes their connections usable; the mathematical bodies develop the constructions in detail.

This also clarifies the connection to methodology. Functions or paths can model how contributions compose, and mathematical laws can expose a failed identification or changed order. The model must retain the state, interactions and outputs relevant to the working method. Method Engineering, including its composition method, concerns the method being designed. Choosing morphisms to describe it provides a mathematical account whose adequacy depends on that interpretation.

Choosing a construction from its required maps is another reusable move. Its specification can lead to a product, a compatibility construction or a function object. The corresponding realization and proof still have to be supplied. This lets MATH.16 help choose among constructions while MATH.2, MATH.5 and MATH.7 retain their detailed quotient, extension and transport methods.

The pattern boundaries follow different reusable moves. Constructing a path differs from interpreting its generators; forming a quotient differs from transporting structure through a bijection. Induction obtains witnesses by input construction, while proof extraction can also use non-inductive steps. Symmetry consequences, orbit construction and compatible choice have different results and stopping conditions. Keeping these moves addressable lets a user take the required contribution and preserve its explanation, countercases and source alternatives.

A textbook can teach these constructions through a sustained sequence. A reference arranged by recurring difficulties supports another use: enter with a blocked question, obtain the relevant construction and continue elsewhere. The pattern language complements detailed source treatments, which remain useful for deeper theory and specialized methods.

There can be further useful scales. A geometric-computation profile may reuse symmetry, transport and variation while adding its own conditions; a narrower profile may develop continuous choices for a particular representation. One pattern can contribute to several such profiles. Specialization, reuse and composition describe those relations; a chapter order only helps a reader navigate them. Profiles should add a useful difference for their narrower situation rather than replace a developed method with a broad summary.

Revise this organization when a recurring use needs a construction that no body supplies, when two bodies duplicate the same useful move, or when a changed method makes their joins misleading. Preserve still-useful operations, explanations and source qualifications during that change.

## MATH.Preface:9 - Source use and currentness


For formation and composition, Fong and Spivak's [Seven Sketches in Compositionality](https://arxiv.org/pdf/1803.05316), §3.2, supplies paths and imposed equations. The patterns adapt these constructions to explicit enabling states and interpretation of composite operations. Direct enumeration remains useful when a small set of paths already answers the question.

For specifying an object through its needed maps, Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §§2.3, 3.1–3.2, supplies universal properties and set constructions. Fong and Spivak's Example 3.72 supplies currying: a function with two inputs becomes a function returning a function. MATH.16 uses these constructions to clarify an undecided use; directly defining a familiar representation remains sufficient when that choice is already settled.

Burris and Sankappanavar's [A Course in Universal Algebra](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), Chapter II, supplies congruences, quotients, term evaluation and isomorphisms. These support MATH.2, MATH.5 and MATH.7. The partial-operation convention in MATH.2 additionally preserves whether an operation is available at the represented state; the total-algebra definition alone does not choose that convention.

For obtaining objects from arguments, [Wadler's Propositions as Types](https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf) and [Rijke's Introduction to Homotopy Type Theory](https://arxiv.org/pdf/2212.11082) supply constructive rules and their mathematical setting. The maintained Lean and Rocq accounts linked in MATH.4 and MATH.12 expose the consequences of data representation, proof erasure and choice for execution. The resulting method asks which operation actually obtains the data and permits classical reasoning in a justification of an independently computable operation.

Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §§1.1, 1.3 and 1.5, supplies composition, transformations preserving it, and equivalence through compatible isomorphisms. MATH.17 uses those structures where the requested operation needs their laws; MATH.18 combines the family-level comparison with direct interpretations of primitives and assertions. A supplied inverse map remains sufficient for a simpler representation question.

For building and changing arguments, the maintained [Logic and Proof](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_propositional_logic.html#forward-and-backward-reasoning) and [Theorem Proving in Lean](https://lean-lang.org/theorem_proving_in_lean4/Tactics/) accounts provide forward and backward proof steps. MATH.19 adapts them to finding a sufficient intermediate claim, including useful generalization; a known direct theorem remains cheaper when it already closes the goal. MATH.22 combines this proof-dependency work with model and interpretation comparison, retaining the distinction between failure of one proof and failure of the theorem.

For bounds and approximations, MATH.20 derives bounds from feasible constructions, universal inequalities and residual-to-error relations, using Vandenberghe's duality account and Higham's sensitivity analysis. MATH.21 uses Cauchy completion, compatible finite information and operation-specific convergence. Its maintained Lean sources make the conditions for passing a limit through an operation explicit; Bauer and Kavkler's constructive-real account supplies an implementation alternative to a fixed convergence rate. The mathematical existence argument and the method of obtaining a requested approximation remain separately available.

For developing a new question, MATH.23 combines Lakatos's proof-and-refutation method with [Georgiev, Gómez-Serrano, Tao and Wagner's account](https://arxiv.org/html/2511.02864v3) of AI-assisted conjecture and counterexample work. The latter contributes concrete search and proof routes and their resource limits. The [Mathematical Research in the Age of AI declaration](https://mathandai.org/) raises the retention of mathematical methods as a concern; it is treated as a position in that comparison. The adopted method returns a revised claim and an attainable next operation. A person or an AI agent can supply that contribution.

The symmetry bodies compare group-action constructions with equivariant output requirements and their obstructions. MATH.9's source account distinguishes compatible selection from the additional regularity questions studied in geometric learning. MATH.10 and MATH.13 retain the separate assumptions for variation, physical conservation and numerical evolution. Return to their source comparisons when one of those stronger conclusions matters.

For invariants, [Bayarmagnai, Mohammadi and Prébet](https://arxiv.org/html/2412.14043v2) supplies a constructive comparison with polynomial-loop methods. MATH.11 uses unknown coefficients and preservation equations at their stated scope. A global polynomial identity is one useful result; a restricted-state question can call for a different construction. The finite-state countercase shows when a cheaper check is sufficient.

These sources play different roles. Established mathematics supplies definitions and arguments; maintained formal libraries and current research expose further constructions, limits and implementation choices. A publication date alone does not make one answer replace another. Revisit a choice when the receiving question changes, a relied-on assumption fails, or another method obtains a more useful result at acceptable cost. The individual bodies keep the operative source passages and the conditions of that comparison.

## MATH.Preface:10 - Relations to further reasoning and work

FPF B.5.RC and B.5.RA recover an available construction or argument; B.5.RR follows a changed premise through it. Mathematical Thinking supplies specific constructions that such reasoning can recover, use and revise. B.5.QD develops a further question from an obstruction or a successful result; C.39.RO and C.40.CD support reusable operations and their development. A construction can be worth retaining because it makes another operation or question possible before its final application is known. When choosing which question to pursue, state the work its answer could enable; E.10.INT distinguishes that usefulness from other senses of interest.

For expressions, A.6.3.RT and A.6.3.RT.OE help make an operation performable in a notation. Mathematical Thinking constructs selected mathematical structures and transports their operations. Developing a notation for a new range of work can require additional notational-engineering methods.

For application, the C.29 family and B.5.MPC connect mathematical results, computational constructions and physical accounts. Method Engineering contributes when the result is used to design or revise a way of working. Other subject frameworks supply the physical, organizational or professional methods used with the mathematics.

For evaluating alternatives, reuse FPF's characteristic, comparison and improvement methods. C.11 supports a consequential choice; C.11.DUA helps decide whether further calculation or inquiry can change that choice enough to justify its cost. Mathematical Thinking supplies the relevant construction or quantitative relation.

## MATH.Preface:End

# Part A - Choose and relate constructions

## MATH.16 - Choose a Mathematical Construction from Its Required Maps (Universal Property)

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.16:1 - Problem frame

Use this pattern when you need a mathematical object but have not decided how to construct it. You can describe what should be recoverable from it, what data should determine it, or which functions it must support. The difficulty is choosing among constructions that can all look plausible while supporting different uses.

For example, a result may need to carry two answers together, carry either kind of answer, or combine answers that agree about a shared quantity. These requests lead to different mathematical objects. Choosing a familiar representation first can hide the difference until a later operation fails.

Start by naming one operation the new object must support and the information that should determine its result. Draw the corresponding functions, including their directions. A useful first result is a requirement that distinguishes two candidate constructions. Continue to a construction and its use when the question needs them.

The method develops a **universal property**: a specification of an object through the maps it must admit and the equations those maps satisfy. The main route uses sets and all functions between them. The reader needs elementary sets, function composition and equality; the remainder example also explains the modular arithmetic it uses. Paragraphs marked **Additional structure** are optional and assume knowledge of the named mathematical theory.

If an available object and operation already answer the question, use them. A universal specification becomes useful when choosing, explaining, comparing or changing the construction is part of the work. Establishing the property for every allowed input needs an argument; working a few examples can expose a failure but cannot establish that general claim.

### MATH.16:2 - Problem

A familiar notation can suggest an object without explaining why it has the right structure. A pair of entries, a sequence, an equivalence class and a tagged alternative may all hold related information, yet the operations available on them differ.

Even an apparently adequate requirement can leave the object underdetermined. An object from which two entries can be recovered might also contain an extra entry. To say that the first two entries determine the whole, we need a further condition. Without it, a later map may require information that the proposed construction never supplied.

The problem is to turn the intended use into a mathematical specification, construct an object that satisfies it, and derive the maps and comparisons needed next.

### MATH.16:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar representation and needed operations | A convenient notation can make calculation easy while omitting a required construction or recovery. |
| Recoverable data and additional choice | Recovering the inputs leaves open whether they determine the complete result. |
| General specification and existence | A universal property can identify the desired object even when it has no realization in the chosen setting. |
| Structural sameness and computational effort | Two constructions can support the same maps while requiring different work to calculate with them. |

### MATH.16:4 - Solution

**Local mantra:** start from the use; choose maps and laws; construct the object; derive its uses; revise the changed requirement.

#### MATH.16:4.1 - Express the needed use as maps and equations

Describe what a user of the mathematical object will put in and obtain. Introduce symbols after those meanings are clear. A function `f:X -> A` takes an input in X and returns one element of A. Its direction matters: receiving an A and returning an X is another operation.

Ask what information completely determines the proposed result. If later use needs an extra choice, include that choice in the input. If the supplied data should suffice, require the resulting map to be unique.

The following contrasts help select a construction; they are examples of different mapping requirements:

| Needed use | Maps and question to formulate |
| --- | --- |
| Carry two components together and recover each one. | Seek maps from the new object to both component objects. What combined map is determined by supplying the two components? |
| Carry either kind of input, then process it according to that kind. | Seek maps from each input object into the new object. Do the two processing rules determine one rule on the combined object? |
| Combine components that must agree about a common quantity. | Express both accounts of that quantity in one codomain and require equality. |
| Identify inputs while retaining selected answers. | Which maps give the same answer on identified inputs, and therefore can operate on classes? MATH.2 supplies that quotient construction. |
| Interpret everything built from generating operations. | Which assignment to generators extends to a map preserving the operations? MATH.5 supplies the extension and its uniqueness. |

Choose the mathematical setting along with the maps. In the main route, the objects are sets and the permitted maps are all functions between them. A category specifies a setting through its objects, maps, identity maps and associative composition.

**Additional structure -- groups and topology.** For groups, choose homomorphisms preserving the group operation; for topological spaces, choose continuous functions. These choices change what must be constructed and proved.

#### MATH.16:4.2 - State the universal property before choosing an encoding

Turn the use into a requirement by comparing the proposed object with arbitrary permitted ways of supplying or processing its data:

1. Fix the objects already given by the question, together with their maps and laws. They remain the same throughout this comparison.
2. Introduce a variable object X for a possible source of data, or Z for a possible destination. Describe the maps and equations that make it an allowed instance of the needed use. Let it vary over every permitted instance, not just one sample. For example, a source of two components supplies functions from X to each fixed component set.
3. Seek an object P with the maps through which it will be used. Ask how an allowed instance should relate to P: should its data assemble into P, or should processing extend from P to a destination? Draw that comparison map in the corresponding direction.
4. Combine the comparison map with P's use maps in the order their domains require, and equate the resulting routes with the original maps. Require a comparison map for every allowed instance, and uniqueness when the supplied data should determine it completely.

This specifies the behavior a construction must realize. If the intended use leaves the maps or agreements undecided, return to that particular choice before asking for a universal object. The prepared-function case in :5.4 follows these steps for a use beyond pairing or tagging.

Suppose the question requires two recoverable components in A and B, and those components must determine the entire result. A and B are fixed; a trial source X supplies maps to both. Seek an object P with projections `pA:P -> A` and `pB:P -> B`.

For every allowed object X and maps `f:X -> A`, `g:X -> B`, require a unique map `<f,g>:X -> P` such that:

`pA composed with <f,g> = f`;

`pB composed with <f,g> = g`.

These equations say that forming the combined result and reading either component returns the supplied component. Uniqueness says there is no further choice in that combination. Any map `h:X -> P` is consequently recovered from its components:

`<pA composed with h, pB composed with h> = h`.

An object with these projections and property is a **product** of A and B. Its specification describes both how to construct a result and how to use it.

Now suppose the components must agree through maps `s:A -> C` and `t:B -> C`. Seek projections that satisfy:

`s composed with pA = t composed with pB`.

Require a unique combined map only for f and g satisfying `s composed with f = t composed with g`. This is a **pullback** of s and t: it combines precisely the data compatible under that equation.

To choose an object for either kind of input, reverse the mapping question. Seek maps `iA:A -> S` and `iB:B -> S` that place the inputs in the new object. For maps `f:A -> Z` and `g:B -> Z`, require a unique map `[f,g]:S -> Z` with `[f,g] composed with iA = f` and `[f,g] composed with iB = g`. This is a **coproduct**. In sets, a tag can preserve which input was supplied, so the processing rule can select the correct branch.

The comparison points into the product or pullback and out of the coproduct. Its direction follows the needed operation: assemble supplied components or extend supplied processing rules.

#### MATH.16:4.3 - Construct an object and establish the property

In sets, the product is the set of ordered pairs `A x B`. Use the coordinate projections and define `<f,g>(x)=(f(x),g(x))`. Both projection equations follow by reading the corresponding coordinate. Any function with those projections must return that same pair at every x, which proves uniqueness.

For the pullback, form the subset:

`Q={(a,b) in A x B | s(a)=t(b)}`.

The same pairing formula lands in Q exactly when the compatibility equation holds. Reading the coordinates again proves uniqueness. Q may be empty. The empty set is still a valid pullback in sets; it says no pair meets the stated compatibility requirement.

For a coproduct of sets, distinguish the two input branches with tags 0 and 1:

`S=({0} x A) union ({1} x B)`.

The injections are `iA(a)=(0,a)` and `iB(b)=(1,b)`. Define `[f,g](0,a)=f(a)` and `[f,g](1,b)=g(b)`. Every element has one of these forms, which establishes existence and forces the rule uniquely. Even when A and B are the same set, the tags keep the two branches distinct. For `A=B={0}`, handlers `f(0)=0` and `g(0)=1` therefore extend to a function taking `(0,0)` to 0 and `(1,0)` to 1.

**Additional structure -- groups and topology.** Establish that the object and maps have the chosen structure. For groups, define product multiplication componentwise. If f and g preserve multiplication, then their paired map does too, because each coordinate does. For a pullback of group homomorphisms, the compatibility equation is preserved by multiplication and inverses. A construction with continuous maps requires the appropriate topology and continuity arguments.

Use a known applicable construction when available. For quotient and generator questions, MATH.2 and MATH.5 provide the detailed operations. If the required object cannot yet be constructed, identify the unresolved existence or construction question. An existence theorem may supply a result for reasoning while leaving an effective way to obtain its elements for further work.

#### MATH.16:4.4 - Derive the next map, comparison or operation

Use the universal property to build the map the question needs. For a product, give the two component maps. For a pullback, also establish their agreement in C. For a coproduct, give a processing rule for each input kind.

The property also supplies equality tests. Two maps into a product or pullback are equal when both their projections agree. Two maps out of a coproduct are equal when composing each with iA gives equal maps and composing each with iB gives equal maps. This lets you compare an entire map through its required parts.

It can compare different constructions of the same object. If P and P' satisfy the same product property for A and B, the projections of each determine a map to the other. Composing these maps preserves both projections. The identity does too, so uniqueness makes the composites identities. Thus the two constructions are isomorphic by the maps that preserve their projections. MATH.7 develops the transport of further structure when a usable bijection has been obtained.

A new operation on the components needs a compatibility test. Here take Q to be the pullback of sets and `u:A -> A`, `v:B -> B` to be functions proposing updates. They induce a function `(a,b) -> (u(a),v(b))` on Q exactly when:

`s(u(a))=t(v(b))` whenever `s(a)=t(b)`.

The original agreement does not settle the changed one. A failed pair identifies which update or agreement condition must change. This gives a way to work on operations themselves while keeping their required uses visible.

**Additional structure -- groups.** When the update must also be a homomorphism, establish preservation of the group operation. Agreement of the updated components alone establishes only a function on the set of compatible pairs.

#### MATH.16:4.5 - Use the result and return to a changed requirement

Return the construction with the maps and conditions needed by its consumer. A name such as “product” helps recognition; the projections, formation rule and applicable laws let the receiver use it.

For a mathematical question, stop with the required map, equality, usable construction or demonstrated obstruction. For computation, obtain the procedure and resources needed for the chosen representation through C.29.2. A finite pullback can be enumerated by testing pairs, while a large or infinite one needs an appropriate computational method.

For an application to another subject, C.29 supplies the correspondence that gives the mathematical objects and equations their subject meaning. In particular, a compatibility equation must represent the actual agreement needed by the work. A pairing of functions on one input describes a different operation from two executions that modify a shared input. For the latter use, first specify which values each step reads and changes, and which intervening steps are permitted. Use that account to decide whether a function construction represents the work; the pairing alone leaves those interactions unspecified.

When the question changes, return to the affected mapping requirement. Adding agreement can turn a product question into a pullback question. Needing to accept either input can call for a coproduct. Needing only selected answers can call for a quotient. Retain a useful earlier construction while its earlier question remains current.

### MATH.16:5 - Archetypal Grounding

#### MATH.16:5.1 - Two classifications, then one shared integer

Two separately chosen integers have been classified. The first report gives its remainder modulo 2; the second gives its remainder modulo 4. The task is to combine the reports so that both can be recovered, and to add combined reports by adding their corresponding remainders. The two reports should determine the complete combined result.

Let `A={0,1}`, with addition reduced modulo 2, and `B={0,1,2,3}`, with addition reduced modulo 4. Adding the two reported numbers into one number loses recovery: reports `(0,1)` and `(1,0)` both give 1. Keeping a pair supplies both projections and requires no additional choice. All eight pairs are possible because the original integers may be chosen separately.

Now both reports must describe the same integer. The pair `(0,1)` fails: an integer with remainder 1 modulo 4 is odd. The modulo-4 report determines parity through `t(b)=b modulo 2`. Set s to the identity on A and construct the compatible pairs:

`Q={(0,0),(1,1),(0,2),(1,3)}`.

Every member comes from an integer. Addition stays within Q: `(1,1)+(1,3)=(0,0)`. A report determines the original integer only modulo 4.

**Additional structure -- groups.** With the stated modular additions, A and B are groups. The identity on A and the parity map t preserve addition, so Q with componentwise addition is also their pullback in groups.

The projection `(a,b) -> b` has inverse `b -> (t(b),b)`. If the next calculation is easier with one modulo-4 value, MATH.7 transports it through these maps. If the next question is which integers may be identified while retaining both reports, MATH.2 instead constructs their quotient modulo 4.

Returning to functions on the underlying sets, a proposed update exposes another choice. Incrementing the modulo-4 component alone sends `(0,0)` to `(0,1)`, outside Q. Incrementing both components gives `(1,1)` and preserves agreement for every pair in Q. The intended change to the underlying integer determines which component updates belong together.

**Additional structure -- groups.** The joint increment is not a homomorphism: it takes the identity `(0,0)` to `(1,1)`. It is suitable for updating the represented integer, but fails a requirement to preserve the group operation.

#### MATH.16:5.2 - Process both results or either result

One calculation returns an integer count; another returns a text label. A report containing both results needs a product. Its projections recover the count and the label, and the two values determine the report.

A different interface accepts either an integer count or a text label. It must display a count numerically and leave a text label as supplied. A tagged union, the coproduct of these sets, allows both handlers to determine one display function. An input tagged as a count follows the numeric handler; a text-tagged input follows the text handler.

The word “combine” did not decide which object to build. The question about formation and use did: recover two components from one report, or process either input through its own rule. These constructions describe values and functions. Whether executing the calculations reads or changes shared state is a further question about their execution.

#### MATH.16:5.3 - Two views of one quantity

A model has candidate states A and B for two component descriptions. Each description specifies the value of a shared quantity in C. For example, the two ends of an ideal connection may be required to have equal potential.

The product contains arbitrary state pairs. Requiring agreement selects the pullback of the two quantity maps. Its projections retain both component states, so a later calculation can still use their other quantities.

The physical account must justify the ideal connection and the meaning of that potential. If the connection has a relevant drop, the equality premise changes. A relation involving the drop and other quantities must be modeled before constructing its compatible states. The mathematical construction supplies the combination once that relation has been formulated; it does not choose the physical interaction law.

#### MATH.16:5.4 - Construct an object that can itself be applied

A function can be prepared by supplying a setting, then used with different inputs. We want a mathematical object representing the prepared function. Fix the input set A and output set B. A possible set of settings X supplies behavior `eX:X x A -> B`: it returns an output for a setting x and input a. Different X and eX describe different ways to prepare such behavior.

Seek a set E of prepared functions and an evaluation rule `ev:E x A -> B` for applying them. Preparing from a setting should give a map `h:X -> E`. To retain the original behavior, require:

`ev(h(x),a)=eX(x,a)` for every x and a.

Here prepared functions are equal when they give the same answer for every input. Thus the behavior specified by eX should determine h completely. Require a unique such h for every X and eX.

Construct `E=B^A`, the set of all functions from A to B. Define `ev(k,a)=k(a)`, and let `h(x)` be the function sending a to `eX(x,a)`. The required equation follows by evaluation. Any other proposed value for `h(x)` must give that same answer at every a, so it is the same function. This proves uniqueness.

For example, take A, B and X to be the integers and `eX(n,a)=n+a`. Then `h(3)` is the function that adds 3; `ev(h(3),6)=9`. The construction allows us to pass, apply and compare that function as an object. The conversion from a two-input function to a function returning a function is called **currying**. Distinguishing procedures with the same answers but different costs requires a further computational description of those procedures.

### MATH.16:6 - Bias-Annotation

Recognizing a familiar construction can make its requirements seem inevitable. In :5.2 the same informal request to combine results leads to a product or a coproduct depending on the needed operation. Write that operation before naming the construction.

The set examples make existence easy to see. Other choices of objects and allowed maps can change existence or require additional structure. Carry that choice into the argument rather than relying on the appearance of paired entries.

### MATH.16:7 - Conformance Checklist

- The working question identifies what must be formed, recovered or compared.
- Each map has a domain, codomain and meaning; its direction matches the required operation.
- The permitted maps and their preservation conditions are stated.
- Fixed objects are separated from the allowed varying instances of use.
- The universal property identifies the supplied data, the comparison map for every allowed instance, its equations and why uniqueness is wanted.
- A construction or applicable existence result supplies the object; a claimed construction has its existence and uniqueness arguments.
- A changed requirement is reflected in the construction or its admissible maps.
- Any computational or subject use obtains the additional operations and premises it needs.

### MATH.16:8 - Common Anti-Patterns and How to Avoid Them

**Recovery mistaken for full determination.** Take `A=B={0}`. Recovering both components from `A x B x {0,1}` works, but forming an element also requires choosing 0 or 1. If only A and B should determine the result, require the unique combining map. If the extra choice is useful, name it as part of the input.

**Compatible components processed incompatibly.** A map on each component need not preserve their agreement. Test the equation in :4.4; the one-component increment in :5.1 supplies a failing case and its repair.

**A familiar encoding chosen before its use.** A pair and a tagged alternative support different functions. Recover the intended formation and processing operations before selecting either.

### MATH.16:9 - Consequences

The result can be specified and compared through its permitted uses. Construction, extraction and equality arguments become connected, and a changed requirement identifies which mathematical work must be revisited.

The universal property leaves room for different implementations. Their mathematical correspondence can be established through the property, while their computational costs remain a separate reason for choosing one implementation.

### MATH.16:10 - Architectural Rationale

Organizing the choice around maps makes the required operations explicit before committing to an encoding. Including uniqueness expresses when the supplied data determine the whole result. It also gives reusable arguments for comparing maps and comparing realizations.

A direct representation remains economical for a single familiar calculation. The universal-property method earns its additional abstraction when several constructions are plausible, a representation must be changed, or later maps and arguments need to be derived. The product, pullback and coproduct cases expose different requirements. The prepared-function case shows how to formulate another requirement by varying its settings and behavior while keeping the input and output sets fixed.

Detailed quotient, generator-extension and structure-transport methods remain separately usable. They supply constructions and proofs after this method has identified the needed property. This separation permits a broader choice method without compressing those techniques into unexplained instructions.

### MATH.16:11 - SoTA-Echoing

For choosing an object through the maps it must support, the adopted line is universal construction in category theory. Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §§2.3, 3.1 and 3.2, gives the general account and concrete set constructions. The present method uses that line to move from a working requirement to a construction, then to its derived maps and equality arguments.

Fong and Spivak's [Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316), especially the chapter on databases and categories, develops the use of these constructions across applications. Its contribution here is the attention to what transformations and queries the constructed object supports. Example 3.72 supplies the function-as-object construction through currying used in :5.4.

At comparable effort, a direct pair or tagged union is often enough when the operation is already settled. Use the universal account when the ambiguity or later reasoning makes it useful. A more elaborate categorical description adds no benefit to a calculation whose relevant conditions and result are already clear.

The elementary examples use ordinary equality and functions. If the work changes the permitted maps or the meaning of equality, reformulate the comparison and its equations in that setting. A requirement to compute the result can also reopen the choice of construction.

### MATH.16:12 - Relations

- **MATH.1** constructs composable paths when the required object retains generating steps and their order.
- **MATH.2** constructs quotients while preserving the selected operations and answers.
- **MATH.5** extends generator assignments to operation-preserving maps and proves their uniqueness.
- **MATH.7** transports structure through a bijection when a different representation is useful.
- **B.5.FM and B.5.TU** connect the working question, construction and use at the common reasoning level.
- **C.29 and C.29.2** supply subject correspondence and computational formulation.

### MATH.16:End

## MATH.17 - Construct Mathematical Spaces of Operations and Operations on Them

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.17:1 - Problem frame

Use this pattern when the rule for constructing or transforming something has itself become the object of work. You may need to combine allowable rules, apply a rule to a different kind of input, compare ways of repeating it, or change the rule while retaining a useful property. Knowing how to execute each individual rule leaves these questions open.

Start with the operation you want to perform on rules and the consequence you need from it. For example: “Can these permitted updates be composed?” or “Can I transform each stage separately and obtain the same result as transforming their composite?” One constructed operation, together with its applicability and the law or counterexample that answers that question, is a useful result.

Here a **space of operations** is a specified collection of operations with the equality, composition and further structure needed by the question. The main route uses sets and functions; it requires understanding function application, composition, sets and elementary equality arguments. MATH.16 explains functions as mathematical objects, evaluation and currying. The polynomial example is an optional branch using polynomial arithmetic.

Use an existing rule directly when its application settles the question. Construct a space of operations when you need to reason about, generate or change rules. A topology, metric or order on that space becomes part of the construction when the question needs continuity, approximation or comparison in that sense.

### MATH.17:2 - Problem

An operation can be permissible on its own yet leave the permitted class when combined with another. A transformation of operations can produce a valid operation yet alter the result of a sequence. These failures occur at different places: membership, composition, or the proposed transformation.

To locate the failure, specify the rule's domain, construction and relevant laws. These supply the mathematical questions: which operations belong to the permitted collection, what can be done with them, and which conclusions follow?

### MATH.17:3 - Forces

| Force | Tension |
| --- | --- |
| Individual applicability and composition | Two allowable operations can have a composite that violates the condition used to select them. |
| Useful abstraction and needed distinctions | Functions expose input-output behavior; questions about construction steps or cost need a representation retaining those distinctions. |
| Changing rules and retaining consequences | A higher-order operation may preserve some laws, replace others, or require a narrower domain. |
| Uniform construction and branch-specific structure | One construction can work across many sets, while continuity, differentiability or other additional requirements need their own arguments. |

### MATH.17:4 - Solution

**Local mantra:** state the change to the rule; construct its admissible inputs; establish composition; construct the higher-order operation; derive its consequence; use or revise it.

#### MATH.17:4.1 - Specify the operations and the question about them

Name the inputs and outputs of an operation. Write `f:A -> B` when f assigns an element of B to every element of A. Write `g∘f` for “first f, then g”; it is defined when f's output is an allowed input to g.

Choose what counts as equality for the present question. In the main function route, f and g are equal when they have the same domain and codomain and `f(x)=g(x)` for every input x. If the question concerns the steps used, resource cost or another distinction between ways of producing that function, retain a construction or program representation carrying that distinction. A function value alone leaves it unavailable. MATH.1 supplies constructions retaining ordered steps; MATH.2 handles an identification when the needed operations respect it.

Formulate the intended operation on rules. It might take two operations and compose them, send an operation on individual inputs to an operation on collections, or turn an expression for a function into another expression. State which result matters: admissibility, an identity, a comparison, a changed construction, or a failed requirement.

#### MATH.17:4.2 - Construct the admissible collections

For each relevant pair A, B, specify `Adm(A,B)`, the collection of operations allowed from A to B. Give a condition that can be used to establish membership. Examples include preserving an order, maintaining a relation between components, or mapping a designated subset into itself.

When the operations are functions, MATH.16 supplies the function object and evaluation `ev(f,x)=f(x)`. Restrict that object by the required condition. A rule with several inputs can be represented by a function on their product when a tuple contains all the inputs it needs.

For a partial operation, include its domain of definition. If f is defined on D within A and g on E within B, their composite is defined on `{x in D | f(x) in E}`. Whether this is an acceptable domain belongs to the current question.

Changing the admissibility condition changes the collection. An update preserving a set of possible states and a map preserving an algebraic operation answer different requirements. State the requirement before using either as an admissible rule.

#### MATH.17:4.3 - Establish the composition that the work needs

Try to construct:

`Adm(B,C) x Adm(A,B) -> Adm(A,C), (g,f) -> g∘f`.

The formula already defines a function composite. To obtain the displayed operation, establish that the composite satisfies the selected admissibility condition. Establish identity membership when doing nothing must be an allowable operation. Associativity then follows from function composition.

For example, fix a subset P of X and admit every `f:X -> X` with `f(P) contained in P`. If f and g are admitted and x lies in P, then f(x) lies in P and g(f(x)) lies in P. Thus their composite is admitted, as is the identity. These operations form a **monoid**: a set with associative composition and an identity. Several object types with identities and compatible associative composition form a **category**. These names make the established structure reusable.

If closure fails, use the failing input or pair to choose the repair. You might restrict the operations, enlarge the permitted result class, or keep a sequence of operations whose total admissibility is checked separately. For a cumulative resource bound, for example, retain the sequence and accumulated cost needed to assess the whole. Calling each step allowable leaves that total unresolved.

An interchange of steps is another claim. Establish `g∘f=f∘g` when a proposed reordering needs it; associativity by itself only changes the grouping of a fixed order.

#### MATH.17:4.4 - Construct an operation on operations and its law

Give the higher-order operation its own input and output types. For a transformation sending a function f to a new function T(f), start with an arbitrary input x of the desired new function. Express its required output using f and the available operations. That expression defines T(f)(x). Then establish that the constructed function belongs to the promised output collection.

Choose the law from the needed use. If T is meant to translate a sequence stage by stage, test:

`T(g∘f)=T(g)∘T(f)` and `T(id)=id`.

The types on both sides must agree. When T also changes the objects, specify that object assignment and the corresponding operation collections. An assignment preserving these compositions and identities is a **functor**.

For instance, we want to apply `f:A -> B` separately to each entry indexed by a fixed set I. Represent the input by `s:I -> A`; the set of such inputs is `A^I`. At index i the input is s(i), so the required output is f(s(i)). Collecting these outputs gives the function `i -> f(s(i))` from I to B. We have constructed:

`L_I(f):A^I -> B^I`, defined by `[L_I(f)(s)](i)=f(s(i))`.

To derive the composition law, take arbitrary s and i:

`[L_I(g∘f)(s)](i)=g(f(s(i)))=[(L_I(g)∘L_I(f))(s)](i)`.

Equality at every index proves the composition law. The identity law follows by applying the identity at every index. If admissibility requires each entry to remain in P, the earlier membership argument applies entry by entry. A condition relating different entries needs a further preservation argument.

A different higher-order operation can have a different useful law. Differentiation of polynomials preserves sums and scalar multiples and obeys the product and chain rules. Use those laws when deriving a derivative; a composition-preservation requirement would ask it to do a different job. The needed mathematical operation determines which laws to establish.

#### MATH.17:4.5 - Use the construction to change or compare rules

Compute the proposed changed operation and derive the consequence that motivated it. When comparing “transform each step” with “transform the whole”, keep both expressions until their equality is established or a separating input is found.

The result consists of the usable construction and the conditions supporting the particular consequence. For a finite example, a counterexample can settle a failed universal claim. A general preservation claim needs an argument over its stated inputs.

Return to the affected condition when the task changes. A new interaction between entries may invalidate pointwise lifting. A narrower resource budget may invalidate closure. A new question about how the operation was obtained may require retaining the construction that an input-output function discarded.

When this mathematics describes a working method, use C.29's correspondence to identify what the mathematical operations represent and which practical distinctions they retain. A proposed program transformation also needs its execution semantics. Those connections let the result inform actual work while keeping the mathematical and subject claims recoverable.

### MATH.17:5 - Archetypal Grounding

#### MATH.17:5.1 - Individually permitted changes and a permitted whole

Let `X={0,1} x {0,1}`. An update is allowed to change at most one coordinate of each input pair. Flipping the first coordinate is allowed; flipping the second is allowed. Their composite sends `(0,0)` to `(1,1)` and changes two coordinates. The proposed collection is not closed under composition.

If the requirement limits each elementary step, keep a sequence of these steps and inspect intermediate states. If it limits the difference between initial and final states, test the composite against that bound and reject this pair. The same counterexample distinguishes the two intended uses.

Now take another requirement: the two coordinates must stay equal. Put `P={(0,0),(1,1)}` and admit functions sending P into P. The joint flip belongs; either single-coordinate flip fails. Closure follows from :4.3. This change of admissibility supplies a composable class suited to the equality requirement.

#### MATH.17:5.2 - Lift a rule, then change how repetition is distributed

Take integer operations `f(n)=n+1` and `g(n)=2n`. Pointwise lifting to pairs is the case `I={1,2}`. Applied to `(1,3)`, the lifted composite produces `(4,8)`. Lifting f and g separately and then composing produces the same pair. The proof in :4.4 establishes that agreement for arbitrary inputs and functions.

Consider a different change: `S(h)=h∘h`, meaning repeat an operation twice. This always gives another integer endofunction, but the two sequencing proposals give:

`S(g∘f)(n)=4n+6`;

`(S(g)∘S(f))(n)=4n+8`.

At n=0 the answers are 6 and 8. To repeat the complete sequence, retain `(g∘f)∘(g∘f)`. To run each stage twice, use `g∘g∘f∘f`. If f and g commute, rearrangement proves the two proposals equal; the present f and g do not.

The construction therefore returns both a valid operation on operations and a failed composition-preservation claim. That failure determines which changed rule implements the intended repetition.

#### MATH.17:5.3 - An operator whose useful law has another form

Let `P=R[x]`, the real-coefficient polynomials in one variable, and define `D:P -> P` by differentiating each monomial: `D(a*x^n)=n*a*x^(n-1)` for n>0, and D(a)=0 for constants. This constructs an operation on functions through their polynomial expressions.

For `p=x^2` and `q=x+1`:

`D(p*q)=3*x^2+2*x`.

The product of derivatives is `D(p)*D(q)=2*x`. The applicable law is instead:

`D(p*q)=D(p)*q+p*D(q)`,

which gives the required result. To establish the law generally, first expand two monomials: differentiating `a*b*x^(m+n)` gives coefficient `(m+n)*a*b`, the sum of the two product-rule contributions. Distributing over the finite sums proves it for polynomials.

The same method of working is used as in :5.2: construct the operator, identify the law needed for the proposed use, and establish that law. Here it enables transforming a product expression into its derivative.

#### MATH.17:5.4 - Change a function while preserving its increments

Given a function f from the real numbers to the real numbers and a chosen point c, construct a function g that fixes c and preserves every increment of f. The requirements are g(c)=c and g(x)-g(y)=f(x)-f(y) for every x,y.

Set y=c in the second requirement. It forces g(x)=f(x)-f(c)+c. This defines a real-valued function; substituting c establishes the fixed point, and subtracting its values at x and y cancels the added constant and preserves the required increment. Thus the formula supplies the unique function under these requirements.

The transformation takes f itself as an input and returns g. Fixing a point and preserving increments do not settle an additional question about composition or cost. The repetition case in :5.2 shows how different requested changes lead to different operations on the same input rules.

### MATH.17:6 - Bias-Annotation

A familiar collection of “valid operations” can conceal an unproved closure claim. A familiar higher-order operation can conceal the choice of law used to combine its results. Work with the actual membership condition and proposed equation; the failing inputs in :5.1 and :5.2 locate those different errors.

The set-and-function route makes these questions accessible. A question involving topology, approximation, randomness or an alternative equality calls for the corresponding additional structure and argument.

### MATH.17:7 - Conformance Checklist

For the construction being used:

- The operations have recoverable inputs, outputs, equality and admissibility conditions.
- The needed compositions land in the claimed collection, or a concrete failure has changed the proposed use.
- The higher-order operation has a construction and returns an admissible output.
- Each law used to derive the result has the required scope and an argument; a tested finite case supports only what it establishes.
- The resulting comparison or changed rule answers the starting question.
- A subject or computational application supplies the correspondence or execution account needed by that use.

### MATH.17:8 - Common Anti-Patterns and How to Avoid Them

**Inferring closure from individual permission.** The two flips in :5.1 each meet the step condition but fail it when composed. Decide whether the requirement concerns a step, a sequence or the whole input-output change, and construct the corresponding collection.

**Moving a transformation through composition without its law.** Repeating each stage twice changed the answer in :5.2. Derive the transformation equation before using it to reorganize a sequence.

**Demanding the wrong preservation law.** Polynomial differentiation supplies a useful operator through linearity and the product rule. Choose the law from the intended transformation instead of requiring every operator to preserve multiplication or composition.

### MATH.17:9 - Consequences

Operations become available for construction, comparison and change. A law established for the higher-order construction can replace repeated case-by-case reasoning, while a counterexample can identify a proposed change that needs revision.

The abstraction has a cost: the operation collection and its laws must be constructed. It pays when the rule itself is changing or when one result will organize many operations. Questions about implementation, approximation or real interaction can require further structure beyond the function account.

### MATH.17:10 - Architectural Rationale

Separating membership, closure and higher-order transformation locates three different sources of failure. Combining them into a generic instruction to “check composition” would leave the repair unclear.

MATH.16 supplies the function-object construction. Here the practitioner selects a collection of allowable operations and constructs further operations whose arguments are members of that collection. Monoid and category language make the established composition reusable; the derivative example shows why other higher-order operations need other laws. The choice follows the problem about rules.

The same structure can support mathematical work, computational transformations and mathematical accounts of methods. Its applicability in the latter two depends on the interpretation of operations and consequences, which remains the responsibility of the receiving method.

### MATH.17:11 - SoTA-Echoing

Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §§1.1 and 1.3, supplies the algebraic account of composable maps, monoids and functors. The adopted contribution is the ability to study transformations of operations by their preserved structure. This pattern turns that account into a method for selecting admissible operations, finding a failed closure condition and constructing the transformation required by the question.

A direct formula is sufficient when one operation settles the task. The structured account helps when rules must be combined or changed. Polynomial operators illustrate the alternative: linearity and a product rule may provide the useful calculus even when composition preservation is inapplicable. Additional mathematical structure is selected by the needed consequence.

### MATH.17:12 - Relations

- **MATH.16** constructs function objects, evaluation, products and maps selected by their required uses.
- **MATH.1** retains generating steps and their order; **MATH.5** extends an assignment to generators through the operations it must preserve.
- **MATH.2** establishes when an identification of operations supports the proposed further operations.
- **MATH.7** transports structure through a bijection. Comparing broader mathematical accounts uses interpretations of their objects, operations and assertions.
- **MATH.11 and MATH.13** develop invariant and symmetry consequences once the transformations are specified.
- **B.5.FM, C.29 and C.29.2** connect the mathematical construction with a working question, subject correspondence and computational use.

### MATH.17:End

## MATH.1 - Build a Mathematical Structure of Composable Paths

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.1:1 - Problem frame

Use this pattern when you know elementary steps and their permitted connections, but still need mathematical objects for their finite combinations. Typical questions are: which steps form a permitted sequence, how can two sequences be joined, and which distinctions must remain available for a later operation?

The construction below makes paths from generating arrows. An arrow has a starting object and an ending object; these can be states, types or mathematical objects. A path is a finite ordered list of arrows whose adjacent endpoints agree. The resulting structure can describe formal words as well as possible routes through a process. Its mathematical laws come from the construction.

Start by writing two steps you want to join and their endpoints. If the first ends where the second starts, their ordered pair is already a useful first path. If the written endpoint hides a condition that changes whether the second step is available, refine the endpoint before joining them.

You need elementary sets, ordered lists and equality. If an existing structure already supplies the combinations and distinctions your question needs, use its operations directly. This pattern is useful when constructing or changing those operations is itself the difficulty.

### MATH.1:2 - Problem

A list of elementary steps leaves the composite objects and their operations undecided. Joining names that merely look compatible can produce a combination that the generating rules do not permit. Collapsing two paths to the same endpoint can also erase their different steps, costs or available continuations.

The mathematical task is to construct the combinations, define when composition is possible, and establish the laws that follow. The result should let another person or computational agent reproduce a path and reason about a longer combination from its parts.

### MATH.1:3 - Forces

| Force | Tension |
| --- | --- |
| Finite description and unbounded reuse | A few generators can produce arbitrarily long paths; listing all paths is usually impossible. |
| Keeping distinctions and economical reasoning | Remembering the generators preserves information, while a later question may need only a quotient or a numerical value. |
| Local compatibility and later use | An endpoint sufficient for today's composition may hide a condition needed by a changed continuation. |
| Composition and interpretation | Concatenation has laws by construction; a physical or computational interpretation has further conditions of its own. |

### MATH.1:4 - Solution

**Local mantra:** name the endpoints; form paths; join matching paths; use the composition laws; retain the distinction needed by the next operation.

#### MATH.1:4.1 - Choose objects and generating arrows

Write the objects at which the elementary steps start and end. For each generator `a`, give a source `s(a)` and a target `t(a)`. Several generators may have the same source and target.

Include conditions that determine the availability of the selected continuations. A location may be enough for one problem; another may require a pair such as `(location, permission)`. Use a failed attempted continuation to find the needed distinction. There is no requirement to anticipate every possible future operation.

The generating arrows and endpoints form a directed graph in the mathematical sense. A drawing can display it, but the vertices, arrows and endpoint functions define the structure. A physical network or an organization's work may be interpreted through this graph; that application supplies its own claims about what the arrows can represent.

#### MATH.1:4.2 - Form finite paths

A path of length `n>0` is a list `[a1,…,an]` with `t(ai)=s(a(i+1))` for every adjacent pair. Its source is `s(a1)` and its target is `t(an)`.

At each object `x`, add an empty path `id_x`. It starts and ends at `x` and contains no generator. Keeping its object matters: the empty path at one object cannot serve as the identity at another.

Initially, two nonempty paths are equal when their lists contain the same generators in the same order. The empty paths are equal only at the same object. This choice retains the sequence used to construct the path. A later identification can deliberately forget part of it, using MATH.2.

Construct only the paths needed for the immediate question, or describe a family by its formation rule. Cycles make infinitely many paths possible, but each path remains finite.

#### MATH.1:4.3 - Define composition by concatenation

For paths `p:x→y` and `q:y→z`, write `p;q` for the path obtained by putting the list of `q` after the list of `p`. Here the semicolon is read in execution order: first `p`, then `q`.

Composition is defined when the full intermediate object agrees. Its source is `x` and its target is `z`. If the endpoints disagree, repair the proposed sequence, supply a connecting arrow that is actually permitted, or return the failed connection.

Concatenation gives two laws:

- `id_x;p=p=p;id_y` for `p:x→y`, because an empty list adds no generator.
- `(p;q);r=p;(q;r)` for three consecutively composable paths, because both sides contain the same three lists in the same order.

These arguments establish identity and associativity for this construction. They can be reused while the definitions stay unchanged. They leave the order of the generators intact: `p;q` and `q;p` can differ or one can be undefined. A structure with objects, arrows and these laws is a category; the path construction gives the free category on the generating graph.

#### MATH.1:4.4 - Use the path at the needed level

Return the path that answers the immediate composition question, or the formation and composition rules when the receiving work needs a reusable family.

If each generator has a supplied additive cost, obtain a path's cost by adding the costs of its generators; the empty path has cost zero. Keep the path as well when the receiver needs to execute it or inspect why it is available. Two paths with the same cost can contain different generators.

If a representation hides an intermediate object, test the attempted composition that made the distinction matter. Refine the objects or retain the paths until the subsequent operation is well defined. MATH.2 constructs an identification that preserves selected operations; it can later reduce the structure deliberately.

An interpretation can associate generators with transformations in another setting. The mathematical path then specifies their composition. Whether those transformations are available and adequate in that setting is the application's question, using such common methods as FPF C.29 and B.5.MPC.

Stop when the receiving question has a permitted path, a reusable construction, or a specific failed connection. Constructing every possible path or proving an unchanged concatenation law again adds no result to that use.

### MATH.1:5 - Archetypal Grounding

#### MATH.1:5.1 - A continuation that needs a permission

Two routes `p` and `q` start at `S` and reach location `V`; their costs are 1 and 4. A final step `r` costs 2. Under the first rule, `r` is available after either route, so `p;r` and `q;r` are paths and their costs are 3 and 6.

Now change the rule: only `q` grants the permission needed for `r`. Keeping a single endpoint `V` would still make `p;r` appear composable.

Construct two intermediate objects, `V0=(V,0)` and `V1=(V,1)`. Set:

| Generator | Source | Target | Cost |
| --- | --- | --- | ---: |
| `p` | `S` | `V0` | 1 |
| `q` | `S` | `V1` | 4 |
| `r` | `V1` | `T` | 2 |

The path `q;r` exists and costs 6. The expression `p;r` fails the endpoint test. Selecting the cheaper prefix first would therefore lose the available completion. The useful result is the permitted path and its cost; the refined endpoint explains why it is permitted.

If a further generator `a:V0→V1` grants permission at cost 1, a new path `p;a;r` becomes available at cost 4. The former failure has opened a construction question: what additional arrow would connect the available prefix to the required continuation?

#### MATH.1:5.2 - Natural numbers from repetition

Take one object `X` and one generating loop `a:X→X`. The paths are the empty word, `a`, `a;a`, and longer repetitions. Write `a^n` for the list containing `n` copies, with `a^0=id_X`.

Concatenating `a^m` and `a^n` gives `a^(m+n)`. Thus lengths supply an arithmetic account of this structure: the identity corresponds to 0 and composition corresponds to addition. Every path is determined by its length in this one-generator case.

Adding a second loop `b` changes the situation. The paths `a;b` and `b;a` both have length 2 but are different lists. Counting generators now loses their order. It still answers a length question; a question about which generator acts first requires the path.

#### MATH.1:5.3 - Order matters under interpretation

On integers let `f(x)=x+1` and `g(x)=2*x`. Both generators start and end in the integer type, so both orders are composable. Starting from 0, `f;g` returns 2, while `g;f` returns 1.

The associativity argument allows regrouping a longer list. It does not authorize exchanging `f` and `g`. The differing results make that boundary consequential.

#### MATH.1:5.4 - Keep the intermediate states of interacting updates

Two updates to a counter each read its current value, retain that reading and later write the reading plus one. From zero, finishing one update before the other gives two. If both read zero before either writes, the final value is one.

To represent the difference, a state retains the counter, each update's saved reading and whether its read and write have occurred. A read copies the counter into that update's saved value; its later write replaces the counter by that saved value plus one. Form paths in which each read precedes its own write. The paths read-A, write-A, read-B, write-B and read-A, read-B, write-A, write-B return two and one respectively.

Treating each update as one indivisible arrow would lose the second path. If the work can require one complete update to finish before the other, the restricted paths preserve both increments. FPF C.29 establishes how these transitions describe the implemented work; Method Engineering ME.7 helps change its composition. Choosing an implementation also depends on how it handles waiting, interruption and failure.

### MATH.1:6 - Bias-Annotation

A familiar drawing can make location seem like the whole state. The permission case exposes the omitted condition through a failed continuation, then repairs the mathematical object.

The construction also favors retaining history. This is useful while the role of the generators is unsettled, but it can be unnecessarily expensive when only a value or an equivalence class is needed. Use the subsequent quotient or evaluation deliberately, stating the operation or question it preserves.

### MATH.1:7 - Conformance Checklist

- Can the reader identify each generator's source and target?
- Does each constructed path satisfy the adjacent-endpoint condition, including any action-changing refinement such as permission?
- Are empty paths attached to their objects and composition defined in one stated order?
- Are the claimed identity and associativity laws supported by the construction used?
- Does the returned path retain the detail required by its next use? If only a cost, length or class is returned, is that sufficient for the receiving question?
- When a connection fails, is the missing or incompatible endpoint recoverable without inventing an available generator?

These questions assess the construction in use. They do not require a separate record for each path.

### MATH.1:8 - Common Anti-Patterns and How to Avoid Them

**Join by location while losing an enabling condition.** In :5.1, replacing `V0` and `V1` by `V` creates an apparent connection that the permission rule excludes. Restore the condition in the intermediate object and try the composition again.

**Use a path value as a substitute for a path.** The same length can describe `a;b` and `b;a`. Return the list when order matters; return the value when the question only consumes that value.

**Read associativity as permission to reorder.** Parentheses choose grouping. They leave generator order unchanged, as the `f;g` example shows.

### MATH.1:9 - Consequences

The construction turns elementary connections into reusable mathematical objects and an operation on them. It provides a witness for a permitted combination and a precise location for a failed one. Different contributors can prepare subpaths and compose them at shared endpoints.

Retaining all generator lists can produce a much larger structure than the final question needs. A quotient can remove selected distinctions; a cost calculation can compare alternatives. Each reduction has to preserve what its receiving use consumes.

A new continuation may reveal an inadequate object description. The repair then changes the endpoint distinction and the affected paths, while unchanged generating rules and concatenation arguments remain reusable.

### MATH.1:10 - Architectural Rationale

Generating first and identifying later separates two mathematical decisions: which composites exist and which of them count as the same. It gives a small constructive starting point when an application or theory has elementary steps but no satisfactory account of their combinations.

The empty path and endpoint conditions make composition uniform. An already completed segment can be treated like an elementary arrow in a larger composition. This is why the same construction supports words, typed transformations and possible routes through a process.

A concrete transformation structure can be more economical when only its resulting transformations matter. Paths earn their additional detail when the sequence, its formation conditions or its later reinterpretation affects the answer. The examples expose both uses: one generator is recoverable from length, while two generators can lose consequential order.

This method constructs a particular mathematical structure. FPF B.5.RC helps recover a construction already described, and C.29 helps relate a mathematical structure to another subject. Their results can be used before or after this construction.

### MATH.1:11 - SoTA-Echoing

**Question:** how can permitted elementary connections generate reusable composites while retaining their order and formation conditions?

**Adopt** the free-path construction in Fong and Spivak's [*Seven Sketches in Compositionality*](https://arxiv.org/pdf/1803.05316), §3.2.1, pp.82-83, 2018 manuscript: arrows generate finite paths, with empty paths and concatenation. It supplies the constructive definitions used in :4.2-:4.3.

An alternative is to compose the interpreted transformations directly. Retaining permission in the state can make the required continuation's availability explicit; the functions in :5.3 already distinguish the two orders. By comparison, a location-only summary in :5.1 loses permission, and length alone in :5.2 loses order.

**Adapt** the construction by retaining generator history when the receiving question needs it. On the integers let `f(x)=x+1` and `h(x)=x-1`. The path `f;h` and the empty path induce the same identity function. With unit cost for each generator their costs are 2 and 0. Direct function composition answers the transformation question; the paths retain the steps for inspection or replacement, while a cost-only question can use their calculated costs. The trade-off is the larger space of paths in exchange for recoverable history.

Section 3.2.2, pp.84-85, supplies the later option of imposing path equations; MATH.2 develops operation-preserving identification. The route and permission cases here are authored applications of the mathematics. Reconsider this choice if a quotient or an interpreted structure supports the same required continuations with less retained detail, or if the problem's compositions are not finite sequential paths.

### MATH.1:12 - Relations

- **Uses FPF B.5.RC when needed:** recover an unfamiliar source's objects and construction rules before choosing generators.
- **Supplies MATH.2:** paths and composition can be the objects and operation whose identification is tested.
- **Connects with FPF C.29 and B.5.MPC:** carry a mathematical path or obstruction to an interpreted subject, and revisit the subject formulation when the correspondence fails.
- **Connects with FPF B.5.QD and C.39.RO:** a missing connection can motivate a new generating operation or a new mathematical question.

### MATH.1:End

## MATH.2 - Treat Objects as the Same While Preserving Operations (Quotient)

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.2:1 - Problem frame

Use this pattern when you want to treat several mathematical objects as one because a working question appears not to distinguish them. You still intend to apply operations to the resulting classes. The recurring difficulty is that two apparently interchangeable inputs can produce different classes of output, or permit different next operations.

Start with the proposed identification and one operation the receiver will use. Find two identified inputs and apply that operation. A differing output class, or availability after only one input, is already a useful counterexample. Repair the identification or change the intended use before calculating with the classes.

The method constructs a quotient: a set of equivalence classes with operations inherited from the original objects. You need elementary sets, relations and functions. It applies to specified total operations, and to partial operations under the additional domain condition in :4.3. When individual objects already support the question economically, use them directly.

### MATH.2:2 - Problem

An equivalence relation makes classes, but by itself it does not determine usable operations on those classes. An operation defined by selecting a representative is ambiguous if a different representative changes the returned class.

There is a second loss to check: even a mathematically sound quotient may discard the quantity or distinction the receiver wants. The task is to construct an identification that preserves both the selected operations and the intended class-level question, or to expose why the proposed identification cannot do so.

### MATH.2:3 - Forces

| Force | Tension |
| --- | --- |
| Fewer objects and retained operations | Merging objects simplifies reasoning but may erase a distinction used by an operation. |
| A convenient resemblance and an equivalence relation | Closeness or one shared property may suggest a grouping without giving reflexivity, symmetry and transitivity. |
| Total and partial operations | Matching returned classes is enough for a total operation; a partial operation also has an availability condition. |
| Valid quotient and useful answer | An operation can descend to classes while the receiver's requested quantity cannot. |

### MATH.2:4 - Solution

**Local mantra:** choose what may be identified; test the operations; repair the distinction; form the classes; answer only what those classes determine.

#### MATH.2:4.1 - Specify the carrier, operations and receiving question

Name the set `A` of objects and the operations to retain. An n-ary total operation `f` maps every tuple in `A^n` to an element of `A`. A partial operation has a stated domain `D_f⊆A^n`.

When an operation takes inputs from different sets or returns a result in another set, choose an equivalence relation on each participating set. Compare corresponding inputs under their sets' relations and the resulting outputs under the output set's relation. A transition on states and concatenation of paths are different operations; choose the one actually used by the proposed identification.

State the receiving question. For example, the receiver may need the parity of a sum, the cost of a continuation, or whether a next step is available. This determines which distinctions a useful quotient can lose.

#### MATH.2:4.2 - Make the proposed equality into an equivalence relation

Write `a~b` for the proposed identification. An equivalence relation is reflexive, symmetric and transitive. Its class `[a]` contains all objects identified with `a`; these classes partition `A`.

If the candidate is a resemblance, test the missing law before forming classes. For instance, on integers `a~b` defined by `|a-b|≤1` is reflexive and symmetric but fails transitivity: 0 is related to 1 and 1 to 2, while 0 is not related to 2.

You can refine a proposed relation by retaining an additional property. Requiring both `a~b` and `h(a)=h(b)` remains an equivalence relation when `~` was one. Choose `h` from the failure that matters to the operation or query. The repaired relation still needs the operation test.

#### MATH.2:4.3 - Test compatibility, including the domain of a partial operation

For a total operation `f`, compare tuples whose corresponding entries are equivalent. The compatibility condition is:

`a1~b1, …, an~bn ⇒ f(a1,…,an)~f(b1,…,bn)`.

An equivalence relation satisfying this condition for every retained total operation is a congruence for those operations.

For a partial operation, first require agreement about whether it can be applied:

`a1~b1, …, an~bn ⇒ ((a1,…,an)∈D_f ⇔ (b1,…,bn)∈D_f)`.

Where both tuples are in the domain, require equivalent outputs as above. This pattern uses the resulting quotient convention in which availability is independent of the representative. A set-valued or approximate account that deliberately combines differing possibilities is another construction.

Use an algebraic argument for a general claim, or exhaustive checking when the specified carrier is finite. A few successful examples can suggest the relation; one failure is enough to refute compatibility.

If the test fails, keep the distinguishing information in the objects or narrow the operation/question being claimed. For a finite partition, split the failing class using the exposed distinction and retest the affected operations. This is a local repair; repeated splitting is not being offered here as a general minimization algorithm.

#### MATH.2:4.4 - Define the quotient operation and show that it is well defined

When the conditions hold, form `A/~`, the set of classes, and define the inherited operation by:

`f_bar([a1],…,[an])=[f(a1,…,an)]`.

The right side is independent of the chosen representatives precisely because compatible inputs return equivalent outputs. For a partial operation, agreement of domains also makes its availability independent of that choice.

This argument is reusable for unchanged conditions. The useful result is an operation on classes, together with the relation and the reason it is valid. There is no need to reproduce the proof for every subsequent calculation with the same quotient.

Preserve a representative or a way to construct one when later work needs an individual object. Knowing only a class may be sufficient for one answer and insufficient for a later request about a member.

#### MATH.2:4.5 - Check which answers can be recovered and use the result

A value `q(a)` can be recovered from `[a]` when it is constant on that class: `a~b ⇒ q(a)=q(b)`. Then define `q_bar([a])=q(a)`. If this fails, return to the original objects, retain more information, or return the range of possibilities when that answers the question.

Use the quotient for the declared operations and answers. A new operation or query can require a finer relation. The old quotient retains its earlier use; revise the part that the new question distinguishes.

Stop with a valid class-level operation and usable answer, or with a counterexample identifying the lost operation or quantity. Additional formalization is useful only when it resolves a remaining mathematical or receiving question.

### MATH.2:5 - Archetypal Grounding

#### MATH.2:5.1 - Absolute value fails, parity works for addition

Suppose integers are identified when they have the same absolute value. Then 1 and -1 are identified. Add the same integer 1 to both: the results are 2 and 0, which have different absolute values. This equivalence relation therefore cannot support addition inherited from integer representatives.

For a question about parity, choose a different relation: `n~m` when `n-m` is even. Reflexivity, symmetry and transitivity follow from the corresponding facts about differences divisible by 2.

If `n~n'` and `m~m'`, then `(n+m)-(n'+m')=(n-n')+(m-m')` is even. Addition therefore preserves the relation. There are two classes:

| `+` | Even | Odd |
| --- | --- | --- |
| Even | Even | Odd |
| Odd | Odd | Even |

The class of 7 plus the class of 4 is Odd. This answers the parity question using two classes. It does not determine whether the sum is 11 or another odd integer; a request for the sum itself requires the operands or more information.

Now request multiplication as well. The earlier addition argument does not settle the new operation. Here a separate calculation does:

`n*m-n'*m'=(n-n')*m+n'*(m-m')`.

Both terms on the right are even when the corresponding inputs have the same parity. The quotient can therefore also support multiplication. The changed request led to a new compatibility argument while preserving the earlier addition result.

#### MATH.2:5.2 - A location class loses availability

Let `V0` and `V1` be states at location `V`, without and with permission. A partial transition `r` is defined at `V1` and returns `T`; it is undefined at `V0`.

The proposed location-only relation identifies `V0~V1`. Output comparison alone would find no conflicting pair of returned values, because one value does not exist. The domain test detects the failure: `V1∈D_r` and `V0∉D_r`.

Refine the relation to retain permission. The two states are now in different classes, and the inherited transition is available only on the class containing `V1`. In MATH.1's route case, this retains the permitted `q;r` of cost 6 and excludes the apparent `p;r` of cost 3.

A convention that declares a class enabled whenever any representative is enabled would answer a different question: a transition is possible from some member. To execute it from the actual state, that convention still needs a suitable member or an enabling step. The present construction preserves the availability of the given operation at the represented state.

#### MATH.2:5.3 - Identifying words changes the question they answer

Take the one-generator paths `a^n` from MATH.1, with concatenation `a^m;a^n=a^(m+n)`. Impose `a^2~a^0` and choose the smallest equivalence relation compatible with concatenation that contains this equation.

Compatibility propagates this equation under concatenation. Adding one `a` gives `a^3~a`, and repeated deletion of a pair reduces every even-length word to the empty path and every odd-length word to `a`. These two groups remain distinct: parity itself is a compatible relation satisfying the imposed equation, as :5.1 shows, so the smallest such relation cannot identify opposite parities. This yields two classes and a composition table identical to the addition table above.

The quotient can describe the parity of repeated toggling. It discards the number of toggles. If each use takes time, elapsed cost cannot be recovered from those two classes alone. Retain the length or accumulated cost for a question that consumes it.

#### MATH.2:5.4 - Normalize labelled values before identifying them

A temperature-checking method accepts values labelled Celsius or kelvin. It converts them to kelvin, then tests membership in the inclusive interval [273.15,303.15]. Grouping inputs by their numeral alone loses the answer: 20 Celsius becomes 293.15 kelvin and passes, while 20 kelvin fails.

Let n(v,C)=v+273.15 and n(v,K)=v. Identify inputs when their n-values agree. Every input has a normalization result, and identified inputs have equal results; both the normalization and the following interval test therefore descend to these classes. This uses the separate input and output sorts of :4.1.

A later question about the original unit cannot be answered from the class alone. Retain the label when that question matters. If the description of the working method places comparison before normalization, Method Engineering ME.12:4.4 helps locate and repair that contradiction. The mathematical compatibility test and the repair of the described work answer different parts of this example.

### MATH.2:6 - Bias-Annotation

A shared appearance or outcome can make identification seem self-evident. The absolute-value case tests that intuition through an operation, and the permission case tests it through availability.

Compression can also look like improvement simply because there are fewer classes. The query condition in :4.5 keeps the receiving answer in view. A larger description can be preferable when it retains a consequential distinction.

### MATH.2:7 - Conformance Checklist

- Are the carrier, retained operations and receiving query identifiable?
- Does the relation used to form classes satisfy equivalence, rather than only resemblance or proximity?
- Do equivalent input tuples give equivalent outputs for every operation claimed on the quotient?
- For each retained partial operation, is availability also independent of the representative?
- Does the quotient definition return one class without requiring an unstated representative choice?
- Is the requested answer constant on the relevant classes, or is the lost information explicitly retained or returned as possibilities?
- Has a changed operation or query been checked at the condition it changes?

A counterexample closes a failed proposed identification. It does not require a completed replacement quotient before it can be useful.

### MATH.2:8 - Common Anti-Patterns and How to Avoid Them

**Use a resemblance as if it partitioned the set.** The distance-at-most-one example fails transitivity. Establish the relation being used before computing with its classes.

**Check outputs but ignore availability.** In the permission case, the absence of one output is the failure. Include the domain condition when operations are partial.

**Treat any valid quotient as adequate for every query.** Parity supports addition of classes while losing the numerical sum. Check the value the receiver actually asks for.

**Impose one equation but ignore its consequences under composition.** Identifying `a^2` with the empty path also identifies `a^3` with `a`. Carry the equation through the retained operation, or keep the objects distinct.

### MATH.2:9 - Consequences

A successful construction gives equivalence classes on which the retained operations remain meaningful. It can reveal a simpler mathematical structure, such as addition on two parity classes.

A failure identifies the information that the proposed grouping would erase. This can improve the original formulation, expose an unavailable continuation, or suggest a better question before an algorithm is built.

Refinement preserves more information and can increase the cost of representation and calculation. Deliberate approximation or set-valued abstraction can be worthwhile alternatives when their weaker answer is useful; they require their own stated operation and result conditions.

### MATH.2:10 - Architectural Rationale

Quotient construction and result transfer answer related but different questions. Here the mathematical operation on equivalence classes is constructed and its well-definedness established. A subsequent interpretation determines whether those classes and operations answer a question about another subject.

The domain condition is explicit because partial operations can fail before returning a value. The permission example would pass an output-only test vacuously, yet the intended next step would depend on the representative. Preserving availability repairs that defect.

The receiver's query remains separate from operation compatibility. A congruence can make addition well defined and still lose the requested sum. This separation lets one quotient remain useful for parity while a different use retains the individual numbers.

The method is about the particular identification proposed. Broader search for an optimal quotient, automated state minimization or a learned abstraction can reuse these conditions while supplying additional algorithms and selection methods.

### MATH.2:11 - SoTA-Echoing

**Question:** when can operations be inherited by classes without depending on an arbitrary representative?

**Adopt** congruence and quotient algebra from Burris and Sankappanavar, [*A Course in Universal Algebra*, corrected 2012 edition](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), Chapter II §5, pp.35-36. The compatibility condition and quotient definition supply :4.3-:4.4 for total operations. This is a constructive answer whose general reason applies beyond any one example.

The serious alternative is an equivalence relation chosen only by a shared property. It costs less to state, but the absolute-value example cannot support the required addition. The compatibility argument adds work where the quotient operation is claimed and resolves that ambiguity.

**Adapt** the construction to the partial-operation use by preserving domain membership as well as output classes. The alternative existential convention permits an operation when some class member permits it. That is useful for a possible-transition question but loses availability at the represented state. The permission case selects the stronger convention and places its added condition in :4.3. The cited total-algebra passage does not supply this partial-operation convention.

**Adopt** the composition consequences of imposed path equations from Fong and Spivak's [*Seven Sketches in Compositionality*](https://arxiv.org/pdf/1803.05316), §3.2.2, pp.84-85, in :5.3. Reopen the choice if the receiving question accepts a weaker bound or set of possibilities at lower cost, or a new operation distinguishes members of an existing class. Neither source establishes that a particular physical or organizational interpretation is adequate.

### MATH.2:12 - Relations

- **Uses or follows MATH.1:** a generated path structure provides objects and composition to identify.
- **Connects with FPF C.29.1:** use the quotient and its map in a wider result correspondence; check the subject interpretation separately.
- **Connects with FPF A.3.3.PI:** a description can lose a distinction needed to predict continuation; the present method supplies the quotient-side operation and domain test.
- **Connects with FPF B.5.RR and B.5.QD:** revise the argument after a changed operation, or turn a counterexample into a new construction question.

### MATH.2:End

## MATH.5 - Extend a Generator Assignment While Preserving Operations (Homomorphism)

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.5:1 - Problem frame

Use this pattern when you know what the basic elements of a mathematical construction should become and need a compatible map on everything built from them. A value assigned to a variable, a transformation assigned to a command, or a cost assigned to a generating step must extend to composite expressions in a way that preserves the chosen operations.

The needed map is a *homomorphism*: it carries each source operation to the corresponding target operation. To construct it, evaluate composite expressions from the assigned generator values. If the source identifies different expressions, establish that those expressions receive the same value.

Start with one generator and one composite expression. Return their images and the rule that extends the assignment, or a source equality that the proposed images cannot preserve. A first calculation can expose an incompatible assignment before a large translation is attempted.

The reader needs functions, finite expressions and the operations used in the chosen construction. The method covers total operations with finitely many inputs, finite words with associative composition, and the finite typed paths built by MATH.1. A typed path starts and ends at named objects; its interpretation must supply their images as well as the images of its arrows.

If the required map or one needed value is already available, use it. An arbitrary map on a small finite set can be simpler to specify directly when preserving operations is not part of the question.

### MATH.5:2 - Problem

A list of corresponding symbols leaves most compound expressions unassigned. Filling them independently can violate the operation that made the correspondence useful. Two source expressions may also denote the same object while their proposed target values differ.

The task is to obtain a reusable mapping rule and identify its scope. The assignment on generators must determine the composites, and every source identification used by the map must remain valid after evaluation.

### MATH.5:3 - Forces

| Force | Tension |
| --- | --- |
| Few generators and many composites | A compact assignment can govern arbitrarily large finite expressions, provided the extension rule is established. |
| Free construction and imposed equations | Syntax permits independent construction; equations identify expressions and restrict their possible images. |
| Preserved operations and retained information | A homomorphism can preserve composition while forgetting distinctions needed by another question. |
| Reusable translation and one calculation | Building the general map costs more than evaluating one expression, but supports substitutions and repeated use. |

### MATH.5:4 - Solution

**Local mantra:** name the generators and operations; assign their images; extend by construction; preserve the equations; use the resulting map.

#### MATH.5:4.1 - State the source construction and target operations

List the generators and the rules for building finite expressions from them. An expression can be a generator, a constant, or an operation applied to constituent expressions. State each operation's number of inputs. With generators `x,y`, constants `0,1` and binary operations `+` and `*`, the expression `(x*y)+1` is obtained by two construction steps.

Distinguish the freely formed expressions from any equations imposed on them. For example, treating `x*y` and `y*x` as the same requires a commutativity equation. The written resemblance of the expressions does not supply that equation.

Name the target set and a corresponding operation for each source operation, including the value of each constant. Every required target operation must be defined on the inputs it receives. This pattern's total-operation construction does not supply a partial operation's domain.

For a word construction, state the target composition `star` and its identity `e`. The operation must be associative for unparenthesized words to denote a composition independently of grouping. MATH.1 constructs the source words or paths; here the task is to build their map into the target structure.

For typed paths, assign each source object X a target object F(X). The target must supply arrows, associative composition on matching endpoints, and an identity at each object. Assign each generator `a:X -> Y` an arrow `a_target:F(X) -> F(Y)`. A target can consist of sets and functions; different source objects may then receive sets of different kinds of values. Check these domains before composing.

#### MATH.5:4.2 - Extend the assignment recursively

Assign a target value `a(x)` to every generator `x`. Define the evaluation `E` on finite expressions:

- a generator `x` receives `a(x)`;
- a constant receives its named target value;
- `op(t1,...,tn)` receives `op_target(E(t1),...,E(tn))`.

Each recursive call uses a constituent expression. MATH.4 supplies the finite-construction argument and the treatment of a result that needs additional information.

For a word `[x1,...,xk]`, the same move evaluates the assigned generator values in order. The empty word receives `e`; extending a word by `x` changes its value from `v` to `v star a(x)`. Associativity and the identity laws make this evaluation preserve concatenation:

`E(p;q)=E(p) star E(q)`.

For a typed path, set `E(id_X)=id_F(X)`. If `p:X -> Y` has been evaluated and `a:Y -> Z` is the next generator, set `E(p;a)=E(p) star a_target`, where `star` is again read in execution order. The intermediate object F(Y) makes this composition defined. Recursing by path length evaluates every finite path while keeping its endpoints. In a target of sets and functions, this means applying E(p) first and a_target second.

The image of a composite is now computed from its parts. It is no longer an independently chosen entry in a correspondence table.

#### MATH.5:4.3 - Establish preservation and uniqueness

For freely formed expressions, preservation follows from the defining clause: evaluating an operation on expressions gives the target operation on their evaluations. The generator and constant clauses cover the starting cases.

Suppose another operation-preserving map `H` has the same assigned generator values. It agrees with `E` on generators and constants. If it agrees on the constituents of an expression, preservation forces agreement on the whole expression. Induction therefore gives `H(t)=E(t)` for every expression.

The conclusion is uniqueness among maps preserving the named operations and agreeing with the given assignment. Changing the assignment or required operations changes that question.

For words, the corresponding argument starts with the empty word and extends by one generator. Every concatenation-preserving map with the same identity and generator images must return the same ordered product.

For paths, the base case uses the identity at each F(X). Induction on the second path's length, using target associativity, gives `E(p;q)=E(p) star E(q)` for every permitted join. A map preserving identities and composition with the same object and generator assignments must follow those recursive clauses, so it is unique. Such an object-and-arrow map between categories is called a functor. The one-object word construction is its monoid case.

#### MATH.5:4.4 - Make the map respect identified expressions

If the source equates expressions, test the equations under `E`. To define `E_bar([t])=E(t)` on an equivalence class, require:

`t~u implies E(t)=E(u)`.

MATH.2 supplies the quotient and representative-independence construction. Here it is applied to the evaluation just obtained.

For typed paths with the objects retained, impose equations between paths having the same source and target. Compare their target arrows, including the appropriate identity for an empty path. Closure under permitted composition makes the evaluation descend just as above. Identifying different source objects changes this setup and requires a construction that also accounts for their identities and permitted joins.

When the source equivalence is generated by stated equations and their use inside larger expressions, show that each generating equation has equal evaluated sides. Equality is preserved when equal values enter the same target operation. It is also preserved along reversal and a finite sequence of equation replacements. These facts extend the result to the generated equivalence.

An equation schema such as `s*t=t*s` ranges over its permitted substitutions. Checking one numerical substitution leaves the other instances unresolved. Establish the target law for the required range or return a failing instance. If the source also has additional identifications, include them in the comparison.

A failed equation gives a concrete choice: change the generator assignment, change the target operations, or use a source construction that retains the distinction. Each option changes the mathematical account. Select the one that still answers the receiving question.

#### MATH.5:4.5 - Use the map and inspect what it forgets

Evaluate the needed expression or pass the reusable map to its consumer. The preservation argument permits calculation by parts and supports substitution of an equivalent source expression.

Equal target values can still come from different source objects. If the receiver needs to recover a source object, obtain an inverse, a retained representative, or another construction that supplies it. A homomorphism by itself does not provide such recovery.

After a changed generator value, reuse the recursive definition and preservation proof for freely formed expressions. Recheck any imposed equation whose evaluated sides can change. After a changed target operation, revisit the clauses and laws that used it.

Stop with the needed value, the reusable homomorphism, or an equation that prevents the proposed extension. A mathematical map can then contribute to FPF C.29's interpretation-and-return method when the receiving question concerns another subject.

### MATH.5:5 - Archetypal Grounding

#### MATH.5:5.1 - Evaluate expressions, then test an equation

Build expressions from `x,y,0,1,+,*`. Assign `x=2` and `y=3`, and use ordinary integer addition and multiplication. Evaluation returns `E((x*y)+1)=7`. The same rules evaluate every finite expression and preserve its two operations.

Now let the source identify expressions using the usual commutative-semiring laws: associativity, the two identities, commutativity of both operations, distributivity, and multiplication by zero. Integer arithmetic satisfies those laws, so evaluation also defines a map from the identified expressions.

Change the assignment to matrices:

`A=[[0,1],[0,0]]`, `B=[[0,0],[1,0]]`.

Use matrix addition and multiplication, the zero matrix and identity matrix. This still evaluates freely formed expressions. But:

`A*B=[[1,0],[0,0]]`

`B*A=[[0,0],[0,1]]`.

The source's equation `x*y=y*x` therefore fails under this assignment. A substitution into the commutative quotient would give two answers for one source element.

If ordered multiplication is needed, use expressions whose equations retain its order. Matrix addition, multiplication, zero and identity support the remaining semiring laws. If commutative multiplication is essential to the original question, retain a target and assignment that satisfy it instead. The failed equation identifies the mathematical change required.

#### MATH.5:5.2 - Calculate the combined effect of a word of operations

Let a word contain commands `I` and `D`. Their mathematical effects on an integer are:

`I(x)=x+1`, `D(x)=2*x`.

Represent an affine transformation `x -> s*x+t` by the pair `(s,t)`. Thus `I` receives `(1,1)` and `D` receives `(2,0)`.

For `(s,t)` followed by `(u,v)`, define:

`(s,t) star (u,v)=(u*s,u*t+v)`.

Substitution derives this rule: `u*(s*x+t)+v=(u*s)*x+(u*t+v)`. The identity is `(1,0)`. For a third pair `(w,z)`, either grouping gives `(w*u*s,w*u*t+w*v+z)`, so the rule is associative.

Extend the two generator assignments to words. Then:

- `I;D` receives `(2,2)`, meaning `x -> 2*x+2`;
- `D;I` receives `(2,1)`, meaning `x -> 2*x+1`;
- `I;D;I` receives `(2,3)`, meaning `x -> 2*x+3`.

The third word sends 10 to 23. The pair describes its effect for every integer, allowing it to be composed with another affine operation without expanding the whole word again.

A different map can send each generator to cost 1 and concatenate by addition. It gives both `I;D` and `D;I` the value 2. This is a valid cost homomorphism but loses their different effects. Requiring the source equation `I;D=D;I` would preserve that cost map while preventing the stated effect map. The receiving question decides which distinction must remain.

If a command's availability depends on intermediate state, the all-words construction is no longer the intended source. Use state-sensitive paths under MATH.1 and preserve their interfaces when constructing the interpretation.

#### MATH.5:5.3 - Interpret paths with different kinds of values

Take source objects A and B, with generators `u:A -> B` and `v:B -> A`. Interpret A as the integers and B as pairs of integers. Assign `u_target(n)=(n,0)` and `v_target(n,m)=n`. The empty path at A becomes the identity on integers; the empty path at B becomes the identity on integer pairs.

Extension gives `E(u;v)(n)=n`, whereas `E(v;u)(n,m)=(n,0)`. The first composite therefore equals `E(id_A)`. The second differs from `E(id_B)`: it sends (7,5) to (7,0). The interpretation can descend through the source equation `u;v=id_A`, together with the equations generated from it by permitted composition. It keeps the information that the return path loses the second component.

Now require `v;u=id_B` as well. The same assignment fails that new equation. Keep the free-path interpretation or the first quotient, change the assigned maps, or change the required identification. Both composites are valid paths; the failed assertion concerns their values, not whether they can be formed. This distinction lets a representation carry construction followed by recovery without claiming recovery in both directions.

### MATH.5:6 - Bias-Annotation

Recognizable notation can encourage an unexamined substitution. Matrix multiplication retains order even when the same multiplication sign denotes commutative arithmetic elsewhere. Test the law that the source expression uses.

A compact target value can also be mistaken for a reversible description. The cost example preserves concatenation while merging words with different effects.

Finally, a few successful evaluations can hide an equation schema's range. The reusable extension depends on preservation for every admitted instance of the equations it consumes.

### MATH.5:7 - Conformance Checklist

- For typed paths, do the object assignments, generator endpoints and identities determine the extension, and do imposed equations compare arrows with the same endpoints?

- Are the generators, constants and source operations specified?
- Does each source operation have a defined target operation with the required inputs?
- Do the evaluation clauses determine every finite expression?
- Does the preservation argument cover the named operations and the identity?
- Is any uniqueness claim restricted to maps with the same assignment and preservation requirements?
- If expressions are identified, do their evaluated values agree for every required equation instance?
- Does the returned value retain the information needed by its consumer?
- Does a changed assignment, equation or operation lead to the affected comparison?

### MATH.5:8 - Common Anti-Patterns and How to Avoid Them

**Assign unrelated values to composites.** Define their values through the target operations. Otherwise the map can fail the very composition it is intended to represent.

**Carry commutative arithmetic into ordered operations.** The matrix and command cases supply counterexamples. Keep the source order or justify the commutativity required by the quotient.

**Check one instance of a general equation.** Recover its substitution range. Establish the law there or return a failing instance.

**Infer reversibility from operation preservation.** The cost map returns the same value for different effects. Retain a suitable source representative or construct the additional inverse needed for the question.

**Drop a composition precondition.** An unavailable word is not repaired by assigning it a numerical image. Use a source that represents permitted joins.

### MATH.5:9 - Consequences

A small assignment determines a map over arbitrarily large finite constructions. Its evaluation rule supports calculation, substitution and comparison of composite effects. A failed equation can locate the required change before the entire map is used.

The map may deliberately discard distinctions. Preserving operations and recovering original objects are separate results. Equality checks on complicated presentations can remain difficult even when the recursive evaluation itself is simple.

### MATH.5:10 - Architectural Rationale

The method connects three mathematical contributions: recursive construction, preservation of operations, and compatibility with imposed equations. Their combination answers a different question from constructing the source objects alone: how a chosen interpretation extends across that whole source.

The free-expression step makes evaluation and uniqueness accessible. The quotient step then exposes the obligations introduced by an identification. Keeping them separate lets a failed equation leave the valid free-expression map available.

For one small expression, direct evaluation can be sufficient. The general construction earns its cost when many expressions, substitutions or a reusable representation are needed. A ready homomorphism can supply the same result without reconstructing its proof.

The affine-pair case gives the same composition a second mathematical description. Its equation connects the descriptions.

### MATH.5:11 - SoTA-Echoing

**Question:** how can a generator assignment determine an operation-preserving map, including when the source equates different constructions?

Burris and Sankappanavar's [*A Course in Universal Algebra*, corrected 2012 edition](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), II §10, definitions 10.1-10.5, lemma 10.6 and theorem 10.8, supplies term formation, recursive evaluation and unique extension. **Adopt** that construction. The examples apply it to arithmetic expressions and composed affine transformations. The pattern's quotient step uses the congruence construction supplied by MATH.2 and gives its preservation argument.

The [Mathlib free-monoid implementation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/FreeMonoid/Basic.html#FreeMonoid.lift) gives an executable formalization of the word case. `FreeMonoid.lift` extends generator values by the product of their images; `hom_eq` states uniqueness from generator agreement. **Adapt** that presentation into ordinary mathematical instructions, retaining the monoid premises.

The [Mathlib path-category construction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/PathCategory/Basic.html#CategoryTheory.Paths.lift) formalizes the typed branch: `Paths.lift` extends an object-and-generator assignment; `lift_nil`, `lift_cons` and `lift_unique` establish the identity, recursive composition and uniqueness clauses. The pattern spells out those operations for use after MATH.1. The integer/pair case derives a consequence and a failed additional equation directly from its assigned functions.

The useful comparison is with a supplied map or independent evaluation of a small number of expressions. Extension by generators improves repeated compositional use, while an imposed equation adds a real preservation obligation. Reopen when a partial operation has a domain beyond the path-endpoint construction supplied here, the source admits infinite constructions, an equation fails, or a simpler available map supplies the receiving result.

### MATH.5:12 - Relations

- **Uses MATH.1 where the source is a path construction:** assign images to its objects and generators, then extend to its identities and permitted composites.
- **Uses MATH.4:** construct the evaluation on finite expressions and prove its recursive clauses and uniqueness.
- **Uses MATH.2 when equations identify expressions:** obtain representative-independent evaluation on the quotient.
- **Connects with FPF C.29:** use the mathematical map in a subject correspondence and recover the result needed there.
- **Connects with Method Engineering:** a mathematical account of composed methods can use the affine-effect construction; ME.7 develops the proposed composition account; ME.12 checks its claims and returns a correction to the description or construction that needs it.

### MATH.5:End

## MATH.7 - Transport a Mathematical Structure Through a Bijection

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.7:1 - Problem frame

Use this pattern when another representation makes a mathematical construction easier to work with and you need to carry its operations and results across a reversible map. You may want to calculate with coordinates, encode sets by bit vectors, or give a familiar carrier a different algebraic structure.

A *bijection* pairs every element of one set with one element of another and has an inverse in both directions. It can be used to define operations and relations on the receiving set. With those definitions, the map becomes an *isomorphism* of the chosen structures: it preserves their operations and reflects their relations.

Start with one needed operation and one input. Recover the input in the source, perform the source operation, and map its result back. Return the resulting operation and its domain, or the part of the proposed correspondence that cannot be reversed.

The reader needs functions, composition, inverse functions and elementary algebra. The main construction covers operations with finitely many inputs, constants and relations on sets. The worked coordinate example also uses squared Euclidean length. If the map and the needed preservation result are already available, use them. A one-way representation or a summary that deliberately forgets distinctions can instead use MATH.2, MATH.5 and FPF C.29.1 for the result it preserves.

### MATH.7:2 - Problem

Changing the names or coordinates of elements leaves the receiving operations undecided. Reusing the familiar operation on the new labels can produce a different result. Even when one operation survives unchanged, another quantity or relation may require a different formula.

The task is to construct the receiving structure, establish what it preserves, and use that preservation to calculate or solve a problem. If the receiver already requires particular operations, the transported construction must be compared with them.

### MATH.7:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar carrier and chosen structure | The same set can carry several operations with different identities and laws. |
| Reversible elements and preserved work | Recovering elements supplies the means to transport operations; it does not choose which operations matter. |
| One convenient representation and several quantities | A change can simplify one calculation while complicating another. |
| Reusable proof and computing cost | Transport can reuse an algebraic argument, while repeated encoding and decoding can make a calculation expensive. |

### MATH.7:4 - Solution

**Choose the structure to carry → establish both inverse equations → transport operations and relations → derive the retained laws → calculate and return the result.**

#### MATH.7:4.1 - Choose the source structure and the receiving use

Name the source set X and the operations, constants or relations needed by the question. For an additive structure these might be addition, zero and negation. For an ordered structure the comparison relation matters too. Include a quantity such as length when the requested conclusion depends on it.

Name the receiving set Y and distinguish two tasks: constructing its operations, or showing that operations already required there correspond to the source. In the second task, retain those required operations for the comparison. Replacing them with different transported operations changes the proposed mathematical structure.

For a single update, C.29.1's correspondence comparison can be sufficient. Use the construction below when you need the related operations, their laws, a reusable representation or a way to move solutions between the two structures.

#### MATH.7:4.2 - Establish the reversible map on its declared sets

Give `h:X→Y` and `r:Y→X` and establish both equations:

`r(h(x))=x` for every `x` in X;

`h(r(y))=y` for every `y` in Y.

They establish that r is the inverse of h. A formula, a complete finite table or an existing applicable result can supply the maps and these equations.

If h only covers part of the proposed Y, you can take its image `h(X)` as the receiving set when that answers the question. If h combines distinct source elements, returning the whole original element requires more information or a different map. A quotient may still retain the requested operation under MATH.2. MATH.6's left-inverse examples show why recovery in one direction alone leaves the other direction open.

Keep restrictions in the sets. For example, squaring is reversible from nonnegative real numbers to nonnegative real numbers, with the nonnegative square root as inverse. Squaring on all real numbers combines opposite inputs and cannot support that inverse construction for the whole source.

#### MATH.7:4.3 - Define the receiving operations and relations

For a source operation `op_X:X^n→X`, define:

`op_Y(y1,...,yn)=h(op_X(r(y1),...,r(yn)))`.

In words: decode each input, perform the source operation, then encode the output. Constants have no inputs, so a source constant c becomes `h(c)`. A source relation R becomes:

`R_Y(y1,...,yn)` holds exactly when `R_X(r(y1),...,r(yn))` holds.

The construction can have different input and output sets. For `op:X1×...×Xn→Z`, use a bijection `h_i:Xi→Yi` for each input and `k:Z→W` for the output. Then:

`op_target(y1,...,yn)=k(op(h_1^-1(y1),...,h_n^-1(yn)))`.

An unchanged scalar result uses the identity map on that scalar set. Thus transporting a length calculation changes its input coordinates while retaining the numerical length.

For a partial source operation, transport its domain too. The receiving tuple is allowed precisely when its decoded tuple is in the source domain; define its output there by the same formula. A larger independently supplied receiving domain needs its own comparison before its extra inputs are used.

Calculate one small case in both descriptions. Use it to check the direction of the maps, the constants and the operation being performed. The general preservation result comes from the defining formula and inverse equations.

#### MATH.7:4.4 - Derive the laws that the chosen structure retains

For each operation, substituting `h(x_i)` into its definition and cancelling `r(h(x_i))` gives:

`op_Y(h(x1),...,h(xn))=h(op_X(x1,...,xn))`.

Any other receiving operation with this equality must coincide with the constructed one: every receiving input has the form `h(x_i)`. Thus the source operation and h determine the transported operation uniquely on Y.

To carry an equation built from these operations, follow its expressions from the variables and constants through each operation. Variables are mapped by h, constants by their specified images, and the displayed equality carries each composite expression. This is an induction on the expression's construction; MATH.4 supplies that form of argument.

For expressions s and t in one carrier, it yields:

`s_Y(h(x1),...)=h(s_X(x1,...))` and `t_Y(h(x1),...)=h(t_X(x1,...))`.

An equality of the source expressions therefore gives equality of the receiving expressions. Conversely, h is injective, so equality of those receiving values gives equality of the source values. Surjectivity covers all assignments in Y. The same reasoning with the map for each sort treats operations with different input and output sets.

This transfers equational laws such as associativity, an identity law or distributivity for the operations actually carried. A further order, distance or other relation must use its own transported definition or an established compatibility result. For partial operations, compare the definedness of the compound expressions as well as their values.

#### MATH.7:4.5 - Calculate in the useful representation and recover the answer

Translate the inputs, constants and requested relation. Calculate or solve the corresponding problem using the receiving operations. Map the result back with the inverse appropriate to its kind.

For example, a source equation `t_X(x)=b` becomes `t_Y(y)=h(b)`, where `y=h(x)` and all other parameters in t are translated too. A receiving solution y returns `x=r(y)`. The correspondence gives both directions, so it also carries absence or uniqueness of a solution when the equations range over the declared sets.

Use a simpler formula for a transported operation after establishing equality with its defining formula. This can avoid repeated encoding and decoding. Compare the resulting calculation effort with direct source calculation when the representation is being chosen for efficiency. Preservation alone establishes no speed advantage.

If Y already had a required operation, compare it with the constructed one before transferring its laws or solutions. A disagreement can lead to a changed map, a different receiving structure, or continued use of the original description.

#### MATH.7:4.6 - Revisit only what the changed question uses

When h changes, derive the affected receiving operations and constants again. When the question adds a quantity or relation, construct its receiving form even if the earlier operations are unchanged. When a domain restriction changes, revisit both inverse equations and the allowed operation inputs.

Return a failed equation or two source cases that the map cannot distinguish through MATH.6 or MATH.2 as appropriate. Use C.29 when the mathematical representation is being related to another subject. Stop with the needed calculation, reusable transported structure, or identified obstruction.

### MATH.7:5 - Archetypal Grounding

#### MATH.7:5.1 - Shifted numbers with a shifted addition law

Start with real numbers under addition. Let `h(x)=x+1` and `r(y)=y-1`. Both inverse equations hold on all real numbers. The transported addition is:

`u ⊕ v=h(r(u)+r(v))=u+v-1`.

The source zero becomes `h(0)=1`, and source negation becomes `neg_Y(u)=h(-r(u))=2-u`. Thus `u⊕1=u` and `u⊕(2-u)=1`. Associativity follows directly because both groupings of three inputs give `u+v+w-2`; it also follows from the general transport argument.

To solve `x+3=7`, translate it as `y⊕4=8`. The receiving equation gives `y=5`, and decoding gives `x=4`. Using ordinary addition on the new labels would instead solve `y+4=8` and return `x=3`, which fails the original equation.

The transported operation is useful as a representation of the source addition. If ordinary addition on Y is part of the receiving requirement, this h does not preserve that requirement; the construction has exposed a different operation.

The same map can transport real division, defined when the source denominator is nonzero. Its receiving formula is `u⊘v=(u-1)/(v-1)+1`, with domain `v≠1`. The label 1 decodes to the forbidden denominator zero; the label 0 decodes to the allowed denominator −1. For example, `3⊘0=-1` decodes to −2, the result of the source calculation `2/(-1)`. Using the familiar restriction `v≠0` would exclude an allowed input and admit a forbidden one.

#### MATH.7:5.2 - Sets represented by bit vectors

Let X be the subsets of `{a,b,c}`. Map a subset to its membership vector in `{0,1}^3`; for example, `{a,c}` maps to `(1,0,1)`. Decode by selecting the positions marked 1. These maps are inverse on all eight subsets and all eight vectors.

Take symmetric difference as the source operation: an element belongs to `S△T` when it belongs to exactly one of S and T. Its transported operation is coordinatewise XOR, whose output bit is 1 exactly when the two input bits differ. The empty set becomes `(0,0,0)`.

For `S={a,c}` and `T={b,c}`, symmetric difference gives `{a,b}`. In coordinates:

`(1,0,1) XOR (0,1,1) = (1,1,0)`.

Decoding returns `{a,b}`. This gives a way to perform the set operation in a binary representation and recover its result. The inverse map and operation formula explain why the method works for every subset pair; the eight-by-eight table is a finite check if needed.

If the next question asks for union instead, derive its operation: coordinatewise OR. Reusing XOR would discard an element present in both inputs. The same bijection supports both operations once each is defined.

#### MATH.7:5.3 - Addition survives a coordinate change while length needs a new formula

In `X=R^2`, let `h(x,y)=(x+y,y)`. Its inverse is `r(u,v)=(u-v,v)`. Transported vector addition coincides with ordinary coordinatewise addition because h is linear.

Now ask for squared Euclidean length, `L_X(x,y)=x^2+y^2`. The result is a real number whose interpretation stays unchanged, so its output map is the identity. The transported quantity is:

`L_Y(u,v)=(u-v)^2+v^2`.

The source vector `(0,1)` has squared length 1 and maps to `(1,1)`. The transported formula still returns 1. The familiar formula `u^2+v^2` would return 2.

A length bound `L_X(x,y)≤1` consequently becomes `(u-v)^2+v^2≤1`. It does not become `u^2+v^2≤1` through this coordinate map. The example separates an unchanged operation from a quantity whose receiving formula must be constructed. A later physical interpretation of these coordinates uses C.29 for its subject correspondence.

### MATH.7:6 - Bias-Annotation

Bijections give a particularly strong form of transfer: full recovery on the declared sets. Many useful summaries and approximate models intentionally retain less information. They can still answer a specific question through a different correspondence method. The elementary examples also make the maps cheap to calculate; a complicated inverse may remove the computational benefit of a representation while leaving its mathematical validity intact.

### MATH.7:7 - Conformance Checklist

- The receiving question determines the operations, constants and relations to carry.
- Both inverse equations hold on the sets used by the result.
- Each receiving operation uses the appropriate input and output maps, including transported domains for partial operations.
- The claimed laws concern the transported structure or operations shown to coincide with it.
- The calculation translates its parameters and returns a result of the required kind.

### MATH.7:8 - Common Anti-Patterns and How to Avoid Them

**Change the labels and retain an incompatible operation.** In :5.1 ordinary addition on the new labels solves a different equation. Construct the receiving operation and compare any required incumbent.

**Recover source elements and assume every target element is covered.** Establish the second inverse equation or restrict the target to the image, as :4.2 requires.

**Transfer every property after checking one operation.** The coordinate example preserves addition while squared length needs another formula. Include the quantity or relation used by the requested result.

**Choose a familiar operation for a new question.** The bit-vector example needs OR for union and XOR for symmetric difference. Translate the operation the question actually asks for.

### MATH.7:9 - Consequences

A reversible correspondence becomes a constructive way to obtain operations, laws and solutions in another representation. The same carrier can support a newly useful structure, and the proof of preservation can be reused across many calculations.

The benefit can be a clearer expression, an easier proof or a cheaper computation. These benefits can differ. More than one representation may remain useful for different parts of the work.

### MATH.7:10 - Architectural Rationale

Encoding the result of a decoded operation determines the structure that the bijection preserves. Uniqueness prevents an independent choice of a familiar operation from being silently treated as the same construction. The expression-induction argument then explains why equations and their solutions travel.

C.29.1 already gives the common correspondence method and conjugation of a single update. This pattern develops the mathematical structure construction: constants, operations of several arities, relations, their laws and solution return. A single-update use can stay with C.29.1. MATH.5 starts instead with generator images and builds a homomorphism, which may forget information; here a supplied reversible map determines the receiving operations.

Transport is preferable when an available source structure and a useful bijection save construction or reasoning work. Direct definitions can be simpler or faster. A pre-existing isomorphism can supply the result without repeating the derivation. These alternatives retain the question that the representation is meant to answer.

### MATH.7:11 - SoTA-Echoing

**Question:** how can a reversible map supply a usable mathematical structure and carry its calculations?

Burris and Sankappanavar's [*A Course in Universal Algebra*, corrected 2012 edition](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), II §2, definition 2.1, states algebraic isomorphism through a bijection and operation preservation. **Adopt** that mathematical relation. The pattern makes the receiving operations constructive and gives an expression-based argument for the transferred equations.

The maintained [Mathlib algebraic-structure transfer definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/TransferInstance.html) implement transport of constants, operations and their laws through an equivalence. **Adapt** this as the general construction here. Its library note also identifies an implementation cost from repeated unfolding; mathematical equivalence does not choose the most efficient computational representation. The [module-transfer construction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/TransferInstance.html) further illustrates retention of a fixed scalar domain while carrying vector structure.

A direct definition or an existing isomorphism can provide the same result with less work. Transport earns its cost when the correspondence and reusable law matter. Reopen when the inverse, the selected operations, or the required result domain changes.

### MATH.7:12 - Relations

- **Uses MATH.4:** extend preservation through finite expression construction.
- **Connects with MATH.5:** distinguish extending generator images from constructing structure through an already reversible map.
- **Returns to MATH.2 when the representation combines elements:** construct the quotient and determine the retained operation.
- **Uses MATH.6 for a failed preservation claim:** exhibit the incompatible input or missing inverse direction.
- **Specializes the mathematical construction used by C.29.1:** construct operations, relations and laws through a bijection. Use C.29 for their interpretation in another subject.
- **Connects with A.6.3.RT.OE:** use the available expression rules to make the transported calculation operable; invention of a notation language is a further notational method.

### MATH.7:End

## MATH.18 - Compare Mathematical Accounts through Interpretations

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.18:1 - Problem frame

Use this pattern when two mathematical descriptions appear to address the same construction or question but use different objects, primitive operations, relations or notions of equality. You need to know which calculations, arguments or changes can be carried from one description to the other.

Begin with one consequence you want to transfer. It may be a constructed object, an equation, a solution, or a way of composing operations. An interpretation of that consequence, with its supporting construction or a reason it fails, is the first useful result. A broader equivalence claim requires correspondingly broader comparison.

A **mathematical account** here consists of the objects, operations, relations and assumptions used to describe the question. An **interpretation** specifies how to read those ingredients through another account and establishes the consequences needed for the proposed use. The main route requires functions, elementary algebra and reasoning with “for every” and “there exists”. It explains the order and algebra used in the first worked case. The vector-and-matrix case is an optional branch requiring elementary linear algebra.

If a supplied bijection and its transported operations already settle the change of representation, use MATH.7. Use the present method when primitives must be reconstructed, only part of an account transfers, or the round trip needs a structural comparison rather than literal equality.

### MATH.18:2 - Problem

Matching names or formulas can conceal different allowed objects, operations or solutions. Two descriptions may recover the same objects while allowing different transformations between them. A translation may preserve calculations for the translated inputs while a target quantifier ranges over additional objects and changes the answer.

The task is to construct the interpretation, determine the scope of the resulting agreement, and use it to transfer a consequence or locate the distinction that prevents transfer.

### MATH.18:3 - Forces

| Force | Tension |
| --- | --- |
| Different primitives and recoverable structure | An operation in one account may be definable through a relation in another, but its existence and uniqueness need an argument. |
| Object correspondence and allowed maps | Matching objects leaves open whether the accounts permit the same transformations of them. |
| Useful one-way translation and equivalence | An interpretation may carry the needed result without supporting a reverse interpretation or a broader equivalence. |
| Comparison scope and effort | A local consequence may need only a short argument; comparing entire theories requires their logical and structural conditions. |

### MATH.18:4 - Solution

**Local mantra:** choose the consequence; interpret the ingredients; derive what transfers; compare the round trips; use the agreement or its failure.

#### MATH.18:4.1 - Set the scope of the comparison

Name the source account, target account and intended use. Identify the objects involved, their operations and relations, and what counts as an answer. If transformations between objects matter, include those transformations in the comparison.

For each ingredient that the intended consequence uses, ask how the target will express it. Keep optional additional structure separate. For example, an additive operation, an order and a distance support different questions even when carried by the same underlying set.

Decide the strength of the needed conclusion. Transferring one equation, constructing a solution, comparing all compositions in a selected family, and establishing equivalence of two presentations are different claims. Inspect the ingredients and reasoning needed for that claim. Expand the comparison when the next use expands it.

#### MATH.18:4.2 - Construct the interpretation

Specify the source objects' target counterparts and the operations or relations that interpret each required primitive. Give a construction rather than a matching name. If an operation is to be recovered through a defining condition, establish that a result exists and is determined to the degree required by the source.

Respect the domains and arities. A binary operation needs two admitted inputs; a relation needs the participants on which it is asserted. When the source uses equivalence classes, establish that different representatives give equivalent interpreted results. MATH.2 supplies the detailed quotient test.

Extend the interpretation through constructed expressions. Interpret each input, then interpret the operation applied to those inputs. A composite expression is handled by repeating this rule through its construction. MATH.5 develops the extension from generators when the source is presented that way.

An assertion also has a construction. Translate equality, conditions and quantifier ranges. For `there exists x in A with P(x)`, the target must express both the interpreted domain A and the interpreted condition P. Enlarging that range can admit a solution that the original problem excludes; :5.2 works this failure.

When an interpretation uses a basis, representative or another choice, supply it or a means of obtaining it. Determine whether changing the choice changes the result, or only changes a representation with a known comparison.

#### MATH.18:4.3 - Establish what the interpretation preserves and reflects

For the consequence being transferred, follow its construction or argument through the interpretation. Establish that the required operations remain applicable and that each used equality or relation remains valid.

Distinguish the two directions. Preservation takes a source consequence to a target consequence. Reflection takes an interpreted target consequence back to the source. To use a target calculation as the source answer, obtain the required recovery and reflection argument.

For operations composed as maps, an object assignment F also assigns `F(f):F(A) -> F(B)` to each source map `f:A -> B`. To translate a sequence stage by stage, establish:

`F(g∘f)=F(g)∘F(f)` and `F(id_A)=id_F(A)`.

Such an assignment is a functor. Fix source objects A and B. To recover maps, determine which target maps `F(A) -> F(B)` have counterparts `A -> B`. To recover an equality, take two source maps `f,g:A -> B` and determine whether `F(f)=F(g)` implies `f=g`. The equality test concerns maps with these same endpoints. Recovery of the objects themselves is a further question, handled in :4.4.

**Formal-theory branch.** When the intended result is transport of theorems, give the translation of the relevant syntax and logic. Establish the interpreted axioms and justify the inference rules used by the theorem. Comparing collections of models through maps supplies a different mathematical result until its connection to this theorem-translation claim is established.

A failed preservation or reflection equation is useful. Work its inputs far enough to show what answer or construction changes. Then restrict the claim, enrich the interpretation or keep the accounts distinct for that purpose.

#### MATH.18:4.4 - Construct the return and examine the composites

When two-way use is needed, construct a return interpretation G. Apply `G∘F` to source ingredients and `F∘G` to target ingredients. Inspect what each round trip returns.

Sometimes the ingredients are recovered literally, as in the order-and-operation case below. Sometimes a specified isomorphism supplies recovery: an invertible map preserving the structure used by the comparison.

When whole systems of objects and maps are compared, pointwise isomorphisms need compatibility with the maps. If `eta_A:A -> G(F(A))` provides source recovery, require for every source map `f:A -> B`:

`G(F(f))∘eta_A = eta_B∘f`.

Both routes start in A and finish in `G(F(B))`. This equation means that translating and then applying the map agrees with applying the map and then translating. Require the corresponding compatibility on the target side as well. In categorical language, functors with these natural isomorphisms give an equivalence of categories.

Use that equivalence for properties supported by the chosen structure and invariant under its isomorphisms. If a later question uses additional structure, include it in the comparison. The length question in :5.3 shows why this return matters.

If only one direction is constructed or needed, retain that useful interpretation at its established scope. If two-way recovery fails, name the unrecovered operation, assertion or distinction that matters to the work.

#### MATH.18:4.5 - Transfer the result and reopen only the changed demand

Carry the intended calculation, construction or argument into the receiving account and recover its answer where required. State the conditions that make the transfer usable. A receiver needs the interpretation and relevant consequence; an equivalence label alone leaves the work to be reconstructed.

A changed primitive, quantifier range or allowed-map class can change the comparison. Revisit the affected construction and its argument. Keep conclusions whose ingredients and conditions are unchanged.

For mathematical work, the result may be an equivalence at the selected scope, a useful one-way interpretation or a separating consequence. For a computational or working-method application, C.29 and C.29.2 supply the further correspondence and execution questions. Mathematical agreement can then inform the application through those explicit connections.

### MATH.18:5 - Archetypal Grounding

#### MATH.18:5.1 - Recover an order from an operation, then compare allowed maps

One account starts with a set S and a binary operation `a∨b` satisfying associativity, commutativity and idempotence:

`(a∨b)∨c=a∨(b∨c)`; `a∨b=b∨a`; `a∨a=a`.

Another starts with a partial order in which every pair has a least upper bound. An upper bound of a and b is an element z with `a<=z` and `b<=z`. The least upper bound lies below every such z. Antisymmetry makes it unique. We want to move constructions between these descriptions.

From the operation, define `a<=b` to mean `a∨b=b`. Idempotence gives reflexivity. If `a∨b=b` and `b∨a=a`, commutativity gives a=b, establishing antisymmetry. If `a∨b=b` and `b∨c=c`, associativity gives:

`a∨c=a∨(b∨c)=(a∨b)∨c=b∨c=c`.

Thus the relation is transitive. Also `a∨b` is an upper bound of a and b. If z is any upper bound, then `(a∨b)∨z=a∨(b∨z)=a∨z=z`. So `a∨b<=z` and the original operation supplies the least upper bound.

Conversely, define `a∨b` to be the least upper bound in the ordered account. Uniqueness makes the operation commutative and idempotent. Both `(a∨b)∨c` and `a∨(b∨c)` are the least upper bound of the same three elements, giving associativity.

The round trips recover both primitives. Starting from the operation returns it as the least upper bound just proved. Starting from the order returns it because `a<=b` holds exactly when b is the least upper bound of a and b.

Now the intended use expands: can every order-preserving map be used as a map preserving the binary operation? A join-preserving map is monotone: apply it to `a∨b=b`. The converse fails. Take subsets of `{u,v}` ordered by inclusion, with union as join, and target `{0,1}` with its usual order. Define h to return 1 only on the full set and 0 on all other subsets. It is monotone, yet:

`h({u} union {v})=1`, while `max(h({u}),h({v}))=0`.

For constructions that combine joins, select join-preserving maps in both accounts. If all monotone maps are needed, retain that broader ordered account and its different transformation class. The objects matched; the expanded map claim required and received its own answer.

#### MATH.18:5.2 - An enlarged domain changes the available solution

The natural numbers `N={0,1,2,...}` embed in the integers Z. Inclusion preserves 0, addition and equality of expressions evaluated on natural-number inputs. It also reflects those equalities: two included natural numbers are equal in Z precisely when they were equal in N.

Suppose the next task is to solve `x+1=0`. The integer solution x=-1 is outside N. The interpretation useful for additive calculations therefore has not supplied a natural-number solution.

To express the original existential question in Z, retain its range: “there exists an integer x with `x>=0` and `x+1=0`.” That statement remains false. To use Z as a calculation space for another natural-number equation, compute there and test the recovered candidates against the source domain.

The revised use keeps the beneficial integer calculations and makes their return condition explicit. A demand to identify all natural-number and integer solution questions would instead fail this comparison.

#### MATH.18:5.3 - Compare linear maps with matrices, then add a length question

**Additional structure -- finite-dimensional real vector spaces.** In one account, each space comes with a specified ordered basis, and maps between spaces are all linear maps. In the other, an object is a nonnegative integer n and a map n to m is an `m-by-n` real matrix. Maps compose by matrix multiplication.

For a space V with basis `(b1,...,bn)`, let `c_V:V -> R^n` send a vector to its coefficients in that basis. Interpret `f:V -> W` by the matrix of `c_W∘f∘c_V^(-1)`. Composition agrees because the adjacent coordinate conversion and its inverse cancel. Identity maps become identity matrices.

The return takes n to `R^n` with its standard basis and a matrix to its linear map. The round trip on matrices is literal. The round trip on V returns its coordinate space, with recovery supplied by `c_V`. For each f, the equation `matrix(f)∘c_V=c_W∘f` establishes the required compatibility. This compares the entire selected system of linear maps, including their compositions, rather than only matching vector values.

Now ask for lengths in Euclidean space. With basis `b1=(1,0)`, `b2=(0,2)`, coordinates `(0,1)` represent a vector of length 2; their ordinary coordinate length is 1. The linear comparison did not include the inner product. Carry it as a Gram matrix: here `G=diag(1,4)` and squared length is `c^T*G*c`. Retaining G lets us calculate the same vector's length after changing coordinates.

A different question asks which linear maps preserve lengths. For a map from V to W represented by matrix M, with Gram matrices `G_V` and `G_W`, require `M^T*G_W*M=G_V`. This follows by comparing the squared length `c^T*G_V*c` of every input with `(M*c)^T*G_W*(M*c)` of its output. Use that condition to select the length-preserving maps. The earlier interpretation of arbitrary linear maps remains available when length preservation is not required.

#### MATH.18:5.4 - Recover an operation using a chosen origin

On the integers, one account supplies the ternary operation t(x,y,z)=x-y+z and a marked origin 0. It recovers addition as t(x,0,y) and negation as t(0,x,0). Conversely, addition and negation recover t. Substitution verifies both returns for every integer input.

Now remove the marked origin. Choosing any integer c gives an addition x+_c y=t(x,c,y)=x-c+y, identity c and inverse 2c-x. Combining these operations again gives the same t(x,y,z). The ternary operation alone therefore permits several choices of origin and corresponding binary operations.

For example, c=0 makes the sum of 2 and 3 equal 5; c=1 makes it equal 4 under +_1. Both choices recover the original ternary operation. A question using only t can continue without selecting an origin; recovering the former addition needs its marked origin again. This distinguishes a usable one-way interpretation from a return that silently supplies extra structure.

### MATH.18:6 - Bias-Annotation

Familiar terminology can encourage an equivalence claim before the allowed operations and quantifiers have been compared. Follow one consequential construction through both accounts, then enlarge the claim only as far as its arguments support.

The categorical branch is useful when objects and maps are already the subject of comparison. Algebraic definitions, order relations and explicit logical translations can provide more direct constructions for other questions. Select the form that makes the required transfer inspectable.

### MATH.18:7 - Conformance Checklist

For the comparison being used:

- The source, target, intended consequence and claimed scope are recoverable.
- Each required primitive has a constructed interpretation with its domain and assumptions.
- Needed preservation, reflection and recovery claims have arguments at that scope.
- Two-way claims inspect both composites and the compatibility required by the allowed operations.
- A failed claim identifies a changed answer or unavailable construction and determines the retained use or repair.
- The receiver can perform the intended transfer with the supplied result and conditions.

### MATH.18:8 - Common Anti-Patterns and How to Avoid Them

**Matching objects while silently widening maps.** The order-and-join comparison recovers the objects, but its operation-preserving maps form a narrower class than all monotone maps. Select the class required by the next construction.

**Solving the translated equation in an enlarged domain.** The integer solution in :5.2 fails the original domain condition. Translate the quantifier range and check the return of any computed candidate.

**Using an equivalence for added structure.** The linear comparison in :5.3 supports linear operations. A length question adds an inner product and the obligation to carry it through the coordinate change.

### MATH.18:9 - Consequences

Different mathematical descriptions can become usable alternatives with known transfers and returns. The comparison can also expose a useful one-way interpretation or a distinction that a proposed equivalence would erase.

The cost follows the scope. Recovering one primitive may settle a local use; comparing whole families of constructions requires their maps and compatibility laws. A changed task can reuse earlier results while reopening the additional structure it now needs.

### MATH.18:10 - Architectural Rationale

Organizing the method around a consequence keeps interpretation connected to mathematical work. Comparing objects, assertions and transformations prevents an object-level match from silently becoming a claim about every use.

The operation-and-order case reconstructs different primitives on the same carrier. The natural-number case exposes domain-sensitive assertion transport. The matrix case compares families of objects through compatible isomorphisms. Together they show different uses of one method without making any one mathematical branch its scope.

MATH.5 and MATH.7 remain direct construction methods for generator extension and bijective transport. This pattern supplies the wider comparison in which those methods may solve one part. MATH.17 supplies operations on operations when the interpretation itself must be constructed or transformed that way.

### MATH.18:11 - SoTA-Echoing

Fong and Spivak's [Seven Sketches in Compositionality](https://arxiv.org/abs/1803.05316), §§1.2-1.3, develops order, joins and what their maps preserve. The adopted contribution is to compare an observation or transformation by the operations it carries, including the ones it loses. The order-and-operation construction here makes that question usable when the accounts start from different primitives.

Riehl's [Category Theory in Context](https://emilyriehl.github.io/files/context.pdf), §1.5, supplies equivalence through functors and compatible isomorphisms. It supports the family-level comparison. A claim about translated theorems additionally depends on the chosen logic and interpretation.

For a prepared change of coordinates, explicit inverse maps can be enough. A broader account comparison becomes useful when available operations, assumptions or quantifiers differ. The present method combines these alternatives according to the consequence to be transferred.

### MATH.18:12 - Relations

- **MATH.5** constructs the interpretation of generated objects from its values on generators.
- **MATH.7** transports mathematical structure through a supplied bijection.
- **MATH.2** establishes when an interpretation and its operations descend through identification.
- **MATH.16** constructs objects and comparison maps from required uses.
- **MATH.17** constructs operation collections and higher-order transformations, including composition-preserving assignments.
- **MATH.6** constructs a countermodel when an asserted transfer or equivalence fails.
- **B.5.RA and B.5.TU** recover an unfamiliar argument and carry a theoretical consequence into its intended case.
- **C.29 and C.29.2** supply subject correspondence and computational formulation for applications of the mathematical comparison.

### MATH.18:End

# Part B - Construct and criticize arguments

## MATH.19 - Construct a Proof through Intermediate Claims

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.19:1 - Problem frame

Use this pattern when you have a mathematical claim to establish and some relevant definitions or results, but no argument connecting them. A calculation may suggest the answer while leaving its generality unexplained. An induction step may need information that its hypothesis does not provide. A familiar theorem may almost fit, with one missing premise.

Construct intermediate claims that connect what is available to what is required. A **lemma** is an auxiliary proved claim used in another argument. Finding a useful lemma is part of the work: its conclusion must help the next step, and its premises must be obtainable where it is used.

**First useful move:** unfold the wanted conclusion once. Ask what would suffice to establish it, and which available statement or construction could supply that condition. Try to complete this connection on an arbitrary admitted object.

The reader needs elementary mathematical statements, functions and the idea of a proof from assumptions. The worked cases explain their additional notation. The method supports arguments about numbers, functions, structures and mathematical models; each branch retains its own assumptions.

Use a supplied theorem directly when its premises are met and its conclusion answers the question. B.5.RA helps recover an existing unfamiliar argument. MATH.4 develops the inductive construction when induction is the required step; MATH.12 recovers an obtaining procedure from a proof. Here the missing contribution is the proof's construction and organization.

### MATH.19:2 - Problem

Forward calculation can produce true statements without approaching the wanted conclusion. Working backward can produce a useful-looking requirement that is stronger than the available assumptions. Combining the two requires discovering a statement that is both obtainable and sufficient for the next inference.

The difficulty can be hidden in a parameter or an order of composition. A proof for one selected object may be used as if it covered all objects; an auxiliary claim may quietly assume the theorem being proved. A recursive step can demand a result for a changed parameter even though the induction hypothesis fixes it.

The needed result is an argument with its assumptions and connections recoverable. If it cannot yet be completed, identify the remaining mathematical claim and what proving or refuting it would enable.

### MATH.19:3 - Forces

| Force | Tension |
| --- | --- |
| A conclusion guides search | A sufficient intermediate claim can itself be harder than the original target. |
| Available constructions guide inference | Many consequences of the premises do no work in the desired argument. |
| Stronger lemmas support more uses | Extra hypotheses or conclusions can make the lemma unavailable or unnecessarily difficult. |
| Local reasoning supports collaboration | A lemma can be assigned separately only when its inputs, premises and required consequence are clear. |
| Automation can complete steps | The obtained proof still has to establish the mathematical statement the work requires. |

### MATH.19:4 - Solution

**Local mantra:** recover the claim; work backward from what would suffice; work forward from what is available; construct the connecting lemma; complete the argument; use it or revise the remaining question.

#### MATH.19:4.1 - State the claim at the scope its use needs

Identify the objects, assumptions and required conclusion. Unfold a definition when doing so exposes the operation the proof needs. For injectivity of f, the task becomes: for arbitrary a and b in its domain, derive a=b from f(a)=f(b).

Keep track of which parameters are fixed and which may vary. A claim for every input requires reasoning that covers every admitted input. A temporary assumption belongs to the implication or case in which it was introduced.

Choose the kind of conclusion needed. Proving existence, obtaining a particular object and supplying a uniform effective procedure can require different contributions. MATH.12 handles extraction when the proof is expected to yield data; CMP supplies execution and cost methods when those become the next question.

When the intended statement is still unclear, first recover or change it with B.5.FM or B.5.RA. Proof construction can begin with an informal mathematical statement whose objects and inferential obligations are clear.

#### MATH.19:4.2 - Work backward to sufficient claims

Inspect how the conclusion could be established. Common entry moves include:

| Wanted conclusion | First proof obligation |
| --- | --- |
| P implies Q | Assume P for this part of the argument and establish Q. |
| P and Q | Establish both claims under the required assumptions. |
| Every admitted x satisfies P(x) | Take an arbitrary admitted x and establish P(x) without adding a special property of it. |
| Some x satisfies P(x) | Construct a suitable x and establish P(x), when a witness construction is available. |
| Two mathematical expressions are equal | Find permitted transformations or an intermediate expression connecting them. |
| A theorem's conclusion applies here | Match its objects and discharge all premises needed for that application. |

An established theorem can replace one target with several premise obligations. A proposed lemma can do the same, but remains an obligation until proved. Retain why the proposed premises would suffice: this is the connection that makes the lemma useful.

Some backward moves deliberately strengthen the task. To show that two complicated expressions have the same value, finding one common normal form may be convenient. If the stronger task becomes obstructed, return to the weaker conclusion or find another route.

#### MATH.19:4.3 - Work forward and construct the connecting lemma

From the available definitions, equations, hypotheses or objects, derive consequences likely to supply an open obligation. Apply a function to an established equality; construct an element that a definition requires; substitute a known relation; or separate cases when they give different available facts.

Compare the expressions produced with the expressions needed. Their difference often identifies the lemma: an operation must commute past a repeated operation, an equality must survive a map, or a parameter must be allowed to vary. State that relation with all operands and hypotheses.

Then ask two questions together: can the lemma be established from what is available, and does it actually complete the next inference? Test the proposed statement on a small revealing case before investing in a long argument when such a case could defeat it. MATH.6 constructs a countermodel when a false intermediary is suspected.

Use the simplest sufficient connection. If substitution and a supplied identity finish the argument, no separate named lemma is needed. If several later steps need the same derived fact, prove it once and use it with its conditions.

When an auxiliary claim asks for more than the next inference needs, try a weaker conclusion that still closes that inference. Keep the original theorem fixed, prove the weaker lemma, and check its use in the argument. For a limit argument, a bound valid from some index onward may suffice even when the same bound on every term is false.

#### MATH.19:4.4 - Change the carried claim when a step needs more

At a stalled step, inspect what it actually consumes. It may need the claim for a different parameter, an additional retained quantity, or all smaller inputs instead of only the immediate predecessor.

Strengthen or generalize the carried claim to supply that information, then recheck its starting cases and every affected step. MATH.4 develops the corresponding inductive constructor and property proof. A stronger hypothesis inside an induction argument must come from the chosen induction principle and its proved cases.

Adding a new premise is a different repair. It narrows the theorem's applicability. Check whether the receiving problem supplies that premise; otherwise the revised theorem answers a changed question. The changed commutation condition in :5.2 demonstrates this boundary.

The argument may also need a different representation. MATH.17 supplies operations on operations, and MATH.18 compares interpretations when that change can make the missing mathematical relation available.

#### MATH.19:4.5 - Assemble the argument and inspect its dependencies

Order the proved claims so that each step uses available results. State an auxiliary lemma with the hypotheses under which it was proved, then bind its variables to the objects of the receiving step.

Inspect any apparent cycle. Induction can justify use of a smaller case under its decrease condition; it cannot justify using the current theorem as an unproved premise of its own auxiliary lemma. Separate the required earlier result or change the argument.

For cases, establish the target for every admitted branch. For an implication, discharge its temporary assumption when returning to the outer argument. For a contradiction argument, retain the logical principle that turns the contradiction into the requested conclusion; extracting a witness can remain a further question.

Write enough of the completed argument for another prepared reader to recover the decisive inference. A proof assistant can check a formal derivation and its dependencies when that is useful. Compare the checked statement with the intended statement before using the result.

#### MATH.19:4.6 - Return the result to its use

A completed proof supplies its conclusion under the stated assumptions. Use that result in the next mathematical construction, model argument or algorithmic design. When a changed premise invalidates a lemma, reopen its dependent steps and retain arguments that still apply.

An incomplete proof plan can still locate useful work: name the remaining lemma, its available premises, and the step it would close. This can support another reader, a specialist or an AI agent without concealing the open part. If a counterexample defeats the claim, return it and the failed premise or implication.

An obstruction can also motivate changing an axiom or developing a conjecture. Carry the failed relation and the intended use into that new mathematical question.

### MATH.19:5 - Archetypal Grounding

#### MATH.19:5.1 - Choose the intermediate equality that proves injectivity

Let f:A->B and g:B->A satisfy g(f(a))=a for every a in A. Prove that f is injective.

Work backward from injectivity: choose arbitrary a,b in A and assume f(a)=f(b). The required conclusion is a=b. The given identity involves g(f(a)), so work forward by applying g to the assumed equality:

g(f(a))=g(f(b)).

Substitute the two given identities to obtain a=b. The intermediate equality connects the assumption to the goal; no larger theory is needed.

Now replace the given identity by f(g(b))=b for every b in B. The same proof cannot simplify g(f(a)). What it does supply is surjectivity of f: for an arbitrary b, choose a=g(b), then f(a)=b.

For a concrete separating case, take `A={0,1}`, `B={*}`, `f(0)=f(1)=*`, and `g(*)=0`. The changed identity holds, but f is not injective. The failure identifies which composite was required and produces the useful conclusion that remains. MATH.18 can use these two composites when comparing descriptions.

#### MATH.19:5.2 - Discover the lemma needed to repeat a composition

Let f and g be maps `X->X` with f composed with g equal to g composed with f. Write composition as juxtaposition, with fg meaning apply g first and then f. Define `f^0=id` and `f^(n+1)=f^n f`, and similarly for g. Prove:

`(fg)^n=f^n g^n`

for every natural n.

The base n=0 holds. At the next step, the proposed induction hypothesis gives:

`(fg)^(n+1)=f^n g^n f g`.

The target is `f^(n+1)g^(n+1)`. The difference exposes a missing lemma: `g^n f=f g^n`. This states precisely how to move f past the repeated g.

Prove that lemma by induction. At n=0 both sides are f. If it holds at n, then:

`g^(n+1)f=g^n g f=g^n f g=f g^n g=f g^(n+1)`.

The second equality uses gf=fg; the third uses the lemma's induction hypothesis. Return to the original step:

`f^n g^n f g=f^n f g^n g=f^(n+1)g^(n+1)`.

The two inductions now have separate proved responsibilities. MATH.4 supplies their general induction method; the present work found which additional statement makes the main step possible.

Remove the commutation premise. On integers, `f(x)=x+1` and `g(x)=2x` give `(fg)^2(0)=3`, while `f^2 g^2(0)=2`. The theorem has become false. Retaining the premise or retaining the actual interleaved composition are different useful responses; continuing the old rearrangement would lose the result needed by the calculation.

#### MATH.19:5.3 - Generalize a parameter to make the proof close

Suppose a finite list is built as [] or x::xs. Define append ++ in the usual way, with []++a=a and (x::xs)++a=x::(xs++a). Let [x] denote the one-element list.

Define reversal by R([])=[] and R(x::xs)=R(xs)++[x]. A second construction carries an accumulator:

T([],a)=a,

T(x::xs,a)=T(xs,x::a).

The wanted result is T(xs,[])=R(xs). Induction on xs with only this statement stalls: the recursive call uses accumulator x::[], while the hypothesis concerns [].

Generalize to every accumulator a:

T(xs,a)=R(xs)++a.

The empty-list case gives a=[]++a. For a nonempty list, the generalized induction hypothesis gives:

T(x::xs,a)=T(xs,x::a)=R(xs)++(x::a).

Using x::a=[x]++a and associativity of append, this equals (R(xs)++[x])++a=R(x::xs)++a. Append associativity itself follows by induction on its first list: the empty case is the defining rule, and the nonempty case reduces after the common leading element to the induction hypothesis.

Setting a=[] recovers the original target, using append's right-identity law. That law also follows from the same two formation cases. On [1,2,3], the accumulator states [], [1], [2,1], [3,2,1] make the changed parameter visible.

The proof establishes equality of the two list results. A claim that one implementation uses less time or storage additionally depends on its list representation and execution model. Those are computational questions for the obtained construction.

### MATH.19:6 - Bias-Annotation

A short final proof can hide the search that found its auxiliary claim. When helping another reader construct a proof, expose the expression or missing premise that motivated the lemma, as in :5.2.

Successful instances can guide that search. The universal conclusion still needs an argument covering its admitted objects; the noncommuting maps in :5.2 show why one successful calculation could miss the decisive premise.

### MATH.19:7 - Conformance Checklist

For the argument being constructed:

- The objects, variable scope, assumptions and wanted conclusion are recoverable.
- Each backward obligation has a stated implication to the claim it is meant to establish.
- Each reused or newly proved lemma has its premises satisfied at the point of use.
- A strengthened induction claim supplies the actual changed parameter or retained information, with its starting cases and step rechecked.
- Every admitted case is covered, and circular dependence is discharged by a valid argument such as induction.
- The final statement is the one the mathematical work needs; any additional applicability condition is visible.
- The result is a completed argument, a counterexample, or a particular remaining mathematical obligation with a useful continuation.

### MATH.19:8 - Common Anti-Patterns and How to Avoid Them

**Using the desired conclusion inside its supporting lemma.** If the lemma that justifies a rearrangement is proved by assuming that rearrangement, the gap remains. Prove the smaller commuting statement from its own premise, as in :5.2.

**Fixing a parameter that the next step changes.** The empty-accumulator hypothesis in :5.3 cannot be applied to a nonempty accumulator. Generalize the statement and recheck the base and step.

**Silently changing a premise to finish the proof.** Commutation makes the rearrangement in :5.2 valid. If it is absent from the intended use, state the changed theorem or retain the interleaved operation.

**Closing a different composite.** The two inverse identities in :5.1 support different conclusions. Compare the operands and order of the proved statement with the question being answered.

### MATH.19:9 - Consequences

Proof construction becomes work on smaller mathematical claims with visible dependencies. The remaining difficulty can be assigned or investigated without requiring another agent to reconstruct the entire search.

A successful argument can reveal a more reusable lemma, a changed theorem or a new construction. When the claim fails, the separating case can guide the next problem. The resulting generality follows from the proved assumptions and operations.

### MATH.19:10 - Architectural Rationale

Backward obligations expose what would suffice; forward constructions expose what can be obtained. A useful intermediate claim joins the two. This organization supports informal reasoning and formal derivations while preserving the mathematical question as the governing object.

Induction, countermodels, interpretation and witness extraction contribute different operations. The stalled inference determines which contribution the argument needs: the list example requires a varying parameter, while the composition example requires a separately proved commutation relation.

The proof plan and its completion have different uses. A plan can locate a lemma for a collaborator; a completed argument supports the mathematical conclusion. Making that distinction visible permits useful incomplete work without treating the remaining obligation as already solved.

### MATH.19:11 - SoTA-Echoing

The working question is how to construct a missing mathematical argument from available objects, assumptions and results. The selected approach combines backward proof obligations with forward derivation, then changes an intermediary or the carried claim when their connection fails.

Avigad, Lewis and van Doorn's [Logic and Proof, §3.3](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_propositional_logic.html#forward-and-backward-reasoning) gives an explicit account of the two reasoning directions and hypothesis scope. The current [Theorem Proving in Lean 4, Tactics](https://lean-lang.org/theorem_proving_in_lean4/Tactics/) shows how applying a result creates premise goals and how local intermediate claims organize a derivation. Here those contributions inform :4.1-.3/:4.5; using Lean is optional.

Tao's [mathematical research advice](https://www.math.ucla.edu/~tao/advice.html) connects progress at lemma scale with the larger problem and recommends changing the point of attack when present methods are insufficient. The pattern gives that move concrete form through a failed intermediate claim and its revised continuation. This source is methodological advice, not a completeness guarantee for proof search.

A direct calculation or an already applicable theorem is preferable when it settles the claim with less effort. Unstructured forward manipulation becomes a poor alternative when it leaves the target unchanged; a single backward chain becomes a poor alternative when its generated premise cannot be obtained. The adopted combination changes :4.2-.4, as the missing commutation lemma and accumulator generalization demonstrate.

The sources provide construction methods and inspectable formal mechanisms. They do not make the proposed heuristic complete for all mathematical theories. Reopen the chosen proof route when a premise changes, a lemma fails, a better theorem or representation becomes available, or the receiver needs a constructive output or execution property not yet supplied.

### MATH.19:12 - Relations

- **B.5.RA** recovers an existing argument for its next use; **B.5.FM** helps formulate an unresolved question.
- **MATH.4** constructs and justifies inductive operations, including strengthened parameters.
- **MATH.6** develops a countermodel when an intermediate or final claim may be false.
- **MATH.12** extracts the construction an argument supplies.
- **MATH.17/.18** develop operations on operations and interpretations used by a proof.
- **C.29** connects a mathematical result to its modeled subject. Computational realization and cost remain with the corresponding CMP methods.
- **B.5.QD and C.40.CD** develop the next useful question when the argument or obstruction opens one.

### MATH.19:End

## MATH.4 - Construct a Witness by Induction

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.4:1 - Problem frame

Use this pattern when an input is given as a finite construction from smaller inputs, and you need a way to produce an object with a required property for every such input. You may know the desired equation or have an existence argument, while the operation that obtains an answer remains missing.

A witness is the object that satisfies the requirement: a quotient and remainder, for example, or a coloring with a stated property. Construct a witness for each base case, then construct one for a larger input from the witnesses for its immediate constituents. The same case structure gives a reason why the result has the required property.

Start with the smallest input and one step that builds the next input. Return a base witness and a usable step, or identify what the step still cannot construct. You need functions, elementary logical conditions and the input's formation rules. The number example also uses integer arithmetic; the tree example explains its own constructors.

This method starts with freely formed constructor expressions: each input supplies its outermost constructor and its constituent inputs. When different expressions represent the same object, section 4.4 explains the additional step needed for a function of that object. If a supplied operation already returns the required object, use it. An existence result can also be sufficient when no witness or way of producing one is needed. Infinite behavior or a recursion that does not follow smaller constituents needs a different termination or continuation argument.

### MATH.4:2 - Problem

An assertion that a suitable object exists can leave the receiver unable to obtain it. A recursive formula can leave a different gap: it may call itself without reaching an answer, omit a case, or return objects that fail the required property.

The mathematical task is to build the operation and its justification together. The case for a larger input must use only what the smaller-input results actually provide. Sometimes this reveals that the proposed result was too weak: the step needs an extra parameter or an auxiliary value.

### MATH.4:3 - Forces

| Force | Tension |
| --- | --- |
| One requested object and a reusable construction | A single instance may be easiest to solve directly; a family benefits from one operation and argument that cover its formation rules. |
| A small result and a usable inductive step | Discarding an auxiliary value can make the next case impossible to construct. |
| A complete definition and executable choices | Every input case needs an output rule; saying that a suitable choice exists may leave the rule missing. |
| Simple recursion and efficient execution | Following the input's construction makes correctness accessible, but another algorithm may use fewer operations or less storage. |

### MATH.4:4 - Solution

**Local mantra:** state the wanted object; build the base; build the next case from smaller cases; justify the construction; use the witness.

#### MATH.4:4.1 - State the input construction and wanted result

Name the input family, its constructors and any fixed parameters. For natural numbers, the constructors are zero and successor. A finite binary tree can be a leaf or a new root joining two smaller trees. The supplied constructor and constituents determine which recursive clause applies. If different constructions are later identified, retain that identification as a separate condition.

For each input `x`, state the kind of output `y` and the property `P(x,y)` it must satisfy. Include bounds or retained information that the next use consumes. For division by a positive integer `d`, the output is a pair `(q,r)` satisfying `n=q*d+r` and `0≤r<d`.

Use the input's actual formation rules to choose the cases. A proof about trees cannot be applied to a structure with additional edges without considering those edges.

#### MATH.4:4.2 - Construct the base witnesses

For each constructor with no smaller inputs, give an output and show that it satisfies the required property. This supplies the point at which recursive evaluation can return a value.

If the base fails, inspect the specification or its parameter conditions. Do not invent a default output that fails the requirement merely to complete the cases.

#### MATH.4:4.3 - Construct the step and strengthen what it needs

Take one constructor with smaller inputs. Assume that each smaller input already has an output satisfying the stated property. Give an operation that uses those outputs to build the required output for the whole input.

Show why the construction preserves the property. Check each branch that changes the returned object. When the step needs information absent from the proposed output, strengthen the result or generalize a fixed parameter, then revisit the base cases and affected steps.

For example, a tree-coloring step may need to choose either color for a subtree's root. A construction that promises only a root of color zero leaves that step unsupported. A construction parameterized by the required root color supplies what the step uses.

To obtain an executable construction, each case distinction must be decidable from the supplied data, and each operation used to build an output must itself return. A step that says only “choose a suitable object” identifies further mathematical work unless a way to make that choice is already supplied.

#### MATH.4:4.4 - Define the operation and establish its result

For a natural-number input, let `b` be the base witness and let `step(n,y)` produce a witness for `n+1` from one for `n`. Define:

`F(0)=b`

`F(n+1)=step(n,F(n))`.

The base argument establishes `P(0,F(0))`. The step argument establishes `P(n+1,F(n+1))` from `P(n,F(n))`. Induction therefore establishes the property for every natural number.

For another finite inductive input, give one defining clause and one property argument per constructor. Recursive calls use its immediate constituents. Evaluation terminates because these calls descend through a finite input construction, provided the operations within each clause terminate.

When different constructor expressions represent one object, the recursion first gives a function of expressions. To obtain a function of the represented object, establish that all its permitted expressions yield the same required output, using MATH.2. Alternatively, supply an additional rule that chooses one construction from the object. Keeping the construction as part of the input is also useful when its history matters.

For example, build a finite set with `Empty` and `Insert(a,S)` for `a` outside `S`. Returning `[]` at the base and prepending `a` at each step gives a list containing each element once. Yet `Insert(1,Insert(2,Empty))` and `Insert(2,Insert(1,Empty))` represent the same set and return `[1,2]` and `[2,1]`. Both are valid witnesses, but these clauses define a function of the insertion construction. If a function of the set is required and its elements have a supplied total order, strengthen the output requirement to an increasing list and insert each element in order. The unique increasing list then makes the output independent of insertion order. This repair uses the ordering operation and a stronger specification.

A dependent-type description can package the output with a proof of its property. Its first projection returns the witness; the other component justifies that witness for the stated input. An ordinary mathematical presentation may instead give the function and proof separately. Use the presentation needed for the receiving work.

#### MATH.4:4.5 - Use the witness and return after a changed requirement

Evaluate the construction for the needed input. Return the object and the property on which its next use relies. Reuse the general argument while its constructors, clauses and premises remain unchanged.

If the receiver needs another quantity, check whether the current result retains it. If a parameter or formation rule changes, return to the affected base or constructor clause. If constructions are newly identified, check whether the output still defines a function on those identified inputs. A failed clause can supply a counterexample or a more specific construction question.

An executable recursive construction is already an algorithm. Its operation count, storage and representation can become further design questions when the intended scale makes them matter. A faster implementation can retain the same mathematical specification; the correspondence between the two constructions needs its own argument.

Stop with the required witness, a reusable construction with its property, or a particular unresolved clause. Formalizing the same result in a proof assistant is useful when that receiving use needs it.

### MATH.4:5 - Archetypal Grounding

#### MATH.4:5.1 - Obtain quotient and remainder together

Given a natural number `n` and a fixed positive integer `d`, construct natural numbers `q,r` such that `n=q*d+r` and `0≤r<d`.

At `n=0`, return `(0,0)`. The equation holds, and positivity of `d` gives the remainder bound.

Suppose the result for `n` is `(q,r)`. To obtain the result for `n+1`:

- if `r+1<d`, return `(q,r+1)`;
- otherwise return `(q+1,0)`.

Because `r<d` and the values are integers, the second branch has `r+1=d`. In the first branch, `n+1=q*d+(r+1)`; in the second, `n+1=(q+1)*d+0`. Both branches preserve the required bound. This proves the recursive construction for all natural-number inputs.

For `d=3`, successive witnesses include:

| Input `n` | Witness `(q,r)` |
| ---: | --- |
| 0 | (0,0) |
| 1 | (0,1) |
| 2 | (0,2) |
| 3 | (1,0) |
| 4 | (1,1) |
| 5 | (1,2) |
| 6 | (2,0) |
| 7 | (2,1) |
| 8 | (2,2) |

The output for 8 determines both two completed groups of three and a remainder of two. Keeping only the remainder would lose the number of completed groups. MATH.2 explains which questions such a reduced result can still answer.

The construction takes one successor step per unit of `n`. It exposes the witness and proof economically as mathematics, but a large encoded integer can call for a different division algorithm. If division with the same convention is already supplied, use that operation.

Changing the parameter to `d=0` defeats the specification: no natural `r` satisfies `0≤r<0`. This returns a failed input condition before any recursive step. Extending the input to negative integers also requires a new case; the natural-number recursion does not cover that extension.

#### MATH.4:5.2 - Strengthen the construction to color a tree

Consider finite binary trees formed as `Leaf` or `Branch(left,right)`. A leaf is one vertex. A branch adds a new root with edges to the roots of its two constituent trees. The constituent vertices occur separately in the constructed tree.

The required output colors each vertex 0 or 1 so that each edge joins different colors. Suppose a first attempt always colors a root zero. At a new branch, using those subtree results unchanged would give edges from zero to zero.

Generalize the construction: `Color(t,c)` takes a tree and a required root color `c∈{0,1}`. Its result must have root color `c` and different colors across every edge.

- For `Leaf`, return its single vertex with color `c`.
- For `Branch(left,right)`, color the new root `c`, and use `Color(left,1-c)` and `Color(right,1-c)` for its constituent trees.

The leaf has no edge to violate the property. At a branch, the induction hypotheses supply the property within each constituent tree. Their roots have color `1-c`, so both new edges also join different colors. The construction therefore satisfies the specification for both choices of `c`.

For `Branch(Leaf,Branch(Leaf,Leaf))` with root color 0, the two children receive color 1 and the two grandchildren receive color 0. The strengthened parameter made the recursive step possible.

Now add edges beyond the tree construction. On a triangle, choosing colors 0 and 1 for two adjacent vertices forces the third to be 0 to differ from the second, but it then agrees with the first. The tree result therefore cannot provide the requested coloring for every graph. The new edge condition leads to a different construction or an obstruction, while the tree method retains its original use.

### MATH.4:6 - Bias-Annotation

A familiar induction proof can tempt the writer to leave the output operation implicit. Recover the witness produced in each case and the information the next case uses.

A second temptation is to keep the initial statement fixed even after the recursive step exposes missing information. The tree case needs both root colors; strengthening that specification repairs the construction.

Simple recursion can also look like a recommended implementation. The division case states its cost so that a mathematically useful construction can be replaced for a larger computational use.

### MATH.4:7 - Conformance Checklist

- Are the input constructors, supplied construction and parameter conditions stated?
- When different constructions represent one object, is any claimed function of that object independent of the construction or supported by a stated selection rule?
- Does each base case return an object satisfying the specification?
- Does every constructor clause use only supplied data and results justified for smaller inputs?
- When an auxiliary value or parameter is needed, do the strengthened specification, base and step agree?
- Are all case distinctions and witness-producing operations available for the claimed executable use?
- Do recursive calls descend through finite constituents, or is another termination argument supplied?
- Can the receiver obtain the witness and recover the property it uses?
- After a changed requirement, is the affected clause or missing construction identified?


### MATH.4:8 - Common Anti-Patterns and How to Avoid Them

**Prove existence while omitting the requested witness.** Recover the producing operation in each case. If the argument supplies no such operation, keep its existence conclusion and return the remaining construction question.

**Fill an uncovered case with an arbitrary value.** A total expression can still violate the specification. Check the value under the case's premises or expose the failed condition, as with division by zero.

**Use an induction hypothesis too weak for the step.** The tree's fixed-root-color attempt fails at the new edges. Quantify the needed color parameter and establish the stronger base and step.

**Recurse on an unchanged input.** The finite-constituent argument no longer establishes termination. Change the recursive calls or obtain a different well-founded argument.

**Transfer the proof after changing the input's formation.** The extra edge in the triangle is absent from the tree constructors. Reopen that new case before claiming the property for the larger family.

### MATH.4:9 - Consequences

The result is a reusable way to obtain witnesses, with a reason for the property each witness satisfies. Construction and justification expose the same case boundaries, making a changed premise easier to locate.

Strengthening the result can add parameters or auxiliary values. Those additions cost representation and calculation but can supply the information that makes the inductive step work.

An efficient implementation remains a further opportunity when the simple construction is too costly.

### MATH.4:10 - Architectural Rationale

The input's formation rules determine the cases. Pairing each output rule with its property argument links object construction, reasoning and computation without requiring a proof-assistant language.

The stronger specification is part of the construction method. It lets a smaller-input result provide what a larger input needs, as the root-color parameter shows. Returning the witness separately from optional proof packaging keeps the result usable in different mathematical and computational descriptions.

Structural recursion was selected because finite constituent structure supplies a local termination argument. Finite enumeration is a serious alternative for one small instance, and an existing operation can be the cheapest way to obtain its answer. Inductive construction earns its extra work when a family, reusable operation or premise-sensitive argument is needed.

The division and tree cases use different objects while sharing the base-and-constructor move.

### MATH.4:11 - SoTA-Echoing

**Question:** how can a specification over inductively formed inputs produce a witness-building operation and a reusable correctness argument?

**Adopt** the induction and computation rules from Egbert Rijke's [*Introduction to Homotopy Type Theory*](https://arxiv.org/pdf/2212.11082), §3.1, printed pp.19-22. Section 4.6, pp.33-34, supplies dependent pairs and their projections as one formal presentation of an output with dependent information. The pattern uses these construction questions in ordinary mathematical language; it does not require univalent foundations for the examples.

The current [*Theorem Proving in Lean 4*, §8.3](https://lean-lang.org/theorem_proving_in_lean4/Induction-and-Recursion/) gives an operative comparison: recursive definitions and induction follow the input constructors, with recursive calls on smaller constituent terms. **Adapt** that organization here by foregrounding the wanted witness and strengthening the result when a step cannot be built. The integer and tree constructions are authored examples of the method.

The book's [axiom-of-choice discussion](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/) shows why formal existence and executable witness production require separate attention: definitions that manufacture data through classical choice are noncomputable in that setting. This makes recovering the output rule consequential; classical reasoning about an independently computable operation can still be useful.

Direct enumeration or a supplied operation can answer a small instance with less construction work. Reopen the selected method when the input is no longer finite and inductively formed, a required choice lacks an obtaining operation, or execution cost calls for another algorithm. The set example adds the representative-independence question supplied by MATH.2: producing a witness from each expression and defining one function on identified inputs require different arguments.

### MATH.4:12 - Relations

- **Uses FPF B.5.RC and B.5.RA when needed:** recover an unfamiliar input construction or proof before choosing the cases.
- **Connects with MATH.1:** a witness can itself be a constructed path; a changed step can alter its permitted joins.
- **Uses MATH.2 when input constructions are identified:** establish whether the output is independent of their representative. MATH.2 also helps retain the information needed by the next operation when simplifying a witness.
- **Connects with FPF B.5.RR and B.5.QD:** locate the first failed clause after a changed premise and develop the resulting construction question.
- **Connects with FPF C.29 and C.29.2:** interpret the mathematical result and relate an executable procedure to its claimed result.
- **Connects with algorithm design:** compare other constructions, representations and resource use while preserving the needed specification.

### MATH.4:End

## MATH.12 - Extract a Construction from a Proof

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative unless marked informative

### MATH.12:1 - Problem frame

Use this pattern when a mathematical proof says that an object can be obtained, but you still need the operation that obtains it. The proof may describe the object through several intermediate results, hide it inside a pair, or use cases whose choice must be made from the input.

Recover the values and operations carried by the argument. A proof that a number is divisible by four can supply the quotient; a proof connecting two function types can supply transformations between their functions. When a step supplies only existence, the same reading identifies the construction still needed.

**First useful move:** find where the wanted object is introduced. Write the expression for that object and the inputs used to form it. Follow each needed input back to a supplied value, an available operation or a missing construction.

The reader needs functions, pairs, case distinctions and elementary mathematical reasoning. The arithmetic cases use integers and fractions. The function case explains its own notation. Use an already available operation directly when it returns the required object. An existence conclusion can be sufficient when the receiving question does not require obtaining a witness.

This method works through constructive proof steps and their computation rules. A claim about every input needs a construction that can be applied to every input in that scope. Some proofs establish their conclusion without supplying such a construction; :4.4 determines what can still be used from them.

### MATH.12:2 - Problem

Knowing that an answer exists can leave the next calculation impossible to perform. Even when a proof contains an answer, its presentation may separate the values needed to compute it or suppress their dependencies.

There is also a possible mismatch between mathematical reasoning and execution. A proof can distinguish two cases without providing a procedure that selects one. A formal system can store an existence proposition in a form that does not expose its witness as program data.

The needed result is an operation with stated inputs and an argument that its output satisfies the requested relation. A missing branch decision, unavailable auxiliary operation or unsupported termination claim is a specific remaining problem.

### MATH.12:3 - Forces

| Force | Tension |
| --- | --- |
| Existence and obtaining an answer | Existence may settle the mathematical question; a subsequent calculation can require the witness itself. |
| Concise proof and visible dependencies | An omitted intermediate value saves exposition but can prevent reconstruction of the operation. |
| General statement and available input | An argument for each input must retain the information on which its witness depends. |
| Mathematical correctness and execution | The proof's logic and a program's evaluation rules need a correspondence for the claimed computational use. |
| Equal outputs and affordable use | Two extracted expressions can return the same result while repeating different amounts of work. |
| Reusable proof and changed premises | A local assumption change can alter a branch, an output type or the computation that uses it. |

### MATH.12:4 - Solution

**Name the wanted output → recover its construction → compose the supplying steps → check computation → obtain the witness → revise affected dependencies.**

#### MATH.12:4.1 - State what must be obtained

Name the input x, any parameters and the relation R(x,y) required of the output y. A statement “for every x there is a y satisfying R(x,y)” leaves the next task open until the needed y can be supplied.

State what the input actually contains. A value with an associated proof, a procedure returning such a value, and a proposition asserting that some value exists support different operations. For example, a pair (k,p), where p justifies n=4k, supplies k by projection. A statement that n is divisible by four may require recovering or constructing that k.

Keep the order of dependence. The output of “for each x, construct y” may depend on x. It does not thereby supply one y that works for every x.

When the argument is unfamiliar, B.5.RA can recover its premises and deductions before this computational reading.

#### MATH.12:4.2 - Recover what each proof step supplies

Begin at the desired conclusion and follow the steps needed to produce its object. Give each supplied value a name. For a lemma used along the way, recover the obtaining operation when the next step consumes its output as data.

The following constructions give a small working repertoire:

| Form of the argument | Construction to recover | How its result is used |
| --- | --- | --- |
| Given x, construct t(x) | A function `x ↦ t(x)` | Supply a particular input and evaluate t at that input. |
| Construct both b and c | The pair (b,c) | Project the component needed by the next step, or retain both. |
| Establish one of two cases constructively | A tag naming the chosen case and the data for that case | Select the corresponding branch using that tag. |
| Exhibit y and establish R(x,y) | A pair containing y and its justification | Return y; use the second component when the next argument needs the property. |
| Use an already constructed operation f on a value a | The application f(a) | Feed the returned value to the next construction. |

A constructive disjunction carries which case holds. If the source argument provides no such choice, name the missing decision before turning it into a conditional program.

For an inductive argument, recover the base and constructor operations through MATH.4. That pattern also handles a step that needs a stronger result. The present method assembles the values supplied by those operations with the other proof steps.

#### MATH.12:4.3 - Compose the operations and simplify their use

Substitute each supplied result into the place that consumes it. Preserve names for inputs whose values differ or whose dependencies matter.

Some simplifications directly expose a wanted value:

- Applying `x ↦ t(x)` to a gives t with a substituted for x.
- The first component of (b,c) is b; the second is c.
- A case distinction applied to a tagged value runs the branch named by its tag.

These are computation rules for the chosen constructions. Use their conditions, including the input type and any variable binding. Rename an auxiliary variable when substitution would confuse it with another input.

For a proof supplying a dependent pair p(x)=(y,q), define F(x) as its first component. The second component then supplies R(x,F(x)). This gives both an obtaining operation and the relation its output satisfies, provided the construction of p(x) is available.

Write the resulting expression or procedure in a representation the receiver can use. A short formula can be sufficient. Pseudocode or a proof-assistant term is useful when its evaluation or composition is the next question.

#### MATH.12:4.4 - Determine which computation the argument supports

Inspect every operation on which the returned data depends. Is it supplied? Does it return on the permitted inputs? Can the case distinctions be decided? Finite composition of terminating operations gives an obtaining procedure; recursion needs its stated termination argument.

A proof step that invokes a classical choice of an element does not, by that invocation alone, give an executable choice procedure. Retain the existence result and either obtain a construction for that step or use another proof that supplies one. Classical reasoning can still justify a separately defined computable function.

Suppose a finite list is supplied together with a terminating test P and a proof that some listed element passes. Test the elements in order and return the first that passes. The list makes the search finite, and the proof rules out exhaustion without a result. For [2,5,8] and P(n)=(n>6), this returns 8 after three tests. The existence proof may use classical reasoning: the returned data comes from the search.

For a formalized proof, inspect the system's actual rules for data and proofs. In Lean, for example, an existential proposition in `Prop` is not a data-bearing dependent pair whose witness a program may simply project. A value packaged in a data type with a proof of its property can retain its data while compilation erases the proof. Choice used to manufacture the data is a separate computational issue.

The chosen logic and evaluation rules determine the proof-to-computation correspondence. General recursion can describe a computation that never returns; its type alone need not establish the requested terminating construction. An ordinary proof narrative also needs its object-producing steps recovered before it provides that construction.

#### MATH.12:4.5 - Obtain the result and use its justification

Apply the extracted operation to the input of interest. Follow its reductions far enough to obtain the requested value, and use the proof's retained relation to justify that value.

A worked input checks that the expression can be followed. The general output claim comes from the construction and its proof under the stated assumptions. Where the representation can overflow, round or reorder dependent updates, establish that its operations preserve the mathematical result needed here.

Retain intermediate results when recomputation would matter. A proof transformation that preserves a function's output can still duplicate an expensive calculation. Compare implementation choices under the same output requirement.

For work on another subject, use C.29 to establish the correspondence between the mathematical construction and that subject. C.29.3 connects a computation with its input preparation, execution and result interpretation. A mathematical function transformation can inform a change of method while the changed method still needs its physical, resource and interaction conditions.

Stop with the required object, a reusable obtaining operation with its property, or the particular premise that still lacks a construction.

#### MATH.12:4.6 - Return to the changed dependency

If only the input value changes within the proved scope, apply the same operation. If a premise changes, locate the earliest producing step or branch that uses it.

A stronger output requirement can need an additional value. A changed representation can remove a previously available projection or decision. Reconstruct that part, then follow its effects through the receiving expressions and justification.

When different input descriptions are identified, MATH.2 determines whether the obtained output is independent of the description; MATH.7 can carry it through a reversible representation. B.5.RR follows changed premises through the surrounding argument.

### MATH.12:5 - Archetypal Grounding

#### MATH.12:5.1 - Recover the witness in an arithmetic argument

For integers a,b, a proof shows that `(a+b)^2-(a-b)^2` is divisible by four. The receiver wants the quotient.

Expanding the squares gives:

`(a+b)^2-(a-b)^2 = 4*a*b`.

The existence statement is “there is an integer k such that the difference is 4k.” Its witness-introducing step chooses `k=a*b`. The extracted operation is therefore multiplication of the two inputs, with the displayed identity as its justification.

At a=3,b=2, the difference is 25-1=24 and the operation returns k=6. The receiver can use 6 without reconstructing the expansion on every input.

Now ask for divisibility by eight. The old proof supplies 4ab, which is insufficient: at a=b=1 the difference is 4. A supplied stronger premise a=2r repairs the construction:

`4*a*b = 8*r*b`.

The new witness is `r*b`. If the input already carries r, the procedure uses it. If only an assertion that a is even is supplied, obtain the integer r with a=2r or use an available integer-division operation with its conditions. The changed proof identifies both the new premise and the additional input needed by its expression.

#### MATH.12:5.2 - Read a function equivalence as two transformations

Suppose f maps each a in A to a pair in B×C. A proof can split this into two functions by projecting its output:

`Split(f) = (a ↦ first(f(a)), a ↦ second(f(a)))`.

Conversely, given g:A→B and h:A→C, pair their values:

`Join(g,h) = a ↦ (g(a),h(a))`.

Applying Join after Split gives, at each a:

`(first(f(a)),second(f(a))) = f(a)`.

Applying Split after Join returns g and h pointwise. Thus the argument supplies transformations in both directions, together with the equalities that justify using the returned functions.

For `f(n)=(n+1,n^2)`, Split gives `g(n)=n+1` and `h(n)=n^2`. Joining their values at n=3 returns (4,9). The projections and applications are the computational content of the proof.

The equality concerns functions with values determined by their input. If evaluating f is expensive, the expression using two calls can repeat work; calculate f(a) once and keep its pair when both components are needed.

If the proposed implementation instead reads and increments a hidden counter, repeated calls change the situation. A single call returning (c,c) might give (1,1), while separate component calls yield (1,2). This no longer implements the fixed mathematical f used by the proof. Include the changing state in the model and reconsider the transformation before using this function equivalence to reorganize the work.

#### MATH.12:5.3 - Extract a case decision and its answer

For a rational input r=p/q, with integer p and positive integer q, construct either an indication that r=0 or a rational y such that r*y=1.

The proof examines the decidable integer condition p=0:

- If p=0, return `Zero` with the equality r=0.
- Otherwise return `Inverse(q/p)`. Since p is nonzero, the fraction is defined, and `(p/q)*(q/p)=1`.

The result includes which case holds. At p=4,q=6 it returns `Inverse(3/2)`. At p=0,q=5 it returns `Zero`. This tag lets a receiving calculation choose its continuation.

Merely reporting that one of the two conclusions holds loses the branch information the continuation needs. The construction obtains that information by testing an integer, then carries it with the result.

Now replace the rational representation by access to successively narrower rational intervals enclosing an arbitrary real number. The rational procedure's test p=0 is no longer available. A nondegenerate rational interval containing zero does not by itself establish that the represented real is zero, because it also contains nonzero values. An interval [0,0] would establish equality, but the representation does not guarantee reaching such an interval. The previous proof does not supply a terminating zero test for this representation.

The next move is to obtain an appropriate decision procedure under additional input conditions, change the requested output to allow an unresolved case, or retain the existence conclusion without claiming the obtaining operation. The rational construction remains usable on its stated inputs.

### MATH.12:6 - Bias-Annotation

A familiar proof can make its witness look obvious to an author while leaving a reader without the expression that produces it. Starting at the witness-introducing step exposes that omission.

A second bias is to treat logical existence, a computable selection and an efficient implementation as one result. The branch and function cases make their different requirements visible through changed inputs and repeated work.

### MATH.12:7 - Conformance Checklist

1. The requested output and its relation to the input are stated.
2. Each data-consuming step has a supplied value or an obtaining operation.
3. Witness dependencies follow the statement's quantifier order.
4. Pairs, projections, functions and case tags retain what the next step consumes.
5. Every claimed executable branch has its decision, and a terminating construction has the needed computation argument.
6. The selected representation exposes the required data. An executable construction has an available procedure for every choice used to produce its data.
7. The extracted expression produces the worked result under the original relation.
8. A changed premise returns to its affected construction and receiving uses.

Recognition can recover one witness-producing step. Assurance of the general obtaining operation examines the dependencies and computation rules needed for that claim.

### MATH.12:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Read “there exists” as an available obtaining operation | Recover the witness-producing step or name the construction still needed. |
| Turn an unspecified disjunction into an executable branch | Supply a decision and return its case tag with the relevant data. |
| Change a witness that depends on x into one fixed witness for every x | Keep the input parameter and the statement's quantifier order. |
| Project program data from a formal proposition that does not expose it | Use an appropriate data-bearing construction or obtain the value by another supported method. |
| Infer termination from a program type that permits general recursion | Establish termination for the actual computation or retain its partial scope. |
| Replace one calculation by repeated calls while forgetting changing state or cost | Retain shared results and restore the state needed by the mathematical model. |

### MATH.12:9 - Consequences

The proof becomes usable for obtaining an object and for locating what changes when its premises change. Its constructive parts can be composed or assigned to different contributors through their stated inputs and outputs.

The recovered operation may be inefficient or depend on an unavailable decision. These are specific construction or implementation questions, which can be pursued while retaining the logical result already established.

### MATH.12:10 - Architectural Rationale

The central move reads object production through the structure of a proof. Function application, pairing and case analysis let a receiver carry the proof's intermediate results into the wanted output. Their computation rules explain why simplifying the construction preserves that output.

Inductive witness construction is one contributor. Recovering and assembling the computational content of an arbitrary supported argument also involves non-inductive steps, as the arithmetic identity and function equivalence show.

The correspondence between proofs and programs depends on the logic, data representation and evaluation rules. Keeping those choices explicit makes the connection usable: one can recover a mathematical construction, choose an implementation and then ask how it operates in the receiving subject.

### MATH.12:11 - SoTA-Echoing

**Adopt** the proof/construction correspondence explained by Philip Wadler in *Propositions as Types*, especially §3 and the paired proof and computation rules in §§6-7. Its useful contribution here is to reconstruct operations from proof structure rather than treat a logical consequence as a finished obtaining procedure. Sections :4.2-:4.3 and the function case use that distinction. The selected correspondence concerns a stated logic and typed computation; a different calculus can require different rules. [Author's paper](https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf).

**Use** Egbert Rijke's *Introduction to Homotopy Type Theory*, §2.2 and §4.6, for function application and dependent pairs with their projections. These give :4.3 a way to retain the witness together with its dependent property. The pattern presents those constructions without requiring the broader univalent foundation. [Book](https://arxiv.org/pdf/2212.11082).

**Compare** current Lean's *Axioms and Computation* with a blanket interpretation of every existence proof as executable witness production. Its distinction between proof erasure, computation and classical choice changes :4.4: trace the data-producing operation and the evaluation actually claimed. Classical reasoning can remain in a correctness argument for an independently computable function. [Lean documentation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/).

For an implementation using program extraction, Rocq's *Program extraction* explains how logical content, informative axioms and supplied realizations affect the extracted code. This supports checking the actual extraction assumptions rather than reading a successful proof as validation of arbitrary inserted implementation code. Such implementation work becomes useful when the receiver needs executable code; it is not required for the hand calculations here. [Rocq 9.1 documentation](https://rocq-prover.org/doc/V9.1.0/refman/addendum/extraction.html).

Reopen the chosen method when a needed proof rule has no available computational interpretation, a representation prevents a required decision, a source result changes that limit, or a more affordable construction provides the same wanted output.

### MATH.12:12 - Relations

- **B.5.RA** recovers an argument's premises and consequences. This pattern obtains the values and operations carried by its constructive steps.
- **MATH.4** constructs witnesses by induction; **MATH.5** extends assignments through mathematical composition. Their results can supply operations used in the extracted construction.
- **MATH.2** governs independence from identified input descriptions; **MATH.7** transports a construction through a bijection.
- **MATH.9** constructs a choice compatible with symmetry. Its existence and computation conditions remain relevant when the extracted result includes such a choice.
- **B.5.RR** revises an affected argument; **B.5.QD** develops a missing construction into the next mathematical question.
- **C.29.1** supplies a needed result-transfer argument; **C.29.2** develops a missing computational formulation; **C.29.3** connects a computation with its execution and interpreted result.

### MATH.12:End

## MATH.6 - Refute a Mathematical Claim with a Countermodel

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.6:1 - Problem frame

Use this pattern when a proposed mathematical implication might fail and you need a construction that settles the failure. Examples include a claimed property of every relation of a certain kind, a proposed inverse, or an interchange of quantifiers that would make a result more useful.

A *countermodel* gives mathematical objects, operations or relations in which the assumptions hold and the proposed conclusion fails. A counterexample to a statement about fixed objects supplies the particular values that make it fail. Both let you stop trying to prove the original claim and identify a useful change of question or assumptions.

Start by stating what must remain true and what would defeat the conclusion. Then construct one such case. Return the case and its decisive calculation or argument. A familiar counterexample already satisfying the present assumptions can finish the work immediately.

The reader needs elementary sets, relations, functions and quantified statements. The constructions below use ordinary mathematical truth and explicit witnesses; symbolic logic notation is explained where it changes the construction. A proof of a true claim, an estimate of how often a procedure fails, and an observation about a physical system require their corresponding methods. Countermodel construction answers whether the stated mathematical assumptions force the conclusion.

### MATH.6:2 - Problem

Several successful examples can hide the condition on which a conclusion depends. Conversely, an apparently failing example can violate an assumption, use different arithmetic, or assign inconsistent values to one object. It then leaves the proposed implication unanswered.

The working difficulty is to keep the assumptions and the failed conclusion in one construction. Quantifier order determines which choices may depend on which inputs. The carrier and operation rules determine whether the proposed objects are admissible. Search limits determine what can be concluded when no failure is found.

### MATH.6:3 - Forces

| Force | Tension |
| --- | --- |
| Small examples and the stated domain | A small construction is easier to understand, but the required failure may need a larger or infinite carrier. |
| Freedom to construct and retained assumptions | Changing a relation or operation can expose the failure while also destroying a premise. |
| Local witness and quantified failure | One input defeats a universal claim; defeating an existence claim can require a reason covering every candidate. |
| Criticism and continuation | Refutation removes one route to a result; its mathematical structure can suggest a different useful route. |

### MATH.6:4 - Solution

**State the implication → construct its failure condition → realize the objects and rules → establish assumptions and failure together → use the result or change the search.**

#### MATH.6:4.1 - Recover the mathematical claim

Name the carrier sets, constants, operations and relations that may vary. Retain the restrictions already given: total or partial operations, finite or infinite carriers, allowed values, and any equations or other assumptions. Expand a definition when its content determines the case you need to build.

Write the proposed implication in the form “under these assumptions, this conclusion holds.” Keep a definition or assumption separate from the conclusion being tested. For example, adding transitivity to the assumptions would remove all nontransitive relations from a test of whether reflexivity and symmetry imply transitivity.

If the claim comes from another practice, first recover its mathematical formulation and the intended interpretation through FPF C.29. The mathematical countermodel will test that formulation. Its consequence for the practice depends on that correspondence.

#### MATH.6:4.2 - Work out what failure requires

Keep the assumptions true and negate the conclusion. Preserve the order and permitted dependence of choices. The following ordinary forms cover common starting points; `P` and `R` denote the stated properties, and each variable keeps its declared domain.

| Conclusion to defeat | Construction or argument needed for failure |
| --- | --- |
| Every `x` has property `P(x)`. | One allowed `x` for which `P(x)` fails. |
| Some `y` has property `P(y)`. | A reason why `P(y)` fails for every allowed `y`. |
| For every `x`, some `y` satisfies `R(x,y)`. | One allowed `x` for which every allowed `y` fails. |
| Some `y` satisfies `R(x,y)` for every `x`. | For each allowed `y`, an `x` that defeats it; this `x` may depend on `y`. |

An equation between operations can often be defeated by one input tuple. Failure of transitivity requires three elements with the first two links present and the third absent. Start with those witnesses and use them to constrain the construction.

Where failure contains a universal requirement, give its argument or a complete finite case distinction. Finding one unsuccessful candidate for an existential conclusion leaves the other candidates open.

#### MATH.6:4.3 - Build objects that can realize the failure

Choose a familiar structure or a small carrier that has room for the required witnesses. Assign the constants and the critical relation entries or operation values first. Fill the remaining entries so that the assumptions continue to hold. Total operations need an output for every allowed input; partial operations retain their domains of definition.

For a finite relation, a table can make the critical choices visible. For a function, give its value at each element or give a defining rule. If the objects are classes of expressions, ensure the operation has the same value for equivalent representatives; MATH.2 supplies that construction.

Use the assumptions to reduce the choices. Symmetry determines the reversed relation entry; an identity law determines part of an operation table. After a forced assignment, return to any assumption that uses the changed entry. A conflict means this attempted construction needs revision.

Try a larger carrier or another kind of structure when the failure condition needs it. Smallness is useful for discovery and explanation; a smallest countermodel is required only when its minimality answers the question. A symbolic construction can cover an infinite carrier without listing its elements.

A model finder can supply assignments when the interacting constraints make manual construction expensive. Give it the assumptions together with the negated conclusion and the chosen search scope. Retain the meaning of its types, arithmetic and undefined values when interpreting the returned assignment.

#### MATH.6:4.4 - Establish that the construction defeats the claim

Evaluate every assumption used by the implication in the constructed case. Then exhibit the false conclusion with the witnesses or quantified argument from :4.2. These two parts establish the countermodel.

For a finite carrier, universal premises can be checked over all relevant tuples. For an infinite carrier, use a rule and an argument covering the required inputs. A program's finite output can help discover that rule; the argument determines the wider conclusion.

If a search tool used a restricted interpretation, substitute its proposed counterexample back into the intended mathematical definitions. For example, a truncated representation of the natural numbers needs its missing values accounted for. Repair an assignment that relies on an unavailable value or an altered operation before using it to refute the original statement.

Suppose the source claim is `n+1≠0` for natural numbers. An encoding instead uses addition modulo 2 and returns `n=1`. Its `1+1=0` becomes `1+1=2` in the source arithmetic, so this assignment fails to refute the source claim. Restore the source arithmetic before continuing that search, or prove the claim directly from `n+1≥1`.

Remove dispensable elements or assignments when that makes the reason easier to see. After such a simplification, repeat the affected assumption and failure checks. Keep a larger readable case if further minimization adds work without helping its use.

#### MATH.6:4.5 - Interpret an unsuccessful search

State what the search covered. Exhaustive failure to find a countermodel establishes absence only in the fully searched class and under the encoded semantics. A timeout or a partial enumeration leaves even that class unresolved.

When this absence is unexpected, compare the encoded assumptions with the intended ones. A contradictory or overrestrictive premise set can exclude the very cases under examination. Constructing one model of the assumptions alone can help distinguish that problem from an unsuccessful search for failure.

Choose the next move from what could answer the question: a different carrier, a symbolic infinite construction, a proof of the proposed claim, a weaker conclusion, or stopping with the searched-scope result. FPF C.11.DUA helps decide whether further inquiry is worth its cost. Enlarging the search is one option.

#### MATH.6:4.6 - Use the failure to revise the mathematical work

Return the assumptions that survived, the failed consequence, and the construction that separates them. This can reject an identification, stop an invalid proof attempt, expose a needed input, or identify an operation for which a proposed representation is unsuitable.

A repair is a new mathematical question. Restrict the domain, strengthen a justified premise, weaken the requested conclusion, or change the construction according to what the receiving work needs. Establish the revised claim on that scope; merely excluding the exhibited case can leave other failures.

Use B.5.RR to follow the effect through an existing argument. Use MATH.2 or MATH.5 when the affected step forms classes or interprets generating operations. Stop once the countermodel and its intended consequence are usable. No separate report form is needed for an ordinary calculation.

### MATH.6:5 - Archetypal Grounding

#### MATH.6:5.1 - A relation that cannot serve as the proposed equivalence

The claim is that every reflexive, symmetric relation is transitive. On `X={a,b,c}`, assign the following relation; 1 means the pair is in the relation.

| R | a | b | c |
| --- | --- | --- | --- |
| a | 1 | 1 | 0 |
| b | 1 | 1 | 1 |
| c | 0 | 1 | 1 |

The diagonal establishes reflexivity. Matching entries across the diagonal establish symmetry. But `a R b` and `b R c` hold while `a R c` fails. This is a countermodel with the required three witnesses.

With at most two elements, every reflexive symmetric relation is transitive: in a two-link sequence `x R y R z`, either `x=z`, or one adjacent pair is an equal pair and the other link already supplies `x R z`. The third element makes the failure possible.

If the work needs the smallest equivalence relation containing this R, its transitive closure adds the missing pairs and gives the single class `{a,b,c}`. It answers whether elements are connected through R-links. A question about the original direct relation still needs the original table. For classes on which further operations must be defined, continue with MATH.2's operation-preservation condition.

#### MATH.6:5.2 - A left inverse and the elements it does not recover

Consider the claim: if `f:A→B` has `g:B→A` with `g(f(a))=a` for every `a`, then `f(g(b))=b` for every `b`.

Choose `A={u}`, `B={0,1}`, `f(u)=0`, and `g(0)=g(1)=u`. Both maps are total. The premise holds at the only element of A, but `f(g(1))=0`. The claim fails because the left-inverse condition constrains recovery of source elements while B also contains an element outside the image of f.

Now require A and B to be the same finite set. The premise makes f injective: equality `f(a)=f(a')` gives `a=a'` after applying g. An injective self-map of a finite set is surjective. Write any `b` as `f(a)`; then `f(g(b))=f(g(f(a)))=f(a)=b`. This supplies a proof for the changed domain.

For the same infinite set `N={0,1,2,...}`, take `f(n)=n+1`, `g(0)=0`, and `g(n+1)=n`. Then `g(f(n))=n` for every n, but `f(g(0))=1`. Every finite self-map search can miss this failure because the finite claim is true. The symbolic construction locates the lost premise: finiteness supplied the step from injection to surjection.

A receiving construction can retain the original left inverse for source recovery, require surjectivity for recovery of every target element, or restrict the target to the image. Which result is useful depends on the proposed representation.

#### MATH.6:5.3 - A separate answer for each input and one answer for all inputs

Let `X=Y={0,1}` and let `R(x,y)` mean `x≠y`. For every x there is a y satisfying R: choose `y=1-x`. The proposed stronger conclusion is that one y works for every x.

To defeat that conclusion, take any proposed y and choose `x=y`. Then R fails. This gives the required argument for both possible choices of y. It does not replace the premise's input-dependent choice with a uniform one.

The useful result can instead be a function `h(x)=1-x`, satisfying `R(x,h(x))` for every x. MATH.4 supplies inductive witness construction when a comparable task has finite inductively formed inputs and suitable base and constructor clauses. The countermodel identifies which input dependence the requested result must retain.

### MATH.6:6 - Bias-Annotation

Small finite structures are prominent here because they expose the construction and make universal checks affordable. That preference can conceal infinite-only failures, as :5.2 demonstrates. The quantified claims also presuppose the stated mathematical interpretation; a probabilistic failure rate or empirical prevalence requires another question and method.

### MATH.6:7 - Conformance Checklist

- The construction uses the domains, operation rules and assumptions of the claim being tested.
- The failure condition retains quantifier order and the allowed dependence of each choice.
- The proposed objects satisfy the assumptions and defeat the conclusion in the same interpretation.
- A finite search result states its covered scope; any wider conclusion has its own argument.
- The result changes the receiving proof, construction or question, with any proposed repair stated separately.

### MATH.6:8 - Common Anti-Patterns and How to Avoid Them

**Put the desired conclusion among the assumptions.** This excludes countermodels by construction. Keep the conclusion outside the retained assumptions, and inspect an unexpected empty search.

**Use a failing case outside the stated domain.** The infinite shift in :5.2 refutes the unrestricted self-map claim while the finite claim remains true. Carry the actual domain into the returned conclusion.

**Keep one witness while reversing quantifier order.** The witness in :5.3 depends on the input. Preserve that dependence, or establish a uniform witness as a different result.

**Treat a search limit as the theorem's limit.** Recover which mathematical cases were represented. Change the construction or retain the bounded result when the desired claim reaches beyond them.

### MATH.6:9 - Consequences

A countermodel gives a conclusive failure of the stated implication and a concrete object for further work. It can reveal a useful narrower theorem, a needed distinction, or a replacement construction. Its direct result is refutation on the stated interpretation; choosing and proving the repair remains further work.

An unsuccessful attempt can still identify an incompatible set of assignments or a limited class with no failure. Its usefulness depends on how that result changes the next mathematical move.

### MATH.6:10 - Architectural Rationale

The method joins logical failure conditions with mathematical construction. Negating the conclusion tells the worker what to build; satisfying the assumptions makes the constructed case relevant; carrying the result back into the argument makes the criticism usable.

Separating these operations exposes two different errors: an inadmissible example and a failure condition that does not defeat the actual quantified claim. The finite and infinite inverse cases show how the same question can move between refutation and proof as the domain changes.

B.5.RA recovers an available argument, and B.5.RR revises reasoning when its premises or question change. This pattern supplies the mathematical countermodel they can consume. MATH.2's failed-identification witness is a direct use, while the relation and inverse cases give this construction independent mathematical entries.

A known case or a short direct construction is preferable when it already settles the implication. Constraint solving helps when the assumptions interact enough to make that construction difficult. Neither route requires finding a smallest example unless its size matters to the receiving question.

### MATH.6:11 - SoTA-Echoing

**Question:** how can a mathematical claim be refuted by a constructed interpretation while preserving its assumptions and quantifier dependencies?

Blanchette's [*A User's Guide to Nitpick for Isabelle/HOL*, 18 January 2026](https://isabelle.in.tum.de/doc/nitpick.pdf), §§3.2-3.5, demonstrates carrier search, recovery of assigned constants, dependent witnesses and the treatment of infinite number types. **Adopt** those distinctions. The manual's use of finite subsets for infinite types makes interpretation of a returned assignment important. The hand constructions here make the decisive reasoning accessible without requiring Isabelle.

The [Alloy language reference, Commands](https://alloytools.org/spec.html#command-section) specifies assertion checking as assumptions and declarations together with the negated assertion, within a scope. **Adapt** that construction to mathematical relations and operations; retain its distinction between assumptions, asserted consequences and search bounds. An empty search can expose an overrestricted formulation as well as an absence of counterexamples.

Direct construction, a supplied counterexample and a proof are meaningful alternatives at comparable effort. A model finder is useful when it supplies a difficult assignment, while symbolic reasoning remains important for quantified or infinite constructions. Reopen the chosen approach when a changed domain, equation or search interpretation changes what its result can establish.

### MATH.6:12 - Relations

- **Uses MATH.1 and MATH.2 when operations or classes are involved:** construct permitted combinations and test whether the proposed identification preserves them.
- **Connects with MATH.4:** retain the dependence of a constructed witness on its input.
- **Connects with MATH.5:** a failed source equation can refute the proposed extension to identified expressions.
- **Supplies B.5.RA and B.5.RR:** use a mathematical failure in criticism and in revision of the affected argument.
- **Uses C.29 for an external subject:** establish what the mathematical failure means for that subject.
- **Uses B.5.QD or C.11.DUA when continuation is the question:** choose a worthwhile new problem or further inquiry from the result.

### MATH.6:End

## MATH.20 - Bound a Mathematical Unknown by Comparable Constructions

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.20:1 - Problem frame

Use this pattern when obtaining a mathematical value or object is difficult, but a justified comparison could already answer the receiving question. Construct something known to lie below, above, inside or outside the unknown in the relevant mathematical order.

Examples include bounding a best attainable value by a feasible construction and an inequality, enclosing a set between simpler sets, or converting an equation residual into a bound on solution error. The common method is to build and justify the comparison, then determine what it permits next.

**First useful move:** name the unknown and one comparison that would change the next action. A single feasible construction can settle an existence question or one side of an optimum bound. A proved enclosure can exclude a region. Construct only the bound the current question needs.

The reader needs elementary inequalities, sets and functions. The examples introduce their graph and set constructions; the residual example also uses linear equations and an inverse map. More specialized bounds require the properties of their particular mathematical objects.

If an available value or direct calculation answers the question more easily, use it. FPF's characterization and choice methods select among alternatives; this pattern supplies mathematical bounds those choices may use. A mathematical comparison applied to a physical or organizational subject also requires the correspondence work in C.29 and MMP.

### MATH.20:2 - Problem

A plausible estimate can be close in familiar cases while lying on the wrong side of an unknown elsewhere. A bound on an intermediate quantity can also be mistaken for a bound on the requested result. For example, a small equation residual need not imply a small error in its solution.

Bounds themselves can be uninformative. A wide interval may leave the receiving choice unchanged, and separately sharp coordinate bounds may never be attained together. The work needs both a justified relation and a way to tell whether improving that relation would help.

### MATH.20:3 - Forces

| Force | Tension |
| --- | --- |
| Obtaining and comparing | It can be easier to bound a result than to construct it, but the comparison still needs an argument. |
| Direction | Feasible constructions and relaxed problems bound optima in different directions. |
| Tightness | A simpler bound can be cheaper; a tighter one matters only through the result it enables. |
| Propagation | An operation can preserve, reverse or destroy a comparison. |
| Attainability | A bound may be approached without being attained, or may require incompatible equality conditions. |
| Reuse | A proved comparison remains useful while its domain and premises survive. |

### MATH.20:4 - Solution

**Local mantra:** name the unknown and the needed comparison; construct a simpler comparator; prove its direction and scope; carry the comparison through the required operations; tighten or expose the gap; return the bounded result to use.

#### MATH.20:4.1 - Choose the quantity or object and its order

State what is unknown: a number, a function, a set, an error, an optimal value, or another mathematical object. State the comparison relation. Numerical order, pointwise order between functions and set inclusion support different conclusions.

For a numerical bound `L≤q≤U`, say which q is being bounded and under which assumptions. For an enclosure `L⊆S⊆U`, L consists of established members of S, while U contains every possible member under the stated description. Cardinality alone does not establish either inclusion.

For an optimum, distinguish the optimal value from an object attaining it. A bounded nonempty set of real values has an infimum and supremum, but an attaining object needs a further argument. For example, the interval `(0,1)` has infimum 0 and contains no minimum.

Select the needed direction and strength. To show `q≤t`, an upper bound at most t suffices. To refute that claim, a lower bound greater than t suffices. If the bounds straddle t, they leave this question open.

#### MATH.20:4.2 - Construct a comparator from available structure

Choose a construction whose relation to the unknown can be proved with available information.

| Requested result | Useful construction | Reason for the direction |
| --- | --- | --- |
| Minimum of an objective | A feasible candidate gives an upper bound; minimizing over a larger feasible set gives a lower bound. | The minimum is no larger than any admitted value; added choices can only lower the infimum. |
| Maximum of an objective | A feasible candidate gives a lower bound; maximizing over a larger feasible set gives an upper bound. | The maximum is no smaller than any admitted value; added choices can only raise the supremum. |
| Unknown set | Build a subset of verified members or a superset containing all admitted possibilities. | Membership proofs establish the two inclusions in opposite directions. |
| Error in a result | Relate a computable discrepancy to that error through the governing equation or map. | The derived inequality, such as the inverse-map bound in :5.2, connects the measured quantity to the requested one. |

Other constructions can use symmetry, a conserved quantity, a norm inequality or a comparison theorem. Select the property that supplies the missing direction. A familiar shape or similar-looking value is a candidate for investigation until that relation is established.

A comparator can be a different kind of object from the result. In :5.1 a node potential produces a numerical lower bound on every path length. The derivation makes those resulting values comparable; it does not compare a potential directly with a path.

#### MATH.20:4.3 - Establish the bound over its claimed domain

Prove the inequality or inclusion for every admitted case to which the result will apply. A feasible witness establishes one attainable value. A claim about all candidates needs a relation covering all of them, as the edge inequalities in :5.1 cover every path.

Track the assumptions used. For a relaxed feasible set, establish the original set's inclusion in it and keep the objective unchanged on original candidates. For a norm estimate, specify the norm and the operator property that supports it. For a probabilistic inequality, retain its distributional conditions and probability claim.

Use a known comparison theorem when it settles this question. If it does not, MATH.19 can construct the missing intermediate inequality and MATH.6 can test a suspected overclaim with a separating case.

Where the comparison cannot be established, return the condition that is missing or the counterexample. A trial value may remain useful for exploration without being used as the unproved bound.

#### MATH.20:4.4 - Propagate the comparison through the needed operations

For an order-preserving map F, `L≤q≤U` implies `F(L)≤F(q)≤F(U)`. For an order-reversing map, the endpoints exchange roles. Establish the relevant behavior on the admitted domain.

For example, multiplication by a nonnegative scalar preserves numerical order, while multiplication by a negative one reverses it. Squaring is increasing on nonnegative inputs; an interval crossing zero needs its minimum and maximum square computed on that interval. From `-2≤x≤1`, the bound is `0≤x²≤4`.

For sets, image and preimage under a fixed function preserve inclusion; complement reverses it in a fixed ambient set. Thus an enclosure can be carried into a subsequent transformation without requiring the original set to be enumerated.

Keep shared variables and constraints when combining bounds. If `x∈[0,1]`, separately bounding x and -x gives `-1≤x+(-x)≤1`, but retaining the dependency gives equality to zero. The loose result is valid; its loss comes from forgetting that the terms use the same x.

A bound computed with approximate arithmetic must preserve the claimed direction after that computation. A computational continuation can use error bounds or enclosing arithmetic for this purpose; the mathematical argument states the comparison it must maintain.

#### MATH.20:4.5 - Tighten the comparison or identify what prevents it

Inspect where the proof introduces slack. It may enlarge the feasible set, forget a dependency, replace a quantity by a worst-case value, or use one norm for effects that could be bounded separately.

Improve the part that can change the receiving result. Construct a better feasible candidate, strengthen the inequality, partition the domain, retain a lost relation, or add an available premise. A bound on a requested component can be enough when a bound on the whole object is costly or impossible.

Check attainability and equality conditions. When a feasible value meets a proved bound in the opposite direction, the optimum is established. When equality conditions conflict, the current bound can remain valid while failing to identify an attainable result. A sequence approaching a bound can establish an infimum or supremum without an attaining object.

If the gap reflects missing information, expose it. Two admissible constructions with different answers can show why the current assumptions do not determine a narrower result. That identifies a useful next assumption, observation or mathematical question.

#### MATH.20:4.6 - Use the bounded result and stop at the needed strength

Return the comparator, its relation to the requested result and the premises needed by the next use. A numerical interval, a set inclusion or a short inequality can carry this result.

For a minimization with feasible value U and lower bound L, the candidate is within `U-L` of the optimal value when these quantities are finite. The receiver can use that gap to decide whether further optimization matters. If only exclusion, existence or a threshold result was needed, stop once that result follows.

General choices about cost, value and further work use FPF's existing characterization, Pareto and improvement methods. Componentwise mathematical bounds can inform them, but a candidate attaining one coordinate need not attain another. Preserve which constructions actually realize the compared results.

Reopen the affected bound when its domain, objective, available information or following operation changes. Preserve bounds whose proofs still apply.

### MATH.20:5 - Archetypal Grounding

#### MATH.20:5.1 - Bound a shortest path before completing a search

Consider a finite directed graph with nonnegative edge weights and at least one path from s to t. Its shortest path length D is attained: cycles can be removed without increasing length, leaving one of finitely many simple paths.

Any particular s-to-t path of length U gives `D≤U`. For a lower bound, assign a number p(v) to each node such that, for every edge from u to v,

`p(v)-p(u)≤w(u,v)`.

Along any path, add these inequalities. The intermediate potentials cancel, giving `p(t)-p(s)≤path length`. Therefore `p(t)-p(s)≤D≤U`.

Take nodes s,a,b,t and these edges:

| Edge | Weight |
| --- | ---: |
| s to a | 2 |
| a to t | 5 |
| s to b | 4 |
| b to t | 1 |
| a to b | 1 |

The path s-a-t gives U=7. Choose `p(s)=0, p(a)=2, p(b)=3, p(t)=4`. The edge differences are respectively 2,2,3,1,1, each no larger than its edge weight. Thus `4≤D≤7`.

The equality cases suggest s-a-b-t. It has length 4, meeting the lower bound, so D=4. The proof of optimality uses a feasible path and the comparison applying to every path; it does not need a list of every possible path.

**Changed condition.** Add an edge s-to-t of weight 1. The old potential violates its new edge inequality, since `4>1`; its lower bound is invalid for the enlarged graph. The old path still supplies upper bound 4, and the new edge improves that to 1. The potentials `p(s)=p(a)=p(b)=0, p(t)=1` satisfy every new edge inequality, proving D=1. Only the comparison affected by the new edge had to be replaced.

#### MATH.20:5.2 - Convert a residual to the error actually requested

Suppose `Ax=b` has an invertible linear map A, and an available approximation is xhat. Define its residual by `r=A xhat-b`. Then

`xhat-x=A⁻¹r`.

If the chosen vector norm and induced operator norm give `||A⁻¹||≤K`, it follows that

`||xhat-x||≤K||r||`.

The bound K is the missing comparison between residual and solution error. It can come from a proved estimate of the inverse action; forming the entire inverse is unnecessary when a cheaper bound is available.

For a concrete case, A is diagonal with entries 1 and 0.001, b=(1,1), and xhat=(1,999). Use the maximum absolute coordinate as the vector norm. The inverse scales the coordinates by 1 and 1000, so its operator norm is 1000. The residual is (0,-0.001); the bound on solution error is 1. The actual solution (1,1000) attains that error.

A requested error of at most 0.01 therefore requires a residual bound of at most 0.00001 under this comparison. The apparent smallness of 0.001 was insufficient for that request.

**Changed condition.** Let the second diagonal entry become zero and b=(1,0). The equation fixes the first coordinate and leaves the second arbitrary. Residual zero cannot bound distance to a specified second-coordinate value: solutions with arbitrarily different second coordinates have the same residual. A request about the first coordinate alone is still answerable. Return that determined component or supply an additional condition selecting the second.

The method has derived an error relation and exposed its failure condition. A numerical method can now decide how accurately to obtain the residual and the approximation; the bound itself has not selected a solver.

#### MATH.20:5.3 - Enclose a set and improve the consequence

Let S be the disk `{(x,y): x²+y²≤1}`. The work needs the largest value of `g(x,y)=x+y`, but first seeks cheaper comparable sets.

The diamond `L={(x,y): |x|+|y|≤1}` lies inside S, because `x²+y²≤(|x|+|y|)²≤1`. The square `U=[-1,1]×[-1,1]` contains S, because each coordinate square is at most one. Thus `L⊆S⊆U`.

Over L, `x+y≤|x|+|y|≤1`, attained at (1,0). Over U, `x+y≤2`. Therefore the maximum over S lies between 1 and 2. Its existence follows, for example, from continuity of g on the compact disk.

The point (1,1) attaining the outer bound is outside S. To tighten that bound, retain the relation between the coordinates:

`(x+y)²≤2(x²+y²)≤2`,

where the first inequality follows from `(x-y)²≥0`. Hence `x+y≤sqrt(2)`. The point `(1/sqrt(2),1/sqrt(2))` belongs to S and attains this value, completing the comparison.

The inner set supplied feasible values; the outer set supplied a restriction on all feasible values. A better inequality and its equality case closed the gap. The same inclusion method can enclose a feasible region, a family of functions or another set, with the corresponding proof of membership and bound on the requested operation.

### MATH.20:6 - Bias-Annotation

A single numerical answer can hide which object or property was bounded. The examples make that choice visible: path length, error in a vector, and an enclosed set with an objective on it.

Simple bounds can look weak beside a precise calculation, yet already settle the receiving question. A small displayed residual can produce the opposite bias. Judge the comparison by its proved relation to the needed result, keeping its cost in view.

### MATH.20:7 - Conformance Checklist

For the comparison being used:

- The unknown, comparison relation and requested consequence are identifiable.
- A feasible witness, enclosing object or inequality supplies the claimed direction.
- The proof covers the domain and assumptions of the intended use.
- Operations preserve or reverse the comparison under stated conditions.
- Shared variables and dependencies are retained when their loss matters.
- The bound on a value is distinguished from an object attaining it.
- The remaining gap identifies either sufficient precision or a useful refinement.
- A changed premise reopens the comparison it invalidates, while unaffected results remain available.

### MATH.20:8 - Common Anti-Patterns and How to Avoid Them

**One attainable value used as a universal bound in the wrong direction.** A path of length 7 bounds the shortest length from above. The potential inequalities supply the lower bound.

**The comparator's optimizer used as an original solution.** The square's maximizing point in :5.3 is outside the disk. Check membership in the original feasible set before using it as a candidate.

**An operation applied without its order conditions.** Squaring an interval crossing zero requires inspecting zero and both endpoints; simply squaring endpoints in their original order gives the wrong enclosure.

**A discrepancy used as the requested error.** In :5.2 the inverse action amplifies the residual, and singularity removes the full-solution bound. Derive the relation or restrict the requested output.

**Separate extrema treated as jointly attainable.** Retain the common variables and equality conditions. Their incompatibility can explain why a valid bound remains loose.

### MATH.20:9 - Consequences

A justified bound can terminate a search, establish an impossibility, support a controlled approximation or identify missing information. It can also make a difficult problem workable before its complete solution is available.

The constructions reveal further methods: improve a feasible witness, solve a relaxation, exploit a dependency or change the requested output. The comparison provides a reason to choose among these next mathematical operations.

### MATH.20:10 - Architectural Rationale

The unknown is reached through another construction whose mathematical relation to it is tractable. Feasible witnesses, potential inequalities, inverse-map estimates and set inclusions give different ways to establish that relation. Their common structure is an order with a proved direction and operations that preserve the intended consequence.

Constructing bounds and choosing between alternatives have different results. The first supplies an inequality or enclosure; the second uses it with the purposes and costs of the work. This lets the same mathematical method serve proofs, computations and modeling without adding a separate preference system.

The gap is itself useful mathematical information. Matching attainable bounds can establish an optimum; a failed equality condition or two separating cases can show what prevents a narrower answer.

### MATH.20:11 - SoTA-Echoing

The working question is how to obtain a useful justified comparison without first solving the whole problem. The selected line combines feasible construction, relaxation or a comparison identity with explicit order propagation and an examination of the remaining gap.

Vandenberghe's [Duality, EE236A lecture 6, especially 6-4](https://www.seas.ucla.edu/~vandenbe/ee236a/lectures/duality.pdf) derives the relation between feasible primal and dual values. Its contribution to :4.2/:5.1 is that a feasible construction and a general inequality can bound the same optimum from opposite sides. A complete optimal solution is unnecessary for each bound. Direct solution is cheaper for an easy instance; bounding becomes useful when a partial construction already settles the receiving question. Equality and attainment require the particular argument, not an unrestricted assumption of strong duality.

Higham's [What Is Backward Error?](https://nhigham.com/2020/03/25/what-is-backward-error/) and [What Is a Condition Number?](https://nhigham.com/2020/03/19/what-is-a-condition-number/) explain why a discrepancy must be combined with the relevant sensitivity and why norm, perturbation class and requested output matter. The adopted consequence is :4.3/:5.2: derive a bound for the requested error and inspect the inverse action. A bare residual is a cheaper observable but can answer a different question. A proved componentwise or structure-specific estimate can be more informative than a coarse whole-vector estimate; no one condition number is imposed on every problem.

The current [Mathematics in Lean treatment of monotonicity](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html) and [set inclusion](https://leanprover-community.github.io/mathematics_in_lean/C04_Sets_and_Functions.html) makes the quantified preservation steps explicit. It supports :4.3-.4 and the set branch of :5.3. These mechanisms are usable in ordinary proofs or formal checking; choosing Lean is optional.

The synthesis retains the cheapest comparison that supports the requested result and exposes the part of its proof that could be tightened. Reopen it when the domain, objective, available premises or required operation changes, or when a different bound would resolve a still-open use with less work.

### MATH.20:12 - Relations

- **MATH.19** constructs the intermediate inequality or inclusion; **MATH.6** separates a claimed bound from a counterexample.
- **MATH.11** develops invariants that can constrain the unknown; **MATH.17** helps analyze operations used to propagate comparisons.
- **MATH.21** uses bounds to construct limits and obtain sufficient finite approximations.
- **C.29 and MMP** connect the mathematical comparison to the modeled subject.
- Computational methods can use these results in search exclusions, relaxation, approximation and resource analysis.
- FPF's characterization, Pareto and improvement methods use the resulting comparisons to choose the next work.

### MATH.20:End

# Part C - Change a construction and develop its theory

## MATH.11 - Construct an Invariant from Transformation Rules

> **Type:** Method pattern
> **Status:** Usable, evolving
> **Normativity:** Normative unless marked informative

### MATH.11:1 - Problem frame

Use this pattern when a mathematical construction can take many steps and you need a relation that survives every allowed step. Such a relation can rule out a proposed result, constrain a search or derive a formula for a quantity that the steps accumulate.

Here an **invariant** is a function whose value is unchanged by each allowed transformation. The method constructs that function from the transformations. It starts with a small family of expressions, derives conditions on their coefficients and uses the resulting expression in a proof. Conserved weighted totals, polynomial relations and residues provide different ways to carry out that construction.

**First useful move:** write one allowed change, substitute it into a candidate expression and calculate what changes. Derive coefficient conditions that make the change vanish, then include the remaining allowed rules. Once preservation holds for them all, compare the invariant at the starting and proposed states.

The reader needs substitution, elementary algebra and the arithmetic used by the example. The polynomial branch uses collection of like terms and linear equations; the residue branch explains arithmetic modulo two. An available invariant can be used directly after checking that it fits the allowed transformations. When a short explicit sequence already answers the question, constructing an invariant may add no useful result.

### MATH.11:2 - Problem

Trying more sequences can leave a reachability question unresolved. A proposed formula may hold in the first few calculations but fail at a later step or a different branch. Guessing that an unweighted total stays constant can also fail when a rule replaces two units of one kind with three of another.

The difficulty is to obtain a relation from the actual rules and explain why it survives sequences of arbitrary finite length. A useful relation must then answer the question: a constant function is always preserved, but cannot distinguish a reachable proposal from an impossible one.

The result is a constructed invariant with its preservation argument and a consequence for the stated task. A failed search within the chosen expression family can instead identify a reason to change that family or try another method.

### MATH.11:3 - Forces

| Force | Tension |
| --- | --- |
| Short calculation and unbounded sequences | One substitution can establish what every step preserves, but only when it covers all allowed steps. |
| Simple expression and useful distinction | A small expression family is cheap to search, while its invariants may leave the target question undecided. |
| Mathematical rule and implementation | Integer, real and modular arithmetic can preserve different expressions under similar-looking updates. |
| Necessary condition and construction | Different invariant values prove impossibility; equal values can leave ordering and enabling conditions unresolved. |
| General preservation and one starting state | An identity valid for every input is reusable, while a particular reachable set can satisfy further relations. |
| Stable reasoning and changed operations | A changed start may require only a new value; a changed transformation can invalidate the preservation proof. |

### MATH.11:4 - Solution

**Specify the transformations → choose expressions → derive preservation equations → solve and verify → use the invariant → revise the affected part.**

#### MATH.11:4.1 - Specify the states, steps and requested consequence

Let X be the mathematical state set, and write x → y when one allowed step takes x to y. Retain every condition that enables a step and every component of the state that its calculation uses. A rule may be given as y=T(x) with a condition on x, or as a relation allowing several possible successors.

Name the initial state a and the target question. You may need to exclude a particular state b, derive the value of an accumulated quantity after a stated number of steps, or restrict the candidates worth searching.

For an invariant I, the required preservation statement is:

`x → y implies I(y)=I(x).`

It concerns each allowed step. When several rules or branches are available, each needs that equality. If X describes an external process, establish the correspondence between the mathematical steps and that process through C.29.

#### MATH.11:4.2 - Choose a small expression family

Look at what the transformations add, remove or combine. For states represented by counts x1,...,xn, try a weighted total:

`I(x)=w1*x1+...+wn*xn`.

The unknown weights let different kinds contribute differently. For additive changes x → x+d, the change in that total is `w1*d1+...+wn*dn`.

If the update combines variables or changes an accumulated sum, try a few expressions suggested by those operations. For example, an update containing n can make n² useful because `(n+1)^2-n^2=2*n+1`. Write a candidate as `I(x)=c1*p1(x)+...+ck*pk(x)`, where the expressions pi are chosen and the coefficients ci are unknown.

A known invariant, a calculated short sequence or an equation needed at the target can suggest these expressions. Choose only as large a family as the next question warrants. A larger polynomial degree adds unknowns and substitution work.

Choose the value arithmetic too. If the question concerns a remainder, calculate the proposed invariant modulo the relevant integer. That can preserve a distinction which an ordinary rational-valued linear expression misses.

#### MATH.11:4.3 - Derive and solve the preservation equations

For every rule T, calculate `I(T(x))-I(x)` in the chosen arithmetic. Require it to be zero wherever that step is allowed.

For a rule given as a relation, use `I(y)-I(x)` on its allowed pairs. A finite relation supplies one equation per pair; a supplied parameterization gives expressions to substitute. If neither is available, obtaining a usable description of those pairs is the missing construction.

For additive count changes, this gives one linear equation on the weights per change. Solve the equations jointly. If all weights must be zero, this family supplies no distinguishing weighted total.

For polynomial updates and a rational-coefficient polynomial family, expand the difference and collect like monomials. Setting every resulting coefficient to zero gives a linear system in the unknown ci. Solving it constructs polynomial identities that preserve I for every input. On a state set or enabled region smaller than the full polynomial domain, this identity test is sufficient but can be stronger than the preservation actually required. A relation valid only on the reachable states may therefore need another construction.

For example, let X={0,1}, T(x)=x² and I(x)=c*x+d. Requiring the polynomial identity `c*(x²-x)=0` over all rational x forces c=0. On X the two allowed pairs are 0→0 and 1→1; checking them admits I(x)=x. Starting at 0, this invariant excludes 1. Here inspecting the allowed pairs produces a useful invariant within the same linear family.

The simultaneous equations can be solved by substitution in a small case or by linear algebra for a larger one. If several independent solutions are useful, keep them together as a tuple of invariants. A constant solution can be discarded for a target-separation question because it has the same value at every state.

If a tool proposes coefficients, substitute the resulting expression into the original rules. This confirms the identity and the arithmetic to which it applies. A few numerical trials can reveal an error; a proof for all allowed steps needs the corresponding algebraic argument or an exhaustive finite check.

#### MATH.11:4.4 - Prove the consequence for a sequence

Let a=x0 → x1 → ... → xm be any finite allowed sequence. Preservation gives:

`I(xm)=I(xm-1)=...=I(x0)=I(a)`.

Equivalently, use induction on the number of steps: the zero-step state has value I(a), and one more preserving step keeps that value.

Now use the relation. If `I(b)≠I(a)`, no finite allowed sequence reaches b. If an invariant equation determines an output quantity from other known quantities, derive that output under the equation's conditions. When several invariants are retained, every component must agree.

For a set of initial states, compare the target's invariant value with the values of I on that set.

#### MATH.11:4.5 - Resolve what equality leaves open

If the target and start have the same invariant value, the invariant has supplied a necessary condition. To claim reachability, construct an allowed sequence or use a theorem that supplies one under the remaining conditions.

Inspect a failed continuation. A rule may be irreversible, lack the required input units or require an order the invariant ignores. Refine the state or expression when that can answer the question. MATH.1 constructs paths with their intermediate conditions; MATH.8 generates a family when the available transformations form the relevant symmetry action.

When the coefficient calculation yields only constants, state the family actually exhausted. Changing from linear to polynomial expressions or from rational values to residues can change what is found. General polynomial-invariant search has its own algorithms and scope conditions; it is worthwhile when the simpler construction leaves a consequential question open.

Stop with the established formula, impossibility result, useful restriction or identified next construction. A request for one of these results need not expand into finding every invariant.

#### MATH.11:4.6 - Retain the construction through a change

For a changed initial state, retain the preservation equations and recompute the initial invariant value. For a changed target, compare its value using the same proved relation.

For an added or altered transformation, substitute that rule into the current invariant first. If it fails, include the new preservation equation and solve the affected system again. Removing transformations preserves any old invariant, although further invariants may become available.

A change of arithmetic, rounding or retained state can change the algebra itself. Recompute the affected identity before using its consequence. MATH.7 can transport the expression through a reversible representation; MATH.2 addresses an identification that must preserve a requested operation or answer. B.5.RR follows the changed mathematical result through a larger argument.

### MATH.11:5 - Archetypal Grounding

#### MATH.11:5.1 - Derive weights for an exchange construction

States are triples (a,b,c) of nonnegative integer counts. Two rules are allowed:

- Replace two A units with three B units when a≥2: `(a,b,c) → (a-2,b+3,c)`.
- Replace one B unit with one C unit when b≥1: `(a,b,c) → (a,b-1,c+1)`.

Starting with four A units, can the construction end with exactly five C units and nothing else?

The unweighted count changes under the first rule. Try `I(a,b,c)=α*a+β*b+γ*c`. The two differences are `-2*α+3*β` and `-β+γ`. Their joint equations have the solution `(α,β,γ)=(3,2,2)`, giving:

`I(a,b,c)=3*a+2*b+2*c`.

Every allowed step preserves this value. The start (4,0,0) has value 12; the target (0,0,5) has value 10. The target is impossible under the stated rules, however many steps are attempted.

The same invariant helps formulate a useful alternative: six C units have value 12. They are attainable. Apply the first rule twice to obtain (0,6,0), then the second rule six times to obtain (0,0,6). This sequence supplies the contribution that equality of the invariant alone left open.

Now start at (0,3,0) and ask for (2,0,0). Both values are 6, but the first rule cannot create A and the second only consumes B to create C. Thus the requested target is unreachable. Adding the reverse exchange `(a,b,c) → (a+2,b-3,c)` when b≥3 makes that target reachable in one step. Its invariant change is `2*3-3*2=0`, so the old invariant survives while the reachability answer changes.

For a material or operational application, interpret the counted kinds and allowed exchanges before using this mathematical result. The calculated weights express preservation by these rules; identifying them with physical mass or monetary value requires the corresponding subject account.

#### MATH.11:5.2 - Derive an accumulated sum from an update

A construction starts at `(n,s)=(0,0)` and repeatedly applies:

`(n,s) → (n+1,s+n+1)`.

The question is what s will be when n has reached a chosen nonnegative integer. The new term added to s depends on n, so try `I(n,s)=a*s+b*n^2+c*n+d`.

Substitution gives:

`I(n+1,s+n+1)-I(n,s)=(a+2*b)*n+(a+b+c)`.

Set `a+2*b=0` and `a+b+c=0`. Choose `a=2`, `b=-1`, `c=-1` and `d=0`. The resulting invariant is `I(n,s)=2*s-n^2-n`. It starts at zero, so every state reached by the update satisfies:

`2*s=n^2+n`, hence `s=n*(n+1)/2`.

After three steps, (3,6) satisfies it. The proposed state (3,7) has invariant value 2 and cannot result from these updates.

The same relation can be used with a different start. Starting at (2,10) gives invariant value 14, so later states satisfy `2*s-n^2-n=14`. One step produces (3,13), which satisfies that changed equation. The preservation proof is unchanged.

Now change the update to `(n,s) → (n+1,s+2*n+1)`. Substitution into the old invariant gives change `2*n`, so the old formula fails in general. Reusing the same candidate family gives equations `2*a+2*b=0` and `a+b+c=0`. Choose `a=1`, `b=-1`, `c=0`: the new invariant is `s-n^2`. From (0,0), it gives `s=n^2`.

These constructions use integer arithmetic without overflow. They also use the update as a simultaneous substitution: the expression for the new s contains the old n. An implementation that increments n before evaluating that expression would need a different calculation.

#### MATH.11:5.3 - Change the value arithmetic to find a parity obstruction

The state is an integer n. Allowed steps add 2 or subtract 2. Starting at zero, can the construction reach 1?

A rational-valued linear candidate `I(n)=a*n+b` changes by `2*a` under addition of 2. Requiring zero forces a=0, leaving only constants in this family.

Instead take `I(n)=n mod 2`, with values 0 and 1. Both +2 and -2 preserve the remainder. The start has remainder 0 and the target remainder 1, proving impossibility.

Here the necessary condition also leads to a construction. For any even target n=2k, use k additions of 2 when k≥0, or -k subtractions of 2 when k<0. Thus the reachable states are exactly the even integers. The invariant and the explicit sequence establish the two directions of that statement.

Adding the steps +1 and -1 destroys this parity invariant: 0 can now move to 1. Every integer becomes reachable by repeated unit steps. The earlier two-step rules and their parity calculation remain correct, but no longer cover all allowed steps.

### MATH.11:6 - Bias-Annotation

A familiar conserved total can be imposed before examining the transformations. Deriving its weights from each rule makes the assumed conservation testable. A small search can also encourage the claim that no useful invariant exists; retain the searched expression family and arithmetic when interpreting its failure.

An easily generated invariant may have little value for the target question. Compare its values or use its equation to obtain a consequence before investing in a larger repertoire.

### MATH.11:7 - Conformance Checklist

For the construction and use at hand:

1. The state set, initial condition and every allowed transformation are recoverable.
2. The candidate expression family and its value arithmetic are stated.
3. The preservation equations cover all allowed rules, with any stronger polynomial-identity requirement visible.
4. The constructed expression satisfies those equations and gives the stated initial value.
5. The finite-sequence argument supplies the reach of the conclusion.
6. An impossibility claim separates invariant values; a reachability claim also has its sequence or sufficient theorem.
7. A failed invariant search retains the family and scope actually searched.
8. Changes to initial data, target, transformations or arithmetic reopen the corresponding calculation.

Recognition can begin with one rule and a useful candidate expression. Assurance of a general consequence examines the preservation and sequence argument on which that consequence depends.

### MATH.11:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Assuming an ordinary total is preserved by an exchange with unequal counts | Derive weights from the contribution of each rule. |
| Checking only one branch of a construction | Include every allowed branch in the preservation equations. |
| Inferring reachability from equal invariant values | Supply a sequence or a theorem that also resolves enabling and ordering conditions. |
| Calling a constant-only coefficient result proof that no invariant exists | Retain the exhausted family; change expressions or arithmetic when useful. |
| Treating a polynomial identity search as complete for a restricted reachable set | Check preservation on the stated set using a description of its allowed steps. |
| Using a mathematical identity after changing update order or arithmetic | Substitute the implemented rule and recalculate the affected relation. |

### MATH.11:9 - Consequences

A small equation system can replace an unbounded search for an impossible construction. The resulting relation can also derive an output formula or narrow the next construction to candidates consistent with it.

The method's cost depends on the chosen expressions and substitutions. Weighted totals are often inexpensive; polynomial expansion can grow quickly. When an invariant leaves the consequential question open, a constructive path or a different mathematical method may be the better next move.

### MATH.11:10 - Architectural Rationale

The preservation question is local to a transformation, while the useful conclusion concerns any finite composition of transformations. The sequence argument joins those scales. Deriving the expression from the rules supplies the missing step in the advice to “find an invariant.”

Unknown coefficients turn a family of guesses into equations. Weighted counts expose exchange ratios; polynomial terms expose accumulation; residues retain divisibility information. The examples use different arithmetic but the same question: what function stays unchanged, and what does that prevent or determine?

An invariant usually compresses the state. Equality of its values can forget irreversible directions or unavailable inputs, as the exchange example shows. A proof of reachability therefore needs more than this compression. Conversely, different values can close an impossibility question without reconstructing every sequence.

These are mathematical constructions even when their states represent programs, resource transformations or physical models. Their interpretation and use in another subject need the correspondence and premises of that subject. Mathematical construction, subject interpretation and implementation can be divided among contributors while preserving those dependencies.

### MATH.11:11 - SoTA-Echoing

For deriving a condition valid after arbitrarily many steps, **adopt** the induction-based Invariant Principle in Lehman, Leighton and Meyer's *Mathematics for Computer Science*, §5.4.3. Compared with inspecting more executions, :4.4 uses one preservation proof to cover every finite sequence. This pattern constructs an invariant function; the book's principle also covers broader preserved predicates. Stop when the resulting relation answers the question, and reopen if an allowed transition changes. [MIT text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).

For constructing polynomial expressions from update rules, **adapt** Bayarmagnai, Mohammadi and Prébet's *Algebraic and Algorithmic Methods for Computing Polynomial Loop Invariants*, §5, Corollary 5.4 and Algorithm 6. The adopted move substitutes an expression with unknown coefficients and solves the resulting linear equations. It improves on unstructured guessing in :4.2-:4.3 and the sum construction in :5.2. The source's stronger algorithms distinguish invariant form, initial-value conditions and search space. Here the polynomial-identity construction has its stated scope; a restricted reachable-set question can require a different method. Reopen when a richer family or specialized algorithm obtains a more useful relation at acceptable cost. [Extended paper](https://arxiv.org/html/2412.14043v2).

For count transformations, **adapt** the conserved linear expression described by Gopalkrishnan in *Autocatalysis in Reaction Networks*. The weighted-exchange derivation in :5.1 makes such a quantity available instead of assuming an unweighted total. Equal values still require a reachability construction. The source's chemical-network results need their own premises; they are not used to identify the counted kinds in this mathematical example. A changed exchange rule reopens the weight equations. [Author's account](https://johncarlosbaez.wordpress.com/2013/10/11/autocatalysis-in-reaction-networks/).

The three worked constructions and their changed conditions are derived here. The source algorithms do not establish that these mathematical rules describe a particular physical system or implementation.

### MATH.11:12 - Relations

- **MATH.1** constructs permitted paths and retains intermediate state; **MATH.4** constructs witnesses by induction. This pattern constructs a preserved function and uses induction to obtain its consequence.
- **MATH.2** forms identifications under retained operations. Equal invariant values give a possible identification, whose adequacy for another operation remains a separate question.
- **MATH.5** extends a supplied generator assignment through composites. This method instead solves for an assignment that transformations preserve.
- **MATH.7** transports an expression with its structure through a bijection. **MATH.8** generates solution orbits; an invariant can rule out membership but need not distinguish all orbits.
- **B.5.RA** recovers the resulting argument; **B.5.RR** revises its affected dependencies; **B.5.QD** develops the next question from its obstruction or formula.
- **C.29** connects the mathematical result to another subject. **C.11.DUA** helps decide whether a larger invariant search would change the next useful action.

### MATH.11:End

## MATH.13 - Derive a Consequence from a Symmetry

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.13:1 - Problem frame

Use this pattern when a transformation appears to preserve the structure relevant to a problem, and you need to turn that observation into a useful restriction, a transferred solution or a reason that a requested answer cannot be selected from the available information.

A symmetric allocation problem can constrain its unique optimum before a full calculation. An anonymous arrangement can make a unique choice impossible under a stated selection rule. A rotationally symmetric physical law can relate motions with different initial states. The useful consequence depends on what the transformation actually preserves and how the required answer transforms.

A *symmetry* here is an invertible transformation preserving the stated structure. The object of the Method is that transformation together with the problem and answer it acts on. State the structure: preserving a shape, an equation, a criterion or a fully specified problem gives different premises.

The first result is a consequence with its reason: another valid solution, a restriction on possible answers, or a conflict between the input symmetry and the required output. This can reduce a search or identify the additional distinction a computation needs.

The reader needs the problem's conditions and enough subject mathematics to apply the transformation and test its effect. The allocation and selection examples need algebra and permutations. The dynamics example additionally needs differentiation and elementary state updates.

If no symmetry-related conclusion is needed, use the direct calculation. If the live problem is a general change of mathematical representation, C.29.1 supplies result transfer without requiring a symmetry.

### MATH.13:2 - Problem

A suggestive symmetry can omit the feature that decides the problem. Equal-looking components can have different costs. A law can be unchanged while its boundary or initial data change. A function can require its output to rotate with its input rather than stay numerically identical.

A second error begins after a real symmetry is established: the solver assumes more than it implies. A symmetric problem can have several asymmetric solutions. A rotation-respecting numerical scheme can fail to conserve the physical angular momentum. To obtain a usable conclusion, follow the transformation through the actual solution condition.

### MATH.13:3 - Forces

| Force | Tension |
| --- | --- |
| Structure of interest | A transformation can preserve one structure while changing a criterion, condition or distinction needed by the question. |
| Whole problem and law | Symmetry of a law can relate different input problems; a conclusion about one fixed problem needs its data preserved as well. |
| Solution multiplicity | A transformation preserves the solution set, but individual solutions can move within it. |
| Computational saving | Symmetry can reduce repeated work, while the output may need information lost by the reduction. |
| Physical use | A mathematical symmetry can suggest a conserved quantity; its conservation needs the relevant dynamics or theorem. |

### MATH.13:4 - Solution

**Specify the transformation → follow every relevant condition → transform the answer → derive the consequence → use it within those premises.**

#### MATH.13:4.1 - Name what must stay the same and what may transform

Recover the problem: admitted candidates, supplied data, conditions, criterion if there is one, and the required kind of answer.

Choose a transformation g and say how it acts on those participants. A permutation can exchange components; a rotation can change coordinates or rotate a physical configuration. Explain which operation is intended. For a symmetry claim, the transformation must be invertible on the relevant domain and retain the stated structure.

Several transformations may form a group: they include doing nothing, composing transformations and undoing each transformation. Name the action on the objects used by the problem. A familiar group name alone leaves that action unspecified.

Keep supplied data in the comparison. If swapping two components also swaps their different costs, the result can be an equivalent problem with transformed data. It is a symmetry of the fixed original problem only if the data required to remain fixed are preserved.

#### MATH.13:4.2 - Establish the problem-to-solution relation

Apply the transformation to the conditions. Show that an admitted solution is taken to an admitted solution of the stated target problem.

For an optimization problem, check feasibility and the criterion. If g maps the feasible set onto itself and `J(g(x))=J(x)`, it maps every minimizer to a minimizer of that same problem.

For a rule `f:X->Y`, specify the input action g and the corresponding output action r(g). The relation

`f(g(x))=r(g)(f(x))`

is called *equivariance*: transforming the input and then computing agrees with computing and then transforming the output. *Invariance* is the case where the output stays unchanged. Classification of an object and prediction of its position can require these different relations.

For a dynamics law, transform the state, parameters and initial or boundary data. A transformed trajectory may solve the law with transformed data. Establish that correspondence before claiming anything about the solution with the original fixed data.

Use a mathematical argument for the range claimed. A few successful transformations can reveal or test a candidate symmetry; a conclusion covering an entire stated family requires the corresponding preservation argument.

#### MATH.13:4.3 - Obtain the useful consequence

Follow the consequence needed by the question.

**Transfer a solution.** From a known solution x, obtain g(x) and use the preservation argument from :4.2 to establish what problem it solves. Compositions can generate further related solutions. These are distinct answers only when the transformed objects differ under the problem's equality.

**Restrict a unique solution.** If the fixed problem has exactly one solution x, every symmetry g of that problem must satisfy `g(x)=x`: g(x) is a solution, so uniqueness identifies it with x. Solve this fixed-point condition to restrict or find the candidate.

If uniqueness has not been established, retain the weaker result: symmetries move solutions within the solution set. A symmetric candidate may be worth testing, but the existence of asymmetric solutions remains possible.

**Test a requested deterministic answer.** Suppose an input x is fixed by g and the requested rule must be equivariant. Then `f(x)=r(g)(f(x))`. Check whether any permitted output can satisfy that condition for every transformation fixing x. If none can, the requested deterministic rule cannot answer that input under the stated requirements. The missing distinction or incompatible output requirement is a useful result.

These deductions use preservation and, where stated, uniqueness or equivariance. A conservation law along physical time evolution is a different conclusion. Obtain it from the dynamics or the applicable theorem, including its conditions.

#### MATH.13:4.4 - Preserve the information needed for use

When symmetry reduces a calculation, state what the reduced answer means in the original problem.

An invariant output can often be calculated from a representative of a symmetry class. An equivariant output may need the transformation used to choose that representative so the answer can be returned to the original coordinates. If several transformations give the same representative, their different output actions must agree on the returned answer, or the result remains ambiguous.

For example, rotating an image to a standard orientation can help classify the object. Reporting a location in the original image additionally requires the corresponding inverse coordinate transformation. If the task distinguishes orientations, the normalization must retain that information.

Use C.29.1 when establishing this representation-and-return relation is itself the difficulty. Use C.29.2 to construct the actual computation; the existence of a symmetric formulation does not supply an efficient algorithm.

#### MATH.13:4.5 - Return a failed symmetry to its decisive premise

When the comparison in :4.2 fails, identify what changed: an allowed candidate, supplied datum, criterion, output meaning or modeled law. Use that difference to revise the symmetry claim or the problem formulation.

An approximate symmetry can still help, but the allowed discrepancy must be related to the requested result. Establish the bound needed by that use. Small-looking changes are insufficient when they reverse a selection or destroy uniqueness.

After obtaining the consequence, continue with the reduced calculation, transferred solution or revised requirement. Stop when it answers the current question. Add observations or input distinctions only when they can resolve the remaining choice; C.11.DUA supplies the cost-sensitive decision about further work.

### MATH.13:5 - Archetypal Grounding

#### MATH.13:5.1 - A symmetric allocation and an asymmetric optimum

Let `x1,x2>=0`, `x1+x2=10`, and minimize `J=x1^2+x2^2`. Swapping x1 and x2 preserves both the feasible set and J.

The cost is strictly convex on this feasible segment, and a minimizer exists because the segment is compact and the cost is continuous. Hence the minimizer is unique. The symmetry condition requires `(x1,x2)=(x2,x1)`, so the only possible optimum is `(5,5)`. The direct calculation `J(5+h,5-h)=50+2*h^2` confirms it for every feasible h.

Now use `J=x1^2+2*x2^2` under the same resource constraint. Swapping the allocations changes the cost: `J(10,0)=100` and `J(0,10)=200`. The original exchange symmetry is gone. The optimum is `(20/3,10/3)`, as the admissible-variation construction in MATH.10 shows.

Symmetry alone also need not make individual solutions symmetric. If the original sum-of-squares criterion is maximized on the same segment, `(10,0)` and `(0,10)` are both maxima. The swap exchanges them. The midpoint is fixed by the swap but is the minimum, so selecting it from symmetry without the uniqueness and optimization premises would answer a different question.

#### MATH.13:5.2 - A unique choice from an indistinguishable arrangement

A selector receives a three-vertex cycle with identical vertex attributes and equal edge attributes. Its output must designate exactly one vertex. Rotating the cycle is treated as a relabeling: the requested deterministic rule must rotate its selected vertex in the same way.

For this input, a one-step rotation leaves the supplied arrangement unchanged. Equivariance therefore requires the selected vertex to be fixed by that rotation. No vertex is fixed: each moves to the next vertex. The requested deterministic selector has no permitted output for this input.

One repair is to supply a distinguished attribute, such as an available unique priority, and let the rule use it. Another is to change the requested result to the set of all three equally admissible vertices. Random selection is another problem: a uniform distribution can be rotation-invariant even though a sampled vertex is not fixed. The construction of a coordinated random choice would need its own procedure.

This is a mathematical result about the given input and rule requirements. Extra identifiers, timing distinctions or other available attributes can change the input symmetry and therefore the conclusion. It does not establish that every real three-agent arrangement faces this obstruction.

#### MATH.13:5.3 - A symmetry of motion and what a numerical step preserves

Consider the planar model `qdot=v`, `vdot=-q`. Applying the same planar rotation R to q and v preserves these equations. Thus a trajectory starting at `(q0,v0)` produces a rotated trajectory starting at `(R*q0,R*v0)`.

For `q0=(1,0)`, `v0=(0,1)`, a quarter-turn changes the initial data. The transformed trajectory solves another initial-value problem. Uniqueness for the original data therefore does not imply that its trajectory is fixed by every rotation.

In this model, `J=x*vy-y*vx` is angular momentum for unit mass. Direct differentiation gives

`Jdot = x*ay-y*ax = x*(-y)-y*(-x)=0.`

This establishes conservation along its trajectories. A radial law `vdot=-k(t)*q` gives the same cancellation. The proof uses the acceleration relation; the rotational description alone is not the argument.

Now compute with explicit Euler:

`q_next=q+h*v; v_next=v-h*q.`

The update is equivariant under the same rotations because R distributes over the linear combinations. Yet substitution gives

`J_next=(1+h^2)*J.`

Starting with J=1, h=0.1 and taking one hundred steps yields about 2.7048. Rotation equivariance of the scheme has survived while conservation of J has failed. If the question uses angular momentum, the computational construction must be changed or its error made acceptable for that use.

For this model, the update `v_next=v-h*q; q_next=q+h*v_next` preserves J by substitution. Its preservation of this quantity is one property of that scheme; questions about phase or other errors retain their own numerical analysis.

### MATH.13:6 - Bias-Annotation

Visual sameness can distract from a cost, label meaning or boundary datum that distinguishes the cases. Transform those inputs explicitly.

A solver familiar with unique linear problems may carry uniqueness into a problem with several solutions. Keep the solution-set result available until uniqueness has its own basis.

A conserved-looking scalar can also invite the wrong inference from equivariance. Distinguish a quantity unchanged under a spatial transformation from a quantity unchanged as the system evolves. The oscillator computation exposes the practical difference.

### MATH.13:7 - Conformance Checklist

| Question | Passing result |
| --- | --- |
| What structure is preserved? | The transformation, its domain, inverse and action on relevant participants are stated. |
| Which problem is related? | The argument identifies a fixed problem or a problem with transformed data. |
| How does the answer transform? | The solution condition, criterion or required input-output relation is preserved as claimed. |
| What follows from that relation? | The transferred solution, fixed-point restriction or output obstruction follows with its needed uniqueness or equivariance premise. |
| What information must return? | A reduced or normalized calculation can supply the output in the required interpretation. |
| What changes the conclusion? | The decisive datum, constraint, output requirement or law is identifiable when the symmetry fails. |

### MATH.13:8 - Common Anti-Patterns and How to Avoid Them

| Text-invited mistake | Repair |
| --- | --- |
| Swap components but ignore their different costs. | Apply the transformation to the complete criterion and identify whether the data remain fixed. |
| Infer a symmetric individual solution from a symmetric solution set. | Establish uniqueness or retain the whole transformed family of solutions. |
| Rotate a law while silently keeping changed initial data as the same problem. | Track the transformed initial or boundary values. |
| Demand an invariant output when the task needs an equivariant position or direction. | Specify and apply the output action. |
| Normalize an input and lose the original coordinate relation. | Retain the transformation needed to return the answer or expose the remaining ambiguity. |
| Infer physical conservation from an equivariant update alone. | Derive the quantity's change along the actual dynamics or numerical step. |

### MATH.13:9 - Consequences

Symmetry can reduce calculation, generate useful related solutions or expose an impossible selection requirement before implementing a solver. The preservation argument also locates what new information would make a choice possible.

The main cost is identifying the relevant structure and following the transformation through the whole problem. Large or continuous symmetry groups may require substantial mathematical methods. The direct consequence obtained here can make that further work worthwhile or show that the simpler calculation already suffices.

### MATH.13:10 - Architectural Rationale

The Method follows a transformation through a problem and its answer. This keeps a visible symmetry from becoming an unrestricted claim about every quantity or every use.

The fixed-point argument is particularly useful because it converts invariance of the input into a restriction on the answer. Uniqueness and equivariance enter at the point where that conversion needs them. Keeping those premises explicit makes the same reasoning useful in optimization, mathematical construction and computational selection.

A dynamics symmetry, a conservation theorem and a numerical method can contribute to one physical answer while doing different work. The oscillator case retains that connection and exposes where a valid property is lost during computation. A specialized construction of Noether quantities or structure-preserving integrators is a further Method when that result is required.

### MATH.13:11 - SoTA-Echoing

The selected approach defines the structure and input-output action before using symmetry. It supports direct algebra for a small problem and provides the premise for more specialized group, optimization or numerical constructions.

[Bronstein, Bruna, Cohen and Veličković, *Geometric Deep Learning*, draft chapter 3, §§3.1-3.2](https://geometricdeeplearning.com/book/algebraicpriors.html) develops symmetries as invertible structure-preserving maps and distinguishes invariant and equivariant outputs. Adopt that explicit action and output discipline. Whether a transformation preserves a label or target still comes from the modeled task. Architecture construction and learning-performance claims need the corresponding further Methods and evidence.

[Tong, *Classical Dynamics*, §2.4](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) derives conserved quantities from continuous symmetries of a Lagrangian using its equations of motion. The useful contribution is the extra argument connecting symmetry with time evolution. The simple oscillator calculation above performs that connection directly; it does not substitute for the wider Noether construction.

[Hairer, *Geometric Numerical Integration*, lecture 2, §1](https://www.unige.ch/~hairer/poly_geoint/week2.pdf) supplies the symplectic Euler formulas and their Hamiltonian conditions. The direct comparison above shows why a requested invariant must be examined under the actual numerical update. A different model or requested accuracy can favor a different scheme.

C.29.1 supplies the general result-transfer comparison. The fixed-point and selection constructions here make one specific consequence available without a full group-theory survey. Revisit the use when its structure, output meaning, uniqueness premise or transformation law changes.

### MATH.13:12 - Relations

- **C.29** establishes the mathematical interpretation and its return to the working subject.
- **C.29.1** constructs the preservation and recovery of a result through a changed representation.
- **MATH.10** derives consequences from changes that retain constraints; symmetry additionally preserves the specified structure or criterion.
- **C.29.2 and C.29.3** connect a computation with its represented operations and realization.
- **A.3.3.TR** constructs state change from the available laws. **B.5.MPC** connects that physical account with mathematical and computational contributions.
- **B.5.RR** revises reasoning after a premise changes. **C.39** helps obtain a missing construction or reformulate an obstructed result.

### MATH.13:End

## MATH.8 - Generate a Solution Family by Symmetry

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.8:1 - Problem frame

Use this pattern when a mathematical solution is known and transformations that preserve its defining conditions can produce further useful solutions. You may need related roots of an equation, arrangements considered equivalent under rotation, or answers to problems whose data have been permuted.

Start with the known solution and one proposed transformation. Apply it and establish which problem the result solves. This can return another answer immediately, expose changed data, or identify a condition that the transformation fails to preserve.

A *symmetry* is an invertible transformation preserving the structure named by the problem. Its *orbit* at an object is the family of objects reached by the chosen group of transformations. The construction below obtains that family, distinguishes repeated objects, and explains what is still missing from a claim to have found all solutions.

The reader needs sets, functions, elementary equations and composition. The required group-action rules are stated below. The polynomial example uses factorization; the finite-arrangement example needs only binary strings and rotation. Use a direct calculation when it already supplies the needed answer. A transformation that changes the problem can still transfer a solution to the changed problem when that is useful.

### MATH.8:2 - Problem

Several transformed answers can be repetitions of one object. An orbit can also omit whole families of solutions. Conversely, a supposed symmetry can change a coefficient or boundary datum that the original problem holds fixed.

The mathematical task is to obtain solutions with a stated reach. This requires the transformation's action on both data and candidate answers, an argument that it preserves the solution condition, and a way to identify the objects its repeated use actually reaches.

### MATH.8:3 - Forces

| Force | Tension |
| --- | --- |
| Reusing one solution and finding all solutions | Transformations reuse a known answer, but another answer may lie in a different orbit. |
| A law and a fixed problem | Transforming the data can preserve the form of a law while changing the problem being solved. |
| Many transformations and distinct objects | Different transformations can return the same object. |
| Reduced calculation and returned information | Treating an orbit as one case can simplify an invariant question while losing an orientation or label needed by another result. |

### MATH.8:4 - Solution

**Specify the actions → preserve the solution relation → transform a known solution → construct its orbit → establish the family's reach → return the needed answer.**

#### MATH.8:4.1 - Specify the problem and the transformations

Write the solution condition as `S(d,x)`: candidate x solves the problem with data d. State the data that are held fixed, the domain of candidates and the equality used to distinguish answers. An equation, a feasibility condition or a minimum under a stated criterion can provide S.

Give the transformations and their actions on d and x. For a group G, the action satisfies `e*x=x` and `(g*h)*x=g*(h*x)`; the same rules apply to the data action. Here e is the identity transformation, and multiplication in G means composition, with h applied first. Every g has an inverse. A supplied family of permutations can make these rules immediate.

If the group is given by generating transformations, include their inverses and retain the relations they must satisfy. MATH.5 can construct an action from generator images that respect those relations. Listing generators without their action leaves the proposed symmetry undecided.

For a fixed datum d, retain only transformations with `g*d=d`. These form its stabilizer: the subgroup of transformations that leave that datum unchanged. Include compositions when finding this subgroup: the two-mark case in :5.2 is fixed by a half-turn although a single turn changes the marks. A larger group can relate different data instances, which is a different useful calculation.

#### MATH.8:4.2 - Establish the solution-preserving relation

Show that `S(d,x)` implies `S(g*d,g*x)` for every transformation and candidate in the claimed range. Applying the same implication to the inverse gives the converse. The transformation therefore pairs the two solution sets.

For an equation, substitute the transformed variables and data. For several constraints, preserve each one used by the solution. An optimization result needs both transformed feasibility and the corresponding criterion: if feasible candidates are paired bijectively and `J_(g*d)(g*x)=J_d(x)`, a better transformed candidate would return a better original candidate. Thus a minimizer transfers.

Preservation for generating transformations and their inverses extends to every finite composition by applying the implications successively. Use MATH.4's finite-construction argument when that extension needs explanation. A check on a few candidate values establishes only those cases unless a general argument is also available.

If a transformation fails, retain the first changed condition and decide whether the changed problem is useful. MATH.6 can exhibit the failure; FPF C.29 relates the mathematical correspondence to another subject when one is involved.

#### MATH.8:4.3 - Generate related solutions and remove repetitions

From a known solution x, calculate `g*x` and return it with the data `g*d`. To obtain solutions of the original fixed problem, use its data stabilizer from :4.1.

For a chosen group H acting on the same fixed problem, define the orbit:

`H*x={h*x | h in H}`.

All its members solve that problem by :4.2. Compare the resulting objects using the problem's equality; distinct transformation expressions can give equal answers.

With a finite list of generating transformations, a finite orbit and decidable equality, generate the orbit by closure. Start with x. Apply each generating transformation and its inverse to every newly found member, adding only previously absent results. Once every stored member has been processed and no new one appears, the set is closed under the generators and inverses. Every finite word in them stays in that set, so it is the whole generated orbit.

This procedure terminates when the reached orbit is finite and the stated operations return. For an infinite orbit, a formula such as `{h*x | h in H}` with a usable parameterization can be the result. A stopped enumeration without closure supplies only the reached subset.

#### MATH.8:4.4 - Explain duplicates and the limit of one orbit

The transformations fixing x form its stabilizer `H_x={h in H | h*x=x}`. Two transformations give the same answer precisely when the composition of one with the other's inverse fixes x:

`h1*x=h2*x` exactly when `(h2^-1*h1)*x=x`.

Choose one transformation h0 in H. All transformations returning the answer `h0*x` have the form `h0*k` with k in H_x: composing with k leaves x unchanged, and any h giving that answer satisfies `h0^-1*h` in H_x. These sets of transformations are called the left cosets of the stabilizer. They partition H, and each contains as many transformations as H_x, since multiplication by h0 is reversible. Therefore, for finite H, the number of distinct answers is `|H|/|H_x|`. Use this count when it helps construct or check the requested family; explicit comparison can be simpler for a small example.

One orbit contains exactly the answers reachable from its starting member under H. To claim all solutions, establish that every solution belongs to a represented orbit. This can use a complete finite classification, a mathematical reduction, or an argument that H acts transitively on the solution set, meaning that every solution is reachable from the starting solution. Finding no new member in the current orbit proves its closure, not that another orbit is absent.

When another solution lies outside the family, use it as the starting member of another orbit. A property unchanged by every transformation can show that two candidates cannot belong to the same orbit. Such a property can also suggest what a wider transformation group would need to change.

#### MATH.8:4.5 - Use an orbit representative without losing the requested result

A quantity constant on each orbit can be calculated from any representative. To define additional operations on orbit classes, use MATH.2's representative-independence condition; an orbit partition by itself only supplies classes.

When a problem is solved using representative data d0 and solution x0, retain a transformation g with `g*d0=d` for the requested data d. Return `g*x0`. If two transformations satisfy `g1*d0=g2*d0=d`, an answer independent of that choice requires `g1*x0=g2*x0`. A disagreement identifies information that the representative alone does not supply.

MATH.13 supplies the fixed-point restriction on a unique solution and the test for an impossible equivariant choice. Those questions require the output action and, for the unique-solution deduction, a justified uniqueness premise. Generating a solution set here does not select one member from it.

Stop with the requested related solution, complete orbit, orbit classification or identified failure of preservation. When data, constraints or the output change, reopen the affected action and preservation argument before reusing the family. A more costly enumeration or symmetry computation is useful only if it can improve the receiving result.

### MATH.8:5 - Archetypal Grounding

#### MATH.8:5.1 - An even polynomial has more than one solution orbit

For real x, solve `P(x)=x^4-5*x^2+4=0`. The two transformations are identity and sign reversal `r(x)=-x`. Since `P(-x)=P(x)`, they preserve the equation.

The known solution 1 gives the orbit `{1,-1}`. Applying sign reversal again returns to 1, so this orbit is complete. It is not the complete root set: 2 also solves the equation and belongs to the different orbit `{2,-2}`.

Factorization `P(x)=(x^2-1)*(x^2-4)` establishes that these two orbits cover all real roots. Symmetry generated each pair; factorization supplied the missing completeness argument.

Now change the equation to `Q(x)=x^2+x-2=0`. The value 1 remains a root, but `Q(-1)=-2`. The linear term breaks the sign symmetry. Reusing the old transformation would give a false answer to the changed problem.

#### MATH.8:5.2 - Binary arrangements on a cycle

Consider binary strings of length four with exactly two entries equal to 1. Positions are numbered 0 through 3 around a cycle. Let r move each entry to the next position, wrapping the last to the first. Four rotations return the original string, and rotation preserves the number of ones.

Starting with `1100`, repeated rotation gives:

`1100 -> 0110 -> 0011 -> 1001 -> 1100`.

There are four distinct members. Only the identity rotation fixes `1100`, agreeing with the count `4/1=4`.

Starting instead with `1010` gives:

`1010 -> 0101 -> 1010`.

A rotation by two positions fixes either alternating string. Its stabilizer has two members, so the orbit count is `4/2=2`.

Every two-one string either has adjacent ones around the cycle or has opposite ones. This covers the six possible strings and separates the two orbits. If the question asks for arrangements up to rotation, two representatives suffice. If it asks for every labeled string, return all six.

If position 0 receives a distinguished mark that must remain fixed, only the identity rotation preserves that data. The old orbit classification then forgets a distinction required by the new problem. The strings remain available; their identification must change.

Instead put identical marks at positions 0 and 2, with neither mark distinguished from the other. A single rotation and its inverse move the marked set to {1,3}; a half-turn returns it to {0,2}. The data stabilizer is therefore {e,r²}. To find this subgroup, examine compositions such as r² as well as the supplied generators.

#### MATH.8:5.3 - Permuting coefficients changes which equation was solved

Let the data be coefficients `a=(2,1)` and right-hand side 5. The equation is `2*x1+x2=5`, with known solution `x=(1,3)`.

The swap sends `a` to `(1,2)` and x to `(3,1)`. Their scalar product remains 5 because both positions are exchanged. Thus the transformed solution satisfies `x1+2*x2=5`.

Keeping the original coefficients instead gives `2*3+1=7`. The swap preserves the relation between transformed data and transformed solutions; it does not preserve this fixed original equation.

For comparison, `x1+x2=5` has equal coefficients. Its data are fixed by the swap, so a solution `(1,4)` gives another solution `(4,1)` of the same equation. Neither the swap nor the equation singles out one of them. A requirement for one distinguished answer needs an additional criterion or a compatible choice method.

For a representative-data calculation, take coefficients (1,2) and its solution (3,1). The swap maps those data back to (2,1) and the solution back to (1,3), recovering the original answer. With the equal coefficients (1,1), both identity and swap return the same data, while the chosen solution (1,4) returns as either (1,4) or (4,1). Each is a valid solution, but this choice does not define a transformation-independent rule. This ambiguity concerns the chosen pair; a request for a swap-fixed solution can instead use (5/2,5/2).

### MATH.8:6 - Bias-Annotation

Finite permutations make complete orbits cheap to display. Infinite and continuous actions can instead require symbolic parameterizations, different equality procedures or further mathematical methods. The complete finite examples therefore establish their own construction, while the general group argument states what can be reused.

Familiar visual symmetry can also hide supplied labels or coefficients. The equation and marked-cycle cases keep those data in the comparison.

### MATH.8:7 - Conformance Checklist

- The actions on the data and candidates satisfy the claimed composition and inverse rules.
- The preservation argument uses every condition required by the solution.
- Each returned solution is attached to its unchanged or transformed data.
- Distinct orbit members are distinguished by the problem's equality.
- A complete-orbit claim has closure or a corresponding argument; an all-solutions claim covers the other possible orbits too.
- A representative retains the information required to recover the requested answer.

### MATH.8:8 - Common Anti-Patterns and How to Avoid Them

**Close one orbit and declare the equation solved.** The polynomial has two complete sign orbits. Supply the additional classification or restrict the returned claim to the generated family.

**Count transformation expressions as different solutions.** The alternating string is fixed by a half-turn. Compare objects or use the stabilizer to account for repetition.

**Transform variables while silently retaining changed data.** Swapping variables and coefficients preserves the linear relation; swapping only the variables can fail it. Return the corresponding data with the solution.

**Use every old rotation after a mark is added.** The fixed mark changes the permitted subgroup. Recompute the identification from the new data.

**Return a normalized answer without its coordinate relation.** An invariant quantity and an equivariant answer need different return information. Retain the transformation or expose the remaining ambiguity.

### MATH.8:9 - Consequences

A known solution can supply a useful family without solving every transformed case independently. Orbit closure and stabilizers explain both the family and its repetitions. Separate orbits reveal a remaining construction problem rather than an apparent lack of progress in the same enumeration.

The gain depends on the cost of finding and applying the transformations. For a small isolated equation, direct calculation may finish sooner. For repeated or related questions, the shared preservation argument can save substantial work; the construction alone does not quantify that saving.

### MATH.8:10 - Architectural Rationale

The method builds a solution family from an action and a preservation relation. Keeping data inside that relation distinguishes transformations of one fixed problem from transformations between problems of the same form.

Generating the orbit and classifying all solutions answer different questions. The finite-closure argument explains when generation is complete; a stabilizer explains repeated results; another representative or reduction accounts for a missing orbit. These operations keep useful mathematical content beyond the instruction to notice a symmetry.

MATH.7 constructs operations through an arbitrary bijection. Here the transformations act on a specified problem and preserve its solution relation. MATH.5 can construct the action from assigned generators, while MATH.2 controls additional operations on identified results. The same orbit can support different receiving questions without giving its quotient every operation of the original set.

A direct solution, an existing orbit classification or a supplied parameterization is preferable when it already supplies the requested result. The group construction earns its cost when related answers, reduced cases or the reach of a family matter.

### MATH.8:11 - SoTA-Echoing

**Question:** how can transformations construct related mathematical solutions while retaining data, distinguishing repetitions and establishing the reach of the family?

Milne's [*Group Theory*, version 4.01, November 2025](https://www.jmilne.org/math/CourseNotes/GT.pdf), chapter 4, definition 4.1, the orbit discussion and proposition 4.7/corollary 4.8, supplies actions, orbit partition and the stabilizer description of an orbit. **Adopt** those mathematical relations. The procedure here makes finite generation, returned data and the separate all-solutions question explicit.

[Bronstein, Bruna, Cohen and Veličković, *Geometric Deep Learning*, chapter 3, §3.1](https://geometricdeeplearning.com/book/algebraicpriors.html) distinguishes the structure preserved by an automorphism from a change to an isomorphic object. **Adapt** that distinction to a relation between problem data and solutions. A fixed mark or coefficient can change the available symmetries.

The selected construction competes with direct calculation or a ready classification. It is useful when one preservation argument replaces repeated solution work or exposes omitted families. Direct calculation remains sufficient for a single easy result. The finite examples demonstrate closure and incomplete coverage; they make no comparative performance claim for a solver or learning system.

Reopen when the action, data, solution relation, equality procedure or requested return changes. A more effective orbit-generation or canonicalization method can replace the finite implementation while retaining its required mathematical result.

### MATH.8:12 - Relations

- **Uses MATH.1 and MATH.5:** compose generating transformations and construct an action that respects their relations.
- **Uses MATH.4:** extend preservation through finite compositions and justify the finite-closure result.
- **Uses MATH.2:** decide which further operations remain defined on orbit classes.
- **Connects with MATH.6:** exhibit a changed condition or a counterexample to a completeness claim.
- **Connects with MATH.7:** compare an arbitrary representation change with an action preserving a given structure.
- **Uses C.29 for another subject:** recover what the mathematical transformation and returned solution mean there.
- **Uses MATH.13 when the requested answer is unique or must be chosen equivariantly:** obtain its fixed-point restriction or an obstruction under the stated premises.
- **Uses B.5.QD and C.11.DUA when continuation matters:** choose a useful missing family, new transformation or further calculation.

### MATH.8:End

## MATH.9 - Determine Whether and How a Choice Rule Can Respect Symmetry

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.9:1 - Problem frame

Use this pattern when a mathematical rule must choose an answer and transforming the input should transform that answer in the corresponding way. Examples include selecting an element after relabeling a configuration, returning a direction after rotating geometric data, and choosing a solution from problems related by a symmetry.

Start with one transformation that leaves the supplied input unchanged. Ask which permitted answers it leaves unchanged too. This can identify an admissible answer or expose an impossible choice before a selector is implemented.

The method then constructs a rule from one suitable answer for each represented input orbit. It also uses uniqueness, when established, to restrict a solution to the points fixed by the input's symmetries. A useful result is a compatible choice rule, a restricted candidate to calculate, or a requirement that must change.

The reader needs sets, functions, composition and elementary algebra. MATH.8 supplies group actions, orbits and stabilizers; the definitions needed for the choice argument are restated here. The plane example uses vector length and rotation. If a supplied rule already has the required correspondence, apply it. If the task accepts any answer in the given coordinates and requires no symmetry relation, use an ordinary selection method.

### MATH.9:2 - Problem

A problem can allow several answers while supplying no distinction that a requested deterministic rule is allowed to use. An arbitrary tie-break can then violate relabeling or rotation consistency.

Normalization can hide the same difficulty. Two transformations may put the input into the same representative form but return a proposed answer to different places. A common representative alone leaves that choice unresolved.

The task is to determine which permitted outputs respect the symmetries of the supplied input, then extend those choices consistently to related inputs.

### MATH.9:3 - Forces

| Force | Tension |
| --- | --- |
| One answer and indistinguishable alternatives | A deterministic output may require a distinction absent from the input. |
| A symmetric problem and its individual solutions | Symmetry preserves the solution set; uniqueness supplies the additional step that fixes an individual solution. |
| Reduced input and returned coordinates | The transformation used for normalization can affect an output even when the normalized input is unchanged. |
| Pointwise consistency and other requirements | A rule can satisfy the transformation law while its evaluation is expensive or its values change discontinuously. |

### MATH.9:4 - Solution

**State the permitted answers and their transformation → find the input stabilizer → choose a permitted fixed answer → extend it along the orbit → construct the needed scope → return the rule or revise the obstructed requirement.**

#### MATH.9:4.1 - State the input, permitted answers and transformation law

Let D be the inputs and Y the possible outputs. Write A(d) for the subset of outputs permitted for input d. An admissible root, minimizing allocation or selected vertex can define this subset.

Give a group G acting on both D and Y. Its action satisfies `e*d=d` and `(g*h)*d=g*(h*d)`, with analogous rules for outputs; every transformation has an inverse. Different actions on input and output can use the same group elements.

Establish that the permitted answers transform with the input:

`A(g*d) = g*A(d)`,

where `g*A(d)` means the set of `g*y` for y in A(d). MATH.8 supplies the solution-preservation argument when it has to be constructed.

The requested deterministic rule f must satisfy both f(d) in A(d) and

`f(g*d)=g*f(d)`.

This relation is *equivariance*. If the requested output stays unchanged under the transformations, use the trivial output action `g*y=y`; the relation then expresses invariance.

Keep attributes that the rule is allowed to use inside d. A distinguished label, orientation or mark can change the stabilizer and the existence of a choice. A coordinate label that merely changes under relabeling cannot silently serve as a fixed priority.

#### MATH.9:4.2 - Find the permitted answers fixed by the input's stabilizer

The stabilizer of d is the subgroup

`K_d = {g in G | g*d=d}`.

For every g in `K_d`, equivariance requires `f(d)=g*f(d)`. Thus the permitted answers for an equivariant rule at d are

`B(d) = {y in A(d) | g*y=y for every g in K_d}`.

To construct B(d), first obtain the transformations fixing the supplied data, then solve their fixed-point conditions together with membership in A(d). For a finite supplied group and a finite decidable answer set, enumerate those elements and test them. When either is infinite, use an algebraic description or another available construction; a failed finite search leaves the unsearched range open.

If B(d) is empty, no deterministic equivariant rule can answer this input under these requirements. Return the input symmetry and the fixed-output condition that permitted answers fail. This result concerns the supplied data and output requirement; it identifies what a repair must change.

If the original problem has a unique permitted answer y, its preservation under `K_d` forces every `g*y` to equal y. The fixed-point equations can therefore restrict or find that answer. Establish existence and uniqueness on the range used by this deduction. With several permitted answers, use the same fixed-point calculation to find a compatible choice; it need not recover every permitted answer.

#### MATH.9:4.3 - Extend a selected answer over one input orbit

Choose representative data d0 and an answer y0 in B(d0). For input d in the orbit of d0, obtain g with `d=g*d0` and define

`f(d)=g*y0`.

The answer is permitted because the relation in :4.1 carries A(d0) to A(d). It is independent of the transformation used. Indeed, if `g1*d0=g2*d0`, then `k=g2^-1*g1` fixes d0. Since k fixes y0,

`g1*y0=g2*(k*y0)=g2*y0`.

The rule is also equivariant: for another transformation q,

`f(q*(g*d0))=(q*g)*y0=q*f(g*d0)`.

This constructs the entire rule on that orbit. To evaluate it, retain a way to find g, or an equivalent formula for f(d). An existence argument for g alone may leave the computation unresolved.

If a normalization procedure instead supplies h with `h*d=d0`, return `h^-1*y0`. Keeping the direction of this transformation prevents returning a coordinate answer in the normalized frame. The position-selection case in :5.4 carries out both inverse returns.

#### MATH.9:4.4 - Cover the requested input range

For a finite group acting on a finite input set, enumerate input orbits as in MATH.8. Pick one representative d0 per orbit, compute B(d0), choose one of its members and extend it by :4.3. This supplies a rule on every processed orbit. Empty B(d0) blocks a total rule on a range containing that orbit.

For a larger or infinite range, give the representative construction and a compatible answer for each orbit needed by the claimed rule. These choices can be supplied by formulas or previously established mathematical results. Pointwise nonempty B(d) alone has not provided an evaluation algorithm or the choices across an arbitrary infinite family.

When an existing direct formula can be checked against A(d) and equivariance, use it without building an orbit table. The stabilizer argument can still expose a failed input or explain why its tie-break works.

Before returning the rule, check the other properties actually requested for it. If a geometric or learned model must vary continuously with its data, continuity requires its own argument: the pointwise construction here permits unrelated choices on different input orbits. If the result will be computed repeatedly, compare its evaluation cost with the available direct rule.

#### MATH.9:4.5 - Repair an obstructed choice

Choose the change that answers the receiving problem.

A supplied distinguished attribute can reduce the stabilizer. Include that attribute and its transformation in the new input, then repeat the fixed-output test. The marked-cycle case below constructs such a rule.

A different output may retain the alternatives the input leaves open. Returning the whole set A(d) respects its induced transformation from :4.1. When A(d) is finite and nonempty, a uniform probability distribution on it does too, if a distribution is the requested result. Sampling a single value is a further calculation with its own randomness and comparison requirement.

An average is usable only when it belongs to the permitted output set and has the required transformation law. The mean of two opposite unit directions is zero, which fails a unit-direction requirement.

The receiving task may instead allow coordinate-dependent choice or a narrower input range. State that changed requirement and construct the corresponding rule. Adding distinctions or weakening a requirement is useful only when the resulting answer serves that task; C.11.DUA helps decide whether obtaining further input is worth its cost when that question is unresolved.

#### MATH.9:4.6 - Return the result and reopen its changed premise

Return the rule with its input range, permitted output and transformation law, or the obstruction that changes the choice problem. A known unique solution can return a smaller fixed-point calculation instead.

When a criterion, attribute or output changes, recalculate the affected stabilizer and fixed-output condition. Retain orbit calculations and proofs whose premises are unchanged. Small perturbations can remove a tie and reverse a selected answer, so use the changed criterion when the choice depends on it.

Use FPF C.29 to establish what this mathematical result means for another subject. The obstruction for an abstract arrangement leaves available attributes and interventions in a real arrangement to that subject comparison.

### MATH.9:5 - Archetypal Grounding

#### MATH.9:5.1 - Select a cheapest position on a cycle

Four positions are arranged in a cycle with a given clockwise direction. A rule receives real costs c=(c0,c1,c2,c3) and must select one minimum-cost position. Relabeling by k moves position j to j+k modulo 4 and moves its cost with it. The selected position must move in the same way.

Take c=(1,3,1,3). Its minimizers are {0,2}. A half-turn leaves c unchanged but exchanges both permitted answers. Neither is fixed, so B(c) is empty. A deterministic rotation-equivariant selector cannot answer this input. Choosing the smallest coordinate label returns 0 both before and after the half-turn, whereas equivariance requires the result to move to 2.

Now supply a marked position m as part of the input. Choose, among minimizers, the one with least clockwise distance

`dist_m(j)=(j-m) modulo 4`,

using the values 0,1,2,3. The distances are distinct, so this gives one answer. Under joint rotation of costs, mark and position, `dist_(m+k)(j+k)=dist_m(j)`. The rule therefore respects rotation for every cost vector and mark.

With c=(1,3,1,3) and m=3, the distances of minimizers 0 and 2 are 1 and 3, so the rule selects 0. Rotating once gives costs (3,1,3,1), mark 0 and selected position 1. The same reasoning applies to every rotation.

For the unmarked input, returning {0,2} is a compatible set answer. If a probability distribution is wanted, assign probability 1/2 to each of those positions. Both alternatives retain the choice left open by the input.

A change of costs can also settle it: (1,3,0.9,3) has the unique minimizer 2; (1,3,1.1,3) has the unique minimizer 0. Their closeness to the tied input does not preserve that input's fixed-point obstruction. It also exposes a discontinuity for a rule required to return one minimizing index as these costs vary through the tie.

#### MATH.9:5.2 - Restrict a unique optimum by exchange symmetry

Let x1,x2 be nonnegative real numbers with x1+x2=10, and minimize J=x1²+x2². Exchanging the two allocations preserves feasibility and cost.

If the minimizer is known to exist uniquely, the exchange must fix it. Hence x1=x2, and the constraint gives the candidate (5,5). For this example, existence, uniqueness and its optimality can also be established directly: every feasible point has the form (5+h,5-h), and

`J(5+h,5-h)=50+2h²`.

The minimum is attained only at h=0. The direct calculation can finish this small problem; the symmetry deduction is reusable when uniqueness has another available justification.

If the same J is maximized on the segment, its maxima are (10,0) and (0,10). The exchange moves one to the other. Its fixed midpoint is the minimum, so the fixed-point equation alone would solve the wrong optimization question.

Now minimize x1²+2x2² with the same resource constraint. Exchange changes the criterion. Substituting x2=10-x1 gives

`J=3*(x1-20/3)²+200/3`,

so the unique optimum is (20/3,10/3). The old equality x1=x2 no longer follows. MATH.10 supplies the more general admissible-variation construction when the remaining optimization is the difficulty.

#### MATH.9:5.3 - Return a direction after geometric normalization

The input is an unordered pair P={-v,v} of opposite nonzero vectors in the plane. The requested answer is one of the two unit directions along its axis. Rotating the input should rotate the selected direction.

For P0={(-1,0),(1,0)}, a half-turn leaves the pair unchanged and negates every permitted unit direction. No permitted output is fixed, so a rotation-equivariant deterministic direction cannot be selected from this input.

The same failure appears in normalization. Both the identity and a half-turn map P0 to the same standard pair. Selecting (1,0) there and undoing those transformations returns opposite directions. The standard pair did not determine a direction of return.

Returning both directions, `{-v/|v|,v/|v|}`, is compatible with rotation when that set is the required output. Averaging them returns zero, whose length is zero rather than one.

Alternatively, mark one endpoint w in P and return `w/|w|`. Every rotation R preserves length, so `R*w/|R*w|=R*(w/|w|)`. The marked-input rule is therefore equivariant. It answers a question with additional supplied information, which the unmarked pair lacked.

#### MATH.9:5.4 - Choose a position despite an ambiguous normalization

Let the six permutations of positions 1, 2 and 3 act on the triples formed by permuting d0=(a,a,b), where a and b differ. An answer may be any of the three positions, and relabeling the triple must relabel the answer.

The transformations fixing d0 are the identity and the swap of positions 1 and 2. All three positions are permitted answers, but only position 3 is fixed by both transformations. Thus B(d0)={3}; choose y0=3.

For the input d=(a,b,a), two transformations normalize it to d0. The first, h1, swaps positions 2 and 3. The second, h2, sends positions 1 to 2, 2 to 3 and 3 to 1. Both carry the b entry to position 3 while placing the two a entries in the remaining positions.

Returning y0 uses their inverses:

`h1^-1(3)=2=h2^-1(3).`

For every permutation of d0, the transported answer is the position carrying b. This gives the rule on the entire three-input orbit. The stabilizer calculation makes the return independent of the normalizer even though the input initially permits three different answers.

### MATH.9:6 - Bias-Annotation

Finite cycles make an obstruction or a constructive repair cheap to display. Larger symmetry groups can make stabilizers, representatives or their transformations expensive to obtain. The rule's mathematical existence and a feasible evaluation procedure remain different contributions.

A symmetry claim also depends on what is actually supplied. Position names used only for coordinates differ from a distinguished mark the problem permits the rule to use. Keep that difference when translating a real selection problem into the mathematical input.

### MATH.9:7 - Conformance Checklist

- The permitted-answer set and both group actions belong to the declared input range.
- The solution relation carries A(d) to A(g*d).
- A selected representative answer is permitted and fixed by the representative's whole stabilizer.
- Different transformations reaching the same input return the same answer.
- The claimed range has the required representative and answer construction.
- Any changed input, output type or choice requirement is reflected in the returned rule.

### MATH.9:8 - Common Anti-Patterns and How to Avoid Them

**Use coordinate order as an unannounced priority.** The cycle's smallest-label tie-break fails a half-turn. Supply a distinguished priority that the task permits, or return the alternatives.

**Infer a symmetric optimum from a symmetric feasible set.** Preserve the criterion and establish the premise needed for the fixed-point deduction. The sum-of-squares maximum and weighted minimum give different answers.

**Normalize the input and discard the transformation.** An answer in source coordinates needs the inverse return. If several normalizing transformations remain, check their agreement on the proposed output.

**Average valid answers into an invalid answer.** The zero mean of opposite unit directions is outside the required output set. Test the averaged result's membership or retain the set.

**Call a compatible pointwise rule continuous.** The cycle's minimizing index jumps near a tie. Apply the receiving regularity requirement when it is part of the task.

### MATH.9:9 - Consequences

A fixed-output calculation can prevent work on an impossible selector and identify what information or output change would make it possible. Where a compatible answer exists, the orbit construction turns it into a reusable rule for related inputs.

Different representatives can support different valid rules. Their evaluation cost, continuity and usefulness for a receiving task can differ even when each satisfies equivariance. The mathematical construction supplies a comparison basis; the receiving requirements select the rule.

### MATH.9:10 - Architectural Rationale

The stabilizer condition is necessary because transformations invisible at the input must leave a deterministic answer unchanged. It is sufficient for extension over one orbit because those same transformations account for every ambiguity in how that orbit is reached. The construction supplies both the impossibility result and its positive counterpart.

MATH.8 generates solution families from an action. This method selects a compatible member and extends that selection across related inputs. A unique solution supplies the fixed-member condition automatically, but several permitted solutions can still contain a suitable fixed member.

A canonical input and a normalizing transformation are different outputs. Choosing the same input representative throughout an orbit is an invariant operation. Recovering an oriented answer additionally uses a transformation and its output action; :5.3 shows why that transformation may not be unique.

Orbit-by-orbit construction is preferable when its fixed-point test settles existence or produces a useful rule. A direct formula can avoid representative search. Set or distribution outputs answer different questions, and geometric continuity can require a construction beyond the pointwise rule.

### MATH.9:11 - SoTA-Echoing

**Question:** when does a symmetry-compatible deterministic choice exist, how can it be constructed, and which changed requirement resolves an obstruction?

[Milne, Group Theory v4.01, November 2025](https://www.jmilne.org/math/CourseNotes/GT.pdf), chapter 4 and exercise 4-1 with its solution, characterizes maps between transitive group actions through stabilizers. **Adopt** that mathematical relationship. The argument in :4.2-:4.4 develops it as a construction constrained by the permitted-answer set. [Mathlib's fixed-point action results](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/FixedPoints.html), including MulActionHom.map_mem_fixedPoints, supply the corresponding necessary preservation property.

[Ma and colleagues, A Canonicalization Perspective on Invariant and Equivariant Learning, 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/702b67152ec4435795f681865b67999c-Paper-Conference.pdf), §2.1, distinguishes canonicalized inputs from a single equivariant group-valued canonicalizer, which can be obstructed at inputs with nontrivial stabilizers. **Adapt** this distinction in :4.3/:5.3/:10. It gives a concrete alternative to assuming normalization has selected a unique return transformation.

[Dym, Lawrence and Siegel, Equivariant Frames and the Impossibility of Continuous Canonicalization, 2024](https://arxiv.org/html/2402.16077), §2.2, separates orbit and group canonicalization and examines continuity; §6 retains stabilizer-related conditions when extending weighted constructions to equivariant outputs. **Adopt** the separate regularity question in :4.4. Their weighted-frame methods address additional geometric-learning requirements; they are not replaced by the finite construction here.

An arbitrary tie-break is cheaper but can fail the requested transformation law. A supplied direct rule with that law is preferable when it already works. The orbit construction earns its cost by revealing impossible outputs or generating a consistent rule. The cases demonstrate those differences; they do not compare runtimes of geometric-learning implementations.

Reopen when the input attributes, action, permitted answer, demanded regularity or available construction changes.

### MATH.9:12 - Relations

- **Uses MATH.8:** obtain the action, solution-preservation relation, input orbits and stabilizers.
- **Uses MATH.2:** check independence when a calculation is defined on identified inputs; the stabilizer argument supplies the concrete independence proof here.
- **Connects with MATH.7:** carry a computed answer through the appropriate inverse map, including its output interpretation.
- **Connects with MATH.13:** use the existing unique-solution and output-obstruction deductions; this method also constructs the compatible rule.
- **Uses MATH.10 when optimization remains:** construct admissible variations after symmetry has restricted a candidate.
- **Uses C.29 for another subject:** recover which supplied attributes and outputs the mathematical choice represents.
- **Uses C.11.DUA when further information has a material cost:** decide whether acquiring the distinction can improve the receiving choice.

### MATH.9:End

## MATH.10 - Improve a Mathematical Candidate or Derive a Necessary Condition by Admissible Variation

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### MATH.10:1 - Problem frame

Use this pattern when you have a candidate allocation, shape, history or other mathematical construction under constraints, and need to find an improving change or a condition that an optimum or stationary construction must satisfy.

For example, two allocations obey the same resource limit, but it is unclear how moving some resource between them changes the criterion. Or a proposed physical history has fixed endpoints, and you need to find what its action principle requires of the motion between them. In both cases, construct changes that preserve the relevant constraints, calculate their effect and determine the strength of the resulting conclusion.

The subject of the Method is a family of admissible mathematical candidates and the change of a stated scalar quantity over that family. A *variation* is a specified change within the family; *admissible* means that the changed candidate satisfies the conditions retained for this question.

The first useful result is an improving candidate, a necessary condition, a justified minimum or maximum, or a located obstacle to obtaining one. A necessary condition can narrow a search even when it does not settle the optimum.

The reader needs the candidate, its constraints, the quantity being compared and the mathematical operations used to calculate its change. Elementary algebra is enough for the allocation example. The history example additionally uses differentiation and integration. A specialist can supply a construction or theorem at the step where that preparation is needed.

If an available evaluation of a few fixed alternatives already answers the question, use that comparison. This Method is useful when constructing the allowed changes or reasoning from them is the difficulty.

### MATH.10:2 - Problem

Changing one value independently can leave the allowed set. A derivative calculated in that direction can then recommend an impossible change. Even with admissible directions, a zero first derivative can describe a maximum, a saddle point or a flat comparison; further reasoning is needed for a minimum.

The reverse difficulty occurs at a constraint boundary: an optimum can have a nonzero derivative because the improving direction is unavailable. A calculation that discards the allowed parameter range loses that conclusion.

These errors share a missing connection between what can vary, what the variation does to the quantity and what the examined family establishes about the original question.

### MATH.10:3 - Forces

| Force | Tension |
| --- | --- |
| Preserved conditions | A convenient change is easy to calculate, but it must retain the constraints used by the conclusion. |
| Local information | A first-order change can expose a useful direction cheaply; stronger conclusions can require finite changes, further terms or a theorem. |
| Coverage | A small family can reveal an obstruction, while a claim about every candidate needs a reason that the family or argument covers them. |
| Form of the candidates | Discrete choices, smooth vectors and histories support different kinds of variation. |
| Use of the result | A mathematical improvement can guide a decision or a model construction; its application still depends on the meaning of the criterion and constraints. |

### MATH.10:4 - Solution

**Construct an admissible family → calculate the change → derive the condition → establish what it settles → use or revise the result.**

#### MATH.10:4.1 - Fix the comparison

State the candidate, the conditions to retain, the scalar quantity and the conclusion sought. Write the candidate as `x` and the quantity as `J(x)` when that notation helps. For minimization, smaller values of J are preferred; for maximization, reverse the comparisons below.

Keep the meaning of J visible. It might be a supplied allocation cost, an approximation error or a physical action functional, which assigns a number to a history. A physical principle can require stationarity of an action without selecting its minimum. Recover that principle and its conditions before using the variational calculation to describe physical behavior.

Distinguish a search for one improving change from a claim of local or global optimality. Local optimality concerns a specified neighborhood of the candidate; global optimality concerns all candidates admitted by the problem.

#### MATH.10:4.2 - Construct changes that remain admissible

Build a family `x(h)` with `x(0)=x`. State the allowed values of the parameter h and substitute the family into the constraints. The parameter may be a scalar, a vector or a discrete choice.

For a fixed total `x1+x2=b`, the change `(x1+h, x2-h)` preserves the total. If both components must stay nonnegative, its range is `-x1 <= h <= x2`. A further capacity limit can shorten that range.

For a history with fixed endpoint values, try `q_h(t)=q(t)+h*eta(t)`, where eta vanishes at both endpoints and has the regularity required by the functional. Check any additional path constraint as well.

A direction tangent to a constraint may preserve it only to first order. At `(1,0)` on the unit circle, `(1,h)` has squared length `1+h^2` and leaves the circle whenever h is nonzero. The curve `(cos(h),sin(h))` stays on it. Use an admissible curve for a finite comparison, or keep a tangent calculation at the first-order scope its mathematical argument supports.

When a useful family cannot yet be constructed, the missing result is concrete: a parameterized change that retains the named constraint. Obtain the corresponding mathematical construction rather than continue with an inadmissible substitute.

#### MATH.10:4.3 - Calculate the effect of the variation

Form the difference

`DeltaJ(h) = J(x(h)) - J(x(0)).`

Substitute the whole changed candidate, including dependent values. Simplify enough to determine the sign or magnitude relevant to the question.

For a differentiable comparison with a scalar parameter h near zero, write

`DeltaJ(h) = a*h + r(h), with r(h)/h -> 0,`

when that expansion is justified. The coefficient a is the first variation along this family. Higher-order terms or a bound on the remainder can be needed when a vanishes, or when choosing a finite step.

A derivative tells how sufficiently small changes behave under its limit assumptions. To select a particular step, check the finite difference or a bound that covers that step. For a discrete family, compare its admissible members directly; differentiability is not an entry requirement.

If the calculation uses a numerical approximation, relate its error to the sign or comparison being used. C.29.2 develops that computational task. A difference interval entirely below zero can establish improvement for minimization; an interval spanning zero leaves that comparison unresolved.

#### MATH.10:4.4 - Derive a condition with the allowed directions

For minimization, an admissible h with `DeltaJ(h)<0` supplies an improvement. For a local conclusion, use families whose candidates approach the base candidate as h approaches zero, under the neighborhood notion of the problem.

At a local minimum, a differentiable family allowing sufficiently small changes of both signs must have `a=0`: a positive or negative a would give a decrease in one of those directions. If only small nonnegative h are allowed, the necessary condition is `a>=0`. For other parameter domains, test the directions actually available.

When a is zero, inspect the remaining change. The differences `h^2`, `-h^2` and `h^3` all have zero derivative at zero but respectively give a minimum, a maximum and neither on a two-sided neighborhood. This distinction changes whether the candidate is selected, rejected or needs a stronger argument.

For a vector of variation parameters, keep their joint constraints. Checking one coordinate at a time can miss an improving combination.

#### MATH.10:4.5 - Establish the reach of the conclusion

Say which candidates the family reaches and which conclusion the calculation proves.

If every admissible candidate can be represented by a member of the family, and `DeltaJ(h)>=0` throughout its allowed domain, the base candidate is a global minimizer. If equality occurs only for the base candidate, it is the unique minimizer. An argument restricted to a neighborhood establishes the corresponding local result.

A narrower family can still supply an improving candidate or a necessary condition. Extending that condition to a stronger conclusion requires coverage of the relevant variations or an applicable sufficiency theorem. A convexity argument can sometimes supply the latter; recover its hypotheses before using it. Repeated failure of a chosen local move supplies no general global-optimality guarantee.

For a physical action, derive the stationarity condition required by the physical model. Establish a minimum only if the functional and allowed histories support that stronger conclusion. The free-history example below does so by a nonnegative finite difference.

#### MATH.10:4.6 - Return the result to the working question

Use the obtained change or condition in the calculation, model or decision that needed it. Keep the admissible family and the reason for the conclusion in the explanation so another practitioner can alter the comparison.

When a criterion changes, recalculate its difference. When a constraint changes, rebuild the parameter domain or family first. B.5.RR helps revise the dependent reasoning while retaining what remains valid.

The mathematical comparison can be completed before any physical change is performed. B.5.MPC supplies the return to physical interpretation and use. If the question is whether an actual intervention causes a result, C.28 supplies the causal-use question.

Stop at the result sufficient for the current use. An improving feasible candidate can be enough to continue; a demand for the global optimum calls for the stronger argument.

### MATH.10:5 - Archetypal Grounding

#### MATH.10:5.1 - Reallocate a fixed total, then change the criterion

Allocate ten divisible units between two uses: `x1>=0`, `x2>=0` and `x1+x2=10`. The supplied cost is `J=x1^2+x2^2`. Take the admissible family `(x1+h,x2-h)`, with `-x1<=h<=x2`.

Substitution gives

`DeltaJ(h)=2*(x1-x2)*h+2*h^2.`

For an interior candidate, both signs of small h are allowed. The first-order condition gives `x1=x2`, hence `(5,5)`. At this candidate, the entire finite difference is `2*h^2`. Every feasible allocation is `(5+h,5-h)` for `-5<=h<=5`, so this proves the unique global minimum, with cost 50.

Now change the cost to `J=x1^2+2*x2^2`, retaining the total and nonnegativity. The same family gives

`DeltaJ(h)=2*(x1-2*x2)*h+3*h^2.`

The condition becomes `x1=2*x2`, giving `(20/3,10/3)`. Its difference is `3*h^2` across the whole feasible interval, so its cost `200/3` is the unique minimum. Keeping the earlier equal split would miss the change introduced by the new criterion.

If the units must instead be whole, x1 and x2 are integers. Completing the square gives `J=3*(x1-20/3)^2+200/3`; the admissible integer closest to 20/3 is 7. Thus `(7,3)` has the lowest cost, 67, in that discrete problem. The continuous stationary point helped locate the candidates; the integer comparison settles their use.

Keep the weighted cost `J=x1^2+2*x2^2`, make the units divisible again, and add `x1<=6` while retaining the total and nonnegativity. The previous continuous minimizer `(20/3,10/3)` is now unavailable. At `(6,4)`, the allowed family has `-6<=h<=0` and

`DeltaJ(h)=-4*h+3*h^2>=0.`

This family covers every newly feasible allocation. Thus `(6,4)`, with cost 68, is the unique global minimizer despite its nonzero derivative along the unrestricted line. The parameter domain carries the decisive information.

These are calculations for the stated cost model. Its use in an allocation decision requires the supplied cost to represent the consequence being compared.

#### MATH.10:5.2 - Compare histories between fixed endpoints

Consider a one-dimensional free particle with mass `m>0`, elapsed time `T>0`, and fixed positions `q(0)=0`, `q(T)=L`. The model's action is

`J[q] = integral from 0 to T of (m/2)*(qdot(t))^2 dt.`

Take the straight history `q0(t)=L*t/T`. For any continuously differentiable eta with `eta(0)=eta(T)=0`, construct `q_h(t)=q0(t)+h*eta(t)`. Expanding the square gives

`DeltaJ(h) = (m*h*L/T)*integral eta_dot(t) dt + (m*h^2/2)*integral eta_dot(t)^2 dt.`

The first integral is `eta(T)-eta(0)=0`. The remaining term is nonnegative, and it vanishes for a changed history only when its derivative change is identically zero; the fixed endpoints then force the change itself to vanish. Every continuously differentiable history with these endpoints can be expressed as q0 plus such a change. The straight history therefore uniquely minimizes this functional over that class.

The construction exposes the reason: the fixed endpoints remove the cross term, while every remaining velocity deviation adds a nonnegative contribution.

Now include a restoring potential. In dimensionless variables, use the harmonic-oscillator action `J[q]=integral from 0 to 2*pi of (qdot^2-q^2)/2 dt`, with `q(0)=q(2*pi)=0`. At the history `q=0`, every admissible family `q_h=h*eta` has zero first variation. Yet the admissible directions `eta=sin(t/2)` and `eta=sin(3*t/2)` give respectively `DeltaJ=-3*pi*h^2/8` and `DeltaJ=5*pi*h^2/8`: integration uses `integral eta^2 dt=pi` and `integral eta_dot^2 dt=n^2*pi/4` for these directions with n=1 and n=3. Arbitrarily small changes of both lower and higher action are available. The stationary history is therefore a saddle, not a minimum.

Changing an endpoint condition also requires rebuilding the allowed histories before reusing the free-particle argument. Its vanishing cross term depended on both endpoint values.

This example uses a supplied classical model. Constructing an appropriate action for an unfamiliar physical system is a further physical and mathematical modeling task.

### MATH.10:6 - Bias-Annotation

A convenient coordinate can make some changes easy to express and hide others. State what the chosen family reaches before treating its result as a property of all candidates.

A modeler can also import minimization from an allocation problem into a physical action principle. Recover whether the subject requires improvement, an extremum or stationarity; the same variation calculation supports different conclusions under those premises.

For a search procedure, separate a failure to find a better local move from a proof about the full feasible set. This matters when discrete choices or disconnected regions prevent the chosen family from reaching other candidates.

### MATH.10:7 - Conformance Checklist

| Question | Passing result |
| --- | --- |
| What is being compared? | The candidate, retained conditions, scalar quantity and sought conclusion are stated. |
| Which changes are allowed? | Substitution or another applicable argument establishes the family's admissibility and parameter domain. |
| What does the change do? | The difference, first variation or bounded numerical comparison is obtained for that family. |
| Which directions matter? | Boundary and joint-parameter constraints remain in the sign or stationarity argument. |
| How strong is the conclusion? | The reached candidate class and the argument distinguish improvement, necessity, local optimality and global optimality. |
| What follows in use? | The receiving calculation or decision can use the result, or the missing construction is located. |

### MATH.10:8 - Common Anti-Patterns and How to Avoid Them

| Observed or text-invited mistake | Repair |
| --- | --- |
| Vary each allocation independently while retaining a fixed-total claim. | Couple the changes so the total remains fixed and derive their allowed range. |
| Use a tangent displacement as a finite feasible move on a curved constraint. | Construct a feasible curve or retain only the first-order conclusion supported by the tangent argument. |
| Accept a zero derivative as a minimum. | Determine the remaining change or use a sufficiency theorem with its hypotheses. |
| Reject a boundary optimum because its unrestricted derivative is nonzero. | Test the available one-sided or constrained changes. |
| Apply a small-step sign to an arbitrarily large step. | Calculate the finite difference or bound the remainder over that step. |
| Declare global optimality after testing one restricted family. | Supply the missing coverage or limit the conclusion to that family. |

### MATH.10:9 - Consequences

A constrained comparison becomes a reusable calculation. It can expose a feasible improvement, reduce an optimization problem to a condition or explain why a proposed change cannot help.

The main effort is constructing a useful admissible family and establishing the sign over the range needed by the conclusion. The Method permits an early useful result; full optimization is a larger task when the working question demands it. Keeping the family and argument makes later changes of criterion or constraints easier to handle.

### MATH.10:10 - Architectural Rationale

The admissible family, change calculation and conclusion are separated because each can fail independently. A correct difference can describe impossible candidates. An admissible comparison can yield only a necessary condition. A strong mathematical result can still use a criterion that does not answer the practitioner's question.

Finite differences provide the direct comparison whenever they are manageable. Derivatives expose local structure economically, and sufficiency theorems can extend that information under additional hypotheses. Keeping these routes connected lets the reader use the least machinery that obtains the needed result.

The same construction spans a resource allocation and a continuous history. What carries across is the preservation of conditions and reasoning from the resulting change. The cost model and the physical action retain their different origins and uses.

### MATH.10:11 - SoTA-Echoing

For a constrained comparison, the selected approach is to construct feasible changes before interpreting their effect. Direct substitution is useful for small expressions; differential conditions and numerical optimization become useful as the candidate class or calculation grows. The choice depends on the result needed and the assumptions available.

[Boyd and Vandenberghe, *Convex Optimization*, §4.2.3](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=153) gives the differentiable convex case: the gradient's inner product with every feasible displacement characterizes optimality. Adopt its attention to the feasible set and the hypotheses that make a first-order condition sufficient. The Method above also admits nonconvex and discrete comparisons, where that sufficiency cannot be inherited. Specialized convex formulations and algorithms remain useful external constructions when their inputs fit.

[Tong, *Classical Dynamics*, §2.1](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) develops variations of a history with fixed endpoints and the resulting Euler-Lagrange equations. Adopt the explicit endpoint conditions and the distinction between stationary action and a minimum. This is an established classical source; it supplies neither an action for every new physical system nor its empirical justification.

C.29 supplies the mathematical interpretation and return, while C.29.2 supplies computational formulation and error-sensitive use. Here the reusable contribution is construction of the admissible family and the argument from its change. If those operations require a specialized variational, optimization or physical-modeling technique, recover that technique at the point where the needed result becomes specific.

Revisit the construction when constraints, regularity, candidate class or the required conclusion change. A newer solver can improve cost without changing the meaning of the admissibility and optimality claims.

### MATH.10:12 - Relations

- **C.29** connects the mathematical candidates and conclusion to the original subject and working question.
- **C.29.1** establishes the transfer of a result when a change of representation could lose a relevant distinction.
- **C.29.2** constructs a computation and relates numerical error to the comparison being used.
- **B.5.RC and B.5.RA** help recover a needed mathematical construction or argument; **B.5.RR** revises dependent reasoning after a premise changes.
- **B.5.MPC** connects the physical account, mathematical construction, computation and use. **C.28** handles a causal consequence attributed to an intervention.

### MATH.10:End

## MATH.21 - Construct an Object through Convergent Approximations

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.21:1 - Problem frame

Use this pattern when a number, function, infinite structure or other mathematical object is to be obtained from increasingly informative constructions, and the work needs to establish what their limit is and what can be done with it. A formula, finite prefix or finite family can describe an approximation even when the object it describes is infinite.

The governing question is what the receiving argument or operation must retain as approximation improves. Examples include a value within a tolerance, the settled first part of an infinite sequence, or a function whose integral or derivative can be obtained from approximating functions. These requests can require different notions of convergence.

**First useful move:** state one requested observation or operation on the intended object, then find a condition under which an approximation supplies it. A shrinking interval can answer a numerical tolerance request. A compatible prefix can answer a request for finitely many entries. This gives a usable result before constructing every property of the limiting object.

The reader needs elementary reasoning about functions, sequences and inequalities. The numerical case introduces its use of real completeness; the function case also uses elementary differentiation. Other spaces require the knowledge needed to state their convergence and operations.

Use an already supplied object or applicable limit theorem when it answers the question. Use the fuller method when existence, retained structure, or use of a finite approximation remains unresolved. Physical adequacy and computational realization add their own questions to the mathematical construction.

### MATH.21:2 - Problem

Finite stages can look increasingly satisfactory while leaving the mathematical result undetermined. The intended limit may be absent from the chosen space. Agreement at each fixed input may fail to control all inputs together. An operation valid on every stage may cease to be valid at the limit.

Even established convergence can leave a practical question open: which stage supplies the requested result? Conversely, a finite observation can be available before an entire limiting construction has been resolved. The method must connect the convergence claim to the particular subsequent use.

### MATH.21:3 - Forces

| Force | Tension |
| --- | --- |
| Finite access | A finite construction can supply an observation of an infinite object without exposing all its properties. |
| Choice of space | A sequence can have a limit in a larger space while lacking one among the originally admitted objects. |
| Strength of convergence | A stronger condition can preserve more operations but require unnecessary work for a weaker request. |
| Representation | Different approximation families can construct the same object; their operations must respect that identification. |
| Existence and obtaining | A theorem can establish a limit while leaving the procedure for a requested approximation unspecified. |
| Reuse | An established convergence theorem saves work when its hypotheses match the new construction. |

### MATH.21:4 - Solution

**Local mantra:** name the limiting object and its next use; construct the approximation family; choose and establish convergence; obtain the object in the admitted space; carry only the justified properties and operations; return a sufficient finite result or the remaining mathematical question.

#### MATH.21:4.1 - State what approximation must preserve

Name the space of intended objects, the approximating objects and how the latter are compared with the former. If they initially have different kinds, supply an embedding or interpretation. For example, a rational number can approximate a real number; a finite word can determine the beginning of an infinite word.

State the requested result. Does the receiver need a value, an operation on the limit, an existence theorem, or a finite observation? For a numerical use, specify the error quantity and tolerance. For a prefix use, specify which entries must be settled. The mathematical question determines the approximation requirement.

Choose a convergence notion that supports that result. In a metric space, with distance d, a sequence x_n converges to x when, for every positive epsilon, all sufficiently late terms satisfy d(x_n,x)<epsilon. For functions, pointwise convergence allows the sufficiently late index to depend on the input; uniform convergence requires one index to work for all inputs in the named set. For infinite words, convergence can mean eventual agreement on every fixed finite prefix.

These are different constructions of the convergence requirement. Use their definitions to decide what they permit. Numerical distance is useful when it measures the requested difference; finite observation or another mathematical relation can be more suitable elsewhere.

#### MATH.21:4.2 - Construct and compare the finite stages

Give the approximating rule and establish the relations on which improvement depends. For nested intervals, prove containment and decreasing width. For compatible prefixes, prove that later stages retain the earlier entries. For a series or iterative construction, obtain a bound on the unresolved remainder.

The same argument must cover the stages used by the conclusion. A finite sample can suggest a bound or expose a failure; a claimed statement about all later stages needs the corresponding argument.

When the candidate limit is not yet available, a Cauchy condition can express progress using only the approximations. In a metric space it says: for every positive epsilon there is N such that d(x_m,x_n)<epsilon whenever m and n are at least N. This compares the entire remaining tail.

If a stopping rule uses only successive changes, derive how they bound the remaining tail. Successive changes of size 1/n become small, yet their accumulated sum is unbounded. A summable bound, a contraction estimate or another proved remainder relation can make a successive-change test useful.

Retain a cheaper construction when it already supplies the requested observation. Refinement need not improve every property at every stage.

#### MATH.21:4.3 - Obtain the limit where it is needed

If a candidate object is already available, prove convergence to it by the selected definition or a suitable theorem. Otherwise use an existence result whose conditions the approximation satisfies.

For example, completeness of a metric space means that every Cauchy sequence in it has a limit there. Establishing a Cauchy condition and applying a known completeness result can obtain an object without guessing its closed form. A local existence argument may suffice even when the whole space is incomplete.

When the limit falls outside the original objects, decide whether the receiving work admits an extension. Construct the new objects and the embedding of the old ones; prove the properties the subsequent work will use. One route takes suitable Cauchy sequences as representations and identifies those whose mutual distance tends to zero. MATH.2 supplies the quotient operation: operations on equivalent representatives must produce equivalent outputs, so the quotient result is independent of the representative. The real-number construction is one instance of this route.

Establish uniqueness when the receiver needs a single result. In a metric space, if x_n tends to both x and y, the triangle inequality gives d(x,y)≤d(x,x_n)+d(x_n,y); the right side can be made arbitrarily small, so x=y. Other convergence structures need their own uniqueness condition or an explicitly retained class of possible limits.

If convergence or existence fails, return the failed condition and the still valid finite information. That can suggest a different space, a different approximation family, or a weaker requested conclusion.

#### MATH.21:4.4 - Pass properties and operations through the limit

For every operation used next, establish the relevant interchange. If F is continuous for the chosen source and target convergence, x_n→x gives F(x_n)→F(x). The argument can be local to this family; global continuity is sufficient in many cases but is more than every use needs.

Check the property actually consumed. A limit of objects in a closed subset remains in that subset. Other properties can disappear: finite words padded with zeros can converge to an infinite word with infinitely many ones.

For a function limit, distinguish a claim about its values from a claim about integration or differentiation. The required limit theorem may ask for uniform control, domination, or another hypothesis specific to the operation. In :5.3 a uniform value bound supports integration over a finite interval, but it does not support differentiating the approximations to obtain the limiting derivative.

When an interchange fails, retain the established limit and repair the affected operation. Strengthen the convergence condition, choose another family, restrict the domain, or calculate that operation by a different argument. Select the repair from the receiver's need.

#### MATH.21:4.5 - Obtain a sufficient finite result

Translate the receiving request into a condition on a stage. If an established bound gives d(x_n,x)≤e_n, a stage with e_n within the requested tolerance supplies the approximation. For nested numerical intervals, the midpoint has error at most half their width. For compatible prefixes, a stage containing all requested entries supplies them.

When execution must find that stage, provide either an obtaining rule or a recognizable stopping condition with a reason it will be reached. An explicit rate of convergence is one option. An enclosure whose width can be checked during refinement may suffice without a rate fixed in advance.

A residual is useful only through its established relation to the requested error. A small equation residual can accompany a large error in the unknown; the comparison needed by the use must connect them.

Return the approximation with the mathematical bound or settled observation it supplies. If only existence has been established, retain that result and identify the missing obtaining procedure for a computational continuation. Numerical conditioning, finite arithmetic and execution cost belong to that continuation.

#### MATH.21:4.6 - Use and revise the construction

Use the limiting object in the argument, or use the finite result for the selected observation. Keep the convergence notion and any condition needed by the next operation with that use.

A changed tolerance can require a later stage. A changed operation can require a stronger convergence result. A changed space can remove existence or uniqueness. Reopen the affected argument and retain the finite constructions and proved consequences that survive.

In modeling, interpret the resulting mathematical consequence against the subject using C.29 and the corresponding modeling method. The approximation's mathematical convergence and its ability to answer the subject question remain separately assessable.

### MATH.21:5 - Archetypal Grounding

#### MATH.21:5.1 - Obtain a real object from rational intervals

The task is to construct a positive number r with r²=2 and obtain rational approximations with a chosen absolute error.

Start with l_0=1 and u_0=2. At each step take the rational midpoint m. If m²≤2, replace the lower endpoint by m; otherwise replace the upper endpoint. Squaring is increasing on the positive interval, so each step retains l_n²≤2≤u_n². The intervals are nested and their widths are 2⁻ⁿ.

The lower endpoints form a bounded increasing sequence. In the real numbers, their supremum r exists. Each l_n≤r≤u_n: every later lower endpoint is at most u_n, and earlier ones are no larger than l_n. The shrinking width makes this r the only common point.

Both r² and 2 lie between l_n² and u_n². Since the endpoints stay between 1 and 2, the width of this squared interval is (u_n-l_n)(u_n+l_n)≤4·2⁻ⁿ. It tends to zero, so r²=2. This obtains the desired object without presupposing a square-root value to drive the construction.

After four bisections the interval is [22/16,23/16]. Its midpoint 45/32 differs from r by at most 1/32. For a smaller tolerance epsilon, choose a stage with 2⁻ⁿ⁻¹≤epsilon, or refine until the interval width is at most twice epsilon.

**Changed space.** If the result must remain rational, existence fails. In a fraction p/q in lowest terms, p²=2q² would make p even, and then q even, contradicting lowest terms. The rational approximations and their widths remain available, but they construct a real number rather than a missing rational solution. The next decision concerns admitting that extension or retaining a finite rational answer.

#### MATH.21:5.2 - Construct an infinite word and return a finite observation

Let p_n be a binary word of length n, with p_n a prefix of p_(n+1). Positions start at zero. Define b(k) to be entry k of p_(k+1). Compatibility makes that entry agree with every later prefix, so b is an infinite binary word whose first n entries are p_n.

For a common space of approximations, pad each p_n with zeros to obtain an infinite word b_n. Use convergence by eventual agreement on each finite prefix. For a request about the first m entries, every b_n with n≥m agrees there with b. This proves convergence and gives the return stage: p_m supplies those entries. Any calculation depending only on them, such as their count of ones, can use that finite result.

The global property "has only finitely many ones" does not pass to this limit. Take p_n to consist of n ones. Each zero-padded b_n has finitely many ones, but b has a one at every position. A question about a fixed finite prefix is settled; a question about the entire tail needs another argument.

The construction uses a consistency relation between finite stages and a rule for obtaining every entry. Its computational realization additionally needs a way to obtain the required p_m. Merely knowing that such prefixes exist does not supply their generator.

#### MATH.21:5.3 - Preserve values and integrals, then inspect differentiation

For n≥1, let f_n(x)=sin(nx)/n on [-1,1]. The inequality |f_n(x)|≤1/n holds for every input in the interval. Thus the functions converge uniformly to f(x)=0.

For a requested value error epsilon, n≥1/epsilon is sufficient. Integration over the interval is also controlled: the absolute integral of f_n-f is at most 2/n, by the interval length and the uniform bound. This estimate supplies an integral-error result without depending on cancellation of positive and negative values.

Now ask for the derivative at zero. Each f_n has derivative cos(nx), so f_n'(0)=1 for every n. The limit function has f'(0)=0. The value convergence therefore fails to justify passing this operation through the limit, even at that one point.

One possible sufficient repair, for differentiable functions on a common open interval, is pointwise convergence of the functions together with locally uniform convergence of their derivatives. A suitable limit theorem then identifies the limiting derivative. The present f_n fail that condition. If the construction can change, a family with controlled derivatives can support the stronger use; if it must stay fixed, obtain the derivative of its limit by another argument.

The result retains uniform convergence and its finite value and integral bounds. Only the derivative interchange has been refused. This is why the requested next operation belongs in the initial choice of approximation.

### MATH.21:6 - Bias-Annotation

Numerical examples can make convergence look like increasing decimal accuracy. The prefix case exposes another form: agreement on finitely many observations of an infinite object. Function examples show that even numerical convergence has different strengths according to the subsequent operation.

The examples use ordinary classical mathematics. An effective or constructive account must retain the obtaining information its logic and representation require. A user of a known complete space can apply its theorems directly; a constructor of a new space must establish the relevant properties of that construction.

### MATH.21:7 - Conformance Checklist

For the proposed construction:

- The intended space, approximation family and comparison between their objects are stated.
- The receiving observation or operation determines the convergence requirement.
- The general argument covers the stages claimed, including the unresolved tail when it matters.
- The limit exists in the admitted space, or the required extension is justified.
- Uniqueness and representative independence are established where the subsequent use needs them.
- Each retained property or limit interchange has its applicable condition.
- A finite return supplies the requested error or observation; an executable return has an obtaining or stopping rule.
- A failed condition leaves the remaining valid construction and a useful next question identifiable.

### MATH.21:8 - Common Anti-Patterns and How to Avoid Them

**Small increments used as a tail bound.** The harmonic increments in :4.2 shrink while their sum grows. Derive a remainder estimate before using such an increment to decide that the requested approximation has been reached.

**An absent limit treated as an object of the original space.** The intervals in :5.1 have no rational point in common. Admit the real extension or return a finite rational approximation.

**A property inherited merely because every stage has it.** Each padded word in :5.2 has finitely many ones; its limit does not. Establish preservation for the particular property.

**A value approximation used for a different operation.** The functions in :5.3 approximate values uniformly but supply the wrong limiting derivative at zero. Inspect the interchange needed by the operation.

### MATH.21:9 - Consequences

The method can obtain new objects, justify a finite use of them, and localize the reason a proposed use fails. A family can remain valuable even when one requested operation does not pass to its limit.

Changing the space, convergence relation or preserved operation can open a further mathematical problem. Those changes also create different modeling and computational possibilities, whose additional costs and subject conditions can then be compared.

### MATH.21:10 - Architectural Rationale

Approximation is a construction through a relation between stages and a result. The relation determines what information accumulates and what a finite stage can supply. This explains the common method across rational intervals, prefixes and functions without making their convergence definitions interchangeable.

Existence, identification of equivalent constructions, preservation of operations and finite return are connected tasks. Quotient construction handles identification; proof construction supplies missing implications; convergence and continuity supply the limiting passage. Keeping their contributions explicit lets a changed operation reopen the relevant mathematical step.

A stronger notion of convergence is useful when it supports a needed consequence. A weaker one is sufficient when it already supplies the receiver's observation. This permits economical use of mathematical results while preserving their conditions.

### MATH.21:11 - SoTA-Echoing

The working question is how a family of approximations supplies an object and the operations needed on it. The selected line combines a convergence relation, an existence argument in the chosen space, preservation of the required operations, and a finite-use condition.

Avigad, Lewis and van Doorn's [Logic and Proof, §§21.3-21.4](https://leanprover-community.github.io/logic_and_proof/the_real_numbers.html#constructing-the-real-numbers) develops the Cauchy-sequence quotient and completeness of the reals. Its construction informs :4.3: specify when approximation families represent the same object and make arithmetic respect that identification. An existing completeness theorem is a cheaper alternative when its space already fits; constructing a new completion is useful when a missing object prevents the intended operation.

[Mathematics in Lean, chapter 11](https://leanprover-community.github.io/mathematics_in_lean/C11_Topology.html) organizes convergence and continuity through filters, while exposing metric versions for ordinary calculations. This supports the generality of :4.1/:4.4 without requiring filter notation for every use. Mathlib's current [uniform convergence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/UniformConvergence.html) and [limits of derivatives](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/UniformLimitsDeriv.html) give inspectable statements with different hypotheses. They inform the operation-specific repair in :5.3. Repeated numerical agreement cannot replace those hypotheses; an applicable theorem can avoid repeating its proof.

Bauer and Kavkler's [A Constructive Theory of Continuous Domains Suitable for Implementation](https://math.andrej.com/wp-content/uploads/2008/01/constructive-domains.pdf), 2008, is an implementation-oriented methodological anchor. It compares prescribed approximation rates with interval representations that test a requested width during computation, keeping the logical assumptions of that implementation explicit. The adopted contribution to :4.5 is the choice between a supplied rate and a justified stopping observation. Its particular logic and real-number implementation are alternatives for that branch, not requirements on every convergent construction.

Use the weakest established condition that supports the requested result. Reopen the comparison when the space or operation changes, when a claimed approximation cannot be obtained, or when a different representation supplies the same use with less work. These sources support the stated constructions; choosing a particular numerical algorithm remains a further task.

### MATH.21:12 - Relations

- **MATH.2** identifies equivalent representations and carries well-defined operations to their quotient.
- **MATH.19** constructs an existence, convergence or preservation argument when an intermediate implication is missing.
- **MATH.18** compares different mathematical accounts of a limiting construction.
- **MATH.22** changes assumptions when a needed limit or operation is absent; **MATH.23** develops the resulting conjecture.
- **C.29** interprets the mathematical consequence in its subject. Modeling methods choose the subject-relevant approximation and computational methods obtain its finite realization.
- **B.5.QD and C.40.CD** develop the next useful question after a construction, obstruction or changed use.

### MATH.21:End

## MATH.22 - Change Axioms and Trace Their Consequences

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.22:1 - Problem frame

Use this pattern when a mathematical assumption excludes a construction you need, a theorem uses a stronger premise than its intended application supplies, or two accounts differ in what they assume. The work is to change the assumptions and establish what the changed theory permits.

An **axiom** is a statement taken as a premise of the theory being developed. A **model of those axioms** is a mathematical structure in which they hold under a stated interpretation. For example, an ordered set interprets an order relation; a collection of permutations interprets composition. This use of model concerns mathematical satisfaction. Applying the structure to an observed subject requires the additional correspondence work in C.29 and MMP.

**First useful move:** isolate one assumption and one construction or conclusion affected by it. Try to derive that conclusion from the remaining assumptions, or construct a case where they hold and the conclusion fails. The result identifies what can be retained and what must change.

The reader needs elementary reasoning about sets, operations, relations and their laws. The examples introduce the group, order and arithmetic assumptions they use. A change of logical inference rules needs the corresponding knowledge of that logic.

If a supplied theorem already works under the available assumptions, apply it. MATH.6 suffices for refuting one proposed consequence. Use the present method when the receiving work needs a revised theory, its changed constructions and its surviving results.

### MATH.22:2 - Problem

A familiar axiom set can make a useful construction impossible or unnecessarily restrictive. Dropping a premise admits more structures, but a familiar proof may then fail. Adding a convenient operation can conceal an existence assumption, and adding a desired law can conflict with laws already retained.

There are different outcomes to establish. A proof might survive unchanged, admit a new proof, need an extra condition, or have a counterexample. A stopped proof search leaves these possibilities unresolved. The revised theory must expose the difference because later reasoning and computation consume its consequences.

### MATH.22:3 - Forces

| Force | Tension |
| --- | --- |
| Generality | Fewer assumptions can cover more structures while supporting fewer conclusions. |
| Stronger constructions | Added axioms can supply an object or simplify a proof while excluding intended cases. |
| Familiar notation | A new symbol can abbreviate an existing construction or introduce a new assumption. |
| Proof reuse | A theorem may remain valid even when its familiar proof uses a removed axiom. |
| Useful metatheory | A small countermodel can settle a local question; a consistency claim about a foundation can require much stronger work. |
| Computational use | An existence principle can support a mathematical argument while leaving an obtaining procedure to be supplied. |

### MATH.22:4 - Solution

**Local mantra:** isolate the assumption and wanted construction; choose the change; build or interpret the changed structures; trace the affected arguments; establish what the comparison warrants; return the revised theory to use.

#### MATH.22:4.1 - Identify the assumption and its mathematical job

State the objects, operations and laws currently used. Find the step where the disputed assumption enters. It may justify rearranging operations, comparing two objects, choosing an element, taking a limit, or introducing an object with a required property.

Distinguish a law about the objects from a logical rule used to infer statements about them. Removing commutativity changes the structures being studied. Restricting proof by contradiction can change the permitted arguments even when the question concerns the same objects.

State the desired gain. Examples include admitting noncommuting operations, retaining incomparable alternatives, obtaining a missing limit, or preserving the computational content of a proof. This gain guides which consequences to examine first.

For a local question, the relevant definitions and proof dependencies are enough. Reconstruct a whole formal foundation only when the conclusion being sought depends on it.

#### MATH.22:4.2 - Choose the change and what stays fixed

With a fixed language and logic, removing axioms weakens the theory: every old model still satisfies the retained axioms, and additional models may become possible. Adding axioms strengthens it: every new model must satisfy the old axioms as well, so some old models may be excluded. Replacing an axiom combines removal and addition; neither direction of inclusion follows automatically.

Name the fixed assumptions and the changed one. If the vocabulary changes too, give the interpretation used to compare the accounts. MATH.18 develops that comparison.

When introducing a symbol for an operation, ask how the operation is obtained. An abbreviation such as d(x,y)=x+(-y) expands into operations already available. If a proposed definition instead asks for the unique object satisfying a property, establish existence and uniqueness on its intended inputs. Calling it a definition does not complete that construction. In :5.2, a least upper bound exists in one order and is absent in another.

An added operation can also require a larger collection of objects. In that case construct the extension and the map from the earlier structure, then establish which old operations and relations the map preserves. MATH.1/.2/.16 supply construction methods for objects and operations. An extension by limits also requires specifying convergence and establishing that the needed limiting objects exist.

#### MATH.22:4.3 - Construct models and separating cases

Give the objects and the interpretation of every operation and relation needed by the claim. Establish each retained axiom. For an infinite family, use a general argument; enumerated cases suffice only when they exhaust the admitted possibilities.

Choose a case that distinguishes the changed theories. To investigate an axiom A relative to retained assumptions T, a model of T in which A fails shows that A is not a consequence of T. A model where A holds shows that adding A is compatible with that model. These are different results, and both can matter.

Use MATH.6 to construct a countermodel. Finite structures are often a cheap first attempt because their operations and relevant failures can be displayed completely. An existing infinite structure with a short argument may be simpler.

If the changed account uses different objects or primitives, an interpretation can carry its constructions into an established theory. Check the translated axioms and the translated steps of inference needed for the result. A picture suggesting an analogy is a starting point for this work.

#### MATH.22:4.4 - Trace the consequences that the receiving work uses

For each required result, locate the affected proof step.

- Retain a proof when its steps use only assumptions that remain.
- Try another proof when the old one uses the removed assumption. A dependency of one proof need not be a necessary premise of the theorem.
- Keep a conditional result when the receiving use can supply the additional premise.
- Return a countermodel when the conclusion fails under the revised assumptions.
- Leave a particular consequence unresolved when neither an argument nor a countermodel has been obtained.

Apply the same reasoning to constructions. Check whether their inputs are still admitted, the operations remain defined, and the properties used by the next step still follow. For example, :5.1 retains cancellation after dropping commutativity but loses unrestricted rearrangement of factors.

When a proof is formalized, its recorded dependencies can help find affected steps. They report what that proof uses. A claim that no proof can avoid an axiom requires an additional argument.

If the result will generate data or a program, trace what the new principle supplies operationally. An existence argument and an effective construction support different next uses. MATH.12 handles extraction; the relevant computational method handles execution and cost.

#### MATH.22:4.5 - State what the model or proof establishes

In a sound interpretation of a deductive system, a proof preserves truth in every model of its premises. Therefore a model of T where A fails rules out a proof of A from T. If another model of T satisfies A, it likewise rules out a proof of not-A. Together these establish that A is independent of T, relative to the logic and semantics being used.

A model also supports consistency: a sound derivation of a contradiction from its axioms would have to make a contradiction true in that model. The construction of the model relies on background mathematics. Keep that dependence when reporting a consistency result, especially when comparing foundations. A failure to find a contradiction supplies no such construction.

For a definitional extension, expand the new symbols in the affected claims and arguments. When all new operations are definable in the old theory and the definitions can be eliminated, conclusions stated wholly in the old language retain their old justification. If an existence principle or inference rule has been added, examine its consequences separately.

The preceding model arguments use their stated semantics. A change to intuitionistic, dependent-type or another logic requires an interpretation sound for its own rules; an arbitrary transfer of classical model arguments could answer the wrong question.

#### MATH.22:4.6 - Use the revised theory

Return the changed assumptions together with the construction, theorem or obstruction needed by the receiving work. Carry the conditions under which it can be used. An unresolved consistency or consequence question can be handed to a collaborator without presenting it as settled.

Choose between revised theories by the work they enable and the costs they impose. One can admit more objects, another can make a needed construction available, and another can retain an effective procedure. FPF's ordinary characterization and choice methods apply when these alternatives must be compared; the present method supplies their mathematical consequences.

Use the changed result to reformulate a model, modify a method, or pose the next mathematical problem. For a new conjecture, state which further relation might hold under the retained assumptions. A later failure reopens the assumption or inference on which the failed use depends.

### MATH.22:5 - Archetypal Grounding

#### MATH.22:5.1 - Drop commutativity while preserving invertible composition

Suppose a collection has an associative operation, an identity e and an inverse for every element. These are the group assumptions. Add commutativity, xy=yx, and familiar rearrangements become available. For example, MATH.19's argument proves `(xy)^n=x^n y^n`.

The intended new use composes invertible operations whose order matters. Remove commutativity and retain the group assumptions.

Cancellation survives, although its proof may change. A commutative proof multiplies `ax=ay` on the right by the inverse of a, then rearranges `axa⁻¹` and `aya⁻¹` to obtain `x=y`. This uses commutativity. A replacement proof multiplies on the left: `a⁻¹(ax)=a⁻¹(ay)`. Associativity gives `(a⁻¹a)x=(a⁻¹a)y`, hence `x=y` by the inverse and identity laws. The theorem therefore survives after removing commutativity.

Unrestricted rearrangement fails. Consider all permutations of {1,2,3}, composed with the rightmost permutation acting first. Composition is associative, the identity leaves each element fixed, and each bijection has an inverse. Let f swap 1 and 2, and let g swap 2 and 3. Then fg sends 1 to 2 to 3 to 1 as a cycle, while f² and g² are identities. Thus (fg)² sends 1 to 3, but f²g² sends 1 to 1.

This is a model of the group assumptions with noncommuting elements. The two-element group {e,h}, with h²=e, is a model where every pair commutes. Under ordinary classical group logic, the two models show that commutativity is independent of the retained group axioms.

The revised theory now admits ordered compositions. It retains cancellation and inverses. Rearrangement remains usable for particular pairs whose commutation is established; it has ceased to be a general permission.

#### MATH.22:5.2 - Remove total comparability and inspect a proposed new operation

A partial order is reflexive, antisymmetric and transitive. A total order additionally compares every pair: x<=y or y<=x. Suppose the work needs to retain pairs for which neither direction holds.

Remove total comparability. On pairs of natural numbers, define (a,b)<=(c,d) when a<=c and b<=d. The three partial-order laws follow coordinate by coordinate. The pairs (1,0) and (0,1) are incomparable. The ordinary order on natural numbers supplies a model with total comparability; the pair order supplies a model without it.

Now ask for a least common upper bound of two objects. In the pair order, it is the coordinatewise maximum. It is above both inputs, and any common upper bound is above each coordinatewise maximum. This proves both the construction and its leastness.

The partial-order axioms alone do not supply that operation. Take four distinct objects a,b,u,v. Besides reflexive comparisons, require a<=u, a<=v, b<=u and b<=v, and no others. This is a partial order. Both u and v are upper bounds of a and b, but neither is below the other; a and b are not upper bounds. There is no least upper bound of the pair.

Consequently, writing "x join y" for every pair in an arbitrary partial order adds an existence requirement unless a construction has already supplied it. The work can select an order where joins exist, add the join assumption and accept its narrower class of models, or undertake a construction that enlarges the objects. Choosing one of u or v alone supplies an upper bound, not the missing least one.

This separates two changes that a generic instruction to "relax the order" would hide: allowing incomparability and requiring a combining operation. A model of alternatives can use the resulting order; any decision to prefer one alternative remains a separate choice.

#### MATH.22:5.3 - Introduce total reciprocal notation without retaining a false law

Suppose arithmetic uses field laws, including `0!=1` and distributivity, and the reciprocal law `x*inv(x)=1` for `x!=0`. The proposed change makes inv a total operation and asks that same law to hold at zero.

The retained laws already imply `0*y=0`. Indeed, `(0+0)*y=0*y+0*y` by distributivity, and cancelling one `0*y` from `0*y=0*y+0*y` leaves `0=0*y`. The proposed new reciprocal law at zero would therefore imply `0=1`. The retained assumptions and the new law conflict.

A different change works: over the rational numbers, define `inv(0)=0` and `inv(x)=1/x` for `x!=0`. This gives a total operation, retains the nonzero reciprocal law, and leaves the field operations unchanged. It has not made cancellation of a zero factor valid.

For a use involving the equation `x*y=x*z`, cancellation still requires `x!=0`. At `x=0`, all rational y,z satisfy the equation. A calculation using total reciprocal notation must retain that condition or inspect the zero case.

The result is a consistent construction within rational arithmetic and a revised law with its condition, rather than the initially requested unconditional inverse law. Total notation and stronger algebraic permission have been separated.

### MATH.22:6 - Bias-Annotation

Familiar structures can make their extra laws feel unavoidable. The permutation and partial-order cases expose assumptions that integers with addition or a single numerical scale can conceal.

The examples use elementary classical structures so that the changed laws can be inspected directly. They demonstrate the method without deciding between competing foundations of mathematics. A foundational change needs its own interpretation and consequences, including any change in constructive use.

### MATH.22:7 - Conformance Checklist

For the change being made:

- The altered axiom, definition or inference rule and the assumptions retained are identifiable.
- The desired construction or consequence explains why the change is useful.
- A claimed model supplies the required objects and interpretations and satisfies every retained axiom.
- A definition has its required existence and uniqueness, or the additional assumption is stated.
- Reused proofs survive at the steps that matter; a lost proof is distinguished from a refuted theorem.
- Independence, consistency and non-derivability claims have the appropriate model or argument and retain their background assumptions.
- The receiving use gets the revised consequence with its applicability and any obtaining procedure still needed.

### MATH.22:8 - Common Anti-Patterns and How to Avoid Them

**Removing a premise while retaining its rewrite permission.** Dropping commutativity in :5.1 permits noncommuting operations. Reordering their factors requires a local commutation argument.

**Defining an object that need not exist.** The four-object order in :5.2 has common upper bounds but no least one. Supply a construction or change the assumptions before using join as a total operation.

**Extending notation and silently strengthening a law.** Total reciprocal notation in :5.3 is available with a conditional inverse law. The unconditional law contradicts the retained arithmetic.

**Treating a failed proof as independence.** The proof may need a different lemma. Establish non-consequence through a separating model or a suitable metatheoretic argument. For the model route in :4.5, establish both directions of separation before claiming independence.

### MATH.22:9 - Consequences

The result exposes which generalizations preserve a useful conclusion, which additions buy a new construction, and which changes require a different problem. A small separating structure can prevent repeated attempts to derive a false consequence.

Changing axioms can also open a family of new questions. Which maps preserve the revised structure? Which previous constructions still work? Can a missing operation be supplied by extending the objects? These questions continue the mathematical development and give modeling or methodological work new usable constructions.

### MATH.22:10 - Architectural Rationale

A proof states what follows from assumptions. A model makes their simultaneous satisfaction and separating consequences inspectable. Using both permits directed theory change: follow a needed construction to its assumptions, change them, and return the consequences to that construction's use.

MATH.6 constructs countermodels, MATH.18 compares accounts through interpretations, and MATH.19 constructs missing arguments. Here these methods support a revised theory whose consequences can be used deliberately.

Logical consistency, mathematical fruitfulness and correspondence to an observed subject answer different working questions. The first controls what the axioms jointly permit; the second concerns the further constructions and questions they open; the third requires subject knowledge and observation. Their connection supports mathematical modeling without making one stand in for the others.

### MATH.22:11 - SoTA-Echoing

The working question is how to change mathematical assumptions while retaining justified and useful consequences. The selected line combines proof-dependency analysis, construction of models and interpretations, and explicit separation of definitional change from added principles.

**Adopt the model-and-consequence method.** The Open Logic Project's [Models and Theories](https://builds.openlogicproject.org/content/first-order-logic/introduction/models-theories.pdf) makes the relation between axioms and satisfying structures explicit. [Logic and Proof, §§10.1-10.5](https://leanprover-community.github.io/logic_and_proof/semantics_of_first_order_logic.html) supplies interpretation and soundness for the first-order branch. These are method sources for :4.3/:4.5. Their use defeats an inference from unsuccessful proof search to non-consequence: a separating structure supplies the needed reason. A known theorem or short existing interpretation is cheaper when it already settles the same question. The chosen branch accepts the cost of constructing a model when that difference remains unresolved.

**Adapt dependency analysis to the required return.** [Theorem Proving in Lean 4, Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/) explains how added principles affect proof and computational interpretation, and how axiom dependencies can be inspected. This changes :4.1/:4.4: trace the principle actually used and what a later construction can obtain. Reading a proof's dependencies is a useful alternative to rebuilding it. That inspection alone does not settle whether another proof avoids the principle. A non-derivability claim needs a separate argument, such as a separating model under the stated soundness assumption. The source describes one formal system; Lean use is optional, and its evaluation mechanisms are not generalized to all mathematics.

Retain these approaches while their constructions answer the local question at acceptable effort. Reopen the comparison when the logic changes, a proposed interpretation fails, another proof removes the alleged dependency, or the receiving use needs computational content that the revised theory has not supplied.

### MATH.22:12 - Relations

- **MATH.6** constructs a countermodel; **MATH.18** compares accounts through interpretations.
- **MATH.19** constructs or replaces affected arguments; **MATH.12** recovers their constructive output.
- **MATH.1/.2/.16** supply construction methods when a changed theory needs different objects or operations.
- **B.5.FM, B.5.TC and C.29** use the resulting assumptions and structures in reformulation, theory change and correspondence to a subject.
- **MMP and the relevant CMP methods** use the revised mathematical construction, adding subject interpretation or an executable procedure when required.
- **ME** can use this mathematical account to change formal descriptions of methods; the behavior of the described work still needs its own justification.

### MATH.22:End

## MATH.23 - Develop a Conjecture by Changing a Construction

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.23:1 - Problem frame

Use this pattern when a mathematical construction works in some cases, fails after a change, or reveals a relation that could support a new theorem. You need to formulate the next claim and a way to investigate it.

A **conjecture** is a mathematical assertion proposed for investigation. Developing it includes choosing its objects, assumptions, quantifiers and conclusion. The result can become a theorem, a refuted claim, or a more useful question. Its value lies in what the answer would let someone construct, infer, explain or change.

**First useful move:** change one mathematically consequential part of the construction and compare what happens. Replace a parameter by a variable, combine two outputs, remove a used assumption, or ask the same operation to preserve another property. Try the changed construction and identify the equation, condition or obstruction that controls its result.

The reader needs the mathematical operations used by the starting construction and elementary proof reasoning. The examples explain their additional operations; the last example develops a limit argument. The method can be performed by a person, an AI agent or cooperating contributors with the needed preparation.

Use an established result when it already answers the question. MATH.19 helps prove a sufficiently clear claim. B.5.QD develops questions more generally. Here the work develops a mathematical assertion through construction, variation, proof analysis and counterexamples.

### MATH.23:2 - Problem

A list of successful cases leaves many possible general claims. A formula can match every computed value and fail beyond them. A proposed proof can depend on a property absent from the conjecture. Conversely, a failed conjecture can reveal a useful operation or a stronger question.

The difficulty is to extract a relation that can be investigated generally. Changing a number produces another instance; changing the construction law, allowed maps or quantifier can create a new problem. The latter change needs a mathematical reason and a feasible first attack.

### MATH.23:3 - Forces

| Force | Tension |
| --- | --- |
| Examples guide invention | Their generating rule may conceal a restriction that the conjecture omits. |
| Generality increases reuse | A broader claim can lose the construction that made the original case work. |
| Counterexamples improve understanding | Excluding a troublesome case can also discard the phenomenon the work needs to understand. |
| Computation expands exploration | Search quality depends on representation, tested cases and the property being evaluated. |
| A new problem opens work | Its first attainable result can be much smaller than the eventual theorem. |
| Results and methods develop together | An answer can be useful immediately while its construction opens further questions and transfers. |

### MATH.23:4 - Solution

**Local mantra:** recover the construction and its use; vary a consequential ingredient; express the suggested law; seek its reason and a separating case; revise the assertion or construction; choose and begin the next useful problem.

#### MATH.23:4.1 - Recover what makes the starting construction work

Write the inputs and the operations that produce the result. Identify a relation the result satisfies and where that relation is used. Separate what has been proved from what has only occurred in inspected cases.

Look inside the operation. Repeated updates may expose a recurrence. Combining two constructions may expose closure or an order dependence. A successful quotient may reveal which distinctions can be discarded. MATH.17 helps make the operations themselves available for this investigation.

When a program supplies examples, recover the class it actually generates. For instance, a generator that produces only trees cannot investigate a claim about arbitrary graphs unless the missing graph classes are handled elsewhere. The representation and evaluator are part of the available mathematical experiment.

#### MATH.23:4.2 - Construct a variation with a reason

Choose an ingredient whose change could affect the wanted relation. Useful mathematical moves include:

| Starting opportunity | Construction of the next problem |
| --- | --- |
| Several parameter values work similarly. | Replace the parameter by a variable, derive the update rule and ask which identity holds over its domain. |
| Two outputs can be combined. | Define their combination and ask whether it remains in the same class and preserves the required relation. |
| A proof uses a special hypothesis. | Remove or weaken it, locate the affected inference and ask for a replacement condition or counterexample. |
| A desired property fails. | Isolate the obstruction and ask whether it completely characterizes failure or only gives one sufficient obstruction. |
| The result survives a change of representation. | Construct the interpretation and ask which assertions, operations and equalities it preserves. |
| An approximation supports a limiting claim. | State the order of its quantifiers and ask which operations or properties survive the limit. |

These are possible operations, not required stages. Choose the one selected by the construction. MATH.8/.11/.13 supplies symmetry or invariant reasoning; MATH.18 supplies interpretations; MATH.22 develops changed assumptions. Use their fuller methods when that mathematical contribution is needed.

Keep the original use visible. Requiring equal-sized groups repairs a mean-of-means formula, but leaves a request about arbitrary groups unanswered. The latter needs another construction, as in :5.2.

#### MATH.23:4.3 - State the proposed law and its answer form

Give the objects, domains, allowed operations, assumptions and proposed conclusion. In particular, make the quantifiers distinguishable. These statements ask different questions:

- For each input, some construction has the property.
- One construction works for every input.
- Every admitted construction has the property.

A finite pattern of results can suggest a formula. Derive it from the generating operation, a recurrence, an invariant or another mathematical relation when possible. If that derivation is missing, retain the formula as a conjecture and identify the step that would establish it.

Say what would resolve the present question. An explicit construction, a characterization of all admissible cases, a bound, or a counterexample can open different next uses. A conjectured optimal construction needs both an attainable value and an argument excluding better ones when optimality is the required conclusion.

Check whether the proposed law is already a known result under another description. MATH.18 can compare representations. An available theorem can close this question and expose a more useful next one.

#### MATH.23:4.4 - Alternate a proof attempt with revealing cases

Use MATH.19 to find intermediate claims connecting the construction to the proposed conclusion. Identify which mathematical property each step consumes. This can expose a condition that the conjecture has not yet stated.

At an uncertain step, construct a case that challenges that condition. Prefer one that distinguishes plausible accounts. To test whether a summary supports composition, find inputs with the same summary and place them in the same surrounding construction. If their required outputs differ, the summary has lost information that composition needs.

Inspect the status of a failure. A counterexample satisfying the conjecture's premises refutes the conjecture. A failure of an auxiliary lemma may leave a different proof possible. A failed program may instead concern its representation or implementation. Recover the mathematical obstruction before revising the claim.

Computational search can propose constructions and counterexamples. Check a returned candidate against the mathematical conditions that its use requires. For a finite explicit object, this may be a small complete calculation. Sampled tests of an infinite family leave its universal claim to be justified.

#### MATH.23:4.5 - Revise the claim without hiding the lost use

Use the failure to choose the next mathematical change. Three common returns are:

1. **Repair a hypothesis.** State the condition that makes the failed lemma work, prove its sufficiency and check whether the intended cases satisfy it.
2. **Repair the construction.** Retain the original problem and change the objects, representation or operation so that the required property can be obtained.
3. **Change the conclusion.** Obtain a conditional answer, bound, obstruction or weaker property that still serves a useful question.

A sufficient condition can be worth developing before necessity is known. Label that difference: a proof that uniform convergence preserves continuity does not show that every continuous limit was obtained uniformly.

A counterexample can itself become a constructive ingredient. Ask what class it belongs to, which transformations preserve its obstruction, and which related conjectures it can test. The new question can concern the method of generating cases as well as the cases themselves.

Retain the result that survived. Changing the theorem should not erase a valid construction or an earlier unresolved requirement.

#### MATH.23:4.6 - Choose a next problem and begin its mathematical work

Compare the few continuations whose answers would change further work. A useful result can supply a missing lemma, a reusable combining operation, an explanation of failure, or a method that makes another class of questions approachable. Immediate engineering application is one possible use; developing a new mathematical operation can also enable later inquiry whose destination is not yet known.

Choose a first attempt that the available contributors can perform. For a broad characterization, this might be one direction of the theorem. For an extremal problem, it might be one explicit improved construction or a bound. For a limit question, it might be the estimate needed to justify one passage to the limit.

Return the conjecture, the mathematical basis that suggested it, the most revealing success or obstruction, and the next operation. An expression and a short argument can carry this result.

Use B.5.QD and C.40.CD when several questions and ways must develop together. E.10.INT helps distinguish the interest of further possible work from surprise, fame or a search score. C.36.RP supplies retention of the reconstructible method when continuing capability is at stake. Obtain further observations or checking only when their possible outcomes can change the next move enough to justify the effort.

### MATH.23:5 - Archetypal Grounding

#### MATH.23:5.1 - From repeated instances to a family of operations

Repeatedly apply `f(x)=a*x+b` over real numbers. A few calculations give:

`f²(x)=a²*x+(a+1)*b`,

`f³(x)=a³*x+(a²+a+1)*b`.

The useful next question is how to represent any number of repetitions without expanding every substitution. The conjectured formula is:

`f^n(x)=a^n*x+b*S_n`, where `S_0=0` and `S_n=1+a+...+a^(n-1)` for `n>0`.

Recover the generating rule. Applying f once more changes the coefficient of x from `a^n` to `a^(n+1)`, and the constant from `b*S_n` to `b*(a*S_n+1)`. The identity `S_(n+1)=a*S_n+1` therefore supplies the induction step. At `n=0`, `f^0` is the identity and `S_0=0`. The formula is proved for every natural n.

Now vary the problem: combine two potentially different maps `f(x)=a*x+b` and `g(x)=c*x+d`. Their composite is:

`f(g(x))=(a*c)*x+(a*d+b)`.

This constructs an operation on coefficient pairs: `(a,b)` composed with `(c,d)` gives `(a*c,a*d+b)`. The class is closed under composition. MATH.17 can study this operation; a computational method can use it to combine repetitions.

Order now becomes a useful question. Reversing the maps gives the same linear coefficient but constant `c*b+d`. Thus they commute exactly when `d*(a-1)=b*(c-1)`. This condition says when reordered operations retain the result.

The progression has produced a general iteration formula, a closed combining operation and a condition for rearrangement. A further question about vector-valued affine maps needs its matrix composition law; scalar commutation cannot be silently carried into that new setting.

#### MATH.23:5.2 - A failed combination produces a better summary and another conjecture

A computation stores the arithmetic mean of each nonempty group of real numbers. The proposed combining operation takes the mean of those means. For groups [0] and [2,4], it returns (0+3)/2=1.5, while the combined group has mean 2.

Inspect the missing mathematical relation. Each group mean gives a total only when its group size is known. Equal group sizes make the proposed operation work, but arbitrary groups require another construction.

Retain a sum s and count n. Combine (s,n) and (t,m) as (s+t,n+m), then return (s+t)/(n+m) when n+m>0. Associativity and commutativity follow from those of addition in both coordinates; (0,0) is an identity. Thus grouping and order of the combination do not change the final mean in real arithmetic. A finite-precision implementation needs its own error account.

The construction opens a broader mathematical question: **Which summaries permit the summary of a combined input to be computed from the two summaries alone?**

Let q map a collection of finite lists, closed under concatenation, to proposed summaries; let ++ concatenate lists. Means and medians here use nonempty lists, while sum and count also admit the empty list. A necessary condition is:

if q(u)=q(u') and q(v)=q(v'), then q(u++v)=q(u'++v').

It is also sufficient for defining a combining operation on attained summaries: choose lists representing the two summaries and apply q to their concatenation. The condition makes the result independent of those choices. This proves mathematical existence of the operation. Computing it from a concrete representation of the summaries still needs an effective rule. MATH.2 develops the compatible identification; MATH.12 and CMP handle obtaining the operation.

For means alone, take u=[0], u'=[0,0], and v=v'=[6]. The input summaries match, but the concatenated means are 3 and 2. The necessary condition fails. Sum and count repair it by an explicit operation.

Now ask whether median and count suffice. Take u=[0,1,100] and u'=[-100,1,2]. Each has count 3 and median 1. Append the same list [50,50]. The resulting five-element medians are respectively 50 and 2. This new conjecture is refuted by the same method.

The next useful problem concerns what more to retain. Sorted full lists are sufficient and can be merged, while a use requiring less storage can ask for a restricted input class or an approximate median with a stated error. The mathematical obstruction now informs a computational and modeling choice.

#### MATH.23:5.3 - A failed limit argument reveals a stronger condition

Consider the claim that a pointwise limit of continuous real functions is continuous. On `[0,1]`, let `f_n(x)=x^n` for positive natural n. Each function is continuous. At any fixed `x<1`, `x^n` tends to zero; at `x=1` it equals one. The limit f is zero below one and equals one at one, so it is discontinuous.

Locate the failed proof step. Pointwise convergence lets the approximation index depend on x. Continuity near a point needs control over nearby x together. Choosing a good approximation at the one point alone does not control its neighborhood.

This suggests a sufficient condition: **uniform convergence**. For every positive error allowance, one index makes all later approximations close to f at every point of the domain.

Work the proposed repair. Fix a point x0 and an error allowance e>0. Choose N so that the approximation error between f_N and f is less than e/3 everywhere. Continuity of f_N gives a neighborhood of x0 in which the difference between f_N(x) and f_N(x0) is less than e/3. The triangle inequality bounds the difference between f(x) and f(x0) by these three errors, hence by e. This proves continuity of f at x0.

The repaired theorem supplies a condition for transferring continuity. Here proof analysis discovered which quantifier change made the desired inference possible. A subsequent limit construction can use the proved condition to retain continuity.

Uniformity is sufficient, not necessary. On the domain `[0,1)`, the same `x^n` sequence has the continuous limit zero, but convergence is not uniform: for every n there is an `x<1` with `x^n=1/2`. The next question can therefore seek a weaker condition suited to the receiving use, rather than treating uniform convergence as the definition of every acceptable limit.

### MATH.23:6 - Bias-Annotation

Small examples are chosen to expose a relation and permit a full calculation. In a larger inquiry, simple generators can miss structures with different behavior. Change the generating rule or inspect a contrasting class when that difference could defeat the proposed claim.

A solved or famous problem can attract attention while its reusable mathematical contribution remains unclear. Recover the construction and the questions it opens. The choice of a next problem depends on the work and contributors, not on a universal ranking of interesting statements.

### MATH.23:7 - Conformance Checklist

For the conjecture being developed:

- The starting construction, established result and receiving use are recoverable.
- A mathematical change explains why the new question arises.
- Objects, domains, hypotheses, quantifiers and answer form distinguish the proposed claim.
- A proof attempt exposes its needed intermediate relation, and the chosen case tests a consequential condition.
- A counterexample is classified at the claim, lemma or implementation it actually defeats.
- A repaired hypothesis, construction or conclusion preserves the distinction between the new question and any earlier unsatisfied need.
- Generality follows from an argument over the stated class; tested cases retain their actual scope.
- The selected continuation has a useful attainable first operation and retains the earlier construction needed to perform it.

### MATH.23:8 - Common Anti-Patterns and How to Avoid Them

**Extrapolating the displayed values without the generating law.** The iteration formula in :5.1 is justified by its recurrence and induction. Agreement at a few n values alone would leave other continuations possible.

**Excluding the counterexample and abandoning the required class.** Equal-sized groups rescue the mean-of-means formula in :5.2, but not a requirement to combine arbitrary groups. Sum and count answer that requirement.

**Treating a convenient condition as necessary.** Uniform convergence repairs the continuity argument in :5.3. The final countercase shows why necessity remains a different claim.

**Losing the operation behind a successful answer.** Keeping only the mean hides the combining structure. Retaining sum and count makes later aggregation possible; retaining the compatibility argument supports the next summary question.

### MATH.23:9 - Consequences

A result becomes material for developing another mathematical problem. A failure can yield a condition, a construction or a new object of study. A success can reveal a family of operations and a way to transfer the result.

The method can stop with a well-formed conjecture and first attempt. Completing its proof, obtaining a computational procedure, learning the method and applying it to a physical subject have their own requirements. Keeping the connection to those uses makes partial progress useful without claiming their completion.

### MATH.23:10 - Architectural Rationale

B.5.QD locates a consequential next question. The mathematical contribution here is to construct its proposed law: expose composition and closure, change a quantifier, characterize a compatible identification, or isolate a premise through proof analysis. The cases show how these operations produce statements that can be proved or refuted.

MATH.17/.18, MATH.19/.22 and the other mathematical patterns supply the operative constructions. This pattern assembles them around the development of a conjecture. A case can close with a new question, an answer, or a further obstruction; a universal fixed order of research stages would obscure these returns.

A correct answer and a reusable method have related but different uses. Either can be obtained by people or AI agents. Retaining the derivation, allowed transformations and failed conditions permits another prepared contributor to adapt the work and formulate its next problem.

### MATH.23:11 - SoTA-Echoing

The working question is how to develop a mathematical conjecture from constructions and their failures, with a useful route into further work.

**Adapt proof analysis.** Lakatos's [Proofs and Refutations, Appendix 1](https://www.cambridge.org/core/books/abs/proofs-and-refutations/another-casestudy-in-the-method-of-proofs-and-refutations/AF9D68A35602B7F8F1409DF3E56C5D7B) connects counterexamples to the hidden lemmas and concepts in an attempted proof. The adopted move changes :4.4-.5: inspect the failed inference and consider a revised condition or construction. It improves on simply excluding the offending example when that exclusion abandons the intended class. The method can require more work than proving a fixed, adequate claim; use the latter route when its premises and conclusion already serve the inquiry. Lakatos supplies a method for developing the conjecture; its use can still leave the conjecture unresolved.

**Adapt construction search and generalization.** Georgiev, Gómez-Serrano, Tao and Wagner's [Mathematical exploration and discovery at scale, §§1.3-1.6 and 4](https://arxiv.org/html/2511.02864v3) distinguishes search for constructions from finding a program or formula that generalizes, and describes transitions to proof. It also reports evaluator defects and the limits of the tested search methods. This informs :4.1/:4.3-.4: inspect the generator and evaluator, recover a general construction, then establish the claim its use needs. Compared with direct object search, program search can retain reusable structure but adds generation and evaluation cost. A cheap direct search or existing theorem can be preferable. The paper supports these bounded choices, not a universal preference for AI search.

**Retain methods as a usable result.** The [Math and AI declaration of 11 September 2026](https://mathandai.org/) argues that counting solved problems can obscure understanding and transmission of methods. Adopt that question in :4.6 and the relation to C.36.RP: preserve what another prepared contributor needs to change and use the construction. The declaration is a position on the purpose of mathematical work, not evidence that transmission must remain exclusively human. The construction-to-proof account above supplies a concrete alternative involving AI contributors.

Reopen the route when a new counterexample changes the admitted class, another representation makes the conjecture simpler, or the receiver needs a result the present construction cannot provide. Improved search tools change the means and cost of investigation; they leave the proposed mathematical assertion and its possible use to be stated.

### MATH.23:12 - Relations

- **B.5.QD and C.40.CD** develop questions and obtaining ways across practices; this pattern supplies the mathematical conjecture-forming contribution.
- **MATH.17/.18** supply operations on constructions and interpretations between accounts.
- **MATH.8/.9/.11/.13** supply symmetry, selection and invariant methods that reveal general relations or obstructions.
- **MATH.19/.6/.22** supply proof construction, countermodels and changed axioms.
- **MATH.2** supplies the compatible identification used by composable summaries.
- **C.29 and MMP** interpret the mathematical result for a subject; **CMP** supplies effective search, construction and execution when needed.
- **E.10.INT, C.36.RP and HCD/DOCA** support interest, continuing availability of methods and acquisition of a missing capability.

### MATH.23:End
