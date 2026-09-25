# Notational Engineering DPF

> A pattern language for designing expressions that people and computational agents can interpret, manipulate, translate and use together.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 20 September 2026
- **Status:** Eternal alpha: a repertoire open to correction and extension.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF ecosystem repository](https://github.com/ailev/FPF)

Begin with something a reader needs to do: distinguish two cases, trace a dependency, change a rule, translate a diagram or follow a score. Use the Table of Contents to find the relevant method, then open its Problem frame, Solution, worked cases and checklist. The Readme follows worked connections between methods; the Preface explains how the methods connect and why they are organized this way.

The reference code **NOT** names this DPF. Its numbers are stable pattern addresses; § shows position within a Part. Expressions can use written symbols, spatial arrangement, sound, gesture or a combination. Each method states what its reader must already know or be able to obtain.

This publication belongs to the [Foundational Thinking DPF Suite](https://github.com/ailev/FPF/tree/main/Foundational%20Thinking%20DPF%20Suite). Its [Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains the mathematical, physical, computational and methodological connections. References such as A.6.3.RT.OE and C.2.8 name patterns in [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). Open a supplier when its contribution is needed, and revisit a dependent conclusion when that contribution changes.

To cite this edition: Anatoly Levenchuk, *Notational Engineering DPF*, [FPF ecosystem repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Notational Engineering - Readme](#notational-engineering---readme) | Follow connected notational work. |
| Preface | [Notational Engineering - Preface](#notational-engineering---preface) | Understand the connected methods, their rationale, sources and limits. |

## Part A - Design what can be expressed and done

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [NOT.1 - Choose the Distinctions and Operations a Notation Must Support](#not1---choose-the-distinctions-and-operations-a-notation-must-support) | Usable, evolving | notation design; reader operation; consequential distinction; expression gallery; requirement. What must a reader distinguish, infer or change using this notation? | C.2.8 for recovered structure; A.6.3.RT.OE for an expression under available rules; NOT.2/.3/.7 for construction and repair. |
| 2 | [NOT.2 - Define Expression Rules for Recoverable Binding and Composition](#not2---define-expression-rules-for-recoverable-binding-and-composition) | Usable, evolving | syntax; grammar; grouping; binding; scope; reference; composition. Which rules let users form expressions and recover their grouping, name bindings and connections? | NOT.1 for the operation; A.6.3.RT for relation and expression distinctions; NOT.3/.4 and CMP.12 for interpretation and transformation. |
| 3 | [NOT.3 - Give Expressions an Operative Interpretation](#not3---give-expressions-an-operative-interpretation) | Usable, evolving | semantics; interpretation; tacit operation; diagram reading; consequence; evaluator. Which operations let a prepared reader obtain a result from these signs? | NOT.2 for formed expressions; MATH.18 for mathematical interpretation; CMP.12 when an effective interpreter is needed. |
| 4 | [NOT.4 - Construct Transformations of Expressions That Preserve Their Use](#not4---construct-transformations-of-expressions-that-preserve-their-use) | Usable, evolving | rewrite; substitution; graph transformation; side condition; preserved observation; equality saturation. Which expression changes preserve the receiving use, and under what conditions? | NOT.2/.3 for binding and meaning; MATH.17/.18 for composition and interpretation; CMP.12 for executable transformation. |

## Part B - Translate, combine and improve notations

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [NOT.5 - Translate between Notations while Tracking Lost Distinctions](#not5---translate-between-notations-while-tracking-lost-distinctions) | Usable, evolving | translation; abstraction; many-to-one mapping; information loss; complement; round trip. What can the receiver recover, and which discarded distinctions must accompany the translation? | NOT.3 for the interpretation; MATH.2/.7/.18 for identification and preserved relations; NOT.6 for continued joint use. |
| 2 | [NOT.6 - Coordinate Complementary Representations through Shared References](#not6---coordinate-complementary-representations-through-shared-references) | Usable, evolving | multiple representations; shared reference; linked view; synchronization; update intent; constraint conflict. Which correspondences let readers combine results and propagate an intended change between representations? | NOT.5 for translation limits; MATH.18 and C.29 for correspondence; ME.9 when representations describe a working method. |
| 3 | [NOT.7 - Redesign a Notation around the Reader's Difficult Operations](#not7---redesign-a-notation-around-the-readers-difficult-operations) | Usable, evolving | notation redesign; cognitive dimensions; dependency; editing burden; preparation; comparison. Which change makes the difficult operation easier, and where does it move effort? | NOT.1–.6 for requirements and operative rules; C.2.8, EXD and HCD for recovery, explanation and capability questions. |
| 4 | [NOT.8 - Construct Temporal or Embodied Notation with a Reading Procedure](#not8---construct-temporal-or-embodied-notation-with-a-reading-procedure) | Usable, evolving | temporal notation; embodied notation; rhythm; gesture; frame; segmentation; replay; enactment. How can order, duration or movement be expressed with a usable reading procedure? | NOT.1–.7 for design and interpretation; CMP.12 for an effective interpreter; B.5.MPC for physical realization. |

# Notational Engineering - Readme

A notation should let its users do something with an expression: derive a consequence, follow a dependency, change an assumption or instruct another performer. The methods in this language connect that work to the expression's structure and interpretation, then help carry the result between forms and through changes. They apply to symbolic, graphical, verbal, gestural and executable expressions. The subject practice supplies what the expressed distinctions mean and which consequences matter.

Bring an expression, the operation it should support and enough subject knowledge to recognize a useful result, or a collaborator who can supply that knowledge. Keep conventions that already work. Constructing an expression under adequate existing rules can start with FPF A.6.3.RT.OE; use this language when those rules, their interpretation or the supported operations need development.

You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.” Ask it to demonstrate the reading or change and identify any rule, input or capability it had to supply.

## Practical entries

These selected connections show how results pass between methods. They are examples, not a catalogue or a prescribed sequence. Enter where the difficulty occurs and stop when the needed result is available. The Table of Contents and each pattern's `Use this when` provide direct access for other questions. The [Preface](#notational-engineering---preface) explains the repertoire and develops the first connection in greater detail.

### NT-CHANGE-TOGETHER - Carry a changed request through several representations

- **Situation:** A group uses a formula, operation graph and table for different operations, and a local request changes what their users should read or do.
- **Question:** What does the request change, and how can the useful forms remain connected?
- **First useful result or blocker:** The request expressed as a constraint on the shared construction, followed by its affected expressions or a conflict between requirements.
- **Start with:** [NOT.6 - Coordinate Complementary Representations through Shared References](#not6---coordinate-complementary-representations-through-shared-references) when the forms are already interpreted; [NOT.1 - Choose the Distinctions and Operations a Notation Must Support](#not1---choose-the-distinctions-and-operations-a-notation-must-support) when the required operation is still unclear.
- **Stop or return:** Keep unaffected interpretations. Return to the changed assumption, discarded distinction or incompatible requirement; an adequate existing representation needs no redesign.

#### Worked connection for NT-CHANGE-TOGETHER

1. **Give the forms something definite to express.** A stipulated rule is `r(q,b) = q + q + b` over real numbers. Both q occurrences use one supplied input; b is one shared parameter. The work is to obtain outputs and revise b. If grouping or references are unclear, [NOT.2 - Define Expression Rules for Recoverable Binding and Composition](#not2---define-expression-rules-for-recoverable-binding-and-composition) supplies those rules. Its result lets [NOT.3 - Give Expressions an Operative Interpretation](#not3---give-expressions-an-operative-interpretation) specify the reading: add q to itself, then add b. In the operation graph, q feeds both inputs of the first addition; that result and b feed the second. At b=1 and q=0, 1, 2, the outputs are 1, 3, 5.

2. **Use the interpretation to justify a useful change of expression.** [NOT.4 - Construct Transformations of Expressions That Preserve Their Use](#not4---construct-transformations-of-expressions-that-preserve-their-use) can replace the formula by `2*q + b`. Real arithmetic establishes the same output for every admitted q and b. The graph exposes the dependence; the compact formula makes the shared parameter easy to locate. Their value comes from those operations, not from one form being universally simpler.

3. **Give a translation only the work it can support.** [NOT.5 - Translate between Notations while Tracking Lost Distinctions](#not5---translate-between-notations-while-tracking-lost-distinctions) produces the table `(0,1), (1,3), (2,5)` at b=1. This supports lookup at the listed inputs. The table alone does not determine the output at q=3: `2*q + 1` and `2*q + 1 + q*(q-1)*(q-2)` agree on all three rows but give 7 and 13 there. Keep the generating rule with the table when the receiver needs other inputs or a rule change. If only the three listed answers are required, stop with the table.

4. **Interpret the request before propagating it.** The group asks for r(1,b)=4 while retaining the coefficient 2. NOT.6 uses the correspondence between that table row and the formula to obtain `2*1 + b = 4`, hence b=2. This new parameter supplies the graph and regenerates the table as `(0,2), (1,4), (2,6)`. The unedited old cells were derived values, not instructions to hold them fixed. If the request also keeps r(0,b)=1, it requires b=1 and conflicts with b=2. Return the two requirements to the group for a decision. If a separate record says that an output of 3 was observed at q=1, keep that observation beside the new prediction of 4. A parameter change does not revise the past event.

5. **Reopen the relevant rule when an occurrence changes meaning.** Suppose each q occurrence now means a fresh sensor read. With successive readings 4 and 5 and b=1, `read() + read() + b` gives 10; `2*read() + b`, using the first reading, gives 9. Return to NOT.3 for the meaning of an occurrence and NOT.4 for the transformation's conditions. If one sample is intended, bind that sample once and reuse it. If two observations are intended, retain both. The measurement method supplies the meaning of a read; [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md#cmp12---construct-an-interpreter-or-a-meaning-preserving-translation) supplies an effective interpreter when software must execute the expression.

6. **Repair the remaining burden only if it matters.** If common parameter changes are still laborious, [NOT.7 - Redesign a Notation around the Reader's Difficult Operations](#not7---redesign-a-notation-around-the-readers-difficult-operations) compares one accessible definition of b with repeated independent entries. The shared definition makes a common edit local but adds reference-following for individual readings. Keep the table for frequent lookup if that benefit warrants its maintenance. A later local exception returns to the sharing assumption: it cannot be expressed by a global parameter change alone.

The result can be the new expressions, a sufficient table, an exposed conflict or a missing interpretation. Applying the rule to a physical quantity requires the corresponding subject account; the arithmetic construction supplies no observation of that subject.

### NT-CARRY-A-SEQUENCE - Keep a sequence usable when its reader or reference frame changes

- **Situation:** A spoken or gestured instruction must also support later inspection, comparison or execution by another reader.
- **Question:** Which references and intermediate results must survive the change of carrier or reader?
- **First useful result or blocker:** A recoverable ordered account with its reference frame and interpretation, or the missing information or performer capability.
- **Start with:** [NOT.8 - Construct Temporal or Embodied Notation with a Reading Procedure](#not8---construct-temporal-or-embodied-notation-with-a-reading-procedure) for the reference and reading route; use NOT.5 when an interpreted sequence is available but the proposed translation loses what its receiver needs.
- **Stop or return:** Stop at the required reading. A changed frame returns to the interpretation; a request for enactment requires the performer's method and the observation needed to establish its result.

#### Worked connection for NT-CARRY-A-SEQUENCE

1. **Retain the references needed after a sign has passed.** A plan describes successive completed displacements on a grid. East is positive x, north positive y; the starting position is (0,0) and the performer faces north. `R` means one unit to the performer's right without turning; `F(2)` means two units forward without turning. The spoken score is `R; F(2)`, where the semicolon means complete the first displacement before starting the second. To inspect it later, use NOT.8 to construct a persistent companion with the same ordered signs, starting pose and frame convention. NOT.6 connects each spoken occurrence to its position in that score. Retain these references rather than only a list of recognized words.

2. **Carry the interpreted state to the next operation.** Use NOT.3's reading procedure: recover the facing direction, convert each displacement to grid coordinates, update the position, then read the next sign. Here R gives (1,0); F(2) then gives (1,2). No turn occurs. The intermediate position lets a receiving reader ask where the first displacement ends. The score leaves duration and the continuous path within each displacement open. Speaking it more slowly changes the delivery time, but supplies no new movement duration or distance.

3. **Test the translation against its receiving question.** An endpoint-only description gives (1,2). It is sufficient for the final-position question under this starting pose. It loses the order needed to recover the intermediate position: `F(2); R` has the same endpoint but passes through (0,2) rather than (1,0). NOT.5 therefore retains the ordered displacements when the receiver needs that distinction. A richer display of the endpoint alone cannot restore it. If a proposed abbreviation changes order while preserving only the number of signs, NOT.4 must return to the observation that the transformation was meant to preserve.

4. **Propagate a frame change, or change the score for a different intention.** Now the performer starts facing east, with the same body-relative signs and no turns. R moves south to (0,-1); F(2) moves east to (2,-1). NOT.6 updates the derived grid account from this changed premise. If the actual request is to retain the old grid displacements instead, define grid-relative signs `E(1)` and `N(2)` as one unit east and two units north, each without turning, and write `E(1); N(2)`. This restores the specified waypoints (1,0) and (1,2). Construct these new sign rules through NOT.2 and use NOT.3 to recover their different reading. The continuous path cannot be recovered from the old score alone, because it was never specified.

5. **Pass the right result to a performer.** A program receiving the ordered account still needs CMP.12's input representation and effective interpretation. Physical enactment additionally needs an applicable motion method, physical meaning for a grid unit, timing choices and control. A prepared person may already possess the required movement method. FPF B.5.MPC connects the mathematical, physical and computational contributions when the work needs all three; interpreted observation is needed to establish what movement occurred. The decoded endpoint is already a useful answer to the reading question.

This connection applies whenever changing medium or reader can remove references needed for later operations. A rhythm, laboratory signal or interaction trace needs its own relevant time references and subject rules. The movement case shows how the methods work together; it does not supply those other interpretations.

## Continue with the contribution the work needs

A notation can support thinking by keeping an assumption, dependency or alternative available for another operation. It can support methodology by making the descriptions of a working method usable together. When those descriptions serve different users, [ME.9 - Relate Method Representations across Their Different Uses](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me9---relate-method-representations-across-their-different-uses) selects and relates the claims those uses need; NOT.6 constructs their notational correspondence.

A missing inference belongs to the mathematical, physical, computational or other subject method that supplies it. A reader who lacks an available operation may need explanation or capability development. Change the notation when its form, references or interpretation cause the difficulty; obtain the other contribution when that is what prevents the next result.

# Notational Engineering - Preface

## NOT.Preface:1 - Problem frame and the work of designing a notation

Use this language when an expression's conventions need to be constructed or changed so that people or computational agents can work with it. The work may involve mathematical reasoning, a model, an algorithm, a diagram of a method, a movement score or another structured expression. Its subject supplies the distinctions and correct consequences; notational engineering supplies ways to make those distinctions expressible and usable.

A reader can recognize all the signs and still be unable to compose them, recover a dependency or perform the next transformation. Two displays can look consistent while referring to different objects. An abbreviated instruction can rely on preparation that its new reader lacks. These difficulties become especially visible when descriptions pass between specialists, people and AI agents.

Begin with one operation and an expression on which it matters. You need enough subject knowledge to say what a correct result would be, or access to someone who can supply that contribution. The individual methods then expose their additional prerequisites: rules for binding names, an interpretation, an allowed transformation, a temporal reference or a performer's available operations. Knowing a particular branch of mathematics, physics, programming or music is required only for a use that needs it.

Keep a sufficient notation when its conventions already serve the work. A.6.3.RT.OE in FPF helps construct an expression around a needed operation under available conventions. This DPF becomes useful when the conventions themselves leave a consequential distinction, interpretation or manipulation unsupported. Repair a mistaken subject account at its source; notation design can make that mistake visible without supplying the subject's answer.

## NOT.Preface:2 - Forces that shape the choice

| Requirement | Choice it creates |
| --- | --- |
| Express the needed distinctions | More detail can support one inference while obscuring another. |
| Make a frequent operation easy | A form convenient for lookup can make revision or composition expensive. |
| Preserve meaning during change | A compact rewrite can hide binding, side conditions or an observable intermediate result. |
| Retain complementary strengths | Several forms can aid different operations while adding correspondence and update work. |
| Fit the reader's preparation | A familiar shorthand can depend on acquired skills or an interpreter unavailable to the next reader. |
| Fit the medium | A persistent inscription, a sound and a gesture make different inspection and replay operations available. |

A notation's quality is relative to the work, reader and access conditions. C.2.8 characterizes the structure a reader can recover from a publication under stated resources and preparation. Use that common account when comparing expressions; the number of symbols or successful recognition of their names does not by itself measure useful understanding. C.11.DUA helps decide when an additional comparison can change the choice enough to warrant its cost.

## NOT.Preface:3 - The methods and their connections

### NOT.Preface:3.1 - Design what can be expressed and done

[NOT.1](#not1---choose-the-distinctions-and-operations-a-notation-must-support) derives a design requirement from the operation and from cases that need different treatment. [NOT.2](#not2---define-expression-rules-for-recoverable-binding-and-composition) constructs formation, grouping, scope and reference rules. [NOT.3](#not3---give-expressions-an-operative-interpretation) gives the resulting expressions a meaning and a route by which a prepared reader obtains a consequence. These contributions connect what the work needs, what can be written and what the reader can do with it.

[NOT.4](#not4---construct-transformations-of-expressions-that-preserve-their-use) constructs changes to expressions, with their applicability conditions and preserved observations. A mathematical argument may justify a rewrite. A computational procedure may apply it. A surrounding physical or organizational use determines whether the preserved observation is sufficient. The same marks can therefore admit one transformation in a pure calculation and require another treatment when each occurrence performs an interaction.

### NOT.Preface:3.2 - Translate, combine and improve notations

[NOT.5](#not5---translate-between-notations-while-tracking-lost-distinctions) constructs a translation with the receiving question in view. It identifies losses, needed supplements and the limits of returning to the source. [NOT.6](#not6---coordinate-complementary-representations-through-shared-references) keeps several useful forms in joint use: it connects their referents and dependencies, then interprets an edit before propagating its consequences. A derived display value and an independently observed value can require different treatment even when they occupy similar cells.

[NOT.7](#not7---redesign-a-notation-around-the-readers-difficult-operations) locates an actual reading or editing burden, changes the expression or editing arrangement there, and compares both the intended improvement and effort moved elsewhere. [NOT.8](#not8---construct-temporal-or-embodied-notation-with-a-reading-procedure) adds the origins, frames, segmentation and available replay or enactment operations needed when signs unfold in time or bodily action. A temporal score can need the same formation, interpretation, translation and redesign methods as a static diagram.

There is no compulsory eight-stage process. Enter where the difficulty occurs. A translation loss can return to the original design requirement. An inconsistent update can expose a reference problem. A reading difficulty can require teaching a missing operation rather than another symbol. The working reminder for a longer combination is: **Recover the operation; make references and interpretation usable; carry the intended change; retain useful differences; repair the remaining burden.** The relevant bodies supply the conditions under which each continuation is needed.

### NOT.Preface:3.3 - Constituent actions in ongoing work

Defining an operator's binding rule can be part of constructing an expression grammar while a notation for working calculations is being designed. If users must transform an expression without changing its meaning, visually convenient grouping is insufficient: the interpretation of the transformed expression must remain recoverable. Symbol recognition and subject knowledge can both be present while the intermediate ability to follow binding and transformation rules is absent. The notation design must provide those rules and support their use; a successful reading of one expression does not establish the whole notation's suitability.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Use the parts of the vertical that can change the present result. A Method described here can require additional capability, available support and compatible resources at other grains.

## NOT.Preface:4 - Worked connection - A formula, graph and table must change together

### NOT.Preface:4.1 - Construct the expressions and their interpretation

A group uses a simple rule, `r(q,b) = q + q + b`, over real numbers. Here q is one supplied input value and b is a shared parameter. The immediate work is to obtain values, inspect dependence on b and change that parameter. This stipulated mathematical example supplies its own interpretation; applying it to a price, measurement or other subject would require a separate account of that subject.

NOT.1 makes the operations explicit. A list of output values supports lookup at listed inputs. It does not necessarily support changing the rule or obtaining an answer at an unlisted input. NOT.2 fixes the references: both q occurrences use the same supplied value; b denotes the same parameter throughout this use. Parentheses or graph connections determine which operands each addition consumes.

For an operation graph, connect the input q to both inputs of one addition, then connect its result and b to a second addition. NOT.3 interprets those connections as addition of the supplied real values. With b=1 and q=0, 1 and 2, the outputs are 1, 3 and 5. A reader can obtain them by following the graph without a software implementation.

NOT.4 permits the transformation `q + q + b` to `2*q + b` under that interpretation. The arithmetic identity supplies preservation for every admitted q and b. A shorter inscription may be useful for changing or explaining the rule, but its symbol count does not establish that every reader will find it easier.

### NOT.Preface:4.2 - Translate only as far as the receiving question allows

NOT.5 translates the rule at b=1 into the table `(0,1), (1,3), (2,5)`. Lookup at those three inputs survives. The table alone does not determine the value at q=3: both `2*q + 1` and `2*q + 1 + q*(q-1)*(q-2)` agree on its rows, but give 7 and 13 respectively at q=3.

If the receiving work needs the general rule, retain that rule or a sufficient construction of it alongside the table. If it only needs the three listed values, the table can suffice. There is no reason to demand recovery of discarded distinctions that cannot affect the requested use.

### NOT.Preface:4.3 - Interpret an edit before propagating it

Now a participant asks that the output at q=1 become 4 while the coefficient 2 remains fixed. NOT.6 treats this as a constraint on the rule, not as an isolated replacement of a displayed cell. It gives `2*1 + b = 4`, hence b=2. The graph receives the new parameter; the table becomes `(0,2), (1,4), (2,6)`. Its former values were derived outputs, so they are recalculated.

If another participant also requires the old output at q=0 to remain 1, that requirement gives b=1. It conflicts with b=2 under the retained rule. The useful result is the conflicting pair of requirements and the assumption on which it depends. Silently choosing one edit would conceal the decision that the group must make.

An independent measurement record is different again. If its row says that an observed output was 3, a parameter change does not change that past observation. Keep the record and updated prediction separately so that the difference can inform the subject inquiry. Correspondence between representations does not license overwriting every similarly named value.

### NOT.Preface:4.4 - Change the operation and revisit the affected construction

Suppose a later description replaces each occurrence of q with a fresh sensor read. This changes the operation assumed in :4.1. If consecutive reads return 4 and 5 while b=1, `read() + read() + b` returns 10; `2*read() + b` using the first reading returns 9. The former rewrite is still correct for a single supplied q, but it cannot be transferred to this new interpretation merely by replacing the printed name.

NOT.3 restores what an occurrence now does; NOT.4 reopens the transformation's condition. If the intended operation is to take one sample and reuse it, explicitly bind that sample once. If two observations are required, retain them. CMP.12 provides the algorithmic interpretation when implementing those instructions. The physical measurement method supplies what each read obtains and under which conditions. These are connected contributions, and each has a result that another performer can consume.

Finally, NOT.7 can compare the group’s editing arrangements. A single named b avoids separately editing every derived row, while a table remains useful for direct lookup. Keeping both requires the correspondence already constructed in NOT.6. The comparison is about the actual operations, not a declaration that formulas or tables are universally better.

The connected result is a usable rule, its complementary expressions and an account of what the change affects. An adequate answer may be the new table, the conflict, or the need for a different reading operation. This combination also applies to other expression families: the arithmetic and sensor supply the worked conditions, while the transferable work is to recover references, interpretation, loss and intended change.

## NOT.Preface:5 - Conditions of use, checks and recurring failures

When a combined use needs checking, ask whether its participants can recover the same subject references, whether each operation has the inputs and interpretation it consumes, and whether a change reaches every dependent expression that matters. Keep independent observations, intended constraints and derived values distinguishable. An unchanged source can retain its previous interpretation; a new receiving question can make a formerly harmless loss important.

Three failures illustrated above need different repairs. More explicit syntax repairs ambiguous grouping or binding. A restored interpretation repairs an unknown operation. A translation supplement repairs a discarded distinction. Repeating a correct legend will not necessarily repair any of them. Use the method that changes the difficulty actually observed.

Prepared readers can fill gaps without noticing. A worked use by such a reader supports that use under its preparation and access conditions. Human learning, performance by an AI agent and reliable machine execution need their own applicable evidence. To assess understanding, ask for an actual consequence and a meaningful change; do not infer general capability from recognition of labels or fluent repetition of the example. EXD and HCD supply explanation and learning methods when those are the missing contributions.

Temporal and embodied uses require further care. Recover the reference that determines when or where a sign applies. A pause may be a specified rest or an observation gap; turning a body changes the room direction of body-right. NOT.8 carries these distinctions through decoding and keeps a correctly interpreted instruction separate from the capability to enact it. Its rhythmic and movement cases offer different ways to test that general method.

Additional assurance should serve the next use. A small construction and its changed-condition case can settle a local design choice. A claim about faster human learning or broad usability requires more than that construction. Seek the corresponding evidence when that stronger claim matters; retain the useful bounded result meanwhile.

## NOT.Preface:6 - Consequences and Architectural Rationale

This repertoire makes the expression and its interpretation available for deliberate work. Practitioners can expose a tacit step, preserve a useful rewrite, return from a lossy summary, coordinate complementary forms or redesign an expensive operation. They can hand a named contribution to another person or computational agent without assuming that the receiving agent reconstructs the same conventions unaided.

The organization follows operations across media. A catalogue organized by mathematical symbols, programming languages, diagrams, music and dance is valuable for finding established conventions. It would repeat several design problems here while hiding their common structure. Conversely, imposing one universal notation would sacrifice distinctions or useful operations of particular practices. The selected methods support reuse of existing notations and construction of differences where the receiving work needs them.

Formation, interpretation and transformation have distinct results. A well-formed expression can still lack an interpretation; an interpreted expression can lack an effective evaluation algorithm; a valid result can be expressed in a form that makes its revision difficult. Keeping those questions separate lets their methods connect without crediting syntax for a mathematical proof, a computational construction or a performer's preparation.

Translation and coordination also differ. A one-way translation may deliberately discard information irrelevant to its receiver. Continued joint use needs correspondence and an update policy, sometimes retaining several noninterchangeable accounts. Redesign then asks whether the resulting reading and editing operations justify their combined burden. NOT.8 specializes these operations where temporal or embodied carriers change the references and access conditions; it does not make every notation a performance score.

The two Parts group this presentation. They do not prescribe an order of work or imply that all eight methods are parts of every project. A narrower mathematical, programming or performance profile can reuse several bodies and add the rules peculiar to its practice. Such a profile must state which new operation or distinction it adds. The present language provides no complete grammar for every subject and no general theory of perception or learning.

## NOT.Preface:7 - Shared sources, alternatives and refresh

The bodies preserve their adopted contributions and limits. Several source lines also explain the arrangement of the language as a whole.

| Source line | Contribution and comparison |
| --- | --- |
| Blackwell and Green's [Cognitive Dimensions account](https://www.cl.cam.ac.uk/~afb21/publications/BlackwellGreen-CDsChapter.pdf), especially activities and notation/environment distinctions | This historical framework makes the actual operation and design trade-offs discussable. NOT.1 and NOT.7 connect those observations to a construction and a comparison. A list of desirable dimensions alone does not decide a redesign. |
| [NotaScope](https://ieeevis.b-cdn.net/vis_2023/pdfs/v-full-1328.pdf) and the [2024 Programming User Experience method](https://ppig.org/files/2024-PPIG-35th-brazauskas.pdf) | Matched expression galleries and structured expert observations can expose design differences. The bodies retain the limits of metrics and the small expert study; they do not turn either into a universal measure of understanding. |
| Formal expression, binding and graphical-reasoning sources in NOT.2–.4, including Macbeth, Dutilh Novaes and Piedeleu/Zanasi | Their contributions make the permitted manipulations and the reader's reasoning operations explicit. The synthesis allows syntax and spatial arrangement to support reasoning while requiring the actual interpretation and applicable rule. A resemblance between drawings alone supplies neither. |
| [Bidirectional programming](https://janis-voigtlaender.eu/papers/ThreeComplementaryApproachesToBidirectionalProgramming.pdf) and [partial states](https://link.springer.com/chapter/10.1007/978-3-032-22723-2_2) | These constructions expose information loss, retained complements and different meanings of an update. NOT.5–.6 adapt those questions to coordinated representations; automatic two-way copying is inadequate when a target edit is ambiguous or conflicts with a retained condition. |
| Ainsworth's [DeFT account](https://www.inf.ufpr.br/alexd/REPRESENTACOES_EXTERNAS/Ainsworth_2006.pdf) and the [recent meta-analysis of multiple representations](https://link.springer.com/article/10.1007/s10648-024-09958-y) | Complementary forms can constrain interpretation and support different operations, but coordination and preparation cost matter. These contributions support a conditional choice of several forms, not an assertion that adding forms always improves learning. |
| Solkattu, Takadimi, movement-notation and auditory-notation sources compared in NOT.8 | Different conventions reveal the importance of temporal reference, segmentation and the distinction between a score and its realization. The synthesis keeps their differences rather than assigning one meaning to every syllable, gesture or silence. |

Current rewriting and binding research can improve how expressions are transformed; bidirectional methods can change which updates are recoverable; empirical studies can revise the assumed burden for particular readers and media. Reopen the affected method when such a contribution changes its construction or supported use. A newer source or more familiar convention alone does not establish a better choice.

## NOT.Preface:8 - Relations to the rest of the Suite

[Mathematical Thinking](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md) supplies objects, compositions, arguments and interpretations used when the represented construction is mathematical. [Computational Thinking](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md) supplies effective procedures, including interpreters and translations. NOT designs the expression conventions those methods can consume; it does not substitute a mathematical meaning for an algorithm that obtains its consequence.

[Mathematical Modeling](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md), [Physical Thinking](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/PHYSICAL-THINKING-DPF.md) and FPF C.29 connect a subject with mathematical constructions and interpreted observations. B.5.MPC coordinates mathematical, physical and computational contributions when they are jointly needed. NOT.5–.6 help express those correspondences while keeping the related objects and claims distinguishable.

Within [Engineering DPF Suite](https://github.com/ailev/FPF/tree/main/Engineering%20DPF%20Suite), Method Engineering's ME.9 relates the claims needed when different uses of a working method require complementary descriptions; EXD develops explanations; HCD develops and assesses capabilities. They remain external contributions, used when the work needs that result. A notation repair can help any of them, while an operation missing from the method or from the reader's preparation needs the corresponding method or learning contribution.

The [Suite Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) locates the publications and their shared architecture. Use the cited body's operative rules when its question arises. If an available edition changes those rules or no longer supplies the result your use needs, revisit that dependency rather than assuming that the shared PatternID guarantees compatibility.

## NOT.Preface:End

# Part A - Design what can be expressed and done

## NOT.1 - Choose the Distinctions and Operations a Notation Must Support

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.1:1 - Problem frame

**Use this when** you are choosing or designing a notation and cannot yet say what its users must be able to express, recognize or do with an expression. A candidate may name all the right objects while hiding their order, dependence or duration. Another may express the distinction but make a frequent change require rebuilding the whole description.

Start with a piece of work: composing operations, comparing two models, tracing a dependency or performing a sequence are examples. Identify an operation that a person or computational agent needs to carry out using the notation. Then find two cases that this operation must treat differently. Trying to express and use those cases gives the first design requirement that can be acted on.

The reader needs enough knowledge of the practice to explain why the cases differ and what a useful result would be. That knowledge can come from a collaborator. Choosing the notation does not require the designer to perform every specialist inference unaided; it does require access to the distinctions that those inferences use.

The result is a choice of distinctions and operations to support, together with a small expression or interaction that shows how a proposed notation could support them. It may instead be a reason to keep an existing notation, preserve an unresolved choice, or obtain a missing account of the work before adding symbols.

If a suitable notation already exists and only one expression needs repair, construct that expression under its rules using A.6.3.RT.OE. Return here when the rules themselves lack a needed distinction or make the required operation impractical.

### NOT.1:2 - Problem

How can a notation designer determine what the notation needs to make possible before committing to its symbols and rules?

A list of concepts leaves the work underdetermined. The same concepts can enter different compositions, questions and changes. A notation sufficient for recognizing an object may be insufficient for constructing it; a description sufficient for one question may discard what another question needs. Designing from familiar examples alone can conceal these differences until somebody tries a new case.

### NOT.1:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Discrimination and economy | Showing more distinctions increases expression and reading work; omitting one can prevent the required conclusion. |
| Reading and changing | A compact finished description can be expensive to revise. |
| Shared conventions and reader preparation | Familiar conventions save explanation for one group while imposing learning or translation on another. |
| Expression and environment | A distinction may be carried by marks, layout, an interaction or available context. Changing the medium can remove that support. |
| Present work and discovery | Trying a notation can expose a useful operation absent from the initial requirements. |

### NOT.1:4 - Solution

**Choose a working operation → find a consequential difference → locate what carries that difference → try a notation choice → compare the work it enables and displaces → retain or revise the requirement.**

#### NOT.1:4.1 - Choose an operation and the conditions for performing it

Describe what the user starts with, what they do and what they need to obtain. Prefer a question such as “after exchanging these two operations, what changes in the result?” to an aim such as “make the notation intuitive”. The former exposes what an expression must support.

Specify the preparation and access on which the operation relies. A mathematician may use established algebraic conventions; a performer may recognize a learned gesture; a program may receive only serialized text. An AI agent's access to a rendered page, a text extraction and an editor's internal structure are different conditions. Include the context that is actually available, rather than assuming that every reader receives the designer's view.

For a small task, one operation is enough to begin. If the notation will be used for a family of operations, choose cases that exercise materially different demands. For example, interpreting a completed expression and changing a shared component can need different support. Do not turn this selection into an inventory of every conceivable use.

#### NOT.1:4.2 - Find cases whose difference changes the work

Construct or recover a pair of cases that require different answers, permitted changes or actions. Explain the difference in the practice before deciding how to write it. Two arrangements of the same components can have different outputs; two performances with the same starting times can have different sustained intervals.

Attempt to express both cases with the candidate notation and its allowed context. If they become indistinguishable while the required answers differ, something needed by that operation has been omitted. Recover it through an expression rule, an accessible annotation, a query to another representation or a narrower declared use. The choice depends on how the expression will be used.

Conversely, two visibly different cases may be interchangeable for the present operation. Keep their shared representation if that simplification preserves the needed result. The question determines which differences matter.

A deliberately unfinished choice can itself matter. If the work permits an unspecified order or duration, retain a way to leave it unspecified and a way to recognize when the next operation needs it settled. A convention that silently chooses a value would change the work being described.

#### NOT.1:4.3 - Locate the information and operations behind the marks

Follow the user through the proposed operation. Which part of the expression identifies a participant, establishes a relation or permits a transformation? Which part is supplied by a convention, the surrounding account or an interaction with a tool?

This examination can reveal three different needs:

- The difference is known but cannot be expressed or recovered under the available rules. Design a way to carry it.
- The expression carries the difference, but obtaining or changing it is too costly. Change the arrangement or the supported operation; NOT.7 develops that redesign.
- The practice has not supplied the needed distinction or inference. Obtain that contribution from the relevant practitioner or method before prescribing how it must be expressed.

Test the whole expression and its usable context. A symbol may be ambiguous in isolation yet clear in a composition. A diagram may be clear to a prepared human reader while its plain-text export loses the grouping on which that reading depends. Preserve the effective context or revise the notation for the receiving conditions.

#### NOT.1:4.4 - Try a design choice through use

Propose a small change capable of supporting the selected operation. Examples include marking operand groups, adding a reference to a shared component, exposing event duration, or making an unresolved alternative visible. Construct the contrasting cases with that change and carry out the operation using the proposed reading rule.

Where modification matters, change an input, component or relation and follow the resulting edits. A notation that displays one finished example well may make the required family of changes error-prone or laborious. Include a contrasting case that challenges the same rule, rather than polishing the first example until it looks convincing.

Separate the notation's contribution from supplied subject knowledge. In a diagram for composing functions, arrows can expose the order of application; the functions and the ability to apply them supply the numerical result. If the result cannot be obtained because an algorithm or physical law is missing, return that question to the corresponding practice.

An expert walkthrough can establish an explicit loss or a useful candidate change. When it remains uncertain whether the intended reader can recover or perform the operation, use C.2.8 to choose a bounded reading probe with the intended preparation and access. Obtain further evidence only when its outcome could change the design or the permitted use.

#### NOT.1:4.5 - Compare the work enabled and the work displaced

Compare candidate notations on the selected operations under comparable conditions. Look for a practical trade-off: a shared definition may make one update cheap while requiring the reader to follow references; expanded expressions may be easy to read locally while repeating changes in several places.

Keep both alternatives when they serve different necessary operations and the correspondence between them can be maintained. NOT.6 develops that arrangement. For a choice among alternatives, compare only characteristics that affect the work and state the selection criterion. A simple contrast can settle the local choice: one notation loses an answer that the other preserves.

When the comparison must be reused across alternatives or design iterations, A.19.CPM governs comparison under a declared comparator; A.19.SelectorMechanism governs selecting a set from those results under stated criteria. A Pareto criterion can retain alternatives that are not dominated on the chosen characteristics. It does not by itself resolve a trade-off between reading and editing effort. Keep that trade-off visible until the work supplies a reason to choose, or retain both notations for their different uses. A vocabulary of design trade-offs can help notice a difficulty, but a vocabulary or weighted checklist cannot establish that a user can perform the operation.

Trying a candidate can reveal that the original question was incomplete. Revise the selected operations or cases when the newly visible distinction changes a useful next move. Then test the affected requirement again. This is a development of the problem and its proposed solution, for which C.40.CD supplies the common method.

#### NOT.1:4.6 - Retain the decision at the scale needed for the next construction

State the operation to support, the distinction it needs, how a candidate carries it and the burden or unresolved choice that remains. A short explanation beside the candidate can suffice. Keep the contrasting cases when they will help construct, teach or revise the rule; no separate requirements document is necessary for an ordinary small use.

Stop when the next notation construction or choice is clear enough to undertake. Detailed expression formation, interpretation and transformation can then be developed where needed. Do not reopen every design choice merely because a new example is available; reopen the choice whose supported operation or conditions changed.

### NOT.1:5 - Archetypal Grounding

#### NOT.1:5.1 - Same components, different composition

A team is designing a diagram notation for constructing pipelines of functions. Its first sketch shows the input, output and an unordered collection of function names. The current operation is to determine the result and then exchange two functions without losing their connections.

Use the supplied functions `f(z) = z + 1` and `g(z) = 2z`, with input `3`. Applying `f` then `g` gives `g(f(3)) = 8`. Applying `g` then `f` gives `f(g(3)) = 7`. Both cases have the same named components. The unordered sketch therefore loses a difference that the operation needs.

The designer tries directed connections, with the rule that a connection passes the output of one function to the input of the next:

```text
3 -> f -> g -> result     gives 8
3 -> g -> f -> result     gives 7
```

Now the reader can recover the composition order and derive each result from the supplied functions. Exchanging the two functions changes their connections; merely dragging a box on the page must either preserve those connections or expose that it changed them. The design has acquired both an expression requirement and a question about the editing operation.

If the diagram is only an inventory of available functions, the original unordered sketch can remain adequate. If later work needs branching or shared intermediate results, try those operations before deciding how their connections and identities will be expressed. Success with this linear case leaves those questions open.

#### NOT.1:5.2 - Same starting times, different durations

A notation for a sequence of signals lists their starting times in units of a shared pulse. Two sequences both start signals at `0` and `2`. In sequence A each signal lasts one unit; in sequence B each lasts two. The intervals are half-open: the signal is active at its start and inactive at its end.

For the question “when should each signal begin?”, the list `0, 2` suffices. For “is a signal active at time 1.5?”, it does not: the answer is no for A and yes for B. The omitted duration now changes the answer.

Try pairs of `(start, duration)`. Sequence A becomes `(0, 1), (2, 1)`; B becomes `(0, 2), (2, 2)`. The reader adds duration to start and compares 1.5 with the resulting interval. This exposes the needed difference with one simple convention. A timeline with interval bars might make repeated overlap questions easier; the pair notation is easier to transmit as plain text. Their comparative value depends on the operation and access.

If a performer's action determines the duration later, retain that unresolved value and identify which questions remain answerable. Suppose the first signal's duration is still to be chosen between 1 and 2. Write `(0, d)` with `d in {1, 2}, not yet chosen`. In either permitted case the signal is active at 0.5; at 1.5 the answer remains unresolved. Choosing `d = 2` makes the latter answer yes. The starting-time question remains answerable throughout. This continuation adds a requirement to preserve an unfinished choice, with no default that prescribes behavior the work has left open. Temporal and embodied notation design in NOT.8 develops such cases beyond this elementary timing example.

### NOT.1:6 - Bias-Annotation

Fluency can hide a notation's demands. A designer who knows the answer may supply order, grouping or duration from memory while believing the expression carries it. Test the selected operation with only the expression, declared conventions and available context. C.2.8 distinguishes this expert judgement from an actual reader's recovery.

A successful notation for one audience can require unavailable preparation in another. Preserve the audience and operation when drawing conclusions; human reading results do not establish an AI agent's interpretation, or vice versa. Check the receiving conditions that can change the choice.

### NOT.1:7 - Conformance Checklist

Use these questions to examine the design decision when its adequacy matters. They do not require a separate written answer for each ordinary application.

- Can the intended user identify the working operation, its starting information and the result they need?
- Does a consequential difference between cases explain why the selected distinction is required? If a difference is omitted, is the resulting loss acceptable for that use?
- Is the necessary information available in the expression, its declared conventions or an accessible interaction?
- Has the proposed rule been used on the contrasting cases, including a change when modification is part of the work?
- Are the subject knowledge and reader preparation needed for that use recoverable?
- Does the next construction follow from the decision, with remaining uncertainty and displaced work visible where they matter?

### NOT.1:8 - Common Anti-Patterns and How to Avoid Them

| Failure | What changes the next move |
| --- | --- |
| Choosing symbols from a concept inventory | Add the relation or operation that distinguishes cases. The pipeline inventory names both functions but loses their order. |
| Validating recognition while relying on manipulation | Try the required change. A reader's ability to name a diagram's boxes leaves the effect of moving or reconnecting them unresolved. |
| Requiring every difference to be written | Keep the simpler expression when the omitted distinction cannot change the selected result; the onset list suffices for starting times. |
| Completing an unknown to fit the notation | Express the unresolved choice or narrow the answerable question. A supplied duration would change the partly designed signal sequence. |
| Treating a familiar layout as shared context | Check what the receiver receives. Text export can remove grouping used in the displayed diagram. |

### NOT.1:9 - Consequences

The next notation decision becomes a choice about work that can be attempted. A designer can explain why a distinction, convention or editing operation is needed and can recognize when a simpler notation suffices.

The method costs representative construction and use. It can reveal a gap in the subject account that notation design alone cannot settle. Its result is local to the selected operations and conditions; extending use can expose another requirement. Keeping the contrast behind a decision makes that extension easier to reason about.

### NOT.1:10 - Architectural Rationale

A notation provides ways to form and use expressions. What to support depends on what the user needs to obtain or change. Starting with that operation connects the subject matter, reader preparation and representation without making any one of them a substitute for the others.

Contrasting cases make an omitted distinction consequential. If two cases with the same available representation require different answers, a reader using only that representation cannot be guaranteed the right answer in both. The design must recover the difference, obtain additional information or accept the resulting limitation. This argument identifies a requirement; trying the supported operation is still needed to learn whether the candidate is usable at the available effort.

The pattern chooses requirements through small constructive trials. NOT.2-.4 develop formation, interpretation and transformation rules. A.6.3.RT.OE addresses a different starting condition: the scheme is available and an operative expression must be built under it. C.2.8 characterizes what a prepared observer can extract; the present method uses that question to construct or choose a scheme. These contributions can be combined without making notation design a compulsory step in every reading task.

### NOT.1:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Blackwell and Green, [Cognitive Dimensions of Notations](https://www.cl.cam.ac.uk/~afb21/publications/BlackwellGreen-CDsChapter.pdf), historical foundation, especially the activity and system analysis sections | Adopt analysis relative to activity, notation, environment and medium. The method uses concrete operations to expose costs and trade-offs. It retains the source's warning that the dimensions are not a checklist yielding a universally best notation. |
| Brazauskas and Blackwell, [PUX Explorer](https://ppig.org/files/2024-PPIG-35th-brazauskas.pdf), PPIG 2024, §§2, 4.2 and 6 | Adapt the co-development of design problem and solution and the activity/experience comparison. Its study involved six specialist music-notation researchers. This supports a design aid at that scope, not general performance gains. Its trade-off weights were assigned from textual descriptions; they are not measured universal effects and are not imported here as quality scales. |
| Ross and colleagues, [Affordances of Sketched Notations for Multimodal UI Design and Development Tools](https://arxiv.org/abs/2508.09342), 2025 preprint, abstract-level contribution | Retain the distinction between isolated-symbol recognition and interpretation of a whole contextual sketch in AI-assisted work. The abstract motivates checking the receiving context. It does not establish a general advantage of a particular design or interpreter. |
| Kruchten, McNutt and McGuffin, [Metrics-Based Evaluation and Comparison of Visualization Notations](https://ieeevis.b-cdn.net/vis_2023/pdfs/v-full-1328.pdf), IEEE VIS 2023, §§3–4 | Reuse matched examples and their metrics to locate differences for closer reading when comparing working notations. The method assumes expressions implementing the shared tasks. Its metrics do not capture the whole user experience or supply a universally best notation. |

**Choosing the design move.** When the needed distinction is still unknown, construct a contrasting pair first. A gallery-based comparison already needs expressions that implement chosen tasks; preparing that gallery cannot replace discovering the missing task or distinction. Once several viable notations support a stable family of work, a shared set of examples becomes useful: compare the same readings and edits, use metrics to find costly cases, then inspect those cases. This costs more than the first pair but can expose repeated-change burdens hidden by one successful example. Reopen the small comparison when that broader burden could change the choice; NOT.7 develops the corresponding redesign. Cognitive Dimensions and PUX can also help discover or reformulate the operations to compare.

The contrast-based requirement construction and the two worked cases are the present synthesis. They connect notation design to available FPF representation, extraction and problem-development methods without prescribing one notation across practices.

### NOT.1:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| A.6.3.RT and A.6.3.RT.OE | Supply representation-scheme distinctions and the construction of an operative expression under available rules. A missing rule can become a notation-design question here. |
| C.2.8 | Characterizes recoverable structure for a prepared reader with stated access and effort; use it when extraction difficulty changes the notation choice. |
| C.40.CD | Develops a problem and candidate ways of dealing with it together when a notation trial changes the useful question. |
| C.11.DUA | Helps decide whether another comparison or reader probe can change the choice enough to justify its cost. |
| A.19.CPM and A.19.SelectorMechanism | Govern reusable comparison and set selection under declared conditions; preserve trade-offs instead of forcing one winner. |
| MATH.17/.18 and CMP.12 | Supply mathematical constructions and interpretations, or an effective interpreter and translation. They develop consequences and operations whose needed expression can be selected here. |
| NOT.2-.4 | Develop the chosen expression-formation, interpretation and transformation rules. |
| NOT.5/.6 | Develop translation and complementary representations when the needed operations call for more than one notation. |
| NOT.7/.8 | Develop redesign around difficult operations and notation whose distinctions unfold in time or embodied action. |

### NOT.1:End

## NOT.2 - Define Expression Rules for Recoverable Binding and Composition

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.2:1 - Problem frame

**Use this when** a notation needs rules for combining expressions or referring to their parts, and the proposed marks leave those rules unclear. Readers may disagree about an operation's operands, the declaration an occurrence of a name uses, or which connections join two components.

The working question is “How can another user construct and recover the intended arrangement under these rules?” Start with one expression that admits two consequentially different readings. Give its components explicit places, make their grouping and references recoverable, and use the resulting construction to perform the intended operation.

The result is a small set of formation, binding and connection rules demonstrated by an expression and a contrasting case. These rules can support mathematical formulas, diagrammatic descriptions or structured sequences. A complete grammar or software parser is needed only when the work requires it.

The reader must know what the relevant components and operations mean, or obtain that account from a practitioner. The examples below require elementary arithmetic and the stated conventions. Theory of formal languages and category theory are optional tools for extending or proving properties of a scheme.

Use the rules already provided by a suitable notation when they settle the question. A.6.3.RT.OE helps construct an operative expression under such a scheme. Use NOT.1 first if the work has not yet determined which distinctions or operations the notation must support.

### NOT.2:2 - Problem

How can the rules for forming an expression expose its components, references and permitted composition well enough to support the required reading or change?

A printed formula can conceal two groupings. The same letter can name an external parameter and a locally introduced variable. Diagram ports with the same value type can have different roles. Correctly recognizing the individual signs therefore leaves open which whole has been expressed.

### NOT.2:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Compact writing and recoverable structure | Omitting delimiters saves space but can hide an operand boundary. |
| Local naming and larger composition | A useful short name inside one component can collide with a name supplied by its surroundings. |
| Equal types and different roles | Two admissible inputs may occupy different positions in an operation. |
| Flexible presentation and stable interpretation | Layout may change while connections remain; another layout change may alter the expression. |
| Partial construction and usable interpretation | An unfinished expression can retain a missing part, provided the reader knows which operations remain available. |

### NOT.2:4 - Solution

**Identify the constructors and their places → make grouping recoverable → define how references are resolved → define permitted connections → construct and read contrasting cases → abbreviate only what the reader can recover.**

#### NOT.2:4.1 - Identify the expression constructors and their operands

Take the needed operation and distinctions from the working question or NOT.1. Describe the elementary expressions and the ways to construct a larger expression from them. For each construction, identify the required parts and what may occupy each place.

For example, a summation expression needs an index declaration, bounds and a body. A two-input transformation needs both inputs and a way to distinguish their roles. A repeated sequence needs a repeat count and the sequence being repeated. These are different constructors with different rules.

State the restrictions that the intended use needs. The restrictions may concern the kind of an operand, the number and order of connections, or a relation between component interfaces. Keep a missing part visible when partial construction is allowed. Identify the operation that requires the part to be supplied.

#### NOT.2:4.2 - Make the composition structure recoverable

Choose how a user can determine which parts belong to each construction. Text may use delimiters, indentation or precedence; a diagram may use enclosures, named ports or connections. A notation unfolding in time may use a learned boundary gesture or a segmentation convention. Explain the selected rule where its effect is not already established for the intended reader.

Try a nested construction. Recover the outer operation and its immediate parts, then repeat that reading within each part. This is a useful structural reading for tree-like expressions. When a component is shared or a connection returns to an earlier component, expose its reference or connection instead of pretending that every use is an independent nested copy.

Choose the structural distinctions needed by the operation. Some schemes identify several bracketings or drawings as the same expression. Establish the relevant equivalence before omitting their differences. If alternatives are intentionally unresolved, show that unresolved choice and postpone only the operation that needs it decided.

#### NOT.2:4.3 - Define which declaration or external value a reference uses

Identify the constructions that introduce local names and the parts in which those names apply. State how a name occurrence reaches its declaration or an input supplied from outside. The visible extent of a box or line becomes a scope boundary only through an established rule of the notation.

For a notation with lexical scope, a common rule resolves a name at its nearest enclosing declaration with that name; if there is none, the value must come from the declared external context. Adopt that rule only when it fits the intended interpretation. Other schemes can make references available through earlier statements, explicit identifiers or connections. Define their resolution accordingly.

Trace the references in one expression with repeated names and one expression with a free input. Here a free input is one whose value must be supplied from outside the expression. If insertion, copying or renaming changes which declaration an occurrence reaches, expose that change before treating the result as equivalent. NOT.4 develops transformations that preserve the intended use.

For a reusable component, distinguish its locally introduced names from the inputs and results made available at its boundary. Compose components by those boundary references. A displayed label can be repeated without identifying its occurrences as the same declaration; the reference rule must settle that question.

#### NOT.2:4.4 - Define the permitted connections between components

Specify which component places can be connected and what the connection means for forming the expression. If a connection passes a result to an operand, include the operand's position or role as well as its accepted kind. Two inputs of the same kind may still be ordered.

Construct the compound expression and determine its remaining external inputs and outputs. Check each newly connected boundary; an unconnected required input remains an input to be supplied. If the scheme permits shared values, show how repeated references obtain that value. If it describes resources whose copying requires an operation, include that operation rather than deriving copying from a forked line alone.

A connection that forms a cycle needs a rule admitting and interpreting that cycle. Depending on the practice, it might describe an equation, feedback through time or a repeated computation. Choose the intended construction before using one picture for these different operations. NOT.3 develops its interpretation, and CMP.12 supplies an effective evaluator when one is required.

Formation rules establish a permitted expression. Whether its described mathematical construction exists, its algorithm terminates or its physical realization works remains a question for the corresponding methods. The rules should expose the information those questions need.

#### NOT.2:4.5 - Construct and read the cases that challenge the rule

Build the intended expression from the declared parts. Recover its grouping, resolve the references and identify the component boundaries. Then perform the required operation with the supplied interpretation.

Use a contrasting case that could reveal a mistaken rule. Depending on the chosen construction, change the grouping, reuse a name inside another scope, exchange two ports or introduce a shared component. Select the challenge because its interpretation can change the result.

If two readers still recover different arrangements that matter to the work, locate the point of divergence. Add or repair the corresponding delimiter, reference rule or connection convention. If both arrangements express the intended equivalence, make that equivalence part of the scheme instead of forcing one arbitrary drawing.

#### NOT.2:4.6 - Retain usable conventions and controlled abbreviations

Keep the rule at the scale required by its next use. A legend and a worked construction can suffice for a local diagram; repeated automated processing can justify a grammar, parser or structural editor. A user must be able to recover any omitted structure that changes the operation.

For an abbreviation, give the expansion or another way to establish its meaning. If several expansions are allowed, show why the difference does not affect the intended use. NOT.4 handles the corresponding preservation argument. Retain a visible distinction when no such argument is available and the choice matters.

The method finishes with rules that permit the required construction and make its use recoverable, or with a specific unresolved formation or interpretation question. Teaching those rules and comparing their reading cost use the relevant learning and explanation methods; a more explicit syntax alone does not establish that a reader has learned it.

### NOT.2:5 - Archetypal Grounding

#### NOT.2:5.1 - A sum with a local index and an external parameter

A team is designing a compact notation for repeated addition. Its proposed expression is:

```text
sum i=1..2 of i + p
```

The notation has not specified where the summation body ends. At external parameter `p = 10`, two readings give different results: `(1 + 10) + (2 + 10) = 23`, or `(1 + 2) + 10 = 13`.

Choose a constructor `sum(index, lower, upper, body)`. It introduces the index only within `body`; bounds use the surrounding context. Choose `add(left, right)` for addition. These rules express the first reading as:

```text
sum(i, 1, 2, add(i, p))
```

The occurrence of `i` in `add(i, p)` reaches the local index declaration. The occurrence of `p` has no local declaration and uses the external value 10. Substituting the two index values gives 11 and 12, then 23. The second reading has a different construction:

```text
add(sum(i, 1, 2, i), p)
```

Its outer operation adds the external parameter once and gives 13. The notation now makes the two operand structures recoverable.

Naming also matters. The expression `sum(p, 1, 2, add(p, p))` is a valid expression under the chosen lexical rule, but both occurrences in its body refer to the index. It gives 6 and no longer uses the external parameter. To rename the index while preserving that parameter, choose a name such as `j` that does not capture it: `sum(j, 1, 2, add(j, p))` still gives 23. This example identifies the binding condition; NOT.4 supplies the general transformation method.

#### NOT.2:5.2 - Two ports of the same type with different roles

A diagram notation describes a ratio operation. It has two numeric inputs, `numerator` and `denominator`, and a numeric output. The supplied rule divides the numerator by a nonzero denominator. Source A supplies 6 and source B supplies 3.

The first drawing joins both sources to an unlabeled box. Knowing that both connections carry numbers leaves their operand positions undecided. Choose named input ports and preserve their identities when the box is moved or redrawn:

```text
A: 6 -> ratio.numerator
B: 3 -> ratio.denominator
ratio.result -> answer
```

The result is 2. Reversing the two input connections is another well-formed construction with result 0.5. Port names make that change visible even though the input types remain the same.

Now enclose the ratio in a reusable component. Its exposed inputs refer to those two ports, and its output refers to `ratio.result`. Renaming the internal ratio box or changing its position can preserve those boundary connections. Swapping the connections changes the expressed operation. A rule that permits the former does not thereby permit the latter.

The same design question arises whenever compatible participants occupy different roles in a relation or operation. More elaborate diagram calculi can give the permitted connections and drawing equivalences mathematical definitions.

#### NOT.2:5.3 - Scope in a structured sequence

Suppose `sequence(A, B)` means perform A and then B, and `repeat(n, S)` means repeat S n times. Then `repeat(3, sequence(A, B))` contains three performances of each action. `sequence(repeat(3, A), B)` contains three of A and one of B. A written delimiter, spoken grouping cue or learned gesture can carry this boundary if the receiver can reliably use its convention. The temporal realization and effort of perceiving or performing it are further questions for NOT.8.

#### NOT.2:5.4 - Resolve a movable label at the time of its use

Three physical cups have permanent numbers 1, 2 and 3, volumes 20, 10 and 0 ml, and capacity 50 ml each. Removable tags A, B and C initially mark cups 1, 2 and 3 respectively. An instruction H says to transfer 5 ml from A to B. Each letter refers to the cup bearing that tag when the transfer is performed.

Write `H; swap-tags(B, C); H`, where the swap moves only tags. The first H gives volumes `(15, 15, 0)` by permanent cup number. After the swap, B marks cup 3. The second H therefore gives `(10, 15, 5)`. Both transfers have sufficient source volume and destination capacity.

The abbreviation H retains a lookup to perform, not cup numbers fixed when H was defined. If the intended instruction instead bound A and B permanently to the original cups, the same two transfers would give `(10, 20, 0)`. The designer must choose the rule matching the work. Changing the tags is an action on the represented situation; renaming a letter in the notation while preserving its reference is a different change.

### NOT.2:6 - Bias-Annotation

A designer can mistake their own intended grouping for a rule already available to the reader. Recover the expression from its declared conventions before relying on the intended result. The sum example separates those two readings with different outputs.

Familiar programming conventions can also be imported into another notation without justification. State the resolution policy that fits the represented work. An arrow, enclosure or repeated name acquires its binding and composition role through that policy.

### NOT.2:7 - Conformance Checklist

Use the applicable questions when the construction rules need checking.

- Can the reader recover the components and the places they occupy from the expression and available conventions?
- Are the groupings that change the operation distinguishable, or explicitly retained as unresolved alternatives?
- Does each needed reference reach its declaration, external input or unresolved place according to the stated policy?
- Do composition rules account for the roles of connected participants and the resulting external boundary?
- Does a contrasting construction expose a consequential change of grouping, reference or connection?
- Can an abbreviation be expanded or otherwise interpreted without losing a distinction needed by the operation?

### NOT.2:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Supplying a constructor list without binding rules | State which constructors introduce names and where those names apply. The sum's index declaration governs its body. |
| Treating a repeated spelling as the same reference | Resolve the occurrence through its context. Local `p` can hide the external parameter in the sum example. |
| Checking input types but ignoring operand roles | Identify ordered or named places. The ratio receives numbers in either arrangement but computes different answers. |
| Letting layout imply an undocumented operation | Define which spatial or temporal relations carry grouping and connection; preserve those relations when changing presentation. |
| Dropping delimiters without recoverability or equivalence | Retain them until the precedence rule or an appropriate equivalence justifies their omission. |

### NOT.2:9 - Consequences

Users can construct expressions whose parts and references can be recovered, and can locate where a change alters the described operation. The same rules provide an input to interpretation, translation and automated processing.

Explicit structure can make an expression longer or impose conventions to learn. Controlled abbreviations and alternative views can reduce that burden once their interpretation is established. A scheme can also require a richer account of scope or interfaces than the first examples revealed.

### NOT.2:10 - Architectural Rationale

Formation, binding and composition answer connected questions. Formation identifies how an expression is built. Binding determines how its references obtain their values or participants. Composition determines how component boundaries are joined. A grammar that answers only the first question can leave the other two undecided.

This method develops the missing rules. NOT.1 selects what the work needs them to support; NOT.3 gives the interpretation and reading operations. A.6.3.RT.OE supplies construction under an available scheme. MATH.17/.18 can describe the operations and their interpretations mathematically, while CMP.12 constructs an effective interpreter or translation when required. The general notation-design result remains usable without first constructing all of those formal accounts.

Different graphical presentations or local names can express the same construction under the chosen rules. Treating them as equivalent requires the corresponding argument; it cannot be inferred from visual similarity. Conversely, giving two ports the same type cannot identify their roles. Keeping those questions explicit allows the notation to help reasoning about the construction itself.

### NOT.2:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Gheri and Popescu, [A Formalized General Theory of Syntax with Bindings](https://www.andreipopescu.uk/papers/bindings.pdf), §2 | Constructors alone leave binding positions undecided. Sections :4.1/.3 add the required binding rules; :5.1 works the sum and capture contrast. The source's alpha-equivalence, freshness and substitution theory supports formal development when needed. Its full mechanization adds no necessary step to the local notation example. |
| Piedeleu and Zanasi, [An Introduction to String Diagrams for Computer Scientists](https://arxiv.org/abs/2305.08768), §2 | Sections :4.2/.4 use typed, ordered interfaces and drawing equivalence under stated equations; :5.2 shows why equal input types alone lose a needed role distinction. Symmetric monoidal categories supply one mathematical class of schemes, not every notation's composition law. |
| Wehmeier, [Binding in classical and dynamic predicate logic](https://link.springer.com/article/10.1007/s10849-026-09472-0), 2026, introduction and §2 | Shared surface syntax can have different semantic binding behaviour. Section :4.3 therefore selects a resolution policy that fits the interpretation instead of treating nearest lexical binding as universal. The paper's proposed general binding schema is not imported into every notation. |
| Dutilh Novaes, [Formal Languages in Logic](https://doi.org/10.1017/CBO9781139108010), 2012, pp. 53-54 and §5.2.1, historical foundation | Keep diagrammatic formation and work with external inscriptions among the available choices in :4.2/.6. This counters selecting textual syntax merely because it has explicit rules. The resulting convention still has to support the reader's operation; explicitness alone establishes no learning advantage. |
| Zwaan and van Antwerpen, [Scope Graphs: The Story so Far](https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.EVCS.2023.32), 2023, §§1–2 and 5 | Scopes, references and declarations can be related by paths with visibility and precedence policies. This is a developed alternative when static name resolution crosses nonlexical boundaries. Its expressiveness and execution costs remain relevant; the method is not a universal account of physical references or component composition. |

**Choosing the rule design.** Retain familiar conventions when they already determine the needed grouping, reference and connection. A constructor list or an implicit layout is cheaper to state, but the sum and ratio cases show the price when it leaves two consequential readings. For that local difficulty, add the missing scope, delimiter or operand role and try the changed expression. This costs more signs or conventions to learn, while preserving a first use through a legend and worked construction.

When static references cross imports or other boundaries that simple nested environments do not handle conveniently, a scope-graph model can make the resolution policy explicit and reusable. It requires constructing those scopes, paths and priorities, and assessing the available implementation. Use that richer account when the reference problem calls for it, rather than adding it to the elementary sum. Likewise, choose a formal binding theory or diagram calculus when its laws are needed for repeated transformation or reasoning.

Revisit the retained choice when a needed expression cannot recover its references or composition, the interpreted operation changes, or a less costly available scheme preserves the same needed distinction. The synthesis is a way to construct and revise those rules; it does not select one notation or one binding policy for every practice.


### NOT.2:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1 | Selects the distinctions and operations the notation must support. |
| A.6.3.RT and A.6.3.RT.OE | Supply representation-scheme distinctions and expression construction when rules already exist. |
| NOT.3 | Develops the interpretation and reader operations that use the constructed expressions. |
| NOT.4 | Develops transformations with the necessary preservation, binding and side conditions. |
| MATH.17/.18 | Supplies operations on operations and interpretations for formal accounts of composition and binding. |
| CMP.12 | Constructs effective evaluation and translation of an admitted expression structure. |
| NOT.5/.6 | Develops translations or complementary expressions while retaining needed references. |
| NOT.7/.8 | Develops redesign for difficult reader operations and notation carried through time or embodied action. |
| C.2.8 | Characterizes what the prepared reader can recover under the actual access and effort conditions. |

### NOT.2:End

## NOT.3 - Give Expressions an Operative Interpretation

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.3:1 - Problem frame

**Use this when** a notation can form expressions, but its users lack a clear way to obtain the consequence those expressions are supposed to support. A legend may explain the signs while leaving the reader to invent how to combine, inspect or manipulate them.

Start with one question an expression should help answer. Give its relevant parts an interpretation, supply the operations needed to read them together, and follow that reading to a result. A useful first result can also be a located gap: a value, interpretation rule or reader capability that must be supplied before the question can be answered.

An **operative interpretation** here connects what an expression stands for with what a prepared reader can do to obtain a needed consequence from it. Reading can involve calculation, inspection of a diagram, rule-based manipulation or enactment. The reader may be a person or a computational agent; the applicable operations and preparation depend on that reader.

The designer needs the intended subject account and the operations on which the reading depends. The first example uses elementary Boolean reasoning, explained in the case; the temporal example uses addition and interval comparison. A machine implementation is a further construction when required.

Use an existing interpretation directly when it already supplies the needed reading. A.6.3.RT.OE addresses building an operative expression under an available scheme. Use the present method to develop or repair the scheme's interpretation and its reading operations. NOT.2 addresses missing grouping, binding and connection rules.

### NOT.3:2 - Problem

How can a notation's interpretation give its intended reader a usable way to obtain a consequence, while keeping the conditions of that consequence recoverable?

Assigning names to marks can leave their combined use unexplained. Assigning a mathematical meaning can specify an answer without providing a way to obtain it. A familiar reader may bridge either gap from experience while a new reader cannot tell which operation is missing.

### NOT.3:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Meaning and obtaining | An expression can denote a result that the available reader cannot compute or recognize. |
| Local rules and whole expression | A reading of each component must account for their composition and context. |
| Useful tacit skill and recoverable preparation | A trained perceptual or manipulative operation can be efficient but unavailable to another reader. |
| Several reading routes and one required consequence | Different routes can expose different structure or cost different effort while agreeing on the intended answer. |
| Represented condition and actual occurrence | A model can imply a result without establishing that the described situation obtained. |

### NOT.3:4 - Solution

**Choose the consequence → interpret the expression's parts and composition → supply the reading operations → perform a case → test a consequential change → retain the usable reading and its conditions.**

#### NOT.3:4.1 - Choose what the reading must produce

State the question, the expression and the information available outside it. Identify what would count as a useful result. Examples include the value of a formula, a permitted next action, whether two intervals overlap, or a consequence of a diagram's relations.

Distinguish obtaining the expressed answer from establishing its use in the subject matter. Reading an interval from a schedule can answer what is planned; observing what happened needs the corresponding observation. The interpretation should identify which question it answers.

Specify the reader's available operations. It may be reasonable to presuppose arithmetic, following a visible connection or a trained movement. Expose a less familiar operation if the intended reader could otherwise mistake its absence for a defect in the expression. A short prerequisite explanation can suffice; a capability that requires practice belongs in the appropriate learning method.

#### NOT.3:4.2 - Interpret components, composition and context

For the parts used by the question, specify what they denote or instruct and how their combination is interpreted. Include grouping and reference rules from NOT.2. An arrow may supply an input to an operation, express a precedence condition or prescribe a movement; choose its role in this scheme before deriving a consequence.

Give the interpretation of a compound expression in terms that permit its use. For a compositional mathematical scheme, interpret the parts and then apply the corresponding operation to their interpretations. MATH.5/.18 develops that construction and its preservation questions. When context contributes to interpretation, include the relevant context among the inputs rather than assigning a context-free meaning that the notation does not support.

If the expression admits alternatives or has an unresolved part, specify what can still be concluded. A reader may be able to obtain a common consequence across the alternatives. Another question may have to wait for the missing information. Preserve that distinction instead of silently completing the expression.

#### NOT.3:4.3 - Construct the reading operations

Show how the intended reader moves from the expression and available inputs to the result. For each indispensable step, identify what is inspected or changed and how the next step uses what was obtained. The procedure may reuse an established method rather than explain that method again.

For a formula, this can mean resolving a parameter, evaluating selected subexpressions and combining their values. For a diagram, it can mean identifying a boundary, following the admitted connections and applying the corresponding inference. For a performed notation, it can mean recognizing a cue and executing a learned action. Choose operations that the reader can actually perform under the stated conditions.

Keep the reasoning behind a manipulation available at the level required by the work. A rule may be applied fluently after training, while changing the rule requires understanding what it preserves. NOT.4 develops expression transformations; B.5.RC/RA helps recover an unfamiliar construction or argument when that is the missing contribution.

If a mathematical interpretation leaves the required obtaining procedure unavailable, name that remaining problem. CMP.12 constructs effective evaluation when the expression's operations admit it; other CMP methods can help construct the needed algorithm. Denotation alone does not establish computability or affordability. A human reading or trained perceptual operation also needs its actual capability and access conditions.

#### NOT.3:4.4 - Perform the reading and locate where it depends on additional knowledge

Take an expression whose relevant parts and input values are supplied. Carry the reading through to its stated result. At a step that cannot be performed, distinguish a missing input, an undefined interpretation and an unavailable operation. These lead to different repairs.

Compare the result with the intended consequence under the subject account. Repair an interpretation rule when it yields a different answer. Repair the reader preparation or access when the rule is usable in principle but cannot be carried out under the current conditions. If the subject account itself leaves the consequence unresolved, return that question to the corresponding mathematical, physical, computational or other practice.

When more than one reading route is offered, perform the routes on a case that could expose a difference. Establish the agreement needed by the use, or explain why the routes answer different questions. A route that only returns a final value may lose the dependency structure another operation needs.

#### NOT.3:4.5 - Change one condition that matters to the interpretation

Change a value, grouping, reference, context or intended question that could alter the result. Use the same rules to recover the new answer, or locate the rule that must change. The challenge should test the chosen interpretation rather than introduce an unrelated subject problem.

For a formal family, a general argument can establish that the reading operations implement the interpretation across that family. MATH.18 supplies interpretation-preservation questions; CMP.12 supplies executable translation and evaluation. For human or embodied use, C.2.8 can characterize what the prepared reader recovers and distinguish an expert walkthrough from observed use. Choose further checking when it can change the interpretation or permitted reliance.

#### NOT.3:4.6 - Keep the operative reading available to its users

Provide the interpretation, the indispensable reading operations and their prerequisites where the intended user can find them. A legend, one worked reading and a reference to a known method may be enough. A new operator needs enough explanation to use it, rather than only a new name.

Stop when the required consequence can be obtained at the declared scope, or when the missing contribution and the next way to obtain it are clear. Retain a slower explanatory route alongside a fluent route when users need to learn, justify or change the operation. A further notation redesign belongs to NOT.7 if the reading works but imposes avoidable difficulty.

### NOT.3:5 - Archetypal Grounding

#### NOT.3:5.1 - Turn a condition diagram into a reading procedure

A team designs a notation for combinations of conditions. Labels `P`, `Q` and `R` refer to conditions with supplied truth values. An `ALL` enclosure holds only when every enclosed condition holds. An `ANY` enclosure holds when at least one enclosed condition holds. The conditions are stable while the expression is read, and reading them does not change their values.

Consider:

```text
ALL {
  P
  ANY { Q R }
}
```

The legend defines the operators, but a new reader still needs a way to apply them to a nested expression. Supply this reading procedure: resolve each condition label from the given inputs; evaluate the innermost enclosure; replace it by its Boolean result; continue outward.

With `P = true`, `Q = false` and `R = true`, the inner enclosure is true because R is true. The outer enclosure combines true with true, so the whole condition holds. This result concerns the supplied conditions. Establishing their truth in an actual project is separate work.

A second route examines only values that can still change the answer. For `ALL`, one false child settles the result as false; for `ANY`, one true child settles it as true. With the same inputs, the reader checks P, then Q and R, and obtains the same result. If P changes to false, the outer `ALL` is false without inspecting Q or R. The stable, side-effect-free condition premise makes this omitted reading legitimate.

Now change the inner operator from `ANY` to `ALL` while keeping the original inputs. The inner result becomes false and therefore the outer result becomes false. The reader has followed the changed expression through the same interpretation rules. Replacing a label without resolving its value would leave a different gap: the input is missing, not the nesting rule.

The two reading routes expose a choice about obtaining the answer. They agree on these Boolean results; one shows every intermediate value, while the other can avoid work. A user who also needs all intermediate values should retain the first route or extend the second to produce them.

With P false and the values of Q and R not supplied, the whole expression is still false. A request for every intermediate value still needs those missing inputs.

#### NOT.3:5.2 - Recover what an interval notation means before using it

A signal plan contains the pair `(2, 4)`. The notation designer must say whether the second component is an ending time or a duration. Under the first interpretation, the planned active interval is `[2, 4)`; under the second it is `[2, 6)`. Half-open intervals include their start and exclude their end.

Choose `(start, duration)`. Give the reader two operations: add duration to start to obtain the end, then test whether a queried time is at least the start and less than the end. At time 5 the planned signal is active, because `2 <= 5 < 6`. If duration changes from 4 to 2, the new end is 4, and the signal is inactive at time 5.

The pair's two numeric entries did not establish this interpretation by themselves. The chosen convention and the comparison procedure make the answer obtainable. A timeline can support another reading by locating the queried point against a drawn interval, provided its scale and endpoints carry the same values.

This answers a question about the plan. To determine whether a device actually emitted the signal at time 5, obtain the relevant observation and the conditions relating it to emission. The notation can retain that observation or a model of the device, but the planned interval alone supplies neither.

### NOT.3:6 - Bias-Annotation

Expert familiarity can conceal a reading step. A fluent reader may move from a symbol to a consequence without noticing the convention or skill used. Recover that step when it changes what another reader needs to know or be able to do.

The opposite bias treats every interpretation as a complete algorithm awaiting transcription into code. A mathematical meaning can leave an obtaining problem unsolved, and a practiced perceptual operation can lack a suitable machine realization. Keep these different contributions visible when allocating work among agents.

### NOT.3:7 - Conformance Checklist

When the interpretation needs checking, ask the following questions at the scope of the proposed use.

- Is the consequence to be obtained distinguishable from the subject claims on which it depends?
- Do the used parts, their composition and relevant context have an interpretation?
- Can the intended reader identify and perform the indispensable reading operations, or locate the missing input or capability?
- Does the worked reading obtain the stated result without an unexplained inference supplied only by the author?
- Does a consequential change lead to the corresponding new result or to a located interpretation question?
- If several routes are offered, is their agreement or difference established for the observations the user needs?

### NOT.3:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A legend names signs but leaves composition unused | Read a compound expression through to its result. The condition example needs a rule for proceeding through nested enclosures. |
| Treating a denotation as an available computation | Identify the operation that obtains the denoted answer and its conditions, or return the missing algorithmic problem. |
| Hiding a learned reading skill | Explain the operation or name the preparation needed to perform it. Test access and capability where uncertainty changes the next move. |
| Reusing a shortened reading after its premise changes | Recheck which observations it preserves. Short-circuit reading in the first case presupposes stable conditions without reading effects. |
| Reading a plan as a report of events | Obtain the observations needed for the event claim; the signal schedule alone states what is planned. |

### NOT.3:9 - Consequences

The notation acquires a path from expression to a useful consequence. Users can distinguish a missing input from a missing rule or capability and can allocate those contributions among people and computational agents.

Providing an operative interpretation can require more work than defining symbols. Several reading routes may be worth retaining because users need different intermediate results or have different preparation. A successfully performed small case supports that use; wider claims need the corresponding argument or experience.

### NOT.3:10 - Architectural Rationale

The interpretation connects representation with work. It identifies the meaning relevant to a question and the operations through which a reader can obtain a consequence. Neither a symbol inventory nor a description of intended meaning alone guarantees that those operations are available.

The separation between interpretation and obtaining preserves generality. MATH.18 can establish a mathematical interpretation. CMP.12 can construct an effective evaluator under its algorithmic conditions. NOT.3 asks what reading the notation is to support and supplies the missing connection for its intended user. It can therefore include a manual or embodied route without assuming that every semantic assignment is computable.

Several useful readings may expose the same structure differently. Choosing among them can change the work needed to recover an answer or the intermediate structure made available. This is one reason to design notations around operations, rather than treating them only as shorter ways to write conclusions.

### NOT.3:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Macbeth, [Seeing How It Goes: Paper-and-Pencil Reasoning in Mathematical Practice](https://doi.org/10.1093/philmat/nkr006), 2011, opening discussion and treatment of Peirce's alpha graphs, historical foundation | Adopt the distinction between recording an answer and working through signs to obtain or expose reasoning. Her different readings of a graph motivate retaining useful reading routes. Their mathematical case does not establish equal accessibility to every reader. |
| Dutilh Novaes, [Formal Languages in Logic](https://doi.org/10.1017/CBO9781139108010), 2012, §5.2, historical foundation | Adapt attention to the operations people perform with external inscriptions and the preparation those operations require. Treat the cited human studies at their studied scope; no general learning gain or cross-agent equivalence follows here. |
| Piedeleu and Zanasi, [An Introduction to String Diagrams for Computer Scientists](https://arxiv.org/abs/2305.08768), mathematical syntax/semantics account | Use compositional interpretation when the notation and target operations admit it: the whole interpretation follows the specified combination of parts. This offers a formal alternative to a merely demonstrated reading. The required obtaining procedure and the reader's access still depend on the intended use. |

**Choice between approaches.** If a known formal interpretation and an available evaluator already answer the question, use them; a new reading procedure adds no value. When the difficulty is obtaining the consequence from a new notation, the present method supplies that route and locates its tacit requirements. A trained reading can be useful before a full formal calculus exists; a broader preservation or automation claim can justify constructing that calculus through the mathematical and computational suppliers.

### NOT.3:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1/.2 | Supply the required operations and the formation, reference and connection rules. |
| A.6.3.RT.OE | Constructs an operative expression when the scheme and reading operations are already available. |
| MATH.5/.18 | Constructs and compares mathematical interpretations, including consequences preserved through composition. |
| CMP.12 | Constructs an effective interpreter or meaning-preserving translation when the obtaining problem is algorithmic. |
| B.5.RC/RA | Recovers the construction or argument needed when a reading contains an unfamiliar step. |
| NOT.4/.5 | Develops use-preserving transformations and translations once the relevant interpretation is available. |
| NOT.7/.8 | Develops an easier reading or a temporal/embodied notation where the available route remains difficult. |
| C.2.8 | Characterizes recoverable structure under the reader's preparation, access and effort conditions. |
| C.29 and B.5.MPC | Connect an interpreted mathematical consequence with its physical subject and the work needed to use it. |

### NOT.3:End

## NOT.4 - Construct Transformations of Expressions That Preserve Their Use

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.4:1 - Problem frame

**Use this when** an expression is difficult to read, derive from or change, and you need a rule for turning it into a more useful expression without losing the consequence on which the work relies. Examples include naming a repeated construction, exposing a hidden intermediate step, regrouping a diagram, or replacing a long sequence by an expandable abbreviation.

Start with the reader operation that is difficult. Construct a proposed manipulation from the expression's formation and interpretation rules. State where the manipulation applies, explain what it preserves, then obtain and use a transformed expression. The result can instead be a located condition that prevents the proposed transformation.

The reader needs the notation's interpretation and the subject laws used in the manipulation. NOT.2 supplies grouping and reference rules; NOT.3 supplies interpretation and reading operations. Elementary arithmetic and ordered sequences suffice for the worked cases. More specialized laws can be supplied by a collaborator.

Apply an existing transformation directly when its rule and conditions already answer the question. Use this method when that rule must be constructed, extended or repaired. A change of notation calls for NOT.5's translation and recovery work. Constructing an effective interpreter or compiler calls for CMP.12. Choosing a different physical process or working method requires the corresponding subject methods as well as a way to express the change.

### NOT.4:2 - Problem

How can a notation provide useful transformations whose applicability and preserved consequences remain understandable when the expression or its context changes?

A visually simpler expression can hide a necessary distinction. Reusing a name can bind an occurrence that previously referred elsewhere; combining repeated signs can combine two actions that were meant to occur separately. A valid equality may hold only under a local assumption. Without those conditions, a transformation can preserve one displayed answer while changing the work it is supposed to support.

### NOT.4:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Easier use and retained distinctions | A compact or regular expression can discard information needed by another operation. |
| Local manipulation and surrounding context | Replacing a part must respect the names, connections and assumptions supplied by its surroundings. |
| One useful result and a reusable rule | A successful instance supports that instance; a rule for a family needs an argument covering that family. |
| More alternatives and search cost | Keeping several equivalent forms can enable a later move while increasing the work of finding and comparing them. |
| Meaning and execution | Equal mathematical values can come from computations or actions with different effects and costs. |

### NOT.4:4 - Solution

**Choose the use to preserve → construct the manipulation → establish its conditions → transform and read → challenge the changed condition → retain the useful rule or alternatives.**

#### NOT.4:4.1 - Choose the operation and the observations to preserve

Identify the expression, its interpretation and the next operation that should become easier. The aim may be to see a shared construction, carry out an inference, change one definition, or recover a particular step in a sequence. A shorter expression is useful only insofar as it helps such work.

State what must remain obtainable. A numeric value, a sequence of actions, the identity of a shared component and an explanation of intermediate steps are different demands. Retain the distinctions used by the actual question. If users need both a compact result and the derivation, keep the derivation available rather than assuming the result reconstructs it.

For a computation or action description, include the effects that matter: repeating a measurement twice can produce different inputs from reading one measurement twice. CMP.12 develops the corresponding execution-preservation question. A purely mathematical reading may require only equality of values under its stated interpretation.

#### NOT.4:4.2 - Build a rule from the structure causing the difficulty

Follow the difficult reading or edit and locate the expression structure responsible for it. Propose a manipulation using the available constructors and interpretation laws. For repeated subexpressions, try a named definition and references to it. For a long regular sequence, try an abbreviation with a defined expansion. To expose an inference, try expanding a definition or introducing an intermediate expression justified by a subject law.

Describe the matched form and its replacement, including which parts may vary. Preserve the surrounding expression and the connections through which it uses the replaced part. A diagram rule needs the relevant input and output places, not only similar-looking boxes. NOT.2 supplies those structural distinctions.

Introduce a name with a scope that reaches the intended occurrences. Choose a fresh name, or rename conflicting bound occurrences consistently, when the new scope would otherwise change an existing reference. Repeated spelling alone does not establish that two occurrences can be replaced by one shared definition.

For a growing rule family, construct several candidates and reuse previously established laws. Automatic enumeration or an AI proposal can help generate candidates. Their source of generation does not establish their validity: connect each used rule to its interpretation or an already established derivation. The search and validation algorithms belong to the applicable computational methods; this method determines the notation operation they must realize.

#### NOT.4:4.3 - Establish where replacement preserves the needed consequence

Interpret the matched form and the replacement under the same allowed inputs and context. Follow the meaning of their parts and composition far enough to obtain the required agreement. Use a known law where its premises hold; derive the missing law when that is the unresolved mathematical contribution. MATH.17 and MATH.18 supply operations-on-operations and interpretation reasoning.

Check the conditions that the proposed rule actually uses. Freshness of a name matters for introducing a binding; defined division matters for cancellation; an ordered boundary matters for a diagram connection. For a rule such as `x/x -> 1` over real numbers, `x != 0` is necessary. A condition established inside one branch remains local to that branch.

When replacement may occur inside a larger expression, show that the relevant enclosing constructors respect the chosen agreement. If the rule preserves a final value but changes an intermediate observation used outside the replaced part, restrict the replacement or retain that observation. A local equality under one assumption is not permission to merge every occurrence of the same printed term.

For a single bounded use, a direct derivation can suffice. For every expression in a family, establish the corresponding general argument. A separating case can refute the proposed rule; agreement on a few examples cannot establish a universal law. Choose additional checking when uncertainty about the rule can change its permitted use.

#### NOT.4:4.4 - Construct and use the transformed expression

Match the rule to the selected expression, instantiate its varying parts and satisfy its side conditions. Replace only the matched part, reconnect it to its surroundings and read the resulting expression using the notation's rules. Obtain the answer or perform the edit that motivated the transformation.

Compare the actual work before and after. A named definition can remove repeated edits while adding reference-following. An expanded derivation can be longer while making a missing inference accessible. Preserve both forms when they serve different needed operations; NOT.6 develops their maintained correspondence.

If the new form loses information needed to continue, restore that information or narrow the claim to the uses it still supports. Retaining a link to a derivation or an expandable definition can be enough. A label saying that the expressions are equivalent does not supply the missing reading procedure.

#### NOT.4:4.5 - Challenge the condition most likely to fail in reuse

Change a relevant binding, assumption, input class or intended observation. Repeat the affected transformation and reading, or explain why the rule no longer applies. Test the rule's boundary rather than adding an unrelated difficult example. Sections :5.1 and :5.3 show changed bindings and local assumptions.

If a transformation is to run automatically, give CMP.12 the admitted expression structures, matching and replacement rules, and observations to preserve. An algorithm for repeatedly applying rules also needs a search strategy and a stopping condition. The availability of several valid rewrites does not imply that applying them in arbitrary order terminates or finds the most useful form.

#### NOT.4:4.6 - Retain a useful rule or a useful set of forms

Keep the rule, the conditions that matter to its use and a recoverable reason for the preserved consequence. A short explanation beside a simple rule is enough when no larger account is needed. Reopen the affected rule when its interpretation, allowed context or required observation changes.

For one known operation, stop after a suitable transformed expression is obtained. When committing to one form repeatedly blocks other useful transformations, retain alternatives and defer the choice. Equality saturation is one computational way to represent many equivalent forms and select from them. It requires a suitable expression theory, valid rules, a selection criterion and resource limits; it is not the default procedure for a small manual rewrite.

Compare retained forms by the work they support, using NOT.1's comparison and NOT.7's redesign where needed. No one presentation needs to serve every reading, derivation and edit.

### NOT.4:5 - Archetypal Grounding

#### NOT.4:5.1 - Name a repeated construction without capturing another input

A reader wants to see and change the repeated construction in `(x + 1) * (x + 1)`. The expression denotes ordinary integer arithmetic with a fixed input x. Introduce a local definition: `let v = x + 1 in v * v`. Here `let` gives v the value of its defining expression within the following body.

At x = 3 the original expression gives `4 * 4 = 16`; the new one first obtains v = 4 and then the same result. For any integer x, substitution of v's definition recovers the original expression, establishing the general equality under this interpretation. To change the repeated construction to x + 2, change the one definition. The new value at x = 3 is 25, and expansion shows both occurrences received that change.

Now use a larger expression `u + (x + 1) * (x + 1)` with external inputs u = 10 and x = 3. Introducing `let u = x + 1 in u + u * u` is wrong: it turns the external u into a local reference and produces 20 instead of 26. A fresh v gives `let v = x + 1 in u + v * v`, which produces 26. The repair changes the binding choice, not the arithmetic law.

The rule applies to the pure arithmetic interpretation supplied here. If each occurrence instead instructs a fresh observation, sharing their results changes the operation. For example, two sensor reads may return 4 and 5, whose product is 20; one read returning 4 reused twice gives 16. Retain two observations unless their consolidation is justified for the intended use.

#### NOT.4:5.2 - Compress a sequence while preserving its order

A notation describes ordered cues A and B. The sequence `A; B; A; B` is to be shortened without changing the order of cues. Define `repeat 2 { E }` to expand into two copies of the entire finite sequence E, preserving its order. Then:

```text
A; B; A; B  ->  repeat 2 { A; B }
```

Expansion returns A, B, A, B. The third cue remains A. A reader changing B in every repeated unit can now change it once in the repeated body. If only the final B must change to C, expand or separate that occurrence: `A; B; A; C`. The earlier abbreviation no longer expresses the intended two identical units.

The tempting form `repeat 2 { A }; repeat 2 { B }` expands to A, A, B, B. It preserves counts but changes the third cue to B. Counts are insufficient for the selected ordered reading. No rule for exchanging cues was supplied.

This notation states cue order. If intervals, accents or bodily actions distinguish the repetitions, retain those distinctions in E or choose a different abbreviation. The order-preservation result alone supplies no claim about those further observations.

#### NOT.4:5.3 - Keep a cancellation inside the condition that permits it

For real x, consider `if x != 0 then x/x else 0`. Only the selected branch is evaluated. Within the first branch, division is defined and the quotient is 1, so the expression can become `if x != 0 then 1 else 0`.

At x = 2 both expressions return 1; at x = 0 both return 0 without evaluating the quotient. More generally, the two branches cover all real inputs and give the same result in each. Replacing the whole expression by 1 would fail at zero. Replacing an unrelated occurrence of x/x outside that guarded branch would also need its own domain condition. The useful transformation follows the local assumption through its scope.

#### NOT.4:5.4 - Reconnect an ordered pair after removing two swaps

A diagram carries an ordered pair of integer values on two wires: port 1 carries a and port 2 carries b. A swap exchanges the two values. Its output is (b, a); a second swap restores (a, b). Replace the two swaps by straight connections preserving port numbers. This argument holds for every integer pair.

The enclosing operation subtracts port 2 from port 1. In compact diagram notation:

```text
(1:a, 2:b) -> swap -> swap -> subtract(1, 2)
(1:a, 2:b) -> straight     -> subtract(1, 2)
```

Both forms return a - b. The replacement makes the source of each subtraction input directly traceable. If the replacement's outgoing wires are accidentally crossed, the enclosing operation instead receives (b, a) and returns b - a. Inputs (5, 2) then give -3 instead of 3; inputs (2, 5) give 3 instead of -3. Retaining two ports without retaining their correspondence loses the required use.

The diagram describes pure value operations, and the enclosing operation consumes only the ordered pair. That interpretation justifies this replacement in its context. Physical wire length or signal delay would be additional observations requiring a different preservation argument.

### NOT.4:6 - Bias-Annotation

A familiar algebraic identity can be applied under a different interpretation without notice. Integer or real arithmetic, finite machine arithmetic and effectful actions can admit different replacements. Recover the interpretation that the actual expression uses before transferring a rule.

The preference for a short final expression can hide the operation a learner or collaborator needs to recover. Retain an expandable or explanatory form when it enables that work. Conversely, keep a fluent compact form when repeated expansion only adds effort to an already understood operation.

### NOT.4:7 - Conformance Checklist

When the proposed transformation needs checking, examine the questions that bear on its intended use.

- Is the reading or edit to improve stated, together with the consequence to preserve?
- Can the matched structure, replacement and their connection to the surrounding expression be recovered?
- Do references, local assumptions and side conditions remain valid at each place where the rule is used?
- Does the preservation argument cover the stated family, or is the conclusion limited to the instances examined?
- Has a transformed expression actually supported the intended reading or change?
- Does the nearby failing case reveal the condition that blocks an invalid reuse?
- Can the work stop with this result, or does a stated further use justify retaining or searching additional forms?

### NOT.4:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Choosing a fresh-looking spelling without checking its scope | Check the existing references. The u-to-v repair in :5.1 preserves the external input. |
| Sharing repeated signs that denote distinct actions | Retain the distinct executions or observations unless their consolidation preserves the needed behavior. |
| Keeping counts while changing order | Expand the sequence rule and inspect the ordered result; :5.2 separates these observations. |
| Promoting a branch-local equality to a global rule | Carry the assumption to each permitted use, as in guarded cancellation. |
| Treating one equality check as a rule for every context | Establish the context-sensitive argument, or keep the conclusion at the checked scope. |
| Applying transformations indefinitely because each is valid | Choose the needed form or use a bounded search with a stopping and selection rule. |

### NOT.4:9 - Consequences

The notation gains a usable way to derive, expose or change expressions. A reader can apply the rule, recognize a failed condition and preserve a useful earlier form when the new one supports different work.

Constructing the rule costs interpretation and sometimes a mathematical argument. More forms can improve choice while making reading, search and maintenance harder. Preserving one consequence leaves other observations to their own conditions; widening use can therefore require retaining additional structure.

### NOT.4:10 - Architectural Rationale

Transformation rules are operations on expressions with an interpretation. Their useful content includes both the replacement and the conditions under which it preserves the relevant consequence. This is why a copied shape or a familiar equality alone is insufficient.

Mathematical construction and computational realization supply different contributions. MATH.17/.18 establishes laws for the transformed operations and interpretations; CMP.12 makes a translation or evaluator effective. The present method constructs a notation-level manipulation for an intended reading or edit. It can be used manually, in an editor or in an automated transformation without identifying those implementations with one another.

The retained observation determines the strength of the rule. Identifying expressions by the same value can discard a derivation, evaluation order or history that another use needs. Selecting that equivalence and respecting it in surrounding constructions makes the limitation explicit. A richer needed result calls for a richer interpretation or another retained form.

### NOT.4:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Piedeleu and Zanasi, [An Introduction to String Diagrams for Computer Scientists](https://arxiv.org/abs/2305.08768), §§2 and 6.1 | Adopt rewriting relative to declared structural laws and matching that respects the expression's boundaries. Their graphical rewriting constructions concern specified categorical structures; an arbitrary diagram does not inherit those equations. |
| Willsey and colleagues, [egg: Fast and Extensible Equality Saturation](https://arxiv.org/abs/2004.03082), POPL 2021, §§2.2, 4 and 5 | Use the distinction between committing to one rewrite and retaining equivalent forms for later selection. Conditional rules and binding analysis show why syntax matching alone can be insufficient. An e-graph relies on supplied valid equations; its compact storage does not establish those equations or guarantee affordable saturation. |
| Hou, Laddad and Hellerstein, [Towards Relational Contextual Equality Saturation](https://arxiv.org/abs/2507.11897), 2025 work in progress, §§1–3 | Retain the distinction between context-local and general equality in :4.3. The proposed contextual reasoning still has implementation and cost questions; it supplies no completed general engine here. The guarded-division case derives a permitted local replacement from its own stated arithmetic conditions. |
| Pal and colleagues, [Equality saturation theory exploration à la carte](https://arxiv.org/abs/2609.14527), 2026 extended preprint, §6.3.1 and §8 | Rule generation can combine guided search and LLM proposals with separate validity checks and derivability from prior rules. The study remains domain-specific; its discussion leaves conditional rule inference partly open. Do not infer a sound general rewrite system from plausible generated rules. |

**Choice of method.** Prefer a directed, justified manipulation when one known operation needs a better expression. An automated search that retains many forms becomes useful when early commitment repeatedly prevents later improvements and the expression theory admits such search. Equality saturation addresses that alternative without making every notation problem a compiler project. Its cost and supplied validity conditions still matter; the current [egglog scheduling tutorial](https://egraphs-good.github.io/egglog-tutorial/04-scheduling.html) shows why deriving a needed condition before expanding alternatives can avoid wasted work. Reopen the choice when the number of interacting rules or repeated uses makes the small direct route inadequate.

The source contributions are combined here with notation requirements and reader operations. The worked arithmetic, cue and guarded-division cases demonstrate distinct conditions of that synthesis, not universal gains from a particular notation or tool.

### NOT.4:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1 | Supplies the operation to improve and the comparison of work enabled and displaced. |
| NOT.2/.3 | Supply expression structure, binding, interpretation and reading operations. |
| MATH.17/.18 | Construct operations on operations and establish the interpretation or composition laws used by a transformation. |
| CMP.12 | Constructs an effective interpreter or translation and relates source and target execution where automation is needed. |
| C.2.8 | Characterizes what a prepared reader can recover from the transformed expression; a formal equality alone does not establish reader accessibility. |
| NOT.5/.6 | Develop translation between schemes and coordination of retained complementary representations. |
| NOT.7/.8 | Develop reader-operation redesign and temporal or embodied notation where those are the affected demands. |

### NOT.4:End

# Part B - Translate, combine and improve notations

## NOT.5 - Translate between Notations while Tracking Lost Distinctions

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.5:1 - Problem frame

**Use this when** work must continue in another notation and you need to construct or repair the translation. A diagram may need a textual form, an ordered performance may need a compact score, or an expression may need a representation accepted by another reader or tool.

Start with the operation the receiving notation must support. Construct its expression from the source's interpreted parts and connections, then use it to obtain the needed answer. Find a pair of source expressions that the translation would make indistinguishable. If the work needs their difference, retain it, enrich the target or restrict the translation's use.

The first result is a usable translation with an answer-recovery procedure, or a demonstrated loss and a concrete way to repair it. Recovering a needed answer, reproducing the source expression and carrying a target edit back are different demands; choose the ones the work actually has.

The reader needs the two notations' formation and interpretation rules, supplied by NOT.2 and NOT.3 where they are missing. Subject knowledge establishes which consequences matter. The examples need directed connections, ordered sequences and elementary arithmetic.

Use an established translation directly when its conditions meet the need. NOT.4 handles transformations within one notation. NOT.6 handles continuing coordination of several representations and their changes. CMP.12 develops an effective translator and its execution-preservation argument when software must perform the translation. A.6.3.RT governs the underlying representation change and the claims it can preserve.

### NOT.5:2 - Problem

How can a change of notation make the next operation possible while keeping its answer connected to the source and exposing distinctions that can no longer be recovered?

Two source expressions can produce the same target expression. The target may still answer a useful question, but a reverse converter cannot infer which source was used from that target alone. A familiar default can conceal this loss. Conversely, requiring complete reversibility can exclude a cheap summary that is sufficient for the actual question.

A target edit adds another difficulty. There may be several source changes consistent with it, each preserving different features of the earlier source. Successful conversion in one direction does not choose among them.

### NOT.5:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Receiving operation and source detail | A simpler target can make one operation easier while removing distinctions needed by another. |
| Meaning and expression form | The same consequence can survive different layouts or spellings; some work also needs those forms retained. |
| Recovery and retained information | Keeping extra source information enables a return but adds storage, access and maintenance work. |
| Forward translation and backward change | A forward rule can determine the view without determining which source update the user intended. |
| Composition and accumulated loss | A locally usable conversion can remove information that a later conversion needs. |

### NOT.5:4 - Solution

**Choose the receiving operation → construct the translation → obtain and return an answer → expose collapsed distinctions → repair the needed loss → establish the required return.**

#### NOT.5:4.1 - Choose what must remain possible

Name the source notation, target notation and intended reader operation. Specify the source expressions admitted for this use and the context required to interpret them. A drawing may use position as meaning or only as layout; a spoken sequence may rely on a separately maintained beat. Carry the context that the question uses.

Decide what the recipient must return: a value, a construction, an explanation, a reconstructed expression or a proposed change. These demands can require different information. An answer expressed in target units or names needs a way back to the source question.

If a source choice is unresolved, preserve the alternatives or the unresolved status that matters to the question. A default introduced by the translation is an added decision. Accept it only when making that decision is part of the intended work and its basis is available.

#### NOT.5:4.2 - Construct target expressions from interpreted source structure

For every kind of source part used by the operation, give its target construction. Then give a rule for translating their composition. Preserve operand order, connections, scope and reference where the interpretation uses them. Copying labels does not supply those rules.

Translate an expression by following its construction. For a diagram, this can mean declaring its nodes and translating each directed connection; for a sequence, translating each event while retaining its position or duration. Derive the target composite from those contributions. NOT.2 supplies the formation and reference rules; NOT.3 supplies the reading operations.

When a source ingredient has no target counterpart, choose an explicit treatment. Extend the target, carry an annotation, leave a visible unresolved part, or limit the admitted source expressions. Make this choice from the receiving operation. Silently deleting the ingredient or guessing its counterpart leaves the recipient unable to locate the loss.

For a mathematical interpretation, MATH.18 develops preservation and reflection of the required constructions and assertions. For a bijective change of mathematical representation, MATH.7 transports the operations through the inverse. Use those arguments when their conditions hold; a correspondence between printed signs alone does not establish them.

#### NOT.5:4.3 - Perform the receiving operation and recover its answer

Translate a small source expression, perform the intended operation in the target and interpret the result as an answer to the original question. Show the return explicitly. If the target gives a list of numbered nodes, say which source nodes those numbers refer to. If it supplies only a bound or a set of possible answers, retain that limitation on return.

Compare this result with what follows from the source under its declared interpretation. A mismatch locates a failed translation rule, a missing premise or a target operation that answers a different question. Repair the affected correspondence before relying on that answer.

A target-side answer can be spurious for the source if the target admits additional possibilities. Retain the source restriction or construct the needed reflection argument. For example, allowing arbitrary real values does not preserve a source question that admits only whole counts.

One successful expression establishes that case. A reusable translation needs an argument for its admitted family, such as a rule-by-rule construction over expressions. A separating example can refute a proposed general claim. Additional checking is warranted when its result can change the use or repair of the translation.

#### NOT.5:4.4 - Expose distinctions the target collapses

Look for different admitted source expressions with the same target expression. Ask whether the required operation gives different answers on them. If it does, the target alone cannot determine that answer: the translation has removed something the work needs. Section :5.2 makes this failure visible through cue order.

If every collapsed pair gives the same needed answer, the loss need not obstruct that question. For a claim about the whole admitted family, justify this independence over that family rather than infer it from a few pairs. MATH.2 supplies the mathematical construction through equivalence classes when that form is useful.

Include differences in assumptions, unfinished choices, references and reading context when they can change the answer. Equal visible strings can have different interpretations under different contexts. Conversely, two differently laid out diagrams can express the same directed structure when position has no role in their interpretation.

For several translation stages, follow the information needed by the final operation through each stage. A later, richer format cannot recover a distinction that an earlier stage removed unless another input supplies it.

#### NOT.5:4.5 - Repair the loss needed by the work

Choose the least burdensome repair that actually restores the operation. Retain the original expression when an occasional return is enough. Add the missing distinction to the target when the recipient must work independently. Otherwise, carry supplementary information with a defined recovery rule.

Call that supplementary information a *complement* when the target and the supplement together permit the required source recovery. State what it contains and how the return uses it. In :5.2 the position of a cue complements its count; in :5.3 a retained phase duration selects one backward update. A statement that the conversion is reversible cannot replace this construction.

Keep the target and its supplement associated with the same source. If the target is edited, check whether the old supplement still permits the intended reconstruction. A stored position can become invalid after deleting an event. Locate that conflict instead of returning an invented original.

The repair may instead be an explicit narrower use. A cue count remains useful for inventory even when it cannot recover order. Retain that useful result and identify the additional contribution needed by an order-sensitive question.

#### NOT.5:4.6 - Establish the return that the work requires

For an unchanged round trip, translate and reconstruct the source at the required level: the same expression, the same interpreted structure or the same needed consequence. State which level is obtained. Recovering a directed graph up to layout does not recover where its boxes were drawn.

For a target edit, construct a backward update using the edited target and retained source information. Specify what remains fixed and what may change. In the ordinary single-view setting, check two properties: returning an unchanged view leaves the source unchanged; translating the updated source yields the requested view. These properties still leave a choice of update policy, worked in :5.3. They do not mean that all possible edits must be accepted.

When several views constrain a shared source, distinguish the user's changed requirement from values merely copied from the earlier view. NOT.6 handles their propagation and possible conflict. An unchanged value in a submitted view is not necessarily an instruction to freeze it.

If conversion performs effects such as asking a reader for missing information or changing external state, include the relevant behavior in the return claim. Recovering the same output value need not undo those effects. CMP.12 supplies the computational correspondence when an executable implementation is required.

Stop once the chosen operation and required return work within their stated conditions. Retain the translation rule, any supplement and the loss that changes later use where the recipient can find them. Reopen the affected construction when the receiving question, source interpretation or admitted edits change.

### NOT.5:5 - Archetypal Grounding

#### NOT.5:5.1 - Translate a dependency drawing without inventing geometric meaning

A drawing has named nodes A, B, C and D. An arrow X→Y means that Y takes X's result as its direct input. Box positions carry no meaning. In one drawing the arrows are A→B and B→C; D is isolated. The receiver must determine C's direct input using ordinary text.

Construct this textual notation:

```text
nodes: A, B, C, D
direct-input pairs (supplier, receiver): (A, B), (B, C)
```

The reading rule selects the pair whose receiver is C and returns its supplier, B. Translating back draws one node per declared name and one arrow per pair. This recovers the named directed structure, including isolated D. It need not recover the original layout.

A list of node names alone fails. The second drawing with A→B and A→C would give the same list but a different answer for C. Retaining the pairs repairs that loss. Retaining only pairs would create a different loss: isolated D would disappear from a reconstructed drawing.

Now suppose horizontal position additionally records a planned start time. The earlier translation still answers the direct-input question, but it cannot reconstruct that timing. Add a start-time value for each node if timing is now needed. That extension follows a changed interpretation or question; it is not evidence that the original drawing already specified times.

#### NOT.5:5.2 - Keep a useful count without pretending it preserves a rhythm

A toy score is a sequence of four equally spaced cue positions. D and T name two distinct sounds; there are no rests. Translate a score into the counts of D and T. Both `D T D D` and `D D T D` become `D:3, T:1`.

The target answers how many sounds are required: four. It cannot answer which sound occurs second. In the first score it is T; in the second it is D. No reverse choice made from the counts alone can recover both originals.

For this family with one T, retain its position as a supplement. Counts plus `T-position:2` reconstruct `D T D D`: place T at position 2 and fill the remaining positions with D. This permits both the count and the second-cue question. If the score may contain several T cues, retain their positions, check that they are distinct and within the score, and check that their number agrees with the count. If rests or unequal intervals become relevant, the chosen description needs further distinctions.

The counts remain a sufficient result for inventory. Reconstructing performance order requires the supplement; reconstructing tempo would require a time scale that this toy score never supplied.

#### NOT.5:5.3 - Choose what a backward update preserves

A plan describes two successive phases by `[A:3; B:5]`, in whole minutes. A summary notation shows only their total, 8. The recipient changes that total to 10. Several source plans fit: `[A:3; B:7]` and `[A:5; B:5]` both do. The new total does not choose between them.

Suppose the work requires A to remain fixed. Retain A's duration, 3, and reconstruct B as `new total - 3`. The requested total 10 gives `[A:3; B:7]`. Returning the unchanged total 8 recovers `[A:3; B:5]`; summing the updated plan returns 10. If instead B must remain fixed, the other update policy gives `[A:5; B:5]`.

Assume phase durations must be nonnegative. A requested total of 2 is incompatible with retaining A at 3. Report that conflict and obtain a changed requirement if the work allows one. Substituting B = -1 would preserve the sum while violating the admitted source plan.

### NOT.5:6 - Bias-Annotation

A familiar target can look more definite than its source. Preserve the source's unresolved choices and restrictions where they affect the receiving use. A translator's chosen default is additional content.

Conversely, fear of information loss can make every conversion retain a complete original. Start with the actual question. The cue inventory needs counts; an editable score needs more. Retain the extra information when it opens a needed operation.

### NOT.5:7 - Conformance Checklist

When the translation needs checking, use the questions relevant to its declared use.

- Can the recipient construct the target from the source parts, connections and required context?
- Can a target result be returned as an answer to the source question at the stated strength?
- Do two collapsed source cases require different answers for any promised operation?
- Does a necessary supplement have a usable recovery rule and remain associated with the right source?
- Is the round-trip claim about expressions, interpreted structures or selected consequences?
- For an edited target, is the backward policy explicit, including incompatible edits?
- Does a changed question or translation stage require a distinction already discarded?

### NOT.5:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Matching labels while losing their connections or scopes | Translate interpreted structure; the node/pair construction in :5.1 retains the required relation. |
| Recovering an arbitrary source and calling it the original | Exhibit the collapsed alternatives and retain the information needed to distinguish them. |
| Treating a useful summary as a complete substitute | Keep its successful use and add the missing information for the new question. |
| Returning a target answer outside the source's admitted cases | Restore the source restriction and the return argument. |
| Accepting a target edit by silently changing a protected source feature | Declare the backward policy and expose incompatible edits, as in :5.3. |
| Assuming a later format restores an earlier loss | Trace the needed distinction through the translation sequence or return to a retained source. |

### NOT.5:9 - Consequences

The recipient gains a usable expression and can tell which answers, reconstructions and changes it supports. A loss becomes a reason to choose a supplement, a richer notation or a narrower use instead of an unexplained conversion failure.

Retained information has an access and maintenance cost. A more restrictive reverse policy can protect a source feature while excluding useful edits. These trade-offs remain choices about the work; a round-trip law alone does not settle them.

### NOT.5:10 - Architectural Rationale

Translation changes the means through which an operation is performed. Its success therefore depends on both interpretation and the receiving operation. Two expressions may be interchangeable for counting and different for performing an ordered sequence.

The constructive loss test gives a local reason for a limit: when one target stands for two sources with different required answers, the target cannot by itself select the answer. Supplementary information repairs that failure only through a defined recovery operation.

Backward change is a further construction. Keeping one source feature fixed and changing another can realize the same target edit as a different policy. This is why two-way translation needs its own use conditions, and why continuing coordination of shared views belongs with NOT.6.

### NOT.5:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Foster, Matsuda and Voigtländer, [Three Complementary Approaches to Bidirectional Programming](https://janis-voigtlaender.eu/papers/ThreeComplementaryApproachesToBidirectionalProgramming.pdf), 2012, §§2–3 | Retain the historical construction of recovery from a view and a complement, and its treatment of partial backward updates. This grounds :4.5–4.6 without requiring complete invertibility of the forward view. Its pure-function setting does not cover every interactive conversion. |
| Xie, Schrijvers and Hu, [Effectful Lenses: There and Back with Different Monads](https://lirias.kuleuven.be/4268513), ICFP 2025, §§2.1–2.2 and 2.5 | Their effect-sensitive round-trip relations extend the pure setting. Use the consequence in :4.6: state which effects the return claim covers. Adopt no general promise that recovering values reverses external actions; implementing their formal framework is a separate computational construction. |
| Matsuda, Nguyen and Wang, [Lenses for Partially-Specified States](https://link.springer.com/chapter/10.1007/978-3-032-22723-2_2), ESOP 2026, §1 | Their shared-source problem shows why a copied value and an intended update constraint differ. Preserve that distinction in :4.6 and return multi-view coordination to NOT.6. The paper's stronger compositional results need its formal partial-state construction; this pattern does not infer them for arbitrary notations. |

**Choosing the translation method.** A bijection with transported operations is a strong choice when both notations express the same required information and a suitable inverse exists. It unnecessarily restricts a useful summary that deliberately omits detail. For that case, construct the receiving answer and retain only the information needed by the required return. A lens-style backward policy becomes useful when edits must propagate; it adds conditions and design choices that a one-way question need not carry. The pure view-and-complement account remains adequate for pure single-view conversions. Effects or interacting views select the stronger lines above when those difficulties actually occur.

This synthesis adapts those computational constructions to notation design by making the reader's operation determine the needed recovery. It does not claim that every diagram, performance or human interpretation already has an effective bidirectional implementation. Reopen the chosen method when a previously harmless loss obstructs a new question, an edit violates its preserved feature, or conversion effects change the relied-on result.

### NOT.5:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| A.6.3.RT | Governs representation changes, preservation of the claimed content and disclosure of loss or narrowed use. |
| NOT.1–.3 | Supply the needed operations, expression construction and operative interpretations used by the translation. |
| NOT.4 | Supplies justified transformations within a notation that can be combined with translation. |
| MATH.2/.7/.18 | Supply quotient-based independence, reversible transport, and preservation/reflection through mathematical interpretations when those constructions apply. |
| C.29.1 | Supplies correspondence and result return when using a mathematical representation for the original problem. |
| CMP.12 | Constructs an effective interpreter or translator and the required relation between executions. |
| NOT.6 | Maintains complementary representations and propagates changes through their shared references. |
| NOT.7/.8 | Develop reading-effort redesign and temporal or embodied representations when the target has those demands. |

### NOT.5:End

## NOT.6 - Coordinate Complementary Representations through Shared References

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.6:1 - Problem frame

**Use this when** different representations support different parts of the work, but a reader cannot reliably combine their results or carry a change between them. A formula can support derivation, a table direct lookup and a diagram recognition of a relationship. Their usefulness together depends on knowing what corresponds and which claims each supplies.

Start with one operation that needs contributions from two representations. Identify the objects, quantities or relations those contributions concern. Construct the correspondence, perform the combined operation, then follow one relevant change through it.

The result is a usable combination: readers can obtain the joined answer, locate a disagreement and update the affected contributions. A discovered incompatibility can instead identify the subject decision that must be made before combining them.

The reader needs the interpretations of the participating representations and the subject relations used to connect them. NOT.2 and NOT.3 supply missing formation and reading rules; NOT.5 supplies a needed translation. A name or explicit correspondence beside the two representations can suffice for a small use.

Keep a single adequate representation when another adds no useful operation. Use NOT.5 for a one-time translation whose target alone supports the remaining work. This method is for continuing joint use, including representations that cannot be fully translated into each other. When different uses of a working method need complementary descriptions, ME.9 relates the claims those uses require; this construction supplies their notational connections.

### NOT.6:2 - Problem

How can several representations jointly support reading, reasoning and change without requiring every reader to reconstruct their correspondence or silently reconcile their disagreements?

Side-by-side placement leaves that work unresolved. Equal names can denote different things; one thing can have different names. A table cell may be calculated from a model or measured independently. A displayed value may be old context or a constraint that a proposed edit must preserve. These differences determine which results can be combined and what should change next.

Forcing all representations into one form can remove the different operations that made them useful. The task is to construct the necessary connections while retaining those useful differences.

### NOT.6:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Local usefulness and joint reading | A representation can work well alone while making its connection to another hard to recover. |
| Shared references and different subjects | An object, its model and its encoded value can be related without being the same thing. |
| Redundancy and maintenance | Repeated content can aid comparison but must follow relevant changes. |
| Automatic propagation and intended edits | Updating every displayed value can erase a constraint or alter independently obtained information. |
| More operations and coordination effort | An additional representation earns its place through useful work, while it adds learning and navigation demands. |

### NOT.6:4 - Solution

**Choose complementary operations → recover referents → construct correspondences → perform a joined reading → propagate the intended change → retain the useful combination.**

#### NOT.6:4.1 - Select representations for the operations they support

Name the working question and the contributions needed to answer it. Use each representation for an operation it actually supports. A table may expose a recorded value, a formula generate values outside the table, and a graph reveal a shape under a declared scale. State what the reader obtains from each.

Keep a representation because it adds a needed distinction, constrains a plausible misreading or enables a useful operation. Do not infer a gain merely from using different media. Try the intended combination before expanding it.

The representations can overlap partially. They need not carry every fact or support identical operations. Identify the overlap needed for this use and the information that remains available only in one of them. Use NOT.5's loss and recovery construction when movement between them needs a translation.

#### NOT.6:4.2 - Recover what each sign refers to

For the joined operation, follow the relevant labels, positions and references to their referents. Establish whether two occurrences concern the same thing, different parts or versions of it, or things connected by a model or measurement relation. The same spelling does not decide this.

Give the correspondence a form the reader can follow: shared labels with a declared meaning, a small pairing table, a drawn connection or an explicit mapping rule. Use stable identifiers when names or positions can change independently. For a temporary two-item comparison, a direct explanation may be enough.

Include the context that makes the reference determinate. A column named time needs its unit and origin when compared with an axis; a position in a repeated score needs its cycle when several cycles are shown. Distinguish actual, planned and modeled values where they are different claims.

One source item can correspond to several target items, or several items to a summary. Show that multiplicity where it affects the operation. NOT.5 identifies what such a projection loses; a repeated label alone does not recover the missing distinctions.

#### NOT.6:4.3 - Construct the relations that let results be combined

Give the reading or construction rule connecting the matched contributions. A formula-to-table relation specifies which inputs generate which cells. A table-to-plot relation specifies axes, units and which cells determine a point. A procedure-to-flow-diagram relation specifies which described actions and conditions each node and connection expresses.

Distinguish a derived representation from an independent contribution. A graph generated from the same table can check rendering but does not supply an independent observation supporting the table's values. An observed trajectory and a predicted trajectory require the subject correspondence and comparison that relate them; C.29 supplies that modeling use.

Decide how a change will be handled. When a value is derived, give its source and transformation. When either side can be edited, give the backward policy or the condition under which a human choice is needed. Preserve information that the other representation cannot reconstruct.

For a chain of correspondences, follow the connection through the intermediate representations. If two routes reach what is supposed to be the same result, determine the agreement the work requires. A numerical tolerance can be appropriate for a plot, while an identity-sensitive reference needs the same referent. MATH.18 supplies the mathematical argument when the correspondence compares formal structures.

#### NOT.6:4.4 - Perform the joined operation

Take one input or object and follow it across the representations. Obtain each contribution, combine them using the stated relation and return the answer to the working question. Show where a reader switches representations and what is carried across that switch.

If the connection exists only in the author's memory, add the missing reference or operation. If the correspondence is clear but the subject inference is missing, obtain that contribution from the subject method or a collaborator. Merely adding another display will not perform the inference.

Use one consequential contrast to challenge the connection. A row with the same label but a different unit, a node in another version or a modeled value beside an observation may require different treatment.

For an immediate use, a worked joined reading may settle the question. A broader claim about how readily users can combine the representations requires evidence appropriate to their preparation and work; C.2.8 characterizes that recovery. Do not infer learning or transfer from the existence of the correspondence.

#### NOT.6:4.5 - Propagate the intended change and expose conflicts

Identify what changed and what the change asks to preserve. Separate an explicit new requirement from values merely retained in an old display. A change to one coefficient can require several table cells to change even if those cells were not directly edited.

Follow the affected references and derivations. Recompute dependent contributions or update their correspondence; leave independent information unchanged unless the subject work calls for its revision. If a representation no longer agrees and cannot yet be updated, make that limitation visible before its next joined use.

When edits arrive through several representations, combine their requirements and check whether a compatible result exists. The result can be several admissible revisions or a conflict. Do not manufacture a unique update when the supplied constraints leave a choice; use the declared policy or obtain the missing decision.

Distinguish changes with the same visible outcome but different meanings. Removing an item from an unfinished-work list can mean completion, cancellation or deletion. The intended action determines which other representations change. A suitable change description can be more informative than comparing two finished displays.

If a model and an observation disagree, return to their governing subject account. Updating the observation to match the model would destroy the independent contribution; changing the model may require a modeling decision. Coordination makes the disagreement usable rather than hiding it.

#### NOT.6:4.6 - Retain the combination at the needed effort

Keep the participating interpretations, references and change rules available where the joint work happens. For a small construction, shared labels, one mapping rule and a worked change can suffice. Repeated edits or many interdependent elements can justify automated propagation, but the software needs the same declared correspondence and conflict behavior.

Stop when the intended joined operation works and the selected change can be handled or its unresolved decision is located. Remove a representation that adds upkeep without enabling a needed operation. NOT.7 helps redesign a connection that is correct but difficult to use.

Reopen the affected correspondence when the subject identity, version, unit, interpretation, reader operation or permitted edit changes. Unaffected representations may remain useful for their own questions even when a particular combined answer is temporarily unavailable.

### NOT.6:5 - Archetypal Grounding

#### NOT.6:5.1 - Combine a formula, sample table and plot without freezing old values

A mathematical account defines `f(x) = 2x + b` for real x. A table stores its values at x = 0, 1 and 2, and a plot shows those same sample points with x horizontally and f(x) vertically. With b = 1, the table values are 1, 3 and 5.

The formula supports a value outside the table: f(3) = 7. The table supplies direct sample lookup; the plot exposes the relative positions of the samples. Connect each row's x to the formula input and each plotted point to that row's pair. The plot is generated from the table. Its agreement is not additional evidence that the formula describes some physical phenomenon.

Now the user requests f(1) = 4 while keeping the coefficient 2 fixed. The relation `2*1 + b = 4` gives b = 2. Recompute the table as 2, 4, 6 and move the plotted points accordingly; the formula now gives f(3) = 8. The old values at 0 and 2 were earlier derived values, not constraints freezing those points.

If the user instead requires f(0) = 1 and f(2) = 5 to remain, the three requested values cannot belong to a line of this form. f(0) fixes b = 1 and hence f(1) = 3. Expose the conflict. Choosing a different model or dropping a requirement changes the mathematical task; silently moving one representation would only hide it.

Finally, the three samples alone do not establish the formula for other inputs. Their generating formula is supplied here. If the table instead contains measurements, recover that different status before treating interpolation as a derivation.

#### NOT.6:5.2 - Link a component label, an adopted dimension and a mesh

A drawing identifies a beam as B9. A dimension note gives its adopted modeling length as 2.00 m. A one-dimensional model uses the variable L for that length, and a computational representation divides it into twenty equal segments. A correspondence states that B9's adopted length supplies L and that segment length is `L/20`.

The reader can now identify which beam a segment calculation concerns and obtain 0.10 m per segment. B9, the variable L and a segment-array entry are different things connected by the stated construction. Replacing their names by one common name would not express that relation.

An accepted model revision changes B9's adopted length to 2.02 m while keeping twenty equal segments. Update L to 2.02 and recompute the segment length as 0.101 m. The component reference remains B9. A copied old segment length of 0.10 would contradict the new construction because twenty such segments total only 2.00 m.

Suppose instead that 2.02 m is a new observation while the dimension note still describes a nominal 2.00 m design. Those values can coexist. Keep their different meanings and let the modeling work decide whether its adopted L changes. The correspondence does not itself turn an observation into a revised design.

This example coordinates quantities and references. It establishes no claim that twenty segments are sufficient for a physical simulation; that is a separate modeling and computational question.

### NOT.6:6 - Bias-Annotation

Visual agreement can be mistaken for independent support. Two displays generated from the same source share its error unless one checks a different contribution. Use the correspondence to distinguish repeated presentation from independent evidence.

The opposite tendency treats every difference as inconsistency. A nominal dimension and a measured dimension, or a prediction and an observation, can legitimately differ. Recover their claim and subject before choosing an update.

### NOT.6:7 - Conformance Checklist

When the combination needs checking, ask the questions that can change its use.

- Does each retained representation support a named operation or needed distinction?
- Can the reader recover the referents and the relation between their occurrences?
- Are derived values distinguished from independent contributions and different claim kinds?
- Can one joined answer be obtained by following the stated correspondences?
- Does a change preserve its actual requirements rather than every value copied from an earlier display?
- Are incompatible edits or interpretations exposed at the affected contribution?
- Can the work stop with the usable combination, without unnecessary synchronized copies?

### NOT.6:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Placing representations together and leaving their connection implicit | Construct the referent mapping and perform a joined reading. |
| Treating a shared label as identity between an object, its model and its encoding | State the relation between those different things, as in B9, L and the mesh. |
| Treating two generated displays as independent confirmation | Trace their common source and identify which new question a comparison can actually test. |
| Freezing all old displayed values during a local edit | Separate the changed requirement from earlier derived context; :5.1 shows the difference. |
| Erasing an observation to make it agree with a prediction | Preserve the observation and return the discrepancy to the subject account. |
| Adding another representation to every explanation | Retain it for a useful operation and compare the added navigation or maintenance burden. |

### NOT.6:9 - Consequences

Different representations can contribute to one answer without pretending that they contain the same information or that their referred things are identical. Readers can move between their useful operations and find where a changed assumption affects the combination.

The connections cost interpretation and upkeep. More automatic propagation can reduce repetitive work but makes the update policy consequential. Some disagreements locate a genuine subject decision; notation design cannot settle that decision by synchronizing appearances.

### NOT.6:10 - Architectural Rationale

Complementarity concerns operations, not media count. Two textual forms can support different work, while a text and picture can duplicate the same limited information. The useful whole consists of contributions and the relations through which they can be combined.

Reference and derivation are distinct relations. A variable may represent a quantity of a component; a table value may result from evaluating that variable's formula. Retaining those relations allows a change to reach the right contribution without making the representations or their subjects identical.

Update intention is also content. A finished state can conceal whether an unchanged value is fixed by the user or merely carried forward. Making that intention recoverable permits local propagation and reveals conflicting demands before one silently replaces another.

### NOT.6:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Ainsworth, [DeFT: A conceptual framework for considering learning with multiple representations](https://www.inf.ufpr.br/alexd/REPRESENTACOES_EXTERNAS/Ainsworth_2006.pdf), 2006, §§3–4 and 7.5 | Use the historical distinction between a representation's task contribution and the effort of relating it to another. It informs :4.1 and :4.4. Linked displays do not by themselves show that a reader has learned the correspondence. |
| Rexigel, Kuhn, Becker and Malone, [The More the Better?](https://link.springer.com/article/10.1007/s10648-024-09958-y), 2024, cognitive-load analysis, discussion and limitations | The synthesis reports benefits in studied STEM settings but also heterogeneous effects, publication-bias concerns and a small underlying basis for some load comparisons. Use this to bound the learning claim in :4.4, not to impose a number of representations or promise a gain for every reader. |
| Matsuda, Nguyen and Wang, [Lenses for Partially-Specified States](https://link.springer.com/chapter/10.1007/978-3-032-22723-2_2), ESOP 2026, §§1–2 | Adapt their distinction between whole displayed state and update intention into :4.5 and :5.1. Partial constraints can expose a compatible propagation or conflict. Their compositional guarantees depend on the formal construction; the ordinary method here does not confer them on arbitrary manual correspondences. |

**Choice of coordination.** A single sufficient representation avoids the effort of maintaining correspondence. Several become useful when their operations contribute to the actual answer. Manual labels and a direct rule can then be enough. Repeated edits across shared information can justify a maintained transformation; the 2026 partial-state approach addresses an important failure of replacing whole views indiscriminately. It also requires a model of update intentions and admissible merging. Choose that added construction when propagation and conflicts matter, rather than adopting it merely because several displays exist.

The synthesis retains cognitive and computational contributions at their own scopes: a formally consistent update need not be easy to understand, and an easy comparison need not preserve a user's edit. Reopen the chosen arrangement when a useful operation remains inaccessible, navigation or upkeep outweighs its gain, or a changed edit exposes an inadequate correspondence.

### NOT.6:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1–.3 | Supply the operations, expression rules and interpretations on which the joined reading relies. |
| NOT.5 | Constructs translations, answer recovery and retained information where one representation omits needed distinctions. |
| MATH.18 | Establishes the formal preservation and compatibility needed when mathematical accounts are compared. |
| C.29 | Relates a mathematical model to its subject and governs the return of a modeled result. |
| ME.9 | Relates the claims needed for different uses of a working method; NOT.6 supplies their notational correspondences. |
| C.2.8 | Characterizes recoverable structure for the intended reader, preparation, access and effort. |
| NOT.7/.8 | Develop difficult reading-operation repair and temporal or embodied coordination. |

### NOT.6:End

## NOT.7 - Redesign a Notation around the Reader's Difficult Operations

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.7:1 - Problem frame

**Use this when** a notation can express the required content, yet reading or changing that content is unnecessarily difficult. A reader repeatedly loses a dependency, has to reconstruct a grouping, or must change the same assumption in several places. Another symbol or a shorter inscription may leave the difficult operation unchanged.

Begin with one such operation on an actual expression. Find what the reader has to locate, infer, remember or alter. Change the notation or its editing arrangement at that point, then compare the operation and another operation that the change could burden.

The result is a repaired notation with a reason to prefer it for the intended work, or a decision to retain the existing form. A useful diagnosis may instead identify missing subject knowledge, an unavailable operation or inaccessible content that a notation change cannot supply.

The reader needs the subject criterion for a correct result and enough knowledge of the existing notation to inspect its interpretation. NOT.1 supplies a missing use requirement; NOT.2–.3 supply formation and interpretation. A sketch and a worked comparison can be enough for a local repair.

Keep a sufficient familiar form when no consequential reading or change difficulty is present. If the underlying account is wrong, repair that account. Use EXD.1–.3 when the needed work is to construct an explanation; use the instructional method appropriate to the missing capability when the reader cannot yet perform the required subject operation.

### NOT.7:2 - Problem

How can a notation be made easier to use without removing the distinctions, dependencies or operations on which its usefulness depends?

Shortness, visual neatness and familiarity can each help particular work, but none identifies the difficult operation. A repeated value may be easy to read and costly to change. A shared name may make the change local while sending readers elsewhere to recover the value. A new arrangement must be judged through those operations.

The repair also has to separate expression from assistance. An author can explain the missing connection during a trial, making an unchanged notation appear successful. A trained reader can reconstruct a relation that the expression never supplies. Those contributions may be useful, but they change what the notation itself has achieved.

### NOT.7:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Ease of one operation and another | Making a dependency explicit can consume space; sharing a definition can add a lookup. |
| Familiarity and better construction | A new convention can reduce later work while imposing an initial learning cost. |
| Local repair and general reuse | One expression can be fixed cheaply; a rule used across many expressions needs broader comparison. |
| Simplification and preserved meaning | Removing detail helps only when the needed distinctions remain obtainable. |
| Observation and intervention | Assistance or practice can improve a trial independently of the changed notation. |

### NOT.7:4 - Solution

**Locate the difficult operation → explain its burden → construct a targeted alternative → preserve the required meaning → compare use and displaced effort → retain or revise.**

#### NOT.7:4.1 - Locate the operation and its failure

Select a concrete question and the expression on which the reader must work. Ask for the answer or modification, not only an opinion of the notation. Recover the route taken: where the reader searches, which reference is followed, what has to be held in memory and where the result goes wrong or the work becomes costly.

Use an available response or observed difficulty when one exists. Otherwise, walk through the operation and treat the diagnosis as a design estimate. An actual trial is useful when plausible reader responses would change the repair decision; it is not a prerequisite for every obvious correction.

State the relevant preparation, permitted help, display or access conditions and effort limit. A reader who knows the local grouping convention faces a different question from one learning it. A page that hides half a diagram can create a different difficulty from the diagram's structure.

Keep the intended result in view. If the reader has correctly recovered the notation but lacks the subject inference, obtain that inference or capability. If an interpretation is ambiguous, NOT.2 or NOT.3 repairs the rule before comparisons of ease can settle its use.

#### NOT.7:4.2 - Explain which work the current form imposes

Describe the burden through operations: repeated searching, uncertain grouping, reconstruction of an unstated dependency, simultaneous retention of distant values, or many edits for one intended change. Choose the description that explains the observed case.

Locate the source of the burden. The expression, the construction rule, the editing environment and the reader's preparation can make different contributions. An editor that cannot show two needed passages together may be changed without introducing a new notation. A missing dependency needs expression even when the display is large enough.

Use Cognitive Dimensions as a vocabulary for such trade-offs when it helps the design conversation. Its activity-relative descriptions suggest where to look; a list of dimension names does not establish that a reader can perform the operation.

Retain successful uses of the current form. They identify what the repair must preserve and may reveal why an apparently awkward convention exists.

#### NOT.7:4.3 - Construct a change at the source of the burden

Choose a change that alters the difficult operation. The following constructions supply starting points; their costs determine whether to keep them.

| Difficult operation | Possible construction | Other work to inspect |
| --- | --- | --- |
| Matching an item to its corresponding value or next step | Align the participating entries, give them shared references, or place the relation beside them. | Reading across another ordering, crowding and maintaining repeated entries. |
| Recovering the extent or operands of an expression | Make grouping or operand roles visible and keep their formation rule available. | Added space and the reader's ability to construct the grouped expression. |
| Changing one assumption repeated in many places | Introduce a named common definition and make its uses recoverable. | Following references and expressing a legitimate local exception. |
| Reconstructing a long nested operation | Expose useful intermediate results with their inputs and continuation. | Additional names and the possibility of losing the connection between stages. |
| Exploring a construction before every choice is known | Permit a clearly marked partial expression and show which operations it already supports. | Distinguishing an unresolved choice from a completed value. |

A local label, grouping mark or rearrangement can suffice. Use NOT.4 when an expression transformation needs a preservation argument, NOT.5 when the alternative omits distinctions, and NOT.6 when both forms will remain in joint use.

Keep the alternative small enough to inspect. If construction reveals that the original question was wrong or incomplete, revise the requirement through NOT.1. Do not keep optimizing the old operation merely to preserve the initial design brief.

#### NOT.7:4.4 - Preserve what the work needs from the expression

Identify the meaning and operations that must survive the change. Work through one consequential contrast: reversed dependency, local exception, changed grouping or unresolved input, as appropriate to this notation. The new form must make the required difference recoverable.

If the repair adds a claim that was absent before, treat it as a content addition. If it supplies a new procedure or teaches a missing convention, include that contribution in the comparison. A useful combined repair is allowed; attribute its effect to the actual combination.

Preserve the path from a compressed form to the detail needed for its use. A shared definition needs a resolvable reference; an intermediate name needs its construction; an omitted branch needs a rule showing when it can be omitted. Compression is useful when it reduces the relevant work, not merely the displayed size.

#### NOT.7:4.5 - Compare the same operation and the burden it moves

Perform the selected operation with the old and new forms under comparable conditions. Compare correct and missing results first, then the effort relevant to the use: searches, unresolved references, edits, elapsed time or another suitably defined measure. C.2.8 distinguishes structure recovered from the effort of recovering it.

Also perform an operation plausibly made harder by the repair. A shared parameter may make a global change easy and a local exception harder. An outgoing-dependency index may improve downstream search while an incoming-dependency list remains better for finding prerequisites. Keep that trade-off visible in the choice.

For a human or agent trial, retain the first response before explanation or correction. If the same reader sees both forms, practice can contribute to the second result. For a local decision, that limitation may be acceptable. A general superiority or learning claim requires a comparison that supports that stronger conclusion; EXD.6 and, for instructional use, HCD.19 supply the corresponding evaluation methods.

A family of alternatives can justify matched examples and computed measures. Use those measures to locate an expression or change that needs inspection. Shorter code, fewer symbols or a smaller edit count does not alone establish better understanding. Do not build a comparison gallery when one bounded contrast can settle the local repair.

#### NOT.7:4.6 - Choose the repair at the needed scale

Retain the change when its demonstrated or reasonably expected contribution is worth the new burden for the actual work. Keep the incumbent when it remains sufficient. If different forms serve different important operations, preserve the useful alternatives and their correspondence rather than force one universal winner.

Use the existing contribution and choice methods in C.11.CRC/C.11 when cost or competing improvements affect the decision. When the work needs maintained comparison and selection rules, use A.19.CPM for comparison and A.19.SelectorMechanism for selection. This method supplies notation changes and their use differences, not a separate scoring system.

Leave the needed convention, reference or operation available with the retained expression. A repair that works only while its author explains it has not supplied a self-sufficient notation for that reading condition.

Stop when the present use is adequately supported and further comparison would not change the choice. Reopen when the operation, preparation, access, scale of use or meaning changes, or an actual response contradicts the claimed benefit.

### NOT.7:5 - Archetypal Grounding

#### NOT.7:5.1 - Turn prerequisite lookup into downstream search

A small dependency account gives the immediate inputs of four tasks:

| Task | Immediate inputs |
| --- | --- |
| A | None |
| B | A |
| C | A |
| D | B and C |

This form answers “what does D need?” directly: B and C. The new working question is “after A changes, which tasks may need reconsideration?” The reader must repeatedly search the input column for dependents, then do so again for each newly found task.

Construct the reverse index: `A → {B, C}`, `B → {D}`, `C → {D}`, `D → {}`. Here an arrow goes from a supplied input to a task using it. Starting at A, follow arrows and retain newly reached tasks until none remains. The resulting set is {B, C, D}; D is retained once even though two paths reach it.

The repair changes the lookup arrangement and supplies a reading procedure. It does not add a new dependency. It makes the required direction directly available, but finding the immediate inputs of D is now less direct. Keep the original table as a complementary view if that operation remains frequent, using NOT.6 to maintain the connection.

Now remove C from D's input list. Remove the arrow from C to D as well. A still reaches D through B. A reader who merely drops D from the downstream set has confused removal of one path with removal of every path. The changed case tests the reading operation, not the prettiness of the index.

This construction demonstrates the dependencies and operations preserved. It supplies no measured claim that every reader finds the index faster; the local display and reading conditions can change that comparison.

#### NOT.7:5.2 - Share a parameter while retaining a local exception

Three quoted amounts use the same tariff, 3 units per item, for quantities 2, 5 and 7. The expressions are `3*2`, `3*5` and `3*7`. Their intended common assumption is known, but the written expressions repeat it independently.

To make a common tariff change local, introduce `p = 3` and write `p*2`, `p*5` and `p*7`. A change to p = 4 then gives 8, 20 and 28. There is one tariff definition to change, while a reader of an individual expression now follows p to that definition. The definition must remain accessible.

The next request keeps the second quote at the old tariff and changes the others. A global change of p alone cannot express that request. Write the second expression as `3*5`, with its fixed-tariff meaning stated, while the others remain `p*2` and `p*7`. The amounts are now 8, 15 and 28. If later exceptions acquire their own shared rule, give that rule its own name.

For work dominated by common tariff changes, the shared parameter can be useful. For independently negotiated quotes, the assumption of a common tariff may be wrong. The notation repair therefore needs the subject's sharing relation; identical printed numbers alone do not establish it.

### NOT.7:6 - Bias-Annotation

A designer's fluency can hide the work a new reader performs. Recover an actual route or state the preparation assumed by a design estimate. When the author supplies missing information during use, include it among the enabling contributions.

Optimizing a visible measure can also remove the method's value. A shorter inscription can hide the dependency needed for a change. Compare the operation and its result before treating size or edit count as an improvement.

### NOT.7:7 - Conformance Checklist

When the repair needs checking, ask the questions that can change its adoption.

- Is a concrete difficult operation identified, with its intended result?
- Does the repair change the cause of that difficulty?
- Can the needed distinctions and references still be recovered?
- Are content, notation, preparation, help and access changes distinguished where they affect attribution?
- Has an operation plausibly burdened by the repair been considered?
- Does the comparison support the claimed scope of benefit?
- Can the work stop with a sufficient local repair or a justified choice to retain the current form?

### NOT.7:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Replacing symbols while leaving the same search or reconstruction work | Change the arrangement or operation responsible for the difficulty. |
| Hiding a repeated value behind a name whose definition cannot be found | Provide the reference and include its lookup cost in the comparison. |
| Treating equal printed values as a common parameter | Recover the subject's sharing relation; :5.2 exposes the local-exception consequence. |
| Claiming a notation succeeds after its author supplied the missing explanation | Retain what the initial expression supplied and what the assistance added. |
| Declaring a universal winner from symbol count or one favorable task | Compare the relevant operations and their trade-offs. |
| Requiring an empirical study before a bounded useful correction | Use sufficient current evidence or a reversible, qualified design estimate. |

### NOT.7:9 - Consequences

A repair can make a needed relation or operation available with less reconstruction, or make an intended change less error-prone. It also makes the reason for keeping a familiar convention explicit when a proposed alternative would burden important work.

New conventions require learning and migration. Complementary views add maintenance. A local improvement remains local until broader use supports a wider claim. Some failures return to subject knowledge or explanation rather than notation.

### NOT.7:10 - Architectural Rationale

The unit of redesign is the reader's operation on meaningful content. Appearance matters through what it makes available, distinguishable or changeable in that operation. This lets the method apply to formulae, diagrams, programs and other notations without prescribing one visual style.

Meaning preservation and ease of use answer different questions. A transformation can preserve the result while making its construction harder to inspect. Conversely, a helpful explanation may add missing content. Keeping those contributions separate permits a fair comparison without forbidding useful combined repairs.

An activity-relative choice also avoids inventing a universal quality scale. The existing characterization and contribution methods compare the relevant gains and burdens. Notational engineering supplies the constructions and the operation-level differences those methods need.

### NOT.7:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Blackwell and Green, [Notational Systems: The Cognitive Dimensions of Notations Framework](https://www.cl.cam.ac.uk/~afb21/publications/BlackwellGreen-CDsChapter.pdf), 2003, §§2 and 4 | Historical foundation for activity-relative trade-offs among notation, editing environment and medium. Use it to diagnose burdens in :4.2–.3, not as a universal score or evidence of a particular reader effect. |
| Kruchten, McNutt and McGuffin, [Metrics-Based Evaluation and Comparison of Visualization Notations](https://ieeevis.b-cdn.net/vis_2023/pdfs/v-full-1328.pdf), 2023, §§1–4 | Adopt matched examples and computed measures as aids to close comparison in :4.5 when several reusable alternatives warrant that work. The measures do not replace interpretation or establish usability by themselves. |
| Brazauskas and colleagues, [PUX Explorer and PUX Matrix study](https://ppig.org/files/2024-PPIG-35th-brazauskas.pdf), 2024, §§5–7 | Adapt problem/solution co-development into :4.3 and retain existing benefits during repair. Six specialist music-notation researchers supplied bounded, mixed feedback; the study does not establish universal effectiveness or empirical quality coefficients. |

**Choice of repair method.** A local walkthrough can settle an explicit lost dependency or burdensome edit. Activity-based diagnosis helps discover the trade-off when the trouble is less obvious. Matched galleries become useful for recurring comparisons across a family, but add construction and interpretation cost. Reader trials answer a remaining recoverability question when their outcomes can alter the choice. None of these methods replaces subject correctness.

The synthesis connects those notation-design methods with C.2.8's qualified structural comparison and the existing marginal-choice methods. Keep design estimates, measured responses and formal preservation arguments at their own scopes. Reopen when observed use defeats the proposed mechanism, a newly important operation changes the trade-off, or stronger evidence changes a claimed benefit.

### NOT.7:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1 | Defines or revises the operation and distinction the notation must support. |
| NOT.2–.3 | Repair formation, binding and interpretation when those prevent a determinate operation. |
| NOT.4–.6 | Supply use-preserving transformation, loss-aware translation and continuing coordination of forms. |
| C.2.8 | Compares the selected structure recoverable by the intended reader under stated conditions. |
| C.11.CRC / C.11 | Relate the proposed gain to its burden and the current improvement choice. |
| A.19.CPM / A.19.SelectorMechanism | Supply comparison and selection of alternatives when those maintained rules are needed. |
| EXD.6 / HCD.19 | Evaluate explanation repairs and instructional material for their respective receiving uses. |
| NOT.8 | Constructs temporal and embodied reading operations whose difficulties may motivate this repair. |

### NOT.7:End

## NOT.8 - Construct Temporal or Embodied Notation with a Reading Procedure

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### NOT.8:1 - Problem frame

**Use this when** a notation carries important distinctions through timing, sound, gesture or bodily position, and recognizing its individual signs does not yet let a reader follow or perform the intended sequence. The reader may lose the cycle, confuse a gesture's reference frame, or recognize a command without knowing how to enact it.

Start with the distinction the work needs: an onset within a beat, two simultaneous events, a body-relative direction or another stated relation. Choose how the carrier expresses it, provide its reference and segmentation, then construct the procedure by which a reader recovers and uses it.

The result is a temporal or embodied expression with a usable interpretation and reading procedure. It states what a prepared reader can obtain, what remains for performance or control, and how a consequential change affects the reading.

This is notational engineering. Rhythm, movement, laboratory signals and interaction traces supply different subjects; their subject methods determine which timing or motion relations matter. The notation designer needs that subject meaning and the relevant capabilities of the intended reader. NOT.1–.3 supply the general design, formation and interpretation methods.

Reuse a familiar adequate convention when it already supports the operation. An ordinary static expression may suffice when no temporal or embodied distinction matters. Knowing the notation is not by itself a claim that a person can perform a movement or a machine can realize it; obtain the missing performance or control method when the work requires enactment.

### NOT.8:2 - Problem

How can a reader recover and manipulate relations that unfold in time or action, including those no longer immediately present when the next sign arrives?

A sequence of recognized sounds can lack a known starting point or grouping. A pause can mean a specified rest, an unobserved interval or a wait for an event. A gesture to the right can refer to the performer's body, a room or a drawing. These interpretations permit different continuations.

The carrier's behavior also matters. Playing a recording faster changes its audible duration, but need not change the duration represented by a coded timestamp. A score can specify a desired action while leaving its bodily or algorithmic realization to the performer. The reading procedure must make the relevant convention available.

### NOT.8:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Transient expression and continued use | A reader may need an earlier sign after it has ceased to be perceptible. |
| Relative and absolute reference | A beat, body direction and clock time support different comparisons. |
| Recognizable sign and interpretable relation | A clear tone or gesture can still have uncertain scope, participant or timing. |
| Compact direction and adequate preparation | A short score can rely on skills or an interpreter that must actually be available. |
| Replay and live enactment | Pausing or slowing can aid analysis while changing the physical process or coordination. |

### NOT.8:4 - Solution

**Select the temporal or embodied distinction → establish references → segment and encode → construct the reading or enactment route → vary a consequential condition → retain a usable expression.**

#### NOT.8:4.1 - Select what is expressed and what the reader should do

Identify the subject relation and the needed operation. The work may be to recognize an order, reproduce a rhythm, compare two movements, locate a missing event or construct instructions for another performer. Choose the distinctions that operation consumes.

Say whether the expression describes an observed occurrence, proposes a future performance or presents a construction for analysis. The same cue sequence can serve these different uses, but a plan does not establish that its events happened.

Separate the sign's physical properties from the represented properties. A sustained tone might represent duration by its length, or merely identify an event kind. A hand position might be an action being performed, a sign for another movement, or a reference against which a different action is timed. Use the convention that supports the selected work.

State the reader's available perception and operations. Distinguishing two timbres, maintaining a pulse, recognizing a body part and following a formal event code are different prerequisites. A computational reader needs a suitable input representation and interpretation, not an assumed human sensory skill.

#### NOT.8:4.2 - Establish the references that locate an occurrence

Give the origin, unit, frame or recurring reference needed to interpret the signs. For cyclic time, identify the cycle and position within it when occurrences across cycles must be distinguished. For movement, identify the participant, body part, spatial frame and starting condition that affect the interpretation.

Choose whether timing is absolute, relative to another event or relative to a maintained pulse. If a tempo change should retain relative positions, preserve that relation when changing elapsed durations. If a deadline is in seconds, a mere proportional rescaling may change the required result.

Give different participants a way to align their references when joint action or comparison needs it. A shared visible pulse, a named event or a common clock can supply alignment under its own conditions. Separately timestamped records do not establish event order unless their clock relation supports that inference.

Keep the reference identifiable during use. A repeated syllable can denote the same position in successive beats while being a different occurrence each time. A rightward direction can change in room coordinates when its body frame turns.

#### NOT.8:4.3 - Segment and encode the needed relations

Choose recognizable units and a rule for joining them: separate events, intervals, phases, gestures or other parts appropriate to the subject. Mark a beginning, boundary or return to a cycle where losing it would change the reading.

Assign signs and their temporal or spatial arrangement to the selected distinctions. Make order, overlap and duration recoverable when the work needs them. Writing two signs successively does not express simultaneity unless a grouping or interpretation rule supplies it.

Provide a way to distinguish a specified absence from a missing observation. A rest within a known beat and a recording gap can both be silent, but only the former supplies the intended absence. Use a marker, an accompanying record or another recoverable convention where the difference affects the next operation.

Inspect discriminability under the intended conditions: speed, overlap, background sound, viewing direction or available sensors. A symbol family that is distinct on a page can become confusable when sounded or gestured. Change the encoding or access arrangement if the needed contrast disappears.

Choose detail for the receiving use. A movement score can constrain endpoints while leaving the route open; a different use can require the route, timing or body-part coordination. Keep an omitted choice with the performer or construction method that is to supply it, rather than silently giving the notation credit for it.

#### NOT.8:4.4 - Construct the reader's route through the expression

State how the reader establishes the reference, identifies the current part, combines it with retained information and obtains the next result. Make the necessary repetition, count, comparison, transformation or enactment available. A legend naming sounds or gestures may need this additional procedure.

For a transient carrier, choose how earlier parts remain usable: replay, a persistent companion record, a repeated reference, trained retention or another available means. Use only what the receiving conditions permit. NOT.6 connects a score, sound and event table when several forms remain necessary.

If the task is performance, connect the decoded instruction to the performer's available method. A person may already know how to realize a gesture or syllable. A machine may need a parser, state representation, control algorithm and physical realization. CMP.12 constructs an effective interpreter; B.5.MPC connects the abstract construction to preparation, execution and interpreted observation. Notation alone does not supply those methods.

A demonstration can be part of the supplied interpretation. Identify what it teaches and keep it available if the text relies on it. If another prepared reader can use the expression without that demonstration, the reading condition is different; assess the contribution at the condition actually offered.

#### NOT.8:4.5 - Challenge the relation with a meaningful change

Carry out or inspect a small use and a contrast that can change its result. Shift a cue while retaining its identity, change a body's orientation, remove a timing reference or ask for simultaneity rather than order. Choose a contrast grounded in the intended operation.

Distinguish reading from successful physical performance. A correctly decoded sequence can still be infeasible for a particular body or controller. Locate that missing realization contribution rather than changing the meaning until the observed performance appears correct.

When using replay, decide which property it can preserve. Slowing a recording can aid segmentation. It cannot by itself demonstrate that a performer meets the original speed, that two live processes stay synchronized or that a paused physical system stops evolving.

A worked interpretation supports its stated use. Claims about human fluency, learning or transfer require their own basis; C.2.8 and the applicable capability-development method characterize the relevant recovery or performance. Use the current sufficient result, and seek an additional trial only when its outcome can change the next choice.

#### NOT.8:4.6 - Retain the expression with its operative convention

Keep the reference, segmentation, interpretation and needed reading procedure available with the expression. A short local convention may suffice; reusable performance material may also need a demonstration, an interpreter or an accessible alternative carrier.

State an unresolved performer choice or lost distinction where the next use needs it. A score specifying endpoints can be useful before a motion path is chosen. A recording with an unobserved interval can support the observed segments without settling the missing order.

Stop when the selected operation is supported or the missing contribution is located. Use NOT.7 if the interpretation is determinate but difficult to follow. Reopen the affected convention when the reference frame, timing, medium, required observation or reader capability changes.

### NOT.8:5 - Archetypal Grounding

#### NOT.8:5.1 - Recover a cue's place in a beat

Choose a beat divided into four equal positions. In the Takadimi convention these positions are voiced as ta, ka, di and mi. For this example, a dot in the written grid means no new onset at that position; it does not specify how long an earlier sound continues.

| Position within the beat | 0 | 1/4 | 1/2 | 3/4 |
| --- | --- | --- | --- | --- |
| Position syllable | ta | ka | di | mi |
| First onset pattern | ta | . | di | . |
| Shifted onset pattern | . | ka | . | mi |

Establish a steady beat, divide it into four and keep the beat's start identifiable. The first pattern has onsets at 0 and 1/2. A shift of one quarter-beat, within this one-beat example, yields onsets at 1/4 and 3/4. The new syllables identify the new positions. Repeating the same two spoken syllables without their reference would not express this change of placement.

At a beat duration of one second, the first onsets occur at 0 and 0.5 seconds; the shifted ones at 0.25 and 0.75 seconds. At a beat duration of half a second, the corresponding times halve while the relative positions remain. A requirement for an onset at an absolute 0.5 seconds is therefore a different requirement.

If the sound between two known positions is unrecorded, do not replace that gap by a written dot claiming no onset. Preserve the missing-observation status. If the next operation asks how long notes are held, add the needed duration convention: the onset grid alone does not answer it.

This is a notation construction, not a claim that reading the table teaches fluent rhythmic performance. Maintaining the beat and coordinating speech are available skills or contributions to be learned.

#### NOT.8:5.2 - Read a movement relative to a changing body frame

A tabletop movement score uses two signs. `R` means move one grid unit to the performer's right without turning; `F(2)` means move two units forward without turning. The signs describe successive completed displacements. The starting position is (0, 0), with east as positive x and north as positive y.

A performer initially facing north reads `R; F(2)` as an eastward unit displacement followed by two northward units. The endpoint is (1, 2). The reading procedure first recovers the starting orientation, translates each body-relative direction into the grid frame, updates the position and continues from there.

Now the performer starts facing east. The same score yields one unit south and two units east, ending at (2, -1). Treating R as page-right would give a different route. If the intended task is to preserve the original grid-space path regardless of orientation, choose a grid-relative notation or construct the appropriate body-relative instructions; keeping the marks unchanged does not meet that new task.

The score leaves the speed and path within each displacement unspecified. It can guide a prepared person moving a token. Making a physical robot perform it additionally requires an applicable motion method and an account of its realization. Reading the endpoint establishes neither that method nor a performed movement.

### NOT.8:6 - Bias-Annotation

Expert fluency can conceal the reading procedure. A musician or dancer may supply pulse, segmentation and bodily realization without noticing those contributions. Recover them before expecting a newcomer or computational agent to use the same expression.

A familiar carrier can also invite the wrong relation. Spoken order can be mistaken for event order, silence for a rest and a facing gesture for a room-fixed direction. Use a consequential contrast to determine which reference the notation supplies.

### NOT.8:7 - Conformance Checklist

When the expression needs checking, ask the questions that can change its use.

- Is the represented relation and intended reading or performance operation recoverable?
- Are the needed origin, unit, cycle, participant and frame available?
- Can the reader segment occurrences and distinguish the relevant order, overlap or duration?
- Is a specified absence distinguishable from missing information where it matters?
- Does the reading procedure identify the retained state or replay that it needs?
- Are perception, interpretation and physical performance contributions supplied at their stated scopes?
- Does a meaningful change preserve the intended relation or reveal the required repair?

### NOT.8:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Providing a list of sounds or gestures without their temporal or spatial reference | Establish the beat, origin, participant or frame needed to interpret occurrences. |
| Equating recording silence with a specified rest | Preserve the observation gap and request the missing contribution only if the use needs it. |
| Reading body-right as page-right | Recover the frame and transform directions, as in :5.2. |
| Counting correct sign recognition as successful enactment | Connect the decoded result to a capability or control method that can realize it. |
| Claiming original-speed competence from slowed replay | Limit replay to the property it preserves; inspect performance under the required timing when that claim matters. |
| Giving every score maximal movement detail | Express the constraints the receiving use consumes and retain the performer choices compatible with those constraints. |

### NOT.8:9 - Consequences

Temporal and embodied expression can become a manipulable part of reasoning: readers can locate occurrences, vary a relation, compare performances or hand an interpretable instruction to another agent. A score can retain useful constraints while allowing more than one realization.

The method exposes preparation and access costs that a fluent practitioner might leave tacit. Additional references can burden performance; a persistent companion representation can help analysis while requiring coordination. Some expressions remain useful only with a trained performer or an available interpreter.

### NOT.8:10 - Architectural Rationale

Temporal or embodied expression adds reference and availability problems to ordinary formation and interpretation. What a sign means can depend on phase, orientation or the reader's retained state. These conditions belong in the operative convention rather than an assumed resemblance between mark and action.

Segmentation serves the receiving operation. An action can be described by its intended result, selected intermediate constraints or a detailed movement account. Those descriptions require different contributions from a performer. Keeping that distinction permits transfer between people and machines while exposing what must be reconstructed.

Reading and enactment are connected methods. Their separation makes the connection constructive: decode what the score requires, determine what the performer must supply, obtain that method and interpret the resulting action. This retains the relation between mathematical structure, algorithms and physical realization.

### NOT.8:11 - SoTA-Echoing

| Source and contribution | Adoption and limit |
| --- | --- |
| Nelson, [Solkattu Manual](https://www.weslpress.org/9780819574480/solkattu-manual/), Introduction, pp. 2–3 | The account connects spoken patterns with recurring hand references and distinguishes spoken from played realization. It informs :4.2 and :4.4. The book explicitly resists a simple one-syllable/one-stroke identification; the method keeps the actual convention and training contribution. |
| [Takadimi Basics](https://www.takadimi.net/basics.html) and [Teaching with Takadimi](https://www.takadimi.net/teachingWithTakadimi.html) | The position-based syllable convention supplies :5.1; coordinated pulse and voice illustrate a reading procedure. This is a particular convention, distinct from Nelson's treatment, not a general theory or an empirical guarantee of instruction quality. |
| Salaris, Abe and Laumond, [A Worked-Out Experience in Programming Humanoid Robots via the Kinetography Laban](https://doi.org/10.1007/978-3-319-25739-6_16), 2016, §1 and pp. 346–348 | The worked connection distinguishes a score's action constraints from detailed human or robot motion and exposes the control-space contribution. Adapt that distinction in :4.3–.5. The earlier robotic demonstration supplies a constructive anchor, not a claim that any score automatically yields feasible robot motion. |
| Guerreiro, Amaral and Goulão, [Unleashing the Power of Sound](https://arxiv.org/abs/2304.08654), 2023, §§III and VI.D–E | Adopt the question of audible discrimination and context into :4.3. The UML sound study measures bounded preferences and perceived relevance, with limitations in baseline choice, sample and setting; it does not establish general comprehension, multi-representation integration or universal sound meanings. |

**Choosing a form for the same operation.** In :5.1 the reader must locate and shift two onsets within a beat. Compare a static position grid with a sounded score, for a reader who knows the syllables and can count the four positions. The grid already answers the question and remains available for inspection. Keep it when that is the whole task; adding voiced practice would cost effort without improving this answer. A familiar convention also needs no extra account when its references and reading operations are already available to the reader.

For following the onsets during a performance, both a retained grid and a sounded score still need a way to keep place in the beat. Here we adapt Nelson's recurring reference and Takadimi's positional reading into :4.2 and :4.4: maintain the reference, locate each occurrence and retain or replay the parts needed for the next operation. This repairs the case in which a sign legend identifies syllables but leaves their positions unavailable. It does not require a new symbol vocabulary. A prepared reader may maintain the reference while reading the grid; a sounded or embodied form is preferable only when its coordination benefit warrants the added perception or practice. Those costs are the accepted trade-off, not a demonstrated general learning advantage.

The beat calculation in :5.1 shows the information gained from the reference; it does not compare human performance speeds. The source table supplies the limits of transferring this reasoning to movement and audible interfaces: a recovered instruction still needs its performer method, and preferred sounds need not improve interpretation. Reopen this choice if a simpler available convention supports the same operation and timing with less burden, or if the chosen reference or reading procedure fails under the receiving conditions.

The synthesis uses these different practices to expose recurring design operations; it does not merge their symbol systems. A position syllable, a stroke-associated syllable and a motion sign can carry different relations. Reopen the construction when a relevant contrast is not perceptible, a reader lacks an assumed operation, a new realization cannot supply the omitted work or a receiving use needs a previously unexpressed relation.

### NOT.8:12 - Relations

| Pattern | Contribution to the working method |
| --- | --- |
| NOT.1–.3 | Supply distinction selection, expression formation and operative interpretation. |
| A.6.3.RT.OE | Constructs an expression around the operation it should make possible. |
| NOT.4–.5 | Preserve selected temporal or embodied uses during transformation and expose translation losses. |
| NOT.6 | Coordinates transient expression with a score, event record or other complementary form. |
| NOT.7 | Repairs difficult reading or manipulation after the interpretation is established. |
| CMP.12 | Constructs the effective interpreter or translation when a computational reader is needed. |
| B.5.MPC | Connects abstract relations and computation to preparation, physical execution and interpreted observation. |
| C.2.8 | Characterizes structure recovered under the intended reader's preparation, access and available operations. |

### NOT.8:End
