# Systems Engineering Principles Framework

> **Edition:** First edition — see [Framework Boundary and Refresh](#framework-boundary-and-refresh).

# Table of Contents

Use the Readme when you have a working difficulty but do not yet know the direct pattern. Use this Table of Contents when you already know the problem family or PatternID. Pattern bodies contain the authoritative working moves.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Systems Engineering Principles Framework Readme](#systems-engineering-principles-framework-readme) | Start from a recognizable engineering difficulty and choose one direct pattern or a small set of patterns. |
| [Preface](#preface) | Understand the distinctions that make the 24 patterns work together. |
| [Cross-Pattern Applications](#cross-pattern-applications) | Use two navigation walkthroughs and two filled applications in software and cyber-physical equipment. |
| [Framework Boundary and Refresh](#framework-boundary-and-refresh) | Check scope, source return, omissions, and reopen conditions. |

## Part I — Project Focus, Environment, Consequences, and Problem/System-Family Development

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [SYSE.1 - Choose and Reopen the Project System-of-Interest](#syse-1) |  | Which System is this project changing? system of interest; project boundary | FPF A.1.SCR, C.11 |
| 2 | [SYSE.16 — Recover the Systems and Conditions Needed for a Use Decision](#syse-16) |  | What contains or uses the System? environment; suprasystem; operational neighbours | SYSE.1; FPF A.22 |
| 3 | [SYSE.17 — Find Systems That May Bear Engineering Consequences](#syse-17) |  | Who or what may undergo an engineering consequence? affected systems; obtaining relations; modal paths | SYSE.1, SYSE.16; FPF A.1.CSD, C.28, A.10 |
| 4 | [SYSE.2 - Develop Linked Use and System Concepts](#syse-2) |  | How will the System be used, and what System concept could realize that use? | SYSE.1, SYSE.16, SYSE.17; FPF C.17 |
| 5 | [SYSE.22 — Coevolve Engineering Problems and System-Family Options](#syse-22) |  | How can problem formulations and System-family options develop together without freezing either? | SYSE.1, SYSE.2, SYSE.6, SYSE.13; FPF C.11, C.17-C.19, G.11 |

## Part II — Architecture, Descriptions, Offerings, and Professional Contributions

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 6 | [SYSE.5 — Develop Functional Organization and Bearer Alternatives](#syse-5) |  | Which functions, bearers, and interfaces could produce the intended effect? | SYSE.2, SYSE.16; FPF A.6.F, A.22 |
| 7 | [SYSE.6 — Decide and Reopen the Engineering Architecture](#syse-6) |  | Which architecture should we choose, and what would reopen it? | SYSE.2, SYSE.5; FPF C.30, C.32 |
| 8 | [SYSE.7 — Maintain a Decision-Usable Engineering Description Ensemble](#syse-7) |  | Do the models, requirements, analyses, and records support the same decision? | SYSE.6; FPF C.29, A.10 |
| 9 | [SYSE.8 — Develop an Integrated Offering and Provider Concept](#syse-8) |  | What offering and provider arrangement make the intended use possible? | SYSE.2; FPF A.2.3 |
| 10 | [SYSE.9 — Request and Use Specialist Engineering Results](#syse-9) |  | Which specialist result is needed, by whom, for which receiving decision? | SYSE.2, SYSE.6; FPF A.6.REL, E.10.ROLE |
| 11 | [SYSE.10 — Assess Research, Model, and Trial Results for an Engineering Decision](#syse-10) |  | What can this model, experiment, or trial support in the engineering decision? | SYSE.6, SYSE.7; FPF A.10, C.16 |

## Part III — Obtaining Engineering Results, Recursive Realization, Platforms, Independent Constituents, and Evolvability

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 12 | [SYSE.24 — Choose How the Project Will Obtain a Needed Engineering Result](#syse-24) |  | How will the project obtain one needed engineering result through a comparable whole arrangement? | SYSE.1, SYSE.2; FPF C.11, C.18 |
| 13 | [SYSE.3 — Develop the Recursive Realization Network](#syse-3) |  | Which changed Systems and builder Systems can realize the selected architecture? | SYSE.6, SYSE.8; FPF E.18.NET, A.15 |
| 14 | [SYSE.11 — Integrate a System for One Bounded Use](#syse-11) |  | What bounded configuration is usable now, with what integration and operating evidence? | SYSE.3, SYSE.12, SYSE.13, SYSE.18; FPF A.3.4 |
| 15 | [SYSE.12 — Develop an Engineering Platform for Practitioner Work](#syse-12) |  | What platform must enable the engineers' actual modeling, building, test, release, and observation Work? | SYSE.15, SYSE.20; FPF A.2.2 |
| 16 | [SYSE.18 — Integrate Systems Governed by Different Agents](#syse-18) |  | How do we integrate constituent Systems with independent authority and evolution? | SYSE.6; FPF E.18.NET |
| 17 | [SYSE.23 — Choose What to Change So Later System Changes Become Easier](#syse-23) |  | Which changes to the project system-of-interest or builder arrangement preserve valuable future changes? | SYSE.22, SYSE.3, SYSE.6, SYSE.12, SYSE.20; FPF C.11, C.25, C.30, C.32 |

## Part IV — Configuration, Continuing Change, and Source Continuity

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 18 | [SYSE.13 — Establish Configuration Identity, Variants, and Effectivity](#syse-13) |  | Which unit, variant, version, configuration, and effectivity range is in scope? | SYSE.6; FPF A.22, C.2.1, C.27.TA |
| 19 | [SYSE.14 — Make a Release Decision for Named Engineering Work or Use](#syse-14) |  | What changed, who may release it, and what evidence applies to that configuration? | SYSE.13, SYSE.19; FPF C.11, A.10, B.3 |
| 20 | [SYSE.19 — Revalidate Engineering Decisions When a Relied-on Source Changes](#syse-19) |  | Which decisions must be revalidated after a relied-on source changes? | SYSE.7, SYSE.10; FPF C.2.1, A.10, G.11 |

## Part V — Assurance, Method and Work Architecture, Repertoire, and Cultural Continuation

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 21 | [SYSE.4 - Select an Engineering Challenge and Qualify Evidence Use](#syse-4) |  | Which result could change reliance on this engineering claim? assurance; evidence return | SYSE.10, SYSE.11, SYSE.14; FPF A.10, B.3 |
| 22 | [SYSE.15 — Choose and Refresh the Engineering Methods Needed by a Project](#syse-15) |  | Which engineering Method variant fits this situation, and what evidence would retain or reject it? | FPF A.3.2, C.36, E.23 |
| 23 | [SYSE.20 — Reconcile Overlapping Engineering Work and Required Order](#syse-20) |  | Which engineering Work overlaps now, and which dependencies really require order? | SYSE.15; FPF A.15.1, A.22.CGUS, E.18.NET |
| 24 | [SYSE.21 — Deliberately Continue and Change Systems Engineering Culture](#syse-21) |  | Should this Systems Engineering Method variant be retained, changed, branched, or stopped across a practitioner population? | SYSE.20; FPF C.36, G.11 |

# Systems Engineering Principles Framework Readme

This framework helps engineers and managers change or bring about an engineered System while keeping its use,
problem formulations, System-family options, architecture, realization, configuration, evidence, engineering
platform, evolvability, and continuing Method development connected. It is for Systems Engineering across kinds of engineered System. Software, electrical, ship,
building, medical-device, cyber-physical, and other application profiles retain the specialist Methods and
sources that differ because their engineered Systems differ.

The framework begins from working difficulties, not from a lifecycle. Engineering Work can overlap: a team can
refine use, architecture, realization, configuration, assurance, and its engineering Method during the same
bounded project interval. A logical dependency still matters when one result cannot be used before another
exists. Use the patterns to recover the actual result dependency; do not turn the order of this file into a prescribed
project sequence.

## Practical entries

The five Parts group patterns by recurring Systems Engineering problem families. They are reading groups, not
entry recipes. Each ordinary entry below deliberately starts with one pattern and stops at one first result or
blocker. Follow the single stated condition to another pattern only when that blocker occurs. If none of these
examples fits, use the Table of Contents and open the pattern whose working situation matches yours.

### SYSE-ENTRY-PROJECT-USE — Recover the project system-of-interest and the use that matters now

- **Situation:** Participants use one project name for several Systems or uses, so different decisions silently
  concern different subjects.
- **Question:** Which actual System or intended-system designator has this project selected as the project
  system-of-interest, and for which use is the next engineering decision being made?
- **First useful result or blocker:** A project-system choice account that identifies the actual System or
  intended-system designator selected as the project system-of-interest, the receiving use, and the decision
  horizon; or the unresolved System or use ambiguity.
- **Start with:** `SYSE.1`.
- **Stop or return:** Stop when the receiving decision can refer to the same System and use. Use `SYSE.16` only
  when an unresolved containing, using, neighbouring, or interacting System prevents that focus.

### SYSE-ENTRY-ARCHITECTURE — Choose among available engineering alternatives

- **Situation:** Several functional, bearer, or interface alternatives exist, but the project has no explicit
  architecture choice or condition for reopening it.
- **Question:** Which alternative should the project select for the named use and comparison basis?
- **First useful result or blocker:** One architecture decision with the selected structures, accepted
  losses, supporting evidence, and reopen conditions; or the missing comparison basis.
- **Start with:** `SYSE.6`.
- **Stop or return:** Stop when the receiving Agent can act on that decision. Use `SYSE.5` only when the apparent
  alternatives do not yet give genuinely different functions, bearers, or interfaces to compare.

### SYSE-ENTRY-OBTAINING — Compare complete ways of obtaining one needed engineering result

- **Situation:** The project has jumped to *build*, *buy*, *provider*, *reuse*, or *AI* before the alternatives
  describe the same result and include their integration, assurance, support, capability, and exit burdens.
- **Question:** Which whole arrangement should provide the result needed for the named use?
- **First useful result or blocker:** Several comparable obtaining arrangements and one choice, retained
  tie-set, worthwhile probe, rejected set, or a deferral until another named question is answered; or the missing result identity or acceptance
  basis that prevents comparison.
- **Start with:** `SYSE.24`.
- **Stop or return:** Stop at its bounded `C.11` choice result. Use `SYSE.3` only after an arrangement survives and
  its first unsupported realization branch becomes the next engineering question.

### SYSE-ENTRY-REALIZATION — Turn locally completed changes into one usable System increment


- **Situation:** Parts, software, or local changes are reported complete, but no actual System configuration has
  been shown usable for the intended operating purpose.
- **Question:** What is the smallest changed configuration that can be integrated and observed in that use?
- **First useful result or blocker:** A bounded usable increment with its configuration, use, evidence,
  fallback, and unresolved limits; or the missing integration or use evidence.
- **Start with:** `SYSE.11`.
- **Stop or return:** Stop when the release or operating decision can use that bounded result. Use `SYSE.3` only
  when the missing blocker is the realization arrangement that should produce an included part or result.

### SYSE-ENTRY-CONFIGURATION — Identify what exists and where a claim applies

- **Situation:** Versions, baselines, installed units, description editions, and releases are mixed, so a change
  or evidence claim has no recoverable subject or effectivity.
- **Question:** Which System configuration does the claim concern, and where and when does it apply?
- **First useful result or blocker:** A configuration-and-effectivity account fit for the receiving
  decision; or the missing identity, configuration relation, or effectivity boundary.
- **Start with:** `SYSE.13`.
- **Stop or return:** Stop when the receiving decision can identify the same configuration and effectivity. Use
  `SYSE.14` only when a proposed or performed change now requires a release decision.

### SYSE-ENTRY-ASSURANCE-METHOD — Decide whether available evidence supports one engineering claim

- **Situation:** Tests or checks have passed, but no one can state which claim they support or which decision may
  rely on them.
- **Question:** What does the available evidence justify for the named claim, subject, conditions, and receiving
  decision?
- **First useful result or blocker:** A claim-specific evidence-use result with its limits; or the missing
  observation, correspondence, configuration, or authority.
- **Start with:** `SYSE.4`.
- **Stop or return:** Stop when the receiving Agent can rely, refuse reliance, or request the missing evidence.
  Use `SYSE.13` only when configuration or effectivity ambiguity prevents that judgement.

### Practical-Use Cards

These are selected examples of extended use across several patterns, not a catalogue or a prescribed workflow.
The mantra helps retain the dependency among results; each pattern body still supplies the working method and
its stop conditions.

#### SYSE-CARD-01 — Release a mixed physical-and-software change without losing service, configuration, or evidence

- **Situation:** A change crosses physical equipment, control software, operating service, configuration, and
  assurance. Participants use different meanings of the System and release readiness, while some engineering
  Work overlaps and some results have real dependencies.
- **Question:** How can the engineering team reach one qualified release recommendation and preserve the
  conditions under which the changed System, its evidence, and the trialled engineering Method may be used later?
- **First useful result or blocker:** A decision-usable project-system choice account and bounded operational-
  use account; or the missing System referent, project designation, boundary, use, consequence-bearing System,
  configuration, or evidence that prevents a responsible release decision.
- **Mantra:** A project-system choice account and operational-use account expose affected Systems and support
  linked use, functional, bearer, and architecture choices. The selected change is bounded by configuration and
  effectivity; claim-specific release evidence retains its limits and unresolved safety conditions. A trialled
  Method enters the repertoire only for the claim class supported by evidence. Change of the engineering
  repertoire or culture requires observed receiving enactment and later project consequences. These are result
  dependencies, not a calendar lifecycle: architecture, realization, configuration, assurance, platform, and
  specialist Work may overlap.
- **Start with:** `SYSE.1`. If the project focus already exists, start with the first unsupported result exposed
  by `SYSE.16`, `SYSE.2`, `SYSE.13`, or `SYSE.4`; use the other patterns only when their result is needed.
- **Stop or return:** Stop at a configuration- and effectivity-bounded release recommendation, its qualified
  assurance basis, and a bounded Method-repertoire disposition usable by the separately identified release
  authority. Return missing permission, functioning evidence, source claim, configuration fact, authority, or
  long-horizon observation. Reopen when the System, use, configuration, evidence horizon, or relied-on Method
  changes.

##### Expansion for SYSE-CARD-01

The cooperating patterns are `SYSE.1`, `SYSE.16`, `SYSE.17`, `SYSE.2`, `SYSE.5`, `SYSE.6`, `SYSE.13`,
`SYSE.14`, `SYSE.4`, `SYSE.15`, and `SYSE.21`. `APP-SYSE-01` shows one bounded use; it is not a universal
release sequence.

#### SYSE-CARD-02 — Develop a problem portfolio and System family without freezing either

- **Situation:** A project repeatedly optimizes one System option while the problem question, comparison
  conditions, available options, or the arrangement that realizes them keeps changing.
- **Question:** Which System-family option should survive the next decision, and does the obstacle call for a
  change to the selected System-family option, its builder arrangement, or both?
- **First useful result or blocker:** A bounded problem-and-option result from `SYSE.22`: one named problem
  question, a reidentifiable set of comparable System-family options, current evidence and protected conditions,
  and one decision to choose now, reject the set, run a worthwhile probe, or return a missing question or
  authority.
- **Mantra:** One problem question and the current System-family options remain distinct but linked by evidence.
  A shared comparison basis supports one of four outcomes: choose now, reject the set, run a worthwhile probe, or
  return the missing question or authority. When a valuable surviving option is blocked by its builder
  arrangement, the next comparison includes changes to that option, the builder arrangement, both, and the
  unchanged arrangement. The resulting choice remains current until a named input changes.
- **Start with:** `SYSE.22`. If the project system-of-interest designation or use is still ambiguous, first use `SYSE.1`; if option
  identities or configurations cannot be compared, return that blocker to `SYSE.13`.
- **Stop or return:** Stop after the `SYSE.22` choice when no builder constraint changes it. Use `SYSE.23` only
  when a surviving option is valuable and the relation between the selected System-family option and builder arrangement changes the next investment or
  reconfiguration choice.

##### Expansion for SYSE-CARD-02

Apply `SYSE.22` to the problem-and-option comparison and `SYSE.23` to the conditioned choice between changes to the System-family option, the builder arrangement, or both.
Route a focus blocker to the Agent applying `SYSE.1` and a configuration blocker to the Agent applying `SYSE.13` only when that blocker prevents the corresponding Work. `APP-SYSE-02` is a navigation
walkthrough; it does not turn these result dependencies into a lifecycle.

# Preface

Systems Engineering changes or brings about engineered Systems through explicit reasoning about use, problem
formulations, System families, architecture, realization, configuration, evidence, evolvability, and the
engineering arrangement itself. The phrase is not a synonym for *engineering of systems*. Software engineering,
electrical engineering, ship engineering, building engineering, medical-device engineering, and other profiles
concern different kinds of engineered System and retain specialist Methods, evidence, laws, tools, and sources.
This framework provides the common Systems Engineering layer that materially changes their Work without
replacing those profiles.

FPF supplies the transdisciplinary distinctions used here: holons and Systems, parts and relations, Methods and
MethodDescriptions, Work and results, architecture as selected structures, evidence and assurance, decisions and
authority, cultural evolution, and precise plain language. This DPF does not repeat those distinctions as generic
advice. It adds engineering-specific moves: choosing a project system-of-interest, relating use and System concepts,
developing a problem portfolio and System-family options together, developing functional and bearer
alternatives, deciding engineering architecture, coordinating specialist returns, realizing recursively through
builder Systems, developing the platform used by practitioners, maintaining configuration and release evidence,
choosing changes to the project system-of-interest, its System-family option, the builder arrangement, or both for evolvability, and continuing engineering Methods.

## One System can appear in several engineering structures

An engineered System can be the project focus, a part of a using or containing System, the bearer of functions,
the result of realization Work, one configuration in a product family, a participant in operation, and the subject
of evidence. These are not interchangeable labels. Each pattern states which relation obtains and which decision needs
that view. Ownership does not prove parthood; interaction does not prove membership; a description is not
the described System; a release record is not the released configuration; and a passed component test is not an
outside benefit.

The operational environment is therefore not a residual box called *everything else*. It includes the containing,
using, neighbouring, and interacting Systems and the conditions that matter to the current use. Call a System a suprasystem only when the engineered System under discussion is its proper part. `SYSE.16` restores those relations; `SYSE.17` follows the
planned use, realization, operation, maintenance, misuse, and change to Systems that can bear benefit, harm, or
another engineering consequence.

## Use and System concepts stay linked

A concept of use says how actual or intended Systems participate in an operating situation and what effects are
expected. A System concept says what engineered System arrangement could participate that way. Either can expose
a defect in the other. `SYSE.2` therefore guides an Agent in developing linked use-concept and System-concept
candidate families rather than letting one preferred technical solution determine the use story after the fact.

Functional organization and constructive organization answer different questions. A function claim concerns a
contribution under conditions. A bearer claim concerns an actual System or intended System referent that could
make that contribution. `SYSE.5` guides the Agent in developing alternatives for both and making allocation and
interface choices explicit. `SYSE.6` then guides the Agent's architecture-decision Work: compare the candidates
for the current engineering use, record the selected result, and state the evidence and conditions that would
reopen the choice.

## Realization is recursive and continuous

The framework does not prescribe a lifecycle. A concept or architecture is not handed once to an undifferentiated
implementation stage. Agents change engineered Systems by performing Work with Methods. Those Agents rely on
builder and enabling Systems that may themselves require platforms, capabilities, resources, suppliers,
facilities, models, software, data, and further engineering. `SYSE.3` makes this recursive realization
arrangement visible. `SYSE.11` uses it
to obtain and modernize bounded usable increments instead of waiting for a fictitious terminal completion.

The engineering platform is also an engineered System when it is deliberately developed to enable named
practitioner Work. `SYSE.12` starts from that Work—modeling, computation, build, integration, test, release,
observation, or another engineering activity—and asks which actual capability, service condition, access, data,
tool, automation, facility, or provider contribution is needed. Buying a tool or naming a platform does not
establish that engineers can perform the Work.

Independently governed constituent Systems require another distinction. Their authority, operation,
configuration, or evolution can remain partly independent even when a higher-level use depends on them.
`SYSE.18` coordinates commitments, interfaces, configurations, decisions, and evidence without pretending that
all constituents are ordinary internal parts or that the label *system of systems* solves the integration problem.

## Configuration and evidence travel with continuing change

Engineering identity is decision-relative but not arbitrary. A product-family item, actual unit, installed
configuration, software realization, description edition, baseline, variant, state, and effectivity range can
differ. `SYSE.13` supplies the configuration basis needed by a named decision. `SYSE.14` connects a proposed or
performed world-side change to that basis, its deciding System, permission, implementation, release, cited
evidence, and unresolved conditions.

Evidence supports a stated claim only for the receiving decision and conditions to which that evidence applies. A model, experiment,
trial, test, certificate, review, or observation is not evidence for every nearby claim. `SYSE.10` connects
research and trial results to engineering claim assessments. `SYSE.4` first reuses compatible current results,
then plans the smallest missing challenge, qualifies evidence use, changes reliance, and returns the result to
the earliest answer it can actually change. Safety, security, legal, ethical, financial, certification,
acceptance, permission, and release decisions keep their specialist criteria and authority.

A source change is not automatically a world-side System change. A changed model, standard, requirement,
MethodDescription, architecture description, or supplier claim first changes an episteme. `SYSE.19` traces the
claims and engineering decisions that relied on it and revalidates only the affected uses. Ignoring every source
change and reopening the whole project are both errors.

## A Method has several structures; Work can be simultaneous

An engineering Method can be described through several non-isomorphic structures. Its constructive composition
asks which Methods or method parts make up a larger Method. Its unfolding asks which results and dependencies
permit a next move. A Work account asks which Work occurrences overlap, participate in a larger Work whole, or
must occur in a real order. A provider or build-the-builder account asks which enabling Systems and capabilities
must exist. A cultural account asks how Method variants are generated, transmitted, enacted, recognized,
selected, retained, changed, and lost across a practitioner population.

Do not call every vertical list a level stack. A *first–then* relation normally describes an unfolding or Work
order. Simultaneous participation at different holonic or scale positions is different: physical computation,
model use, architecture judgement, configuration coordination, and assurance can all contribute during the same
bounded engineering Work while remaining different Methods or Work wholes. `SYSE.20` guides the Agent in
recovering those overlaps, conflicts, dependencies, and required orders instead of replacing them with one
lifecycle diagram.

`SYSE.15` guides development of a decision-usable engineering Method repertoire. A standard, branded framework,
model-based recipe, toolchain, or AI workflow is a candidate contribution, not *the Method* by title. The
repertoire records fit, evidence, exclusions, branches, and reopen conditions. `SYSE.21` guides a different
decision: how an authorized Agent deliberately continues or changes the Systems Engineering culture of a named
practitioner population. One team choice or one successful project does not prove transmission, retention, or
cultural change.
 Later enactment and engineering consequences must be
observed, and the deciding and affected Systems must remain explicit.

## Project Work participates in, but does not equal, engineering culture

A gadget release, a subsystem architecture decision, a platform improvement, or an assurance account is a
bounded project result. The Systems Engineering Discipline is a continuing cultural phenomenon: Method variants,
terms, examples, tools, criteria, institutions, and practitioner habits are reproduced and changed across many
Work occurrences. A project can generate a candidate variant, enact it, produce consequences, and influence
selection. It does not become the culture or determine cultural retention by declaration.

This distinction keeps the framework practical. Most users should stop with the project pattern that resolves
their current difficulty. Open `SYSE.21` only when the receiving question is deliberately to continue or change a
Systems Engineering Method variant across a named practitioner population. Open the FPF cultural-evolution
patterns when the claim is transdisciplinary rather than Systems-Engineering-specific.

## What this publication carrier foregrounds and what it leaves outside

This publication carrier foregrounds five connected problem families: project focus, use, and joint
problem/System-family development; architecture and professional contributions; obtaining engineering results,
recursive realization, engineering platforms, independent constituents, and evolvability across the project system-of-interest and builder arrangement;
configuration and continuing change; and assurance, Method-and-Work architecture, repertoire, and cultural
continuation. The 24 pattern bodies provide the authoritative descriptions of engineering Methods, cases,
checks, source uses, and relations. The Readme provides selected entries. This Preface explains the distinctions
that make the entries cohere. Two navigation walkthroughs show result dependencies; the worked software and
cyber-physical applications demonstrate joint use with filled values and reopen conditions, without defining a
lifecycle.
The publication carrier leaves specialist application-profile Methods, a full history of Systems Engineering,
curricula for developing human capability, organization design, operations management, corporate governance,
finance, law, safety, security, ethics, and detailed domain standards to their own patterns, DPFs, or sources.
Return there when those results change the engineering decision. This boundary is not a claim that the omitted
Work is unimportant; it prevents a common Systems Engineering DPF from speaking vaguely where a specialist
practice can act precisely.


# Part I — Project Focus, Environment, Consequences, and Problem/System-Family Development

<a id="syse-1"></a>
## SYSE.1 - Choose and Reopen the Project System-of-Interest

### SYSE.1:1 - Problem frame

Use this pattern when a project is already discussed through a familiar name—for example, a product, solution,
tool, provider, organization, component, desired effect, or broad programme—but no defensible current decision
yet identifies which System the project is intended to change or bring about. The choice matters because it
changes later questions about use, boundary, architecture, realization Work, evidence, and specialist decisions.

A conforming use returns a **project-system choice account**: claim-bearing project decision content that names the
selected actual System or intended referent, the current reason for the choice, and what may reopen it. The
account is not the selected System.

First useful move: name one candidate actual System or intended referent, state the present use or change reason
for choosing it, and write the main unresolved assumption. This small project-system choice account is enough
to ask the next use-and-system concept question. Expand it only when disagreement, a valuable alternative, or a
later answer can change the choice.

If the choice is missed, participants can work competently on different projects while using the same project
name. A supplier optimizes a component, an integrator changes an operating assembly, and a client expects an
outside effect, yet each assumes that the familiar noun names the same project system-of-interest.

The payoff is a shared and revisable project focus, not an eternal boundary. The choice can stabilize current
coordination while evidence from use, architecture, realization, or operation remains able to reopen it.

Use this pattern only when project coordination needs a System designation. If the decision already concerns
another recognized subject—for example Work, a Method, a capability, a state, a material portion, a
description, a collection, a structure, or a transformation—keep that subject under the pattern that defines
or constrains its claim. If the issue is only whether a named entity is a System, use `A.1.SCR`. If the System
has already been selected and the live question is how it participates in use, continue with `SYSE.2`.

At the first consequential use of source wording such as *system of interest*, *target system*, *our system*,
*product*, or *solution*, ask one question: **is the project choosing which actual System or intended referent
it will change?** If yes, state the candidate and its current use or change reason. *Project
system-of-interest* names the designation made for this project; it is not another System kind.

### SYSE.1:2 - Problem

Project names are chosen early, often before outside use, engineering boundaries, and realization constraints
are understood. The first plausible referent then becomes invisible infrastructure for later decisions. A tool
is selected as the project system-of-interest merely because it is purchased; a provider System is selected
merely because its people perform the Work; or a desired state is forced into a System because the project is organized around achieving
it.

The opposite error is also common: a useful tool, software product, or component is excluded by a slogan even
when its own product project legitimately selects it. The engineering problem is not to apply one preferred
answer. It is to compare referents for the current project and keep the choice revisable as coupled problem and
solution understanding changes.

### SYSE.1:3 - Forces

| Force | Tension |
| --- | --- |
| Coordination and revision | Contributors need one usable focus now, while new evidence may change it. |
| Outside use and technical discovery | Outside use justifies the choice, while architecture and realization discoveries can revise the use and boundary. |
| Actual and intended Systems | Brownfield work can concern an existing System, while new development may only have an intended referent in decision or plan content. |
| One project and related projects | Related parties—for example, a client, supplier, integrator, provider, and operator—may share components and evidence while their projects select different Systems. |
| Candidate breadth and decision cost | A single familiar candidate hides alternatives, while an exhaustive catalogue delays the next useful question. |
| Stable language and ontic precision | A shared designation aids communication, while its name, description, or agreement does not establish System identity or the designation itself. |

### SYSE.1:4 - Solution

#### SYSE.1:4.1 - State the current project decision

Begin with the project whose coordination is current. State:

1. what change or later use this project is meant to enable;
2. which plan or decision needs a shared project-system designation now; and
3. which subject is presently proposed as the System to be changed or brought about.

Keep related projects separate. A manufacturer's planning-improvement project, a software vendor's product
project, and an integration provider's deployment project may use the same software and evidence without making
the same project-system choice. A programme or portfolio may coordinate shared matters—for example, priority,
resources, investment, risk, or evidence—without thereby becoming a composite acting System.

#### SYSE.1:4.2 - Recover the direct subject before forcing a System choice

Use `A.15.6` when project, process, or case wording hides whether the current subject is performed Work, a
reusable Method, a selected structure, a transformation-flow structure, a changed referent, or another claim.
If that direct subject answers the decision, stop this pattern use and keep the subject under its own FPF
pattern.

When the decision does need a System, distinguish two cases:

- For an actual System, use `A.1.SCR` when recognition is unresolved. Its constructive criterion supplies the
  tested System identity and boundary used in the comparison.
- For a System that does not yet exist, keep the intended referent in the current plan, decision, or description.
  Do not describe it as an already acting System.

Recognition and project designation remain different claims. Recognizing an actual System does not select it
for the project; selecting an intended referent does not make it physically present.

#### SYSE.1:4.3 - Generate and criticize materially different referents

Generate alternatives from the working situation, not from a mandatory taxonomy. After the direct-subject exit
in §4.2, retain a candidate referent for the project system-of-interest only when it is one of two things:

1. an actual System, with `A.1.SCR` recognition when that recognition is decision-relevant; or
2. an intended referent for a System not yet present, kept as a designator in plan, decision, or description
   content rather than described as an already acting System.

Examples include an actual product System, tool System, engineering platform, operating System, provider
System, containing System, or organization System, and the intended referent of any such possible-future
System. A provider arrangement or organization qualifies only when that whole is an admitted actual System or
such an intended referent. A
subject changed by a tool, a collection, Work, Method, capability, state, description, or another holon remains
the direct subject or a related structure unless it satisfies the same System condition. The examples are
non-exhaustive. Retain only candidates that would change a later decision.

For each candidate, compare the claims that matter now:

- the outside use or change the candidate is expected to support;
- the project boundary and the relation to related projects;
- the participating and affected Systems;
- the boundary, interaction, constituent, containment, ownership, authority, or other direct relations that
  actually change the choice;
- the important characteristics, constraints, feasibility branches, evidence, and uncertainty; and
- the assumption or observation that would defeat the candidate.

Treat familiar project facts—payment, delivery, ownership, enterprise boundary, a diagram, the transformer that
performs realization Work, or the subject visibly changed by a tool—as evidence about candidates or project
boundaries. Choose the project system-of-interest through the project's stated use and decision.

Retain several candidates when later learning can change their order or when different candidates preserve
valuable options. Let the current decision, available resources, and named stop determine the candidate count
and comparison effort. Stop when the current choice is good enough to ask the next consequential question and
its reopening evidence is named.

#### SYSE.1:4.4 - Record the smallest useful choice account

The cheap first result contains only:

```text
Project-system choice account:
  current project and decision:
  selected actual System or intended referent:
  current use or change reason:
  main unresolved assumption:
  reopen condition:
```

This is a readable rendering, not a mandatory record schema. Add further content—for example, comparison
grounds, candidate alternatives, boundary and participation claims, affected Systems, authority, realization,
or evidence—only when it changes the current choice or a downstream use.

Stop when the project can ask a concrete use-and-system concept question about the named referent for the stated
reason. The resulting account supplies that referent, reason, boundary question, alternatives, and reopen
condition to `SYSE.2`.

#### SYSE.1:4.5 - Reopen the choice from the answer that failed

Reopen the account when one of these changes the comparison:

- observed or expected use crosses the assumed boundary;
- authority or permission makes the intended change unavailable;
- an architecture candidate moves important functioning to another System;
- no feasible realization branch supports the selected referent;
- operating or assurance evidence defeats the reason for the choice; or
- a related project is separated, combined, or reoriented in a way that changes the current project decision.

Return to the smallest failed claim. A changed use assumption may require `SYSE.2` before the project focus
changes. A failed bearer or architecture candidate may return through `C.30` or `C.32`. Reopen `SYSE.1` only
when the evidence changes which System should orient this project or where the project boundary lies.

### SYSE.1:5 - Archetypal Grounding

#### Pumping station under flood risk

A flood-reduction project starts with the phrase “new pump”. The engineer compares the pump unit, the pumping
station, the drainage-control System, and a provider arrangement. Flood-control use crosses the pump-unit
boundary: positioning, power, control, discharge conditions, and downstream exposure belong to the station's
current use question. The engineer selects the pumping station and records:

```text
selected referent: intended pumping station
current reason: move water under the selected flood load as part of flood-control use
main unresolved assumption: downstream exposure remains acceptable
reopen: use, architecture, realization, or operating evidence changes that assumption or boundary
```

This result is already useful. `SYSE.2` can now link a concrete flood-load use claim to a station concept.
Later discovery that the proposed station increases downstream harm changes the linked use claim. It reopens
the project-system choice only when that changed claim defeats the reason or boundary used by the choice account.

#### Manufacturer and ERP vendor

A manufacturer opens a “new ERP” project because production plans repeatedly fail. The manufacturer compares
the software product, the planning organization, a deployed planning System containing people, software, data,
and decision interfaces, and the wider production-control System. It selects the intended deployed planning
System because the current project changes production-planning use and records data quality as the main
assumption.

The vendor's product project can separately select the ERP software product. “Software is always the project
system-of-interest” and “software is never the project system-of-interest” both erase the project-specific
decision. The two accounts preserve the shared software and the different uses.

#### Continuing building through several projects

For example, design, construction, operating retrofit, and heritage-restoration Work can concern one continuing building
while using different plans, transformer Systems, access arrangements, and evidence. In an occupied retrofit,
the engineer selects the continuing building because its occupied performance is being changed and records
access during use as the main unresolved assumption.

Several descriptions of the building do not create several Systems or projects. Conversely, one programme does
not become the performer of all Work. Each project account states its own reason for selecting the building and
can reopen that choice without inventing a birth-to-retirement order.

### SYSE.1:6 - Biases to Watch

Two recurring biases matter in this decision. **System inflation** forces every important project subject into
`U.System`; use `A.1.SCR` and the direct-subject exit before choosing. **First-candidate lock-in** turns the first
plausible referent into permanent project scope; retain material alternatives and state the reopen condition.

### SYSE.1:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-SYSE1-1` | A conforming use SHALL name the current project and the decision that needs a project-system choice. |
| `CC-SYSE1-2` | It SHALL retain a direct non-System subject when System designation is not needed, and SHALL use `A.1.SCR` when actual System recognition remains load-bearing. |
| `CC-SYSE1-3` | It SHALL distinguish an actual System from an intended referent in plan, decision, or description content. |
| `CC-SYSE1-4` | The first useful account SHALL name the selected referent, current use or change reason, main unresolved assumption, and reopen condition. |
| `CC-SYSE1-5` | When materially different actual Systems or intended System referents remain plausible, the account SHALL compare their decision-relevant claims and SHALL keep every non-System subject under its direct pattern rather than admit it as a candidate referent for the project system-of-interest. |
| `CC-SYSE1-6` | Additional account content SHALL be added only when it changes the current choice or a downstream use. |
| `CC-SYSE1-7` | A stop SHALL make the next use-and-system concept question askable; a reopen SHALL name evidence or a changed project condition that can alter the choice. |
| `CC-SYSE1-8` | Related projects SHALL keep their own designation decisions even when they share Systems, Work, resources, descriptions, or evidence. |

### SYSE.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Project-name shortcut | The noun in a charter or backlog is used as the selected System without a use or change reason. | State the current project decision, generate plausible referents, and compare how each changes the next question. |
| Tool or provider substitution | The most visible tool or the System performing realization Work replaces the System whose use the project changes. | Keep tool, transformer, provider, changed subject, and project designation as separate claims; compare them as candidates only when each could orient this project. |
| First-candidate freeze | Work has started, so later use or feasibility evidence is treated as irrelevant to project focus. | Record the main assumption and reopen condition with the first choice; return evidence to that claim when it changes. |
| Important-subject inflation | A desired state, Work result, description, collection, capability, or transformation is called a System because the project centres on it. | Keep the direct subject and use its FPF pattern. Open `SYSE.1` only if a System designation is required for the current project decision. |
| Programme-as-performer | Shared resources or one programme plan are treated as proof of one composite acting System. | Use the programme or portfolio grouping for its coordination decision and establish any System composition separately. |

### SYSE.1:9 - Consequences

The project gains a focus that is stable enough for coordinated Work and explicit enough to challenge. Related
projects can share resources and evidence without being collapsed. Architecture and realization discoveries
can change the project focus without being treated as late exceptions.

The cost is visible uncertainty. Several candidate referents may remain current, and the account must be
revisited when a named assumption fails. That cost replaces the larger cost of optimizing an architecture or
realization network for the wrong project system-of-interest.

### SYSE.1:10 - Rationale

Systems Engineering needs a project focus because architecture, realization, and assurance questions require a
referent. That focus is a decision under uncertainty, not a fact supplied by the project name or by System
recognition alone. Separating actual System identity, intended reference, project designation, and the account
that describes the choice lets practitioners coordinate without confusing an episteme with the physical or
operational System.

Ask about outside use when comparing candidates because it tests why each candidate matters. This check does
not prescribe the calendar order of project Work. Problem framing, candidate development, architecture,
realization, and evidence can change one another; the explicit reopen condition makes that movement normal.

### SYSE.1:11 - SoTA-Echoing

| Current practice line | What changes in this pattern | Source and use | Adoption status |
| --- | --- | --- | --- |
| Design framing treats what matters to a design problem as revisable while problem and solution understanding develop together. | The Solution makes the project-system choice revisable and requires the use, assumptions, and contextual relations behind it. | Kelly and Gero (2022), Litster, Cardoso, and Hurst (2024), and Nickel, Hurst, and Duimering (2024). These conceptual and small empirical studies support explicit framing and revision, not one framing ontology or universal Method. | **Adopt and bound.** Adopt co-development and contextual comparison; reject an algorithmic or consensus-made designation. |
| Set-based design retains alternatives while learning can change feasibility or trade-offs. | The Solution asks for materially different referents and preserves valuable alternatives when the decision needs them. | Toche, Pellerin, and Fortin (2020) review the set-based line; Al Handawi et al. (2024) demonstrate margin-based exploration in one aeroengine-component case. | **Adapt.** Retain alternatives and narrow them by evidence; let the receiving project determine candidate count and decision choreography. |
| Decision making under deep uncertainty uses robust alternatives, staged commitments, monitoring, and revision rather than prediction alone. | The first account carries an unresolved assumption and a reopen condition; later evidence can change the choice. | Haasnoot et al. (2013), Marchau et al. (2019), Lempert et al. (2024), and Akse (2024), mainly in climate, infrastructure, policy, and sociotechnical-transition settings. | **Adapt.** Use staged commitment and explicit reopening; let the receiving project establish its scenarios, thresholds, triggers, and decision Method. |
| Entrepreneurial-action research treats available means, commitments, contingencies, prediction, and judgement as context-dependent complements. | Candidate generation may use available Systems and commitments without treating them as proof of the project referent or of success. | Chen, Liu, and Chen (2021), Zhang et al. (2023), and Rapp, Olbrich, and Packard (2026). Meta-analytic associations and conceptual synthesis do not establish one causal engineering Method. | **Adapt narrowly.** Keep contingent action and revision as candidate pressure; leave business and Strategy decisions with their practices. |

These sources constrain a guide-derived Systems Engineering move. They support comparing and revising project
focus; none establishes the `U.System` criterion, the project designation, or the project-system choice for a
particular case. The pump, ERP, and building cases therefore use current FPF distinctions and case facts rather
than source prestige.

### SYSE.1:12 - Relations

- `A.15.6` distinguishes project Work, process, case, Method, transformation, selected structure, and project
  system-of-interest wording before the practitioner uses this pattern to make a System choice.
- `A.1.SCR` supplies the constructive recognition result when the comparison depends on whether a candidate is
  an actual acting or changed System. It also supplies the direct-subject exit when systemhood is not
  load-bearing.
- `SYSE.16`, `SYSE.17`, `SYSE.2`, and `SYSE.8` may use the project-system choice account when their question
  concerns the same subject, configuration, decision, and evidence window. That use identifies the engineering
  focus for the receiving question; it imposes no temporal order.
- An engineer uses `SYSE.2` to develop linked use and concept claims whose failure may revise the choice. The
  resulting linked proposal helps frame the architecture question. `C.30` defines that question and `C.32`
  guides candidate synthesis; infeasibility or harm returns
  through the smallest linked claim and reopens this pattern only when project focus changes.
- `A.1.STM` provides the wider systems-mantra traversal when a practitioner must reconnect this local choice to
  outside use, architecture, realization Work, change, and recursive transformer Systems. It adds no project
  designation or fixed Work order.
- The applicable FPF decision, authority, evidence, value, harm, temporal, and direct-relation patterns define
  or constrain those claims when they become current; this pattern does not replace them.

### SYSE.1:End

<a id="syse-16"></a>
## SYSE.16 — Recover the Systems and Conditions Needed for a Use Decision

### SYSE.16:0 — Use This When

Use this pattern when an engineering decision concerns an actual System or intended-system designator selected as the project system-of-interest, but everything outside it
has been reduced to one box called *environment*, *stakeholders*, *users*, *the business*, or *the platform*.
The decision needs to know which larger Systems contain it, which other Systems interact with it, which
transformation flows and interfaces matter, and which outside conditions can change the result.

Begin with one use situation and one receiving engineering decision. Recover only the Systems, direct relations,
selected structures, conditions, evidence, and assumptions that can change that decision.

The first useful result is a **bounded engineering-use account**. It describes how an actual System participates,
or how an intended System is expected to participate, in one named use situation. The account is an episteme used
by the decision. The situation, actual Systems, containing wholes, and other obtaining relations remain its
world-side subjects.

Do not use this pattern merely to draw a context diagram or inventory every nearby object. Use the governing FPF
pattern directly when one already-known relation—such as parthood, interface, interaction, flow, or an architecture
relation—answers the question. If the project system-of-interest designation is still unclear, use `SYSE.1` first.

### SYSE.16:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| project system-of-interest | A project-relative designation in plan or decision content. It names either an actual System or an intended-system designator. The designation, actual System identity, intended referent, and existence are separate claims. |
| use situation | A bounded actual situation in which the System participates, or a described possible-future situation in which the intended referent would participate. A scenario or diagram is a description of that situation. |
| containing whole | An actual System of which the selected System is a proper part under a stated relation, or a possible-future whole in a proposed proper-part claim. One System can belong to several relevant wholes under different relations. |
| suprasystem | Optional source wording for a containing whole. Use it only when the proper-part claim is stated; it is not a grand name for everything outside the boundary. |
| other System in the use situation | An actual System, or intended referent, connected by a named non-part relation that matters to the decision. Examples include an interaction or transfer between named Systems; observation of one System by another; access granted by a provider System to a receiving System; supply of a named result from provider to receiver; receipt or use of that result; a commitment between named Agents; or a consequence relation. The examples define no common relation kind. |
| operating condition | A decision-relevant condition—for example, temperature, load, connectivity, price, an applicable regulation, or an available resource. A condition is a System only when it independently meets the System criteria. |
| functional organization | Selected transformation flows, interactions, and contributions, with the actual Systems that bear or participate in them. |
| constructive organization | Selected actual or proposed parts, bearers, modules, interfaces, and connections. Establish its parthood and connection relations independently of functional contribution. |
| engineering-use account | The episteme returned here: selected Systems, relations, structures, conditions, evidence, unsupported assumptions, and reopen conditions for one use decision. |

Relations commonly hidden by *environment* include parthood, interaction, ownership, location, authority,
access, permission, service provision, use, and consequence. Name the relation that actually bears on the
decision.

### SYSE.16:1 — Problem Frame

Engineering choices—such as choices about System functions, architecture, interfaces, offerings, assurance,
or change—depend on larger working situations. Teams nevertheless often begin with an inside representation,
such as a product boundary, organization chart, component list, requirement set, or model repository. Outside
Systems appear only as labels around a box.

The missing result is not another stakeholder list. The decision needs several selected structures: functional
transformation and interaction, constructive parts and interfaces, direct relations across the selected boundary,
operating conditions, and claims about what may change. One context diagram or tree cannot carry all of them.

### SYSE.16:2 — Problem

A generic environment box hides incompatible claims. A customer can own a System without operating it. An
operator can interact with it without containing it. A building can spatially contain a device while another
System whole receives the result of its functioning. A cloud service can sit outside a product boundary while
remaining part of an offering arrangement. A regulator can constrain Work without being part of the operational
System.

When those relations remain implicit, a plausible concept can fail in use, an interface can be assigned to the
wrong bearer, a provider can promise a result no arrangement can deliver, or later evidence can have no clear
decision to reopen.

### SYSE.16:3 — Forces

Recurring tensions include:

- A small use account helps early decisions; an exhaustive world model is neither possible nor useful.
- Project boundaries simplify Work, while outside Systems and conditions can still change the engineering choice.
- One System can participate in several wholes and selected structures at once.
- Functional transformation and constructive structure must correspond without being collapsed.
- Design choices concern possible futures; actual participation and observed conditions concern what obtains.
- Relevant surroundings continue to change—for example, providers, users, infrastructure, rules, competing
  offerings, or operating conditions.
- Existing vocabulary helps communication but can import ownership, lifecycle, or stakeholder assumptions that do
  not match the current relation.

### SYSE.16:4 — Solution

Recover the smallest set of Systems, structures, relations, and conditions that makes one use decision
well-grounded. Begin with the actual System or intended-system designator selected as the project system-of-interest and a named use situation; stop when the account
exposes a material mismatch, alternative, evidence gap, or reopen condition.

#### SYSE.16:4.1 — Perform the Move

1. **Bound the use and decision.** State the actual System or intended-system designator selected as the project system-of-interest,
   the use situation, configuration or variant, decision, relevant place, interval or horizon, and the description
   sources being used. Keep the descriptions separate from the Systems and situation.
2. **Find containing and receiving Systems.** Identify every larger System that matters because the selected
   System is its proper part, and every System that receives a result of its functioning. State each direct
   relation; retain several wholes when the decision depends on them.
3. **Recover functional organization.** Identify the transformation flows, interactions, and contributions in
   which the System participates, including the changed or receiving Systems and conditions. Use `A.6.F` for
   function-like claims and `E.18.NET` when a transformation-flow network is needed.
4. **Recover constructive organization.** Identify the structures that matter to this use—for example, parts,
   bearers, modules, interfaces, or connections. Use `A.22` for each selected structure and `A.6.M` only when
   module or interface claims obtain. Do not infer constructive parthood from a functional contribution.
5. **Add other Systems and conditions.** Include only a System or condition whose named relation can alter the use
   result or engineering choice. State that relation and its participants or state the relevant condition. Examples
   include a transfer from a named supplier System to a named receiver, access granted by a provider System, a
   permission or commitment between named participants, an available resource, or an operating constraint. When
   provider Work matters, identify the dated Work occurrence, performer Agent, and applied Method separately. Then
   name only the direct relations used by the decision: Agent participation in that Work, the Work's result-
   production relation, supply or access from provider to receiver, receipt or use of the result, a commitment, or
   another governed provision relation. Do not hide any of these objects or relations under *environment*.
6. **Separate future choices from present facts.** Mark descriptions as observations, predictions, design choices,
   commitments, or unsupported assumptions. A proposed interface or whole does not obtain merely because a model
   contains it.
7. **Test outside change.** Ask which relevant outside factors—for example, Systems, conditions, interfaces,
   providers, uses, or regulations—can change during the relevant horizon and which change would reopen the
   concept, architecture, offering, assurance, or configuration decision.
8. **Return the decision-changing result.** Supply the mismatch, alternative, evidence need, or qualified
   assumption to the receiving engineering Work. Leave unrelated surroundings out.

The numbered presentation is an `A.22.CGUS` learning unfolding, not a Work sequence. Work such as observation,
concept development, architecture development, or trial can overlap with changes in outside Systems and recur.

#### SYSE.16:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| focus and decision | Project System-of-interest as an actual System or intended referent, project designation, use situation, receiving decision, configuration, place when relevant, and horizon. |
| containing and receiving Systems | Each larger or receiving System and the proper-part, transfer, interaction, or other direct relation that matters. |
| functional organization | Selected transformations, flows, interactions, contributions, changed or receiving Systems, and operating conditions. |
| constructive organization | Selected parts, bearers, interfaces, modules, and connections needed by the use. |
| other Systems and conditions | Providers, users, resources, constraints, and their stated obtaining or possible-future relations. |
| epistemic status | Observation, evidence-backed claim, prediction, design choice, commitment, or unsupported assumption. |
| co-change and return | Outside changes that reopen the decision, evidence that would reveal them, and the mismatch, alternative, or missing result supplied to receiving Work. |

A thin first-use account needs only one decision-changing containing or neighbouring System, one named relation
or condition, its epistemic status, and one return. A load-bearing unknown names the decision it blocks. The
account can use several representations, but no diagram is the use situation or System whole.

#### SYSE.16:4.3 — What Changes in Practice

The engineer stops asking only what lies outside a product box and asks which Systems, structures, direct
relations, and conditions make this use work. Functional transformation and constructive structure stay
separate, outside change becomes an engineering input, and unsupported assumptions become visible results rather
than hidden context.

### SYSE.16:5 — Worked Case: Upgrading an Occupied Building's Heat-Pump Plant

An engineering team is deciding whether to add a new controller configuration to an existing heat-pump plant for
the next heating season. The decision asks whether occupied rooms can remain within the selected thermal range
while the plant responds to grid signals. A four-box context diagram does not answer it.

The decision-sized engineering-use account distinguishes these structures and relations:

- **Actual System and containing whole.** The heat-pump plant is an actual System and a proper part of the
  building heating System. The proposed controller is still an intended referent. The occupied building and its
  heating System are not assumed to be the same whole.
- **Functional transformation and transfers.** An electricity-distribution System transfers electrical energy
  through the feeder. A signal channel transmits demand-response information. The plant transfers thermal energy
  to the hydronic loop, and the loop and radiators transfer it to room air. Envelope heat transfer and occupant
  control actions also change room temperature. These are different claims, not generic participation.
- **Constructive organization.** The feeder, hydronic connections, sensors, controller interface, signal channel,
  and cabinet clearance are the selected bearers and interfaces for this decision. Their constructive relations
  do not follow from the functional-flow description.
- **Maintenance supply, access, and Work.** Under `MaintenanceCommitment-14`, maintenance company `HeatCare-7` commits to supply `ControllerInspectionResult-14` to building operator `BuildingOperator-1` before the controller-configuration decision. The building operator grants `HeatCare-7` plant-room access during stated windows. Technician `T-4` is the intended Agent for `ControllerInspectionWork-14`; that Work has not occurred. If it occurs, the Work produces the inspection result, `HeatCare-7` supplies the result to `BuildingOperator-1`, and the operator receives it for the controller-configuration decision. The commitment, access grant, intended assignment, capability claim, planned Work, result production, supply, and receipt remain separately supported claims.
- **Systems that may bear consequences.** Residents in a nearby building may experience increased low-frequency
  noise during night cycling. A model supports this possible consequence; no night measurement yet establishes
  an observed effect.
- **Unsupported assumptions.** Sensor latency and occupant override behaviour are unknown at the required load. A
  planned insulation change may alter the thermal model. Cabinet clearance is supported by a drawing but has not
  been checked in the plant room.

The account changes three next decisions. The Agent applying `SYSE.17` uses the possible acoustic-exposure and
maintenance-access consequences. The Agent applying `SYSE.8` uses the provider, access, remote-monitoring promise,
and missing acceptance questions. The Agent applying `SYSE.2` uses the revised use claims and low-noise, cabinet-
location, and remote-monitoring concept alternatives. The team can act on those inputs without first completing
a world model or a full process plan.
**When the full pattern is unnecessary.** If the current question is only whether one already identified sensor
is a proper part of one known controller under an admitted relation, use the direct System and parthood patterns.
A broader engineering-use account adds no value.

### SYSE.16:6 — Bias Annotation

A source or representation—such as an official context diagram, stakeholder list, standard, or organization
chart—does not by itself establish that a relation obtains or a Method is effective. Any capable and authorized
Agent may develop the account; professional title, substrate, and organization label have their own evidence.
Specialist Methods and evidence remain with their domains—for example, electrical, building, safety, legal,
environmental, or financial practice. Agents with the relevant authority make the corresponding decisions.

### SYSE.16:7 — Conformance Checklist

- [ ] The actual System or intended-system designator selected as the project system-of-interest, use situation, receiving decision,
      configuration, and horizon are stated.
- [ ] Actual Systems and intended referents remain distinct from accounts, models, scenarios, and diagrams.
- [ ] *Suprasystem* is used only with a stated actual or possible-future proper-part relation.
- [ ] Functional transformation remains separate from constructive parts, bearers, and interfaces.
- [ ] Other Systems and conditions appear only when a named relation can change the decision.
- [ ] Observations, predictions, design choices, commitments, and unsupported assumptions remain distinct.
- [ ] Outside changes and evidence that reopen the decision are stated.
- [ ] The account returns a mismatch, alternative, evidence need, or qualified assumption rather than an
      exhaustive inventory.

### SYSE.16:8 — Common Failures and Repairs

These recurring abstractions hide a relation that changes the engineering decision:

| Failure | Repair |
| --- | --- |
| Everything outside becomes one environment box | Recover only the wholes, other Systems, conditions, and direct relations used by the decision. |
| Stakeholders stand for operational structure | Identify actual Systems and relations; use `SYSE.17` for consequence-bearing Systems. |
| Every larger or influential object is called suprasystem | Require a proper-part claim or use the actual relation. |
| Function is treated as a component | Keep transformation flows and constructive structures separate and state their correspondence. |
| Diagram is treated as reality | Keep the representation, subject, currentness, and evidence distinct. |
| Outside Systems are held constant | Record co-change and reopen evidence for the relevant horizon. |
| Environment analysis becomes an early phase | Revisit the account when concepts, architecture, evidence, configuration, or outside Systems change. |
| The team models the whole world | Stop at the smallest account that changes the receiving decision or exposes a missing result. |

### SYSE.16:9 — Consequences

Engineering alternatives become comparable in the use that gives them meaning. Interface choices expose their
bearers and receiving Systems, outside changes gain reopen conditions, and System or offering concepts no longer
rely on an unexplained environment label.

The cost is maintaining several selected structures and their correspondence. That cost is smaller than
preserving one stable diagram after its hidden assumptions have ceased to obtain.

### SYSE.16:10 — Rationale

Systems matter through particular part, interaction, transformation, interface, transfer, and consequence
relations under conditions. FPF supplies the general ontology for those claims. The engineering specialization is
the repeatable move from one use decision to the smallest outside structure that can change concept,
architecture, offering, assurance, configuration, or continuing development.

### SYSE.16:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R6.6:7–10 and R8.4:7–R8.5:2 | Functional, constructive, interface, use, and continuing-development views. | The guides are maintained practitioner syntheses, not proof of universal prevalence or causal effectiveness. |
| [Naikar et al. 2023](https://doi.org/10.1080/00140139.2023.2281898) | Work domain, activity, strategies, social organization, cooperation, and Agent capabilities as coupled design questions in distributed human–AI settings. | Conceptual synthesis with an illustrative application; cognitive work analysis is one candidate Method, not a universal procedure. |
| [Polojärvi, Palmer, and Dunford 2023](https://doi.org/10.1002/sys.21664) | A review of sociotechnical Systems Engineering shows both broad social–technical usage and more precise specialist traditions. | The review proposes no single normative definition and does not show that technical Systems Engineering replaces social, legal, political, or ergonomics Methods. |
| Current FPF `A.1.SCR`, `A.22`, `A.6.F`, `A.6.M`, `C.28`, and `E.18.NET` | Actual-System recognition, selected-structure discipline, function and bearer repair, module and interface discipline, causal qualification, and transformation-flow structure. | These transdisciplinary moves do not supply the engineering-use return or redefine the subject relations used here. |

Reopen only a source-dependent claim that newer evidence can change. A newer standard, notation, or framework does
not by itself establish enacted prevalence, effectiveness, or a reason to restore lifecycle staging.

### SYSE.16:12 — Relations

- `SYSE.1` supplies the System designation, decision, boundary question, alternatives, and reopen evidence needed
  here. Its result creates no temporal order.
- `A.1.SCR` distinguishes an actual acting or changed System from a designation, role word, description, process,
  or organization label.
- `A.22` governs each selected structure. `A.6.F` restores function, bearer, capability, Work, and
  MethodDescription distinctions; `A.6.M` applies only to an obtaining module or interface claim.
- `E.18.NET` applies when the use needs a transformation-flow network. The network is a representation of
  selected transformations and dependencies, not the containing whole or a lifecycle.
- Agents applying `SYSE.17`, `SYSE.8`, or `SYSE.2` can use the account's consequence, provider, or concept
  results. Each Agent rechecks subject, configuration, horizon, evidence, and compatibility for the receiving use.
- Application profiles retain domain Methods and evidence—for example, Methods and results for operating physics,
  safety, legal compliance, medical use, finance, software, electrical systems, buildings, or ships.

### SYSE.16:End

<a id="syse-17"></a>
## SYSE.17 — Find Systems That May Bear Engineering Consequences

### SYSE.17:0 — Use This When

Use this pattern when a decision about a proposed System, configuration, or use change already names some
participants—for example, users, owners, operators, or interacting Systems—but may still omit actual Systems whose
states or decision-relevant characteristics could change through Work or events such as realization, operation,
maintenance, misuse, failure, recovery, retirement, or later modification.

Begin with one proposed engineering alternative or change and the decision that can still alter it. Trace possible
consequences beyond the current contractual, organizational, and technical-interface boundaries. Keep obtaining
relations, modal path claims, observed changes, value judgements, and specialist decisions separate.

The first useful result is a **bounded engineering consequence account**. It names each actual System or intended
System referent that may bear a material consequence, qualifies the consequence and its evidence, and connects it
to an action or unresolved need in the receiving decision—for example, a constraint, alternative, probe, safeguard,
specialist question, monitoring condition, or explicit gap. The account is an episteme; the Systems and changes it
describes remain world-side. Add a value or representation claim only when the receiving decision uses it and its
own grounding is available.
`A.1.CSD` supplies the general discovery move. This pattern specializes it for engineering choices: start from a
proposed System, configuration, or use change and connect qualified consequences to the named engineering
decision.
Use `C.28` when one already identified causal claim is the whole question. Obtain a result from the applicable
specialist practice whenever the decision relies on authority outside Systems Engineering.

### SYSE.17:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| focus of inquiry | A proposed engineering alternative or change, together with the actual System or intended System referent and configuration to which it applies. If an observed result prompts the inquiry, use it as evidence for a newly stated change question. |
| consequence-bearing System | An actual System whose state or decision-relevant characteristic may change under the proposed alternative or change. A possible-future bearer remains an intended System referent inside a modal claim until it exists and can be recognized. |
| supported obtaining relation occurrence | An actual relation occurrence between identified participants under stated conditions. Record its predicate and conditions in a claim and support that claim with evidence; a line in a diagram is only a representation. |
| modal consequence-path claim | An episteme describing relations and changes that may connect the proposed alternative or change to a bearer, with candidate participants, conditions, evidence, uncertainty, and a probe. Establish every world-side relation occurrence in the path separately. |
| consequence claim | A claim about a possible or observed change, bearer, conditions, direction, time, evidence, uncertainty, and causal status. The claim and its world-side change have separate identities. |
| value-qualified consequence claim | A descriptive consequence plus a stated value judgement—for example, benefit, harm, burden, or opportunity—under a named value frame, bearer, scope, and evidence. |
| affected-System claim | A consequence claim that identifies the System bearing the possible or observed change. It supports that bearer–consequence statement; establish any project assignment, authority, or other relation separately when the decision needs it. |
| unresolved decision need | An episteme naming a result or relation that the receiving decision needs but does not yet have—for example, additional evidence, a specialist result, an authority relation, an authorized representative, or a safeguard. |
| engineering consequence account | The episteme returned here: focus, examined situations, bearer references, supported obtaining relations, modal path claims, consequence claims, evidence, uncertainty, decision contributions, unresolved needs, and reopen conditions. |

Test System identity independently for every population or collection. Candidate bearers include actual Systems
such as a person, organization, technical System, or ecological System. Keep a not-yet-present or unidentified
bearer as an intended System referent inside the modal claim. A project assignment or decision authority requires
its own grounding.

### SYSE.17:1 — Problem Frame

Engineering decisions and descriptions guide realization, operation, maintenance, and modernization Work. The
resulting changes can reach Systems outside the project's influence and formal organization—for example, a
downstream resident, future operator, maintenance provider, ecological System, supplier, bystander, competing
resource user, or later user. Discover such a bearer from the consequence claim rather than from a stakeholder
label.

The engineering problem is to discover enough consequence-bearing Systems, qualify the claims about them, and
return unresolved consequences while the receiving engineering decision can still be altered.

### SYSE.17:2 — Problem

Stakeholder lists are commonly built from cues such as visibility, power, contracts, interfaces, or organization
charts. Those cues can miss, for example, quiet, weakly represented, future, indirect, non-human, or cross-boundary
consequence bearers.
The opposite error is to call every mentioned party affected without naming a change, evidence basis, or decision
use.

Diagrams create another error: a plausible arrow from a proposed change to a possible bearer is reported as an
actual relation or causal effect. Treat the arrow as a representation and ground its participants and predicate
separately. Scale words such as *person*, *team*, *organization*, *society*, and *ecosystem* provide candidate
scopes; recover actual Systems, whole–part relations, causal relations, and observed changes from their own
evidence.

Too little discovery exports cost or harm. Unbounded discovery makes action impossible because every imaginable
consequence appears equally real and authoritative.

### SYSE.17:3 — Forces

Recurring tensions include:

- Consequences can cross, for example, contractual, ownership, organizational, interface, and project boundaries.
- Early choices need expert judgement; exhaustive measurement is often unavailable or uneconomic.
- A weakly supported possibility can justify a cheap probe or reversible design, but not an observed-effect claim.
- A descriptive consequence claim, a value judgement, and a deontic or governance claim use different predicates
  and evidence.
- Constituent, containing, neighbouring, and later reidentified Systems can change differently; aggregates can
  hide those distributions.
- Specialist safeguards must inform the engineering decision without Systems Engineering claiming authority it
  does not have.

### SYSE.17:4 — Solution

Apply the general affected-System discovery move to one proposed engineering alternative or change. Retain only
consequence claims that change or hold open a named engineering decision, and state what supports each claim.

#### SYSE.17:4.1 — Perform the Move

1. **Name the focus and receiving decision.** State the proposed alternative or change, the actual System or
   intended System referent and configuration to which it applies, the use situation, relevant scope and horizon,
   and the engineering decision that can use the result.
2. **Generate consequence-producing situations.** Consider Work and events that may expose the alternative's
   consequences—for example, realization, intended use, maintenance, plausible misuse, failure, recovery,
   retirement, or later modification. Retain only situations whose consequences could alter the receiving decision;
   these examples do not impose a lifecycle.
3. **Trace outward without promoting hypotheses to facts.** Follow supported obtaining relation occurrences
   separately from modal consequence-path claims. For each modal path, name candidate participants and proposed
   relation kinds—for example, material transfer, energy transfer, information transfer, exposure, access, resource
   use, an economic relation, or an institutional relation—together with conditions, evidence, uncertainty, and a
   feasible probe.
4. **Recognize the bearer.** Identify each actual System from evidence about its identity and boundary. A role
   label, organization name, collection, description, or representative can help locate a candidate but does not
   establish that identity. Keep a possible-future bearer as an intended System referent in the claim until the
   System exists and can be recognized. Record an honest unknown when recognition needed by the decision fails.
5. **Qualify the consequence.** State the characteristic or condition that may change, bearer, configuration,
   conditions, direction or magnitude cue when known, interval, and uncertainty. Distinguish an observed occurrence
   from a modal claim. State the evidence basis—for example, observation, measurement, simulation, model-based
   prediction, or a bounded expert estimate—and its limits. Use `C.28` when reliance depends on a causal,
   intervention, or counterfactual claim.
6. **Add value and specialist claims only when needed.** Name the bearer and value frame for a value-qualified
   consequence—for example, a claimed benefit, harm, burden, opportunity, or accepted loss. Preserve conflicts and
   distributions. Send specialist questions with the System, claim, evidence, and receiving decision; keep the
   returned authority boundary visible.
7. **Change the engineering choice.** Add or revise a decision contribution—for example, a constraint, alternative,
   probe, safeguard, monitoring condition, reversible step, refusal, or escalation. When that contribution relies
   on permission, authority, responsibility, or representation, establish the required relation separately.
8. **Stop with a useful residual.** Return the smallest account that changes or holds open the decision. Record
   plausible missing bearer references or modal paths and the cheapest next discovery action. Name what would
   reopen the decision—for example, a new observation, a newly identified System, changed evidence, a specialist
   result, or an outside change.

The numbered presentation is an `A.22.CGUS` learning unfolding, not a required Work sequence. Discovery,
design, trial, specialist inquiry, and consequence observation can overlap and reopen one another.

#### SYSE.17:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| focus and receiver | Proposed alternative or change; actual System or intended System referent and configuration to which it applies; use, scope, horizon, and receiving engineering decision. |
| examined situations | Consequence-producing Work or events retained because their consequences could alter the decision. |
| bearer references | Each actual System and its recognition basis, or each intended System referent and modal-reference basis; unresolved population, collection, or whole questions remain explicit. |
| relations and modal paths | Supported obtaining relation occurrences; separately stated modal consequence-path claims; conditions, evidence, uncertainty, probes, and missing-relation blockers. |
| consequence claims | Changed characteristic or condition, bearer, configuration, time, direction or magnitude cue, observed-or-modal status, evidence basis, uncertainty, and causal status. |
| value and specialist results | Current value judgement and value-frame source, any conflict, the required specialist result, and its authority boundary. |
| engineering decision contribution | A named change to or unresolved need in the receiving decision—for example, a constraint, alternative, probe, safeguard, monitoring condition, reversible step, refusal, escalation, authorized representative, or protection result. |
| residual and reopen | Plausible missing bearer references or modal paths, cheapest next action, and the concrete change or observation that reopens the decision. |

A thin first-use account can contain one qualified consequence and one named uncertainty—for example, an
unidentified bearer, unsupported relation, or missing specialist result—when they already change the decision. A
bounded expert estimate is usable when better evidence is not affordable; label it as judgement with its basis and
uncertainty rather than measurement or prevalence evidence.

#### SYSE.17:4.3 — What Changes in Practice

Visibility, influence, contract, and project role stop being the entry criteria. Engineers trace a proposed
alternative or change to actual Systems or intended System referents, distinguish obtaining relations from modal
path claims, and feed uncertain but material consequences back into decisions while change remains affordable.

### SYSE.17:5 — Worked Case: Quiet Consequence Bearers of a Heat-Pump Upgrade

The engineering-use account from `SYSE.16` describes an existing heat-pump plant, a proposed controller, the next
heating season, and the architecture decision. The team examines consequences of the proposed controller for
Systems not captured by the original user-and-owner list:

| Possible bearer and change | Claim and evidence status | Engineering decision contribution |
| --- | --- | --- |
| Heat-pump plant: increased compressor cycling and wear | The current command relation obtains. Manufacturer data support a conditional wear estimate; the proposed configuration has not run for a heating season. | Add a cycle-rate constraint and monitored-service condition. |
| Maintenance-provider organization: higher expected inspection workload and less remaining recovery capacity | Service records and the current agreement identify the provider organization and the maintenance Work it performs. The additional workload remains an estimate, and no current commitment covers it. | Keep remote monitoring conditional; use `SYSE.8` or `SYSE.24` to settle provider capacity and commitment. |
| Maintenance technician: reduced cabinet clearance and greater exposure during inspection | Current geometry is described by drawings; the reduction under the proposed cabinet position remains unmeasured. | Hold the cabinet-location choice open pending a plant-room measurement and specialist safety result. |
| Individual residents in a nearby building: increased low-frequency night noise | An acoustic model supports a possible increase; no night measurement establishes an observed effect or its distribution among residents. | Add a low-noise alternative and a pre-release measurement. The model settles neither legal compliance nor ethical acceptability. |
| Individual building occupants: room-temperature deviation during grid load shifting | Current thermal relations are supported, but sensor latency, override behaviour, and the distribution of deviations among occupants remain unresolved. | Add a latency trial and an override-safe concept branch before selection. |
| Electricity-distribution System: changed peak-load contribution | Meter history supports the baseline; the proposed controller effect is simulated. | Keep the grid-response claim conditional and add a measurement requirement. |

Each row names a possible or observed change rather than inventing a stakeholder role. Each row supports only
the stated consequence and decision contribution; ground any authority or representation used later with separate
evidence. The team can make a reversible architecture choice using these qualified contributions without claiming
that every consequence has been measured.

**When the full pattern is unnecessary.** If one identified causal claim about one already identified System is
the whole question, use `C.28` and the direct subject pattern. A broader consequence-discovery account adds no
value.

### SYSE.17:6 — Bias Annotation

Trace consequences from proposed engineering alternatives and changes rather than sector stakeholder
taxonomies or institutional visibility. Declared compliance, publication volume, and academic or press attention are evidence about documents
and discourse. Actual prevalence needs observation or an appropriately qualified estimate of performed practice.

Use affordable evidence. A bounded expert estimate, simulation, or modal path claim can justify a reversible probe;
an observed-effect claim needs observation. Include any actual System or intended System referent whose qualified
consequence can change the decision; specialist authority remains with the applicable practice.

### SYSE.17:7 — Conformance Checklist

- [ ] One proposed alternative or change, its actual System or intended System referent, configuration, use,
      horizon, and receiving decision are stated.
- [ ] Actual Systems or intended System referents are found by tracing the proposed alternative or change, not by
      closing a role or stakeholder list.
- [ ] Supported obtaining relation occurrences remain distinct from modal consequence-path claims and
      missing-relation blockers.
- [ ] Every affected-System claim states the qualified consequence and bearer; every further relation used by the
      decision is grounded separately.
- [ ] Every material claim states bearer, changed characteristic or condition, configuration, time, evidence,
      uncertainty, and causal status.
- [ ] Every value-qualified consequence names its bearer and value frame, and any conflict remains explicit.
- [ ] Each retained consequence changes or holds open an engineering choice through a named decision contribution.
- [ ] The account records residual uncertainty, the cheapest next action, and a concrete reopen condition.

### SYSE.17:8 — Common Failures and Repairs

These recurring failures hide a bearer, relation, claim status, or decision contribution:

| Failure | Repair |
| --- | --- |
| Only purchasers, owners, formal roles, or influential participants appear | Trace the proposed alternative or change outward and challenge the current boundary. |
| An affected-System claim is read as a project role | State the System and consequence; add a role or assignment only when that separate relation obtains. |
| A System is ignored because it cannot object | Discover bearers from possible consequences, whether or not they can object or are represented in project governance. |
| A diagram arrow becomes an actual relation | Keep it as a modal path claim until the represented relation occurrences and conditions are supported. |
| Scale labels become a System hierarchy | Recover actual Systems and the relations used to organize them; a scale label is only a search cue. |
| Every mentioned party is called affected | Require a decision-relevant possible or observed change under stated conditions. |
| Consequence list becomes an ethical verdict | Send actual value conflicts and authority questions to their governing practices. |
| Simulation becomes causal proof | Use `C.28` and retain the narrower supported claim. |
| Inquiry produces no usable result until definitive research exists | Use a bounded expert estimate or uncertainty claim when it improves a reversible choice. |
| Official visibility becomes prevalence | Separate source status, enacted practice, observed consequence, and expert estimate. |

### SYSE.17:9 — Consequences

Engineering decisions become harder to optimize for visible participants while exporting consequences elsewhere.
Quiet and future bearers enter through qualified consequence claims. Those claims can change the decision through,
for example, a probe, safeguard, specialist result, monitoring condition, or unresolved decision need.

The cost is additional inquiry and maintenance of uncertain claims. Every retained bearer or modal path claim must
change a decision, evidence need, probe, or reopen condition so the account does not grow without bound.

### SYSE.17:10 — Rationale

`A.1.CSD` supplies the transdisciplinary discovery action. Systems Engineering adds a recurring subject-specific
move: start from a proposed System, configuration, or use change, examine physical and operational consequences,
and connect qualified claims to the engineering decision that can still change the choice.

This specialization changes the engineering action while reusing the FPF result for discovering consequence-bearing
Systems. Questions that need specialist authority remain with the applicable practice.

### SYSE.17:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R5.3, R5.6, and R6.4 | Recurring omission problem, toxic-pipe and public-use cases, active discovery, and repairs to universal preference, agreement, and immediate-contribution claims. | The guides are maintained practitioner syntheses. Retain only claims that survive the current ontology and evidence checks. |
| [Polojärvi, Palmer, and Dunford 2023](https://doi.org/10.1002/sys.21664) | Systems Engineering literature reaches sociotechnical and societal settings and benefits from precise specialist accounts. | Use the review as evidence for that scope and need; ground any universal definition or sufficiency claim separately. |
| [Volden and Welde 2022](https://doi.org/10.1016/j.ijproman.2022.06.006), [Williams et al. 2023](https://doi.org/10.1080/09537287.2023.2256287), and [Thabit, Sancino, and Mora 2025](https://doi.org/10.1111/puar.13877) | Plural success criteria, changing beneficiaries, continuing benefits, representation, equity, and broader outcome concerns. | Use these studies for the reported plurality and changing concerns; choose any score, representative, aggregation Method, or decision result under its own evidence and authority. |
| FPF `A.1.CSD`, `A.1.SCR`, `A.10`, `C.27`, `C.28`, `D.1`–`D.5`, and `E.10.ROLE` | General bearer and consequence discovery, System recognition, evidence, time, causality, value and conflict handling, audit use, and role-word recovery. | This DPF contributes recurring consequence-producing engineering situations, configuration inputs, receiving engineering decisions, and the specialist-interface move. |

Reopen only a source-dependent claim that newer evidence can change. Treat a new standard or academic framework
as evidence about its published claims; use observations or qualified estimates of performed practice for
prevalence and effectiveness.

### SYSE.17:12 — Relations

- `A.1.CSD` supplies the general discovery move and bounded consequence account. This pattern adds engineering
  alternatives, configuration, physical and operational situations, decision contributions, and specialist
  interfaces.
- `SYSE.1` supplies the System and candidate boundary; `SYSE.16` supplies use structures, other Systems,
  conditions, and unsupported assumptions. Equivalent qualified direct sources can be used without implying a
  temporal order.
- `A.1`, `A.14`, `B.1`, `B.1.2`, and `C.13` govern Systems, wholes, collections, delimitation, crossings, and
  constructive facts. Treat a scale word only as a cue until those objects and relations are grounded.
- `C.28` qualifies a causal-use claim. The Agent performing consequence-discovery Work applies this pattern to
  identify the Systems that may bear consequences and supplies the resulting account to the receiving engineering
  decision.
- `D.1`–`D.5` govern value frames, actual conflicts, mediation, and audits when those questions arise. An
  affected-System claim states the qualified consequence and bearer.
- A compatible consequence account can inform `SYSE.2`, `SYSE.8`, `SYSE.4`, `SYSE.6`, `SYSE.10`, `SYSE.14`, and
  specialist practices. Each receiver rechecks focus, configuration, use, horizon, evidence, and authority.
- Application profiles retain their own consequence-discovery Methods—for example, safety, security, medical,
  ecological, legal, economic, software, electrical, building, or transport specializations.

### SYSE.17:End

<a id="syse-2"></a>
## SYSE.2 - Develop Linked Use and System Concepts

### SYSE.2:1 - Problem frame

Use this pattern when a project has selected an actual System, retained an intended System referent, or bounded
another engineering subject, but the proposed concept cannot yet be defended through concrete use. The team may
have, for example, an internal block diagram, requirement set, component list, product concept, or preferred
technical solution
while phrases such as *environment*, *suprasystem*, *using system*, *Concept of Operations*, *use case*,
*scenario*, *requirement*, or *user story* stand in for several Systems, intended System referents, conditions,
relations, and effects. A compatible `SYSE.16` use-context account supplies decision-relevant operational
structures, neighbours, conditions, and outside changes. A compatible `SYSE.17` affected-system account supplies
qualified consequence claims and unresolved bearers. This use consumes only those compatible result claims.

A conforming use returns a **linked use-and-system concept proposal**: bounded claim content that connects a
concrete
use situation with a candidate System concept and states their main uncertainty. One or more descriptions may
carry the claims; no document form is required.

First useful move: link one concrete use claim to one candidate system-concept claim and state their main
uncertainty. This is enough to expose a grounded architecture question. Add further content—for example,
another use situation, structure, participant, failure, effect, or representation—only when it can change the
candidate or its boundary.

If this link is missing, internal elegance can substitute for usefulness. A pump passes a component test but
worsens downstream flooding; planning software is installed but cannot support production decisions with the
available data; a retrofit design works in an empty building but cannot be realized while the building is
occupied.

The payoff is a revisable account that keeps outside use connected to concept content about the selected actual
System, retained intended System referent, or other bounded engineering subject. Evidence about use can change
that concept content, while architecture and realization findings can change the use, boundary, or
affected-System claims.

Use this pattern while a concrete use claim and a candidate System concept still need to be developed together.
Use `C.30` and `C.32` when the current question is grounded architecture and candidate synthesis, `A.3.4` when
the question is whether one actual bounded change occurred, and the applicable Operations Management pattern
for continuing Work. Return to `SYSE.1` when evidence changes which System should orient the project.

At the first consequential use of source wording, ask: **does this claim connect concept content about the
selected actual System, retained intended System referent, or other bounded engineering subject with a concrete
use situation, participating or affected Systems, conditions, and outside effects?** If yes, name those
subjects and relations and use this pattern. A representation—for example, a ConOps, use case, scenario,
requirement, user story, diagram, or model—presents some of these claims. Its form establishes neither their
truth nor the required form for the proposal.

### SYSE.2:2 - Problem

A project-system choice does not determine the useful boundary or organization of the selected actual System or
intended referent. The same desired effect can be achieved through different actual or proposed changes—for
example, changes to the designated System, an external System, an interface, a
Work arrangement, or several sides together. A containing System may matter, but parthood must be established
directly. Use, interaction, placement, ownership, authority, affectedness, and shared environment are other
relation kinds and require their own grounds.

One-way handoffs make this worse. A supposedly complete use description is handed to concept development, then
architecture or realization discovers that the use cannot be supported. Conversely, one attractive technical
concept narrows the use description until only its successes remain visible. The recurring engineering problem
is to develop the use claims and system concepts together while preserving the distinctions needed to return a
failed claim.

### SYSE.2:3 - Forces

| Force | Tension |
| --- | --- |
| Outside effect and project boundary | Use justifies the System concept, while the useful change may cross the assumed boundary. |
| Several environment Systems and one simple story | A compact scenario helps reasoning, while one hierarchy can hide non-nested participants and affected Systems. |
| Function and feasible bearer | Required functioning guides concept development, while a function word or diagram does not supply a bearer. |
| Working descriptions and physical grounding | Models and scenarios keep claims inspectable, while their form does not establish use, transformation, architecture, or evidence. |
| Early usefulness and completeness | One linked claim can expose the next question, while a fixed comprehensive form delays learning. |
| Continuing revision and decision stability | Use and concept claims must change with evidence, while each downstream architecture question needs a stated current basis. |

### SYSE.2:4 - Solution

#### SYSE.2:4.1 - Start with one decision-changing use situation

Take the selected actual System or intended System referent and current reason from the project-system choice
account, or state the bounded engineering subject when no project-system choice is needed. If that choice is
needed but no compatible `SYSE.1` account is available for the same subject and decision, use a qualified direct
source for the focus claim or record the missing project-focus result and stop only the linked claim
it blocks. For an actual System, describe an actual or possible-future situation in which it participates. For a not-yet-present referent, keep the
intended participation in modal plan, decision, or description content; do not assert an actual System or
participation relation before identity inception. State:

1. the subject that relies on, uses, changes, or is affected by the proposal;
2. the direct relation by which that subject enters the use;
3. the condition or change expected;
4. the outside effect that matters to the current decision; and
5. the uncertainty that could change the concept.

Name the relying subject under its admitted kind; a person and a System are only two possible kinds. State the
direct relation by which it enters the use—for example, reliance, participation, performed Work, or affectedness.
Include affected Systems or intended System referents whenever their qualified consequence claims can change the
decision; participation in or ownership of the designated System is not required.

#### SYSE.2:4.2 - Name the subjects and direct relations hidden by environment language

Start from compatible current `SYSE.16` and `SYSE.17` results for the same subject, configuration, use, horizon,
and decision. If either result is unavailable, recover only the subjects and direct relations needed for the first
linked claim. Use `SYSE.16` when the decision needs several operational structures or a co-change boundary, and
`SYSE.17` when it needs active discovery of consequence-bearing Systems. A neighbouring System may matter, for
example, through constructive parthood, placement, interface, interaction, causal participation, use,
transformation, collection membership, assignment, ownership, permission, authority, or affectedness. State
only relations that are current and apply the FPF pattern that defines or constrains each claim.

Use `A.1.SCR` when the System status of a proposed participant or containing whole is unresolved. Use `A.22`
when the current question selects an organization among independently identified constituents and obtaining
relations for a named use. Keep several non-nested structures when one decomposition would hide a relevant
claim—for example, an interaction, control relation, affected System, or source-return condition.

Authority constrains who may change a System; it does not draw the System boundary. Ownership can matter to a
decision without establishing containment. A proposed containing whole is useful only when its actual part
relations and whole-level consequences change the use or concept.

#### SYSE.2:4.3 - Develop the use claim and candidate system concept together

Write one outside-facing use claim and one inside-facing concept claim:

```text
Linked use-and-system concept proposal:
  concrete use claim:
  candidate system-concept claim:
  main uncertainty:
  architecture question exposed:
  reopen condition:
```

This is a readable rendering, not a mandatory form. The use claim names participating or affected Systems,
conditions, expected transformations or behavior, and outside effects only as far as the current decision
needs. The system-concept claim names what the proposed concept needs—for example, a boundary, functioning,
interface, resource, constraint, or placement—without pretending that a full architecture has already been
selected.

Use `A.6.F` when function-like wording carries a claim. Name the required functioning and its proposed bearer.
Any remaining question—for example, about function, capability, Method, Work, module, interface, evidence, or
architecture—stays under the pattern that defines or constrains it. Use `A.6.M` only when an actual module or interface claim is
current. If no feasible bearer can support required functioning, revise the concept or use claim before
admitting an architecture candidate.

Use `A.3.4` for an actual observed transformation only after the continuing subject, boundaries,
before/during/after facts, and continuity rule are available. A required, intended, or simulated transformation
remains modal claim content; its description does not establish that the change occurred.

A functional or transformation-flow description of relevant environment structure can support the linked
proposal, but it is not the whole proposal. It shows selected functioning or flow relations for a named use;
the proposal also states which use situation matters, which Systems participate or are affected, which outside
effect changes the decision, which candidate System concept is being considered, and what remains uncertain.
Model only the environment structure needed by those claims rather than an imagined complete suprasystem.

#### SYSE.2:4.4 - Compare changes on either side of the boundary

Develop alternatives when changing a different subject would change the engineering answer. Compare, for
example:

- an actual or proposed change to the designated System;
- a change to an external System or operating arrangement;
- a changed interface, placement, or resource relation; or
- coordinated changes on several sides.

Use a compatible `SYSE.8` provider-arrangement account episteme when its supported provider-arrangement claims
or design constraints change the use, candidate System or intended referent, boundary, interfaces, realization
needs, or evidence. Consume only the compatible claims named for this use. Without a compatible current
`SYSE.8` account, use a qualified direct source for the needed provider-arrangement claim or record the missing
result and stop only the linked claim it blocks. Either account
may need revision when a shared claim changes; that dependency does not prescribe the order of engineering Work.
Obtain other decision-changing results from the specialist practice that owns them—for example, organization
change, Operations Management, Platform Engineering, Governance, safety, security, ethics, law, or finance—
rather than inventing their Methods inside this pattern. Keep each result claim linked to the
use or concept claim that consumes it.

For example, when source material names a product-service system, digital twin, digital thread, MBSE, PDM, PLM,
eXperience platform, or Multi-D arrangement, recover the actual contribution before using the umbrella term. A
concrete contribution—for example, a maintained model, configuration relation, simulation, observation return,
integration capability, or change decision—can enter the linked proposal through its direct claim. The umbrella
name alone does not decide whether this pattern, architecturing, realization, assurance, or a specialist practice
is the next use.

#### SYSE.2:4.5 - Expand only when another claim can change the candidate

The cheap first result is one linked use claim, one candidate concept claim, and their main uncertainty. Expand
when further content—for example, another use situation, load, failure, participant, affected System, harm,
benefit, or representation—could change the candidate. Add only the relevant:

- environment structures and obtaining relations;
- transformations, interactions, conditions, and effects;
- functioning, interface, placement, resource, and constraint claims;
- correspondence between a representation and the represented claims;
- alternatives, assumptions, evidence limits, and specialist returns.

If source words such as *operational system*, *system in operation*, *operations*, or *operational flow* are
current, distinguish two questions. Use this pattern for a System's participation in use and the concept that
supports it. Use Operations Management when the difficulty is managing continuing Work, queues, policies, or
flows. An operational adjective does not settle that choice.

#### SYSE.2:4.6 - Stop at a grounded architecture question and reopen from failed support

Stop when the current use claim and candidate concept expose a grounded architecture question and their main
uncertainty. The linked proposal supplies required functioning, operating conditions, outside effects,
decision-relevant environment structures, assumptions, and evidence limits to `C.30` and `C.32`.

Use `C.30.ASV` only when a structural description and its adequacy for a selected architecture use are current.
Do not open a full view or architecture-description apparatus merely because a sketch helped the discussion.

Reopen the smallest linked claim when:

- the use claim and concept claim no longer support each other;
- a candidate architecture lacks a feasible bearer or hides a harmful effect;
- realization evidence defeats an interface, resource, placement, or capability assumption;
- operating observation changes a condition or effect; or
- a specialist result changes permission, feasibility, harm, value, or the participating Work arrangement.

Return to `SYSE.1` only when the failed claim changes which System should orient the project or where the project
boundary lies.

### SYSE.2:5 - Archetypal Grounding

#### Pumping station under flood risk

In the preceding `SYSE.1` use, the engineer retains the intended referent `PumpingStation-P1` in decision content
and records downstream exposure as unresolved. No actual `PumpingStation-P1` exists yet. The first linked proposal
says:

```text
use claim: the intended referent would move water under the selected flood load without unacceptable downstream harm
system-concept claim: the description assigns pumping, positioning, power, control, and discharge functioning to the intended station referent
main uncertainty: downstream conditions may make the proposed discharge harmful
architecture question: which selected structures and possible bearers could support the claim
```

This is enough to use `C.30` and `C.32`. A component pump test can contribute evidence about an actual bearer,
but it establishes neither the not-yet-present station nor its outside effect. The engineer uses downstream-harm evidence to revise the use claim. The project-system choice reopens only if
the station referent no longer supports the project decision.

#### Manufacturer's ERP-enabled planning change

The manufacturer keeps `PlanningSystem-P1` as an intended System referent in its project decision; the phrase does
not admit a future System. Actual person Systems `Planner-A` and `Planner-B` perform `PlanningWork-PW1`. They use
actual deployed software runtime `ERP-Runtime-E3` and demand, capacity, material, and production-order records as
resources and evidence. The records are epistemes; `PlanningAPI-PA2` and the user interface are separately
identified interfaces; none is said to *participate* under one generic relation.

The linked use claim says that `Planner-A` and `Planner-B` would revise production commitments during
`PlanningWork-PW1` using current records and `ERP-Runtime-E3`. The system-concept claim describes a possible
future organization in which these actual Systems, records, interfaces, and planning Methods could satisfy a
separately tested A.1 System criterion. Data currentness and interface latency are the main uncertainties. The
ERP vendor's product project can instead select `ERP-Runtime-E3` or its product referent for its own decision.
Installation completion, an organization chart, and user acceptance establish neither the manufacturer's
production effect nor the intended composite `PlanningSystem-P1`.

#### Occupied building heat-pump control

For `HeatPumpPlant-HP1`, `ControllerConfig-C2`, the next heating season, and `ArchitectureDecision-AD1`, the three
compatible input accounts use the same subject, configuration, use, horizon, evidence window, and receiving
decision:

- the `SYSE.16` use-context account states the `BuildingHeatingSystem-BH1` proper-part claim, energy and
  information transfers, plant-room access permission, and unsupported latency, override, insulation, and
  clearance assumptions;
- the `SYSE.17` affected-system account supplies the qualified `AcousticResult-AR4`, `SafetyResult-SR7`,
  `ThermalResult-TR5`, and their authority boundaries, including the unmeasured neighbour-noise and cabinet-
  clearance branches; and
- the `SYSE.8` provider-arrangement account supplies only the supported provider claims and design constraints:
  actual provider System `MaintenanceTeam-MT4`, the current access permission, expected diagnostic Work, the
  communications bearer, and the missing commitment and authority result for remote monitoring.

The linked proposal is therefore changed, not merely annotated:

```text
use claim: occupied rooms remain within the selected thermal range while qualified neighbour-noise and maintenance-access constraints hold
system-concept claim: ControllerConfig-C2 includes a cycle-rate limit, a low-noise branch, a measurable cabinet-location alternative, and a latency-tested override-safe branch
main uncertainty: night acoustic measurement and plant-room clearance are unavailable; remote-monitoring authority and commitment are unresolved
architecture question: which controller, sensor, cabinet, communications, and operating structures support those qualified claims
reopen condition: a specialist result, measurement, provider result, or operating observation defeats one of the linked claims
```

The remote-monitoring branch remains conditional because the provider-authority and commitment result is
unavailable. Realization and WorkPlan descriptions may include cabinet relocation, access preparation, and test
Work, but they are not renamed as the System concept. If no feasible architecture supports the linked claims, revise this proposal. Reopen `SYSE.1` only if the
failure changes the project focus itself.

### SYSE.2:6 - Biases to Watch

Two recurring biases matter here. **Representation lock-in** treats a familiar use-model form as the use itself;
recover the represented Systems, relations, conditions, and effects. **Concept lock-in** narrows use until the
preferred concept always succeeds; keep the use claim revisable and return failed evidence to the smallest claim.

### SYSE.2:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-SYSE2-1` | A conforming use SHALL name one concrete use situation, one candidate system-concept claim, and their main uncertainty before requesting fuller documentation. |
| `CC-SYSE2-2` | It SHALL name the participating and affected subjects and SHALL state each decision-changing relation through the applicable FPF pattern. |
| `CC-SYSE2-3` | It SHALL distinguish parthood, placement, interaction, use, ownership, authority, and affectedness when more than one is current. |
| `CC-SYSE2-4` | Function-like wording SHALL identify the required functioning and proposed bearer through `A.6.F` before architecture use relies on it. |
| `CC-SYSE2-5` | Required or intended transformations SHALL remain modal claims; an actual transformation claim SHALL satisfy `A.3.4`. |
| `CC-SYSE2-6` | A ConOps, use case, scenario, requirement, model, diagram, or other representation SHALL remain distinct from the linked claims it presents. |
| `CC-SYSE2-7` | Conditional expansion SHALL add only information that can change the current concept, architecture question, evidence use, or return. |
| `CC-SYSE2-8` | The stop SHALL expose a grounded `C.30` or `C.32` question and the uncertainty carried into it. |
| `CC-SYSE2-9` | Failed architecture, realization, observation, or specialist evidence SHALL return to the smallest use, concept, or project-focus claim it can change. |

### SYSE.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Environment-as-container | One box called environment, owner, or suprasystem is assumed to contain every relevant System. | Name the participating and affected Systems and the direct relation by which each changes the decision. |
| Representation lock-in | A ConOps, use-case, SysML, FAS, requirements, or story format is required before the working question is known. | Start from one linked claim and choose representations only for the use they improve. |
| Concept-as-finished-architecture | An internal concept diagram is treated as the selected architecture and other structures disappear. | Stop this pattern at the grounded architecture question; use `C.30` and `C.32` for architecture relations, selected structures, and candidates. |
| Fixed outside world | External Systems and Work arrangements are treated as fixed while only the designated System or its intended design may change. | Compare actual or proposed changes to the designated System, an external System, their relations, or several subjects; obtain specialist results where needed. |
| Test-as-benefit | One component or integration test is used as proof of outside use, benefit, acceptance, or complete assurance. | State which claim the evidence can support, its conditions, and which use or concept claim remains open. |

### SYSE.2:9 - Consequences

The project can ask architecture questions from a concrete outside-use basis without waiting for a complete
requirements package. It can compare changes across the assumed boundary, preserve non-nested environment
structures, and return failed evidence to the claim it can actually change.

The cost is ongoing concept maintenance. A use claim, System concept, and representation can diverge as new
evidence arrives. Keeping their relations explicit requires more care than freezing one document, but it avoids
the larger cost of treating an obsolete description as the use or architecture itself.

### SYSE.2:10 - Rationale

A System concept becomes useful to an engineering decision through concrete relations with other Systems and
conditions, yet no single containing whole or representation captures every consequential relation. Linking
use and System concepts makes the outside reason and inside proposal inspectable while leaving architecture
selection to the applicable FPF patterns.

The link is intentionally small. One use claim, one concept claim, and one uncertainty can already reveal a
missing bearer, harmful effect, or misplaced boundary. Fuller descriptions are justified by decisions they can
change, not by a prescribed documentation sequence.

### SYSE.2:11 - SoTA-Echoing

| Current practice line | What changes in this pattern | Source and use | Adoption status |
| --- | --- | --- | --- |
| Current use-case practice starts from user goals, admits human and nonhuman participants and failure paths, and revises end-to-end slices as work proceeds. Model-based system-architecture practice connects use cases to candidate functional groupings and interfaces. | The Solution starts with a concrete use situation and keeps success, failure, participants, behavior, and the system-concept claim connected while both change. | Jacobson et al., *Use-Case 3.0: The Definitive Guide — Refreshed* (2024); Weilkiens et al., *Model-Based System Architecture*, 2nd ed. (2022). These are provider and textbook Methods, not comparative proof of one universal sequence. | **Adopt and adapt.** Use revisable slices and explicit links to candidate functioning; choose the representation form for the receiving engineering decision. |
| Agile and continuing requirements research treats models, requirements, traceability, monitoring, and compliance links as maintained parts of changing work rather than one frozen preliminary package. | The linked proposal stays revisable, and representations are chosen for the decision and maintained only while they continue to carry useful claims. | Liebel and Knauss (2023) report one large software/telecommunications setting; Hernández, Moros, and Nicolás (2023), Norheim et al. (2024), and Kosenkov et al. (2025) synthesize software- and CPS-heavy requirements and compliance work. | **Adapt.** Maintain useful claims and choose representations by use; let the receiving project determine how requirements Work is organized. |
| Product-service system and servitization research treats useful offerings as configurations of products, service Work, provider and customer relations, capabilities, operations, digital support, and consequences. Reported performance is mixed and configuration-dependent. | The Solution compares actual or proposed changes to the designated System, external Systems, interfaces, and Work arrangements and asks for the specialist results that make those alternatives credible. | Brambila-Macias, Sakao, and Kowalkowski (2018); Braga Junior, de Toledo, and González (2020); Kim (2020); Brax et al. (2021); Åkesson et al. (2024); Menon et al. (2024); Zhao et al. (2025). | **Adapt.** Use the cross-boundary design pressure; establish each System, Work, provider relation, Method, and consequence directly in the receiving project. |

These current lines support continuing, use-led, model-linked revision within their stated domains. The guide
contributions at `R6.4:4–7`, `R6.6:7–10`, `R8.4:7`, and `R8.5:1–2`, together with compatible `SYSE.16`,
`SYSE.17`, and `SYSE.8` results, support the domain move: connect a use situation, subjects and relations, qualified consequences, and a candidate concept, and relate
evidence to the claim it can change. Apply each source within its stated domain and test any cross-domain
transfer against the receiving use, Systems, relations, and evidence.

### SYSE.2:12 - Relations

- A `SYSE.1` project-system choice account supplies the selected actual System or intended System referent,
  current reason, boundary question, alternatives, and reopen condition used here. A changed use or boundary
  returns to `SYSE.1` only when it changes the project focus.
- A compatible `SYSE.16` result supplies selected operational structures, conditions, and unsupported
  assumptions; a compatible `SYSE.17` result supplies qualified consequence claims and unresolved representation
  or protection needs; a compatible `SYSE.8` account supplies only its supported provider-arrangement claims and
  design constraints. Use each result only for a compatible subject, configuration, use, horizon, evidence
  window, and decision. These relations do not prescribe an order of engineering Work.
- Use `A.3.4` for the identity and boundary test of an actual bounded transformation. Intended, required, and
  simulated transformations remain claims or representations until that test applies.
- Use `A.6.F` to recover the object or claim meant by function-like wording and select the direct subject
  pattern. Use `A.6.M` only when a module or interface claim is current.
- Use `A.22` for selected-structure identity in decision-relevant environment structures. Use `C.30.ASV` for
  structural-view adequacy only when a description is relied on for a selected architecture use.
- The linked use-and-system concept proposal supplies functioning, operating conditions, outside effects,
  selected environment structures, assumptions, and evidence limits to the architecture question. `C.30`
  defines grounded architecture claims and relations; `C.32` guides candidate synthesis over selected
  structures. This pattern duplicates neither contribution.
- Architecture, realization, operation, or assurance evidence returns to the smallest linked claim it can
  change. Practitioners in organization change, Operations Management, Platform Engineering, Governance, safety,
  security, ethics, law, finance, and other specialist practices keep their Methods and supply only the results
  consumed by the linked proposal.

### SYSE.2:End

<a id="syse-22"></a>
## SYSE.22 — Coevolve Engineering Problems and System-Family Options

### SYSE.22:0 — Use This When

Use this pattern when an engineering project keeps improving one problem statement and one proposed System while
the situation around both has changed. For example, a new operating condition, affected-System consequence,
supplier limit, technology, or evidence result can make the old problem–solution pair obsolete even while its
backlog closes.

Begin with one observation or claim that can change the current engineering decision. Put the selected problem
record beside the System option it currently constrains. State the receiving decision and the claim within it that
would change—for example, an admission rule, comparison coordinate, affected-System consequence, evidence need,
or choice. If none changes, keep the observation without reopening this decision.

The first useful result contains four parts; this is the complete first-result set:

1. the problem records selected for current attention and a separately retained problem archive;
2. actual Systems in current configurations and possible-future System-family specifications with their
   architecture, membership, and effectivity bases;
3. supported problem–option correspondences and unresolved mismatches; and
4. one replayable `ChoiceResult`: choose an option or tie-set, reject the current set, request one worthwhile
   probe, or refer the question to the decision and authority that can answer it.

An Agent makes the bounded choice under authority. Other Agents later perform any authorized experiment or
implementation Work. A `DecisionSubject` states whose choice is represented; this is separate from the Agents who
later perform Work.

Use `SYSE.1`, `SYSE.16`, and `SYSE.17` first when project focus, operating environment, or affected Systems are
unclear. Use `SYSE.2` when one linked use-and-System concept is the immediate result, and `SYSE.6` when the problem
and option set are stable and only an architecture choice remains. Use `C.18` when the question concerns only an
archive or Front. A contested problem formulation may require a Problem Structuring and Decision Support Method;
a changed Method may require Method Engineering.

### SYSE.22:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| problem situation | The world-side condition or relation that can frustrate an interest or intended use. |
| problem record | A `ProblemCard` episteme describing a problem situation or unresolved claim for one decision and period. |
| problem archive | Retained problem records, weak signals, alternative formulations, and stepping stones kept for possible later inquiry under a stated retention rule. This is an open content set governed by that rule. |
| selected problem portfolio | The finite set of problem records receiving attention, resources, or experiments in the current decision horizon. |
| actual System configuration | A world-side System and its obtaining configuration during a stated interval. |
| possible-future System-family option | A specification of a candidate member, variant, or configuration under a named family architecture, membership rule, and effectivity basis. |
| System family | A family relation among member Systems or possible-future specifications under explicit membership and effectivity rules. The family is identified through that relation rather than reclassified as another System. |
| exploration archive | Retained candidate descriptions and lineage kept under a stated exploration-value rule. |
| Front | A non-dominated set identified for one candidate set, admission rule, comparator or dominance relation, characteristic set, and date. |
| decision OptionSet | The finite set admitted for one current `C.11` choice. Membership in an archive or Front supplies no automatic membership here. |
| problem–option correspondence | A supported claim stating how one option changes admission, comparison, consequence, evidence need, or next action for one selected problem. |
| experiment proposal | Possible-future content describing a bounded change and distinguishing observation whose expected decision value can be compared with its cost. |

The following identities are kept separate throughout this pattern: record, world-side subject, possible-future
specification, decision, planned Work, performed Work, and observation.

### SYSE.22:1 — Problem Frame

Engineering problems and System concepts develop together. For example, an architecture can expose a
manufacturing constraint; a prototype can change what users consider possible; an operating failure can reveal
an affected System absent from the original scope; a new component can make a previously unaffordable option
feasible.

Five recurring confusions make that mutual development hard to manage:

1. a problem situation is confused with its `ProblemCard`;
2. a problem archive is confused with the finite portfolio receiving attention now;
3. an actual System is confused with a possible-future specification;
4. an exploration archive or Front is confused with the current decision's `OptionSet`; and
5. an experiment proposal is confused with authorized and performed experiment Work.

These confusions are documented in the source guides and worked cases used by this pattern. Repairing them lets
the project preserve lineage while changing only the claims that the new observation reaches.

### SYSE.22:2 — Problem

The usual failure is a frozen pair: one backlog becomes *the problem* and one baseline becomes *the solution*.
Local optimization continues after a relevant condition changes—for example, intended use, environment, a
protected characteristic, a supplier condition, or the reachable System family.

Another failure retains many alternatives without their identities and rules. A single *portfolio* mixes records
of unlike kinds—for example, signals, problem formulations, architectures, configurations, experiment proposals,
and decisions. A moving Pareto Front then hides changes in its candidate set or comparator and appears to
demonstrate improvement across incomparable questions.

Reopening everything after every signal is equally costly. The project needs claim-sized dependencies and
currentness conditions so that honest reframing does not become administrative restart.

### SYSE.22:3 — Forces

- Stable identities preserve evidence and decisions, while stale problem or family boundaries make that
  continuity misleading.
- Retained variants preserve stepping stones, while a project still needs finite current commitments.
- Shared family architectures reduce repeated Work, while one environment or affected System can require a
  distinct branch.
- Several options can remain non-dominated, while the next project move still needs a choice or probe.
- Novelty can open a useful region, while admission, safety, evidence, integration, and service constraints remain.
- Dependencies support selective reopening, while records that change no decision add maintenance cost.
- A local gain can move cost, risk, Work, or failure exposure to another affected System.

### SYSE.22:4 — Solution

Maintain a finite selected problem portfolio and a separately identified set of System-family options. Connect
them through decision-bearing correspondence claims, compare them under the current use and evidence, and end the
pass with one replayable choice or probe result. Observations from either side can then reopen the other without
discarding archives and lineage.

#### SYSE.22:4.1 — Pattern-Use Unfolding

The Method uses eight recurring moves. They organize production of the account; problem-development, System-development,
research, realization, integration, operation, and decision Work can overlap.

1. **Decision boundary.** The Agent identifies the actual System or intended-system designator selected as the project system-of-interest, or the System family and its
   membership and effectivity rules; current use, environment, affected Systems, configuration, horizon,
   resources, `DecisionSubject`, and authority complete the boundary.
2. **Situation and problem records.** The Agent separates the world-side occurrence or condition from assertions,
   observations, and evidence about it. Each selected `ProblemCard` states detection, problematic relation or
   unresolved claim, improvement check, constraints, affected Systems, evidence, expiry, and receiving decision.
3. **Archive and portfolio.** Alternative formulations and weak signals remain in the archive under retention
   rules. The selected portfolio is finite and states why each record receives current attention or resources and
   what removes or reopens it.
4. **System-family options.** Actual Systems and configurations, candidate architectures, family membership and
   effectivity rules, and possible-future specifications are identified separately. Each option states what is
   realizable now and which builder or platform change it needs.
5. **Problem–option correspondences.** Every relied-on pair states the changed admission, comparison coordinate,
   protected characteristic, affected-System consequence, evidence need, or next action. A pair with no supported
   decision-bearing difference remains an unresolved mismatch.
6. **Plural comparison.** Archives, Fronts, and the decision `OptionSet` retain their own membership rules. The
   Agent compares several result and resource coordinates, protected losses, uncertainty, and non-dominated
   alternatives without manufacturing one scalar objective.
7. **Choice or probe.** The current `OptionSet` is fixed. The deciding Agent performs comparison-and-choice
   Work, applies `C.11.CRC` when a finite configuration-relative contribution comparison is needed, and applies
   `C.11` to produce a decision result: a choice, tie-set, rejection, named probe, or reroute. The Agent selects a
   probe only when its expected decision value exceeds its cost within the available authority and budget.
8. **Later Work and selective reopening.** Assigned Agents plan, authorize, perform, and interpret later Work
   through the applicable relations. New observations reopen only the problem records, correspondences, options,
   Fronts, configurations, or decisions that relied on the changed claim.

#### SYSE.22:4.2 — Record the Result

The joint problem–System-family account contains the eight result positions below. This is the complete content
set for this pattern's first result.

| Result position | Required content |
| --- | --- |
| decision boundary | Project System or System family, membership and effectivity basis, current use, environment, affected Systems, configuration, horizon, resources, chooser, authority, and receiving decision. |
| situation and claim basis | World-side occurrence, condition, or unresolved possibility; separate assertions, observations, evidence, source, interval, and uncertainty. |
| problem archive and portfolio | Retained and selected problem records, their different membership rules, lineage, resources, expiry, stops, and reopen conditions. |
| System-family options | Actual Systems and configurations, family identity, architecture, variant and effectivity rules, possible-future specifications, realizability, and builder dependencies. |
| plural-search results | Exploration archive and each Front with its candidate set, retention or admission rule, comparator, characteristics, date, and currentness. |
| correspondences | Every decision-bearing problem–option claim, its source and uncertainty, plus unresolved mismatches. |
| choice or probe | Fixed `OptionSet`, shared comparison basis, choice rule, probe budget and value when relevant, lawful result, reason, and overturn conditions. |
| continuation | Retained alternatives, planned and performed later Work when it occurs, receiving results, and selective reopen relations. |

#### SYSE.22:4.3 — What Changes in Practice

The project stops treating backlog items and design variants as two fixed columns. It can say which world-side
change reopened which problem–option pair, why a candidate remains in an archive but not the current decision,
and why the next lawful result is a choice, rejection, probe, or reroute.

### SYSE.22:5 — Worked Case: Heat-Pump Controller Family

A manufacturer maintains heat-pump controllers for occupied apartment buildings. The current decision concerns
the controller family and a reversible building pilot. Installed controllers and a laboratory unit are actual
Systems; the options below are possible-future specifications under the family's architecture and effectivity
rules.

The earlier selected problem was peak electrical demand during cold mornings. The preferred specification used a
schedule optimizer and cloud forecast service. Three field observations now reopen the comparison; this is the
complete triggering observation set for the case:

1. several buildings lose network service during the coldest periods;
2. compressor cycling increases service calls in one installed configuration; and
3. a new tariff rewards short demand reductions but penalizes slow recovery that leaves occupants cold.

The current problem portfolio and System-family options produce four correspondence rows:

| Problem record | System-family option | Decision-bearing correspondence |
| --- | --- | --- |
| peak demand, now with recovery-time and occupied-temperature acceptance | cloud schedule specification | Network loss makes the option inadmissible without a qualified fallback; recovery time enters comparison. |
| network-loss continuity | local-fallback specification | Local forecasting can change continuity and recovery, but processor-load and fallback evidence are missing. |
| compressor cycling for the affected configuration | variable-speed-control specification and incumbent control | Variable speed can change cycling and energy use while increasing calibration and service burden. |
| speculative voice-control request, retained only in the archive | voice-gateway specification, retained only in the option archive | No current use or affected-System consequence gives this pair decision priority. |

The final row explains archive retention and current non-selection; it supplies no `OptionSet` member. The first
three rows are the complete correspondence set used by the current decision.

The earlier Front compared energy use and peak demand. The current comparison uses a new candidate set and the
following complete coordinate set: continuity, recovery time, occupied-zone temperature, peak power, compressor
cycling, processor load, calibration effort, and service burden. It is therefore a new Front with its own basis.

The fixed current `OptionSet` has three members:

1. continue developing the cloud-schedule specification;
2. develop the local-fallback specification; or
3. develop the variable-speed-control specification.

Safety and occupied-zone comfort are hard guards. The remaining coordinates form a partial order. The cloud-
schedule specification without a qualified local fallback fails the network-loss guard. The variable-speed option
retains the incumbent local control during network loss and remains admitted, but evidence about processor load
and cold recovery is missing for the local-fallback option. That option cannot yet be admitted or rejected.

The **controller-family council** is the deciding Agent. Its current assignment authorizes it to choose the next
engineering probe and allocate no more than 160 engineering hours. A building operations manager separately
authorizes any occupied-building trial; the product-family owner separately authorizes later adoption. The probe
choice grants neither authority.

The council uses one shared comparison basis:

- The fixed `OptionSet` remains cloud schedule, local fallback, and variable-speed control.
- The current `BeliefState` contains the three field observations, the hard safety and comfort guards, the cloud
  option's network-loss failure, the variable-speed option's admitted local control, and the missing local-fallback
  processor-load and recovery evidence.
- The `OutcomeModel` states how each possible probe observation changes admission and the survivor relation. A
  local-fallback pass admits that option and leaves it non-dominated with variable-speed control; a guard failure
  or processor overload rejects it. The current calibration uncertainty changes burden estimates for variable-
  speed control but does not change its admission or resolve the local-fallback question.

| Candidate next probe | Bounded burden | Distinguishing observations | Effect on the current decision |
| --- | --- | --- | --- |
| Scripted network-loss and cold-recovery trial | 96 engineering hours, two hardware-in-the-loop bench days, one three-day reversible building-pilot window, and about one week of decision delay. | In each of two representative building configurations: no safety violation; occupied-zone recovery inside 20 minutes; and controller processor load below 70%. The contrary outcome is any safety or comfort guard failure or processor load at or above 70%; mixed results remain unresolved. | A pass admits local fallback and leaves it with variable-speed control in the survivor set while cloud-only is rejected. A contrary outcome rejects local fallback and leaves variable-speed control as the admitted next-development option. Mixed results preserve the unresolved local-fallback status and require a new bounded decision. |
| Variable-speed calibration trial | 128 engineering hours, four calibration-rig days, the same single building-pilot allocation, and about two weeks of decision delay. | Calibration effort and service burden may fall or rise within the currently supported range; the trial does not observe network-loss recovery or local-fallback processor load. | Either bounded outcome refines the burden comparison for an already admitted option but leaves the local-fallback admission defect and survivor question unchanged. |
| No probe | No immediate trial resource use or delay. | No new observation. | Local fallback remains unresolved, so the current choice would discard or retain it without the evidence needed by the hard-guard comparison. |

The `ChoiceRule` is: within the authorized budget, choose the least burdensome feasible probe whose possible
observations can change option admission or the survivor relation under the hard guards; choose no probe only when
none has that decision value. The network-loss trial fits the budget and can admit or reject a live option. The
calibration trial costs more and cannot repair the current comparison defect. The deciding Agent therefore applies
`C.11` and records `ChoiceResult-HPF-1 = probe_again` for the network-loss and cold-recovery trial.

That `ChoiceResult` is not a WorkPlan, trial authorization, performed trial Work, or family-adoption decision. A
planning Agent must still prepare the trial plan, the building operations manager must authorize the occupied-
building trial, and assigned Agents must perform and interpret the Work. If pilot authority is withdrawn before
that Work, a new decision pass records `reroute` and the missing authority without rewriting `ChoiceResult-HPF-1`.
Later observations reopen only the three current problem–option correspondences and dependent family results; the
voice-control archive entry remains unchanged.

### SYSE.22:6 — Bias Annotation

The following six biases recur in the source guides and engineering literature used by this pattern.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| requirements-freeze bias | The approved backlog becomes the permanently current problem. | Recover the world-side situation, evidence interval, and expiry; reopen only dependent decisions. |
| solution-fixation bias | Every observation becomes a modification of the incumbent design. | Reopen both problem formulations and family alternatives; admit a branch, replacement, or stop when supported. |
| archive-as-portfolio bias | Everything worth remembering receives current attention and budget. | Keep retention membership separate from current portfolio membership. |
| one-Front bias | Points from changed candidates or comparators are plotted as one improvement curve. | Identify each Front and its basis; make any cross-basis comparison separately. |
| novelty bias | A distant or AI-generated option is treated as useful or admissible by novelty alone. | State the reference set, admission rules, consequences, and evidence. |
| measurement maximalism | The project waits for field-wide prevalence or conclusive causal attribution before a reversible probe. | Use proportionate evidence with explicit uncertainty and limits. |

### SYSE.22:7 — Conformance Checklist

- [ ] The decision boundary identifies the actual System or intended-system designator selected as the project system-of-interest, or the System family; current use, environment, affected
      Systems, configuration, horizon, chooser, and authority.
- [ ] World-side problem situations and `ProblemCard` epistemes remain separate.
- [ ] The problem archive and finite selected problem portfolio have separate membership rules.
- [ ] Actual Systems and configurations remain separate from possible-future specifications.
- [ ] Every option identifies its family architecture, membership or variant rule, and effectivity basis.
- [ ] Exploration archive, Fronts, and current `OptionSet` retain their own candidate and admission rules.
- [ ] Every relied-on correspondence changes a decision-bearing claim or remains visibly unresolved.
- [ ] The comparison preserves relevant result and resource coordinates, protected losses, affected-System
      consequences, uncertainty, and non-dominated alternatives.
- [ ] The choice or probe result states its basis, rule, budget and value when relevant, authority, and reopen
      condition.
- [ ] Proposal, planning, authorization, performed Work, observation, and later adoption retain separate results.

### SYSE.22:8 — Common Failures and Repairs

The rows below are recurring failures documented in the source guides and the heat-pump probe.

| Recurring failure | Repair |
| --- | --- |
| Backlog equals problem portfolio | Repair the selected `ProblemCard` values and state why each receives current attention. |
| Candidate specification equals future System | Keep the specification possible-future; state realization and later-test Work. |
| *Addresses problem* fills every correspondence cell | State the changed admission, coordinate, consequence, evidence need, or next action. |
| Archive equals Front | Preserve archive membership under its retention rule and Front membership under its comparator. |
| A changed Front is presented as improvement on the old Front | Identify both bases and make any cross-basis claim separately. |
| A probe choice is presented as family adoption | Identify later planning, authorization, Work, evidence, and adoption decision. |
| Every new source restarts the project | Trace the source claim to its receiving use and reopen only dependent results. |

### SYSE.22:9 — Consequences

The project can change both what it is solving and what Systems it considers without discarding lineage. Useful
stepping stones remain recoverable, stale comparisons become visible, and one bounded probe can be chosen without
pretending that the final problem or System family is known.

The cost is maintenance of identities and decision-bearing correspondences. Some cells remain unresolved, and
the best current result may be a probe, rejection, or reroute rather than a selected System variant.

### SYSE.22:10 — Rationale

FPF already supplies problem records, plural search, archives, Fronts, currentness, comparison, and choice.
Systems Engineering adds the action-changing specialization: selected problem formulations must be compared with
architecture- and configuration-identified System-family options under project use, operational environment,
affected-System consequences, realization limits, and engineering evidence.

The *problem factory* and *solution factory* from R11 describe different but corresponding Work and Method
structures. They can operate at the same time. Their names establish neither Systems nor a sequence; `SYSE.20`
governs their overlap and required order when that becomes the current engineering problem.

### SYSE.22:11 — SoTA and Source Use

This table is the complete source-use register for this pattern body.

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| R0 and R8 Systems Engineering material plus [R11, *Development for Advanced Practitioners*](../../../GuidesProject/R5-R10-pedagogical-companion-md/converted-md/R11-DevelopmentForAdvanced.md) | Project-System focus, continuing engineering, problem archive and portfolio, comparison and acceptance bases, parity, and recursive problem/System/builder Work. | Treat the guide and seminar as practitioner syntheses; recover each current object and relation through current FPF and direct project evidence. |
| Dorst and Cross (2001), [*Creativity in the design process: co-evolution of problem–solution*](https://doi.org/10.1016/S0142-694X(01)00009-6) | Mutual development of problem and solution spaces in protocol studies of experienced industrial designers. | Use as bounded design-process evidence; establish the current System family and configuration separately. |
| Liker et al. (1996) and Sobek, Ward, and Liker (1999) on set-based concurrent engineering | Communication about design sets, delayed commitment, feasibility, and narrowing in automotive product development. | Transfer the set-based moves only where the receiving profile's constraints and evidence support them. |
| Castle, Stock, and Gorochowski (2024), [*Engineering is evolution*](https://doi.org/10.1038/s41467-024-48000-1) | Variation, expression, evaluation, selection, exploration, and exploitation as an engineering perspective. | Use the evolutionary analogy as a hypothesis source; ground the current engineering Method and cultural claims separately. |
| Taylor (2018), [*Evolutionary Innovations and Where to Find Them*](https://arxiv.org/abs/1806.01883), and Adams et al. (2019), [*The MODES Toolbox*](https://doi.org/10.1162/artl_a_00280) | Exploratory, expansive, and transformational change and operational measures for open-ended dynamics. | Apply these distinctions only when a possibility-space or open-ended-engineering claim changes the current decision. |
| Zhang et al. (2025), [*Darwin Gödel Machine*](https://arxiv.org/abs/2505.22954) | An AI-engineering case retaining a lineage-bearing archive of coding-agent variants for later improvement. | Treat coding benchmarks as one application case; test transfer to physical Systems and causal claims separately. |

Reopen one source-use row when changed evidence alters its practical contribution or boundary.

### SYSE.22:12 — Relations

- `SYSE.1`, `SYSE.16`, and `SYSE.17` supply project focus, operational environment, and affected-System
  consequences for compatible uses.
- `SYSE.2`, `SYSE.6`, `SYSE.7`, `SYSE.10`, and `SYSE.13` supply linked concepts, architecture decisions,
  descriptions, evidence, and family/configuration/effectivity identity.
- `SYSE.15` can supply a compatible engineering-Method repertoire. `SYSE.21` can supply bounded observations of
  an enacted variant and its population; each claim keeps its own evidence and transfer boundary.
- `C.22.2` governs `ProblemCard` epistemes and `C.22.PFR` any world-side `ProblematicForRelation`. `C.17`, `C.18`,
  `C.19`, `G.5`, and `G.11` govern characterization, archives and Fronts, live pools, selected sets, and
  currentness.
- `C.11.CRC` governs finite configuration-relative contribution comparisons and `C.11` the bounded choice.
- The Agent performing `SYSE.22` problem-and-option decision Work supplies its project focus, selected problem
  portfolio, System-family option set, correspondences, unresolved mismatches, and current `ChoiceResult` to the
  Agent making the investment or reconfiguration decision through Work applying `SYSE.23`.
- Feedback reopens `SYSE.2`, `SYSE.6`, or `SYSE.13` only when the changed result crosses their stated reopen
  condition.
- Problem Structuring and Decision Support, Strategy, Method Engineering, and Operations Management retain their
  domain Methods even when their Work uses the same archives or decisions.

### SYSE.22:End

# Part II — Architecture, Descriptions, Offerings, and Professional Contributions

<a id="syse-5"></a>
## SYSE.5 — Develop Functional Organization and Bearer Alternatives

### SYSE.5:0 — Use This When

Use this pattern when engineers can name a desired outside effect, use situation, or observed functioning
failure, but have already treated one familiar bearer cue—for example, a component, product, service, software
partition, or supplier offering—as the only candidate. Use it also when a functional diagram exists but no one
can show which actual Systems or intended System referents could bear the contributions named by its claims under
decision-relevant conditions—for example, operating, interface, placement, integration, or assurance conditions.

The first result is an **account that compares several functional organizations with the Systems and
interfaces that could realize them**. It records proposed many-to-many allocations, the conditions under which
each proposal could work, conflicts among proposals, evidence limits, and the first unsupported dependency.
The account is a claim-bearing episteme used by later architecture-decision Work. Realization and integration
require performed Work; observed functioning and evidence require their own grounding.

**First move.** In one sentence, name the required outside effect, the current decision question, and the first
familiar bearer assumption. Add one materially different way in which the contribution might instead be borne. If no
bearer or allocation choice is current, stop and use `A.6.F` for the function-like claim.

Use this pattern while an allocation choice can change an engineering decision. For one function-like
claim, use `A.6.F`; for one module or interface claim, use `A.6.M`; for transdisciplinary candidate synthesis
across several structures, use `C.32`; and for choosing an architecture from developed alternatives, use
`SYSE.6`. When a subject-specific Method—for example, one for physics, software semantics, clinical action,
electrical protection, or structural integrity—determines the answer, use the relevant application DPF with this
allocation account.

### SYSE.5:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| required outside effect | A claim about a change or preserved condition needed in a named receiving System under stated use and operating conditions. The claim is an episteme; the change, when it occurs, is world-side. |
| functional contribution claim | A function-like claim recovered through `A.6.F`: it names a predicate, a possible bearer, conditions, and the larger effect or functioning to which the contribution matters. A label such as *sense*, *control*, *store*, or *protect* is only a source cue until those positions are recoverable. |
| functional organization | A selected structure of required effects, functional contribution claims, and relations among them for a named System and use. In FPF it is a selected `U.Structure` described by an `ArchitectureStructuralView` in an `ArchitectureOf@Context` claim. Other representations—for example, a parts list, Work breakdown, or sequence diagram—describe their own subjects and require stated correspondence to this structure. Evidence of actual functioning requires its own grounding. |
| candidate bearer | An actual System considered for the contribution, or an intended System referent in candidate content. A bearer entry identifies that System or referent and the proposed contribution. Source cues—for example, a component kind, product label, module name, system-role kind, capability claim, or location—must be resolved to those subjects and relations. |
| constructive organization | A selected structure of actual Systems and relations among them—for example, parthood, connection, or placement—together with decision-relevant boundaries, modules, and physical interfaces; or candidate content describing such a possible-future structure. The structure, the Systems in it, and its descriptions are different objects. |
| interface specification | An episteme stating conditions for interaction across a boundary, such as exchanged quantity, units, geometry, protocol states, timing, capacity, error handling, or effectivity. The specification names its intended participants; actual connectors, conduits, physical boundaries, interaction occurrences, and compatibility evidence are identified separately by their own kinds and relations. |
| proposed function-to-bearer allocation | Candidate content that associates one or more functional contribution claims with one or more candidate bearers for stated use, conditions, configuration, and horizon. Establish any actual assignment, performed Work, demonstrated capability, or obtaining functioning through its own relation and evidence. |
| bearer-and-interface proposal | One linked candidate functional organization, constructive organization, proposed allocations, interface specifications or gaps, operating conditions, and predicted consequences. |
| materially different alternative | A proposal whose physical principle, distribution, placement, containment, redundancy, control boundary, interface grammar, realization dependency, or other selected structure can change the answer to a named decision question. Renaming the same arrangement or changing only drawing notation does not create another alternative. |
| allocation conflict | An explicit incompatibility between claims that cannot be satisfied together under the same conditions, or a protected loss created by one proposal. The account names the affected claims, Systems, characteristics, and conditions. |


Words such as *functional block*, *module*, *service*, *component*, *agent*, *sensor*, *platform*, and *open
interface* do not establish a common kind. Restore their subjects and relations before using them in an
allocation proposal.

### SYSE.5:1 — Problem Frame

An engineered System obtains its use through interactions under conditions. A desired outside effect can often
be produced by several functional organizations, and one functional contribution can often be borne by several
Systems together. Conversely, one System can bear several contributions in one configuration and different
contributions in another. Distribution can change, for example, across operating modes, failure states, product
variants, sites, and time.

The engineer therefore needs more than functional decomposition and more than a component search. The working
result links functional and constructive candidates to their outside use, proposed allocations, interface
realizations, placement, integration dependencies, and evidence. The result table below states its required
content. These selected structures answer different questions and need explicit correspondence where the decision
depends on them.

### SYSE.5:2 — Problem

Starting from the incumbent construction makes familiar parts look necessary. Starting from a functional graph
alone makes abstract elements look like purchasable or assignable things. A supplier search can then be mistaken
for proof that the proposed functioning is feasible, while an unsuccessful search can be mistaken for proof
that no bearer is possible.

The result is an allocation that survives on paper but fails in use. For example, a bearer may lack power,
capacity, placement, access, timing, environmental tolerance, or realization support. Two nominally conforming
interfaces may fail to interoperate. Several Systems must cooperate but their joint contribution and failure
handling are absent. A standard connector admits a damaging wrong connection. A general-purpose supporting
System can reduce one development burden while increasing, for example, latency, energy use, certification Work,
or continuing-change burden. Procurement and Work are
then organized around functional labels before actual supply items, assembly relations, and evidence needs are
known.

The opposite failure is endless decomposition and candidate generation. The engineering account is useful only
when it exposes alternatives and conflicts for a named decision question and stops at the first unsupported
feasibility dependency.

### SYSE.5:3 — Forces

The move must manage these recurring tensions:

- Reusing an incumbent construction saves effort, while it can hide a better physical principle or distribution.
- Functional abstraction protects solution freedom, while abstract labels can conceal, for example, physics,
  operating conditions, or joint bearer requirements.
- A general-purpose bearer can absorb several contributions, while specialization can improve, for example,
  performance, safety, energy use, evidence production, or fault containment.
- Standard interfaces can reduce coordination cost, while compatibility, integration, substitutability, and
  correct-use claims still need their own grounds.
- More alternatives preserve option value, while every alternative adds Work—for example, modeling, specialist
  analysis, comparison, or evidence production.
- Early quantitative estimates help eliminate infeasible candidates, while premature precision can hide
  unknown models, wrong subjects, or unsupported measurements.
- AI-assisted generation can widen a functional candidate set quickly, while bearer-feasibility and
  project-correctness claims still need project evidence.
- Engineering Work must proceed under incomplete knowledge, while later commitments—for example, purchase,
  realization, integration, or release commitments—need progressively stronger grounds.
- Selected structures—for example, functional, constructive, placement, control, information, configuration,
  and evidence structures—constrain one another while each answers its own engineering question.

### SYSE.5:4 — Solution

Develop several functional organizations and materially different bearer-and-interface proposals together. Enter
at the claim that blocks the current decision, keep the outside effect and use visible, and iterate between
functional and constructive accounts. Make every allocation, interface condition, conflict, evidence limit, and
decision-relevant consequence explicit. Use `C.32` for the general multi-structure candidate palette; apply the
Systems Engineering content below to make that palette usable for realization, integration, procurement,
assurance, and continuing change.

#### SYSE.5:4.1 — Perform the Move

1. **Bind the engineering decision.** Name the actual System or intended-system designator selected as the project system-of-interest, decision question,
   use situation, required outside effect or observed failure, configuration or variant, operating envelope,
   horizon, and protected characteristics. Use `SYSE.2` candidates and unresolved use–System mismatches when
   they are current and compatible; otherwise use a qualified direct source or record the missing result.
2. **Restore the blocking function-like claims.** For each material contribution, use `A.6.F` to state the
   predicate, possible bearer, receiving whole or effect, conditions, and claim status. Begin from outside use,
   an observed internal failure, a candidate construction, or a feasibility result as the current question
   requires. Do not turn one useful entry direction into a stage law.
3. **Develop several functional organizations.** Vary how interactions and contributions could combine to
   produce the required outside effect. Include decision-relevant situations—for example, operating, degraded,
   maintenance, recovery, or consequential foreseeable use—when they can change the decision. A tree is optional;
   other selected structures may represent, for example, flows, feedback, cooperation, shared contributions, or
   mode-dependent relations.
4. **Generate materially different bearer arrangements.** Start with actual or intended Systems that might
   carry the contributions. For each arrangement, state how each candidate System would be obtained and operated—
   for example, by using an available System, procuring or realizing one, relying on provider Work, or combining
   software and physical Systems. Record shared resources and changes to supporting Systems as dependencies
   unless they themselves carry a contribution. Vary decision-relevant structures—for example, physical principle,
   distribution, placement, redundancy, containment, control boundary, or interface grammar. State separately
   whether an actual System exists, whether it is procurable, what realization or provider Work is needed, and
   which candidate claim still lacks support.
5. **Write many-to-many proposed allocations.** Associate functional contribution claims and candidate bearers
   explicitly. Permit several bearers for one contribution, several contributions for one bearer, and different
   allocations by mode, use, configuration, place, or effectivity. Treat weak cues—for example, co-location,
   matching names, diagram overlap, product kind, ownership, or system-role assignment—only as possible evidence
   for a separately stated claim.
6. **Develop interface and placement conditions.** For every material interaction, state the boundary and
   participants. Add the conditions that matter to the decision—for example, exchanged quantity or signal,
   units, geometry, protocol states, timing, capacity, environment, error handling, configuration, and
   effectivity. Identify the physical realization or missing realization separately from the interface
   specification. Add decision-relevant constraints—for example, placement, access, assembly, maintenance,
   supply, or resource constraints—when they change feasibility.
7. **Challenge intended and unintended interaction.** Test the proposed arrangement against relevant cases—for
   example, loads, failures, swaps, reversals, stale configuration, unavailable resources, human or machine
   misuse, and external change. For consequential wrong use, compare candidate changes—for example, to geometry,
   keying, protocol, control, detection, containment, or operation. A mitigation lowers only the tested interaction possibility
   under its conditions.
8. **Check realization and integration dependencies.** Identify each dependency needed to make and join the
   bearers—for example, a System, Method, capability, resource, service, assembly Work, configuration episteme,
   or specialist result. Record each dependency with its own kind and relation to the proposal. Distinguish a missing catalogue
   item from a missing physical principle and from a missing project capability. When a recursive realization
   dependency is current, use `SYSE.3` to develop it; do not hide it in a module name.
9. **Compare engineering consequences.** For each proposal, state predicted gains, losses, and unknowns for the
   current decision. Use characteristics such as performance, energy, safety, security, fault containment,
   latency, placement, service access, manufacture, assembly, integration, supply, cost, configuration,
   changeability, evidence burden, and affected-System consequences only when their subjects, conditions,
   Scales, and comparison frames are explicit. Bring in specialist Methods for the actual physics and risks.
10. **Exercise a representative slice.** Choose challenge Work suited to the claim—for example, computation or
    simulation Work, prototype-building and test Work, or a physical trial—and use representative conditions. Identify
    each performed Work, the Agent that performed it, and the observations produced. A model, simulation result, or trial
    observation remains an input to later claim assessment; its form alone does not establish feasibility of the
    whole proposal.
11. **State the decision use and local stop.** Record which alternatives remain usable, were revised, combined,
    or rejected; record the reasons, protected losses, and smallest unresolved dependency. When an architecture
    decision is current, use this account as an input to the Work governed by `SYSE.6`. When no admitted bearer
    can satisfy a sound contribution, choose explicitly among another bearer, a changed functional organization,
    new realization or supporting-System capability, bounded exploratory Work, or stopping the current proposal. Pause
    only the commitment whose basis is missing.

This numbered list is a learning and presentation unfolding governed by `A.22.CGUS`, not a WorkPlan or a
temporal account of performed Work. It keeps the reasoning questions together without requiring Work to follow
the displayed order. Functional reasoning, construction search, specialist analysis, realization, integration,
trial, and concept revision can overlap and recur. The logical dependency of one claim on another does not imply
that all Work producing the first result finishes before Work on the second begins.

#### SYSE.5:4.2 — Record the Result

| Result position | Required content |
| --- | --- |
| bounded use | Project System or intended referent, decision question, outside effect or observed failure, use situations, configuration, operating envelope, horizon, and protected characteristics. |
| functional alternatives | Several candidate claims about functional organization, or a justified smaller set; each names the selected functional structure or possible-future structure content, its functional contribution claims, interactions, conditions, modes, and unresolved causal or functioning claims. |
| bearer-and-interface alternatives | Candidate actual Systems or intended referents, obtaining or proposed constructive and placement structures, interface specifications and physical realizations or gaps, separate existence, procurement, provider-Work, and realization claims, and materially distinguishing principles. |
| proposed allocations | Explicit many-to-many function-to-bearer associations qualified by use, conditions, configuration, place, mode, and effectivity; actual functioning is grounded separately. |
| feasibility and conflict | Capability needs, loads, margins, resources, placement, realization and integration dependencies, wrong-use cases, conflicting characteristics, supported and unsupported claims, and first unsupported dependency. |
| evidence boundary | Models and descriptions used, performed analysis or trial Work, the Agents that performed it, observations, source editions, uncertainty, and claims those observations do and do not support. |
| decision use and local stop | Alternatives retained, revised, combined, or rejected; reasons and protected losses; the decision question and architecture-decision Work that can use the account; and the smallest unsupported commitment to pause or proposal to stop. |

The account can use several linked representations. Each representation names the functional organization,
constructive organization, or engineered System it describes, and the account states the correspondence among
those subjects.

#### SYSE.5:4.3 — What Changes in Practice

Engineers stop asking which named component implements each box and start asking which materially
different arrangements can produce the required outside effect under the actual use conditions. They no longer
treat functional names as purchase items or procurement specifications. Interface standards become inspectable
specifications and evidence questions. Failed feasibility changes the smallest affected functional or bearer claim instead of
silently collapsing the candidate set or restarting the whole project.

### SYSE.5:5 — Worked Case: Heat-Pump Plant Control and Protection

An occupied building has a heat-pump plant whose controller must respond to electricity-price and grid-flexibility
signals while maintaining room comfort and protecting compressors. The engineering team must choose a control
architecture for plant configuration `HP-2` that remains useful for the next three heating seasons. Earlier
concept-development Work produced two viable use/System concepts and one unresolved mismatch: centralized
optimization improves plant coordination, but communication loss must not remove local protection.

During allocation Work, the engineers restore four contribution families as claims whose bearer arrangements
remain to be chosen:

- modulate heat production against building demand under temperature, occupancy, tariff, and plant conditions;
- keep compressor pressure, temperature, cycling, and flow within protected limits;
- accept, validate, and act on external price or flexibility signals within declared timing and authority;
- retain local safe operation and recover state after communication, sensor, or controller failure.

They develop three materially different proposals:

1. A central building controller carries demand estimation, optimization, dispatch, and most protection logic;
   unit controllers provide actuation and a small emergency stop.
2. Local unit controllers carry protection and normal regulation; a supervisor sends bounded set-points and
   coordinates units, while loss of the supervisor leaves a declared local operating envelope.
3. Thermal storage and a tariff scheduler carry most time-shifting; local controllers retain protection and
   regulation, so grid response is split across storage, scheduler, drives, sensors, and plant state estimation.

The functional contribution claims and candidate bearers are not one-to-one. Protection is distributed across
software, local electronics, sensors, drive limits, valves, and physical pressure relief. Grid response depends
on the supervisor or scheduler, communication bearer, storage state, unit capability, and operating permission.
Every bearer entry identifies an actual System or intended referent and its proposed allocation. A model-box
label such as *protection* or *optimization* is only a cue for recovering those claims.

The interface account separates signal semantics, units, timestamps, command validity, latency, state quality,
fallback behavior, configuration identity, and physical connections. The team separately tests rejection of stale
commands, agreement of sensor units, local fallback behavior, and the integrated plant contribution. Simulation
Work challenges thermal and tariff behavior; Hardware-in-the-Loop Work
challenges timing and fallback; a bounded plant trial challenges actual integration. Each produces observations
with different claim limits.

An AI coding Agent proposes a fourth function graph and controller split. That Agent and the engineers perform
candidate-generation and criticism Work; the generated graph is a description candidate. It enters the
account only after its functional claims, candidate bearers, interface assumptions, and unsupported physical
dependencies are recovered.

The account retains proposals 2 and 3 and rejects proposal 1 because its local protection split cannot satisfy
the declared communication-loss condition. It also records one unresolved storage-cycling evidence need. The
two alternatives, allocation conflicts, predicted losses, and conditions for revisiting the decision become
inputs to architecture-decision Work governed by `SYSE.6`; this account does not select the architecture.

#### SYSE.5:5.1 — Small Wrong-Use Check

A service machine uses one lubricant cartridge and one cleaning-solvent cartridge. Cross-connection damages
seals. The engineer states the two fluid-delivery contributions and service conditions, then compares candidate
cartridges, ports, seals, and connection arrangements. The retained proposal uses mechanically distinct keyed
couplings whose materials and geometry fit the relevant fluids, pressure, assembly, and service conditions.

The check attempts every intended connection and the consequential swapped connections under the declared
conditions. A colour label is a cue, not evidence that cross-connection is impossible. If an intended connection
fails or a damaging swap remains possible, the allocation and interface proposal reopens. The resulting observations can support claims only about the tested configurations and wrong-use
cases.

### SYSE.5:6 — Biases to Watch

Three recurring biases matter here. **Incumbent-form bias** lets a function tree, current parts, or a supplier
catalogue determine the candidate architecture; start from the required effect and compare materially different
arrangements. **Conformance-label bias** lets an interface name, standard, or certificate replace project evidence;
state the interface claim and test it under the relevant conditions. **Fluent-generator bias** lets a plausible
human- or AI-generated graph outrun bearer physics; recover the claims, Systems, and unsupported dependencies.

Agents—for example, a person, team, organization, robot, or sufficiently agentic AI System—may perform
candidate-generation, modeling, criticism, or trial Work when they have the needed capability and authority. For each performed Work, record the
Agent, assignment, Method, observations, and claim limits. Application DPFs supply subject-specific Methods—for
example, Methods for physics, software, safety, law, environment, economics, or assurance.

### SYSE.5:7 — Conformance Checklist

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE5-1` | names one actual System or intended-system designator selected as the project system-of-interest, decision question, use, configuration, operating envelope, horizon, and required outside effect or observed failure. |
| `CC-SYSE5-2` | restores function-like claims through their predicates, possible bearers, conditions, and receiving effects rather than relying on functional labels. |
| `CC-SYSE5-3` | develops materially different functional and bearer-and-interface alternatives or justifies why a smaller set is decision-sufficient. |
| `CC-SYSE5-4` | keeps functional organization, constructive organization, placement, Work, Method, descriptions, and evidence distinct. |
| `CC-SYSE5-5` | states many-to-many proposed allocations with use, mode, configuration, place, and effectivity where they change the decision. |
| `CC-SYSE5-6` | separates interface specifications, physical realizations, connections, interactions, and compatibility evidence. |
| `CC-SYSE5-7` | challenges consequential load, failure, integration, and wrong-use cases and states the tested boundary. |
| `CC-SYSE5-8` | states separately whether an actual System exists, whether it is procurable, what realization or provider Work is needed, and which candidate claim remains unsupported. |
| `CC-SYSE5-9` | names each decision-relevant dependency by its own kind and relation to the proposal. |
| `CC-SYSE5-10` | makes alternatives and explicit conflicts usable by named architecture-decision Work and records selection and realization as separate Work and claims. |

### SYSE.5:8 — Common Failures and Repairs

These documented recurring failures justify the local guards in this pattern:

| Failure | Symptom | Repair |
| --- | --- | --- |
| Incumbent-parts decomposition | The current bill of materials becomes the functional organization. | Restate the outside effect and develop rival functional organizations before preserving the incumbent allocation. |
| Functional element as purchase item | A box named *sensor*, *protection*, or *storage* is treated as a procurement specification or purchase item. | Recover the function-like claim, candidate actual or intended bearer, interfaces, placement, capability need, and assembly relation. |
| One-to-one allocation | Every contribution is forced into one component and every component into one contribution. | Permit many-to-many and mode-dependent proposals; inspect joint and shared functioning. |
| Diagram overlap as relation | Matching labels or co-located symbols establish identity, allocation, or functioning. | State the direct claim and supporting evidence; keep representation correspondence separate. |
| Interface label as proof | *Standard*, *open*, or a connector name establishes compatibility or substitution. | State interface conditions and test conformance, integration, intended interaction, and consequential wrong use separately. |
| Available product as only candidate | Catalogue availability is treated as the boundary of possible construction. | Keep physical candidate generation separate from the choice of obtaining arrangement; use `SYSE.24` when that obtaining choice becomes current. |
| Unavailable product as no construction | An unsuccessful search erases candidate bearer descriptions already examined. | Retain the candidates and failure reasons; distinguish market absence, physical infeasibility, and missing project capability. |
| Fewer bearers as automatic improvement | Consolidation or a universal platform is assumed superior. | State transferred contributions, affected characteristics, scale window, losses, and evidence burden; keep it as one candidate. |
| AI graph as design truth | A generated function graph is accepted because it is connected or plausible. | Recover claims and bearers, challenge physical and interface dependencies, and qualify the generator and evidence. |
| Trial as universal proof | One simulation or bench result establishes full functioning and architecture adequacy. | State the Agent, Method, conditions, configuration, observations, claim limits, and the later claim-assessment Work that can use them. |
| Architecture decision hidden in generation | The preferred candidate is silently selected during modeling. | Preserve the decision-usable candidate account, including explicit losses and unresolved claims, as an input to architecture-decision Work governed by `SYSE.6`. |
| Whole-project stop | One missing bearer blocks every Work stream. | Pause only the unsupported commitment; select another bearer, revise the function, change realization capability, explore, or stop the bounded proposal. |

### SYSE.5:9 — Consequences

Engineers gain alternatives that can survive contact with physical realization, integration, procurement, and
operation. Functional freedom remains tied to stated bearer claims and use conditions. Supplier
claims and AI-generated candidates become inspectable inputs. Wrong-use cases, interface gaps, unallocated
contributions, and unsupported realization dependencies appear early enough to change the architecture choice.

The cost is maintaining correspondence among several selected structures and qualifying claims by use,
configuration, and evidence. Candidate diversity also costs modeling and specialist Work. Those costs are bounded by the decision question and stop rule: stop with decision-sufficient alternatives and
the first unsupported feasibility dependency.

### SYSE.5:10 — Rationale

FPF already explains functions, structures, modules, interfaces, candidate synthesis, and architecture choices.
The Systems Engineering specialization changes the working move: it keeps the required outside effect and use
visible while engineers iteratively develop functional organizations, actual or intended bearer arrangements,
many-to-many allocations, physically meaningful interfaces, realization dependencies, wrong-use challenges,
and bounded evidence use for one engineered-System decision. Without this specialization, the general C.32 palette
can be formally correct yet omit the constructive and integration content needed by procurement, realization,
assurance, and continuing engineering Work.

### SYSE.5:11 — SoTA and Source Use

| Source line | Use here | Epistemic boundary |
| --- | --- | --- |
| R5.4:2; R5.6:28 and :31; R6.4:7; R6.5:1–3, :6, Mod1–2, :8, Quiz1–2; R6.6:7–8 and Quiz2; R8.4:6–7; R8.5; R8.7:4–6 | Used for the recurring functional/constructive mismatch, many-to-many allocation, interface, wrong-use, integration, and iterative-revision cases. | The guides are maintained conceptual syntheses and practitioner sources. Treat universal sequence, prevalence, and effectiveness as separate claims. Current FPF governs lifecycle, selected-view, role, and allocation relations where it supersedes source wording. |
| [Eisenbart, Gericke, and Blessing 2017](https://doi.org/10.1007/s00163-016-0242-3), [Yildirim and Campean 2020](https://doi.org/10.1007/s00163-020-00343-8), and [She, Belanger, and Bartels 2024](https://doi.org/10.1007/s00163-024-00434-w) | Supports heterogeneous function-model purposes and formalisms, iterative functional/structural reasoning, flow- and time-aware analysis, and functional decomposition as an exploratory move. | The reported ten-company exploration, mobility case, and preliminary metrics example support their bounded uses. Notation, sequence, broad effectiveness, and decomposition policy remain open questions. |
| [Monetti, Lundström, and Maffei 2025](https://doi.org/10.1080/21693277.2025.2566066) and [Grønvald et al. 2026](https://link.springer.com/article/10.1007/s11740-025-01412-4) | Brings assembly and modular-product consequences into early candidate development and requires explicit economic and data limits. | The sparse, bounded company evidence supports local assembly and modular-product consequences. Broader benefit, cost, substitutability, and Method-dominance claims remain open. |
| [Haddad and Seibel 2025](https://doi.org/10.1017/pds.2025.10205) | Supports AI-assisted generation and iterative refinement of candidate function structures. | The bounded course comparison reported 42% error-free and 72% fully connected outputs for its best configuration and left, for example, non-functional requirements, domain interdependencies, physical effects, and principal solutions outside. Use it as evidence for candidate generation under the reported conditions; project correctness, bearer feasibility, and architecture selection require project evidence. |
| Current FPF `A.6.F`, `A.6.M`, `A.22`, `C.30`–`C.32`, `C.31`, representation, comparison, evidence, and assurance patterns | Used for the normative ontology and transdisciplinary candidate-synthesis machinery. | This DPF uses those kinds and the general palette, then adds the applied Systems Engineering Method and result needed for engineered functional contribution, bearer allocation, physical interfaces, realization, integration, wrong-use challenge, and decision use. |

Official modular-open-system or model-based guidance may contain current interface fields or candidate prompts.
Treat enacted project prevalence, interoperability, effectiveness, and SoTA as separate claims grounded by direct
industrial observations or qualified expert estimates when stronger evidence is unavailable. State their
epistemic status.
Reopen only the claims affected by a newer source that changes the allocation Method, interface test, AI-use
boundary, modularity consequence, or application-profile restriction.

### SYSE.5:12 — Relations

- When compatible, practitioners can use linked use/System candidates and unresolved mismatches from a
  `SYSE.2` result as inputs. They must still check the subject, configuration, horizon, evidence, and compatibility
  before developing the alternatives in this account.
- Use `A.6.F` to restore each function-like claim and possible bearer. `A.6.M` governs module and interface
  claims; `A.22` and `C.30` govern selected structures and architecture relations. Applying those patterns alone
  does not produce the Systems Engineering allocation account defined here.
- Use `C.32` for general multi-structure architecture-candidate synthesis. `SYSE.5` specializes that Method with
  the required-effect, functional-organization, constructive-bearer, physical-interface, realization,
  integration, wrong-use, and decision-use questions. Use a C.32 candidate palette here only when its subject and
  fields fit the current decision question.
- The allocation-alternative account is an input to architecture-decision Work governed by `SYSE.6`. That Work
  may produce a chosen architecture and conditions for revisiting it. Candidate generation in `SYSE.5` does not
  select the architecture.
- When an unsupported realization or build-the-builder dependency, evidence claim, description-correspondence
  problem, or assurance question is current, apply `SYSE.3`, `SYSE.10`, `SYSE.7`, or `SYSE.4` respectively to
  its own subjects and sources. The realization dependency, evidence claim, description-correspondence problem, and assurance question concern different engineering subjects and require different Work results; Work performed for one does not supply the missing results for the others. A description ensemble remains distinct from candidate Systems, allocations,
  interfaces, and the selected architecture.
- Under `XRI-03`, practitioners can reuse a compatible `SYSE.5` result in `MDPE.3` when an engineered instrument,
  robot, hybrid body, venue, or software System is itself an architecture subject in the performing whole. Recheck
  the reused result against the MDPE subjects, authority, conditions, evidence, and current music-and-dance
  sources.
- Agents performing downstream application Work—for example procurement, manufacturing, configuration,
  maintenance, operations, software, electrical, mechanical, safety, or human-factors Work—use the result through
  their own Methods, authority, conditions, and evidence.

### SYSE.5:End

<a id="syse-6"></a>
## SYSE.6 — Decide and Reopen the Engineering Architecture

### SYSE.6:0 — Use This When

Use this pattern when an engineering project has several architecture candidates, yet local design choices are
accumulating without one recoverable decision about the project-shaping structures of the engineered System.
Use it also when an earlier architecture decision still appears in a record, but changed conditions—for
example, use, integration, configuration, evidence, or operation—may have made its accepted losses and open
refinements stale.

The intended result is an **engineering architecture decision that selects one option, fixes the
project-shaping constraints, and states when to reconsider it**. In FPF this is an
`ArchitectureDecisionRelation@Project` supplied by `C.32.PAD`, not a second decision kind. In this Systems
Engineering specialization, the decision uses the required engineering content recorded below: each
candidate's use, functional organization, bearers, interfaces, realization, integration, affected-System
consequences, and evidence. The decision names
the selected option, explicit constraints, and results needed by later engineering Work.

**First move.** Name the architecture question, the decision subject, and the smallest project-shaping
structure choice that two current candidates answer differently. When the choice requires authority, cite the
separate authority relation; an assignment or architecture record does not supply it.

This pattern begins after candidate development and ends with a decision plus conditions for reconsideration.
Use `C.32` and `SYSE.5` to develop the candidates, `SYSE.7` to maintain architecture descriptions, `C.32.PAD`
directly when no Systems Engineering specialization changes the choice, and `SYSE.4` to qualify the decision or
identify the basis it still lacks. Release approval and evidence that the intended architecture now obtains
remain separate decisions and claims.

### SYSE.6:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| engineering architecture | Plain domain wording for one or more `ArchitectureOf@Context` relations concerning an actual engineered System and selected `U.Structure` values, or for possible-future architecture claim content concerning an intended System referent. Identify the architecture relation, its descriptions and candidates, the decision, and the later actual structure separately. |
| architecture candidate | An episteme that proposes selected-structure content, consequences, and conditions for one architecture option. It does not make an architecture relation obtain. |
| engineering project architecture decision relation | The `ArchitectureDecisionRelation@Project` supplied by `C.32.PAD` for an actual engineered System or intended referent and a recoverable composite project `U.Work`. It links the decision subject, candidate basis, selected option, constraints, accepted losses, and reconsideration conditions. The relation does not create the intended System or perform implementation Work. |
| chosen architecture | Ordinary shorthand for the selected option and affected-structure content cited by that decision relation. Before the relevant structure obtains, the shorthand remains modal decision content. |
| architecture characteristic criterion | One decision-specific criterion row supplied by `C.32.ACS`, with the characteristic, bearer, scale or qualitative frame, use, conditions, protected loss, and guardrail or comparison use needed by the decision. A quality word or metric name is not a criterion row. |
| architecture evaluation result | The result of an eval program under `C.32.ACE`, with its subject, configuration, conditions, parity frame, observations, and limits. It informs a decision; it does not select an option. |
| engineering architecture residual | An unresolved mismatch, loss, unsupported dependency, or omitted consequence tied to selected-structure content, a bearer or affected System, use and operating conditions, and a receiving engineering decision. The tie to that decision distinguishes a residual from an unrelated open task. |
| accepted loss | A disadvantage or unresolved residual that the decision subject knowingly accepts for the declared option, scope, horizon, and protected characteristics. Acceptance does not erase the consequence or establish permission from another decision subject. |
| open refinement | Decision content that leaves named lower-scope or neighboring structure choices undecided while fixing the project-shaping constraints they must satisfy. Interface, evidence, and affected-System claims retain their own Methods and grounds. |
| reopen condition | A stated event or observation—for example, a source or configuration change, characteristic crossing, failed dependency, or changed use—that requires the named decision subject to reconsider the decision. The condition opens reconsideration; the later decision remains a separate occurrence. |

Words such as *architecture*, *style*, *pattern*, *platform*, *modular*, *open*, *integrated*, *distributed*,
*AI-native*, and *evolutionary* are recognition cues until the current claim identifies the selected structures,
criteria, Method, decision relation, or observed change meant.

### SYSE.6:1 — Problem Frame

Engineering architecture decisions coordinate many later choices without deciding every detail. They can fix a
functional allocation, module boundary, interface grammar, placement, control boundary, redundancy principle,
product-family variation policy, evidence boundary, or other selected structure that several realization and
specialist decisions must respect. The useful decision is therefore neither an early master diagram nor a list
of everything important.

The decision sits between possible futures and physical realization. Its grounds may include, for example,
current descriptions, comparisons, estimates, experiments, or specialist returns. Later Work may produce a different actual structure
or expose consequences that were not visible. The architecture decision must close enough choice for current
engineering Work while preserving alternatives and explicit conditions for revision.

### SYSE.6:2 — Problem

Without a bounded architecture decision, local choices become a de facto architecture. Contributors—for
example, component suppliers, software teams, construction specialists, operators, safety specialists, or
providers of supporting Systems—each optimize their own structure. Their decisions can be individually
reasonable and jointly incompatible. Burdens such as interface, placement, configuration, assurance, or
affected-System consequences appear only during integration or operation.

An oversized architecture decision causes the opposite failure. It fixes low-level details without the local
knowledge needed to choose them, substitutes centralized approval for specialist contribution, and makes every
revision look like a whole-project exception. A broad quality catalogue or one score does not solve the problem:
characteristics have different bearers, Scales, conditions, evidence, and protected losses.

A decision record can hide both failures. A file can be complete while the candidate basis is narrow, accepted
losses are absent, the selected structure is unclear, or no observation can reopen the decision. Engineers then
preserve documentation instead of maintaining a current engineering choice.

### SYSE.6:3 — Forces

The decision must manage these recurring tensions:

- Current engineering contributors need stable constraints, while architecture knowledge and operating
  conditions continue to change.
- Whole-System coherence requires cross-boundary constraints, while detailed choices need local specialist
  knowledge and room to vary.
- A small characteristic set makes trade-offs visible, while omitted affected Systems or scales can move the
  burden outside the chosen boundary.
- Early estimates are cheaper than realization, while integration and operating evidence are often more
  decision-relevant.
- Architecture moves such as modularity, reuse, distribution, or standardization can reduce one burden while
  increasing others—for example, coordination, evidence, latency, supply, cost, or failure-coupling burdens.
- Current contributors need one selected option as a common decision basis, while rejected or deferred
  alternatives can remain valuable when the environment, technology, or evidence changes.
- AI-assisted synthesis and analysis can widen and criticize alternatives, while authority, accepted loss, and
  the engineering decision still require an identified decision subject and adequate grounds.
- A decision that is easy to supersede supports continuing change, while a decision with no stable identity or
  effectivity cannot coordinate implementation and configuration.

### SYSE.6:4 — Solution

Apply `C.32.PAD` to the Systems Engineering decision. Compare candidates only when their engineering
consequences are visible enough for the current commitment. Select the smallest set of project-shaping
structures needed to coordinate later Work. State accepted losses and open refinements, then state which
later results—for example, from realization, integration, configuration, specialist, assurance, or operating
Work—can confirm or reopen the choice.

#### SYSE.6:4.1 — Perform the Move

1. **Bind the architecture question.** Name the actual engineered System or intended referent, composite
   project Work, decision subject, deciding Agent, use, configuration or variant, operating envelope, horizon,
   and the later decisions this architecture choice must coordinate. If the intended System does not yet exist,
   keep its referent in claim content as required by `C.32.PAD`. When the decision requires authority, cite the
   independently obtaining direct authority relation with its bearer, scope, basis, applicability, and interval.
   If that relation lacks a current governor or does not obtain, candidate analysis may continue, but return the
   missing governor instead of claiming that an assignment or record authorizes the decision.
2. **Select the project-shaping structures.** Identify the selected structures whose alternatives can change
   several downstream choices or a protected characteristic. Examples include functional, constructive,
   placement, control, transformation-flow, information, evidence, Method, Work, and organization structures.
   Name each structure and the relation under discussion; *important*, *cross-cutting*, and *hard to change* are
   prompts, not membership tests.
3. **Prepare candidates for the decision.** Start with a compatible `SYSE.5` account or a qualified direct
   source for functional organizations, candidate bearers, allocations, interfaces, and conflicts. Add
   provider-arrangement constraints from `SYSE.8`, description evidence from `SYSE.7`, specialist results from
   `SYSE.9`, and engineering claim assessments from `SYSE.10` only when they fit the same subject, configuration,
   use, horizon, decision, and evidence window. For each input, state what it describes and which claim it can
   support. Evidence informs the decision but neither authorizes nor entails it; a specialist result answers only
   its receiving question under its stated conditions. If an input is unavailable or incompatible, use a
   qualified direct source or record the missing result. Keep a candidate only when its unsupported
   dependencies—for example, bearer, interface, realization, integration, configuration, or evidence
   dependencies—are visible as bounded residuals that the decision subject can knowingly accept.
4. **Define the criteria before evaluating.** Select a small set of `C.32.ACS` rows tied to this use and decision.
   For every characteristic, name the bearer, scale or qualitative frame, operating conditions, protected loss,
   comparison use, and guardrail or reopen reading when one is justified. Keep non-equivalent characteristics—
   for example, safety, performance, cost, resilience, changeability, or evidence burden—in separate rows unless
   the decision supplies and justifies an aggregation Method that preserves the distinctions it uses.
5. **Compare coherent candidates.** Compare whole proposals rather than isolated module choices. Include
   decision-relevant consequences—for example, expected functioning, physical principle, interfaces, placement,
   failure containment, realization and integration dependencies, supply and provider conditions, configuration
   continuity, operating and maintenance effects, affected Systems, evidence burden, or change consequences. Use `A.19.CPM`, `C.11`, or another direct
   comparison or choice pattern for the claim actually being made.
6. **Challenge the preferred option.** Use challenge Work suited to the claim—for example, specialist criticism,
   computation or simulation Work, prototype and bench tests, integration trials, or operating observation. For
   each challenge, record the performed Work, the Agent that performed it, Method, configuration, conditions, and
   claim limits. Ask which omitted structure or
   affected System would reverse the preference. An AI-produced ranking or architecture description is one
   input, not a decision subject or evidence of physical adequacy.
7. **Make the decision relation explicit.** Fill the current `ArchitectureDecisionRelation@Project` with the
   candidate basis, selected option, affected structures, criteria and trade-offs, accepted losses, rationale,
   consequences, effectivity and currentness claims, horizon, and rejected or retained alternatives. A bounded exception is a decision only
   when its scope, cost, protected loss, and reopen condition are explicit.
8. **Fix constraints and preserve refinement freedom.** State the decision-relevant constraints—for example,
   structure relations, interfaces, allocations, variation policies, or characteristic guardrails—that later
   Work must preserve. Separately state
   which implementation details and lower-scope structures remain open. Establish Work assignments, authority,
   commitments, and permissions through their own relations rather than through the architecture decision.
9. **Name the engineering uses.** Identify the receiving Work and the constraint or question it needs. Supply
   compatible selected-structure constraints and reconsideration conditions to `SYSE.3`, `SYSE.13`, and
   `SYSE.18` only where they change the receiving design choice. During decision Work, use `SYSE.9` to request a
   specialist contribution when one is needed. Use `SYSE.7`, `SYSE.10`, or `SYSE.4` for a current description
   gap, evidence question, or assurance question. Each receiver rechecks subject, configuration, horizon,
   authority, and compatibility.
10. **Design the continuation.** For each material assumption or accepted loss, name the event or observation
    that calls for reconsideration—for example, a source change, actual-structure comparison, characteristic
    reading, failed interface, changed use, or affected-System consequence. Name the decision subject and the question to reconsider. A
    threshold crossing supplies an observation, not an automatic replacement decision.
11. **Check what actually obtains.** After realization or integration Work, compare the observed configuration
    and selected structures with the decision content. Record divergence and evidence separately from the
    decision and its description. Supersede the decision when the smallest material changed claim alters the
    selected option, accepted loss, fixed/open boundary, or receiving Work.
12. **Stop at coordination sufficiency.** Return when affected practitioners can tell what current structures
    and constraints guide their Work, what remains open, which losses are accepted, which result they must
    return, and what can reopen the choice. Do not wait for complete detailed design or universal certainty.

This list is a learning and reasoning aid, not a lifecycle or temporal order. Work such as candidate
development, specialist analysis, realization preparation, evaluation, configuration, or architecture revision
can overlap. A
result dependency states which earlier result the receiving decision Work needs; it does not prescribe when each
producing Work occurrence must finish.

#### SYSE.6:4.2 — Record the Result

Record the decision with `C.32.PAD`. For Systems Engineering use, include the following content in the
decision relation and its cited subjects:

| Result position | Required content |
| --- | --- |
| bounded decision | Composite project Work, actual engineered System or intended referent, decision subject, use, configuration, operating envelope, horizon, question, and intended receiving decisions. |
| candidate basis | Compatible `SYSE.5` alternatives or qualified direct sources; provider-arrangement, affected-System, specialist, realization, configuration, and evidence conditions material to the choice. |
| selected structures | Obtaining structures or possible-future claim content, affected relations, selected option, fixed project-shaping constraints, and open refinements. |
| criteria and evidence | Decision-specific `C.32.ACS` rows, any `C.32.ACE` results, comparison or choice result, sources, observations, uncertainty, and limits. |
| trade-offs | Expected gains, accepted losses, unresolved residuals, rejected or retained alternatives, protected characteristics, and affected-System consequences. |
| engineering returns | Named constraints, questions, and result conditions supplied to receiving decisions—for example, realization, integration, configuration, description, specialist, assurance, supporting-System, operation, or maintenance decisions. |
| continuation | Observations and source changes that call for reconsideration, the decision subject and authority for that reconsideration, the supersession condition, and comparison of later actual structures with decision content. |

An ADR-like file or architecture description can publish parts of this result through `C.32.ADR` and
`C.30.AD`. Identify its correspondence to the decision relation. Ground the actual architecture and later Work's
use of the decision independently.

#### SYSE.6:4.3 — What Changes in Practice

The engineering project stops collecting local choices and starts making a bounded, inspectable commitment
across the structures that constrain several contributors. Downstream teams receive constraints and questions
their Work must answer, rather than an authoritative diagram. Detailed design remains free where the decision
leaves it open, and later integration or operating evidence can supersede the smallest affected decision rather
than forcing either silent drift or a whole-project restart.

### SYSE.6:5 — Worked Case: Architecture Decision for the Heat-Pump Plant Controller

Engineers using `SYSE.5` have produced two viable alternatives for an occupied-building heat-pump plant. In
alternative A, local unit controllers carry protection and normal regulation while a supervisor sends bounded
set-points. In alternative B, thermal storage and a tariff scheduler carry most time-shifting while local
controllers retain protection and regulation. Both can satisfy the current use concept; their structures and unresolved evidence
differ.

The project must choose the controller architecture for plant configuration `HP-2` for the next three heating
seasons. Its architecture board is the decision subject; a separate project relation gives the board authority
to make this decision. The board's assignment and the decision record do not create that authority. The resulting
`ArchitectureDecisionRelation@Project` selects these project-shaping structures:

- local protection remains within each unit boundary and does not depend on supervisor or utility
  communication;
- the supervisor can coordinate set-points only inside declared unit operating envelopes;
- plant-state and command interfaces carry units, timestamps, quality, validity, fallback, configuration, and
  effectivity conditions;
- a later storage branch can enter only through the declared thermal, control, configuration, and assurance
  interfaces.

The architecture board compares protection independence, room-comfort response, grid-flexibility response,
integration burden, energy and cycling consequences, maintenance access, and continuing change. Each criterion
names its bearer and conditions. Current evidence supports alternative A. Alternative B remains a future option
because storage-cycling, plant-space, supply, and economic claims are not yet sufficient for the current
commitment.

The accepted loss is less global optimization than the most centralized candidate predicts. The decision does
not declare that loss harmless; it protects local fail-safe behavior and records the operating evidence that can
reopen the balance. Algorithm choice, hardware supplier, detailed state estimator, and user-interface design
remain open refinements provided they preserve the fixed structures and guardrails.

The controller and integration teams use the fixed structures while shaping controller, bench, installation,
and integration Work with `SYSE.3`. Configuration and interface-version Work uses `SYSE.13`; utility-signal
authority and service conditions are handled with `SYSE.18`. Model and trial results are assessed through
`SYSE.10`, and the assurance question is handled through `SYSE.4`. The Agents performing these neighboring
Work occurrences apply their respective Methods, and each Work occurrence produces its own result for its named
receiving use. The architecture decision only supplies relevant constraints and questions.
The architecture board reconsiders the decision if communication-loss trials violate local protection,
room-comfort or cycling observations cross their guardrails, the utility changes signal semantics, storage enters
current project scope, or the installed structure diverges materially from the selected option. A new decision
then names the changed configuration, remaining horizon, unresolved evidence gaps, and operating envelope. It may
supersede the earlier decision without turning this reconsideration into a lifecycle stage.

The architecture decision does not make the plant configuration obtain. After integration, observations of the
actual installed Systems and relations are compared with the decision content. A different wiring, fallback,
or control allocation is an implementation divergence even if the architecture record was left unchanged.

### SYSE.6:6 — Biases to Watch

Three recurring biases matter here. **Record-presence bias** treats a complete diagram or file as a current
decision; recover the selected option, constraints, accepted losses, effectivity, and reopen conditions.
**Single-score bias** lets a modularity measure, connection count, maturity level, or aggregate score hide different
bearers and losses; compare decision-specific criteria. **Software-transfer bias** imports a software architecture
example as a general engineering rule; recheck the physical realization, operating conditions, and evidence of
the engineered System.

Agents—for example, people, teams, organizations, robots, or sufficiently agentic AI Systems—may contribute to
synthesis, modeling, criticism, evaluation, or implementation when they have the needed capability and
assignment. The decision still names the decision subject, authority, accepted losses, evidence, and affected
Systems. Application DPFs supply subject-specific Methods—for example, Methods for physics, safety, software,
medicine, electrical or civil engineering, shipbuilding, manufacturing, law, environment, or economics.

### SYSE.6:7 — Conformance Checklist

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE6-1` | names the composite project Work, actual engineered System or intended referent, decision subject, use, configuration, horizon, and receiving decisions. |
| `CC-SYSE6-2` | identifies project-shaping selected structures and relation claims rather than using *important* or *hard to change* as an architecture definition. |
| `CC-SYSE6-3` | admits candidates only with explicit functional, bearer, interface, realization, integration, affected-System, and evidence consequences or bounded residuals. |
| `CC-SYSE6-4` | defines decision-specific architecture-characteristic criteria before relying on eval results or scores. |
| `CC-SYSE6-5` | compares coherent alternatives and exposes gains, accepted losses, unknowns, and burdens moved elsewhere. |
| `CC-SYSE6-6` | returns one `C.32.PAD` decision relation and grounds the architecture claim, description, actual architecture, Work, and evidence through their own kinds and relations. |
| `CC-SYSE6-7` | distinguishes fixed project-shaping constraints from open refinement and preserves specialist authority. |
| `CC-SYSE6-8` | names each result needed by receiving Work—for example, a realization, configuration, specialist, description, assurance, supporting-System, operating, or maintenance result. |
| `CC-SYSE6-9` | states observable reopen conditions, the decision subject for reconsideration, and the question reopened. |
| `CC-SYSE6-10` | later checks the actual configuration and structures separately from the decision content and its publication. |

### SYSE.6:8 — Common Failures and Repairs

These documented recurring failures justify the local guards in this pattern:

| Failure | Symptom | Repair |
| --- | --- | --- |
| Local choices as architecture | Interfaces, modules, suppliers, and software partitions accumulate without a joint decision. | Select the project-shaping structures and make one bounded `C.32.PAD` decision relation with explicit receiving Work. |
| Architecture as everything important | The decision includes every design detail and unresolved issue. | Keep only selected structures coordinating several choices or protected characteristics; leave named refinement open. |
| Hard-to-change definition | Costly change alone makes an item architectural. | Name the selected structure, current alternatives, consequences, and decision use; difficulty is one possible characteristic. |
| Quality catalogue | Generic qualities are scored without bearers, conditions, Scales, or protected losses. | Create a small `C.32.ACS` criteria set for the current decision and preserve non-equivalent readings. |
| Metric as selector | A dashboard or eval result chooses the architecture automatically. | Interpret the reading under its subject and parity frame, then use the direct comparison and decision patterns. |
| Modularity as universal good | More modules, fewer connections, an open standard, or one supporting System is assumed better. | Compare decision-relevant consequences—for example, function bearing, coupling, cohesion, substitution, integration, evidence, cost, supply, or change—under the stated use. |
| Candidate without realization | A plausible structure lacks a needed realization dependency—for example, a transformer System, capability, interface realization, integration relation, or evidence return. | Record a bounded residual or return the unsupported branch to `SYSE.3`; do not hide it in an architecture label. |
| Organization mirroring shortcut | Current teams or communication links are copied into technical architecture by analogy. | Use `C.32.CONWAY` only for a stated influence or correspondence question; keep organization and engineered-System structures distinct. |
| Record as decision | An ADR or diagram exists, but selected option, relation, losses, and effectivity are unclear. | Recover the decision relation first; publish it afterward through the description and publication patterns. |
| Decision as actual structure | Possible-future selected content is reported as installed architecture. | Inspect the actual Systems and obtaining relations after Work; keep divergence and evidence separate. |
| Frozen architecture | Later integration or operation contradicts the basis, but the old record remains authoritative. | Apply the named reopen condition and supersede the smallest affected decision. |
| Whole-project exception | Any local refinement or residual requires centralized architecture approval. | Preserve the fixed/open boundary and escalate only changes that cross a declared structure, guardrail, or affected decision. |

### SYSE.6:9 — Consequences

Engineering contributors gain a current structural commitment that is strong enough to coordinate their Work
and narrow enough to preserve local design knowledge. Accepted losses and unresolved residuals become visible.
Realization, configuration, assurance, operation, and maintenance receive explicit questions and return
conditions. The architecture can evolve through superseded decisions rather than through undocumented drift.

The cost is deliberate comparison and continuing maintenance of decision identity, descriptions, evidence, and
effectivity. Some candidates remain open longer, and a preferred local solution can be rejected because it
moves an unacceptable burden elsewhere. That cost is bounded by selecting only the project-shaping structures
and the smallest evidence capable of changing the decision.

### SYSE.6:10 — Rationale

`C.32.PAD` already supplies the transdisciplinary architecture decision relation. This specialization changes
the Systems Engineering move: candidates must expose use, functional organization, actual or intended bearers,
physical and informational interfaces, realization and integration feasibility, affected Systems, and
specialist evidence. The decision turns the selected option into constraints and result conditions for
realization, configuration, integration, assurance, operation, maintenance, and later checks of the actual
structure. Those engineering admission, commitment, result, and reconsideration conditions are the
subject-specific contribution.

### SYSE.6:11 — SoTA and Source Use

| Source line | Use here | Epistemic boundary |
| --- | --- | --- |
| R6.6:8, :10, and :16; R6.7:4; R8.6; R8.7:1 and :3–6 | Supplies applied module/interface trade-offs, architecture characteristics, accepted residuals, realization and integration returns, decision rationale, and continuing revision. | The guides are maintained practitioner syntheses. A modularity optimum, fixed process, interface standard, or universal architecture-characteristic set requires its own grounds. |
| [Ford, Parsons, Kua, and Sadalage, *Building Evolutionary Architectures*, 2nd ed.](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/) and [Richards and Ford, *Fundamentals of Software Architecture*, 2nd ed., 2025](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/) | Supplies the current practitioner line for guided incremental architecture change, contextual characteristics, trade-offs, objective evaluation, and reopening. | The examples are software-centred. Their general Method is already generalized by `C.30`–`C.32`; software mechanics, team topologies, pipelines, and metric sets are not transferred as universal Systems Engineering rules. |
| [Monetti, Lundström, and Maffei 2025](https://doi.org/10.1080/21693277.2025.2566066), [Grønvald et al. 2026](https://link.springer.com/article/10.1007/s11740-025-01412-4), [Eichenwald et al. 2024](https://doi.org/10.1016/j.procir.2024.03.018), [Ghanjaoui et al. 2024](https://doi.org/10.1007/s13272-024-00773-3), and [Meixner et al. 2024](https://arxiv.org/abs/2402.09882) | Supports early assembly and realization feedback, explicit positive and negative modularity consequences, sparse economic evidence, and return from production feasibility to architecture. | The studies are bounded manufacturing and company cases. They do not establish universal modularity savings, one product/process/resource ontology, or automatic architecture-to-Work derivation. |
| [Demir, Chouseinoglou, and Tarhan 2024](https://doi.org/10.1002/smr.2703) | Supports the recurrence of architecture-decision participation, information-sharing, tracking, and rationale problems. | The 101-practitioner self-report survey is software-specific and does not establish a cross-domain decision Method or causal superiority of one authority arrangement. |
| [Lynch et al. 2025](https://doi.org/10.1016/j.jenvman.2025.126419) | Supports the distinction among an authorized decision, later observation, a reopen condition, and later re-evaluation. | The three natural-resource cases do not supply universal triggers, decision rights, or responses. The receiving engineering use must establish its own observations, consequences, evidence, authority, and choice. |
| [Becker et al. 2025 with the 2026 METR update](https://metr.org/blog/2026-02-24-uplift-update/), [Agarwal, He, and Vasilescu 2026](https://arxiv.org/abs/2601.13597), and [Pradas Gomez et al. 2025](https://doi.org/10.1017/pds.2025.10045) | Supports AI participation in bounded software and engineering-design Work with task-dependent gains, review needs, and integration consequences. | Use the evidence for bounded, task-dependent AI contribution. Complete-process autonomy, productivity transfer, independent problem selection, authority or responsibility transfer, and architecture adequacy remain separate claims. |
| Current FPF `C.30`–`C.32`, especially `C.32.ACS`, `C.32.ACE`, `C.32.PAD`, `C.32.ADR`, `C.32.CONWAY`, `C.31`, and comparison, choice, evidence, Work, and architecture-description patterns | Supplies the normative ontology, general criteria/eval/candidate/decision machinery, and description boundary used directly. | This DPF uses the `C.32.PAD` schema and general evolutionary-architecture Method, then adds the engineered-System admission and result-return specialization stated in the Solution and Rationale. |

Recheck an affected AI allocation or evidence claim when the tool generation, task distribution, engineering
profile, or quality outcome changes.

### SYSE.6:12 — Relations

- `SYSE.5` describes how to produce explicit allocation choices and conflicts. Practitioners using `SYSE.6`
  recheck a compatible result's subject, configuration, horizon, evidence, and conditions before using it as a
  candidate-set input; generation does not select.
- A compatible `SYSE.8` account can supply provider-arrangement constraints that change this architecture
  decision. Recheck its subject, configuration, use, horizon, evidence window, and availability. If it does not
  fit, use a qualified direct source or record the missing result. Keep the described offering or arrangement,
  provider Systems, performed Work, consequences, responsibility, and authority as distinct objects.
- A compatible `SYSE.7` account or `SYSE.10` assessment supplies evidence only when it can change this decision
  at the same configuration and horizon. A compatible `SYSE.9` account supplies a specialist result for its
  receiving question and conditions. During decision Work, a conditional `SYSE.9` request names the question,
  subject, conditions, authority, and desired result. Evidence and specialist results inform the choice; the
  decision subject retains the authority to make it. If an input does not fit, use a qualified direct source or
  record the missing result.
- `C.32.PAD` supplies the decision relation and the distinction among selected option, affected structures,
  Method and Work consequences, publication projection, and reopen conditions. `C.32.ACS` defines criteria rows;
  `C.32.ACE` defines eval programs and results; direct comparison and choice patterns govern their own claims.
- `SYSE.6` can supply selected-structure constraints and reconsideration conditions to `SYSE.3`, `SYSE.13`,
  and `SYSE.18` when they constrain the receiving design choice. The Agent performing each receiving Work
  applies its Method to generate and compare that Work's own alternatives and checks subject, configuration,
  horizon, and compatibility. If the decision result does not fit, use a qualified direct source or record the
  missing result.
- Practitioners use `SYSE.4` in assurance Work to qualify the engineering decision or identify the basis it
  still lacks. That assurance result is separate from architecture selection and from later acceptance,
  permission, release, and observed use success.
- `C.32.ADR`, `C.30.AD`, `E.17`, and `E.24.PUB` govern decision projection, architecture description,
  source-backed publication, and audience availability. A current decision can exist without one particular
  file, and a file can persist after the decision is superseded.
- Application DPFs retain subject-specific architecture Methods and safeguards for engineered-System
  profiles—for example, software, electrical, mechanical, civil, ship, medical, manufacturing, or human–AI
  engineering.

### SYSE.6:End

<a id="syse-7"></a>
## SYSE.7 — Maintain a Decision-Usable Engineering Description Ensemble

### SYSE.7:0 — Use This When

Use this pattern when an engineering decision depends on several epistemes—for example, descriptions, models,
requirements, analyses, configuration records, test results, or operating observations—but the project cannot
yet tell whether they concern the same subject, compatible configurations and intervals, mutually interpretable
claims, or the evidence needed by that decision.

The first useful move is to name one receiving decision and the smallest set of claims that could change it.
For every description used by those claims, identify its subject, edition, reference scheme, intended use,
currentness, and the Work that relies on it. State a cross-description relation only when its participants and
meaning are recoverable.

The result is a **decision-bounded account of usable descriptions and their relations**: it names usable claims,
contradictions, unsupported correspondences, omitted claims, and refresh conditions. Its technical label is
`EngineeringDescriptionEnsembleAccount@Project`, a project-local `U.Episteme`. The account remains distinct
from the described engineered System, the descriptions it selects, their publication carriers, configuration
baselines, and evidence that their claims obtain.

Use a simpler description directly when one episteme already supports the decision and no material
cross-description claim is being made. Use `SYSE.10` when the problem is the credibility of an evidence source—for example, a model, experiment,
or trial—for a named engineering claim; use `SYSE.13`, `SYSE.14`, or `SYSE.19` when configuration identity,
change, release, or a changed source edition is the governing problem.

### SYSE.7:0.1 — Precision Restoration

Words such as *model*, *view*, *specification*, *requirement*, *data*, *digital thread*, *digital twin*,
*traceability*, and *single source of truth* are recognition cues. Before relying on them, restore the
objects and relations that matter to the decision.

| Cue | Decision-usable interpretation in this pattern |
| --- | --- |
| description | One claim-bearing `U.Episteme` with a recoverable `EntityOfConcern`, claim content, effective reference scheme, edition, and current use. An expression or carrier—for example, a file, diagram, database row, screen, or spoken utterance—may carry it or be used in a publication occurrence; identify the episteme and publication relation separately. |
| model | A description episteme used under a stated modeling purpose, assumptions, omissions, interpretation, and validity boundary. Record these conditions independently of its executable, mathematical, visual, or tool form. |
| view | The same episteme individual qualifies as `U.View` only when a `U.Viewpoint` episteme and obtaining `EpistemeViewpointConformanceRelation` are present under `E.17.0`. Establish that membership through the conformance relation; presentation labels—for example, a page title, diagram type, dashboard face, or `viewpointRef`—remain publication cues. |
| viewpoint | A claim-bearing episteme specifying concerns and conformance rules for a view. A cue such as a stakeholder name, discipline label, screen layout, or familiar view list qualifies only when it supplies that content. |
| representation | A visible or formal expression and, when current, its correspondence to an independently recovered object, relation, claim, or mathematical structure. Treat expressions—for example, diagrams, tables, queries, graphs, or executable files—as representations. Ground performed Work through Agent–Work attribution, authority through its own relation, and depicted claims through evidence. Use `C.29` for a declared mathematical-lens use and its preserved and lost structure. |
| publication | An `E.24.PUB` publication occurrence with its form, carrier, audience, bounded use, and selected source edition when those identities matter. Ground the described world-side relation independently and use `E.17.0` when `U.View` membership matters. |
| engineering data | Claim-bearing epistemes and values used in engineering Work, together with the identities, editions, reference schemes, provenance, applicability, and relations needed by that use. Ground their world-side subjects separately. |
| trace or link | A recoverable direct relation: for example, a claim depends on a source claim; a test result assesses a named claim; an interface description concerns a selected configuration; or a change affects a configuration item. A hyperlink or same-name token is only an index until the intended relation and participants are stated. |
| digital thread | A maintained arrangement of description, source, configuration, change, publication, and use relations across named engineering Work. State its bounded use, participating relations, Agents assigned to maintenance Work, and currentness conditions instead of inferring them from one chain or repository. |
| digital twin | A selected description, model, data, automation, observation, and use arrangement concerning a named subject. Support every additional claim—for example, about System kind, fidelity, synchronization, beneficial use, or completeness—on its own grounds. |
| ensemble | The selected description epistemes and relations needed by one bounded set of decisions. This is an ordinary collective word. Identify each carrier and governing reference scheme independently. |
| consistency | A named set of claims can be jointly used under stated schemes, configurations, intervals, and tolerances. Establish it from claim content under those conditions; syntactic agreement, shared identifiers, and storage co-location are only comparison cues. |
| coherence | The selected claims and their correspondences support the receiving decision without an unresolved contradiction or missing distinction material to that use. Its scope is the named decision and material claims. |

The described subject, description episteme, model use, representation, mathematical lens, view, viewpoint,
publication occurrence, carrier, source, evidence relation, configuration, and performed Work remain different
objects. Restore only the distinctions that can change the receiving decision, but do not merge them merely to
obtain a shorter inventory.

### SYSE.7:1 — Problem Frame

Engineering decisions rarely depend on one self-sufficient description. A controller architecture can involve,
for example, an outside-use account, a functional organization, a bearer and interface arrangement, an equation-
based plant model, a control-state description, a wiring schedule, a component catalogue claim, a configuration
record, a test procedure, test observations, or an assurance argument. These epistemes may concern different subjects,
scales, configurations, and intervals. They may use different reference schemes and intentionally omit
different characteristics.

The difficulty is not solved by putting every expression into one repository or by declaring one model
authoritative. Engineers need to know which claims support which decision, what each claim concerns, how a
cross-description comparison is warranted, and what world-side or evidence result would expose a mistake.
Otherwise a coordination cue—for example, a model identifier, diagram label, common part number, generated
link, or synchronized timestamp—is silently treated as identity and agreement.

Two symmetric failures recur.

1. **One-model overreach.** A familiar product—for example, an architecture model, CAD assembly, requirements
   database, ontology, simulation, or digital-twin product—is expected to contain every useful engineering
   distinction. Its local
   ontology and omissions then become hidden project law.
2. **Unrelated-description accumulation.** Specialists maintain useful local epistemes but no one states their
   shared subjects, configuration applicability, interpretation, evidence, contradictions, or receiving
   decisions. The project has many artifacts and little joint decision support.

`SYSE.7` describes the applied engineering move between these failures. FPF supplies the transdisciplinary
distinctions for representations, epistemes, publications, views, evidence, configurations, and source
currentness. This pattern specializes their joint use for engineering descriptions supporting decisions—for
example, concept, architecture, realization, integration, operation, assurance, or modernization decisions—
about an engineered System and its affected Systems.

### SYSE.7:2 — Problem

An engineering description collection becomes unsafe when a decision-critical description gap remains hidden.
These documented recurring gaps include:


- the receiving decision and the claim that a description is expected to change;
- the actual System, intended referent, configuration, part, environment, Work occurrence, or other holon
  that a claim concerns;
- whether two descriptions concern the same individual, the same kind, related parts, successive
  configurations, or merely similarly named subjects;
- the reference scheme, scale, coordinate frame, units, tolerance, assumptions, omissions, and modeled interval;
- whether an alleged cross-description link is a representation correspondence, source dependency,
  configuration relation, transformation relation, evidence relation, or only a navigation aid;
- the edition and currentness of each source episteme and the Work that still relies on it;
- whether a diagram or simulation output describes a candidate, an intended configuration, an actual
  configuration, an observed occurrence, or a possible-future structure;
- which Agents produced, checked, changed, published, or use each result, through which Work and with what
  capability and authority;
- which contradiction, unsupported relation, or omitted characteristic blocks the next decision;
- what observation, configuration change, source change, or decision change requires refresh.

The result is often a false impression of precision. Every artifact may have an identifier and version while
the central engineering claim remains ambiguous. Automated trace generation can multiply this impression:
thousands of links exist, yet the project cannot say which direct relation each link records or which decision
would change if the linked claim failed.

### SYSE.7:3 — Forces

| Force | Tension to manage |
| --- | --- |
| Local specialist fitness and cross-specialist use | A local model should use the distinctions needed by its specialist Work; a receiving engineering decision still needs explicit correspondences and limits. |
| Minimum useful set and missing perspectives | Every additional description costs maintenance and collision checking; an omitted claim—for example, a functional, physical, temporal, affected-System, realization, or evidence claim—can make the decision unsound. |
| Stable subject identity and changing configurations | Several epistemes may concern one enduring System while referring to different particulars—for example, parts, variants, versions, effectivities, or intervals. Recover the identity relation instead of relying on a shared name. |
| Human readability and machine-supported checking | Text and diagrams can reveal meaning to people; formal expressions and automation can expose selected contradictions. Warranted reliance still requires an explicit interpretation, completeness boundary, and world-side correspondence. |
| Executable model and physical result | Simulation and generated code can shorten feedback; they can also reproduce shared assumptions and omit physical effects—for example, manufacturing, installation, environmental, or operating effects. |
| Shared model and federated descriptions | One common model can reduce translation for a bounded use; independently maintained descriptions can preserve needed expertise and authority. Choose from the receiving decision and the losses of each arrangement. |
| Current decision and future reuse | General data structures can enable later use; speculative completeness can delay the present decision and preserve obsolete distinctions. |
| Publication convenience and epistemic identity | One publication occurrence can make several epistemes available, and one episteme can appear through several publication forms. Carrier consolidation leaves claim content and editions distinct. |
| AI-assisted production and warranted reliance | AI Systems can produce candidate outputs—for example, text, code, diagrams, mappings, checks, or summaries—quickly. The outputs still need recoverable sources, subjects, error checks, and decision-specific acceptance. |
| Standards compatibility and present practice | Standards supply useful distinctions and exchange constraints. Treat conformance, official publication, and academic visibility as evidence of declared content; assess practical adoption, effectiveness, and current engineering Methods separately. |

### SYSE.7:4 — Solution

Maintain the smallest current set of engineering description epistemes that can change the receiving decisions,
and make every material cross-description use explicit. Select descriptions from decisions and Work. Existing
document inventories, notations, process presentations, and tool repositories are candidate sources rather than
the selection rule.

#### SYSE.7:4.1 — Perform the Move

1. **Name the receiving decision and its decision-changing claims.** State the decision, decision subject,
   intended use, project focus, current option set, and the claims for which a changed value, contradiction, or
   evidence result could change the choice. Start from this decision rather than from a generic instruction to
   “document the system.”
2. **Recover each described subject.** For every needed claim, identify the actual System, intended referent,
   selected structure, configuration, part, environment, Work occurrence, Method, or other holon concerned.
   Distinguish an individual from its kind, one part structure from another selected structure, and a current
   configuration from a possible-future candidate.
3. **Select the description uses.** Choose the smallest set of epistemes needed, for example, to express,
   calculate, compare, communicate, realize, observe, or assure those claims. Examples include a use account,
   functional description, physical-structure description, equation model, state model, interface account,
   configuration record, trial
   result, or operating observation. Include each one only for a stated use.
4. **Identify each episteme and expression.** Record claim content, `EntityOfConcern`, effective reference
   scheme, edition, source, provenance, modeled interval or effectivity, assumptions, omissions, and relying
   Work. Separately identify any material expression or publication object—for example, a carrier, publication
   form, rendering, executable expression, database object, or generated summary—when its identity changes use.
5. **State interpretation and model-use conditions.** As needed by the decision, name conditions such as units,
   coordinate frames, scales, tolerances, abstractions, parameter sources, boundary conditions, solvers or
   inference procedures, and validation limits. A language specification or tool capability is not the project interpretation.
6. **Recover cross-description relations.** For every material link, state its participants and relation:
   same subject under different schemes; part or interface correspondence; claim dependency; source derivation;
   configuration applicability; transformation from one expression to another; test-to-claim assessment; or
   another direct relation. If the project lacks a governed relation kind or evidence for that claim, record an unsupported
   correspondence rather than inventing a generic trace edge.
7. **Check collisions at the claim level.** Compare claims only after subject, configuration, interval, scheme,
   scale, and tolerance are aligned or their differences are explicit. Classify the result as agreement for the
   bounded use, an explainable difference, an unresolved contradiction, a missing interpretation, or a missing
   world-side check.
8. **Check correspondence to realization and observation.** Identify which claims describe candidates or
   intentions and which concern actual configurations or occurrences. Connect design claims to relevant
   observations—for example, from realization, integration, trials, commissioning, operation, or affected
   Systems—through their evidence
   and configuration relations. Do not let description-to-description consistency substitute for physical
   adequacy.
9. **Choose publication forms for actual users.** Publish only the forms needed by the receiving Work and its
   users. Reuse or author a viewpoint only when `U.View` membership and conformance matter. Keep the source
   episteme, view, publication occurrence, form, carrier, and audience use separate.
10. **Assign maintenance Work.** For each material entry, identify the Agent assigned to change its description,
    decide a contested interpretation, accept a cross-description relation, or stop reliance, together with the
    needed capability and authority. Specify the observations that call for refresh and the Work that will update
    the affected account.
11. **Return the bounded result.** Make the usable claims, contradictions, unsupported correspondences, gaps,
    reliance limits, and refresh conditions available to the named engineering decisions and dependent Work.

This numbered list is a learning unfolding governed by `A.22.CGUS`, not a claim that description Work occurs
in one serial lifecycle. Description production, realization, checking, operation, and decision Work can overlap.
The displayed order expresses a logical dependency: claims cannot be compared until their content and subjects
are recoverable. It does not prescribe the order of performed Work.

#### SYSE.7:4.2 — Record the Result

Use a compact `EngineeringDescriptionEnsembleAccount@Project` when several descriptions materially support one
decision. It is a project-local episteme; the FPF kinds of its participants remain unchanged.

| Field | Required content |
| --- | --- |
| receiving decision | Decision, decision subject, intended use, interval, and downstream Work that will use the result. |
| decision-changing claims | The smallest claim set whose value, contradiction, evidence, or absence can change the decision. |
| description entries | For each episteme: source and edition, claim content, `EntityOfConcern`, reference scheme, configuration/effectivity, modeled interval, assumptions, omissions, and relying Work. |
| expression and publication entries | Material carriers, publication occurrences and forms, renderings, executable expressions, database objects, or generated summaries, each kept separate from the source episteme. |
| model-use conditions | Purpose, scale, units, coordinates, tolerances, boundary conditions, parameter sources, interpretation, calculation or inference Method, and validity limits needed by this use. |
| relations | Direct same-subject, part, interface, configuration, source, transformation, evidence, or other governed relations; unsupported correspondence hypotheses are marked as such. |
| collision results | Claim-level agreements, explainable differences, unresolved contradictions, missing interpretations, and missing world-side checks. |
| realization correspondence | Actual configuration or occurrence, observation/evidence basis, and the decision claim it can confirm, weaken, or reopen. |
| maintenance assignments | Assigned Agents, their system-role assignments, authority, capability, Work, and acceptance conditions for producing, checking, changing, or retiring description uses. |
| return and refresh | Receiving Work and the Agents assigned to it, accepted reliance limits, current gaps, triggering observations, and the smallest affected account or decision to reopen. |

The account can be published through, for example, linked text, tables, model queries, a repository view, or
generated reports. Its identity and sufficiency do not depend on one storage technology.

#### SYSE.7:4.3 — What Changes in Practice

Engineers stop asking whether documentation or “the model” is complete. They ask whether the current
description ensemble can support a named decision without hiding a subject mismatch, configuration mismatch,
interpretation gap, contradiction, or unsupported world-side claim.

The Agent performing modeling Work enacts the Method; modeling tools are resources. Ground decision authority
and warranted reliance on modeling results through their own relations. Traceability becomes a collection of
testable relations rather than a link count.
A digital thread becomes a maintained arrangement for named engineering uses rather than a product slogan. Use
the local label *digital twin* only when its selected subject, descriptions, automation, observations, and use
are stated.

The account includes conditions for reconsideration. A change to, for example, a configuration, source edition,
environment, model assumption, trial result, or receiving decision can call for refresh. The assigned Agent then
refreshes the affected claims and relations. Unaffected descriptions remain usable under their stated conditions.

### SYSE.7:5 — Worked Case: Controller Architecture Description Ensemble

The project is preparing evidence for a controller-architecture decision: whether plant configuration `HP-2`
should use direct compressor modulation alone or modulation coordinated with thermal storage over the next three
heating seasons. The plant, use, configuration, and decision focus are the same across the selected inputs.
Outside-use, functional, and bearer descriptions already exist, but the decision-changing claims remain
distributed across several descriptions. The engineering team constructs this bounded account:

| Entry | Subject and use | Material interpretation or relation |
| --- | --- | --- |
| use and operating-scenario episteme | The intended heat-pump plant in occupied-building use; supplies temperature, noise, maintenance, power-price, and grid-response situations. | Scenarios are possible use descriptions, not performed operation or test evidence. |
| functional-organization episteme | Candidate control organization: demand estimation, compressor modulation, storage dispatch, limit protection, and fault handling. | Treat the listed elements as functions until separate bearer and realization relations assign them to controller modules or software processes. |
| bearer-and-interface account | Candidate controller hardware, plant sensors, actuator connections, storage valve, communication interfaces, and allocations. | Names candidate Systems, physical interface specifications, and many-to-many function allocations for the decision. |
| equation-based plant model | Thermal plant and storage behavior under selected boundary conditions. | Modelica equations describe one selected physical abstraction; solver output is not observed plant behavior. |
| controller state and timing description | Control states, transitions, sampling assumptions, fallback conditions, and actuator commands. | The description concerns intended controller behavior and must correspond to the hardware timing and sensor claims. |
| component and wiring records | Sensor variants, controller I/O, update rates, error bounds, cable and connector configurations. | Catalogue claims apply only to component variants and conditions. |
| bench and commissioning results | Observations from controller-in-the-loop Work and later installed-plant trials. | Engineers use `SYSE.10` to qualify which engineering claims those results support and `SYSE.13` to keep tested configurations explicit. |

A collision check finds that the plant simulation and controller description assume a two-hertz supply-water
temperature update with an error bound of plus or minus 0.1 kelvin. The currently selected procurement variant
is specified only for a half-hertz update and plus or minus 0.3 kelvin under the installed cable length and
filtering arrangement. Matching the token `SupplyTemperatureSensor` across three tools had hidden the
difference.

The engineers recover the sensor variant and interface configuration instead of merely synchronizing names.
They update the model-use assumptions, evaluate another component and estimator option, and perform a
controller-in-the-loop trial. The resulting evidence revises the architecture comparison: direct modulation
remains acceptable for one building profile, while the storage branch remains unselected until it has either the
faster sensing configuration or a different estimator and the corresponding assurance result. This evidence
informs the current decision; it does not approve a later storage increment.

The account records the usable description editions, the unresolved estimator claim, the tested
configuration, and a reconsideration condition tied to component substitution or a changed grid-response
requirement. Controller, procurement, integration, configuration, and assurance Work use different publication
forms over recoverable source epistemes while the decision-changing relations remain explicit. The result stays
bounded to this decision rather than becoming a master model.

An AI System also produces a proposed cross-description summary and candidate correspondence list. Those
outputs are new epistemes produced by performed Work. They are checked against source editions and
accepted only where the relation and participants are recoverable. The generated confidence score supplies
neither an evidence relation nor authority to alter the architecture decision.

### SYSE.7:6 — Bias Annotation

This pattern resists four recurrent source and practice biases.

- **Artifact bias.** Sources such as standards, university curricula, tool vendors, and process descriptions
  often organize engineering around named documents or model kinds. The pattern preserves useful distinctions but begins from
  current decisions and Work.
- **Official-model bias.** A heavily published source—for example, a normative language, standard, ontology,
  or repository—may have limited or ceremonial use in projects. Official publication establishes scope and declared
  capability; assess practical adoption, beneficial use, shared interpretation, and current SoTA separately.
- **Software-transfer bias.** Software practices such as executable models, generated links, continuous
  integration, and automated checks can be valuable. Physical concerns—for example, realization, supply, installation, calibration, environmental
  exposure, or operating evidence—remain distinct and may require slower or destructive checks.
- **Academic-evidence bias.** A bounded study—for example, a prototype consistency checker, digital-twin
  mapping study, or one case—can sharpen a Method without establishing broad industrial effectiveness. Use the
  best available expert judgment with a stated epistemic status when comparative field evidence is unavailable;
  do not demand an unaffordable prevalence study or upgrade publicity to use evidence.

### SYSE.7:7 — Conformance Checklist

- [ ] One receiving engineering decision, its decision subject, and the decision Work are named.
- [ ] Every selected description has a source episteme and edition, claim content, `EntityOfConcern`,
      effective reference scheme, configuration or effectivity where material, modeled interval, and use.
- [ ] Actual Systems, intended referents, kinds, parts, configurations, and occurrences are not merged by name.
- [ ] Model purpose, assumptions, omissions, scale, units, tolerances, and interpretation are sufficient for the
      receiving decision.
- [ ] A `U.View` claim cites a viewpoint episteme and obtaining E.17.0 conformance; otherwise *view* stays
      ordinary source wording.
- [ ] Publication occurrence, form, carrier, rendering, and source episteme remain separate where their
      identities change reliance.
- [ ] Every material “trace” is resolved to a relation or marked as an unsupported correspondence.
- [ ] Cross-description comparison aligns or explicitly distinguishes subject, configuration, interval,
      reference scheme, scale, and tolerance.
- [ ] Claims about physical realization, benefit, safety, compliance, and acceptance use their own evidence;
      description consistency supplies only its stated comparison result.
- [ ] AI-generated, transformed, or summarized descriptions retain source provenance, subjects, check
      results, and reliance limits.
- [ ] The maintenance Agent, assignment, capability, authority, triggering observations, and refresh Work are
      stated for material entries.

- [ ] The returned account names contradictions, gaps, unsupported relations, accepted reliance limits, and the
      smallest decision or account to reopen.

### SYSE.7:8 — Common Failures and Repairs

These documented recurring failures justify the local guards in this pattern:

| Failure | Repair |
| --- | --- |
| Start from a compulsory document or view list | Start from the receiving decisions and decision-changing claims; add a description only when its use changes Work or reliance. |
| Treat one repository as one model | Recover each claim-bearing episteme, source edition, subject, scheme, and use independently of storage co-location. |
| Treat same names as same subjects | Resolve actual identity, kind, part, configuration, interval, and designation separately. |
| Count links as traceability | For each material link, name its participants, relation, relying decision, and failure consequence. |
| Call every publication face a view | Apply `E.17.0` only when `U.View` membership matters; otherwise name the publication form and bounded use plainly. |
| Let a simulation stand for the plant | State the modeled subject, assumptions, validity boundary, and evidence needed for the physical claim under `SYSE.10`. |
| Freeze one baseline as lifecycle truth | Keep configuration and effectivity under `SYSE.13`; refresh affected claims and relations when the world or source changes. |
| Demand one shared ontology | Use a shared scheme only where its benefits exceed lost specialist distinctions; otherwise maintain explicit correspondences and unresolved differences. |
| Create a digital twin by label | Name the selected subject, description/model set, automation, observations, current use, evidence, and maintenance Work; drop the label if it changes nothing. |
| Accept generated correspondence by confidence score | Treat it as a candidate episteme; inspect sources, subjects, relation, exceptions, and decision consequence. |
| Let specialists exchange files without a receiving use | Use `SYSE.9` to state the requested professional contribution, receiving decision, acceptance condition, and result to return. |
| Make the pattern or account act | Name the Agent, Method, and performed Work; epistemes describe, support, or constrain through use relations. |

### SYSE.7:9 — Consequences

**Benefits.** Decisions can use several specialist descriptions without pretending they form one total model.
Contradictions become claim-sized and actionable. Model, configuration, and evidence changes reopen bounded uses
rather than the whole project. Publication can be tailored to actual readers without changing source claims.
Automation can check more relations because the relation kinds and subjects are explicit.

**Costs.** Engineers must maintain subject identity, editions, interpretation, configuration applicability,
and selected correspondences. Some attractive links will remain unsupported. Specialists must expose enough of
their assumptions for the receiving decision, and the integration team must understand where formal checks stop.

**Risks.** The account can itself grow into a master-model bureaucracy. Prevent this by requiring a receiving
decision for every maintained entry and by retiring a relation when no current Work relies on it. Conversely,
aggressive minimization can omit a slow feedback channel—for example, a physical, affected-System, or
specialist channel; the result
check therefore asks what decision would become unsound if the omitted claim failed.

### SYSE.7:10 — Rationale

FPF already gives general precision for the needed transdisciplinary objects and relations, including epistemes,
descriptions, publications, views, reference schemes, representations, mathematical lenses, evidence,
currentness, configurations, and Work. Repeating those definitions with engineering nouns would add no
subject-specific Method.

The engineering specialization lies in the working combination. A project selects a heterogeneous set of
descriptions from engineered-System decisions; preserves subjects and configurations across several uses,
including functional, physical, behavioral, analytical, realization, and assurance uses; exposes collisions; and
connects candidate and
intended descriptions to actual realization and operating evidence; and turns gaps into questions for the
engineering Work that can change the System or revise the decision. This changes what engineers do beyond the
general statement that every episteme has a subject and reference scheme.

The ensemble is decision-bounded because no description is complete for every use. The same plant can require
different selected structures and representations for different uses—for example, control design, installation,
maintenance, economic choice, safety assurance, or operator training. The pattern does not rank those
descriptions by visual position or force them into one adjacent hierarchy. Users ask which claims must be jointly usable now.

### SYSE.7:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R6.2:9, R6.5, R6.6 and `R6-GC-07` | Decision-specific description selection; separation of subject, description, scheme and carrier; several simultaneous descriptions; explicit correspondences, collisions, gaps, and refresh. | Use the guide material to select descriptions for the current decision. Establish aspect inventories, level relations, creator relations, model federation, and refresh timing from that decision rather than treating the guide examples as universal requirements. |
| R8.4–R8.7 and `R8-GC-04`–`05` | Descriptions support professional contributions, research returns, realization, integration, and decisions; actual Work and authority retain their own relations. | Use role titles and automation forecasts only as cues; ground performed Work, authority, and independent criticism for the current project. |
| [ISO/IEC/IEEE 42010:2022 and ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/74393.html) | Current standard vocabulary separates entity, architecture description, viewpoint, view, model kind, correspondence, and iterative or concurrent process application. | Use the standards for their declared vocabulary and constraints. Ground the project architecture, modeling Method, practical adoption, shared interpretation, and current practice separately; organize the DPF by recurring engineering problems rather than a lifecycle. |
| [Lehner et al. 2025](https://doi.org/10.1007/s10270-025-01264-7) | A systematic mapping study shows heterogeneous model automation and uses in digital-twin engineering, with domain and subject dependence. | Treat the manufacturing- and transport-heavy literature as evidence of heterogeneous arrangements. Select ontology, Method, and subject kind for the current engineering use. |
| [ISO/IEC 30173:2023, ISO 23247-5:2026, and ISO 23247-6:2026](https://www.iso.org/standard/81442.html) | Current institutional work makes maintenance, continuity, connectivity, and integrated, unified, or federated composition visible as engineering-data arrangement choices. | Use these manufacturing standards to expose arrangement choices. Assess completeness, effectiveness, adoption, and the need for a digital-twin or digital-thread arrangement in the current engineering Work. |
| [Wu et al. 2025](https://doi.org/10.1016/j.aei.2025.103490) | One landing-gear case connects heterogeneous model semantics, conflict handling, traceability, and versioning. | Use it as a worked case for those relations. Physical configuration selection, release, supply, and broader use require their own evidence and Methods. |
| [SysML 2.0](https://www.omg.org/spec/SysML/2.0), [Modelica 3.7](https://modelica.org/language/), [ModelingToolkit 11](https://docs.sciml.ai/ModelingToolkit/stable/), and [Dyad 3.3.0](https://help.juliahub.com/dyad/stable/manual/changelog.html) | Rechecked 2026-08-25: the maintained families serve different uses—for example, architecture, requirements, acausal physical, symbolic-numeric, simulation, calibration, control, or integration uses—and a project may need several. Dyad 3.3 adds compiler-resolved editing and 3D multibody capabilities; each use still needs decision-led selection and explicit cross-description correspondence. | Specifications, changelogs, and provider documentation establish declared capabilities and maintenance. Assess comparative adoption and effectiveness separately; choose the model boundary, evidence, and correspondence from the engineering decision. |
| [Riedmaier et al. 2021](https://doi.org/10.1007/s11831-020-09473-7) and [Schwarzburg et al. 2024](https://doi.org/10.1017/dsj.2024.14) | Model use requires decision-specific verification, validation, uncertainty and extrapolation attention; warranted reliance can depend on model history, competence, access, and decision risk. | Treat confidence as one evidence result under stated conditions. Establish physical adequacy, decision correctness, and reliability separately; interpret the small non-probability practitioner sample accordingly. |
| [Becker et al. 2025 with the 2026 METR update, Agarwal et al. 2026, and Pradas Gomez et al. 2025](https://metr.org/blog/2026-02-24-uplift-update/) | AI Systems already participate in bounded software and engineering-design Work; task-specific allocation, provenance, review, integration, and observation remain necessary. | Use the sources for bounded contribution claims. Ground further claims—for example, productivity transfer, autonomous performance of larger Work, decision authority, or generated-description correctness—separately. |

Refresh a source-dependent claim when a new edition changes a relied-on language capability, composition option,
model-use boundary, automation result, or engineering-data relation. Treat publicity, standards announcements,
university curricula, and vendor demonstrations as evidence of what is declared or taught. Change DPF guidance
when evidence with a stated epistemic status changes a bounded engineering use.

### SYSE.7:12 — Relations

- `C.2.1` supplies episteme identity, `EntityOfConcern`, effective reference scheme, and edition discipline.
- `C.2.P.DR` repairs declarative-representation overread; `C.29` applies only when a mathematical-lens use and
  its explicit correspondence, preserved structure, loss, and stop condition are current.
- `E.17.0` supplies the dependent `U.View` membership and viewpoint-conformance relation; `E.17` and
  `E.24.PUB` keep selected episteme, publication occurrence, form, carrier, reader, and use distinct.
- `A.6.3.RT` governs a representation-scheme transition when the same `EntityOfConcern` is deliberately
  redescribed; it does not establish world-side identity or the correctness of the receiving claims.
- `A.10`, `B.3`, and `G.11` govern evidence reliance, assurance, and source-edition currentness. `SYSE.10`
  specializes the return from research, models, and trials to engineering decisions.
- `E.15`, `C.27`, `SYSE.13`, `SYSE.14`, and `SYSE.19` govern configuration continuity, temporal claims, change,
  release, and revalidation when those are the current problems.
- A compatible `SYSE.1` result can supply the scope and intended-result frame for the same subject and decision.
  It does not prescribe Work order. If it does not fit, use a qualified direct source or record the missing
  result. Descriptions such as concept, candidate, provider, affected-System, or specialist descriptions remain
  governed by their own subject patterns.
- `SYSE.7` supplies evidence to `SYSE.6` only when the account can change the same architecture decision at the
  same configuration and horizon. The account neither authorizes nor entails that decision. If the account
  cannot serve the use—for example, because it is unavailable, stale, outside scope, or incompatible—`SYSE.6`
  uses a qualified direct source or records that missing result.
- `SYSE.7` supplies a MethodDescription or representation input to `SYSE.19` only for the named receiving use.
  Description order or conformance does not establish Method order or effectiveness. If the account
  cannot serve the use—for example, because it is unavailable, stale, outside scope, or incompatible—`SYSE.19`
  uses a qualified direct source or records that missing result.
- When the current problem is requesting and accepting a professional contribution, apply `SYSE.9` to that
  result and receiving decision. When neighboring Work—for example, realization, integration, supporting-System engineering, description
  federation, or assurance Work—needs a description, its governing pattern uses the source episteme through its
  own subject, configuration, evidence, and use relations. The Agent performing each neighboring Work applies its governing Method, and that Work produces its own result for the named receiving use.
- Engineering profiles—for example, engineering-data, physical, software, electrical, control, manufacturing,
  medical-device, ship, or building profiles—may specialize description Methods where their subjects,
  formalisms, evidence, and realization relations change the working move. A profile name alone adds no pattern.

### SYSE.7:End

<a id="syse-8"></a>
## SYSE.8 — Develop an Integrated Offering and Provider Concept

### SYSE.8:0 — Use This When

Use this pattern when a project is defining what a provider will make available and under what promise. The
proposal may, for example, transfer a product, grant access to a shared enabling System, maintain an agreed
condition, or accept responsibility for an agreed result, but the project has not yet connected that promise to
the provider arrangement needed for the receiving use.

The result is an **account that connects a bounded offering to the provider arrangement, responsibility claims,
and evidence needed for it**. It becomes an input to engineering and neighboring decisions. The account
describes an engineering proposal; commercial viability, actual provider Systems, performed Work, duties, and
authority claims require their own support.

Apply the pattern when a choice among forms of provision—for example, transfer, access, continuing provision,
or responsibility for a result—changes the engineered System, interfaces, provider Systems, capabilities,
risks, or realization network. A mere change from *product* to *service* wording is outside its boundary. Use `A.2.3` for promise content alone; use `SYSE.1`,
`SYSE.16`, and `SYSE.2` when the project system-of-interest or use is unclear. Neighboring specialist practices retain
their own Methods, results, and authority—for example, practices governing demand, positioning, price, finance,
legal duty, organization change, continuing operations, or shared enabling Systems.

### SYSE.8:0.1 — Precision Restoration

The everyday words in this field are overloaded. Recover the object or relation before relying on them:

| Name in this pattern | What it denotes |
| --- | --- |
| client-side use | A bounded actual or possible-future situation in which a receiving System obtains or attempts to obtain a result. A scenario or journey is a description of that use. |
| promise content | A consumer-facing `U.PromiseContent` episteme stating the promised outcome, applicability, access terms when access is promised, and acceptance claims. Ground the provider, Method, Work occurrence, and any commitment through their own relations. |
| supplied or accessed subject | The product, asset, material portion, data, episteme, capability access, or other subject transferred, changed, accessed, or made available. It need not be a System. |
| provider System | An actual System that participates in a named provider relation, is classified under a local provider SystemRole kind, or holds an assignment under that kind. A department or company name is only a clue until the underlying System and relation are identified. |
| provider arrangement | The Systems and relations through which provision is expected to happen. Its account names actual providers and partners, possible-future provider referents, their assignments and other relations, and the capabilities, Methods, Work, interfaces, resources, and enabling Systems needed for provision. Claims about duty, risk, and evidence remain separate. |
| integrated offering concept | The engineering proposal that connects client-side use, promise content, supplied or accessed subjects, engineered Systems, provider arrangement, realization needs, evidence, and reopen conditions. This is a local collective name; the FPF kinds of its participants remain unchanged. |
| fulfilment or acceptance claim | A claim that evaluates evidence about performed Work, affected subjects and states, and the relevant direct relations against the promise content. Treat the promise, payment, fulfilment, and acceptance through their own relations. |

Bare *service* is a recognition cue. At a consequential use, apply the FPF service-word recovery in
`A.6.P:4.11a` and name the recovered referent or relation. A local `ProviderSystemRole` kind, an assignment
occurrence, an actual provider System, its capability, its Method, and its dated Work remain different objects.

### SYSE.8:1 — Problem Frame

Many engineered results are usable only through an arrangement that continues beyond transfer of a product.
For example, software needs operating infrastructure and change capability; a machine may need consumables,
calibration, maintenance, logistics, data, trained operators, or financing; and a promised condition such as
temperature, availability, or stock level needs Systems that can observe and restore it. Changing the commercial
or access relation can also change the technical architecture and the allocation of risks—for example,
variability, failure, asset, or update risk.

Product-only engineering leaves those changes to later improvisation. Service-first rhetoric creates the
opposite failure: every object and Work occurrence is bundled under one broad word, and the project assumes that
renaming the offer creates a desired effect—for example, demand, recurring revenue, sustainability, or
provider capability.

### SYSE.8:2 — Problem

A plausible technical product concept can coexist with an impossible provider concept. Recurring mismatches
include promising availability without observing the relevant state, retaining ownership without financing or
maintenance capability, automating access while transferring exception Work to users, and depending on partner
Systems whose responsibilities and interfaces are not engineered.

Four documented artifact failures recur: a business model omits bearer and interface constraints; a technical
architecture omits obligations and continuing Work; an SLA omits the actual provider arrangement; and a service
blueprint treats a diagram as evidence that provision will work. No one representation contains the whole
decision.

### SYSE.8:3 — Forces

The engineering decision must manage these recurring tensions:

- A useful first concept must be cheap, while the provider arrangement crosses several kinds of boundary—for
  example, technical, operational, organizational, financial, legal, or commercial.
- Arrangements such as product transfer, access provision, continuing activity, availability responsibility,
  or result responsibility allocate assets, variability, evidence, and risk differently.
- Provider Agents need freedom to choose Methods, yet promise content and acceptance claims must be explicit.
- A technically feasible arrangement can be commercially unattractive; a commercially attractive promise can
  be physically unrealizable.
- Partner Systems and internal shared enabling Systems can supply capability through relations that make them
  neither parts of the provider System nor subjects of the same project.
- Continuing change makes a frozen launch configuration inadequate; evidence must reopen both offer and provider
  choices.
- Current PSS and servitization literature supplies many representations and Methods. Selecting one for the
  current use and claiming a performance gain still require project evidence.

### SYSE.8:4 — Solution

Develop several client-use and provider-arrangement candidates together. For each candidate, distinguish the
promise content, supplied or accessed subjects, Systems, assignments, Methods, Work, responsibility and
authority claims, evidence, economic claims, and consequences that matter to the decision. Name the engineering
decision that consumes each choice and the specialist practice that must answer each specialist question.

#### SYSE.8:4.1 — Perform the Move

1. **Bound the use and decision.** Name the client-side use, intended change, receiving Systems, project
   system-of-interest or intended System referent, configuration, horizon, and decision. Use `SYSE.1`, `SYSE.16`, or `SYSE.17` results only
   when they fit that subject, configuration, use, horizon, decision, and evidence window. Otherwise use a
   qualified direct source or record the missing result, then pause only the decision that needs it. These result
   dependencies do not prescribe the order of Work.
2. **Recover the promise.** State the consumer-facing promise content, eligibility or applicability, access
   terms when access is promised, acceptance conditions, and evidence needed to evaluate fulfilment. Keep each
   actual commitment, permission, delivery relation, acceptance relation, payment, and Work occurrence separate.
3. **Name the subject.** Identify what is transferred, accessed, changed, used, restored, or kept within a
   stated range or condition: for example, a machine, material lot, software edition, data, access point, temperature range,
   stock state, or performed Work. Keep non-System subjects in their recovered kinds.
4. **Generate materially different candidates.** Compare plausible arrangements such as product transfer with
   support, access or use provision, continuing availability responsibility, result-oriented provision, and
   mixed forms. These are examples, not a required taxonomy. Retain variety when evidence can still change the
   choice.
5. **Develop the provider structure.** For each candidate, identify the actual provider and partner Systems.
   Represent a provider that does not yet exist only as an intended referent in a possible-future claim. Record the
   relations and assignments that obtain. Then name the capabilities, Methods, recurring and exceptional Work,
   interfaces, resources, data, tools, shared enabling Systems, supply relations, and recovery arrangements that
   can change the decision. State the kind of each relation—for example, parthood, interaction, transfer, access,
   obligation, or contribution—and ground it independently of any intended referent.
6. **Separate expected Work from responsibility and authority.** For planned Work, name the intended performer
   Agent or the conditions for selecting one, together with the sought result. For Work that has occurred, identify the actual performer Agent and the Work
   independently; add assignment-bound attribution only when the receiving use needs it. Separately identify the
   System that holds or owns each asset; the Agent expected to bear or manage variability and failure exposure,
   observe or restore a condition, and receive each decision or evidence result; and any current responsibility,
   commitment, permission, legal duty, or authority relation.
7. **Connect realization and continuing change.** Identify the realization and change Work, its intended or
   actual performer Agents as applicable, and the Systems it uses or changes. Name the subjects changed—for
   example, the product, provider capability, interfaces, data, operating arrangement, or shared enabling
   Systems. State what later evidence or change will reopen the concept—for example, evidence from a new
   configuration, update, migration, maintenance event, partner change, or recovery attempt.
8. **Obtain specialist results.** Request a specialist result only when it can change the candidate—for example,
   a result from strategy, marketing, commercial analysis, finance, law, organization change, operations,
   supporting-System engineering, safety, security, or environmental engineering. Preserve its source and
   authority boundary.
9. **Compare the candidates.** Compare decision-relevant consequences—for example, client-side use, technical
   feasibility, architecture, capability, value, cost, financing, risk allocation, operational burden,
   changeability, evidence, or affected-System consequences. Keep non-equivalent measures separate unless an
   explicit aggregation Method preserves the distinctions used by the decision.
10. **Record the bounded concept.** Give each candidate one current disposition: select it, retain it for later
    comparison, branch it by a stated condition, or reject it. Record unsupported claims, needed specialist and
    realization results, responsibilities, evidence needs, and conditions for reconsideration. A conditional
    candidate is useful when it makes the next decision visible.

These numbered moves are a CGUS presentation of the Method under `A.22.CGUS`: they expose logical
dependencies but do not prescribe Work order. Work such as use analysis, concept development, architecture,
organization change, operations, commercial analysis, trials, or realization can overlap and reopen earlier
decisions.

#### SYSE.8:4.2 — Record the Result

The smallest useful offering-and-provider account contains:

| Field | Required content |
| --- | --- |
| client-side use | Receiving Systems, intended change, use situation, configuration, horizon, and current decision. |
| promise and acceptance | Promise-content edition, applicability, access terms when access is promised, acceptance claims, evaluation Method, and required evidence. |
| subjects | The supplied, accessed, changed, or maintained subjects named by the proposal—for example, products, Systems, assets, material portions, data, epistemes, states, access, or Work. |
| candidate arrangements | Materially different arrangements—for example, transfer, access, continuing provision, responsibility for a result, or a mixed form—and each candidate's current disposition. |
| provider structure | Actual provider and partner Systems; named possible-future provider referents; the relations and assignments that obtain; and the capabilities, Methods, Work, interfaces, resources, data, shared enabling Systems, and recovery arrangements needed for provision. |
| expected Work, responsibility, and risk | Planned or performed Work, intended or actual performer Agents as applicable, result-restoration actions, asset custody or ownership, variability and failure exposure, and separately supported responsibility, obligation, permission, remedy, or authority claims. |
| realization and change | Required realization and change Work, the Systems it uses or changes, configuration and update conditions, provider-capability changes, dependencies, and unsupported feasibility claims. |
| specialist returns | The needed specialist result and its receiving use—for example, a commercial, financial, legal, organizational, operational, supporting-System engineering, safety, security, or environmental result. |
| evidence and consequences | Decision-relevant evidence and its limits—for example, evidence about fulfilment, use, performance, cost, value, burden, benefit, harm, or consequences for affected Systems. |
| receiving engineering use | Selected or retained concepts, the architecture or realization decisions that use them, and reopen conditions. |

A thin first-use account needs the client-side use and decision, one promise claim, the supplied or accessed
subject, one actual provider System or named possible-future provider referent, one critical Work or direct
relation, and one
evidence gap or receiving decision. Other fields may say *not yet needed* when they cannot change the current
candidate; a load-bearing unavailable answer says *unknown* and names what it blocks. The result may use several
representations. A publication or representation—for example, a canvas, contract draft, architecture view,
service blueprint, financial model, or operations account—is one source. Ground the provider arrangement from
its actual Systems and relations.

#### SYSE.8:4.3 — What Changes in Practice

The practitioner treats transfer as one boundary in a longer provider arrangement and recovers the objects and
relations hidden by *service*. The account keeps client-side use, promise content, subjects, technical
architecture, provider capability, continuing Work, responsibilities, evidence, and change distinct while
connecting them to the same engineering decision.

### SYSE.8:5 — Worked Case: Cast-Iron Transfer, Delivery, or Replenishment

A foundry organization and a machining company must decide how an accepted grey-cast-iron lot will reach the
machining plant. The lot is a material portion, not a System. The two organizations compare three provider
arrangements for the same machining use, material specification, unloading point, and planning horizon.

A commercial lead may decide price and credit and select an arrangement only after an operations coordinator
accepts its schedule. Each person has a current assignment and a separate authority relation. The assignments
identify their project participation; they do not create authority.

| Candidate | Promise and subject | Provider arrangement | Evidence and decision |
| --- | --- | --- | --- |
| **Gate transfer** | The accepted lot will be available at the foundry gate. | The foundry organization performs production Work; the machining company arranges transport from the gate. | Current lot and gate records support availability. The operations coordinator accepts the handover window. The current gate quote is EUR 40,000 with payment due in 30 days. The machining company would also pay EUR 1,800 for haulage within 7 days and perform eight staff-hours of pickup and exception coordination, valued at EUR 50 per hour under `CommercialComparisonRule-2`. The commercial lead retains gate transfer as the low-provider-burden alternative for the foundry, while recording the transport burden received by the machining company. |
| **Scheduled delivery** | The accepted lot will reach the plant's unloading point between 08:00 and 12:00 on the agreed day. | `ForgeHaul-A` is the proposed logistics-provider System. `Truck-12` is the intended transport bearer, and a driver selected under the qualified-driver condition is the intended Agent for the planned transport Work. The proposed `PlantHandover-and-Acceptance-Lot-27` relation keeps custody with the foundry until handover at the unloading point and lets the machining receiver accept only the identified lot, seal, mass, and visible condition against `LotAcceptanceRule-7`. Under proposed `DeliveryExceptionRecovery-Lot-27`, the provider dispatcher must arrange a replacement truck within four hours after a truck failure before handover. No transport, handover, acceptance, or recovery Work has yet occurred. | Operations coordinator `OC-4` performed delivery-assessment Work by applying the plant's delivery-planning Method. The resulting `DeliveryScheduleAssessment-Lot-27` uses the current carrier roster, unloading calendar, and ten recent runs on the same route: nine arrived inside a four-hour window, and one truck failure was recovered with a replacement in three hours. It supports the 08:00–12:00 window and four-hour recovery only for this route, lot class, season, and current provider roster; it establishes neither future performance nor legal responsibility. The authorized operations coordinator accepts that schedule. The current delivered-lot quote is EUR 42,000 with payment due in 30 days. The machining company would perform one staff-hour of arrival confirmation and handover Work, valued at EUR 50 under `CommercialComparisonRule-2`. For schedule-accepted candidates, that rule compares quoted buyer payments plus receiving transport-coordination Work valued at EUR 50 per hour; it selects a candidate only when its advantage exceeds EUR 100 and records any earlier payment obligation. Gate transfer totals EUR 42,200 and includes a haulage payment due within 7 days; scheduled delivery totals EUR 42,050 with payment due in 30 days. The authorized commercial lead therefore selects scheduled delivery for this lot and retains gate transfer as fallback. |
| **Stock replenishment** | Accepted stock at the plant will remain above a stated minimum during operating windows. | A stock sensor exists, but the replenishment controller is only an intended System referent. Observation Work, replenishment Work, access permission, custody, ownership, and restoration commitment remain separate claims. | Sensor history does not yet establish observation reliability; no finance result supports retained inventory; no authorized commitment supplies restoration responsibility. The candidate remains open only for a named observation test and finance decision. |

The authorized commercial lead uses `DeliveryScheduleAssessment-Lot-27`, the operations coordinator's schedule acceptance, and `CommercialComparisonRule-2` with the quoted payments, credit terms, and receiving transport burden to select scheduled delivery. Gate transfer remains the
fallback; stock replenishment remains a possible-future candidate pending its named observation test and finance
decision. The selection does not assert that transport, handover, acceptance, or recovery Work has occurred, and
the intended driver is not an actual performer until separately identified Work occurs. Engineers use the account
to carry product, interface, custody, Work, provider System, evidence, and recovery constraints into use,
architecture, and realization decisions. Commercial and operations decisions remain separate and use their own
authority and evidence. Replacing these relations with the phrase *cast iron as a service* would lose the decision.

### SYSE.8:6 — Bias Annotation

Select candidate distinctions and Methods for the named engineering decision rather than importing a branded
framework as a whole. Sources such as PSS, servitization, service design, SaaS, outcome contracting, or
engineering of shared enabling Systems can contribute bounded alternatives. Reported economic and
environmental gains are configuration-dependent. Academic popularity or official adoption is evidence of
visibility or declared use, not of enacted prevalence or success.

Identify each provider or receiving System from its own basis and name the actual Agent performing each Work
occurrence. Keep neighboring claims separate—for example, claims about ownership, legal duty, capability,
authority, assignment, or a later provider-development decision—even when one System participates in several of
them.

### SYSE.8:7 — Conformance Checklist

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE8-1` | names a client-side use, intended change, receiving Systems, project system-of-interest or intended System referent, configuration, horizon, and decision. |
| `CC-SYSE8-2` | separates promise content, commitments, permissions, supplied or accessed subjects, Systems, Methods, Work, fulfilment, acceptance, payment, and evidence. |
| `CC-SYSE8-3` | compares materially different offering and provider arrangements rather than renaming one product. |
| `CC-SYSE8-4` | identifies provider and partner Systems, relations, assignments when current, capabilities, interfaces, Work, resources, shared enabling Systems, and recovery. |
| `CC-SYSE8-5` | separates expected Work, result restoration, custody or ownership, and risk exposure from any independently supported responsibility, duty, permission, or authority claim. |
| `CC-SYSE8-6` | connects the selected concept to realization, provider-capability change, configuration, continuing operation, and reopen evidence. |
| `CC-SYSE8-7` | preserves specialist decisions and authority rather than absorbing, for example, strategy, finance, law, organization change, operations, or Platform Engineering. |
| `CC-SYSE8-8` | returns a bounded conditional or selected concept with unsupported claims, evidence needs, receiving decisions, and reopen conditions. |

### SYSE.8:8 — Common Failures and Repairs

These documented recurring failures justify the local guards in this pattern:

| Failure | Symptom | Repair |
| --- | --- | --- |
| Rename and declare victory | A product is called a service or solution with no changed engineering claim. | Recover the promise, subjects, provider arrangement, and decision; stop if none changes. |
| Service-object collapse | Provider, API, promise, Method, Work, ticket, access, product, and result share one referent. | Apply `A.6.P:4.11a`; name each referent and direct relation. |
| Product-only architecture | Technical transfer is designed while continuing provision and recovery are assumed. | Develop provider Systems, capability, Work, interfaces, resources, evidence, and change with the product concept. |
| Provider as organization label | A company or department label is used as if it had identified the actual Agent for every provider Work occurrence. | Recognize the actual Systems and Agents; separate local SystemRole kinds, assignments, capabilities, and Work attribution. |
| Universal PSS recipe | One canvas, maturity ladder, or servitization sequence is made mandatory. | Generate context-relevant alternatives and compare them under the named use and evidence. |
| Guaranteed gain | Recurring revenue, sustainability, loyalty, or market growth is inferred from the arrangement form. | Return the commercial, financial, environmental, and use claims to evidence and specialist decisions. |
| Hidden burden transfer | Automation or self-service reduces provider effort while increasing user Work or excluding cases. | Trace Work, exception handling, affected Systems, and burden under each candidate. |
| Specialist absorption | Systems Engineering invents a neighboring result—for example, a price, legal duty, organization design, operating policy, or Platform Engineering result. | Obtain the specialist result and use it as an input with its authority boundary. |
| Frozen provider | Launch architecture is treated as sufficient for continuing provision. | Record configuration, update, maintenance, partner, migration, recovery, and reopen evidence. |

### SYSE.8:9 — Consequences

The project can compare arrangements that genuinely change the engineered System and provider capability.
Promises acquire feasible bearers and evidence plans; technical architecture exposes operational and
organizational dependencies; specialist decisions arrive at named interfaces instead of disappearing inside a
service bundle.

The cost is coordination across several practices and maintenance of corresponding descriptions. Viability and
success retain their own evidence and decisions. Work applying this Method records unsupported promise, capability, responsibility, and evidence claims in the offering-and-provider account so that concept comparison and realization decisions can branch or stop the candidate before commitment.

### SYSE.8:10 — Rationale

FPF already distinguishes promise content, SystemRole assignments, Systems, Methods, Work, evidence,
commitments, permissions, value, and direct relations. The recurring Systems Engineering difficulty is more
specific: a choice among transfer, access, continuing provision, or result responsibility changes both the
engineered subject and the provider arrangement that realizes and sustains use. This pattern connects those
choices without reducing them to the general claim that products and providers are Systems.

### SYSE.8:11 — SoTA and Source Use

| Source line | Use here | Epistemic boundary |
| --- | --- | --- |
| `R6.4:4–7` and `Tasks1` | Supplies promise, access, participation, provider, Method, Work, evidence, obligation, fulfilment, acceptance, salon, SaaS, sharpening, delivery, payment, update, and aircraft-production cases. | Use the cases to recover separate subjects and relations. Ground any product-to-service transition, shared project referent, Agent attribution, and market or provider gain for the current project. |
| [Brambila-Macias, Sakao, and Kowalkowski (2018)](https://doi.org/10.1017/dsj.2018.3), [Braga Junior, de Toledo, and González (2020)](https://doi.org/10.4322/pmd.2019.017), and [Kim (2020)](https://doi.org/10.1017/dsj.2019.30) | Support interdisciplinary PSS design, plurality of development Methods, and several possible representation structures. | Use the reviews and case comparison to generate alternatives. Select ontology, practical Method, and representation for the current engineering decision. |
| [Brax et al. (2021)](https://doi.org/10.1108/IJOPM-08-2020-0535), [Åkesson et al. (2024)](https://doi.org/10.1108/JMTM-11-2021-0457), [Menon et al. (2024)](https://doi.org/10.1016/j.jclepro.2024.142459), and [Zhao et al. (2025)](https://doi.org/10.1016/j.jclepro.2025.146690) | Support configuration-dependent provider performance, SME limits, mixed economic and environmental outcomes, and fragmented technical–social–ecological integration. | Use the studies as bounded evidence. Choose the enterprise arrangement from its use and evidence; assess prevalence separately; qualify any reusable provider-design Method through further cases. |
| Current FPF `A.2.3`, `A.1.SCR`, `A.13`, `A.15.1`, `A.15.6`, `F.6`, `A.6.P:4.11a`, `A.10`, `A.22`, `C.11`, `C.17`, `E.10.ROLE`, and `E.18.NET` | Supplies promise content, actual-System recognition versus intended reference, actual-performer and Work identity, optional assignment-bound attribution, project-focus distinctions, service-word recovery, evidence use, selected structures, value and temporal distinctions, role-word recovery, and transformation-flow structure. | Use these general distinctions directly. `SYSE.8` adds the engineering comparison of offering and provider arrangements and the bounded account returned to later decisions. |

Reconsider the affected source-dependent claim when later evidence changes a practical Method, performance
boundary, or receiving engineering decision. Treat academic or institutional visibility as evidence of
publication or declared use; assess enacted prevalence separately and import only the distinctions needed by the
current decision.

### SYSE.8:12 — Relations

- `A.15.6` supplies the general project-focus and system-of-interest distinctions. `SYSE.1` specializes that
  result for an engineering project; `SYSE.16` supplies the operational use-context account; and `SYSE.17`
  supplies consequence-bearing Systems and unresolved consequences. Compatible current results can be supplied
  directly; the relations do not impose a lifecycle order.
- A `SYSE.8` account supplies only its supported provider-arrangement claims and design constraints to the
  Agents performing linked-concept, realization, or architecture-decision Work. Those Agents apply `SYSE.2` to
  compare linked use and System concepts, `SYSE.3` to develop the recursive realization network, or `SYSE.6` to
  decide the engineered architecture.
- `A.2.3` defines promise content and its acceptance-facing structure. `A.6.P:4.11a` recovers the actual referent
  or relation hidden by *service* or *access* wording. Neither pattern selects a provider arrangement.
- Organization Change Engineering changes provider organization and capability; Operations Management
  coordinates continuing provision; and Platform Engineering changes shared enabling Systems and the Methods
  used to provide or evolve them. Neighboring practices—for example, strategy, commercial analysis, finance,
  law, safety, security, environmental engineering, or governance—retain their own decisions and authority.
- Application profiles retain specialized offering and provider Methods—for example, software, electrical,
  mechanical, building, ship, transport, medical, industrial, or public-sector Methods—when their subjects,
  risks, evidence, or working moves differ.

### SYSE.8:End

<a id="syse-9"></a>
## SYSE.9 — Request and Use Specialist Engineering Results

### SYSE.9:0 — Use This When

Use this pattern when an engineering decision needs a result from another professional practice, but the
project is asking for a document, meeting, review, or job title instead of saying what the decision needs.
Typical requests such as *get architecture approval*, *send it to safety*, or *ask the electrical team* leave
the specialist question, scope, evidence, and later use unclear.

Start with the receiving engineering decision. Ask for the smallest specialist result that could change that
decision: state the question, subject and configuration, applicable Method, expected evidence, acceptance
conditions, authority boundary, and intended use. That bounded contribution request is the first useful result.

For a low-consequence exchange, the request and return may fit in two ordinary sentences. When one decision
depends on several contributions, or an incorrect result would be costly, maintain a **professional-contribution
account** that connects each request to the Agent expected to perform the Work, the Work that occurred, the
returned result, its evidence and acceptance, and its receiving use. The account describes these facts and their
relations. Capability, assignment, authority, Work, and result remain independently supported.

Use `SYSE.17` when the first problem is finding affected Systems, `SYSE.10` when research, model, experiment, or
trial evidence must be qualified, and `SYSE.4` when the project needs an assurance result. `SYSE.9` coordinates
the request, return, and engineering use. The applicable specialist DPF or direct source supplies the specialist
Method, whether the question concerns, for example, law, medicine, safety, security, economics, human factors,
manufacturing, software, or a physical science.

### SYSE.9:0.1 — Precision Restoration

The terms below keep the contribution separate from the organizational labels used to find it:

| Name in this pattern | What it denotes |
| --- | --- |
| professional contribution | Local shorthand for a bounded request, the specialist Work performed in response, its returned result, and the receiving use. The professional-contribution account is an episteme about these objects and relations, not another root kind. |
| specialist | The Agent considered or selected to perform the requested Work because current evidence supports a relevant capability. When role classification or assignment matters, name the local system-role kind and assignment separately. |
| discipline | An admitted `U.Discipline`: a durable field-level practice-and-knowledge whole recognized through `C.20`. A field name or department alone is only a retrieval cue. |
| profession | A Plain collective designation for a socially maintained practice, its practitioners, and institutions that recognize or regulate their work. Recover the particular culture, practitioner classification, credential, or authority relation used by the decision. |
| contribution request | An episteme stating the result needed by a receiving decision. Any WorkPlan, assignment, or commitment needed to obtain it is a separate fact. |
| assignment | An `A.2.1` relation occurrence connecting a holder to a system-role kind for a stated situation and interval. Current capability and performed Work require their own support. |
| returned result | An independently identified result produced by specialist Work and supplied to a receiving decision. Name its governed kind; here it is often an episteme such as a calculation, constraint, observation, objection, or specialist decision. |
| review | A Plain word that may refer to a reusable review Method or to one dated review Work occurrence. State which is meant and identify any returned claim or decision separately. |
| authority or decision right | A separately supported relation with a bearer, scope, basis, applicability, and interval. |

Ordinary prose should stay ordinary: “the refrigeration engineer supplied the compressor operating envelope” is
often enough. For a consequential decision, keep the Agent, capability basis, relevant assignment, Work, Method,
returned result, evidence, authority boundary, and receiving use recoverable. Agents perform the contribution
Work; discipline and profession names help find Methods and candidate Agents.

### SYSE.9:1 — Problem Frame

Whole-System decisions combine results from unlike practices. For example, controller selection may depend on
refrigeration performance, electrical protection, control stability, maintainability, acoustics, and safety.
Each specialist result can concern a different boundary, configuration, interval, characteristic, evidence
standard, and authority relation.

A project loses these differences when it exchanges department names and documents. Recurring examples are
an *architect* assumed to decide every cross-cutting question, a safety specialist asked to approve a design
beyond the available evidence, an AI Agent's report treated as the decision, and a scheduled review treated as
completed Work.

The opposite failure is administrative overload. For example, a small calculation acquires a responsibility
matrix, fixed role catalogue, approval workflow, and document template, yet the receiving engineer still cannot
say what result would change the decision. The remedy begins with the engineering question, not with an
organization chart.

### SYSE.9:2 — Problem

Producing and using a specialist result requires answers to seven questions. The first contribution request
may leave the performer or Method unresolved when it names that gap and the decision it blocks.

1. Which engineering decision or Work is waiting, and what could change because of the result?
2. What should the specialist return, and what kind of result will it be?
3. What subject does the result concern? For a System claim, which configuration, environment, use, interval, and
   assumptions bound it?
4. What Method, inputs, and evidence can answer the question, and where do they stop applying?
5. Which Agent can perform the Work within a current capability envelope, with the needed access and resources?
6. Which assignment, permission, authority, commitment, or responsibility relations matter, and what independently
   supports each one?
7. What will the receiver do with the return—for example, rely on it within a stated limit, reject it, request
   repair, or reopen the receiving decision?

When these questions remain hidden, documents move and approval fields fill while the engineering decision stays
unsupported. A useful return may instead identify a blocker, such as missing evidence, capability, authority,
input, or an applicable Method, together with the decision that cannot yet proceed.

### SYSE.9:3 — Forces

- Specialists need freedom to use their own Methods, while the receiving decision must compare results without
  erasing their limits.
- A contribution kind can remain useful when its performer changes, but capability, access, authority, workload,
  and conflicts depend on the current Agent.
- Assignment can make Work admissible without showing that Work occurred or produced an adequate result.
- Early collaboration reduces translation loss; independent criticism can expose shared assumptions. The
  consequence and conflict of interest determine which arrangement is needed.
- Informal conversation is often enough for a small reversible choice; high-consequence reliance needs
  recoverable scope, provenance, evidence, authority, and acceptance.
- Bounded contribution Work may be performed by any Agent with supported current capability, including a
  human, collective, AI, or robotic Agent. Allocate the Work from that evidence rather than from a species label
  or automation claim.
- A discipline evolves over years, while a project requests and performs dated Work now. These are related but
  not successive stages of one process.

### SYSE.9:4 — Solution

Request a bounded specialist result in the language of the receiving engineering decision. Then select a
capable Agent, establish the relations needed for the Work, assess the returned result, and use it only within
its supported scope.

#### SYSE.9:4.1 — Perform the Move

1. **Name the receiving decision.** State the question, alternatives, deciding Agent, Work that will use the
   result, and consequence of delay or error.
2. **Request a result, not a title or document.** Name what the receiver needs—for example, a calculation,
   constraint, objection, option, observation, or specialist decision—and say how it could
   change the receiving decision.
3. **Bound the result.** Name its subject and the applicability dimensions that could change the answer. For a
   System claim these may include the actual or intended System, configuration, part, environment, affected
   System, use, interval, scale, and assumptions.
4. **Choose the Method and evidence.** Identify the specialist Method, any source family it uses, expected result
   form, inputs, observations, uncertainty, and non-use boundary. If no applicable Method is known, return an
   inquiry problem rather than disguising it as assigned Work.
5. **Choose and enable the performing Agent.** Check current capability and the conditions that affect this Work,
   such as access, workload, conflicts, resources, and tools. Establish an assignment only when it matters.
   Establish permission, authority, commitment, or responsibility separately and from its own governing relation.
6. **Perform and identify the Work.** Keep planned Work distinct from dated Work. Record the enacted Method,
   inputs, performer, relevant assignment, and production of the result. A ticket, calendar entry, generated
   activity trace, or tool label does not prove this Work.
7. **Assess and use the return.** Check its subject, configuration, provenance, evidence, uncertainty, limits,
   and acceptance conditions. Accept it within a stated reliance limit, reject it, request repair, choose another
   contribution, or record the blocker.
8. **Observe and reopen.** Use later evidence—for example from integration, realization, operation, affected
   Systems, or assurance—to reopen the smallest affected request, assignment, Method use, result, or engineering
   decision.

This is an `A.22.CGUS` learning unfolding, not a required temporal sequence for all project Work. Several Agents
may perform specialist Work concurrently and return partial results iteratively. The logical dependencies remain:
a title cannot replace a requested result, an assignment cannot replace Work, and a produced result cannot
replace its assessment and use.

#### SYSE.9:4.2 — Record the Result

Use an ordinary sentence for a small reversible exchange. For several or consequential contributions, record:

| Field | Required content |
| --- | --- |
| receiving decision | Question, alternatives, deciding Agent, relying Work, consequence, and needed interval. |
| request and scope | Needed result, intended use, acceptance conditions, subject, configuration, environment, affected Systems, assumptions, and permitted blocker return. |
| Method, inputs, and evidence | Applicable Method or source, input editions, access, physical subjects, resources, tools, expected observations, uncertainty, and non-use boundary. |
| performer and governing relations | Candidate or selected Agent, capability envelope and currentness, assignment when relevant, conflicts, and separately supported permission, authority, commitment, or responsibility. |
| Work and returned result | Dated Work, performer, enacted Method, production relation, result content, provenance, evidence, dissent, limits, and currentness. |
| receiving disposition | Accepted reliance, rejection, requested repair, alternative contribution, or blocker and the decision or Work it changes. |
| reopen condition | Later source, configuration, use, capability, authority, conflict, or evidence change and the smallest claim or decision to reconsider. |

Several requests may serve one decision, but each result retains its own subject, Method, performer, authority
boundary, evidence, and use. The account is an episteme for reasoning and coordination; it is not the Work or the
world-side relations it describes.

#### SYSE.9:4.3 — What Changes in Practice

Instead of “sending the model to safety” or “waiting for architecture approval,” engineers request a result that
a capable Agent can produce and a receiving decision can use. Missing inputs, capability, authority, evidence,
or applicability become visible before they turn into late integration failures.

Useful returns include the requested supported result, a bounded objection that narrows or rejects the current
proposal, and a blocker. If no current Agent can produce the needed result, the next decision may, for example,
develop capability, obtain an external contribution, change the Method, or change the architecture. Those are
subsequent organization, capability, procurement, or engineering decisions; `SYSE.9` makes the need visible
without absorbing those practices.

### SYSE.9:5 — Worked Case: Contributions to a Heat-Pump Controller Decision

A project is deciding whether a heat-pump controller should use direct compressor modulation alone or coordinate
modulation with thermal storage. Its first coordination table contains rows labelled *controls*, *electrical*,
*acoustics*, *service*, and *safety*. Files have been uploaded, but the deciding engineer cannot tell which
configuration each result concerns or whether any result can change the decision.

The project replaces title rows with bounded requests:

| Requested result | Receiving use | Performer and boundary |
| --- | --- | --- |
| Compressor and refrigerant operating envelope for two compressor variants under named plant and climate assumptions. | Compare controller and storage options. | A refrigeration-analysis team with current model-and-test capability. Its result does not decide control stability or acoustics. |
| Stability, estimator, sampling, fallback, and storage-dispatch assessment for named sensor, actuator, and plant-model configurations. | Decide which controller option may enter trial. | A controls-engineering Agent. An AI Agent may search parameter candidates, but this assignment does not include validation or the architecture decision. |
| Supply, protection, harmonic, I/O, and failure-isolation constraints for the controller, inverter, and installation. | Select interfaces and plan integration. | An electrical specialist with access to the actual supply arrangement and component editions. |
| Access, isolation, diagnostic, and replaceability objections for the installed arrangement. | Compare bearer placement and maintenance conditions. | A maintainer familiar with the intended installation; the result does not speak for every future operator. |
| Tonal-noise and vibration observations for stated compressor speeds, mounting, and rooms. | Compare use consequences and choose further trials. | An acoustics specialist. A generic product noise rating is an input, not the requested site-use result. |
| Refrigerant, leak, ventilation, and installation claims needed before release. | Decide whether the candidate may proceed and what remains unresolved. | The bearer of the relevant specialist authority is named separately; the word *safety* creates neither authority nor a universal veto. |

The controls request exposes a hidden gap. An AI Agent has produced an optimization report, and its provider
interface labels the run *verified*. The assignment covered parameter search, not validation, physical trial, or
the architecture decision. A controls specialist checks the stability assumptions, and controller-in-the-loop
Work supplies observations that `SYSE.10` qualifies for the receiving claim. The provider label proves none of
those results.

The refrigeration team returns a blocker: the supplier data and available tests do not cover the low-ambient,
high-storage-charge region used by one candidate. The project can run another trial, restrict the operating
envelope, choose another compressor, or change the storage strategy. Refusing an unsupported approval has made
the next engineering choices clearer.

The deciding engineer uses each accepted result only within its stated scope. The project neither merges the
specialist Methods nor transfers all authority to a “chief architect.” Later commissioning observations reopen
only the claims and architecture choices they can affect.

### SYSE.9:6 — Bias Annotation

Formal engineering literature often proposes arrangements such as fixed role catalogues, review boards, and
maturity ladders, especially for regulated public or military programmes. Software practice often proposes
cross-functional teams, fast feedback, DevOps, and platform arrangements. These are candidate Methods and
organization arrangements for their domains, not evidence that one arrangement fits every engineering project.

Evidence about a candidate Agent can come, for example, from credentials, prior Work, professional membership,
and tool-supported trials. Use each source only for the capability or relation it supports; current capability,
assignment, authority, performed Work, and result adequacy remain separately established. Apply the same rule to
human, collective, AI, and robotic Agents: allocate bounded Work from current evidence and observe the result.

Public sources such as standards, university courses, and publications show declared practice and public
attention. They do not by themselves establish enacted prevalence or better project results. When comparative
field evidence is not affordably available, state the expert estimate and its uncertainty.

### SYSE.9:7 — Conformance Checklist

- [ ] The receiving decision, deciding Agent, relying Work, and consequence are named.
- [ ] Each request states a result or specialist decision rather than only a title, department, meeting, review
      stage, or document.
- [ ] Subject, configuration, environment, interval, assumptions, and non-use boundary prevent application to the
      wrong case.
- [ ] The Method, inputs, expected evidence, and acceptance conditions are stated, or the request is returned as an
      inquiry problem.
- [ ] The performing Agent has a supported capability envelope and the needed access and resources; assignment,
      permission, authority, commitment, and responsibility remain separate claims.
- [ ] Dated Work, enacted Method, performer, production relation, and returned result are recoverable when the
      decision consequence requires them.
- [ ] The receiver accepts within a reliance limit, rejects, requests repair, selects another contribution, or
      records the blocker and affected decision.
- [ ] Reopen conditions name the later change that can invalidate the result instead of requiring a generic
      periodic review.

### SYSE.9:8 — Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| Request a title, department, review, or document | Name the receiving decision and the smallest result that could change it. |
| Treat assignment as capability or performed Work | Check current capability, then identify the dated Work and result separately. |
| Put authority into *architect*, *owner*, or *safety* | Name the authority relation, bearer, scope, basis, applicability, and interval, or return the missing governor. |
| Ask for broad approval | Bound the claim, subject, configuration, Method, evidence, authority, and intended use; accept a bounded objection or blocker. |
| Treat an AI output or tool status as a specialist result | Recover the performing Agent, provider and tool boundaries, assignment, Work, provenance, checks, and decision use. |
| Hide a blocker to preserve the schedule | Name the missing condition or unsupported relation, the evidence needed to resolve it, and the decision it blocks. |
| Redesign the organization for one small missing result | Request the smallest contribution first; change organization or capability only when the resulting gap requires it. |

### SYSE.9:9 — Consequences

Specialist results arrive in a form that an engineering decision can use. Missing capability, inputs, authority,
and evidence become visible early; dissent and applicability limits survive integration; and a performer can
change without redefining a discipline.

Consequential contributions require more explicit scope, provenance, and acceptance than title-based
coordination. The account becomes unnecessary administration if it is kept without a receiving decision, so use
ordinary sentences for small reversible exchanges and add structure only where it changes reliance or action.

### SYSE.9:10 — Rationale

Relevant distinctions already supplied by FPF include local system-role kinds, assignment, capability, Method,
Work, production, evidence, deontic relations, and decisions. Repeating them beside a list of engineering titles
would add no useful specialization.

This Systems Engineering specialization adds a request-and-use move for whole-System decisions that depend on
unlike professional results. Engineers begin with the integrating decision, formulate the smallest useful
request, preserve each specialist Method and authority boundary, and make the supported result or blocker usable
without collapsing the contributions into one discipline. This changes engineering action beyond the generic
advice to assign capable Agents to roles.

Professional culture and project Work remain different structures. A discipline may vary, select, and retain
new Methods over years. A project may select one of those Methods for intended use before it is enacted. Claim
actual project use only after capable Agents perform dated Work under the needed enabling arrangements and enact
the Method; accepted results and later evidence separately support continued use.

### SYSE.9:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R5.6–R5.7, `R5-GC-27`–`28`, R6.2/R6.6 and `R6-GC-11`, R8.3–R8.8 and `R8-GC-04` | Separate contribution, System, local system-role kind, classification, assignment, capability, authority, Method, Work, result and receiving decision; derive coordination from needed Work rather than title lists. | Guide-local universal agent taxonomies, fixed role rosters, lifecycle handoffs, leadership manufacture, and title-based functions are not retained. |
| [Grote et al. 2025](https://doi.org/10.1109/ISSE65546.2025.11370103) | A current positive Method derives organization-specific engineering-role bundles from required process contributions and stakeholder evidence; three industrial cases report clearer responsibilities and recognized gaps. | The conference study is limited to Advanced Systems Engineering organizations, uses judgment-laden workshops and one clustering technique, and does not merge kind, position, capability, assignment or Work. |
| [Naikar et al. 2023/2024](https://pubmed.ncbi.nlm.nih.gov/38018437/) | Complex human–AI design should include distributed teams, artifacts, networked technologies, communication, adaptation and self-organization rather than one human–machine task list. | This is a conceptual synthesis with an illustrative application, not validation of one complete Method; its institutional cases do not justify military or centralized-authority ontology. |
| [Waterson et al. 2025](https://publications.ergonomics.org.uk/uploads/Function-Allocation-for-Responsible-Artificial-Intelligence-How-do-we-allocate-trust-and-responsibility.pdf) | Function allocation should include system interdependencies, joint operation, decision points, responsibility points, outcomes, authority and dynamic trust. | The framework and experiments are early and small; they establish neither universal responsibility allocation, AI moral agency, legal rules, nor a complete Work-design Method. |
| [Becker et al. 2025 with the 2026 METR update, Agarwal et al. 2026, and Pradas Gomez et al. 2025](https://metr.org/blog/2026-02-24-uplift-update/) | AI Systems already perform bounded software and engineering-design Work; allocation needs task-specific capability, quality, provenance, integration and observation. | Software dominates the evidence, and the sources do not establish autonomous complete engineering, independent problem selection, authority transfer, role-holder replacement, or universal productivity. |
| [INCOSE Competency Framework 2018](https://www.incose.org/docs/default-source/professional-development-portal/isecf.pdf) | Historical counterexample to title inference: role statements differ from job descriptions, one job can combine several roles, local tailoring and proficiency evidence matter. | It inherits a 2015 handbook, lifecycle/acquisition/defense framing and a fixed proficiency ladder. Its catalogue is neither current SoTA nor FPF ontology, assignment, Work or capability proof. |
| [Team Topologies, second edition 2025](https://teamtopologies.com/book) | Current author summary keeps cognitive load, platform grouping, whole-organization use and continuing adaptation visible as organization-design considerations. | The public page is not detailed chapter evidence or an independent effectiveness comparison. Software-team types and interaction modes are candidates, not universal engineering roles or DPF structure. |

Use an explicit epistemic status when field prevalence or causal effectiveness is not cheaply knowable. Expert
judgment can guide a bounded DPF move without pretending to be a population measurement. Reopen a contribution
claim when a later engineering profile, role-derivation comparison, human–AI allocation study, actual project
result, or changed capability makes the current request, holder, authority, acceptance, or DPF boundary wrong.

### SYSE.9:12 — Relations

- The cited FPF patterns `A.2`, `A.2.1`, `A.2.2`, `C.3`, `F.4`, `F.6`, and `E.10.ROLE` distinguish System
  recognition, local system-role kinds, classification, assignment, capability, and Work attribution. `SYSE.9`
  uses those distinctions; it does not create an engineering-title ontology.
- `C.20` identifies an admitted `U.Discipline` as a durable practice-and-knowledge whole. A profession name remains
  a Plain retrieval cue until the relevant culture, classification, institution, credential, or authority relation
  is identified. The Agent, rather than either label, performs the contribution Work.
- `A.3.1`, `A.3.2`, `A.15.1`, `A.15.2`, and `A.15.PROD` distinguish Method, MethodDescription, planned Work,
  dated Work, and result production. A request, assignment, Work record, returned result, delivery, acceptance,
  and use remain different objects or relations.
- `A.2.8`, `A.2.8.PER`, and the applicable domain governors keep commitment, permission, authority, and
  responsibility separate. Use `A.6.RCD` when a needed relation has no admitted governor.
- Work guided by `SYSE.7` maintains decision-usable descriptions; Work guided by `SYSE.10` qualifies research,
  model, experiment, and trial results; Work guided by `SYSE.4` builds an assurance result. These results can
  contribute to one engineering decision without becoming one Method or a mandatory temporal sequence.
- Work guided by `SYSE.9` can produce a specialist result for a `SYSE.6` decision only for the stated question
  and conditions. The result neither entails the architecture decision nor transfers the deciding Agent's
  authority. If it is unavailable or outside scope, the receiver uses another supported source or records the
  missing result.
- Organization Change Engineering supplies Methods for changing positions, units, assignments, authority, and
  capabilities when the contribution arrangement must change. Operations Management supplies Methods for
  coordinating continuing Work. Administrative Work maintains recurring records, access, and schedules.
  Procurement or provider Work obtains an external contribution. These remain distinct from requesting and using
  the specialist result.
- An applied engineering profile should specialize this pattern only when its Systems, risks, evidence, or
  professional Methods change the working move. A profession label by itself adds no profile pattern.

### SYSE.9:End

<a id="syse-10"></a>
## SYSE.10 — Assess Research, Model, and Trial Results for an Engineering Decision

### SYSE.10:0 — Use This When

Use this pattern when an engineering decision relies on a knowledge or evidence input such as a theory,
heuristic, model, simulation result, benchmark result, experiment, prototype trial, test result, operating
observation, or research paper, but the project has not said what engineering claim the input supports, where
that support stops, or how the decision changes.

Begin with one sentence: “This decision may rely on this claim about this subject, configuration, use, and
interval.” Then connect each source or produced result to that claim and state whether it supports, contradicts,
narrows, or leaves the claim unresolved. The first useful result is a **bounded engineering claim assessment**
that names the decision effect and the stronger nearby claim that remains unsupported.

A small reversible choice may need only that sentence and its source. A fuller assessment is useful, for example,
when several evidence bases disagree, the result must survive handoff or delay, automation obscures provenance,
or an error would be costly. The assessment is an episteme about evidence use and its decision effect. It cites
the separately identified sources, subjects, Work, results, and any assurance or acceptance decision on which it
relies.

Use `A.10` directly when ordinary evidence reliance needs no Systems Engineering specialization. Use `C.28` for
causal, interventional, or counterfactual support; `C.11` when deciding whether one further probe is worth its
cost before a local choice; a specialist experimental-design Method for a set or sequence of experiments; and
`SYSE.4` for an assurance conclusion or release-facing consequence. Scientific and specialist practices retain
their own research Methods.

### SYSE.10:0.1 — Precision Restoration

The same research word can name a Method, dated Work, a result, or a publication. Restore the object and
relation needed by the engineering claim:

| Name in this pattern | What it denotes |
| --- | --- |
| research result | An episteme produced or revised by inquiry Work. A paper or another publication carries claims; identify the Agent and inquiry Work separately when their performance matters. |
| theory, hypothesis, or heuristic | A theory or hypothesis is a claim-bearing episteme proposed for explanation, prediction, or criticism. A heuristic may supply a context-dependent Method or a claim about such a Method for search, diagnosis, or choice. Use either as evidence only through a bounded evidence relation. |
| model or mathematical lens | A model is a description used for a stated subject, purpose, assumptions, omissions, and validity boundary. A mathematical lens additionally states its correspondence, preserved and lost structure, payoff, and blocked overread under `C.29`. The represented subject remains separately identified. |
| simulation | Plain wording that may denote a simulation Method, one dated simulation Work occurrence, or its result. For a relied-on result, identify the Agent, Method, model, Work, inputs, and produced result separately. A simulation result concerns model behavior unless a separate evidence relation supports a physical claim. |
| experiment, trial, or test | Plain words that may denote reusable Methods or dated evidence-producing Work. An experiment varies selected conditions to distinguish claims; a trial exposes an actual configuration to selected conditions; a test applies a Method and criterion to a named claim. State the Method, Work, and result separately. |
| verification, validation, or calibration | Plain words that may name a Method, dated Work, comparison, or result claim about a named subject. State that subject, the applied criterion or comparison, and the result. Calibration can improve fit while transfer and future adequacy remain separate questions. |
| observation or measurement result | An observation is an episteme about an occurrence or state. A measurement result attributes a value to a measurand with its Method, model, calibration, uncertainty, and time. The observed occurrence or measured state remains separately identified. |
| evidence | Use of an episteme for a named claim with provenance, polarity, scope, relevance window, and reliance limit under `A.10`. Citation or availability alone does not establish this use. |
| acceptance or assurance | An acceptance result records application of a governed rule to a named subject and input. An assurance result addresses a named assurance claim and reliance threshold. Each has its own Method, Work, authority, and evidence when those facts matter. |
| engineering claim assessment | The local episteme produced here: which claims the named evidence supports, contradicts, narrows, or leaves unresolved for one engineering decision. It is not a new FPF root kind. |

A dashboard or report may display several of these objects together. Identify each object and relied-on relation
before using the display in an engineering decision.

### SYSE.10:1 — Problem Frame

Engineering decisions often precede complete knowledge. Models make alternatives cheap to explore; experiments
and trials expose selected parts of reality; operating observations arrive only after use. Each can be valuable
without supporting the whole decision.

For example, a heat-transfer model can compare storage concepts while saying little about installation error. A
controller bench can expose timing and interface faults while omitting occupants and seasonal operation. A field
trial can support one configuration in one environment while leaving rare failures and another variant
unresolved. A formal proof can establish a property of a formal object while leaving the implementation-to-model
correspondence unsupported.

Projects fail in both directions. Scientific or mathematical prestige is promoted to a universal engineering
law, so “the model says” or “research proves” dictates the design. Or useful partial knowledge is rejected
because it cannot settle the whole outcome. The engineering move is to use the strongest claim supported by the
current basis, state the stronger claim it does not support, and show what changes in the decision.

### SYSE.10:2 — Problem

A decision-usable assessment answers seven questions:

1. Which decision and alternative can change?
2. What claim about which subject, configuration, environment, use, interval, scale, and criterion is at issue?
3. What theory, model, observation, prior result, or other source is current, and what are its transfer limits?
4. Which Agent performed the dated Work that produced each result, which Method did that Work apply, and which inputs, tools, and physical or simulated subject did it use?
5. What evidence relation connects the result to the claim, with what polarity, uncertainty, and unsupported use?
6. What could overturn the reliance—for example, a rival explanation, shared assumption, configuration mismatch,
   failed trial, or affected-System consequence?
7. What decision effect follows—for example, a changed choice or constraint, another probe, postponement, redesign,
   or stop—and what later change reopens the assessment?

Without these answers, *validated*, *verified*, *passed*, *peer reviewed*, and *AI confidence* become authority
labels. Conversely, *not proved* becomes an excuse to ignore a well-scoped result that should change a reversible
choice.

### SYSE.10:3 — Forces

- Waiting for exhaustive evidence can destroy opportunity; relying on an unbounded claim can create avoidable
  harm and rework.
- Useful models omit detail deliberately. The missing structure matters only when it can overturn the decision.
- Simulations and formal analyses run quickly; later physical conditions such as manufacture, installation,
  wear, environment, and use may dominate the eventual result.
- Different practices use *verification* and *validation* for different subjects and relations. One universal
  ladder hides the current engineering question.
- More evidence costs time and can repeat one shared assumption. `C.11` governs one next local probe; specialist
  experimental design governs a non-myopic set or sequence.
- Independent criticism can expose common-mode error; collaboration can repair subject and interpretation
  mismatch. Neither arrangement is always superior.
- AI Agents can generate artifacts such as models, tests, scenarios, and summaries at scale. The same scale can
  amplify source opacity, benchmark leakage, hidden tool changes, and integration errors.
- Counterevidence—including failed trials, abstentions, contradictions, and out-of-envelope results—can matter
  more than the positive cases favored by publication and project reporting.

### SYSE.10:4 — Solution

Assess each engineering claim against the results actually available, preserve the distinction between model
behavior and physical evidence, and supply a supported reliance limit to the receiving decision. An authorized
Agent performs decision or experimental-design Work by applying `C.11` or a specialist experimental-design
Method. That Agent chooses the additional evidence-producing Work and records the probe or experiment-design
result. Assessment Work applying `SYSE.10` later evaluates the available results; it does not make that choice.

#### SYSE.10:4.0.1 — Keep Different Decision Inputs Distinct

Do not turn every promising input into one *signal*. An evidence-bearing result keeps its result kind and enters
a claim through `A.10`. An objective, reward, loss, or heuristic enters `C.11` as the evaluative or choice-rule
input it actually supplies; a number does not make it evidence. A novelty or surprise characterization remains a
characteristic claim. An Agent performing assessment Work applies `SYSE.10` to the engineering claim and its
evidence use. The deciding Agent separately applies `C.11` in decision Work to choose a current option or record a
next-probe result.

#### SYSE.10:4.1 — Perform the Move

1. **Name the decision and claim.** State the alternatives, deciding Agent, consequence, needed interval, and
   claim whose support can change the choice. Bind the claim to a subject, configuration, environment, use,
   interval, scale, and criterion.
2. **Recover the current knowledge basis.** Identify the relevant source epistemes and editions, including
   explanations, hypotheses, heuristics, models, mathematical lenses, observations, prior Work, and contradictory
   results. State their currentness and transfer limits. Evidence does not define the claim it supports.
3. **State what each result can distinguish.** Name the rival claims or alternatives, applicable conditions,
   inputs and controls, measurements, sensitivity, uncertainty, and the result that would leave the decision
   unchanged. If the live problem is choosing one further probe, use `C.11`; for an experiment set or sequence,
   use a specialist experimental-design Method.
4. **Qualify model and representation use.** State the modeled subject, purpose, assumptions, omissions,
   parameters, boundary conditions, solver or inference Method, verification, calibration, validation,
   uncertainty, sensitivity, and extrapolation boundary needed by this claim. Use `C.29` for a mathematical
   correspondence and loss account.
5. **Identify Work, observations, and measurements.** Keep planned Work separate from dated Work. Name the
   performing Agent, enacted Method, tools, resources, subject configuration, inputs, controls, disturbances,
   result production, calibration, measurement interval, uncertainty, and missing data to the degree the claim
   needs.
6. **Construct the evidence use.** For each relied-on result, state the target claim, polarity, the actual grounding
   subject when one is part of the claim, source scheme, scope, relevance window, provenance, supported use, and unsupported use.
   Use `C.28` separately when the claim is causal or counterfactual.
7. **Compare and criticize.** Seek possible defeaters such as shared assumptions, implementation-to-model gaps,
   configuration mismatch, rival explanations, contradictory or negative results, selection effects, failed
   transfer, extrapolation, and affected-System evidence omitted by the original study.
8. **Record the assessment and decision effect.** State what is supported, contradicted, narrowed, or unresolved;
   the reliance limit; residual uncertainty; and the stronger blocked claim. Then state the resulting engineering
   action—for example, choose, narrow, postpone, redesign, seek evidence, or stop. The assessment itself supplies
   neither the decision nor its authority.
9. **Stop and reopen deliberately.** State why the current basis is enough for this decision. Record a compatible
   `C.11` result or specialist experimental-design result when further evidence is chosen. Name the later change
   that would matter, such as a change to a relied-on source, configuration, environment, use, Method, capability,
   observation, or claim.

This is an `A.22.CGUS` learning unfolding, not a lifecycle. Evidence-producing Work may overlap, iterate, or
occur in another order. A physical trial can precede simulation during reverse engineering; operating evidence
can reopen theory and architecture; a formal check and bench trial can address different claims concurrently.

#### SYSE.10:4.2 — Record the Result

Use one claim-and-decision sentence for a small reversible choice. For several evidence bases or consequential
reliance, record:

| Field | Required content |
| --- | --- |
| decision and claim | Alternatives, deciding Agent, relying Work, consequence, claim, subject, configuration, environment, use, interval, scale, criterion, and stronger nearby claim. |
| source basis | Source epistemes and editions, currentness, hypotheses, explanations, heuristics, prior observations, rival accounts, and transfer limits. |
| Method and Work | Evidence-producing Method, discrimination question, planned or dated Work, performer, tools and resources, inputs, controls, disturbances, subject configuration, and result production. |
| model or representation use | Modeled subject, purpose, assumptions, omissions, parameters, boundary conditions, computation or inference, verification, calibration, validation, uncertainty, sensitivity, extrapolation, and `C.29` correspondence when relevant. |
| observations and evidence | Observed occurrence or state, measurement Method and result, uncertainty and interval; target claim, polarity, grounding subject, scope, provenance, relevance window, supported and unsupported use. |
| criticism | Rival explanations, common assumptions, contradictions, negative results, configuration or implementation mismatch, selection effects, transfer limits, and omitted affected-System evidence. |
| assessment and decision effect | Supported, contradicted, narrowed, and unresolved claims; reliance limit; residual uncertainty; blocked stronger claim; and the choice, constraint, redesign, postponement, or stop that changes. |
| further evidence and reopen | Compatible `C.11` or specialist experimental-design result when current; otherwise the missing result; stopping reason and later change that reopens the assessment. |

The assessment may cite supporting records—for example, model cards, trial reports, measurement records, or
evidence graphs—instead of copying them. A long report with no receiving decision is not a better result.

#### SYSE.10:4.3 — What Changes in Practice

Engineers stop asking whether a model is *validated* or a test *passed* in the abstract. They ask which claim
about which configuration is supported for which use, which nearby claim remains unsupported, and how the
decision changes.

Different inputs change different parts of the decision. For example, a theory can generate an alternative, a
heuristic can guide search, a simulation result can reject an infeasible region, a failed trial can expose an
interface assumption, and an operating observation can reopen a model-use claim. Each input keeps its governed
kind and epistemic status. Additional evidence is obtained only after an authorized Agent performs decision or
experimental-design Work by applying the Method that governs that choice, not because this assessment demands a
universal ladder.

### SYSE.10:5 — Worked Case: Evidence for a Heat-Pump Controller Increment

A heat-pump project is deciding whether to integrate a first controller increment that coordinates compressor
modulation with thermal storage. The claim is:

> For the named controller, sensor, and plant configurations, the controller keeps supply-water temperature
> within the declared comfort envelope and avoids harmful compressor cycling in selected low-ambient and
> tariff-response situations inside the qualified compressor-map region.

The project uses several unlike results:

| Method and Work | Result used | Supported and unsupported use |
| --- | --- | --- |
| analytic control reasoning | Stability and sampling claims for a linearized plant region. | Supports local stability under the stated approximation; does not cover nonlinear storage behavior, sensor faults, or installed performance. |
| Modelica simulation | Plant and controller traces over selected weather, load, and tariff situations. | Rejects several storage-dispatch candidates and supports one timing range; does not provide observed physical performance or cover unmodeled installation effects. |
| software-in-the-loop checks | Repeatable results for controller logic, state transitions, and selected properties. | Supports correspondence for the tested software edition; does not establish hardware timing, sensor behavior, actuator response, or building benefit. |
| controller-in-the-loop trial | Measurements from controller hardware, sensor emulation, inverter interface, and selected fault injections. | Supports timing, I/O, fallback, and selected cycling claims for the bench configuration; does not establish installed hydraulic, acoustic, or occupant effects. |
| installed-plant trial | Calibrated temperature, power, state, and fault observations during a bounded low-ambient interval. | Supports the first increment inside the observed and modeled envelope; does not establish seasonal reliability, another compressor variant, or every tariff policy. |
| independent criticism | Compressor-map and maintenance-access checks by relevant specialists. | Exposes an out-of-envelope map region and an inaccessible recovery action; neither result alone decides release. |

The simulation initially appears to support the timing claim, but the model assumes two sensor updates per
second while the selected installed configuration supplies one update every two seconds after filtering. The
project does not reuse that simulation for the installed timing claim. It updates the model account, changes the
estimator, repeats the controller-in-the-loop trial, and narrows the first increment's operating envelope.

An AI Agent produces fault scenarios and a trace summary. One scenario invents an interface state absent from
the source configuration. The summary is useful for finding source traces, but the project relies only on claims
connected to those traces, the actual configuration, and checking Work. The AI Agent's confidence score is not
validation, assurance, acceptance, or release.

The assessment supports integration inside the stated plant, sensor, compressor-map, charge-state, and
environment envelope; rejects reliance on the old timing simulation; and leaves seasonal cycling, the
high-storage-charge region, and another compressor variant unresolved. The architecture decision uses this
assessment, while `SYSE.4` separately determines the assurance result and any permission needed before
commissioning. Later operating observations reopen only the claims and choices that relied on the changed
envelope.

### SYSE.10:6 — Bias Annotation

Sources such as official verification procedures, software test automation, peer-reviewed papers,
sophisticated models, and AI benchmarks can contribute useful Methods or results. Their prestige, publication,
conformance label, mathematical form, or benchmark score does not establish a universal evidence order or the
project's effectiveness.

Across physical, cyber-physical, biological, and social-system cases, the relied-on evidence may depend on
configuration, calibration, integration, environment, use, or affected-System consequences that a software test
or simulation does not cover. Failed trials and actual project practice can matter more than published positive
cases.

Demanding definitive proof can be as harmful as overclaiming when no affordable study can settle the choice. Use
the best current assessment, state its epistemic status, make the decision reversible where possible, and name
the observations that would reopen it.

### SYSE.10:7 — Conformance Checklist

- [ ] The receiving decision, alternatives, deciding Agent, consequence, and claim are named.
- [ ] The claim has a subject, configuration, environment, use, interval, scale, criterion, and stronger nearby
      claim that remains unsupported.
- [ ] Theory, model, simulation, experiment, trial, observation, evidence use, assurance, and decision remain
      different objects or relations.
- [ ] Source editions, Work, performer, Method, model assumptions, physical grounding, observations, measurement
      uncertainty, and transfer limits are recoverable to the degree the reliance needs.
- [ ] Each evidence use states its target claim, polarity, scope, provenance, relevance window, supported use, and
      unsupported use; causal reliance uses `C.28`.
- [ ] Rival explanations, common assumptions, contradictions, negative results, configuration mismatch, and
      affected-System evidence have been sought in proportion to the decision consequence.
- [ ] The assessment states what is supported, contradicted, narrowed, or unresolved and how the decision changes;
      it is not treated as authority or acceptance.
- [ ] A further local probe comes from `C.11`, an experiment set or sequence from a specialist Method, and the
      stopping and reopen conditions are explicit.

### SYSE.10:8 — Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| “Research proves the architecture” | Connect the source claim to the project claim, transfer limits, evidence use, and decision effect; keep the architecture decision separate. |
| “The model is validated” | State the modeled subject, purpose, configuration, comparison basis, result, uncertainty, unsupported use, and currentness. |
| Treat simulation as physical evidence | Keep model behavior separate from observations of the actual configuration; seek physical evidence only for claims that need it. |
| Treat test pass as acceptance or release | Separate test Work, criterion result, evidence use, acceptance rule, assurance, permission, and release decision. |
| Count reports or climb one universal test ladder | Examine independence, shared assumptions, claim match, and decision value; use `C.11` or specialist experimental design for further Work. |
| Hide a failed or negative trial | Record the result, validity limits, and alternatives it changes. |
| Accept a benchmark or AI confidence as general capability | State the task, population, configuration, Method, measure, result, checking Work, and transfer boundary. |
| Demand certainty before a reversible action | Use a stated reliance limit, accepted uncertainty, reversible choice, observation, and reopen condition. |

### SYSE.10:9 — Consequences

Research and models become useful without being promoted to physical ontology or universal law. Tests and trials
become claim-specific rather than ceremonial; negative and partial results can change concepts, architecture,
and realization Work early.

The cost is preserving configuration identity, assumptions, measurement provenance, uncertainty, evidence
polarity, and unsupported uses. Some decisions remain unresolved or receive a narrower operating envelope. Too
little evidence can shift harm to other Systems; too much low-value testing can delay the project. The Agents
performing Work guided by `SYSE.17`, `SYSE.4`, specialist Methods, or Methods for choosing further probes retain
their respective decision authority.

### SYSE.10:10 — Rationale

FPF already supplies evidence, measurement, causal-use, mathematical-lens, dynamics, assurance, decision, and
currentness patterns. A Systems Engineering DPF should not restate them as an evidence hierarchy.

This specialization connects heterogeneous knowledge and evidence results, actual configurations, and decisions
An authorized Agent performing decision or experimental-design Work applies `C.11` or a specialist Method to choose further probes and records a choice or experiment-design result.
Assessment Work keeps descriptions, simulation results, and observations of actual Systems separate, preserves
configuration and extrapolation boundaries, and returns a claim-specific result to the receiving engineering
Work.

Research and engineering remain neighboring practices. Inquiry Work can produce, for example, explanations,
observations, models, and Method candidates; engineering Work uses them while choosing and realizing changes in
Systems, and later trials or operation can revise the inquiry account. Neither practice is a temporal stage or
subtype of the other.

### SYSE.10:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R0.7 and R0.11–R0.13; R6.7 and `R6-GC-23`; R8.2–R8.9 and `R8-GC-05`, `R8-GC-11` | Separate physical phenomenon, model, computation, hypothesis, experiment, observation, evidence, candidate and decision; qualify explanatory research and return bounded results to engineering. | Quantum-like, FEP, constructor, active-inference, scale-free, universal AI and other research lines remain bounded until current evidence changes a practitioner move; quizzes and teaching narratives are not DPF law. |
| Current FPF `C.11:4.2.2–4.2.4` and [Huan, Jagalur, and Marzouk 2024/2026](https://arxiv.org/abs/2407.16212) | An authorized Agent performing decision Work applies `C.11` to choose one next feasible probe using budget, cost, information or computation value, a choice rule, and a `ChoiceResult`; current OED distinguishes the design of experiment sets and sequential policies through utility, design variables, model assumptions, computation, and robustness. | Assessment Work guided by `SYSE.10` uses a compatible `C.11` or specialist experimental-design result and produces an engineering claim assessment. `C.29` can govern a mathematical-lens use, but neither a lens nor this assessment is an experiment plan. |
| [Riedmaier et al. 2021](https://doi.org/10.1007/s11831-020-09473-7) and [Schwarzburg et al. 2024](https://doi.org/10.1017/dsj.2024.14) | Decision-specific model use requires verification, validation, uncertainty quantification, extrapolation attention and consideration of model history, competence, access and decision risk. | No one VV&UQ Method is universal; the 2024 practitioner sample is small and non-probability. Confidence is not truth, physical adequacy, decision correctness or complete reliability. |
| [Papalambros et al. 2025, Yilmaz et al. 2015, and Koen 2003](https://www.cambridge.org/core/journals/design-science/article/design-science-why-what-and-how-revisited/75E30B42E451F82466818FDD4525D6EF) | Heuristics can be context-dependent strategies for intentional variation and candidate generation; current field synthesis retains their engineering relevance. | Koen is historical and philosophical; the 2015 experiment is one short task; the 2025 source is a retrospective. No heuristic family becomes universal law or proof of effectiveness. |
| [Lehner et al. 2025](https://doi.org/10.1007/s10270-025-01264-7) | Digital-twin engineering uses heterogeneous model transformations, code generation and interpretation across design, implementation and operation. | The mapped literature is manufacturing- and transport-heavy with heterogeneous maturity; it establishes neither one twin ontology nor physical evidence by synchronization. |
| [Hernández et al. 2023, Norheim et al. 2024, and Kosenkov et al. 2025](https://doi.org/10.1007/s00766-023-00396-w) | Requirements and compliance Work persist under continuous software and cyber-physical development through collaboration, traceability, monitoring, models and changing descriptions. | The evidence is software-heavy and uses *requirements* in several senses. It neither restores a requirements phase nor shows that legal interpretation, independent assurance or physical evidence disappear. |
| [Mohanani et al. 2022, Binamungu and Maro 2023, Fakhoury et al. 2024, and Wang et al. 2025](https://doi.org/10.1016/j.jss.2023.111749) | BDD, test-driven interaction and requirements-driven testing can connect selected software intents, scenarios and executable checks; template fixation and incomplete automation remain material. | Software cases do not turn tests into obligations, outside-use effects, acceptance, compliance or complete assurance; industry evidence and full automation remain limited. |
| [Krajcer et al. 2026](https://doi.org/10.1017/dsj.2026.10060) and [Mirzaei et al. 2026](https://doi.org/10.1017/dsj.2026.10054) | Current evidence supports task-specific AI acceleration or widening alongside losses in engagement, confidence, opacity, bias and diversity; critical evaluation and integration remain necessary. | The experiment concerns novice UX students and one tool family; the review aggregates heterogeneous design-thinking studies. Neither establishes transfer across engineering profiles or holder replacement. |
| [Becker et al. 2025 with the 2026 METR update, Agarwal et al. 2026, and Pradas Gomez et al. 2025](https://metr.org/blog/2026-02-24-uplift-update/) | AI already participates in bounded software and engineering-design Work, with task-, quality-, prior-use- and integration-dependent results. | The sources do not establish universal productivity, complete engineering autonomy, independent problem selection, authority transfer, or correctness of generated evidence. |

Treat “current SoTA” as claim- and use-specific. A newer paper does not automatically supersede a still-useful
Method; it must change the relied-on claim, alternative, validity boundary or engineering move. Conversely, an
old standard, famous framework or official procedure does not remain current merely because it is widely cited.
Use expert judgment with an explicit epistemic status when direct comparative evidence is unavailable and the
cost of obtaining it would exceed the decision value.

### SYSE.10:12 — Relations

- `C.2.1`, `A.3.1`, `A.3.2`, `A.3.3`, and `C.29` distinguish source and result epistemes, Methods,
  MethodDescriptions, dynamics, and mathematical-lens use without making them physical results.
- `C.11` governs the choice of one next local probe among available options. A specialist experimental-design
  Method governs a set or sequence of experiments. An authorized Agent applies one of those Methods in separate
  decision or experimental-design Work and supplies its result to assessment Work. The Agent performing assessment
  Work applies `SYSE.10`; that assessment Work does not include the distinct Work that chooses the probe or
  produces the experiment plan.
- `A.15.1`, `A.15.2`, `F.6`, and `A.15.PROD` distinguish planned Work, dated Work, performer attribution, and
  result production. A procedure, model, report, or status does not establish Work.
- `C.16`, `C.16.P`, and `A.18` govern measurement, characteristics, scales, units, uncertainty, and admissible
  operations. `A.10`, `G.6`, and `G.11` govern evidence use, provenance, and currentness; `C.28` governs causal
  and counterfactual support.
- `B.3`, `A.21`, `G.4`, and the applicable acceptance and permission patterns govern assurance, gates, and
  consequence-bearing reliance. An engineering claim assessment emits none of those results.
- Assessment Work can produce evidence for `SYSE.6`, `SYSE.4`, or `SYSE.19` only when the claim, configuration,
  horizon, and receiving decision match. Evidence neither authorizes nor entails those decisions.
- Results from engineering Work—for example realization, integration, operation, configuration change, specialist
  Work, or affected-System inquiry—become evidence only through their source and evidence-use relations. Adjacency
  between pattern names creates no such relation or temporal order.
- Applied engineering profiles should specialize Methods for modeling, simulation, experiments, tests, trials,
  or evidence use only when a domain-specific fact—such as the engineered-System kind, physical mechanism,
  regulation, characteristic, scale, or consequence—changes the working move. A domain noun by itself adds no
  profile pattern.

### SYSE.10:End

# Part III — Obtaining Engineering Results, Recursive Realization, Platforms, Independent Constituents, and Evolvability

<a id="syse-24"></a>
## SYSE.24 — Choose How the Project Will Obtain a Needed Engineering Result

### SYSE.24:0 — Use This When

Use this pattern when a project needs one engineering result but someone has already assumed *we will build it*,
*we will buy it*, *a supplier will do it*, or *an AI agent can handle it*. The assumed answer may be attractive,
yet the other ways of obtaining the same result have not been described on a comparable basis.

Start by naming the result and its actual kind. It may be, for example, an engineered System, one usable System
configuration, a reusable Method or `MethodDescription`, access to a capability, performed provider Work, or an
engineering episteme. These examples do not form one result kind. State who will use or rely on the result, what
acceptance means for that use, and when the result must exist or the Work must occur.

The first useful result is a written comparison of at least two complete arrangements that would produce,
perform, transfer, or make the same result available. One `C.11` `ChoiceResult` then says: choose one arrangement
or a retained tie-set now, reject the current set, perform one worthwhile probe, or reroute to another named
question. Each arrangement says what result would exist or occur, which Agents would perform which Work, which
Methods and Systems they would use, what relations would provide ownership or access, and what integration,
configuration, assurance, support, capability, and exit conditions the project would accept.

An arrangement is complete enough for comparison when its omitted burden cannot reverse the choice. *Purchase*
is a possible transfer or agreement inside an arrangement. An AI Agent is a possible performer inside an
arrangement. Method development is an enabling branch unless the sought result is a Method or `MethodDescription`; in that
case use `A.15.6` to decide whether the Method is the project Method-of-interest for the current question. The
short labels above identify parts or cues, while the comparison alternatives are whole arrangements.

Use `SYSE.5` when the unresolved question is only how functions could be borne. Use `SYSE.3` after an obtaining
arrangement has been retained and the next difficulty is whether its realization branches can work. Use
`SYSE.8` when the project is designing an offering and the provider arrangement that will sustain another
System's use. Specialist decisions—for example, commercial, financial, legal, governance, organization, operations, asset,
and capability-development decisions—remain with their specialist practices.

### SYSE.24:0.1 — Precision Restoration

| Wording in this pattern | Meaning used here |
| --- | --- |
| needed engineering result | The particular result this decision seeks, not a universal kind. The practitioner states the actual System, configuration, Method, `MethodDescription`, capability, access relation, performed Work, episteme, or other result and the use that makes it needed. |
| obtaining arrangement | The Systems, Agents, Work, Methods, and direct relations that would produce, perform, transfer, or make the result available in one possible future. The compared option is an episteme describing that arrangement; the described result still needs its own world-side facts. |
| complete arrangement | One option that states the result, performers and Work, Methods and means, provision or access relations, interfaces, integration, configuration, assurance, support, capability consequences, resources, and exit conditions far enough for the present comparison. *Complete* is relative to this decision. |
| internal or external | A qualifier relative to the project boundary chosen for this decision. Name the qualified System, Agent, Work, Method, capability, ownership or access relation, and authority separately when each matters. |
| buy, reuse, commission, subscribe, lease, develop | Common cues to relations and Work inside an arrangement. Expand a cue into the whole arrangement before comparing it. |
| provider | A System on the supplying side of a stated provision or access relation. When Work is expected or observed, name the Agent that performs it and state capability, assignment, duty, Work, and result claims separately where the comparison relies on them. |
| AI Agent | A possible Agent for named Work when the arrangement supports its agency, assignment, authority, capability, access, evidence, and stop conditions. Place it inside an arrangement and support the Work claim separately. |
| parity basis | The same acceptance conditions, use, configuration, horizon, consequence set, and counted burdens used to compare every arrangement. A scalar score is optional and cannot replace a protected condition. |


An Agent performs Work. Other participants—for example, tools, equipment, supplied Systems, materials, data,
and the changed subject—retain their own relations. Name the decision-making person, team, organization, or other
sufficiently agentic System and use the applicable FPF agency, assignment, and authority patterns when the
decision relies on that Agent.

### SYSE.24:1 — Problem Frame

Several recurring failures make this difficulty visible, often only after commitment. Internal development
begins because building is
prestigious or familiar. A polished supplier demonstration is accepted as if integration, configuration,
assurance, migration, support, and exit were already included. Outsourcing is treated as removal of engineering
responsibility. A continuing provider relation is compared with a one-time purchase price. An AI Agent is placed beside a department as a short label. Comparison becomes meaningful only after each
label is expanded into an arrangement that names Work, Methods, means, assignments, integration, and acceptance.

The practical difficulty is not merely make versus buy. It is constructing several ways of obtaining the same
result so that each way exposes the burdens and dependencies that can change the engineering choice. Until that
happens, general decision theory receives a false `OptionSet`: its rows seek different results, use different acceptance
conditions, and hide different Work.

### SYSE.24:2 — Problem

An engineering result can be obtained through many arrangements. For example, a project may adapt a System it
already has, acquire a ready product and integrate it, commission a custom result, obtain continuing provider Work
or access, develop the result with its own Agents, or combine several contributions. The same visible result can
depend on very different conditions, such as interfaces, provider capabilities, data custody, rights, configuration
evidence, support, internal capability, and recovery arrangements.

Ordinary make-or-buy tables hide these differences. Documented recurring failures include placing a purchase
price beside a fully burdened internal estimate, comparing an external demonstration with an internal production
configuration, omitting integration or continued-access burdens, omitting assurance, and treating contract award
as if the System, access, Work, or episteme had already been accepted and used.

The opposite failure is an exhaustive procurement programme before the engineering question is clear. A project
team can spend months choosing contract or tender forms while the needed result, acceptance basis, interfaces, and
capability consequences remain unsettled. The first pass therefore starts from one result and stops at the smallest
decision that changes the team's next Work.

### SYSE.24:3 — Forces

The following eight tensions recur in this decision.

| Force | Tension |
| --- | --- |
| Fast availability and later change | A ready product or provider arrangement may reduce time to first use while increasing dependence, migration cost, or change latency. |
| Internal capability and immediate delivery | Internal development can grow capability while delaying the result; an arrangement that relies on provider Work can make the result available sooner while displacing learning or making it dependent on continued access. |
| Comparable result and heterogeneous means | Every option must obtain the same result under the same acceptance conditions, while the Agents, Work, Methods, Systems, and relations can differ radically. |
| Low entry price and full burden | A visible price is easy to compare, while integration, assurance, data, support, change, and exit burdens often decide the outcome. |
| Provider freedom and engineering assurance | The Agent performing provider Work needs freedom to choose its Methods, while the receiving engineering team still needs evidence that the accepted result and interfaces satisfy the stated use. |
| Technical choice and specialist authority | Systems Engineering must connect the arrangement, while specialist practices retain their decisions, Methods, and authorities—for example, for commerce, law, finance, governance, organization, operations, safety, security, and assets. |
| Option generation and option choice | The engineering team must generate materially different complete arrangements before the deciding Agent applies `C.11` to the fixed `OptionSet`; generating and choosing are different Work. |
| Local result and affected Systems | An arrangement may help achieve the project result while transferring work, risk, lock-in, delay, or harm to affected Systems such as users, maintainers, partners, and providers. |


### SYSE.24:4 — Solution

#### SYSE.24:4.1 — Name one result and one decision

Write one sentence containing these five elements:

- the result being sought and its actual kind;
- the receiving use and the Systems whose use or condition matters;
- the configuration, operating conditions, horizon, and acceptance claims;
- the decision-making Agent and the decision it is authorized to make; and
- the latest useful date for that decision.

If the sentence alternates among a product, access, performed Work, capability, and an evidence episteme, the
decision still has several subjects. Split it or select the one result that changes the next commitment. If the
project system-of-interest, its actual or intended status, or its intended use remains unclear, return to
`A.15.6`, `SYSE.1`, `SYSE.16`, and `SYSE.2`.

The acceptance basis must be usable before arrangement generation. It can include several characteristics and
thresholds; it need not reduce them to one score. State protected conditions and affected-System consequences
that no arrangement may hide.

#### SYSE.24:4.2 — Generate complete ways of obtaining the result

Construct materially different arrangements by using the following six forms as prompts, not as a taxonomy:

- adapt or reuse an available System, capability, Method, or result;
- acquire a ready System and combine it with project integration, configuration, and assurance Work;
- commission provider Work that produces a custom result;
- obtain continuing provider Work, access, or operation under stated availability and recovery conditions;
- develop the result through Agents, Methods, and Systems within the chosen project boundary; or
- combine ready, provider, internal, and shared contributions.

For every surviving prompt, answer the eight common questions in §4.3 and write one whole possible-future
arrangement. Put only whole arrangements in the `OptionSet`. The same purchase relation can occur in several
arrangements; the same AI Agent can perform Work in internal, provider, or mixed arrangements; the same Method-
development branch can enable several options.

Apply `C.18` only when the team also runs a named open-ended generation effort whose archive, Front, descriptors,
telemetry, lineage, or next governing relation must remain available. In that branch, identify the generation
Method and fill the applicable `C.18` generation, archive, or Front record. `C.18` preserves that search result; it
does not supply the domain Method for constructing an obtaining arrangement.

#### SYSE.24:4.3 — Describe every arrangement with the same questions

The following eight questions form the common comparison set. Answer a question only as far as it can change
this comparison, but use the same basis for every option.

| Question | Required content |
| --- | --- |
| What result will exist or occur? | The result kind, identity or designator, acceptance claims, receiving use, configuration, horizon, and completion or availability condition. |
| Who does what? | Agents that may perform the named Work, applicable Methods, assignments and authority when relied on, and the Systems, data, tools, facilities, materials, and services participating in that Work. |
| How will the result be produced, performed, transferred, or made available? | Proposed production, transfer, custody, ownership, licence, access, provision, acceptance, or other relations. Use the specialist result that governs each relation when it changes the choice. |
| How will it fit and remain identifiable? | Interfaces, integration Work, configuration identity, effectivity, migration, interoperability, and any earlier engineering decision that an interface or integration failure would reopen. |
| What supports reliance? | Provider or builder capability, evidence for acceptance, assurance needs, uncertainty, unsupported claims, and one feasible next probe when it could change the choice. |
| What happens after first use? | Support, maintenance, updates, data and knowledge custody, replaceability, recovery, exit, and response to provider or technology change. |
| What capability changes? | Capability gained, retained, displaced, or made dependent on tools or providers for the named later Work. Use `E.23.CDI` or the Human Capability Development DPF when a capability-development decision becomes current. |
| What resources and consequences matter? | Relevant examples include time, money, scarce attention, capacity, risk, burden, benefit, and harm. Keep specialist results and affected Systems visible rather than folding them into one unexplained score. |

An unknown answer can remain unknown when it cannot change the choice. If it can reverse the choice, record it as
the comparison defect and either obtain the specialist result or make it the subject of one bounded probe.

#### SYSE.24:4.4 — Restore parity before comparing

Apply the same five parity elements to every arrangement: acceptance conditions, operating environment,
configuration boundary, evidence horizon, and burden categories. Compare ready demonstrations with representative project conditions,
not with unfinished internal work. Compare a provider fee with the receiving team's remaining Work, retained risks, and exit burden that remain
outside the fee. Compare internal development with the opportunity cost, capability gap, assurance,
support, and time to use that it actually requires.

Do not force unlike consequences into one weighted total when that would hide a protected condition or a
non-compensable loss. Keep a tie-set or a partial order when the available evidence supports several
non-dominated arrangements.

Apply `C.11.CRC` only when the missing input to arrangement comparison is what a finite proposed change
contributes relative to the project's current configuration. Name the current configuration `S0`, the finite
change `Δ`, the realizable changed configuration `S1`, and the arrangement-choice decision that will use the
comparison. Work applying `C.11.CRC` returns only that configuration-relative contribution claim. It neither
constructs an obtaining arrangement nor chooses among arrangements.

#### SYSE.24:4.5 — Use specialist results without taking over their Methods

Use a specialist result only where it can change the comparison. Examples include:

- Strategy for the result's contribution to a strategic choice and for option-set scope;
- Finance for funding, cash, valuation, and financial-risk claims;
- commercial and legal practice for offers, duties, remedies, rights, licences, and contracting;
- Governance or Administration for permission, accountability, tender, and public-procedure claims;
- Organization Change Engineering for positions, assignments, authority, human–AI or provider Work allocation,
  and internal capability arrangements;
- Operations Management for continuing demand, capacity, queues, service, exceptions, and provider performance;
- Enterprise Asset Management for portfolio-level acquire, retain, modify, share, or retire decisions;
- Human Capability Development for a person's capability-development programme; and
- safety, security, environmental, clinical, or other application practices for their acceptance and assurance
  results.

The Systems Engineering comparison cites the specialist result it uses and preserves that result's conditions.
The responsible specialist practice and authorized Agent still supply such results as the contract form, spending
decision, Work assignment, legal duty, or specialist assessment.

#### SYSE.24:4.6 — Choose, reject, probe, or reroute

Pass the completed `OptionSet` to `C.11`. State the `DecisionSubject`, comparison basis, `ChoiceRule`, and one
lawful `ChoiceResult`:

- choose one arrangement or a retained tie-set now;
- reject the current set and return to candidate generation;
- perform one feasible probe whose result can still change the survivor set; or
- reroute because a named realization, organization, finance, law, authority, or other question now governs the
  decision.

For a chosen or retained arrangement, identify its first unsupported realization branch and continue with
`SYSE.3`. The `ChoiceResult` is an episteme. Producing, performing, transferring, accepting, and using the sought
result still depend on the applicable Agents, Work, Methods, and direct relations.

#### SYSE.24:4.7 — Observe use and reopen the choice

Reopen when a changed premise can change the choice. Such a premise may concern result identity, acceptance,
provider or builder capability, an interface, configuration, evidence, a resource limit, support, an affected-
System consequence, or exit. A later provider failure can reopen the obtaining arrangement without reopening the
project system-of-interest. A changed project use can require a wider return to `SYSE.1` or `SYSE.2`.

#### SYSE.24:4.8 — Record the first useful result

The written comparison and choice are usable when a reader can recover the following seven contents:

| Content | Minimum useful answer |
| --- | --- |
| decision | Decision-making Agent, authority boundary, decision date, and the commitment that the Agent may make for the project. |
| sought result | Actual kind, identity or designator, receiving use, configuration, horizon, and acceptance basis. |
| arrangements | At least two materially different whole arrangements, including their Agents, Work, Methods, means, provision or access relations, integration, assurance, support, capability, resources, and exit conditions far enough for parity. |
| evidence and gaps | Evidence used, unsupported claims, specialist results still needed, and affected-System consequences. |
| choice | One `C.11` `ChoiceResult` and the basis that makes it lawful now. |
| continuation | First unsupported realization branch for a retained arrangement, or the named neighboring question that receives a `reroute` result. |
| reopen | Observations or changed conditions that can reverse the choice. |

#### SYSE.24:4.9 — What Changes in Practice

The engineering team stops comparing *buy*, *build*, *outsource*, *AI*, and *reuse* as if those words named
equivalent options. It compares complete ways of obtaining one result. This exposes integration, configuration,
assurance, provider dependence, internal capability, and exit before the commitment makes them expensive.

### SYSE.24:5 — Worked Cases

#### SYSE.24:5.1 — Climate control for a new greenhouse configuration

Small equipment company `GreenHeat-4` needs a climate-control System for greenhouse `GH-2`. Until identity
inception, `GreenhouseClimateControl-GH2` remains the designator for the intended System in the WorkPlan and
descriptions. The receiving use is control of heating, ventilation, misting, and shading during cold-night, rapid-
solar-rise, and failed-humidity-sensor conditions. Acceptance requires bounded temperature and humidity
performance, no unsafe actuator command after the sensor failure, identified software and controller
configuration, recoverable observations, and a supported fallback to manual operation. `GreenHeat-4`'s authorized
management team may choose the obtaining arrangement within its approved equipment budget; electrical-safety
acceptance remains with the named specialist authority.

`GreenHeat-4`'s engineering team develops four complete arrangements:

| Arrangement | Agents, Work, Methods, and means | Integration, assurance, support, capability, and exit |
| --- | --- | --- |
| Ready controller plus integrator | The controller vendor's engineering team supplies a configured controller; the integration company's team performs sensor, actuator, network, and commissioning Work; `GreenHeat-4`'s engineering team maintains greenhouse requirements and accepts the result. | The controller supports the existing field interface, but the greenhouse-specific failure behaviour and configuration export remain unsupported. Vendor support is available for three years; control logic cannot be maintained without vendor access. |
| Commissioned custom controller | The engineering provider's team designs and integrates a custom controller using its named engineering Method and supplies source, configuration, test evidence, and support. | The arrangement gives change access and an escrow proposal, but the provider has not shown representative sensor-failure evidence and cannot meet the required commissioning date without narrowing the first configuration. |
| Internal development with AI assistance | `GreenHeat-4`'s controls engineers lead development; a general AI Agent assists with code and test generation; an independent controls specialist reviews the safety-relevant behaviour. | The company can retain knowledge and change the result quickly, but it lacks a qualified hardware-in-the-loop environment and evidence that the team can complete assurance before commissioning. The receiving team uses its checks of the AI-produced code and tests as evidence for capability and acceptance claims. |
| Ready controller plus internal supervisory layer | The vendor controller retains safety interlocks and local fallback; `GreenHeat-4`'s controls team develops a supervisory optimization layer through a documented interface. | This preserves a supported safety boundary and gives the company control over greenhouse-specific optimization. The arrangement still depends on the controller interface, configuration export, and vendor update policy; failure of that interface defeats the option. |


The parity basis includes the same three operating conditions, commissioning date, interface set, configuration
evidence, assurance burden, data access, support horizon, internal capability consequence, expected change
latency, and exit condition for all four arrangements. The internal-only and commissioned-custom arrangements do
not survive the commissioning-date condition. The ready-controller and hybrid arrangements form a tie-set.

The two survivors have different burdens. The ready-controller arrangement is estimated at EUR 84,000, nine
weeks, and eighteen days of `GreenHeat-4` engineering Work; later greenhouse-specific changes require a vendor
release expected to take four to six weeks. The hybrid arrangement is estimated at EUR 96,000, eleven weeks, and
thirty-two days of internal engineering Work; if the supervisory interface remains supported, the controls team
can make a greenhouse-specific change within five working days. The operating plan expects at least three such
changes during the next three years.

The management team is authorized to commit up to EUR 7,000, forty engineering hours, two hardware-in-the-loop
laboratory days, and five elapsed working days to the obtaining decision. Those limits fit the remaining one-week
decision reserve without moving the commissioning date. The electrical-safety specialist may authorize the
failed-sensor injection in the laboratory; that authorization does not extend to a greenhouse trial.

The management team uses this `ChoiceRule`: preserve the failed-sensor, configuration-identity, and commissioning-
date conditions first. Probe only when the probe stays within the stated limits and every possible outcome changes
what the team may lawfully do. If both arrangements survive, choose the hybrid only when its added price is no more than EUR
15,000 and its added internal burden is no more than fifteen engineering days; otherwise choose the ready-
controller arrangement.

The proposed replay costs EUR 5,500, thirty-two controls-engineering hours, eight integrator hours, two laboratory
days, and five elapsed working days. It uses the intended sensor and actuator interfaces and injects the failed-
humidity-sensor condition while checking configuration export and the supported supervisory API. Its possible
observations have three decision effects:

- an unsafe local fallback or a configuration export that cannot reidentify the tested controller and software
  rejects both survivors and returns the team to arrangement generation;
- a safe fallback and usable configuration export combined with failed supervisory timing or withdrawn API
  support rejects the hybrid and retains the ready-controller arrangement; and
- a safe fallback, usable configuration export, and supported API within the timing limit retain both survivors;
  the price-and-burden branch of the `ChoiceRule` then selects the hybrid arrangement.

`ChoiceResult-GH2-1` is **probe again**. Choosing either arrangement without the replay would leave a protected
acceptance claim unsupported, while rejecting both would discard a survivor that one bounded replay can retain.
This worked case stops at that first useful result. APP-SYSE-04 continues the case through performed replay and a
later choice. `SYSE.3` begins only after the replay retains an arrangement and exposes its first unsupported
realization branch.

#### SYSE.24:5.2 — Obtain a pipeline-condition account rather than an inspection device

`WaterUtility-North` must decide which pipe sections enter its next replacement programme. The sought result is
engineering episteme `PipeConditionAccount-2027` for twelve kilometres of buried pipe; an inspection device is
only one possible means. Acceptance requires stated coverage, location error, uncertainty for wall-loss estimates,
blind-sample checks, raw observation access, configuration and date of the inspected pipe segments, and a
supported relation from observations to replacement decisions. The utility's engineering team compares four
arrangements:

- a specialist provider's field team performs inspection Work and supplies interpreted results but keeps the raw
  data;
- the utility acquires inspection equipment; its engineering team develops internal capability, performs the
  Work, and maintains the equipment and analysis Method;
- the utility leases equipment while the provider's qualified field team operates it and the provider's analysts supply raw observations and interpreted results; and
- a provider's field team performs data collection while the utility's engineering team controls the interpretation
  Method, acceptance checks, and continuing data custody.

The whole arrangements expose different calibration Systems, field access, operating interruption, performer
capability, data rights, configuration identification, blind-sample evidence, support, future repeatability,
internal capability, cost, and exit conditions. A purchase price is not compared with a provider invoice alone.
The internal arrangement includes training, qualification, equipment maintenance, field Work, analysis, and the
cost of delaying the replacement decision. The provider arrangements include acceptance and rework conditions,
raw-data access, repeatability, and recovery if the provider leaves the market.

The utility needs the account once within three months and has no present inspection-equipment capability. Its
asset-replacement board is authorized to choose the inspection arrangement within a EUR 250,000 ceiling and to
allocate at most thirty utility analyst-days. Operations separately authorizes pipe access and interruption; the
board cannot supply that result itself.

The equipment-purchase arrangement fails the time condition. The interpretation-without-raw-data arrangement
fails the evidence-custody and exit conditions. The Finance result compares funding, the Operations result states
pipe-access and interruption conditions, and the legal-practice result states data and remedy terms. The board
uses those results but does not replace their Methods or authorities.

The two survivors are compared on the same basis:

| Basis | Leased equipment with provider collection and interpretation | Provider collection with utility interpretation |
| --- | --- | --- |
| Interpretation capability | The provider presents three comparable surveys and blind-sample results within the required location and wall-loss limits. | The utility's two asset-integrity analysts have replayed the identified analysis Method on held-back observations from the same instrument family and pipe material; all six blind samples met the same limits. |
| Field access and time | The provider mobilizes the qualified field team and leased equipment in six weeks and supplies the account in eight weeks. | The same field team completes collection in six weeks; utility interpretation and acceptance take four more weeks. Both arrangements fit the three-month limit. |
| Evidence custody | The utility receives raw observations in an open format and an interpreted account, but only a summary of the provider's analysis Method. | The utility receives the raw observations, keeps the identified MethodDescription and analysis configuration, and produces the account itself. |
| Repeatability and support | Reanalysis depends on the provider's analysts; the price includes eighteen months of analysis support. | The utility can repeat the analysis; the provider supports instrument calibration and collection for twelve months. |
| Resources | EUR 230,000 and eight utility analyst-days. | EUR 185,000 and twenty-four utility analyst-days. |
| Capability and exit | The utility gains inspection data but remains dependent on an analysis provider. After provider exit, another analyst must be qualified before the account can be reproduced. | The utility gains interpretation capability and retains the account, observations, MethodDescription, and configuration. Provider exit affects later collection but not reanalysis of observations already held. |

The board's `ChoiceRule` first rejects any arrangement that misses acceptance, raw-data custody, or the three-
month limit. Among survivors, it prefers the arrangement that the utility can reproduce after provider exit when
its total price stays within EUR 200,000 and its internal burden stays within thirty analyst-days. If the utility
capability evidence or either resource limit fails, the rule retains provider interpretation instead; if both
interpretation claims fail, it returns **probe again** on one shared blind dataset.

The evidence supports the utility-interpretation branch. `ChoiceResult-PCA-2027-1` is **choose now**: the provider's
field team performs collection and the utility's engineering team controls the interpretation Method, acceptance
checks, and raw-data custody. A further probe would not change which arrangement survives because the utility capability and both resource
limits have already been checked on the common basis. `PipeConditionAccount-2027`
states the provider capability evidence still required for field collection, the blind-sample acceptance Work,
and the first unsupported field-access branch for `SYSE.3`. The subsequent contract, inspection, account acceptance, and pipe-replacement decisions are produced by
their own Work.

### SYSE.24:6 — Bias Annotation

The pattern favours one decision-usable result over a complete procurement programme and favours comparable
whole arrangements over familiar make-or-buy labels. This makes hidden integration and capability burdens
visible early. It may underdescribe specialist concerns—for example, sector-specific market engagement, tender, contracting,
law, public accountability, finance, and post-award operations. Those Methods remain with their specialist
practices.

The pattern also favours preserving several non-dominated arrangements when evidence does not support a winner.
That can look slower than selecting a familiar supplier or internal team, but it prevents missing information
from being disguised as certainty.

### SYSE.24:7 — Conformance Checklist

The following twelve requirements form this pattern's complete conformance checklist.

| ID | Requirement |
| --- | --- |
| `CC-SYSE24-1` | The decision states one sought result with its actual kind, receiving use, configuration, horizon, and acceptance basis, and separately names the decision-making Agent. |
| `CC-SYSE24-2` | Every option is a whole possible-future obtaining arrangement. Treat cues or parts such as a purchase relation, provider label, AI Agent, internal team, or Method-development branch only inside such an arrangement. |
| `CC-SYSE24-3` | At least two materially different arrangements are generated before the deciding Agent applies `C.11` to the fixed `OptionSet`. |
| `CC-SYSE24-4` | The same result, acceptance conditions, operating environment, evidence horizon, and burden categories are applied to every arrangement. |
| `CC-SYSE24-5` | Each arrangement identifies Agents and Work separately from Methods, tools, supplied Systems, materials, data, changed subjects, assignments, and authority. |
| `CC-SYSE24-6` | Integration, interface, configuration, assurance, support, capability, data or knowledge custody, change, and exit consequences are stated wherever they can reverse the choice. |
| `CC-SYSE24-7` | Commercial, legal, financial, governance, organization, operations, asset, HCD, safety, security, and other specialist claims are obtained from their practices rather than decided by Systems Engineering wording. |
| `CC-SYSE24-8` | The comparison ends in one lawful `C.11` result: choose now, reject the current set, probe again, or reroute to another named question. |
| `CC-SYSE24-9` | A retained arrangement names its first unsupported realization branch, while its `ChoiceResult` remains separate from performed Work and the resulting production, integration, acceptance, or use facts. |
| `CC-SYSE24-10` | Reopen conditions name observations or changed assumptions that can reverse the obtaining choice without automatically reopening the project focus. |
| `CC-SYSE24-11` | The comparison remains usable for unlike result kinds, including a System configuration and an engineering episteme. |
| `CC-SYSE24-12` | The public explanation leads with the working difficulty, move, and result; source and ontology detail remains only where it changes the move. |

### SYSE.24:8 — Common Anti-Patterns and How to Avoid Them

The following ten rows document recurring failures and their repairs.

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Make-or-buy word comparison | Rows say *buy*, *build*, *outsource*, *AI*, or *reuse* without the result-bearing arrangement behind them. | Replace every row with a whole arrangement that answers the common questions in §4.3. |
| Demonstration versus production comparison | A polished external demonstration is compared with unfinished but fully burdened internal work. | Apply the same operating conditions, configuration, acceptance evidence, integration, support, and exit basis. |
| Award as result | Supplier selection or contract award is reported as if the System, Work, access, capability, or episteme had been obtained and accepted. | Keep commercial selection, Work, production, integration, acceptance, and use as separate results. |
| Provider absorbs engineering | Outsourcing is treated as removal of interface, configuration, assurance, affected-System, and change responsibility. | State what remains with the receiving project and which provider result supports each reliance. |
| AI as an arrangement | An AI Agent is a peer row beside purchase and internal development. | Place the Agent inside each arrangement where it may perform named Work; state capability, access, authority, evidence, stop, and recovery. |
| Method development as free support | A required new Method is hidden inside an option with no time, evidence, or capability consequence. | Treat it as a separate enabling realization branch, or as the sought result when Method development is the decision itself. |
| Lowest visible price | Purchase or provider price wins while integration, support, knowledge, opportunity cost, exit, and displaced capability remain uncounted. | Restore parity and obtain the financial and specialist results that can change the choice. |
| One scalar hides a protected condition | A weighted score compensates for a safety, authority, evidence, or exit failure that the receiving use cannot accept. | Keep thresholds and partial order visible; reject arrangements that violate protected conditions. |
| Procurement umbrella | Systems Engineering silently chooses tender, contract, incentive, legal duty, financing, organization, or operating policy. | Request the specialist result and use only its consequence for the obtaining decision. |
| Endless option inventory | The team keeps expanding market and technology lists after no new arrangement can change the next choice. | Use `C.19` for exploration policy and `C.11` for the bounded probe-or-choose stop. |

### SYSE.24:9 — Consequences

Projects gain a comparable choice before architecture, integration, supplier, capability, and assurance
commitments become difficult to reverse. Reuse, acquisition, provider Work, access, internal development, and
mixed arrangements can be considered without pretending that their short labels identify equivalent objects.

The cost is that an apparently simple purchase decision becomes an engineering decision with explicit
interfaces, configuration, evidence, support, capability, and exit. Another practice may have to answer a named
question first, so the first result may be a retained tie-set or one worthwhile probe rather than an immediate winner.

### SYSE.24:10 — Rationale

General decision theory can compare options only after they answer the same decision question and carry a shared
comparison basis. Systems Engineering adds the missing domain move: it constructs complete ways of obtaining an
engineering result across a designated project system-of-interest and its builder arrangements when those
structures matter, together with provider and internal Work, interfaces, configuration, assurance, and continuing
change.

The arrangement, not the word *buy* or *build*, is the useful unit of comparison. That unit also prevents a
category mistake seen in AI and Method discussions. An AI Agent can perform Work in several arrangements; it is
not itself a way of obtaining every result. Method development can enable an arrangement or be the result of a
separate project; it is not automatically a peer to purchasing a System.

The pattern stops before procurement becomes a universal Systems Engineering Method. Specialist areas—for
example, market engagement, contracting, incentives, tender, public authority, finance, organization, and
provider operation—have their own problem families and evidence. Systems Engineering keeps their consequences connected to the engineered result
without taking over their decisions.

### SYSE.24:11 — SoTA Echoing

The following five source rows show how this pattern uses and limits the literature.

| Practice line | Contribution used here | Source and limit | Disposition |
| --- | --- | --- | --- |
| Systems engineering covers acquisition and supply whether performed within or outside an organization. | Keep internal and external provision inside one engineering comparison and preserve recursive, concurrent Systems Engineering use. | [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html). The standard supplies process scope and terminology, not one obtaining Method or evidence that every listed process works in every project. | **Adopt the scope; reject lifecycle organization as the pattern's required order.** |
| Product realization distinguishes purchase, make/code, reuse, enabling products, integration, verification, and retained work products. | Generate unlike implementation arrangements and keep enabling Systems, integration, configuration, and evidence visible after the form is chosen. | [NASA Systems Engineering Handbook](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf), Rev 2 (2016). NASA programme practice is a bounded source, not a universal commercial or application-profile Method. | **Adapt.** |
| Software acquisition-versus-development guidance compares off-the-shelf acquisition, internal development or service, contracted development or service, enhancement, and reuse with their risks. | Use these as candidate prompts and as a software transfer probe; do not turn the list into one cross-domain type. | [NASA SWE-033](https://swehb.nasa.gov/spaces/SWEHBVB/pages/32604475/SWE-033%2B-%2BAcquisition%2Bvs.%2BDevelopment%2BAssessment). It is NASA software guidance and does not settle hardware, provider, finance, law, or public-procurement choices. | **Adapt as one unlike-domain case.** |
| Procurement strategy can connect outcomes, internal and market capability, make-or-buy, packages and interfaces, delivery and contracts, tender, integration, risk, incentives, and collaboration. | Preserve the connected-arrangement view and the need to relate capability and interfaces to the outside result. | Prasetya et al., [“Procurement Strategy in Megaprojects”](https://discovery.ucl.ac.uk/id/eprint/10226738/) (2026), a review of 4,228 screened records and 91 full papers. Its evidence is centred on megaprojects and much of its process ends at award. | **Adapt the connected questions; keep the megaproject and pre-award limits.** |
| Payment form trades cost incentive against adaptation when design is incomplete. | Treat price and contract form as specialist inputs whose effect depends on uncertainty and change, not as engineering defaults. | Tadelis, [“Public procurement design: Lessons from the private sector”](https://faculty.haas.berkeley.edu/stadelis/pub_proc_des.pdf) (2012). The model and public/private comparison do not establish one universally superior contract. | **Use as a bounded contrast; leave contract choice outside this pattern.** |

These sources support the need for a connected obtaining decision but do not establish one complete Method for
every sector. Reopen this synthesis when cross-sector evidence changes the common arrangement questions, or when
several acquisition or procurement problem families remain after this pattern and the other named DPFs are
applied.

### SYSE.24:12 — Relations

The following relations locate this pattern's inputs, specialist boundaries, and continuations.

- `A.15.6` distinguishes an actual from an intended project system-of-interest and designates a project Method-of-
  interest only when that Method is the current question. `SYSE.1`, `SYSE.16`, `SYSE.17`, and `SYSE.2` supply the
  relevant use, environment, affected Systems, and linked use-and-System concepts when their results fit this
  decision.
- The six prompts and eight common questions in §§4.2–4.3 guide the Agent's Work of constructing complete
  obtaining arrangements. Apply `C.18` only to a named open-ended generation effort when its generation Method,
  variants, archive or Front, descriptors, telemetry, lineage, and next governing relation need a durable record.
  `C.19` governs how broadly to continue exploration. The deciding Agent performs comparison-and-choice Work by
  applying `C.11` to the available arrangements and produces a `ChoiceResult` for the receiving project decision:
  `choose now`, `reject current set`, `probe again`, or `reroute`. The Agent applies `C.11.CRC` only when a
  configuration-relative contribution comparison is missing.
- `SYSE.5` supplies functional and bearer alternatives; it does not choose how the project will obtain a needed
  result. `SYSE.6` supplies architecture decisions for the engineered System.
- `SYSE.8` may supply an offering-and-provider account when the sought result depends on continuing provision,
  access, custody, or responsibility. It does not choose the receiving project's obtaining arrangement.
- `SYSE.9` supplies a needed professional contribution and its receiving use. `SYSE.10` supplies bounded
  research, model, experiment, and trial results used in the comparison.
- The realization Agent applies `SYSE.3` to a retained obtaining arrangement and develops its first unsupported realization branch. Use
  the applicable FPF and DPF patterns separately for the realization network, WorkPlan, performed Work, and
  resulting facts.
- `SYSE.12`, `SYSE.18`, and `SYSE.23` supply platform, independently governed constituent, and project-system-
  of-interest-and-builder evolvability results when those questions can change the arrangement.
- `SYSE.13`, `SYSE.14`, and `SYSE.4` govern configuration, change and release, and claim-specific assurance.
- `A.13`, `A.15.1`, `A.2.1`, `F.6`, and the authority patterns establish actual Agent, Work, assignment,
  attribution, and permission facts separately; the obtaining-arrangement description remains an episteme.
- `E.23.CDI` and the Human Capability Development DPF govern capability-development questions. Organization
  Change Engineering, Operations Management, Strategy, Finance, Governance, Administration, Enterprise Asset
  Management, law, commercial practice, and application DPFs retain their own Methods, evidence, and decisions.

### SYSE.24:End

<a id="syse-3"></a>
## SYSE.3 — Develop the Recursive Realization Network

### SYSE.3:0 — Use This When

Use this pattern when one grounded engineering architecture candidate or decision exists, but no current account shows which actual Systems, capabilities, Methods, resources, interfaces, and Work could bring about the
proposed System or change.

The first useful move is to name one unsupported realization branch, its proposed transformer System or the
need to find one, the missing enabling condition, and one next planned action or earlier answer to revisit.
Expand only when another build-the-builder branch changes that next action.

The result is a `RecursiveRealizationArrangementResult@Project`, a project-local `U.Episteme` containing a
provisional realization-network description plus a distinct `U.WorkPlan`. It identifies the first unsupported
branch, proposed transformer and enabling Systems, identified gaps, result dependencies, and the earlier
answers that each gap can reopen. The description and WorkPlan are epistemes for analysis and planning. Establish
performed Work, actual change, an obtaining network, and feasibility through their direct evidence and patterns.

Use current FPF architecture patterns when the architecture or bearer choice is still open. Use the relevant specialist pattern when the question has left this realization account—for example, a
question about performed Work, transformation, production, capability, platform engineering, operations,
organization change, configuration, or assurance.

### SYSE.3:0.1 — Precision Restoration

| Cue | Meaning used here |
| --- | --- |
| realization | Actual or intended Work and transformations by which an engineered System or configuration can be produced or changed. A description or decision does not realize its subject. |
| creator, builder, developer, or manufacturer | A cue to recover separately the admitted System, its local SystemRole and assignment, its capability, its Method, and its performed Work. |
| realization-network description | A project episteme that describes proposed transformations, participating Systems, result dependencies, and gaps for one current realization question. It is not the selected world-side structure it describes. |
| selected realization network | An `A.22`/`E.18.NET` `U.Structure` established through independently identified transformation-flow or nested-network members, obtaining cross-boundary relations, endpoint bindings, and one use frame. Other project descriptions contribute only the claims that support those values. |
| build the builder | A recursive branch in which Work changes or produces a System, capability, Method support, tool, or platform needed by later realization Work. It is not a permanent creator hierarchy. |
| platform or toolchain | A cue to identify the enabling Systems, services, interfaces, capabilities, and conditions that matter here, then establish their availability, fit, Work, and integration contributions separately. |

An engineer is an admitted System classified by and assigned to an engineering SystemRole for the Work. The
performer System, SystemRole, assignment, Method, capability, WorkPlan, Work, transformation, result episteme,
and engineered System remain distinct.

### SYSE.3:1 - Problem frame

Use this pattern when an engineer has one grounded architecture candidate or project architecture decision,
but cannot yet show how existing Systems and feasible Work can bring about or change the proposed System and
its selected structures. The architecture may name suitable bearers for required functioning while a
realization branch—for example, fabrication, adaptation, integration, configuration, installation,
qualification, or build-the-builder Work—remains unsupported.

First useful move: name one unsupported realization branch, the proposed transformer System, the missing
enabling condition, and one next planned action or earlier answer to revisit. This is enough to turn a broad
claim that the architecture is "buildable" into a specific feasibility question. Expand the description only
when several branches interact or the next action itself depends on realizing a transformer System,
capability, Method, tool, or platform contribution.

If this move is missed, a project description—for example, a product tree, WBS, schedule, toolchain diagram,
or platform name—can look like a realization argument. Engineers can then plan Work for a System that does not exist, assign Work to a label
that has no capable holder, or discover late that a selected interface, material, access condition, or
integration relation cannot be realized.

The payoff is a bounded realization account. The engineer inspects dependencies only far enough to find the
first unsupported one, plans one useful next action, and uses an infeasibility result to reopen only the
smallest earlier answer it changes. A build-the-builder branch appears only when changing an enabling System,
capability, Method support, tool, or platform changes that next action.

Use this pattern after the architecture has at least one candidate bearer for every required functioning at
issue. Otherwise keep the architecture question open with `A.6.F`, `C.30`, and `C.32`. Use `A.3.4` for an actual
bounded change, the A.15 family for Work and production claims, and `E.18` or `E.18.NET` only when their
selected-structure conditions are met. Use Operations Management or project-portfolio practice when the live
question is queue, capacity, priority, or shared-resource coordination rather than realization of one
architecture candidate.

At the first consequential use of words such as *creator*, *builder*, *developer*, *design*, *production*,
*deployment*, *platform*, *toolchain*, or *baseline*, ask: **which realization branch is unsupported?** Name
the intended result or change, the proposed transformer System or unresolved need for one, and the missing
enabling condition. Use the local `TransformerSystemRole` only when that work-facing distinction matters; it
is not a new kind of person or organization. Treat a source stage name or tool label as a cue; establish the
Work order, assignment, capability, and relation that the current branch actually uses.

### SYSE.3:2 - Problem

An architecture candidate proposes an organization of the System, but it does not make that organization
exist. For example, a selected module, interface, placement, control relation, or configuration may depend on
changes to
pre-existing materials and Systems, first constitution of new Systems, integration Work, and Systems capable
of performing that Work. Those transformer Systems can themselves need new capabilities, tools, Methods,
resources, configuration, or prior change.

A single decomposition rarely exposes all of these dependencies. A component tree follows the proposed
System; a WBS follows intended Work; an organization chart follows one organization; a platform inventory or
diagram follows selected technical means. None alone answers which actual Systems can perform the needed Work
under the stated conditions. The engineering difficulty is to connect these descriptions without merging
architecture, intended change, transformer capability, WorkPlan, performed Work, and evidence into one diagram.

### SYSE.3:3 - Forces

| Force | Tension |
| --- | --- |
| Architecture intent and physical feasibility | Selected structures guide realization, while their candidate or decided status does not make them actual. |
| Backward dependency and forward Work | Reasoning backward reveals missing support, while actual Work and change proceed through their own facts and may follow another order. |
| Useful recursion and endless decomposition | A missing transformer capability can open another realization branch, while most questions need only the first unsupported branch. |
| Readable provisional description and typed relations | A provisional realization-network description makes dependencies visible, while an actual `E.18.NET` selection requires independently identified members, obtaining relations, and endpoint bindings. |
| Shared platforms and local conditions | A platform can enable several branches, while its name does not establish availability, fit, capability, or one universal pipeline. |
| Project focus and specialist depth | Systems Engineering must keep the whole realization question connected, while specialist practices retain their Methods and decisions. |
| Plan stability and revision from feasibility evidence | A WorkPlan coordinates the next action, while new evidence can revise the branch, architecture candidate, system concept, or project focus. |

### SYSE.3:4 - Solution

#### SYSE.3:4.1 - Start from one named architecture result

Start with one current architecture result for one described holon:

1. the current `C.30` architecture question and claim;
2. one `C.32` candidate configuration or one `C.32.PAD` project architecture decision;
3. the selected structures, constraints, assumptions, and expected architecture gain that matter to
   realization; and
4. the next use for which feasibility must be known.

The input may remain modal. A candidate structure is not an obtaining `ArchitectureRelation`, and a project
decision does not make the decided structure actual. Keep the architecture result and the realization account
as separate claims. When provider capability, continuing provision, access, custody, responsibility, or recovery
can change realization, use only the supported claims and design constraints from a compatible `SYSE.8`
provider-arrangement account for the same subject, configuration, use, horizon, decision, and evidence window.
Without a compatible current account, use a qualified direct source for the claim needed by this branch or
record the missing result. The account supplies supported provider claims and design constraints. Establish the
provider arrangement, provider Systems, performed Work, responsibility, and authority separately when the branch
uses them.

Check the architecture boundary before proceeding. If the candidate lacks a bearer for required functioning,
reopen the bearer question under `A.6.F` and `C.32`. Continue here when the candidate has a proposed functional and
structural answer but the Systems and Work needed to constitute, change, integrate, or qualify it remain
uncertain.

#### SYSE.3:4.2 - Describe one realization branch

Write one branch in ordinary language. Include only the distinctions that change the feasibility question:

- the architecture result to be realized;
- the pre-existing System, material, assembly, description, or other referent that would be changed, or the
  identity and completion conditions for a System that does not yet exist;
- the intended change, production result, interface state, integration state, or configuration relation;
- the proposed transformer System or unresolved need for one and the local `TransformerSystemRole` condition
  it would meet for this Work;
- the needed Method, capability envelope, resource, tool or platform contribution, access condition, interface,
  integration, and configuration relation; and
- the fact or specialist result that would make the branch usable, require its repair, or reopen an earlier answer.

Keep modal and actual claims apart. An intended change belongs in a plan or description until an actual
continuing referent, boundary, conditions, and before/during/after facts satisfy `A.3.4`. When the proposed
System does not yet exist, describe changes to pre-existing materials or assemblies and use `A.15.PROD` later
for independently grounded identity inception and production completion. Do not describe transformation of a
future System before it exists.

A proposed transformer is also modal. Name the candidate holder System, or the unresolved need for one, and the local `TransformerSystemRole` condition in
the WorkPlan. Use `A.2.1` only when an assignment occurrence actually obtains, and use `A.2.2` only when the
holder's capability has a recoverable Work family, envelope, measures, qualification window, and currentness
condition. Treat a job title, supplier category, tool list, past success, or Method description as possible
evidence inputs; establish the capability claim through its Work family, envelope, measures, qualification
window, and currentness.

#### SYSE.3:4.3 - Find the first unsupported answer

Use the `A.1.STM` long mantra to keep the architecture result, intended outside use, and builder dependencies in
attention. Read the logical dependency backward and find the first unsupported answer that prevents one credible
next realization action. *First* means logically first for this dependency, not earliest in a calendar or
prescribed process.
Classify the first gap with the following six working questions. This is the complete question set used by
this pattern:

| Working question | Result or next practice that resolves the gap |
| --- | --- |
| Which existing System could perform the intended Work? | Name a candidate transformer System and role condition, or use the System-recognition or specialist-search Method that can supply one. |
| Can that System perform the Work under the required conditions? | State the missing `A.2.2` capability claim, threshold, envelope, qualification, or currentness result. |
| Which Method and means make the intended result plausible? | Name the Method question and the missing resource, tool, access condition, or platform contribution. |
| Can the selected structures be constituted and connected? | Name the missing interface, integration, configuration, placement, or production-feasibility result. |
| Which prior change makes the transformer or means available? | Open one recursive realization branch for that System, capability, Method, tool, or platform contribution. |
| Does the proposed architecture still have an admissible realization? | If no branch remains, name the `C.32` candidate, architecture decision, or linked use-and-system concept that the failure requires the practitioner to reopen. |

Record the first gap even when later gaps are already suspected. The first useful result is a decision aid, not
an inventory of everything that could fail.

#### SYSE.3:4.4 - Recurse only when the next action depends on it

Open another branch when the current transformer System, capability, Method, tool, or platform contribution
must itself be brought about or changed before the current branch can proceed. Apply the same questions to that
branch. Do not introduce fixed builder levels: a transformer System can serve several branches or projects,
and evidence from a later branch can change an earlier branch claim.

When several branches must be considered together, begin with a Plain provisional realization-network
description. Name the proposed members and the missing cross-branch relation or binding. Use `E.18` only for one
selected transformation-flow structure whose identity is established. Use `E.18.NET` only after at least two
independent member structures, the obtaining cross-flow relation occurrences, the endpoint bindings,
applied constraints, and the current use frame are recoverable. Until then, the episteme describes a proposed
realization network; it is not the selected network itself.
When a cross-branch arrow uses a generic cue—for example *creates*, *builds*, *uses*, *supplies*, or *depends
on*—replace it with the actual production, participation, use, evidence, integration, configuration, supply, or
other relation through the pattern that defines it. If the relation kind or case facts are not yet available, keep the dependency as a
provisional claim and name what must be established.

Keep each `DesignRunTag` local to one leaf-position binding. Represent any wider dependency or Work order
through the direct relations that establish it.

#### SYSE.3:4.5 - Plan the next Work separately

Create or amend one `A.15.2` WorkPlan after the first unsupported answer is visible. The smallest useful
WorkPlan needs one substantive PlanItem that states:

- the present EntityOfConcern and planning horizon;
- the intended Work or investigation;
- the candidate performer System and local SystemRole-kind conditions;
- the Method, capability threshold, resources, tools, access, and dependencies needed for that Work; and
- the result or evidence that will update the branch or reopen an earlier answer.

The next Work can take different forms—for example, investigating a supplier, qualifying a capability,
developing a fixture, changing a transformer System, obtaining a specialist result, integrating a bounded slice,
or revising the architecture candidate. Select the
action that resolves the first unsupported answer; do not schedule every visible branch.

The WorkPlan states intended Work and its conditions. Establish every later assignment, capability, resource
availability, relation, Work occurrence, transformation, and result through its direct evidence and pattern. When Work is later performed, use `A.15.1` and `F.6` for its performer and
attribution, `A.3.4` for actual changes, and `A.15.PROD` for production, identity-inception, or completion
claims. Compare the resulting facts with the plan only when that separate question is current.

#### SYSE.3:4.6 - Obtain specialist results without absorbing their Methods

Keep the realization branch connected while leaving specialist decisions with the practice that can make
them. The following rows are recurring specialization boundaries, not a closed taxonomy of practices:


| Current gap | Result needed here | Practice that keeps the detailed Method |
| --- | --- | --- |
| A shared tool or platform cannot yet support the Work | capability, availability, interface, configuration, or change result for the named platform System | Platform Engineering or the applicable domain engineering practice |
| A transformer organization lacks a suitable structure, assignment, authority, or coordination relation | a named organizational or authority result and its conditions | Organization Engineering, Systems Management, Governance, or the applicable authority practice |
| Several projects contend for a transformer or resource | the direct interdependency, capacity, timing, or priority result used by this branch | Operations Management or project-portfolio practice |
| A configuration or integration relation is unresolved | the configuration identification, compatibility, change, integration, or release result needed by the branch | configuration or integration practice for that domain |
| A capability or use claim needs a challenge | the claim-bound evidence and reliance result | `SYSE.4` and the applicable assurance or specialist practice |

Name the contribution that an enabling arrangement actually makes. For example, a platform, team, supplier,
administrative service, or configuration repository can supply one bounded contribution rather than a universal
realization layer. When no maintained receiving pattern exists, retain
the unresolved specialist need and the decision it blocks.

#### SYSE.3:4.7 - Stop at one actionable gap and name the affected earlier answer

The first result can be stated in five lines:

1. **Architecture input:** the named candidate or decision and the selected structures at issue.
2. **Unsupported branch:** the intended result or change whose realization is not yet supported.
3. **Missing support:** the proposed transformer System or unresolved need for one and the capability,
   Method, resource, platform contribution, interface, integration, or configuration result still needed.
4. **Next Work:** one WorkPlan item that can resolve that gap.
5. **Affected earlier answer:** the branch, architecture answer, linked concept, or project-focus claim to reopen if the result defeats it.

Stop when these five lines make the next action and affected earlier answer clear. Expand only when interacting branches or
build-the-builder recursion changes that next action.

When feasibility evidence arrives, update the branch description and WorkPlan. If one branch fails but another
admissible branch remains, repair or replace that branch. If no admissible realization remains, reopen the
architecture candidate or decision. Reassess the linked use-and-system concept under `SYSE.2` only when its use or concept claim must change,
and reassess the project-system choice under `SYSE.1` only when the project focus or boundary must change. Cost already incurred supplies no
reason to preserve an unsupported answer.

### SYSE.3:5 - Archetypal Grounding

#### Pumping station under flood risk

`FloodPumpStation-7 : U.System` exists at configuration `FPS7-C18`. `SYSE.2` supplies a compatible station
concept for changing that station so it can move water under the selected flood load without unacceptable
downstream harm. `StationArchitectureDecision-7`, a compatible `SYSE.6` result, selects
`StationArchitectureCandidate-7` with a changed discharge assembly, interfaces, placement, and control
relations. The architecture has proposed bearers for the required station functioning; the open question is how
to realize the changed assembly. `Station7ProviderArrangementAccount-R1`, a compatible `SYSE.8` result, supplies
only current provider, access, custody, and recovery claims that bear on the supplier branch. It establishes no
supplier capability, assignment, Work, or production result.
The first use produces this filled five-line result:

1. **Architecture input:** `StationArchitectureCandidate-7`, including the selected discharge interface,
   placement, material, geometry, and tolerance claims.
2. **Unsupported branch:** `ManifoldRealizationBranch-1`; a pre-existing discharge-manifold blank must be
   changed, and a newly constituted mounted subassembly must satisfy those claims.
3. **Missing support:** `SupplierWeldCell-4` is the candidate transformer System for later welding Work. The
   branch still needs a capability result for the selected material and geometry and a feasible positioning
   fixture.
4. **Next Work:** the WorkPlan contains `FixtureAndSupplierFeasibilityInvestigation-1`. Its intended performer
   is `StationRealizationEngineeringTeam-2`, not the supplier weld cell whose later production capability is
   being investigated.
5. **Affected earlier answer:** if no fixture-and-weld branch meets the selected interface and access conditions,
   reopen the `C.32` comparison of interface, material, module split, and placement alternatives.

One minimally useful PlanItem fills the planning half of that result. This is a case instance, not another
required form:

| PlanItem part | Pump case value |
| --- | --- |
| Present EntityOfConcern and horizon | The one present EntityOfConcern is the already identified architecture-candidate episteme `StationArchitectureCandidate-7`. `ManifoldRealizationBranch-1` remains PlanItem content about the unsupported branch. The case-local supplier-feasibility window is 2026-09-07 through 2026-09-18, before the next discharge-interface choice. |
| Intended Work | Compare feasible fixture and welding arrangements for the selected manifold material, geometry, tolerance, access, and interface conditions. |
| Intended performer and local role condition | The already admitted System `StationRealizationEngineeringTeam-2` is the intended performer. The plan requires a positive classification judgment under local `FixtureAndSupplierFeasibilityInvestigatorSystemRole`, constituted in `StationRealizationFeasibilityPractice-2026` by the assignable contribution of comparing fixture-and-weld branches and producing `FixtureAndWeldFeasibilityAccount-1`. This investigation-facing condition is distinct from `SupplierWeldCell-4` as the candidate transformer System for later welding Work. The plan establishes neither the classification judgment nor an assignment occurrence. |
| Method, capability, resources, and dependencies | The plan names `FixtureAndSupplierFeasibilityMethod-v2`; requires a current capability-fit result for the engineering team before Work entry; and supplies the architecture candidate, manifold material and geometry claims, access conditions, supplier capability statements, and their evidence references as inputs. These planned conditions establish no capability or resource availability. |
| Planned result and affected earlier answer | The intended result is `FixtureAndWeldFeasibilityAccount-1`, which identifies a supported fixture-and-supplier branch or names the failed interface, material, module, or placement assumption that requires renewed `C.32` comparison. The result does not yet exist merely because the PlanItem names it. |

`Station7RecursiveRealizationArrangement-R1 : U.Episteme` is the case result. Its EntityOfConcern is
`StationArchitectureDecision-7` for the bounded station-realization question. It cites the provisional
realization-network description and the distinct WorkPlan, names `ManifoldRealizationBranch-1` as the first
unsupported branch, records the proposed transformer and enabling Systems, and names the earlier architecture claim that the
fixture-and-weld gap can reopen. It establishes neither an obtaining realization network nor performed Work.

If the fixture itself must be developed, that need opens one recursive branch for a toolmaking System and its
capability. The engineer stops there unless this branch changes the immediate investigation. If no admissible
weld or fixture branch remains, the engineer reopens the `C.32` comparison of interface, material, module split,
and placement alternatives. The engineer reassesses the linked station concept under `SYSE.2` only if the concept or outside-use claim must change.
The fixture does not become part of the pump merely because realization needs it. The supplier's shop title
does not establish welding capability, and the WorkPlan does not establish that welding Work or manifold
change occurred.

#### Manufacturer's ERP-enabled planning change

The architecture candidate concerns one deployed production-planning System. It names the software bearer,
interfaces to order and shop-floor Systems, selected data and decision relations, and the planning functions
that those Systems are expected to support.

The first unsupported branch is the change from current product, order, and resource descriptions to the
configuration and integration state required by the candidate. `PlanningIntegrationTeam-2` is the candidate
transformer System for `RepresentativePlanningDataIntegrationWork-1`: mapping one representative data family
and configuring its source-to-planning interface. The planned holder-dependent capability requirement is the
ability of that team to apply `BoundedPlanningDataMappingMethod-v1` under the actual source semantics, access,
timing, and configuration conditions. This is WorkPlan content until `A.2.2` supplies a current capability
result and `A.2.1` supplies an assignment occurrence when one is needed.

`MigrationToolService-3` is a separate proposed tool or service contribution to that Work: access to a named
mapping-execution interface under the selected configuration. This case attributes no transformer assignment
or data-mapping capability to that service label. If a later claim relies on it as an acting System, the
engineer applies System recognition before making separate claims about its role, capability, and Work. The
immediate WorkPlan item names `PlanningIntegrationTeam-2` as intended performer of the representative-slice
feasibility investigation and asks for `RepresentativeIntegrationFeasibilityAccount-1` plus any organization-
design result needed to make the slice feasible.

If the gap concerns who may change source definitions, which organization holds an assignment, or which
authority relation applies, the engineer obtains that result from Organization Engineering or Governance
rather than encoding it as a technical interface. If the branch cannot preserve the required decision timing
or data meaning, the engineer reopens the `C.32` comparison of interface, placement, and responsibility
structures. The engineer reassesses the linked planning concept under `SYSE.2` only when the planning-use claim must change. The words *platform* and *migration pipeline* establish
neither integration capability nor one universal Work order.

#### Occupied building retrofit

`SYSE.2` supplies the continuing building, the occupied-use claim, and a candidate concept through the occupied
region, safe-entry, egress, and essential-service interfaces. `C.30` and `C.32` supply candidate building zones,
service paths, interfaces, and load-bearing relations. Temporary access, work-area isolation, and construction
sequencing remain realization and WorkPlan questions.

The first unsupported branch is how a contractor System can reach and change the selected building region
while the occupied-use boundary and essential services remain supported. The candidate transformer System is
one contractor team. Access-equipment Systems remain separate resources or participating Systems unless their
relation to the team is independently established. The missing support is a capability claim under the occupied
configuration, access, isolation, load, and service-continuity conditions. The first WorkPlan item is a
contractor-capability and temporary-access investigation for those conditions.

If no admissible access arrangement remains, the engineer reopens the `C.32` comparison of zones, service
paths, placement, and interfaces. The engineer reassesses the linked occupied-use concept under `SYSE.2` if continuing occupancy or the use boundary must change. A
construction sequence is plan content; it is not the building concept, the changed building, or evidence that
the Work has occurred.

### SYSE.3:6 - Biases to Watch

Two recurring biases matter here. **Diagram-made feasibility** treats a product tree, schedule, or toolchain
description as proof that capable transformers and relations obtain; return to the first unsupported branch.
**Endless builder recursion** expands every dependency before choosing useful Work; recurse only when the added
branch changes the next action.

### SYSE.3:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-SYSE3-1` | A conforming use SHALL start from one named `C.30`/`C.32` architecture candidate or decision and SHALL state the selected structures and use for which realization feasibility matters. |
| `CC-SYSE3-2` | If required functioning has no candidate bearer, the practitioner SHALL reopen the bearer question under `A.6.F` and `C.32` rather than treating the missing architecture answer as realization Work. |
| `CC-SYSE3-3` | The first result SHALL name one unsupported realization branch, the proposed transformer System or unresolved need for one, the missing enabling condition, one next WorkPlan item, and the earlier answer to reopen if it fails. |
| `CC-SYSE3-4` | Intended change SHALL remain modal; an actual transformation claim SHALL satisfy `A.3.4`, and a not-yet-existing System SHALL use production and identity-inception claims rather than a fictional prior transformation. |
| `CC-SYSE3-5` | A proposed transformer-role assignment and capability SHALL remain plan or candidate content until `A.2.1` and `A.2.2` supply their direct results. |
| `CC-SYSE3-6` | The realization description and `A.15.2` WorkPlan SHALL remain different epistemes; neither SHALL be treated as performed Work, actual change, production, or an actual selected network. |
| `CC-SYSE3-7` | Recursion SHALL be added only when realizing a transformer System, capability, Method, tool, resource, or platform contribution changes the next action. |
| `CC-SYSE3-8` | `E.18` and `E.18.NET` SHALL be used only after their member, relation, constraint, endpoint-binding, and use-frame conditions are met; otherwise the result SHALL remain a Plain provisional realization-network description. |
| `CC-SYSE3-9` | Platform, organization, operations, portfolio, configuration, integration, authority, and assurance questions SHALL retain their specialist Methods and supply named results to this branch. |
| `CC-SYSE3-10` | A branch failure SHALL reopen only the smallest architecture, concept, use, or project-focus claim it can change; a local failure SHALL not reopen every earlier answer. |
| `CC-SYSE3-11` | `DesignRunTag` and flow valuation SHALL remain local to their leaf bindings; the result SHALL establish no global stage or lifecycle order. |

### SYSE.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Architecture realizes itself | A selected module or interface is treated as evidence that it can be produced, changed, integrated, or qualified. | Name one realization branch, transformer System, enabling condition, and the earlier claim to reopen if feasibility fails. |
| WBS as realization network | Work packages or schedule rows stand in for changed referents, transformer Systems, capabilities, and relations. | Keep the WorkPlan as intended Work and describe the realization dependency separately. |
| Transformation before existence | A future pump assembly, software deployment, or building configuration is said to change before it exists. | Name changes to pre-existing referents and use `A.15.PROD` for later identity inception and completion. |
| Creator hierarchy | Fixed developer, builder, producer, and operator levels replace case-specific transformer roles and recursive dependencies. | Recurse from the first unsupported branch without fixed levels; admit each System and assignment separately. |
| Universal platform pipeline | One toolchain or internal platform is prescribed for every engineered System. | Treat the named platform System and its capability, interface, availability, and change contribution as one possible branch. |
| Diagram-made network | Arrows labelled *builds*, *uses*, or *depends on* are treated as an actual `E.18.NET` structure. | Keep a provisional realization-network description until the member structures, obtaining cross-flow relations, endpoint bindings, constraints, and use frame are established. |
| Specialist absorption | Systems Engineering silently chooses organization structure, resource priority, configuration policy, safety argument, or platform Method. | Obtain the specialist result needed by the branch and keep its Method and decision with the specialist practice. |
| Restart every earlier decision | Any failed fixture, interface, or supplier result reopens project focus and all earlier decisions. | Reopen only the branch or architecture claim that the result changes; reopen a wider decision only when that answer also fails. |

### SYSE.3:9 - Consequences

Engineering participants gain an early feasibility result without waiting for a complete WorkPlan. One
unsupported branch becomes visible together with the System and Work needed to resolve it. Recursive
build-the-builder dependencies can be added where they change the next action, while architecture candidates
remain open to repair.

The cost is explicit incompleteness. A provisional realization-network description can contain unresolved
Systems, capabilities, Methods, relations, and specialist needs. Maintaining the distinction between that
episteme, a WorkPlan, and actual Work takes care, but it prevents planned or drawn dependencies from being
mistaken for physical feasibility.

### SYSE.3:10 - Rationale

Systems Engineering connects a proposed System to the Systems and Work that can make or change it. The systems
mantra keeps outside use, architecture, and transformer dependencies in view. In this pattern, engineers inspect
those dependencies toward the first unsupported branch and relate later observed Work and change through their
own facts. These are two views of the case, not one calendar sequence.

The recursive account is deliberately demand-driven. An exhaustive description of every supplier, tool, team,
capability, and possible dependency would be expensive and unstable. One unsupported branch plus one WorkPlan
item is already enough to change what the project does next. Further recursion is justified only by that next
decision.

### SYSE.3:11 - SoTA-Echoing

| Current practice line | What changes in this pattern | Source and use | Adoption status |
| --- | --- | --- | --- |
| Current manufacturing work links product architecture with process, resource, and capability choices and uses assembly or production infeasibility to revise design. | The Solution starts from a named architecture result, exposes one transformation-and-capability branch, and uses feasibility evidence to revise the architecture claim it changes. | Eichenwald et al. (2024), Ghanjaoui et al. (2024), and Meixner et al. (2024). These are manufacturing, aircraft-assembly, and cyber-physical-production studies with proposed ontologies, methods, prototypes, and small evaluations. | **Adopt and bound.** Use the product-process-resource-capability connection and architecture revision from feasibility evidence; select the receiving ontology, toolchain, and planning Method for the project. |
| Multi-project and portfolio research distinguishes precedence, resource contention, timing, uncertainty, interaction, and synergy rather than deriving them from common project membership. | A shared transformer or resource opens a separate operations or portfolio result only when the direct interdependency matters to the branch. Network position selects no priority. | Gómez Sánchez et al. (2023) and Vieira et al. (2024), both literature reviews over formal models and reported applications. | **Adapt.** Preserve typed interdependencies and let the receiving operations or portfolio decision establish its schedule, priorities, boundary, and participating Systems. |
| Continuous integration, delivery, CPS, and SRE practice uses frequent integration, automated and physical checks, feedback, and risk-sensitive change review in bounded technology settings. | A realization branch may request an integration or feedback result and revise the branch from it, while cadence, pipeline structure, release, and assurance remain local questions. | Current DORA capability pages; Thurgood's SRE error-budget example (2018); Zampetti et al. (2022) on ten CPS organizations and a 55-practitioner survey. | **Adapt narrowly.** Use frequent feedback where its engineering conditions fit; establish the local pipeline, cadence, automation boundary, and reliability policy separately. |
| Platform Engineering in technology work and platform-based manufacturing both treat shared Systems as enabling means whose usefulness depends on user tasks, interfaces, extensibility, and operating conditions. | A platform appears as one possible transformer or enabling branch with a named capability and interface contribution, not as a mandatory layer. | DORA, *State of AI-assisted Software Development*, report version 2025.2; Tolio et al., “Platform-based manufacturing” (2023). The evidence comes from technology work and manufacturing ecosystems and uses different platform lineages. | **Adapt and keep plural.** Evaluate the named platform contribution in its domain and establish the receiving organization, service relations, and platform design separately. |

These sources support particular realization branches. The common backward-to-first-gap, bounded recursion, and
local revision rule remains a synthesis of R5–R8 constrained by current FPF. No cited source establishes one
cross-profile recursive realization Method. Reopen the synthesis when broader comparative evidence changes
that common move or shows that a specialist Method belongs in another DPF.

### SYSE.3:12 — Relations

- A compatible `SYSE.6` architecture decision supplies only the selected structures, constraints, alternatives,
  accepted losses, and reopen conditions needed by this realization question. A compatible `SYSE.8` provider-
  arrangement account supplies only supported provider claims and design constraints that change a branch.
  Each use rechecks subject, configuration, use, horizon, evidence window, and availability; otherwise it uses a
  qualified direct source or records the missing result.
- `C.30` supplies the grounded architecture question and claims; `C.32` supplies candidate configurations over
  selected structures; `C.32.PAD` supplies a project architecture decision when that question is current.
  A missing architecture function bearer reopens the bearer question under `A.6.F` and `C.32`.
- `A.1.STM` keeps the outside-use, architecture, and realization questions in attention while the engineer finds
  the first unsupported answer and later relates observed Work and change through independently grounded facts.
  It supplies neither Work order nor an actual realization network.
- `A.2` supplies the local `TransformerSystemRole` kind; `A.2.1` supplies an obtaining assignment; `A.2.2`
  supplies holder-dependent capability and its envelope, measures, qualification window, and currentness.
  Candidate wording and WorkPlan content establish none of these facts.
- `A.15.2` supplies a WorkPlan for intended Work. `A.15.1` and `A.3.1` govern actual Work and enacted Method.
  `A.3.4` governs actual bounded change, and `A.15.PROD` governs subject-specific production results and
  completion claims when those distinct questions are current.
- `E.18` supplies one selected transformation-flow structure. `E.18.NET` supplies a selected network only after
  independent members, obtaining relation occurrences, endpoint bindings, constraints, and use frame are
  established. Before that boundary, keep a provisional description and name the missing discriminator.
- `SYSE.11` may use only the recursive realization arrangement from a compatible result for the same increment
  boundary. It does not perform Work, establish platform use or constituent commitments, or make the proposed
  System actual.
- Feasibility, integration, configuration, cost, delay, and evidence results can change the smallest branch,
  architecture, concept, use, or project-focus claim to which they apply. Platform Engineering, Organization Change,
  Operations, portfolio selection, configuration, safety, security, governance, law, finance, and other
  specialist practices retain their Methods and decisions.

### SYSE.3:End

<a id="syse-11"></a>
## SYSE.11 — Integrate a System for One Bounded Use

### SYSE.11:0 — Use This When

Use this pattern when locally completed items—such as parts, software, documents, tests, or bounded
changes—have accumulated, but no one can name one actual engineered System configuration that is usable for a
stated purpose and supported by current integration and operating evidence.

Begin by naming the actual System, its current configuration, one receiving use, and the smallest joint change
that could produce a usable next configuration. Perform the integration Work, observe the System in that
configuration during the named use, and state where the observations apply. The first useful result is a **bounded
usability assessment**: an episteme about the actual changed System, the Work and transformations that produced
its configuration, the supported use, evidence window, limits, and fallback. Any separately governed decision—
for example, assurance, permission, release, or future change—remains separately identified.

When several finite next changes remain, use `C.11.CRC` to compare what each realizable configuration adds or
loses relative to the current one, then use `C.11` for the next modernization choice. That comparison and choice
remain separate results; they do not become parts of the usable increment by being recorded nearby.

Use `SYSE.14` when the current question is authorization or release, `SYSE.4` when a load-bearing assurance claim
is current, and Operations Management when the problem is continuing queues, allocation, or operating control
rather than production of the engineering increment.

### SYSE.11:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| increment | A project-relative name for an identified actual System under one resulting configuration, selected for a receiving use. The same System, the transformations that changed it, and the configuration claims remain separately identified. |
| usable | A bounded claim that the System in this configuration supports one named use under declared conditions and evidence window. State broader claims—such as benefit, assurance, permission, release, reliability, or completeness—separately when the decision needs them. |
| integration | Dated Work that establishes the selected relations needed by the intended System configuration—for example, physical, software, interface, or operating relations. Each relation must independently obtain; a merge, assembly record, installation flag, or interface description can be evidence but is not that relation. |
| Work and transformation | An Agent performs dated Work by a Method. A transformation is the actual change of a continuing subject across time. Work can cause or participate in a transformation, but the two occurrences remain distinct. |
| actual configuration | The `SYSE.13`-governed structure and state-like claims about one identified actual System over an interval and under a reference scheme. A configuration description is the episteme carrying those claims, not the configured System. |
| modernization | Continuing engineering of an existing System through separately identified bounded changes and resulting configurations. The System's reidentification rule decides whether it continued or another System began. |
| MVP or continuous engineering | Source-local cues. Recover whether *MVP* means, for example, a market probe, demonstrator, or usable engineering configuration. For *continuous*, name the overlapping Work and actual changes intended by the source. |

The performing Agent, dated Work, enacted Method, actual transformation, changed System, description, use
observation, assessment, and deciding Agent remain different objects or relations.

### SYSE.11:1 — Problem Frame

Engineering Work often produces local completion before it produces a usable whole. A manufactured part can
match its drawing while failing an installed interface. Software can satisfy component-test conditions while, for
example, its controller interface, sensor relation, physical plant, operator procedure, or evidence basis remains
incompatible. A prototype can demonstrate one effect without supporting the configuration and operating envelope
needed by the next decision.

No one lifecycle or cadence governs all of these dependencies. Work on, for example, physical parts, software,
evidence, platforms, suppliers, configuration, and operation can overlap at different cadences.
Engineers select one bounded integration boundary, connect the contributing Work and transformations to it,
observe use, and return a result that can support the next decision without pretending the whole System is
complete.

### SYSE.11:2 — Problem

A claimed increment is not decision-usable until the responsible engineers can answer:

1. Which actual System and starting configuration are changing?
2. Which receiving use, operating conditions, affected Systems, and interval bound the result?
3. Which changes belong inside the increment—for example, physical, software, description, procedure, or
   interface changes—and which remain alternatives?
4. Which input results are needed—for example, results from realization, platform, constituent coordination,
   configuration, specialist, or authority Work—and were they available before the Work that relied on them?
5. Which Agents performed which dated Work by which Methods, and which actual transformations and relations
   obtained?
6. What integration and operating observations support usability, and what claims remain unsupported?
7. What fallback, stop, separate assurance or release decision, and later change can reopen the result?

Without these distinctions, *done* becomes a proxy for actuality. Engineers can ship incompatible parts,
overread a component test, confuse a release record with use, or keep adding features without producing a
configuration that anyone can use.

### SYSE.11:3 — Forces

- A small increment shortens feedback, while its use can still depend on relations outside the changed parts.
- Software and descriptions may change quickly; Work involving, for example, procurement, fabrication, access,
  integration, and physical observations often changes more slowly.
- Each contributor needs a local completion condition, but no local completion proves usability of the containing
  System.
- Some changes are easy to reverse; others alter scarce equipment, permits, safety conditions, or independently
  governed Systems.
- Automated tools can help Agents assemble records, compare configurations, and run checks rapidly, but syntax
  cannot choose the governed use, acceptable loss, or authority boundary.
- The receiving use needs a supported System configuration while engineers preserve alternatives for future
  change.

### SYSE.11:4 — Solution

Realize the smallest bounded change that leaves the actual System in a configuration supported for one named
use. Observe that use, state the limits of the result, preserve a fallback, and keep any next modernization choice
separate.

#### SYSE.11:4.1 — Perform the Move

1. **Name the System and use.** State the actual System, starting configuration, receiving use, affected Systems,
   operating envelope, interval, and deciding Agent.
2. **Choose the increment boundary.** Include only the changes whose joint actuality is needed for that use—for
   example, changes to physical parts, software, descriptions, procedures, or interfaces. Keep omitted changes,
   alternatives, and fallback visible.
3. **Check the required inputs at the time of use.** Use input results—for example, realization, platform,
   constituent-coordination, configuration, or specialist results—only for matching subjects, configurations,
   uses, horizons, and evidence windows. Close unsupported branches, replace them with qualified sources, or
   retain them as blockers. Evidence obtained from later Work cannot support an earlier input retroactively.
4. **State completion and evidence conditions.** For each included change, name the transformation, integration
   relation, resulting configuration claim, observation or test, unacceptable result, and stop. A planned check or
   tool status is not evidence.
5. **Perform Work and identify actual change.** Record the performing Agents, dated Work, assignments when
   relevant, enacted Methods, subjects, results, and evidence. Identify the actual transformations separately
   from Work and from descriptions of either.
6. **Integrate and observe.** Establish every relation needed by the selected configuration, including any
   required physical, software, interface, or operating relation. Observe the named use under the declared
   conditions; do not infer containing-System behavior from a component test without the needed correspondence.
7. **Assess usability narrowly.** State which use claim is supported for which configuration, conditions, and
   interval; name unsupported claims and the fallback. Obtain each separately governed assurance, permission,
   release, or specialist result when the receiving decision needs it.
8. **Choose later change only when needed.** If an option such as repair, extension, replacement, rollback, further
   observation, or no current change is justified by what it contributes, use `C.11.CRC` for the finite
   configuration comparison and `C.11` for the choice. Record the selected option, retained alternatives,
   evidence trigger, and claim that later observations can reopen.

This is an `A.22.CGUS` learning unfolding, not a calendar order. Work may overlap, but a decision can rely only
on results already established for its subject and conditions.

#### SYSE.11:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| System and use | Actual System, starting and resulting configurations, receiving use, affected Systems, conditions, interval, and deciding Agent. |
| increment boundary | Included transformations and integration relations, omitted alternatives, effectivity, fallback, and stop. |
| supplied inputs | Input results actually used—for example, realization, platform, constituent-coordination, configuration, or specialist results—their evidence windows, and any unresolved blocker or qualified substitute. |
| Work and actual change | Dated Work, performing Agents, assignments when relevant, Methods, subjects, direct results, transformations, obtaining relations, and resulting configuration claims. |
| usability | Use observations, supported claim, evidence window, limits, unsupported claims, and conditions for reconsideration. |
| separate decisions | Each assurance, permission, release, or other specialist result still needed by the receiving decision. |
| later modernization | Any `C.11.CRC` comparison and `C.11` choice kept as separate results, with alternatives, resources, reversibility, fallback, and reopen evidence. |

The assessment may cite supporting records such as configuration descriptions, Work records, trial results,
and evidence accounts. The actual changed System and its transformations remain separately identified.

#### SYSE.11:4.3 — What Changes in Practice

Engineers stop counting local completion as the engineering result. They integrate the actual System for one
named purpose, observe it in the resulting configuration, preserve the limits and fallback, and decide later
changes from that returned evidence rather than from a feature queue or lifecycle stage.

### SYSE.11:5 — Worked Case: A Flood-Pump Station Ready for Emergency Discharge

A municipal flood-pump station is operating in configuration C18. Municipal engineers need a configuration that
supports emergency discharge during the next flood-risk month. The bounded increment includes a replaced
discharge manifold, a controller package, and a changed sensor mapping. A proposed bearing-temperature sensor is
left outside the increment. C18 remains the fallback.

Before integration, the engineers check four inputs:

- a fabrication result shows that the supplier can make the positioning fixture and qualified weld for the
  selected material and geometry;
- the engineering platform is available in the configuration needed for controller integration and trial, based
  only on observations made before that Work;
- a temporary collector buffer is actually available under the municipality's notice arrangement; and
- the configuration description identifies the station and the effectivity of C18.

The first fabrication result had left the fixture-and-weld branch unsupported. Engineers did not treat the plan
as closed: they performed a feasibility investigation, obtained a fixture design and current capability evidence
for the toolmaking and welding cells, and revised the realization arrangement. Fabrication still had to produce
the actual fixture and manifold assembly; the descriptions and capability evidence were not those physical
Systems.

| Work | Actual subject and result |
| --- | --- |
| Fabricate the fixture and weld the manifold assembly. | Produces the physical fixture, the mounted manifold assembly, and inspection evidence for their stated completion conditions. |
| Integrate the controller package. | Produces integration evidence for the named controller, software, inverter interface, and sensor-mapping editions. This Work overlaps fabrication. |
| Integrate station configuration C19. | Installs the manifold and controller package and changes the sensor relations of the continuing pump-station System. The Work is distinct from the station's actual transformation from C18 to C19. |
| Run the emergency-discharge trial. | Produces observations of station C19, including discharge, controller behavior, buffer participation, and named failure conditions during the bounded trial. |

Under the station's configuration reidentification rule, the same station continues through the change because
its stable boundary, foundation, and pump train remain, while the manifold, controller, interfaces, and sensor
mapping change.

The manifold material undergoes another transformation during positioning, welding, cooling, inspection, and
rework. Shared time or subject does not make either Work occurrence identical to either transformation.

The trial supports use of C19 for the named emergency-discharge conditions and evidence window. It does not
establish all-season reliability, every flood load, release authority, or the benefit of the proposed bearing
sensor. If the temporary buffer relation were absent or stale, the trial and use claim would stop or narrow.

For the next modernization choice, the engineers compare keeping C19, adding the bearing sensor, collecting
another flood-load observation, and reverting to C18. The sensor option lacks qualified placement and maintenance
evidence, so its finite contribution relative to C19 is indeterminate rather than a scalar “sensor benefit.” A
`C.11` decision selects another observed-load window before deciding on the sensor. That decision record does not
perform the future observation Work.

The bounded usability assessment cites C19, the Work and transformations, integration and trial evidence, buffer
participation, use limits, fallback, and reopen conditions. It can become evidence for `SYSE.4`, but it is not an
assurance conclusion, permission, release, or next modernization choice.

**Countercase.** A document bundle is approved while no actual configuration, integration Work, transformation,
or use observation exists. The missing objects and relations should be named; the bundle should not be renamed
an increment.

### SYSE.11:6 — Bias Annotation

Stage-gate sources can mistake a passed gate for an actual integrated System. Software practice can make the
same error with, for example, a merge, sprint, deployment, or fast cadence. Physical engineering can make the
opposite mistake and delay every feedback loop until a large assembly exists. Choose the smallest boundary that
produces decision-relevant use evidence for the actual System.

Institutional status and labels supplied by, for example, vendors, tools, or standards can support particular
claims, but they do not establish actual integration or use. Automation can support bounded Work and checks; the
receiving Agent still selects the use and any authority relation remains separately supported.

### SYSE.11:7 — Conformance Checklist

- [ ] One actual System, starting configuration, bounded use, conditions, interval, and deciding Agent are named.
- [ ] The increment boundary, omitted alternatives, fallback, and stop are explicit.
- [ ] Each supplied input result, including any realization, platform, coordination, configuration, or specialist
      result used in the case, matches the subject, use, horizon, and evidence window and was available before the
      Work that relied on it.
- [ ] Performing Agent, Work, Method, result, transformation, configuration description, actual System, and use
      observation remain distinct.
- [ ] Integration and operating observations support a use claim for the containing System, not only its parts.
- [ ] Separately governed decisions, including assurance, permission, release, operation, and specialist
      decisions used in the case, remain separate.
- [ ] A later modernization comparison and choice are recorded as `C.11.CRC` and `C.11` results, not as actual
      change or future Work.
- [ ] Reopen conditions name the configuration, use, evidence, dependency, or relation whose change matters.

### SYSE.11:8 — Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| Treat a sprint, merge, release, or document bundle as the increment | Identify the actual System, configuration, Work, transformation, and use evidence. |
| Infer whole-System usability from a component test | State the part–whole and configuration correspondence and observe the containing System in the named use. |
| Treat platform availability as platform participation | Separate pre-use capability and condition claims from actual participation or provision Work and later evidence. |
| Put every change into one cadence | Choose the smallest joint integration boundary and preserve the different physical, software, evidence, and authority cadences. |
| Treat modernization as feature accumulation | Compare repair, observation, replacement, rollback, extension, and no current change. |
| Treat a decision record as actual change | Keep decision Work and its result separate from later change Work and transformation. |

### SYSE.11:9 — Consequences

This move shortens feedback to actual System use and exposes incomplete integration. It requires configuration,
Work, transformation, evidence, and fallback records proportionate to the decision. A boundary chosen too narrowly
can hide whole-System effects; one chosen too broadly can delay learning. The use claim and reopen conditions make
that tradeoff revisable.

### SYSE.11:10 — Rationale

An engineered System changes through actual Work and transformations, not through completion labels. A bounded
increment exposes compatibility and use evidence before a larger commitment. Continuing modernization preserves
the System's temporal identity and repeatedly returns evidence to engineering decisions without importing a
lifecycle or software-only cadence.

### SYSE.11:11 — SoTA and Source Use

| Source line | Adopted contribution | Limit retained |
| --- | --- | --- |
| `SRC-SEBOK-APPLY-2026` | Concurrent, iterative, recursive application and successive evolutionary solutions. | The source keeps older lifecycle and requirements framing and does not establish comparative SoTA. |
| `SRC-CI-CD-CPS-SRE-2018-2026` | Frequent integration, automated and physical checks, feedback, and risk-sensitive review in bounded software/CPS settings. | No universal cadence, pipeline, complete automation, or removal of independent assurance transfers. |
| `SRC-CONTINUOUS-RE-COMPLIANCE-2023-2025` | Requirements, traceability, monitoring, models, and compliance Work continue during rapid change. | Software/CPS-heavy evidence does not establish one requirements phase or Method. |
| `SRC-PPR-ARCH-WORK-2024` | Product, process, resource, capability, and architecture evidence return during manufacturing and assembly planning. | Small proposed methods and cases do not establish one cross-domain PPR ontology or toolchain. |

R5–R8 supply the engineering move from completed parts to bounded integrated use. Current sources refine the
move but do not prove field prevalence or causal superiority. Reopen when comparative evidence changes the
cross-domain integration boundary or when an application profile needs a different specialized Method.

### SYSE.11:12 — Relations

- A compatible `SYSE.3` result supplies only the realization arrangement needed by this increment. Every relied-
  on unsupported branch must be closed, replaced by a qualified result, or retained as a blocker before Work
  uses it.
- A compatible `SYSE.12` result supplies pre-use platform capability and condition claims. Later participation or
  provision Work produces later evidence and cannot justify the earlier input retroactively.
- A compatible `SYSE.18` result supplies an obtaining coordination relation and its commitments and limits. It
  supplies no constituent output or borrowed authority. `SYSE.13` supplies configuration and effectivity claims
  for the same Systems and use.
- `A.15.1`, `A.2.1`, and `A.3.1` distinguish Work, assignment, and enacted Method. `A.3.4` distinguishes actual
  transformations, and `A.15.PROD` governs claimed result production.
- `C.11.CRC` constructs a finite contribution comparison when a proposed change's contribution relative to the
  current configuration is not already explicit. `C.11` governs the next choice. Neither result is the later Work
  or transformation.
- A bounded usability assessment can inform `SYSE.4` only within its supported use and evidence window. `SYSE.14`
  retains release and evidence-continuity authority.
- Operations, Maintenance, Platform Engineering, safety, security, law, governance, finance, and other specialist
  practices retain their Methods and decisions.

### SYSE.11:End

<a id="syse-12"></a>
## SYSE.12 — Develop an Engineering Platform for Practitioner Work

### SYSE.12:0 — Use This When

Use this pattern when engineers cannot reliably model, compute, build, integrate, test, release, or observe an
engineered System because shared enablers—such as tools, data, models, automated or physical facilities, provider
Work, and support arrangements—are treated as incidental infrastructure or as a product with no named
practitioner Work.

Begin with one practitioner Work family and the engineering result it must produce. Identify the actual Systems
that enable or obstruct that Work, the capability practitioners need, the capability claimed for each platform
or provider System, the conditions under which those Systems participate or provide a result, and the burden or
failure that should change. Then choose the smallest platform change that can improve the engineering result.

For a decision made before the relying Work, the Agent performing platform-assessment Work applies this
pattern and records a **platform readiness assessment** based only on evidence already available. After
practitioner Work, the responsible Agent performs a second assessment and records a **platform-use assessment**
based on observed participation, provision, burden, failure, and engineering results.
Both assessments are epistemes. Each names the System, capability, Work, relation, result, and evidence it is
about without replacing any of them. The later assessment can revise later reliance but cannot retroactively
support the earlier assessment.

Use Organization Change Engineering when positions, assignments, authority, or organization architecture are
the changed subject; Operations Management for continuing queues, support cases, capacity, and provider Work;
and an application-profile DPF when a specialized platform—such as a laboratory, compiler, manufacturing cell,
clinical environment, electrical bench, or ship facility—changes the working move.

### SYSE.12:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| practitioner | An Agent performing the named engineering Work. Capability, assignment, authority, and actual Work remain separate claims. |
| engineering platform | A project-relative designation for an actual System selected to enable named engineering Work through direct relations such as capability, participation, provision, resource, interface, or condition relations. A future candidate remains a referent in a plan or description until an actual System satisfies its identity conditions. |
| provider arrangement | Plain wording for the provider Agents, other Systems, Work, Methods, interfaces, resources, conditions, and recovery relations on which platform use relies. Recover the actual participants and relations; they need not be parts of one platform System. |
| toolchain | Source-local wording that may denote an actual arrangement of tools or a description of that arrangement. Recover the actual Systems, configurations, interfaces, resource relations, participation in Work, and evidence before making a platform claim. |
| self-service | A source-local claim that a practitioner can obtain a stated result without case-specific provider Work at every step. Provider Work, platform participation, support, authority, conditions, and exceptions can still remain. |
| golden path | Source-local wording for either a recommended MethodDescription or a configured arrangement for a bounded case. Recover which one is meant; either remains separate from the world-side Method, its enactment, and evidence that it fits this Work. |
| practitioner-experience account | An episteme carrying evidence-backed claims about, for example, effort, delay, error, rework, recovery, autonomy, or result quality for named Work. A satisfaction result supports only the claim and population it measured. |
| platform readiness assessment and platform-use assessment | The readiness assessment uses evidence available before the relying Work. The use assessment uses later observations of that Work and the platform's actual participation or provision. They are different epistemes with different evidence windows. |

The platform System, provider Agent, practitioner Agent, capability, promise content, Method, MethodDescription,
dated Work, participation or provision relation, condition, result, and evidence remain distinct. When a source
says *service*, recover which of these objects or relations its current claim needs.

### SYSE.12:1 — Problem Frame

Engineering results depend on more than the architecture of the project system-of-interest. Systems such as
model repositories, simulation and calculation environments, manufacturing cells, test benches, configuration
and evidence stores, AI assistants, integration environments, and data spaces can change what engineers can
observe and do. Provider and support arrangements can do the same. One platform can help one Work family and
obstruct another.

Buying tools or forming a platform team does not establish an enabling System. Useful platform engineering starts
with practitioner Work and consequences for the project system-of-interest or its use, then develops the actual
enabling arrangement. Platform Work and engineering Work on the project system-of-interest may occur
simultaneously; their dependency is not a lifecycle stage or evidence that one System is part of the other.

### SYSE.12:2 — Problem

A decision about an engineering platform requires answers to seven questions:

1. Which practitioner Agents, Work family, Method, result, configuration, and interval are being served?
2. Which actual Systems, provider Agents, interfaces, resources, and configurations form the current enabling
   arrangement, and which future candidates exist only in plans or descriptions?
3. What capability does the practitioner need, which System holds each claimed platform or provider capability,
   and under what envelope and currentness conditions?
4. Which conditions and direct relations actually matter—for example, access, participation, provision,
   availability, resource use, promise, support, exception, or fallback?
5. Which practitioner or System consequences should change—for example, effort, delay, error, rework, recovery,
   evidence continuity, or a result involving the project system-of-interest?
6. Which credible complete arrangements form the current decision alternatives—for example, retaining, changing,
   composing, obtaining, building, branching, bypassing, or retiring—and who has authority to choose among them?
7. What can be supported before practitioner Work, what is observed only later, and what change reopens each
   assessment?

Without these distinctions, platform teams can optimize adoption, ticket closure, or local automation while
moving integration burden to practitioners, concentrating failure, and degrading the engineering result.

### SYSE.12:3 — Forces

- Shared capabilities and provider Work reduce duplication, while different engineering profiles need different
  interfaces, evidence, and physical means.
- Case-independent access can shorten feedback, while consequential changes still require separate permission
  and assurance.
- Recommended arrangements reduce routine burden, while novel Work needs extension, bypass, and exception
  conditions.
- Automation lowers repeated effort, while hidden automation can erase provenance, uncertainty, or recovery.
- Practitioners need stable participation and provision, while Systems designated as project systems-of-interest, Methods,
  descriptions, and evidence demands keep changing.
- A maintained platform needs product care, but platform-local metrics cannot replace practitioner results or
  results involving the project system-of-interest.

### SYSE.12:4 — Solution

Develop the smallest actual enabling arrangement that improves one named practitioner Work result. State the
capability, conditions, participation or provision relations, and evidence separately, then evolve the platform
from observed use rather than from a tool list or platform brand.

#### SYSE.12:4.1 — Perform the Move

1. **Name practitioner Work and result.** State the practitioner Agents or inclusion rule, Work family, Method,
   subject, expected result, current configuration, interval, and receiving decision.
2. **Recover the current enabling arrangement.** Identify actual Systems—such as tools, model or data stores,
   compute resources, AI assistants, laboratories, manufacturing cells, integration environments, evidence
   stores, or support Systems—only where their relations change the Work. Name provider Agents, interfaces,
   resources, conditions, and failures.
3. **Separate capability holders.** State the capability demanded of practitioners and the holder, Work family,
   envelope, measures, qualification window, currentness, and evidence for each platform or provider capability.
   Support each capability claim with evidence that bears on the named holder performing the Work family in
   that envelope. Administrative or descriptive records count only when their evidence relation supports that
   claim.
4. **State conditions and direct relations.** Name the conditions that bound the claim—for example, access,
   configuration, performance, evidence continuity, support, exception, fallback, cost, or resource conditions.
   Then state each direct relation used by the decision: platform participation in Work; production of a named result by a named Work occurrence; supply of the result or access to it from a named provider to a named receiver; receipt or use by that receiver; resource availability or use; applicable promise content; or another governed relation.
5. **Use Method repertoire and architecture when they change the choice.** A compatible `SYSE.15` result can
   supply available Methods and applicability limits; a compatible `SYSE.20` result can supply Method, Work,
   enablement, and conflict structures. Otherwise use a qualified source or name the missing result.
6. **Generate and choose among real alternatives.** Build a `C.11` option set from feasible complete
   arrangements. Candidates may retain the current arrangement, change a capability or relation, compose existing
   Systems, obtain or build a part, branch for a profile, preserve a bypass, or retire a harmful arrangement. Name
   the deciding Agent, authority, accepted losses, and questions outside that authority.
7. **Perform bounded platform-development Work.** Record performing Agents, assignments when relevant, Methods,
   temporal extents, results, actual transformations, resulting configuration, and evidence. A decision record
   does not change the platform.
8. **Issue the pre-use readiness assessment.** State only capability and condition claims supported before the
   practitioner Work, with their evidence cutoff, currentness window, limits, fallback, and stop.
9. **Observe use and issue a later assessment.** Identify the practitioner Work occurrence and the actual
   platform participation, provision Work, or resource relation. Observe the consequences needed by the
   decision—for example, burden, delay, error, rework, recovery, evidence continuity, or results involving the
   project system-of-interest. Record the later assessment separately and use it only for later decisions.
10. **Return and reopen locally.** Supply only the supported claims needed by each receiving decision—for
    example, capability, condition, participation, provision, use, failure, or platform-change claims. Reopen only
    the claim affected by a changed Work, Method, practitioner population, configuration, provider, condition,
    evidence basis, or consequence for the project system-of-interest.

This is an `A.22.CGUS` learning unfolding, not a calendar sequence. Platform development, practitioner Work,
support, change of the project system-of-interest, and evidence Work can overlap. Every claimed use still needs
an obtaining relation, and later evidence cannot make an earlier input self-supporting.

#### SYSE.12:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| practitioner use | Agents or population, Work family, Method, subject, result, configuration, interval, and receiving decision. |
| platform and providers | Actual platform System and selected parts, provider Agents and Systems, interfaces, resources, configurations, and future candidates kept as plan or description content. |
| capabilities | Practitioner capability demands and each platform or provider capability holder, Work family, envelope, measures, qualification window, currentness, and evidence. |
| conditions and relations | Conditions used by the case, such as access, performance, evidence continuity, support, exception, fallback, cost, or resource conditions; each relied-on participation, provision, availability, resource-use, promise, or other governed relation. |
| alternatives and change | Current `C.11` OptionSet of complete arrangements; deciding Agent, authority, accepted losses, selected option, platform-development Work, transformation, configuration, and evidence. |
| pre-use readiness | Claims supported before practitioner Work, evidence cutoff, currentness window, limits, fallback, and stop. |
| observed use | Practitioner Work, actual participation or provision, burden and result observations, later assessment identity, and the decision it can change. |
| return and reopen | Claims supplied to each receiving decision, their limits, and the change that reopens each one. |

#### SYSE.12:4.3 — What Changes in Practice

Platform investment begins with an engineering result and observable practitioner Work rather than a tool list
or team charter. Engineers can improve a shared enabling System while keeping capability, Work, participation,
evidence, operations, organization change, administration, application-profile engineering, and decisions
about the project system-of-interest distinct.

### SYSE.12:5 — Worked Case: Platform Support for Flood-Pump Integration

Engineers integrating a flood-pump controller must reconcile identifiers among the model build,
hardware-in-the-loop bench, controller configuration, and evidence repository by hand. One missed link delays
the station integration result and makes recovery difficult.

The actual engineering platform includes the model-build System, bench, and evidence repository in configuration
C4. A support Agent provides recovery Work but is not made a part of the platform merely by supporting it. A
platform description records the structure; it is not the platform System.

The engineers compare five alternatives: retain manual reconciliation, add configuration-and-evidence links,
replace the bench, obtain bounded evidence-provision Work from another provider, or keep automation bypassed by
the manual fallback. The Agent authorized to make the platform decision selects the linking change because it
preserves the current integration Methods and fallback while reducing a known source of mismatch. The decision
record does not change the platform.

A platform-engineering team configures identifier bindings, repository links, and recovery hooks. This dated Work
is distinct from the actual transformation of the continuing platform from C4 to C5 and from the evidence that
describes the change. A support Agent then performs a recovery exercise.

The readiness assessment, issued after the exercise and before controller integration, states that:

- C5 is current;
- the bench and repository are available in their named configurations;
- the configuration-and-evidence links passed the checks already performed;
- the manual fallback remains executable; and
- automated repository export remains unsupported and blocks only Work that needs automated export recovery.

During later controller-integration and flood-discharge trial Work, engineer Agents use the C5 platform while
its model-build, bench, and evidence-store Systems provide their named functions. The observed relations support
platform participation in those Work occurrences; they do not assign the engineers' Work to the equipment. The
supplier's fixture-fabrication Work uses another arrangement, so the same participation claim does not apply
there.

The later use assessment records that evidence assembly for controller integration fell from the stated local
baseline of six person-hours to two and a half, while a repository outage took 45 minutes to recover and the
export gap remained. These constructed observations support only this case. They can change later platform
decisions, but they cannot retroactively justify the earlier controller-integration reliance.

**Countercase.** A repository and continuous-integration server are installed, but no practitioner Work,
participation, provision, or engineering result is observed. Record the installed Systems and the proposed
enabling arrangement; do not infer platform capability or adoption from installation.

### SYSE.12:6 — Bias Annotation

Software platform practice supplies useful ideas about self-service, configured defaults, fast feedback, and
product care. Vendor catalogues and team-topology literature can also make a tool or team appear to be the whole
platform. Physical and cross-domain engineering adds other platform participants—for example, laboratories,
manufacturing cells, configuration and calibration Systems, evidence stores, provider Work, and recovery
arrangements.

Signals such as publicity, university coverage, procurement, installation, usage counts, or satisfaction support
only the claim they actually measure. When broad prevalence or causal effect cannot be measured affordably, use
the best available case evidence and state its epistemic status.

### SYSE.12:7 — Conformance Checklist

- [ ] Practitioner Agents or population, Work, Method, result, configuration, interval, and receiving decision are
      named.
- [ ] Platform System, provider Agent, practitioner Agent, capability, promise, MethodDescription, Method, Work,
      participation or provision relation, condition, result, and evidence remain distinct.
- [ ] Capability holders and envelopes are supported, and each direct relation states its participants and
      conditions.
- [ ] Alternatives include retaining the current arrangement, a bounded change, a branch or bypass, and stopping
      or retiring where credible; authority and accepted losses are explicit.
- [ ] Platform-development Work, actual transformation, resulting configuration, and evidence remain distinct.
- [ ] A readiness assessment uses only evidence available before practitioner Work.
- [ ] A later use assessment identifies actual participation or provision and cannot justify the earlier reliance
      retroactively.
- [ ] Practitioner burden, recovery, evidence continuity, and results involving the project system-of-interest
      can reopen the smallest affected platform claim.

### SYSE.12:8 — Common Failures and Repairs

| Failure | Repair |
| --- | --- |
| Treat a tool list as the platform | Identify actual Systems, selected structure, capability holders, interfaces, resources, configurations, and participation or provision relations. |
| Treat a platform team as the platform System | Identify the Agent performing platform Work and the changed enabling System separately. |
| Treat availability as use | Identify the practitioner Work occurrence and the obtaining platform-participation or provider-work relation with dated evidence. |
| Use later evidence to justify earlier reliance | Keep the pre-use readiness assessment and later use assessment separate, with their evidence windows and update relation. |
| Treat satisfaction or adoption as engineering value | Observe the practitioner and project-system consequences that matter to the decision, such as effort, delay, error, rework, recovery, evidence continuity, or an engineering result. |
| Treat a golden path as the Method | Separate MethodDescription, world-side Method, enactment, fit evidence, and bypass conditions. |
| Let the platform provider decide matters outside its authority | Return each decision—such as practitioner assignment, release of the project system-of-interest, assurance, organization, or operations—to the Agent authorized for it. |

### SYSE.12:9 — Consequences

This move exposes hidden enabling dependencies and practitioner burden and can reduce repeated integration and
evidence Work. It also adds continuing Work to maintain, support, configure, observe, and recover the platform.
Shared capabilities can also create coupling, provider monopoly, or failure concentration, so profile branches
and fallbacks preserve alternatives where those risks matter.

### SYSE.12:10 — Rationale

Engineering capability is a holder's ability to perform a named Work family or produce a result class within a
declared envelope, measure set, qualification window, and currentness condition. A chosen Method may constrain
that envelope or be tested for fit, but it is not the capability's target. A platform is useful only through
actual relations to practitioner Work. Treating it as an engineered System permits architecture, configuration,
evidence, use, and evolution claims without turning one organization, team shape, or software lineage into a
universal form.

### SYSE.12:11 — SoTA and Source Use

| Source line | Adopted contribution | Limit retained |
| --- | --- | --- |
| `SRC-DORA-2025` | Platform user experience, task-outcome feedback, extensibility, practitioner independence, and coexistence of gains with instability. | Technology-work survey and qualitative evidence does not establish a cross-domain platform organization or causal dominance. |
| `SRC-TOLIO-PBM-2023` | Manufacturing platforms include networks, physical and digital Systems, data spaces, and user/provider decisions. | A manufacturing ecosystem is not an internal developer platform or one universal provider arrangement. |
| `SRC-PPR-ARCH-WORK-2024` | Product, process, resource, capability, and architecture links provide physical-engineering Work and evidence demands. | Proposed ontologies and small cases do not establish one platform architecture or toolchain. |
| `SRC-BANTWAL-ECM-2026` | A bounded engineering-change case connects product descriptions, supply constraints, CAD/CAE, ERP/PLM, and validation. | One proposed brake-caliper case is neither field prevalence nor one generic consistency Method. |

R6 and R8 supply the cross-domain engineering-platform problem. Sources show heterogeneous technology and
manufacturing arrangements; this pattern keeps only the invariant relation to named practitioner Work. Reopen
when a later comparative source changes that invariant or an application profile establishes a different first
result.

### SYSE.12:12 — Relations

- A compatible `SYSE.15` result supplies a bounded Method repertoire and applicability limits; it neither selects
  nor enacts the platform Method.
- A compatible `SYSE.20` result supplies Method, Work, enablement, and conflict structures; it neither turns an
  enabling dependency into a level nor selects the platform change.
- `A.2.2` governs holder-dependent capability. `A.6.P:4.11a` recovers *service* wording into promise, capability,
  bearer, dated Work, participation or provision relation, condition, and evidence claims without creating a
  generic service object.
- `A.15.1`, `A.2.1`, and `A.3.1` distinguish Work, assignment, and enacted Method. `A.3.4` distinguishes actual
  transformation, `A.15.PROD` claimed result production, and `A.22` descriptions of selected platform structure.
- `SYSE.11` may use a readiness assessment only for capability, conditions, and participation or provision
  claims supported before its Work. A later use assessment updates later decisions and cannot support that input
  retroactively.
- Neighboring DPFs retain their own Methods and decisions. These include Organization Change, Operations,
  Administration, application-profile engineering, security, safety, law, finance, procurement, and governance
  whenever the current question belongs there.

### SYSE.12:End

<a id="syse-18"></a>
## SYSE.18 — Integrate Systems Governed by Different Agents

### SYSE.18:0 — Use This When

Use this pattern when one use depends on several actual Systems, but decisions that can change that use—for
example, a constituent's operating condition, configuration, commitment, interface, or later modification—belong
to different Agents. The integrating Agent cannot command every change that can defeat the use, and the phrase
*system of systems* explains nothing by itself.

Begin with the shared use and the actual constituent Systems that can defeat it. For each constituent, state how
it affects that use, who can decide the relevant change, what authority that Agent has, and which configuration,
interface, commitment, evidence, or withdrawal condition the decision relies on. Then compare only the
coordination changes that the relevant Agents can actually decide.

The first useful result is a **bounded constituent-integration decision**. It states the selected change or stop,
the deciding Agent's authority, decisions required from other Agents, accepted losses, unsupported dependencies,
and next Work. If integration Work is later performed, identify that Work, its actual transformation or newly
obtaining relation, and the observed-coordination claim separately from the decision episteme.

Use ordinary architecture and integration patterns when one deciding Agent controls every constituent change
that can alter the use. Use the neighboring practice that owns a different question—for example, Organization
Change when an organization is the System being changed, Corporate Governance for ownership and governing-body
decisions, Operations Management for continuing allocation and coordination Work, or a configuration or other
specialist pattern for its own subject.

### SYSE.18:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| shared use | One named result or use whose conditions depend on several Systems. Any hierarchy or whole–part claim needs its own relation. |
| constituent System | An independently identified actual System whose participation, result, failure, change, or withdrawal can alter the shared use. *Constituent* names that use-relative relation; state any proper-part relation separately. |
| independently governed | A decision relevant to the use—for example, a commitment, operating choice, configuration change, or withdrawal—is controlled outside the integrating Agent's authority. Independence is claim-sized, not absolute. |
| system of systems | A source or domain label that prompts recovery of the actual Systems and relations relevant to the shared use. Classify those Systems and relations directly rather than treating the label as a universal kind. |
| interoperability | The evidence-backed ability of named Systems, under a stated configuration and conditions, to exchange results through identified interfaces and make those results usable for the shared use. Interface descriptions are epistemes about this ability, not participants in the exchange. |
| commitment | An obtaining duty relation with a bearer, referents, scope, validity, governing rule, and instituting basis. Record its content, later Work, delivered result, and evidence of fulfilment as separately grounded claims. |
| constituent-integration decision | The episteme that selects one bounded coordination alternative within stated authority and records outside decisions, unsupported dependencies, next Work, and reopen conditions. |
| observed-coordination claim | A later evidence-backed claim that named Systems coordinated for the shared use under stated configurations and conditions. Record the earlier decision, performed Work, commitments, observation, and claim interval separately. |

A System described, for example, as an owner, operator, integrator, supplier, or decision maker is an Agent only
when the agency claim is warranted. State the direct predicate and participants for every relied-on claim. Use the
applicable pattern when the decision depends on agency, authority, a commitment, performed Work, capability, or
evidence; state constituent participation and the shared use separately.

### SYSE.18:1 — Problem Frame

For example, district drainage can depend on separately governed pump stations, gates, drainage networks,
dispatch Systems, provider organizations, and public infrastructure. A product can likewise depend on independently
evolving software, communication, payment, and energy Systems or regulatory organizations. Each constituent can
remain useful elsewhere and change for reasons outside the integrating project.

Drawing a larger boundary does not create authority or interoperability. A model or interface description can
carry claims. An agreement can institute a commitment. A meeting is Work. A governing body is a System whose
participating Agents may make authorized decisions. For constituent Work, identify its performing Agent; for
another Agent's decision, identify that Agent's authority.

### SYSE.18:2 — Problem

An integrating team needs answers to seven practical questions:

1. Which shared use, conditions, interval, and engineering decision are at issue?
2. Which actual Systems can defeat the use by changing, failing, withdrawing, or withholding a result?
3. Which direct relation connects each System to the shared use, and what does that relation change?
4. Which Agent controls each relevant decision, and what authority, permission, or escalation relation obtains?
5. Which configurations, interfaces, capacities, timings, commitments, and evidence make coordination possible?
6. What can the integrating Agent change, and which decisions must come from other Agents?
7. What actual observation would show that the changed arrangement works for this use?

Missing answers produce four recurring errors: interface syntax is mistaken for interoperability, an agreement
for performance, a constituent label for parthood, or an integration team for authority over Systems it does not
govern.

### SYSE.18:3 — Forces

Recurring tensions include:

- The shared use needs coherent results; constituents retain other uses, priorities, owners, and decision centres.
- Integration benefits from stable interfaces and commitments; Systems and environments continue to change.
- Receiving decisions need comparable evidence; every source keeps its provenance, limits, and authority.
- One Agent can compare shared-use options while several Agents separately permit constituent changes.
- Some coordination can be agreed in advance; operating conditions can require continuing reconfiguration.
- A broad account reveals dependencies, while the current decision must remain feasible within actual authority.

### SYSE.18:4 — Solution

Recover the constituent arrangement from the shared use, make distributed decisions and dependencies explicit,
and choose one bounded change without claiming control over the whole field.

#### SYSE.18:4.1 — Perform the Move

1. **Name the shared use and decision.** State the result, use interval, conditions, constituent Systems, and the
   Agent authorized to make the current integration decision.
2. **Identify actual constituent Systems by consequence.** Include a System only when a stated consequence of
   its condition or behavior—for example, participation, a supplied result, failure, change, or withdrawal—can
   alter the shared use. Keep a future candidate as an intended System referent in plan or decision content until
   it exists and can be recognized.
3. **State the relied-on relation.** For each constituent, say in ordinary language how its behavior, state, result,
   or availability changes the shared use. Then apply the pattern that governs the actual relation—for example, a
   transformation, performed Work, commitment, capability, transfer, interface, availability, or evidence relation.
   Use a separate predicate for each unlike claim.
4. **Recover decisions and authority.** For every choice that can alter the use, identify the deciding Agent,
   assignment when relevant, direct authority or permission, conflict, and escalation. Compare the actual decision
   centres and feedback; neither centralization nor decentralization is beneficial by label.
5. **Check commitments, interfaces, configurations, and evidence.** Record each commitment, later Work, delivered
   result, interface description, actual exchange, and fulfilment evidence as its own claim. State the relevant
   conditions used by the decision—for example, notice, withdrawal, capacity, timing, recovery, or currentness.
6. **Generate feasible coordination alternatives.** Consider alternatives such as retaining the arrangement,
   changing an interface or commitment, adding a mediating System, buffer, or fallback, replacing a constituent for
   this use, narrowing the use, or stopping. Preserve alternatives that require decisions from different Agents.
7. **Choose within actual authority.** Record the selected alternative, deciding Agent, authority, accepted losses,
   decisions still required elsewhere, unsupported dependencies, authorized next Work, and the observation that
   would justify reliance on the changed arrangement.
8. **Perform and observe only when authorized.** If integration Work occurs, identify the performing Agent, Method,
   dated Work, actual transformation or newly obtaining relation, resulting configuration, and evidence. Use a
   representative occurrence to support only the coordination claim actually observed.

The numbered presentation is an `A.22.CGUS` learning unfolding, not a required sequence for constituent Work.
Constituent operation, engineering, governance, and integration can be simultaneous; only stated dependencies and
temporal relations establish order.

#### SYSE.18:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| shared use | Result or use, conditions, interval, affected Systems, current decision, and deciding Agent. |
| constituent Systems and relations | Actual Systems, configurations, other uses, reasons for inclusion, and one direct relation or stated gap for every relied-on contribution or constraint. |
| decisions and authority | Ownership and other governing relations, deciding Agents, assignments when relevant, authority, permissions, conflicts, escalation, and decision-centre boundaries. |
| commitments and interoperability | Commitments with bearers and conditions; interfaces, capacities, timings, actual exchange or use evidence, notice, withdrawal, and failure-recovery conditions. |
| alternatives and choice | Considered feasible coordination alternatives; selected alternative and selection basis; deciding authority, accepted losses, outside decisions, unsupported dependencies, and next Work. |
| later integration, when current | Performing Agent, Method, dated Work, actual change or newly obtaining relation, resulting configuration, representative observation, and evidence limits. |
| decision use and reopen | Decision contribution supplied to next Work; separately supported observed-coordination claim when available; fallback, gaps, and claim-sized reopen conditions. |

The first useful decision does not wait for implementation. A later observed-coordination claim does not rewrite the earlier choice into performed Work or prove that every
constituent commitment was fulfilled.

#### SYSE.18:4.3 — What Changes in Practice

Engineers stop using *system of systems* as an explanation. They can name which Systems matter, what each Agent
can decide, what the integration Agent can change, which dependencies remain unsupported, and what observation
is needed before the shared use may rely on the changed arrangement.

### SYSE.18:5 — Worked Case: Emergency Discharge Across Four Independently Governed Systems

Emergency discharge in one district depends on four actual Systems:

- a flood-pump station, whose configuration and release are decided by the station-owner organization;
- an upstream gate System, whose schedules and overrides are decided by the river-control agency;
- a municipal drainage network, whose capacity commitments and outage notices are decided by the municipal
  operator organization; and
- an emergency-dispatch System, whose regional agency decides which acknowledgement and escalation Methods
  are used.

The four Systems contribute to one use. Company membership and whole–part relations require separate evidence.
The current configuration and interface evidence supports pumping, gate scheduling, network reception, and
dispatch acknowledgement under stated loads and conditions. Four separate commitments bind named Agents under
conditions concerning station configuration, the gate envelope, drainage capacity, and dispatch availability. Later
Work and delivered results require their own evidence.

A tabletop exercise exposes one material mismatch: the municipal operator commits to four hours of outage notice,
while the station fallback needs six. The integration Agent has authority over a station-side buffer and the existing dispatch escalation condition.
The municipal operator retains authority over the notice commitment.

The current options are to accept the two-hour gap, add a temporary buffer, request a changed municipal
commitment, narrow the discharge use, or stop the increment. The integration decision selects a temporary
two-hour buffer plus dispatch escalation while leaving the municipal commitment unchanged. The decision records
the external commitment request as a separate possible improvement, not as an accomplished change.

An integration team later installs a mobile buffer System. Identify the installation Work, installed buffer,
installation evidence, and newly obtaining buffer-availability relation separately. A representative exercise
supports that the buffer absorbs the stated two-hour load and that dispatch acknowledges and escalates under the
tested condition. The observation is limited to that load and interval; constituent commitments keep their
previous values.

The decision is usable before installation as authority-bounded next Work. After the exercise, a separate current observed-coordination claim can inform `SYSE.11`. A change in a relied-on
relation, condition, configuration, or use reopens only the affected claim and decision.

**When the full pattern is unnecessary.** Use ordinary architecture, configuration, integration, and Work
patterns when one Agent has authority over every configuration, release, commitment, and operating decision that
can change the integration result.

### SYSE.18:6 — Bias Annotation

Systems-of-Systems literature is influenced by defence, formal model federation, and software orchestration. Use
each source for the Method and case it actually studies. A cross-domain constituent classification, governance
form, representation, or integration Method needs its own evidence. Official attention and conformance describe
publications or declared rules; project use and effectiveness need evidence from performed Work and outcomes.

Compare several decision centres by their actual authority, operations, outcomes, and feedback. Distributed and
centralized arrangements can each help or harm; the label decides nothing.

### SYSE.18:7 — Conformance Checklist

- [ ] One shared use, conditions, interval, affected Systems, current decision, and deciding Agent are stated.
- [ ] Every constituent is an actual System included because its participation, output, failure, change, or
      withdrawal can alter the use.
- [ ] Each relied-on relation has its own predicate and participants; no umbrella contribution relation replaces it.
- [ ] Independence is stated for named decisions and relations, not as an absolute property.
- [ ] Every deciding Agent, assignment when relevant, authority, permission, conflict, and escalation is stated.
- [ ] Interface syntax is supplemented by configuration-bound exchange and use evidence where interoperability is
      claimed.
- [ ] The selected alternative remains within the deciding Agent's authority and names outside decisions and
      unsupported dependencies.
- [ ] Any claimed coordination change identifies performing Agent, Method, dated Work, actual change or relation,
      configuration, representative observation, and evidence limits.
- [ ] The decision episteme, performed Work, world-side change, and observed-coordination claim are identified and
      grounded separately.

### SYSE.18:8 — Common Failures and Repairs

These recurring failures hide a relation, deciding Agent, or evidence boundary:

| Failure | Repair |
| --- | --- |
| *System of systems* is treated as a kind and explanation | Recover actual Systems, use-relative relations, and decision boundaries. |
| Participation is treated as parthood | State the direct relation and keep Work, capability, commitment, interface, resource, and evidence claims separate. |
| Interface syntax is treated as interoperability | Obtain configuration-bound evidence that results are exchanged and usable. |
| Agreement is treated as performance | Separate commitment, later Work, delivered result, and fulfilment evidence. |
| Integrator is assumed to own constituent decisions | Name each deciding Agent and authority; retain truthful blockers. |
| Decision record is treated as coordination change | Perform authorized Work and identify the actual transformation or relation before claiming a changed condition. |
| Decentralized is assumed to be better | Compare decision centres, operations, outcomes, and feedback for this use. |
| Model federation is treated as physical integration | Separate description consistency, actual configuration, integration Work, and operating evidence. |

### SYSE.18:9 — Consequences

Distributed authority and unsupported dependencies become visible before integration fails. The integrating Agent
can make a bounded useful change without pretending to centralize every constituent decision. The conditions relied
on by the shared use and the monitoring Work needed to maintain them become explicit.

The cost is negotiation and maintenance of constituent claims. Consequence-based inclusion and claim-sized
reopening keep the account from becoming a census of every neighbouring System.

### SYSE.18:10 — Rationale

Shared use depends on actual relations among Systems while authority and evolution remain distributed. Treating
every constituent as an owned component hides withdrawal and decision boundaries; treating the arrangement as
unmanageable emergence hides actionable interfaces, commitments, buffers, and fallbacks. Separate decisions,
Work, changes, and observations make bounded integration possible.

### SYSE.18:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| [Papadopoulos, Tortola, and Geyer 2024](https://doi.org/10.1080/13597566.2024.2334470) and [Baldwin et al. 2024](https://doi.org/10.1111/psj.12518) | Several interdependent decision centres should be compared through their setting, operations, outcomes, and feedback over time. | The reviews report broad terminology, beneficial and harmful outcomes, and long-term evidence gaps; they establish no universally better governance arrangement. |
| [Raz et al. 2024](https://doi.org/10.1109/JSYST.2024.3409231) | Connect mission tasks, constituent capabilities, candidate configurations, consistency, and bounded alternative evaluation. | One simplified defence-funded demonstration establishes neither a universal ontology nor cross-domain effectiveness. |
| [Swickline, Mazzuchi, and Sarkani 2024](https://doi.org/10.1002/sys.21727) | Preserve separately maintained model sources while forming a larger behaviour and structure description. | One SysML/Cameo Method and lunar-rover case supplies description Work, not physical integration or universal architecture. |
| [Ashfaq et al. 2026](https://doi.org/10.1016/j.jss.2025.112661) | A systematic review retains several runtime-composition problems, solution families, tools, and evaluations for dynamic software-intensive Systems. | Software-intensive scope and unresolved sociotechnical alignment prevent a universal integration Method. |
| [SEBoK, “Applying the Systems Approach,” 2026 revision](https://sebokwiki.org/w/index.php?title=Applying_the_Systems_Approach&oldid=78074) | Concurrent, iterative, and recursive use of Systems Engineering across several Systems of interest. | Older lifecycle and requirements framing and component stop rules are not retained as this pattern's structure. |

This is a bounded expert synthesis, not evidence of field prevalence or causal superiority. Reopen a used source
claim when later systematic comparison changes its decision-centre, outcome, feedback, integration, or transfer
boundary.

### SYSE.18:12 — Relations

- A compatible `SYSE.6` result supplies architecture constraints for the same shared use. Ground constituent
  participation, commitments, authority, and interoperability under their direct patterns.
- `A.1.SCR` governs actual System recognition; `A.22` governs selected structures; `E.18.NET` governs a
  transformation-flow network only when its members and relations are independently established.
- `A.6.P`, `A.2.2`, `A.2.8`, and `A.10` separately govern service wording, capability, commitment, and evidence
  claims.
- `A.2.1`, `A.2.8.PER`, `A.15.1`, `A.3.1`, `A.3.4`, and `A.15.PROD` govern assignment, permission, Work, Method,
  actual change, and production claims. Another Agent's decision authority still needs its own direct claim.
- A specialist practice retains its own decisions and authority—for example, Organization Change, Corporate
  Governance, Operations, Configuration, Maintenance, safety, security, law, finance, or contracting.
- `SYSE.11` can use a compatible observed-coordination claim for the same constituent Systems, configuration,
  shared use, and interval. Ground any later fulfilment or authority claim separately.

### SYSE.18:End

<a id="syse-23"></a>
## SYSE.23 — Choose What to Change So Later System Changes Become Easier

### SYSE.23:0 — Use This When

Use this pattern when an engineer or manager says that a product or product family must become *more
evolvable*, but the next change is still slow, expensive, unsafe, or hard to assure. The limiting condition may
be in the project system-of-interest, its family architecture, a builder or enabling System, an engineering
platform, a Method, an Agent's capability, the Work that enacts a change, or a relation among them. Calling all
of these *the system* hides both the present difficulty and the architecture change worth funding.

Here, the **builder arrangement** comprises the named Systems, Agents, Methods, Work, services, configurations,
and direct relations used to make, change, verify, release, or support the project system-of-interest for the
selected future-change family. An account of that arrangement identifies each participant and relation.

The first useful result has three parts:

1. a grounded account of the project system-of-interest and its builder arrangement that keeps five claim kinds separate: characteristics of obtaining selected
   structures, capabilities of named holders for named Work, results and resources of change-Work occurrences,
   claims about a joint arrangement with named participants and relations, and supported causal or contribution
   claims;
2. separate specifications of possible-future selected structures for the project system-of-interest and builder arrangement, including the
   genuine holonic levels, non-holonic dependencies, and Work relations that matter to the decision; and
3. one replayable `ChoiceResult` for a bounded investment or reconfiguration.

**First move.** Name one class of future change the project expects to make: for example, add a sensor variant,
replace a supplier component, adapt to a new operating environment, reuse evidence across configurations, or
change the release Method. Then state what was actually observed. Was it a characteristic of an obtaining
architecture, a holder capability, a result or resource of change Work, a constraint in the joint arrangement of the project system-of-interest and builders, or only a suspected contribution? If the sentence still says only *the system is hard to change*,
the decision is not ready.

In practitioner-facing prose here, an **Agent** means an admitted System considered in an agent role, with
enough agency for the named decision or Work, scope, and period; `A.13` supplies the underlying agency result.
System identity, local system-role classification, capability, assignment, authority, and actual performance
remain separate claims. `C.11` uses `DecisionSubject` for the person, team, organization, or other collectivity
whose choice is recorded.

Use `C.25` when the immediate task is to repair one composite quality claim. Use `C.30` and `C.32` when the
immediate task is to characterize or choose one architecture independently of the relation between the project system-of-interest and builder arrangement. Use
`SYSE.6` when the current option set concerns only the engineered-System architecture. Use `SYSE.12` when the
practical result needed is one engineering-platform service. When the needed change is primarily organizational
or concerns human capability, use the relevant Organization Change Engineering or Human Capability Development
DPF result when available; otherwise name the specialist help needed and use a qualified source. Use `SYSE.21`
when cultural continuation is the current question.

### SYSE.23:0.1 — Short Practitioner Use

For a first pass, use one expected change family and one decision horizon:

1. State the change to be made, the project system-of-interest when it already exists or the intended-system
   claim when it does not, the configurations affected, the horizon, protected consequences, resources,
   `DecisionSubject`, chooser granularity, and authority.
2. Classify each current claim before assigning a quality bearer. Separate architecture characteristics, holder
   capabilities, change-Work results and resources, joint-arrangement claims, and causal or contribution claims.
3. Recover three structures when they matter: genuine part–whole or membership levels with their scale and
   cross-level conflicts; non-holonic dependencies or service relations between the project system-of-interest and builder arrangement; and first–then or
   overlapping Work. State why any omitted structure cannot change this decision.
4. Keep obtaining architecture relations and current observations separate from specifications and expected
   characteristics of possible-future structures.
5. Develop alternatives that change different selected structures of the project system-of-interest or builder arrangement. Show how each alternative
   changes option reachability, change cost, assurance, rollback, and displaced burden.
6. Compare the finite changes through `C.11.CRC`. Then carry the full `C.11` decision record: stable
   `OptionSet`, shared comparison basis, `ChoiceRule`, probe cost and value when relevant, and one lawful
   `ChoiceResult`.
7. Plan, authorize, perform, and observe the chosen change separately. Later Work can support or defeat the
   earlier claims; the decision record does not make the architecture change occur.

This attention order is not a universal Method unfolding. Development of the project system-of-interest,
development of its builders, platform service, Method change, evidence Work, and capability development can
overlap, recur, or remain separate Work wholes.

### SYSE.23:1 — Problem Frame

An engineered System does not become easier to evolve in isolation. A replaceable module may still require a
fixture the factory lacks. A configurable product family may outrun test and evidence reuse. A simulation
platform may generate variants that manufacturing cannot build or service. A flexible Method may depend on
skills, permissions, or data that the assigned Agents do not have. Conversely, a costly redesign of the project system-of-interest
may add little when the actual bottleneck is a slow builder or unavailable test service.

*Evolvability* is therefore an entry word, not a ready-made scalar or one universal quality bearer. An
architecture-characteristic claim concerns an identified selected structure of a System, family relation,
platform, or Method. A capability claim concerns a named holder and target Work under stated conditions. Lead
time, rework, defects, and consumed effort may be results or resources of bounded change Work. A claim about the joint arrangement of the project system-of-interest and builders identifies its participating Systems, Methods, Agents, and relations. A claim
that one architecture change caused or contributed to a Work result needs its own support. These claims may be
compared, but they do not become the same kind.

The structures also differ. The project system-of-interest and a builder System can each have genuine
constructive part–whole levels. Actual family members can participate in a membership structure. A component-
level change can create a simultaneous whole-System or family-level conflict. Those are genuine level claims
only when the part–whole or membership relation, scale, and horizon are stated. A dependency between the project
system-of-interest and builder arrangement, a provider relation, or a platform service is non-holonic unless
another relation establishes otherwise. Build-the-builder Work
that precedes testing of the project system-of-interest is temporal Work order, not a level.

### SYSE.23:2 — Problem

The first failure assigns every evolvability quantity to an unnamed *system*. Evidence from one software
module, prototype, team, or change occurrence is then reported as a characteristic of the product family,
factory, engineering platform, Method repertoire, organization, and culture. No one can tell whether the claim
concerns architecture, capability, Work performance, a joint arrangement, or causal contribution.

The second failure chooses a familiar mechanism before the claim subject is known. Mechanisms such as modularity, standard interfaces, automation, digital twins, feature flags, AI coding,
continuous delivery, or reusable tests are treated as universal answers. Each can help one change family and damage another through latency, coupling,
option loss, verification load, supplier dependence, configuration growth, security exposure, or maintenance
burden.

The third failure describes a desired architecture as if it already obtained. A roadmap contains a configurable
platform and automatic evidence reuse, so current lead-time claims are calculated from those possible-future
features. The investment decision then uses benefits that only the investment could create.

The fourth failure demands open-ended improvement without a bounded horizon or stop. Candidate generation grows,
but admissibility, integration, safety, cost, environmental consequences, and selection do not improve. More
variants become more inventory and assurance debt.

### SYSE.23:3 — Forces

The recurring tensions are:

- **Reachability and control.** More admissible variants can preserve future options, while uncontrolled variation
  increases configuration, integration, safety, and service burden.
- **Modularity and system performance.** Looser coupling can localize change, while added interfaces, indirection,
  mass, latency, or duplicated capability can damage current performance.
- **Gain in the project system-of-interest and builder debt.** A shortcut in the project system-of-interest can deliver one increment quickly while making later
  manufacturing, integration, evidence, or maintenance Work harder.
- **Platform reuse and local difference.** A shared platform can reduce repeated Work, while forcing unlike
  profiles through one service can erase constraints that matter.
- **Change speed and evidence continuity.** Small reversible changes shorten feedback, while assurance and
  configuration evidence must still refer to the changed System and use.
- **Automation and authority.** AI and robotic Agents can generate, implement, or test more variants, while
  assignment, review, permission, release, and responsibility remain separate.
- **Exploration and exploitation.** A project needs alternatives and stepping stones, while a current decision
  needs a finite budget, protected losses, and a stop condition.
- **Project intervention and cultural continuation.** One successful reconfiguration can justify local use, while
  it does not establish discipline-wide selection, prevalence, or retention.

### SYSE.23:4 — Solution

Classify the current claims before deciding what should change. Recover the obtaining structures of the project system-of-interest and builder arrangement, including genuine
levels where they matter. Keep their non-holonic relations separate from temporal Work structure. Specify possible-future structures separately, compare materially different
investments against the current arrangement, and return one replayable architecture `ChoiceResult` whose later
consequences can be observed.

**Local mantra.** An expected change exposes a current difficulty. The team identifies whether the difficulty is
an architecture characteristic, capability limit, change-Work result or resource, joint-arrangement constraint,
or suspected contribution. Several views show genuine levels, dependencies between the project system-of-interest and builder arrangement,
and Work order or overlap without merging them. Alternatives that change either side are compared from one current
basis. A bounded choice is recorded; later Agents perform Work and supply observations.

#### SYSE.23:4.1 — Perform the Move

1. **Bind the future-change question.** Name what the decision concerns. When the designated project
   system-of-interest already exists, cite a compatible `SYSE.1` result and the plan or decision that designates
   it. When the System is still intended, keep its designator and expected change or use in a WorkPlan, decision,
   System description, or other claim episteme until identity inception. When a System family is in scope,
   identify the family, its actual member Systems, possible-future specifications, membership relation, and
   effectivity basis without calling the family another System. Add current configurations, expected change
   family, use, environment, affected Systems, horizon, frequency or scale of change, protected characteristics,
   resource limits, receiving decision, `DecisionSubject`, chooser granularity, and authority. The expected
   changes must be concrete enough that an engineer can tell what counts as admitted, completed, failed, or out
   of scope.
2. **Classify the claim before naming its subject.** Use one of five working forms:
   - an architecture-characteristic claim about an identified selected structure and its bearer;
   - a capability claim about a named holder, target Work, conditions, and evidence;
   - a result or resource claim about a bounded change-Work occurrence or a declared class of comparable Work;
   - a claim about a joint arrangement with the named project system-of-interest, builder Systems, Methods, Agents, and direct relations; or
   - a causal or contribution claim that connects a changed structure or capability to a later result.
   Identify the world-side subject independently. Treat descriptions, role labels, organization charts, Method
   accounts, and dashboard rows as epistemes or presentation elements used by Work.
3. **Qualify each claim on its own basis.** For an architecture characteristic or `C.25` quality bundle, state
   the bearer, selected structure, change family, scale, reference scheme, window, constraints, mechanism,
   evidence, uncertainty, and unsupported stronger claim. For capability, state holder and target Work. For
   change Work, state the Work occurrence, enacted Method, result and resource coordinates, configuration, and
   conditions. For a joint arrangement, state participants and relations. Keep causal contribution separate
   from co-occurrence, sequence, and correspondence. Do not compare claims that use different subjects, change
   families, scales, or horizons without a declared comparison relation.
4. **Recover three different structures.** For each view, state its `EntityOfConcern`, relation type, scale,
   horizon, and decision use.
   - In the **holonic or membership view**, identify constructive parts and wholes or actual family members.
     Record simultaneous cross-level conflicts when a local change improves one level while burdening another.
   - In the **system-of-interest–builder relation view**, identify the direct dependencies, correspondences,
     provider, service, interface, or enabling relations used by this decision. Do not infer part–whole from dependence.
   - In the **Work view**, identify first–then, overlap, concurrency, and recurrence among Work occurrences. Do
     not infer a level from earlier Work.
   If one view cannot change the decision, record that bounded non-use instead of drawing an empty universal
   stack.
5. **Separate current facts from possible-future specifications.** For every proposed change—for example, a
   module boundary, interface, product-family rule, fixture, test service, automation, Method change, or provider
   arrangement—write a possible-future architecture specification and the later Work and observation needed to establish it.
   Keep expected characteristics separate from current readings.
6. **Find the constraining relation and its evidence.** Ask which proposed change to the project system-of-interest is unreachable, too costly, too slow, too hard to
   assure, or too hard to roll back under the current builder arrangement. State the selected structure of the
   project system-of-interest, the builder structure or service, their direct relation, the affected result,
   evidence, uncertainty, and moved burden. When a causal contribution is needed, state the mechanism and the comparison or intervention basis;
   do not promote co-occurrence or earlier order into causation.
7. **Develop alternatives on both sides.** Include the incumbent and materially different changes such as a
   boundary or interface of the project system-of-interest, family configuration rule, builder fixture or manufacturing cell, test
   and evidence platform, release Method, supplier arrangement, or a change spanning both sides. In product–production cases,
   include production-process and production-System reconfiguration when they constrain product-family change
   across generations. State which selected structure each alternative changes and which constraints it leaves
   untouched.
8. **Compare finite changes.** Use `C.32.ACS` to choose a few optimization indicators and monitored guardrails
   with their actual claim subjects and scales. Apply `C.11.CRC` to each realizable finite change relative to the
   current configuration of the project system-of-interest and builder arrangement. Preserve result and resource vectors, implementation Work,
   interactions, uncertainty, reversibility, future-option effects, and displaced burdens. Do not score possible
   option reach as an already realized operating result.
9. **Return a replayable investment choice.** Freeze the viable `OptionSet`. State one shared preference order
   or evaluative measure, `BeliefState`, and `OutcomeModel`. When another probe is live, state its action set,
   budget, cost, and expected decision value. Apply one `ChoiceRule` and emit one `ChoiceResult` from the current `C.11` result set: choose a change to the
   project system-of-interest, builder arrangement, or both; retain a tie-set; reject the current set; request a
   probe; or reroute and end this decision pass because the question, authority, or needed input lies elsewhere.
   Record protected losses, budget, dependencies, the reason the result is lawful, and overturn conditions. The choice may issue an
   implementation request, but it does not authorize or perform the change.
10. **Realize and observe separately.** Assigned Agents later perform separately identified Work that changes the project system-of-interest, a builder
    System, platform, Method, or organization arrangement under its own authority and enacted Method. Observe
    representative future changes through measures relevant to this decision—for example, reachability, lead
    time, rework, defect introduction, evidence reuse, rollback, consequences for the project system-of-interest,
    provider burden, or newly exposed constraints. Revise only the claims and architecture decisions that the
    observations support or defeat. Send human capability demand to Human Capability Development and cultural-continuation
    evidence to `SYSE.21` rather than hiding either inside an evolvability score.

#### SYSE.23:4.2 — Record the Result

Use a linked set of descriptions for the stated decision. The table below is the complete content set for the first result. Each claim keeps its own subject and scope; one
reader-facing index does not merge architecture, capability, Work, arrangement, contribution, decision, or
observation records.

| Account content | What to record |
| --- | --- |
| decision boundary | Project system-of-interest when it already exists, or the intended-system claim when it does not; any System family with its membership and effectivity basis; configurations, expected change family, use, environment, affected Systems, horizon, scale, protected characteristics, resources, `DecisionSubject`, chooser granularity, authority, and receiving decision. |
| current claim inventory | Claim kind; identified subject; architecture bearer and selected structure, capability holder and target Work, change-Work occurrence and its result/resource coordinates, or joint-arrangement participants and relations; scale, window, evidence, uncertainty, and unsupported stronger claim. |
| holonic or membership view | `EntityOfConcern`; obtaining part–whole or actual-member relations; decision-bearing levels; scale and horizon; simultaneous cross-level characteristic conflicts; reason for any bounded non-use. |
| system-of-interest–builder relation view | `EntityOfConcern`; selected structures of the project system-of-interest and builder arrangement; the direct dependency, correspondence, provider, service, interface, or enabling relations used by this decision; consequence, moved burden, evidence, uncertainty, and unsupported causal claim. |
| Work view | `EntityOfConcern`; Work occurrences, performing Agents, enacted Methods, first–then, overlap, recurrence, required order, and separately obtaining assignment and authority. |
| possible-future specifications | Proposed selected structures and mechanisms, expected characteristic changes, required realization and evaluation Work, assumptions, and failure conditions. |
| alternatives and comparison | Incumbent and materially different changes to the project system-of-interest, builder arrangement, or both; current and candidate configurations; result and resource vectors; guardrails; interactions; uncertainty; reversibility; future-option effects; and displaced burdens. |
| investment `ChoiceResult` | `DecisionSubject` and granularity; stable `OptionSet`; shared comparison basis; `ChoiceRule`; probe budget, cost, and value when relevant; choose, tie-set, reject, probe, or reroute result; reason it is lawful now; protected losses; budget; implementation request if any; and overturn conditions. |
| later Work and observation | WorkPlan and authorization when they obtain; performed Work, changed structures, representative future-change cases, observations, supported and defeated claims, separately supported contribution claims, consequences for the project system-of-interest and other affected Systems, and receiving feedback. |

#### SYSE.23:4.3 — What Changes in Practice

Managers stop buying *evolvability* as a generic promise. Engineers can say what kind of claim failed, which
current structure or Work result it concerns, which genuine level or system-of-interest–builder relation matters, what burden each alternative moves, and why
the present choice is lawful. A platform investment competes with a redesign of the project system-of-interest on one declared basis instead of being justified by an unrelated platform metric.

### SYSE.23:5 — Worked Case: Where to Invest for the Next Heat-Pump Controller Variants

The heat-pump controller project from `SYSE.22:5` expects three changes over the next two years: support another
compressor supplier, add a local fallback mode for buildings with unreliable networks, and reuse assurance
evidence across controller configurations. Management says that the controller family must become *more
evolvable*.

The following table is the complete current claim set used by this decision:

| Claim kind and subject | Current claim | Evidence and limit |
| --- | --- | --- |
| architecture characteristic of the selected compressor-control and network-interface structure in controller configuration `C17` | the current coupling exposes four firmware components to one compressor replacement | one recent replacement found those four changes; it does not establish the same coupling in every family member. |
| architecture characteristic of the `ControllerFamily-F7` membership and effectivity structure | six released variants remain admitted under current interface, configuration, and assurance rules | two proposed supplier/network combinations lack effectivity and evidence; specifications are not current family members. |
| result and resource claim for `RigChangeWork-41` on the hardware-in-the-loop rig | representing another compressor interface required eleven hours of manual rewiring and produced coverage for only two interface variants | this is a result and resource use of one Work occurrence under one rig configuration, not a quality of every platform or future test. |
| result and resource claim for the 2026 commissioning and recovery Work sample | manual parameterization produced repeated field errors and slow restoration | the service records bound the sample; they do not establish platform automation as the only cause or repair. |
| capability claim for release-team Agent `RT2` | `RT2` can review the current configuration, evidence, and rollback package but lacks supported capability for the proposed cross-variant evidence slice | the current Method account and observed review Work support this bounded claim; a report about the Method is not the team's capability. |
| joint-arrangement claim for `C17`, rig `R4`, release Method `M2`, and team `RT2` | the compressor-interface coupling, rig adapter correspondence, test-service relation, and release-evidence dependency constrain the currently reachable supplier-change cases | the named participants and relations support the bounded arrangement claim; they do not establish how much each participant causes the observed Work result. |
| proposed causal-contribution claim about changing the compressor boundary and rig adapter | the mixed change is expected to reduce supplier-change lead time and improve evidence reuse | this is a possible-future contribution claim. Only later comparable change Work and observations can support or defeat it. |

The team then fills three different architecture views:

| View and `EntityOfConcern` | Obtaining relations | Decision use |
| --- | --- | --- |
| holonic and membership view of controller `C17`, rig `R4`, and family `F7` | `C17` has processor board, I/O assembly, and network module as constructive parts. `R4` has a host, I/O rack, compressor emulator, and network-fault injector as constructive parts. Six actual controllers are members of `F7` under the current effectivity basis. | A versioned compressor boundary can localize component replacement while adding processor load at controller level and configuration/evidence burden at family-member level. Rig parameterization can reduce rewiring Work while adding maintenance and qualification burden at rig-whole level. These are simultaneous cross-level conflicts, not stages. |
| non-holonic system-of-interest–builder relation view of the `C17`–`R4` test arrangement | the controller compressor interface corresponds to a rig adapter; the rig provides a test service to release Work; the evidence pipeline depends on configuration identity | The controller does not contain the rig, team, or Method as parts. Changing either side can move the supplier-change and assurance burden. |
| Work view of the next supplier-change trial | adapter parameterization precedes closed-loop test; evidence review overlaps later testing; rollback preparation and service planning overlap the release decision | Earlier and overlapping Work constrain the investment, but their order creates no holonic level. |

The positive level view matters here; omitting it would hide processor and evidence burdens that appear at a
different level from the interface change. The system-of-interest–builder relation view matters because the rig is not a part of the controller. The Work view matters because test readiness and review overlap determine calendar and assurance
resources. None of the three can be inferred from another.

Three alternatives survive admission beside the incumbent:

1. **Redesign the controller:** isolate compressor and network dependencies behind versioned interfaces. This can
   localize later changes but adds interface translation, processor load, and an immediate verification burden.
2. **Change the builder arrangement:** parameterize the test rig and configuration/evidence pipeline for the known
   supplier and network-loss variants. This can shorten trial and evidence Work but leaves four coupled controller
   components unchanged.
3. **Mixed bounded change:** introduce one compressor boundary for the next supplier and parameterize only the
   corresponding rig and evidence slice. This preserves less future reach than a general redesign but limits
   current cost and provides evidence for the larger choice.

The deciding Agent applies `C.11.CRC` to compare each finite change with the current controller-and-builder configuration. For this case, the complete result-coordinate set contains admitted supplier and network variants, change lead time, defect reintroduction, evidence reuse, rollback
time, comfort, energy, safety, and service error exposure. Resource coordinates include engineering time, rig
outage, supplier Work, review load, capital, and later maintenance. The team does not add these to one
evolvability score.

The architecture choice is replayable:

| `C.11` content | Filled result |
| --- | --- |
| `DecisionSubject` and granularity | The `ControllerFamily-F7` investment council at team level may allocate the approved two-year architecture budget. Safety and product-release authorities remain separately identified. |
| current `OptionSet` | Retain the incumbent arrangement; redesign the controller; change the builder arrangement; or make the mixed bounded change. |
| shared comparison basis | Safety, comfort, and rollback are hard guardrails. The `BeliefState` contains the observed four-component coupling, manual rig rewiring, service errors, current family/effectivity records, and bounded transfer uncertainty. The `OutcomeModel` relates each finite option to the declared result and resource vectors over the two-year horizon. |
| probe decision value | Feasible pre-choice probes are an additional supplier-interface simulation and a rig mock-up, bounded to four weeks and one rig outage. Neither can establish the coupled interface–rig–evidence result without constructing nearly the same slice as the mixed option; their expected information value does not justify their delay and cost. |
| `ChoiceRule` | Reject any option that violates safety, comfort, effectivity, or rollback guardrails. Among survivors, retain the non-dominated set and choose a change within budget that improves at least the next supplier replacement and evidence-reuse case while minimizing irreversible burden. Request a probe only when it can change the survivor relation enough to justify its cost. Reject the set if no option survives; reroute when the decision subject, authority, or comparison basis is missing. |
| `ChoiceResult` | `choose_now`: make the mixed bounded change. It survives the guardrails, addresses both controller coupling and rig/evidence burden within the approved horizon, and no smaller pre-choice probe is worth its cost. The implementation request for one interface and one rig/evidence slice is a later record, not implementation or improved evolvability. |

The controller-redesign option would replace this result if evidence showed that the rig already supports the new
supplier. The builder-arrangement option would replace it if controller coupling proved local and stable. A cheap probe that
could reverse the survivor relation would change the result to `probe_again`; guardrail failure by every option
would produce `reject_current_set`; missing authority would produce a reroute that ends the current decision pass without stopping unrelated Work. These are
overturn conditions, not footnotes.

Assigned Agents later perform redesign, platform, test, release, and observation Work under their own
authorities. Two supplier-change occurrences provide observations about controller coupling, rig time, evidence
reuse, and service burden. A failed transfer reopens only the claims and decision that used it; it does not erase
the separate facts about released configurations.

The manufacturing coevolution studies used below support joint product-family and production-system work across
generations. Applying that line to this test, release, and service arrangement is a bounded engineering
synthesis. The case must be reopened if the transfer hides a software, Method, organization, or capability
difference that changes the decision.

### SYSE.23:6 — Bias Annotation

The following nine biases recur in the source material and engineering cases used by this pattern.

| Bias | Likely drift | Repair |
| --- | --- | --- |
| claim-kind collapse | Architecture characteristics, holder capability, change-Work results, joint arrangements, and causal contribution are all assigned to one *evolvability bearer*. | Classify the claim first; identify the subject and evidence required by that claim kind. |
| system-of-interest-only bias | All change difficulty is attributed to the architecture of the project system-of-interest. | Inspect family, builder, platform, Method, Agent, Work, and cross-structure constraints for the named change family. |
| single-score bias | Lead time, option reach, evidence reuse, rollback, defects, and cost collapse into one evolvability number. | Use one characteristic where sufficient or a `C.25` quality bundle with visible coordinates and windows; keep Work results and resources under their own subjects. |
| modularity dogma | More modules and interfaces are assumed to mean easier evolution. | Name the change family, coupling affected, interface cost, cross-level conflict, performance loss, and evidence needed. |
| software-transfer bias | Feature flags, CI/CD, fitness functions, or microservices are copied into physical engineering unchanged. | Preserve material configuration, manufacturing, integration, specialist, safety, assurance, release, and service constraints. |
| platform halo | A new engineering platform is assumed to improve product outcomes. | Compare its finite contribution to representative changes of the project system-of-interest and displaced provider burden. |
| automation and AI bias | Variant generation or code change is treated as autonomous whole-project evolution. | Identify the performing Agents, assignments, Work, review, authority, evidence, and release decisions. |
| level-and-stage bias | The project system-of-interest, family, builders, platform, Methods, capabilities, and culture are arranged as one vertical sequence, or genuine part–whole levels disappear with the false stack. | Recover part–whole or membership levels, non-holonic system-of-interest–builder relations, and Work order or overlap separately; state cross-level conflicts when they matter. |
| success-story bias | One fast change is treated as establishing a durable characteristic or cultural improvement. | State the case, exposure, horizon, competing explanations, transfer limit, and later observations required. |

### SYSE.23:7 — Conformance Checklist

All ten conditions below are required for a conforming use of this pattern.

| ID | A conforming use... |
| --- | --- |
| `CC-SYSE23-1` | names one expected change family, project system-of-interest when it already exists or intended-system claim when it does not, configurations, use, environment, affected Systems, horizon, scale, protected characteristics, resources, `DecisionSubject`, chooser granularity, and receiving decision. |
| `CC-SYSE23-2` | classifies each relied-on claim as an architecture characteristic, holder capability, change-Work result/resource, joint-arrangement claim, or causal/contribution claim before naming its subject. |
| `CC-SYSE23-3` | gives each claim its required subject, scale, window, constraints, evidence, uncertainty, and unsupported stronger claim; one description or common word does not merge them. |
| `CC-SYSE23-4` | distinguishes current obtaining architecture relations and selected structures from possible-future architecture specifications. |
| `CC-SYSE23-5` | positively recovers genuine part–whole or membership levels and simultaneous cross-level conflicts when they matter; keeps them distinct from dependencies between the project system-of-interest and builder arrangement and from Work order or overlap. |
| `CC-SYSE23-6` | states a supported dependency, correspondence, provider, service, interface, or enabling relation between the project system-of-interest and builder arrangement that changes option reachability, cost, assurance, rollback, or another decision coordinate; causal contribution has separate support. |
| `CC-SYSE23-7` | compares the incumbent and materially different changes to the project system-of-interest, builder arrangement, or both relative to one current arrangement, preserving result and resource vectors and guardrails. |
| `CC-SYSE23-8` | gives AI, robot, person, team, supplier, or organization Agents only the Work and authority supported for the named scope and window. |
| `CC-SYSE23-9` | carries the stable `OptionSet`, shared comparison basis, `ChoiceRule`, probe cost and value when relevant, lawful `ChoiceResult`, and overturn conditions; implementation and observation remain separate. |
| `CC-SYSE23-10` | states the transfer limit of product–production coevolution evidence and sends human capability and cultural-continuation results to HCD and `SYSE.21`. |

### SYSE.23:8 — Common Failures and Repairs

The following rows describe recurring failures in the source material and engineering cases used by this pattern.

| Failure | Symptom | Repair |
| --- | --- | --- |
| *The system is evolvable* | No claim kind, subject, change family, scale, horizon, or evidence is named. | Classify the claim, identify its subject, and use `C.25` only when several typed quality coordinates are required. |
| Work result becomes System quality | One change duration or defect count is assigned to a platform, family, Method, or team. | Keep the Work occurrence, enacted Method, result/resource coordinate, configuration, and conditions visible; make a separate architecture or capability claim only with its own evidence. |
| Mechanism equals characteristic | The presence of modules, APIs, tests, a digital twin, or AI establishes evolvability. | Assess the declared architecture characteristic or Work result and preserve the mechanism as an explanatory input. |
| Builder mistaken for a system-of-interest part | A factory, test rig, platform, or team is drawn below the project system-of-interest as a holonic level. | Recover the builder, service, dependency, assignment, or Work relation separately; also retain genuine part–whole levels inside the project system-of-interest and builder Systems when they matter. |
| Possible future equals current architecture | Roadmap benefits enter the baseline. | Keep current relations, candidate specifications, implementation Work, and later readings separate. |
| More variants equals improvement | Candidate count rises while admissibility, integration, evidence, and selection degrade. | Preserve archive value, Front basis, guardrails, and finite resource constraints. |
| Platform metric chooses product investment | Deployment or test speed improves locally, but consequences for the project system-of-interest and provider burden are absent. | Compare changes to the project system-of-interest and builder arrangement on one shared basis and expose displaced burden. |
| Project choice equals cultural selection | A local change is called a new engineering culture. | Use `SYSE.21` and later population evidence for transmission, recognition, selection, retention, and loss. |

### SYSE.23:9 — Consequences

The project gains a practical answer to *where should we invest so that the named later changes become reachable
and affordable?* Redesign of the project system-of-interest, family architecture, builder reconfiguration,
platform Work, Method change, and separately justified capability or organization work can be compared without pretending that they
are one object or one level. Genuine cross-level conflicts remain visible. Possible-future benefits do not enter
the current baseline.

The cost is a more disciplined claim and architecture account. There may be no single evolvability number, and
the best first decision may improve only one change family. Some constraints require a neighboring DPF or
specialist source; a bounded project cannot establish profession-wide cultural continuation or unlimited
open-endedness.

### SYSE.23:10 — Rationale

`C.25`, `C.30`, `C.32.ACS`, `C.32.HCS`, `C.32.MWA`, and `C.36` already govern quality bundles,
architecture relations, project criteria, holon-family starter material, several practice structures, and
cultural evolution. Systems Engineering adds the applied decision that survives subtraction: relate the project
system-of-interest and family to builder and enabling Systems, platform, Methods, Work, configuration, evidence,
and consequences for named affected Systems; then choose which selected structure to change for one future-change family.

The pattern keeps builder Work separate from Work on the project system-of-interest and retains genuine levels.
It can use a constructive part–whole view of the project system-of-interest or a builder System, a family-
membership view, a non-holonic system-of-interest–builder relation view, and a Work-order or overlap view because these answer different concerns. Each view
states its `EntityOfConcern` and relations. Correspondences and contribution claims among views need their own
basis.

### SYSE.23:11 — SoTA and Source Use

This table is the complete source-use register for this pattern body.

| Source line | Use here | Epistemic boundary |
| --- | --- | --- |
| R8 Systems Engineering material and [R11, *Development for Advanced Practitioners*](../../../GuidesProject/R5-R10-pedagogical-companion-md/converted-md/R11-DevelopmentForAdvanced.md) | Supplies continuing engineering, target and builder development, engineering platforms, product and problem portfolios, recursive factory-development views, characterization, reversible change, and evidence return. | These are practitioner syntheses. Their factory, lifecycle, target, stack, and process labels do not establish current FPF kinds, one universal architecture, or measured field prevalence. |
| Bryan et al. (2007), [*Co-Evolution of Product Families and Assembly Systems*](https://doi.org/10.1016/j.cirp.2007.05.012); Tolio et al. (2010), [*SPECIES—Co-evolution of products, processes and production systems*](https://doi.org/10.1016/j.cirp.2010.05.008); and Albers et al. (2022), [*Product-Production-CoDesign*](https://doi.org/10.1016/j.procir.2022.05.231) | Supplies joint product-family and assembly/production-system design, product–process–production-system coevolution, coupling across generations, future-characteristic treatment, and production reconfiguration. This pattern adopts joint alternative development, adapts it into the system-of-interest–builder relation and the manufacturing branch in steps 4, 6, and 7, and rejects the idea that product architecture can be optimized independently of the production arrangement. | The studies concern manufacturing and product–production settings. They do not establish transfer to software, Methods, organizations, human capability, or every builder arrangement. Those extensions remain bounded engineering syntheses and reopen when a transfer failure changes the practitioner decision. |
| Fricke and Schulz (2005), [*Design for changeability*](https://doi.org/10.1002/sys.20039) | Supplies a Systems Engineering account of incorporating changeability into architecture and distinguishes flexibility, agility, robustness, and adaptability across industries. | It is a historical field anchor. Its lifecycle and quality vocabulary does not create one FPF evolvability characteristic or settle the claim subject and system-of-interest–builder relation in this pattern. |
| Ross, Rhodes, and Hastings (2008), [*Defining changeability*](https://doi.org/10.1002/sys.20098) | Supplies explicit change agents, change effects, change mechanisms, context change, and tradespace-based changeability distinctions. | Its filtered-outdegree measure answers a declared tradespace question; it is not a universal evolvability scalar and does not include every builder, Method, capability, culture, or evidence relation used here. |
| Ford, Parsons, Kua, and Sadalage (2022), [*Building Evolutionary Architectures*, second edition](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/) | Supplies practical software-architecture mechanisms for guided incremental change, several architectural dimensions, fitness functions, deployment pipelines, reversibility, and appropriate coupling. | Software examples do not transfer automatically to physical configuration, manufacturing, integration, safety, assurance, specialist authority, or product-family effectivity. A fitness function is evidence input, not the architecture characteristic itself. |
| MacCormack, Rusnak, and Baldwin (2008), [*The Impact of Component Modularity on Design Evolution*](https://doi.org/10.2139/SSRN.1071720) | Supplies empirical motivation and cautions for relating component modularity to later software-design evolution, including the need for repeatable measures and longitudinal evidence. | Software source structure and one modularity construction do not make more modules better or establish causality for another engineering profile. |
| Castle, Stock, and Gorochowski (2024), [*Engineering is evolution*](https://doi.org/10.1038/s41467-024-48000-1), and Zhang et al. (2025), [*Darwin Gödel Machine*](https://arxiv.org/abs/2505.22954) | Supplies bounded examples in which engineers change variation-and-selection arrangements or a lineage-bearing builder that generates later variants. | Bioengineering perspective and coding-agent benchmarks do not establish one universal OEE Method, unrestricted self-improvement, transfer to every system-of-interest–builder arrangement, or cultural selection. |

Currentness is claim-sized. Reopen a source row only when changed evidence alters the claim kind or subject,
change family, architecture relation, transfer limit, decision, or observation used here. Recency alone does not
make a Method or mechanism preferable.

### SYSE.23:12 — Relations

The following direct relations are used by this pattern body.

- Receive a compatible `SYSE.22` result containing the project focus, selected problem portfolio, System-family
  options, supported correspondences, unresolved mismatches, and replayable `ChoiceResult`. Accept or qualify
  that account even when its lawful result was choose, reject, or reroute rather than an experiment. If a needed
  input is missing, state which `SYSE.23` decision it blocks. The input selects neither the claim subject nor the
  architecture investment.
- Use `SYSE.3` for the recursive realization arrangement; `SYSE.6` for the current engineered-System architecture;
  `SYSE.7` for descriptions and provenance; `SYSE.10` for evidence; `SYSE.12` for engineering-platform
  capabilities; `SYSE.13` for configuration and effectivity; `SYSE.15` for the Method repertoire; and `SYSE.20`
  for Method-and-Work structures. Each result keeps its own subject and use boundary.
- Use `C.25` only after the quality bearer and Q-Bundle have been recovered. Use `C.30` for obtaining
  architecture relations and selected structures, `C.32.ACS` for a small project criteria set, `C.32.HCS` for
  family-specific starter material, and `C.32.MWA` for several non-isomorphic Method, Work, subject, dependency,
  and cultural structures. None supplies the engineering decision that compares changes to the project
  system-of-interest and builder arrangement by itself.
- Use `C.18` for archive and Front claims, `C.11.CRC` for finite configuration-relative contribution
  comparisons, and `C.11` for the later choice. Keep generation, selection, architecture, capability, Work
  result, implementation, observation, and causal attribution distinct.
- Supply revision feedback to `SYSE.3`, `SYSE.6`, `SYSE.11`, `SYSE.12`, `SYSE.15`, or `SYSE.20` only when later
  evidence crosses a stated limit or changes an assumption of the receiving result. Feedback is an input to
  another decision, not an automatic stage.
- Supply `SYSE.23 → SYSE.21` only with a bounded Method or arrangement variant and observations relevant to later
  cultural work. A project choice or successful change establishes no transmission, cultural selection, or
  retention.
- Send a human capability demand to Human Capability Development only for a named human holder population,
  target Work, support arrangement, capability evidence, and horizon. Do not treat an AI or robot as a human
  holder, or turn a platform, Method, assignment, organization, or authority relation into a capability of that
  human population. Use `A.15.1` and `F.6` for actual Work performance and attribution, and use the pattern that
  defines the named assignment or authority relation.
- For organization or assignment reconfiguration, continuing flow and capacity, Method construction, or service
  intervention and restored use, use the relevant DPF result when available. Otherwise name the specialist help
  that is missing and use a qualified source. Similar change language does not merge Organization Change
  Engineering, Operations Management, Method Engineering, and Maintenance Engineering.

### SYSE.23:End

# Part IV — Configuration, Continuing Change, and Source Continuity

<a id="syse-13"></a>
## SYSE.13 — Establish Configuration Identity, Variants, and Effectivity

### SYSE.13:0 — Use This When

Use this pattern when an engineering decision depends on an actual System's identity and configuration or on a
description's applicability—for example, which physical unit has which part and installed software, or which
description edition applies to that unit—but records reuse a label such as a part number, version, baseline,
release, or status as if it answered all of those questions.

Begin with the receiving decision and the actual Systems whose differences can change it. Select only the
configuration-item boundaries needed for that decision. Restore every distinction used by the case—for example,
actual units, product-family variants, software packages and installed realizations, description editions,
reference baselines, or effectivity. Then state the supported correspondences that allow one record to be used
with another.

The first useful result is a **decision-specific configuration basis**: an episteme that tells an engineer which
actual units and descriptions can be used for one decision, where each claim applies, which collisions or gaps
remain, and what later change reopens it. The actual Systems and configurations are its subjects; descriptions
carry its claims; evidence supports them; and release decisions and performed Work remain their own results.
Use the governing FPF pattern directly when one identity, structure, characteristic, edition, or temporal claim
already answers the question. Use `SYSE.7` when several descriptions must be made jointly usable, `SYSE.14` when a proposed or
performed change must be connected to release, and `SYSE.19` when a changed source may reopen earlier decisions.

### SYSE.13:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| actual configuration | The decision-relevant actual constituents, obtaining relations, and characteristic values of one identified actual System over an interval. A configuration description carries claims about that configuration; a database value or dashboard status is not the configured System. |
| configuration item | A decision-local designation of an already identified entity whose separate identity, parthood where relevant, and change matter to the receiving decision. The entity may be, for example, a System, physical part, software-package episteme, or description episteme. The designation creates no universal kind. |
| physical or serial unit | One actual System individual. Its part number, family description, bill of material, variant name, and status record are separate descriptions or claims. |
| product family | A stated grouping of actual Systems or possible-future System referents under a classification and variation scheme. The current claim must say whether it concerns a kind, set, lineage, or description. |
| variant | A combination of design or configuration claims, normally carried by a description and possibly realized by actual units. A variant label does not prove realization. |
| software package and installed realization | In this pattern, a package or build episteme specifies software content. The content installed in a unit and its actual operation in that unit are separate world-side facts whose correspondence to the package needs evidence. |
| description edition | One episteme related to an earlier edition only under an edition-continuity relation. A changed filename, timestamp, or revision number is insufficient. |
| baseline | A selected reference episteme or claim set used for one comparison. Actual configuration, evidential support, authority, and release require their own claims or decisions. |
| effectivity | A claim that a description, change, release, or configuration claim applies to identified subjects and conditions—for example, Systems, serial units, lots, sites, intervals, operating conditions, or a stated combination. A date alone is insufficient when the subject or condition is unknown. |
| status | A claim or decision value about a subject for a use and interval. A value such as *approved*, *released*, *installed*, or *current* in one tool does not establish the corresponding world-side fact. |
| comparison labels such as *as-designed*, *as-realized*, *as-integrated*, or *as-maintained* | Source terms for local comparison roles of configurations and descriptions. Recover the role used by the decision; the label imposes no lifecycle and guarantees no correspondence. |

Record the performing Agent, assignment, Method, and Work separately from the configuration basis and from the
Systems, descriptions, and evidence it concerns. Record the deciding Agent separately when another Agent performs
the configuration Work.

### SYSE.13:1 — Problem Frame

Continuing engineering keeps several configurations relevant at once—for example, candidate architectures,
manufactured variants, installed software realizations, experimental units, or service replacements. Engineering,
manufacturing, operating, and maintenance descriptions can also differ. Each kind of receiving Work may need
different item boundaries.

Shared identifiers and records—whether kept in a product-data system, a bill of material, linked-model
infrastructure, or a naming standard—do not remove the semantic problem. These resources can preserve identifiers
and links, while engineers still decide what each identifier denotes, which differences matter to the decision,
and what evidence connects the record to the actual System. One label can hide incompatible granularity;
different labels can denote the same unit under different schemes.

### SYSE.13:2 — Problem

A decision-specific configuration basis answers eight questions:

1. Which actual or intended subject does the decision concern—for example, a System, part, serial unit, lot,
   or site?
2. Which boundaries need independent identity for this decision, and why?
3. For each identifier, which reference scheme gives it meaning, which Agent issues or maintains it, over what
   interval, and in which record?
4. Which variant and software-package claims are candidates, and which actual units have evidence of realizing
   them?
5. Which constituents and relations obtain for each unit and interval, and which characteristic values are
   supported—for example, installed realizations or parameter values?
6. To which subjects and conditions does each description or change apply—for example, units, lots, sites,
   intervals, or operating conditions?
7. What does each cross-tool mapping preserve or lose, what evidence supports it, and is that loss acceptable for
   receiving Work such as build, integration, release, operation, service, or modernization?
8. Which Agent can settle a disputed identity or mapping, which receiving Work relies on the answer, and what
   change reopens it?

Without those answers, every local record can be internally consistent while the engineering decision is wrong.
Firmware can fit one board variant and fail another; an engineering bill of material can disagree with an
installed unit; a release can name the right part number but omit the units to which it applies.

### SYSE.13:3 — Forces

Recurring tensions include:

- A change can preserve or end an entity's identity; reusing its earlier label settles neither case.
- Design, manufacturing, integration, operation, and maintenance need different item boundaries, while receiving
  Work needs supported mappings among them.
- Family descriptions enable reuse; release, service, and failure decisions often depend on serial units and
  installed configurations.
- Extra fields and links cost maintenance, while one omitted unit, edition, condition, or correspondence can
  invalidate the choice.
- Several descriptions can agree with each other and still be wrong about the actual System.
- Automated comparison exposes differences among identifiers, bills, hashes, and editions quickly, but syntax
  cannot decide intended referent, applicability, or acceptable loss.
- A selected reference basis aids comparison while experimental, installed, and service configurations can
  legitimately coexist.

### SYSE.13:4 — Solution

Develop the smallest configuration basis that lets one engineering decision distinguish actual Systems,
variants, descriptions, and applicability without treating tool labels as ontology.

#### SYSE.13:4.1 — Perform the Move

1. **Name the decision and differences that matter.** State the deciding Agent, question, use, project
   System-of-interest or other subject, interval, and configuration differences that can change the result. Do not
   begin by inventorying everything.
2. **Identify actual and intended subjects.** Name every subject needed by the decision—for example, an actual
   unit, part, site, or possible-future referent. State needed part–whole and structure relations; a product code
   or bill-of-material row is not the bearer.
3. **Choose item boundaries for this use.** Designate only the entities that must be distinguished independently,
   such as Systems, parts, software-package epistemes, or descriptions. Different kinds of receiving Work may
   choose different boundaries; relate them instead of forcing one granularity.
4. **State identifier schemes and mappings.** For each item, name the identifier, scheme, issuing or maintaining
   Agent, interval, and supported mapping to another scheme. Shared spelling is not identity; a mapping need not
   be symmetric or lossless.
5. **Separate variants, units, packages, installations, and editions.** Name the variant description, actual units
   claimed to realize it, software package, observed installed realization, and description edition. Mark
   unsupported realization claims as gaps.
6. **State actual configuration and effectivity.** Name the actual constituents, obtaining relations, and
   characteristic values needed by the decision—for example, parts, interfaces, installed software, or parameter
   values. State the supporting evidence and interval, then name the subjects and conditions to which every
   description or change applies. Keep candidate and intended configurations modal.
7. **Choose a baseline only for comparison.** Identify the reference episteme and its decision. Keep it unchanged
   for that comparison; establish actual configuration and decision authority separately.
8. **Check collisions and return the basis.** Align bearer, boundary, scheme, edition, interval, and tolerance
   before comparing. Classify each problem by the action it requires—for example, repair an actual
   incompatibility, reconcile contradictory descriptions, qualify a lossy mapping, obtain missing evidence, or
   accept a harmless naming difference. State receiving Work, the Agent with revision authority, blockers, and
   the smallest reopen condition.

The numbered presentation is an `A.22.CGUS` learning unfolding, not a lifecycle. Work may overlap—for example,
identification, design, realization, integration, observation, or change Work—but receiving Work can rely only on
claims whose bearer and effectivity are known for that use.

#### SYSE.13:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| receiving use | Decision, deciding Agent, actual System or intended-system designator selected as the project system-of-interest, or another subject, interval, affected Work, and differences that can change the result. |
| subjects and item boundaries | Actual Systems, serial units, parts, or sites; possible-future referents where needed; selected item designations; rationale; and needed part–whole or structure claims. |
| identifiers and mappings | Schemes, issuing or maintaining Agents, intervals, directional mappings, preserved meaning, losses, evidence, and use limits. |
| variants, units, software, and descriptions | Candidate variant descriptions, actual-unit realization claims, software packages, installed realizations, description editions, and unresolved gaps. |
| configuration and effectivity | Actual constituents, obtaining relations, characteristic values, supporting evidence, and interval; subjects and conditions to which each description or change applies. |
| reference and collisions | Optional baseline and purpose; incompatible actual elements, contradictory claims, unsupported or lossy mappings, missing evidence, and harmless naming differences. |
| maintenance and return | Agents and authority for revision, receiving Work, reliance limits, blockers, and smallest reopen conditions. |

The basis may be published in a form such as text, a table, a product-data query, a model view, or a generated
report. Publication form and repository location determine neither its identity nor its truth.

#### SYSE.13:4.3 — What Changes in Practice

Engineers stop asking whether a configuration record exists and ask whether the current basis distinguishes the
units, variants, descriptions, and conditions needed by the decision. Product-family reuse remains available,
while release and service claims become serial-unit and effectivity aware.

Tools may expose a mismatch without deciding what it means. Engineers resolve the first collision that can change
the decision and leave unrelated inventory alone. A changed source reopens the smallest affected claim rather
than freezing the whole product or silently rewriting the reference baseline.

### SYSE.13:5 — Worked Case: Pump-Controller Variants and Ten Installed Units

A pump manufacturer is deciding which of ten installed controllers may receive a cold-start protection change.
The first export gives all ten the same product number and the status *current*. Inspection results and source
records show four different decision-relevant groups:

| Installed units | Observed configuration | Effect on the release decision |
| --- | --- | --- |
| S001–S004 | Input board IO-A and the older installed firmware realization. | Outside the candidate firmware package's hardware compatibility claim. |
| S005 | Input board IO-B and temperature sensor TS-2, but no current sensor calibration evidence. | Possible candidate after calibration evidence; not currently eligible. |
| S006–S008 | IO-B, TS-2, current calibration evidence, and an installed realization corresponding to the supported firmware lineage. | May enter the current release comparison, subject to installation and verification Work. |
| S009–S010 | IO-B and TS-2; the database says *installed*, but current calibration evidence is absent. | Possible candidates after the missing evidence is obtained; status alone is insufficient. |

The candidate firmware package is an episteme describing support for IO-B. It is not the software realization
currently executing in any controller. Installation and observation are needed before that correspondence can be
claimed.

The engineering and manufacturing bills of material use different item boundaries. Engineers maintain a
directional mapping from the engineering board item to the manufacturing board-and-harness items. The mapping
loses installation-routing detail and cannot be used in reverse without another check. They do not create
configuration items for every fastener or database row because those differences cannot change this release.

The effectivity proposal names S006–S008, the supported operating-temperature conditions, the candidate package
edition, and the required installation and verification Work. S001–S004 are excluded; S005 and S009–S010 retain
explicit evidence gaps. A selected reference configuration supports comparison but does not claim that every
installed unit realizes it.

The configuration basis can inform `SYSE.14` and bound the integration Work in `SYSE.11`. It establishes neither
installation, permission, release, nor successful operation. A changed board, sensor, package edition,
calibration source, inspection, or release question reopens only the affected unit and correspondence claims.

**When the full pattern is unnecessary.** If a laboratory engineer needs only to know whether one already
identified controller contains IO-B at the current inspection time, direct System, structure, temporal, and
evidence patterns answer the question. A product-family configuration basis adds no value.

### SYSE.13:6 — Bias Annotation

Document-control practice can make the record or baseline appear more real than the physical unit.
Software-centred records can hide installed hardware and effectivity; hardware-centred records can collapse
software packages and description editions into part numbers. Start with actual Systems and the receiving
decision.

A signal such as an official identifier, required form, vendor schema, digital-thread label, or declared
conformance status supports only the claim it actually records; actual project use and configuration
correspondence require their own evidence. Use expert judgment with an explicit
epistemic status when broad field evidence is unavailable.

### SYSE.13:7 — Conformance Checklist

- [ ] One receiving decision and the configuration differences that can change it are stated.
- [ ] Each actual System and part has its own identity; descriptions, identifiers, records, and status claims have
      their own bearers.
- [ ] Every configuration-item boundary has a decision-specific reason.
- [ ] Product-family variants, actual units, software packages, installed realizations, and description editions
      remain distinct.
- [ ] Each load-bearing effectivity claim names the units or lots, sites, intervals, and conditions required by
      the use.
- [ ] Cross-scheme mappings state direction, preserved meaning, loss, evidence, and use limits.
- [ ] Reference epistemes, status claims, actual configurations, decisions, permissions, releases, and performed
      Work retain separate identities and relations.
- [ ] The basis records collisions, unsupported correspondences, missing evidence, receiving Work, revision
      authority, and the smallest reopen conditions.

### SYSE.13:8 — Common Failures and Repairs

These recurring failures can change the engineering decision:

| Failure | Repair |
| --- | --- |
| Treat one identifier as one bearer everywhere | Name the bearer and reference scheme for each use; state supported mappings among schemes. |
| Treat configuration item as a universal kind | Use it as a local designation of an already identified System, part, software package, or description chosen for this decision. |
| Treat a variant as an installed unit | Keep the variant description and unit separate and require realization evidence. |
| Treat latest as applicable | Name the edition and effectivity; current publication does not establish compatibility with the unit. |
| Treat a baseline or green status as reality | Keep the reference or status episteme separate from the observed actual configuration. |
| Make one product-data system the ontology | Use it as a resource and recover Systems, parts, epistemes, relations, schemes, and losses outside its schema when needed. |
| Inventory everything before deciding | Select the smallest item boundaries and claims that can change the receiving decision. |

### SYSE.13:9 — Consequences

Release, integration, service, and modernization decisions can identify the units and descriptions they concern.
Product-family reuse no longer hides serial-unit differences, and cross-tool automation can be used without
treating identifiers as semantic proof.

The cost is maintaining selected identifiers, mappings, evidence, and effectivity claims. Some questions remain
unresolved until actual-unit observation or authority is available. Application profiles may still need specialized Methods for domain relations—for example,
interchangeability, software-package identity, regulated genealogy, ship configuration, or electrical
qualification.

### SYSE.13:10 — Rationale

The useful result is a decision-specific configuration episteme, not a database category. Starting from one
decision makes the boundary and maintenance burden testable. Keeping actual Systems, variant descriptions,
software packages, installed realizations, episteme editions, baselines, and status claims separate prevents the
situation in which every record is valid but no one knows which unit may be changed or released.

Effectivity is load-bearing because change rarely applies uniformly across a family. Time is only one condition;
another condition—for example, serial unit, lot, site, installed part, software realization, environment, or
operating envelope—may determine applicability.

### SYSE.13:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R6 `GC-09`, R7 `GC-05`, and R8 `GC-08`/`GC-10` | Separate product kinds, actual units, variants, versions, description editions, releases, status, and effectivity; keep configuration Work continuing and concurrent with other engineering Work. | Lifecycle stages, fixed document sets, frozen-baseline doctrine, and one universal responsibility ladder are not retained. |
| Frank B. Watts, *Configuration Management for Senior Managers* (2015), historical practitioner lineage | Recurring manufacturing distinctions among part identity, revision, interchangeability, bill of material, technical release, effectivity, implementation, status, and field change. | The paper-form, phase, central-department, sanction, and universal-policy recommendations are not current DPF authority. |
| [Brovar, Sadeghzadeh, and Fortin 2024](https://doi.org/10.1017/pds.2024.40) | One engine-front-mount case shows that engineering and manufacturing descriptions need explicit configuration links rather than a shared label. | One directional matrix case; reverse use and universal digital-thread architecture are not established. |
| [Wu et al. 2025](https://doi.org/10.1016/j.aei.2025.103490) | One landing-gear case connects heterogeneous model semantics, conflict handling, traceability, and model versioning. | The study concerns MBSE model versions in one case; it does not establish physical-unit effectivity, release, supply coordination, or broad dominance. |
| [Lehner et al. 2025](https://doi.org/10.1007/s10270-025-01264-7) | A systematic mapping study makes the heterogeneity of model-driven digital-twin uses and domain dependence visible. | Publication volume and tool capability do not establish one twin ontology, one configuration Method, industrial prevalence, or effectiveness. |
| [Bantwal and Fatahi Valilai 2026](https://doi.org/10.1007/s00170-025-17175-2) | A proposed engineering-change framework and brake-caliper demonstration connect parts, representations, supply constraints, CAD/CAE, ERP/PLM, and validation. | One proposed framework and demonstration support the need for connected configuration claims, not a universal item granularity or adopted SoTA workflow. |

Refresh a source-dependent claim when a new edition changes an item-boundary distinction, mapping capability,
effectivity rule, evidence limit, or transfer conclusion used here. Standards status, academic visibility, vendor
promotion, or a product named *digital thread* supplies no prevalence or effectiveness claim. When no affordable
empirical prevalence evidence exists, state an expert estimate as such rather than replacing engineering judgment
with official-source visibility.

### SYSE.13:12 — Relations

- `A.1` and `A.1.SCR` distinguish actual Systems from intended referents. `A.22` governs selected structures,
  `A.19.SPR` state-like claims, and `C.27.TA` temporal aspects. None by itself produces an engineering
  configuration basis.
- `C.2.1` keeps descriptions, editions, subjects, reference schemes, carriers, and publications distinct. `A.10`
  and `B.3` govern evidence and assurance when current; neither proves the actual configuration.
- `F.10`, `A.21`, `A.2.8.PER`, `C.11`, `A.15.1`, and `A.3.4` distinguish status, gate, permission, choice, Work,
  and transformation from configuration claims.
- A compatible `SYSE.6` result can supply architecture constraints for the same System, decision, configuration,
  and horizon. It neither selects item boundaries nor proves an actual configuration.
- A decision-specific configuration basis can inform `SYSE.14` only for the same change and release question and
  can inform `SYSE.11` only for the named integration or modernization increment. It establishes neither release
  nor realization.
- `SYSE.7` coordinates several decision-usable descriptions. `SYSE.19` revalidates decisions after a relied-on
  source changes. Co-use creates no additional dependency or temporal order.
- Application profiles—such as software, electrical, mechanical, manufacturing, medical-device, ship, or
  building profiles—may specialize item identity, effectivity, interchangeability, evidence, and release when
  the kinds or uses of Systems designated as project systems-of-interest change the working move. A profile label alone adds no pattern.

### SYSE.13:End

<a id="syse-14"></a>
## SYSE.14 — Make a Release Decision for Named Engineering Work or Use

### SYSE.14:0 — Use This When

Use this pattern when a workflow says that an engineering change is *approved*, *released*, *deployed*, or
*implemented*, but the receiving Agent still cannot tell what may happen next, to which actual Systems, under
whose authority, on what evidence, or under which conditions.

Begin with one question: may an identified description, software package, or actual System in a stated
configuration enter named Work or use—for example, realization, integration, trial, deployment, delivery, or
service? A release decision relates that subject to a permitted next use under stated conditions; a generic status
label does not. Recover each object needed by the case: the trigger, proposed change, technical choice, governing
authority and permission, release decision, later Work and actual transformation, resulting configuration, and
the records and evidence about them.

The first useful result is a **bounded engineering release decision**. It states what may enter the named Work or
use, for which units and conditions, what evidence and authority support the decision, what remains blocked, and
what later observation reopens it. The decision is an episteme. Separate evidence establishes the deciding
Agent's authority and any required permission, the observed configuration, performed change Work, resulting
transformation, and operating result.

Use `SYSE.13` when the immediate difficulty is identifying the relevant units, configurations, or effectivity.
Use `SYSE.19` when a changed source may invalidate an earlier decision. Use a governing FPF pattern directly when
one isolated result—such as a choice, permission, gate, Work, transformation, evidence, assurance, status, or
transfer result—already answers the question.

### SYSE.14:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| trigger | A source event such as a request, criticism, incident, opportunity, or changed source that starts reconsideration. Its problem claim, proposed response, and permission each need their own grounds. |
| change candidate | An episteme describing a possible-future change, affected Systems and descriptions, expected consequences, conditions, and evidence gaps. It is not an actual transformation. |
| technical choice | A `C.11` result comparing stated options. Authority, permission, release, and later realization require separate relations or results. |
| release subject and release kind | The identified description, software package, or actual System being considered, its relevant configuration, and the named next Work or use. Release for realization and release to service are different decisions. |
| authority | A grounded relation that makes an Agent competent to make the named decision within a stated scope. A title, assignment, signature field, or meeting attendance does not create it. |
| permission | A separately governed allowance concerning a named action, holder, subject, scope, and interval. Authority, evidence, assurance, and release retain their own relations and results. |
| implementation or integration Work | A dated Work occurrence performed by an Agent using a Method and relevant Systems. A ticket state or released description is not performed Work. |
| actual change | A world-side transformation of an actual System under stated conditions. It remains distinct from the Work, Method, candidate description, and decision. |
| actual configuration and effectivity | The actual configuration comprises the resulting System's constituents, obtaining relations, and characteristic values over an interval. Effectivity is an episteme stating which identified Systems and conditions a description, change, or release applies to. |
| evidence and assurance | Evidence bears on named claims; assurance evaluates warranted reliance for a use. Neither supplies authority or entails release. |
| description or status update | An episteme used for coordination. Updating it neither changes the System nor proves that the intended change was realized. |
| handover, delivery, deployment, or commissioning Work; acceptance decision | Different Work and decision results that source vocabularies often call *release*. Name the result at issue. |

The deciding, performing, permission-granting, and receiving Agents may differ. Evidence-producing Work may be
performed by another Agent. The release subject, changed System, and other affected Systems retain their own
identities and need not be Agents.

### SYSE.14:1 — Problem Frame

One controller change can alter actual Systems, interfaces, and behaviour; change needed manufacturing or service
Work; and invalidate descriptions or supporting evidence. A release for realization can lawfully precede
implementation. A release to service normally concerns an actual System in an observed configuration after
implementation. Treating both as one generic approval loses the decision subject and its evidence.

Workflow tools can coordinate records and checks, but their status labels are not the engineering ontology.
*Approved* can denote, for example, acceptance for analysis, technical selection, permission, release for build,
a gate result, an installed-state claim, or acceptance for use. Those results have different Agents, authority,
evidence, subjects, and consequences.

### SYSE.14:2 — Problem

The recurring engineering difficulty is to move fast without releasing the wrong change, the wrong unit, or a
change supported by evidence from another configuration. A usable release decision answers seven questions:

1. What identified description, software package, or actual System in which configuration may enter the named
   Work or use?
2. Which actual units, sites, intervals, and operating conditions are covered?
3. What current configuration basis connects the candidate, descriptions, and actual Systems?
4. Which affected Systems, interfaces, Work, obligations, and downstream consequences can change the choice?
5. Which Agent makes the decision, what authority obtains, and which separate permissions are required?
6. Which evidence supports which claim for this configuration and use, and what material uncertainty remains?
7. What may happen next, what remains withheld, and which change or observation reopens the decision?

Without those answers, a technically sound change can reach an incompatible unit, a valid partial release can
wait behind irrelevant approvals, or a green status can conceal missing implementation and operating evidence.

### SYSE.14:3 — Forces

Recurring tensions include:

- Routine and reversible changes benefit from fast feedback; consequential or hard-to-reverse changes need
  stronger criticism, evidence, and permission.
- Participants need one connected change case, while the request, choices, permissions, Work, transformations,
  descriptions, and decisions remain different objects.
- A local improvement can shift failure, service burden, cost, or risk to another System.
- Family descriptions support reuse, while release and service decisions can depend on serial units and installed
  configurations.
- Automated checking shortens feedback, while decision authority and any required legal, safety, commercial, or
  organizational permission need their own grounds.
- Change Work continues; one release question still needs a usable current answer.

### SYSE.14:4 — Solution

Develop one bounded release decision around the named next Work or use. Carry forward only the configuration,
consequence, authority, permission, and evidence claims that can change that decision.

#### SYSE.14:4.1 — Perform the Move

1. **Bound the release question.** State the identified description, software package, or actual System under
   consideration; its relevant configuration; the named next Work or use; the deciding Agent; the interval and
   conditions; and the current options. The option set may include release, narrower release, trial, withholding,
   rejection, or obtaining another result first.
2. **Establish the configuration and effectivity.** Use a compatible `SYSE.13` result or qualified direct sources
   for the units, descriptions, installed realizations, sites, intervals, and conditions that matter. Return a
   missing configuration result instead of guessing correspondence.
3. **Separate the trigger from the candidate.** Record the triggering event—for example, a request, criticism,
   incident, opportunity, or source change—with its evidence status. Describe viable change candidates separately.
   Keep the unchanged-System option when viable; treat deferral as a decision to await an event or obtain another
   result.
4. **Trace consequences far enough to change the choice.** Identify affected actual Systems and relations,
   descriptions, realization and integration Work, provider and receiving Agents, obligations, supporting evidence,
   and reversibility. Files, team names, and hyperlinks can locate records or Agents but do not identify the
   affected world-side objects and relations.
5. **Name the Agents and governing relations.** Identify the Agent making the release decision, Agents granting
   required permissions, Agents performing later Work, and receiving Agents. State assignments, authority,
   permissions, conflicts of interest, and abstention conditions separately.
6. **Qualify the evidence.** Connect each evidence result—for example, a test result, model evaluation, trial
   observation, specialist result, or assurance result—to the claims, configurations, conditions, and uses it
   supports. When a relied-on source changed, use a compatible `SYSE.19` result or reopen the affected claim
   directly.
7. **Compare the current options.** Hold the option set and comparison basis stable long enough to choose. State
   protected characteristics, acceptable losses, material uncertainty, and the next affordable observation that
   could change the choice. Use `C.11` for the choice itself.
8. **State and return the release decision.** Name the selected disposition, subject, effectivity, conditions,
   evidence, authority, permissions, unresolved risks, lawful next Work, withheld scope, and reopen conditions.
   If a decision-changing input is missing, return that missing result rather than *approved with caveats*.
9. **Connect later realization without inventing it.** When implementation or integration has occurred, identify
   the performing Agent, dated Work, Method, actual transformation, resulting configuration, and observations.
   Update affected descriptions and recipients, but do not use a record update as proof of realization.

This is an `A.22.CGUS` learning unfolding, not a universal Work sequence. A release for realization can occur
before implementation; release to service can depend on later implementation and observation; emergency
containment Work can precede a full technical choice under its own authority. The case must state its actual
dependencies and timing.

#### SYSE.14:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| release question | Release subject and kind, deciding Agent, receiving Work or use, current options, interval, and conditions. |
| configuration and effectivity | Identified actual Systems; actual constituents, obtaining relations, and characteristic values; relevant descriptions; supporting evidence; and the subjects and conditions to which the decision applies. |
| trigger, candidates, and consequences | Trigger with epistemic status; viable candidates; affected Systems, interfaces, Work, obligations, downstream consequences, reversibility, and retained alternatives. |
| Agents, authority, and permissions | Deciding, permission-granting, performing, and receiving Agents; assignments; direct authority and permission relations; conflicts and abstention conditions. |
| evidence and choice | Claim-sized evidence with provenance and limits; comparison basis; selected disposition; accepted losses; material uncertainty; probe-or-stop judgement. |
| decision and continuation | Released, narrowed, trial-only, withheld, rejected, or probe-again result; lawful next Work; withheld scope; blockers; withdrawal and reopen conditions. |
| later realization, when relevant | Performing Agent, dated Work, Method, actual transformation, resulting configuration, observations, description updates, recipients, and known correspondence gaps. |

The result may be carried, for example, by an issue record, release note, model view, linked engineering
records, or generated report. The decision keeps its identity and grounds across those carriers; authority,
permission, performed Work, and actual configuration remain separately established.

#### SYSE.14:4.3 — What Changes in Practice

Engineers stop treating *approved*, *merged*, *passed*, and *released* as interchangeable completion signals.
They can release a supported subset of units without pretending that the whole family is ready, and they can add
independent evidence or permission to consequential changes without imposing the same burden on every change.

The receiving Agent gets a usable next action: perform the named Work, use the released configuration, obtain a
missing result, or stop. Later implementation and operating evidence may narrow or supersede the decision without
retroactively turning the earlier decision into performed Work.

### SYSE.14:5 — Worked Case: Cold-Start Protection for Ten Pump Controllers

A pump manufacturer must decide which of ten installed controllers may enter monitored service with a cold-start
protection change. The configuration basis from `SYSE.13` distinguishes four groups:

| Installed units | Current finding | Consequence for this release |
| --- | --- | --- |
| S001–S004 | IO-A input board; candidate package supports IO-B. | Outside the candidate's hardware compatibility claim. |
| S005 | IO-B and the required sensor; current calibration evidence is missing. | Withheld until the missing evidence is obtained. |
| S006–S008 | IO-B, current calibration evidence, installed candidate realization, and chamber-test evidence. | Eligible for the current service-release comparison. |
| S009–S010 | IO-B; database says *installed*, but current calibration and cold-start evidence are absent. | Trial or service release is not supported by the current evidence. |

The original request asked for release to all ten units. The engineering team retained three real options:
withhold the change; release it to monitored service on S006–S008; or extend a trial to S006–S010. The last option
failed the stated calibration-evidence threshold. Withholding avoided change risk but left an observed cold-start
failure mode uncorrected on the three eligible units.

The release board acts as the deciding Agent and has authority for this service-release decision. An independent
safety team acts as the permission-granting Agent; its permission covers only S006–S008, the named temperature
envelope, and the monitoring interval. Assignment to either team is recorded separately from authority.

The controller-integration team had already performed the installation Work on S006–S008. The firmware package
description, installation record, software attestation, and physical inspection are separate sources for the
resulting configuration claim. A revised calibration source had reopened only the cold-start claim. Chamber tests
for S006–S008 restored that evidence. A maintenance observation showed restored pump-train functioning for S006
under one load and temperature interval; it added evidence for S006 only and established neither safety nor the
state of S007–S008.

The release decision therefore admits S006–S008 to monitored service under the stated conditions. S005 and
S009–S010 remain withheld pending calibration and cold-start evidence; S001–S004 remain outside hardware
compatibility. The next Work is monitored service, not another installation inferred from the decision. A sensor
replacement, firmware change, calibration-source change, cold-start failure, or operating-envelope change
reopens only the affected unit and claim.

The decision can supply bounded evidence to `SYSE.4`, whose assurance Work may still find an unsupported claim or
return a blocker. The release decision itself establishes no assurance conclusion.

**When the full pattern is unnecessary.** A reversible internal script has one known configuration, no physical
effectivity question, and an established deployment Method that already supplies the needed choice, evidence,
permission, Work, and rollback results. Use those direct patterns instead of constructing a connected engineering
release case.

### SYSE.14:6 — Bias Annotation

A document-control Method can turn every change into a long approval chain. A software workflow can treat a
green pipeline result as universal release authority. Scale scrutiny to consequence and reversibility while keeping
actual Systems, descriptions, evidence, authority, permission, and performed Work distinct.

Official procedures, vendor workflow labels, and declared conformance support claims about their records or
requirements. Actual enacted practice, effectiveness, and configuration need their own evidence. Use expert
judgement with an explicit epistemic status when broader field evidence is unavailable.

### SYSE.14:7 — Conformance Checklist

- [ ] One release subject, release kind, receiving Work or use, deciding Agent, and current option set are stated.
- [ ] The configuration basis concerns the same actual Systems, descriptions, conditions, and release question.
- [ ] Trigger, change candidate, technical choice, authority, permission, release decision, performed Work, actual
      transformation, configuration, evidence, assurance, status, and transfer remain distinct.
- [ ] Consequence tracing reaches affected Systems and direct relations, not only files, departments, or links.
- [ ] Every relied-on authority, permission, and evidence result has the subject, scope, interval, and source
      needed by the decision.
- [ ] The comparison basis, selected disposition, retained alternatives, acceptable losses, material uncertainty,
      and probe-or-stop judgement are recoverable.
- [ ] Any claimed implementation identifies the performing Agent, dated Work, Method, actual transformation,
      resulting configuration, and evidence.
- [ ] The result states lawful next Work, withheld scope, blockers, and the smallest withdrawal and reopen
      conditions.

### SYSE.14:8 — Common Failures and Repairs

These recurring release errors change the next permissible action:

| Failure | Repair |
| --- | --- |
| Request equals decision | Keep the request as a trigger and compare viable change options. |
| Signed form supplies authority | Identify the deciding Agent and the authority relation for this decision. |
| Gate pass equals release | Use the gate result as one premise and state the release subject, kind, and effectivity separately. |
| Release equals implementation | Identify performed Work and actual transformation, or state that they remain future. |
| Updated status equals actual configuration | Obtain evidence about the identified units and keep the status as a claim. |
| Apply one software pipeline to every engineered System | Select review, automation, assurance, and permission by consequence, reversibility, and the actual System or intended-system designator selected as the project system-of-interest. |
| All units inherit one release | Name supported units and conditions; narrow or withhold the rest. |
| A changed source reopens everything | Trace the changed claim and repeat only the affected decision. |

### SYSE.14:9 — Consequences

Release speed and scrutiny can vary with consequence without losing accountability. Implementation, operation,
maintenance, and assurance receive a decision that names configuration, effectivity, evidence, authority, and
next Work. Mixed physical and software changes can share one connected case without pretending that their Work
cadence or evidence is identical.

Consequential cases cost additional impact recovery, evidence maintenance, and authority checks. Some decisions
must remain narrowed or blocked. Specialist rules—for example, safety, legal, cybersecurity, medical, aviation,
financial, commercial, or organizational rules—remain with their own patterns and application DPFs.

### SYSE.14:10 — Rationale

The useful unit is one decision about one subject entering one named Work or use, not an administrative change
form. This boundary lets contributors see how configuration, consequences, evidence, authority, and permissions
bear on the same current choice while preserving each result's identity.

Effectivity makes partial release possible when evidence differs by unit or condition. Explicit reopen conditions
let engineering continue without keeping the present decision open forever or silently applying it to a changed
configuration.

### SYSE.14:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R8 `GI-19`, `GI-71`, `GC-08`, and the connected configuration/change discussions | Separate request, criticism, technical decision, permission, release, implementation, effectivity, status, and transfer; continue engineering beyond one release. | Lifecycle and document-control language is normalized to continuing Work and current FPF ontology. |
| Frank B. Watts, *Configuration Management for Senior Managers* (2015), historical practitioner lineage | Manufacturing cases distinguish request screening, technical release, effectivity, implementation, status accounting, field change, delay, and collision. | Central departments, phase spine, paper forms, sanctions, and universal metrics are not retained. |
| [Beibl and Krause 2024](https://doi.org/10.1017/pds.2024.253) | Interviews at one automotive manufacturer show different affected-component and downstream-change problems in development, production, and customer-owned contexts. | One company supports recurrence and viewpoint differences, not a universal Method or prevalence claim. |
| [Gangl, Gollmann, and Gruchmann 2024](https://doi.org/10.1016/j.procir.2024.01.090) | One automotive case shows that change continues beyond released engineering data into master-data changes and plant implementation. | One company and one comparator do not establish a universal sequence. |
| [DORA, “Streamlining change approval,” updated 2025-10-30](https://dora.dev/capabilities/streamlining-change-approval/) | For routine software changes, current guidance favours peer review and automated feedback while retaining stronger scrutiny for detected high-risk changes. | The evidence is software-specific and partly correlational; it does not remove physical configuration, independent assurance, permission, or domain release authority. |
| [Zampetti et al. 2022](https://doi.org/10.1145/3571854) | Interviews and survey evidence show mixed continuous and periodic builds, simulation, hardware-in-the-loop, deployment, feedback, and hardware/software expertise. | Limited generalizability; no single pipeline, cadence, or complete automation is implied. |

Use source scope and expert judgement rather than treating standards authority, academic visibility, vendor
promotion, or self-reported adoption as evidence of actual prevalence or effectiveness.

### SYSE.14:12 — Relations

- `C.11` governs choice among current options. `A.21` governs a gate decision. `A.2.8.PER` governs permission,
  `A.15.1` Work, `A.3.4` actual transformation, `F.10` status, `A.10` evidence, and `B.3` assurance. This pattern
  composes their results for one engineering release and replaces none of them.
- `C.2.1`, `E.17`, and `E.24.PUB` keep change descriptions, decision epistemes, publications, forms, and carriers
  distinct from the changed System and performed Work.
- A compatible `SYSE.13` result supplies configuration and effectivity only for the same change and release use.
  It establishes neither permission nor release.
- A compatible `SYSE.19` result supplies revision consequences only for decisions that relied on the changed
  source. Co-use does not impose a universal temporal order.
- Restored-function evidence from maintenance or operation can support only the same actual System,
  configuration, conditions, and claim. It neither selects the change nor authorizes release.
- `SYSE.14` can supply bounded evidence to `SYSE.4` for the same release question and evidence window. `SYSE.4`
  performs its own assurance Work.
- Application moves—such as software deployment, electrical energization, medical-device release, ship
  alteration, building commissioning, or manufacturing release—may specialize the Method because their project
  Systems-of-interest, permissions, evidence, and effectivity differ. They are not synonyms merely because each can use this pattern.

### SYSE.14:End

<a id="syse-19"></a>
## SYSE.19 — Revalidate Engineering Decisions When a Relied-on Source Changes

### SYSE.19:0 — Use This When

Use this pattern when an engineering decision relied on a claim in a model, requirement, standard,
MethodDescription, supplier specification, research result, or another engineering source, and a later edition or
replacement may change that claim. The project needs to know which decisions remain usable and which need new Work.

Begin with the predecessor and later source epistemes. Compare the claims that can change engineering action, then
recover decisions and Work results whose stated reasoning depends on those claims. Revalidate only the affected
use; a new file or edition label is only a cue to inspect.

The first useful result is a **bounded source-change impact decision**. It states which engineering decisions remain
usable, which are narrowed or reopened, what revalidation Work is needed, what cannot yet be decided, and what the
project does next. Later performed Work, returned evidence, and a replacement engineering decision are separately
identified results.

Use `SYSE.14` when the engineered System or its release is changing, and `SYSE.13` when configuration identity and
effectivity are the main question. Use `SYSE.7` to maintain several descriptions used by one decision and `SYSE.10`
to qualify new model, experiment, or trial evidence. Use FPF `E.15` when an FPF pattern edition itself changes.

### SYSE.19:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| engineering source | A claim-bearing episteme that an Agent uses while performing engineering Work. Record its publication, carrier, or access relation only when that relation changes the use. |
| source edition | An episteme related to an earlier episteme by the `C.2.1` edition-continuity predicate. A revision label or date is evidence to inspect, not the edition relation itself. |
| replacement source | A later episteme proposed for the predecessor's use when edition continuity is absent or unresolved. Its applicability is decided for that use. |
| publication or carrier change | A change to availability or presentation—for example, another URL, file, layout, form, or publication occurrence. Compare claim content before treating it as a semantic change. |
| material claim change | A change in claim content or applicability that can alter engineering action—for example, a changed proposition, scope, assumption, limit, evidence status, or MethodDescription statement. |
| direct reliance | A named engineering decision or Work result whose justification or content depends on a source claim as a premise under stated conditions. A citation or link is discovery evidence until the receiving content confirms that dependence. |
| affected reach | The smallest set of decisions reached through direct-reliance relations whose engineering action can change because of the material claim change. |
| revalidation Work | Work that rechecks an affected claim or decision under the current configuration, conditions, Method, evidence needs, and authority. |
| decision disposition | One choice from the closed set used here: `preserve`, `narrow`, `reopen`, `supersede`, `withdraw reliance`, or `blocked`. |

The source episteme, its publication, the claim-change observation, planned revalidation, performed Work, returned
evidence, and engineering decision have separate identities. An Agent performs revalidation Work. Equipment,
models, repositories, and the engineered System are examples of other participants; state each direct relation.

### SYSE.19:1 — Problem Frame

Engineering decisions depend on changing sources. For example, a supplier can revise a material limit, a standard
can change an interface claim, a MethodDescription can narrow an operating range, or a research result can weaken
an evidence line. The engineered System may stay unchanged while the warranted decision basis changes. Conversely,
a new carrier or revision label may leave every relied-on claim intact.

The project needs two kinds of continuity. Historical source and decision identities stay recoverable so earlier
Work can be understood. Current decisions reopen only where a relied-on premise changed. Repeating everything is
expensive and hides the reason for change; comparing only files can miss a one-sentence change that alters release.

This pattern specializes source-change impact for engineering decisions. It connects changed claims to their
actual use in engineering Work and returns a bounded revalidation decision for the current configuration.

### SYSE.19:2 — Problem

Two shortcuts cause most of the damage. Version-based reopening repeats every downstream activity merely because
the source label changed. Carrier-based preservation keeps every decision merely because the engineered System did
not change. Both avoid the central question: which relied-on claim changed enough to alter engineering action?

Other recurring failures appear when the source episteme cannot be identified, reliance is known only at document
level, a semantic difference is confused with a text diff, revalidation uses the wrong configuration, or a passing
test is treated as permission or release. The project then either spends effort without a decision or keeps a
decision whose premise no longer applies.

### SYSE.19:3 — Forces

Recurring tensions include:

- Revalidation should stay bounded, while an undeclared reliance can matter more than a declared trace link.
- Source identity must remain recoverable without turning every carrier change into a semantic event.
- One changed sentence can alter release; a large rewrite can leave the relied-on premise intact.
- Automated search can find candidate uses, while materiality and applicability still need engineering judgement.
- A newer official or popular source can fit the use worse than an older bounded source.
- Preserved decisions remain usable only when the reason for preservation is recoverable when later Work needs it.

### SYSE.19:4 — Solution

Compare source claims, recover their actual engineering uses, and perform the smallest decision-closed revalidation
that can change the current engineering result.

#### SYSE.19:4.1 — Perform the Move

1. **Name the receiving decision.** State the engineering decision at risk, any relied-on Work result, the current
   configuration and use, the relevant interval, and the action that could change.
2. **Identify the source epistemes.** Recover the predecessor and later claim-bearing epistemes, their applicability,
   provenance, and publication or carrier facts when those facts matter. Establish an edition relation only when
   its predicate obtains; otherwise treat the later source as a replacement candidate or record an identity gap.
3. **Compare claims rather than files.** State every material change in claim content or applicability—for
   example, proposition, scope, assumptions, limits, evidence status, or MethodDescription content. Classify the
   remaining differences as publication or carrier changes.
4. **Recover direct reliance.** For each material claim, inspect candidate receiving content found by means such
   as search, citations, traces, or AI assistance. State the decision or Work result and the direct premise or
   evidence-use relation that connects it to the claim.
5. **Bound the affected reach.** Give each candidate use one of three discovery dispositions: `depends`, `mentions
   only`, or `unresolved`. Follow a `depends` branch only while a downstream engineering action can still change.
6. **Choose revalidation Work.** Name the Agent, Method, current configuration and conditions, evidence needed,
   authority, cost, and stop. Select only the Work needed by the material claim—for example, analysis, model use,
   comparison, test, trial, verification, assurance, permission check, or decision Work.
7. **Perform and qualify the Work.** Identify performed Work and returned evidence separately. State what the new
   result supports for the current configuration and what remains unknown.
8. **Decide at engineering-decision grain.** Assign one decision disposition from the closed set in section 0.1 and
   state its reason, evidence, applicable interval, and next Work. A passing check becomes a decision premise only
   when authorized decision Work uses it.
9. **Supply the result and preserve history.** Give the Agent making the relevant engineering change or release
   decision the affected and preserved decisions, revalidation evidence, blockers, and next Work. Keep earlier
   source editions and decisions recoverable for their original uses and intervals.
10. **Stop at bounded dependency closure.** Finish when every material changed claim has a disposition for every
    actual in-scope use, or when a named gap—for example, a missing source, applicability fact, evidence, capability,
    or authority—prevents the next decision.

The numbered presentation is an `A.22.CGUS` learning unfolding, not a lifecycle or a required Work sequence.
Source comparison, design, testing, operation, and release Work may overlap. Only dependencies established for the
current claims impose an order.

#### SYSE.19:4.2 — Record the Result

Record only the content needed by the receiving decisions.

| Result position | Required content |
| --- | --- |
| receiving decision | Engineering decision, any relied-on Work result, current configuration and use, relevant interval, deciding Agent, and action that may change. |
| source comparison | Predecessor and later or replacement epistemes; material claim changes; publication or carrier changes; source-access and identity gaps. |
| direct reliance | Every affected decision or Work result, the source claim on which it depends, and the premise or evidence-use relation that establishes the dependence. |
| affected reach | `depends`, `mentions only`, or `unresolved` for each candidate use; downstream closure at the last action-changing decision. |
| revalidation | Planned and performed Work, Agent, Method, configuration, conditions, evidence needs, authority, results, cost, and stop. |
| decision dispositions | One disposition from section 0.1 for each affected decision, with reason, evidence, interval, and next Work. |
| continuation | Receiving Agent and decision, remaining gaps, historical source and decision references, and the condition that reopens this result. |

For example, a compact table, linked decision note, model query result, or generated report may present this
episteme. Treat the form as a representation; keep the source claims and direct-reliance relations recoverable.

#### SYSE.19:4.3 — What Changes in Practice

Engineers stop using a source version as a proxy for impact. A source update can matter while the engineered System
stays unchanged because the warranted decision basis changed. A carrier update can leave engineering decisions
usable when claim content and applicability remain compatible.

Revalidation produces a bounded decision result: it identifies decisions that remain usable and decisions that
need new Work. Search and AI-assisted comparison reduce discovery effort, while an Agent with suitable capability and
authority judges materiality and applicability.

### SYSE.19:5 — Worked Case: A Changed Sensor-Calibration MethodDescription

A pump-controller project used edition E2 of a sensor-calibration MethodDescription. E2 states that temperature
compensation for sensor module `TS-2` is valid from `-20 °C` to `50 °C`. The supplier publishes E3 under the same
edition scheme. E3 narrows ordinary validity to `-10 °C` through `50 °C`; lower-temperature use now requires a new
calibration Method and evidence.

The source-impact team has authority to classify engineering reliance but not to release controller units. It
compares the two claim-bearing epistemes and finds four candidate uses of the old temperature claim:

1. the thermal model uses it as a cold-start parameter bound;
2. the cold-start test MethodDescription uses it as an acceptance condition;
3. the safety claim uses evidence produced under that condition; and
4. the interface architecture description cites E2 only in its bibliography.

Inspection gives the first three uses `depends` and the bibliography citation `mentions only`. The interface
decision and room-temperature evidence therefore remain usable. The cold-start model, test criterion, and service-
release premise enter the affected reach.

The team chooses three revalidation Work occurrences. A modeling Agent revises the cold-start model. A calibration
Agent performs the new low-temperature calibration for units `S006`–`S008`. A test Agent performs the chamber test
under the current hardware, interface, sensor, and firmware configuration. Each Work occurrence has its own Method,
result, and evidence.

The returned evidence supports cold-start use for `S006`–`S008` under the tested conditions. Units `S009` and
`S010` still lack calibration evidence. Units `S001`–`S004` use another hardware configuration, so this changed
claim does not reach their release premise.

The bounded source-change impact decision now:

- preserves the interface decision and room-temperature evidence;
- supersedes the old cold-start model parameter and test criterion for current use;
- preserves cold-start release eligibility for `S006`–`S008` under the new evidence;
- reopens the release premise for `S009` and `S010`; and
- supplies the result to `SYSE.14`, where the authorized Agent makes the service-release decision.

Each bullet applies one disposition from section 0.1 to a named decision branch.

**Carrier-only countercase.** The supplier republishes the same E3 episteme at another URL with a new PDF layout.
The publication and carrier facts change; claim content, applicability, and direct use stay compatible. The source
record is updated and the engineering decisions remain preserved.

**World-change boundary.** Replacing an actual `TS-2` sensor is a configuration and world-side engineering change.
Use `SYSE.13` and `SYSE.14` for that change.

### SYSE.19:6 — Bias Annotation

A newer official source deserves inspection because its claims or authority may matter. Official status,
publication volume, and academic attention describe the source and discourse. Project use and effectiveness need
evidence about performed engineering Work and outcomes.

Search, dependency graphs, and AI summaries can find candidate uses. Actual reliance still depends on the receiving
claim or decision, and authority remains with the Agent who holds it.

### SYSE.19:7 — Conformance Checklist

- [ ] The predecessor and later or replacement source epistemes are identified.
- [ ] Edition continuity is established under `C.2.1` or left unresolved.
- [ ] Material claim changes are separated from publication and carrier changes.
- [ ] Every affected use names the source claim, receiving decision or Work result, and direct-reliance relation.
- [ ] Every candidate use receives `depends`, `mentions only`, or `unresolved`, and tracing stops at action-changing
      dependency closure.
- [ ] Revalidation Work names its Agent, Method, configuration, conditions, evidence needs, authority, result, and
      stop.
- [ ] The decision episteme, performed Work, evidence, permission, assurance, and release decision are grounded
      separately.
- [ ] Historical source editions and decisions remain recoverable for their original uses and intervals.
- [ ] The receiving Agent gets a usable decision disposition, blockers, and next Work.

### SYSE.19:8 — Common Failures and Repairs

| Recurring failure | Repair |
| --- | --- |
| A new version triggers a full rerun | Compare claims and trace actual reliance; reopen only action-changing dependent reach. |
| A small text diff is assumed harmless | Ask what a relying engineer may now do or conclude differently. |
| A new file is treated as a new source meaning | Separate source episteme, edition relation, publication, and carrier. |
| A trace link is treated as reliance | Inspect the receiving content and state the direct-reliance relation. |
| No physical change is treated as no impact | Recheck the epistemic basis of engineering decisions. |
| A passing test is treated as the decision | Ground evidence-producing Work, evidence use, decision Work, and authority separately. |
| The latest official source wins automatically | Compare applicability and evidence for the named use. |
| `Pending review` hides the blocker | Name the missing source, claim content, applicability fact, evidence, capability, or authority. |

### SYSE.19:9 — Consequences

Source refresh becomes proportional. Decisions remain stable when their premises remain compatible, while one
material claim can reopen a release even if the engineered System is unchanged. Historical sources and decisions
remain inspectable, and automated discovery can reduce effort without becoming decision authority.

The cost is claim-level source identification and maintenance of actual reliance. When source content or
applicability cannot be obtained, the Agent applying this pattern records a named blocker. Application DPFs may add source controls for
domains such as regulated products, software supply chains, clinical devices, finance, or contracting.

### SYSE.19:10 — Rationale

The pattern separates a changed source claim from a world-side engineering change. A changed episteme can alter the
warranted basis of a decision while the engineered System remains unchanged. Revalidation Work and later
engineering change therefore receive separate identities.

Claim-sized dependency closure is the lowest-cost adequate unit. File-level closure is too broad, while token-level
comparison cannot establish engineering meaning or reliance. Preserving source editions, actual uses, performed
checks, and decision dispositions makes the Method replayable with project-local trace sources.

### SYSE.19:11 — SoTA and Source Use

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| R5.6:32 and `CS-R5.5-02` | Separate source episteme, Agent, MethodDescription, performed Work, decision, evidence, edition change, applicability, and affected use. | Use the guide as practitioner synthesis and case material; qualify each claim under current FPF ontology and evidence rules. |
| Current FPF `C.2.1`, `A.10`, `E.15`, and `G.11` | Episteme and edition identity, claim-bound evidence, affected-use inspection, and bounded refresh. | `E.15` governs FPF pattern editions; this DPF supplies the engineering source-use specialization. |
| [Wu et al. 2025](https://doi.org/10.1016/j.aei.2025.103490) | One landing-gear case demonstrates tool support for heterogeneous model semantics, conflict handling, traceability, and versioning. | Use the case for candidate impact discovery; establish reliance, configuration change, and release authority separately. |
| [Hernández, Moros, and Nicolás 2023](https://doi.org/10.1007/s00766-023-00396-w) | A multivocal mapping reports requirements Work continuing through DevOps with changing descriptions and monitoring. | The software-heavy review supports this recurring source-change problem, not a universal requirement or revalidation Method. |
| [Norheim et al. 2024](https://doi.org/10.1017/dsj.2024.8) | Analysis of LLM use in requirements Work exposes source, consistency, verification, and cyber-physical limits. | Use generated summaries for candidate discovery; ground engineering evidence and decisions separately. |
| [Kosenkov et al. 2025](https://doi.org/10.1016/j.infsof.2024.107622) | Regulatory-compliance research connects legal interpretation, engineering descriptions, evidence, and change Work. | The mapping study supplies candidate relations; the applicable legal interpretation and permission need their own authority. |
| [Bantwal and Fatahi Valilai 2026](https://doi.org/10.1007/s00170-025-17175-2) | A brake-caliper case exposes change propagation across physical parts, descriptions, supply constraints, engineering tools, and validation. | Use its links as candidate affected reach; inspect actual reliance before reopening a decision. |

Currentness claims carry an epistemic status. Signals such as academic attention, institutional promotion, a
supplier's `latest` label, or public reporting are evidence about communication. Use direct observations or
qualified expert estimates for enacted engineering practice, prevalence, and effectiveness.

### SYSE.19:12 — Relations

- `C.2.1` governs source-episteme identity and edition continuity. `E.17` and `E.24.PUB` govern publication forms,
  carriers, audiences, and availability.
- `A.10` governs claim-bound evidence, `B.3` assurance, and `C.11` the later choice. This pattern adds the direct-
  reliance and affected-reach move for engineering source changes.
- `E.15` applies when an FPF pattern edition changes. `G.11` supplies only its declared Part-G refresh results.
- A compatible `SYSE.7` result can supply a MethodDescription or representation use for the named claim. A
  compatible `SYSE.10` result can supply evidence for the same engineering claim, configuration, decision, and
  evidence interval.
- `SYSE.19` supplies source-change feedback to `SYSE.14`; the authorized Agent in `SYSE.14` still chooses and
  releases any world-side engineering change.
- `SYSE.13` and `SYSE.14` govern configuration and world-side engineering change. An episteme edition relation is
  used only as source-change input.
- Application profiles may specialize this Method for domains such as software supply chains, electrical parts,
  regulated products, medical devices, ships, or buildings. A specialization adds an action-changing source or
  revalidation distinction.

### SYSE.19:End

# Part V — Assurance, Method and Work Architecture, Repertoire, and Cultural Continuation

<a id="syse-4"></a>
## SYSE.4 - Select an Engineering Challenge and Qualify Evidence Use

> **Primary working result:** either an engineering-assurance plan for a future challenge or an
> engineering-assurance account for evidence that already exists. The plan names one claim whose use matters to a
> decision, one challenge or evidence need, the conditions and configuration that bound it, and the earlier answer
> the practitioner must reassess if reliance changes. The account additionally names dated Work and its direct
> result, the descriptive `A.10` evidence/provenance path, current validity limits, changed reliance, and the affected
> earlier answer. These are DPF-local names for claim-bearing working epistemes, not new U-kinds. When challenge
> Work remains future, a separate `A.15.2` WorkPlan coordinates it. Both DPF results are claim-bearing
> epistemes. Establish target-claim support, performed tests, evidence currentness, and decision authority through
> their direct results and relations.

### SYSE.4:1 - Problem frame

Use this pattern when an engineering decision depends on a claim from project focus, use and system concepts,
architecture, realization, or a specialist practice, but the project cannot yet say what challenge could change
reliance on that claim. Also use it when an engineering result—for example, a test, simulation, model, measurement, inspection,
acceptance record, certificate, or operating observation—is being treated as proof beyond the conditions it
actually addresses.

First useful move: write five lines.

1. **Claim:** the named claim episteme and the subject, conditions, configuration, and time for which it is used.
2. **Decision question:** the current question or contemplated decision whose answer would change if reliance changes.
3. **Challenge:** one measurement, analysis, simulation, test, integration check, inspection, or operating
   observation capable of changing that reliance.
4. **Validity boundary:** the configuration, conditions, scale, uncertainty, and currentness limits that matter
   to this use.
5. **Affected earlier answer:** the project-focus, concept, architecture, realization, or specialist answer that
   the practitioner must reassess if the result does not support present reliance.

This five-line form is a learning and presentation unfolding, not a WorkPlan or a claim about the order of
performed Work. It is enough for the engineering-assurance plan. When challenge Work remains future, use
`A.15.2` for a separate WorkPlan: its present EntityOfConcern, effective reference scheme, horizon, and the
smallest PlanItem that coordinates the intended Method, performer or local role condition, window, capability,
resource, dependency, and result target. The engineering-assurance plan references that WorkPlan; the five
lines do not constitute it. Expand the assurance plan only when the decision question depends on several evidence
kinds, configurations, conditions, scales, or uncertainty sources. When evidence already exists, add the dated
Work, direct result, descriptive `A.10` evidence/provenance path, current validity limit, changed reliance, and
affected earlier answer to obtain the engineering-assurance account.

If this move is missed, checks are often chosen after an architecture or implementation is already treated as
settled. A passed component test can then stand in for System behaviour and outside benefit; a model confidence
score can stand in for validity; or acceptance, certification, permission, release, and assurance can collapse
into one pass/fail label. The earlier claim remains unchanged even when the evidence applies to another
configuration or contradicts its use conditions.

The payoff is decision-centred evidence use. Engineers ask what result could change the current decision,
recover the actual evidence through direct FPF patterns, and revise only the earlier answer to which the result
applies. Engineering assurance can therefore accompany other Systems Engineering Work without becoming a
terminal stage or a fixed test programme.

Use this pattern when the project must choose or interpret a challenge for an engineering decision. Use `A.10`
when the remaining question is only provenance for an already named bounded evidence use, `C.16` for measurement
validity, `C.32.ACE` for an architecture-characteristic eval programme, `A.1.1` for model applicability or use
under stated conditions, and `C.28` for a causal-use claim. Use `B.3` only when an assurance claim or material
reliance threshold is current. Neighboring specialist questions—for example, safety, security, ethics, legal compliance, finance,
certification, acceptance, permission, or release—retain their own criteria, Methods, Work, and decisions.

At the first consequential use of an assurance cue such as *verification*, *validation*, *test*,
*acceptance*, *certification*, or *assurance*, ask: **which claim is relied on, for which decision?** Name the claim, the challenge or obtained
result, its configuration and conditions, and the decision question whose answer can change. Source terminology
remains a retrieval cue until those distinctions are recoverable.

### SYSE.4:2 - Problem

Systems Engineering decisions rely on different claims. A project-system choice relies on a use and boundary
account. A system concept relies on proposed participation and outside effects. Architecture relies on
functioning, selected structures, characteristics, and feasibility. A realization branch relies on transformer
Systems, capabilities, Methods, resources, interfaces, integration, and configuration. Each claim can fail for
a different reason and needs a different challenge.

Engineering sources offer many useful checks, for example observation, measurement, calculation, review, analysis,
simulation, prototype, component test, integration test, Hardware-in-the-Loop, inspection, operational
monitoring, audit, and assurance argument. Their names do not say which claim they support. A pump bench test can
support a component capability claim but not the station's downstream effect. A software acceptance record can
support a bounded acceptance decision without establishing production benefit. A structural analysis for an
empty building can be inapplicable to one occupied retrofit configuration.

The practical problem is to select a challenge from the claim and decision question, perform or recover the
relevant Work and result, state the limits of its use, and revise the smallest affected answer. This must remain
possible before realization, during change and integration, and after the System participates in use.

### SYSE.4:3 - Forces

| Force | Tension |
| --- | --- |
| Early challenge and sufficient warrant | A cheap early check can expose a bad claim, while consequential reliance may require several independent evidence lines. |
| Models and physical evidence | Models and simulations can explore inaccessible conditions, while their applicability, error, uncertainty, and extrapolation limit what they warrant. |
| Automation and claim scope | Automated checks provide frequent feedback, while automation does not enlarge the claim, configuration, or decision they address. |
| Component result and outside effect | A component can meet its technical criterion while the containing System or affected environment fails the use claim. |
| Stable records and changing reality | Evidence can be replayed, while configuration, environment, source, calibration, policy, and time can make its use stale. |
| Common engineering move and specialist depth | Systems Engineering must connect challenges to engineering decisions, while specialist practices define their own criteria and Methods. |
| Local revision and terminal gate | Evidence should change only the smallest earlier answer to which it applies, while a late pass/fail ritual encourages a one-way lifecycle. |

### SYSE.4:4 - Solution

#### SYSE.4:4.1 - Select one load-bearing claim and decision question

Start with one named claim episteme already used by a current engineering question. It may come, for
example, from a project-system choice account, a linked use-and-system concept, a `C.30` or `C.32` architecture
result, a `SYSE.3` realization branch, or a specialist result. Recover:

- the claim's subject and predicate;
- its scope, conditions, configuration or version, and temporal stance;
- the result or source account from which the claim came;
- the current uncertainty or failure mode; and
- the decision or intended Work that would change if reliance narrows, stops, or becomes stronger.

*Load-bearing* is ordinary wording for this decision-specific use. It adds no claim kind or intrinsic property.
The same claim may be load-bearing for one decision and incidental for another. Name the decision question
before selecting a challenge; a generic wish to increase confidence does not yet select assurance Work.

The decision may still be contemplated. Record in the plan what result is meant to inform it. Establish any
later decision occurrence, choice, gate passage, permission, acceptance, or release through its direct relation
and evidence.

#### SYSE.4:4.2 - Reuse current evidence or choose a challenge that can change reliance

Before selecting or planning new challenge Work, check whether current engineering result epistemes already
contain or cite evidence and relations the practitioner can use:

- a compatible `SYSE.10` engineering claim assessment may contain claim-sized evidence-use relations for the same
  claim, decision, subject, configuration, use, conditions, interval, and evidence window;
- a compatible `SYSE.11` bounded usable-increment result may contain integration and observed-use evidence for the
  same actual System, configuration, use, conditions, interval, and evidence window; and
- a compatible `SYSE.14` change-and-release decision may cite evidence, configuration and effectivity
  basis, and unresolved conditions for the same release question, configuration, effectivity, interval, and
  evidence window.

Use only the compatible claims and cited evidence, not a neighbouring decision or authority. If the needed
evidence already exists, recover the direct result and its descriptive `A.10` evidence/provenance path, then write
the engineering-assurance account without creating another WorkPlan. Without a compatible current result, use a qualified direct source. If that still leaves a gap, record the
missing result and plan the smallest challenge that can close it. Availability or a familiar result name establishes no evidence use.

For a remaining evidence gap, ask: **what observable or computed result would justify keeping, narrowing,
replacing, or stopping reliance on this claim for the decision?** Choose the smallest challenge that can answer
that question. Examples include:

- a `C.16` measurement of one declared Characteristic;
- a `C.32.ACE` evaluation over existing architecture-characteristic criteria;
- a model, simulation, or analysis whose applicability and uncertainty are explicit;
- a component, integration, or system test against one stated expectation;
- an inspection or review with an identified subject and criterion;
- an operating observation under the configuration and conditions named by the claim; or
- a specialist safety, security, legal, ethical, financial, certification, or acceptance result required by the
  decision question.

State the challenge's intended Method, subject, configuration, conditions, scale or criterion, uncertainty
treatment, time window, intended result form, and intended evidence use. When Work is still intended, put performer,
local system-role-kind condition, Method, window, capability needs, resources, dependencies, and result target
in a separate `A.15.2` WorkPlan. The engineering-assurance plan cites that WorkPlan; it is not the WorkPlan.

Choose an independent or specially authorized performer only when the specialist rule governing the decision
requires one. Systems Engineering identifies that need but does not invent independence, authority, competence,
or approval from a job title or organizational boundary.

#### SYSE.4:4.3 - Write the engineering-assurance plan

Write the first result in the five-line form from the Problem frame. The result is usable when a practitioner can
recover:

1. one named claim and its current use conditions;
2. one decision question;
3. one challenge and, when future Work needs coordination, a reference to its separately identified `A.15.2`
   WorkPlan;
4. the configuration, validity, uncertainty, and currentness boundary; and
5. the earlier answer the practitioner must reassess if the challenge does not support present reliance.

The engineering-assurance plan is a C.2.1 claim-bearing episteme. Its one EntityOfConcern is the named
load-bearing claim episteme. Its ClaimGraph states the planned challenge, decision question, validity boundary,
and possible affected earlier answer as claims and references concerning that target claim. The other named
entities remain participants in those claims rather than a composite subject. Use `C.2.1` to identify the claim
content, target claim, and effective reference scheme. The plan performs no Work. Changed identity-bearing content
can identify another episteme. A later engineering-assurance account is not automatically an edition of the plan
merely because a file or identifier is reused; claim identity and any edition relation remain with `C.2.1`.

Stop at this plan when it makes the next evidence-producing Work and possible revision target explicit. Expand
to a fuller artifact—for example, a test matrix, evidence graph, assurance case, or release process—only when the
receiving decision needs it.

#### SYSE.4:4.4 - Recover performed Work, direct results, and evidence use

When the challenge is performed, identify the dated Work and performer through `A.15.1` and the applicable
assignment and Work-attribution patterns. Then use the direct pattern for the result:

- `C.16` for a measurement result, its uncertainty, and comparability;
- `C.32.ACE` for an architecture-characteristic eval programme and its separately typed result;
- `A.1.1` for model applicability, actual model use in assigned Work, or fixed-content coherence;
- `C.28` when the conclusion is causal rather than merely observational;
- the applicable test, comparison, acceptance, safety, security, legal, certification, or other specialist
  result pattern when that is the actual claim.

Use `A.10` to make the descriptive claim-bound evidence/provenance path replayable. Keep the source, carrier,
performed Work, result, result episteme, provenance relation, currentness assessment, evidence use, assurance
result, and decision question distinct. The path represents independently established relations; it moves no
result and creates no evidence relation. Use `G.11` and `C.27.TA` when source currentness, evidence age, calibration,
configuration time, observation window, or decay changes admissible use.

A planned challenge is not evidence. A performed test is not its result. A result becomes evidence for this
claim only through the named use and its conditions. Provenance, repetition, automation, or a familiar tool does
not widen that use.

#### SYSE.4:4.5 - Update the engineering-assurance account

After evidence is available, write an engineering-assurance account that names:

1. the named target claim and decision question;
2. the actual challenge Work and its direct result;
3. the descriptive `A.10` evidence/provenance path and currentness basis;
4. the result's configuration, condition, scale, uncertainty, and applicability limits;
5. the practical change in reliance for this decision; and
6. the smaller earlier answer, specialist question, or next challenge affected by that change.

The account remains a C.2.1 episteme about the named target claim. Its ClaimGraph adds claims about performed
Work, direct results, evidence use, changed reliance, and the affected earlier answer. Those named participants do
not become a composite EntityOfConcern.

State the reliance change in ordinary language: the claim remains usable for the decision within the stated
limits; the practitioner must narrow reliance; the practitioner must replace or withdraw the claim for this use;
or available evidence leaves the question unresolved. These are case conclusions, not a new universal status
enumeration. When the current question is an assurance claim or material reliance threshold, use `B.3` for the
named assurance-result claim or no-assurance disposition. The engineering-assurance account cites that result;
it does not replace it.

An unresolved result is useful. Use it to identify the missing input—for example, a configuration, comparator,
observation window, calibration, causal link, specialist criterion, or independent challenge—then plan one next
Work item. Do not
turn missing information into a negative engineering claim.

#### SYSE.4:4.6 - Combine evidence only for the decision question

Some decisions depend on several evidence lines—for example, model predictions, physical tests, integration
results, operating observations, and specialist arguments. Keep each direct result and evidence use visible. Combine them
only through the composition or assurance rule needed by the decision question, including congruence and scope
limits when `B.3` is current.

Representations and automation—for example, digital twins, evidence dashboards, traceability graphs, assurance
cases, test-report collections, or continuous pipelines—can help maintain these relations. Name the contribution
used by the account, then establish model applicability, physical correspondence, evidence completeness, and any
downstream acceptance, certification, permission, release, or target-claim use independently.

#### SYSE.4:4.7 - Apply the result to the smallest affected answer

The practitioner uses the changed reliance to reassess only the smallest earlier answer to which it applies:

- reassess `SYSE.1` when evidence changes the selected project referent, project reason, or boundary;
- reassess `SYSE.2` when observed participation, conditions, effects, benefit, or harm change the linked use or
  system concept;
- reassess `C.30`, `C.32`, or the applicable architecture decision when criteria, bearers, structures, or
  trade-offs must change;
- reassess `SYSE.3` when capability, integration, configuration, production, access, or another realization
  branch fails;
- use the specialist practice when its safety, security, legal, ethical, financial, certification, acceptance,
  permission, or release question remains open.

Stop when the account makes the evidence use, its limits, changed reliance, and affected answer clear. Reassess a
wider answer only when the narrower answer also fails. The result can become available at any time. The stated
relations are claim-dependency and revision relations; they impose no lifecycle stage or prescribed Work order.

### SYSE.4:5 - Archetypal Grounding

#### Pumping station under flood risk

In earlier steps, the engineer selects an intended pumping station, links the use claim “move water under the
selected flood load without unacceptable downstream harm” to a station concept, records
`StationArchitectureCandidate-7`, and opens the fixture-and-weld realization branch. The outside-effect claim is
now load-bearing for the decision whether to retain the selected discharge architecture.

The first engineering-assurance plan is:

| Plan part | Pump case value |
| --- | --- |
| Load-bearing claim | Claim episteme `StationFloodUseClaim-4` states that the station under `StationConfiguration-S7` and `FloodLoadProfile-3` moves the required water without crossing the declared downstream-exposure guardrail. |
| Decision question | `StationDischargeArchitectureQuestion-5` asks whether a later decision should retain, revise, or replace the selected discharge architecture. The question is current; the later decision occurrence is not. |
| Challenge and intended Work | Select a hydraulic component check and a station-and-downstream operating observation under the named configuration and comparable flood conditions. Cite the separately identified `StationFloodChallengeWorkPlan-2` shown below. The intended results remain separately typed measurement, test, and observation results. |
| Validity boundary | Pump configuration, station control state, discharge placement, flood-load range, downstream measurement locations, calibration, uncertainty, observation window, and the guardrail's specialist basis must remain recoverable. |
| Affected earlier answer | A failed component-capability claim requires reassessment of the realization branch and any architecture claim that relies on it. A downstream-guardrail breach requires reassessment of the `SYSE.2` use claim and discharge architecture. Reassess `SYSE.1` only if the project boundary or selected referent must change. |

The cited WorkPlan remains compact. `StationFloodChallengeWorkPlan-2` is one identified `A.15.2` WorkPlan episteme:

| `StationFloodChallengeWorkPlan-2` part | Planned claim content |
| --- | --- |
| Present EntityOfConcern, scheme, and horizon | The one present EntityOfConcern is claim episteme `StationFloodUseClaim-4`. The effective reference scheme is `StationFloodChallengePlanningScheme-E1`; it contains the interpretation rules for the local names, configuration, criteria, role condition, and time claims. The planning horizon is `[2026-09-21T00:00Z, 2026-10-16T00:00Z)`. |
| PlanItem and intended Method | `StationFloodChallengeInvestigation-2` designates possible future Work applying `StationFloodClaimChallengeMethod-v1`: conduct the bounded hydraulic component check and the station-and-downstream observation, then compare each direct result with the claim it can address. |
| Window, intended performer, and local role condition | The component check is planned for 2026-09-21 through 2026-09-25. Entry to the operating observation requires `StationConfiguration-S7` and conditions comparable with `FloodLoadProfile-3` within the horizon. The already identified System `StationRealizationEngineeringTeam-2` is the intended performer. Its planned local role condition is a positive classification under `StationFloodChallengeInvestigatorSystemRole`. `StationFloodChallengeCapabilityFitCondition-1` requires the team to be able to apply the named Method with the planned instruments, station access, and configuration within those windows; the PlanItem requires a positive fit result before Work entry. |
| Resources, dependencies, and result targets | Planned inputs include the pump test arrangement, calibrated flow and downstream-level instruments, station access, `StationConfiguration-S7`, the flood-load comparison, and the specialist guardrail basis. The result targets are one separately typed hydraulic-test result and one separately typed downstream-measurement result suitable for the evidence-use questions stated above. |

The WorkPlan claims only intended coordination. Later direct patterns must identify any role classification or
assignment, capability fit, resource availability, performed Work, results, and evidence use.

The direct result of later component-test Work is `PumpHydraulicTestResult-12`: the pump meets its declared flow
criterion. That result can support the pump capability claim within its test envelope. It does not support the
whole station-use claim by itself.

The direct result of later station-operating and observation Work is `DownstreamLevelMeasurementResult-9`.
`C.16` identifies the measurement result and uncertainty for the stated locations and window; the result shows
that the declared guardrail was crossed while the station operated under `StationConfiguration-S7`. An `A.10` descriptive evidence/provenance path represents the independently established use of that result as
evidence for `StationFloodUseClaim-4` in `StationDischargeArchitectureQuestion-5`. The engineer records the
narrowed reliance for this configuration in the engineering-assurance account and reassesses the `SYSE.2` claim
and discharge architecture on that basis. The observation does not by itself prove a complete causal account or make the specialist
harm, acceptance, permission, or release decision. Use `C.28` or the specialist pattern if one of those stronger
claims is needed.

#### Manufacturer's ERP-enabled planning change

The manufacturer's claim is that the deployed planning System will improve one named production-planning
decision under the current data, integration, staffing, and configuration conditions. The decision question is
whether to continue the investment and wider rollout. Installation completion and user acceptance are available,
but neither measures the claimed production effect.

The first plan names the effect claim, planning and production observations that could change the investment
decision, the comparison basis and time window, the deployed version and data configuration, and the `SYSE.2`,
architecture, `SYSE.3`, or Organization Engineering answer to reassess according to the first failed relation. If only installation and acceptance records are available, the engineer records in the
engineering-assurance account that the effect claim remains unresolved for the investment decision and plans
the missing observation Work. The engineer does not report that the effect is false or treat the platform,
organization chart, or vendor label as evidence.

#### Continuing building under occupied retrofit

The retrofit decision relies on a configuration-specific claim that the continuing building can retain the
declared structural performance and occupied-use constraints during one staged change. The challenge combines a
model or analysis applicable to that configuration with inspection and monitoring results from the
occupied stage. A result obtained for an empty building or another temporary-support arrangement does not carry
the same applicability.

The engineering-assurance plan names the claim, `OccupiedRetrofitSequenceQuestion-3`, the intended analysis and
observation Work, the temporary-support and access configuration, the validity window, and the temporary-access
branch in `SYSE.3` or architecture choice that the practitioner may need to reassess. If monitoring later
contradicts the assumed load or access condition, the engineer records that change in the account and reassesses
the affected branch or choice.
Building acceptance, a permit, contractor authorization, and release of the next Work window remain separate
decisions under their own criteria.

### SYSE.4:6 - Biases to Watch

Two recurring biases matter here. **Available-test bias** selects the familiar check before naming the claim and
decision; start with the load-bearing claim. **Pass-label inflation** lets one bounded result stand for assurance,
acceptance, permission, release, or outside benefit; state the exact evidence use and return the result to the
smallest answer it can change.

### SYSE.4:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-SYSE4-1` | A conforming use SHALL name one load-bearing claim episteme, its subject, conditions, configuration or version, temporal stance, and decision question. |
| `CC-SYSE4-2` | The first result SHALL name one challenge or evidence need, its validity boundary, and the smallest earlier answer to reopen. |
| `CC-SYSE4-3` | Intended challenge Work SHALL be coordinated through a separate `A.15.2` WorkPlan; the engineering-assurance plan SHALL NOT be treated as that WorkPlan or as performed Work. |
| `CC-SYSE4-4` | Performed challenge Work and its performer SHALL be identified through the direct Work and assignment patterns, and every measurement, evaluation, model-use, causal, test, or specialist result SHALL satisfy its own pattern. |
| `CC-SYSE4-5` | An evidence use SHALL name the target claim, result, conditions, provenance, currentness, and bounded use through `A.10`; its descriptive path SHALL represent only independently established relations, and a carrier, result record, or graph edge SHALL NOT establish the use by presence. |
| `CC-SYSE4-6` | A `B.3` assurance result SHALL be used only when assurance or material reliance is current; the DPF account SHALL NOT substitute for that result. |
| `CC-SYSE4-7` | Model, simulation, test, and digital-twin results SHALL retain their applicability, error, uncertainty, extrapolation, configuration, and evidence limits. |
| `CC-SYSE4-8` | Component behaviour, containing-System performance, outside effect, causality, benefit, harm, acceptance, permission, certification, release, and decision SHALL remain separately recoverable. |
| `CC-SYSE4-9` | The updated account SHALL state the practical change in reliance and the smallest project-focus, concept, architecture, realization, or specialist answer that the practitioner must reassess. |
| `CC-SYSE4-10` | When evidence is missing or inapplicable, the practitioner SHALL record a named gap or next challenge rather than a negative target claim. |
| `CC-SYSE4-11` | A conforming use SHALL allow evidence-producing Work at any relevant time and SHALL let its results revise affected engineering answers without establishing a terminal assurance stage or lifecycle order. |

### SYSE.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Working symptom | Repair |
| --- | --- | --- |
| Test chosen after commitment | The implementation is treated as settled before anyone asks what result could change the decision. | Name the load-bearing claim and decision question, then select the smallest challenge that could change reliance. |
| Component pass as outside benefit | A pump, deployed software System, or material passes a bounded test and the containing System's use claim is declared proven. | Keep component, containing-System, and outside-effect claims separate and obtain evidence for the claim the decision actually uses. |
| Assurance plan as evidence | Planned checks, booked facilities, or named results are treated as if Work and results already exist. | Keep the DPF plan, `A.15.2` WorkPlan, actual Work, result, evidence use, and account separate. |
| Model confidence as validity | Familiarity, model history, or a confidence score replaces applicability, uncertainty, extrapolation, and physical evidence. | Recover the model-use claim and its limits; obtain another evidence line when the decision requires it. |
| Digital twin or pipeline as assurance | Automation and traceability are treated as a complete assurance Method. | Name the model, check, observation, result, evidence use, and missing specialist decision maintained by the arrangement. |
| Evidence pile | Reports, dashboards, tests, and certificates are accumulated without a target claim or decision question. | Retain only the descriptive `A.10` paths needed by the current claim and bounded use; keep other results available without claiming relevance. |
| Stale configuration reuse | A result from another version, calibration, environment, load, or observation window is reused unchanged. | Recheck applicability and currentness; narrow the use or plan a challenge for the current configuration. |
| Acceptance or release by test | A technical result is treated as acceptance, permission, certification, gate passage, or release. | Apply the result only to the decision and criteria that can use it; record only the engineering claim it supports here. |
| Terminal assurance stage | Evidence is collected once at the end and cannot revise project focus, concepts, architecture, or realization. | Use SYSE.4 whenever a claim becomes load-bearing, and reassess only the earlier answer changed by each result. |

### SYSE.4:9 - Consequences

The project gains an early, inexpensive way to expose unsupported reliance. A single claim, challenge, decision
question, and affected earlier answer can guide useful Work before a large test programme or assurance case exists. Evidence from
models, integration, physical tests, and use can later accumulate without losing its subject, configuration,
currentness, or decision boundary.

The cost is explicit separation. Engineers must keep the DPF account, WorkPlan, performed Work, result,
descriptive evidence/provenance path, assurance result, specialist verdict, and decision question distinct. This takes more care
than one pass/fail status, but it shows which answer should change and prevents a locally successful check from
silently proving the whole project worthwhile.

### SYSE.4:10 - Rationale

Engineering assurance is useful when it changes engineering action. Starting from the relied-on claim prevents
the project from selecting familiar tests merely because tools, standards, or organizational routines make them
available. Naming the decision question makes sufficiency and effort decision-relative: the same evidence can
be enough for a reversible exploration and inadequate for safety, legal compliance, certification, or release.

The plan–account distinction keeps expected and actual evidence separate. The engineer selects a challenge and
intended Work and records them in the plan. The account records actual Work, direct results, their bounded
evidence use, and changed reliance.
Applying that change only to the affected earlier answer makes assurance part of continuing Systems
Engineering rather than a final checkpoint.

### SYSE.4:11 - SoTA-Echoing

| Current practice line | What changes in this pattern | Source and use | Adoption status |
| --- | --- | --- | --- |
| Current model credibility research treats model use as decision-specific and makes error, uncertainty, extrapolation, technical validity, model history, competence, access, and decision risk visible. | A model or simulation challenge names its applicability, uncertainty, extrapolation, configuration, and decision question; confidence does not become validity or physical truth. | Riedmaier et al. (2021), survey of more than 200 sources; Schwarzburg, Trauer, and Rebentisch (2024), literature review, 40-person survey, and an untested confidence-assessment proposal. | **Adopt and bound.** Use decision-specific credibility questions; select the VV&UQ Method and warranted reliability claim for the receiving model use. |
| Digital-twin engineering uses heterogeneous model transformation, code generation, and interpretation across design, implementation, and operation, mainly in manufacturing and transport. | A digital-twin arrangement can contribute a named model, automation, observation, or evidence-maintenance relation, but is not itself the challenge, physical evidence, or assurance result. | Lehner et al. (2025), mapping study of 66 included publications and 136 reported applications. | **Adapt.** Recover the twinned subject, model use, domain, result, and maturity limit; use the arrangement only for its established contribution. |
| Continuous integration, CPS, and SRE practice combine automated feedback with simulation, Hardware-in-the-Loop, physical checks, and risk-sensitive review in bounded technology settings. | Challenges may run frequently and produce results used as evidence during realization and operation, while cadence, pipeline structure, risk rule, permission, and release remain local. | Current DORA capability pages; Thurgood's 2018 SRE error-budget example; Zampetti et al. (2022), interviews in ten organizations and a 55-practitioner survey. | **Adapt narrowly.** Use frequent feedback where conditions fit; establish the local automation boundary, cadence, pipeline, and independent-assurance need. |
| Continuing requirements and compliance research keeps collaboration, traceability, monitoring links, legal interpretation, engineering descriptions, and evidence connected as systems change. | A challenge can cite maintained traceability and monitoring, but the account keeps legal interpretation, engineering claim, evidence use, specialist verdict, and decision separate. | Hernández, Moros, and Nicolás (2023); Norheim et al. (2024); Kosenkov et al. (2025). | **Adapt within scope.** Preserve continuing evidence links; let the receiving legal and engineering practices determine their Methods and Work organization. |
| BDD and test-intent research shows that software scenarios and executable checks can clarify part of intended behaviour, while industry evidence and automation coverage remain limited. | A scenario-to-check link can become one planned challenge for a software claim, but the check does not establish an outside effect, obligation, acceptance, or complete assurance. | Mohanani et al. (2022); Binamungu and Maro (2023); Lahiri et al. (2022); Fakhoury et al. (2024); Wang et al. (2025). | **Use as a bounded branch.** Retain test-intent clarification for software and qualify transfer of its metrics or result scope for each other engineered System. |
| Early model-based V&V and system-theoretic assurance research remains heterogeneous and profile-specific. | The common claim–challenge–evidence-use–revision method stays a guide-derived synthesis; specialist frameworks contribute only the named analysis, traceability, or argument result used by the decision. | Cederbladh, Cicchetti, and Suryadevara (2024), systematic review, DOI `10.1145/3631976`; Ahlbrecht, Sprockhoff, and Durak (2024), aircraft-safety proof of concept, DOI `10.1007/s10270-024-01209-6`. | **Keep provisional.** Use each V&V or safety-assurance framework within its supported profile and transfer only its established contribution. |

These sources support particular challenge, model-use, automation, traceability, and specialist-assurance
branches. The common claim–challenge–evidence-use–revision Method remains a cross-source synthesis. Reopen it
when later cross-domain comparison changes evidence composition, operating-feedback use,
assurance-case applicability, or the boundary with specialist safety, security, ethics, legal, certification,
acceptance, permission, or release decisions.

### SYSE.4:12 - Relations

- A practitioner can recover the named claim and decision question from results produced through `SYSE.1`,
  `SYSE.2`, `C.30`, `C.32`, `C.32.PAD`, `SYSE.3`, or a specialist practice. The engineering-assurance account
  states changed reliance and the smallest affected answer; the practitioner decides whether to revise that
  answer.
- A compatible `SYSE.10` engineering claim assessment may contain claim-sized evidence-use relations only for the
  same load-bearing claim, decision question, subject, configuration, use, conditions, interval, and evidence
  window. The practitioner uses `SYSE.4` to select any further challenge, qualify the evidence use, and record an
  assurance or reliance judgement. If the assessment is unavailable, stale, outside scope, or incompatible, use
  qualified direct evidence sources or record the missing assessment. Using the assessment gives no experiment
  choice, technical decision, assurance conclusion, acceptance, permission, or release authority.
- A compatible `SYSE.11` result may contain integration and observed-use evidence only for the same actual
  System, configuration, use, conditions, interval, and evidence window. The practitioner uses `SYSE.4` to qualify
  that evidence through `A.10` and record an assurance or reliance conclusion. If the result is unavailable,
  stale, outside scope, or incompatible, use a qualified direct source or record the missing integration or use
  evidence. Using the result gives no modernization choice, release, permission, or assurance authority.
- A compatible `SYSE.14` change-and-release decision may cite claim-sized evidence, configuration and
  effectivity basis, and unresolved conditions only for the same release question, configuration, effectivity,
  interval, and evidence window. The practitioner uses `SYSE.4` to qualify that evidence and may narrow reliance,
  abstain, or record the blocker. If the result is unavailable, stale, outside scope, or incompatible, use
  qualified direct evidence and configuration sources or record the missing change-and-release result. Using the
  decision episteme as a source gives no release authority, permission, or assurance conclusion; it also does not
  substitute for the evidence it cites.
- Use `A.15.2` for the intended challenge WorkPlan. Use `A.15.1`, the applicable system-role assignment pattern,
  and Work-attribution patterns when the challenge Work actually occurs. Naming the DPF plan or account does not
  establish an assignment, performer capability, resource availability, performed Work, result, or obtaining
  transformation.
- Use `C.16` for measurement, `C.32.ACE` for architecture-characteristic evaluation, `A.1.1` for model
  applicability and use, and `C.28` for causal use. Each result retains its subject, Method, configuration,
  uncertainty, applicability, and validity limits before it can be used as evidence.
- Use `A.10` to recover the descriptive claim-bound evidence/provenance path. Use `G.11` and `C.27.TA` when currentness,
  decay, calibration, configuration time, or an observation window changes admissible use. Use `B.3` only for a
  named assurance use or material-reliance threshold.
- Use `C.11` for a local decision, `A.21` for a gate decision, and `A.2.8.PER` for permission when those claims are
  current. Acceptance, certification, release, obligation, responsibility, authority, safety, security, ethics,
  law, compliance, and finance remain with their direct patterns and specialist practices.
- The engineering-assurance plan and account are C.2.1 epistemes carrying the working claims and references used
  to plan a challenge or reassess reliance. Use the direct patterns for tests, evidence bundles, assurance
  results, decisions, gates, and lifecycle structures.

### SYSE.4:End

<a id="syse-15"></a>
## SYSE.15 — Choose and Refresh the Engineering Methods Needed by a Project

### SYSE.15:0 — Use This When

Use this pattern when an engineering project has adopted a source bundle—for example, a lifecycle, standard,
model-based framework, toolchain, or AI workflow—as if it were the whole engineering Method, yet practitioners
cannot say which reusable Methods the project's Agents should apply in Work to obtain the results their current decisions need. Use it also when a local automation
makes one task faster while integration, assurance, rework, or the engineered System shows no benefit.

Begin with one recurring engineering result that is missing, unreliable, or too costly. State the project
System-of-interest, the relevant use and conditions, and the decision that needs the result.
Then identify and compare reusable ways of obtaining that result without importing an entire source bundle.

The first useful result is a **decision account for the project's engineering Method repertoire**. It states
which Methods are retained for the named results, which alternatives or gaps remain, where each Method applies,
which relations among Methods are supported, what evidence informed the choice, and what change reopens it. The
account is an episteme about the choice. MethodDescriptions, capability and provider claims, Work plans, and
performed Work retain their own identities and grounds.

Use direct FPF patterns when the question concerns one already identified Method or MethodDescription. Use
`SYSE.20` when the difficulty is a conflict among simultaneous Methods or Work wholes, `SYSE.12` when the missing
result is an engineering-platform capability, `SYSE.21` for wider cultural continuation, and `SYSE.24` when the
project must choose how to obtain a needed engineering result.

### SYSE.15:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| engineering Method | A reusable way of obtaining or preserving a named engineering result under stated participant meanings, conditions, applicability, and limits. |
| MethodDescription | An episteme about one identified Method that states a substantive way-of-doing claim. A standard, handbook, program, diagram, or workflow qualifies only when `A.3.2` admits it. |
| recurring engineering result | A result needed in more than one relevant Work situation—for example, an operating-situation account, prediction, design choice, changed System, integration observation, configuration basis, assurance result, or release decision. The current claim must name its kind and use. |
| project conditions affecting Method choice | The actual System kind and use, or the intended System kind and use stated in the project-system choice account, operating environment, physical phenomena, configuration, evidence and authority needs, provider conditions, decision horizon, and losses that must be protected. These conditions form the comparison boundary. |
| Method-repertoire account | The episteme returned here: current Method choices, alternatives, exclusions, evidence, limits, supported relations, gaps, and reopen conditions for named project conditions. Use `G.5` separately when a later selector needs a formal shortlist or joint-use set. |
| unresolved Method cue | A source phrase such as *model-based process*, *AI workflow*, *agile*, or *systems approach* whose reusable action, participant meanings, intended result, or boundary has not yet been recovered. |
| Method classification and specialization | A Method can meet several kind criteria and therefore have several broader Method kinds. This does not make the broader kinds parts, stages, or providers. |
| Method participation in whole Methods | One Method can contribute to several whole Methods. State each whole–part relation separately; shared participation does not identify the wholes with one another. |
| result use and dependency | A result from one Method can inform a decision involving another. That relation neither makes one Method part of the other nor proves a first–then Work order. |
| Work order and concurrency | Dated Work can overlap, recur, or follow a case-specific order while enacting the same or different Methods. A lifecycle diagram or table order does not establish that timing. |
| capability, assignment, provider, and platform | Different claims about which Agents can perform Work, who is assigned, how a result is obtained, and which supporting Systems are available. None follows from selecting a Method. |
| cultural prevalence | Claims about generation, transmission, recognition, selection, retention, or loss of Method variants in a population. One project choice establishes none of them. |

During this choice, each candidate Method is a project Method-of-interest because its identity, applicability,
comparison, and retention are current project questions. That designation is project-relative, not a Method kind.
After the choice, the Method's enactment in engineering Work, any later Method-development Work, the
Method-development Method, and the Agents and Systems involved retain separate relations.

Also keep the choosing Agent separate from performing Agents, and keep Methods separate from descriptions, tools,
Work, results, authority, capabilities, provider arrangements, and the actual System or intended-system designator selected as the project system-of-interest.

### SYSE.15:1 — Problem Frame

Systems Engineering is not one Method. Engineering different Systems—for example, a software-intensive
controller, ship, building, electrical installation, medical device, or experimental machine—can require different
physical models, trials, specialist evidence, permissions, platforms, and release Methods. Useful Methods can be
shared across those applications, but domain phenomena and consequences change how some Methods are performed and
checked.

An Agent that is also the actual System designated as project system-of-interest may enact an operating Method.
When that System does not yet exist, its intended-system designator carries an expected operating-Method claim
rather than performing Work. The project also uses engineering Methods to obtain results such as an account of intended use, a design, a created or changed System, an integration
observation, an assurance result, or a release decision. An operating Method enacted by the System and an
engineering Method used to create or change that System answer different questions, even when one project must
understand both. A non-agentic System has behaviour and functions but performs no Method.

Methods also have several structures at once. A trial Method can belong to several Method kinds, participate in
several whole Methods, supply results to several decisions, and be enacted concurrently with modeling or
implementation Work. Those are different relations; no single stack, tree, or lifecycle diagram captures all of
them.

### SYSE.15:2 — Problem

A named framework makes Method choice look easier than it is. A standard can contain useful obligations and
descriptions without showing which Methods work together or whether they fit this project. A lifecycle can show
contributions while falsely suggesting one pass. A connected model can improve some decisions while hiding
missing physical evidence for others. An AI Agent can shorten generation Work while review, integration, and
assurance become the limiting contributions.

The opposite error is to invent every Method afresh. Sources such as standards, handbooks, engineering
specializations, tool-supported practice, and observed successful or failed Work contain recoverable Method
candidates. Retain useful distinctions while testing source-specific elements—such as authority, vocabulary,
stages, roles, or artifacts—under current FPF kinds instead of importing the source whole.

### SYSE.15:3 — Forces

Recurring tensions include:

- Reusing familiar Methods saves search and learning effort; source authority and internal coherence do not prove
  fit for the current result.
- Smaller reusable Methods are easier to compare; false decomposition can destroy a working whole or invent
  Method parts that do not obtain.
- Shared engineering Methods reduce coordination cost; specialist physics, evidence, permissions, and failure
  modes still change the move in some domains.
- Representative trials cost time and equipment; document completion, declared conformance, and local task speed
  are weak substitutes for System and decision consequences.
- Method choices need a current answer while tools, sources, Agent capabilities, provider conditions, and project
  constraints continue to change.
- A project can justify a local Method choice without proving wider cultural prevalence or universal superiority.

### SYSE.15:4 — Solution

Choose and refresh engineering Methods from the results the project needs and evidence from representative Work.
Identify Methods before comparing them, preserve every relation that matters, and return capability, provider,
platform, or cultural questions to their own decisions.

**Local mantra.** Start from a needed engineering result. Recover reusable Methods, not an entire framework.
Compare them under the same project conditions. Keep classification, whole–part structure, result use, and Work
timing separate. Exercise the Methods together where interaction can reveal loss. Retain, replace, develop, or
leave a gap with evidence and a reopen condition. This is a recall aid, not a Work order.

#### SYSE.15:4.1 — Perform the Move

1. **Name the engineering result and receiving decision.** State the actual System or intended-system designator selected as the project system-of-interest, relevant use,
   configuration, conditions, decision horizon, intended users of the account, and the first recurring result whose
   Method is missing or doubtful.
2. **Recover candidate Methods from Work.** Inspect representative Work, including successful, failed, and
   difficult occurrences. For each candidate, recover the reusable action, generic participant meanings,
   conditions, intended result,
   nearest non-use case, and evidence. Keep actual performing Agents, assignments, capabilities, and authority
   with the dated Work.
3. **Recover candidates from sources without importing the source whole.** Inspect relevant sources—for example,
   standards, handbooks, lifecycles, model-based frameworks, AI workflows, or local traditions. Apply `A.3.1`
   before identifying a Method and `A.3.2` before relying on a MethodDescription. Keep an unresolved cue when the
   reusable way cannot yet be stated.
4. **Compare the same result under the same conditions.** Hold the result, actual or intended System kind stated in the project-system choice account, use,
   configuration, evidence needs, and protected losses stable while varying the Method. A new tool, description,
   assignment, or parameter is not automatically a new Method.
5. **Test whether specialization changes the work.** Compare a narrower engineering Method with the broader FPF
   or DPF move at comparable effort. Retain the specialization only when it changes what practitioners notice,
   decide, do, obtain, check, or use as a stop or return, and that difference is useful and warranted for this
   domain. A domain noun or extra example is insufficient.
6. **State each Method relation separately.** Record broader-kind classifications, participation in whole
   Methods, alternatives, refinements or replacements, result-use dependencies, and compatibility only when
   their own conditions obtain. Do not infer any of them from a list, vertical diagram, shared source, or Work
   order.
7. **Exercise an interacting engineering slice.** Use bounded representative Work in which several candidate
   Methods interact—for example, physical modeling, implementation, integration trial, configuration, assurance,
   and release around one change. Observe whether the needed decisions and System effects improve. Also record
   relevant costs or limits—for example, integration loss, rework, elapsed time, capability, platform constraints,
   or a protected characteristic that would otherwise be traded away silently.
8. **Make the repertoire decision.** The authorized Agent records which Methods are retained now, retained as
   alternatives, replaced, excluded for this use, proposed for development, or still unresolved. If a retained
   Method lacks a capable Agent, provider, platform, or assignment, record that separate gap and send it to the
   appropriate capability, provider, platform, or obtaining-arrangement decision.
9. **State evidence, currentness, and return conditions.** Give each relied-on claim its actual epistemic status—
   for example, project observation, qualified expert estimate, institutional description, academic or press
   visibility, declared conformance, or evidence of enacted practice. Reopen only when a changed result, source,
   Method, project condition, capability, provider, or platform can change the decision.

The numbered presentation is an `A.22.CGUS` learning unfolding. Work such as source inquiry, modeling,
realization, integration, assurance, platform development, or Method development can overlap and recur. The
presentation supplies no lifecycle or universal temporal order.

#### SYSE.15:4.2 — Record the Result

| Field | Required content |
| --- | --- |
| use boundary | Project System-of-interest, use, configuration, relevant conditions, decision horizon, intended account users, recurring engineering results, and protected losses. |
| Method choices and open cues | Methods retained now, alternatives, replacements, exclusions, proposed developments, unresolved cues, and relied-on MethodDescriptions or direct sources. |
| Method identity | For each Method: reusable action, generic participant meanings, intended result or preserved condition, applicability, and nearest non-use case. |
| Method relations | Supported classifications, whole–part participation, alternatives, refinements or replacements, result uses, and compatibility claims. Table order supplies no relation. |
| representative Work evidence | Work situation, performing Agents, assignments, enacted Methods, relevant Systems, results, evidence limits, System consequences, integration loss, cost, time, capability, and platform observations. |
| separate realization gaps | Missing capable Agent, assignment, provider result, platform capability, permission, evidence, or authority; receiving decision for each gap. |
| decision and currentness | Authorized choosing Agent, retained and excluded Methods, reasons, accepted losses, source status, currentness window, and smallest reopen conditions. |

Use a `G.5` shortlist or joint-use set only when a later selector needs that formal result. The ordinary repertoire
account does not create Method membership, capability, provider availability, cultural uptake, or performed Work.

#### SYSE.15:4.3 — What Changes in Practice

Practitioners stop asking which complete methodology to adopt. They can say which reusable Methods the
project's Agents should apply in Work to obtain each needed engineering result, which results representative Work
applying those Methods has actually produced, why the Methods fit this System and use, how they relate, where
evidence is weak, and what capability or provider result must be obtained next.
Standards become bounded sources, tools become Systems used in Work, and local speed is checked against
integration and System consequences. The account can change without renaming every Method or pretending that a
changed assignment, tool, or publication changed the reusable way of doing.

### SYSE.15:5 — Worked Case: Methods for a Heat-Pump Controller Change

An engineering team is changing the controller of an occupied-building heat-pump plant. Its current process
description points to a V diagram, a Systems Engineering handbook, a simulation repository, an issue tracker, a
hardware-in-the-loop bench, an AI coding service, and a release checklist. The V diagram, handbook, and checklist
are descriptions. The repository and issue tracker store or carry records. The bench is a platform System. The AI
service may be an Agent, provider resource, or tool depending on the actual arrangement and agency. Calling this
heterogeneous set *our model-based process* does not make it one Method.

The engineering lead acts as the Agent authorized to choose Methods for this controller project. Release
authority remains with another Agent. The team starts from recurring results rather than the list of assets:

| Needed result | Candidate or retained Method | Evidence and current gap |
| --- | --- | --- |
| Operating situations and protected room-temperature and equipment conditions | Recover operating situations, affected Systems, and required effects before choosing a controller concept. | Existing operating records cover normal weather; rare grid events remain an explicit gap. |
| Plant-response prediction | Identify physical parameters and simulate the heat-pump, building, sensor, and controller interaction. | Earlier predictions omitted measured sensor latency. |
| Controller implementation candidate | Generate a bounded code candidate, then perform an independent implementation review. | *Use AI* is not a Method; the reusable generation-and-review ways and their different results are stated separately. |
| Integration observation | Exercise the actual controller interface and plant model on the hardware-in-the-loop bench. | Bench time is scarce; occupied-building trials require separate safety and release conditions. |
| Configuration, assurance, and release decisions | Use the corresponding configuration, assurance, and release Methods for the identified controller and plant conditions. | None of these decisions follows from the V diagram or a green code check. |

The hardware-in-the-loop trial Method meets both experimental-engineering and cyber-physical-integration Method
criteria. The team also uses it as a part of two stated whole Methods: controller integration and release-evidence
development. Those classifications and whole–part relations are recorded separately. The modeling result informs
the controller choice, but that result use does not make modeling a stage of one universal lifecycle.

In a representative three-day slice, an AI coding Agent performs bounded generation Work, a controls engineer
reviews the candidate, and a test engineer performs the bench trial. If the coding service lacks enough agency to
perform the assigned Work, it is recorded as a tool used by the controls engineer instead. The trial reveals
sensor latency that destabilizes the candidate despite an acceptable simulation prediction. The release Agent
withholds the candidate, and the controls engineer revises the physical model. Faster code generation did not
shorten the limiting integration and assurance Work.

The repertoire account retains operating-situation recovery, linked concept development, physical modeling,
bounded implementation generation, independent review, hardware-in-the-loop trial, configuration, assurance,
and release Methods. It retains an occupied-building trial only under the stated safety, plant-state, weather,
and release conditions. The V diagram remains an overview. The phrase *AI workflow Method* remains unresolved.

Scarce bench capacity is not repaired by changing the trial Method. It becomes a platform or obtaining-arrangement
question for `SYSE.12` or `SYSE.24`. Simultaneous modeling, generation, review, trial, and assurance conflicts go
to `SYSE.20`. Evidence of wider use, selection, retention, or loss can later inform `SYSE.21`; this project choice
does not establish a cultural trend.

**When the full pattern is unnecessary.** If one identified Method already supplies a well-understood result for
the same System and conditions, and no interaction, specialization, capability, provider, or currentness question
can change the decision, use that Method and its direct evidence patterns.

### SYSE.15:6 — Bias Annotation

Sources such as official standards, handbooks, maturity schemes, curricula, publications, and project
declarations provide evidence about descriptions or institutional activity. Evidence of enacted Work and practical
worth requires observations of the relevant practice and consequences. When broader observations are unavailable,
use a bounded expert estimate and state its population, period, basis, uncertainty, and application limit.

Check software and AI evidence against the receiving engineering application. Fast feedback can transfer without
identical cadence, physical evidence, release authority, or assurance. Specialist Methods—for example, safety,
security, legal, manufacturing, maintenance, clinical, maritime, electrical, or building Methods—remain where
their domain changes the Work.

### SYSE.15:7 — Conformance Checklist

- [ ] The System to be created or changed, recurring engineering result, receiving decision, conditions, and
      protected losses are stated.
- [ ] Every Method remains distinct from descriptions, tools, Work, performing Agents, assignments, capabilities,
      evidence, provider arrangements, and cultural relations.
- [ ] Each Method has a reusable action, participant meanings, applicability, intended result, and non-use case.
- [ ] A narrower engineering Method is retained only when its specialization changes useful and warranted action
      at comparable effort.
- [ ] Classification, whole–part participation, alternatives, replacement, result use, compatibility, and Work
      timing are stated separately.
- [ ] Interacting Methods are exercised in representative engineering Work, and limiting System, integration,
      assurance, cost, time, capability, and platform consequences are observed.
- [ ] Missing capability, assignment, provider, platform, permission, evidence, or authority is returned to its
      own decision rather than hidden as a Method defect.
- [ ] Project evidence and expert estimates remain distinct from visibility, declared conformance, and cultural
      prevalence.
- [ ] The account names retained, replaced, excluded, proposed, and unresolved Methods with material reopen
      conditions.

### SYSE.15:8 — Common Failures and Repairs

These recurring substitutions hide a Method choice or send the project to the wrong next decision:

| Failure | Repair |
| --- | --- |
| Framework status stands for practical worth | Recover the Methods actually used and test their fit and consequences separately. |
| Tool or notation stands for Method | State the reusable action and result; keep representation, mechanism, tool, and Work separate. |
| A stage, role, artifact, or meeting is called a submethod | Apply Method identity and whole–part tests; retain the item under its actual kind when the Method claim fails. |
| Lifecycle order stands for Method architecture | State classifications, whole–part relations, result uses, compatibility, and actual Work timing independently. |
| Every result is expected from one connected model | Name the decisions each model supports and the physical, specialist, or operating evidence it does not supply. |
| AI speed stands for engineering improvement | Compare generation gains with review, integration, assurance, maintenance, and System consequences. |
| Missing capable Agent or platform is called a bad Method | Keep the Method choice and return the separate capability, provider, assignment, or platform gap. |
| Visibility stands for prevalence | State observed use or a bounded expert estimate; publication and teaching coverage establish neither enactment nor retention. |
| Generalize one application profile to all engineering | Preserve the project-system choice and domain boundary and obtain the relevant specialist result. |

### SYSE.15:9 — Consequences

The project gains an inspectable repertoire without repeatedly importing or rejecting whole frameworks. Useful
combinations become visible, representative Work exposes limiting contributions, and a changed source or
condition reopens only the affected choice. Capability, provider, platform, and culture decisions receive named
gaps instead of Method-shaped ambiguity.

The cost is real comparison and trial Work. Some source cues remain unresolved, some Methods cannot be safely
decomposed, and evidence from one project may not transfer. Recording those limits is more useful than hiding
them behind a universal process name.

### SYSE.15:10 — Rationale

FPF supplies general Method identity, descriptions, specialization, whole–part relations, Work, cultural change,
and source-use discipline. Systems Engineering adds the recurring subject-specific question: for the actual
or intended System selected by this project-system choice under these physical and organizational conditions,
which reusable Methods should the project's Agents apply in Work to obtain the connected engineering results—
for example, concept, modeling, realization, integration, configuration, assurance, release, or continuing-change
results—and what did representative Work applying those Methods actually produce?
Starting from those results preserves valuable engineering specializations. Representative Work tests the
Methods together, because a locally faster activity can move cost or failure to integration, assurance,
operation, or maintenance. The resulting choice remains bounded to the project rather than being advertised as a
universal methodology or cultural fact.

### SYSE.15:11 — SoTA and Source Use

| Source line | Retained contribution | Limit and guard |
| --- | --- | --- |
| R7.2–R7.5 | Method, MethodDescription, and Work separation; several Method structures; framework and source-bundle disassembly; improvement from observed loss. | R7 is a maintained practitioner synthesis. Its lifecycle vocabulary and source-school claims require current comparison. |
| R8.2–R8.9 | Recurring engineering results; research and modeling returns; continuing realization, integration, configuration, platform, assurance, and source-restoration Work. | R8 establishes no single universal engineering Method, performer roster, or prevalence claim. |
| [Henderson-Sellers and Ralyté 2010](https://opus.lib.uts.edu.au/handle/10453/13456), [Tsai, Zdravkovic, and Söder 2023](https://doi.org/10.1007/s10270-022-01068-z), [Bender 2024](https://doi.org/10.1007/s10257-024-00675-1), and [Ralyté, Koutsopoulos, and Stirna 2025](https://doi.org/10.1007/s10270-025-01304-2) | Situational Method construction and adaptation candidates, plus separate consistency, fit, and practical-worth questions. | Much of the evidence concerns information systems, business processes, and modeling Methods; source-local fragments, roles, and artifacts do not transfer automatically to physical engineering. |
| [ISO/IEC/IEEE 24774:2021](https://www.iso.org/standard/78981.html) and [OMG Essence](https://www.omg.org/spec/Essence) | Current process- and practice-description comparisons. | Institutional status and conformance do not prove Method identity, fit, composition, or worth. |
| [DORA Continuous Integration](https://dora.dev/capabilities/continuous-integration/), [DORA Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/), [DORA Platform Engineering](https://dora.dev/capabilities/platform-engineering/), and [Zampetti et al. 2022](https://doi.org/10.1145/3571854) | Bounded evidence for small changes, fast feedback, frequent integration, risk-sensitive approval, platform use, and mixed cyber-physical cadence. | Evidence is heterogeneous and predominantly software or technology Work; it does not prescribe one cadence or automation level for every engineered System. |
| [Becker et al. 2025](https://arxiv.org/abs/2507.09089), [METR February 2026](https://metr.org/blog/2026-02-24-uplift-update/), [METR task-substitution note](https://metr.org/blog/2026-05-08-task-substitution-and-uplift/), [METR self-report study](https://metr.org/blog/2026-05-11-ai-usage-survey/), [Agarwal, He, and Vasilescu 2026](https://arxiv.org/abs/2601.13597), [Pradas Gomez et al. 2025](https://doi.org/10.1017/pds.2025.10045), and [Luke et al. 2026](https://doi.org/10.1017/pds.2026.10600) | Conflicting evidence that AI-capable Systems can change speed, value, quality, maintainability, task mix, and integration differently. | Software dominates the evidence; bounded studies and self-reports establish neither autonomous performance of all engineering Work nor transfer of authority. |

A new source, tool, or AI release reopens only the Method choice, evidence claim, applicability condition, or
protected loss that it can change. Novelty alone does not restore a discarded framework.

### SYSE.15:12 — Relations

- `A.3.1` identifies each Method; `A.3.2` identifies a MethodDescription; `A.15.1` governs dated Work. A source,
  description, assignment, capability, tool, or run does not occupy the Method position. `A.15.6` governs the
  project-relative Method-of-interest designation. It distinguishes a Method enacted in the subject's operational
  Work, a Method used to create or change a System, a solution Method, a Method-of-interest, and a Method used to
  develop that Method-of-interest.
- `A.3.1` distinguishes several broader Method kinds from participation in several whole Methods. `A.22`,
  `B.1.5`, and direct relation patterns still govern selected structures and whole–part claims.
- `C.32.MWA` keeps Method classification, Method holarchy, result dependencies, Work order, provider or enabling
  Work, capability development, and cultural change as different structures that may all be needed in one case.
- `E.8:4.1.3` tests whether a narrower engineering contribution changes useful and warranted action at comparable
  effort. It neither selects the Method nor proves practical worth.
- Apply `E.23` when a named Method itself must be improved. In this pattern, the Agent choosing a bounded
  engineering Method repertoire performs the decision Work described here. When a Method must be created or
  changed, use the applicable Method Engineering result or a qualified direct source.
- `G.5` supplies a shortlist or joint-use set only when a later selection needs that result. It establishes
  neither Method identity nor actual capability, compatibility, enactment, or uptake.
- Route platform, simultaneous-Work, cultural-continuation, and obtaining-arrangement questions to the Agents
  applying `SYSE.12`, `SYSE.20`, `SYSE.21`, and `SYSE.24`, respectively. Their co-use creates no automatic
  temporal order.
- Application Methods—for example, organization-change, operations-management, software, electrical, medical,
  maritime, or building Methods—retain the Systems they create or change, their evidence, authority, and
  applicability. Shared
  vocabulary does not make them parts of one universal process.

### SYSE.15:End

<a id="syse-20"></a>
## SYSE.20 — Reconcile Overlapping Engineering Work and Required Order

### SYSE.20:0 — Use This When

Use this pattern when engineering Work overlaps to shorten feedback, but some results, configurations, or safety
conditions still require a particular order. A local improvement—for example faster simulation, earlier review,
or self-service tooling—may delay or weaken the integrated engineering result.

Begin with that result and the decision that will use it. Name the Work that is actually being performed, the
Methods it enacts, and the direct relations that matter. Do not infer those relations from a lifecycle diagram,
team chart, toolchain, or list of disciplines.

The first useful result has two parts:

1. a **Method-and-Work architecture account** showing the current Methods, Work occurrences, direct relations,
   conflict, and moved burdens; and
2. a **bounded reconfiguration decision** choosing how one part of that arrangement will change.

These are two epistemes. An authorized Agent performs the decision Work. Later Agents perform any implementation
and test Work. The Methods, Work occurrences, participating Systems, and changed engineering arrangement retain
their own identities.

Use `C.32.MWA` when the main difficulty is synthesizing several practice structures in any domain. Use this
pattern for the engineering specialization: overlapping contributions to an engineered System create a conflict
among constraints such as configuration identity, integration, evidence, platform availability, or specialist
assurance, and the project must choose a change. Use Operations Management when the main result concerns continuing flow, queues, or throughput. Use
Method Engineering when the reusable Method itself is the subject being developed. Use `SYSE.15` first when the
project still lacks a usable account of its engineering Methods.

### SYSE.20:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| engineering result at risk | A named result whose usability can change with the Work arrangement—for example an integration recommendation, accepted configuration, verified interface claim, released design, or usable service condition. State its kind and the decision or Work that uses it. |
| Method-and-Work architecture account | An episteme describing the selected Method and Work structures, their direct relations, the conflict, alternatives, and moved burdens for one decision. It is a description of the arrangement. |
| Work overlap | A temporal relation between admitted Work occurrences whose extents intersect under a named temporal reference. Overlap alone establishes neither Work parthood nor Method composition. |
| required order | A direct dependency that makes one occurrence or condition precede another for a named use—for example a temporal meet, transformation completion, result-use guard, configuration release, or authority condition. State the governing relation. |
| Method unfolding | An organization of positions, branches, returns, or stops inside one identified reusable Method. Dated Work order supplies evidence about Work; it establishes a Method unfolding only when the Method structure is grounded separately. |
| enabling or provider Work | Separately admitted Work that changes an enabling System or supplies a needed result or service. Its direct dependency on engineering Work is stated without absorbing it into the same Work whole. |
| capability-development Work | Work intended to change an Agent's capability for later Work. Its earlier occurrence establishes temporal order; capability change needs its own evidence. |
| moved burden | A material cost, delay, evidence need, dependency, risk exposure, or loss of control that decreases in one scope and increases in another. This is an open example set; name the actual burden and receiving scope. |
| reconfiguration alternative | Possible-future content proposing a change to one or more named relations in the engineering arrangement. |
| bounded reconfiguration decision | An authorized choice among the admitted alternatives for the named result, configuration, use, and time window. The choice becomes input to later implementation Work. |

An Agent performs Work. Systems can participate as, for example, equipment, a platform, the engineered subject,
or part of its environment. Models are epistemes used by Work. State each direct relation, and use the more
specific Agent wording when agency matters to the claim.

### SYSE.20:1 — Problem Frame

Engineering does not normally proceed as one total sequence. Modeling can overlap implementation, evidence review
can begin before a test finishes, and provider Work can restore a service while project Work continues. At the
same time, some dependencies are real: a test uses a released rig configuration; a simulation result refers to a
particular model and solver configuration; a release decision waits for admitted evidence.

Several structures can therefore matter to one decision. Common examples are:

- a Method structure showing composition or an unfolding;
- a Work structure showing parthood, overlap, and required order;
- a subject structure showing the engineered System and enabling Systems;
- a representation-use structure showing which models and evidence refer to which configuration; and
- provider, capability-development, or cultural-change structures when they change the decision.

This is an open example set, not a universal view list. The project selects only structures that expose a
decision-relevant relation or conflict. Their descriptions can correspond without lining up one-for-one.

### SYSE.20:2 — Problem

Three recurring errors make the engineering arrangement hard to change.

First, a sequence-only account serializes Work that could overlap and postpones integration feedback. Second, an
“everything is concurrent” account loses guards and result dependencies. Third, a diagram turns unlike relations
into levels: a Work part, a model use, provider Work, and earlier training appear as one stack merely because they
occupy different rows.

Local optimization then hides the project result. Faster code generation can increase review and integration
delay. More simulation can strengthen a claim about the wrong configuration. A self-service platform can shorten
setup while moving maintenance and assurance burdens to a provider. The local metric improves, but the receiving
engineering decision gains no usable result.

### SYSE.20:3 — Forces

The recurring tensions are:

- Useful overlap shortens feedback, while stale configuration and provisional evidence can propagate through it.
- Required order protects identity, safety, and authority, while total serialization delays learning.
- Several Methods can be enacted together, while co-use does not by itself compose one larger Method.
- Shared models can improve correspondence, while every model preserves some distinctions and loses others.
- Provider services can reduce local effort, while availability, compatibility, and maintenance remain project
  concerns when the engineering result depends on them.
- A project can choose a new arrangement, while cultural continuation depends on later recognition, enactment,
  selection, and retention.
- More views can reveal a hidden conflict, while views that cannot change the decision add reading and maintenance
  cost.

### SYSE.20:4 — Solution

Describe the obtaining engineering arrangement through the few structures that change the decision. State each
direct relation, expose the conflict and moved burdens, generate materially different reconfigurations, and let an
authorized Agent choose one change for later implementation and test.

#### SYSE.20:4.1 — Pattern-Use Unfolding

The reusable Method has the following eight recurring moves. They organize use of this pattern; they do not claim that
the project's engineering Work occurs as eight consecutive stages.

1. **Decision boundary.** The Agent names the engineering result at risk, its configuration and intended use, the
   decision that needs it, the time window, and the authority for changing the Work arrangement.
2. **Obtaining Work and Methods.** The Agent identifies representative performed Work with its extent, performing
   Agents, assignments when attribution matters, and enacted Methods. A possible-future arrangement instead uses
   a WorkPlan or intended-use description and names the later Work that would test it.
3. **Direct Work relations.** The Agent states every needed Work relation—for example parthood, temporal overlap,
   required order, result use, or service dependency—through its governing pattern. A common interval is evidence
   only for overlap; a Work part supplies no Method-part claim.
4. **Decision-relevant companion structures.** Other structures—for example subject, representation,
   configuration, provider, capability, or cultural structures—are added only when one changes the decision. Each
   description states its subject, use, important correspondences, and losses.
5. **Conflict and moved burden.** The Agent identifies the incompatible results or constraints and the engineering
   consequence. Every claimed local gain names any material burden moved to another Agent, System, decision, or
   time interval.
6. **Alternatives.** The Agent develops a finite current option set whose members change at least one named
   relation. Renaming a diagram or citing an ungrounded Method creates no new option. The incumbent remains when
   it is feasible.
7. **Choice.** The authorized Agent uses `C.11` or a domain decision Method to compare the fixed option set on one
   stated basis and choice rule. The result identifies the selected alternative or the next probe, accepted
   losses, preserved constraints, missing evidence, and reopen condition.
8. **Realization and return.** Assigned Agents perform separately identified implementation Work. Later
   representative Work supplies observations about the changed arrangement and the engineered result. An
   authorized Agent uses those observations to preserve, narrow, or reopen the decision.

#### SYSE.20:4.2 — Record the Result

The Method-and-Work architecture account contains the seven result positions below. This table is the complete
content set for this pattern's first result; a project may represent it as prose, a table, or linked model content.

| Result position | Required content |
| --- | --- |
| use boundary | Engineering result at risk, receiving decision or Work, configuration, intended use, time window, deciding Agent, and authority scope. |
| current Method and Work structures | Representative Work, performing Agents, enacted Methods, Work wholes, and every direct relation used by the decision. |
| companion structures | Only structures that change the decision, with each structure's subject, use, important correspondences, and losses. Section 1 gives an open example set. |
| conflict | Incompatible results or constraints and the consequence for the engineered result. |
| moved burdens | Each material burden, the scope that loses it, and the scope that receives it. |
| alternatives and choice | Fixed admitted option set, changed relations, comparison basis, choice rule, selected option or next probe, accepted losses, and preserved constraints. |
| continuation | Implementation Work, later representative Work, receiving Agents and their decisions, each supplied result, missing evidence, and the reopen condition. |

The bounded decision is a separate episteme because it adds the authorized choice and its reason. It does not
alter the earlier Work. The account can supply a design constraint to `SYSE.12` and a project-local Method variant
to `SYSE.21`; each receiver makes its own decision.

#### SYSE.20:4.3 — What Changes in Practice

Engineers stop choosing among package labels such as *waterfall*, *concurrent*, *agile*, *model-based*, or
*AI-native*. They decide which Work may overlap, which dependency requires order, which Methods are actually
enacted, and where a local improvement moves burden. The resulting change is small enough to implement and test,
while the architecture account remains rich enough to prevent the same conflict from reappearing under another
diagram.

### SYSE.20:5 — Worked Case: Power-Converter Integration

A team is preparing an integration recommendation for a power converter. The recommendation will be used by a
separate release decision. During one laboratory run, five Work occurrences obtain:

| Work occurrence | Interval on the run clock | Directly relevant relation |
| --- | --- | --- |
| physical-model correction | minutes 0–25 | overlaps simulation during minutes 10–25 |
| numerical simulation | minutes 10–35 | depends on a compatible solver service and named model editions |
| rig reconfiguration | minutes 30–50 | must finish and receive rig-release authority before closed-loop test |
| closed-loop test | minutes 50–75 | uses the released rig and named converter configuration |
| evidence review | minutes 70–90 | overlaps the final five minutes of test; its recommendation remains conditional until test evidence arrives |

A platform team also performs solver-service recovery during minutes 32–43. That provider Work overlaps the run
but remains a separate Work occurrence. Earlier laboratory training is capability-development Work; it is neither
simultaneous with nor part of this run. Capability claims rely on training evidence, not on temporal priority.

Each Work occurrence has a performing Agent, an enacted Method, and the relevant assignment and authority when
the receiving claim needs them. The case gives no basis for treating all five Methods as parts of one composite
Method. It does establish three different Work relations: temporal overlap, the rig-change-before-test guard, and
simulation dependence on a provider result.

The decision uses three selected structures:

1. a Work structure containing the relations in the table;
2. a subject structure containing the converter, control board, power stage, rig, load bank, and platform under
   their actual component, connection, and service relations; and
3. a representation-use structure connecting model editions, solver configuration, simulated results, measured
   traces, and release criteria to the converter configuration and intended claim.

This is the complete selected set for this case because no other inspected structure changes the choice. The live
conflict is clear: simulation starts while the model is changing and continues while the solver service is
degraded; review can therefore receive a simulation result that no longer corresponds to the tested
configuration.

The Agent admits three reconfiguration alternatives as the fixed option set:

| Option | Changed relation | Main gain | Moved burden |
| --- | --- | --- | --- |
| A — total serialization | Every project Work occurrence waits for the previous one; provider recovery blocks simulation. | Simple evidence order. | Feedback is slower and laboratory time is idle. |
| B — guarded overlap | Overlap remains; every simulation result names model, solver-service, and intended converter configurations; the rig-release guard remains; evidence review marks provisional results. | Fast feedback with usable configuration correspondence. | More traceability and service-health checking. |
| C — laboratory-local solver service | Guarded overlap remains and simulation uses a local service. | Shared-service outages no longer block the run. | Solver validation, security, configuration, and maintenance move to the laboratory. |

An authorized engineering lead compares the options. The rule rejects an option that breaks evidence-reference
eligibility, the rig-release guard, or the lead's authority boundary. Among surviving options, it prefers useful
overlap and then the option with the lower continuing service burden. Current evidence supports the lead's choice of B. A
failed compatibility replay would reopen that decision; validated evidence of a lower continuing burden could
support a later choice of C.

The decision requests separate implementation Work to update the applicable MethodDescription and WorkPlan.
The next representative run tests the new references, provisional-result rule, and rig guard. The architecture
account supplies the platform-design constraint to `SYSE.12`. Its description of a guarded-overlap variant may
enter `SYSE.21` as one project observation; cultural continuation requires later evidence from other Work and
Agents.

### SYSE.20:6 — Bias Annotation

The following table records four recurring interpretation biases found in the source guides and engineering
literature used by this pattern.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| lifecycle or maturity bias | A familiar stage diagram or maturity ladder becomes the Work architecture. | Recover the obtaining Work, Methods, and direct relations before retaining any structure. |
| software-transfer bias | Software evidence sets cadence, assurance, and release conditions for physical engineering. | Transfer only the supported contribution and retain the physical configuration, specialist, safety, and test conditions of the receiving case. |
| official-source bias | Publication or institutional prominence is treated as enacted prevalence or effectiveness. | State the supported source claim and use bounded observations or qualified expert estimates for actual practice. |
| human-only or AI-replacement bias | A job title is assumed to perform all Work, or one AI-produced result is treated as autonomous whole-project engineering. | Identify the performing Agents, their bounded Work and capability, the participating Systems, evidence use, and decision authority. |

### SYSE.20:7 — Conformance Checklist

The following conditions are required for a conforming use of this pattern.

- [ ] The opening names a recognizable conflict between useful Work overlap and a required order or dependency.
- [ ] The first result contains both a current Method-and-Work architecture account and a bounded reconfiguration
      decision.
- [ ] Every Work occurrence has a temporal extent, a performing Agent, and an enacted Method; assignments are
      stated where attribution matters.
- [ ] Method composition, Method unfolding, Work parthood, Work overlap, and required order use separate claims.
- [ ] Provider or enabling Work, capability-development Work, and cultural change keep their own relations.
- [ ] Every selected structure changes the current decision and states important correspondences and losses.
- [ ] Every local gain names any material moved burden and its receiving scope.
- [ ] The fixed options differ by a named relation and are compared on one stated basis and rule.
- [ ] Choice, implementation Work, later observations, and cultural continuation remain separate results.
- [ ] The receiving Agent gets the decision, missing evidence, next Work, and reopen condition.

### SYSE.20:8 — Common Failures and Repairs

These are the recurring failures reported in the source guides or exposed by the power-converter and cross-domain
probes used for this pattern.

| Recurring failure | Repair |
| --- | --- |
| A first–then procedure is presented as levels | Keep the direct temporal or transformation relation; recover Method organization separately. |
| Overlapping Work is treated as proof of Method composition | Identify each Method and require an obtaining Method-part relation before claiming a composite Method. |
| A Work part is placed inside the engineered System | Keep the Work structure and subject structure separate; relate their descriptions through named uses. |
| A connected model is treated as the integrated engineering reality | Name the model epistemes, their subjects, correspondences, losses, and receiving uses. |
| A platform service is assumed usable whenever dependent Work runs | State the provider Work, service condition, compatibility evidence, access, and moved maintenance burden. |
| One local activity becomes faster while the engineering result still waits | Measure the receiving result and identify the limiting contribution and moved burden. |
| A selected option lacks a comparison rule or authority | Recover the fixed option set, basis, rule, deciding Agent, authority, and next probe before calling it a decision. |
| A decision is reported as changed practice | Identify later implementation Work and representative observations separately. |
| One project choice is reported as cultural success | Supply it as one project observation to `SYSE.21` and seek later recognition, enactment, selection, and retention evidence there. |

### SYSE.20:9 — Consequences

The project can retain productive overlap without losing real guards, configuration identity, evidence status, or
authority. Several structures remain non-isomorphic, but their direct relations and correspondences make one
bounded engineering choice possible. Platform and capability dependencies become visible before a local gain is
accepted.

The cost is recovery of the Work occurrences, Methods, configurations, result uses, and authority needed by the
choice. Some attractive diagrams will remain merely descriptions, and some local improvements will lose priority
when their moved burdens become visible.

### SYSE.20:10 — Rationale

Method organization, dated Work order, and simultaneous Work answer different questions. A Method unfolding says
how a reusable way of doing is organized. A temporal relation says when admitted Work occurs. Work parthood says
which occurrence contributes constitutively to another Work whole. Treating them as interchangeable destroys
either useful overlap or necessary order.

Engineering adds a recurring domain difficulty to the general `C.32.MWA` problem: several contributions must
produce a result about one configured engineered System while using models, evidence, specialist decisions, and
enabling Systems with their own identities. Connecting the recovered structures to that result makes a bounded
reconfiguration decision more useful than choosing a universal lifecycle or accumulating a large architecture
dossier.

### SYSE.20:11 — SoTA and Source Use

This table is the complete source-use register for this pattern body.

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| R7.2–R7.5 | Method-holon inspection, continuing engineering, disassembly of heavyweight methodologies, and separation of Method change, organization change, and current Work coordination. | Treat R7 as maintained practitioner synthesis; ground current Methods and Work relations in the receiving case. |
| R8.3, R8.4, R8.7, and R8.8 | Recursive integration and concurrent design, realization, integration, operation, platform, and evidence contributions. | Retain application-specific physics, evidence, timing, and authority. |
| R0.2, R0.7, and R0.12 | Recovery of relations hidden by stack wording and separation of physical phenomenon, model, computation, realization, decision, and action. | Chapter order supplies presentation order only; current FPF supplies the maintained kinds and relations. |
| Current FPF `A.3.1`, `A.15.1`, `A.22`, `B.1.5`, `C.27.TA`, `C.30.STRAT`, `C.32.MWA`, `C.32.MLAO`, and `C.36` | Method and Work identity, direct temporal claims, selected structures, specialization and composition, stratification checks, several-structure synthesis, moved-burden comparison, and cultural-change relations. | This DPF adds the engineering conflict, configured result at risk, applied alternatives, and bounded reconfiguration decision. |
| [DORA Continuous Integration](https://dora.dev/capabilities/continuous-integration/), [Platform Engineering](https://dora.dev/capabilities/platform-engineering/), [Change Approval](https://dora.dev/capabilities/streamlining-change-approval/), and [DORA 2025](https://dora.dev/research/2025/dora-report/) | Software evidence and practitioner guidance about frequent integration, feedback, risk-sensitive approval, and platform-mediated Work. | Apply those observations to the stated software populations and use them as candidate contributions in other engineering profiles. |
| Flow Engineering, [*The Iterative Systems Engineering Handbook*, Volume I](https://www.flowengineering.com/handbook/iterative-systems-engineering/volume-1) | Candidate moves for shorter feedback, coordination across engineering contributions, and repeated hardware integration. | Treat provider-authored advocacy and anecdotes as hypothesis and case material; qualify prevalence and causal claims separately. |
| Current AI-engineering evidence qualified in `SYSE.15` | Bounded observations about AI-capable Systems participating in software and engineering-design Work. | Reuse only compatible claims for the named profile, Work, result, and evidence window. |

Reopen the affected claim when a later source or representative Work changes a Method, Work relation, conflict,
alternative, or decision. Novelty or publication status alone does not reopen the pattern.

### SYSE.20:12 — Relations

The following direct relations are used by this pattern body.

- `SYSE.15` supplies compatible engineering-Method repertoire claims. Availability alone supplies no fit or
  enactment claim.
- `A.3.1` governs Method identity, multiple-parent classification, participation in several whole Methods,
  refinement, and replacement. `B.1.5` governs any claimed Method composition.
- `A.15.1`, `F.6`, and `C.27.TA` govern performed Work, attribution when needed, and direct temporal claims.
- `A.22`, `C.30`, `C.30.STRAT`, `C.32.MWA`, and `C.32.MLAO` govern selected structures, architecture claims,
  level or stack claims, several-structure synthesis, and moved burdens.
- `C.11` governs the bounded choice after alternatives are available; `C.18` governs alternative generation and
  `C.24` later implementation sequencing when those questions are current.
- `C.2.1`, `C.29`, and the applicable model-use, evidence, configuration, and assurance patterns govern the
  epistemes and correspondences used by the decision.
- `SYSE.20` supplies one bounded platform-design constraint to `SYSE.12`. It supplies one project-local Method
  variant observation to `SYSE.21`, where cultural continuation is evaluated.
- Operations Management retains continuing-flow specialization; Organization Change Engineering retains
  organization capability and assignment changes; application DPFs add the physical, computational, clinical,
  legal, safety, or other specialist distinctions that change their engineering action.

### SYSE.20:End

<a id="syse-21"></a>
## SYSE.21 — Deliberately Continue and Change Systems Engineering Culture

### SYSE.21:0 — Use This When

Use this pattern when an engineering organization wants to retain, change, branch, or stop a Systems Engineering
Method variant and needs to know what practitioners actually do. Standards, training, conference discussion, and
tool promotion may describe one culture while project Work enacts another.

Begin with a bounded practitioner population, period, engineering profile, and representative Work. Identify the
Method variant from that Work. Then state which cultural-continuation relations are observed—for example
transmission, receiving enactment, recognition, local selection, memory, retention, or loss—and which remain
unknown.

The first useful result has two parts: a **project-local cultural-continuation account** and a separate
**practice-change decision**. The account identifies the enacted Method variant, supported cultural claims, later
engineering observations, consequences for named affected Systems, retained alternatives, evidence gaps, and
reopen conditions. The decision records one bounded choice and its authority.

An authorized Agent performs the decision Work. Other Agents perform the intervention and later engineering Work.
A project choice supplies one possible input to cultural change; later Work and cultural relations establish what
continued in the population.

Use `C.36` alone when the general cultural-evolution account is enough. Use this pattern when the decision also
depends on engineering configuration, integration, assurance, release, service, practitioner burden, or
consequences for the project system-of-interest or other named affected Systems. Use `SYSE.15` for the project-profile Method repertoire and `SYSE.20` for a conflict
among Method and Work structures. Use an application DPF when the decisive distinction comes from, for example,
software, electrical, maritime, building, medical, or manufacturing engineering.

### SYSE.21:0.1 — Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| Systems Engineering Discipline | A `U.Discipline` established through `C.20`. When that result is unavailable, the pattern uses *Systems Engineering* as a discipline-facing label and states the bounded practice population directly. |
| Systems Engineering culture | An ordinary phrase for a bounded cultural-evolution case concerning identified Methods, Work, practitioner Agents, carriers, and supported cultural relations. The phrase introduces no additional root kind. |
| practitioner population | Agents selected by a stated inclusion rule for one place, period, engineering profile, and claim. A roster is an episteme describing this population. |
| enacted Method variant | An identified `U.Method` enacted by representative dated Work in the population and period. Its MethodDescription and public labels are separate epistemes. |
| carrier | An identified System, episteme, or publication bearer used in a stated transmission, memory, mediation, or evidence relation. State the bearer's kind and relation. |
| variant generation | Work or another grounded occurrence that produces or differentiates a Method, MethodDescription, arrangement, or other variant. Production of a description establishes that episteme; Method identity is established separately. |
| transmission | A relation by which a variant or its description becomes available to another Agent or population. Receiving enactment requires later Work. |
| receiving enactment | Work by a receiving Agent that enacts the identified Method under applicable conditions. |
| recognition | A supported relation through which an Agent or population treats a variant as distinguishable and relevant to a use. |
| cultural selection | Later relations showing that Agents in the population choose, reproduce, or transmit one variant during the stated period. |
| memory | Bearers and use relations through which later Agents can recover and apply the variant. |
| retention | Repeated later enactment or reproduction in the population, with the carriers and conditions needed for continuation. |
| loss | A bounded cessation claim about an earlier variant, carrier, relation, or capability in the named population and period. |
| practice-change decision | An authorized project choice among admitted continuation alternatives. Later intervention Work and effects are separate occurrences and claims. |

The rows above define the claim names used by this pattern. They are not a closed ontology of cultural evolution;
another cultural claim keeps its own direct pattern and relation.

An Agent performs Work. For example, a repository or publication can preserve a carrier, an AI Agent can perform
bounded Work when it has the needed agency and capability, and a standard or description states claims. These
participants keep their own relations.

### SYSE.21:1 — Problem Frame

Systems Engineering changes through Methods, descriptions, tools, platforms, assignments, evidence arrangements,
and practitioner populations. A configuration-linked release Method can spread in one organization while a staged
handoff remains current elsewhere. An AI Agent can generate candidate impacts while engineering Agents retain
review and release authority. One application profile can integrate continuously while another preserves a
physical test guard.

A project can deliberately design and choose an intervention, but continuation remains distributed. Practitioners
may ignore the description, adapt the Method, retain another branch, or recover an older variant when their
situation changes. Conversely, a variant can spread without formal endorsement.

Public visibility is evidence about communication. Project Work is evidence about enactment. A bounded expert
estimate can support a decision when a larger study is unavailable, provided that its population, period, basis,
uncertainty, and decision limit are stated. The project needs enough evidence for a reversible next move, not an
unaffordable census of the profession.

### SYSE.21:2 — Problem

Two shortcuts cause expensive errors. The first treats a standard, certification, tool installation, school name,
or public claim as proof that engineering practice changed. The second refuses any action until field-wide
prevalence and causal effectiveness have been measured.

The first shortcut can impose a fashionable Method that no representative Work enacts. The second can preserve a
costly incumbent after local evidence already supports a bounded trial. Both hide the practical questions: which
Method is enacted, which relations carry it forward, who may change the arrangement, what burden moves, and what
later engineering consequence would justify retaining or stopping it?

### SYSE.21:3 — Forces

The recurring tensions are:

- A familiar school or branded Method improves communication, while one label can cover incompatible Methods and
  authority arrangements.
- A project can revise a description or tool quickly, while receiving enactment and retention depend on later
  Agents and Work.
- Repeated local use can support a bounded cultural claim, while transfer to another profile needs new evidence.
- AI Agents can make variant generation cheaper, while review, provenance, configuration, assurance, and
  authority can become limiting contributions.
- Official sources are highly visible, while commercial and local engineering Work can follow different Methods.
- Shared carriers help transmission, while forced uniformity can erase a useful profile branch.
- A local performance gain can justify continued trial, while short exposure supplies weak causal evidence about
  safety or effectiveness.

### SYSE.21:4 — Solution

Recover the enacted Method variant and the cultural relations supported in the named population. Compare
materially different continuation alternatives, let an authorized Agent choose a bounded intervention, and use
later engineering Work to decide what continued and whether the repertoire or capability question should reopen.

#### SYSE.21:4.1 — Pattern-Use Unfolding

The Method has eight recurring moves. They organize use of this pattern; variant generation, transmission, enactment,
selection, intervention, and later observation can overlap or occur through different Agents.

1. **Practice boundary.** The Agent names the engineering profile, project or organization, place, period,
   practitioner population, the project system-of-interest when one is designated or another decision-relevant
   world-side subject, affected Systems, and receiving decision. A `U.Discipline` is named only when a compatible
   `C.20` result is available.
2. **Enacted variant.** Representative Work identifies the performing Agents, enacted Methods, subject
   configuration, results, and evidence window. A compatible `SYSE.20` account can supply the local Method-and-
   Work architecture and one project variant observation.
3. **Cultural claims.** For each claim needed by the decision—for example generation, transmission, receiving
   enactment, recognition, cultural selection, memory, retention, or loss—the Agent states the variant,
   participants, relation, population, period, evidence, and uncertainty. Missing links remain gaps.
4. **Decision and authority.** The deciding Agent, assignment when attribution matters, decision Method, direct
   authority, and permitted practice-change scope are identified separately.
5. **Continuation alternatives.** The finite current option set includes a feasible incumbent and candidates that
   change a Method or another decision-bearing relation. Common disposition families are retain, change, branch,
   and stop or revert; the project gives each admitted option concrete content.
6. **Engineering comparison.** Alternatives are compared on the engineering consequences that matter to this
   use. Evidence may include, for example, direct observations, small cases, qualified expert estimates,
   self-reports, institutional descriptions, or publication-visibility measures; each keeps its epistemic status.
7. **Choice and intervention.** The deciding Agent performs decision Work by applying `C.11` or a domain
   decision Method. That Work produces a decision result naming the selected option or next probe, accepted
   losses, fallback, implementation request, and reopen conditions for the authorized intervention-planning use.
   Later Agents perform the intervention Work.
8. **Observation and feedback.** Later Work supplies cultural and engineering observations. The Agent making the
   project-profile Method-repertoire decision reopens `SYSE.15` only when compatible feedback crosses a stated
   repertoire limit. A human capability-demand result is supplied to
   `HCD.1` only when the human holders, representative Work, capability need, and evidence are recoverable.

#### SYSE.21:4.2 — Record the Result

The cultural-continuation account contains the seven result positions below. This is the complete content set for
the first result of this pattern.

| Result position | Required content |
| --- | --- |
| use boundary | Engineering profile, project or organization, place, period, project system-of-interest when designated or another decision-relevant world-side subject, affected Systems, practitioner population, receiving decision, and Discipline result or bounded discipline-facing label. |
| enacted variant | Identified Methods, MethodDescriptions, representative Work, performing Agents, subject configuration, results, evidence window, and stop condition. |
| cultural claims | Every asserted cultural relation with its variant, participants, population, period, evidence, uncertainty, and missing links. |
| decision reference | Deciding Agent, authority, fixed options, comparison basis, choice rule, selected intervention or next probe, fallback, accepted losses, limits, and a reference to the separate practice-change decision. |
| later observations | Performed intervention and later engineering Work, observed cultural relations, practitioner burden, engineering consequences, consequences for the project system-of-interest or other named affected Systems, and causal limits. |
| downstream use | Compatible repertoire feedback for `SYSE.15`, compatible human capability-demand input for `HCD.1`, or the named missing result that prevents either use. |
| continuation | Retained alternatives, evidence gaps, source and carrier references needed by later use, and reopen conditions. |

When a suite-level reference product summarizes this result, it begins with the bounded Discipline or practice
boundary, Method variant, practitioner population, place and period, carriers, deciding Agent and authority, and
intended consequence. That summary remains a reference to this result, not another cultural claim.

#### SYSE.21:4.3 — What Changes in Practice

Engineers stop using public prominence as a proxy for engineering culture. They inspect representative Work,
choose one reversible change, and say what later observations would support retention, branching, or stopping.
Project evidence can then revise a bounded Method repertoire without claiming that the whole profession has
changed.

### SYSE.21:5 — Worked Case: Continue an AI-Assisted Release Method

PumpWorks is a constructed case. Two release cells prepare controller and mixed physical-control changes for a
district-heating pump station. A practice council must decide whether to continue an AI-assisted release Method
after one trial. The decision concerns PumpWorks during 2026-Q4 and 2027-Q1; it makes no field-wide prevalence
claim.

The case supports two `B.1.5` Method-part relations inside the candidate Method:

1. an AI Agent generates claim-sized change-impact candidates with source, configuration, and effectivity
   references; and
2. an assigned engineering Agent accepts or rejects each candidate with a recorded reason before separate
   integration, assurance, and release decisions.

The Method stops when a required source or configuration reference cannot be recovered, suitable independent
review is unavailable, or a specialist safety result is missing. Its description, examples, review criteria, and
demonstration result are carriers held in an engineering repository.

The first release cell enacts the Method during one 2026-Q4 release-preparation Work occurrence. The AI Agent
generates candidates; an assurance pair reviews them; the cell prepares the evidence set. One previously missed
controller-to-sensor dependency is found before integration. Review effort increases because source checking,
configuration binding, and rejection explanations are now explicit.

An enablement team then performs Work that makes the MethodDescription, examples, criteria, and demonstration
result retrievable by the second release cell. Retrieval establishes transmission of the carriers. The second
cell's later release-preparation Work establishes one receiving-enactment observation.

During 2027-Q1 the two release cells choose and enact the same Method for three further eligible changes. Every
evidence set keeps the required references, independent review, and manual fallback. Review effort is 5.2, 5.8,
and 5.5 person-hours, below the project's six-hour limit.

The case asserts the following seven cultural claims; this is the complete claim set used by the current decision:

| Claim | Evidence and boundary |
| --- | --- |
| variant generation | Method-design Work produced the MethodDescription, while `A.3.1` and the reusable action identify the Method itself. |
| transmission | Enablement Work and repository access made the carriers retrievable by the second release cell. |
| receiving enactment | The second cell performed release-preparation Work that enacted the Method under compatible conditions. |
| local cultural selection | Both cells chose the Method over the manual fallback for all three eligible 2027-Q1 changes. |
| memory | The cells repeatedly retrieved and used the same description, examples, and criteria editions. |
| retention | Four later enactments across both cells continued through the stated period with the same fallback and review conditions. |
| local carrier loss | The repository stopped presenting an older prompt-only instruction; the claim concerns access through that repository only. |

The practice council considers three admitted alternatives as its fixed option set:

| Option | Decision-bearing change | Expected gain | Moved burden or limit |
| --- | --- | --- | --- |
| A — retain manual impact review | Use the incumbent search and checklist without AI candidate generation. | Familiar evidence and authority arrangement. | More candidate-generation effort and the previously observed missed-dependency risk. |
| B — continue bounded AI assistance | Keep AI candidate generation with source and configuration references, recorded review reasons, independent review, and a replayable rejected-candidate sample. | Faster, more inspectable candidate generation. | More provenance, review, and replay Work. |
| C — stop and revert | Remove the AI Agent from the arrangement and restore the incumbent description. | Removes AI-source and integration uncertainty. | Loses the observed candidate-generation contribution. |

A candidate in which the AI Agent issues release recommendations is screened out before the option set is fixed:
the practice council lacks that authority and compatible assurance evidence. That finding becomes a separate
future authority and assurance question rather than a disguised current option.

The comparison rejects any option that loses configuration identity, source provenance, independent review,
safety or release authority, or service protection. Among survivors it prefers fewer unexamined impact
hypotheses, lower total burden, and reversibility. The council selects B, retains A as the manual fallback, and
uses C as the stop condition when references or review fail.

Later Work supports a bounded repertoire update from *defer after the first trial* to *retain for this change
class with references, independent review, and fallback*. It does not yet supply an `HCD.1` input: the case has
team-level review burden but no observation identifying which human-holder capability needs development. The next
capability inquiry must identify those holders, their representative Work, and the limiting capability.

District-heating service continues during the case. This is a service observation; the short case does not
attribute it causally to the Method. Reopen when the profile, population, Method or carrier edition, six-hour
burden limit, safety authority, or a consequence for a named affected System changes.

### SYSE.21:6 — Bias Annotation

The following five biases recur in the source guides and evidence used by this pattern.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| official-source bias | A standard, certification, public programme, or declared conformance is treated as enacted current practice. | Recover representative Work in the named population and period. |
| publication and teaching bias | Academic attention, curricula, press, or tool promotion is treated as project use or practical worth. | Keep visibility, teaching, recognition, enactment, selection, and engineering consequence as separate claims. |
| lifecycle and maturity bias | A stage diagram or maturity ladder becomes the natural cultural direction. | Recover the Methods, Work structures, variants, guards, and consequences before comparing arrangements. |
| software-transfer bias | Software evidence sets the cadence and authority of physical engineering. | Transfer only the supported contribution and preserve the receiving profile's physical and specialist constraints. |
| measurement maximalism | The project waits for a field-wide study it cannot afford. | Use proportionate evidence with explicit population, period, basis, uncertainty, and decision limit. |

### SYSE.21:7 — Conformance Checklist

The following conditions are required for a conforming use of this pattern.

- [ ] The pattern use names the engineering profile, population, place, period, project system-of-interest when
      designated or another decision-relevant world-side subject, and receiving decision.
- [ ] Representative Work and enacted Methods ground the current variant.
- [ ] Performing Agents, participating Systems, MethodDescriptions, carriers, and result epistemes retain their
      own relations.
- [ ] Every asserted cultural claim names its variant, participants, population, period, evidence, and
      uncertainty.
- [ ] The deciding Agent, decision Work, assignment when needed, and direct authority are recoverable.
- [ ] The fixed options differ through an engineering Method or another decision-bearing relation.
- [ ] The comparison includes engineering consequences, consequences for named affected Systems, and every
      material moved burden.
- [ ] Project choice, intervention Work, later enactment, cultural selection, retention, and effect remain
      separate claims.
- [ ] Repertoire and human-capability returns cross the receiving result's stated threshold and use boundary.
- [ ] A cold engineer or manager can state the next action, stop, and reopen condition without decoding private
      identifiers.

### SYSE.21:8 — Common Failures and Repairs

The rows below are documented recurring failures from the source guides, cultural-evolution literature, and the
two engineering probes used by this pattern.

| Recurring failure | Repair |
| --- | --- |
| A school or branded label is treated as the Method and its history | Recover the Methods, Work, population, carriers, and supported cultural relations. |
| A revised description is reported as changed practice | Establish the world-side Method and later enactment separately. |
| Tool deployment is reported as receiving enactment | Identify dated Work that enacts the Method under compatible conditions. |
| A project pilot is reported as population selection or retention | Obtain separate later enactment, selection, and retention evidence. |
| Press, academic, certification, or teaching visibility is reported as prevalence | State the proxy and population limit; use representative Work or a qualified estimate for actual practice. |
| A team label, tool, or document is said to engineer and decide | Identify each performing Agent, Work occurrence, Method, result relation, and authority. |
| One profile's case is transferred to all Systems Engineering | Keep the profile, population, period, and unlike-case comparison visible. |
| A faster local task is enough to retain the variant | Inspect integration, evidence, assurance, service, practitioner burden, and consequences for the project system-of-interest or other named affected Systems. |
| Every observed difficulty becomes a human training request | Separate Method, tool, assignment, organization, authority, human capability, and nonhuman capability causes. |

### SYSE.21:9 — Consequences

The project can improve actual engineering practice without claiming control over a profession. Current enactment,
project intervention, cultural continuation, and consequences for named affected Systems remain inspectable. Bounded evidence
can revise a Method repertoire, while missing human capability evidence becomes a specific inquiry rather than a
generic training request.

The cost is later observation and claim separation. Some links remain unknown, useful variants can branch by
application profile, and short projects rarely settle prevalence or causal effectiveness. The result keeps those
limits actionable through fallbacks, probes, bounded transfer, and reopen conditions.

### SYSE.21:10 — Rationale

`C.36` supplies the transdisciplinary cultural-evolution distinctions. Systems Engineering adds a recurring
domain decision: an engineering Method variant is worth continuing only in relation to configured project Work,
integration, evidence, assurance, release, service, practitioner burden, and consequences for the project
system-of-interest or other named affected Systems.

A Method can be described before it is enacted, and a project can create conditions for later enactment. Only
later Work and cultural relations show which variant continued. Keeping project choice and distributed
continuation separate supports both deliberate improvement and honest uncertainty.

### SYSE.21:11 — SoTA and Source Use

This table is the complete source-use register for this pattern body.

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| R7 sections *Вариативность культур* and *Эволюция методов* | Method variants, professional carriers, changing mastery, and the distinction between simultaneous enactment and sequential teaching descriptions. | Treat R7 as practitioner synthesis; recover each current Method, Work occurrence, cultural relation, and evidence claim through current FPF. |
| R8 sections on scale-free evolutionary Systems Engineering | Continuing engineering, co-evolution of target and builder Systems, and profile-sensitive transfer. | Treat its pedagogical stacks and dated institutions as source descriptions; establish the receiving Method architecture and population separately. |
| Current FPF `C.36`, `C.36.P`, `C.20`, `A.3.1`, `A.3.2`, `A.15.1`, `C.11`, `A.10`, `E.10`, `E.10.ROLE`, `F.18`, and `F.19` | Cultural relations, wording recovery, Discipline construction, Method and Work identity, choice, evidence, and precise plain language. | This DPF adds the engineering profile, engineering consequences, repertoire feedback, and human capability-demand interface. |
| The power-converter case in `SYSE.20` and the PumpWorks case here | Unlike engineering probes for overlap/order and deliberate cultural continuation. | Treat them as constructed cases; use project observations or qualified estimates for actual prevalence and effect. |
| [DORA, *State of AI-assisted Software Development 2025*](https://dora.dev/research/2025/dora-report/) | Evidence that AI use interacts with the underlying organizational System and can amplify strengths and weaknesses. | Apply the evidence to its stated software population and measures; test physical-engineering transfer separately. |
| [Kemell et al. 2025, *Still just personal assistants?*](https://doi.org/10.1016/j.infsof.2025.107805) | Exploratory observations of GenAI use and adoption difficulties across seven European software companies. | Use as a bounded adoption comparison; the small software sample supplies no field-wide prevalence claim. |
| [Luke et al. 2026, *How are professional practices adopting generative AI?*](https://doi.org/10.1017/pds.2026.10600) | A three-week embedded case in one automotive engineering-design organization, including workflow fit, toolchain, governance, skill, and sustained-use concerns. | Use as one profile-specific case; test wider enactment and benefit with later Work. |

Reopen the affected source-use claim when a later edition or representative Work changes the practical move. A
new publication or tool release alone supplies no cultural relation.

### SYSE.21:12 — Relations

The following direct relations are used by this pattern body.

- `C.36` governs the general cultural-evolution case and direct cultural claims; `C.36.P` restores overloaded
  culture, practice, school, community, and regime wording.
- `C.20` governs any `U.Discipline` claim. A bounded practitioner population can be used while that wider claim is
  unresolved.
- `A.3.1`, `A.3.2`, `A.15.1`, and `F.6` govern Methods, MethodDescriptions, performed Work, and attribution when
  needed. `A.13` supplies the agency test when a performing System's agency is disputed.
- `C.11` governs the project choice; the applicable authority relation governs permission. `A.10` and the effect
  patterns govern evidence and causal claims.
- A compatible `SYSE.20` result supplies only the local Method-and-Work architecture, project variant, and bounded
  choice for its stated use. `SYSE.21` establishes any later cultural claim separately.
- `SYSE.21` supplies revision feedback to `SYSE.15` only when later evidence crosses a repertoire limit. The
  `SYSE.15` Agent makes the repertoire decision.
- Cross-DPF result `XRI-21` supplies `HCD.1` only with a current human capability demand for compatible holders,
  Method, Work, period, and evidence. Nonhuman capability development remains with its applicable pattern.
- Application DPFs retain their profile-specific physical, computational, clinical, legal, safety, and specialist
  Methods. Organization Change Engineering retains organization capability and assignment change; Method
  Engineering retains Method construction.

### SYSE.21:End

# Cross-Pattern Applications

`APP-SYSE-01` and `APP-SYSE-02` are navigation walkthroughs: they show where pattern results enter and which
dependencies matter, but they do not provide filled evidence from which to reproduce a recommendation.
`APP-SYSE-03` and `APP-SYSE-04` are worked applications. The first tests a software-only migration; the second
tests a cyber-physical greenhouse decision that includes internal, provider, and mixed realization arrangements.
They show intermediate values, resulting recommendations, and observations that reopen each result. None is a
project lifecycle: Work may overlap, and an order is asserted only where one result cannot be used before another
exists.

## APP-SYSE-01 — Navigation walkthrough: release a vibration-control change for a district-heating pump station

`DistrictHeating-PumpStation-17` must receive changed vibration-control configuration `PS17-C42`. The change
combines a physical pump-train modification, control-software changes, updated operating limits, and a trialled
AI-assisted analysis Method. District heating must continue. A component test can pass while station-level
functioning or a downstream condition still fails, and an earlier source can change during release preparation.

### 1. Recover the subject, use, and consequences

Use `SYSE.1` to designate the actual station as the project system-of-interest and keep that designation distinct from
the System's identity. Use `SYSE.16` to recover the containing district-heating arrangement, operating neighbours,
conditions, and part and interaction relations. Use `SYSE.17` to identify Systems that can bear engineering
consequences, including the operator, connected heating network, maintainers, and affected users. Use `SYSE.2`
to keep the proposed operating use and the changed station concept linked.

The first return is either a bounded focus and linked concepts or a named blocker. If the station configuration,
using System, operating interval, or consequence claim cannot be identified, do not compensate with a generic
stakeholder list or release checklist.

### 2. Compare architecture choices

Use `SYSE.5` to compare functional contributions, physical and software bearers, and interfaces for vibration
control under the declared operating conditions. Use `SYSE.6` to select an architecture candidate and state the
trade-offs, accepted losses, evidence, and reopen conditions. Architecture and assurance Work may overlap; the
architecture decision still cannot rely on an assurance result that does not yet exist.

### 3. Bind change and evidence to configuration

Use `SYSE.13` to identify `PS17-C42`, its parts, software realization, variant relations, and effectivity. Use
`SYSE.14` to connect the proposed and performed change to the deciding System, permission, implementation,
release question, actual configuration, cited evidence, and unresolved conditions. A release decision does not
become its cited evidence and does not transfer release authority to the assurance practitioner.

Use `SYSE.4` to check compatible results before planning new challenge Work. Component evidence applies only to
its component claim and conditions. Station and downstream observations apply to their own claims. The
engineering-assurance account can support, narrow, or refuse reliance for the release question; an independent
safety permission remains a separate specialist result.

### 4. Bound the Method and cultural return

Use `SYSE.15` to decide whether the trialled AI-assisted analysis Method belongs in the engineering repertoire,
for which claim class, with which evidence and exclusions. Use `SYSE.21` only if the question extends beyond this
release to transmission and retention across a named practitioner population. Record later enactment and project
consequences; do not infer cultural retention from the local trial or publicity around the tool.

### Result and stop

The bounded result is a recommendation to release `PS17-C42` only after the named restored-function check, with
configuration, effectivity, evidence limits, unresolved safety permission, and the AI-assisted Method
disposition explicit. Stop there when the release authority can decide. Return missing permission, long-horizon
bearing-temperature observation, source claim, configuration fact, or specialist result to its source. Reopen
only the decisions whose relied-on System, use, configuration, evidence horizon, or Method basis changed.

## APP-SYSE-02 — Navigation walkthrough: develop a district-heating inspection System family while the damage-detection problem changes

Engineering team `ET2` develops successive inspection Systems for district-heating networks. Candidate `IS-A`
combines a mobile sensing unit, models, an operator interface, and an evidence service. Candidate `IS-B` changes
both sensing and builder-platform assumptions. The problem portfolio contains distinguishable questions about
early damage recognition, false alarms, inaccessible locations, operating interruption, evidence for
intervention, and deployment burden.

### 1. Bound the project and keep two portfolios visible

Use `SYSE.1`, `SYSE.16`, and `SYSE.17` to identify the actual System or intended-system designator selected as the project system-of-interest, operating environment, and Systems that may
bear consequences. Use `SYSE.22` to keep problem formulations and System-family options distinct but connected.
Each problem has its own affected Systems, comparison and acceptance conditions, evidence horizon, and
currentness. Each System option has a recoverable family and configuration relation. Neither portfolio becomes a
fixed requirement list or a bag of unrelated ideas.

### 2. Compare options and choose the next evidence

Use `SYSE.2`, `SYSE.5`–`SYSE.7`, `SYSE.10`, and `SYSE.13` to keep use concepts, architecture candidates,
descriptions, evidence, family identity, configuration, and effectivity comparable. The deciding Agent applies `SYSE.22` in problem-and-option decision Work and records one
replayable next-decision `ChoiceResult` for later planning or authorization. The Agent records a bounded probe only when a named feasible probe can change
the decision enough to justify its cost. Otherwise the Agent chooses among surviving options, rejects the option
set, or sends a question or missing-authority result to the Agent responsible for the named receiving decision.

### 3. Separate the designated System, builder arrangement, platform, Method, Work, and culture

Use `SYSE.3`, `SYSE.11`, and `SYSE.12` to identify the realization arrangement, usable increments, and engineering
platform contribution. Use `SYSE.20` to distinguish simultaneous Work from dependencies that require order.
Use `SYSE.15` for the Method repertoire, `SYSE.19` when a relied-on source changes, and `SYSE.21` only for a
question about continuation across a practitioner population.

Use `SYSE.23` to compare changes to a surviving System-family option, its builder arrangement, or both. A part
or family-membership structure of an actual or intended System, a service or dependency relation with a builder
System, and Work order are different relations. Practitioner
capability and cultural continuation remain results of their own patterns. A build-before-trial dependency is a
bounded unfolding; it does not make problem development, System-family development, and builder development
three universal stages or levels.

### Result and stop

The application returns an updated problem portfolio, a reidentifiable System-family option set, supported
correspondences and unresolved mismatches, one next-decision `ChoiceResult`, a grounded account of evolvability across the selected System-family option and its
builder arrangement, separate possible-future architecture specifications, and one investment or
reconfiguration `ChoiceResult`. Stop when the named authorities can act on those decisions. Selection,
realization, adoption, cultural retention, and reliance on a future Open-Ended Evolution Engineering result
remain separate decisions and claims.

## APP-SYSE-03 — Worked application: choose and bound an authentication-service migration

This constructed case tests whether the common Systems Engineering patterns still help when the System designated as project system-of-interest
is software-only rather than electromechanical. It assumes the named software-security result; it does not teach
cryptographic design or threat modeling, decide privacy or law, or grant release authority.

### 1. Fix the System, use, and decision

`SYSE.1` identifies deployed software System `AccountAccessService`, current configuration `AS-7.4`, and the
bounded use: tenant login during a five-minute loss of communication between two regional session stores. The
next decision is whether to prepare one candidate architecture for a limited production canary. Account holders, tenant applications, the incident-response team, and the service operator are the affected
Systems relevant to this choice. The first result, `AccountAccessProjectFocus-R1`, excludes unrelated identity-
governance and user-interface changes.

### 2. Compare architecture alternatives using displayed evidence

The project's software-security Agent performed `AuthenticationThreatModelingWork-TM4` by applying
`ProjectSoftwareSecurityThreatModelingMethod`. That Work produced `AuthenticationThreatModelResult-TM4`, which
supplies two constraints used here: regional cache replication must be mutually authenticated and encrypted,
and acceptance of a revoked credential must end within 120 seconds. The architecture Agent uses those constraints
to admit alternative `A` and exclude a ten-minute bearer token under the current threat model. The result neither
selects the architecture nor grants release authority.
Using `SYSE.5`, the architecture Agent develops three materially different bearer and interface alternatives.
Using `SYSE.6`, the same Agent compares them against four declared limits: failed logins below 1%, acceptance of a revoked credential for no more than 120 seconds,
95th-percentile login latency no greater than 3 seconds, and rollback within 30 minutes. A controlled partition
replay for configuration candidate `AS-7.5-rc2` returns these values:

| Alternative | Failed logins | Revoked-credential exposure | p95 login latency | Rollback | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| `A` — replicated regional session cache | 0.6% | 80 s | 2.4 s | 18 min | Meets all four limits; adds replication and operating complexity. |
| `B` — signed ten-minute tokens with a revocation feed | 0.4% | 600 s | 1.8 s | 12 min | Rejected for this use because the 120-second security limit fails. |
| `C` — retain the single-region session store | 8.2% | 35 s | 2.1 s | 8 min | Rejected because the failed-login limit fails during the partition. |

`AuthenticationArchitectureDecision-AD7` therefore selects `A` for canary preparation. It records the added
replication burden as an accepted loss. The choice uses `AuthenticationThreatModelResult-TM4`; the table does not establish that specialist result or
transfer the specialist's authority.

### 3. Bind the recommendation to configuration, effectivity, and evidence

Using `SYSE.13`, the configuration Agent identifies candidate configuration `AS-7.5-rc2` and its proposed
effectivity: tenant cohort `TenantCohort-Canary`, 5% of eligible traffic, regions `EU-West` and `EU-Central`, for
seven days. Using `SYSE.4`, the assurance Agent qualifies the partition replay only for the four claims and
conditions shown above. It does not support wide release, other regions, a different token lifetime, or a
different threat model.

The release-preparation Agent uses `SYSE.14` with the architecture decision, configuration account, replay
result, `AuthenticationThreatModelResult-TM4`, and rollback evidence. The Work returns this recommendation: prepare alternative `A` as `AS-7.5-rc2` for the stated 5%
canary; retain `AS-7.4` as the rollback configuration; do not widen effectivity until the release Agent receives
the canary observations and the required security permission. The recommendation is not the release occurrence
and grants no authority.

### 4. What transfers and what remains specialist

The same Systems Engineering moves transfer unchanged: choose the project system-of-interest and use; expose affected
Systems; develop bearer and interface alternatives; bind claims to configuration and effectivity; qualify
evidence for a receiving decision; and keep the designated System distinct from the CI/CD and observability platform
used to change it. The software profile specializes cryptographic construction, authentication threat modeling,
privacy and data-protection analysis, secure deployment, and incident response. Their Methods, sources, and
authorities remain outside this common DPF.

### Result, stop, and reopen

Another practitioner can reproduce the recommendation by applying the four limits to the displayed values:
`A` is the only surviving architecture, and its evidence supports only the stated canary. Stop when the release
Agent can decide that canary with the named security permission and rollback available.

| Changed input | Reopen |
| --- | --- |
| project system-of-interest designation, partition use, affected Systems, or decision horizon | `SYSE.1` project-focus result |
| an architecture option, bearer/interface relation, or any of the four limits | `SYSE.6` architecture choice |
| candidate configuration, cohort, region, traffic share, or seven-day effectivity | `SYSE.13` configuration result |
| replay conditions, observation values, evidence window, or claim correspondence | `SYSE.4` evidence-use result |
| security permission, rollback availability, or canary observations | `SYSE.14` release recommendation |
| threat model, cryptographic construction, privacy constraint, or security authority | the owning software-security or legal Method and source |

## APP-SYSE-04 — Worked application: obtain climate control for a new greenhouse configuration

This case shows the common Systems Engineering patterns in a small cyber-physical equipment company. It includes
physical equipment, control software, provider Work, an AI Agent, internal capability, and continuing support.
Greenhouse-control, electrical-safety, commercial, legal, financial, and organization-design results enter as
inputs; their Methods remain with those practices.

### 1. Fix the System, use, and result to obtain

`SYSE.1` keeps `GreenhouseClimateControl-GH2` as an intended-system designator selected as the project
system-of-interest and distinguishes it from greenhouse `GH-2`, company `GreenHeat-4`, and any actual System
identity that may begin later. `SYSE.16` identifies the greenhouse,
electrical supply, heating, ventilation, misting, shading, sensors, operator station, weather, and manual fallback
that form the relevant operating surroundings. `SYSE.17` identifies operators, crops, maintainers, the equipment
company, and the greenhouse owner as Systems that can bear consequences.

The receiving use is control during three representative conditions: a cold night, a rapid solar rise, and a
failed humidity sensor. `SYSE.2` supplies linked use and System concepts. Acceptance requires bounded temperature
and humidity performance, no unsafe actuator command after sensor failure, identified controller and software
configuration, recoverable observations, and supported manual fallback. These are case inputs from greenhouse-
control and electrical-safety Methods. The case takes its thresholds from those specialist results.

### 2. Construct complete obtaining arrangements

`GreenHeat-4`'s managers initially propose buying a controller or having an AI Agent write one. The engineering
team applies `SYSE.24` and rejects those two phrases as a usable option set. A purchase is one relation inside an
arrangement; an AI Agent is one possible performer of named Work. The team uses the six arrangement prompts and
eight common questions in `SYSE.24` to construct four whole arrangements for the same required greenhouse-control
result.
| Arrangement | Agents, Work, Methods, and means | Evidence, integration, support, capability, and exit |
| --- | --- | --- |
| Ready controller plus integrator | The controller vendor's engineering team supplies a configured controller. The integration company's team performs sensor, actuator, network, and commissioning Work. `GreenHeat-4`'s engineering team maintains greenhouse requirements and accepts the result. | The controller supports the stated field interface and can be commissioned in nine weeks. Greenhouse-specific failed-sensor behaviour, configuration export, and the supervisory interface remain unsupported. Vendor support is offered for three years; changing the control logic requires vendor access. |
| Commissioned custom controller | The engineering provider's team designs and integrates a custom controller and supplies source, configuration, test evidence, and support. | The provider estimates sixteen weeks against a twelve-week need date. It proposes source escrow but has supplied no representative failed-sensor evidence for this hardware family. |
| Internal development with AI assistance | `GreenHeat-4`'s controls engineers lead the Work. A general AI Agent assists with code and test generation. An independent controls specialist reviews safety-relevant behaviour. | The company would retain knowledge and change access, but it has no qualified hardware-in-the-loop environment and no evidence that the team can finish assurance within twenty weeks. AI-produced code supplies no capability or acceptance result by itself. |
| Ready controller plus internal supervisory layer | The vendor controller retains local safety interlocks and manual fallback. `GreenHeat-4`'s controls team develops greenhouse-specific supervisory optimization through a documented interface. | The arrangement is estimated at eleven weeks and preserves internal change capability above the safety boundary. It still depends on configuration export, interface timing, and the vendor update policy; failure of any one defeats the arrangement. |

The Finance result compares resource and cash consequences. The Organization Change result states the proposed
human–AI–provider Work allocation and its authority gaps. The safety result states the protected failed-sensor
condition. The commercial and legal results state the proposed access, update, data, and remedy terms.
`SYSE.24` uses those results but does not recreate their Methods or decide their questions.

### 3. Restore parity and choose the next probe

The comparison uses the same three operating conditions, commissioning date, field interfaces, configuration
evidence, assurance burden, data access, support horizon, internal capability consequence, expected change
latency, and exit condition. The provider demonstration is not compared with an unfinished internal prototype;
both are compared with the accepted `GH-2` configuration and representative conditions.

The internal-only and custom-provider arrangements fail the need-date condition. The ready-controller and hybrid
arrangements form a tie-set because the hybrid arrangement is better for later greenhouse-specific change only
if the vendor interface preserves timing, configuration export, and supported fallback.

The ready-controller arrangement costs EUR 84,000 and eighteen internal engineering days; the hybrid costs EUR
96,000 and thirty-two internal engineering days. Both fit the need date. The operating plan expects at least three
greenhouse-specific changes in the next three years, so the deciding management team will prefer the hybrid when
its added price stays within EUR 15,000 and its added internal burden stays within fifteen engineering days, but
only after the protected interface and fallback claims are supported.

The same team is authorized to spend up to EUR 7,000, forty engineering hours, two hardware-in-the-loop laboratory
days, and five elapsed working days on this decision. The safety specialist separately authorizes the failed-
sensor injection in the laboratory. `ChoiceResult-GH2-1` is **probe again**: a EUR 5,500 replay uses thirty-two
controls-engineering hours, eight integrator hours, two laboratory days, and the available five-day reserve.

The decision rule distinguishes three outcomes. Unsafe fallback or unusable configuration export rejects both
survivors. Safe fallback and export combined with failed supervisory timing or unsupported API retains only the
ready-controller arrangement. If fallback, export, API support, and timing all pass, both survive and the stated
price-and-burden rule selects the hybrid. Without the replay, neither survivor has enough evidence for a lawful
choice; rejecting both would discard an arrangement that the bounded replay can retain.

The performed replay returns the third outcome: the local controller enters the supported fallback without an
unsafe actuator command, the supervisory command round trip remains below the application-profile limit, and the
configuration export reidentifies the tested controller and software values. The safety specialist limits the
first observation to the tested failure and configuration. The deciding Agent applies `C.11` again and records
`ChoiceResult-GH2-2`: **choose now** for the hybrid arrangement under that basis. A different safety limit or
withdrawn vendor-update support would reopen the choice.

### 4. Continue with realization, configuration, and assurance

The realization Agent applies `SYSE.3` to the retained arrangement and identifies its first unsupported realization branch: whether the
internal integration Agent can configure the supervisory layer and produce the commissioning evidence before the
need date. The vendor controller is a supplied System and the AI Agent is a possible performer in selected Work;
neither becomes the whole realization arrangement.

`SYSE.13` identifies controller, software, interface, sensor, and greenhouse configuration and effectivity.
`SYSE.10` keeps the hardware-in-the-loop replay tied to the claims it observed. `SYSE.4` states which acceptance
claims may rely on those observations and which still need greenhouse commissioning evidence. `SYSE.14` governs
the later change and release decision. Performed integration Work, accepted configuration, payment, provider
duty, and changed internal capability remain results of their own Methods.

### Result, stop, and reopen

The worked application returns a project-System focus, linked use and System concepts, four comparable whole
obtaining arrangements, one evidence-qualified `C.11` choice, and the first unsupported realization branch. The
decision-making Agent can now commit the hybrid arrangement without claiming that integration or acceptance has
already happened.

Stop there. Reopen `SYSE.24` when the result, use, need date, provider capability, interface, configuration
export, support, internal capability, evidence, or exit condition can reverse the choice. Reopen only the
affected realization or assurance result when the arrangement remains preferred but one branch or claim fails.

# Framework Boundary and Refresh




## Intended use and non-use boundary

Use this framework for recurring common Systems Engineering difficulties that materially change decisions about
an engineered System, its use and operational environment, problem formulations and System-family options,
architecture, realization, enabling platform, configuration, evidence, evolvability, continuing change, or
engineering Method. It is intended for engineers, engineering
managers, architects, technical leads, specialist contributors, and assisting agents able to use the required
FPF distinctions and domain evidence.

Do not use the framework as a substitute for an application profile or specialist decision. It does not provide
software algorithms, electrical design rules, naval architecture, structural calculations, medical regulation,
safety cases, security controls, legal advice, financial authority, certification criteria, or organization-
change Methods. It tells a Systems Engineering practitioner where such a result enters, what claim and decision
it may support, and where authority remains outside this framework.

## PatternID discipline

`SYSE.*` identifies patterns in this Systems Engineering Principles Framework. A PatternID is an address for an
authoritative pattern body, not a project stage, organizational function, document type, SystemRole, or claimed
sequence. The five Parts, six ordinary practical entries, and two Practical-Use Cards group patterns for reading; they
create no semantic parent, Method composition, project order, or separate framework.

## Source use and epistemic status

Each pattern carries its own source-use decisions, adopted payload, rejected shortcuts, evidence limits, and
reopen conditions. Standards, textbooks, academic attention, vendor claims, institutional promotion, and press
coverage can identify candidate Methods or terminology. They do not by themselves show actual project use,
causal effectiveness, widespread retention, or state of the art. When direct prevalence evidence is unavailable,
use an explicit expert estimate with a stated uncertainty instead of manufacturing a measurement programme.

Current common engineering, AI-native engineering, Platform Engineering, configuration and change,
architecture, assurance, continuous engineering, and cultural-evolution sources can change quickly. Return first to the source-use claim on which the affected pattern relies. Reopen only the dependent claim, example, relation, or pattern
unless the new evidence defeats the framework field boundary or a cross-pattern result relation.

## Dependence on FPF and neighbouring products

FPF remains the source for transdisciplinary ontology, holons and Systems, Method and Work distinctions,
architecture, evidence, assurance, decisions, cultural evolution, precision restoration, pattern form, and DPF
publication form. This framework specializes those moves for common Systems Engineering. A relied-on FPF result
remains external to this DPF; citing it does not make it a `SYSE.*` pattern.

Application-profile frameworks and direct specialist sources remain external. Another DPF may use a named
Systems Engineering result only when the subject, conditions, edition or current state, receiving use, and
availability fit. Co-listing in a collection or Guide does not establish dependency, compatibility, currentness,
or authority.

## Edition scope and refresh

The first edition contains the 24 `SYSE.*` pattern bodies indexed in this publication carrier, this Readme,
this Preface, two navigation walkthroughs, two filled cross-pattern applications, and this boundary-and-refresh
unit. The bodies remain the authority for working moves; the Readme, Preface, ToC, and applications help readers
find and combine them.
Recheck the affected pattern and its receiving relations when:

- an FPF dependency changes a kind, relation, evidence, architecture, Method, Work, culture, or publication rule
  used by the pattern;
- a direct source changes a load-bearing engineering claim or exposes a better current Method;
- a project case shows that a pattern's first result, stop, authority boundary, or specialist return is wrong;
- repeated use shows that two patterns duplicate the same move or that one recurring Systems Engineering problem
  family remains uncovered;
- an application profile shows a common specialization that changes the cross-profile working move; or
- the publication carrier no longer preserves the pattern bodies, first entries, cross-pattern use, source return, or
  framework boundary for its intended readers.

Refresh the smallest affected unit first. Reopen the framework architecture only when evidence changes the
promised field, selected problem families, pattern split, material result relations, publication form, or
maintenance boundary.
