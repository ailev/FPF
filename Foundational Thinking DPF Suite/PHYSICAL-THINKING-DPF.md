# Physical Thinking DPF

> A pattern language for forming physical accounts, deriving usable consequences, constructing observations and revising the physical assumptions.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 22 September 2026
- **Status:** Eternal alpha: a usable repertoire that remains open to correction and extension.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF ecosystem repository](https://github.com/ailev/FPF)

Begin with the physical question in your work. Use the Table of Contents to find a relevant method, then open its Problem frame, Solution, worked cases and checklist. The Readme follows worked connections between methods; the Preface explains how the methods connect, which knowledge they require and how to revise a physical account.

The reference code **PHY** names this DPF. Its numbers are stable pattern addresses; § shows position within a Part. The methods can be used separately or in longer routes with mathematical and computational contributions.

This publication belongs to the [Foundational Thinking DPF Suite](https://github.com/ailev/FPF/tree/main/Foundational%20Thinking%20DPF%20Suite). Its [Reference](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains those connections and the available publications. References such as B.5.MPC and C.29 name patterns in [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). Open the cited body when its contribution is needed; revisit a receiving conclusion when that contribution changes.

To cite this edition: Anatoly Levenchuk, *Physical Thinking DPF*, [FPF ecosystem repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Physical Thinking - Readme](#physical-thinking---readme) | Follow worked connections between physical methods. |
| Preface | [Physical Thinking - Preface](#physical-thinking---preface) | Understand the connected methods, their rationale, sources and limits. |

## Part A - Construct and constrain a physical account

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [PHY.4 - Constrain an Unknown Physical Law by Transforming the Situation](#phy4---constrain-an-unknown-physical-law-by-transforming-the-situation) | Usable, evolving | unknown law; symmetry; physical transformation; dimensions; balance; dissipation. What can be concluded before a full response law is known? | MATH.13 for a symmetry consequence; MMP.11 for an unknown response family. |
| 2 | [PHY.5 - Choose an Effective Physical Description by Scales and Couplings](#phy5---choose-an-effective-physical-description-by-scales-and-couplings) | Usable, evolving | scale separation; coupling; memory; fluctuation; transient; effective description. Which physical effects can be omitted for the consequence and duration of interest? | MMP.9 for mathematical elimination; PHY.6/.8 when evolution or collective preparation matters. |
| 3 | [PHY.6 - Construct Physical Evolution from Balances and Response Laws](#phy6---construct-physical-evolution-from-balances-and-response-laws) | Usable, evolving | participants; exchange; balance; constitutive response; preparation; boundary condition. Which physical laws and conditions close the proposed evolution? | C.29.BB for balances; MMP.10 for coupled equations; C.29.2 for computational formulation. |
| 4 | [PHY.7 - Obtain Motion from a Physical Variational Principle](#phy7---obtain-motion-from-a-physical-variational-principle) | Usable, evolving | physical action; admissible history; constraints; boundary freedom; variation. What physical grounds permit a variational construction, and what motion follows? | MATH.10 for mathematical variation; PHY.6 for the direct balance alternative. |
| 5 | [PHY.8 - Infer Macroscopic Physical Behavior from Microscopic Alternatives](#phy8---infer-macroscopic-physical-behavior-from-microscopic-alternatives) | Usable, evolving | microstates; preparation; ensemble; correlation; fluctuation; relaxation. Which physical distribution and dynamics support a collective prediction? | MMP.7 for probability composition; MMP.9 for reduction; PHY.6 for the required physical evolution. |

## Part B - Compare, observe and act

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [PHY.1 - Construct Physical Similarity Across Changed Conditions](#phy1---construct-physical-similarity-across-changed-conditions) | Usable, evolving | scaling; similarity; dimensionless groups; prototype; changed regime. When does a physical result transfer to a different size, material or condition? | PHY.5 for consequential omitted effects; mathematical methods for the resulting comparison. |
| 2 | [PHY.2 - Construct a Physical Analogue from Interactions](#phy2---construct-a-physical-analogue-from-interactions) | Usable, evolving | physical analogue; mechanism; interaction; preparation; readout. How can another physical arrangement supply a wanted consequence? | PHY.5/.6 for physical description and evolution; PHY.9/.10 for observation and comparison; C.29.3 for computing realization. |
| 3 | [PHY.9 - Construct a Measuring Interaction for a Physical Distinction](#phy9---construct-a-measuring-interaction-for-a-physical-distinction) | Usable, evolving | measuring interaction; transduction; reference; calibration; disturbance; ambiguity. How can the needed property be made to affect an observable indication? | C.16.MR for the measurement relation; C.16.IR for inference from indications; PHY.10 for competing physical accounts. |
| 4 | [PHY.10 - Construct a Physical Test That Separates Rival Accounts](#phy10---construct-a-physical-test-that-separates-rival-accounts) | Usable, evolving | rival accounts; physical contrast; preparation; apparatus; parameter freedom; noise. Which feasible comparison separates the consequences that matter? | PHY.9 for a needed readout; PHY.6 for evolution; B.5.TC for theoretical comparison. |
| 5 | [PHY.3 - Derive a Physical Limit from Permitted Transformations](#phy3---derive-a-physical-limit-from-permitted-transformations) | Usable, evolving | physical limit; impossibility; reversible reference; complete exchanges; changed premise. What can a proposed transformation achieve under the physical laws and resources supplied? | C.29.BB for balances; MATH.11/.20 for invariants or bounds; PHY.2 for another physical construction. |

# Physical Thinking - Readme

## Practical entries

Bring the physical question from your work. A useful answer may need a physical account, a consequence derived from it, and an observation that distinguishes what remains unresolved. The worked connections below show how one method's result becomes another's input, where an existing result lets you enter, and which changed condition sends you back.

These are selected examples, not a catalogue or a prescribed sequence. Use the Table of Contents and each pattern's title and Problem frame for other questions or direct help. The bodies explain their methods, prerequisites, examples and return conditions. The physical theory and mathematics stated for a case belong to that application, not to every method.

You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.” Ask it to show what the quantities and operations mean, where the physical premises enter, and what the result lets you do next.

### PH-PREDICT-AND-DISTINGUISH - Develop a physical prediction and the test it needs

- **Situation:** Several physical accounts fit what is known but imply different consequences for the work.
- **Question:** How can we construct the consequences and resolve only the difference that matters?
- **First useful result or blocker:** A conditional prediction that answers the working question, or a consequential difference and a feasible comparison that could resolve it.
- **Start with:** [PHY.4](#phy4---constrain-an-unknown-physical-law-by-transforming-the-situation) when the law is unknown; [PHY.6](#phy6---construct-physical-evolution-from-balances-and-response-laws) consumes a supplied response to construct evolution; [PHY.10](#phy10---construct-a-physical-test-that-separates-rival-accounts) is needed when rival consequences remain worth distinguishing.
- **Stop or return:** Stop at a sufficient consequence. Return to the affected law, preparation or observation when its premise changes.

#### From an unknown resistance to a useful comparison

**1. Carry the remaining freedom into candidate laws.** The work needs the distance a body travels while slowing from 1 m/s to 0.5 m/s through a medium. Stipulate an effective inertia of 1 kg, no other force along the motion, and an instantaneous resistance at fixed material conditions. PHY.4 uses an isotropic comparison and a passive response to constrain the resistance's direction. Those conditions leave its speed dependence unresolved. A force magnitude of 1 N at 1 m/s admits both `D=b*v`, with b=1 N·s/m, and `D=c*v²`, with c=1 N·s²/m². These are two candidate laws, not all possibilities allowed by that information.

**2. Consume each law in the requested prediction.** PHY.6 combines resistance with `m*dv/dt=-D(v)` and `dx/dt=v`. MMP.10 formulates those relations with the preparation; C.29.2 obtains the requested consequence. Eliminating time gives `dx/dv=-m*v/D(v)`. Over the stated speed interval, the linear law gives a distance of 0.5 m, while the quadratic law gives `ln(2)` m, about 0.693 m. With only 0.6 m available, the two accounts give different answers. With more than 0.7 m available, both satisfy this requirement under their premises, so this difference alone supplies no reason for another test.

**3. Make a consequential difference observable.** If the 0.6 m question still matters, PHY.10 consumes the two response laws to select a comparison at maintained speed 0.5 m/s. They predict 0.5 N and 0.25 N. A supplied calibrated force arrangement with indication error bounded by 0.02 N gives non-overlapping ranges [0.48,0.52] N and [0.23,0.27] N. An indication of 0.25 N would be compatible with the quadratic candidate and incompatible with the linear candidate under these conditions. If the required readout is unavailable, [PHY.9](#phy9---construct-a-measuring-interaction-for-a-physical-distinction) takes the predicted force difference as the distinction its measuring interaction must expose; the distance result remains conditional meanwhile.

**4. Check the physical transfer, then reopen only what changed.** The maintained-speed comparison informs coasting only if the instantaneous-response and material premises cover both preparations. [PHY.5](#phy5---choose-an-effective-physical-description-by-scales-and-couplings) examines a consequential wake or relaxation time if that transfer is doubtful; memory can require another state in the evolution rather than a changed coefficient. If the medium's material condition changes between force comparisons, recover its effect before treating the later indication as a test of the original candidates. Their conditional integrals remain correct; their applicability to the changed run has reopened. Neither result establishes behavior at zero speed or in a new physical regime.

[PHY.Preface:4](#phypreface4---worked-connection---from-an-unknown-resistance-to-a-useful-comparison) gives the connected account and division of physical, mathematical and computational work. The same dependence can arise in an unfamiliar transient, a collective response or a physical analogue. The physical laws and observable change with the situation; the contributions still have to support one interpreted answer.

### PH-COLLECTIVE - Choose a collective description for the time that matters

- **Situation:** A simpler collective law may answer a late-time question while losing a response needed soon after preparation.
- **Question:** Which microscopic behavior survives into the requested observable, and does the proposed reduction retain it accurately enough?
- **First useful result or blocker:** A collective prediction with an adequate error for the requested time, or the state or preparation that must remain.
- **Start with:** [PHY.8](#phy8---infer-macroscopic-physical-behavior-from-microscopic-alternatives) for the microscopic alternatives and preparation; PHY.6 connects their transport and transitions into evolution; PHY.5 chooses which physical response a reduced account may omit.
- **Stop or return:** Use a sufficient conditional prediction. A changed time, observable or preparation returns to the part of the account that supplied it.

#### From persistent motion to a justified diffusion calculation

**1. Keep the preparation with the microscopic law.** In [PHY.8:5.3](#phy853---derive-transport-from-persistent-microscopic-motion), particles start at the origin on an unbounded line, with either direction equally likely. Each moves at speed v>0 and reverses direction at independent Poisson events of rate alpha>0. These are supplied physical premises; a fitted position histogram would not establish the reversal mechanism or its time scale.

**2. Turn those premises into the collective evolution.** PHY.6 balances transport and transitions between the two directions. With n the total position-probability density and j its current, the resulting relations are

`partial_t n = -partial_x j`,

`partial_t j = -v²*partial_x n - 2*alpha*j`.

The ideal point preparation leaves probability atoms at x=±v*t for particles that have not yet reversed; these density equations are understood in the distributional sense. PHY.8 connects their solution to the observable needed here: mean-square displacement at a specified time. The current carries directional persistence even though the mean position stays zero.

**3. Decide whether the faster response can be omitted.** PHY.5 compares the observation time with the current's relaxation time `1/(2*alpha)` and checks the spatial variation. When the reduction is justified, [MMP.9](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp9---derive-a-reduced-mathematical-model-of-state-evolution) supplies the mathematical reduction: replace the relaxed current by `j approximately -D*partial_x n`, with `D=v²/(2*alpha)`, to obtain a diffusion equation. The question still decides whether its consequence is accurate enough.

For v=2 cm/s and alpha=1/s, PHY.8's full account gives

`E[x(t)²] = (v²/alpha)*(t-(1-exp(-2*alpha*t))/(2*alpha))`,

while diffusion gives `2*D*t`. At 20 s these are about 78 and 80 cm². The relative overestimate is about 2.56%, so a 3% allowance for this observable permits the reduced result under the supplied premises. This is a comparison with the microscopic model, not an experimental validation of it.

**4. Return through the consequence that changed.** Ask instead for the spread at 0.1 s. The full result is about 0.03746 cm²; diffusion gives 0.4 cm². Restore the current response for this early question. A finer computation of the same diffusion equation cannot recover what its reduction removed. A question about arrival at a boundary would need the corresponding boundary conditions and its own comparison; agreement on mean-square displacement does not supply that answer.

A simulation used to obtain these timed predictions must implement the stated reversals and their physical time. An artificial sampler that reproduces a position distribution supplies a different result. If the conditional prediction already serves the work, no new measurement is mandatory; if the physical mechanism or preparation is the consequential uncertainty, that becomes the next physical question.

### PH-LIMIT - Use a physical bound before designing a mechanism

- **Situation:** A proposed cyclic device promises 60 J of work from 100 J of heat taken from a 600 K reservoir, rejecting heat only to a 300 K reservoir.
- **Question:** Can a different mechanism achieve this with the same resources and restoration conditions?
- **First useful result or blocker:** The stated second-law comparison bounds net work by 50 J, excluding the 60 J proposal within these conditions.
- **Start with:** [PHY.3:5.1](#phy351---bound-a-proposed-engine-without-designing-its-mechanism), which constructs the comparison from complete exchanges.
- **Stop or return:** Use the exclusion without designing every possible engine. Reopen the exchange account if an extra resource or a different end condition is allowed.

The reservoirs have fixed absolute thermodynamic temperatures, the device returns to its initial state, and no other resource is consumed. Under the supplied classical second-law account, `W <= (1-300/600)*100 J = 50 J`. Energy balance alone would allow the proposed 60 J and therefore would not settle the question. The bound restricts net work; it neither supplies an attaining design nor its power or cost. External work, a nonthermal resource or an unrestored auxiliary changes the account to be compared, not the arithmetic of the original bound.

# Physical Thinking - Preface

## PHY.Preface:1 - Problem frame - Construct a physical account you can use and change

You may know a physical definition, solve a supplied equation or run a simulator and still be unable to begin an unfamiliar physical problem. The participants in the definition may be hard to recognize in the observed situation. The equation may omit the interaction that changes the answer. A computed result may concern a different preparation from the one available in the project.

Physical Thinking supplies methods for constructing and changing those connections. Its ten patterns constrain an unknown law, choose an effective description, construct evolution and collective behavior, develop similarity and analogues, make distinctions observable, compare rival accounts and derive physical limits. They are methods used across physical subjects. Particular material laws, devices and experimental techniques enter as the physical knowledge needed by an application.

The reader may conduct an investigation, design a system, interpret a result, or work with specialists and AI. Begin with the consequence that matters. A useful outcome can be a possible construction, a conditional prediction, a bound, a failed physical premise or a next question whose answer would change the work.

You need to follow what the quantities represent and what the proposed physical laws assume, or obtain an explanation of the missing contribution. The mathematical preparation depends on the chosen method: a similarity calculation, a differential evolution and a quantum measurement use different constructions. Each pattern states the preparation for its own cases. Reading a worked solution can help acquire that capability; applying the method to a changed situation tests a different and necessary part of learning.

Use a familiar adequate law and procedure directly when they already answer the question. This language is useful when the physical account, its applicability or its connection with observation and computation still needs work.

## PHY.Preface:2 - Problem and forces - Keep the physical question through the calculation

A physical calculation operates on mathematical objects chosen to describe participants, states, interactions and observations. A consequence of those objects answers the physical question only through the interpretation and premises that connect them. A correct calculation can therefore expose an omitted physical distinction without supplying the law that repairs it.

Several tensions shape the choice of method:

| Working tension | Choice that changes the result |
| --- | --- |
| A complete mechanism and a useful first consequence | Can a direction, bound or constrained family answer before the whole law is known? |
| Physical detail and obtainable calculation | Which scale, state or interaction can be omitted for this consequence? |
| A mathematical comparison and a changed physical situation | Which participants, preparation and surroundings must transform together? |
| A predicted difference and an observable difference | Can the actual interaction and readout expose the distinction? |
| Agreement and criticism | Does the observation separate the accounts, or do their free parameters and apparatus effects still overlap? |
| Further inquiry and available effort | Would another computation or experiment change a decision worth its cost? |

These choices can occur in theory construction as well as in an applied project. An unexplained dependence, a failed comparison or an impossibility can open a useful new question. The next question may seek another law, a different observation, a new way to prepare the system or an application of an established result.

## PHY.Preface:3 - Solution - Connect physical methods through their results

### PHY.Preface:3.1 - Construct and constrain the account

[PHY.4](#phy4---constrain-an-unknown-physical-law-by-transforming-the-situation) begins while the response law is still unknown. Recover the participants, transform the relevant situation, and derive the restrictions supplied by symmetry, dimensions, balances and dissipation where their physical grounds hold. The remaining unknown function or state directs further work.

[PHY.5](#phy5---choose-an-effective-physical-description-by-scales-and-couplings) chooses the physical detail needed at the requested scale and duration. An omitted state can leave memory or fluctuations; a fast response can matter during a transient. Its result tells mathematical reduction what must be retained or bounded.

[PHY.6](#phy6---construct-physical-evolution-from-balances-and-response-laws) combines physical participants, exchanges, response laws and compatible preparation into an evolution. A balance alone can leave a response undetermined. Locating that missing contribution is useful before any solver is selected.

[PHY.7](#phy7---obtain-motion-from-a-physical-variational-principle) offers another construction when a physically justified variational principle applies. The interactions, allowed comparisons and boundary freedoms determine what is varied. Mathematical variation then derives a consequence. A direct balance remains sufficient in many cases; applying an action formalism to every problem adds work without a corresponding gain.

[PHY.8](#phy8---infer-macroscopic-physical-behavior-from-microscopic-alternatives) constructs collective predictions from physically admissible alternatives and their weighting grounds. It retains correlations, preparation and the difference between sampling a distribution and following physical evolution. A distribution or sufficient bound can remain useful when a particular moment or equilibrium approximation is unavailable.

### PHY.Preface:3.2 - Compare, observe and construct another use

[PHY.1](#phy1---construct-physical-similarity-across-changed-conditions) determines which effects and scale relations let a physical result travel to changed conditions. PHY.5 deepens the question when a neglected effect changes that transfer.

[PHY.2](#phy2---construct-a-physical-analogue-from-interactions) constructs an arrangement whose interactions supply a wanted physical consequence. The construction must include preparation and interpretation. Similar-looking equations can suggest an analogue while leaving those physical tasks unresolved.

[PHY.9](#phy9---construct-a-measuring-interaction-for-a-physical-distinction) makes the wanted difference affect an indication. It develops the coupling, reference or preparation, including disturbance and ambiguity. The result supplies the observation relation used in subsequent inference or comparison.

[PHY.10](#phy10---construct-a-physical-test-that-separates-rival-accounts) constructs a physical contrast between accounts that agree under earlier conditions. It follows the changed preparation through the response and readout, retaining parameter freedom and alternative apparatus explanations. A failed comparison returns to the particular premise that can change it.

[PHY.3](#phy3---derive-a-physical-limit-from-permitted-transformations) derives a bound or impossibility from the complete transformation and an admissible comparison. That result may finish the question or show which physical premise a different construction would have to change.

These connections form possible routes. They do not prescribe a ten-stage workflow. A known response can enter at measurement; an unknown interaction can enter at law construction; a useful impossibility can end work before a device or computation is built.

### PHY.Preface:3.3 - Constituent actions in ongoing work

Acquiring a reading can be part of testing a physical account while the discriminating investigation is already under way. If rival accounts agree at equilibrium but differ during a transition, a settled-value observation cannot answer the same question: its timing must change. Instrument use, the mathematical consequence and knowledge of the accounts can be available separately while the coordination of intervention and observation is missing. The domain's observation Method supplies that intermediate contribution and its equipment conditions.

FPF B.1.5.EW helps recover these constituent–whole connections; B.1.5.RS examines a proposed replacement. Use the parts of the vertical that can change the present result. A Method described here can require additional capability, available support and compatible resources at other grains.

## PHY.Preface:4 - Worked connection - From an unknown resistance to a useful comparison

Consider a body moving through a medium with positive speed v. The work needs to know how far it travels while slowing from 1 m/s to 0.5 m/s. Use a stipulated effective inertia of 1 kg and no other force along the motion. The proposed account treats resistance as an instantaneous function of relative speed at fixed material conditions.

**Constrain before selecting a law.** PHY.4 recovers the medium, relative motion and the conditions kept fixed. In an isotropic comparison without another relevant direction, resistance opposes motion under the passivity premise, while its magnitude can retain an unknown speed dependence. A force magnitude of 1 N at 1 m/s alone leaves, among other possibilities, linear resistance D=b v and quadratic resistance D=c v². Take the corresponding candidates b=1 N·s/m and c=1 N·s²/m². These are two proposed accounts, not all laws admitted by the initial restriction.

**Construct evolution and obtain its consequence.** PHY.6 combines the resistance with the momentum balance and position change: m dv/dt=-D(v), dx/dt=v. MMP.10 retains these relations and their preparation. Eliminating time over the stated positive-speed interval gives dx/dv=-m v/D(v). The computation under C.29.2 can now use the two supplied integrals:

`distance_L = (m/b) (v_0-v_1) = 0.5 m`,

`distance_Q = (m/c) ln(v_0/v_1) = ln(2) m, approximately 0.693 m`.

If the available travel distance is 0.6 m, the two accounts give different answers. For an available distance above 0.7 m, both would meet this particular requirement under their premises; resolving their difference would then need another reason. Neither comparison licenses extrapolation to zero speed or a new physical regime.

**Expose the difference that matters.** PHY.10 asks for a preparation where the candidates diverge. At a maintained speed of 0.5 m/s they predict force magnitudes 0.5 N and 0.25 N. An available calibrated force arrangement with error bounded by 0.02 N separates their predicted indication ranges. An indication of 0.25 N is compatible with the quadratic account and incompatible with the linear one under these conditions. If no suitable readout is available, PHY.9 supplies its construction question; the distance comparison remains conditional meanwhile.

The steady comparison can inform coasting only if the retained instantaneous-response and material premises cover both preparations. PHY.5 examines a consequential wake, relaxation time or other omitted state if that transfer is doubtful. A memory effect can require a different evolution rather than a new value of the old coefficient.

**Change a premise and return locally.** Suppose the medium's material condition changes between the initial and final force comparisons. The coefficient is no longer established as the same. Recover or constrain that dependence before treating the new indication as a test of the two original candidates. Their conditional integrals remain correct; their applicability to the changed run is what reopened.

The resulting work can be divided. A physical contributor supplies the interaction and preparation account, a mathematical contributor derives the permitted consequences, and a computational contributor obtains them in a useful form. B.5.MPC keeps those contributions connected to the distance question; B.5.MPC.R locates the affected return after the material change.

## PHY.Preface:5 - Bias, use checks and recurring failures

The worked cases use tractable theories and idealized arrangements so that the construction and its changed conditions can be followed. A real material, instrument or field situation can require additional subject knowledge. Astronomical or historical physical questions may offer observations without freely controllable interventions. Their comparison must use the physical grounds available there.

When using several contributions together, recover the common question, relevant participants and preparation, the meaning of each result, and the condition under which the next contribution consumes it. Check whether the final consequence answers the requested physical use. Reopen a changed dependency while retaining consequences whose premises still hold.

Several failures recur in the bodies:

| Failure | Practical correction |
| --- | --- |
| A familiar equation supplies a law the situation never established | Retain the unknown dependence and use physical constraints or a discriminating comparison. |
| A simplified state works at one time scale but misses the requested transient | Restore the consequential state, memory or fluctuation before interpreting the computation. |
| A mean or detector indication is treated as the whole physical response | Recover the distribution, recording relation or hidden compatible alternatives needed by the question. |
| An unsuccessful experiment is assigned to the subject law alone | Inspect the preparation, interaction and readout premises that also produced the prediction. |
| Every uncertainty launches another experiment | Use a sufficient bound or conditional result; compare further inquiry with what it can change. |

A learner's ability to repeat one derivation does not establish their ability to choose its physical premises in a new situation. Try changed participants, preparation or observable requirements, and ask what the earlier construction still supports. Explanations and practice can develop that capability; the quality of the explanation and the demonstrated capability are separate questions.

## PHY.Preface:6 - Consequences and Architectural Rationale

This arrangement makes physical construction accessible before a complete equation is supplied. A constraint can guide a model, a balance can locate a missing response, an observable distinction can select an experiment, and a physical limit can redirect development. The cost depends on which contribution is missing. A short derivation may suffice; a new interaction or difficult measurement can require substantial specialist work.

The methods are organized by recurring work rather than by mechanics, optics or another chapter of physics. Those subjects supply theories and techniques used in applications. Organizing a reference by subject remains useful when a practitioner already knows which law is needed; it does less to resolve the preceding choice of physical account or the relation between different accounts.

The separation from Mathematical Thinking and Mathematical Modeling follows the work that remains. A variational calculation does not choose its physical action or boundary freedom. A reduced mathematical system does not by itself establish that discarded physical effects are negligible. Conversely, the physical argument can use a mathematical construction unchanged across several subjects. Keeping that construction available from its supplier prevents each physical method from developing an incompatible version.

There is no universal order of mathematics, physics and computation. A mathematical obstruction can finish a physical proposal; a computed discrepancy can reveal an omitted interaction; a measuring procedure can change what the model has to retain. B.5.MPC governs that connected reasoning. The physical patterns supply methods for the physical contributions.

This is also a way to develop methods of work. A team can change who constructs, interprets or computes a contribution, provided the next contribution can still use its result and conditions. New theory, a changed instrument or a better computational construction can reopen a local choice without replacing the whole repertoire.

## PHY.Preface:7 - Shared sources, alternatives and relations

Physical construction and executable mathematical reasoning meet explicitly in [Sussman and Wisdom's Structure and Interpretation of Classical Mechanics](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/9579/sicm_edition_2.zip/preface001.html). PHY.7 adopts the connected recovery of configuration, interaction and permitted variation. Its comparison with the direct balance route in PHY.6 retains the cheaper sufficient construction and the limits of an ordinary action principle. The shared lesson is to expose the physical premises that a compact formalism can hide.

The [VIM measurement-principle account](https://jcgm.bipm.org/vim/en/2.4.html), GUM measurement-modeling work and the sensing sources discussed in PHY.9 connect the intended quantity, interaction, preparation and indication. PHY.9 uses that connection to construct a missing distinction; PHY.10 uses it to discriminate physical accounts. Merely improving the precision of an insensitive arrangement can leave that work undone.

The statistical-mechanics synthesis by [Baldovin and colleagues](https://arxiv.org/abs/2411.08709) informs PHY.8's separation of physical preparation, collective statistics and time behavior. A useful stationary distribution need not describe an arbitrary transient. Its source discussion compares ensemble calculation, physical simulation and inference, retaining the conditions under which each supplies the needed result.

The experimental-design and noise-spectroscopy sources in PHY.10 develop selection among possible observations and physical changes that expose hidden dynamics. They also bound their claims by the model set, noise account and controllable operations. The framework uses these contributions where they change the method; each body's SoTA discussion gives the adopted comparison and limits. A new source matters when it changes an available construction, a premise, a useful result or the work needed to obtain it.

Within the Foundational Thinking DPF Suite, Mathematical Thinking supplies constructions and arguments; Mathematical Modeling connects a subject question with an interpreted model; Computational Thinking develops obtaining procedures; Notational Engineering develops interpretable expressions and operations on them. The Suite Reference explains their shared arrangement and current availability. Physical work can already use FPF's computational and notational contributions, or another suitable method, when a more specialized Suite contribution is still unavailable.

C.29.1 supplies transfer between mathematical accounts, C.29.2 computational formulation, and C.29.3 the connection to physical execution. C.16.MR and C.16.IR supply measurement relations and inference from indications. B.5's inquiry methods and C.11.DUA help choose a useful next question and the effort worth spending on it. These results can enter directly; using a physical pattern does not require traversing every supplier.

The ten bodies are one repertoire that can be used in different combinations. The two Parts group their presentation; they do not define two sequential stages or a single Method performed by every user.

## PHY.Preface:End

# Part A - Construct and constrain a physical account

## PHY.4 - Constrain an Unknown Physical Law by Transforming the Situation

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.4:1 - Problem frame

Use this pattern when an observed or proposed physical effect needs an account, but the interaction law is not supplied. A detailed mechanism may be unresolved and a familiar analogue may be inadequate. You can still ask how the situation could be changed, what would remain physically equivalent, and which responses those comparisons allow.

Start with one physical response or relation needed by the work. Describe its participants, preparation and relevant surroundings. Construct one comparison that could rule out a proposed dependence or restrict its form. A conditional restriction, together with the dependence it leaves unresolved, is a useful first result.

The method uses transformations justified for the physical situation: changes of position, orientation, scale, preparation, participant assignment or other relevant conditions. It combines their consequences with applicable dimensions, balances and dissipation. The question selects which of these contributions is useful.

You need enough physical understanding to propose the comparison and explain its conditions. Obtain an unfamiliar physical premise from a suitable account or collaborator. A qualitative comparison can already change the next move. The vector example additionally uses rotations and dot products; the chamber example uses elementary algebra and particle balance. Their branch-specific preparation belongs to those examples.

If an established interaction law already answers the question under the intended conditions, apply it. PHY.1 develops physical similarity across changed conditions, PHY.2 constructs a physical analogue, and PHY.3 derives a performance limit from permitted transformations. Return here when the unresolved contribution is the form of the interaction law itself.

### PHY.4:2 - Problem

A formula can be easy to calculate with while admitting a physically impossible direction, an unjustified dependence or an omitted influence. Choosing the formula first can hide those differences.

Conversely, an appeal to symmetry or conservation can appear to determine a law while leaving important functions or parameters free. The task is to obtain the restriction that follows from the physical comparison and carry its remaining freedom into the next construction or inquiry.

### PHY.4:3 - Forces

| Force | Tension |
| --- | --- |
| Unknown mechanism and usable physical grounds | Partial knowledge can constrain the law, while a premise about an omitted influence can invalidate the constraint. |
| Changed description and changed experiment | Coordinates can change without changing the situation; changing the apparatus alone can alter its relation to the surroundings. |
| Strong restriction and remaining freedom | A direction, sign or balance can be established while the magnitude law remains unknown. |
| Idealized comparison and intended use | A conditional law family can guide work before all its physical premises have been resolved for an application. |

### PHY.4:4 - Solution

**Local mantra:** recover the physical situation; construct its transformations; justify the comparison; restrict the relation; retain its unknown part; use the consequence or revise the premise.

#### PHY.4:4.1 - Recover the participants and the relation being sought

Name what interacts, what is prepared, what can be exchanged and what response matters. Include surrounding bodies, material state, fields or boundaries when they can change that response. An omitted orientation or stored state may matter more than an additional numerical parameter.

Choose candidate quantities from that physical account. Explain how each quantity describes a participant, preparation or interaction. A.3.3.TR supports constructing a state that distinguishes different possible continuations; here the physical account supplies what retains and changes that state.

Decide what kind of relation is being proposed. An instantaneous mean response `y=F(x)` assumes that the chosen current inputs determine that mean. Memory, unresolved states or several possible responses can require a history, additional state, a probability law or a relation admitting several outputs. MMP.10 and MMP.11 express those mathematical choices after the physical conditions are identified.

Retain the status of the premises. A studied physical law, an idealization and a proposed hypothesis can all support reasoning, with different conditions on its use. Use the resulting conditional consequence when it already answers the present question.

#### PHY.4:4.2 - Construct the transformation of the situation

Describe what happens to every relevant participant and condition under the proposed change. If an apparatus is rotated, what happens to gravity, nearby surfaces, an applied field and its preparation? If two participants are exchanged, which material properties and connections move with them?

Separate two comparisons:

- **Changed coordinates:** the same physical situation is expressed with different components or labels. Transform every quantity representing that situation consistently.
- **Changed physical situation:** participants or conditions are changed. Explain which physical premise predicts corresponding behavior in the new situation.

For an isotropic material, all spatial directions are physically equivalent under the stated conditions. An oriented material can also be described in rotated coordinates; its material direction must then rotate in the description. These are different premises for restricting a response.

Select the actual transformation class. A justified rotation condition supplies rotation consequences. Reflection, time reversal, scaling or exchange requires its own physical grounds when used. PHY.1 supplies the detailed work for a scaling comparison.

A thought comparison can be enough. When a physical premise is unsettled, identify a rival case that could make the responses differ. C.11.DUA helps decide whether resolving that difference is worth the work needed now.

#### PHY.4:4.3 - Turn the comparison into a constraint on the unknown relation

Specify how inputs and responses transform. If x changes by T and y by U, a proposed response function has the comparison condition:

`F(T(x))=U(F(x))`.

For a reversible symmetry of a relation R, the corresponding condition is `R(x,y) iff R(T(x),U(y))`. This permits constraining an account before choosing a direction in which to solve it.

Derive the restriction. One useful move is to hold the input fixed under some allowed transformations. The output must then remain fixed under its corresponding transformations. Another is to compare inputs related by a transformation: a value chosen at one constrains the value at the other. MATH.13 develops these mathematical consequences once the physical action has been supplied.

For example, in three-dimensional space, rotations about a nonzero vector w leave w fixed. A vector response determined only by w and unchanged physical conditions must therefore lie along w: any perpendicular component would turn. Rotations between equal-length velocities then make the scalar coefficient depend only on their length. The physical work is establishing that no additional direction or state must also be supplied; :5.1 makes those assumptions explicit.

If a proposed input was held fixed even though the physical transformation changes it, restore that input and repeat the derivation. The anisotropic case in :5.2 shows how the changed argument opens additional response directions.

#### PHY.4:4.4 - Combine applicable dimensions, balances and dissipation

Use the physical restrictions relevant to the requested consequence:

- **Dimensions:** terms combined as one physical quantity need compatible units. Determine the dimensions of remaining coefficients and arguments. PHY.1 supplies dimensionless similarity groups when scale is part of the question.
- **Balance:** account for the relevant quantity retained, transferred, supplied or lost across the chosen boundary. A flux entering and leaving a region can differ when the region stores the quantity.
- **Dissipation or passivity:** identify the exchange whose sign is constrained and the regime in which the constraint holds. For an instantaneous passive resistive force at relative velocity w, the mechanical power condition is `F(w) dot w <= 0`.

Derive each condition at its stated scope. A storage element can temporarily return energy that it received earlier; its instantaneous power need not satisfy the memoryless resistance condition. Including storage changes the applicable balance and inequality.

Combine the constraints and examine whether any candidate remains. If they conflict, return to the assumptions or allowed class that caused the conflict. If they leave several laws, express the unresolved function, parameter or state dependence. Symmetry and dimensions often narrow a family without selecting one member.

#### PHY.4:4.5 - Obtain the needed consequence and choose the next use

Use the constraint for the original question. It may reject an impossible response direction, locate a missing input, restrict a learned or symbolic model, bound a consequence, or identify a condition under which competing laws disagree.

MMP.11 supplies a mathematical family respecting the physical constraints. When a quantitative value is needed, an interaction theory, interpreted observations or another appropriate method can constrain its remaining freedom. C.16.IR handles inference from interpreted indications; MMP.7 formulates a probability law for recorded data when the inference uses that form. C.29.2 supplies a computational formulation.

Choose further work from the unresolved consequence. A direction or family-wide bound may already suffice. If a missing magnitude changes the decision, obtain the needed contribution at a useful range and precision. A proposed experiment or simulation should discriminate something that matters to that next move.

When a changed situation gives a response outside the family, inspect the physical comparison before adding arbitrary terms. A preferred direction, external drive, stored state or different regime can change the family itself. Retain earlier consequences where their premises still hold.

### PHY.4:5 - Archetypal Grounding

These are constructed physical accounts. They illustrate how physical premises constrain an unknown law and how a changed premise changes the result.

#### PHY.4:5.1 - Restrict an unknown resistive force

Seek the instantaneous mean resistive force on a body moving through a homogeneous isotropic medium at a fixed material state, in a classical three-dimensional regime. Assume the body and preparation introduce no preferred direction, relevant memory is negligible, and relative velocity w is the only varying input. These assumptions define the proposed comparison; their adequacy in a particular experiment remains a physical question.

Rotating the entire relevant situation rotates w and the force together. Because there is no further directional input, `F(Qw)=QF(w)` for every spatial rotation Q. For nonzero w, rotations about w rule out a perpendicular force component. Equal-length velocities are related by rotation, so write:

`F(w)=-a(|w|^2)*w` for w different from zero.

At w=0, rotational symmetry gives `F(0)=0`. The coefficient a is an unknown scalar function at the fixed material conditions. Its dimension is mass divided by time. Memoryless passive resistance gives:

`F(w) dot w=-a(|w|^2)*|w|^2 <= 0`,

so `a(s)>=0` for s>0.

The result determines a direction and sign while leaving the speed dependence unresolved. Both `a(s)=a0` and `a(s)=b0*sqrt(s)` with suitable nonnegative dimensional constants satisfy these restrictions. They predict different force magnitudes when speed changes. The comparison alone therefore provides neither a linear nor a quadratic drag law.

For a direction-only question, use the result directly. To predict stopping time, supply further information about a over the speeds involved, or obtain a sufficient bound over the admissible family. MMP.11 keeps that unresolved relation visible instead of inserting a familiar drag coefficient.

#### PHY.4:5.2 - Add a physical direction

Now the body is oriented or the environment has an aligned surface. Include its unit direction n in the input. Under a rotation of the complete situation, both w and n change, so the condition becomes:

`F(Qw,Qn)=QF(w,n)`.

A rotation fixing w can now change n. The earlier argument that fixed all inputs while rotating a perpendicular output component is no longer available.

For example, one admissible linear resistive family is:

`F(w,n)=-alpha*w-beta*(n dot w)*n`.

For unit n, its power is `-alpha*|w|^2-beta*(n dot w)^2`. Resolving w into parts parallel and perpendicular to n shows passivity for every w when `alpha>=0` and `alpha+beta>=0`. This is a possible family, not an exhaustive determination of the changed law.

With consistent units, take alpha=1, beta=3, `w=(1,1,0)` and `n=(1,0,0)`. The force is `(-4,-1,0)` and power is -5. The force resists motion while pointing in a direction different from -w. This possibility is excluded by the earlier isotropic account and allowed by the additional physical input.

If n is fixed in the laboratory while only the body motion changes, retain that fixed n in the experiment's account. Rotating the coordinate system changes the components of both quantities; it supplies no premise that removes the material or environmental direction.

#### PHY.4:5.3 - Exchange two participants

Two identical chambers at the same temperature exchange one kind of particle through a symmetric passage. Let a and b be their current concentrations and let `J(a,b)` be the instantaneous mean transfer rate from the first chamber to the second. Assume the proposed regime needs no additional passage state, and the surroundings introduce no directional bias.

Keep the chamber labels and the positive counting direction fixed, and exchange the concentrations in the two preparations. Because the chambers and passage are symmetric and the surroundings supply no bias, this physical exchange predicts a reversed measured transfer rate:

`J(b,a)=-J(a,b)`.

At equal concentrations, `J(a,a)=0`. A proposed law `J(a,b)=k*(a-b)^2` with k>0 fails the interchange condition: it gives a positive rate in the same counted direction after the preparations are exchanged.

Both `J(a,b)=k1*(a-b)` and `J(a,b)=k3*(a-b)^3` satisfy the interchange condition when their constants have the corresponding units. Symmetry has not chosen between them or determined their coefficients. Directional thermodynamic claims would additionally use the physical driving potentials and the applicable dissipation law.

If the passage stores no particles, the chamber particle numbers satisfy `dN1/dt=-J` and `dN2/dt=J`, preserving their sum. If appreciable particles accumulate in the passage, include its particle number and separate inlet and outlet rates. The earlier two-chamber balance then omits a relevant participant.

This comparison uses exchange and balance rather than rotation. It opens the same kind of result: an admissible law family and the physical condition that would require revising it.

### PHY.4:6 - Bias-Annotation

A familiar formula can conceal a missing physical premise. An elegant symmetry argument can conceal the same omission. Recover the participants, preparation and surroundings before deciding which transformations the situation admits.

A conditional family is useful when its remaining freedom is stated. Supplying an unexplained familiar coefficient would replace an unresolved physical question with apparent precision. Obtain further information only for the consequence that needs it.

### PHY.4:7 - Conformance Checklist

For the restriction being used:

- The physical response or relation, participants, preparation and relevant surroundings are recoverable.
- The transformation states what changes and what remains physically comparable.
- The mathematical input and output transformations follow that physical account.
- Each dimensional, balance or dissipation constraint has applicable physical premises.
- The derived consequence distinguishes what is constrained from what remains unknown.
- The result changes a construction, interpretation, prediction or next inquiry.
- A changed physical condition returns to the affected premise and constraint.

### PHY.4:8 - Common Anti-Patterns and How to Avoid Them

**Dropping the surroundings from the transformation.** Rotating a body relative to a fixed material direction can change its response. Transform the complete relevant account and distinguish that experiment from a coordinate change.

**Selecting a magnitude law from direction symmetry.** The linear and quadratic resistance possibilities in :5.1 satisfy the same directional restriction. Carry the unknown scalar function until a further physical contribution constrains it.

**Applying an instantaneous dissipation inequality to an energy-storing interaction.** Recover stored energy and the exchange balance. Temporary return of stored energy changes the instantaneous power without establishing an active energy source.

**Using a balance with an omitted participant.** Accumulation in the passage changes the two-chamber balance in :5.3. Include the storage and its exchanges before computing the chamber changes.

### PHY.4:9 - Consequences

Useful physical restrictions become available before a complete mechanism or fitted law is known. They can guide formulation, reject an incompatible model or direct a discriminating inquiry. The remaining freedom also becomes a specific task rather than an implicit assumption.

The result is conditional on the physical comparison. An added direction, stored state or changed regime can reopen the law family. This makes the dependence of the conclusion inspectable and supports retaining the portions that still apply.

### PHY.4:10 - Architectural Rationale

The physical construction precedes the mathematical symmetry calculation. MATH.13 can derive what a supplied transformation preserves; the present method supplies and criticizes the physical grounds for choosing that transformation and its inputs.

The unknown relation remains explicit through the work. This supports relational formulations as well as response functions, and allows later symbolic, numerical or learned models to use the same physical restrictions.

Similarity, analogy and performance bounds remain separately usable methods. Their results may settle the physical question directly. When a law is still missing, this method constrains its form and identifies the remaining contribution without requiring a detailed mechanism first.

### PHY.4:11 - SoTA-Echoing

Feynman's [discussion of symmetry in physical laws](https://www.feynmanlectures.caltech.edu/I_52.html), especially §52-2, is a historical methodological anchor for transforming an experiment together with its relevant surroundings. The adopted contribution is the physical construction of the comparison. The particular transformation and its regime are selected from the physical account being used.

Villar and colleagues' [Scalars are universal](https://arxiv.org/html/2106.06610v4), Proposition 4 and Appendix H, provides a contemporary constructive connection between specified symmetry actions, scalar invariants and equivariant response families. Its distinctions between rotation and reflection groups and between different input quantities matter when selecting a model. The paper's mathematical representation results are used under their hypotheses; the present physical method establishes which input and transformation account is appropriate.

When formulating an unfamiliar interaction law, a common alternative is to select a familiar constitutive formula and fit its coefficients. With only the physical premises in :5.1, that choice would insert a speed dependence the premises do not determine. The transformation method in :4.2-:4.4 first establishes the allowed direction and sign, leaving the scalar function open. For a direction-only question, this supplies the needed answer without obtaining a detailed law or fitting its coefficients. For a stopping-time prediction, :4.5 requires further information about that function or a sufficient bound; the restriction alone leaves the prediction unresolved.

An established constitutive account or reliable analogue is preferable when it applies to the intended regime and supplies the needed consequence with less work. The present method then helps inspect its physical assumptions or a proposed change of conditions. Reopen this choice when a new physical input or regime invalidates the comparison, an improved account changes its grounds or offers an easier answer, or the receiving question requires information that the constrained family leaves open.

### PHY.4:12 - Relations

- **PHY.1** constructs physical similarity and scale-dependent comparisons.
- **PHY.2** constructs a physical analogue or proposed mechanism from interactions.
- **PHY.3** derives a physical performance limit from the permitted transformations.
- **MATH.13** derives mathematical consequences of a supplied symmetry.
- **MMP.10 and MMP.11** formulate compatible conditions and relations with unresolved dependence.
- **A.3.3.TR** supplies common state and joint-change construction.
- **C.29.1, C.29.2 and C.29.3** connect correspondence, computational formulation and physical realization.
- **C.16.IR and MMP.7** support interpreted indications and the probability law used for recorded observations.
- **C.11.DUA** compares the value and effort of resolving a remaining physical question.

### PHY.4:End

## PHY.5 - Choose an Effective Physical Description by Scales and Couplings

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.5:1 - Problem frame

Use this pattern when a physical question leaves you uncertain which motions, interactions or material details its description must retain. Resolving every microscopic change may be impractical. Omitting a fast motion or a small interaction may change the answer that matters.

Begin with one consequence: a response over a stated interval, a propagation speed, an accumulated exchange, or a distribution of outcomes. Choose one proposed omission and follow how it could affect that consequence. A simpler account with a justified range of use, or a reason to restore the omitted contribution, is a useful first result.

An *effective physical description* here describes the physical behavior needed at chosen scales without resolving every underlying process. Unresolved processes can still contribute through response coefficients, constraints, dependence on earlier states or fluctuations. The method helps choose and examine that description across physical branches.

You need to identify the physical participants, explain the interactions relevant to the question and compare their characteristic sizes or rates. A qualitative separation can direct the next construction. The examples add their own mathematical preparation: elementary differential equations for the motor, waves for the discrete chain, and covariance for thermal motion.

When a known physical account already answers the question under the intended conditions, use it. PHY.1 supplies similarity between changed arrangements; PHY.2 constructs an analogue from physical interactions. MMP.9 supplies mathematical reduction once the governing relations and retained quantities have been chosen. Use this pattern for the physical choice of those quantities, relations and conditions.

### PHY.5:2 - Problem

A detailed account can obscure the mechanism that determines a response. A convenient coarse account can erase the same mechanism. The relevant distinction depends on the question: a description may preserve a mean displacement while losing its spread, or preserve slow motion while losing an initial torque.

A comparison of isolated time scales also misses how parts interact. A rapidly adjusting part can exert a sustained force. Unresolved molecular motion can produce both drag and continuing fluctuations. A small length can become consequential when the imposed variation approaches that length.

The task is to retain the physical influence required by the intended result, while choosing how much of its underlying process to describe.

### PHY.5:3 - Forces

| Force | Tension |
| --- | --- |
| Resolution and usable explanation | More resolved variables can expose a mechanism while making the relevant consequence harder to obtain. |
| Scale separation and coupling | A fast process can relax quickly yet continue to alter the slow behavior through its response. |
| Mean response and variability | An average can settle one question while missing fluctuations that determine another. |
| Local approximation and changed conditions | A useful omission can fail at a boundary, during preparation or after the work changes the forcing. |
| Available grounds and further inquiry | Existing laws and bounds may settle the choice; an unresolved physical premise can sometimes justify a targeted comparison. |

### PHY.5:4 - Solution

**Choose the consequence → locate its physical influences → compare their scales in the coupled situation → retain the needed effects of unresolved processes → test the resulting answer → use it or restore the consequential difference.**

#### PHY.5:4.1 - Choose the physical consequence and its resolution

State what the answer will let someone interpret, choose or do. Identify the relevant quantity and how it is used: an instantaneous value, a time integral, a spatial average, a peak, a correlation or a probability can require different descriptions of the same situation.

Include the preparation, forcing, spatial range and observation interval when they affect that answer. For example, the first moment after switching can include a motion that has already decayed when a later reading is taken. A question about a wave's arrival concerns a propagating disturbance and the wavelengths present in it.

Use the working question to choose adequate resolution. If a bound already determines the choice, recovering a detailed trajectory may add nothing to that choice. C.11.DUA helps when the value of further inquiry is uncertain. B.5.MPC connects the mathematical result and its conditions to the physical question.

#### PHY.5:4.2 - Locate the interactions and compare their scales

Follow the influence from preparation or input to the consequence. Identify what stores, transports, exchanges or dissipates the quantities involved. Include a boundary, contact, surrounding medium or measuring interaction when it carries an influence on that consequence.

Obtain the governing physical relations at the detail needed for this comparison. A studied theory, measured response or working hypothesis can supply them; retain which of these is being used. PHY.4 helps constrain an unresolved law. MMP.11 constructs its remaining mathematical family.

Derive characteristic sizes or rates from these relations and the proposed regime. Compare contributions to the same physical change. For time scales, compare relaxation with the fastest relevant forcing and with the interval of use. For spatial scales, compare a variation length with the scale of material structure or transport. An energy comparison may determine which states can be appreciably excited.

Inspect the coupled arrangement. A coupling can change a relaxation rate or create a collective mode. For a proposed rapidly adjusting state, ask whether small departures from its proposed response actually decay while the retained variables change. A response near loss of stability can become slow even though one component, considered alone, relaxes rapidly.

Scaling the equations as in PHY.1 makes these comparisons explicit. Keep the physical reason for each scale: a narrow gap, driving period or relaxation distance can matter more than the size of the whole apparatus.

#### PHY.5:4.3 - Choose how unresolved processes enter the retained account

Select the variables and interactions needed by the consequence. They may describe individual participants or collective quantities such as a displacement field, concentration or slowly changing amplitude.

For a part that adjusts rapidly, first determine what it adjusts *to*. Substitute that response into its coupling with the retained part. The resulting force, constraint or transport remains in the effective account. In the motor example, eliminating rapidly changing current retains its effect on torque and damping.

For a collection of unresolved processes, determine which of their effects remain:

- a mean response changes the retained forces or transport coefficients;
- a delayed response makes current change depend on earlier states;
- fluctuations produce a spread of possible changes around a mean response;
- a persistent unresolved mode may require another retained state.

Choose among these from the physical preparation and interactions. Eliminating variables mathematically can expose a memory term even in deterministic dynamics. A statistical description additionally needs grounds for the distribution of unresolved states. MMP.7 supplies probability composition for a specified information and recording situation; it does not choose the physical preparation.

An effective coefficient can be obtained from a more detailed description, existing measurements or a constrained response law. Compare the predicted quantity in a regime where the two descriptions apply and choose the coefficient to preserve that contribution. This matching can be useful even when no complete microscopic theory is available. Carry the range and remaining uncertainty that change its later use.

#### PHY.5:4.4 - Construct the approximation and its first omitted contribution

Use MMP.9 for the mathematical elimination or retained-state evolution. Keep the physical assumptions that permit the construction alongside its result.

For a rapidly relaxing state, examine its initial departure and response to changing inputs. Replacing it by a steady response is useful when the remaining departure has sufficiently little effect on the requested consequence. The motor calculation below derives that departure instead of assigning it zero at the initial instant.

For a spatial or energy expansion, choose the ratio in which the description is expanded and compare the first omitted contribution with the retained ones. The ratio and its powers come from the physical relations. In the chain example, expansion in the small ratio of lattice spacing a to wavelength lambda, or equivalently in `q*a=2*pi*a/lambda`, yields a continuum wave description and its leading correction.

When unresolved correlations persist over the interval of interest, retain their delayed influence or add variables that reproduce it. Replacing a delayed response by an instantaneous one needs a comparison of that response time with the retained motion and driving. A mathematically equivalent auxiliary state is another way to calculate the memory; its interpretation as a material component requires a separate physical account.

Maintain the relevant exchanges and constraints through the approximation. Recover the condition for a balance or an allowed motion when changing the variables or boundaries. C.29.BB supplies the common balance construction.

#### PHY.5:4.5 - Judge the influence on the requested answer

Follow the approximation through to the actual output. A small state error can grow under differentiation, accumulation, feedback or a sensitive later choice. MATH.20 supplies bounds. If the consequence is obtained in another mathematical account, C.29.1 establishes what transfers between the accounts.

Examine conditions suggested by the construction itself. An omitted initial transient matters when the reading moves into it. A spatial approximation becomes suspect when the wavelength approaches the unresolved structure. A weak loss can determine a resonant response. A nearly unstable mode can defeat the earlier time-scale separation. Use the conditions that affect the proposed account.

For a statistical description, compare the statistic the work uses. Preserving an average response need not preserve a variance or a transition probability. In thermal motion, eliminating velocity while retaining random forcing can preserve long-time displacement statistics. Deleting that forcing gives a different result.

A derivation, an existing limiting result or a suitable comparison can settle the choice. If a physical premise remains unresolved, identify a feasible change of preparation or readout for which the plausible accounts give different useful answers. Obtain that comparison when its possible outcomes warrant the effort. A conditional physical conclusion can remain useful while a stronger claim is unresolved.

#### PHY.5:4.6 - Use the account and reopen the affected physical choice

Return the answer with the conditions needed to use it. These may be expressed in a short derivation, an annotated model or an ordinary explanation.

Choose what the work now permits: use the simpler computation, interpret a measurement, change a drive, retain a fluctuation model, or restore an interaction. If several accounts provide complementary consequences, retain their respective uses. When a choice among available descriptions matters, C.11 supplies the comparison, including whether more inquiry is worth its cost. Use G.5 when the retained set itself must be stated: distinguish alternatives for later choice from descriptions used together for a named result. E.23 supports improvement when the chosen characteristics can judge a change.

For a new question or failed prediction, return to the influence whose omission is implicated. Change the physical variables, coupling, preparation or range, then redo the affected reduction and interpretation. B.5.MPC.R helps separate a physical-account failure from a mathematical or computational one.

The result can also change the method of work. A team may calculate a slow response with one model and delegate a short transient to another. ME.7 describes those contributions and their joins; ME.12 examines the claims needed for the combination. Each result retains the physical conditions that make it usable by the next participant.

### PHY.5:5 - Archetypal Grounding

#### PHY.5:5.1 - Keep a motor's torque while eliminating fast current dynamics

Consider an ideal linear motor over a range in which resistance R, inductance L, inertia J, damping b and conversion constant k are positive and constant. In consistent SI units, use the same k for torque per current and back voltage per angular speed:

`L*i' = V - R*i - k*omega`

`J*omega' = k*i - b*omega`

The electrical and mechanical balances describe the assumed device, including its load in J and b. Saturation, variable load or a different drive would require the corresponding physical relations.

Suppose the work needs the slow speed response. The electrical relaxation time is `tau=L/R`. The current toward which the electrical part relaxes is `q(t)=(V(t)-k*omega(t))/R`. Replacing i by q gives

`J*omega' = (k/R)*V - (b+k^2/R)*omega.`

The eliminated current still supplies driving torque and additional damping. The slow response time of this candidate is `J/(b+k^2/R)`. Compare tau with that time and the drive's variation time.

To examine the neglected response, set `e=i-q`. The full electrical equation gives `tau*e'=-e-tau*q'`. If `|q'|<=K` on the interval, integration yields

`|e(t)| <= |e(0)|*exp(-t/tau) + tau*K*(1-exp(-t/tau)).`

The bound on q' can come from `|q'|<=(|V'|+k*|omega'|)/R` and the allowed drive and acceleration, using the full physical account where needed. A bound inferred only by assuming the proposed approximation would leave that assumption unresolved.

For example, let R=2 ohms, L=0.02 henry, k=0.1 in the stated SI convention, J=0.02 kg m² and b=0.01 N m s per radian. Then tau=0.01 s and the candidate slow time is about 1.33 s. With `|e(0)|<=0.5` ampere and K=1 ampere per second, the current departure at 0.05 s is at most 0.01331 ampere, giving a torque departure at that instant of at most 0.001331 N m relative to kq.

The slow speed error is a different output. With the same initial speed and drive, let delta be full speed minus reduced speed. It satisfies

`J*delta' + (b+k^2/R)*delta = k*e.`

Let `B(s)` denote the current-departure bound above. Since the initial speed difference is zero and the response kernel is positive, integration gives

`|delta(t)| <= (k/J)*integral_0^t exp(-(b+k^2/R)*(t-s)/J)*B(s) ds.`

For the stated values, this speed-departure bound at 0.05 s is about 0.026064 rad/s, hence less than 0.02607 rad/s. An allowed error of 0.03 rad/s therefore permits the reduced calculation for that speed reading. The integral carries the earlier transient into the answer; the small current departure at the final instant alone would not give this bound.

**Changed work.** If the next question concerns torque immediately after switching, the bound includes the initial current departure. Use the electrical transient. If the drive varies on the electrical relaxation time, recompute its departure instead of extending the slow-drive approximation. These returns change which physical response is retained.

#### PHY.5:5.2 - Decide when a chain can be treated as a continuous medium

Consider an infinite ideal one-dimensional chain with identical masses m, spacing a and linear springs of stiffness kappa. Each mass moves a small distance u_j from its reference position. The balance is

`m*u_j'' = kappa*(u_(j+1)-2*u_j+u_(j-1)).`

For waves with wavenumber q in `0<q*a<pi`, substitution of a sinusoidal wave gives

`omega^2 = (4*kappa/m)*sin^2(q*a/2).`

For wavelengths long compared with a, expanding the neighboring displacements gives the continuum equation `u_tt=c^2*u_xx` with `c=a*sqrt(kappa/m)`. It predicts both phase and group speed c. The chain's phase speed divided by c is `sin(q*a/2)/(q*a/2)`; its group speed divided by c is `cos(q*a/2)`. Expanding those ratios gives `v_phase/c = 1-(q*a)^2/24+O((q*a)^4)` and `v_group/c = 1-(q*a)^2/8+O((q*a)^4)`, exposing their different first corrections.

At q*a=0.2 these ratios are about 0.99833 and 0.99500. A half-percent allowance for these speeds accommodates this ideal comparison, subject to the question's waveform and other physical premises. The group-speed difference is already larger than the phase-speed difference.

**Changed work.** A disturbance containing wavelengths near the shortest traveling waves of the chain probes q*a near pi. The chain's group speed tends to zero, while the continuum account keeps c. A question about that disturbance's propagation requires retaining the discrete dispersion or an adequate extension. Making the computation of the uncorrected continuum equation more accurate cannot recover the omitted physical dependence.

This case concerns an ideal linear chain. It demonstrates choosing spatial resolution from the wave that matters. It supplies no claim that every material, boundary or large deformation obeys the same chain law.

#### PHY.5:5.3 - Retain fluctuations after fast velocity has relaxed

For a one-dimensional Brownian particle in a uniform equilibrium bath, take mass m, drag coefficient gamma and temperature T, with no applied force. The underdamped account has position x, velocity v and thermal forcing. Let `tau=m/gamma` and `D=k_B*T/gamma`. With an initially equilibrated velocity, its velocity covariance is `(k_B*T/m)*exp(-|t-s|/tau)`.

Integrating that covariance over the two times gives

`E[(x(t)-x(0))^2] = 2*D*(t-tau*(1-exp(-t/tau))).`

At times large compared with tau, the overdamped diffusion description gives `2*D*t`. Its omitted contribution to this mean-square displacement is bounded by `2*D*tau`. This calculation states which long-time consequence the reduction preserves.

Setting the mean velocity to zero and deleting the forcing instead gives no displacement spread. The unresolved bath continues to transfer random impulses after the velocity's preparation has relaxed. For the displacement distribution, retain their diffusion effect.

**Changed work.** Change the bath to a spatially varying temperature and ask about entropy production. The uniform-bath calculation no longer answers the question. Celani and coauthors show a further distinction: under their smooth-temperature and small-inertia conditions, the overdamped position process has the appropriate limit, while the mean rate of entropy production retains an additional positive contribution absent from the naive overdamped expression. Return to the thermodynamic observable and its limiting calculation. Position accuracy alone cannot decide that use. Their [2012 paper](https://arxiv.org/html/1206.1742v2) states the preparation and the contribution.

### PHY.5:6 - Bias-Annotation

The worked calculations emphasize classical continuous-time descriptions with explicit laws. The method also applies to choosing physical states and interactions when only a constrained response or statistical account is available. In such cases the first result can be a qualified regime choice or a discriminating physical question.

Time-scale separation is especially convenient and can dominate the choice too early. The spatial chain and changed thermodynamic observable show other reasons to retain a contribution. Quantum coherence, rare transitions and collective behavior require their own physical grounds; the classical examples do not decide them.

### PHY.5:7 - Conformance Checklist

- The intended consequence specifies the physical quantity, relevant preparation, range and interval.
- The comparison uses the coupled physical arrangement and explains the characteristic scales.
- Each omitted process retains any mean response, constraint, delayed influence or fluctuation needed by that consequence.
- The approximation follows from stated physical relations or remains an identified hypothesis.
- A bound or comparison reaches the actual requested output, including a relevant initial or boundary contribution.
- A changed condition that can defeat the selected description leads back to the implicated physical choice.
- Existing results are used when sufficient; further inquiry is selected for what it could change.

### PHY.5:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the construction | Consequence | Repair |
| --- | --- | --- |
| Delete a fast part and its coupling together | The motor loses the torque and damping supplied by its adjusting current. | Substitute the part's response into the retained interaction. |
| Apply the settled response at every instant | The initial current and switching response disappear. | Carry the transient and propagate its effect into the requested output. |
| Match one propagation speed and assume the other matches | A continuum approximation can misstate the arrival of a wave packet. | Compare the dispersion and the output the disturbance uses. |
| Replace unresolved motion by its mean | The Brownian particle loses its displacement spread. | Retain the fluctuation contribution when the question uses that distribution. |
| Use a successful position reduction for a thermodynamic observable | A limiting position process can omit entropy production. | Reduce the observable and its physical exchanges with the dynamics. |

### PHY.5:9 - Consequences

A useful effective account makes a physical mechanism easier to reason about and calculate with. Its stated regime supports a targeted return when the forcing, observation or intended action changes.

The choice costs physical analysis and sometimes a comparison with a richer account. It saves work when those results permit a cheaper calculation or a clearer explanation. A range without adequate scale separation can require a coupled, memory-bearing or more resolved description.

### PHY.5:10 - Architectural Rationale

This method organizes the choice by physical consequence and coupling. Comparing parameter sizes alone would miss how an omitted process enters the result. Starting from the most detailed available theory can impose work that the question does not need.

Effective-theory construction supplies a useful way to retain selected influences and improve an approximation systematically. Projection and coarse-graining show why unresolved motion can remain as memory and fluctuations. The observable-specific limit shows why their adequacy is judged at the receiving physical result.

MMP.9 owns the mathematical elimination; PHY.1 uses an effective account to compare changed physical arrangements; PHY.2 uses it when constructing an analogue. The contribution here is choosing and revising the physical resolution and remaining influence of unresolved processes. The motor, chain and Brownian particle demonstrate that contribution in different comparisons.

### PHY.5:11 - SoTA-Echoing

[Stewart's introduction to effective field theory](https://ocw.mit.edu/courses/8-851-effective-field-theory-spring-2013/e4ebfd74257683c3efa47b240196c505_WB8r7CU7clk.pdf) (MIT, 2013, lecture transcript pp. 2-4) is a historical teaching source for selecting relevant degrees of freedom, scales and an improvable leading description. This pattern adapts that construction beyond its quantum-field setting. It retains the need to identify an expansion and its range; improvement by further terms remains conditional on that expansion being useful.

[Dalton and coauthors, Memory and Friction: From the Nanoscale to the Macroscale](https://doi.org/10.1146/annurev-physchem-082423-031037) (2025; [accessible manuscript, section 3](https://arxiv.org/html/2410.22588v1)) supplies the contemporary account of retained observables, memory-dependent friction and simulation through auxiliary variables. Adopt the distinction between eliminating explicit variables and discarding their influence. An instantaneous response saves computation when its conditions hold; resolved memory preserves effects that such a response misses. The review's stated projection, equilibrium and preparation conditions govern its particular equations.

[Celani, Bo, Eichhorn and Aurell](https://arxiv.org/abs/1206.1742) (2012) provide the observable-specific counterexample used in :5.3. Adopt the comparison of the physical result before and after the limit. Their thermal-gradient result qualifies an otherwise successful position reduction; it does not rule out overdamped modeling for the position questions it answers.

The synthesis combines controlled omission, retained coupling and use-specific comparison. It favors the least costly description that supplies the needed consequence under the established physical conditions. Memory kernels, white-noise diffusion and a fully resolved model are alternative constructions with different requirements, selected by the question.

### PHY.5:12 - Relations

- **B.5.TU and PHY.4:** supply application of a physical theory and constraints on an unresolved law.
- **A.3.3.TR and C.29.BB:** supply common state, interaction and balance constructions used by the physical account.
- **MMP.9:** supplies elimination and reduced evolution; **MMP.7/.11** supply probability composition and constrained response families.
- **MATH.20** bounds the unresolved contribution; **C.29.1** establishes transfer of a bound or consequence between mathematical accounts.
- **PHY.1/.2/.3:** use the chosen description in similarity, analogue construction and physical limits.
- **C.11.DUA and C.11:** examine the value of further inquiry and choose among available descriptions.
- **G.5 and E.23:** state retained alternatives or jointly used descriptions when needed, and guide improvement by the chosen characteristics.
- **B.5.MPC.R and ME.7/.12:** return to a failed contribution and revise the method that uses the physical result.

### PHY.5:End

## PHY.6 - Construct Physical Evolution from Balances and Response Laws

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.6:1 - Problem frame

Use this pattern when you can identify physical participants and their interactions, but cannot yet say how their coupled situation will evolve. You may know what is conserved while lacking the law that determines an exchange rate. You may have equations for each part while their connection or initial preparation remains inconsistent.

Start with the consequence you need: an initial response, a trajectory, a transported amount, a settled state or a distribution of outcomes. Choose the participants, exchanges and response laws needed for that consequence. A usable first result is a coupled physical description from which the consequence follows, or an identified missing response or incompatible condition that tells you what to resolve next.

Here a *response law* relates a physical interaction or change to the conditions on which it depends. A constitutive law is one such relation for a material or component. The method constructs an account from physical balances, response laws and preparation; it works across physical branches.

You need to identify the physical quantities and interpret the proposed relations and their conditions. The worked cases add their own preparation: elementary motion and energy calculations, a spatial continuity equation, and charge storage. These are different demonstrations of the same construction.

If a known physical account already supplies the required result, use it. If a balance alone settles the question, stop there. C.29.BB supplies that general balance method. Use PHY.5 when choosing which physical detail to retain; use this pattern when assembling the retained physical relations. Once that account is settled, MMP.10 and C.29.2 help formulate and obtain its mathematical consequences.

### PHY.6:2 - Problem

A balance says how accumulation relates to transfer and production. It can leave the transfer itself unknown. Adding a convenient rate formula may complete an equation system while describing the wrong physical interaction.

Combining individually useful descriptions adds another difficulty. A contact may store a quantity, a connection may impose a constraint, and two parts may use different signs or reference frames. Initial values acceptable to each isolated part can be impossible after they are connected. A solver can then fail for a physical reason, or return a result for a preparation different from the intended one.

The task is to construct mutually compatible physical relations and preparation, then derive the consequence that the work needs.

### PHY.6:3 - Forces

| Force | Tension |
| --- | --- |
| General balance and particular response | Conservation restricts change; material and interaction laws determine much of the remaining behavior. |
| Reusable parts and coupled behavior | A part's relation can remain useful while its boundary conditions change when connected. |
| Ideal connection and physical preparation | An ideal constraint can simplify later evolution while excluding the supplied initial state. |
| Physical detail and sufficient answer | A total or a bound may answer the question even when a detailed trajectory remains undetermined. |
| Available grounds and conditional use | An established response supports a stronger physical claim than an untested working hypothesis, while both can support useful conditional reasoning. |

### PHY.6:4 - Solution

**Choose the consequence → identify participants and exchanges → supply response laws → connect the relations → make the preparation consistent → derive and use the needed consequence.**

#### PHY.6:4.1 - Choose the consequence and physical participants

State what the answer will let someone interpret, choose or do. Identify the quantity, interval and preparation that matter. A peak response, a total transferred amount and a settled value can require different accounts of the same arrangement.

Choose the physical participants and their boundaries at a useful resolution. Locate the interactions that can affect the answer, including supports, surrounding media and measurement when relevant. Distinguish a quantity stored in a participant from a quantity passing through its boundary. Include storage in a contact or field when omitting it would change the consequence.

Use PHY.5 to resolve a consequential choice of scale or omitted interaction. A spatial field, a few aggregate variables and individual particles are possible descriptions; their physical adequacy depends on the question and regime.

#### PHY.6:4.2 - Construct the balances with physical meanings

Use C.29.BB to choose the additive quantity, common interval, signs, transfers and internal production. Write each term with its physical meaning and compatible units. For vector quantities, use a common frame or an explicit transformation between frames.

For a fixed spatial region, a useful form is

`rate of stored quantity = inward transfer - outward transfer + internal production.`

A local continuity equation expresses the same relation for a density and its flux. The choice of quantity determines the production term: a chemical species can be consumed while the atoms it contains remain in reaction products. A closed boundary alone does not make every selected quantity constant.

Identify which terms remain undetermined. A momentum balance may still need forces; a species balance may need transport and reaction rates. If the requested total already follows without those details, retain that consequence and avoid completing an unnecessary model.

#### PHY.6:4.3 - Supply the response and configuration relations

For each unresolved interaction that affects the answer, state how its response depends on the physical conditions. Use an applicable theory, an established material response, an available measurement or a stated working hypothesis. PHY.4 helps constrain a law whose form is unknown; MMP.11 helps represent its remaining freedom.

Recover the conditions under which the relation is used. Does it describe the current state, dependence on earlier states, a spatial gradient, an average response or fluctuations? Does it assume a settled contact, a constant material parameter or a particular preparation? Supply the configuration relations needed to connect that response to the retained variables.

Keep physical restrictions that the chosen description relies on. A passive damping law transfers mechanical energy into other forms; it does not destroy total energy. If that heating changes the response during the intended use, include the resulting dependence. A fitted or learned response can also supply a relation, but its physical restrictions and usable range must come from its construction or grounds, not from the fact that it produces numbers.

When several physically plausible laws remain, derive what each changes in the requested consequence. A bound or a conditional answer may be sufficient. Seek another observation or a more detailed account when its possible result can change the work; C.11.DUA helps decide that inquiry.

#### PHY.6:4.4 - Connect the physical relations before choosing a solving order

State what a connection makes common and what it transfers. Match quantities, units, frames and orientations at that connection. Equal values require a physical reason: two locations in contact can still have a finite resistance or an intervening store. If the connection has its own consequential dynamics, describe those dynamics.

Combine the part balances through the common transfer. Transfers internal to the combined boundary cancel when they describe the same exchange over the same interval. Retain conversions between quantities and energy forms. For an energetic connection, derive its power expression from the physical variables; variable names such as *potential* and *flow* alone do not establish their product as power.

Keep the equations as simultaneous relations while constructing the physical account. They can include derivatives, algebraic constraints, spatial dependence or statistical response. In a differential-algebraic description, some relations constrain values while others describe change. Which variable is solved for is a later mathematical or computational choice; changing that order need not change the physical interaction.

Eliminate a variable only while retaining the relation or reconstruction needed by later use. MMP.9 supplies mathematical reduction and MMP.10 supplies a formulation for the chosen analysis. If two parts disagree at their connection, return to their quantity meanings and physical assumptions before changing a solver.

#### PHY.6:4.5 - Make the preparation compatible with the connected account

Supply the independent initial, boundary and driving conditions needed by the requested evolution. Substitute the proposed preparation into the connected relations. Solve for dependent initial values and reactions. Preserve the difference between a physical initial condition and a numerical starting guess.

A motion constraint also constrains admissible initial velocity. An electrical connection can constrain initial potentials. A spatial description needs boundary conditions appropriate to its transport and response. Determine which conditions can be chosen freely and which follow from the others.

An equation count can expose an omitted relation, but equal counts do not establish a consistent or uniquely determined problem. Examine the dependence of the actual relations and the existence conditions needed for the intended result. C.29.2 supplies the subsequent computational formulation; a solver diagnostic can help locate a problem without deciding whether the physical preparation should change.

If the preparation is incompatible, identify the conflict and its physical alternatives. Correct a mistaken initial value, relax an unjustified ideal constraint, or describe the interaction that establishes the new state. Choose among these from the actual preparation. Do not silently substitute an easier initial state.

#### PHY.6:4.6 - Derive the consequence and return through the implicated premise

Obtain the first result at the resolution the question needs. This may be an initial derivative, an integrated balance, a limiting state or a computed evolution. B.5.MPC connects the mathematical result and its conditions to the physical question.

Use checks that can distinguish a wrong construction for this use. Combining part balances can expose a duplicated exchange; an energy calculation can expose a sign error or an omitted conversion; substituting the preparation can expose an impossible constraint. A limiting case or available observation can test a disputed physical premise. Passing one such check establishes only what it examines.

Distinguish a consequence of the stated equations from evidence that those equations describe the intended situation. Numerical accuracy concerns how the chosen consequence was obtained. Physical adequacy concerns the premises, preparation and interactions represented. Keep those qualifications with the result, without requiring new evidence when the conditional result already serves the work.

When the question, preparation or connection changes, revisit the affected relations. Retain contributions whose conditions still hold. An unresolved exchange law directs work to physical theory or response characterization; inconsistent coupled quantities direct work to the connection; an adequate account with an inaccurate computed result directs work to the computation. B.5.MPC.R supplies the broader repair when physical, mathematical and computational contributions need to change together.

### PHY.6:5 - Archetypal Grounding

#### PHY.6:5.1 - Derive coupled motion and identify where mechanical energy goes

Two bodies move along one line. Their masses are `m1` and `m2`. Displacements `x1` and `x2` are measured from a configuration in which their connecting spring is unstretched, so its extension is `x2-x1`. Velocities are `v1` and `v2`. A spring and a viscous damper act between them; the connector's inertia is neglected in the chosen regime.

The momentum balances need the connecting force. Use the ideal response

`f = k*(x2-x1) + c*(v2-v1)`,

where `k>0` is stiffness and `c>=0` is damping. The force on body 1 is `f`; that on body 2 is `-f`.

**When a response parameter is missing.** Suppose this linear response form is already justified, but its parameters are not yet supplied. A static test with extension `1 m`, zero relative velocity and force `3 N` determines `k=3 N/m`; it leaves c undetermined. At extension `1 m` and relative velocity `-2 m/s`, the choices `c=0` and `c=0.5 N*s/m` predict `3 N` and `2 N`. Both reproduce the static test. A prediction of either body's acceleration therefore remains conditional on c; a supplied value or useful bound can settle a stronger question. A question about total momentum change can already be answered from the external forces, independently of c. The single test does not establish the assumed linear form.

With the response parameters and external forces `u1` and `u2` supplied, the connected evolution is

`x1' = v1;  x2' = v2;  m1*v1' = f+u1;  m2*v2' = -f+u2.`

Adding the momentum balances gives `p' = u1+u2` for `p=m1*v1+m2*v2`. This removes the internal force from the total momentum change while retaining it in the relative motion.

The retained mechanical energy is

`H = (m1*v1^2 + m2*v2^2 + k*(x2-x1)^2)/2.`

Differentiating and substituting the evolution gives

`H' = u1*v1 + u2*v2 - c*(v2-v1)^2.`

For the ideal damper whose lost mechanical energy becomes internal energy `U`, add `U' = c*(v2-v1)^2`. Then `(H+U)'` equals the external mechanical power. Omitting `U` from the motion calculation assumes that its change does not appreciably alter the chosen mechanical response.

Take `m1=1 kg`, `m2=2 kg`, `k=3 N/m`, `c=0.5 N*s/m`, `x1=0 m`, `x2=1 m`, `v1=1 m/s`, `v2=-1 m/s`, and no external force. At that instant, `f=2 N`, the accelerations are `2 m/s^2` and `-1 m/s^2`, total momentum has zero rate of change, and mechanical energy decreases at `2 W`. These are useful initial consequences without computing a full trajectory.

**Changed preparation.** Body 2 is instead held at `x2=1 m` from before the initial instant, so `v2=0`. With the other initial values unchanged, `f=2.5 N`. The support supplies the reaction `u2=f`; body 1 accelerates at `2.5 m/s^2`. The selected pair now exchanges momentum with the support. Keeping the earlier `v2=-1 m/s` together with a fixed-position constraint would describe an inconsistent preparation. Suddenly clamping the moving body would be another physical problem, requiring an account of that transition.

The reusable move is to obtain motion by joining balances to a response and preparation, and to revise the relevant exchange when the connection changes.

#### PHY.6:5.2 - Obtain a total without solving its spatial distribution

Let `c(x,t)` be the concentration of one chemical species in a fixed region. Its prescribed velocity field is `u(x,t)`. Use diffusion coefficient `D>0`, a constant first-order consumption rate `k>=0`, and the flux law

`J = c*u - D*grad(c)`.

The species balance supplies

`partial_t(c) = -div(J) - k*c.`

These equations state the response assumptions: advection, Fickian diffusion and first-order conversion. Their applicability is a physical premise. Impose no flux of this species through the region's boundary, `J dot n = 0`, where `n` is the outward normal.

For the total amount `N(t)=integral_region c(x,t) dx`, integration of the balance gives

`N' = -integral_boundary J dot n dS - k*N = -k*N`,

and therefore `N(t)=N(0)*exp(-k*t)`. The requested total follows from its initial total and the stated boundary and reaction laws. Internal transport need not be solved. Consumption of this species can coexist with conservation of the atoms it transfers into products.

**Changed question.** A local concentration maximum requires the initial spatial distribution and its evolution. The total alone no longer answers. Alternatively, if the reaction rate varies with position, the total rate becomes `-integral_region k(x)*c(x,t) dx`; replacing it by a constant times `N` now needs grounds for that reduction. Return to the spatial distribution or a justified bound when the new use needs it.

This case shows how the intended consequence determines which physical relations must be completed. It also separates a global balance result from a local transport prediction.

#### PHY.6:5.3 - Detect an incompatible ideal connection before attempting a transient calculation

Two ideal linear capacitors have positive capacitances `C1` and `C2`. Their lower terminals share a reference conductor; their upper terminals are connected through a resistance `R>0`. The effective description neglects leakage, inductance and radiation. Let `v1` and `v2` be the upper-terminal potentials relative to the common reference, and let current `I` flow from capacitor 1 to capacitor 2.

Charge balances and the resistive response give

`C1*v1' = -I;  C2*v2' = I;  R*I = v1-v2.`

The total upper-plate charge `Q=C1*v1+C2*v2` is constant. The difference `delta=v1-v2` obeys

`delta' = -(1/C1+1/C2)*delta/R`.

Thus the difference decays with time constant `tau=R*C1*C2/(C1+C2)`, and both potentials approach

`v_final = (C1*v1(0)+C2*v2(0))/(C1+C2)`.

For `C1=1 F`, `C2=3 F`, `R=2 ohm`, `v1(0)=8 V` and `v2(0)=0 V`, the settled potential is `2 V`, `tau=1.5 s`, and `I(t)=4*exp(-t/1.5) A`, with time measured in seconds.

Stored electrical energy is `H=(C1*v1^2+C2*v2^2)/2`. Substitution gives `H'=-R*I^2`. Its initial and final values are `32 J` and `8 J`, so `24 J` is converted into other energy, here heat in the ideal resistance. More generally, the energy difference is

`C1*C2*(v1(0)-v2(0))^2/(2*(C1+C2))`.

**Changed connection.** Set `R=0` as an ideal connection from the initial instant. Its constraint `v1=v2` conflicts with the supplied unequal initial potentials. The smooth evolution above cannot simply start from them under that constraint. Recover the interaction that establishes the common potential when its current, duration or energy conversion matters. Resistance, inductance or electromagnetic emission may matter depending on the actual arrangement and interval; the ideal connection alone does not specify them.

If only the settled potential is needed, conserved charge together with the premise that the connected system settles can already supply it. A transient description is needed for a different question, such as peak current. Taking the positive-resistance time constant to zero does not remove the finite energy conversion. This is why changing an idealization can require revisiting both the preparation and the requested consequence.

### PHY.6:6 - Bias-Annotation

The examples use classical descriptions with explicit response laws. Their calculations are convenient for exposing balance, coupling and preparation. A stochastic, quantum or history-dependent response requires its own physical grounds and mathematical representation; the example equations do not supply those grounds.

Component descriptions can also make localized parts seem necessary. An account can instead describe a continuous medium through fields or many interacting constituents through collective variables. Choose the physical participants and the resolution of their description from the question.

### PHY.6:7 - Conformance Checklist

- The intended physical consequence and relevant preparation determine the scope of the construction.
- Each balance names the selected quantity, physical transfers and any production or conversion.
- Response and configuration relations supply the dependencies needed for the answer, with their physical grounds and conditions.
- Connected descriptions agree on exchanged quantities, signs, units and frames; consequential connection storage or dynamics remain represented.
- Independent initial and boundary conditions are compatible with the coupled relations, and dependent conditions are derived.
- The first consequence is obtained or a particular missing response or incompatible preparation directs the next work.
- Checks and further inquiry concern what can change the intended use; mathematical consequence, computational accuracy and physical adequacy remain distinguishable.

### PHY.6:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the construction | Consequence | Repair |
| --- | --- | --- |
| Expect conservation to determine every rate | The momentum balance still lacks the connecting force. | Supply and qualify the interaction's response law. |
| Remove internal force from each body because it cancels in the total | The relative motion disappears from the description. | Combine balances for the total while retaining the force in the part equations. |
| Treat mechanical damping as destruction of total energy | The energy account misses heating and possible feedback on the response. | Identify the receiving energy form and retain its dynamics when it affects the answer. |
| Read a total as a spatial prediction | An integrated species amount is used to infer a local concentration peak. | Restore the distribution and the conditions its evolution needs. |
| Impose an ideal connection on incompatible initial values | The capacitor transient is undefined within the chosen smooth account. | Resolve the preparation or represent the establishing interaction. |
| Build a detailed transient before using a sufficient balance | Work grows although the settled value or total is already determined. | Derive the required consequence first and expand only where needed. |

### PHY.6:9 - Consequences

The construction makes a physical account easier to use and divide among contributors. A specialist can supply a response law or preparation condition while another derives or computes its consequence. The connection states what each contribution must mean for the combined result.

Balances expose some construction errors cheaply. They leave many response questions open, so a balanced model can still be physically inadequate. Complex constraints, unresolved responses or changing regimes can require more physical work before the desired prediction becomes available. A conditional result or a narrower consequence can remain useful during that work.

### PHY.6:10 - Architectural Rationale

Separating balances, response laws and preparation makes their different contributions recoverable. Balances restrict change; response laws add behavior; preparation selects admissible evolution. Combining these relations before imposing a solving order lets the same physical account support different mathematical questions.

The construction uses C.29.BB for common balance reasoning and adds the physical choice of interactions, response grounds and compatible preparation. MMP.10 and C.29.2 handle the subsequent formulation and obtaining of mathematical results. This division permits a return to the missing physical premise without treating every solver difficulty as a computational defect.

Energy-based composition is especially useful when storage, conversion and exchange dominate the question. Direct momentum, species or charge balances can be simpler for another consequence. A physical variational principle offers another way to derive motion when its premises apply. The balance-and-response route is selected here for the difficulty it resolves, without requiring one formalism for every physical account.

### PHY.6:11 - SoTA-Echoing

**How much physical description is needed to obtain a selected consequence?** Adopt the quantity-first construction supplied by C.29.BB and developed in :4.1-.3. For the species total in :5.2, integration of the balance gives `N(t)=N(0)*exp(-k*t)`. Constructing and solving the full spatial evolution gives the same total under the same laws and boundary condition, but additionally needs an initial concentration field and a way to obtain its evolution. If only the total is used, the integrated account preserves the answer with fewer needed inputs and operations. It deliberately gives up the spatial profile. A local-concentration question or a position-dependent reaction rate reopens that choice. A readily available spatial solution can also supply the total.

**How should a reusable physical account be composed?** Retaining simultaneous component relations, as in :4.4-.5, preserves their meaning when the analysis or connection changes. For the positive-resistance capacitor case, eliminating the common current into two explicit evolution equations gives the same response as the retained three relations. Keeping the charge balances and the resistive relation separately makes their different contributions available when the connection changes: the balances survive, while setting R to zero changes the latter into a voltage-equality constraint that also restricts the preparation. This accepts the extra task of solving simultaneous relations when reuse or changing connections makes it worthwhile. For an isolated explicit evolution already suited to the question, use that simpler form. Reopen the choice when a new connection introduces a constraint or a consequential store.

[Van der Schaft, Port-Hamiltonian nonlinear systems](https://arxiv.org/html/2412.19673v1) (2024 preprint, sections 1.1-1.2) supplies a contemporary synthesis of storage, dissipation and power-conserving interconnection, including differential-algebraic descriptions. Adapt its separation of these contributions to the physical assembly in :4.3-.4. Remark 1.3 makes an important limit explicit: replacing mechanical dissipation by an untracked internal-energy increase is conditional on the relevant thermodynamic feedback being absent. Adopt that qualification in the damper case. For the two-body case, direct momentum equations and their energy derivative already show motion and the conversion into heat. A port-Hamiltonian representation gives the same consequences under the same response laws and makes energy-preserving composition explicit. Adapt the storage/interconnection distinction without requiring the reader to construct that formal representation for this small problem. Its additional structure becomes useful when a later question needs systematic composition or passivity properties of several interacting parts. Reopen the chosen account when an omitted store or thermal feedback changes those consequences.

The [Modelica 3.7 equation rules](https://specification.modelica.org/maint/3.7/equations.html), especially section 8.6, distinguish simultaneous relations, initialization equations and numerical guesses. Its [connection rules](https://specification.modelica.org/maint/3.7/connectors-and-connections.html), section 9.2, give explicit equality and signed flow-sum constructions. Adopt these as a worked formal tradition for composable physical descriptions and consistent initialization. The physical reason for a connection and the adequacy of a response remain separate from language conformance. Retaining algebraic constraints avoids inventing a physical direction merely to obtain explicit state-derivative equations.

The current [Dyad component-construction tutorial](https://help.juliahub.com/dyad/stable/tutorials/creating-components.html) demonstrates reusable connector and response relations with separate analyses. Adapt that distinction so a reader can reuse the component relations for several analyses.

The three worked calculations are constructed examples under their stated idealizations, not reports of physical measurements.

### PHY.6:12 - Relations

- **C.29.BB:** constructs balances across chosen boundaries and distinguishes transfer from production.
- **B.5.TU, PHY.4 and PHY.5:** supply theory use, constraints on an unknown law and the choice of effective physical detail.
- **MMP.10 and C.29.2:** formulate the selected mathematical question and obtain its result; **MMP.9** supplies mathematical reduction when needed.
- **MMP.11:** represents the freedom left in a response law after applicable constraints.
- **A.3.3.TR:** supplies common construction and composition of relations between states; the present method supplies the physical response and preparation.
- **B.5.MPC** connects the consequence to the physical question; **B.5.MPC.R** repairs a failed connection among physical, mathematical and computational contributions.
- **PHY.1 and PHY.2:** use the constructed physical account for similarity and analogue construction.
- **C.11.DUA:** decides whether resolving another physical uncertainty can improve the work enough to justify the inquiry.

### PHY.6:End

## PHY.7 - Obtain Motion from a Physical Variational Principle

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.7:1 - Problem frame

Use this pattern when you need to derive physical evolution from a principle that compares possible histories. The difficulty may be choosing the physical action, incorporating a constraint, or deciding which changes of a history the principle permits. A correct variation of the wrong physical formulation can give a precise but unusable equation.

The first result is an equation of motion, a boundary condition or a conserved consequence with the physical assumptions needed to use it. Sometimes the result is a particular unresolved interaction or constraint rule that must be supplied before the derivation can answer the question.

An *action* assigns a scalar to a history in the chosen physical description. *Stationarity* means that its first variation vanishes for the specified allowed changes. The physical theory supplies the reason to impose that condition. MATH.10 supplies the mathematical reasoning about variations; this method constructs and interprets its physical premises.

You need to identify the physical quantities and understand the proposed principle's range. You also need enough mathematical preparation to interpret a variation, or another contributor who can perform it and explain its result. The examples use elementary constrained mechanics, a charged particle and a continuous field. Their branch-specific laws are stated in the cases.

Use an existing equation or PHY.6's balances and response laws when they already answer the question economically. A variational formulation is useful when it simplifies constrained motion, carries interactions across coordinate changes, exposes a symmetry, or produces both interior and boundary equations. It need not be constructed for every physical problem.

### PHY.7:2 - Problem

Writing `L=T-V` and applying the Euler-Lagrange formula leaves important physical work hidden. Which interactions are represented by the potential? Does a moving support contribute to the velocity? Which endpoint quantities are fixed? Can the constraint really be imposed on every varied history?

These choices can change the resulting motion. A missing velocity-dependent interaction can leave the energy apparently reasonable while removing a force. Discarding a boundary term can replace a loaded boundary by a free one. Extending a rule for position constraints to a different kind of constraint can select a different evolution.

### PHY.7:3 - Forces

| Force | Tension |
| --- | --- |
| Compact principle and physical content | One scalar can generate several equations, but every consequential interaction still needs a physical basis. |
| Convenient coordinates and retained motion | Eliminating a constraint can simplify the calculation while concealing a moving support or an omitted degree of freedom. |
| Interior equations and boundaries | Integration by parts exposes both; the physical preparation decides which boundary variations remain free. |
| Mathematical comparison and physical evolution | Nearby histories define a variation; the predicted motion is selected and used with its own preparation. |
| Reusable formalism and cost | A common derivation helps repeated changes, while a direct balance may obtain one consequence with less work. |

### PHY.7:4 - Solution

**Choose the physical principle → represent the histories and interactions → state the allowed variations → derive the interior and boundary conditions → interpret the consequence → revise the implicated premise.**

#### PHY.7:4.1 - Choose a principle for the physical question

State the consequence needed and the physical situation it concerns. Choose the retained participants, interactions and regime. PHY.5 helps decide which physical detail matters.

Recover an applicable variational principle from the physical theory, or propose one with a stated physical basis and conditional use. Identify what it assigns to a history and what property the realized history is required to have. A stationary action, minimum energy at equilibrium and a dissipative variational rule impose different conditions. Select the one appropriate to the question.

For a smooth classical configuration history `q(t)`, a common form is

`S[q] = integral from t0 to t1 of L(q,qdot,t) dt`,

where `L` is the Lagrangian. A field description can instead integrate a density over space and time. The following steps show how to use such a principle; another physical principle can require a different functional or variation rule.

If the action or its physical grounds are missing, identify the interaction or assumption needed to construct them. A balance with a response law may settle the immediate question while the variational formulation remains open. The availability of a differentiation tool does not resolve that physical choice.

#### PHY.7:4.2 - Construct the histories and their action

Choose coordinates or fields that represent the retained physical configuration. State how they recover the physical quantities needed by the question. Include the time dependence of that recovery: for a position `r=F(q,t)`, velocity is `r_dot=F_q*qdot+F_t`. The second term describes motion of the chosen mapping, such as a moving support.

For a classical mechanical description with the appropriate conservative interactions, construct kinetic energy from those velocities and potential energy from the interactions, then use `L=T-V`. Check the interaction rather than infer this form from the word *energy*. A velocity-dependent coupling, a dissipative interaction or an eliminated environment can require another term or another principle.

Keep relevant boundary contributions. Stored energy at an endpoint, an imposed load and a fixed endpoint are physically different. A field's action can contain an interior density and separate surface or endpoint terms.

When reducing coordinates, retain how the discarded quantities or reactions can be recovered if needed. If the reduction loses a physical effect important to the question, return to PHY.5; MMP.9 handles the mathematical reduction once its physical premises are chosen.

#### PHY.7:4.3 - State what may vary and what must remain fixed

Specify the interval, endpoint conditions, constraints and regularity used in the comparison. For the ordinary fixed-endpoint principle, take `q_epsilon=q+epsilon*eta`, with `eta(t0)=eta(t1)=0`. A position constraint requires a family that preserves that constraint, or a justified multiplier formulation. MATH.10 distinguishes a finite admissible family from a tangent calculation valid only to first order.

The endpoint values used to derive an equation need not be known future observations. Fixing them in the variation removes its endpoint contribution. After deriving the local evolution equation, an initial-value use supplies compatible initial position and velocity; it does not add a guessed final position as another condition.

Distinguish position constraints from restrictions on velocity that cannot be integrated into position constraints. For such a restriction, varying entire constrained histories and requiring zero work of ideal reactions on selected instantaneous virtual displacements can give different equations. A *virtual displacement* here is a comparison of configurations at one fixed time used to state that reaction condition. Obtain the reaction or allowed-variation rule from the physical constraint model before using either construction.

For example, an ideal reaction model for `A(q,t)*qdot+b(q,t)=0` may prescribe zero reaction work on displacements satisfying `A*delta_q=0`. Generalized forces Q are defined by their virtual work, `delta W=Q dot delta_q`. The Lagrange-d'Alembert equations then have the form `d/dt(L_qdot)-L_q=Q+A^T*lambda`, together with the velocity constraint; here Q contains the other forces and `lambda` determines the reactions. This result uses the ideal-reaction premise. Simply putting the velocity constraint into an action with a multiplier is a different construction and need not reproduce it. Use PHY.6 when the balance and reaction description is the sufficient route.

#### PHY.7:4.4 - Derive the interior and boundary conditions together

Apply MATH.10 to the allowed family. Vary the complete action, including dependent quantities and boundary terms. For the smooth finite-dimensional form above, integration by parts gives

`delta S = [L_qdot dot eta] at t0,t1 + integral (L_q-d/dt(L_qdot)) dot eta dt`.

With fixed endpoints and otherwise arbitrary interior variations, stationarity gives `d/dt(L_qdot)-L_q=0`. With restricted variations, derive the condition supported by that restricted family. Retain force terms when the selected principle includes their virtual work.

For a field, perform the corresponding integration in space as well as time. First identify the boundary terms, then decide which vanish because the boundary value is prescribed and which produce a condition because its variation is free. An endpoint force or boundary energy can change the latter condition without changing the interior equation.

Differentiate symbolically or computationally when helpful, but retain the variables held fixed and the substitution rules. A result from varying only part of the action answers that smaller calculation. It does not justify omitting a physical term.

Stationarity alone does not establish a minimum. Use the stronger comparison only when required and supported. MATH.10 gives both a minimizing free-particle case and a stationary oscillator history with changes of either sign in the action.

#### PHY.7:4.5 - Recover the physical consequence and preparation

Interpret the equations in the original physical quantities. Supply the independent initial, boundary and driving conditions needed for the intended use. Check their compatibility with constraints. An equation of motion can be the sufficient first result; obtaining a trajectory or a peak can require the subsequent computation in C.29.2.

Derive a conservation claim from the applicable symmetry and its conditions. For the ordinary unconstrained Lagrangian with no additional generalized force, absence of a coordinate from L gives a constant corresponding `L_qdot`. Absence of explicit time dependence gives a constant `qdot dot L_qdot-L`. Interpret these expressions physically; a velocity-dependent interaction can make a canonical momentum differ from mass times velocity. MATH.13 supplies the broader symmetry-to-consequence reasoning and PHY.4 supplies the physical grounds for the symmetry.

Use a discriminating comparison when it can change the result's use. A force balance can reveal a missing coupling; boundary work can reveal an omitted load; a change of coordinates can expose a missing velocity term. Agreement establishes that comparison under its premises. It does not independently validate the physical principle.

#### PHY.7:4.6 - Return through the premise that changed

When an interaction changes, revise its action term or force contribution. When a support or boundary changes, revise the histories, velocity mapping and allowed variations before reusing the equations. When a coordinate description changes, transform the whole expression while keeping the physical history recoverable.

Equivalent expressions can describe the same motion. In the ordinary fixed-endpoint principle, adding `dF(q,t)/dt` changes the action only by endpoint values, so it preserves the interior equations. A use with different endpoint freedoms must also carry the changed boundary term. Distinguish this redescription from introducing another physical interaction.

If a computed consequence fails, locate whether the fault is the physical principle, admissible comparison, mathematical derivation or obtaining procedure. B.5.MPC.R provides the combined return. Seek additional physical evidence only where its possible result could alter the decision or action; a useful conditional derivation can already be used with its stated limits.

### PHY.7:5 - Archetypal Grounding

#### PHY.7:5.1 - Represent a constraint, then move its support

A point mass m moves in a vertical plane on an ideal rigid, massless rod of length l. Its frictionless pivot is initially fixed. Gravity is uniform with acceleration g. Let theta be the angle from the downward vertical; relative to the pivot,

`x=l*sin(theta);  y=-l*cos(theta)`.

The rod constraint is built into this configuration. For its ideal reaction, virtual motion along the circle has no radial displacement and the reaction does no virtual work. Kinetic energy is `T=m*l^2*theta_dot^2/2`, and potential energy is `V=-m*g*l*cos(theta)`. Thus

`L=m*l^2*theta_dot^2/2+m*g*l*cos(theta)`.

Varying theta with fixed temporal endpoints gives

`m*l^2*theta_ddot+m*g*l*sin(theta)=0`.

For `l=1 m`, `g=10 m/s^2` and initial `theta=pi/6`, the angular acceleration is `-5 rad/s^2`. The radial reaction need not be solved to obtain that consequence. It can be recovered from the physical acceleration if a later question concerns the rod load.

**Changed support.** Prescribe a horizontal pivot position X(t). The physical position becomes `x=X(t)+l*sin(theta)` while y is unchanged. Differentiating the complete position gives

`T=m*(X_dot^2+2*X_dot*l*cos(theta)*theta_dot+l^2*theta_dot^2)/2`.

Keeping the same gravitational potential and varying theta gives

`m*l^2*theta_ddot+m*l*X_ddot*cos(theta)+m*g*l*sin(theta)=0`.

With pivot acceleration `X_ddot=2 m/s^2` at the same angle, the angular acceleration is about `-6.732 rad/s^2`. Omitting the pivot term from the velocity would preserve the old answer while losing a real forcing. The pivot's prescribed motion may do work, so the fixed-pivot mechanical-energy conservation claim does not automatically transfer.

**Changed interaction.** For the fixed pivot, add an established damping torque `Q=-b*theta_dot`, with `b>=0`. The virtual-work equation gives `m*l^2*theta_ddot+b*theta_dot+m*g*l*sin(theta)=0`. The mechanical energy has derivative `-b*theta_dot^2`. Appending this dissipative torque to a conservative scalar potential would require a different physical account. PHY.6 supplies the corresponding balance and receiving energy form; a more elaborate dissipative action is useful only when the intended work needs it.

The general move is to construct the allowed configuration and its velocities, derive the consequence, and rebuild only the affected contribution when the support or interaction changes.

#### PHY.7:5.2 - Recover an interaction that energy alone would miss

A nonrelativistic particle with mass m and charge e moves in the xy plane in a prescribed uniform magnetic field B perpendicular to it. Electric fields, radiation reaction and the particle's alteration of the source field are neglected. The electromagnetic coupling is the physical premise; the field does no mechanical work but changes the direction of motion.

Choose a vector potential `A=(-B*y/2,B*x/2,0)`, whose curl is the specified magnetic field. With zero electric scalar potential, the physical Lagrangian is

`L=m*(x_dot^2+y_dot^2)/2 + e*B*(x*y_dot-y*x_dot)/2`.

Its derivatives give

`d/dt(L_xdot)=m*x_ddot-e*B*y_dot/2;  L_x=e*B*y_dot/2`,

and the corresponding y expressions. The Euler-Lagrange equations are therefore

`m*x_ddot=e*B*y_dot;  m*y_ddot=-e*B*x_dot`.

For `e*B/m=2 per second`, initial `x_dot=3 m/s` and `y_dot=0`, the initial acceleration is `(0,-6) m/s^2`. Substitution into the kinetic-energy derivative gives zero. Conservation of kinetic energy alone would also allow straight uniform motion; it does not determine the magnetic turning. Using only T with zero scalar potential would miss the interaction.

**Changed representation.** Let `chi=B*x*y/2` and use `A_new=A+grad(chi)=(0,B*x,0)`. The new Lagrangian is `L_new=m*(x_dot^2+y_dot^2)/2+e*B*x*y_dot`. Its difference from L is `e*d(chi)/dt`, so the fixed-endpoint equations are unchanged. The canonical momenta `L_xdot` and `L_ydot` do change; the physical velocity and magnetic field do not. Comparing those canonical expressions as though they were two observed mechanical momenta would invent a physical discrepancy.

The action's stationary paths depend on the physical interaction; equivalent gauge descriptions preserve them under the stated endpoint rule.

#### PHY.7:5.3 - Derive an interior law and change the endpoint condition

A taut string has uniform tension T and mass per unit length mu. Its transverse displacement u(x,t) is small enough that slopes can be treated to leading order; changes of tension and longitudinal motion are neglected. The kinetic energy per length is `mu*u_t^2/2`. Expanding the extra length to second order in slope gives the stored elastic contribution `T*u_x^2/2`. For length l, use

`S[u]=integral over time and 0<=x<=l of (mu*u_t^2-T*u_x^2)/2 dx dt`.

Take variations eta that vanish at the two temporal endpoints. Integration by parts gives the interior coefficient `-mu*u_tt+T*u_xx` and the spatial boundary contribution

`integral over time of [-T*u_x*eta] at x=0,l dt`.

Thus the interior equation is `mu*u_tt=T*u_xx`. At a fixed endpoint, eta is zero. At an unloaded endpoint free to move transversely in this model, eta is arbitrary and the corresponding slope must be zero.

For `mu=0.01 kg/m`, `T=100 N` and `l=1 m`, wave speed is `sqrt(T/mu)=100 m/s`. Two fixed endpoints admit the lowest nonzero spatial mode `sin(pi*x/l)`, giving frequency `50 Hz`. Keep the left endpoint fixed and free the right endpoint transversely while maintaining its axial tension; the lowest mode becomes `sin(pi*x/(2*l))` and its frequency is `25 Hz`. The interior equation did not change. Reusing the fixed-end spectrum would miss the changed boundary.

**Loaded endpoint.** Attach a massless transverse spring of stiffness kappa at x=l. Add `-integral kappa*u(l,t)^2/2 dt` to the action. With the right endpoint variation free, its coefficient gives `T*u_x(l,t)+kappa*u(l,t)=0`. The spring changes the boundary condition through its stored energy. If an endpoint mass is consequential, its kinetic term must be included too; the massless condition would no longer supply that boundary's dynamics.

Retain the boundary contribution until the physical freedom or load determines its use.

### PHY.7:6 - Bias-Annotation

The examples make smooth classical stationarity easy to inspect. Quantum or probabilistic descriptions can connect an action to observations through a different rule; the fixed-history calculation here does not supply that rule. Use the principle and interpretation of the relevant physical theory.

Compact energy expressions can also hide how a constraint is maintained. The ideal rod, imposed pivot motion and massless endpoint spring each exclude physical detail. Restore that detail when reaction, compliance or a transient changes the requested consequence.

### PHY.7:7 - Conformance Checklist

- The selected physical theory or stated hypothesis supplies the principle and its range.
- Coordinates or fields recover the needed physical quantities, including time-dependent mappings.
- The action includes consequential interactions and boundary contributions.
- Allowed variations and constraints follow the selected physical principle; endpoint restrictions are explicit.
- Interior, force and boundary terms produce the conditions actually used.
- The interpreted result retains compatible preparation and the reach of its stationarity or conservation claim.
- A changed interaction, constraint or representation returns through its affected contribution; further inquiry serves a consequential question.

### PHY.7:8 - Common Anti-Patterns and How to Avoid Them

| Misstep | Consequence | Repair |
| --- | --- | --- |
| Use T-V without recovering the interaction | The magnetic force disappears although kinetic energy is constant. | Supply the coupling from the physical theory and vary the complete Lagrangian. |
| Differentiate coordinates while omitting their moving reference | The prescribed pivot acceleration is absent from the motion. | Differentiate the complete position map, including its explicit time dependence. |
| Discard a boundary term before deciding what is fixed | A loaded or free endpoint receives the wrong condition. | Retain the term until the boundary freedom and physical contribution are specified. |
| Use one constraint rule for every velocity restriction | Different variational constructions are treated as the same physical model. | Recover the constraint's reaction or admissible-variation premise. |
| Read stationary as minimum | A saddle history receives an unsupported optimality claim. | Use the first-variation result at its established scope and perform the stronger comparison when needed. |
| Read a changed canonical expression as changed motion | Gauge-related descriptions appear to disagree physically. | Recover the physical quantities and the endpoint term preserved by the transformation. |

### PHY.7:9 - Consequences

A useful physical principle can organize several coupled equations and expose what changes when coordinates, constraints or boundaries change. The calculation can be shared with a mathematical specialist or a symbolic tool while the physical premises remain inspectable.

The compact formulation does not remove the need for physical knowledge. Constructing a justified action can be harder than writing a balance. An equation derived from it may still require substantial work to solve or to connect to observation. Stop at the consequence sufficient for the current work and retain unresolved physical choices in any conditional use.

### PHY.7:10 - Architectural Rationale

The action, allowed comparison and physical interpretation carry different information. Keeping them together prevents the mathematical operation of variation from silently choosing a physical theory. Keeping them distinct allows a return to the part that changed.

MATH.10 supplies the common variational argument. PHY.7 adds the physical choice of principle, interactions, constraint model and preparation. PHY.6 offers the alternative construction from balances and response laws. MMP and the computational patterns receive the resulting equations and conditions when the intended consequence needs further formulation or calculation.

### PHY.7:11 - SoTA-Echoing

**When does an action formulation repay its cost?** For the ideal rod in :5.1, both the angular-action calculation and a tangential projection of Newton's force balance obtain the angular acceleration without solving the radial reaction. Both retain the rod constraint as a physical premise. If the rod load is the requested result, the balance or a reaction reconstruction is needed. For :5.3, both local force balance and field variation give the wave equation; retaining the action's endpoint term also makes the changed spring contribution available. Select that organization when repeated constraint or boundary changes make it useful. Use the simpler sufficient balance for an isolated question. These comparisons are constructed uses, not measurements of universal efficiency.

[Sussman and Wisdom, Structure and Interpretation of Classical Mechanics, second edition, chapter 1](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/9579/sicm_edition_2.zip/chapter001.html), is the established source for treating coordinate choice, physical action and variation as a connected construction. Adopt that connection in :4.1-.4. Sections 1.6 and 1.10 limit the automatic use of T-V and of coordinate-constraint arguments. In particular, section 1.10.3 distinguishes stationarity over constrained histories from the ideal-reaction rule for nonintegrable velocity constraints. The resulting instruction is to recover the physical constraint model before choosing the variation. Reopen that choice when the way a constraint is maintained changes a predicted reaction or motion.

[Gaset, Lainz, Mas and Rivas, The Herglotz variational principle for dissipative field theories](https://arxiv.org/abs/2211.17058) (2022 preprint, published 2024), develops two formulations of dissipative field variation. Its section 5.2 gives a mathematical case where they have different solutions; the conclusions identify a condition under which the approaches agree. Adapt the methodological consequence: naming a variational principle is insufficient without its variation rule and conditions. The example establishes formal non-equivalence; it does not select the physical adequacy of either account for an apparatus. An action-based treatment of a new dissipative interaction reopens that choice.

[Galley, Tsang and Stein, The principle of stationary nonconservative action for classical mechanics and field theories](https://arxiv.org/abs/1412.3082) (2014), supplies a distinct route using doubled variables and an initial-value construction. Its opening eliminated-oscillator example shows why eliminating an environment inside the usual endpoint action can lose the intended causal response. For the supplied damping torque in :5.1, the force or virtual-work equation already gives the desired motion with less apparatus. The extended-action route becomes relevant when the work needs elimination within an action or a variational treatment of nonconservative coupling. Retain that choice rather than silently absorbing every loss into an ordinary potential.

The worked calculations are constructed consequences of their stated classical descriptions.

### PHY.7:12 - Relations

- **MATH.10:** constructs admissible variations and establishes the reach of the resulting condition.
- **PHY.4, PHY.5 and B.5.TU:** supply physical symmetry grounds, retained detail and use of a theory in a case.
- **PHY.6 and C.29.BB:** provide balance and response constructions for an alternative derivation or a discriminating comparison.
- **MATH.13:** derives a mathematical consequence from symmetry; this method supplies the physical action and its admissible symmetry.
- **MMP.9, MMP.10 and C.29.2:** reduce or formulate the resulting mathematical problem and obtain the needed consequence.
- **B.5.MPC:** connects the mathematical result and its conditions to the physical question.
- **B.5.MPC.R:** revises a failed physical, mathematical or computational contribution and its affected uses.
- **C.11.DUA:** selects further inquiry when resolving the uncertainty can improve the work enough to justify its cost.

### PHY.7:End

## PHY.8 - Infer Macroscopic Physical Behavior from Microscopic Alternatives

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.8:1 - Problem frame

Use this pattern when you need to explain or predict collective physical behavior from possible microscopic states or histories. The difficulty is deciding which alternatives matter, why they receive particular weights, and whether their aggregate represents the observation you need. Many constituents can produce a stable average, persistent fluctuations or a response that depends on preparation.

The first result is a collective prediction with its physical grounds: a distribution of an observable, its mean and relevant fluctuations, or an evolution law at the required scale. If different plausible preparations give different answers, retain that difference and identify what would settle it.

Here *microscopic* and *macroscopic* refer to levels of physical description. A microscopic description retains distinctions that the selected collective observable combines. The method can apply to a small system's aggregate as well as a large population; the approximation of a stable macroscopic value requires its own grounds.

You need to interpret the physical preparation and interactions, and to understand the probability operations used in the calculation. Quantum cases require the corresponding state and measurement rules. A collaborator can supply those mathematical operations while you retain the question and physical interpretation. The worked cases state their additional branch-specific premises.

Use a direct balance or an established effective law when it already gives the needed consequence with adequate conditions. Construct the microscopic account when fluctuations, changed preparation or a proposed mechanism can alter that consequence. PHY.5 helps choose which detail to retain.

### PHY.8:2 - Problem

A correct average can answer the wrong physical question. A detector saturates on individual excursions, not on the ensemble mean. A system prepared in one part of its state space need not explore all alternatives during the observation. Separate constituents can share a preparation that makes their fluctuations add together.

The weighting is also a physical choice. Counting possible states does not by itself make them equally probable. Fitting a distribution to a signal does not establish the microscopic mechanism that produces it. A numerical sequence can sample the desired distribution without representing the time evolution of the system.

The task is to carry physical preparation and interaction through the statistical construction to the consequence that will be used.

### PHY.8:3 - Forces

| Force | Tension |
| --- | --- |
| Microscopic detail and useful aggregate | A detailed account can explain a changed response, while an unchanged total may need only a balance. |
| State counting and preparation | Many alternatives are possible, but the preparation and dynamics can weight them differently. |
| Typical behavior and rare outcomes | A narrow central range can support ordinary operation while missing a consequential excursion. |
| Individual properties and collective dependence | Local statistics can be unchanged while correlations alter the whole. |
| Long-time theory and available time | A limiting result may be valid yet unavailable within the observation interval. |
| Sampling economy and physical meaning | An efficient sampler can obtain a statistic without reproducing physical motion. |

### PHY.8:4 - Solution

**Choose the collective consequence → construct the microscopic alternatives and their weights → derive the observable statistics → test the relevant fluctuations and times → revise the implicated physical premise.**

#### PHY.8:4.1 - Specify the observable and how it will be used

Name the physical quantity, spatial extent and observation interval. Decide whether the work needs a value at one time, a time average, a response after an intervention or the chance of crossing a threshold. These uses can require different statistics from the same system.

Relate the observable to the retained microscopic description. In a classical account, write it as a function of the state, or of a history when the measurement integrates over time. Include a measurement response when it changes the answer. MMP.7 constructs the probability law of the recorded outcome from a subject law and a recording procedure.

Separate physical variation from uncertainty about a fixed parameter. A rate that changes among preparations, an unknown common rate and a fresh independent rate for each constituent describe different arrangements. Keep a fixed unknown parameter explicit unless a probability law over it is warranted for the intended inference.

#### PHY.8:4.2 - Construct admissible alternatives and their weighting grounds

Choose the microscopic variables and their physical constraints. Use the theory and preparation to determine possible states, conserved quantities, accessible transitions and coupling to the surroundings. Preserve collective restrictions: fixing total energy or particle number can couple otherwise separate constituents.

Then say what supports the weights. A controlled preparation can supply frequencies; an admitted dynamical law can transport an initial distribution; an equilibrium argument can supply a statistical ensemble under its physical assumptions. An ensemble is a statistical description of possible preparations or states, not an additional physical population that must exist.

For an equilibrium construction, identify what the surroundings hold fixed and what can be exchanged. If a weakly coupled subsystem exchanges energy with a large equilibrated reservoir, a canonical distribution may be appropriate. If the total energy is fixed, begin with that restriction instead. Retain state multiplicities: several distinct states with one energy contribute separately. Check equivalence of proposed ensembles for the observable and regime being used before substituting one for another.

A maximum-entropy inference selects a distribution relative to specified alternatives, a reference measure and constraints. It can provide a useful conditional prediction. Its inferential grounds remain distinct from an argument that this preparation physically equilibrates to that distribution.

For a quantum account, use the prepared state and the relevant observable or measurement operators. A density operator can represent a subsystem correlated with its environment. Its decomposition into weighted pure states need not identify a unique physical preparation. Compute the probabilities of the chosen measurement using the theory; do not replace the state by presumed simultaneous values for incompatible measurements.

If the grounds leave several weightings possible, carry their different consequences far enough to see whether the unresolved choice matters. A bound or a common consequence can already answer the work question.

#### PHY.8:4.3 - Derive the collective law without discarding dependence

Obtain the observable's distribution by combining the admissible alternatives with their weights. For a classical state X with probability law P and an observable Y=g(X), the probability of a set B of outcomes is

`P(Y in B) = integral 1[g(x) in B] P(dx)`.

The symbol 1 is one when its bracketed condition holds and zero otherwise. Use a weighted sum for a discrete state set. A non-ideal recording procedure adds its conditional response through MMP.7.

For a quantum state rho and an ideal measurement of observable A, outcome probabilities follow from the corresponding measurement projectors. When the second moment is finite, the mean is `Tr(rho A)` and the variance is `Tr(rho A²) - Tr(rho A)²`. Here Tr denotes the trace, and A represents the physical observable under the selected measurement. When the required moments are not finite, use the outcome distribution or a relevant bounded event instead of these finite-moment summaries. Other measurement arrangements require their own operators and response.

Retain correlations while forming collective quantities. For a finite collection of jointly defined classical outcomes X_i with finite second moments,

`E[sum_i X_i] = sum_i E[X_i]`,

`Var(sum_i X_i) = sum_i Var(X_i) + 2 sum_(i<j) Cov(X_i,X_j)`.

Linearity of the mean needs no independence assumption. The variance equals the sum of individual variances when the total covariance contribution, `2 sum_(i<j) Cov(X_i,X_j)`, is zero. Pairwise zero covariance is sufficient, and independence is a stronger sufficient condition. Retain the dependence supplied by the physical arrangement.

A mean may be all that the question needs. When excursions matter, derive a relevant variance, tail probability or bound. Preserve units and the normalization used for comparison: the variance of a total and that of a per-constituent average differ by the square of the constituent count.

#### PHY.8:4.4 - Establish when the aggregate represents a typical observation

Compare the predicted spread with the tolerance or decision in the work. For any scalar observable Y with finite variance and positive tolerance epsilon, Chebyshev's inequality gives

`P(|Y-E[Y]| >= epsilon) <= Var(Y)/epsilon²`.

This can settle a sufficient bound without reconstructing the whole distribution. If the bound is too loose to decide, a sharper calculation may help. Its cost is justified by the unresolved decision, not by the mere availability of another statistical method.

For an average over N constituents, the variance is bounded by a constant times 1/N when the sum of relevant covariances is bounded above by a constant times N. A common fluctuating influence can instead make the total variance grow as N². Inspect the physical dependence that determines this scaling. Increasing the number of constituents then has different effects on reliability.

Keep a probability claim relative to its measure. A set containing most of the probability need not contain most of the unweighted alternatives. Conversely, a large count of states says little about the prepared distribution until its weights are supplied.

Decide whether a finite system and the requested observable permit the limiting argument. Correlation lengths comparable to system size, constraints, long-range interactions or operation near a transition can invalidate the approximation used to obtain concentration. Return to the physical account when that invalidation changes the required result; do not require a thermodynamic limit for an already sufficient finite calculation.

#### PHY.8:4.5 - Connect ensemble behavior to physical time

An ensemble mean at time t and a time average along one history answer different questions. To use the latter as an estimate of the former, examine the relevant dynamics, preparation and observation duration.

Derive or obtain a relaxation or correlation time for the selected observable. Compare it with the duration available and with any external drive. A stationary distribution can exist while equilibration is too slow for the experiment. An invariant portion of state space can preserve dependence on the initial preparation. A theorem about an infinite-time average supplies no finite settling time by itself.

For a stationary scalar process A(t) with covariance C(tau)=Cov(A(t),A(t+tau)), the variance of its average over duration T is

`Var(A_bar_T) = (2/T²) integral from 0 to T of (T-tau) C(tau) d tau`.

This relation assumes finite second moments and a well-defined time integral. Use it, or a suitable finite-sample counterpart, when the accuracy of time averaging matters. Long correlations reduce the gain from repeated measurements; drawing more points from the same slow fluctuation does not make them independent.

If an eliminated variable leaves memory in the retained evolution, keep that memory or restore a sufficient state through PHY.5 and MMP.9. Decide which description serves the time-dependent question. A stationary histogram alone does not establish the transition law, response time or heat dissipation.

#### PHY.8:4.6 - Compute, compare and return to the physical premise

Use a finite enumeration, analytical calculation or numerical sampler appropriate to the selected statistic. C.29.2 helps formulate the computation. Check that the computation implements the chosen state space, preparation, dependence and observable.

A Monte Carlo sampler can deliberately use artificial transitions to obtain a distribution. Interpret its steps as physical time only when a separate physical transition law and time calibration justify that use. Convergence of a numerical estimate, statistical concentration of the physical observable and adequacy of the microscopic account are different questions.

Make the comparison that can change the work decision. A small case can reveal a lost correlation. An available observation can distinguish two preparations. A changed observation interval can expose an invalid equilibrium approximation. Retain a sufficient conditional answer when further evidence would not justify its cost; C.11.DUA governs that choice.

Return to the implicated premise: the prepared state, weighting, interaction, measurement response or time-scale assumption. Preserve unaffected balances and mathematical consequences. The next question may concern controlling fluctuations, constructing a different preparation or choosing a more informative observable.

### PHY.8:5 - Archetypal Grounding

#### PHY.8:5.1 - Predict an excited population from a reservoir argument

A device contains N=400 distinguishable, weakly interacting units. Each has a nondegenerate ground state of energy 0 and a nondegenerate excited state of energy Delta. The units have equilibrated with a large reservoir at temperature T. Treat interactions between units and their contribution to the reservoir's temperature change as negligible. An ideal readout counts excited units before appreciable relaxation changes that count.

The physical question is the mean count and its variation between independently repeated equilibrium preparations. The reservoir argument weights a unit's state by the number of compatible reservoir states. With reservoir entropy S_R and Boltzmann constant k_B,

`Omega_R(E-Delta)/Omega_R(E) approximately exp(-Delta/(k_B T))`,

using the first-order entropy change and `dS_R/dE=1/T`. This approximation needs the reservoir's temperature to remain effectively constant over the exchanged energies. The equal weighting used for the combined equilibrium energy shell is a premise of this construction.

Choose `Delta=k_B T ln(3)`. The excited-to-ground weight ratio is 1/3, so the excited probability is p=1/4, not 1/2. Two possible energy values do not receive equal weights under this preparation.

Under the stated independence approximation, the count K is binomial:

`P(K=k) = choose(400,k) (1/4)^k (3/4)^(400-k)`.

It has mean 100 and variance 75, giving a standard deviation about 8.66 units. If the receiving requirement is that the count differs from 100 by less than 50 in at least 96% of preparations, Chebyshev gives `P(|K-100|>=50)<=75/2500=0.03`. That bound already satisfies the requirement; calculating every binomial probability is unnecessary for this decision.

Now suppose the excited energy has three distinguishable states at the same Delta, with the same equilibrium and independence premises. Their total weight is three times larger. The excited probability becomes 1/2, the mean count 200 and the variance 100. The energy gap alone no longer supplies the previous count.

If the device is instead prepared with precisely 100 excited units and isolated during readout, the count variance is zero. Individual units can still each have excited probability 1/4 across a permutation-symmetric preparation. The fixed-total restriction prevents the binomial independence assumption. Use the preparation that the work actually supplies.

#### PHY.8:5.2 - Recover collective fluctuations from a prepared joint state

A readout measures the z component of N=100 spin-1/2 systems along one common axis. Write each normalized outcome as s_i=+1 or -1; the physical angular momentum is `(hbar/2) s_i`. The collective normalized signal is `M=sum_i s_i`.

Three ideal preparations give every individual spin equal probabilities of +1 and -1:

| Preparation during readout | Joint property used | Mean M | Variance of M |
| --- | --- | --- | --- |
| Independently prepared maximally mixed spins | Outcomes along the common axis are independent | 0 | 100 |
| Fifty independent singlet pairs | The two outcomes in every pair are opposite | 0 | 0 |
| With equal probabilities, all spins prepared up or all prepared down | Every outcome shares the same prepared sign | 0 | 10000 |

For a singlet pair, the state is `(|up down>-|down up>)/sqrt(2)`. Its ideal common-axis measurements give opposite results, so each pair contributes zero to M. For the last preparation, M itself is +100 or -100 with equal probabilities. The variance entries follow from these joint properties and from addition of independent variances in the first preparation.

A readout designed only from the individual mean would predict the same zero signal in all three cases. Their root-mean-square collective signals are 10, 0 and 100. If saturation occurs when |M| exceeds 50, the last preparation always saturates. The first has probability at most `100/50²=0.04` by the variance bound, and the ideal paired preparation never saturates.

Now retain the paired preparation but read only one spin from each pair. The sum of those fifty outcomes has variance 50, because different pairs were prepared independently. The zero-variance conclusion applied to a complete-pair sum, not to an arbitrary selected subset.

This calculation uses joint states and a stated measurement. Common-axis anticorrelation alone would also be compatible with other preparations; it does not identify the singlet uniquely. Recovering entanglement would require a different question and suitable measurements. Detector errors or correlations between pairs would change the recording law or the preparation premise.

#### PHY.8:5.3 - Derive transport from persistent microscopic motion

Particles move on an unbounded line with speed v>0. Each reverses direction at independent Poisson events of rate alpha>0. Initially each particle is at the origin, with either direction equally likely. This is a physical stochastic model for the motion; its validity must come from the selected mechanism and regime.

Let p_+(x,t) and p_-(x,t) describe position probabilities with positive and negative velocity. The point preparation leaves probability atoms at the unreversed fronts x=+vt and x=-vt; interpret the following density equations in the distributional sense. The transition and transport laws give

`partial_t p_+ = -v partial_x p_+ - alpha p_+ + alpha p_-`,

`partial_t p_- = v partial_x p_- + alpha p_+ - alpha p_-`.

Define total density n=p_++p_- and probability current j=v(p_+-p_-). Adding and subtracting give

`partial_t n = -partial_x j`,

`partial_t j = -v² partial_x n - 2 alpha j`.

The current retains the directional persistence. Eliminating it gives

`partial_tt n + 2 alpha partial_t n = v² partial_xx n`.

For times long compared with `1/(2 alpha)` and spatial variation slow enough for the current to relax, use `j approximately -D partial_x n`, with `D=v²/(2 alpha)`. The resulting diffusion equation is an approximation with physical grounds, not a consequence of fitting a bell-shaped histogram.

The mean position stays zero. For the stated initial preparation, the mean-square displacement is

`E[x(t)²] = (v²/alpha) [t - (1-exp(-2 alpha t))/(2 alpha)]`.

With v=2 cm/s and alpha=1/s, it is about 0.03746 cm² at t=0.1 s. A diffusion calculation would give 0.4 cm², more than ten times as much. At t=20 s, the values are about 78 and 80 cm²: diffusion overestimates this observable by about 2.56% relative to the microscopic model. A 3% tolerance admits the later approximation but not the earlier one.

Changing the requested time therefore changes the needed description. Retain the density-current equations for the early response; use the diffusion reduction when its error is adequate for the requested observable. Boundary arrival probabilities would need their own comparison, since this mean-square agreement does not validate every feature of the distribution.

A simulation that flips velocity with the specified rate implements physical time. A different Markov chain designed to sample a position distribution has no such interpretation merely because its histogram agrees.

### PHY.8:6 - Bias-Annotation

The examples emphasize finite statistics and tractable microscopic laws. Collective behavior can involve phase transitions, long-range coupling, non-equilibrium drive and quantum observables that require more specialized calculations. The reusable move is to connect preparation, weighting, dependence and the used observable; the simple example distributions are not defaults for those cases.

A macroscopic discrepancy can also arise from the recording procedure. Return through MMP.7 when the detector's selection, integration or disturbance changes what is observed.

### PHY.8:7 - Conformance Checklist

- The requested observable, preparation and observation interval are recoverable.
- The microscopic alternatives and their weights have stated physical or inferential grounds.
- Collective constraints and relevant correlations survive the aggregation.
- The statistic answers the intended use, including a fluctuation or tail question when one matters.
- A concentration or equilibration argument has conditions appropriate to the finite system and observation.
- Computational transitions are interpreted as physical time only with a supporting physical law.
- A changed result returns to the implicated premise, while a sufficient conditional answer can remain in use.

### PHY.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Equal weights from a count of alternatives | Two energy values are treated as equally likely despite a biased preparation. | Construct the weights from the reservoir, preparation or other applicable grounds. |
| Independence from separate constituents | A common preparation or fixed total disappears from the joint account. | Form the collective law before discarding dependence. |
| Mean as a prediction of every run | An excursion-sensitive device is assessed only at the mean signal. | Compute the fluctuation or threshold consequence needed for that device. |
| Equilibrium without an available settling interval | A stationary distribution replaces the prepared transient. | Compare the relevant relaxation with the observation time. |
| Sampler steps as elapsed time | Artificial moves become a claimed physical transition law. | Separate distribution sampling from a physically calibrated evolution. |
| One successful statistic validates the whole reduction | Mean-square agreement is used to justify a boundary-arrival probability. | Compare the observable that the changed question actually consumes. |

### PHY.8:9 - Consequences

A collective prediction becomes revisable through its physical premises. A team can assign construction of the preparation and microscopic law, probability calculation, numerical estimation and interpretation to different contributors while retaining what each result assumes.

The work can avoid both unnecessary microscopic simulation and an unjustified average. A bound can finish the present decision; a correlation or finite-time effect can instead open a different preparation, observation or physical account.

### PHY.8:10 - Architectural Rationale

The physical choice of alternatives and weights comes before their mathematical aggregation. This preserves the distinction between a distribution that fits records and a mechanism-based account that can predict a changed preparation. MMP.7 supplies the observation-law construction; this pattern supplies the physical grounds that construction needs.

Fluctuations and physical time remain alongside the mean because they can change the use without changing individual statistics. Keeping those relations explicit makes the method transferable from populations and transport to sensing and physical computation.

PHY.5 decides which physical detail can be omitted. Here a statistical consequence can show that an omitted correlation or memory matters, and return that problem to the effective-description method. A complete microscopic theory is unnecessary when a physically justified restricted account already settles the question.

### PHY.8:11 - SoTA-Echoing

[Baldovin, Gradenigo, Vulpiani and Zanghì, *On the foundations of statistical mechanics*](https://arxiv.org/abs/2411.08709), Physics Reports 1132 (2025), provides a current synthesis of equilibrium foundations. Sections 3.4-3.5 distinguish selected macroscopic observables and useful sampling from unrestricted dynamical claims; sections 5.1.3-5.1.5 connect quantum states, reduced states and equilibrium weighting. The method uses these distinctions without making one universal equilibration argument a prerequisite.

Compare the excited-count question in :5.1. A physically appropriate equilibrium ensemble gives the same count law that sufficiently repeated microscopic simulation would estimate, with less trajectory computation. Simulation is useful when interactions or preparation invalidate the simple ensemble calculation. A maximum-entropy inference from supplied constraints is another usable route when those are the available grounds; it does not alone establish a relaxation time or response to changed coupling. The different questions determine which contribution is needed.

[Corominas-Murtra, Hanel and Jizba, *Typicality, entropy and the generalization of statistical mechanics*](https://arxiv.org/abs/2409.06537) examines extensions of typicality beyond the usual independent-constituent setting. Its distinction between probability concentration and unweighted state counts supports :4.4. The present worked calculations use ordinary finite probabilities; generalized entropy is not required for their decisions. Reopen the concentration argument when the changing alternatives or dependencies defeat its current assumptions.

[Korbel and colleagues, *Quo vadis, stochastic thermodynamics?*](https://arxiv.org/abs/2604.26601), 2026, examines hidden variables, memory and limits of thermodynamic interpretation. Sections II and V matter here: a reduced stochastic description may retain memory, and observable irreversibility does not automatically determine physical dissipation. Use a physical energetic account for a heat claim. For the transport question in :5.3, the density-current account and its diffusion reduction answer the same late-time mean-square question; the current adds useful content when the early response is required. A larger microscopic simulation would cost more without improving this already solvable comparison.

The examples are explicit constructions of the method, not reports of validation of particular devices. More demanding equilibrium, quantum or driven-system questions can require specialized physical and mathematical results. Their use retains the preparation, observable and time conditions that make the result transferable.

### PHY.8:12 - Relations

- **PHY.5:** chooses an effective physical description and restores an omitted coupling, state or memory when its consequence matters.
- **PHY.6 and C.29.BB:** construct the balance and response relations retained in collective evolution.
- **MMP.7:** composes the physical subject law with the recording procedure and derives the law of the recorded data.
- **MMP.9:** derives a reduced evolution from a more detailed mathematical account under stated assumptions.
- **B.5.MPC** connects the mathematical consequence to the physical question; **C.29.2** formulates any needed computation.
- **C.16.MR:** identifies the measurement relation whose physical and statistical realization is being used.
- **B.5.MPC.R:** repairs the implicated physical, mathematical or computational contribution and its affected uses.
- **C.11.DUA:** chooses whether resolving an uncertainty warrants further work or a sufficient conditional result should be used.

### PHY.8:End

# Part B - Compare, observe and act

## PHY.1 - Construct Physical Similarity Across Changed Conditions

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### PHY.1:1 - Problem frame

Use this pattern when you want to learn about a physical situation through another arrangement, but changing its size, material, speed or surroundings changes the effects that produce the answer. You may be designing a smaller experiment, comparing observations made under different conditions, or deciding which part of a previous physical result can be reused.

Start with the quantity or behavior you need to infer about the original situation. Then identify one physical effect whose relative importance could change in the proposed comparison. A smaller object has less weight, for example, but its ability to carry that weight changes by a different factor. That difference can determine how the comparison should be built and loaded.

The result is a set of physically compatible comparison conditions, a justified transfer of a selected result, or a conflict that directs the next construction. Here **physical similarity** means correspondence of the physical behavior needed by the question under stated changes of scale or conditions. Geometric similarity preserves shape under scaling; further conditions can be needed to preserve the relevant behavior.

You need the physical account used in the comparison and the mathematics needed to transform its relations. You can develop that account through B.5.FM and B.5.TU or obtain a missing physical contribution from a collaborator. Algebra and ratios suffice for many first comparisons; fields and time-dependent behavior can require differential equations. A ready comparison whose conditions fit the question can be used directly. If the problem is expressing an already understood account mathematically, MMP.10 supplies that formulation work.

### PHY.1:2 - Problem

A physically different experiment can resemble the original while answering a different question. Keeping shape preserves length ratios. It can still change the competition between weight and strength, inertia and friction, propagation and absorption, or reaction and transport. An experiment that preserves a final value can also change the path by which that value is reached.

The difficulty is constructing the conditions of a useful comparison. A familiar dimensionless number can help, but selecting it requires knowing which physical effects it compares. Several relevant conditions can demand incompatible changes to the same material or control. The requested result determines whether that conflict must be removed or whether a more limited comparison will suffice.

### PHY.1:3 - Forces

| Choice | What it changes |
| --- | --- |
| Whole behavior or one output | Reproducing one displacement or threshold can require less than reproducing the complete field or time history. |
| Smaller experiment or unchanged balance of effects | Length, area and volume scale differently; material properties and preparation may need to change too. |
| Useful simplification or an omitted mechanism | Removing a small contribution simplifies the comparison, but its effect can accumulate or control behavior near a transition. |
| Mathematical settings or available physical means | Equations may require material properties or forcing that the proposed apparatus cannot supply together. |
| One matched experiment or several complementary results | Combining calculations and observations can answer a question that no single scaled arrangement reproduces. |

### PHY.1:4 - Solution

**Choose the result to transfer → recover its physical causes and conditions → express their relative contributions → construct compatible comparison settings → resolve consequential mismatches → use the result and revise it when the question changes.**

#### PHY.1:4.1 - Choose the physical result and the proposed change

Name the original arrangement and the comparison arrangement. Say what each does and what the comparison is intended to reveal. Distinguish a proposed experiment from an observed one.

Specify the result at the detail needed for its use: total extension under a load, the location of a maximum, a response after a stated duration, or a distribution of repeated outcomes. Include the location, interval and preparation when they affect that result. A request for average deformation differs from a request for deformation at every point.

Identify what may change between the arrangements and what is fixed by the proposed work. The available fluid, gravitational acceleration, material, instrument range or support can constrain the construction. A control may be a time history rather than one setting. Preserve any known dependence between settings: changing temperature can alter both viscosity and density.

If the existing physical account already yields a sufficient answer, use it. Constructing another experiment is worthwhile when it supplies a contribution the work still needs. C.11.DUA helps choose between acting on a sufficient answer and obtaining more information.

#### PHY.1:4.2 - Recover the interactions that can change the requested result

Follow the physical route by which the proposed input affects the output. Identify the participants, interactions and constraints on that route. Include an exchange across the chosen boundary when it contributes to the result. In a deformation problem, distinguish the force applied at an end from weight distributed through the body. In a transport problem, distinguish material carried by motion from material spread by diffusion.

Use the applicable theory to express those contributions. B.5.TU supplies the passage from theory to the encountered case; A.3.3.TR helps when several interactions determine the same evolving state. State the physical premises still needed rather than filling an unknown interaction with a convenient equation.

Estimate the relative size or time scale of competing effects. Derive that comparison from their laws: which quantity multiplies each term, and what spatial or temporal variation makes the term large? In a regime where one effect is negligible for the output, retain the reason for that simplification and the conditions under which it can fail.

Bring the preparation into the same account. Geometry, contacts, constraints and initial conditions can alter the solution even when the material equations are unchanged. For a field, a boundary condition applies over a surface or interval; matching its value at one point may leave the intended problem different elsewhere.

#### PHY.1:4.3 - Express the comparison through meaningful scales

Choose reference quantities from the physical question. A reference length might be a gap rather than the total apparatus length; a response time might be compared with the duration of forcing. Explain that choice in the working terms.

For a quantity q, choose a positive reference magnitude Q with the same units and write `q=Q*q_hat`. The number q_hat is its value in that scale. When the law concerns a difference from a reference q0, use `q=q0+Q*q_hat` and carry q0 through the substitution. This matters, for example, when an absolute pressure and a pressure difference enter different relations.

Substitute the scaled quantities into the physical relations. Transform derivatives and integrals too: if `x=L*x_hat` and `t=T*t_hat`, then a time derivative contributes a factor 1/T and a spatial derivative a factor 1/L. Divide each equation by an appropriate nonzero reference contribution. The remaining coefficients show which relative effects must be compared.

For example, in a flow whose speed varies by order U over distance L, characteristic inertial acceleration is `U^2/L`, viscous acceleration is `nu*U/L^2`, and gravitational acceleration is g. Their ratios to the inertial contribution are `nu/(U*L)` and `g*L/U^2`. These ratios compare physical terms. A different physical account can introduce another contribution and another condition.

Scale the geometry and preparation as well as the equations. A prescribed forcing history is compared at corresponding scaled times; a boundary profile at corresponding scaled positions. Keep a separately imposed forcing duration as an independent condition unless the work makes it proportional to the chosen response time.

For many quantities, dimensional analysis can construct dimensionless combinations systematically. Choose a combination whose physical interpretation makes the comparison useful. MATH.11 supports the construction of quantities unchanged by stated transformations. Dimensionless dependence still needs the physical premises that selected the quantities and relations; it can leave an unknown function to be obtained through MMP.11 or other subject work.

#### PHY.1:4.4 - Construct settings that supply the needed correspondence

Write the original and proposed dimensionless relations together. Set equal the coefficients and preparation features needed by the intended transfer, then solve these conditions jointly with the available physical settings. MMP.10 supplies the constraint formulation when several choices interact.

The result may be a recipe: change length by one factor, forcing by another and reading time by a third. Check that the selected properties describe an available material or realizable arrangement. A material's stiffness and density, for example, may not be independently adjustable. Changing a support or adding a mass changes the physical account as well as a number.

When the scaled equations, domains and preparation coincide, express how a solution in the comparison variables becomes a solution of the original model. Include the output scale. C.29.1 supplies that transfer argument. If the model permits several solutions, the correspondence relates the permitted solutions; identifying one realized history requires the relevant physical preparation or selection conditions. Statistical predictions require the corresponding statistical account.

For a question about one output, try a weaker construction when reproducing the whole problem is unnecessary. Derive how that output depends on the settings and match the dependence needed by the question. Additional loading can reproduce total extension without reproducing local strain, as :5.2 shows. Keep the resulting comparison tied to the output it determines.

#### PHY.1:4.5 - Resolve a mismatch by its effect on the answer

If the conditions conflict, identify which physical contribution changes and how that could change the requested result. The conflict can itself rule out the proposed experiment at the chosen settings.

Choose the next move from the remaining physical possibilities. You can change a free setting, construct a different arrangement, retain a simpler physical regime, or derive how the unmatched contribution modifies the output. If several mismatched experiments are to be combined, construct the relation that permits that combination; a fitted relation retains its assumptions and the range over which it can be used. MMP.9 and MMP.11 can supply reduction and constrained model construction for these returns.

A small coefficient can support an approximation when its influence on the output is controlled. Inspect where that argument could fail. Thin boundary layers, a threshold, resonance or a long observation interval can make a nominally small contribution consequential. Derive a useful bound, compare an applicable limiting solution, or obtain a discriminating observation when it can settle the use. C.29.1 carries a bound through the later inference.

Use an existing result when it resolves the mismatch at the required strength. A conditional result or a limit can be enough. Additional measurement is selected by what its possible answers would change, including its cost, through C.11.DUA.

#### PHY.1:4.6 - Use the comparison and follow a changed question

Translate the obtained result into the original quantity, position and time. State the physical conditions on which that translation depends. A short derivation can supply the whole explanation; another contributor needs only the settings, correspondence and unresolved premises that change their use.

If a material experiment performs the comparison, include the effects of preparing, driving and reading it where they affect the inference. C.29.3 supplies this connection when the physical evolution performs a computation. A numerical solution has its own discretization and calculation errors under C.29.2. Keep those errors separate from a changed physical mechanism.

For a changed question, revisit the result first. Asking about a different location, time, range or intervention can make a previously omitted contribution relevant. Retain the conditions that still apply and reconstruct the affected comparison. B.5.MPC.R helps locate a failure across the physical account, mathematical representation and computation.

The useful continuation can be a proposed experiment, a design choice, an interpreted observation, a narrower claim or a new physical question. When the comparison suggests a different way for a team to obtain its result, use ME.7 to describe the proposed operations and their relations. ME.12 checks the claims on which that composition and its description rely and returns a correction to the affected contribution.

### PHY.1:5 - Archetypal Grounding

The following constructed cases derive conditional comparisons. The physical laws and idealizations used in each case are stated; no apparatus measurements are reported.

#### PHY.1:5.1 - Find conflicting requirements before building a smaller flow experiment

A team proposes a quarter-size free-surface water experiment to investigate a flow in which inertia, gravity and viscosity may affect the result. The proposed geometry is similar, gravitational acceleration is unchanged, and the same liquid is initially intended. Use an incompressible Newtonian-fluid account. A relevant surface-tension, compressibility or other omitted effect would add a condition to this account.

Let L be characteristic length, U speed, g gravitational acceleration and nu kinematic viscosity. Comparing the acceleration contributions from :4.3 gives the Froude and Reynolds numbers:

~~~text
Fr = U/sqrt(g*L)
Re = U*L/nu.
~~~

Write `L'=lambda*L` for the model length. To preserve Fr at the same g, solve:

~~~text
U'/sqrt(g*lambda*L) = U/sqrt(g*L)
U' = sqrt(lambda)*U.
~~~

The same liquid then gives `Re'/Re=lambda^(3/2)`. For lambda=1/4, the required speed is U/2 and Re'=Re/8. A corresponding transit time L'/U' is one-half of L/U. Those settings preserve the inertia/gravity ratio while changing the viscosity/inertia ratio.

If the desired output needs both ratios reproduced, changing speed alone cannot repair the comparison. At fixed g, solving both conditions requires `nu'=lambda^(3/2)*nu`, which is nu/8 in this case. Selecting a liquid with that viscosity remains a physical-material question, including its other properties. Alternatively, with the same liquid and variable effective gravity, the conditions give `U'=U/lambda` and `g'=g/lambda^3`. At quarter scale those values are `4*U` and `64*g`; the transit time is divided by sixteen. A rotating apparatus proposed to create that acceleration also introduces rotation and spatial variation that may affect the comparison.

The first result is a decision about the experiment. If viscosity is negligible for the intended output throughout the relevant regime, the Froude-scaled experiment may suffice under that approximation. If viscosity changes separation or another needed behavior, retain that dependence and change the arrangement or the method of obtaining the answer. Matching initial and boundary conditions remains part of either construction.

Now change the question from a large-scale surface response to a local viscous effect near a wall. The previous gravity-dominated approximation leaves the new output unsupported. The method returns to the relative contributions and near-wall scale; the old choice of speed remains useful only for the question it answered.

#### PHY.1:5.2 - Reproduce one deformation without claiming the whole field

Consider a straight uniform bar, fixed at the top, with an axial force F pulling down at the lower end. Let L be length, A cross-sectional area, Y Young's modulus, rho density and g gravity. Use small-strain linear elasticity and uniform material properties. Let x measure height from the bottom. The part below that point contributes weight `rho*A*g*x`, so the tensile force there is `F+rho*A*g*x`. Hooke's law gives local strain:

~~~text
strain(x) = F/(Y*A) + rho*g*x/Y.
~~~

Integrating from 0 to L gives total extension delta and mean strain:

~~~text
delta = F*L/(Y*A) + rho*g*L^2/(2*Y)
delta/L = F/(Y*A) + rho*g*L/(2*Y).
~~~

A geometrically similar bar made of the same material has `L'=lambda*L` and `A'=lambda^2*A`. To reproduce the applied-force contribution to strain, use `F'=lambda^2*F`. Its own weight instead changes by `lambda^3`. At unchanged g, the self-weight contribution to strain changes by lambda. Merely using a smaller copy with the same material does not reproduce the two load contributions together.

Suppose the original bar hangs under its own weight, with F=0, and the question concerns **only total extension relative to length**. An added lower-end force on the smaller bar can match that output. Solve the mean-strain equation for the new force:

~~~text
F' = A'*rho*g*L*(1-lambda)/2.
~~~

At quarter scale, F' is 3/128 of the original bar's weight. Substitution into the smaller bar's mean-strain equation gives `rho*g*L/(2*Y)`, the original value. The comparison therefore reproduces the requested normalized extension within this model.

Now ask for the strain at the lower end. The original unloaded bar has zero strain there; the smaller bar with the added force has `F'/(Y*A')` greater than zero. The output-specific construction cannot answer this new local question. To reproduce the complete strain profile, revisit the distributed loading or the combination `rho*g*L/Y`. The successful first comparison is retained for total extension.

#### PHY.1:5.3 - Preserve competing physical time scales

A substance diffuses along an interval and is consumed by a first-order reaction. A smaller comparison is proposed using the same diffusivity D and reaction rate k. Let c(x,t) be concentration, with the idealized equation:

~~~text
c_t = D*c_xx - k*c,   0 < x < L.
~~~

Both ends absorb the substance, so c(0,t)=c(L,t)=0. For a simple worked preparation take `c(x,0)=c0*sin(pi*x/L)`. Substitution gives:

~~~text
c(x,t) = c0*sin(pi*x/L)*exp(-(pi^2*D/L^2 + k)*t).
~~~

Use `x=L*xi` and the diffusion time `T=L^2/D`. At scaled time tau=t/T, the equation becomes `partial c/partial tau = partial^2 c/partial xi^2 - Da*c` on 0<xi<1, where `Da=k*L^2/D` compares reaction with diffusion. The midpoint concentration relative to c0 is `exp(-(pi^2+Da)*tau)`.

After L'=L/4 at unchanged D and k, the diffusion time is T/16 but Da becomes Da/16. If the original Da is 1, then at tau=1 the smaller experiment has a midpoint concentration exp(15/16), approximately 2.55, times the original normalized value. At that corresponding time, the smaller experiment has lost less substance to reaction.

To reproduce the dimensionless evolution with the same D, the smaller model would require `k'=16*k`, together with the corresponding initial and boundary conditions. A physical change intended to obtain that rate may change D too; solve using the resulting pair of properties. If the question instead concerns diffusion during an interval when consumption has a negligible effect, derive and use that shorter-time approximation. The reaction can re-enter when the requested duration changes.

### PHY.1:6 - Bias-Annotation

The explicit cases use classical continuum laws and positive scale factors because their derivations are easy to inspect. In a new regime, discreteness, quantum effects or a change in material behavior can invalidate such laws. Recover the applicable account before extending their scaling.

The worked algebra assumes access to the physical laws and a reader able to manipulate them. The prerequisites in :1 help locate a needed contribution. One participant can recover the interaction law while another derives the comparison settings; their shared explanation must preserve what the law describes and which settings the arrangement can supply.

### PHY.1:7 - Conformance Checklist

- The original question identifies the result and the proposed physical change.
- The relations and preparation contain the effects that can alter that result, with unresolved physical premises visible where used.
- Reference scales have physical meanings and compatible units; substitution covers the relevant spatial and temporal conditions.
- The comparison settings satisfy the required conditions together and can be supplied by the proposed arrangement, or their unresolved feasibility is stated.
- A limited or distorted comparison has a derivation or bound for the output it is used to answer.
- The result is interpreted at the original scale, with any preparation, computation and readout losses that change its use.
- A changed question returns to the affected physical contribution; an already sufficient result is used without compulsory extra experiments.

### PHY.1:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Build a smaller geometric copy and apply one scale factor to every result. | Derive how the contributing forces, rates and preparation change; :5.1 and :5.2 produce different factors for different contributions. |
| Match one familiar number while another relevant effect changes. | Recover the physical terms behind the requested output and solve their conditions together. |
| Treat all mathematically adjustable properties as independent apparatus settings. | Use the properties of an available material or arrangement, including changes induced by the same control. |
| Transfer an entire field from a comparison designed for one total. | Retain the output-specific result and reconstruct the comparison for the newly requested field or location. |
| Drop a small term without following its effect to the output. | Examine the relevant limit, interval and sensitivity; keep a bound or a more detailed account where that term changes the decision. |

### PHY.1:9 - Consequences

The construction can reveal an impossible experiment before equipment is built. It can also identify useful freedom: a different load, medium, time scale or restricted output may supply the answer with less work. A failed similarity condition becomes a physical design question rather than an unexplained disagreement between experiments.

The price is making the physical premises and coupled settings explicit. A complex account can require several comparisons or a numerical analysis. The method can reduce that work by selecting a sufficient output, but it cannot supply a missing physical law from dimensional consistency alone.

### PHY.1:10 - Architectural Rationale

Physical similarity is constructed from the effects that produce the requested answer. Choosing those effects before solving scale equations makes it possible to explain why a setting matters and to revise the comparison when the question changes. Comparing geometry alone would omit the different scaling of physical contributions. Requiring complete behavioral similarity for every use would exclude cheaper comparisons that preserve one useful result.

The physical and mathematical work remain connected. Physical reasoning supplies the laws, their regime and the realizable changes; mathematical operations expose joint conditions and transfer the consequence. Computation can solve those conditions or examine a mismatch. Their common inference and result-use methods are provided by FPF, while this pattern develops the physical scaling construction.

### PHY.1:11 - SoTA-Echoing

The working question is how to obtain a useful physical result after changing scale or conditions. The selected approach derives and reconciles the relevant physical ratios and preparation, then handles unmatched effects at the output that matters. It combines established similarity reasoning with explicit result-specific transfer and revision.

[Mahajan, The Art of Insight in Science and Engineering (2014), sections 5.2-5.3](https://ocw.mit.edu/courses/res-6-011-the-art-of-insight-in-science-and-engineering-mastering-complexity-fall-2014/3bca850386a3005c22134fa62fb3bad5_MITRES_6-011F14_art_insfin.pdf), provides a methodological anchor: dimensionless dependence can expose omitted physics while leaving an unknown coefficient or function. This changes :4.2-4.3 by making physical selection and the remaining unknown explicit. Its examples supply historical grounding rather than a complete current physics inventory.

[Price's 2024 MIT course](https://live.ocw.mit.edu/courses/res-12-001-topics-in-fluid-dynamics-fall-2024/pages/essay-2-dimensional-analysis-of-models-and-data-sets-similarity-solutions-and-scaling-analysis/) emphasizes selecting a physically useful dimensionless basis and relating coefficients to competing terms. Adopt that choice in :4.3. [NASA's explanation of similarity parameters](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/similarity-parameters/) makes viscosity and compressibility consequences tangible. The warning is applied to effects relevant to the requested output; differing parameters can still permit a useful limited approximation.

[Li et al. (2021), Spatial and temporal scaled physical modeling of fluid convection using hypergravity](https://arxiv.org/abs/2103.16028), report a way to reconcile gravity and viscosity scaling and identify limitations introduced by the apparatus. Their abstract motivates the changed-gravity alternative in :5.1. That case derives the scale factors from its stated conditions; reproducing the reported experiments requires their full apparatus method.

An alternative to a single matched comparison is reconstructing a result from several scales. [Davey and Ochoa-Cabrero (2023), section 2.2](https://doi.org/10.1007/s10665-023-10296-1), derive finite-similitude combinations under additional assumptions about scale dependence. This keeps the multiple-experiment return in :4.5 available when simple matching fails. Their higher-order construction has its own assumptions; the present method does not supply its full calculus or infer them from several measured points.

The output-specific loading and changed-question cases are this publication's conceptual synthesis. Revisit the selected account when a new regime, source result or failed comparison changes a physical premise, available setting or valid approximation. New material or computation can make a previously infeasible comparison useful.

### PHY.1:12 - Relations

B.5.FM and B.5.TU supply first-model construction and theory use when the physical account is still being formed. A.3.3.TR supplies state and the joint representation of change. B.5.MPC connects the physical, mathematical and computational contributions; B.5.MPC.R locates a failed connection after a change.

MMP.10 formulates coupled conditions; MMP.11 constructs unknown dependence; MMP.9 derives reduced evolution where eliminating detail exposes an unresolved contribution. MATH.11 constructs invariants from transformation rules. C.29.1 supplies the mathematical transfer or bound, C.29.2 the computation, and C.29.3 its realization through physical action and readout.

C.11.DUA selects further inquiry by what it could change and what it costs. ME.7 develops the proposed composition of the working method; ME.12 checks its claims and description when the comparison changes how participants obtain a result.

### PHY.1:End

## PHY.2 - Construct a Physical Analogue from Interactions

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### PHY.2:1 - Problem frame

Use this pattern when you want to understand or investigate a physical situation through another arrangement, and the needed analogue must be built or changed. You may know the target's laws but need an arrangement that makes their consequences accessible. Or you may be exploring an unresolved mechanism and need to construct a physical possibility that produces a consequence worth pursuing.

Here the **target** is the situation about which you want to learn. The **source** is the physical arrangement whose behavior supplies the analogy. The source may first be a thought construction: interacting bodies, material, fields or devices whose behavior can be reasoned about. It can then be expressed mathematically, simulated or built, according to the contribution the work needs.

Start with one target behavior and ask what physical interaction could produce it in a source. If two target parts affect one another, for example, ask what connection in the proposed source transmits that influence. The first result is a source construction, a consequence obtained from it, and an account of what that consequence permits you to infer or try in the target.

You need the relevant physical laws or someone able to supply them, together with the mathematical or qualitative reasoning required by the proposed construction. A ready analogue with a sufficient explanation of its use can be used directly. PHY.1 helps when the remaining difficulty is constructing conditions for a change of scale. C.29.1 helps when the physical constructions are already available and the unresolved work is the correspondence between their mathematical descriptions.

### PHY.2:2 - Problem

A resemblance can suggest an analogy while leaving the source unable to produce the behavior that matters. Two components that behave appropriately in isolation can behave differently when connected. A source can also reproduce one target observation through a mechanism that gives a different response to an intervention.

The difficulty is building the source itself. Its components, interactions, preparation and surroundings must jointly produce a useful consequence. When the target mechanism is unresolved, construction and criticism of the source also refine the hypothesis about the target. An unsuccessful source can expose the missing interaction or a physical restriction that the next attempt must address.

### PHY.2:3 - Forces

| Choice | What it changes |
| --- | --- |
| Familiar mechanism or relevant behavior | An accessible mechanism helps reasoning only to the extent that its consequences address the target question. |
| Separate components or coupled operation | A connection can impose a constraint, transfer energy, change loading or introduce another state. |
| Manipulable source or faithful target consequence | Making the source easier to prepare and observe can alter a relation needed for the intended inference. |
| Known target law or proposed target mechanism | The former can support a derived transfer; the latter can yield a hypothesis and a discriminating next move. |
| One construction or complementary constructions | Different sources can expose different consequences, while disagreement can locate an unresolved premise. |

### PHY.2:4 - Solution

**Choose the target consequence → propose physical mechanisms for it → connect their interactions → recover preparation and correspondence → derive or produce a consequence → use it and revise the construction.**

#### PHY.2:4.1 - Choose what the source must help you obtain

State the target question in the terms of the work. You might need a response to an input, a possible mechanism for an observed change, a limit on a proposed behavior, or an arrangement that lets you manipulate an otherwise inaccessible relation. Say what is already known and what remains proposed about the target.

Follow the intended consequence to the relevant participants and interactions. A force on one body may change another through a stored deformation; a change at a boundary may propagate through transport. Recover the target relation that the source must help explain or use. B.5.FM and B.5.TU support this first account and its relation to a theory.

Keep the first construction as small as that question permits. For a question about coupling, two interacting parts can expose what a whole-device sketch leaves implicit. If the target mechanism is unknown, begin with an observed dependence and a proposed way it could arise. The proposal gives something to develop even before a complete target theory is available.

#### PHY.2:4.2 - Propose mechanisms by the physical effect they supply

Ask what the source must retain, transfer, resist, amplify, constrain or change. Then choose physical processes that can perform those contributions under known laws. These are prompts for selecting relevant effects, not a required inventory of every source.

For example, a mass retains motion while a force changes it; a deformable body stores energy under loading; a capacitor accumulates charge while current flows; a dissipative interaction converts organized motion into less accessible energy. A driven body can maintain motion by drawing on an energy supply. A stochastic transition account can express unresolved switching between physically different states. Choose among such mechanisms from the target relation and the proposed source conditions.

Write or explain the law of each chosen interaction, its participants and its regime. Include direction and sign: a coupling can restore a displacement or increase it. Identify what is being approximated when a law is linearized or treated as instantaneous. When no suitable law is available, retain the interaction as the physical contribution still to be found.

A source can combine contributions from several familiar arrangements. Derive the behavior of that combination. A chain of separately plausible resemblances can leave an unconstructed connection in the middle; locate the participants and interaction at that connection. Mathematical formulation through MMP.10 or MMP.11 makes the resulting conditions easier to solve.

#### PHY.2:4.3 - Construct the connection and its effect on the whole

For each connection that carries the target influence, identify what the connected parts share and what each can exchange. Write the interaction conditions together with the component laws. At an electrical junction, current conservation and common voltage connect the components; in a mechanical contact, the allowed motion and transmitted forces do that work. Other interactions need their own physical conditions.

Recover the state needed to continue the coupled behavior. The source may need a relative deformation, stored charge, field or direction of motion that neither isolated-component sketch retained. A.3.3.TR supplies the general state and joint-change construction. Here identify the physical means by which the additional state persists and affects the next change.

Check the physical restrictions that can defeat the construction. For an energy-carrying interaction, account for the relevant storage, exchange, dissipation and driving. A source that uses only passive dissipative elements cannot supply sustained amplification; an active source needs an identified supply. For a transport or switching mechanism, include the travel time, waiting law or constraint that changes the intended result. The useful restriction depends on the source, so follow it to the target consequence.

Use these restrictions to improve the construction. Add the missing coupling, replace an unsuitable element, change a boundary or keep a result limited to the regime the source can produce. If the target's required relation conflicts with the source's physical laws, choose another source or revise the hypothesis. This conflict is an informative result of construction.

#### PHY.2:4.4 - Recover preparation, interpretation and available range

Describe how the relevant source state starts and how it is driven. The initial deformation of a target spring, for example, can require stored current in an electrical source. Setting every source state to zero would solve a different initial-value problem. Likewise, the preparation of a distribution includes more than its mean when its later behavior depends on that distribution.

Connect each source quantity used in the result to what it represents about the target. Include units and scales: source voltage may represent target velocity through a dimensional conversion, and source time may run faster. Derive that correspondence by substituting the conversion into the laws and preparation. C.29.1 provides the general argument that a source result transfers to the intended mathematical target.

When proposing a material realization, determine whether its components can supply the required signs, ranges and rates together. Include the effect of observing or driving the source if it changes the relevant behavior. A nominally passive observation can load an electrical node; a finite switching time can matter when the requested event is short. C.29.3 supplies the preparation, action and readout relation for physical computation.

For a thought construction, state the physical idealizations on which its consequence depends. That conditional result can already direct a useful change or inquiry. Building an apparatus is a further choice, selected when its outcome would add a worthwhile contribution through C.11.DUA.

#### PHY.2:4.5 - Obtain a consequence and determine its reach

Manipulate the source according to its proposed laws. Start with a small input, a change of one interaction, or a limiting case that exposes how the construction works. Obtain the consequence by a derivation, a qualitative physical argument, a computation or an experiment. Use a known limiting case to find an omitted interaction or a sign error where it can discriminate between constructions.

Trace the obtained consequence back through its physical and mathematical premises. A computation can determine a property of the proposed source model. Interpreting an apparatus reading adds the account of the apparatus. Applying either result to a physical target adds the target correspondence and the physical premises used there. An existing explanation can supply those premises; no new evidence collection follows merely from enumerating them.

If the target mechanism remains proposed, use the result as a consequence of that hypothesis. Ask what change would make competing mechanisms disagree. This can reveal a useful intervention, a different observation interval or a parameter relation to examine. MMP.7 helps when the proposed distinction must be expressed through recorded data; C.11.DUA determines whether obtaining that distinction is worth the effort.

Different sources can contribute complementary results. One may expose an invariant or a bound, another the effect of noise or a difficult regime. Compare them for the usefulness, range and cost of the required contribution. G.5 distinguishes alternatives retained for later choice, non-dominated candidates and a set whose members contribute together. E.23 supports repeated improvement when a stated evaluation can judge the changed source.

#### PHY.2:4.6 - Return to the target and change the useful part

Use the result in the target work: choose a preparation, interpret an observation, propose a mechanism, reject a construction, or change the design of an experiment. Explain the physical route that makes the result relevant. EXD.3, in Explanation Design DPF, helps coordinate the words, diagram and equations another participant needs to recover that reasoning. C.2.8 characterizes the structure a recipient can extract with their available preparation and effort.

When a consequence fails or the question changes, locate the affected connection. Did the chosen source law fail, did connection change the source behavior, did computation or observation distort the result, or did the target correspondence omit an important difference? B.5.MPC.R supports this diagnosis. Revise the physical mechanism, state, preparation or correspondence that the failure implicates and retain the contributions that still work.

Keep a newly revealed question when pursuing it could open useful action. The next task can concern the target, the source or their connection. If the new construction changes what participants must produce or how their contributions join, ME.7 helps develop that proposed composition. ME.12 checks claims about the method and its description, and locates the contribution that needs correction.

### PHY.2:5 - Archetypal Grounding

These constructed examples show two uses: obtaining consequences of a known physical account and developing a proposed physical mechanism. The calculations describe idealized sources; they report no apparatus measurements.

#### PHY.2:5.1 - Build the missing coupling in a mechanical/electrical analogue

Two bodies move along a line, joined by an ideal spring. Let their masses be m1 and m2, velocities v1 and v2, and the spring extension be d. External forces are f1 and f2; linear drag coefficients b1 and b2 are nonnegative. With spring stiffness k>0, the physical laws are:

~~~text
m1*dv1/dt = f1 - b1*v1 - k*d
m2*dv2/dt = f2 - b2*v2 + k*d
dd/dt = v1 - v2.
~~~

The question is how a deformation transfers motion between the bodies. Two independent electrical elements for the masses would omit that interaction. Choose node voltages to represent velocities, injected currents to represent external forces, and charge-accumulating capacitors for the masses. A conductance from each node to the reference node can represent its drag. The missing coupling needs a state whose rate is proportional to the difference of the two voltages. An inductor connected between the nodes supplies that relation.

Let `s=r*t` be source time, `V_i=a*v_i` the voltages and `I_i=h*f_i` the injected currents, with positive dimensional conversion factors a and h and positive time ratio r. Let J be current through the inductor from node 1 to node 2. Current conservation and the ideal inductor law give:

~~~text
C1*dV1/ds = I1 - G1*V1 - J
C2*dV2/ds = I2 - G2*V2 + J
L*dJ/ds = V1 - V2.
~~~

Substitute the conversions and `J=h*k*d`. All three relations match the mechanical account when:

~~~text
C_i = r*h*m_i/a
G_i = h*b_i/a
L = r*a/(h*k).
~~~

The constructed inductor carries the coupling state. The initial source state must satisfy `V_i(0)=a*v_i(0)` and `J(0)=h*k*d(0)`. For m1=2 kg, m2=1 kg, k=3 N/m, d(0)=1 m, zero velocities and zero applied forces, the first accelerations are -1.5 and +3 metres per second squared. The prepared inductor current produces the corresponding voltage changes. With J(0)=0, the source would instead remain at rest and miss the deformation-driven motion.

The stored mechanical energy is `(m1*v1^2 + m2*v2^2 + k*d^2)/2`. Differentiating gives power `f1*v1 + f2*v2 - b1*v1^2 - b2*v2^2`. The circuit's stored energy is `r*a*h` times the mechanical energy; its supplied and dissipated powers have the compatible factor `a*h`. The correspondence therefore includes storage and transfer under the stated ideal laws.

The first result is a source design and interpreted initial response. Before building it, choose the conversion factors so capacitances, conductances, inductance, voltages and currents lie in the available ranges. Include losses or loading that would alter the requested response.

Now change the target: a controller supplies a force that increases with velocity, producing effective negative damping over a stated range. A nonnegative conductance cannot realize that contribution. The changed physical construction needs an active element and its energy supply, or another means of obtaining the result. The previously constructed passive analogue still answers the original dissipative question.

#### PHY.2:5.2 - Construct a mechanism whose short-time consequence differs from diffusion

A spreading population of moving particles is approximately diffusive over long observations. The target question is whether that approximation can describe the first short interval after a localized release. Consider a proposed mechanism in which motion persists for a while before its direction changes.

Build a simple source in thought: independently driven shuttles on a line move at speed u, reversing direction at random times. The waiting times are independent exponentials with reversal rate lambda. A drive maintains the speed, and a controller supplies the reversals. Treat reversal duration as negligible relative to the intervals being considered. This source combines sustained physical motion with stochastic switching. Using it for the particles proposes a relation between their direction persistence and their observed spreading.

The motion already supplies a useful qualitative consequence. Starting at x=0, a shuttle travels path length `u*t` in elapsed time t; reversals can only reduce its distance from the start. Thus `abs(x(t)) <= u*t`. Reaching a point at distance d requires at least time `d/u`. An ideal diffusion law with positive diffusivity instead assigns positive probability beyond every finite distance at every positive time. These are different predictions even when their long-time spreading agrees. An arrival before `d/u` would contradict the proposed bounded-speed target mechanism under its stated speed and preparation. Whether an earliest-arrival observation would discriminate the mechanisms also depends on its resolution and on the probability predicted for such arrivals. The bound is already a source result; the target correspondence remains a hypothesis.

For a small interval dt, reversal has probability `lambda*dt` to first order. If p_plus and p_minus are the position densities of right-moving and left-moving shuttles, transport and exchange between the two states give:

~~~text
partial_t p_plus  = -u*partial_x p_plus  - lambda*p_plus + lambda*p_minus
partial_t p_minus = +u*partial_x p_minus + lambda*p_plus - lambda*p_minus.
~~~

The total density is `p=p_plus+p_minus` and the flux is `j=u*(p_plus-p_minus)`. Adding and subtracting the equations yields:

~~~text
partial_t p = -partial_x j
partial_t j = -u^2*partial_x p - 2*lambda*j.
~~~

Direction is the additional state that lets the source retain motion between changes. Omitting it too early would erase the short-time effect under investigation.

Release all shuttles at x=0 with equal probabilities of the two directions, on an unbounded line. The mean position stays zero. Multiplying the equations by x and `x^2` and integrating, with vanishing boundary terms, gives for the mean-square displacement M(t):

~~~text
M''(t) + 2*lambda*M'(t) = 2*u^2
M(0) = M'(0) = 0
M(t) = (u^2/lambda)*[t - (1-exp(-2*lambda*t))/(2*lambda)].
~~~

At short times M(t) is approximately `u^2*t^2`: particles mostly retain their direction. At long times its leading growth is `(u^2/lambda)*t`, corresponding to diffusion coefficient `D=u^2/(2*lambda)`. The source thus produces a long-time diffusion law while giving a different short-time consequence. If u and lambda both have numerical value 1 in the chosen units, M(1) is approximately 0.568 square length units, while the leading diffusion expression gives 1.

The first result is a conditional explanation and a candidate change of observation interval. Long-time diffusive behavior alone leaves the proposed persistence mechanism unresolved. A useful return is to compare direction correlation or early spreading when either could distinguish it from a competing mechanism. An existing measurement can suffice. A physical shuttle apparatus adds no value if the derivation already supplies the consequence the work needs.

Now suppose target turns have an appreciable duration, or their occurrence depends on how long the present run has lasted. The source's instantaneous, memoryless reversal rule no longer supplies that target behavior. Construct the missing turn state or waiting-time dependence, recover its physical interpretation, and derive its effect on the requested interval. The previous model remains a limiting construction where those effects are negligible. For a material shuttle implementation, finite acceleration also limits how short an interval it can reproduce.

### PHY.2:6 - Bias-Annotation

The worked cases use classical interaction laws and stochastic switching that can be manipulated through ordinary differential reasoning. Other physical regimes can require different permitted states, transformations and observations. Reuse the construction method with the physical laws of that regime; the elementary sources here supply examples of it.

A familiar source can be easier to imagine than a suitable one. Follow the behavior required by the target question when choosing and revising mechanisms. Collaborators can supply unfamiliar physical contributions. Human mental-model studies motivate part of this approach; applying the method with AI contributors requires checking the construction they actually produce and the prerequisites its users possess.

### PHY.2:7 - Conformance Checklist

- The target question and the source's intended contribution can be stated in working terms.
- Proposed source mechanisms have physical laws and conditions sufficient for the consequence being obtained, or the unresolved contribution is identified.
- The connection includes the interaction, retained state and physical restrictions that can alter the result.
- Preparation, driving, interpretation and any scale conversions describe the same constructed case.
- A derived or produced consequence leads to an appropriate target inference, intervention, design choice or further question.
- A proposed target mechanism retains the premises still needed to use it; further inquiry is chosen by its possible contribution and cost.
- A changed question or failed consequence returns to the affected mechanism or correspondence while preserving useful existing results.

### PHY.2:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Give components corresponding names but leave their interaction unbuilt. | Construct the connection's physical law and state, then derive the coupled behavior. |
| Reuse isolated-component behavior after connecting a load that changes it. | Include the loading or derive conditions under which its influence is negligible for the output. |
| Start every source state at zero while the target contains stored deformation or another prepared state. | Map and realize the preparation used by the target question. |
| Treat one reproduced observation as enough to identify the target mechanism. | Derive a consequence on which plausible mechanisms differ, or keep the explanation conditional when that suffices. |
| Change a coefficient past the range an available mechanism can supply. | Reconstruct the physical source, including a required drive or new state, or retain the result in its applicable range. |

### PHY.2:9 - Consequences

The method can create a useful source where retrieval of a ready analogy fails. Construction exposes missing interactions, incompatible physical requirements and consequences that were difficult to see in the target. Those discoveries can refine both the source and the question.

Its cost is reasoning about two physical situations and their connection. An elaborate apparatus or simulation can be unnecessary when a short construction already answers the question. The source can also become misleading if its convenient mechanism is carried into the target beyond the inference it supports.

### PHY.2:10 - Architectural Rationale

The operative contribution is constructing physical mechanisms that can work together. Correspondence becomes usable after there is enough source behavior to compare. Preparation, coupling and the means of producing an effect therefore belong inside construction, where they can change the selected source.

The method accommodates both a known target account and development of a target hypothesis. Their first results differ: a derived transfer can answer a target question under its physical premises; a proposed mechanism can reveal a consequence that directs inquiry. This keeps early physical imagination useful while making the strength of its result recoverable.

FPF supplies common first-model reasoning, state construction, correspondence, computation and inquiry choice. Mathematical Thinking and MMP supply the required mathematical operations and formulation methods. The physical contribution here selects interactions, their connections and their attainable behavior. A circuit or a moving-shuttle construction demonstrates that contribution.

### PHY.2:11 - SoTA-Echoing

The working question is how to construct a useful physical source when no ready analogue supplies the required behavior. The approach combines iterative source construction with explicit physical interactions, preparation and result use.

[Nersessian (2025), section 3](https://onlinelibrary.wiley.com/doi/10.1111/tops.12777), examines scientific cases in which the analogy source is itself developed through construction and manipulation. Adopt that contribution in :4.2-4.6: source revision can refine the target problem as well as its candidate solution. Her studies support a human scientific practice; the allocation of work among people and AI here is a methodological extension.

[De Benedetto and Poth (2025, first online 2024), section 3.1](https://doi.org/10.1007/s13164-024-00752-x), reconstruct how combined representational resources can create new inferential possibilities. This supports keeping mechanisms from different sources available during construction. The present pattern develops the physical work of connecting them rather than adopting their full theory of concept learning.

[Hangleiter, Carolan and Thebault, Analog Quantum Simulation (2022), sections 8.3.3-8.4](https://arxiv.org/pdf/2303.00814), distinguish the source apparatus, its mathematical description, the formal target and the physical target. Their analysis changes :4.4-4.5 by locating the premise needed for each inference. The general connection is reused from C.29.1 and C.29.3. Their validation discussion is applied according to the conclusion needed; a conditional hypothesis remains a useful result when a stronger target claim is unresolved.

[Angelani (2016), section 2](https://arxiv.org/pdf/1601.04845), supplies a transparent transport-and-switching construction for the second worked case. His tumble events choose a new direction, whereas lambda here counts actual reversals; the rate convention is stated in the case. [Datta, Beta and Grossmann, version 3 of The random walk of intermittently self-propelled particles](https://arxiv.org/html/2406.15277v3), makes richer run/turn dynamics and waiting-time distributions available. Its section II supports the return when the simple switching assumption fails. The one-dimensional shuttle example is a constructed illustration, not a reproduction of those authors' apparatus or a complete active-matter model.

The dimensional circuit construction and paired changed-condition uses are this publication's synthesis. Revisit a source choice when a new law, available mechanism or observed disagreement changes the correspondence or reveals a useful physical possibility. A new example alone leaves the general method unchanged.

### PHY.2:12 - Relations

B.5.FM and B.5.TU connect the target question with an initial physical account and theory. A.3.3.TR supplies the general construction of state and combined change. PHY.1 develops physical similarity conditions when scaling or changing a material is the operative problem.

C.29.1 establishes the correspondence used in inference; C.29.2 formulates the computation; C.29.3 connects a physical realization with preparation and readout. MMP.10 and MMP.11 formulate and develop the mathematical relations. MMP.7 connects a proposed physical distinction with a model of recorded observations. MMP.9 supplies the mathematical reduction when removing a physical state changes the retained evolution.

G.5 distinguishes the results of choosing alternatives or complementary contributions; E.23 governs repeated improvement under a stated evaluation. C.11.DUA selects worthwhile inquiry and use of sufficient results. B.5.MPC and B.5.MPC.R connect the physical, mathematical and computational contributions and locate a failure between them. C.2.8 characterizes extractable structure, and EXD.3 helps express the explanation; ME.7 develops the proposed composition account; ME.12 checks its claims and locates a needed correction.

### PHY.2:End

## PHY.9 - Construct a Measuring Interaction for a Physical Distinction

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.9:1 - Problem frame

Use this pattern when a physical difference matters to the work, but the available arrangement does not make that difference observable. You may need to choose a sensing effect, prepare a reference, separate a wanted response from another influence, or change a probe that disturbs its subject.

The first result is a proposed measuring interaction with a usable response: what to prepare, what to couple, what to observe, and which physical differences the response can resolve. It can remain conditional on an identified coupling, calibration or operating range.

C.16.MR constructs the relation between a sought property and an indication. This method develops its physical realization when that realization is missing or inadequate. The work concerns designing an interaction, before or after a measurement exists. It need not produce a new instrument; changing a preparation or comparison can suffice.

You need to interpret the relevant physical theory and the conditions under which its effect occurs. Mathematical or experimental collaborators can supply calculations and implementation while you retain the wanted distinction. The examples supply their additional mechanical, fluid and quantum premises.

Use an existing arrangement and calibration when they already resolve the question. If the physical arrangement is suitable and only inference from its records remains, use C.16.IR or MMP.7. A more elaborate sensor is unnecessary when the present response already supports the decision.

### PHY.9:2 - Problem

A property can affect a physical system without appearing in the chosen readout. Mass occurs in the force and inertia of a falling body but cancels from ideal gravitational acceleration. A field can change a quantum state's phase while the selected measurement remains insensitive to it.

A responsive instrument can also confuse the sought property with its own interaction. A capillary responds to pressure through a liquid column, but surface forces contribute to the height. Repeating the same reading more precisely does not separate those contributions.

The difficulty is to construct a physical comparison that exposes the wanted difference under the available conditions.

### PHY.9:3 - Forces

| Force | Tension |
| --- | --- |
| Coupling and selectivity | A strong response can amplify an unwanted influence as well as the target. |
| Preparation and observation | The same interaction can be informative for one prepared state and uninformative for another. |
| Reference and portability | A comparison can remove an unknown contribution while depending on shared physical conditions. |
| Signal and disturbance | The probe can make a difference visible while changing the quantity whose earlier value was wanted. |
| Local sensitivity and usable range | A steep response can improve a local estimate while leaving distant possibilities indistinguishable. |
| Improved measurement and effort | Another interaction is useful only when its added distinction matters enough to the receiving work. |

### PHY.9:4 - Solution

**Choose the wanted distinction → select a responsive physical effect → construct the preparation and comparison → derive the readout and its disturbance → determine what can be resolved → revise the arrangement where needed.**

#### PHY.9:4.1 - Specify the physical distinction and conditions

Name two physical possibilities that the work needs to distinguish, or a quantity range within which an estimate is needed. State where and when the property is sought. A pressure before connecting a probe and the pressure maintained during readout can be different targets.

Choose the needed consequence. Detecting a change, estimating a value and deciding which side of a limit applies place different demands on the same arrangement. C.16 provides the characteristic and scale; C.16.IR determines what a given indication can resolve.

Include the conditions the work permits you to change. A prepared reference, imposed force, interrogation time or detector orientation is a potential experimental choice only when it can actually be controlled.

#### PHY.9:4.2 - Choose an effect that carries the distinction into a response

Find a physical interaction through which the sought difference changes a state, transition, force, flow or other observable response. Derive that dependence far enough to see whether the proposed readout retains it. PHY.4 can constrain an unknown law; PHY.6 or PHY.7 can construct the relevant physical evolution.

Compare a small number of plausible arrangements. For each, ask what differs in the predicted readout between the selected physical possibilities under the same preparation. Reject an insensitive arrangement for this question even if it uses a well-established effect. The falling-body case in :5.1 shows why the occurrence of a quantity in one equation is insufficient.

Identify what supplies a reference. A known imposed quantity, a second preparation or a stable response can make the comparison interpretable. State the physical relation that allows the reference to be transported into this measurement. Numerical labels on two devices do not establish that relation.

Retain an unknown coupling as unknown. An available bound or a calibration can be enough; a proposed response without grounds for its coupling remains conditional. Select new characterization only when it can change the intended use.

#### PHY.9:4.3 - Construct the preparation and comparison

Specify how the subject, probe and reference are prepared before coupling. Then choose what is held fixed, what is varied and what is read. Include the order when the first interaction changes the next state.

Use a differential, reversed, ratio or null comparison when its physical invariance removes a consequential influence. Derive the cancellation from the arrangement. For example, reversing a known applied force while preserving a common force offset changes the wanted response but leaves the offset shared. A reversal that also changes the offset does not support that subtraction.

For a quantum probe, choose a prepared state, the parameter-dependent interaction and the measurement together. The physical interaction may be described by a channel taking rho to rho_theta; measurement operators E_k give outcome probabilities `P(k|theta)=Tr(rho_theta E_k)`. Here rho is the prepared state, theta the sought parameter, and the positive operators E_k sum to the identity. If those probabilities do not change with theta, that preparation and readout supply no information about it.

A reference can also select which part of a response is read. A phase-sensitive measurement needs a phase reference; a differential displacement needs a reference position. Preserve the conditions that make this reference stable during the comparison.

#### PHY.9:4.4 - Include the effect of measuring on the subject

Construct the coupled subject-probe account for the duration that matters. Determine whether connecting the probe changes the sought quantity, changes only another quantity, or leaves its relevant value effectively unchanged. Use the physical coupling rather than a universal claim that measurement must disturb the target.

If the wanted value precedes coupling, derive how it can be recovered from the disturbed response, or change the arrangement to reduce the consequential disturbance. Keep uncertainty in that recovery. When correction is poorly determined, a different interaction or a conditional range can be more useful than more decimal places.

Compare the retained effect with the allowed error or decision margin. Loading, finite response time and backaction matter through their consequences for this question. PHY.5 helps justify an approximation. A usable result does not require modeling every interaction.

A nondestructive or non-demolition measurement protects a specified property under particular conditions; it does not establish that every later use of the subject is unaffected. Preserve any disturbance that changes the receiving experiment or work.

#### PHY.9:4.5 - Determine the distinctions the readout supports

Compose the physical response with the actual recording procedure through C.16.MR. Use MMP.7 when the conclusion requires a probability law for those records. Retain common influences, saturation, timing and finite resolution when they affect the conclusion.

Determine whether different target values remain compatible with the same possible records. If they do, identify which interaction, preparation or readout could separate the relevant alternatives. A local slope measures a local response; it does not resolve a periodic ambiguity or a shared unknown parameter.

Use the uncertainty or error model appropriate to the inference. Strongly nonlinear conversion can change both an estimate and its uncertainty; do not assume that converting an average is equivalent to averaging the converted quantity. Apply the necessary mathematical propagation or inference method, rather than treating a sensitivity coefficient as a complete answer.

When several parameters or performance goals matter, compare achievable combinations under the available resources. Different measurements can favor different parameters. Use C.16 to characterize those combinations and C.11 when choosing between available arrangements.

#### PHY.9:4.6 - Obtain a first result and revise the physical arrangement

Work one admissible preparation through to a predicted readout and an interpreted result. This can reveal an unresolved physical relation before an instrument is built. It also gives collaborators a concrete construction to implement or compare.

Change a condition that could defeat the intended use. Check the shared premise of a subtraction, the range of an inverse, the time available for a response or the disturbance caused by the probe. Return to the smallest implicated part of the arrangement.

Use available observations where they can change confidence or selection. C.11.DUA helps choose between another measurement, a conditional result and proceeding with uncertainty. A statistical comparison or a calibration certificate does not substitute for a missing physical response.

Return the proposed arrangement, its preparation and readout, the result it supports and the conditions that would change that use. The next work may be implementation, calibration, inference or a different measuring interaction. PHY.10 constructs a physical test when the purpose is to separate rival accounts.

### PHY.9:5 - Archetypal Grounding

#### PHY.9:5.1 - Make mass affect the observation

Two bodies fall in a sufficiently uniform gravitational field with negligible drag. The equation `m a=m g` gives a=g. Timing their fall cannot distinguish their masses in this idealization, even though gravity exerts different forces.

Choose instead a known horizontal applied force F whose generation does not depend on the unknown mass. Track the body's acceleration under that force. With other horizontal forces negligible, `m a=F` gives `m=F/a` for nonzero a. The physical change is from a force proportional to the unknown mass to an independently supplied force.

Now a constant horizontal force offset b matters during the short observation. Use two otherwise identical preparations with applied forces +F and -F. Assume the same b and the same mass in both, and measure their initial accelerations:

`m a_+=F+b`, `m a_-=-F+b`.

Subtracting gives

`m=2F/(a_+-a_-)`.

With F=6 N, a_+=4 m/s² and a_-=-2 m/s², the mass is 2 kg and b=2 N. Using only F/a_+ would give 1.5 kg. The controlled reversal made mass distinguishable from the shared force offset.

The two preparations must preserve that offset. Velocity-dependent drag need not do so after the trajectories diverge. Measuring comparable initial responses, including the changed drag law, or selecting another arrangement can repair that use. Taking more samples of two physically different offsets does not justify the shared-b subtraction.

The acceleration readout and the force reference retain their own calibration and uncertainty. A decision whose margin exceeds those effects can use the mass estimate; a tighter use returns to the consequential contribution.

#### PHY.9:5.2 - Separate pressure from the probe's surface force

A large liquid reservoir maintains an unknown gauge pressure p during a small probe's readout. A vertical circular capillary opens to the atmosphere. Let rho be liquid density, g gravitational acceleration, r the tube radius and h the meniscus height above the pressure reference. Assume hydrostatic equilibrium and a capillary regime in which the meniscus curvature is described by the wetting angle theta.

Hydrostatic pressure and the surface-pressure jump give

`p=rho g h - s/r`, where `s=2 gamma cos(theta)`

and gamma is surface tension. The height responds to the wanted pressure and to the capillary surface force.

If s is unknown but the same surface condition can be prepared in two narrow tubes of radii r_1 and r_2, use

`rho g h_1=p+s/r_1`, `rho g h_2=p+s/r_2`.

For distinct radii,

`p=rho g (r_1 h_1-r_2 h_2)/(r_1-r_2)`.

Take rho g=10000 Pa/m, r_1=0.1 mm, r_2=0.2 mm, h_1=0.20 m and h_2=0.15 m. The inferred pressure is 1000 Pa and s=0.10 N/m. Interpreting the first height as p=rho g h_1 would give 2000 Pa. Both narrow radii must remain within the chosen capillary approximation.

Now suppose the two surfaces have different, unknown wetting conditions. The equations contain separate s_1 and s_2. The cancellation no longer determines p: two readings with three unknown quantities leave a consequential freedom. Restore the common surface condition, use useful bounds on the surface terms, or select another pressure-sensitive interaction.

The reservoir premise also matters. If filling the capillary changes the pressure whose earlier value was wanted, include the reservoir-probe volume and pressure relation through PHY.6 and C.16.MR. The maintained-pressure calculation cannot by itself recover that earlier value.

#### PHY.9:5.3 - Prepare a probe whose phase difference can be read

An ideal two-level probe couples to a constant classical field B through

`H=(hbar gamma B/2) sigma_z`,

where gamma is a known coupling coefficient and sigma_z has eigenvalues +1 and -1 for states |0> and |1>. Treat the field as unchanged by this probe during the interrogation time t. The wanted quantity is B within a supplied range.

Prepare |0>. Evolution multiplies it by a global phase; measurements of this state cannot reveal that phase. Increasing t alone does not create a readable field dependence.

Instead prepare `|+>=(|0>+|1>)/sqrt(2)`. Evolution produces a relative phase `phi=gamma B t`. Reading sigma_z still gives equal probabilities and is uninformative about phi. A controlled rotation before detection permits a sigma_x or sigma_y measurement. Their means are cos(phi) and sin(phi), so the two preparations for readout can recover phase modulo 2 pi. Each mean requires the corresponding repeated preparation and measurement.

For gamma=1 rad/(s·field-unit), t=1 s and B=pi/3 field-units, the ideal means are 1/2 and sqrt(3)/2. They select phi=pi/3 modulo 2 pi. A supplied range `-pi < gamma B t <= pi` makes that field value unique.

If the field may instead lie between -4 pi and 4 pi field-units, the same records admit several values. Shorten the initial interrogation, for example to t=0.1 s with the same gamma: the whole supplied range then lies inside the unambiguous phase interval. A later longer interrogation can refine a value once the remaining range supports its interpretation.

Coherence loss, imperfect rotations or an uncertain gamma change the response law. They can be included or constrained where the required estimate needs them. The local phase response alone is not a claim that arbitrarily long interrogation or another quantum resource improves every sensing task.

### PHY.9:6 - Bias-Annotation

The examples use controllable idealized arrangements to expose the construction. A field situation may limit access, preparation, reversibility or repeated sampling. Use those limits in choosing the interaction rather than treating the ideal case as an available apparatus.

Quantum sensing is one implementation of a wider physical move. Classical comparisons, chemical response and mechanical probes can serve the same construction when their physical relations and receiving use fit.

### PHY.9:7 - Conformance Checklist

- The target distinction includes the physical conditions under which it is sought.
- The proposed interaction makes that distinction affect the selected readout.
- Preparation, reference and comparison operations are physically interpretable.
- A cancellation or transferred calibration retains its shared physical premises.
- Disturbance and finite response are included when they change the wanted result.
- Local sensitivity is not substituted for resolution over the required range.
- The first result, remaining ambiguity and useful return to the arrangement are clear.

### PHY.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| The quantity appears, so it is measured | Mass cancels from ideal falling acceleration. | Derive the complete response and choose a coupling that retains the wanted dependence. |
| Responsive interaction, insensitive readout | A relative phase changes while a population measurement stays constant. | Choose preparation and readout together with the interaction. |
| Common offset by notation | Two preparations use one symbol for physically different influences. | Establish the shared condition or retain separate contributions. |
| More readings resolve every ambiguity | Repetition improves a statistic without separating compatible target values. | Change the interaction or use the sufficient compatible range. |
| Correction without the coupled arrangement | Probe loading is removed by a formula from another physical setup. | Derive the effect for the actual target and probe conditions. |
| Maximum local slope means best measurement | A periodic response leaves widely separated possibilities indistinguishable. | Compare the required range, resources and attainable distinctions. |

### PHY.9:9 - Consequences

The measurement can be improved by changing how information is physically produced. Better inference remains useful, but its contribution is tied to an interpretable preparation and response.

Different contributors can construct the coupling, calculate the response, prepare the reference and infer the result without losing the common physical question. When an existing arrangement suffices, the method ends with its use.

### PHY.9:10 - Architectural Rationale

The measurement relation and the measuring interaction solve connected difficulties. A relation can be derived for a fixed setup that is incapable of resolving the wanted difference. Constructing a different coupling, preparation or reference changes what the relation can supply.

This physical construction links theory to observation and intervention. It also links physical computing to readout: a physical state can carry a computed result that the chosen observation does not distinguish. The mathematical and statistical interpretation remains with the corresponding methods; it receives the interaction and its conditions.

### PHY.9:11 - SoTA-Echoing

The [VIM definitions of measurement principle](https://jcgm.bipm.org/vim/en/2.4.html) and [measurand](https://jcgm.bipm.org/vim/en/2.3.html) distinguish the phenomenon supporting a measurement from the quantity sought under specified conditions. [JCGM GUM-6:2020](https://www.bipm.org/documents/20126/2071204/JCGM_GUM_6_2020.pdf/d4e77d99-3870-0908-ff37-c1b6a230a337?download=true&t=1775224426559&version=1.15), especially sections 7.2 and 9, explains theoretical, empirical and hybrid response models and effects of realizing a measurement.

Compare the two mass procedures in :5.1. Timing ideal free fall is simpler but supplies no mass distinction. A known-force comparison supplies it at the cost of a force reference and acceleration readout. Reversal adds another preparation only when separating the force offset matters. Neither a more accurate clock nor more identical falls supplies the missing physical dependence.

[Degen, Reinhard and Cappellaro, *Quantum Sensing*](https://arxiv.org/abs/1611.02427), Reviews of Modern Physics 89 (2017), is a foundational synthesis of preparation, coupling, control and readout. [Pezzè and Smerzi, *Advances in multiparameter quantum sensing and metrology*](https://arxiv.org/abs/2502.17396), 2025, extends the selection question to several parameters, incompatible optimal measurements and finite resources. The adopted contribution is the joint choice of probe, encoding and readout; a quantum sensitivity bound needs its own estimation and attainability assumptions.

For the phase question in :5.3, the same Hamiltonian with an eigenstate probe gives no observable phase, while a superposition and suitable readout do. Short interrogation resolves the wider range; longer interrogation can improve local sensitivity while requiring range information and adequate coherence. More complex entangled or adaptive arrangements require a comparison under the actual resource and uncertainty conditions, not an advantage inferred from their name.

The [2026 amendment to JCGM 100](https://doi.org/10.59161/PPDI3267) explicitly addresses significant nonlinearity in both a measurement estimate and its uncertainty. It supports returning from a local sensitivity approximation when the receiving calculation depends on curvature. The applicable mathematical inference remains separate from construction of the physical coupling.

The numerical cases are constructed demonstrations under stated laws and idealizations. A changed material, interaction, preparation or readout range reopens the corresponding physical premise.

### PHY.9:12 - Relations

- **C.16.MR:** constructs and composes the relation from the sought property and measuring arrangement to an indication.
- **C.16.IR:** determines which target distinctions a supplied indication or response relation can resolve.
- **PHY.4, PHY.6 and PHY.7:** constrain a physical law or construct the evolution needed to derive a response.
- **PHY.5:** determines whether an interaction, disturbance or response time can be neglected for the intended consequence.
- **PHY.8 and MMP.7:** construct physical statistics and the probability law of recorded outcomes when variation and recording affect the result.
- **PHY.10:** uses a measuring interaction in a physical test separating rival accounts.
- **C.29.2** formulates the needed computation; **B.5.MPC** connects what it produces with the mathematical claim and the physical question.
- **C.16 and C.11:** characterize attainable performance and resource combinations, then choose among available arrangements.
- **C.11.DUA:** selects further measurement or inquiry by what it can change and the effort it requires.

### PHY.9:End

## PHY.10 - Construct a Physical Test That Separates Rival Accounts

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative

### PHY.10:1 - Problem frame

Use this pattern when competing physical accounts remain compatible with what has been observed, and the work needs a distinction between them. The missing contribution is a physical test: a preparation, intervention or understood comparison whose recorded consequences can separate the relevant alternatives.

A resistor and a capacitor can produce identical current traces under one imposed voltage history. Changing that history can expose the difference between dissipation and storage. A decaying collective signal can also hide different individual dynamics; a suitable intervention can make those dynamics distinguishable.

The first result is a proposed physical comparison, with the response each account permits, the conditions needed to produce and read it, and what the possible outcomes would change. It can reveal that the available apparatus cannot make the wanted distinction. A performed test adds observations and an interpretation under those conditions.

You need the physical meaning and applicable laws of the accounts being compared. Mathematical, computational and experimental collaborators can supply particular derivations and implementations. B.5.TC helps align the accounts when their questions or predicted quantities still differ. PHY.9 constructs a missing measuring interaction.

Use an existing discriminating observation or sufficient comparison directly. Leave the difference unresolved when it does not change the intended use, or when acting with the remaining uncertainty is preferable to another test.

### PHY.10:2 - Problem

Agreement with an observed response can have several physical explanations. A parameter can compensate for a missing interaction. A particular drive can make two response laws coincide. Different hidden dynamics can produce the same aggregate decay.

Collecting more data under the same uninformative conditions can leave the disagreement intact. Conversely, changing conditions to enlarge a predicted difference can introduce a new interaction, defeat the detector or leave the range in which either account was proposed.

A discrepancy also tests the combined account of the subject, preparation and observation. It need not identify the disputed physical premise by itself. The practitioner needs a comparison that exposes that premise while retaining the alternatives introduced by the apparatus and operating conditions.

### PHY.10:3 - Forces

| Force | Tension |
| --- | --- |
| Discrimination and estimation | Better knowledge of one account's parameters can leave its difference from another account unresolved. |
| Larger contrast and changed regime | A stronger intervention can expose the wanted effect while adding another physical mechanism. |
| Control and feasibility | A mathematically useful input need not be physically preparable with the available actuator, subject and resources. |
| Shared conditions and informative change | A comparison needs enough continuity to interpret a difference, while the test deliberately changes something. |
| Specific prediction and uncertain premises | Different nominal predictions can overlap after consequential parameter and apparatus uncertainty is included. |
| Useful criticism and effort | A simple consequence can settle the working question while a more elaborate experiment promises broader knowledge at greater cost. |

### PHY.10:4 - Solution

**Locate the consequential physical difference → find a condition that exposes it → construct the preparation and readout → compare the permitted responses → use the result and locate any defeated premise → develop the next useful test or stop.**

#### PHY.10:4.1 - State which physical disagreement matters

Ask the accounts the same physical question under corresponding conditions. Recover what each treats as the subject, its state, its interactions and the measured quantity. Use B.5.TC if the apparent conflict instead concerns different questions, representations or approximations.

State the consequence the work needs to distinguish. It may concern a law, an omitted interaction, stored state, a response time or another physical dependence. A distinction matters through what it changes in explanation, prediction, construction or subsequent inquiry.

Retain the parameter freedom that each account still has. An account with an adjustable coefficient is a family of possible responses, not just the curve at one fitted value. Include the available information that restricts that freedom. Do not choose a new parameter value independently at every observation unless the account itself permits that dependence.

Identify the auxiliary premises on which the comparison turns. For a driven specimen, these can include its preparation, the applied input, its coupling to surroundings and the relation between its response and the recorded indication. A test of the specimen's law can fail because one of these premises fails.

#### PHY.10:4.2 - Find a physical change that makes the accounts diverge

Trace the disputed difference forward to an observable consequence. Then ask which feasible change exposes it. For example:

- Change an amplitude, scale or operating regime when the accounts predict different dependence on it.
- Change the time course of a drive when the earlier input made different response laws coincide.
- Interrupt, reverse or refocus an interaction when the accounts retain different state or memory.
- Use a symmetry or balance when one account requires a response to vanish or remain within a bound.

Choose the change from the physical dependence at issue. PHY.4 supplies law constraints, PHY.5 examines a regime change and PHY.6-.8 derive the corresponding evolution or collective response.

Recompute both accounts under the proposed change. A prediction under the original preparation cannot be compared with a rival's prediction under the new one. Retain any changed interaction that can imitate or obscure the intended difference.

If intervention on the subject is unavailable, look for an accessible physical contrast: for example, a naturally varying condition with an understood relation to the accounts. Identify other differences between the observed situations. Their effects remain part of the comparison; naming the contrast does not make it controlled.

#### PHY.10:4.3 - Construct the experiment that can realize the contrast

Translate the mathematical change into physical preparation and operation. Identify the means of imposing the input, the initial or boundary conditions it requires, and the observable response. Include timing when a transient, memory or change of state is decisive.

Determine which shared conditions must survive. Maintaining geometry, material state or a reference can be more consequential than increasing the number of readings. When the intervention itself changes one of these conditions, either include that change in both predictions or construct another contrast.

Derive the subject-apparatus response far enough to establish that the difference reaches the recorded indication. PHY.9 constructs a missing coupling, reference or readout; C.16.MR represents the resulting measurement relation. A detector that clips both predictions to the same indication cannot implement their proposed separation.

Account for feasibility through the parts that can change this design. Available force, pulse duration, preparation time or observation range can rule out a proposed contrast or leave it conditional. An established apparatus or supplied capability can settle those questions without rebuilding its justification. If the required operation remains unavailable, return that specific limit or choose another contrast.

Use a reference or control for a named alternative explanation. A no-drive comparison can reveal an offset; a reference pulse can bound a control error. Add it when the result can change the interpretation.

#### PHY.10:4.4 - Compare the responses that can actually be distinguished

For each candidate design, obtain the readouts allowed by each physical account, including consequential parameter freedom and uncertainty in preparation, conversion and recording. MMP.7 supplies a probability law when records are random; C.16.IR helps determine what an indication can resolve.

Disjoint bounded response ranges give a particularly simple separation under their premises. If the ranges overlap, some outcomes can still discriminate the accounts while others remain compatible with both. Equal expected values likewise need not mean equal distributions or equal time dependence.

When discrimination depends on statistical evidence, use the appropriate model-comparison method with its dependence, sampling and error assumptions. Repeated readings do not automatically supply independent trials. A mathematical design criterion is useful only after the physical design and the interpretation of its records are supplied.

Compare designs on the distinction needed by the work and their full resource demand. A more informative record about one parameter need not be more informative about the rival mechanisms. Use a cheap sufficient contrast before constructing a costly optimization. C.11 compares available options; C.11.DUA addresses the value of another observation or computation.

Before performing the comparison, make its outcome interpretation clear enough to resist changing the question after seeing the result. State what would remain compatible with each account and which apparatus or preparation failure could mimic the disputed effect. The existing explanation or protocol can carry this reasoning.

#### PHY.10:4.5 - Obtain the result and locate the failed premise

Work the proposed preparation through to the predicted indication before committing the apparatus. This can expose an uninformative design or missing physical contribution without a new experiment.

When observations are obtained, interpret them under the stated recording and physical conditions. A response compatible with one supplied account and incompatible with another narrows this comparison. It does not exclude physical accounts that were never represented in the alternative set.

If the result disagrees with both, inspect the consequential premise rather than forcing a winner. Separate a computational error, an incorrect readout relation, an unachieved preparation and a defeated physical account. Follow the dependence of the failed prediction to identify a useful return. A supplied bound on an apparatus effect can sometimes exclude that explanation; when it cannot, retain the competing interpretations.

An agreement can also reveal a design limit. Determine whether the test retained the distinction it was meant to expose. If both accounts predict the observed outcome within the relevant uncertainty, report that limited result and preserve any unaffected consequence.

Reuse a result for the preparation, response range and question it supports. A successful test of a small-signal account does not determine its response after a regime-changing drive.

#### PHY.10:4.6 - Revise the account or develop the next contrast

Return the interpreted result and the physical reason for the next move. This may be use of a sufficient account, a narrower parameter range, an added interaction, a different preparation or readout, or an unresolved difference that the work can tolerate.

Develop a subsequent test from what remains unresolved. One outcome can identify which regime, hidden state or control error matters next. Sequential design can exploit that information, but a complete sequence need not be invented when one comparison already supplies the useful result.

When a revision changes the physical account, propagate it to the mathematical formulation, computation and interpretation that depend on it. Use B.5.RR and B.5.MPC.R for the corresponding reasoning and cross-contribution revision.

Stop when the obtained distinction suffices, or when no worthwhile available test changes the present use. Preserve a promising unresolved physical question when it opens a useful later construction or investigation.

### PHY.10:5 - Archetypal Grounding

#### PHY.10:5.1 - Change speed to separate two drag accounts

A specimen moves through the same fluid at an imposed positive speed v. In the proposed operating range, account L takes the opposing force magnitude to be `F=b v`; account Q takes it to be `F=c v²`. The coefficients are positive and constant under their respective accounts.

At v=1 m/s, an earlier calibrated force comparison places the true drag between 0.95 and 1.05 N. Thus L permits b between 0.95 and 1.05 N·s/m, while Q permits c between 0.95 and 1.05 N·s²/m². Both explain that observation.

A repeat at the same speed leaves this disagreement intact. Instead impose v=2 m/s while retaining specimen geometry and the fluid conditions on which the coefficients depend. L predicts a force between 1.9 and 2.1 N; Q predicts between 3.8 and 4.2 N. With an additional bounded force-readout error of ±0.1 N, the possible indications lie in [1.8,2.2] N and [3.7,4.3] N. They are disjoint.

The drive and readout must sustain that comparison. Under Q the required mechanical power can reach 8.4 W, since P=Fv. A 5 W drive cannot establish the proposed steady speed for every admitted Q response. A 10 W drive at that speed can meet this particular power demand, while its other operating limits remain relevant.

Suppose the comparison returns 2.05 N. It is compatible with L and incompatible with Q under the stated ranges and conditions. A return of 2.9 N instead disagrees with both. It prompts examination of the retained physical regime, parameter constraints and readout; it does not justify selecting whichever nominal curve is closer.

Heating or a geometry change can make a coefficient vary between runs. If that effect can span the separation, the test no longer has the same interpretation. Restore the shared condition, include the changed dependence or choose another contrast. Increasing speed without this return can defeat the very accounts being compared.

#### PHY.10:5.2 - Change a drive that makes storage and conduction coincide

A two-terminal element is driven with `V(t)=V_0 exp(t/tau)`. One proposed account is an ideal resistor, `I=G V`. Another is an ideal capacitor, `I=C dV/dt`, prepared with charge C V_0 at the start of the recorded ramp.

Since `dV/dt=V/tau`, choosing C=G tau makes the complete current traces identical during this ramp. More accurate recording of that same drive cannot distinguish the accounts.

Use V_0=1 V, tau=2 s, G=1 mS and C=2 mF. Stop increasing the voltage when it reaches 2 V and hold it there. After the drive and readout have settled, the resistor predicts 2 mA and the ideal capacitor predicts zero current. The change removed dV/dt while retaining V.

The waiting interval must be interpreted physically. A source with finite output resistance and a detector with finite response can create a transient after the change. Include it or choose a readout time after its consequential effect. The ideal predictions also exclude a significant leakage path.

Now suppose the held-voltage current is 0.6 mA, while the earlier ramp still has I/V=1 mS. The ideal pair is inadequate for these records. A parallel conductance and capacitance give

`I=G V+C dV/dt`.

The hold gives G=0.3 mS. Substitution into the ramp relation `G+C/tau=1 mS` gives C=1.4 mF. The test has opened a physically different account in which conduction and storage coexist. These two records determine its two parameters under the stated idealization; they do not establish that this account suffices at every frequency or voltage.

The resulting distinction changes use. A continuously held voltage dissipates power through the conductance, while the capacitance stores charge and supplies a transient response. Subsequent pulse or frequency use can therefore ask a question that the original exponential ramp could not resolve.

#### PHY.10:5.3 - Refocus a hidden physical difference

A prepared ensemble has a transverse phase signal. Consider two idealized accounts of its free decay. In account S, each member has a fixed frequency offset delta, drawn from the Lorentzian density

`p(delta)=Gamma/[pi (delta²+Gamma²)]`, with Gamma>0.

Each phase advances by delta t. Averaging over the ensemble gives `M_S(t)=exp(-Gamma t)` for t≥0. The individual offsets remain fixed even though the mean signal decays.

In account D, the phase instead has independent Gaussian increments with variance `2 Gamma dt` over an interval dt. This Markov dephasing gives the same free signal, `M_D(t)=exp(-Gamma t)`. The two accounts agree on this free-decay observation.

Apply a refocusing rotation at time tau and read the signal at 2 tau. In the ideal pulse comparison, the sign of phase accumulation is reversed for the second interval. Under S, each accumulated phase becomes `delta tau-delta tau=0`; the ensemble signal returns to 1. Under D, the two intervals have independent phase increments. Subtracting them leaves variance `4 Gamma tau`, so the signal remains `exp(-2 Gamma tau)`.

For Gamma=10 s⁻¹ and tau=0.1 s, the predicted refocused signals are 1 and approximately 0.135. The intervention exposes a difference hidden by the equal free decays.

A physical pulse has finite duration, range and accuracy. Its response over the occupied frequency range, other relaxation during the sequence and readout error must be included where they can change this separation. For illustration, if their combined effect on each predicted normalized signal is bounded by 0.05, the predicted indication intervals around 1 and 0.135 remain disjoint. This bound is a condition of that proposed implementation, not supplied by the ideal calculation.

If the pulse cannot refocus a consequential part of the ensemble, a small return can have that cause as well as irreversible dephasing. Change the pulse or reference comparison, retain its bounded effect, or leave the interpretation conditional. A partial echo can also motivate an account with both static variation and changing noise. The performed comparison then guides which hidden dynamics to retain.

### PHY.10:6 - Bias-Annotation

The cases use controlled laboratory comparisons and idealized response laws. Astronomical, geological and other field questions can require naturally available contrasts whose backgrounds cannot be independently fixed. The relevant physical premises must then support the observational comparison.

A finite candidate set can exclude a useful account before the test begins. A result inconsistent with every candidate, or a new physical dependence exposed by the experiment, can justify developing the set. It need not become a competition among the original labels.

### PHY.10:7 - Conformance Checklist

- The accounts answer the same physical question under corresponding conditions.
- Their remaining parameter freedom and consequential auxiliary premises are retained.
- The proposed physical change makes a difference in an observable response.
- Preparation, drive and readout can realize that change, or their unresolved limit is stated.
- Discrimination is judged with the relevant physical and recording uncertainty.
- Possible results retain their different implications, including agreement with several accounts or disagreement with all supplied accounts.
- The first result and subsequent physical, mathematical or computational return are usable.

### PHY.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Better data from an uninformative drive | The resistor and capacitor retain identical ramp traces. | Change the physical input that made the laws coincide. |
| Nominal curves treated as complete accounts | Adjustable coefficients make the predicted response families overlap. | Compare the responses allowed by the admitted parameter information. |
| Increase the drive until the curves separate | A new physical regime defeats the retained laws or apparatus. | Derive the changed interactions and check attainable preparation. |
| Distinct states, identical indications | The detector erases the predicted difference. | Change the measuring interaction or readout. |
| Nearest curve must win | A response outside both admitted ranges is forced into the original pair. | Locate the failed premise and develop another account when needed. |
| A failed echo proves irreversible loss | Control error or an unaddressed frequency range can suppress the return. | Include or distinguish the consequential pulse and readout effects. |

### PHY.10:9 - Consequences

Physical comparison becomes a construction that can change what is observable. Its result can be a discriminating experiment, a useful limit on current apparatus, an improved account or a justified stop.

The calculation, apparatus and interpretation can be developed by different contributors while retaining the common physical disagreement. The cost is concentrated on the dependencies that determine the comparison. A result may remain local even when it resolves the present work.

### PHY.10:10 - Architectural Rationale

B.5.TC compares how theoretical accounts answer a working question. This method develops a physical consequence of that comparison: how a preparation or interaction can expose the disputed dependence. PHY.9 supplies an observable readout; the statistical or mathematical design uses that physically realizable relation.

Equal unperturbed responses can conceal different retained state. Changing a drive or reversing an interaction therefore supplies more than another sample of the old observation. It asks the accounts how the physical system responds to a different operation. That response can also reveal how the system might be controlled or used.

The test retains the apparatus and preparation because they participate in the consequence being compared. This makes an unsuccessful comparison informative: a return can change the subject account, the experimental construction or their mathematical description, according to which premise failed.

### PHY.10:11 - SoTA-Echoing

[Huan, Jagalur and Marzouk, *Optimal experimental design: Formulations and computations*](https://arxiv.org/abs/2407.16212), Acta Numerica (2024), with corrections and clarifications in the 2026 author revision, distinguishes design for parameter information, prediction and model discrimination. Its sections 2.2 and 6.1 retain uncertain influences and the possibility of model misspecification. These distinctions enter :4.1 and :4.4-.5. A design based on a supplied model set does not establish that the set contains an adequate account.

For the drag comparison, the disjoint force ranges give a sufficient design without a numerical optimizer. When feasible inputs are numerous and predicted records are uncertain, an experimental-design method can compare their expected contribution. Its advantage depends on a useful objective and credible response models. The cost of constructing and evaluating that optimization matters alongside the cost of the experiment.

[Vezvaee et al., *Fourier transform noise spectroscopy*](https://www.nature.com/articles/s41534-024-00841-w), npj Quantum Information (2024), develops noise reconstruction from free-induction and spin-echo measurements. The adopted physical contribution is changing how a prepared probe couples to temporal structure. The paper's spectral reconstruction relies on its pure-dephasing and stationary Gaussian-noise setting; those assumptions are not imposed on the Lorentzian static-offset construction in :5.3.

For a noise question within that setting, the paper compares reconstruction from simple sequences with methods requiring many pulses. It also exposes different limitations: finite pulse timing, a restricted accessible frequency range and sensitivity of time derivatives to measurement error. Choosing more elaborate control is therefore not a general improvement. The simpler sequence can be sufficient for the needed distinction, while a different noise or control question calls for another method.

The three numerical cases are constructed comparisons under stated physical laws. Their purpose is to exhibit the changed preparation, response and interpretation; they are not reports of performed experiments. New physical effects or apparatus limits change the corresponding case premises.

### PHY.10:12 - Relations

- **B.5.TC and B.5.TU:** align the theoretical comparison and construct a missing application of an account.
- **PHY.4-.8:** constrain a law and derive the physical response to a changed preparation or interaction.
- **PHY.9 and C.16.MR:** construct the measuring interaction and its relation to the recorded indication.
- **C.16.IR and MMP.7:** determine what the indication resolves and supply the applicable recording probability law.
- **PHY.1-.3:** receive a discriminating comparison when similarity, a physical analogue or a limiting transformation needs examination.
- **C.11 and C.11.DUA:** compare available designs and the value of further inquiry.
- **B.5.RR and B.5.MPC.R:** revise the affected reasoning and its physical, mathematical and computational contributions.

### PHY.10:End

## PHY.3 - Derive a Physical Limit from Permitted Transformations

> **Type:** Method
> **Status:** Usable, evolving
> **Normativity:** Normative within the stated use

### PHY.3:1 - Problem frame

Use this pattern when you need to determine what a physical process or device could accomplish before choosing its detailed mechanism, or when a familiar physical prohibition appears to rule out a proposed change. A candidate may have an acceptable energy balance yet require an unavailable preparation, consume a resource that was omitted, or perform differently on inputs that one device is supposed to handle.

The first useful result is a necessary condition on the requested performance, a conditional exclusion of a class of proposals, or a changed premise that opens a different construction. You obtain it by describing the complete physical transformation and constructing a comparison that the applicable physical laws constrain. “Permitted” here means allowed under those physical premises.

You need a working description of the requested effect, the resources and surrounding systems it may use, and the physical principles relevant to that effect. A qualitative argument can suffice. A quantitative result also needs the quantities and mathematical operations in its chosen comparison. The two worked cases require different preparation: energy exchanges and elementary ratios in the first, state vectors and inner products in the second. Obtain an unfamiliar physical premise or calculation from a suitable source or collaborator and retain the conditions on which its answer depends.

When an established bound already answers the same question under the same physical conditions, apply it directly. A measurement of a particular device, estimation of an unknown parameter and design of a mechanism have their own methods. Return here when their result changes the allowed transformation or the reach of a physical restriction.

### PHY.3:2 - Problem

A physical proposal usually names the desired effect more readily than the whole change needed to produce it. “Return the machine to service,” “copy an input” and “extract more work” can leave different resources, input families and end conditions implicit. Those differences determine which physical restrictions apply.

Detailed calculation of one design can reveal its failure while leaving other designs available. Conversely, a quoted limit can be applied outside its premises and suppress a useful construction. The difficulty is to derive a restriction whose physical description covers the proposals being considered, and then use it to decide what to change or investigate.

### PHY.3:3 - Forces

| Force | Tension |
| --- | --- |
| Reach across mechanisms | A bound can guide many designs, but its description must cover every design to which the conclusion is applied. |
| Complete physical change | Preparation, surroundings and restoration can determine the result; describing every microscopic detail would make the first inquiry unusable. |
| Admissible comparison | A simple reference can expose a strong limit, while a mathematically convenient inverse may require a physical operation that is unavailable. |
| Useful idealization | A larger class of ideal operations can yield a bound on real devices; an omitted physical contribution can invalidate that inference. |
| Continued construction | An obstruction can redirect work immediately, while removing that obstruction leaves further realization questions. |

### PHY.3:4 - Solution

Construct the complete proposed transformation, identify the physical restrictions shared by its candidate mechanisms, and use an admissible comparison to derive their consequence. Keep the requested performance and its physical conditions attached to the result. Revisit the premise that matters when the resources, input family or required performance changes.

#### PHY.3:4.1 - Specify the physical change and what must remain usable

Start with the proposed input and output. Include the range of inputs and the performance required on them. For a machine expected to handle an unknown input, ask whether one fixed arrangement must work throughout that range or whether the arrangement may be chosen after learning the input. For fluctuating processes, distinguish a guarantee on every run from an average or an allowed failure probability. MMP.8 supplies that formulation when the choice or information condition is difficult.

Follow the resources that can participate in the transformation: material, energy, prepared states, information about the input, external controls and connections to the surroundings. Describe their relevant initial and final conditions. A charged auxiliary, a memory that accumulates records and an initially correlated pair can be consumed resources even if the visible output is unchanged. Use the physical theory to decide which such differences matter to the proposed restriction.

For repeated operation, state what the device must remain able to do. Return to an identical state is needed only when the requested operation or the physical argument requires it. If the construction uses a reset, include its physical change and resource use. A device that still performs the next operation can have changed state; a device restored in one observed variable can have exhausted another needed resource. A.3.3.TR helps choose a sufficient state description where these cases are unresolved.

The result is a physical transformation with its allowed side effects and input conditions. Keep an unspecified preparation visible as an unresolved premise. It can be useful to derive a conditional bound before that premise is settled.

#### PHY.3:4.2 - Establish which physical restrictions cover the candidate mechanisms

Select the physical account that connects the requested change with a conserved quantity, an ordered change, a preserved relation or another necessary condition. State its regime and the systems to which it applies. A local balance law can require a larger boundary when something crosses it; a law for a closed process can require explicit surroundings when the proposed device exchanges matter or information.

Explain why every device in the proposed conclusion admits the chosen description. MMP.10:4.4 supplies this coverage requirement. Physically, it can mean including a reservoir and its controller, representing an unobserved auxiliary, or admitting all interactions allowed by the theory instead of only one circuit. Restrict the conclusion to the designs described if this coverage remains incomplete.

An enlargement of the allowed class can make exclusion easier: if even a class with additional resources cannot realize the requested transformation, its contained class cannot do so. Show that containment. An approximation chosen because it is easy to calculate does not automatically give such an enlargement; it can remove a coupling or noise source that changes what is possible. When only an approximate account is justified, propagate a suitable error allowance or retain a conditional result at that model's stated scope.

Use B.5.TU to recover the physical theory's premise and its consequence for the case. The output of this step is the applicable restriction and the reason it covers the proposed physical class. Further measurement is useful only if its possible result changes that premise or the next choice; C.11.DUA helps resolve a consequential uncertainty about that effort.

#### PHY.3:4.3 - Construct a comparison that exposes the restriction

Choose the operation that fits the available physical structure. The following two constructions address different situations and can be used independently.

**Compose with a reference and cancel selected changes.** Use this when an admitted reference process exchanges the relevant quantities or restores a needed condition. Choose the part of the proposal you want to eliminate from the combined account, then determine the reference's direction, amount and preparation that match it. Establish that the reference can perform that operation under the same connecting conditions. For example, two processes may exchange equal energy but require incompatible temperatures, pressures, phases or forms of delivery. Numerical equality alone cannot establish the physical connection.

Combine the proposed and reference operations, including their auxiliaries. Cancel only the matched exchanges or restored states; keep all remaining changes. C.29.BB supplies the accounting for additive quantities. Apply the physical restriction to the composite. If it would have a prohibited net effect, derive the inequality or condition on the original proposal that avoids that effect. A reference may be an ideal process admitted by the theory; building it in a laboratory is unnecessary for this conditional argument. Using the inverse in an equation still requires a reason that the needed physical reverse process is admitted.

**Compare inputs of the same operation.** Use this when one device must perform the requested transformation on a family of inputs and a physical law relates its actions on different inputs. Select inputs whose relation can expose the limitation. Write their proposed outputs, including allowed auxiliary outputs, while holding fixed the device and its input-independent preparation. Derive the relation the law requires between those outputs. If the requested outputs violate it, the common device cannot provide them under the stated conditions.

An auxiliary output may depend on the input even when the initial preparation cannot. Allow that dependence in the comparison. Requiring the auxiliary to return to a fixed state when the proposal permits a changed state would prove a narrower restriction. Conversely, choosing a different apparatus separately for each input would answer a different question from the fixed-device requirement.

These constructions can reveal a remaining physical premise rather than a bound. Name that premise and what supplying it would enable. Forcing either comparison when its connection conditions or input relation are absent adds no physical result.

#### PHY.3:4.4 - Derive the consequence with every remaining physical change included

Carry the quantities, signs, state conditions and input relations through the chosen comparison. Interpret each term by the physical contribution it represents. Check that the canceled effects have compatible units and conditions, and that the uncanceled effects describe the complete remaining process.

Obtain the requested inequality, an excluded transformation, or the unresolved condition on which either result depends. When using a mathematical invariant, MATH.11 supplies the derivation from the admitted transformation rules. When a numerical tool performs the algebra, retain the symbolic relation or a sufficient explanation that lets another participant inspect what the computation establishes. C.29.2 and C.29.3 govern a computation whose formulation or realization needs further work.

Distinguish a necessary bound from attainability. A proposed device can satisfy one physical restriction and still fail another, or approach a theoretical limit only as time or another resource grows. The useful output at this step says which candidates have been excluded, which remain under consideration, and which premise or construction controls the next question.

#### PHY.3:4.5 - Change the proposal at the premise that controls the result

Return the physical consequence in the terms of the working question. For a proposal outside the bound, identify a consequential change: supply a previously forbidden resource, allow a side effect, narrow the input family, relax precision or reliability, or change the condition for reuse. Derive the affected comparison again for the chosen change. Keep the original result for its original premises.

When the obstruction disappears, continue with a mechanism, an approximation or another limiting principle. PHY.2 can help construct a physical analogue for that inquiry; PHY.1 supplies physical similarity if transferring between regimes is the next difficulty. If the new question concerns an unfamiliar mathematical construction, obtain that contribution from Mathematical Thinking. B.5.MPC helps divide and reconnect those contributions across people and AI agents.

Stop the present derivation when its result is sufficient for the next decision. Further information or a physical trial is a separate action whose value depends on what remains unresolved. A concise explanation of the compared transformation and controlling premise is enough when it allows the intended user to continue.

### PHY.3:5 - Archetypal Grounding

#### PHY.3:5.1 - Bound a proposed engine without designing its mechanism

**Question.** A proposed cyclic machine takes 100 J from an ideal reservoir at 600 K and delivers 60 J as work. Its only other interaction is heat rejection to an ideal reservoir at 300 K. The machine returns to its initial state. Can a different mechanism make the proposal possible under these same conditions?

The physical preparation includes both reservoirs, the work store and restoration of the machine. It supplies no fuel, depleted auxiliary store or initially available nonthermal resource. The two temperatures are absolute thermodynamic temperatures. Energy balance gives 40 J rejected to the cold reservoir; that balance alone leaves the proposed output admissible.

Use the classical second-law account for these conditions. Its Clausius restriction excludes a composite process whose only net effect is transfer of heat from the colder reservoir to the hotter one. An admitted reversible reference between these reservoirs has `eta_ref = 1 - 300/600 = 1/2` and can run backward. This is a theoretical reference; no claim of a finite-power reversible laboratory device is needed.

Choose cancellation of the work exchange. A backward reference consuming the proposed 60 J extracts 60 J from the cold reservoir and delivers 120 J to the hot reservoir. The compatible exchanges combine as follows; positive entries increase the named store.

| Store or component | Proposed engine | Backward reference | Net change |
| --- | --- | --- | --- |
| Hot reservoir | -100 J | +120 J | +20 J |
| Cold reservoir | +40 J | -60 J | -20 J |
| Work store | +60 J | -60 J | 0 |
| Both devices | Each completes its cycle | Each completes its cycle | Restored |

The net process transfers 20 J from cold to hot with no other change. It violates the selected restriction. The argument uses only the proposed exchanges and cyclic condition, so changing the candidate's internal mechanism cannot repair it within this class.

For a general positive requested work `W`, the backward reference requires `Q_hot_ref=W/eta_ref`. If `W > eta_ref*Q_hot`, then `Q_hot_ref > Q_hot`; canceling work again produces the prohibited cold-to-hot transfer. Therefore:

~~~text
W <= eta_ref*Q_hot = (1 - T_cold/T_hot)*Q_hot.
For the stated inputs: W <= 50 J.
~~~

The practical result redirects the design question to work below this bound or to a change in the stated resources. It does not supply the design that attains a chosen value, its power or its operating cost.

**Change the allowed physical operation.** Suppose the proposed device may also receive 20 J of external work. A forward reversible reference producing 40 J from 80 J of hot-reservoir heat, together with routing those 20 J through the work store, can supply 60 J gross output. The net work produced is 40 J. The denominator and net exchange must now reflect the actual question; this construction supplies no engine producing 60 J net work from the original 100 J alone. If exactly 100 J must still be taken from the hot reservoir, an admitted additional transfer of 20 J from hot to cold accounts for the remainder. The total cold-reservoir gain is 60 J, and both laws permit the resulting exchanges. The changed resource condition opens a construction rather than altering the earlier bound.

For a microscopic proposal with initial correlations or a nonthermal auxiliary, use the physical account appropriate to those resources. A reservoir-only calculation leaves their contribution out. The source comparison in :11 identifies a current treatment; it does not prescribe the same generalized formula for every macroscopic device.

#### PHY.3:5.2 - Test copying across inputs while allowing auxiliary outputs

**Question.** Can one device take one input qubit in an unknown pure state and produce two perfect copies on every run? The device can use an auxiliary prepared independently of the input, and its final auxiliary state may depend on that input. Discarding an auxiliary is allowed.

Use the standard quantum description of a deterministic operation. Include the device's environment and any measurement records in the description of the complete process. A fixed mixed auxiliary preparation can be purified by adding a reference system. The total evolution can then be represented by one isometry `V`, which preserves inner products. This includes deterministic operations obtained by interaction and later discarding part of the system; it does not impose that the visible two-qubit map itself be unitary. If both required output copies are pure, their joint output factors from the remaining pure total state.

Choose two distinct nonorthogonal input states `|a>` and `|b>`. Let `|0>` be the blank second qubit and `|e>` the fixed initial auxiliary. Perfect copying would require:

~~~text
V(|a>|0>|e>) = |a>|a>|e_a>
V(|b>|0>|e>) = |b>|b>|e_b>.
~~~

The final auxiliary states are deliberately allowed to differ. Define `s=abs(<a|b>)`, with `0<s<1`, and `r=abs(<e_a|e_b>)`, with `0<=r<=1`. Taking inner-product magnitudes before and after the same isometry gives:

~~~text
s = s*s*r.
Dividing by s>0 gives 1=s*r.
But s*r <= s < 1.
~~~

The requirements are inconsistent. For the concrete pair `|a>=|0>` and `|b>=(|0>+|1>)/sqrt(2)`, `s=1/sqrt(2)` would require `r=sqrt(2)`. That exceeds the allowed overlap of normalized auxiliary states. More unobserved auxiliary output cannot make this deterministic perfect copier possible under the stated account.

This is a physical restriction on one operation across its input family. The mathematical step is preservation of an inner product; the physical work is establishing why the candidate devices admit that common description with the stated preparation. Showing failure of one guessed gate arrangement would leave this broader question unanswered.

**Change the input family.** Restrict it to the computational-basis states `|0>` and `|1>`, with a blank second qubit `|0>`. Controlled-NOT gives `|0>|0> -> |0>|0>` and `|1>|0> -> |1>|1>`. The same arrangement therefore copies every input in that restricted family. A different known orthogonal pair can first be mapped to that basis, copied, and mapped back on both outputs.

**Change the performance instead.** If failed runs may be discarded, the accepted operation is conditioned on an outcome and the all-runs argument no longer directly characterizes its normalized successful output. One must specify the allowed input set, success probability and failure output, then derive their restrictions. Allowing imperfect copies likewise changes the output relation and requires an accuracy question. The present result identifies why either revised problem differs; it supplies no unexamined claim that a desired success rate or accuracy is achievable.

### PHY.3:6 - Bias-Annotation

The method corrects two live errors: treating one device's failure as a prohibition on every mechanism, and applying a quoted prohibition after its resource or input conditions have changed. Its own principal risk is selecting a convenient physical description that omits an allowed device or contribution. Keep the coverage argument next to the conclusion and use a changed-condition return to expose what the result actually depends on.

The worked proofs assume established classical thermodynamics and standard quantum operations in their stated regimes. Their conditional strength should remain visible when a research question concerns the adequacy of those theories themselves. A formal contradiction identifies incompatible premises; it does not choose by itself which empirical premise to revise.

### PHY.3:7 - Conformance Checklist

- [ ] The requested physical effect includes its input family, performance criterion and relevant preparation.
- [ ] Consumed resources, surrounding systems and any required restoration or continued capability are included where they affect the restriction.
- [ ] The selected physical account has a stated regime and a reason to cover the device class in the conclusion.
- [ ] The comparison uses compatible admitted reference operations, or the same operation on inputs linked by the physical law.
- [ ] The derivation retains uncanceled changes and allowed auxiliary outputs.
- [ ] The result distinguishes the derived necessary condition or exclusion from the still-needed realization.
- [ ] The explanation shows which changed premise would require another derivation and what the current result enables next.

### PHY.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure in use | Repair |
| --- | --- | --- |
| A limit quoted without its physical preparation | A bound derived for two reservoirs is applied to a device consuming an additional resource. | Recover the complete transformation and derive the applicable restriction. |
| An algebraic inverse treated as an available apparatus | The comparison depends on a reverse process whose required preparation or control was never admitted. | Establish the physical reference operation before using its cancellation. |
| Failure of one construction promoted to impossibility | Another permitted coupling or auxiliary lies outside the calculation. | Give a covering physical description or restrict the conclusion to the analyzed class. |
| Input-specific devices hidden inside one-device wording | A calculation selects a separate operation after knowing each supposedly unknown input. | Hold the common device and allowed information fixed across the input comparison. |
| Reset or ancillary change omitted | Apparent cyclic performance consumes a stored resource or accumulates a consequential change. | Include that state change and the reset required by the actual repeatability condition. |

### PHY.3:9 - Consequences

A useful physical limit can be obtained before the internal mechanism is known. It can reduce unproductive design work, expose an omitted resource, or suggest a different input family or performance requirement. The derivation also gives collaborators a physical question to answer: a needed reference process, a covering law or an unsettled preparation.

The cost is obtaining a physical account whose reach matches the conclusion. Stronger exclusion usually needs broader coverage than failure of a candidate design. A conditional result is often sufficient to guide the next step while that coverage is developed. Near a limiting value, finite time, noise, size and implementation constraints can determine whether pursuing it is useful.

### PHY.3:10 - Architectural Rationale

The complete transformation is the shared object of the two comparison constructions. It makes hidden resources and restoration conditions available to reasoning, while leaving the internal mechanism open. Reference cancellation reduces a proposal to a constrained composite effect. Input comparison constrains what one operation can do across alternatives. These differences explain the choice in :4.3; neither construction is a compulsory stage of the other.

The physical premise gives the mathematical operation its bearing on a device. A conserved sum or preserved inner product can be studied mathematically without that interpretation. Conversely, knowing the name of a physical principle does not yet specify the permitted exchanges, preparation or input family. The method supplies this physical construction and uses the existing mathematical and common inquiry methods for their contributions.

An ideal reference helps bound real proposals when its admitted operations and the coverage relation are explicit. It serves a different purpose from a realistic simulation of one device. Both kinds of account can remain useful in the same inquiry: the bound directs construction, and the constructed mechanism reveals further practical restrictions. The explanation of a failed proposal can also generate the next problem by identifying a consequential change of premise.

### PHY.3:11 - SoTA-Echoing

**Reversible-reference comparison.** [David Tong, Statistical Physics, §4.3.1-4.3.2](https://davidtong.org/pdfs/teaching/statistical-physics/statphys4.pdf) gives the established Carnot comparison and the thermodynamic temperature ratio. It is a historical methodological anchor for composing processes and canceling exchanges. The pattern uses the construction beyond a particular working substance.

**Input comparison with auxiliaries.** [Peter Shor, Quantum Computation, lecture 5](https://math.mit.edu/~shor/18.435/oldlectures/lecture5.html) presents the no-cloning comparison and explicitly includes an input-dependent ancillary output. The present worked case spells out the total-process interpretation, overlap bound and changed-input return. The classical thermal and quantum arguments exemplify different physical restrictions and different comparison operations.

**Resource conditions in current thermodynamics.** [Aguilar and Lutz, Correlated quantum machines beyond the standard second law, version 2 (2025)](https://arxiv.org/html/2409.07899v2) analyzes initial correlations, nonthermal resources, interaction energy and changes remaining after a driving cycle. These contributions explain why a reservoir-only efficiency claim can need a different account. Its microscopic assumptions determine where its generalized expressions can be used.

**One occurrence and repeatable performance.** [Marletto, Deutsch and Vedral, Tests of constructor theory (2026), §1.4 and §3.2](https://arxiv.org/html/2606.07352v1) develops the distinction between an allowed evolution and a device able to repeat a specified transformation, including the difference between reversing dynamics and supplying a reusable inverse operation. The pattern adopts that problem distinction. The article's new constructor-theoretic principles are research proposals with their own tests; they are unnecessary premises for the two established arguments above.

The synthesis selects operations for constructing a physical limitation and reopening it under changed conditions. It does not require one universal physical resource theory. A new account of the permitted operations, an omitted resource or a changed performance condition is a reason to revisit the affected argument and its source premises.

### PHY.3:12 - Relations

- **B.5.TU and B.5.MPC** supply theory-to-case use and division and reconnection of mathematical, physical and computational work. **B.5.QD** helps develop the next question from an obtained limit or obstruction.
- **A.3.3.TR** supplies a sufficient state description and representation of interacting changes. **C.29.BB** supplies boundary accounting and cancellation for additive quantities.
- **MMP.8 and MMP.10** supply information-conditioned choice, constraint formulation and the coverage requirement for a class-wide conclusion. **MATH.11** supplies mathematical invariant construction and use.
- **PHY.1** supplies physical similarity when the comparison must cross regimes; **PHY.2** constructs a physical analogue for the continuing mechanism question.
- **C.29.1-C.29.3** govern mathematical correspondence, computational formulation and realization where those are unresolved. **ME.7** develops a proposed composition of the work method using the physical result; **ME.12** checks the claims in that account and its description. **C.11.DUA** helps decide whether an additional inquiry can change the useful next action.

### PHY.3:End
