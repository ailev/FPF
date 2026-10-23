# Control Architecture Design Principles Framework

**Edition:** [CAD, 23 October 2026](#cadreference8---names-and-continuing-references).

Use this framework when a control design must reconcile what can be observed in time, what the controller must remember, how decisions are divided, which commands remain feasible, and what the implementation can execute. It helps construct and compare those arrangements for an engineered dynamical system, including the choice to keep one sufficient controller.

The quantitative methods principally cover sampled linear models with bounded uncertainty and specified feedback-law candidates. The planning-and-feedback branch also states a separate conditional continuous-time error-bound construction. This is a bounded practice within control engineering; identification, unrestricted controller synthesis and physical qualification require their own methods.

# Table of Contents

- [Readme](#control-architecture-design-principles-framework-readme)
- [Control Architecture Design Architectural Reference](#control-architecture-design-architectural-reference)
  - [CAD.Reference:1 - What the language helps obtain](#cadreference1---what-the-language-helps-obtain)
  - [CAD.Reference:2 - The objects and independently useful contributions](#cadreference2---the-objects-and-independently-useful-contributions)
  - [CAD.Reference:3 - Information, tracking and execution must describe the same loop](#cadreference3---information-tracking-and-execution-must-describe-the-same-loop)
    - [CAD.Reference:3.1 - How information changes a command margin](#cadreference31---how-information-changes-a-command-margin)
    - [CAD.Reference:3.2 - A complete joint design and a changed delay](#cadreference32---a-complete-joint-design-and-a-changed-delay)
  - [CAD.Reference:4 - The layered planning-and-feedback branch](#cadreference4---the-layered-planning-and-feedback-branch)
    - [CAD.Reference:4.1 - The recurring whole problem](#cadreference41---the-recurring-whole-problem)
    - [CAD.Reference:4.2 - Why these four contributions belong together](#cadreference42---why-these-four-contributions-belong-together)
    - [CAD.Reference:4.3 - Connect dynamics, decisions and computation by their actual quantities](#cadreference43---connect-dynamics-decisions-and-computation-by-their-actual-quantities)
    - [CAD.Reference:4.4 - Reuse the external foundations without losing the subject transition](#cadreference44---reuse-the-external-foundations-without-losing-the-subject-transition)
    - [CAD.Reference:4.5 - Several legitimate entries and their returns](#cadreference45---several-legitimate-entries-and-their-returns)
      - [CAD.Reference:4.5.1 - Keep a qualified loop and govern its commands](#cadreference451---keep-a-qualified-loop-and-govern-its-commands)
    - [CAD.Reference:4.6 - Worked joint revision](#cadreference46---worked-joint-revision)
    - [CAD.Reference:4.7 - Recognition, assurance and the cost of the arrangement](#cadreference47---recognition-assurance-and-the-cost-of-the-arrangement)
    - [CAD.Reference:4.8 - Source boundaries, bias and future change](#cadreference48---source-boundaries-bias-and-future-change)
  - [CAD.Reference:5 - What is covered and what must be supplied](#cadreference5---what-is-covered-and-what-must-be-supplied)
  - [CAD.Reference:6 - Why one language, with independent uses](#cadreference6---why-one-language-with-independent-uses)
  - [CAD.Reference:7 - Sources, external suppliers and consequential change](#cadreference7---sources-external-suppliers-and-consequential-change)
  - [CAD.Reference:8 - Names and continuing references](#cadreference8---names-and-continuing-references)

## A. Choose the information available to control

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| A.1 | [CAD.5 - Choose Observations and Internal State for Control](#cad5---choose-observations-and-internal-state-for-control) | Stable | Delayed observation; partial sensing; action history; information state; set estimation. “Which sensors and memory let this controller act within its limits?” “Can any action work with these observations?” | Uses A.3.3.PI and C.32.LCA; the main use is self-contained. CAD.2–CAD.4 are conditional receivers of :4.7. |

## B. Design a planning-and-feedback architecture

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| B.1 | [CAD.1 - Derive a Control Decomposition from the Whole Problem](#cad1---derive-a-control-decomposition-from-the-whole-problem) | Stable | Control decomposition; information; horizon; computational burden. “Should these decisions be separated?” | Uses C.39 and MMP.9; CAD.2 develops the selected exchange; CAD.4 compares whole candidates. |
| B.2 | [CAD.2 - Construct the Planning and Feedback Interface](#cad2---construct-the-planning-and-feedback-interface) | Stable | Reference meaning; state reconstruction; sample-and-hold; reset; tracking dynamics. “What does the lower loop actually receive?” | Uses the selected decomposition and MMP.18; CAD.5:4.7 supplies the estimate-based branch. |
| B.3 | [CAD.3 - Construct a Jointly Admissible Command Domain](#cad3---construct-a-jointly-admissible-command-domain) | Stable | Invariant error; input reserve; constraint tightening; continuation. “Which commands can remain feasible?” | Uses CAD.2's connected dynamics; CAD.5:4.7 when state is estimated; returns to CAD.1 or CAD.2 on incompatibility. |
| B.4 | [CAD.4 - Co-design and Realize the Whole Control Architecture](#cad4---co-design-and-realize-the-whole-control-architecture) | Stable | Model order; gains; rates; deadlines; whole-candidate comparison. “Which feasible arrangement should be realized?” | Receives applicable CAD.1–CAD.3 and CAD.5 results; uses MMP.22; supplies the broader SYSE.6 decision. |

# Control Architecture Design Principles Framework Readme

Within FPF Library, **CAD** is the reference code and document identifier for the **Control Architecture Design Principles Framework**. A reference such as `CAD.5:4.5` identifies a pattern section; `CAD.Reference:3.2` identifies the Architectural Reference's joint example. The local pattern numbers are addresses, not an execution order.

**Suite:** [Engineering DPF Suite](https://github.com/ailev/FPF/blob/main/DPFs/Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md#engineeringreference0---engineering-specialization-and-maintenance) — control knowledge and design Methods for constructing, changing and sustaining engineered dynamical systems.

## Enter from the control question

| Your working difficulty | Obtain first | Direct entry |
| --- | --- | --- |
| A useful observation arrives after the action deadline, or different channels reveal different parts | An observation and memory arrangement, its error bound and the actions it permits; or a precise information limitation | [CAD.5](#cad5---choose-observations-and-internal-state-for-control) |
| One calculation cannot use the needed horizon, information and execution time together | Competing decompositions and the couplings each would remove | [CAD.1](#cad1---derive-a-control-decomposition-from-the-whole-problem) |
| Planner and feedback code use a “reference” with different timing or meaning | The actual exchange and its derived error dynamics | [CAD.2](#cad2---construct-the-planning-and-feedback-interface) |
| A stable controller cannot follow the requested command within state or actuator limits | A jointly admissible command/error domain with continuation, or a specific incompatibility | [CAD.3](#cad3---construct-a-jointly-admissible-command-domain) |
| A more accurate model, faster planner or extra sensor competes for limited resources | A comparison of complete feasible arrangements and the conditions of their realization | [CAD.4](#cad4---co-design-and-realize-the-whole-control-architecture) |

An engineer can use CAD.5 without introducing a planner or multiple layers. An engineer with a qualified lower loop can retain it and change command admission. If a current complete observation and a simple controller already meet the task, they remain a serious stopping alternative. Read the [Architectural Reference](#control-architecture-design-architectural-reference) when several results must fit together or a change reopens their conditions.

The intended reader can work with state-space models, feedback laws, bounded sets and elementary optimization. A reader who lacks those means needs instruction or a qualified control-engineering contributor. The examples are mathematical constructions. Before relying on a physical installation, establish its model, uncertainty and execution premises.

# Control Architecture Design Architectural Reference

## CAD.Reference:1 - What the language helps obtain

A controller acts on information that can be partial, old or costly to obtain. Its chosen action must affect the plant before another decision is due, fit the available actuation and leave an acceptable continuation. When planning and feedback are separated, their different models and time scales add another coupling: an attractive nominal command may be impossible for the lower loop to realize.

The useful result is a control architecture whose information, command meanings, error allowances and execution conditions are mutually consistent for the required task. The result may instead be a reasoned rejection: no tested realization fits, a sufficient enclosure is too coarse, or indistinguishable states make the required action impossible. These conclusions call for different next work.

There are two directly useful branches. CAD.5 constructs the information available to a specified controller. CAD.1–CAD.4 develop a planning-and-feedback arrangement when separation has a useful reason. Their quantitative results connect where an estimate, command or timing claim is actually used. The language does not require every design to use both branches.

Its recurring tensions are concrete. A precise delayed sensor leaves recent disturbances unknown. A larger model can reduce modeling error while missing the deadline. A gain that reduces tracking error can consume more input authority. Conservative sets can protect a guarantee while excluding a useful design. All of these must be judged against the same task; a smaller isolated error measure is not automatically a better control result.

FPF C.43 supplies the common Method for connecting observation, choice and action in ongoing control. Apply it when the available assessment, alternatives and execution conditions still need to become one coherent continuation; an adequate architecture can remain unchanged. CAD specializes the engineering construction of the information, command and timing relations. Its state sets, error bounds and feasible commands give quantitative answers under declared models; they do not by themselves settle the legitimacy of a goal, the economics of competing resource uses or a developing subject's next worthwhile problem. Conversely, a common control mantra does not replace these calculations. A changed information delay returns to CAD.5 and its dependent bounds; an unavailable correction can reopen CAD.3 or the architecture choice; a changed goal first changes the task against which those results are used.

FPF C.43:4.5.1 also supplies the common construction of required temporal relations without imposing a periodic schedule. CAD.2 makes that construction executable through event ordering, behavior between updates and reset rules; CAD.5 preserves sample phase, information age and observation gaps, and CAD.4 qualifies the shared implementation schedule. An action can vary its timing while another required contribution continues, provided their joint resource and dynamic conditions still hold. Changing one of these relations reopens the dependent calculation; equal update frequencies alone do not preserve it.

## CAD.Reference:2 - The objects and independently useful contributions

The plant, sensors, actuators and controller computers are systems. A dynamical model is a mathematical description of selected behavior. A feedback law prescribes how to choose an input; an implementation performs that calculation and applies an actual input. A design Method constructs or assesses an arrangement; one run of that Method is design work. The framework describes Methods and their relations. A model or feedback-law revision can change the required computation without requiring a different physical plant; changing a processor can change timing without changing the law.

In CAD.5, a *channel* is a realizable observation alternative with a measurement meaning, uncertainty, sample times, arrival conditions and resource demands. An *information state* retains what is needed to update the compatible possibilities and choose the next action. It can be a history, a sufficient recursive state or a conservative set representation; it is not necessarily another sensor or a physical control layer. The estimate \(\hat x\), the true model state \(x\), estimation error \(\eta=x-\hat x\), nominal state \(z\) and tracking error \(e=x-Pz\) have different meanings.

In CAD.1–CAD.4, *planner*, *tracker* and *layer* identify contributions in a selected control organization. They do not automatically identify processor boundaries, physical parts or system-role assignments. Different functions can share a processor; one function can be distributed. Their order is not a ranking of people.

| Recurring design question | What its Method constructs | Why the result can be needed independently |
| --- | --- | --- |
| Information sufficient for action | CAD.5: channel/timing alternatives, sufficient memory and update, estimation uncertainty and admissible action or impossibility | A single controller may need better observations without a different decomposition. |
| Useful separation of decisions | CAD.1: alternative decompositions, reasons for each split and exposed losses | A timing or horizon problem can change the split while sensing remains adequate. |
| Meaning and behavior of an exchange | CAD.2: reconstruction, command, hold/interpolation/reset rules and error dynamics | A communication or reference representation can change without replacing either controller. |
| Feasible command and continuation | CAD.3: compatible error and command sets, state/input margins and continuation conditions | A larger demand can exceed a previously useful domain while the architecture remains unchanged. |
| Realizable whole choice | CAD.4: feasible configurations, comparison under common demands, execution and revision conditions | A processor, solver or scheduling change can alter the preferred realization. |

These are connected problem families with independent uses. CAD.4 constructs the comparison of whole layered candidates; CAD.5:4.8 compares information arrangements. This Reference explains the quantities shared by those Methods and the conditions under which their results can be combined.

## CAD.Reference:3 - Information, tracking and execution must describe the same loop

### CAD.Reference:3.1 - How information changes a command margin

CAD.5 constructs compatible state histories from the measurements actually available before the action. Past inputs must be the inputs actually applied; a planned input or a measured value treated as current can produce a different information set. A run-wide bound \(V_\eta\) must cover startup and every allowed delivery mode, not only a favorable observation window.

When the interface is

$$
u=K(\hat x-Pz)+Qz+Rv,
$$

CAD.5:4.7 derives the estimate-based version of CAD.2's tracking equation:

$$
e^+=Fe+Hz+Gv+w-BK\eta.
$$

CAD.3 therefore receives the effective forcing \(W\oplus(-BK)V_\eta\). For every admitted nominal state and command, its state and input tests become

$$
\{Pz\}\oplus E\subseteq X,\qquad
\{Qz+Rv\}\oplus KE\oplus(-K)V_\eta\subseteq U.
$$

The separate set sums are sufficient enclosures, not assertions that tracking and estimation errors are independent. A tighter joint representation may recover a useful design that these separate margins reject. A failure of a sufficient enclosure is consequently different from CAD.5's indistinguishability proof that no action can meet the demand.

This is a two-way design connection. A tighter required command domain can require fresher observations. A sensor or estimator change can enlarge \(V_\eta\), shrink the usable command domain and invalidate a nominal performance claim. CAD.4 includes the cost of obtaining and updating that information. If a larger planner delays the estimator or communication, the old age bound is no longer a premise of the same realization. Reuse an unaffected result, but return the changed timing to CAD.5 and the resulting error to CAD.3.

### CAD.Reference:3.2 - A complete joint design and a changed delay

Consider the constructed scalar plant

$$
x_{k+1}=x_k+u_k+w_k,\qquad |w_k|\le .005,
$$

with \(|x|\le .65\), \(|u|\le .06\), initial \(x_0=z_0=0\), and a requested nominal motion satisfying \(|z|\le .5\), \(|z_{k+1}-z_k|\le .04\). The required tracking bound is \(|x-z|\le .11\), including intervals in which the nominal command uses the full rate \(.04\). The lower law is \(u=-.5(\hat x-z)\). Assume its update is completed every fast tick. The planner needs two fast ticks to calculate a new segment and supplies one every four ticks. Each calculation starts at least two ticks before its segment takes effect, and each new segment starts at the preceding segment's terminal nominal state. Hold \(z=0\) until the first segment is available. These timing and joining conditions are premises to establish for an actual realization.

A complete scalar sensor has error radius \(.005\) and gives the controller a sample at most two ticks old. CAD.5 propagates that sample through the actual intervening inputs, giving

$$
|\eta|\le r=.005+2(.005)=.015.
$$

Known \(x_0\) gives a startup radius at most \(.01\) before the first two-tick-old sample is usable. Thus the uniform radius \(.015\) covers startup as well. A current complete observation would need less memory and give a smaller radius; the delayed sensor is considered here because it is an available realization, not because delay is desirable.

CAD.2 models the timed segment by \(d_k=z_{k+1}-z_k\), so

$$
e_{k+1}=.5e_k-d_k+w_k+.5\eta_k.
$$

CAD.3 obtains the invariant radius

$$
E=\frac{.04+.005+.5(.015)}{1-.5}=.105.
$$

The initial error is inside it. The input bound is \(.5(E+r)=.06\); the state bound is \(.5+E=.605\le .65\); the required tracking bound is met. At the end of a nominal motion, holding \(z\) sets \(d=0\), which stays inside the same admitted increment set and preserves the continuation. The conclusion is conditional on the stated sample, plant and timing bounds.

This also explains the decomposition and interface choice. Asking the two-tick planner for a fresh result every tick misses its assumed deadline. Sending a held target that jumps by \(4(.04)=.16\) can fail immediately: from exact initial alignment and zero estimation error, that jump requests input \(.08>.06\). Sending a joined segment at the same four-tick planning rate preserves the requested nominal rate and the bound above. CAD.4 compares this whole realization with a faster planner, another controller or a current sensor, including their actual costs; the input margin alone does not rank them.

Now suppose shared computation increases the maximum observation age to four ticks. CAD.5 gives \(r=.025\); the same construction gives \(E=.115\) and input allowance \(.07\). It no longer establishes the required tracking or input limits. Reducing the allowed increment to \(.03\) gives \(E=.095\) and input allowance \(.06\), but does not satisfy the unchanged request for the full \(.04\) rate. Recovering the old age bound, using a more timely observation, changing the interface or controller, or obtaining a less conservative joint bound are different repairs to compare. This failed sufficient calculation is not a proof that every controller with four-tick-old observations is impossible.

The example crosses the information, exchange, feasibility and implementation questions without inventing a new control law synthesis theorem. It is an application of CAD.5:4.5–4.7, CAD.2's substitution and timing construction, CAD.3's invariance test and CAD.4's whole-candidate comparison. The larger task determines whether a smaller command domain remains useful.

## CAD.Reference:4 - The layered planning-and-feedback branch

This branch applies when separate planning and feedback decisions are worth considering. Its exact-state construction remains useful when the state is actually available. The estimate-based connection is in CAD.5:4.7 and CAD.Reference:3; use it wherever the implemented law acts on an estimate. The following sections develop the reasons, quantities, alternatives and returns within the layered branch.

### CAD.Reference:4.1 - The recurring whole problem

A layered control architecture divides decisions while controlling one connected behavior. The division is useful when it lets different calculations use appropriate information, horizons and execution resources. It becomes harmful when each calculation relies on a behavior that the others do not supply.

The difficult question is therefore not just which operation follows another. It is whether the chosen decomposition, models, command meanings, error bounds, feasible commands and execution arrangement can all be true of the same closed loop. A later result can change an earlier design premise. The four Methods are separately usable because these questions arise independently; their results must still agree wherever one receives another.

**Extended reminder.** A useful control split preserves the whole task by making its lost interactions explicit. The exchanged command and its timing determine the error that the lower behavior must contain; the containment consumes state clearance and actuator authority, so it limits what the upper decision may request. Those limits reshape the useful model, horizon and decomposition, while the resources needed to compute and execute them change timing again. Compare and realize this connected choice under one demand, and return a changed condition to the premise it invalidates.

This reminder names a coupled argument. It does not prescribe four approval stages, prove a bound, or replace the constructions below.

### CAD.Reference:4.2 - Why these four contributions belong together

CAD.1 answers a functional design question: which decisions should become distinct and why? Its result determines which interactions are no longer solved together. A long-horizon optimizer and a fast feedback law are useful only if their separation addresses a real difficulty, such as calculation time or unequal access to information.

CAD.2 answers a modeling and realization question: what behavior does that separation actually produce? It turns a selected command into an exchange with units, time, interpolation, feedback and reset semantics, then derives the joint evolution. This can reveal that a presumed “same reference” is a different signal after implementation. The result constrains the decomposition: an upper model that cannot be related to the lower dynamics under useful conditions is a reason to retain more state, change the command or abandon that split.

CAD.3 answers a feasibility question: which behaviors can be requested without contradicting the conditions of their realization? Error is not merely a quality score. It consumes physical clearance and correction authority. A command envelope that makes the bound large can leave no useful actuation range; a smaller envelope can restore feasibility but prevent the required task. This result therefore constrains both the interface and the original functional choice. It also distinguishes a possible next action from a domain in which operation can continue.

CAD.4 answers a whole engineering choice: which mutually consistent configuration is worth realizing under the actual demand and resources? It compares the outputs of the other Methods, but it also changes their inputs. A different processor, horizon, model order or scheduling arrangement changes what can be computed on time and therefore which error dynamics and command domain are relevant.

The relation is not that every engineer must perform these Methods in this textual order. The relation is that a claim used by another part must be available with the conditions that make it useful. An inherited result can supply it. A changed condition can withdraw it. A missing result can block one architecture while leaving another usable.

### CAD.Reference:4.3 - Connect dynamics, decisions and computation by their actual quantities

The common quantities make the reasoning inspectable. The task sets a demanded progression, cost or reachability condition. A candidate command class S says what the planner may send. The interface yields an error evolution, such as $e^+=Fe+Hz+Gv+w$. S and the mismatch domain bound its forcing. An invariant E bounds the difference between nominal and realized behavior. The inclusions $Pz+E\subseteq X$ and $Qz+Rv+KE\subseteq U$ then restrict S. These are the exact-state formulas. When feedback uses an estimate, CAD.5:4.7 adds estimation error to both the forcing and the input allowance.

These are mutually constraining statements, not independent labels. Enlarging S can enlarge E, which can make the proposed S inadmissible. Reducing E by changing a gain can increase the size of KE and consume more actuator authority. Reducing the planning model can shorten computation while increasing H or the mismatch set. A longer update interval can fit the computation and enlarge the change the tracker must absorb. A bigger model can remove an important residual but leave no time to use the result.

Thus “more accurate”, “faster” and “more robust” are incomplete comparisons until their quantities and costs are named. A more accurate nominal prediction does not imply a smaller implemented error if it arrives late. A smaller tracking error does not imply a better task result if the permitted command range becomes too small. A feasible computation does not imply safe execution if its output is applied at the wrong instant.

The mathematical construction does not eliminate the engineering choice. It makes the choice explicit: accept a smaller envelope, change an interface, spend more computation, use another sensor or actuator, or revise an impossible requirement. SYSE.6 remains the place for that larger system decision.

### CAD.Reference:4.4 - Reuse the external foundations without losing the subject transition

C.39 supplies the reasoning from a needed result back to necessary operations and forward through their joins. Here that reasoning asks whether the result called “a feasible controller” includes a realizable command, its timing and a continued path, rather than stopping at the existence of a feedback gain.

MMP.9 supplies the account of what model reduction removes. CAD.1 and CAD.2 consume that account at a specific control decision: does the missing state create memory or forcing that the planner must retain or the tracker must absorb? Calling the lower loop “fast” does not establish that its omitted dynamics are negligible.

MMP.18 supplies the general construction of compatible exchanges and scales. CAD.2 fills its control-specific content: which signal is held, which state is propagated, what resets, and how a reference change enters the error. A well-typed exchange still needs this behavior.

MMP.22 supplies the transformation from mathematical operations to workable performance. CAD.4 consumes it when choosing what to precompute, what data are available at the deadline, what resource is shared and which result can actually arrive. The computation is part of realizing the selected control behavior; successful algebra alone does not enact it.

C.30.LCA then helps describe the resulting control structure adequately. It can expose an unrepresented latency or lower guarantee. It does not establish the guarantee's truth. Conversely, a valid error calculation does not ensure that a view shows the assumptions needed by the next engineer.

These foundations remain useful outside control engineering. The subject contribution here is their specific connection to control decisions, error dynamics, admissible commands and execution. Neither collection of general references nor a single numerical example supplies that connection by itself.

### CAD.Reference:4.5 - Several legitimate entries and their returns

An engineer replacing a communication interface can start at CAD.2. Preserve the task, qualified model and existing controller law if they remain unchanged. Derive what the new delay or interpolation does to their connection, then return only the affected error and command assumptions to CAD.3. If the new interface cannot support any useful domain, the change reaches CAD.1 or the system architecture decision.

An engineer asked to increase speed can start at CAD.3. Hold the implementation and model fixed while testing the enlarged command class. If correction authority is exhausted, CAD.2 can investigate a continuous segment instead of a larger jump. CAD.4 compares that repair with a changed gain, faster planner or different plant arrangement. The order follows the uncertainty that matters, not a mandatory restart.

An engineer moving the same software onto shared computing hardware starts at CAD.4. A model of independent task execution is no longer the implementation premise. Establish the shared scheduling and communication behavior; if it changes the admitted timing, return that timing to CAD.2. A new hardware name alone does not require every control theorem to be reproved, but an unbounded delay removes the old timing-dependent conclusion.

An engineer with a simple controller already meeting the requirement can stop before any of these expansions. A framework that always recommends more layers has lost its baseline. Conversely, a proven lower law does not justify stopping when the upper layer can issue commands outside its qualified envelope.

#### CAD.Reference:4.5.1 - Keep a qualified loop and govern its commands

When an existing loop already tracks and rejects disturbances adequately, but abrupt or excessive commands violate constraints, command admission can be the remaining problem. [Garone, Di Cairano and Kolmanovsky's survey, §2.1 and §6.1](https://merl.com/publications/docs/TR2016-102.pdf) develops reference and command governors as additions before a stabilized loop. They modify commands using the current closed-loop state and predicted constraint admissibility, rather than merely applying a fixed low-pass filter.

For the basic held-command construction, use a model whose state includes the plant and controller. Obtain a set of state-command pairs from which holding the selected command satisfies the constraints at all claimed future instants. A scalar reference governor selects the largest admitted step along the line from the previous command toward the desired one; a command governor can optimize the command vector. The previous command supplies continuation only under the construction's admissibility and initialization conditions. Scalar search is smaller, while the restricted search direction can sacrifice response.

This is a candidate within the control architecture question, not an opposing field. It can preserve a qualified lower controller and avoid introducing a reduced planning model. Compare its reference distortion, progress and computation with the required task. If filtering makes the requested arrival time unattainable, constraint satisfaction alone has not solved that task. If the lower controller, sensor or timing changes, its governor model and admissible sets must change with it.

Later constructions change different premises: observer-dependent domains in CAD.2–CAD.3, online cost adaptation in CAD.1, and inexact computation or controller switching in CAD.4. Use those developments only with their corresponding models and conditions.

### CAD.Reference:4.6 - Worked joint revision

The running example begins with two different concerns: a planner needs two fast ticks of computation, while an inexpensive feedback law runs every tick. CAD.1 makes the reason for separation explicit. The separation does not yet decide the command: a held target and a timed segment remain alternatives.

CAD.2 derives how their meanings change the error. A held target creates a boundary jump; a joined segment supplies bounded increments at every fast tick. CAD.3 turns that difference into actuator reserve. At the doubled demand, the four-tick held target has a direct violating first input; the joined-segment command has a sufficient input bound of 0.05 under the toy model. Its limited reference interval also has an explicit continuation by holding the reference.

CAD.4 returns the result to the practical choice. The segment design fits the declared computation arrangement but requires a clocked generator, continuity at handover and an admitted initial error. The engineer cannot keep only its attractive input number and omit that realization. If physical actuation is later found to be delayed, the error derivation changes and the bound must be reopened. The reason for separating planning from feedback can remain useful even while that specific realization fails.

During the calculation of an error margin, the immediate mathematical work contributes to constructing a command domain, which contributes to choosing a viable control architecture, which contributes to the engineered system's required behavior. A changed whole requirement alters what counts as a useful local margin. This connection explains why a numerically correct sub-result can still fail to resolve the engineering problem.

### CAD.Reference:4.7 - Recognition, assurance and the cost of the arrangement

A layered diagram recognizes a candidate organization. A plausible trace recognizes a candidate behavior. Mathematical invariance establishes a conditional property; a real model, disturbance envelope and execution arrangement must support its premises before physical reliance. These are different results, and the full use needs whichever the intended claim actually consumes.

The primary trade-off is between cheaper or more specialized local decisions and the burden of maintaining their coupling. More patterns or more formal interface declarations do not settle that trade-off. The arrangement earns its cost when separate decisions remain useful and their conditions can be made compatible. A direct controller or direct existing Method remains preferable when it already serves the task.

A whole-use inspection therefore asks whether the selected split has a useful reason, whether the derived exchange is the one realized, whether its command/error dependence closes, whether continuation and performance are distinguished, and whether implementation conditions fit. These questions use the full constructions of CAD.1–CAD.4; they are not an alternative checklist proof.

### CAD.Reference:4.8 - Source boundaries, bias and future change

The constructions compared in the patterns answer different quantitative questions. The reader should not assemble their conclusions into a theorem that none states. The cost-elimination branch, sampled linear margins, continuous error-based safety transfer, reference governing and a specific two-layer co-design each retain their own models and qualifications. The direct derivations and explicit returns here make a first use possible without claiming complete coverage of control engineering.

The running linear case makes computations transparent but can bias intuition toward easy matching, full-state access and deterministic timing. Its general lesson is to derive and reconnect the consequences of a split. Its numerical margins, feasible domain and fallback remain local to the stated model.

When a source revises a relied-on condition, reopen that condition and its consumers. When a physical model or execution fact changes, reopen the claims that use it even if no source publication changed. A new paper can improve a method; a failed application can expose a missing family of problems. Either can justify revising the framework's scope, while an unchanged adequate supplier remains available.

## CAD.Reference:5 - What is covered and what must be supplied

The first quantitative use needs a usable plant model, initial conditions, uncertainty sets, candidate channels and delivery conditions, a specified feedback law or finite family, required state/input limits, and a control objective. CAD.5 develops information and action constructions for that class. CAD.1–CAD.4 add planning models, command reconstruction, error sets, joint constraints and execution choices when their assumptions fit.

The methods do not promise arbitrary nonlinear or learned-controller synthesis, identification of an unknown plant, security of a communication channel, or certification of a physical installation. Those are real neighboring tasks: an unsupported disturbance envelope or an unbounded communication delay can defeat a mathematically correct conclusion here. Obtain the missing model or guarantee, restrict the intended use, or retain the negative result. The separate continuous-time branch in CAD.3:4.5 needs its stated derivative, Lipschitz and forward-containment premises; sampled constraints do not establish intersample safety.

A proposed architecture, a mathematically qualified model and a physically qualified implementation support different claims. The practitioner should be able to answer which observation times and executed inputs were used, which error bound holds over the allowed run, which one action works for all compatible states, what preserves continuation, and how computation realizes those conditions. The full patterns supply these tests; the questions here do not replace their derivations.

The examples favor transparent linear calculations and explicitly bounded uncertainties. Exact sets can be expensive and outer sets conservative. A stochastic expected-cost task may justify a different estimator and schedule; CAD.5:11 compares that alternative. An unqualified biological analogy or a component score cannot replace the chosen model and control criterion.

## CAD.Reference:6 - Why one language, with independent uses

The information and layered branches share a control-engineering question: which implemented arrangement can produce the required behavior under the available information, actuation, time and resources? Their shared state, error and timing meanings make a result from one branch usable by the other. Keeping those connections explicit reduces the amount a reader must privately derive when a sensor, command or processor changes.

The language is narrower than systems engineering. SYSE.5 constructs the engineered system's functional organization and bearer alternatives; SYSE.6 decides the broader architecture. A control result is one input to those decisions. Putting all specialist derivations inside their general explanations would not remove the need to learn control modeling or maintain its source conditions. Conversely, a control engineer changing one sensor need not reopen the whole system design when its interfaces and required effects remain satisfied.

Two separate framework accounts could expose the same Methods, but would still need to maintain the common estimation/tracking/input/timing connection. One account with direct entries keeps that connection available while allowing independent change. Quantization can change CAD.5 and the bounds that consume its result without changing a valid decomposition. A new command governor can change CAD.3 or CAD.4 without changing an adequate information state. A common file does not require a common calculation or a fresh pass through every Method.

The gain is an obtainable connected explanation and localized adaptation, not a measured reduction in learning time or engineering cost. The costs remain substantial: modeling, set computation, numerical qualification, physical evidence and the effort to understand the selected branch. A direct existing controller, a suitable external design or a competent provider can be the cheaper sufficient route. Where the complete needed method is already known, use its result rather than recreate it for this framework.

## CAD.Reference:7 - Sources, external suppliers and consequential change

The full source comparisons belong with the affected Methods. CAD.5:11 distinguishes the historical diversity-enabled sweet-spot model, internal prediction and applied-action feedback, bounded-set estimation and stochastic sensor scheduling. DeSS compares complementary components under a task and resource model; IFP concerns a controller's reuse of internal information. Neither establishes the other. The selected bounded-set construction is used because the stated task asks for hard sampled constraints, not because it is universally superior.

CAD.1–CAD.4:11 compare decomposition, reduced-model interfaces, invariant margins, governors, safety filters, inexact computation and switching under their different conditions. A reference governor can preserve a qualified loop; a safety filter changes the applied control law and therefore the error calculation; separate stable switching modes do not establish a common invariant domain. A more recent result matters when it changes the usable construction or comparison, not merely because it has a later date.

| External supplying publication | Contribution used here | Receiving use and return |
| --- | --- | --- |
| [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md), C.32.LCA | General construction of complete control-architecture alternatives and their joint conditions | CAD supplies the specialized numerical constructions. A changed general architecture requirement reopens the affected framing, not an unchanged algebraic identity. |
| FPF Core, C.30.LCA | Adequacy of a control-structure view | A view must expose the information, authority, timing and lower guarantees needed for its use. Its adequacy does not prove a control bound. |
| FPF Core, A.3.3.PI | Retaining information needed by future prediction and update | CAD.5 constructs a particular sufficient internal state and explains what a reduction must preserve. |
| FPF Core, C.39 and C.32 | Construction of useful connected ways and whole architecture alternatives | CAD.1 and CAD.4 use those general operations with control-specific models, alternatives and constraints. |
| [Systems Engineering DPF](https://github.com/ailev/FPF/blob/main/DPFs/Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md), SYSE.5 and SYSE.6 | Functional organization, bearer alternatives and the system architecture decision | CAD results can supply that wider work. Control feasibility neither chooses every system bearer nor settles the whole project. |
| [Mathematical Modeling DPF](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md), MMP.9, MMP.18 and MMP.22 | Model reduction, compatible coupled models, and transformation of mathematical operations into workable performance | CAD.1–CAD.4 provide the control-specific receiving operations. A changed model exchange or computational realization reopens the error or deadline premise that uses it. |

These remain external contributions. Core does not require this DPF for its own applications. Select an obtainable edition of a supplying publication and the exact relied-on content before applying it; a locator or title alone is not that content. If a relied-on premise changes, revisit its receiving use. If only the carrier or publication date changes, inspect compatibility rather than assuming either breakage or preservation.

For the domain construction, a changed plant, measurement model, uncertainty, command objective, admitted switching, timing or resource arrangement reopens the dependent calculation. A source correction reopens the particular claim imported from it. Unchanged information, interface or model results remain usable under their original conditions.

## CAD.Reference:8 - Names and continuing references

This is the **23 October 2026** edition of **Control Architecture Design Principles Framework (CAD)**, a constituent of the Engineering DPF Suite in FPF Library. Cite the framework and edition together with the full PatternID and section needed for the particular claim or calculation.

*Control architecture design* here means designing the organization of observations, retained information, control decisions, exchanges and execution for the engineered dynamical behavior stated in CAD.Reference:1–2. It does not mean that every controller needs layers. **CAD** is a local reference code for this named framework in FPF Library, not the general engineering abbreviation for computer-aided design.

Each complete Method has one body below. This Reference explains the framework and its conditional connections.

## CAD.Reference:End

# A. Choose the information available to control

## CAD.5 - Choose Observations and Internal State for Control

> **Type:** Method pattern
> **Status:** Stable

### CAD.5:1 - Problem frame

**Use this when** an engineered controller has to act before a complete, accurate observation is available. A rapid channel may reveal only part of the situation; a more complete channel may describe an earlier state. You need to choose the channels and their timing, determine what the controller must remember or predict, and establish what control those arrangements can support.

For example, an inspection result can arrive after two control updates while a simpler sensor reports one critical quantity immediately. Adding both sensors is not yet a solution: the controller must relate their observations to the same evolving system, account for actions already performed, and retain uncertainty about unobserved disturbances.

This is a specialized method for **sampled linear control with bounded uncertainty**. It constructs a sufficient information arrangement for a specified control task and a given state-feedback law or a finite set of such laws. It also supplies a stronger negative result when indistinguishable situations require incompatible actions. It does not synthesize arbitrary nonlinear controllers, identify an unknown plant, or infer biological mechanisms from a control analogy.

The intended practitioner can use state-space models, bounded sets and feedback laws. Start with the required controlled quantities, admissible state and input sets, operating horizon, a usable plant model, and realizable sensor and execution alternatives. The first useful result is a comparison that connects **available information → one executable action → the required continuation**, with the internal state and update needed to maintain that connection.

Retain a simpler qualified arrangement when it already works. A current complete observation can remove the need to reconstruct a delayed state. An unobserved but sufficiently bounded component can remove the need for a sensor. If the only question is whether a diagram represents an already constructed control structure adequately, use C.30.LCA.

### CAD.5:2 - Problem

An accurate observation of the past is not an accurate observation of the present. Between sampling and acting, the plant has evolved under known commands and unknown disturbances. Combining the latest values from several channels can therefore create a state that never existed. A point estimate can also hide alternatives that demand different actions.

Choosing the smallest estimation error does not by itself solve the control problem. Error in a harmless direction may cost more to remove than error in a direction that exhausts an actuator margin. Conversely, a low average error can coexist with an unacceptable possible trajectory.

The design problem is to obtain enough timely information for the required action and continuation, at an acceptable sensing, communication, memory and computation cost. Neither maximum observation nor minimum memory is the goal by itself.

### CAD.5:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Freshness and completeness | A rapid partial observation may constrain the next action more usefully than a delayed complete one; neither dominates without a plant and a task. |
| Prediction and unobserved disturbance | Known actions allow a past observation to be propagated, but prediction cannot reconstruct disturbances that no available channel distinguishes. |
| Compact internal state and retained dependence | A small representation is cheaper; discarding correlation, sample time or applied-input history can invalidate its next update. |
| Estimation and control | A sensor can improve estimation while leaving the limiting action unchanged. A smaller error bound can enlarge the set of feasible commands. |
| Rigorous bounds and execution cost | Exact feasible sets can be expensive. An outer approximation is usable if its additional uncertainty still permits control before the deadline. |
| A chosen realization and architectural necessity | Removing one internal path tests that realization. It does not establish that every controller without that path fails. |

### CAD.5:4 - Solution

Construct the possible current states from the information actually available at the action time. Determine whether **one action**, chosen with that information, works for all those states and admits the required continuation. Use failures of that construction to change the observation, its timing, the internal representation or the control demand. Compare complete alternatives under the same demand.

#### CAD.5:4.1 - Fix the action time and the control-relevant distinctions

Use the sampled plant model

$$
x_{k+1}=A x_k+B u^a_k+w_k,\qquad w_k\in W,\qquad x_0\in X_0.
$$

Here \(u^a_k\) is the input actually applied during the update, not merely the requested command. Specify state or output constraints, input limits and the duration for which they must hold. The discrete guarantee covers sample instants; physical constraints between samples require a qualified intersample model and bound. A tracking problem can use deviation coordinates about a known reference; changes of that reference must remain in the model.

For the direct construction below, \(A,B,W,X_0\) are known, \(W\) and \(X_0\) are bounded, and the executed input is available to the estimator. Known actuator queues can first be included in the plant state. Unknown actuation error must be bounded and included in the model; an unbounded discrepancy between requested and applied input defeats the stated guarantee.

State what is available **before** selecting \(u_k\). A packet that arrives after that selection cannot support that action. Include sampling phase, transmission, computation and actuation timing in this account. Specify a maximum age of usable observations and a maximum gap between required samples: a delivery-delay bound alone does not guarantee that a sensor samples often enough.

Ask which possible situations the controller must distinguish. If two situations consistent with all available information require disjoint admissible action sets, no deterministic causal controller using only that information can meet the requirement for both. Conversely, do not demand that every state coordinate be accurately observed if their remaining differences do not prevent an acceptable action and continuation.

Begin with the least elaborate plausible arrangement. Include a qualified current sensor, a fixed observer already meeting the task, or no observation of a harmless stable component. These are substantive alternatives, not merely baselines to be defeated.

#### CAD.5:4.2 - Form realizable observation and timing alternatives

For each offered channel \(j\), specify its observed quantity \(C_jx\), error model, sampling rule, delivery rule and resource demand. For a nonsaturating bounded-error channel, a packet contains

$$
(j,\tau,y),\qquad y=C_jx_\tau+v,\qquad v\in V_j,
$$

where \(\tau\) is the sample time and \(k-\tau\) is its age when used. The channel's constraint on the sampled state is the set

$$
M(j,\tau,y)=\{x_\tau:y-C_jx_\tau\in V_j\}.
$$

A quantized symbol instead denotes its whole quantizer cell, including the noise bound. A saturated extreme cell may be unbounded; do not replace it with a small symmetric error interval. For adaptive thresholds, retain or communicate the thresholds used for that particular sample.

Construct a finite set of feasible channel-and-schedule alternatives. Include the resource coupling that can change their timing: two sensors sharing a bus, for example, need not retain their isolated delivery bounds. State which loss and delay combinations are allowed. A fixed periodic schedule or an explicitly bounded family of allowed modes supplies timing conditions for the error calculation. The number of cases and the cost of set propagation still have to fit the design and execution effort. Arbitrary online sensing policies require a separate policy construction.

A rapid narrow channel, a slow complete channel and their combination are useful candidates when the problem suggests them. They are not compulsory categories. Future-disturbance preview is different from a delayed observation of the current plant; give it its own prediction model rather than treating its timestamp as negative measurement delay.

Do not assume a universal law exchanging accuracy for speed. Obtain that relation from the proposed device, encoding, bandwidth, energy or other physical constraint. If a fast complete channel fits the same total budget, it may remove the reason for a heterogeneous arrangement.

#### CAD.5:4.3 - Construct an internal state that can be updated

Let \(D\) be the largest allowed measurement age. A general sufficient representation retains the compatible joint set of recent states

$$
\xi_k=(x_k,x_{k-1},\ldots,x_{k-D}),\qquad \xi_k\in\Xi_k,
$$

together with the applied-input history, sample identities and the schedule or arrival mode needed for subsequent updates. At startup retain only states at nonnegative times and use \(X_0\); do not invent a prehistory. The set \(\Xi_k\) represents states compatible with the initial condition, model, applied inputs and all observations already incorporated.

Predict the joint set by the map

$$
T(\xi_k,u^a_k,w_k)
 =(A x_k+B u^a_k+w_k,\;x_k,\ldots,x_{k-D+1}).
$$

For a packet arriving at the next action time, intersect this predicted set with the measurement constraint on its **historical component** \(x_\tau\). With several packets, intersect all their valid constraints. The projection onto the first component gives the possible current states \(X_k=\pi_0\Xi_k\).

This is a constructive sufficient internal state, not a claim of minimum order. It preserves the correlation between a past observation and the present through intervening dynamics and actions. Separate marginal intervals need not preserve that correlation; using them as a Cartesian outer approximation is safe only when the ensuing larger uncertainty is carried into control.

A practical realization can use a replay buffer, an observer with equivalent sufficient memory, or a recursive outer set such as an interval, polytope or zonotope. In each case, the represented set must contain every state compatible with the stated model and data. Approximation may enlarge that set; it may not discard a possible state merely to obtain a feasible control.

#### CAD.5:4.4 - Preserve the information needed by the next update

At each action time, use the following causal order:

1. Propagate the previous representation using the input actually executed and the allowed disturbance.
2. Incorporate each newly available packet at its sample time, then obtain the current-state projection.
3. Choose the estimate or set-based action from that projection, apply it by the qualified deadline, and retain the input information needed by the next update.

A state older than \(D\) can be projected out once no allowed future packet refers to it. This is different from throwing away the dependence between retained states. Duplicate packets do not supply additional independent information. In a bounded-set construction, independent noise need not be assumed: common error sources must be represented jointly or enclosed conservatively. With an uncertain timestamp, use the union of the admissible timestamp hypotheses, not their intersection.

If the compatible set becomes empty, the current model, bounds, packet, timestamp or executed-input record is inconsistent. Do not silently reset to a convenient point. Use a separately qualified fallback, obtain a new trusted initialization, or declare the demanded continuation unsupported. Packet loss or delay outside the allowed family likewise invalidates the relevant bound until a qualified recovery applies.

Reduce the internal representation when its update and control use remain sufficient. One exact reduction is available when \(s=T_rx\) has closed dynamics \(T_rA=A_rT_r\), the needed observations factor as \(C_j=C_{rj}T_r\), and the control law and constrained quantities depend only on \(s\). Then use \(s^+=A_rs+T_rB u^a+T_rw\) and the corresponding observation sets. If an omitted component influences a required future quantity, its influence must instead be retained or bounded.

Thus two histories may be merged only when the merged representation still supports every required future update and action under the allowed future observations and disturbances. Equal current estimates are not enough. A.3.3.PI develops this general sufficiency test; here the joint-state construction provides a direct control-specific realization.

#### CAD.5:4.5 - Obtain a usable error bound

Choose a representative \(\hat x_k\) and compute an enclosure \(V_{\eta,k}\) such that

$$
x_k=\hat x_k+\eta_k,\qquad \eta_k\in V_{\eta,k}.
$$

The enclosure can be obtained directly from \(X_k-\hat x_k\). To qualify a continuing controller, obtain a bound valid over the whole allowed run, including startup, admissible delays, sample gaps and loss modes. A bound from one favorable packet sequence is insufficient.

For scalar propagation from a measurement of age \(d\), with coefficient \(a\), measurement-error radius \(\epsilon\), disturbance radius \(q\) and known intervening inputs, a sufficient radius is

$$
r(d)=|a|^d\epsilon+q\sum_{i=0}^{d-1}|a|^i.
$$

The propagated center includes every executed input. The second term is uncertainty about unobserved disturbances; a more accurate old sample does not remove it.

For a multidimensional plant, a finite-window construction gives a sufficient bound without requiring every sensor to observe every coordinate. Take available samples with times \(\tau_i\in[k-L,k]\), subtract their known input responses, and stack them:

$$
r_i=y_i-C_i\sum_{s=k-L}^{\tau_i-1}A^{\tau_i-1-s}B u^a_s,\qquad
r=O x_{k-L}+n,\qquad O_i=C_i A^{\tau_i-(k-L)}.
$$

The stacked noise has components

$$
n_i=C_i\sum_{s=k-L}^{\tau_i-1}A^{\tau_i-1-s}w_s+v_i.
$$

Obtain \(N\) by applying these linear maps to the allowed joint disturbance and measurement-error set; separate component bounds give a conservative enclosure if the joint set is unavailable. Retain shared disturbances when practical. If \(O\) has full column rank, choose a left inverse \(J\), \(JO=I\), and form

$$
\hat x_k=A^LJr+\sum_{s=k-L}^{k-1}A^{k-1-s}B u^a_s.
$$

A sufficient error enclosure is

$$
V_\eta=\left(\bigoplus_{s=k-L}^{k-1}A^{k-1-s}W\right)
       \oplus(-A^LJ)N.
$$

The Minkowski sum \(\oplus\) adds all allowed elements of its operands. This enclosure may be conservative because the same disturbances occur in both terms; it does not assume their independence. Enumerate the admissible window and schedule modes, include the initial transient from \(X_0\), and enclose their errors. Poor conditioning of \(O\) can make a full-rank window useless for the required control margin.

Full-state observability is sufficient for this particular construction, not necessary for the task. A stable hidden component may have a small enough reachable set; a reduced state from :4.4 may suffice. If the window has no left inverse, return to the compatible-set construction and the required actions rather than declaring every such design impossible.

#### CAD.5:4.6 - Establish control under that information

First test whether the information permits a common action. In the following calculation, the selected \(u\) is executed as represented by the plant model; any bounded execution discrepancy must already be included in its disturbance or augmented state. For a required next-state set \(R_{\mathrm{next}}\), the robust admissible inputs are

$$
\mathcal U(X_k)=
\{u\in U:A X_k\oplus\{Bu\}\oplus W\subseteq R_{\mathrm{next}}\}.
$$

The quantifiers are “choose one \(u\), then allow every \(x\in X_k\) and \(w\in W\),” not “for every possible state, choose a different action.” For a halfspace \(h^\top x\le b\) of \(R_{\mathrm{next}}\), the test is

$$
\sup_{x\in X_k}h^\top Ax+h^\top Bu+\sup_{w\in W}h^\top w\le b.
$$

This provides a direct calculation for polytopes and support-function representations. When the test fails on an outer approximation, refine the approximation or change the design before claiming impossibility. A negative result for one chosen controller is weaker still.

One feasible step does not establish a continuing guarantee. A sufficient construction for a specified feedback \(u=K\hat x+g\), with constant \(g\) in the selected operating mode, uses \(F=A+BK\):

$$
x_{k+1}=F x_k+B g+w_k-BK\eta_k.
$$

Find a set \(R\), containing the allowed initial states and contained in the required state set, for which

$$
F R\oplus\{Bg\}\oplus W\oplus(-BK)V_\eta\subseteq R,
\qquad
K(R\oplus(-V_\eta))\oplus\{g\}\subseteq U.
$$

Together with a valid uniform error bound, these conditions prove state and input admissibility by induction. For a stable \(F\), one constructive candidate is the reachable sum of the forcing set \(D_f=\{Bg\}\oplus W\oplus(-BK)V_\eta\):

$$
R_\infty=\bigoplus_{i=0}^{\infty}F^i D_f.
$$

Use a finite outer approximation with a bounded tail, and enlarge it for the specified initial set if necessary; verify the inclusions after enlargement. For example, if an induced norm satisfies \(\|F\|\le q_F<1\) and \(D_f\) lies in a ball of radius \(d_f\), the ball of radius \(d_f/(1-q_F)\), enlarged to contain the initial ball, is invariant. A Euclidean norm larger than one does not prove that no other norm or set works.

These are sufficient conditions, not a universal synthesis algorithm. A stable hidden mode may be handled without measurement; an unstable or tightly constrained uncertain direction may exhaust the input or state margin. Failure can mean excessive approximation, a poor given feedback, an infeasible information arrangement, or an infeasible demand. Distinguish them.

A decisive impossibility witness consists of two admissible histories producing the same available packets and internal information but requiring disjoint actions, or an unavoidable uncertainty width larger than the permitted state interval. Such a witness rules out all causal controllers under those observation conditions, not merely the proposed feedback. Section :5 supplies both a positive construction and such a negative result.

#### CAD.5:4.7 - Connect the information result to a layered control construction

The method can be used without a layered architecture. When CAD.2 supplies a nominal state \(z\), command \(v\), projection \(P\) and control interface, replace its exact-state feedback by the implemented estimate:

$$
u=K(\hat x-Pz)+Qz+Rv,\qquad e=x-Pz,\qquad \eta=x-\hat x.
$$

For \(x^+=Ax+Bu+w\) and \(z^+=A_pz+B_pv\), the derived error dynamics are

$$
e^+=F e+H z+G v+w-BK\eta,
$$

where \(F=A+BK\), \(H=AP+BQ-PA_p\), and \(G=BR-PB_p\). The additional forcing \(-BK\eta\) is the effect of acting on the estimate.

Use the effective disturbance set \(W\oplus(-BK)V_\eta\) in CAD.3's invariant-error construction. For every allowed nominal state and command, state admissibility requires \(\{Pz\}\oplus E\subseteq X\), while the implemented input requires

$$
\{Qz+Rv\}\oplus K E\oplus(-K)V_\eta\subseteq U.
$$

These sums are conservative enclosures, not assertions that tracking and estimation errors are independent. A joint set can retain their correlation when the separate bounds are too costly.

CAD.4 then compares whole arrangements using the estimator's memory, communication, worst-case completion time, admissible packet timing and resulting error set. A new sensor changes \(V_\eta\), which can change the tracking-error set \(E\), the allowed nominal motion and the value of the whole architecture. A larger planner can also increase sensing or estimation latency through a shared resource, requiring the same calculation in reverse.

The added result is the construction of observation availability, internal information state and estimation uncertainty. CAD.1–4 continue to own decomposition, operational interfaces, tracking bounds and whole architectural comparison; this method does not replace them.

#### CAD.5:4.8 - Compare whole alternatives and return to the failed dependence

For each serious channel-and-schedule alternative, obtain the information update, its cost and delay, the error bound and the control conclusion. Keep the demanded behavior, initialization and resource accounting the same. Compare the alternatives that meet the demand; distinguish a proof of impossibility from failure of a sufficient bound.

Choose a sufficient arrangement with an explained cost and margin. A comparison can establish the best member of a stated finite family only when the objective is comparable and every potentially better member is evaluated decisively. Otherwise return the best qualified member found and the unresolved alternatives. A stochastic design can instead minimize an explicitly selected expected cost, but its covariance or a finite successful simulation is not a deterministic bound for this method's hard constraints.

Return according to what failed:

| Observed failure | Useful design return |
| --- | --- |
| Two compatible histories need different actions before any distinguishing packet arrives | Change what is observed, the sampling or delivery time, the actuator or the required behavior. Extra computation on the same information cannot distinguish them. |
| A feasible set is too large only after coarse approximation | Retain a useful correlation or use a tighter representation; include its execution cost. |
| Estimation uncertainty fits, but the given feedback violates an input limit | Change or requalify the feedback and its continuation, or change the physical limit or demand. Do not label this a sensor impossibility. |
| A longer observation gap or shared-resource delay breaks the bound | Restore a qualified timing arrangement or recalculate the information and control sets for the changed timing. |
| A stable unobserved component fits the task without intervention | Remove an unnecessary channel and its associated internal history. |
| A mode switch changes the permitted error or invariant set | Prove that the actual state and information representation enter the new qualified set, or retain a common valid bound. Nominal mode labels do not establish this. |

#### CAD.5:4.9 - Make the result executable and reusable

Return the selected and rejected complete arrangements with the controlled task, plant and uncertainty conditions, channel meanings and timing, initialization, internal state and update, control law, and the admissibility calculation. Make the unresolved distinction explicit if no candidate has a sufficient guarantee.

For implementation, connect sample timestamps and identities, actually executed inputs and the estimator's update to real producers and consumers. Qualify computation and transport deadlines under the proposed shared load. Select an already qualified behavior for missing data, inconsistent data and late completion; “hold the last command” is not automatically safe.

What changes in practice is the choice of the information the controller obtains and retains. The engineer can explain why a channel matters to an action, what must be remembered while waiting for another channel, and which changed condition invalidates the resulting control. A diagram, estimator score or list of sensors alone cannot supply that explanation.

### CAD.5:5 - Archetypal Grounding

#### CAD.5:5.1 - A rapid partial observation and a delayed complete observation

Consider two normalized deviation coordinates:

$$
x_{k+1}=
\begin{bmatrix}1.2&0\\0&0.8\end{bmatrix}x_k+u_k+w_k,\qquad
|w_{1,k}|\le0.04,\quad |w_{2,k}|\le0.02.
$$

The initial state is known to be zero. At every sample the requirement is \(|x_1|\le0.08\), \(|x_2|\le0.06\), with \(|u_1|\le0.12\), \(|u_2|\le0.08\). Inputs are executed without delay and their executed values are available. All specified packets and computations finish before the relevant input selection. These are assumptions of a mathematical design case, not measurements of a physical installation.

The offered sensor packages are:

| Package | Observation available before \(u_k\) | Error bound | Sensor-resource cost |
| --- | --- | --- | --- |
| F | Current \(x_{1,k}\) only | \(0.01\) | 1 |
| S | Both coordinates at \(k-2\), at every tick after startup | \(0.005\) per coordinate | 1 |
| H | Both current coordinates | \(0.005\) per coordinate | 3 |

The sensor budget is 2. Estimator execution and transport capacity are assumed separately qualified for F+S; the sensor cost is not a claim about total implementation cost. Compare F, S and F+S under this budget, and retain H as the simpler alternative if the budget changes.

With F+S, use F for the first coordinate. Propagate S's second coordinate using the executed inputs:

$$
\hat x_{2,k}=0.8^2y_{2,k-2}+0.8u_{2,k-2}+u_{2,k-1}.
$$

The required internal state includes the two applicable input values and the delayed packet's sample time. The uncertainty bound is

$$
r_1=0.01,\qquad
r_2=0.8^2(0.005)+(1+0.8)(0.02)=0.0392.
$$

Before the first delayed packet arrives, propagate the known initial state and inputs; the second-coordinate uncertainty is at most \(0.02\) after one update and \(0.036\) after two. The same bound \(0.0392\) therefore covers startup. Incorporating S's first-coordinate information as an additional intersection is permissible but unnecessary for the following guarantee.

Choose \(u_i=-a_i\hat x_i\), with \(a_1=1.2,a_2=0.8\). Then \(x_i^+=a_i\eta_i+w_i\), so

$$
|x_1^+|\le1.2(0.01)+0.04=0.052<0.08,
\qquad
|x_2^+|\le0.8(0.0392)+0.02=0.05136<0.06.
$$

Whenever the required state bounds hold,

$$
|u_1|\le1.2(0.08+0.01)=0.108<0.12,
\qquad
|u_2|\le0.8(0.06+0.0392)=0.07936<0.08.
$$

The initial state is admissible, and these inequalities establish the state and input requirements for every subsequent tick and every disturbance and measurement error within the stated bounds. This is a continuing conditional guarantee, not an inference from a plotted trajectory.

One particular run makes the internal information visible. Let measurement errors be zero and take \(w_1=0.04,w_2=0.02\) at every update. At \(k=1\), \(x_2=0.02\), but no S packet has arrived and its prediction is zero. At \(k=2\), \(x_2=0.036\), while S reports \(x_{2,0}=0\). At \(k=3\), S reports \(x_{2,1}=0.02\); the propagated center is \(0.0128\), not the current \(x_{2,3}=0.0488\). The difference \(0.036\) is due to the two unobserved disturbances. The controller applies \(u_{2,3}=-0.01024\). On the next tick its prediction includes this executed input. Reusing the old observation without that input would no longer implement the qualified update.

#### CAD.5:5.2 - Why the individual channels do not suffice

With F alone, the second coordinate is never observed and does not influence the observed first coordinate. Consider two runs with opposite second-coordinate disturbances and otherwise identical information. The controller chooses the same second-coordinate commands in both. After five updates, half their separation is

$$
0.02(1+0.8+0.8^2+0.8^3+0.8^4)=0.067232>0.06.
$$

No common center can place both states inside the required interval. This excludes every causal controller using F alone under the stated assumptions, not just \(u=-A\hat x\).

With S alone, the latest two first-coordinate disturbances are unobserved when the next command is chosen. Even with perfect older observations, the next first-coordinate interval has unavoidable half-width

$$
0.04(1+1.2+1.2^2)=0.1456>0.08.
$$

The same indistinguishability argument rules out the required all-time bound. Improving the old measurement's accuracy cannot recover these disturbances before their consequences matter.

F+S is therefore sufficient where either offered channel alone is insufficient, under the same sensor budget and timing assumptions. This establishes a task-dependent benefit of combining channels. It does not establish that all heterogeneous sensing is superior or that the offered catalog is globally optimal.

#### CAD.5:5.3 - Increase the delay, then change the design or the demand

Suppose bus contention changes S's age from two ticks to four, while F and the requirements remain unchanged. The reconstructed second-coordinate radius becomes

$$
r_2(4)=0.8^4(0.005)+0.02(1+0.8+0.8^2+0.8^3)=0.061088.
$$

The same controller's next-state bound is \(0.8r_2(4)+0.02=0.0688704\), which exceeds \(0.06\). More decisively, four unobserved disturbances plus the next one yield the half-width \(0.067232\) from :5.2 even if S's old measurement is exact. F still reveals nothing about the second coordinate. Thus a different filter or gain using the same available information cannot restore this hard bound.

The engineer must change a consequential condition. Restore the qualified two-tick transport arrangement, obtain a timely observation of the second coordinate, or revise the task or physical dynamics. If the sensor budget becomes 3, H alone supports the same feedback with next-state bounds \(0.046\) and \(0.024\); its input bounds are \(0.102\) and \(0.052\). H needs no delayed-observation reconstruction. It is now a simpler sufficient choice.

A different task can also justify less information. If the allowed second-coordinate deviation becomes \(0.12\), retain F and set \(u_2=0\). The unobserved stable second coordinate has the invariant bound

$$
|x_2|\le\frac{0.02}{1-0.8}=0.1<0.12.
$$

S, its delayed packet processing and its input-history reconstruction are then unnecessary. This is sufficient for the changed task; it is not a cheaper solution to the original \(0.06\) requirement.

#### CAD.5:5.4 - What an internal-path ablation does and does not establish

For the scalar noiseless plant \(x_{k+1}=a x_k+u_k\), with a one-tick delayed observation \(y_k=x_{k-1}\), the predictor

$$
\hat x_k=a y_k+u_{k-1},\qquad u_k=-a\hat x_k
$$

uses the executed-input history. Removing that input term while retaining the remaining gains gives \(u_k=-a^2x_{k-1}\). At \(a=1.2\), the resulting characteristic polynomial is \(\lambda^2-1.2\lambda+1.44\); its roots have modulus \(1.2\), so this ablation is unstable.

It does not prove that every controller lacking that input-history path is unstable. Retuning the memoryless delayed-output law to \(u_k=-0.6x_{k-1}\) gives roots of \(\lambda^2-1.2\lambda+0.6\), both with modulus \(\sqrt{0.6}<1\). The latter establishes stabilization of this noiseless model, not the original predictor's performance or a bounded-disturbance constraint guarantee.

Use the first comparison to explain why a particular realization depends on its internal path. Use an impossibility argument such as :5.2–:5.3 when claiming that the available information cannot meet a requirement under any controller in the stated class.

#### CAD.5:5.5 - Recover two coupled coordinates from observations at different times

The general construction in :4.5 is not a coordinate-by-coordinate delay correction. Consider

$$
A=\begin{bmatrix}6/5&1/5\\1/10&4/5\end{bmatrix},\qquad B=I,
$$

with disturbance radii \((.04,.02)\) and measurement-error radius \(.005\). At time \(k=2\), use a first-coordinate observation sampled at time 0 and a second-coordinate observation sampled at time 1. Both samples and the actually applied \(u_0,u_1\) are available before this estimate is used. After subtracting the known input response,

$$
r=\begin{bmatrix}y_{1,0}\\y_{2,1}-[0\ \ 1]u_0\end{bmatrix},
\quad
O=\begin{bmatrix}1&0\\1/10&4/5\end{bmatrix},
\quad
J=O^{-1}=\begin{bmatrix}1&0\\-1/8&5/4\end{bmatrix}.
$$

Thus \(\hat x_2=A^2Jr+A u_0+u_1\). The second measurement contains \(w_{02}\), the second coordinate of the first disturbance, so it is related to the uncertainty in the subsequent propagation. Writing \(w_0=(w_{01},w_{02})\), \(w_1=(w_{11},w_{12})\), and the two measurement errors as \(v_1,v_2\), substitution gives

$$
\eta_1=\frac65w_{01}-\frac3{10}w_{02}+w_{11}
       -\frac{141}{100}v_1-\frac12v_2,
$$

$$
\eta_2=\frac1{10}w_{01}-\frac1{40}w_{02}+w_{12}
       -\frac{47}{400}v_1-\frac{33}{40}v_2.
$$

The exact coordinate radii for the stated box of original uncertainties are \((.10355,.0292125)\). Using the separate Minkowski enclosure in :4.5 gives the larger radii \((.11155,.0612125)\): the same \(w_{02}\) was allowed to vary separately in two occurrences. Both enclosures are valid; retaining the shared variable can save a margin that a conservative test would spend.

This calculation supplies a finite-window error set, not a controller or an all-time guarantee for this new plant. The next use is :4.6 with the required actions and continuation, or :4.7 when a planning-and-feedback interface is already selected. Repeated use also needs the other allowed sample windows and startup to be covered.

### CAD.5:6 - Bias-Annotation

The finite model and channel catalog can omit a better physical realization. Sensor-resource prices are contextual, and error or delay bounds need engineering grounds. An exact mathematical result cannot establish those grounds.

The bounded-set construction favors robust guarantees and can be conservative. A stochastic expected-cost problem may favor a different sensor schedule or estimator. Neither answer should be presented as the optimum for the other's criterion.

A compelling biological or organizational analogy can suggest a useful design question without supplying the engineered plant, uncertainty set or execution guarantee. Internal information reuse also admits different mathematical and physical realizations; a chosen block diagram is not evidence of a unique anatomy.

### CAD.5:7 - Conformance Checklist

- The controlled task, action time, initialization and allowed uncertainty are explicit, including the meaning of an actually executed input.
- Each observation constrains the state at its sample time; admissible sample gaps, delivery modes and resource coupling are included.
- The internal representation can be updated without discarding a control-relevant dependence; approximations enclose all compatible states.
- The control conclusion uses one action for the available information, and a continuing guarantee includes a valid error bound and continuation argument.
- Serious simpler alternatives are compared under the same demand; a changed demand is not disguised as a cheaper equivalent solution.
- A changed delay, observation or internal-state reduction returns to the affected calculation.
- An ablation, a failed sufficient bound and an information-based impossibility have different stated scopes.

### CAD.5:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Treating the most recently received values as simultaneous current state | Retain sample times and propagate their constraints through actual intervening inputs and disturbances. |
| Selecting sensors solely by total estimation error | Calculate the actions, constraints and continuation that the remaining uncertainty permits. |
| Assuming a complete delayed observation removes uncertainty | Retain the disturbances accumulated since the sample; test whether any action can tolerate them. |
| Keeping only an estimate and losing the means to update it | Construct sufficient history or an equivalent recursive state; verify the next update after the proposed reduction. |
| Turning a smaller covariance or successful simulation into a hard bound | Use the stated stochastic conclusion or derive a separate bounded-set guarantee. |
| Calling a conservative test failure a physical impossibility | Refine the enclosure or provide indistinguishable histories with incompatible consequences. |
| Removing an internal path, keeping all gains, and concluding the path is universally necessary | Retune the competing architecture under the same requirement, or use an information-based impossibility proof. |
| Adding a second sensor without including shared transport and compute load | Recalculate timing and the resulting error under the joint realization. |

### CAD.5:9 - Consequences

The result connects observation selection to admissible control rather than to an isolated estimator score. It can justify a combination of channels, a retained internal history, a tighter representation, or the removal of unnecessary sensing.

The cost is explicit modeling and calculation. Exact joint sets can grow too expensive, and robust outer sets can reject useful designs conservatively. The result remains conditional on the model, bounds, timing and implementation. It supplies neither a general guarantee for learned perception nor a complete treatment of nonlinear, state-dependent sensing and actuation.

### CAD.5:10 - Rationale

Information matters through distinctions the next action must respect. A measurement can refine an old state while leaving recent disturbances unresolved. Applied-input history makes predictable change available to the controller; it does not create missing information about unpredictable change.

The method therefore joins three constructions: compatible state histories, a sufficient internal update, and a common action with a qualified continuation. The two-channel example works because the rapid channel restricts a direction whose uncertainty grows too quickly, while the delayed complete channel is sufficient for the slower direction. The simpler changed-task case works because an unobserved direction remains bounded without intervention.

This separates two ideas often discussed together. **Diversity-enabled sweet spots (DeSS)** concern a favorable whole arrangement of components with different limitations under a specified task and resource model. **Internal feedback pathways (IFP)** concern reuse of internal action, prediction or state information in a controller's realization. One does not prove the other; the information and control calculations must establish their particular connection.

### CAD.5:11 - SoTA-Echoing

The precise question here is how to choose realizable observations and sufficient internal memory for bounded-error sampled control. The method joins state estimation and robust control constructions through their information, timing and admissibility conditions.

- [Nakahira, Liu, Sejnowski and Doyle, 2021, “Diversity-enabled sweet spots in layered architectures and speed–accuracy trade-offs in sensorimotor control”](https://doi.org/10.1073/pnas.1916367118) supplies a historical model of complementary pathways. Retain its demand for a whole-task and resource comparison; do not universalize its particular speed–accuracy relation or infer IFP from that DeSS model.
- [“Internal Feedback in Biological Control: Architectures of Diversity and Delays,” 2022 version](https://arxiv.org/pdf/2109.11752v3) supplies a related mathematical contrast between fast partial and delayed observations. Its selected-model and ablation comparisons do not establish necessity across all retuned architectures. Sections :4.6 and :5.4 retain that distinction.
- [Li, Sarma, Sejnowski and Doyle, 2023, “Internal feedback in the cortical perception–action loop enables fast and accurate behavior”](https://doi.org/10.1073/pnas.2300445120), especially its estimation and attention constructions, makes the role of internally available actions and predictions explicit. Adapt that mechanism, with its stated model limits. Do not adopt its asserted scalar no-IFP optimum: in the one-tick-delay, unit-white-noise model of pp.3/11 at \(a=1\), the proposed gain \(k_1=-1/4\) yields stationary state variance \(80/27\), while \(k_1=-1/2\) yields \(12/5\); both closed loops are stable. This comparison uses the article's state-only cost, not a control-effort penalty. The guarantees here use the separately stated bounded-disturbance criterion.
- [Casini, Garulli and Vicino, “Adaptive Threshold Selection for Set Membership State Estimation with Quantized Measurements,” author copy linked to the 2025 publication](https://www3.diism.unisi.it/casini/pdf/TAC_2025.pdf), §§3–6, develops feasible-set updates and adaptive quantization ([IEEE Transactions on Automatic Control](https://doi.org/10.1109/TAC.2025.3545704)). Adopt the set interpretation and explicit outer-approximation cost. Its higher-dimensional threshold choice targets output uncertainty, so control constraints and heterogeneous delivery timing still need the construction here. In particular, output uncertainty and its asymptotic boundedness are not the same requirement as the all-time state and input constraints in :4.6.
- [Dutta, Wilde and Smith, 2023 version, “A Unified Approach to Optimally Solving Sensor Scheduling and Sensor Selection Problems in Kalman Filtering”](https://arxiv.org/pdf/2304.02692v2), §§II–IV, is a serious alternative when the selected criterion is weighted expected estimation or LQG cost under finite-horizon resource constraints. Its mixed-integer construction can compare schedules under that stochastic formulation. Do not relabel its covariance result as a hard feasible-state bound; use it when its criterion is the required one.

Choose between these approaches by the required conclusion, permitted uncertainty model and executable cost. A fixed observer or current complete observation can remain preferable. Reopen the construction when the demanded constraint, admissible timing, sensor model, available computation or a relevant stronger result changes the design conclusion; a later publication date alone does not establish dominance.

### CAD.5:12 - Relations

[SYSE.5](https://github.com/ailev/FPF/blob/main/DPFs/Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) develops the engineered system's functional organization and bearer alternatives. This method supplies a specialized construction for its observation, internal information and control-use contributions. Its qualified alternatives and limitations can enter SYSE.6's broader architecture decision; they do not decide that whole architecture.

C.32.LCA supplies the general construction and comparison of a control architecture. This specialized method develops the mathematical information construction for the bounded class stated in :1; it does not revise the general method's scope. C.30.LCA qualifies the corresponding control-structure view rather than deriving the estimator or controller.

A.3.3.PI supplies the general test for retaining information needed by future prediction and update. Sections :4.3–:4.5 construct sufficient internal state and error bounds for the present control problem.

[CAD.1–4](#cad1---derive-a-control-decomposition-from-the-whole-problem) supply the connected quantitative construction of decomposition, interfaces, tracking bounds and whole control alternatives. Section :4.7 provides the explicit composition: estimator error enters their forcing and input constraints, while their execution arrangement constrains this method's observation age and computation time.

### CAD.5:End

# B. Design a planning-and-feedback architecture

## CAD.1 - Derive a Control Decomposition from the Whole Problem

> **Type:** Method pattern
> **Status:** Stable

### CAD.1:1 - Problem frame

**Use this when** a control problem seems to call for different planning and reaction times, but “add a strategic, tactical and operational layer” does not tell you which decisions belong where. You may also have an inherited hierarchy whose purpose is no longer clear.

Start by writing one consequential behavior that the entire closed loop must produce, together with the available observations, actuators and execution limits. Then identify the decision that prevents a direct solution. The first useful result is a candidate split and an account of what its parts must jointly preserve.

If one qualified controller already meets the task and implementation constraints, retain it. Layering needs an identified benefit; it is not a requirement for accuracy or sophistication.

### CAD.1:2 - Problem

A hierarchy can divide a diagram while leaving the original difficulty untouched. A planner assumes commands can be realized, a tracker assumes commands change slowly, and neither assumption follows from the split. Conversely, trying to solve every decision at the fastest rate can make a good control formulation impossible to execute.

The design problem is to change the organization of decisions while retaining enough of their interactions to obtain the required behavior.

### CAD.1:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Long-horizon choice and rapid correction | A larger look-ahead can improve a plan while consuming time needed for reaction. |
| Simplification and lost interaction | An easier subproblem can omit actuator limits, memory or coupling that determines feasibility. |
| Local improvement and whole performance | A better isolated planner can issue commands that make the combined system worse. |
| Functional separation and realization | Different decision rates do not require different processors; shared processors introduce interference. |

### CAD.1:4 - Solution

#### CAD.1:4.1 - Formulate the unsplit question

State the controlled quantities, objective or preference, hard constraints, operating domain, relevant disturbances, measurements and available actions. Distinguish three time quantities: the dynamics and disturbance times, the horizon over which a choice matters, and the time needed to obtain and execute that choice. A fast update is useful only if observations, computation and actuation support it.

Use a centralized mathematical formulation when it helps reveal coupling, even if that formulation is too expensive to run. It can be a finite-horizon objective with dynamics and constraints, a reach-and-avoid problem, or a reference-following requirement. It is the common comparison basis, not a promise that one optimizer must solve everything.

Retain a feasible simple controller as a baseline where available. State what it cannot achieve at acceptable effort: for example obstacle look-ahead, preview-dependent economy or long-horizon allocation. If the baseline's actual limitation is unknown, test that uncertainty before adding layers.

When a qualified existing loop has adequate tracking and disturbance rejection but requested commands violate constraints, compare adding a reference or command governor before redesigning that loop. Use the joint plant-controller model, admissible initial conditions and qualified command-update rule described in [CAD.Reference:4.5.1](#cadreference451---keep-a-qualified-loop-and-govern-its-commands). Check whether the resulting command delay or distortion still meets the task. If it does, retain that candidate; if it does not, identify the unmet requirement that a different interface, planner or controller must address.

#### CAD.1:4.2 - Separate decisions because their information and effects differ

For each consequential decision, ask what it changes, which information it needs, how long its effect persists, how quickly a wrong choice becomes harmful, and what resources its computation consumes. Cluster decisions only when those answers support one useful calculation or law.

A slow planning decision might choose a route, reference segment or allocation. A faster decision might reject local disturbance or track that reference. This does not imply that the faster model is less detailed: a tracking model may retain actuator dynamics omitted by a planning model.

Generate materially different candidates. Compare a single loop, a planning-and-feedback split, or another separation motivated by the problem. Do not add a third layer merely because the source diagram contains three. A communication boundary can matter more than a time-scale boundary, and a faster processor can make a proposed split unnecessary.

#### CAD.1:4.3 - Expose what the split removes

A useful way to derive a candidate is to introduce separate variables for decisions that were coupled in the whole problem. Initially constrain them to agree. For example, let a planner choose a nominal trajectory z while the plant state is x; keep the relation that says what plant behavior z represents. Only then relax that relation to obtain separately solvable subproblems.

For each relaxation, recover its price. Replacing equality by tracking allows an error; removing full dynamics requires a realizability condition; replacing continuous interaction by periodic exchange introduces stale information and intersample evolution. Removing future disturbance information requires a prediction or uncertainty treatment. These are concrete missing relations, not a generic “integration risk”.

Use MMP.9 when reduction is involved: derive the retained evolution and identify terms depending on omitted state, past inputs or unresolved quantities. A term does not disappear because the upper model has fewer states. Decide whether it is retained through memory, bounded as mismatch, supplied by a lower closed loop, or left as an unresolved limitation.

The first candidate is complete enough to continue when every removed interaction has a proposed receiving treatment in CAD.2 or CAD.3. A treatment may fail; naming it does not establish it.

#### CAD.1:4.4 - Make the slow decision account for fast consequences

Do not optimize the slow part as if the faster part were free. Eliminate or approximate the fast response inside the slow objective when the model permits it.

For example, suppose a particular linear design starts at x = 0 and keeps x at zero by choosing a fast action f after observing w, while a slow action s remains fixed for a block. If the fast input matrix is invertible, the required correction is

$$
f=-B_f^{-1}(B_s s+w).
$$

Substitution gives a slow objective containing both the cost of s and the anticipated cost of these corrections. With a block of k forecast values, a possible norm-cost objective is

$$
k\|s\|_s+\sum_{i=1}^{k}\|B_f^{-1}(B_s s+\widehat w_i)\|_f.
$$

This is a derivation under a particular model, not a general recipe for plants with saturation or delay. When fast actions are limited, retain their feasibility condition as well as their cost. When an exact elimination is unavailable, use a qualified response model, a bound or joint optimization; label the remaining approximation and compare the actual combined result.

#### CAD.1:4.5 - Preserve the whole question through the next design move

Pass each candidate's controlled behavior, separation reason and lost interactions to CAD.2. A command's type alone is insufficient: a target position, a timed trajectory and a velocity segment imply different problems for the tracking layer.

Keep candidates comparable under the same task, disturbance class and resource limits. A slower update with a smaller demanded reference change may look better only because the task was weakened. Retain a whole alternative until its decisive incompatibility or disadvantage is understood.

### CAD.1:5 - Archetypal Grounding

A constructed actuator model is $x_{k+1}=x_k+u_k$, with $|x|\leq1$ and $|u|\leq0.06$. An existing fast law follows a reference. A planning calculation takes two fast sampling periods on a dedicated resource, so it cannot produce a new result every fast tick. Planning remains useful because it chooses future reference segments; the fast law supplies inexpensive execution.

One candidate sends a new held value every four ticks. Another sends a timed segment whose intermediate values the fast task can generate. They differ in the interaction removed by planning: the first assumes a jump can be tracked within the input limit; the second assumes a known continuous segment and a reliable clock. CAD.2 derives those consequences. Neither candidate has yet earned a safety claim.

As a non-use case, suppose the only task is stabilization around one fixed equilibrium and the existing fast law meets every limit. A slow planner adds no demonstrated decision benefit; keep the simpler controller.

### CAD.1:6 - Bias-Annotation

Organizational hierarchies and biological analogies make layered pictures persuasive. They do not determine a control decomposition. The linear example favors a tractable model; nonlinear or partially observed plants can require a different split and different assurance.

### CAD.1:7 - Conformance Checklist

- The unsplit behavior, constraints, information and resource conditions are recoverable.
- Each separation has a decision-specific reason and a serious alternative.
- Removed interactions have explicit receiving treatments or remain visible gaps.
- Slow choices include material fast consequences.
- The compared candidates serve the same demand.

### CAD.1:8 - Common Anti-Patterns and How to Avoid Them

“Slow is accurate; fast is inaccurate” merges optimization quality, model fidelity and tracking error. State the quantity and comparison. “Three layers are necessary” replaces construction with a diagram; derive only the separations the problem needs. A planner that ignores actuator feasibility hands its original problem to the tracker; retain that interaction in the next construction.

### CAD.1:9 - Consequences

The result is a smaller set of explainable architecture candidates. Some apparently attractive splits will be rejected before controller tuning. The cost is retaining the original problem long enough to compare whole behavior instead of judging each box independently.

### CAD.1:10 - Architectural Rationale

The method starts from coupled behavior because a decomposition is a change to that coupling. Introducing agreement before relaxing it makes the lost condition recoverable. This gives later error and feasibility work a specific obligation rather than an open-ended request to integrate components.

### CAD.1:11 - SoTA-Echoing

**When should the decisions be separated?** The selected line derives the split from the whole problem and keeps a qualified existing loop, with a governor if needed, and a single constrained controller as serious alternatives in :4.1–4.3. Separation earns its additional interface and assurance work when differences in information, prediction horizon or execution resources prevent those simpler arrangements from meeting the same demand. If a single MPC formulation can retain the relevant coupling and meet the deadline, decomposition still has to offer a gain that outweighs maintaining its interfaces.

The method adopts the problem-decomposition and coupling-relaxation move in [Matni, Ames and Doyle, §2.2](https://arxiv.org/html/2401.15185), while treating its particular layer arrangement as a choice. It adapts [Goel, Chen and Wierman's construction, §§II–IV](https://arxiv.org/html/1704.07785v2) in :4.4 to include fast consequences in the slow decision. That fixed two-rate, prediction-dependent cost result does not select a layer count or cover actuator limits. The corresponding price is explicit here: a split that saves computation still owes an error and feasibility construction.

A contemporary alternative is to keep the stabilized dynamics fixed and combine online optimization of references with a governor. [Nonhoff, Al Torshan and Müller, 2026 preprint, §§II–IV](https://arxiv.org/html/2601.23160v1) construct this combination for disturbed linear systems under strong convexity of the steady-state costs, compact convex constraints and their bounded-disturbance and initialization assumptions. Their performance statement concerns regret against varying optimal steady states; it is not a solution for arbitrary trajectory or mission objectives. Retain that alternative when changing costs, rather than preview-dependent motion, create the upper decision. The governor comparison in [CAD.Reference:4.5.1](#cadreference451---keep-a-qualified-loop-and-govern-its-commands) explains when the existing loop can remain.

Reopen the split when measured computation, required preview, available observations or permitted command distortion changes. A newly feasible single-loop or governor solution can remove the reason for a larger architecture; a missed task requirement can justify developing it.

### CAD.1:12 - Relations

C.39 supplies the general construction of a way to obtain a result; CAD.1 supplies the control-specific decomposition. MMP.9 supplies model reduction. CAD.2 consumes the selected candidate and makes its exchanges operational. CAD.4 compares whole candidates, including the unsplit alternative. SYSE.5 consumes the resulting functional organization when developing the engineered system.

### CAD.1:End

## CAD.2 - Construct the Planning and Feedback Interface

> **Type:** Method pattern
> **Status:** Stable

### CAD.2:1 - Problem frame

**Use this when** a planner and a lower controller have been chosen, but their combined behavior is not determined by their separate models. A reference jump, stale state estimate, model reset or held input may be the event that makes the connection fail.

Start with one command actually received by the lower computation: what quantity it represents, when it applies and how it becomes an actuator action. The first useful result is the connected evolution of plant, planning state and interface error, including the events between updates.

If a qualified interface already supplies this evolution under the current timing and command conditions, reuse it. A diagram or a matching data type is not that result.

### CAD.2:2 - Problem

Models can agree at one exchange instant while diverging between exchanges. A planning state can be initialized from the plant without representing every relevant plant state. A controller can track a smooth signal yet fail when the implemented interface replaces it by steps.

The interface must therefore be designed as behavior over time, not just as a list of variables.

### CAD.2:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Simpler planning state and hidden behavior | Projection removes quantities that can still affect control. |
| Sparse exchange and timely correction | Holding information saves work while increasing mismatch. |
| Reinitialization and continuity | A fresh estimate can improve planning while creating a command jump. |
| Convenient implementation and faithful semantics | Units, frames, clocks and interpolation can change the implemented law. |

### CAD.2:4 - Solution

#### CAD.2:4.1 - Define the exchanged behavior

Use MMP.18 to establish meanings, units, coordinate frames, observation times, validity intervals and the operation performed between messages. A target, an input, an output trajectory and a constraint are different commands. State which one the lower computation receives.

Choose how the upper model represents the lower behavior. For a planning state z and plant state x, a reconstruction $Pz$ can define an error $e=x-Pz$. A measured projection $z=\Pi x$ is a different map. Even if $\Pi P=I$, initializing $z=\Pi x$ leaves $e=(I-P\Pi)x$, which need not vanish.

If the controlled quantity is $y=Cx$ and the planner predicts $y_p=C_pz$, then

$$
y-y_p=Ce+(CP-C_p)z.
$$

Output agreement requires the second term to vanish or be included in the bound. State reconstruction, output matching and physical identity are separate questions.

#### CAD.2:4.2 - Derive the error instead of assuming tracking

For a useful linear branch, express both models at the fast sampling instants:

$$
x^+=Ax+Bu+w,\qquad z^+=A_pz+B_pv.
$$

Here w is an admitted bounded mismatch or disturbance, not a name for all unknown behavior. Select an interface law

$$
u=K(x-Pz)+Qz+Rv.
$$

Substitute $x=Pz+e$ before simplifying. The actual error equation is

$$
e^+=Fe+Hz+Gv+w,
\quad
F=A+BK,\quad H=AP+BQ-PA_p,\quad G=BR-PB_p.
$$

This calculation makes three design choices visible. K changes error correction; P and Q determine whether the nominal state evolution can match; R determines input matching. Solving $H=0$ is useful when possible but is not automatically possible or necessary. If it fails, retain $Hz$ and bound or redesign it. A stable F does not remove forced error from H, G or w.

Use MMP.9 to construct and qualify a reduced model before relying on it here. A fitted upper model with unexamined hidden-state memory is not made adequate by a convenient matrix dimension.

#### CAD.2:4.3 - Add the clock, held values and reset events

Specify the fast interval, slow update interval, which variables evolve between slow updates, and the event order at a shared instant: observation, computation, command acceptance and actuation. Derive the state just before and just after each event.

For example, if z and v are held for N fast steps, first derive the held-z mode by setting $A_p=I, B_p=0$ in the residual equation. With F, H and G for that mode, repeated substitution gives

$$
e_N=F^Ne_0+\sum_{i=0}^{N-1}F^i(Hz+Gv+w_{N-1-i}).
$$

When the next planning state is $z_{\mathrm{new}}$, the same physical x gives

$$
e_{\mathrm{new}}=e_N+P(z-z_{\mathrm{new}}).
$$

A reset is thus an error input, even when the tracker is stable. If the planner instead propagates z every fast step, use that evolution in :4.2; do not also treat z as held.

Model a known delay through the state and commands actually available to the controller. Replacing $x_k$ by $x_{k-d}$ changes the law; augmenting the state with the necessary history is one way to derive its dynamics. If an estimator supplies x, include estimation error and its qualification. A full-state result cannot simply be relabeled output feedback.

A variable delay or missed update needs an explicit admissible timing set and an error model covering it. A bound for one fixed period does not establish a bound for arbitrary switching among periods.

#### CAD.2:4.4 - Return an interface that can be tested and changed

Give CAD.3 the combined evolution, initial-error condition, admissible command class, mismatch class and exact moments at which each required constraint must hold. Retain the meaning and time convention of every exchanged quantity. These are engineering design values; no special record format is required.

A failed error bound has several possible repairs: change the reconstruction, retain an omitted mode, alter feedforward, reduce command jumps, supply an interpolated segment, shorten latency or choose another split. The error equation identifies which change addresses the failure. Do not reflexively raise every update rate.

Test the actual exchange implementation with boundary events: simultaneous update, maximum permitted delay, reset, command reversal and missing command. These tests can falsify the model of the interface; they do not prove its physical assumptions.

### CAD.2:5 - Archetypal Grounding

#### CAD.2:5.1 - A held reference

For the constructed plant $x_{k+1}=x_k+u_k$, choose

$$
u_k=(1-a)(r_k-x_k),\qquad a=\tfrac12.
$$

With a held reference r, $e_{k+1}=ae_k$. Let the reference change by $\Delta r_j$ at the start of each N-step block. The error immediately after that change obeys

$$
e_{j+1,0}=a^Ne_{j,0}-\Delta r_j.
$$

For $|\Delta r_j|\leq\delta$, the interval $|e|\leq E$ is invariant at block starts if

$$
E\geq a^NE+\delta,\quad\text{hence}\quad E=\frac{\delta}{1-a^N}.
$$

It also bounds intermediate fast instants because $|a|\leq1$. The initialization condition is $|e_{0,0}|\leq E$. With $N=4,\delta=0.1$, $E=8/75$. The reference jump, not instability of the fast law, determines this worst-case envelope.

#### CAD.2:5.2 - A continuous reference segment

Now let the fast computation generate r from a timed segment and let $d_k=r_{k+1}-r_k$, with $|d_k|\leq v_{\max}$. The same plant and gain give

$$
e_{k+1}=ae_k-d_k,\qquad
E=\frac{v_{\max}}{1-a}.
$$

The planner can still update every four ticks. What changed is the command trajectory between updates. At $v_{\max}=0.05$, $E=0.1$. Segment endpoints must join continuously; an additional jump would add to d and invalidate the bound.

If a new segment is unavailable, holding the current reference gives $d=0$, which remains within this command class. This is an error-bound argument for that fallback, not evidence that holding position satisfies every mission requirement.

### CAD.2:6 - Bias-Annotation

A common output makes unlike models appear interchangeable. Check the mapping and missing dynamics. The linear branch makes exact substitution easy; nonlinear models need the same semantic work but may require set propagation or different Lyapunov constructions.

### CAD.2:7 - Conformance Checklist

- The command's meaning, applicability time and between-update behavior are explicit.
- Projection, reconstruction and controlled-output comparison are distinguished.
- Combined error dynamics include mismatch and every update or reset mode.
- The stated initial set and timing class match the implementation being considered.
- Estimation or delay is represented wherever the law uses it.

### CAD.2:8 - Common Anti-Patterns and How to Avoid Them

Matching array dimensions does not match quantities; recover their meanings and maps. Resetting the upper model does not reset the plant; derive the new error. Using a continuous reference in analysis and a held target in code changes the architecture; analyze the implemented exchange. Independent stability of two components does not establish stability of their connection.

### CAD.2:9 - Consequences

The interface becomes a design object whose consequences can be calculated and tested. A small change to interpolation or initialization may replace an expensive change to controller bandwidth. The cost is modeling events and time conventions that a block diagram suppresses.

### CAD.2:10 - Architectural Rationale

The reconstructed state provides a mathematical reference for comparing the planning model with plant behavior. Substitution exposes both the desired correspondence and the residual terms. Making update events part of the same evolution allows feasibility to be established for the connected system.

### CAD.2:11 - SoTA-Echoing

**Which relation between planning and realization is sufficient to use?** For the stated linear branch, the selected construction is an explicit state reconstruction and tracking interface, followed by residual and event equations. It adopts the tracking-law form used by [Stamouli, Tsiamis, Morari and Pappas, §3.2, Theorem 1](https://arxiv.org/html/2504.10461): feedback on the reconstructed-state error with nominal and input feedforward terms. The serious matching-model alternative is a discrete-time simulation-function construction; its usable output-distance guarantee still needs a verified invariant sublevel set, not only decrease outside it. Section :4.2 adapts the law by retaining nonzero nominal mismatch H and bounded w; :4.1 also retains the output-matching residual. These substitutions do not inherit the source theorem: CAD.3 derives the bound for the resulting equation.

This choice makes a failed exact match actionable, at the cost of bounding more forcing and possibly shrinking the usable command domain. If the existing closed-loop model already supports a governor, use that whole model as explained in [CAD.Reference:4.5.1](#cadreference451---keep-a-qualified-loop-and-govern-its-commands); adding a reduced planning model and P is unnecessary unless it supplies a useful decision or computational gain. The held-value and continuous-segment cases in :5 are constructed applications of the residual equation, not interchangeable implementations of one reference.

For partial observations, [Castroviejo-Fernandez and colleagues, §§3–6](https://arxiv.org/html/2401.02054v1) provide a developed alternative: state and disturbance estimation with time-dependent error bounds for reference governing. Adopt their requirement to carry observer error into constraint predictions when choosing that branch; its extra observer and set computations replace the full-state premise, not merely the notation x. Section :4.3 therefore returns an estimator-based implementation to the connected-dynamics derivation. Reopen the interface when its measured quantities, reconstruction, hold, interpolation, reset or delay changes; compare bounds and computation under the same actual exchange before choosing between these constructions.

### CAD.2:12 - Relations

CAD.1 supplies the decomposition and lost interactions. MMP.9 supplies a qualified reduction; MMP.18 supplies exchange and scale compatibility. CAD.3 consumes the derived error and timing modes. CAD.4 returns implementation changes that require this derivation to be reopened. C.30.LCA can then test whether a control-structure view exposes the relations that the construction actually uses.

CAD.5:4.7 supplies the estimate-based version of the interface when exact state is unavailable. It derives the additional forcing from estimation error; the observation model and timing must describe the same implemented loop.

### CAD.2:End

## CAD.3 - Construct a Jointly Admissible Command Domain

> **Type:** Method pattern
> **Status:** Stable

### CAD.3:1 - Problem frame

**Use this when** a connected controller must respect state, output or actuator limits while following commands from another computation. The upper plan may be feasible in its own model while leaving too little authority for correction below.

Start with the actual connected dynamics from CAD.2 and one limiting constraint. Derive the deviation that consumes its margin. The first useful result is a command domain with an invariant error bound and an admissible continuation, or a specific failure that returns the design for revision.

A simulation that stayed within bounds is useful evidence about that run. It is not the invariant command domain constructed here.

### CAD.3:2 - Problem

The layers can make mutually inconsistent promises. The tracker guarantees a small error only for modest commands, while the planner assumes that error before restricting its commands. Tightening an upper constraint by an arbitrary tolerance conceals that circular dependence. A feasible first command can also lead to a state from which no later command is feasible.

The construction must close both the simultaneous compatibility question and the continuation question.

### CAD.3:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Planning freedom and correction authority | Aggressive nominal commands consume input needed for error rejection. |
| Tight bounds and defensible bounds | A smaller assumed error enlarges the command domain but can invalidate its own premise. |
| One feasible step and continued operation | Current feasibility does not ensure a viable successor. |
| Sampled evidence and continuous constraints | A bound at update instants can miss a violation between them. |

### CAD.3:4 - Solution

#### CAD.3:4.1 - Construct an invariant error set

For the linear interface of CAD.2, write

$$
e^+=Fe+Hz+Gv+w.
$$

Choose a proposed command set S of pairs $(z,v)$, a bounded mismatch set W, and an error set E containing the admitted initial error. A sufficient one-step condition is

$$
FE\ \oplus\ \{Hz+Gv:(z,v)\in S\}\ \oplus\ W\ \subseteq E.
$$

Here $\oplus$ is addition of sets. This is a property to establish, not a consequence of naming E an error tube. Substitution and induction then keep the error in E for every permitted command sequence. Preserve correlations between z and v when they materially reduce conservatism; replacing S by a Cartesian product can enlarge the forcing unnecessarily.

One usable construction takes a positive-definite M and the norm $\|e\|_M=\sqrt{e^\mathsf{T}Me}$. Verify

$$
q=\|M^{1/2}FM^{-1/2}\|_2<1,\qquad
d\geq\sup_{(z,v)\in S,\ w\in W}\|Hz+Gv+w\|_M.
$$

The triangle inequality gives $\|e^+\|_M\leq q\|e\|_M+d$. Therefore

$$
E=\{e:\|e\|_M\leq\varepsilon\},\qquad
\varepsilon\geq\max\{\|e_0\|_M,d/(1-q)\}
$$

is invariant. For a stable fixed F, a positive-definite solution of a discrete Lyapunov equation is a candidate M; verify the displayed norm inequality for the actual values used. Failure of this sufficient construction does not prove that no controller or invariant set exists.

For multiple timing modes, one sufficient condition for arbitrary admissible switching is a common set E containing the initial error and preserved by every admitted mode and reset map. This includes resets caused by a changed reference or error coordinate. Each step then starts in the same E, so induction covers any admitted sequence.

Separate invariant sets for the frozen modes are not sufficient by themselves. With mode-dependent or within-period phase sets $E_i$, prove that every allowed transition from mode or phase i to j, including its reset, sends the admitted part of $E_i$ into $E_j$ for all admitted commands and disturbances. Include initialization and the evolution within each phase. A boundary-map proof can use this construction, but a bound only at period boundaries leaves the intermediate phases uncovered.

#### CAD.3:4.2 - Translate error into planner and actuator constraints

With $x=Pz+e$ and $u=Qz+Rv+Ke$, require

$$
Pz+E\subseteq X,\qquad Qz+Rv+KE\subseteq U.
$$

These constraints reserve physical room and actuator authority for correction. For an output constraint use the actual output map, including the mismatch term in CAD.2:4.1.

For example, if $X=\{x:Lx\leq b\}$ and E is the ellipsoid above, each row must satisfy

$$
L_iPz+\varepsilon\sqrt{L_iM^{-1}L_i^\mathsf{T}}\leq b_i.
$$

If $U=\{u:Du\leq f\}$, the input row becomes

$$
D_i(Qz+Rv)+
\varepsilon\sqrt{D_iKM^{-1}K^\mathsf{T}D_i^\mathsf{T}}\leq f_i.
$$

Thus the amount of tightening comes from the connected dynamics and geometry. It is not a universal safety percentage.

Enforce these conditions at every instant covered by the claim. If z evolves between slow updates, an upper constraint checked only at those updates does not bound $Qz$ at every fast instant. Propagate the nominal trajectory or bound its intermediate states. Continuous-time constraints require a continuous evolution argument, not denser-looking sampled plots.

#### CAD.3:4.3 - Close the dependence between commands and error

The proposed command domain determines d, while the resulting E restricts the command domain. Solve this compatibility deliberately. Start with a desired command envelope, construct a valid E, then test the actual state and input inclusions. If they fail, choose a smaller envelope or change the interface, gains, model or timing, and repeat the affected derivation.

A more direct formulation searches for S and E satisfying the error inclusion and the physical constraints together. For finite-dimensional parameterizations this can be an optimization or feasibility problem. No generic solver or convergence guarantee follows from writing that problem.

Do not treat repeated tightening as automatic convergence. A mapping that sends candidate planning sets to newly permitted sets can reverse inclusion: larger commands produce larger errors and smaller permitted commands. Alternating bounds may remain separated. Establish a nonempty self-consistent pair and its inclusions; do not use a numerically stationary iteration as the proof.

When a bound is conservative, try retaining command correlation, phase-dependent sets or a better model before weakening a hard constraint. For a fixed qualified loop, compare a joint state-command admissible set with the separate command and error envelopes used here; [CAD.Reference:4.5.1](#cadreference451---keep-a-qualified-loop-and-govern-its-commands) gives the governor entry, and :11 identifies a construction using time-dependent estimation bounds. Establish its successor conditions for the actual command rule before replacing this sufficient construction. If the required command is physically impossible, return that incompatibility to the system requirement or architecture decision.

#### CAD.3:4.4 - Construct a continuation, not only one permitted command

A permissible pair $(z,v)$ must also lead somewhere from which work can continue. For the nominal update $z^+=A_pz+B_pv$, seek a set Z such that every admitted z has at least one permitted v with $z^+\in Z$.

One direct construction repeatedly removes states without such a successor:

$$
Z_{n+1}=
\{z\in Z_n:\exists v,\ (z,v)\in S,\ A_pz+B_pv\in Z_n\}.
$$

An exact fixed point is controlled invariant under the stated model. A finite iteration gives an outer candidate, not automatically an invariant set; test the successor condition before relying on it. Gridding a continuous set needs an approximation-error argument.

An alternative is to exhibit a smaller terminal set T and an explicit admissible terminal law. A finite plan ending in T then has a feasible continuation by appending that law. For receding-horizon use, the standard shift argument also needs the actual next nominal state, retained feasible tail, modeled uncertainty and implementation to match the argument. A measurement-based reset must preserve the initialization and feasibility conditions or use an independently qualified recovery.

If a new optimization fails or misses its deadline, continuing a previously feasible tail can be legitimate only while its assumptions still hold. “Use the previous plan” is not a universal fallback.

#### CAD.3:4.5 - Use a continuous-time branch only with its stronger premises

Let D be the domain of the connected continuous state on which the model and the bounds below apply, including the reference and any controller state on which the argument depends. Start the trajectory in D and suppose a differentiable function V satisfies, throughout D under the admitted input law,

$$
V\geq c_e\|x-Pz\|^2,\qquad
\dot V\leq-\alpha V+\beta\|w\|^2,
$$

with positive $c_e,\alpha$, nonnegative $\beta$, and $\|w(t)\|\leq\bar w$. Let $\tau_D$ be the first exit time from D, with $\tau_D=\infty$ if there is no exit. For every $0\leq t<\tau_D$ on which the solution exists, integration gives

$$
V(t)\leq e^{-\alpha t}V(0)
+\frac{\beta\bar w^2}{\alpha}(1-e^{-\alpha t}).
$$

Consequently $\|x-Pz\|\leq\varepsilon$ on that interval, where
$\varepsilon^2=\max\{V(0),\beta\bar w^2/\alpha\}/c_e$.
If h is Lipschitz with constant $L_h$ on a state domain containing both x(t) and Pz(t), requiring
$h(Pz(t))\geq L_h\varepsilon$ implies $h(x(t))\geq0$ on the same interval.

To claim the conclusion for all future time, separately establish continued existence and containment of the connected trajectory in D under the allowed reference evolution and disturbances, for example through a forward-invariant subset of D containing the admitted initial states. A tracking-error bound alone does not prevent the reference and plant from leaving the region where the derivative or Lipschitz bound is valid.

This is a sufficient construction for a particular connected dynamics and admissible input law. Obtain V and verify its derivative, domain, actuator feasibility and treatment of the moving reference; their existence is not supplied by the formula. Sampling, estimation, saturation and delay must either occur in that dynamics or be covered by its perturbation bound.

#### CAD.3:4.6 - Separate recognition, mathematical assurance and physical reliance

A shrinking error trace or plausible margin recognizes a promising design. The invariance and continuation arguments establish conditional properties of a mathematical model. Model validation, parameter and disturbance bounds, execution timing and physical tests determine whether those properties support the intended engineering use.

A decrease condition that applies only outside a threshold does not, in discrete time, prevent a jump from inside to outside. Use an actual invariant-set inclusion or a one-step bound valid on the entire proposed set. Likewise, a small average error is not a worst-case constraint bound.

### CAD.3:5 - Archetypal Grounding

For the held-reference case of CAD.2, $a=1/2,N=4,\delta=0.1$ give $E=8/75$. Since $|u|=(1-a)|e|$, a sufficient input bound is $4/75\approx0.05333<0.06$. Requiring $|r|\leq1-E=67/75$ also suffices for $|x|\leq1$. This position tightening is conservative: the scalar convex update can support less restrictive position arguments. It is not claimed to be the maximal command domain.

Now double the requested average progression from 0.025 to 0.05 per fast tick while retaining four-tick held updates. Then $\delta=0.2$, $E=16/75$, and the sufficient input bound is $8/75\approx0.10667$. More decisively, an initial jump from $x=r=0$ to $r=0.2$ commands $u=0.1$, directly violating the limit. Merely saturating u changes the error dynamics and requires a new analysis.

For continuous joined segments with $|d_k|\leq0.05$, $E=0.1$ and $|u|\leq0.05$. Choose $|r_k|\leq0.9$ and initialize $|x_0-r_0|\leq0.1$. Then the stated state and input limits hold at every fast sample. Generate the next reference by clipping $r_k+d_k$ to the interval $[-0.9,0.9]$, with $|d_k|\leq0.05$. The choice $d=0$ is always available, so the reference domain has an explicit continuation. This proves model feasibility even at a boundary; it does not promise arrival at every requested target or continuous physical safety between samples.

### CAD.3:6 - Bias-Annotation

Robust envelopes can be unnecessarily restrictive, especially when correlations are discarded. Conversely, nominal examples can make the operating domain look larger than the evidence warrants. Keep sufficiency, necessity, conservatism and empirical observation distinct.

### CAD.3:7 - Conformance Checklist

- The bound covers the actual initial condition, command class, mismatch and timing modes.
- Switching uses a common invariant set or proved transitions between the admitted mode or phase sets.
- A continuous-time claim ends at the first exit from its proof domain unless continued existence and containment in that domain are established.
- Every claimed constraint is tied to the instants or continuous intervals actually covered.
- Nominal commands leave justified correction authority.
- The command/error dependence closes without a circular assumption.
- There is a feasible continuation or an explicit limit on the duration of the claim.
- Physical reliance is no broader than the model and implementation evidence.

### CAD.3:8 - Common Anti-Patterns and How to Avoid Them

A tolerance selected first and justified afterward can consume imaginary authority; derive it with the command domain. A nonempty feasible set can contain dead ends; test successors. A sampled safe plan is not a continuous safety argument. A stable controller plus actuator saturation is a different closed loop from the unsaturated proof.

### CAD.3:9 - Consequences

The designer obtains commands that the whole architecture can support under stated conditions, or a precise reason to revise it. Some planning freedom is exchanged for dependable correction. The result may be conservative and computationally expensive; those costs belong in CAD.4.

### CAD.3:10 - Architectural Rationale

The lower guarantee and upper assumption concern the same connected behavior. Error propagation and constraint propagation therefore form one coupled construction. Adding continuation prevents a one-step solution from being mistaken for an operating strategy.

### CAD.3:11 - SoTA-Echoing

**How can a command domain support continued constrained operation?** The selected line is robust error containment, constraint tightening and a separate continuation argument in :4.1–4.4. It adapts [Stamouli and colleagues' constraint-propagation construction, §§4–5](https://arxiv.org/html/2504.10461). Their reported output-constraint guarantee is at slow samples; the all-fast-sample input extension has an additional condition. Here each claimed time interval is explicit, and direct set inclusion establishes invariance without extending a decrease-only condition into a global bound. The price is a sufficient domain that may exclude useful commands.

A serious alternative for a fixed qualified loop is a governor's joint state-command admissible set ([CAD.Reference:4.5.1](#cadreference451---keep-a-qualified-loop-and-govern-its-commands)). It can retain relations discarded by one common error envelope. [Castroviejo-Fernandez and colleagues, §§4–6, especially Proposition 2](https://arxiv.org/html/2401.02054v1) further use observer-error bounds and a sequence of admissible sets with a proved successor relation. Adapt that idea when a worst-case constant disturbance envelope is unnecessarily restrictive; the extra assumptions on estimation and disturbance variation, and the set computation, must be worth the enlarged domain. This motivates the return in :4.3 rather than weakening a hard constraint.

A predictive safety filter is another alternative when the requested object is a plant input and a finite backup trajectory can be computed. [Milios, Wabersich, Berkel and Schwenkel, §§II–IV](https://arxiv.org/html/2404.05496v2) distinguish recursive constraint satisfaction from additional stability guarantees and supply separate stabilizing conditions. Adopt that distinction in :4.4 and CAD.4:4.2. Such a filter needs its model, terminal ingredients and online computation; inserting it after the tracker changes the law analyzed in CAD.2.

For continuous dynamics, the [Matni–Ames–Doyle treatment, §4.5](https://arxiv.org/html/2401.15185) supplies a distinct safety-transfer line. Section :4.5 adapts the connection through an explicit error margin, conditional on remaining in the derivative and Lipschitz domains; it does not assume that every nonlinear controller supplies those premises. Reopen the selected containment construction when conservatism prevents the task, the admitted switching or disturbance changes, or the intended claim changes from constraint satisfaction to convergence or completion.

### CAD.3:12 - Relations

CAD.2 supplies the exact connected dynamics. CAD.1 is the return when no useful command domain exists for the selected split. CAD.4 uses the size and cost of the feasible domain in whole-candidate comparison. MMP.18 supplies general compatibility reasoning; this pattern supplies the control-specific invariance, margin and continuation construction.

For feedback on an estimated state, CAD.5:4.7 supplies the extra forcing and input allowance. Use its run-wide error bound, including startup and allowed delivery modes, before qualifying the resulting command domain.

### CAD.3:End

## CAD.4 - Co-design and Realize the Whole Control Architecture

> **Type:** Method pattern
> **Status:** Stable

### CAD.4:1 - Problem frame

**Use this when** several control architectures appear feasible, or a change of model, hardware, rate or operating demand can invalidate an existing arrangement. Tuning each controller independently does not decide which complete arrangement should be built.

Start with the same required behavior and resource boundary for every candidate. The first useful result is a feasible whole configuration, its comparison with serious alternatives, and the conditions under which its implementation and later use remain justified.

For a fixed, qualified architecture requiring only a local parameter adjustment, use the relevant controller-design method directly and reopen the whole only if that adjustment changes a relied-on interface, resource or constraint.

### CAD.4:2 - Problem

A detailed planning model may improve prediction but miss its deadline. A faster tracker can use more computation or amplify measurement noise. A longer planning interval can save resources while increasing command mismatch. A design assembled from individually preferred choices may have no feasible joint setting.

The problem is to choose and realize a configuration whose control, model and resource assumptions can hold together.

### CAD.4:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Fidelity, horizon and execution time | More planning information can arrive too late to be useful. |
| Strong correction and implementation limits | A gain that shrinks error can increase input, noise sensitivity or computation. |
| Feasibility and performance | Staying within limits does not establish progress, optimality or adequate tracking. |
| Design model and running system | A proven nominal schedule may differ from actual latency, sharing and failure behavior. |

### CAD.4:4 - Solution

#### CAD.4:4.1 - Form complete candidates

Use C.39 to connect the required result to its supplying operations and C.32/SYSE.6 to retain whole alternatives. A candidate specifies the decomposition, model and its operating domain, exchanged command, timing and reset semantics, controller law, feasible command domain, planning continuation and implementation resources.

Keep architecture choices separate from tunable parameters without pretending that the separation is absolute. The number of layers, model order, kind of command, sampling periods, planning horizon and processor arrangement can change the problem being solved. Gains, weights and numeric tolerances tune a selected construction. Changing either group can reopen the other.

CAD.1–CAD.3 supply the positive construction, not merely a screening list. Existing qualified results can replace repeated design work. If the interface law changes, the old error bound is not a reusable result for that new law.

#### CAD.4:4.2 - Evaluate feasibility before ranking attractive scores

For each candidate, establish the connected error behavior, physical constraints and continuation under its own admitted conditions. Include initialization, transitions, planned modes and fallback behavior. A candidate with a missing load-bearing condition is unresolved, not numerically inferior.

Then evaluate the behavior the task actually values: tracking envelope, settling, progress, resource consumption, disturbance rejection or cost. Use the same demand and perturbation class across candidates. An average objective cannot compensate for violating a hard constraint.

Boundedness and convergence are distinct. For example, if the nominal law makes $z_k\to z_*$ and $v_k\to v_*$, the linear error equation has forcing $g_k=Hz_k+Gv_k+w_k$. With a contractive F, $g_k\to0$ implies $e_k\to0$: the contribution of any fixed finite past decays, and the remaining tail is bounded by its shrinking forcing divided by $1-q$. If $Hz_*+Gv_*\neq0$, even zero disturbance can leave a steady bias. A bounded command domain alone establishes neither nominal progress nor zero error.

When the performance claim requires optimality, robust stability or task completion beyond these arguments, supply the corresponding result for the actual connected model. Do not infer it from the presence of MPC, a Lyapunov function for one component, or an optimizer's successful return.

#### CAD.4:4.3 - Include execution in the design equations

Use MMP.22 to turn the mathematical operation into a workable computation. Identify the data needed when the operation starts, the work that can be prepared ahead, the result required at its deadline, and what must happen if it is unavailable.

A necessary timing comparison is

$$
C_{\mathrm{fast}}\leq T_{\mathrm{fast}},\qquad
C_{\mathrm{plan}}\leq T_{\mathrm{plan}},
$$

where C bounds execution under the selected implementation. These isolated inequalities are not sufficient on a shared processor: blocking, interference, communication and scheduling must fit the deadlines together. An operation count or mean runtime is not a worst-case execution bound.

If planning finishes one period after its observation, model that delay and the command that controls the intervening period. Preparing a future segment can make the delay harmless for a predetermined reference but not automatically for a newly observed obstacle. Increasing the processor speed changes the feasible architecture set; increasing the assumed speed in a spreadsheet does not.

Use the implementation to test unit conversions, numerical tolerances, update order, saturation and reset behavior. A numerical optimizer's constraint tolerance belongs in the margin analysis if it can consume physical clearance. Verify that the lower law actually executed is the law used in CAD.2.

If an online solver returns only a partial iterate, separate the time spent solving from the test that permits applying its output. A qualified acceptance rule may allow a feasible inexact result and otherwise keep an admissible prior command or plan. Include the cost of that test and the conditions for progress; a timeout says nothing about admissibility, and feasibility alone does not establish progress. The command-governor alternative in :11 is one developed construction, not a fallback rule for every optimizer.

#### CAD.4:4.4 - Search jointly, with bounded conclusions

A practical first search can enumerate a small number of architecture choices and, within each, solve or tune the continuous parameters. Recompute the error and command domain for every material change. Reject a setting whose necessary constraints fail; retain unresolved settings separately from feasible ones.

Compare feasible candidates through task-relevant trade-offs and costs. Do not collapse incompatible obligations into an invented scalar score. A Pareto comparison can expose choices where one candidate is faster but more resource intensive. If the search covered only a grid, selected controller class or local optimizer, state that reach; it does not prove global architectural optimality.

Investigate the active limitation. If actuator reserve fails, altering the reference interface may help more than enlarging the processor. If timing fails, a reduced model or shorter horizon may help more than increasing gain. If a reduced model loses an important mode, a larger controller budget may be unavoidable. This is the constructive feedback from the whole evaluation to CAD.1–CAD.3.

#### CAD.4:4.5 - Qualify the realization and its revision conditions

Separate mathematical consequence, model qualification and implementation observation. Simulation can reveal an omitted mode or a bad reset. Tests on the target execution arrangement can expose deadline misses. Physical experiments can challenge the model, disturbance envelope and actuator assumptions. None automatically establishes every other claim.

Before relying on the design, identify the operating conditions that support it and the observations that can invalidate them. Examples are a larger reference jump, changed disturbance envelope, delayed sensor, actuator derating, altered model order or shared computing load. Reopen the specific equation, inclusion or comparison using the changed premise.

Choose detection and fallback behavior for the actual failure mode. A reference hold is justified in the running model because it lies within the admitted command class; in another plant it may be unsafe or mission-defeating. For an unexplained timing overrun or model residual beyond the admitted W, stop claiming the old bound and use only a separately qualified response.

The resulting control architecture returns to SYSE.6 with its feasible domain, performance, resource needs and unresolved constraints. That system decision can change sensors, actuators, plant structure or requirements rather than forcing every problem into controller tuning.

### CAD.4:5 - Archetypal Grounding

#### CAD.4:5.1 - Compare rates at the same requested progression

For the discrete actuator example, assume a dedicated planner resource needs two fast ticks per result. The fast controller has a separate resource. Commands are prepared for their applicability interval; initialization supplies the first segment. This is a declared toy resource model, not measured processor performance.

At progression 0.025 per fast tick, a held reference changes by $\delta=N/40$. At progression 0.05 it changes by $\delta=N/20$. The sufficient error and input bounds are derived from CAD.2, with $a=1/2$.

| Command and demand | N | Error bound E | Input bound | Two-tick planning time fits? |
| --- | ---: | ---: | ---: | --- |
| Held, 0.025 per tick | 1 | 0.05 | 0.025 | No |
| Held, 0.025 per tick | 2 | 0.066667 | 0.033333 | Yes |
| Held, 0.025 per tick | 4 | 0.106667 | 0.053333 | Yes |
| Held, 0.05 per tick | 1 | 0.1 | 0.05 | No |
| Held, 0.05 per tick | 2 | 0.133333 | 0.066667 | Yes |
| Held, 0.05 per tick | 4 | 0.213333 | 0.106667 | Yes |
| Joined segment, increment at most 0.05 per tick | 4 | 0.1 | 0.05 | Yes |

At the original demand, two held-command arrangements pass this sufficient input test; their compute use and tracking behavior can be compared. At doubled demand, neither of the considered held arrangements that fits the planning time passes it. The N=4 case also has the direct violating first jump shown in CAD.3. For N=2, two successive positive changes of 0.1 from rest produce an input of 1/16 = 0.0625 at the second change, also above the limit.

The segment arrangement admits the higher demand under the stated sampled model and margins. It adds a clocked reference generator and continuity checks. It does not demonstrate that this arrangement dominates all possible controllers or that more than two layers would help.

#### CAD.4:5.2 - Carry the mathematical result into execution

The planner proposes a next endpoint and applicability time. The reference generator checks that the segment starts at the current reference, remains in $[-0.9,0.9]$, and advances by at most 0.05 per fast tick. The fast law uses that generated reference, not the endpoint held for four ticks. An unavailable segment leaves the reference unchanged; the initialization error must already satisfy the bound.

A hardware test that reveals a one-tick delay in actuation changes $x_{k+1}=x_k+u_k$ into a model with an input delay. The table is no longer sufficient evidence. Return to CAD.2 to derive the delayed dynamics and to CAD.3 for the resulting margins. Retain the comparison of command meanings and the source-independent arithmetic; do not retain the unqualified physical feasibility conclusion.

### CAD.4:6 - Bias-Annotation

A convenient cost model can favor the hardware already at hand. A small parameter search can make its winner look universal. State the tested choices and preserve alternatives whose decisive conditions remain unknown. The running case demonstrates an interface repair, not an empirical prevalence claim.

### CAD.4:7 - Conformance Checklist

- Complete candidates are compared under the same task and constraints.
- Connected feasibility and continuation are established before performance ranking.
- A convergence or optimality claim has its own applicable grounds.
- Execution, communication and scheduling assumptions fit the implemented arrangement.
- Search limits and unresolved candidates are visible.
- Changed-condition and fallback behavior return to the premise that actually changed.

### CAD.4:8 - Common Anti-Patterns and How to Avoid Them

Optimizing each layer and connecting the winners can destroy feasibility; compare complete settings. Choosing rates from “fast” and “slow” labels hides dynamics and execution costs; derive their effects. A predicted runtime is not a deadline guarantee. A fallback that was never part of the model does not inherit its bound.

### CAD.4:9 - Consequences

The choice can change model order, command representation, rates, controller parameters and hardware together. This broadens the search but can avoid tuning an infeasible arrangement. A declared bounded search yields a defensible local decision, not a universal optimum.

### CAD.4:10 - Architectural Rationale

Control behavior and execution are coupled: computation changes latency, latency changes error, and error changes admissible commands. The whole design must therefore be the unit of comparison. Keeping each intermediate result explicit lets an implementation change reopen only the dependent reasoning.

### CAD.4:11 - SoTA-Echoing

**What should change when a complete control arrangement misses its demand or resource limit?** The selected line compares coupled architecture and tuning choices, while retaining a qualified fixed loop with local command modification as a serious alternative. It adopts the joint-choice formulation in [Verhoek, Stamouli, Pappas and Matni, 2026 preprint, §§3–7](https://arxiv.org/html/2610.20900v1): model dimensions, sampling ratios, horizons and controller parameters affect the same feasibility problem. That construction fixes a two-layer LTI setting and specified delay and controller classes; efficient general optimization remains open. Sections :4.1–4.4 adapt the comparison to a bounded candidate search and require implementation timing rather than treating a computation-cost proxy as a deadline bound. The gain is avoiding incompatible local optima; the cost is a larger search and repeated qualification of coupled choices.

When the lower loop already has the required local performance, first compare changing its command admission or solver. [Garone and Kolmanovsky, §§3–4 and Algorithm 1](https://arxiv.org/html/2111.10234) develop command-governor logic permitting inexact optimization and a non-invariant inner admissible set, with stated feasibility and progress conditions. Adopt the separation between accepting a computed command and merely obtaining a solver output in :4.3; neither an arbitrary partial iterate nor an unqualified hold inherits that result. This can be preferable to buying faster computation or redesigning the tracker, but command progress and admissible-set computation remain costs to compare.

Switching among existing controllers is also a genuine architectural alternative. [Wang, Di Cairano and Sanfelice, 2024, §§III–V](https://www.merl.com/publications/docs/TR2024-091.pdf) combine mode-specific admissible sets with explicit switching and Lyapunov conditions. Adapt that comparison when a fast transient and a less oscillatory final approach favor different controllers; carry the guards and transitions into :4.2 and CAD.3:4.1. Separate stable modes alone do not supply the switched guarantee. Reopen the choice when task demand, computing interference or the cost of maintaining those mode conditions changes.

### CAD.4:12 - Relations

CAD.1, CAD.2 and CAD.3 supply candidate decomposition, connected dynamics and admissible commands. Their results are dependencies of the whole comparison, not mandatory fresh work for every application. C.39 supplies general Method construction; MMP.22 supplies the mathematical-to-practical transformation. SYSE.6 receives the control result within the system architecture decision. C.30.LCA tests the resulting view's coverage, not the control theorem.

CAD.5 supplies observation, internal-state and estimator alternatives with their error and execution conditions. Shared computation can change their observation age, so a different implementation can reopen that information result and the dependent CAD.3 margins.

### CAD.4:End

# License

Copyright (c) Anatoly Levenchuk. This framework's original text and worked examples are licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Cited third-party works retain their own terms.
