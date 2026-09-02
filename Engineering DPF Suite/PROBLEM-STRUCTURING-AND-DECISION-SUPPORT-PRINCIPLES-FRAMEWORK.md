# Problem Structuring and Decision Support Principles Framework

> A domain pattern language for clarifying difficult situations, structuring inquiry, comparing alternatives, and returning qualified decision support.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 3 September 2026
- **Status:** Eternal alpha: a published working framework, already used in analyses and worked applications, while continuing to evolve.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

Begin with the difficulty that blocks useful work: what problem is being addressed, whose concerns matter, which inquiry result is missing, or what the available evidence supports returning to a decision-maker.

Use the Table of Contents below to search by a familiar term or working question and find the relevant PatternID. Open the pattern and apply its Problem frame, Solution, worked cases, and checklist to your actual inquiry or decision-support question. Start with the smallest useful result; use another pattern when its contribution is needed, and keep the recipient's choice separate from the advice.

The Readme offers selected practical entries, and the Preface explains recurring distinctions. The full Table of Contents also serves questions outside those examples; the pattern bodies supply the working moves, conditions, and stops. For references to this version, use the [Citation](#citation).

First edition — [edition and use record](PRODUCT-SERIES-AND-PUBLICATION-DECISION.md#edition-and-use).

# Table of Contents

Search the questions and keywords for the result you need. PSD numbers are stable pattern addresses; Parts and positions are reading order, not a workflow. Dependencies below name direct governors and conditional uses, not a requirement to run every listed pattern.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Readme — Problem Structuring and Decision Support](#readme--problem-structuring-and-decision-support) | Find a direct first result and an honest stop for the question at hand. |
| [Citation](#citation) | Cite the framework or one pattern with its author, release date and publication address. |
| [Preface](#preface) | Understand how qualified contributions help without taking another practice's result or the recipient's choice. |
| [Development-direction advising](#psd-advising-development-direction-advising) | Compose development-direction advice from qualified holder-specific results. |
| [Construct a Bounded Development Opportunity](#psd-opportunity-construct-a-bounded-development-opportunity) | Construct a useful conditional opportunity before a result is settled, without requiring an adviser. |
| [Cross-pattern applications](#cross-pattern-applications) | Follow the contested flood and development-direction uses with their scope and source limits. |
| [Framework boundary, sources and refresh](#framework-boundary-sources-and-refresh) | Find the covered problem families, external returns, source arguments and affected-refresh conditions. |

**Part I — Engagement, Participation, Formulation and Boundary**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [PSD.1 - Bound the Decision-Support Engagement and Authority Boundary](#psd-1) | Candidate | *Keywords & queries:* engagement, authority, recipient. What advice is needed, for whom, and who makes the later choice? | FPF A.15.9, A.10, C.11; PSD.2–PSD.4 when participation, formulations or scope remain live. |
| 2 | [PSD.2 - Recover Participants, Concerns, and Affected Systems](#psd-2) | Candidate | *Keywords & queries:* participants, concerns, affected Systems. Whose consequential concern or absence could change the inquiry? | Uses the bounded PSD.1 question; FPF A.1.CSD for consequence-bearer discovery. |
| 3 | [PSD.3 - Generate Plural Problem Formulations](#psd-3) | Candidate | *Keywords & queries:* plural formulations, framing, disagreement. Which different accounts imply different inquiries or interventions? | PSD.1 and PSD.2 when their results are needed; FPF C.17 and C.18 only for their direct objects. |
| 4 | [PSD.4 - Set and Reopen the Problem Boundary](#psd-4) | Candidate | *Keywords & queries:* boundary, exclusions, scope, revision. What is the smallest usable cut, and what would reopen it? | Qualified PSD.1–PSD.3 inputs; FPF A.2.6 for exact scope membership when required. |

**Part II — Models, Methods and Facilitated Inquiry**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 5 | [PSD.5 - Construct Complementary Situation and Option Models](#psd-5) | Candidate | *Keywords & queries:* complementary models, questions, assumptions, losses. Which model supports which claim, and where does the join fail? | Qualified inquiry inputs; FPF A.1.1, C.29 and A.10; PSD.6 or PSD.7 for their live questions. |
| 6 | [PSD.6 - Select and Combine Problem-Structuring Methods](#psd-6) | Candidate | *Keywords & queries:* problem-structuring Methods, fit, combination. Which reusable way supplies the missing contribution under these conditions? | PSD.1; PSD.5 and PSD.7 when joined; FPF A.3.1, A.3.2 and B.1.5 for their exact claims. |
| 7 | [PSD.7 - Facilitate Inquiry and Preserve Material Dissent](#psd-7) | Candidate | *Keywords & queries:* facilitation, attribution, meaning, dissent. What can participants recognize and what remains materially contested? | PSD.2–PSD.4 when live; FPF A.2.9; specialist truth and authority remain direct returns. |

**Part III — Alternatives, Values, Uncertainty, Consequences and Robustness**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 8 | [PSD.8 - Generate Decision Alternatives](#psd-8) | Candidate | *Keywords & queries:* alternatives, mechanisms, staged directions. Which live candidate differs materially from the incumbent? | Bounded engagement and formulation inputs; FPF C.17, C.18 and C.38 only when their results are needed. |
| 9 | [PSD.9 - Represent Values and Trade-Offs](#psd-9) | Candidate | *Keywords & queries:* values, objectives, trade-offs, compensation. Which distinctions matter, and what must a score not compensate away? | PSD.8 and PSD.11 inputs where needed; FPF A.19 and C.16 for applicable space or measurement claims. |
| 10 | [PSD.10 - Represent Decision-Relevant Uncertainty and Evidence Limits](#psd-10) | Candidate | *Keywords & queries:* uncertainty, evidence, scenarios, information. Which unknown can change eligibility, comparison or the current return? | Uses actual candidate and consequence questions; FPF A.10 for reliance and C.11 for later probe choice. |
| 11 | [PSD.11 - Compare Consequences](#psd-11) | Candidate | *Keywords & queries:* consequences, interactions, partial comparison. What follows under the stated configuration, and what comparison is warranted? | Qualified PSD.8–PSD.10 inputs; FPF C.11.CRC and A.19.CPM for their direct comparison contributions. |
| 12 | [PSD.12 - Test Robustness and Sensitivity](#psd-12) | Candidate | *Keywords & queries:* robustness, sensitivity, reversals, information value. Under which justified conditions does the result hold or reverse? | Qualified comparison inputs; PSD.10 for unresolved evidence; FPF C.11 for an actual probe choice. |

**Part IV — Recommendation, Follow-up and the Development of Practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 13 | [PSD.13 - Prepare and Return a Decision-Support Recommendation](#psd-13) | Candidate | *Keywords & queries:* recommendation, retained set, request, blocker, abstention. What can responsibly be returned now without taking the choice? | PSD.1 and the qualified contributing PSD.8–PSD.12 results; FPF A.15.9, A.10 and C.11. |
| 14 | [PSD.14 - Prepare and Use a Decision Follow-up Arrangement](#psd-14) | Candidate | *Keywords & queries:* follow-up, observation, interpretation, change. Which relied-on premise changed, and which advice must be reconsidered? | PSD.13 when recommendation follow-up is live; FPF A.10.1 and direct source or service owners. |
| 15 | [PSD.15 - Develop and Refresh Problem-Structuring and Decision-Support Methods](#psd-15) | Candidate | *Keywords & queries:* Method repertoire, fit, evidence, source refresh. Which offering should be retained, changed, tested or retired? | PSD.6 and actual follow-up evidence; direct Method-engineering and evidence results when required. |
| 16 | [PSD.16 - Reconcile Simultaneous Problem-Structuring and Decision-Support Work](#psd-16) | Candidate | *Keywords & queries:* simultaneous inquiry, coupling, interference, facilitation. Which arrangement preserves a threatened result at acceptable burden? | PSD.5–PSD.7 where their contributions interact; FPF C.32.MWA for needed several-structure synthesis. |
| 17 | [PSD.17 - Deliberately Continue and Change Problem-Structuring and Decision-Support Culture](#psd-17) | Candidate | *Keywords & queries:* cultural continuation, interpretation, retention, mediation. What changes across practitioners beyond publication or local performance? | PSD.15 and PSD.16 when current; FPF C.20 and C.36 for their direct cultural claims. |

# Readme — Problem Structuring and Decision Support

## Practical entries

Bring the question that is blocking useful work. These entries are selected examples, not a catalogue, a coverage boundary or a required sequence. Open the smallest direct pattern that can supply the missing result; use the pattern index or another finding aid when no example fits.

If the useful future contribution itself is still unclear, enter [Construct a Bounded Development Opportunity](#psd-opportunity-use-this-when) directly. You can construct an opportunity and stop at its next question without appointing an adviser. If a distinct performer must recommend a development direction to someone else, use the [advising profile](#psd-advising-development-direction-advising) or the development-direction entry below.

### PSD-BOUND-ENGAGEMENT — Clarify what advice is needed and who decides

- **Situation:** Someone asks you to solve a problem, but the recipient, subject, horizon or later decision is unclear.
- **Question:** What bounded decision-support result is needed, for whom and for which later use?
- **First useful result or honest blocker:** An engagement question separating the recommending performer, recipient, affected holder and choice owner, or the exact missing condition.
- **Start with:** [PSD.1](#psd-1). A formed question needs no invented dispute.
- **Stop or return:** Stop when the next useful result is clear. Return missing authority, receiving use or subject information. If the chooser already has adequate options and needs only their own decision, use the direct decision guidance.

### PSD-STRUCTURE-INQUIRY — Find the missing inquiry result

- **Situation:** An inquiry has a bounded question, but a model, working Method or account of disagreement cannot yet serve it.
- **Question:** Which missing result prevents a useful account of the situation?
- **First useful result or honest blocker:** An adequate model-use account, a fit-for-purpose inquiry Method, shared and contested claims, or the precise missing premise.
- **Start with:** [PSD.5](#psd-5) for a model's question and limits; [PSD.6](#psd-6) for the way of conducting inquiry; [PSD.7](#psd-7) for participation and contested meaning. Select the live question, not all three.
- **Stop or return:** Reuse an adequate result. Return a missing participant, source or model premise. If the underlying problem formulation or boundary is disputed, recover that question through PSD.3 or PSD.4.

### PSD-COMPARE-ALTERNATIVES — Obtain one decision-useful comparison

- **Situation:** Several possibilities are being discussed, but their value, consequences, uncertainty or conditions of preference remain unclear.
- **Question:** What comparison would change the receiving decision?
- **First useful result or honest blocker:** A bounded comparison, retained alternatives, a reversal condition or the exact missing input.
- **Start with:** Use the first missing result: [PSD.8](#psd-8) for alternatives, [PSD.9](#psd-9) for values, [PSD.10](#psd-10) for uncertainty, [PSD.11](#psd-11) for consequences or [PSD.12](#psd-12) for robustness.
- **Stop or return:** Stop when the receiving use has enough support. Preserve partial comparisons and protected conditions; do not rank an unexamined alternative or replace missing evidence with a convenient score.

### PSD-RETURN-RECOMMENDATION — Return what the evidence supports now

- **Situation:** A recipient needs advice, and useful inputs are available, incomplete or changed.
- **Question:** What can responsibly be returned without taking the recipient's later choice?
- **First useful result or honest blocker:** A supported direction, retained or ranked set, bounded probe, exact request, blocker or abstention, with its basis and limits.
- **Start with:** [PSD.13](#psd-13). Use [PSD.14](#psd-14) when a real observation or changed premise makes follow-up current.
- **Stop or return:** Stop at the first usable return. Delivery proves no consent, choice, implementation or effect. Reopen only dependent claims when a relied-on condition changes.

### PSD-CARD-01 — Turn a contested situation into a usable recommendation

- **Situation:** Participants disagree about the problem, values or evidence, while a separate authority must later decide.
- **Question:** How can the inquiry inform that decision without erasing dissent or claiming authority?
- **First useful result or honest blocker:** A bounded engagement and attributed formulations, or the exact missing recipient, participant, boundary or authority premise.
- **Start with:** [PSD.1](#psd-1); if already bounded, use [PSD.2](#psd-2) or [PSD.3](#psd-3) for the missing participation or formulation result. [APP-PSD-01](#app-psd-01--a-flood-pump-calculation-is-not-the-whole-investment-answer) shows the connected use.
- **Stop or return:** Return a qualified recommendation or scoped blocker through PSD.13. Missing access, consequence or authority evidence goes to its owner. Changed concerns, evidence or receiving conditions reopen affected uses; neither agreement nor a calculation makes the investment choice.

### PSD-CARD-02 — Recommend a development direction without taking the choice

- **Situation:** A distinct adviser must combine unlike specialist results for a person's, organization's or AI arrangement's development.
- **Question:** Which direction, retained set, probe or honest return is supported for this recipient, holder and horizon?
- **First useful result or honest blocker:** A bounded advice question, usable recommendation or exact missing premise.
- **Start with:** [PSD.1](#psd-1), or [PSD.8](#psd-8), [PSD.10](#psd-10), [PSD.12](#psd-12) or [PSD.13](#psd-13) for the first missing result when the engagement is adequate. The [profile](#psd-advising-development-direction-advising) and [APP-PSD-02](#app-psd-02--development-direction-advice-with-unlike-holder-premises) show the bounded connections.
- **Stop or return:** Stop at the supported return; use A.15.9 for a missing specialist result. Unsettled opportunity construction can stop without an adviser. No course, programme, assignment, model change, performed work or effect follows merely from the advice.

## Citation

This framework is published in the [FPF repository](https://github.com/ailev/FPF). If you use it, please cite:

```text
Anatoly Levenchuk, with AI-assisted development and review.
Problem Structuring and Decision Support Principles Framework.
3 September 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title, for example: PSD.13 - Prepare and Return a Decision-Support Recommendation. Retain the release date, and include a permanent link or stored copy when the exact wording matters.

# Preface

A useful answer can be smaller than the question that first brought people together. “Which pump should we buy?” may first need a distinction between nominal capacity and reachable assistance. “What should we develop next?” may first need a worthwhile future contribution rather than a training plan or a model upgrade. Problem Structuring and Decision Support helps people make those differences usable without claiming that one discussion, model or recommendation settles the whole situation.

The framework serves practitioners and assisting agents who help others formulate questions, conduct inquiry, compare alternatives and receive qualified advice. It also supports the maintenance of the Methods and working arrangements that make that help dependable. It is not a universal project lifecycle. The parts group recurring difficulties; the pattern numbers are addresses, not instructions to perform everything in order.

## Start from the missing result

A *pattern* describes a recurring difficulty and a useful way to respond. A *Method* is a reusable way of doing the work; a workshop appointment, diagram or software package is not that way merely because it carries a familiar name. Open the pattern that can change the current answer. If an adequate result already exists, use it within its conditions instead of restarting the inquiry.

Some questions are contested. People can disagree about what is wrong, who bears a consequence, what counts as useful service or which evidence should matter. Preserve differences that change action. Making them explicit does not require every position to have equal evidential support, and a shared sentence does not establish unanimous endorsement.

Other questions are already sufficiently formed. They can enter directly at a missing alternative, specialist premise, comparison or recommendation. A person exploring an opportunity can stop even earlier, without asking another performer for advice.

## Keep unlike contributions distinct

A concern map can preserve what different participants mean. A hydraulic model can estimate a stated physical consequence. A value account can explain which differences matter to the receiving decision. These accounts can inform one another, but none becomes the represented situation or acquires the other's evidential authority.

Likewise, human capability and transfer, organization arrangements, AI evaluation, legal conditions and safety are different questions. This framework helps specify the result needed from each practice and how its absence affects advice. It does not supply those practices' conclusions. A qualified source for one holder or configuration is not a result for another simply because the words sound similar.

Use exact technical distinctions when they change the answer. A proposal is not an obtaining arrangement; a description is not its subject; a score is not a choice; an available Method is not a client's result. Plain language is sufficient when it preserves the distinction and its practical consequence.

## Complete a bounded answer in an open situation

Useful inquiry does not require certainty about everything. It requires knowing what the present answer covers, what it leaves open and what could change it. A partial comparison, a retained pair of alternatives, a narrowly qualified recommendation or an exact request can complete the current question.

Keep protected conditions outside a compensating score when their governing source requires that protection. Show a plausible reversal instead of hiding an arbitrary weight or invented probability. A missing premise should block only the claims that need it; independent content can remain useful.

A recommendation belongs to the advising activity. The recipient's choice, authorization, plan, performed work and observed effect need their own basis. This separation protects the recipient's agency and makes a later change intelligible: the new evidence may narrow advice without rewriting what was previously chosen or done.

## Let practice change without making every case start over

A corrected concern, altered access condition or new model configuration can change the current result. Return to the affected claim and its owner. Obtain and interpret the relevant observation before choosing a response; the mere arrival of a notice is not evidence that the new configuration is safe or effective.

A different problem concerns how inquiry itself is conducted. Use [PSD.15](#psd-15) when the professional repertoire needs a justified change, [PSD.16](#psd-16) when simultaneous inquiry activities interfere, and [PSD.17](#psd-17) when a practice must be continued or changed across practitioners. These are conditional uses, not a required tail on every recommendation.

Contemporary source comparisons belong with the pattern claims they support. Earlier traditions remain valuable where their limits are understood. Neither a fashionable school nor an old success is enough to establish the present Method's fit. What changes in practice is the reader's ability to return a useful answer with visible limits—and to change that answer, or the way of obtaining it, when the actual basis changes.


# Part I — Engagement, Participation, Formulation and Boundary

<a id="psd-1"></a>
## PSD.1 - Bound the Decision-Support Engagement and Authority Boundary

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** a **bounded engagement question** that names the decision-support return, its recipient, the holder or subject, the horizon, the receiving decision or Work, the choice owner and authority boundary, the current scope, the smallest missing value, and an observable condition for reopening.

### PSD.1:0 - Use This When

Use this pattern when someone asks a decision-support performer to “help decide”, “structure the problem”, “recommend what to do”, or “say what should develop next”, but the engagement is not yet bounded well enough to produce a responsible result. The missing value may be the recipient, holder or subject, horizon, receiving decision, receiving Work, choice owner, authority, consequence, or kind of return expected.

Begin with the later decision or use that the decision-support result is meant to inform. Separate the performer who prepares decision support from the person or arrangement that receives it and from the Agent that owns the later choice. Then return one bounded engagement question or the exact value that is still missing.

The practical gain is an affordable start that works both before overt contest and inside a disputed situation. It prevents a workshop, model, score, or recommendation from silently becoming the decision, and it gives later problem-structuring or analytical Work a recoverable subject and stop.

Do not use PSD.1 merely because a chooser must select among an already-qualified live option set; use `C.11` or the applicable domain choice rule directly. Use one holder-specific practice directly when it owns the whole question and no decision-support composition remains. A scientific, legal, ethical, safety, governance, or other specialist question stays with that practice unless its result must be returned into a separately governed decision-support engagement.

### PSD.1:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| decision-support engagement | The bounded situation in which a performer is expected to make a useful result available to a receiving decision or Work. The phrase alone establishes no Method, assignment, authority, WorkPlan, dated Work, service, or product. |
| decision-support performer | The actual or intended person, team, organization, tool-supported arrangement, or other capable System expected to prepare the return. A title, department, model, report, or tool output does not establish this performer or its authority. |
| recipient | The person or arrangement to whom the decision-support return is addressed for a named use. The recipient may or may not own the later choice. |
| holder or subject | The person, organization, System, arrangement, place, policy, capability, or other exact subject whose alternatives or consequences are under consideration. It is not inferred from the recipient's identity. |
| choice owner | The Agent authorized to make, reject, defer, probe, or reroute the later decision. It may coincide with the recipient or performer only when that coincidence and authority are independently supported. |
| receiving decision or Work | The later choice or Work whose next action can change because of the decision-support return. A recommendation is one premise for that use, not the choice or Work itself. |
| bounded engagement question | The smallest decision-support question that makes the intended return, use, participants, scope, authority boundary, and reopen condition usable now. It is a practitioner result, not a universal account schema. |

### PSD.1:1 - Problem frame

Decision-support practice often begins before there is a stable “problem”. One engagement opens with several participant groups arguing about causes and values. Another opens with a calm request for advice whose recipient, subject, horizon, or later authority is still vague. Both can be prematurely forced into a workshop brief, model boundary, criteria table, or option set.

The primary concern here is the boundary of one decision-support engagement for one receiving use. The first useful result is not a complete problem formulation, alternative set, comparison, recommendation, plan, or decision. It is a question and authority boundary precise enough to say what result can be prepared now, what remains outside, and where a missing value must return.

Recognition is deliberately cheap: one unclear decision-bearing value is enough to open the pattern. Consequential use adds direct evidence for identity, assignment, permission, authority, source reliance, safety, law, ethics, and other claims that the engagement actually consumes. The short opening does not lower those assurance burdens.

### PSD.1:2 - Problem

An unbounded engagement can expand into every concern, participant, model, consequence, and possible future. The performer gathers material without knowing which later action it can change. A premature boundary creates the opposite failure: the sponsor's wording becomes the only formulation, the visible recipient is treated as the choice owner, or an analytical result is presented as authorization.

These failures compound. A favourite problem-structuring Method can be selected before the decision-support use is known. A list of stakeholders can stand in for affected Systems and material concerns. A model can hide excluded consequences. A recommendation can absorb holder-specific conclusions or take a choice that belongs elsewhere.

The missing discipline is to bind the engagement to one intended return and separately governed later use while keeping the boundary explicitly provisional. Contestation, plural formulations, affected participants, models, alternatives, values, uncertainty, and follow-up open only when they can change that return.

### PSD.1:3 - Forces

| Force | Tension |
| --- | --- |
| Affordable opening | A practitioner needs a first result quickly, while the most visible request may omit the value that makes any result usable. |
| Useful scope | A boundary is needed to act, while early closure can suppress affected participants, rival formulations, or decisive consequences. |
| Advice and choice | A performer must say something useful, while the later decision and its authority remain separate. |
| Stable use and revisable framing | The engagement needs a current question, while new evidence or participation can legitimately reopen it. |
| Plain roles and exact claims | Recipient, adviser, sponsor, analyst, and decider are useful words, while titles and labels establish no assignment, capability, or authority. |
| Domain ownership | Decision support must combine relevant premises, while holder, legal, ethical, safety, scientific, and governance practices retain their Methods and conclusions. |
| Recognition and assurance | One vague value can justify a cheap clarification, while high-consequence use requires stronger direct evidence and stops. |

### PSD.1:4 - Solution

Bind the engagement to the smallest receiving decision or Work that can use a decision-support return. Name the distinct participant positions, subject, horizon, expected return, current scope, and authority boundary. Return the bounded engagement question when those values are adequate; otherwise return the exact missing value instead of inventing it.

#### PSD.1:4.1 - Name the receiving use before the problem statement

Start with one ordinary sentence:

> Make **[kind of decision-support return]** available to **[recipient]** about **[holder or subject]** for **[receiving decision or Work]** within **[horizon]**; **[choice owner]** retains the later choice.

Ask what action can change because of the return and what consequence makes delay, error, or omission material. If no receiving decision or Work can be named, distinguish exploratory inquiry, research, learning, communication, or another direct use rather than manufacturing a decision-support engagement.

The requested return can initially be a bounded question, participant-and-concern account, plural formulation set, model or Method-selection result, alternative gap, comparison, recommendation, blocker, or abstention. Do not require a recommendation when an earlier honest result is more useful.

#### PSD.1:4.2 - Separate performer, recipient, holder, and choice owner

Name each position separately even when one System may occupy two positions:

1. who is expected to prepare the decision-support return;
2. who will receive it and for what use;
3. which exact holder or subject is under consideration; and
4. who owns the later choice, deferral, probe, or reroute.

State any coincidence explicitly. A manager can receive advice without owning the board's later decision. A team can perform analysis for its own authorized choice, but the analysis Work, recommendation result, and later `ChoiceResult` remain distinct. A tool, document, score, model, department, job title, or meeting creates none of these positions by visibility alone.

Recover assignment, capability, permission, responsibility, conflict, commitment, or authority only to the extent that the current use relies on it. Use their direct patterns for consequential claims. If the required choice owner or authority basis cannot be recovered, return that exact gap.

#### PSD.1:4.3 - Bound the subject, horizon, receiving Work, and consequence

State the holder or subject at the grain whose alternatives or consequences can change. Add the relevant configuration, place, population, operating condition, and interval only when they change the answer. State the receiving decision or Work and the horizon over which the return is expected to remain useful.

Name at least one consequence of getting the boundary wrong. This is a recognition cue, not a complete consequence analysis. When affected Systems, missing participants, duties, interests, or representation can change the engagement, continue with `PSD.2`. When several problem formulations imply materially different actions, continue with `PSD.3`. When included and excluded concerns need a deliberate scope decision, continue with `PSD.4`.

#### PSD.1:4.4 - Choose a provisional boundary and the next truthful branch

Record what is inside the engagement now, what remains outside, and what observation would move that boundary. Do not treat package order or the numbering of patterns as a practitioner sequence. Choose the next branch from the missing result:

| Current situation | Next truthful branch |
| --- | --- |
| participants, concerns, consequences, or representation are incomplete | recover the participation and concern account through `PSD.2` |
| materially different formulations or intervention logics remain hidden | generate plural problem formulations through `PSD.3` |
| the engagement has no usable included/excluded scope and reopen basis | set and reopen the problem boundary through `PSD.4` |
| the engagement is bounded but needs models, a PSM arrangement, or facilitation | begin with the first missing result in `PSD.5`–`PSD.7` |
| the engagement is bounded and the live gap is alternatives, uncertainty, comparison, or recommendation | begin with the first missing result in `PSD.8`–`PSD.13` |
| another practice owns a premise that can reverse the return | inspect or request the smallest bounded result through `A.15.9` |
| an authorized chooser already has an adequate option set and comparison basis | use `C.11` or the direct domain choice rule; stop treating engagement framing as the live question |

Several branches may be live together. Their results can proceed concurrently when their subjects and returns are clear. Co-occurrence does not turn the table into a workflow or make the engagement one Method.

#### PSD.1:4.5 - Record the bounded engagement question or exact stop

Use the smallest account that another participant or later use must recover:

| Result position | Required content |
| --- | --- |
| intended return | The smallest decision-support result sought now, including blocker or abstention as valid branches. |
| recipient and use | Who receives the result, which decision or Work can change, and the horizon. |
| holder or subject | The exact subject, configuration, place, population, or interval needed by the current question. |
| participant positions | Decision-support performer and choice owner, plus only the assignments or authority facts the current use needs. |
| current boundary | Included concerns and consequences, important exclusions, and why that cut is usable now. |
| missing value or next branch | The exact participant, formulation, scope, source, alternative, evidence, authority, or other result still needed. |
| reopen condition | The smallest observable change that can alter the question, scope, authority boundary, or next branch. |

A compact result may be one sentence and one stop:

> For **[recipient]** and **[receiving decision]**, prepare **[return]** about **[subject]** within **[horizon]**; **[choice owner]** retains the later choice. The engagement is blocked until **[exact missing value]** is recovered.

Do not add a role register, stage model, workshop plan, evidence pack, or account field merely because a larger case might need it.

#### PSD.1:4.6 - Reopen locally and preserve the later choice

Name the event that can invalidate the current boundary: a changed recipient, holder, horizon, receiving Work, authority relation, participant or concern, formulation, source, alternative family, evidence condition, consequence, or later decision. Reopen only the affected position and its dependent results.

A returned recommendation may inform the later decision, and follow-up may observe that later decision, but neither retroactively turns the decision-support performer into the choice owner. If the later choice changes the problem structure, use `PSD.14` to determine which follow-up or reframing question is current.

#### PSD.1:4.7 - What changes in practice

The practitioner stops accepting “the problem” as a sufficient start. Within the first exchange, they can name the return, recipient, subject, horizon, later use, and choice owner—or return the exact missing value. Method selection, modeling, participation, alternative generation, and recommendation Work begin from that result instead of being used to discover silently what the engagement was supposed to accomplish.

### PSD.1:5 - Archetypal Grounding

#### PSD.1:5.1 - Contested flood-pump decision

A municipal resilience office asks a decision-support team to “solve the pump problem” before the next flood season. Operations staff prefer another permanent pump; finance questions capital exposure; residents contest which districts and harms count; and the emergency investment board owns the later funding and deployment decision.

The team does not begin with a pump model or consensus workshop. It first returns this bounded engagement question:

> For the municipal resilience office, prepare a recommendation for the emergency investment board's pre-season funding and deployment decision about the district flood-pumping arrangement over the next flood season. Compare permanent, mobile, staged, and no-new-purchase branches only after affected districts, operating conditions, safety limits, and material dissent are recoverable; the board retains the later choice.

The boundary is useful but incomplete. `PSD.2` is next because affected residents, operating groups, concerns, and consequence-bearing Systems can change the engagement. `PSD.3` is also live because “insufficient capacity”, “unequal protection”, “maintenance fragility”, and “unsafe deployment” imply different interventions. The team stops before model or option selection if the board's authority, the decision horizon, or an affected district remains unrecoverable.

#### PSD.1:5.2 - Development-direction advice without taking the choice

An engineering executive asks an advisory team, “What should we develop next for AI-assisted incident response?” The phrase does not yet say whether the holder is a person, team, organization capability, model, agent arrangement, or operating platform; whether the recipient or an investment committee owns the choice; or whether the horizon is the next release or the next two quarters.

After one clarification, the holder is the organization's AI-assisted incident-response arrangement, the executive is the recipient, the investment committee owns the later portfolio choice, the horizon is two quarters, and the requested return is a source-qualified development-direction recommendation. The first result is:

> For the executive's two-quarter investment proposal, prepare a bounded recommendation about development directions for the AI-assisted incident-response arrangement; the investment committee retains the later choice. Return the exact missing human-capability, organization, operations, model-evaluation, safety, or authority result before using it as a premise.

No contest is assumed. With the engagement bounded, the practitioner may inspect external results through `A.15.9` and begin with the first missing result among `PSD.8`–`PSD.13`. PSD.1 authorizes no training programme, organization change, model modification, purchase, WorkPlan, or choice.

#### PSD.1:5.3 - Cheap non-use when the choice is already local

A procurement board is the authorized chooser, has three qualified pump options, a current comparison basis, and no unresolved participant, formulation, scope, authority, or outside-practice premise. The live question is which option to select. Use `C.11` or the board's direct choice rule. Repeating PSD.1 would add no useful boundary.

### PSD.1:6 - Bias-Annotation

**Scope:** decision-support engagements for a named receiving decision or Work. **Lenses:** **Gov** concerns participation and decision authority; **Arch**, the engagement boundary and dependent contributions; **Onto/Epist**, keeping the subject, claims, recommendation, and later choice distinct; **Prag**, a useful return at proportionate effort; **Did**, plain entry cues that preserve the distinction between cheap recognition and consequential assurance.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-language bias | The sponsor's first wording becomes the problem and scope. | Name the receiving use, affected consequence, exclusions, and reopen condition before accepting the formulation. |
| authority-by-visibility bias | The meeting chair, report author, model owner, or recipient is treated as the choice owner. | Recover the later decision and its authority basis separately. |
| Method-first bias | A familiar PSM, workshop, model, or scoring scheme determines the engagement boundary. | Return the bounded question first; select Methods only for the result that is actually missing. |
| stakeholder-list bias | A visible list is treated as complete participation and concern recovery. | Continue with `PSD.2` when affected Systems, representation, duties, interests, or dissent can change the return. |
| recommendation-as-choice bias | A confident recommendation, rank, or tool output is presented as authorization. | State the recipient, choice owner, next use, and stop at the recommendation boundary. |
| exhaustive-framing bias | Every possibly related concern is admitted before any useful result can be returned. | Choose the smallest current boundary and one observable reopen condition. |

### PSD.1:7 - Conformance Checklist

- [ ] The opening names a recognizable receiving decision or Work and the smallest useful decision-support return.
- [ ] Decision-support performer, recipient, holder or subject, and choice owner are separately recoverable.
- [ ] Any coincidence among those positions is explicit and does not transfer authority by wording alone.
- [ ] The holder or subject, horizon, relevant configuration, and at least one consequence of a wrong boundary are visible at the grain needed by the current use.
- [ ] The current included and excluded scope and one observable reopen condition are stated.
- [ ] Contestation opens `PSD.2`–`PSD.4` only when participants, formulations, or scope can change the return; it is not a membership requirement for PSD.1.
- [ ] A bounded direct-advice case can proceed to the first missing `PSD.8`–`PSD.13` or external-result branch without a compulsory problem-structuring sequence.
- [ ] Missing authority, subject, horizon, source, or receiving use produces an exact return rather than an invented value.
- [ ] The result does not claim that a recommendation is the later choice, that planned Work occurred, or that an effect obtained.
- [ ] The body supports both a contested-situation entry and development-direction advising without giving either entry a different meaning of engagement or authority.

### PSD.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “First agree what the problem is.” | Preserve materially different formulations and ask which receiving decision each would change. |
| “The client is the decision maker.” | Separate recipient, holder, choice owner, and authority basis; name any supported coincidence. |
| “Run the workshop and the scope will emerge.” | State the intended return and provisional boundary before choosing the workshop Method. |
| “The model says option A, so that is the decision.” | Keep model result, recommendation, authority, and later `ChoiceResult` separate. |
| “We need every stakeholder before we can start.” | Return a bounded current question and use `PSD.2` to expose which missing participant or concern can change it. |
| “This is only advice, so authority does not matter.” | State who may prepare, receive, rely on, and choose whenever those differences change use or consequences. |
| “Use PSD.1 as stage one of every engagement.” | Bypass it when the receiving question and authority boundary are already adequate and another result is the live gap. |

### PSD.1:9 - Consequences

A decision-support engagement gains a usable first result before it gains heavy apparatus. Practitioners can stop on one missing value, route contestation to participation and plural-formulation Work, or proceed directly to alternatives and recommendation when the question is already bounded. Recommendations become easier to inspect because their recipient, subject, horizon, authority boundary, and next use were not reconstructed after the analysis.

The cost is explicit clarification at the start and occasional reopening later. Some requests will stop before analysis because no receiving decision, choice owner, horizon, or subject can be supported. Others will widen after affected participants or rival formulations become visible. Those are useful returns, not failed stages.

### PSD.1:10 - Rationale

The engagement boundary is the smallest professional decision-support result that can coordinate problem structuring and later analysis without pretending that either has already occurred. Starting from a fixed problem statement is too narrow for contested or revisable framing. Starting from an unlimited situation is too broad to guide a return. Starting from a Method confuses the means with the receiving use.

Generic FPF patterns already govern outside-practice results, evidence, permission, agency, and choice. PSD.1 does not reproduce them. It contributes the field-specific opening that connects a separately governed later decision to a provisional problem-structuring and decision-support boundary, and it tells the practitioner which exact downstream question is now live.

### PSD.1:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a practitioner open an ill-structured or contested decision-support situation? | The best-known line is to bind inquiry to a named receiving use while keeping framing plural, contextual, and revisable before committing to one PSM, model, or formulation. | A fixed sponsor brief or Method-first workshop is the serious default; an unbounded “include everything” inquiry is the opposite default. | Both defaults hide the decision-support return: one naturalizes the first frame, the other cannot stop. **Adapt:** `PSD.1:4.1`–`4.4`, the flood-pump case, and the first seven checklist rows require a receiving use, provisional boundary, plural-formulation return, and local reopen before Method choice. | Smith and Shaw's [2019 PSM review](https://doi.org/10.1016/j.ejor.2018.05.003) is a best-known-line candidate for the continuing PSM branch and its differing characteristics; Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) is an application comparator. Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25), Litster, Cardoso, and Hurst's [2024 systems-mapping study](https://doi.org/10.1017/S089006042400012X), and Nickel, Hurst, and Duimering's [2024 contextual trade-off study](https://doi.org/10.1017/dsj.2024.34) support explicit candidate framing, contextual comparison, and revision. The reviews are non-exhaustive; the studies establish neither one framing ontology, universal Method, shared frame, prevalence, nor superiority. | Reopen if comparative practice shows a lower-effort opening that preserves the same receiving-use, plurality, authority, stop, and revision value, or if a source changes the conditions under which framing must be reopened. |
| How should decision-support advice remain useful without becoming the later choice? | The best-known current FPF line is result-first and authority-bounded: name the receiving decision, reuse or request only the outside-practice result it needs, return the recommendation as a premise, and let the authorized chooser produce the separate `ChoiceResult`. | Expert-report, approval, score, or model-output language treated as the decision is the serious default. | The default transfers authority by format and hides blockers. **Adopt:** `PSD.1:4.1`, `4.2`, `4.5`, the development-direction case, and the authority checks keep performer, recipient, holder, outside-result owner, and choice owner distinct. | Current `A.15.9` supplies the smallest bounded-result return and supplier/receiver authority split; current `C.11` supplies choice over an already-available option set. Neither pattern bounds a professional problem-structuring and decision-support engagement or selects its next field-specific branch. | Reopen if direct choice or outside-result guidance gains the complete engagement-boundary move at equal or lower effort, or if practitioner use shows that the current separation prevents rather than improves a necessary authorized combined role. |

### PSD.1:12 - Relations

- `PSD.2` receives a bounded receiving inquiry when participants, concerns, affected Systems, duties, interests, representation, or dissent can change the return.
- `PSD.3` receives the case when materially different problem formulations imply different boundaries, evidence, values, or interventions. `PSD.4` receives the deliberate included/excluded scope and reopen decision.
- `PSD.5`–`PSD.7` receive model, PSM-selection, and facilitation questions only when those results are current. `PSD.8`–`PSD.12` receive alternatives and comparison questions after the engagement is bounded.
- `PSD.13` prepares and returns a recommendation without authorizing the later decision. `PSD.14` relates changed premises and later observations to continuation, adjustment, evidence refresh, or reframing.
- `A.15.9` supplies the inspect-reuse-or-request boundary for one outside-practice result. `A.10` governs any evidence, source, currentness, or bounded reliance claim actually used.
- `C.11` governs the later choice over an already-available option set. `A.13`, assignment, capability, permission, responsibility, and authority patterns govern those actual claims when the engagement relies on them.
- Both `PSD-CARD-01` and `PSD-CARD-02` begin from this same engagement and authority meaning. The entries add unlike extended-use examples; they neither redefine PSD.1 nor impose a traversal order.

### PSD.1:End


<a id="psd-2"></a>
## PSD.2 - Recover Participants, Concerns, and Affected Systems

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** an **explicit participation and concern account** for one bounded receiving inquiry: who is participating or represented, which affected Systems and possible consequences remain material, which concerns, duties, interests, and dissent are recoverable, what is missing or uncertain, and what would reopen the account.

### PSD.2:0 - Use This When

Use this pattern when a bounded decision-support inquiry may be shaped mainly by its loudest, most available, or formally powerful participants, while quieter participants, represented people, consequence-bearing Systems, or material concerns can still change the formulation or return.

Begin from the bounded engagement question in `PSD.1` when it is current. Recover possible consequence bearers through `A.1.CSD`, then recover the participation conditions and concerns needed by this particular inquiry. Return an explicit account rather than treating attendance, a stakeholder list, or one facilitated conversation as proof of completeness.

The practical gain is a visible basis for whose situations and concerns can change the inquiry without requiring universal inclusion or pretending that participation transfers decision authority. Do not use PSD.2 for a generic contact list, public-relations audience map, or organization chart. Use `A.1.CSD` directly when the only live question is which Systems may undergo a material change. Use the direct governance, legal, ethical, safety, representation, conflict, or authority practice when that practice owns the whole question.

### PSD.2:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| participant | A person or arrangement whose contribution is sought or used in the bounded inquiry. Participation alone proves neither System status, representativeness, agreement, capability, nor authority. |
| affected System | An actual System or intended referent that may undergo a relevant change through a supported direct relation or a stated modal path. Use `A.1.CSD` for this discovery and keep actual and possible relations distinct. |
| concern | A source-attributed matter that a participant, represented person, duty holder, interest holder, or affected-System account makes material to the receiving use. A recorded concern is not thereby true, decisive, or jointly held. |
| representation | A supported basis on which one participant speaks, reports, advocates, or acts for another person or constituency. Presence, title, confidence, or similarity does not establish it. |
| participation condition | An access, timing, language, safety, capability, format, dependency, or other condition that changes whether a contribution can be made or relied upon. |
| participation and concern account | The smallest recoverable account of current and missing participation, affected Systems, concerns, duties, interests, dissent, evidence, uncertainty, and next use for one bounded inquiry. |

### PSD.2:1 - Problem frame

Contested situations rarely present a neutral list of stakeholders. Sponsors, operators, specialists, residents, customers, regulators, future users, and consequence bearers enter through different channels and with unequal time, language, safety, information, and formal power. Some affected Systems cannot speak; some people speak without a supported representative relation; some participants hold duties or authority without bearing the largest consequences.

The primary concern here is not universal participation. It is whether the current inquiry has enough explicit participation and concern recovery to avoid a materially misleading formulation, model, alternative set, comparison, or recommendation. Recognition can begin with one plausible missing bearer or one silenced concern. Consequential claims about harm, duty, representation, evidence, law, safety, or authority still require their direct assurance.

### PSD.2:2 - Problem

A stakeholder list collapses several different questions: who attends, who contributes evidence, who may be affected, who holds a duty or interest, who represents whom, and who decides. The most visible contributors then define the concern set. Non-attendance is read as indifference; a representative's statement is generalized beyond its basis; a possible consequence is reported as an observed one; or a facilitator's synthesis becomes false consensus.

The opposite failure is exhaustive participation. Work stops until every possibly related person is present, even when the bounded receiving use needs only the smallest material account and an honest missing-participant stop. PSD.2 must expose consequential absence without claiming that every inquiry is a deliberative assembly.

### PSD.2:3 - Forces

| Force | Tension |
| --- | --- |
| Practical inclusion | Missing voices can reverse the inquiry, while universal recruitment is impossible. |
| Consequence discovery | Affected Systems matter even when they cannot participate, while possible impact must not be reported as fact. |
| Participation and authority | Contributions need access and protection, while neither attendance nor facilitation transfers the later choice. |
| Concern fidelity | Duties, interests, experiences, and dissent must remain attributable, while a usable account cannot become a transcript archive. |
| Representation | Some people must rely on representatives, while titles and self-selection do not prove the relation. |
| Recognition and assurance | Cheap cues should expose a gap, while consequential claims need direct sources and specialist checks. |

### PSD.2:4 - Solution

Recover participants and concerns relative to one bounded inquiry and receiving use. Start from possible consequence bearers, not only invitees. Keep participation, affected-System status, concern attribution, representation, and decision authority as separate claims. Return the smallest account that can change the next problem-structuring or decision-support result.

#### PSD.2:4.1 - Bind the account to one inquiry

Name the `PSD.1` bounded engagement question, or state the same subject, recipient, receiving decision or Work, horizon, and authority boundary directly. Do not import a participation account from another decision merely because the organization, place, or topic is similar. If the engagement identity or receiving use is missing, return that gap to `PSD.1`.

Ask: whose situation, contribution, duty, interest, or possible change could make the current return materially different? This question bounds discovery without assuming that every discovered bearer must attend.

#### PSD.2:4.2 - Discover affected Systems before equating them with participants

Use the smallest `A.1.CSD` pass that can challenge the current boundary. Name the focus, configuration, scope, horizon, receiver, examined possibilities, actual direct relations, modal paths, bearers, possible changed characteristics, evidence, uncertainty, and reopen trigger at the grain the inquiry needs.

An affected System may be a participant, be represented by a participant, or have no feasible participation channel. Participation can reveal a bearer or path, but it does not prove System construction, a relation occurrence, a consequence, or authority. Use the direct relation pattern for an obtaining claim. Open `A.6.REL` only when later work must distinguish this occurrence from another occurrence of the same relation kind, including another episode with the same participants; a readable current relation assertion is otherwise enough.

#### PSD.2:4.3 - Recover participation positions and conditions

For each materially distinct contribution, record who contributes, the basis of involvement, what knowledge or experience is being offered, the participation channel, and any condition that limits access or reliance. Name missing or unsafe participation explicitly.

Recover a representative relation only when the current use relies on it. State whom the participant represents, for what question, under which basis, and with what limit. Keep self-report, specialist evidence, advocacy, delegated representation, duty, interest, sponsorship, facilitation, and choice authority distinct.

#### PSD.2:4.4 - Attribute concerns, duties, interests, and dissent

Record each material concern in ordinary language with its holder or source and the consequence or receiving-use difference it could make. Distinguish:

- reported experience from externally supported evidence;
- duty from preference or interest;
- individual concern from a represented constituency claim;
- disagreement from an unresolved factual question; and
- absence of evidence from evidence of absence.

Keep minority and unresolved positions visible. Facilitation may make contributions usable; it does not establish consensus, truth, priority, permission, or authority.

#### PSD.2:4.5 - Return the smallest explicit account

| Result position | Required content |
| --- | --- |
| bounded inquiry | Subject, receiving use, horizon, recipient, and retained choice owner. |
| current participation | Participants, contribution bases, channels, and material participation conditions. |
| consequence bearers | Actual Systems or intended referents, supported relations or modal paths, possible changes, evidence, and uncertainty. |
| concerns and positions | Attributed concerns, duties, interests, agreements, dissent, and unresolved questions. |
| representation | Any relied-upon representative relation and its scope; otherwise the explicit gap. |
| material absences | Missing participants, bearers, concerns, channels, or assurance that can change the inquiry. |
| next use and reopen | Which formulation, scope, facilitation, value, or later result consumes the account, and what observation reopens it. |

Stop when the account is adequate for the named next use, not when every possible participant has been contacted. If a missing participant or concern can reverse that use, return the gap, narrow the claim, request the direct result, or abstain.

#### PSD.2:4.6 - Use the account without making it decide

Pass materially different concerns into `PSD.3`, boundary challenges into `PSD.4`, participation conditions into `PSD.7`, value inputs into `PSD.9`, and participant-facing inquiry results into `PSD.16`. Inclusion in the account does not settle a formulation, priority, model, alternative, recommendation, or later choice.

Reopen locally when a new bearer, consequence path, participant, concern, duty, interest, representation basis, dissent, participation condition, receiving use, horizon, or authority relation can change a dependent result.

#### PSD.2:4.7 - What changes in practice

The practitioner stops using an invitation list as the social boundary of the problem. They can show who and what may be affected, who contributed under which conditions, whose concerns are attributed rather than generalized, what remains missing, and exactly which next result could change.

### PSD.2:5 - Archetypal Grounding

#### PSD.2:5.1 - Flood-pump participation and concern account

For the emergency investment board's pre-season pump decision, the team begins with the `PSD.1` engagement. Operations and finance staff are available, but district residents, emergency responders, maintenance contractors, downstream ecology staff, and people with limited mobility may bear different consequences.

An `A.1.CSD` pass distinguishes observed basement flooding and pump downtime from possible displacement, access failure, downstream transfer, and ecological change. Resident contributions are attributed by district and channel; one neighborhood association is not assumed to represent every resident. Emergency responders hold operational knowledge and duties but do not thereby own the investment choice. A no-new-purchase concern remains visible beside capacity, equity, maintenance, safety, and environmental concerns.

The returned account names inaccessible evening meetings and missing mobility-service evidence as participation gaps. It is adequate to open `PSD.3`, because the recovered concerns support materially different formulations. It does not declare consensus or recommend a pump.

#### PSD.2:5.2 - Affected System without a speaking participant

A service redesign may change response time for a machine-supported monitoring arrangement and for patients who cannot participate directly. The arrangement and patients can enter the affected-System account through supported paths even when no direct participant is available. A clinician, advocate, or family member contributes only under the stated evidence or representation basis. The practitioner returns the unresolved representation or consequence gap rather than inventing a voice.

#### PSD.2:5.3 - Cheap non-use

A current, low-consequence internal choice has one authorized team, one directly affected workcell, an already-supported consequence account, no representation question, and no material dissent. The live question is comparison among three qualified settings. Repeating PSD.2 adds no value; use the comparison or choice pattern directly.

### PSD.2:6 - Bias-Annotation

**Scope:** participation and concern recovery for one bounded decision-support inquiry. **Lenses:** **Gov** keeps contribution, representation, duty, and choice authority distinct; **Arch** tracks which participants and concerns can change dependent results; **Onto/Epist** separates Systems, reports, possible paths, and supported relations; **Prag** stops at a sufficient account; **Did** supplies plain recognition cues and an explicit assurance boundary.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| visibility bias | Available or powerful speakers define the concern set. | Start from possible consequence bearers and record material absences. |
| attendance-as-representation bias | Presence or title is treated as authority to speak for others. | State the representation basis, scope, and limit separately. |
| participation-as-proof bias | A workshop report is treated as proof of Systemhood, consequence, or consensus. | Keep participation, relation, evidence, and agreement claims distinct. |
| stakeholder-exhaustion bias | Work waits for universal participation. | Stop at adequacy for the named use and return exact gaps. |
| harmony bias | Facilitation erases minority or unresolved positions. | Preserve attributed dissent and its consequence for the next result. |
| human-only bias | Non-speaking or non-human consequence bearers disappear. | Use `A.1.CSD` to recover affected Systems and possible changes. |

### PSD.2:7 - Conformance Checklist

- [ ] The account is bound to one receiving inquiry, subject, horizon, and authority boundary.
- [ ] Participants, affected Systems, represented people, duty or interest holders, and choice owner are not collapsed.
- [ ] Actual relations, modal paths, observed changes, and possible consequences remain distinguishable.
- [ ] Material concerns are attributed; recording them does not imply truth, priority, consensus, or authority.
- [ ] Any relied-upon representation and participation condition is supported and scoped.
- [ ] Missing participants, bearers, concerns, or assurance produce a visible gap, narrowed claim, request, blocker, or abstention.
- [ ] The stopping rule is adequacy for a named next use rather than exhaustive recruitment.
- [ ] Recognition is cheap, while legal, ethical, safety, harm, duty, representation, and authority claims retain their direct assurance.
- [ ] The result can feed plural formulation, boundary, facilitation, value, or inquiry Work without deciding any of them.

### PSD.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The stakeholder register is complete.” | Ask which plausible consequence bearer or participation condition could change the receiving use. |
| “Everyone agreed in the workshop.” | Preserve who expressed what, under which channel and limits; establish consensus only through its direct basis. |
| “The community representative speaks for residents.” | Recover the constituency, mandate, scope, and dissent or return the representation gap. |
| “Affected means invited.” | Discover consequence bearers independently of participation. |
| “Every concern becomes a criterion.” | Pass concerns to the formulation and value patterns; do not convert them silently. |
| “No one mentioned it, so it is irrelevant.” | Distinguish missing evidence or access from supported non-materiality. |

### PSD.2:9 - Consequences

Problem formulations and later recommendations gain a recoverable social and consequence basis. Quiet, represented, missing, and non-speaking bearers remain visible without requiring impossible universal participation. The cost is explicit attribution and occasional stopping when representation, access, or consequence evidence is inadequate.

### PSD.2:10 - Rationale

Problem structuring needs more than generic affected-System discovery and more than a meeting roster. `A.1.CSD` supplies the shared discipline for finding consequence bearers and keeping actual and modal paths honest. PSD.2 adds the field-specific participation move: recover contribution conditions, concerns, duties, interests, representation, and dissent for a bounded receiving inquiry, then pass rather than decide them.

### PSD.2:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should participation be recovered in an ill-structured decision-support situation? | The continuing PSM branch, including facilitated modeling and multi-method arrangements documented for ill-structured situations. | A sponsor-built stakeholder list or open workshop is the serious default; universal recruitment is the opposite default. | A sponsor's list can hide consequential absence, while universal recruitment supplies no usable stop. **Adapt:** `PSD.2:4.1`–`4.5` returns a use-bounded participation and concern account whose omissions and dissent remain visible. | Smith and Shaw's [2019 PSM review](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) support the continuing branch, differing Methods, and documented facilitated or multi-method use. They do not establish representativeness, universal facilitation sufficiency, or comparative superiority. PSD's architecture assigns participation and concern recovery to this pattern; attribution, representation limits, and missing-participant stops are constraints on that account. Current `A.1.CSD` separately supplies consequence-bearer discovery. The resulting combined PSD rule is an adaptation, not an externally demonstrated best participation protocol. | Reopen if newer comparative evidence changes the conditions under which facilitated participation is adequate, the direct FPF contribution changes, or a material bearer or participation condition is discovered. |
| How should affected Systems enter without turning participation into proof? | Use current `A.1.CSD` to recover actual Systems or intended referents, direct relations or modal paths, possible changed characteristics, evidence, uncertainty, and receiver connection; then use PSD.2 only for the participation-specific account. | Attendance, complaint volume, or generic impact language is the serious default. | It confuses reports, bearers, paths, changes, and authority. **Adopt:** `PSD.2:4.2` and the non-speaking-bearer case keep those claims separate. | Current `A.1.CSD` is the direct FPF source for affected-System consequence discovery. Each obtaining claim remains with its direct relation pattern; `A.6.REL` adds occurrence identity only when later use must distinguish occurrences of the same relation kind. These contributions do not recruit participants, establish representation, facilitate inquiry, or rank concerns. Domain safety, legal, ethical, and scientific practices retain their own Methods and thresholds. | Reopen if the direct patterns acquire the full participation-and-concern move at equal or lower effort, or if evidence changes a relied-upon bearer, path, or consequence. |

### PSD.2:12 - Relations

- `PSD.1` supplies the bounded subject, receiving decision or Work, horizon, recipient, and authority boundary; absent or stale values return there rather than being inferred.
- `A.1.CSD` supplies affected-System consequence discovery. The relevant direct relation pattern governs each obtaining claim; `A.6.REL` applies only when the receiving use must distinguish occurrences of the same relation kind.
- `PSD.3` receives materially different participants and concerns as formulation input without treating inclusion as settlement. `PSD.4` receives boundary challenges.
- `PSD.7` receives participation conditions for facilitation; `PSD.9` receives attributed value inputs; `PSD.16` receives participants and concerns needed by the inquiry result.
- Direct governance, conflict, representation, legal, ethical, safety, evidence, assignment, and authority patterns govern those claims. PSD.2 neither replaces them nor authorizes the later choice.

### PSD.2:End


<a id="psd-3"></a>
## PSD.3 - Generate Plural Problem Formulations

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** a **plural formulation set** for one bounded receiving inquiry: materially different accounts of what warrants intervention, each with its subject, boundary, affected participants or Systems, value tension, evidence need, intervention logic, assumptions, and consequence for the receiving use.

### PSD.3:0 - Use This When

Use this pattern when one wording of “the problem” is becoming naturalized even though materially different accounts would change what is included, what evidence matters, which interventions are plausible, whose values are exposed, or what the recipient should do next.

Begin from the bounded engagement question in `PSD.1`. Use the `PSD.2` participation and concern account when affected participants, Systems, duties, interests, or dissent are material. Generate formulations that differ in decision-bearing structure, not merely vocabulary, and return them without selecting a winner.

The practical gain is an inspectable choice of frames before modeling, option generation, or comparison locks in the sponsor's first account. Do not use PSD.3 for a thesaurus exercise, generic creativity session, alternative generation for an already-stable problem (`PSD.8`), or archive/front stewardship (`C.18`). If one formulation is already adequate and no credible rival could change the receiving use, proceed to the actual missing result.

### PSD.3:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| problem formulation | A bounded, source-qualified account of what condition or relation warrants inquiry or intervention for a named receiving use. It proposes a subject, boundary, concern, evidence need, and intervention logic; it is not the situation itself. |
| plural formulation set | Two or more materially different formulations retained together because each can change a downstream boundary, model, alternative family, value treatment, evidence request, or recommendation. |
| material difference | A difference that changes at least one decision-support move. Synonyms, rhetorical emphasis, or unexplained labels are not material plurality. |
| intervention logic | The connection a formulation proposes between the condition treated as problematic and the families of action, inquiry, adaptation, or restraint worth considering. It is a hypothesis, not proof of causation or effectiveness. |
| framing commitment | A supported or provisional inclusion, exclusion, assumption, value emphasis, or causal hypothesis built into one formulation. |

### PSD.3:1 - Problem frame

Ill-structured situations do not arrive with one neutral problem object waiting to be described. “Insufficient capacity”, “unequal protection”, “maintenance fragility”, and “unsafe deployment” can concern the same pumping arrangement while selecting different bearers, boundaries, evidence, interventions, and consequences. The formulations may conflict, overlap, or remain jointly useful.

The primary concern is to make those decision-bearing differences recoverable before one model or Method absorbs them. Recognition is cheap: one credible rival intervention logic is enough to test plurality. Assurance remains direct for every factual, causal, evaluative, legal, ethical, safety, authority, or source claim used within a formulation.

### PSD.3:2 - Problem

The sponsor's first sentence often becomes the model title, data request, option space, and final recommendation. Its assumptions disappear because they are encoded as scope. A second failure produces many “perspectives” that differ only in wording and therefore add ceremony without changing any downstream work. A third treats plurality as permanent indecision and refuses to bound the inquiry.

The needed discipline is neither immediate convergence nor unlimited reframing. It is to construct a small set of materially different formulations, expose what each makes visible and suppresses, and stop when additional formulations no longer change the current receiving use.

### PSD.3:3 - Forces

| Force | Tension |
| --- | --- |
| Plurality | Rival formulations can prevent premature closure, while decorative variety wastes effort. |
| Usability | Each formulation must guide a next move, while early precision can pretend that contested claims are settled. |
| Participant fidelity | Concerns should shape formulations, while participation does not prove the formulation. |
| Evidence | A formulation reveals what evidence matters, while it must not smuggle unsupported causes or effects into the case. |
| Exploration and stopping | New frames can reveal alternatives, while an unbounded set cannot support a decision. |
| Authority | A recipient may compare formulations, while neither a facilitator nor the set itself owns the later choice. |

### PSD.3:4 - Solution

Generate a bounded set of problem formulations whose differences are visible in their downstream consequences. Bind every formulation to the same receiving inquiry unless an identity change is explicitly returned to `PSD.1`. Preserve sources, assumptions, uncertainty, and conflicts; then hand the set to boundary, modeling, alternative, and inquiry patterns without declaring a chosen problem.

#### PSD.3:4.1 - Fix the receiving inquiry, not the problem answer

State the subject, recipient, receiving decision or Work, horizon, and retained choice owner from `PSD.1`. Import only those `PSD.2` participants, affected Systems, concerns, duties, interests, and dissent that can change this inquiry. If the subject or receiving use differs, create or recover the other engagement rather than merging formulations across identities.

Write the current formulation in one sentence. Mark its source, factual support, assumptions, and important exclusions. This makes the default frame inspectable rather than privileged.

#### PSD.3:4.2 - Generate structural contrasts

Seek contrasts along the smallest productive set of questions:

- What condition or relation is treated as problematic, for whom or what?
- Which bearer, place, configuration, horizon, or consequence is central?
- Which value, duty, interest, or risk makes intervention worth considering?
- Which mechanism or dependency is hypothesized, and what evidence could challenge it?
- Which action families become plausible, and which disappear?
- Who can prepare, receive, authorize, or implement a response?

Do not require one formulation per question. Combine contrasts into coherent candidate formulations. If two formulations imply the same boundary, evidence, action family, and receiving-use consequence, merge them or state that their difference is rhetorical.

#### PSD.3:4.3 - Give every formulation a usable face

For each retained formulation, record:

| Position | Required content |
| --- | --- |
| formulation | One ordinary-language account of what warrants inquiry or intervention. |
| subject and bearers | Exact subject, affected participants or Systems, configuration, place, and horizon needed by the claim. |
| boundary and exclusions | What the formulation includes, what it suppresses or defers, and why. |
| value tension | Attributed concern, duty, interest, risk, or desired change that makes the formulation material. |
| evidence need | Current support, uncertainty, contrary evidence, and the smallest question that could reverse or narrow it. |
| intervention logic | Action, inquiry, adaptation, or restraint families made plausible, without claiming effectiveness. |
| receiving-use consequence | Which model, alternative, comparison, scope, recommendation, or decision-support return would change. |

Where a durable formulation is used as a claim-bearing episteme, preserve its source and identity through the direct episteme pattern. Ordinary working sentences need no new root kind.

#### PSD.3:4.4 - Test material plurality without ranking

Compare each pair only far enough to ask whether the difference changes a downstream move. Preserve incompatibility when one formulation requires evidence, values, boundaries, or interventions that another excludes. Record overlap when formulations can be investigated together.

Do not score, rank, vote, synthesize, or select unless another pattern and authority govern that result. `C.17` may characterize novelty, diversity, or use of an already-generated formulation set when that characterization is material. `C.18` applies only when the project must govern generation records, descriptors, archives, fronts, telemetry, or retained exploration value. Neither pattern supplies the PSM-specific construction of problem formulations.

#### PSD.3:4.5 - Stop and return the plural formulation set

Stop when every retained formulation changes at least one named downstream move and another credible formulation would not change the current receiving use enough to justify its cost. There is no universal target count. A claim of plurality requires at least two materially different formulations; a case with only one adequate formulation should not manufacture a set.

Return the formulations, their contrasts, shared and disputed premises, evidence gaps, dependent next results, and reopen conditions. If a missing participant, concern, fact, source, or authority relation prevents a responsible formulation, return the exact gap, narrow the claim, request the bounded result, or abstain.

#### PSD.3:4.6 - Pass plurality forward without creating a workflow

Pass the set to `PSD.4` when included and excluded scope must be chosen, to `PSD.5` when different models are needed, to `PSD.8` when formulations imply different alternative families, and to `PSD.16` when the inquiry result must retain plural formulations. These branches may be concurrent. Pattern numbering is not a compulsory stage sequence.

Reopen locally when a new participant, concern, affected System, evidence result, value tension, intervention family, horizon, receiving use, or authority fact creates a materially different formulation or defeats one already retained.

#### PSD.3:4.7 - What changes in practice

The practitioner stops asking participants to agree on one problem sentence before useful work begins. They can show a small set of genuinely different formulations, the evidence and actions each foregrounds, and the exact next result that plurality changes.

### PSD.3:5 - Archetypal Grounding

#### PSD.3:5.1 - Four formulations of the flood-pump situation

For the board's pre-season decision, the `PSD.2` account supports four material formulations:

1. **Capacity shortage:** peak inflow can exceed available pumping capacity; flow, reliability, and deployment evidence matter; permanent or mobile capacity becomes salient.
2. **Unequal protection:** current arrangements shift flood exposure toward particular districts and mobility-constrained residents; distribution, access, and representation evidence matter; allocation and protection rules become salient.
3. **Maintenance fragility:** failures arise from maintenance, spares, staffing, and coordination dependencies rather than nominal pump count; readiness, contracting, and staged maintenance alternatives become salient.
4. **Unsafe deployment:** emergency placement and operation can create worker, resident, traffic, or downstream risks; safe operating envelopes and restraint branches become salient.

These are not synonyms. They imply different scope, evidence, model, alternative, and value work. The team keeps overlaps and conflicts visible and sends the set to `PSD.4`; it does not vote for “the real problem” or infer that any intervention is effective.

#### PSD.3:5.2 - Development-direction advice

For an AI-assisted incident-response arrangement, “model accuracy is inadequate”, “operator coordination is fragile”, and “authority escalation is unclear” imply different holders, evidence, intervention families, and safety questions. PSD.3 retains all three only if each can change the two-quarter development recommendation. Generic slogans such as “improve AI capability” and “make the system better” fail the material-difference test.

#### PSD.3:5.3 - Cheap non-use

A repair team has a verified broken seal, one affected assembly, one authorized repair decision, and no rival account that changes evidence or action. The live question is which qualified replacement to use. Generating plural problem formulations would add ceremony; proceed directly to comparison or choice.

### PSD.3:6 - Bias-Annotation

**Scope:** plural problem formulation for one bounded decision-support inquiry. **Lenses:** **Gov** keeps framing influence and later choice authority distinct; **Arch** exposes how formulations change dependent results; **Onto/Epist** separates the situation, formulation, claims, evidence, and causal hypotheses; **Prag** requires material difference and a stopping rule; **Did** provides ordinary-language contrasts before formal models.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-frame bias | The opening brief becomes the only formulation. | Externalize it with sources and exclusions, then seek structural contrasts. |
| vocabulary bias | Synonyms are counted as plurality. | Require a changed boundary, evidence need, intervention family, value, or receiving-use consequence. |
| consensus bias | Participants must agree on one wording before inquiry. | Retain incompatible formulations and name their downstream differences. |
| causality bias | A framing hypothesis is reported as the cause. | State mechanism, support, uncertainty, and falsifying or narrowing evidence. |
| option leakage | Problem formulations become preselected solutions. | State intervention families as consequences of a frame, not proven answers. |
| endless-reframing bias | Every possible perspective stays live. | Stop when added formulations no longer change the named use enough to justify cost. |

### PSD.3:7 - Conformance Checklist

- [ ] Every formulation concerns the same bounded subject and receiving use, or the identity change is returned to `PSD.1`.
- [ ] Material participants and concerns from `PSD.2` are used as inputs without being treated as proof or settlement.
- [ ] Each retained formulation changes at least one boundary, evidence need, model, alternative family, value treatment, or receiving-use consequence.
- [ ] Sources, assumptions, exclusions, uncertainty, and intervention logic are visible.
- [ ] Causal, evaluative, legal, ethical, safety, and authority claims retain their direct assurance.
- [ ] The set is not ranked, selected, synthesized, or converted into a decision by this pattern.
- [ ] The stopping rule prevents both decorative plurality and endless reframing.
- [ ] Missing premises produce a gap, narrowed claim, request, blocker, or abstention.
- [ ] The result can feed `PSD.4`, `PSD.5`, `PSD.8`, or `PSD.16` without imposing a universal traversal order.

### PSD.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Agree on the problem first.” | Agree on the receiving use; retain materially different problem formulations. |
| “Brainstorm ten frames.” | Keep only formulations that change a named downstream move. |
| “Every stakeholder gets a frame.” | Build coherent formulations from material differences; participation identity does not define one frame each. |
| “The most popular frame is true.” | Popularity establishes neither truth, causal support, value priority, nor authority. |
| “A novel wording is a new problem.” | Use the material-difference test; use `C.17` only if novelty characterization itself matters. |
| “The formulation set is an option archive.” | Use `PSD.8` for decision alternatives and `C.18` for governed archives or fronts. |

### PSD.3:9 - Consequences

Later models, boundaries, alternatives, and recommendations inherit visible framing assumptions instead of one hidden sponsor frame. Practitioners can investigate incompatible accounts without forcing premature consensus. The cost is explicit source and contrast work, and some engagements will stop because a framing premise cannot yet be supported.

### PSD.3:10 - Rationale

Problem formulation is a field-specific generative move: it connects contested descriptions, concerns, values, evidence needs, and intervention logics to a receiving decision-support use. Generic candidate-set patterns can characterize or steward a set after generation, but they do not construct problem formulations. PSD.3 therefore owns the smallest plural-formulation result while reusing direct FPF patterns for evidence, episteme identity, relations, set characterization, and authority.

### PSD.3:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a practitioner preserve plural framing without losing a usable inquiry? | Treat framing as selection and organization of what matters, externalize materially different formulations, compare their consequences, and revise them as contextual evidence changes. | A fixed sponsor brief is the serious default; unconstrained perspective collection is the opposite default. | The first hides framing commitments and the second cannot stop. **Adapt:** `PSD.3:4.1`–`4.5` requires structural contrasts, downstream materiality, sources, and a receiving-use stop. | Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25) supports multiple non-equivalent meanings of design framing; Litster, Cardoso, and Hurst's [2024 study](https://doi.org/10.1017/S089006042400012X) supports observation of changing externalized team framing; Nickel, Hurst, and Duimering's [2024 study](https://doi.org/10.1017/dsj.2024.34) supports contextual trade-offs. These sources establish neither one framing ontology, universal Method, shared team frame, prevalence, causality, nor superiority. | Reopen if later comparative evidence changes the best-known framing line or if contextual evidence materially changes a retained formulation. |
| What remains specifically PSM work after generic candidate handling is subtracted? | PSM practice retains the construction and facilitation of rival problem formulations for ill-structured situations; FPF supplies direct evidence, relation, identity, and later-choice governors around that result. | Treating formulation as generic brainstorming, alternative generation, or archive management is the serious default. | It loses the relation between a formulation and the concerns, boundaries, evidence, and intervention logic of the receiving inquiry. **Adopt:** the formulation face in `PSD.3:4.3` and the pass-forward boundary in `4.6`. | Smith and Shaw's [2019 review](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) support PSM as a continuing, diverse, facilitated branch for ill-structured situations. Current `C.17` characterizes novelty/diversity/use of a named set; current `C.18` governs open-ended generation, archives, fronts, descriptors, and telemetry. None proves that one PSM, formulation count, facilitation arrangement, or archive policy is universally sufficient or superior. | Reopen if a direct generic pattern acquires the full PSM-specific construction at equal or lower effort, or if PSM evidence changes the material plurality test. |

### PSD.3:12 - Relations

- `PSD.1` supplies the bounded subject, receiving use, horizon, recipient, and authority boundary. `PSD.2` supplies material participants, affected Systems, concerns, duties, interests, and dissent.
- `PSD.4` receives the plural set when the current included/excluded problem boundary must be chosen. `PSD.5` receives formulation-dependent model needs.
- `PSD.8` receives formulation-dependent alternative families; it does not retroactively define the problem. `PSD.16` can retain the plural formulation set in an inquiry result.
- `C.17` may characterize novelty, diversity, or use of the generated set. `C.18` governs archive/front/generation-record stewardship only when those objects are actually needed.
- Direct episteme, evidence, relation, value, causal, legal, ethical, safety, governance, and choice patterns govern their own claims. PSD.3 neither ranks the set nor authorizes the later choice.

### PSD.3:End


<a id="psd-4"></a>
## PSD.4 - Set and Reopen the Problem Boundary

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** a **usable problem scope and reopen basis** for one bounded receiving inquiry: the formulations, participants, affected Systems, concerns, relations, conditions, horizons, and intervention families included now; material exclusions and unknowns; why the cut is usable; and observable conditions for widening, narrowing, or otherwise revising it.

### PSD.4:0 - Use This When

Use this pattern when a decision-support inquiry either expands toward everything connected with the situation or excludes a concern, bearer, relation, horizon, or intervention family that could reverse the usefulness of the result. Use it after or alongside `PSD.3` when plural formulations imply different boundaries.

Choose the smallest boundary that supports the named receiving decision or Work, make consequential exclusions visible, and state how the boundary can reopen. The practical gain is an actionable scope without pretending that what lies outside is false, irrelevant forever, or unaffected.

Do not use PSD.4 merely to decide whether one exact `U.ContextSlice` belongs to an already-declared `U.Scope`; use `A.2.6` for that claim. Do not use it for generic document scope, organizational jurisdiction, a System boundary owned by a direct engineering practice, or a static project charter when no problem-structuring question remains. Return to `PSD.1` if the receiving use or engagement identity itself is unclear.

### PSD.4:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| engagement boundary | The `PSD.1` boundary around the decision-support return, recipient, subject, horizon, receiving use, and authority. |
| problem boundary | The provisional cut that determines which formulations, bearers, concerns, relations, conditions, horizons, evidence, and intervention families are treated as material now. |
| material exclusion | An omitted or deferred item that could change the current result and therefore must remain visible with a reason, uncertainty, and reopen condition. |
| usable scope | The smallest current problem boundary adequate for a named next result and its assurance burden. It need not be exhaustive or permanent. |
| reopen basis | An observable change or newly recoverable value that can make the current boundary too narrow, too broad, or otherwise unfit for the receiving use. |
| `U.Scope` | A declared scope for exact `U.ContextSlice` membership, governed by `A.2.6`. An ordinary problem boundary need not be reified as one. |

### PSD.4:1 - Problem frame

Every formulation makes a cut. It foregrounds some participants, Systems, concerns, causal or modal paths, operating conditions, time horizons, evidence, and intervention families while leaving others outside. In ill-structured situations those cuts are often contested and revisable rather than simply discovered.

The primary concern is not to find the one true perimeter. It is to choose and expose a boundary adequate for one receiving use while preserving the exclusions and observations that could require revision. Recognition can begin with one plausible boundary reversal. Consequential inclusion, exclusion, relation, harm, authority, legal, ethical, safety, or factual claims retain their direct assurance.

### PSD.4:2 - Problem

An implicit sponsor boundary hides who and what the inquiry sacrifices. A comprehensive “whole system” map creates the opposite failure: every related condition enters, no stopping rule survives, and the receiving decision disappears. An exact scope declaration can conceal that the underlying inquiry cut remains contestable.

Once models and data collection begin, their available variables make the boundary appear natural. Excluded concerns then vanish rather than remaining explicit deferrals. A later observation is treated as noise instead of evidence that the inquiry should widen, narrow, or change formulation.

### PSD.4:3 - Forces

| Force | Tension |
| --- | --- |
| Actionability | A current cut is needed to proceed, while premature closure can reverse the result. |
| Completeness | Wider scope can reveal consequences, while unlimited scope destroys affordability and accountability. |
| Explicit exclusion | Material omissions must stay visible, while a boundary register should not become an encyclopedia. |
| Stability and revision | Dependent work needs a current scope, while new evidence can legitimately reopen it. |
| Exact membership | Exact contextual membership sometimes matters, while ordinary problem boundaries need not become `U.Scope` values. |
| Authority | A boundary can inform later work, while it does not authorize the later decision or erase specialist jurisdiction. |

### PSD.4:4 - Solution

Set the problem boundary relative to one receiving use and one or more current formulations. Name what is included, what is excluded or unknown, why the cut is usable now, and which observable changes can reopen it. Use `A.2.6` only when a receiving claim depends on exact `U.ContextSlice` membership in a declared `U.Scope`.

#### PSD.4:4.1 - Fix the receiving use and current formulations

Recover the subject, recipient, receiving decision or Work, horizon, and choice owner from the current `PSD.1` engagement question or a qualified direct source for the same inquiry. Name the `PSD.3` formulations whose consequences the boundary must preserve. If no plural set is needed, state the one current formulation and why a rival is not material.

Use a current `PSD.2` account where participants, affected Systems, concerns, duties, interests, dissent, representation limits, or possible consequence paths can challenge the cut. Inclusion in that account does not require inclusion in every current model or analysis; exclusion from the boundary does require an honest reason when material. When an input needed for the cut is unavailable, stale, or incompatible, obtain a qualified direct result or return the exact missing premise. A formulation alone does not establish current representation or choice authority.

#### PSD.4:4.2 - State the boundary through decision-bearing dimensions

Name only dimensions that can change the receiving use:

- subject, configuration, place, population, and operating condition;
- included formulations and affected bearers;
- concerns, duties, interests, relations, dependencies, and consequence paths;
- evidence interval, uncertainty, and time horizon;
- intervention, adaptation, restraint, and no-action families; and
- participating, receiving, implementing, and choice-authority positions where material.

State the cut in ordinary language; add an exact `U.Scope` declaration only when the receiving use needs it. A boundary is not justified by drawing a box or using the word “system”.

#### PSD.4:4.3 - Keep material exclusions and unknowns alive

For every omitted item that could change a downstream result, record the item, exclusion reason, current evidence or uncertainty, consequence of being wrong, and reopen observation. Distinguish:

- outside for this receiving use from irrelevant in general;
- deferred from rejected;
- unknown membership from supported non-membership;
- absent evidence from evidence of absence; and
- a practical stopping decision from a claim that no relation or consequence exists.

Items with no plausible consequence for the current use need not receive a full record. Items that can reverse a high-consequence result require proportionate direct assurance or an explicit stop.

#### PSD.4:4.4 - Challenge the cut before accepting it

Apply the smallest relevant challenges:

1. **bearer challenge:** could a participant or affected System outside the cut undergo a material change?
2. **formulation challenge:** would another retained formulation include a different mechanism, value, horizon, or intervention family?
3. **action challenge:** does the cut make one alternative appear necessary by excluding feasible restraint, adaptation, or no-action branches?
4. **evidence challenge:** are data availability or model convenience defining the boundary?
5. **authority challenge:** does the cut silently transfer a duty, jurisdiction, implementation burden, or later choice?
6. **reversal challenge:** what smallest observation would make the current result unusable or materially different?

Repair only the affected dimension. A challenge does not require maximal widening.

#### PSD.4:4.5 - Use exact scope membership only when needed

When a downstream claim depends on whether one exact `U.ContextSlice` belongs to one declared `U.Scope`, use `A.2.6`. Distinguish an evaluation result of true, false, or unknown. Unknown means the available basis cannot decide; obtain the missing input, narrow the attempted use, or abstain instead of asserting exclusion. Changing the extension creates a new scope; a refit that preserves the extension does not.

Do not force every ordinary concern or participant into `U.Scope`. PSD.4 governs the field-specific judgement that a problem boundary is usable for the current inquiry; `A.2.6` governs exact contextual membership. A `C.2.3` formality threshold concerns how strictly a claim is expressed and is selected separately, only when the receiving use needs it.

#### PSD.4:4.6 - Return the usable scope and reopen basis

| Result position | Required content |
| --- | --- |
| receiving use | Subject, recipient, decision or Work, horizon, and retained choice owner. |
| formulation basis | Current formulations and the material differences the boundary preserves. |
| included scope | Bearers, concerns, relations, conditions, horizons, evidence, and intervention families included now. |
| exclusions and unknowns | Material omissions or uncertainties, reasons, consequences of error, and direct assurance still needed. |
| adequacy reason | Why this is the smallest scope usable for the named next result. |
| dependent uses | Models, facilitation, alternatives, value treatment, comparison, recommendation, or inquiry results that consume the scope. |
| reopen basis | Observable triggers and the dimension to widen, narrow, replace, or re-formulate. |

If no defensible boundary is available, return the exact missing premise, blocker, narrowed claim, or abstention. Do not hide the stop by expanding the map.

#### PSD.4:4.7 - Reopen locally and state what changed

Reopen when a new participant, affected System, concern, formulation, relation, operating condition, evidence result, value tension, intervention family, horizon, receiving use, or authority fact can change the current result. Name the old boundary, new observation, affected dimension, and dependent result.

Widen, narrow, or replace only that portion. If a declared `U.Scope` or a relied-upon membership result changes, apply `A.2.6`; if the engagement identity or receiving use changes, return to `PSD.1`; if a new formulation is needed, return to `PSD.3`.

#### PSD.4:4.8 - What changes in practice

The practitioner stops treating scope as either the sponsor's box or an ever-growing map. They can state a small usable cut, defend why exclusions are tolerable now, and show the precise observation that would reopen each consequential part.

### PSD.4:5 - Archetypal Grounding

#### PSD.4:5.1 - Flood-pump boundary

For the board's pre-season decision, the current boundary includes the district pumping arrangement, permanent and mobile capacity, maintenance and staffing dependencies, deployment safety, district access, the next flood season, and material downstream transfer paths. It preserves all four `PSD.3` formulations rather than reducing the inquiry to pump count.

Long-term watershed redesign and permanent residential relocation are outside the current investment return, but they are not declared irrelevant. Relocation rights and downstream consequences remain material exclusions because they can reverse a recommendation. The boundary records that verified cross-district flood transfer, a safety limit outside the assumed operating envelope, or evidence that no feasible pump branch protects mobility-constrained residents will reopen the relevant dimension.

The result is usable for model and alternative work. It does not authorize funding, assert that every included consequence obtains, or make the emergency board competent to settle legal, ecological, or safety questions.

#### PSD.4:5.2 - Narrowing after a failed generalization

An incident-response inquiry initially covers all product lines. Evidence shows that the proposed escalation pattern applies only to one regulated line and one staffing configuration. The practitioner narrows the problem boundary and dependent recommendation instead of claiming organization-wide use. Other lines remain explicit unknowns with their own reopen conditions.

#### PSD.4:5.3 - Cheap non-use

A laboratory test claim already has a declared `U.ClaimScope` with population, configuration, and interval selectors. The live issue is whether one proposed test's `U.ContextSlice` belongs to that scope. Use `A.2.6` directly. PSD.4 adds no problem-structuring judgement.

### PSD.4:6 - Bias-Annotation

**Scope:** provisional problem boundaries for a named decision-support use. **Lenses:** **Gov** keeps inclusion, jurisdiction, and choice authority separate; **Arch** exposes dependencies on the cut; **Onto/Epist** distinguishes situation, formulation, ordinary boundary, declared `U.Scope`, and evidence; **Prag** seeks the smallest usable scope; **Did** makes exclusions and reopen cues readable without a specialist notation.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-boundary bias | The brief's perimeter becomes unquestionable. | Challenge it with bearers, formulations, actions, evidence, authority, and reversal. |
| map-completeness bias | More nodes are treated as better scope. | Require each included dimension to change the receiving use. |
| data-availability bias | Available variables define the problem. | Record excluded concerns and evidence gaps independently of the model. |
| box-as-ontology bias | A drawn perimeter is treated as proof of a System boundary or exact scope membership. | State the ordinary decision-support cut; use the direct engineering practice for a System-boundary claim and `A.2.6` for contextual membership when either is needed. |
| exclusion-as-falsehood bias | Outside the current inquiry becomes “does not matter”. | Record material exclusions, uncertainty, consequence, and reopen basis. |
| boundary-freeze bias | Later contrary evidence is absorbed without revising scope. | Reopen the smallest affected dimension and dependent results. |

### PSD.4:7 - Conformance Checklist

- [ ] The boundary is tied to one receiving use, subject, horizon, and authority boundary.
- [ ] Current formulations and material participation or affected-System inputs are recoverable.
- [ ] Included bearers, concerns, relations, conditions, evidence, horizons, and intervention families are stated only at the needed grain.
- [ ] Material exclusions and unknowns retain reasons, consequences of error, and reopen observations.
- [ ] The bearer, formulation, action, evidence, authority, and reversal challenges were applied proportionately.
- [ ] The result explains why the cut is the smallest usable scope for a named next result.
- [ ] Ordinary problem-boundary judgement is not confused with exact `U.ContextSlice` membership in `U.Scope`.
- [ ] Missing premises produce a gap, narrowed claim, request, blocker, or abstention.
- [ ] Reopening changes the smallest affected dimension and identifies dependent results.
- [ ] The scope neither authorizes the later choice nor displaces direct legal, ethical, safety, scientific, engineering, or governance practices.

### PSD.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everything is connected, so include everything.” | Include only what can change the named receiving use; preserve material exclusions and triggers. |
| “Outside scope means irrelevant.” | State outside-for-now, consequence of error, and reopen condition. |
| “The model boundary is the problem boundary.” | Let formulations and concerns challenge available variables and model convenience. |
| “Draw the system boundary.” | Name the problem-structuring cut; establish any System-boundary or exact contextual-membership claim through its direct pattern. |
| “Unknown means excluded.” | Separate true or false membership from an unknown evaluation; unknown does not establish exclusion. |
| “Scope was agreed at kickoff.” | Reopen when the named observation can change the receiving result. |

### PSD.4:9 - Consequences

The inquiry becomes bounded enough to support models, alternatives, comparison, and recommendation while keeping consequential omissions recoverable. Revision can be local rather than a complete restart. The cost is explicit exclusion work and occasional narrowing, widening, or stopping when a premise cannot be assured.

### PSD.4:10 - Rationale

Problem boundaries are practical framing commitments. A discovered perimeter or exact membership test alone does not establish that a cut is adequate for a receiving inquiry. PSD.4 contributes that PSM-specific judgement and preserves the conditions under which the cut must change. `A.2.6` remains the direct owner of exact contextual membership when that stronger claim is needed.

### PSD.4:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a problem boundary remain useful and revisable? | Treat framing as a contextual selection of what matters, compare materially different cuts, state exclusions, and revise the boundary when new evidence changes the receiving use. | A fixed sponsor scope is the serious default; an unbounded whole-situation map is the opposite default. | The first suppresses consequential exclusions and the second cannot stop. **Adapt:** `PSD.4:4.1`–`4.4` and `4.6` require decision-bearing dimensions, material exclusions, explicit challenges, and a smallest-usable-scope reason. | Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25), Litster, Cardoso, and Hurst's [2024 mapping study](https://doi.org/10.1017/S089006042400012X), and Nickel, Hurst, and Duimering's [2024 contextual trade-off study](https://doi.org/10.1017/dsj.2024.34) support explicit framing, externalized change, and contextual trade-offs. They establish neither one framing ontology, universal Method, shared frame, fixed boundary, prevalence, causality, nor superiority. | Reopen if later field evidence changes the best-known boundary practice or if new contextual evidence changes an included or excluded dimension. |
| When does a receiving use need exact contextual scope membership? | Keep ordinary inquiry cuts in plain language; use current `A.2.6` only when the receiving use must decide whether one exact `U.ContextSlice` belongs to one declared `U.Scope`. | Treating every diagram box or topic perimeter as a declared exact scope is the serious default. | It substitutes apparent precision for boundary judgement and can hide unavailable evaluation. **Adopt:** `PSD.4:4.5` distinguishes true, false, and unknown evaluation results and routes extension changes to the direct pattern. | Current `A.2.6` supplies exact contextual membership, extension change, and refit discipline. Its applicability axis is independent of `C.2.3` formality. It does not judge which participants, concerns, formulations, intervention families, or exclusions make a PSM boundary usable. Direct engineering, legal, safety, ethical, and governance practices retain their own boundaries and thresholds. | Reopen if the direct scope pattern gains the complete problem-boundary judgement at equal or lower effort, or if a relied-upon scope or membership result changes. |

### PSD.4:12 - Relations

- `PSD.1` supplies the engagement identity and authority boundary. `PSD.2` supplies participation, concern, and affected-System challenges. `PSD.3` supplies the plural formulation set whose differences the boundary must preserve.
- `PSD.5` and `PSD.6` receive the scope and formulation basis for modeling and PSM-arrangement questions. `PSD.16` receives the scope and reopen basis for the inquiry result.
- `A.2.6` governs exact `U.ContextSlice` membership in a declared `U.Scope` when that claim is needed. `A.1.CSD` supplies consequence-bearer challenges; exact relations remain with their direct governor.
- Direct evidence, legal, ethical, safety, scientific, engineering, governance, assignment, and authority patterns govern their own claims. PSD.4 neither establishes those results nor authorizes the later choice.

### PSD.4:End


# Part II — Models, Methods and Facilitated Inquiry

<a id="psd-5"></a>
## PSD.5 - Construct Complementary Situation and Option Models

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** a **multi-model decision account**: the smallest useful set of situation and option models, the questions each answers, their correspondences and limits, and the claims or unresolved questions that a named receiving inquiry may use.

### PSD.5:1 - Problem frame

**Use this when** one diagram, spreadsheet, simulation, or agreed story is being asked to explain a contested situation, represent everyone's concerns, predict consequences, and identify the best intervention. Also use it when several models exist but their different subjects, assumptions, or meanings make their combined result unclear.

Start with the question that could change the next decision-support move. Choose a model that can answer it, then add another only for a material question the first cannot answer. The gain is a usable account of complementary and conflicting findings, not a larger model collection.

The governed object is that bounded account of model contributions. A model makes selected claims about a subject; a diagram, table, or screen expresses some model content; the people, pumps, service arrangements, and possible changes being considered remain the subjects. The account connects these without making them one object.

**Do not use this pattern** when one already-qualified calculation or model answers the entire receiving question and no material contrast remains. Use the direct modeling, engineering, scientific, or evidence practice for its own validity question. Return to problem formulation or boundary work when the difficulty is that nobody can say what the models should help decide.

### PSD.5:2 - Problem

A capacity calculation cannot show whose service standard should govern. A rich picture can reveal attributed concerns without estimating a failure probability. A scenario can expose a vulnerable condition without predicting how often it will occur. Treating any one of these as a complete account hides questions it was never built to answer.

Adding models does not automatically repair the loss. Two models may reuse the same data, employ incompatible units or populations, or label different quantities “risk”. Agreement can be duplicated error; disagreement can reflect different questions rather than a defect. A composite dashboard can conceal both.

### PSD.5:3 - Forces

| Force | Tension |
| --- | --- |
| Discrimination | Each model should change a claim, alternative, or inquiry priority, while exploratory models may first reveal what question matters. |
| Plurality | Material perspectives deserve distinct expression, while collecting every imaginable model makes the engagement unaffordable. |
| Correspondence | Related models need interpretable connections, while forced translation can erase their different meanings. |
| Credibility | Consequential reliance requires qualified evidence, while a preliminary model can still be useful for recognizing a missing premise. |
| Revision | A shared boundary permits comparison, while a model may reveal why that boundary must reopen. |

### PSD.5:4 - Solution

Build a question-led set of complementary models. For each, state its subject, intended use, assumptions, evidence, and what it omits. Compare only the overlapping claims whose meanings can be aligned, retain material differences, and return the usable claims together with their limits.

#### PSD.5:4.1 - Recover the questions and current boundary

Use the plural formulation set from `PSD.3` where its differences identify claims or intervention logics that models must discriminate. A formulation is an interpretation of the problem, not already a validated model of the situation. Use the `PSD.4` scope and reopen basis for the same subject, receiving decision, operating conditions, and horizon.

These are conditional inputs, not compulsory earlier stages. A qualified direct source may supply the needed formulation or scope. If a needed result is unavailable, stale, outside the present use, or incompatible, return its exact missing premise or narrow the inquiry; do not infer it from the presence of another model.

Turn the live differences into questions, such as “Does this arrangement retain service when road access is lost?” and “Whose loss is omitted by the aggregate service measure?” Keep question, assumed condition, and proposed intervention separate.

#### PSD.5:4.2 - Choose complementary contributions at the needed grain

Consider what each model can actually contribute before selecting a notation or tool.

| Needed contribution | A possible model | Limit to preserve |
| --- | --- | --- |
| Make different interpretations and concerns discussable. | A rich picture, purposeful-activity model, or attributed cognitive map. | It expresses selected interpretations; agreement with the drawing is not agreement with an intervention or proof of a causal relation. |
| Examine a proposed mechanism or dependency. | A causal, stock-and-flow, network, or dependency model. | An arrow may be a hypothesis or structural assumption. A causal claim requires its direct evidence. |
| Explore changed conditions and intervention responses. | A scenario or conditional simulation. | A scenario is not a probability estimate; a simulated response depends on the model and inputs. |
| Expose objectives and distinguish consequences. | An objectives hierarchy, criteria model, or consequence table. | The arrangement does not supply legitimate weights, commensurability, or permission to trade one concern against another. |
| Test a technical feasibility premise. | A domain calculation or qualified engineering model. | Feasibility holds only within its configuration, operating envelope, evidence, and uncertainty limits. |

Select the smallest set that covers the material questions. A qualitative model may reveal a question worth quantifying; a numerical model may reveal a missing qualitative distinction. Neither direction is a universal order. Drop a model that supplies no distinct contribution unless its independently grounded evidence is needed to challenge another.

#### PSD.5:4.3 - Make each model's use intelligible

A reader should be able to say: “This model concerns this subject, answers this question under these conditions, and supports this limited use.” Supply the assumptions, evidence source and interval, important omissions, and an observation that would invalidate or narrow that use. Identify the exact model content or edition when a changed value could alter the result.

For a mathematical formalism, simulation, or learned representation, apply `C.29` when the choice of mathematical object, mapping, preserved structure, or information loss changes the claim. For example, a road graph can preserve routes and travel-time assumptions while omitting residents' access rights and the reliability of an untested deployment procedure. C.29 does not establish those omitted facts.

Ordinary local meaning needs only the relevant meaning, units, scope, or evidence statement. Use `A.1.1` for an actual model-applicability, assigned-Work-use, or fixed-expression-coherence claim; select its broader bounded model-use structure only when that organization changes the receiving decision. Neither a model collection nor the word “context” supplies that structure.

#### PSD.5:4.4 - Reconcile overlaps without forcing one model

For each overlap that matters, compare the subject and configuration, population, time horizon, units, definitions, assumptions, and evidence dependencies. State an actual correspondence only as far as the meanings support it. If “service failure” means lost pumping capacity in one model and inability to reach a refuge in another, keep the meanings distinct and ask whether a further relation can be established.

Classify a consequential mismatch before repairing it: different questions, different assumptions, incompatible meanings, contradicted evidence, or a genuine unresolved conflict. Correct a unit or input error locally. Retain alternative assumptions when their truth is not known. Request a direct investigation when the conflict can reverse the receiving result.

Do not average unlike outputs, infer a shared probability from scenario counts, or count models drawing on one dataset as independent confirmation. A combined explanation may show how models inform one another without claiming that they form one unified model.

#### PSD.5:4.5 - Match assurance to the claim being used

Recognition can begin with a sketch and a plausible contrast. Before consequential reliance, inspect the claims that bear the result: source qualification, implementation or calculation correctness, fitness to the intended use, validation evidence, sensitivity, and extrapolation limits as applicable. The direct domain practice determines what is sufficient; this pattern supplies no universal validation threshold.

Separate confidence in the modeler, internal consistency, empirical adequacy, robustness to assumptions, and authority to decide. A stakeholder's confidence can affect whether a model is used, but cannot substitute for evidence. A model that cannot yet support a recommendation may still support the narrower result “this assumption requires a discriminating test”.

Return a qualified claim, a narrowed use, an exact evidence request, or an explicit inability to discriminate. Where an unresolved safety, rights, legal, or technical premise can reverse the use, retain that stop and obtain its direct competent result.

#### PSD.5:4.6 - Return the account and its reopen basis

Keep enough content for the recipient to recover:

- the subject, question, receiving use, configuration, and horizon;
- each selected model's distinct contribution, current content, source basis, assumptions, and losses;
- the material correspondences, conflicts, and shared evidence dependencies;
- what the account supports, what remains hypothetical or unknown, and which alternatives or claims it can discriminate; and
- the observation that would reopen a model, its connection to another, the problem formulation, or the boundary.

This can be a short annotated comparison; it need not be a new repository or universal record form. If no model combination answers the question, say so. A missing direct result is more useful than a polished but unsupported combined answer.

The same account may inform Method selection, alternative generation, uncertainty treatment, or conflicts between simultaneous inquiries. Each recipient takes only the current, compatible contribution it needs; the account does not complete those later judgements.

#### PSD.5:4.7 - What changes in practice

Instead of asking which model is “the right one”, the practitioner asks which claims need a model, what each selected model contributes, and which difference would change the next move. Models can remain usefully plural while their overlaps and limits are explicit.

### PSD.5:5 - Archetypal Grounding

#### PSD.5:5.1 - Flood-pump models that answer different questions

In this illustrative continuation of the flood-pump inquiry, the board needs a pre-season decision-support return about permanent pumps, mobile capacity, maintenance, staffing, and access. The current formulations distinguish capacity shortage, deployment reliability, unequal service, and transferred downstream consequences. The scope includes the next flood season and preserves relocation rights and long-term watershed change as material exclusions.

The inquiry team constructs the following bounded account. The values are illustrative case premises, not engineering advice.

| Question and model | Account slice | Consequence for inquiry |
| --- | --- | --- |
| Can nominal capacity meet the assumed inflow? A capacity calculation. | Permanent and mobile branches meet the assumed requirement only with the stated operating units available; no deployment delay is represented. | Nominal capacity alone cannot discriminate reliability or access. |
| Can mobile units reach and serve the district? An access-and-deployment scenario model. | With the main road unavailable, the mobile branch has no supported arrival-time claim. A second route is a hypothesis requiring an operations result. | Keep the mobile branch conditional; request route and deployment evidence. |
| What counts as adequate service, and for whom? An attributed concern map. | The residents' association emphasizes property protection. A separately heard group of mobility-constrained residents requires reachable assistance. Neither statement represents all residents. | Preserve the two service meanings; the hydraulic output does not settle their relation or priority. |

The account returns: “Nominal capacity is not presently the discriminating uncertainty. The mobile branch depends on an unqualified access premise. The service comparison must retain both property protection and reachable assistance.” It does not rank the branches.

If verified access evidence closes the transport gap, only the affected model claim and its dependent uses reopen. If no feasible pump branch supports the service concern, the problem boundary reopens. Repeated use of the same inflow dataset by both technical models supplies one evidence dependency, not two confirmations.

#### PSD.5:5.2 - Development advice across two holders

An adviser compares a training direction for two service teams. A skills map suggests similar learning needs, but each team's queue model uses its own demand and staffing evidence. The combined account keeps those holders separate: an improvement simulated for Team A supplies no performance claim for Team B.

For Team B, the return is a bounded trial question with its missing demand premise, not the transferred benefit estimate. More detailed modeling of Team A would not repair the absent Team B evidence.

#### PSD.5:5.3 - Cheap non-use

A technician needs one conversion under an already-qualified formula, with agreed units and no material uncertainty about applicability. Use that calculation directly. A rich picture, scenario set, and second model would add no discriminating result.

### PSD.5:6 - Bias-Annotation

**Scope:** models supporting bounded problem-structuring and decision-support questions. **Lenses:** **Onto/Epist** separates subject, model, expression, and evidence; **Prag** selects useful discrimination; **Arch** exposes model connections; **Gov** preserves later choice and direct authority; **Did** makes different model contributions readable.

Model-prestige bias favors the most technical representation. Agreement bias counts correlated outputs as corroboration. Model-availability bias turns measurable variables into the whole problem. Counter these by naming each model's question, inspecting shared assumptions and evidence, and keeping material unmodeled concerns visible. Plurality itself can become a bias: remove a redundant model when it changes no claim or assurance need.

### PSD.5:7 - Conformance Checklist

- [ ] The account serves a named subject, question, receiving use, configuration, and horizon.
- [ ] Needed formulation and scope inputs are current and compatible, or their exact gaps are returned.
- [ ] Each model supplies a distinct useful contribution; one sufficient model remains a valid cheaper exit.
- [ ] The subject, model content, expression, evidence, and possible intervention remain distinguishable.
- [ ] Assumptions, important losses, and limits accompany every relied-on output.
- [ ] Material overlaps are compared by meaning, scope, units, and evidence dependency; unresolved differences are not averaged away.
- [ ] Mathematical-lens and actual model-use claims receive their direct treatment only when needed.
- [ ] Recognition, validation, confidence, causal evidence, and authority are not substituted for one another.
- [ ] The returned account identifies usable claims, unresolved discriminating questions, and local reopen conditions.

### PSD.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The simulation represents the situation.” | State the exact question, represented conditions, and omitted concerns. |
| “Three models agree, so the evidence is stronger.” | Recover whether their assumptions, data, or implementation errors are shared. |
| “Every perspective needs its own complete model.” | Retain only perspectives whose difference changes a present claim or use; use a smaller expression where sufficient. |
| “The qualitative map supplies the probabilities.” | Keep attributed beliefs separate from calibrated evidence and request the missing basis. |
| “Consistency means validity.” | Test the relevant model-to-world claim through the direct practice. |
| “C.29 governs every picture.” | Open its mathematical-lens branch only for a real mathematical-lens choice that changes use. |

### PSD.5:9 - Consequences

The recipient sees which model can answer which question and where the combined account stops. Contradictions can guide inquiry instead of being hidden by one score. The cost is explicit assumptions and correspondence work; limit that work to overlaps that could alter the result. A smaller qualified answer may replace an apparently comprehensive conclusion.

### PSD.5:10 - Rationale

Complementarity is a relation between useful contributions to a question, not a model count. Purpose-led selection and explicit loss preserve different interpretations while making technical claims inspectable. Separate assurance keeps a useful representation from becoming unearned evidence about the world.

### PSD.5:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should models contribute jointly without hiding their different meanings? | Select models by the questions they answer and inspect the joins between problem structuring and analysis. | One comprehensive model is the serious default; an unconstrained collection is the rival expansion. | **Adapt:** `PSD.5:4.1`–`4.4` choose the smallest complementary set and expose incompatible meanings. Compared with expanding one model, this deliberately accepts some correspondence work to preserve a material concern that the single model omits; it makes no universal claim of lower cost. | Marttunen, Lienert, and Belton's [2017 review of PSM–MCDA combinations](https://doi.org/10.1016/j.ejor.2017.04.041) is a critical synthesis candidate for combination benefits and interface difficulties, including value-tree and weighting issues. Its reviewed applications are not controlled evidence that more models are better or that one combination fits every inquiry. The question-led selection and non-use rule are PSD adaptations. | Reopen if a simpler model answers the same material questions with equivalent limits, or a new mismatch shows that the chosen combination loses a consequential meaning. |
| What justifies relying on a model-supported claim? | Qualify the intended use, evidence, and losses separately from confidence in the model or its producer. | Technical sophistication, modeler reputation, or participant confidence is treated as sufficient credibility. | **Adapt:** `PSD.5:4.3`–`4.6` and the flood-pump case retain applicability, evidence dependencies, and unresolved assumptions. The extra assurance effort is accepted only where it can change reliance; sketches remain usable for recognition. | Schwarzburg, Trauer, and Rebentisch's [2024 confidence study](https://doi.org/10.1017/dsj.2024.14) supplies bounded empirical evidence that model-, modeler-, and stakeholder-related factors are associated with confidence and reliance. Its exploratory survey and proposed application model do not validate a particular decision model or establish causal decision quality. Current `C.29` supplies mathematical mapping and loss discipline, not validation, causality, or authority. `A.1.1` supplies its exact model relations, not universal context machinery. | Reopen when direct validation contradicts a relied-on claim, the use leaves its qualification window, or a current modeling practice offers the same assurance at materially lower effort. |

### PSD.5:12 - Relations

- `PSD.3` supplies formulations only where their differences guide model discrimination. `PSD.4` supplies the scope and reopen basis for the same subject and decision. Missing needed values require qualified direct sources or an exact gap.
- `PSD.6`, `PSD.8`, and `PSD.16` may use the model account to discriminate their Method, alternative, or simultaneous-inquiry claims. Representation does not make the represented condition obtain.
- `PSD.10` may use the account's evidence only for the same configuration and horizon; that evidence neither entails its uncertainty judgement nor authorizes action.
- `C.29` governs load-bearing mathematical-lens use. `A.1.1` governs its exact model-applicability, assigned-use, and expression-coherence claims. Direct scientific, engineering, causal, and evidence practices retain their own truth and adequacy questions.
- Value treatment and comparison remain separate from constructing models. A model can expose a value conflict without settling it, and the later choice remains with its authorized owner.

### PSD.5:End


<a id="psd-6"></a>
## PSD.6 - Select and Combine Problem-Structuring Methods

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** an **engagement Method and limits**: the selected reusable way of conducting the bounded inquiry, why its contributions fit the required result, how any combined Methods connect, and the conditions under which the selection must change or stop.

### PSD.6:1 - Problem frame

**Use this when** a favorite workshop recipe, analytical technique, or problem-structuring method is being proposed before anyone has tested whether it can produce the needed result with these participants, uncertainties, conflicts, and resources. Also use it when several useful Methods are available but their combination has no clear contribution or usable join.

Start by naming the result the engagement is missing. Compare the simplest sufficient Method with a serious alternative, including a bounded combination when one Method cannot supply the needed contributions. The practical gain is a defensible way of proceeding, with visible limits and a cheaper exit when elaborate facilitation adds no value.

A **Method** (`U.Method`) is a reusable way of doing under stated applicability, participant meanings, preconditions, intended effects, and bounds. The governed question here is which such way fits this decision-support engagement and whether a proposed combination is coherent. A document describes it, a plan schedules intended work, and people enact it in actual work; none of those is the Method merely by appearance.

**Do not use this pattern** to select software by feature count, establish that a named person is competent or authorized, or schedule an already-selected Method. If one direct calculation or an existing sufficient Method closes the question, use it. If the missing result is the engagement's purpose or scope, return that question before choosing a workshop.

### PSD.6:2 - Problem

A popular method can be well described and still be wrong for the current inquiry. It may require participation that cannot be obtained, assume a shared purpose that is disputed, depend on data that do not exist, or produce agreement when the recipient actually needs competing claims and discriminating evidence.

Combining methods creates further risks. A concern map becomes numerical weights without an elicitation basis. A scenario becomes a probability distribution. Two workshops duplicate the same task while an essential technical question remains unanswered. A schedule of activities is called an integrated Method even though no one can explain what connects its results.

### PSD.6:3 - Forces

| Force | Tension |
| --- | --- |
| Fit | A Method must address the live difficulty, while familiar expertise makes some candidates easier to enact. |
| Participation | Joint inquiry can expose differences, while access, power, time, language, and willingness constrain genuine participation. |
| Complementarity | Several Methods can supply distinct contributions, while more methods add joins, effort, and failure opportunities. |
| Reuse and adaptation | Reusable ways make preparation and learning possible, while a local adaptation may change their identity or assurance needs. |
| Timeliness | The receiving decision has a horizon, while a deadline does not make missing premises true. |

### PSD.6:4 - Solution

Select by needed contribution and actual applicability, not by a school name or workshop format. Recover what each candidate Method does, compare alternatives at comparable effort, and justify every combination through the meaning of its inputs, outputs, and conditions.

#### PSD.6:4.1 - State the required result and selection conditions

Use the `PSD.4` scope for the same subject and receiving decision when it constrains the selection. Use a `PSD.5` model account only where its models, limits, or conflicts can discriminate candidate Methods. Neither input creates a mandatory sequence.

Recover the current facts that can change Method fit: whether the difficulty concerns interpretation, evidence, interconnected choices, values, or action; who can participate and through which channels; what disagreement must remain visible; the available expertise and data; and the time and resource boundary. Obtain consequential participation, competence, safety, and authority premises from qualified direct sources.

A source is useful only for its named subject, condition, and evidence window. If a required scope, model, or participation premise is missing or incompatible, state the exact gap, select a narrower use if defensible, or stop. Do not treat availability of a MethodDescription as evidence that the Method fits.

#### PSD.6:4.2 - Recover candidate Methods as ways of doing

For each serious candidate, describe the action in plain language: what participants do, with what accepted inputs, to produce which result under which conditions. When the proposed reusable way is already recoverable, use `A.3.1` to identify it.

Use `A.3.1.MR` only when several grounded occurrences or direct sources create a candidate-recovery question about what reusable way the material may show, and no Method has yet been established. It returns provisional source-traceable candidate accounts, a distinguishing question, or an honest lower result; Method identification remains a separate `A.3.1` question.

If the way is known and only its wording is unclear, clarify the statement; use `E.10` only if an FPF kind or relation question remains. If a prospective recipe lacks a decision about its intended action or applicability, return that missing design question to the person designing the engagement Method. A missing design choice is not by itself a reason to reconstruct past practice.

For a concrete contrast, three grounded inquiry accounts may leave two explanations plausible: a fixed question sequence with local exceptions, or a reusable rule that changes questions when a concern is challenged. That is a candidate-recovery question for `A.3.1.MR`. A new proposal saying only “interview residents” leaves its intended return and conditions unstated: ask its author to make those design choices, without inventing earlier inquiries. Once the proposed way is sufficiently stated, apply `A.3.1` without requiring such a history.

For example, an attributed-mapping Method elicits a participant's claims, explores their implied connections, checks the rendering with that participant, and retains unresolved differences. A conditional-analysis Method evaluates named alternatives under stated conditions with qualified models and returns consequences and limits. Their labels are insufficient; their actual contributions and applicability make comparison possible.

A source description can explain a Method without demonstrating its effectiveness in this engagement. Keep instructions, reported applications, direct comparative evidence, and practitioner competence distinct. A document about several Methods is not automatically a `U.MethodDescription` of one composite Method; `A.3.2` governs that membership.

#### PSD.6:4.3 - Compare the simplest sufficient candidate with a real alternative

Choose the comparison dimensions from the required result. The following questions are often decisive:

- Does the Method reveal the material interpretations, or does it require agreement that is absent?
- Can it use the available evidence without manufacturing precision?
- Can affected participants meaningfully contribute or challenge the result through available channels?
- Does it produce the kind of result the next inquiry needs?
- Can the needed expertise, time, and resources be provided?
- What important limitation or failure would remain?

Compare a single sufficient Method, the plausible incumbent, and a bounded combination only when each is a live alternative. Do not turn every engagement into a survey of all PSM families. State the trade-off if a richer result costs more preparation or excludes a faster route. Method popularity, a successful workshop elsewhere, and participant satisfaction do not establish comparative fit here.

If the necessary premise cannot be tested before the receiving decision, select a qualified provisional use or return the limitation. A declared gap is not a low score to be averaged away.

#### PSD.6:4.4 - Combine contributions through explicit joins

Combine only when the second Method contributes something material the first cannot provide at acceptable effort. Name the result or preserved condition passed between them, its meaning, the receiving precondition, and what happens when the join fails.

An attributed concern map can supply candidate objectives for examination. It cannot supply legitimate numerical weights without the separate elicitation and value assumptions those weights require. A qualitative scenario can supply a condition for technical analysis, not its probability. Keep such conversions as explicit additional work or leave the outputs uncombined.

Recover order from dependence. An analysis may need a specific formulation before it can run, while participation inquiry and technical evidence collection can proceed concurrently once their common question is clear. Their later join still needs compatible subject, conditions, meanings, and limits. Document order, calendar order, and simultaneous use do not establish Method composition.

When the engagement needs one composite `U.Method`, first identify the whole under `A.3.1`, then use `B.1.5` to qualify its independently identified part Methods and whole-forming claims. State the whole action, applicability, accepted inputs, result, required joins, allowed variations, exposed interactions, and failure or stop conditions. A different part, ordering, or interface outside the permitted variations can identify another Method.

If several Methods are merely coordinated without a recoverable whole, return that bounded arrangement honestly. It may be useful interim planning content, but it is not yet the promised engagement Method. Name the missing whole-action or join question rather than relabeling the activity list.

#### PSD.6:4.5 - Test the fragile premise and retain a stop

Test the assumption most likely to make the selected way unusable: for example, whether a participant can challenge an attributed statement, whether a model accepts the needed scenario, or whether two outputs mean the same thing. Use a small rehearsal, a direct evidence check, or a bounded trial only where it can change selection.

State what the trial can establish. A successful rehearsal may show that the contribution can be produced under those conditions; it does not demonstrate universal effectiveness or later implementation success. If a required participant, expertise, safeguard, or evidence input is unavailable, adapt the Method within its admitted variation, choose another, narrow the result, or return a blocker.

Continue only while the selected Method can produce its declared result without concealing the unresolved premise. A deadline may justify a narrower return; it does not justify claiming that an omitted contribution was completed.

#### PSD.6:4.6 - Return the selected Method and limits

| Result position | Content the recipient needs |
| --- | --- |
| Required use | The subject, receiving question, needed result, and current selection conditions. |
| Selected Method | Its reusable action, generic participant meanings, preconditions, intended result, and bounds; enough source content to recover that way of doing. |
| Comparative reason | The serious alternative, the defect or trade-off that changed selection, and the effort accepted. |
| Combination, if needed | Identified part Methods, real dependence or overlap, joins and adapters, whole-level conditions, permitted variation, and failure routes. |
| Reliance limits | What the available source and trial evidence establish, what remains untested, and which direct premises are still required. |
| Reopen basis | A changed result need, participant access, evidence, scope, resource, or failed join that would alter the selection. |

Keep dated assignments and scheduling in the work plan. Record actual enactment and its results separately. A selected Method is neither a commitment by absent participants nor proof that anyone has enacted it.

Supply this result to facilitated inquiry or the reconciliation of simultaneous engagements only where the same situation and qualification window fit. A receiving practitioner still checks the current conditions; Method availability is not fit, enactment, or cultural uptake.

#### PSD.6:4.7 - What changes in practice

The practitioner can explain why this way of working fits, which simpler alternative was considered, and where the arrangement would fail. Adaptation becomes a reasoned change of action and conditions instead of an unexamined mixture of workshop exercises.

### PSD.6:5 - Archetypal Grounding

#### PSD.6:5.1 - Choosing a bounded flood-pump inquiry Method

In this illustrative case, the board needs a pre-season return while service meanings remain contested and the mobile-pump branch depends on unqualified road-access evidence. The current scope and model account make two contributions material: recovering attributed service claims and testing the conditional technical premise.

The author of the engagement design compares three plausible ways:

| Candidate | Contribution and present limit | Selection consequence |
| --- | --- | --- |
| Capacity analysis alone. | Can examine nominal capacity, but cannot recover different service meanings or establish mobile access. | Insufficient for the declared return; retain it only as a bounded technical contribution. |
| A broad facilitated exploration of the whole flood situation. | Can expose more interpretations, but exceeds the pre-season question and available participation time. | Defer the broader inquiry; keep its boundary challenges visible. |
| Attributed mapping joined with conditional access-and-capacity analysis. | Addresses the two discriminating needs, provided attribution can be checked and technical premises have competent sources. | Select the bounded combination with explicit joins and stops. |

The proposed reusable whole is: **for a bounded intervention inquiry with contested service meanings and conditional technical feasibility, contrast attributed service claims with qualified conditional consequences, resolve only the joins needed for the receiving question, and return shared findings and unresolved contrasts without choosing the investment.**

The mapping part elicits, connects, and confirms attributed claims. The analysis part tests named configurations and conditions and reports supported consequences or exact gaps. They can proceed in parallel after the subject and conditions are fixed. Their join accepts only outputs concerning the same intervention, service meaning, and horizon; an unmatched service claim is retained as an unresolved question, not converted to a technical metric.

The whole admits written or spoken elicitation when attribution and challenge remain possible. It does not admit replacing participant confirmation with the sponsor's paraphrase. Its externally usable result is the bounded claim account; internal map-editing steps are not separately promised services. Those action, join, variation, and boundary conditions identify the proposed composite Method for the `A.3.1` and `B.1.5` questions.

For the actual engagement, the team must still arrange participation and obtain the access result. If access cannot be qualified before the return, the Method produces the narrower conditional claim and evidence request. The plan's date and assigned analyst are separate from the reusable Method.

#### PSD.6:5.2 - A failed join rather than a failed workshop

A team proposes transferring the frequency of concerns mentioned in interviews into numerical criteria weights. The mapping Method yields attributed concerns, not preferences under a weighting model. The join fails even if the interviews were well facilitated.

The practitioner either obtains a separately justified elicitation Method and tests its assumptions or keeps the value contrast qualitative. The failed conversion does not invalidate the interviews or authorize invented weights.

#### PSD.6:5.3 - Cheap non-use

An operations team has an agreed question, a current qualified calculation Method, sufficient evidence, and no material participation or interpretation conflict. Use that Method. A new multimethod arrangement adds cost without changing the required result.

### PSD.6:6 - Bias-Annotation

**Scope:** selection and bounded composition of Methods for problem structuring and decision support. **Lenses:** **Prag** tests fitness and effort; **Onto/Epist** separates Method, description, plan, enactment, and evidence; **Arch** exposes real joins; **Gov** preserves participation and authority conditions; **Did** makes the reusable action explicit.

Facilitator-familiarity bias favors the method the team can already run. Brand bias mistakes a school name for an identified way of doing. Integration bias treats more techniques as broader competence. Time-pressure bias hides omitted contributions. Counter these with one serious simpler alternative, a result-based contribution comparison, and the exact fragile premise that could reverse selection.

### PSD.6:7 - Conformance Checklist

- [ ] The selection names the missing result and current subject, scope, conditions, and receiving use.
- [ ] Needed model, participation, expertise, and authority premises are qualified or explicitly missing.
- [ ] Candidate Methods are recoverable reusable ways, not merely titles, descriptions, plans, or reported workshops.
- [ ] A serious simpler alternative and the selected trade-off are explicit.
- [ ] Each additional Method supplies a distinct material contribution.
- [ ] Passed results preserve meaning, scope, and limits; conversions requiring new evidence are not hidden.
- [ ] Real dependence and possible overlap are distinguished from document and calendar order.
- [ ] Any composite-Method claim satisfies the direct whole and part questions; a mere arrangement remains an honest lower result.
- [ ] Fragile premises, allowed variation, failure routes, and local reopen conditions are stated.
- [ ] The result establishes neither actual enactment, participant commitment, effectiveness, nor later choice authority.

### PSD.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “We always run this workshop.” | Recover the required result and compare one serious sufficient alternative. |
| “The agenda is the Method.” | State the reusable action and applicability separately from dated scheduling. |
| “The techniques appear in order, so they compose.” | Test actual dependence, part-Method identity, whole action, and joins. |
| “The qualitative output can be scored numerically.” | Identify the extra elicitation, measurement, or model assumptions; otherwise retain the qualitative result. |
| “The method worked elsewhere.” | Carry the source's subjects, conditions, evidence limits, and actual contribution into this selection. |
| “A shorter deadline removes the need for that input.” | Narrow the declared return or stop; do not mark the missing contribution as completed. |

### PSD.6:9 - Consequences

Selection becomes inspectable and adaptations become easier to challenge. Methods can contribute together without forcing one universal workflow. The cost is a small comparison and join analysis; a genuinely composite Method may require more identification and assurance work. The pattern can therefore return an existing single Method, a bounded composite, or an explicit incomplete selection.

### PSD.6:10 - Rationale

Method fit is relational: it depends on what the engagement needs and what its conditions permit. Complementary labels do not establish complementary results. Recovering reusable actions and their joins explains why the combination can work and what would defeat it, while keeping plans and enacted outcomes separate.

### PSD.6:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| Which PSM contribution fits the engagement? | Compare assumptions, contributions, conditions, and needed outcomes; retain a simpler sufficient route. | A familiar branded PSM is used as a default regardless of the difficulty. | **Adapt:** `PSD.6:4.1`–`4.3` compare actual ways of doing and their limits. A short comparison costs more than automatic selection but is justified when a missing contribution can reverse the return; it does not require a full method catalogue. | Smith and Shaw's [2019 PSM characterization](https://doi.org/10.1016/j.ejor.2018.05.003) is a conceptual comparison candidate that makes differences among approaches inspectable; its exploratory family characterization is not a method-ranking algorithm. Lami and Tavella's [2019 workshop comparison](https://doi.org/10.1016/j.ejor.2018.12.016) supplies bounded counterexample evidence to a uniform-usefulness claim: outcomes varied across SCA, SSM, and self-organized workshops in an exploratory MSc-student study. It establishes no universal winner or professional-field effectiveness. | Reopen when the intended outcome or participation conditions change, or better comparative evidence changes the fit of a serious candidate. |
| When does combining Methods improve the result? | Require a distinct contribution and an intelligible join; qualify a composite Method only when its whole action is recovered. | More techniques, a sequence diagram, or an agenda is treated as an integrated Method. | **Adapt:** `PSD.6:4.4`–`4.6` and the failed-weighting example expose the conversion or missing result. **Adopt:** `A.3.1`, `A.3.2`, and `B.1.5` keep reusable way, description, whole-forming facts, and enactment distinct. Extra join work is accepted only for a material contribution; otherwise the single-Method alternative wins. | Marttunen, Lienert, and Belton's [2017 PSM–MCDA review](https://doi.org/10.1016/j.ejor.2017.04.041) supplies the critical combination line and concrete interface difficulties, not evidence that arbitrary mixtures work. The current FPF patterns supply identity and composition rules, not empirical validation of this engagement Method. | Reopen when a join loses meaning, a part or whole identity changes, a critical precondition fails, or a single Method supplies the same useful result at lower effort. |

### PSD.6:12 - Relations

- `PSD.4` supplies the scope/result frame for the same subject and decision. `PSD.5` supplies model contributions only where they discriminate Method alternatives. Either needed input can be replaced only by a qualified direct result or returned as an exact gap.
- `PSD.7` and `PSD.16` may consume the selected Method and limits for the named situation and qualification window. Availability establishes neither fit nor enactment or cultural uptake.
- `A.3.1.MR` supplies provisional accounts only when several grounded occurrences or direct sources create a reusable-way recovery question and no Method is yet established; `A.3.1` identifies a recoverable proposed way without making that recovery compulsory. `A.3.2` governs a description of one identified Method; `B.1.5` governs the composite qualification when needed.
- `A.15.2` governs intended Work and `A.15.1` actual Work and its enactment relation. Direct competence, participation, authority, evidence, and safety practices govern their own premises.
- This selection can request a missing domain result; it cannot manufacture that result by choosing a better workshop format.

### PSD.6:End


<a id="psd-7"></a>
## PSD.7 - Facilitate Inquiry and Preserve Material Dissent

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** **shared and contested claims without forced identity**: a bounded inquiry return that distinguishes what participants understand, support, reject, or leave unresolved, with attribution, evidence limits, consequences for the receiving use, and a way to reopen material differences.

### PSD.7:1 - Problem frame

**Use this when** participants need to work on a decision-support question but disagree about its meaning, evidence, consequences, or acceptable action. Also use it when a smooth workshop is producing an apparently unanimous answer that participants cannot recognize as their own.

Start by making the inquiry's purpose, participation conditions, challenge route, and later choice boundary clear. Help participants state and test claims in terms their holders can recognize. Return useful common ground and material disagreement; agreement is one possible result, not a condition for an honest return.

The governed object is the bounded account of shared and contested claims for the receiving inquiry. Facilitation is the practical work of enabling that inquiry; the account is its result, not the conversation itself or a decision by the group. Shared wording, shared understanding, assent to a claim, consent to an action, and authority to choose remain different.

**Do not use this pattern** merely to circulate one clear qualified fact, record attendance, or administer an already-valid decision rule when no inquiry or interpretation problem remains. Direct mediation, adjudication, safeguarding, or emergency-command work retains its own remit. If the engagement has no recoverable receiving question or choice owner, return that missing premise.

### PSD.7:2 - Problem

Facilitation can suppress the differences it is meant to make usable. A participant's objection becomes a neutral-looking label, an absent group is treated as represented, and silence is recorded as consent. A model becomes “our view” although participants attach different meanings to it.

The opposite failure is endless disagreement. Every difference reopens the whole discussion, no one distinguishes an evidence gap from a value conflict, and the recipient receives a transcript instead of a result. Productive inquiry needs neither forced consensus nor unlimited debate; it needs a bounded account of what matters and what can be done with it.

### PSD.7:3 - Forces

| Force | Tension |
| --- | --- |
| Participation | The inquiry needs relevant voices, while access, language, hierarchy, time, and safety can limit meaningful contribution. |
| Common ground | Shared understanding can support joint work, while common wording can conceal opposed claims. |
| Challenge | Claims should be open to examination, while criticism can be socially costly or become personal conflict. |
| Closure | A usable return is needed, while unresolved dissent may materially constrain it. |
| Attribution | Readers need to know whose claim is carried, while confidentiality and representation limits constrain disclosure. |

### PSD.7:4 - Solution

Create conditions for participants to express, understand, challenge, and revise claims. Distinguish disagreement by what would resolve it, preserve material differences with their consequences, and return only the agreement and support actually established.

#### PSD.7:4.1 - Recover the inquiry, participation, and Method conditions

Use the current `PSD.2` participation and concern account only for participants, affected Systems, concerns, representation limits, and missing voices material to this inquiry. Use the `PSD.6` engagement Method and limits only for the same situation and qualification window. These inputs help establish what to facilitate; their availability does not show that participation is complete or the Method is being enacted.

Recover the receiving question, intended result, and later choice boundary from the current engagement terms or another qualified direct source. Make clear what this interaction can establish and what remains with the decision owner or a direct specialist.

If an input needed for the result is missing, stale, or incompatible, obtain its qualified direct source or name the precise gap. Do not infer consent, representation, permission, or authority from a participant list, a concern map, or a Method description. An affected System need not have a person present who is entitled or able to represent all its concerns.

#### PSD.7:4.2 - Establish workable participation and challenge conditions

Tell participants what is being asked, how their contribution will be used, how attribution and correction will work, and who will receive the return. Choose channels that permit meaningful contribution and challenge: a joint session, separate conversation, written response, accessible format, or a combination suited to the actual conditions. A workshop is not mandatory.

Make the facilitator's remit and material interests visible. If the facilitator also owns a preferred intervention or controls participants' opportunities, choose safeguards appropriate to that conflict, such as independent handling of a contested claim or a different facilitator. Do not describe the arrangement as neutral merely because the facilitation script is neutral.

Recover any rule governing consent, participation, confidentiality, or later decision from its actual authority. Ask whether the proposed conditions are usable, but do not treat acceptance of the discussion format as assent to its eventual findings. Where credible participation would expose someone to material harm or coercion, use an appropriately protected route, obtain competent support, narrow the claim, or stop that part of the inquiry.

#### PSD.7:4.3 - Elicit and test meaning before merging claims

Ask for concrete statements: what is happening or might happen, to whom, under which conditions, why it matters, and what would change the speaker's view. Show how a contribution has been represented and invite its holder to correct the meaning. When useful, ask another participant to restate the claim and let its holder identify the remaining difference.

Separate observations, reported experience, causal hypotheses, preferences, duties, proposed actions, and commitments. A participant may agree that a claim was represented accurately while disagreeing that it is true or desirable. Keep those answers distinct.

Use models and shared displays to make questions discussable. A new connection or translation remains a proposal until its meaning and evidence are established. If two participants use “reliable service” differently, retain the two meanings instead of selecting a single label for convenience.

#### PSD.7:4.4 - Turn material disagreement into a usable inquiry result

A disagreement is material when it can change a formulation, candidate intervention, consequence claim, value treatment, recommendation, implementation condition, or legitimate receiving use. Preserve at least the disputed claim, its attributed positions, why the difference matters, the current basis, and what could change the next move.

| Difference | Useful facilitation move | Honest remaining result |
| --- | --- | --- |
| Different meanings or scopes. | Recover examples and conditions; test a paraphrase or explicit distinction. | A repaired meaning or two still-distinct readings. |
| Different factual or causal claims. | Identify the evidence, assumption, or discriminating observation required. | A qualified claim, unresolved evidence question, or bounded contradiction. |
| Different values, interests, or priorities. | Make the consequence and trade-off explicit without pretending it is a missing measurement. | Attributed value positions for the later value or choice question. |
| Disputed right, duty, representation, or choice authority. | Obtain the direct competent rule or result. | A supported boundary, exact authority gap, or stop on the disputed use. |
| Different willingness to endorse or commit. | Ask what, if anything, each participant actually supports and on what conditions. | Bounded support, dissent, abstention, or a separately established commitment. |

An objection is neither an automatic veto nor something to erase by a majority count. Its effect follows from the actual claim and applicable decision rule. A vote can establish its own result when authorized; it does not settle truth, all participants' consent, or the legitimacy of an unsupported trade-off.

Continue with unresolved differences when the receiving use can honestly preserve them. If a missing premise prevents that use, return the premise or narrow the result. Do not ask participants to manufacture consensus to keep the engagement on schedule.

#### PSD.7:4.5 - Keep the result faithful without collecting everything

Keep enough attribution and evidence for the recipient to understand and challenge each material claim. Retain the scope of representation: “the association's representatives stated” is different from “residents agreed”. Where a protected contribution cannot be openly attributed, preserve its qualified status and disclosure limit without inventing public endorsement.

A transcript is not normally needed. Reuse a concise claim account, a corrected map, or annotated conclusions. Avoid collecting personal detail that contributes nothing to the receiving question, and do not promise anonymity or confidentiality that the actual arrangements cannot support.

Recognition of a difference needs no formal relation register. If later reliance requires a claim that consent, authorization, representation, or another relation obtains, use that relation's direct pattern and evidence. Use `A.6.REL` only when the receiving use must additionally distinguish occurrences of the same relation kind, including separate episodes with the same participants.

#### PSD.7:4.6 - Close with shared and contested claims

Read back the proposed return at the grain needed for its use. Invite correction of meaning, attribution, support, conditions, and omissions. Record a correction that arrives after the discussion if it materially changes the return; identify which dependent use must reopen.

The recipient should be able to distinguish:

- shared understanding of a statement from support for that statement;
- supported common claims from conditional claims, unresolved evidence, and dissent;
- participants who responded from absent, unreachable, unrepresented, or declining participants;
- proposed action from commitment or authorization; and
- what the inquiry enables now from the direct result still needed.

Use `A.2.9` when the live question is whether the communication enabled a named recipient to understand or do something and what smallest repair is needed. An acknowledgement or later action is not sufficient proof of understanding, consent, or causal effect. Add exact communicative-Work detail only when that stronger reliance is actually needed.

Return the common claims, material disagreements, evidence gaps, their consequences for the receiving question, and the next discriminating question or reopen condition. The account may inform alternative generation, a recommendation, or reconciliation between simultaneous inquiries. It neither chooses the matter nor requires all participants to become one collective viewpoint.

#### PSD.7:4.7 - What changes in practice

The facilitator no longer measures success by a smooth meeting or a unanimous closing slide. The useful result is that participants can recognize how their claims were carried and the recipient can see what is shared, disputed, unknown, and still outside the group's authority.

### PSD.7:5 - Archetypal Grounding

#### PSD.7:5.1 - A flood-pump return that retains disagreement

In this illustrative inquiry, the board's current engagement terms reserve the investment choice to the board. The participation account distinguishes the residents' association from a separately consulted group of mobility-constrained residents; neither represents all district residents. Operations staff supply their current technical assumptions, while the selected Method calls for attributed service claims and conditional technical analysis.

The facilitator presents three proposed conclusions and obtains these corrections:

| Proposed conclusion | What inquiry establishes | Returned claim |
| --- | --- | --- |
| “The pumps can protect the district.” | The technical calculation concerns nominal capacity under stated inflow and availability assumptions. It does not establish deployment access or every resident's protection. | The conditional capacity claim is shared by the responding participants; the broader protection claim is unsupported. |
| “Residents want the least expensive pumping option.” | Association representatives emphasize property protection and cost. The separately heard group asks how assistance remains reachable when roads fail. No complete cost comparison or district-wide endorsement is available. | Preserve the two attributed service concerns; do not claim a common preference or a chosen option. |
| “The mobile branch is acceptable if capacity is sufficient.” | Operations staff cannot yet support its arrival-time premise under the road-loss condition. The mobility concern remains material even if nominal capacity is adequate. | Keep the branch conditional on access evidence and retain the service disagreement for alternatives and recommendation. |

The result says: “There is a shared conditional reading of nominal capacity, not shared endorsement of an investment. The mobile branch has an unresolved access premise. Property-protection and reachable-assistance concerns remain separately attributed. The board receives these claims and gaps; the inquiry has made no investment commitment.”

The facilitator sends the wording back through the available channels for attribution correction. Missing replies remain missing replies. A later verified access result can close that technical question without resolving the value difference; a participant's corrected service meaning reopens only the affected claim and its downstream use.

#### PSD.7:5.2 - A manager's summary is not a team's consent

A manager proposes a development direction and asks staff to comment in a meeting where dissent could affect their assignments. Silence is not an adequate basis for “the team supports the plan”.

The facilitator offers an appropriately protected response route or a separately facilitated discussion and states its real disclosure limits. Until usable participation is possible, the return reports the manager's proposal and the limitation on staff input. It does not fabricate agreement, infer hidden opposition, or undertake specialist safeguarding work without its proper support.

#### PSD.7:5.3 - Cheap non-use

Two analysts agree on a clarified unit conversion and only need the corrected value in their calculation note. Send the qualified correction and confirm the needed understanding. A new facilitated inquiry or dissent register adds no useful result.

### PSD.7:6 - Bias-Annotation

**Scope:** facilitated inquiry that supports a bounded receiving decision without owning it. **Lenses:** **Gov** separates participation, representation, consent, and choice; **Onto/Epist** separates claim meaning, support, evidence, and occurrence; **Prag** seeks usable closure; **Arch** preserves dependencies on unresolved claims; **Did** makes contested meanings recognizable.

Consensus bias treats a quiet room as a successful outcome. Sponsor bias gives one formulation privileged status. Attribution bias extends one representative's statement to a population. Conflict-avoidance bias weakens an objection until it no longer changes the result. Counter these by checking the exact proposed return with its holders and preserving each material disagreement's practical consequence.

### PSD.7:7 - Conformance Checklist

- [ ] The inquiry's receiving question, intended result, and later choice boundary are recoverable.
- [ ] Needed participation and Method inputs fit the present situation and qualification window, or their exact gaps are returned.
- [ ] Participation, correction, challenge, attribution, and disclosure conditions are usable rather than merely announced.
- [ ] The facilitator's material interests and limits are visible.
- [ ] Shared meaning, claim support, factual evidence, value preference, consent, and authority remain distinct.
- [ ] Material dissent retains attribution, basis, consequence, and a discriminating question or reopen condition.
- [ ] Absence, silence, abstention, and representation limits do not become agreement.
- [ ] Direct relation claims receive their own assurance; an occurrence register is not compulsory.
- [ ] The return is concise enough to use and precise enough for participants to challenge.
- [ ] Closure neither invents a decision nor conceals a premise that prevents the receiving use.

### PSD.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agreed with the slide.” | Ask which meaning and claim each response actually supports. |
| “No objection means consent.” | Recover the participation conditions and any applicable consent rule; otherwise report only the observed response. |
| “The representative speaks for everyone affected.” | Carry the actual representation basis and limits. |
| “Keep dissent in the transcript; simplify the recommendation.” | Preserve every disagreement that can change the receiving recommendation or its conditions. |
| “Every objection blocks progress.” | Distinguish its consequence under the actual evidence, authority, and decision rules. |
| “A neutral script makes the facilitator neutral.” | Expose material interests and choose an appropriate safeguard or facilitator. |

### PSD.7:9 - Consequences

The receiving practitioner obtains usable common ground without losing the disagreements that can reverse a decision-support claim. Evidence questions, value conflicts, and authority gaps can take different next routes. The cost is explicit correction and dissent handling, and sometimes a narrower return when meaningful participation is unavailable.

### PSD.7:10 - Rationale

Facilitation helps people make claims and differences inspectable; it does not make their meanings, interests, or authority identical. Bounded closure works when the result says what further work can rely on and where reliance must stop. This can preserve disagreement while still enabling a concrete next move.

### PSD.7:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can facilitation make different meanings usable? | Attend to the actual interaction: elicit concrete contributions, test formulations with participants, and revisit how the developing model carries their meanings. | Following a workshop script or completing a shared diagram is treated as sufficient evidence of common understanding. | **Adapt:** `PSD.7:4.2`–`4.3` and `4.6` add targeted meaning and attribution checks within the same interaction. The extra attention is accepted for a material difference, without requiring a full recording or research study. | Franco and Greiffenhagen's [2018 facilitated-modeling analysis](https://doi.org/10.1016/j.ejor.2017.08.016) supplies a bounded empirical account of situated OR practice, not a universal script. Zimmermann and Curran's [2023 microlevel study](https://doi.org/10.1002/sdr.1743) supplies the more specific candidate line on facilitator questions, references to contributions, and recursive development of shared meaning in one heritage-science workshop. Neither establishes universal transfer, consensus, or causal effectiveness for every engagement. | Reopen when participants cannot recognize the returned meaning, the channel suppresses material contributions, or stronger comparative practice supplies the same fidelity with less effort. |
| How should inquiry close when disagreement remains? | Return attributed common claims, material dissent, and the exact missing evidence or authority result. | A unanimous summary is manufactured, or all disagreement postpones every useful return. | **Adapt:** `PSD.7:4.4`–`4.6` and both substantive cases separate meaning, support, truth, consent, and choice. This accepts a less simple summary in exchange for preserving an action-changing difference; an already-clear factual correction takes the cheap exit. | Current `A.2.9` supplies receiving-use judgement and the distinction between communication, response, achievement, consent, and authority. Current `A.6.REL` supplies occurrence distinction only when needed; direct predicates and evidence establish obtaining relations. Retaining material dissent is the PSD solution constraint for contested decision support, not an empirical claim that disagreement always improves decisions or grants a veto. | Reopen when a direct rule changes the effect of dissent, new evidence resolves a disputed claim, attribution is corrected, or the receiving use can no longer preserve the unresolved difference honestly. |

### PSD.7:12 - Relations

- `PSD.2` supplies the current participation and concern account only where it is material to the inquiry. `PSD.6` supplies the engagement Method and limits only for the matching situation and qualification window. Needed missing inputs return to qualified direct sources or exact gaps.
- `PSD.8` may use this inquiry result where it changes the candidate set; agreement is not required and material dissent stays explicit.
- `PSD.13` and `PSD.16` may use the participation and dissent account to preserve material agreement and disagreement in a recommendation or simultaneous-inquiry decision. The account grants no choice authority.
- `A.2.9` governs a communication's receiving-use question and any stronger communicative-Work claim. Direct patterns govern actual consent, representation, permission, duty, and authority; `A.6.REL` adds occurrence identity only for a need to distinguish same-kind occurrences.
- Direct evidence, causal, value, legal, safety, safeguarding, and governance practices answer their own substantive questions. Facilitation can expose their missing results but cannot replace them.

### PSD.7:End


# Part III — Alternatives, Values, Uncertainty, Consequences and Robustness

<a id="psd-8"></a>
## PSD.8 - Generate Decision Alternatives

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** a finite **candidate set** for one decision-support question, with materially different alternatives, their supported and unresolved premises, and the exact candidate gaps that still matter.

### PSD.8:1 - Problem frame

**Use this when** an inquiry has clarified what matters but the proposed decision still contains only the incumbent, a sponsor's preferred project, or two labels such as “buy or build”. Also use it when a request for development advice names a course, provider, reorganization, or AI tool before the possible directions have been constructed.

Start by asking what different action could address each live formulation or concern. Change the mechanism, arrangement, combination, timing, or commitment being considered, then state enough of each resulting alternative for a fair consequence comparison. The practical gain is a choice worth examining, including an honest gap when no supported alternative is available.

The governed object is the candidate set, not a selected action. A candidate describes a possible intervention or commitment; its description does not establish feasibility, permission, performed Work, or benefit. Alternatives may address competing formulations rather than obtain exactly the same result. Preserve that difference instead of inventing parity.

**Do not use this pattern** when an adequate finite set already exists and only comparison or an authorized choice remains. Use the direct domain practice when it already owns the complete alternative-generation question. A population or lineage without a population-local recipient or chooser is not a recipient of development advice; an authorized researcher's intervention is a different decision-support case.

### PSD.8:2 - Problem

An apparently open choice can be closed before analysis begins. A list of pump models omits deployment arrangements; a list of training courses omits changing the Work that prevents capability expression; a list of AI models omits the tool, data, or operating configuration responsible for the failure.

Unrestricted ideation creates the opposite difficulty. Hundreds of names can repeat the same intervention, depend on unsupported capacities, or combine benefits that cannot coexist. Novelty does not make an alternative useful, and an attractive candidate does not become admissible because it survived a workshop.

### PSD.8:3 - Forces

| Force | Tension |
| --- | --- |
| Breadth and relevance | A different mechanism may expose a better direction, while an unbounded search consumes the decision horizon. |
| Plural formulations | Alternatives should address material interpretations without pretending that every interpretation seeks the same result. |
| Imagination and qualification | A proposal may be worth investigating before feasibility is known, while unsupported proposals cannot be presented as ready commitments. |
| Combination and interaction | Hybrid or staged directions can preserve options, while shared resources, incompatibilities, and delay can remove their apparent advantage. |
| Generation and choice | Early preference helps identify concerns but can suppress candidates before their consequences are known. |

### PSD.8:4 - Solution

Construct alternatives from the live decision question and useful differences in the inquiry. Make each candidate complete enough for its next use, separate qualification gaps from rejected directions, and stop with a bounded set or a precise missing-alternative result.

#### PSD.8:4.1 - Recover the receiving question and useful inputs

Name the recipient, holder or subject, horizon, current arrangement, later choice owner, and the commitment being considered. Recover the protected conditions and resource bounds that can change which alternatives are live. If the request still has no recoverable question or authority boundary, return that missing premise rather than inventing a development programme.

Use a `PSD.3` formulation set only where its differences suggest different interventions. A formulation is not itself an action. Use the `PSD.5` model account only where a model discriminates candidate mechanisms or exposes an omitted consequence. Use `PSD.7` inquiry results where a shared or contested claim changes the alternatives; agreement is not required.

These are conditional contributions. Use a qualified direct result when it supplies the same needed premise. If the needed input is absent, stale, or incompatible with this subject and horizon, retain the precise gap. Neither adjacent PatternIDs nor a completed workshop supplies an alternative by itself.

#### PSD.8:4.2 - Vary the decision-changing contents

Ask what the proposal is meant to achieve, why that result matters, and what other way could address the concern. Generate some ideas independently before group discussion when early advocacy could anchor the whole inquiry. Then use differences and objections to construct additional candidates.

Useful prompts include changing the intervention mechanism, obtaining arrangement, scale, timing, resource allocation, or commitment. Consider combining compatible actions, retaining the present arrangement, declining a proposed change, and obtaining information before a larger commitment. These are prompts, not a mandatory taxonomy or a required number of options.

Describe “no new action” against a real baseline. It may still include already authorized maintenance, contractual duties, continuing costs, deterioration, or exposure. It is not a cost-free, consequence-free empty world.

For a staged direction, say what happens first, what later choice remains open, which observation could inform it, and what delay or irreversibility the first commitment introduces. Do not call a probe reversible merely because it is small; obtain the direct feasibility, consent, safety, and recovery premises when they matter.

#### PSD.8:4.3 - Turn labels into sufficiently complete candidates

For each material alternative, state the proposed change from the current arrangement, affected subjects, intended result, enabling conditions, major burdens, evidence basis, and unresolved premise. Distinguish what is supported now from what is proposed or unknown.

Use `C.38` only when several whole ways are intended to make the same receiving result available and labels still hide their different burdens. If the alternatives seek different results, retain the difference and let the decision-support comparison expose it. Do not force a same-result declaration merely to obtain a neat table.

A combination is another candidate when its interactions can change consequences. Check shared staff, facilities, money, dependencies, sequencing, and incompatible assumptions. Two independently attractive components do not establish an attractive combined arrangement. A provider's advertised capability, a course title, or a benchmark score is not a qualified result for this holder.

#### PSD.8:4.4 - Distinguish exploration from a live commitment option

Keep a promising but unresolved proposal available for inquiry without presenting it as an admissible commitment. A short annotation is enough: “comparison-ready within these conditions”, “requires this qualification”, or “excluded for this stated reason”. These phrases describe the present use; they create no new universal status system.

Inspect an adequate existing specialist result before requesting more. Where a decision-changing cross-practice gap remains, use `A.15.9` to request that exact feasibility, allocation, transfer, security, or other result. A missing result may block one branch while others remain useful.

Use `C.17` when a claim about novelty, diversity, or usefulness of the named candidates needs characterization. Use `C.18` when open-ended generation, archive, or front stewardship is actually needed. Neither characterization nor archive membership chooses the decision alternative. Use `C.19` only for an actual live-pool policy question; thin evidence alone supplies no default exploration policy.

#### PSD.8:4.5 - Challenge coverage and stop proportionately

Ask whether the set still reflects only one favored formulation, one available technology, or one powerful participant's concern. Check whether a materially different mechanism, genuine no-change case, compatible combination, or bounded probe was omitted without reason. Merge labels that have the same decision-changing contents; retain differences that alter consequences or supported use.

Stop when the set is sufficient for the present comparison: material formulation differences have an addressed candidate or an explicit gap, each retained row is intelligible, protected-condition exclusions are visible, and additional search has no identified benefit worth the remaining effort. This is bounded sufficiency, not proof that all possible alternatives have been found.

If only one lawful direction survives, report that fact and its basis without manufacturing a rival. If none survives, return the missing qualification, infeasible requirement, or need to reopen the problem. A gap is a useful result; a decorative list is not.

#### PSD.8:4.6 - Return the set without making the choice

Return the question, subject and horizon; the exact candidate contents; their material differences; supported conditions and remaining gaps; excluded branches and reasons; and the observation that would add, remove, or change a candidate. Use the smallest readable form that lets another practitioner reconstruct those distinctions.

`PSD.11` may use this set as the alternatives for its named consequence comparison. The comparison must still establish its own value, evidence, and scope basis. A generation result supplies no ranking, recommendation, authorized choice, programme, WorkPlan, or effect.

### PSD.8:5 - Archetypal Grounding

#### PSD.8:5.1 - Flood-pump alternatives beyond a purchase contest

In this illustrative case, the board needs a pre-season return for the next flood season. The inquiry distinguishes nominal capacity, deployment reliability, unequal service, and downstream consequences. The model account says that nominal permanent and mobile capacity can meet the assumed inflow when the stated units are operating, but mobile arrival under road loss is not yet supported. Reachable assistance remains a separate service concern.

The inquiry turns those premises into four candidate descriptions:

| Candidate | Different action being considered | Present use and gap |
| --- | --- | --- |
| N — continue the present arrangement | Keep already authorized operation and maintenance; make no new capacity commitment. | A real baseline for comparison, not an assumption of adequate service or zero cost. |
| F — fixed-capacity change | Add fixed capacity with the necessary operating, staffing, and support arrangement. | A proposed whole change; direct engineering and service results must qualify its consequences. |
| M — mobile-reserve arrangement | Obtain mobile capacity together with its transport, deployment, staffing, and access arrangement. | Retained for inquiry; the road-loss deployment premise prevents an unconditional commitment claim. |
| S — staged combined direction | Make a bounded initial change and preserve a later capacity choice after a discriminating access or service inquiry. | A distinct candidate only if temporary provision, resource overlap, delay, and recovery can be qualified. It is not F plus M with their benefits added. |

The property-protection and reachable-assistance concerns remain distinct. They lead the team to ask whether each whole arrangement serves both; they do not establish an approved priority between them. No candidate is dropped because its proponent dissents from the majority.

The returned set is N, F, M, and S with those limits. If the current use requires commitment-ready options and M or S lacks a necessary premise, the return names that blocked branch. It does not hide the branch or call the remaining set exhaustive.

#### PSD.8:5.2 - A ninety-day development-direction question

An advisory team is asked which direction a service organization should consider for a ninety-day reliability horizon. “Train, outsource, or use AI” is not yet a set of comparable directions. The adviser resolves the labels into internal development with covered service duties, a qualified provider arrangement, and a mixed human–tool arrangement with specified oversight and fallback. A bounded mixed-arrangement probe is a separate candidate when its information and operating consequences differ from deployment.

Each branch needs its own supplier result. Human capability evidence does not establish transfer to the representative later Work; provider evidence does not establish interface or security fit; model evaluation does not establish reliability of the mixed arrangement. If the organization-allocation comparison is missing, return that exact gap rather than ranking the three labels.

For advice about one person, the same move generates directions only from qualified human and target-Work premises. For an AI arrangement, it distinguishes parameter, data, scaffold, tool, code, and environment changes only where the case makes those objects live. Neither application imports the other's mechanism or evidence.

#### PSD.8:5.3 - Cheap non-use

A recipient already has two complete, qualified ways of obtaining the same repair result and asks which to choose. Use the existing set and the applicable comparison or `C.11` choice guidance. Another brainstorming exercise adds no candidate-changing result.

### PSD.8:6 - Bias-Annotation

**Scope:** alternatives for bounded decision-support engagements. **Lenses:** **Prag** tests useful differences; **Onto/Epist** separates proposed arrangements from facts; **Arch** exposes combinations and dependencies; **Gov** preserves protected conditions and later authority; **Did** replaces label lists with intelligible candidates.

Incumbency, sponsor anchoring, technology availability, and novelty bias can each shrink or distort the set. Challenge the omitted mechanism and baseline, not merely the number of ideas. Counter the opposite bias toward endless variety by asking what additional candidate could actually change the present comparison.

### PSD.8:7 - Conformance Checklist

- [ ] The recipient question, holder or subject, current arrangement, horizon, and separate choice boundary are recoverable.
- [ ] Formulations, models, and inquiry claims contribute only where they change the candidates.
- [ ] Alternatives differ in decision-changing contents, not merely names.
- [ ] The no-change case includes its actual continuing obligations and consequences.
- [ ] Combinations and staged directions expose interactions, delay, and unresolved enabling conditions.
- [ ] Supported, proposed, and unknown premises remain distinguishable.
- [ ] Qualification gaps and excluded branches have exact reasons; missing alternatives are not fabricated.
- [ ] The stopping point states bounded sufficiency, not exhaustive search.
- [ ] The returned set permits a later comparison without asserting selection, authority, Work, or benefit.

### PSD.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Score the sponsor's option against “do nothing”. | Recover a real baseline and a materially different mechanism or explain why none is live. |
| Treat buy, provider, AI, and internal as peer kinds. | Describe the proposed whole arrangements and their receiving results. |
| Exclude a proposal because feasibility is unknown. | Keep the inquiry candidate separate from commitment eligibility and name the missing result. |
| Add component benefits to justify a hybrid. | Qualify the combined configuration and its interactions. |
| Treat novelty or archive membership as selection. | Use the characterization or archive result only for its stated function. |
| Generate forever because the set is not exhaustive. | Stop at the bounded comparison need and retain a specific reopen condition. |

### PSD.8:9 - Consequences

The recipient gets a genuinely wider but finite decision question, with candidate gaps visible before scoring. The cost is some additional construction and qualification effort. Concentrate it on omitted differences that could change the decision; do not describe every possible arrangement in equal detail.

### PSD.8:10 - Rationale

Structured inquiry becomes useful to choice when its differences change what can be done. Alternative construction preserves those differences while qualification prevents imagination from becoming an unsupported commitment. Keeping generation separate from comparison permits a promising proposal to remain investigable without calling it a winner.

### PSD.8:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can an engagement escape the incumbent without producing a decorative idea list? | Use objectives and materially different mechanisms to guide alternative construction. | Unstructured group brainstorming is cheap; a supplied option menu is cheaper still. | **Adapt:** :4.1–:4.3 add concern-led prompts and independent generation where anchoring matters. The deliberate cost is a short construction pass before comparison; an adequate existing set takes the cheap exit. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023), especially its value-focused-thinking discussion, is a current synthesis candidate. Keeney's [2012 value-focused brainstorming](https://doi.org/10.1287/deca.1120.0251) supplies the specific objective-led and individual-before-group procedure. Its policy example is not universal effectiveness evidence. | Reopen if a simpler elicitation gives the same material breadth or the objectives themselves suppress a live formulation. |
| When is a staged alternative genuinely different? | Preserve options only through explicit dependencies, observations, and feasible later changes. | Compare only fixed end-state projects, or label an underspecified pilot “adaptive”. | **Adapt:** :4.2–:4.4 and candidate S require a qualified first commitment, later question, and delay or lock-in consequence. Additional description is justified only when timing changes the comparison. | The [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) is the best-known-line candidate for pathway dependencies and failure conditions; its water-policy applications do not supply PSD's local thresholds, authority, or universal sequence. | Reopen when monitoring, lead time, or reversibility makes the staged direction infeasible or no longer distinct. |
| Does a novelty result already supply the alternatives? | Keep characterization, generation stewardship, and local choice separate. | Read a novelty profile or archive as a ready option set. | **Adopt:** :4.4 uses C.17 and C.18 only for their actual objects; :4.6 retains the PSD candidate result. This avoids reconstructing machinery when ordinary candidate descriptions suffice. | Current `C.17` characterizes bounded novelty or use; `C.18` governs generation, archive, and front stewardship; `C.38` forms same-result ways. Their exact boundaries defeat the broader reading, but none supplies holder feasibility. | Reopen only if a direct contribution or the receiving candidate question changes. |

### PSD.8:12 - Relations

- `PSD.3` supplies formulation differences for candidate formation, not selected actions. `PSD.5` supplies discriminating model claims, not the obtaining conditions they represent. `PSD.7` supplies shared and contested inquiry claims only where they change the set; dissent remains explicit.
- `PSD.11` may consume the candidate set for the same named comparison. It establishes its own comparison result; generation does not select.
- `C.17`, `C.18`, `C.19`, and `C.38` supply characterization, generation stewardship, live-pool policy, and same-result construction only under their own use conditions.
- `A.15.9` supplies an inspect-use-or-request move for a material outside-practice gap. Direct holder and domain practices supply feasibility, mechanisms, protected conditions, and evidence.
- `C.11` governs the later local choice over an adequate option set. A missing or incompatible input returns to its qualified direct source or remains an exact gap; no neighboring body is a compulsory prerequisite.

### PSD.8:End


<a id="psd-9"></a>
## PSD.9 - Represent Values and Trade-Offs

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** a **decision-usable value account**: attributed concerns and objectives, their consequence measures, protected conditions, admitted trade-offs, unresolved disagreements, and limits for one named comparison.

### PSD.9:1 - Problem frame

**Use this when** a scorecard's criteria came from a template, “importance” weights have no stated meaning, or the same benefit appears under several headings. Also use it when people agree that reliability, development, safety, or fairness matters but mean different consequences for different subjects.

Begin with one concern: important to whom, about which subject and situation, and why? Trace it to a consequence that could distinguish the live alternatives. Then state how that consequence will be represented and whether it may be traded against another. The gain is a comparison whose value assumptions can be understood and challenged.

The governed object is the value account for that comparison. An objective expresses what is wanted; a measure describes a characteristic; a preference orders consequences; a protected condition limits permissible trade-offs. They can be related without becoming the same thing. Neither an expressed preference nor a numerical weight supplies authority to waive a duty or another person's rights.

**Do not use this pattern** when a current, qualified value account already answers the exact comparison question. Use the direct measurement practice for a missing measurement alone, the appropriate authority or domain practice for a binding condition, and the authorized choice owner for the later decision. This pattern does not determine universally correct values.

### PSD.9:2 - Problem

Criteria can appear neutral while deciding the result. “Install more pumps” embeds an action in an objective. “Service quality” may count the same avoided outage again under reliability, satisfaction, and reputation. Equal weights may silently favor the concern represented by the largest number of criteria.

Numbers can conceal a second substitution. A budget amount, a probability, an ordinal judgement, and a protected condition become interchangeable entries in a spreadsheet. Normalizing each to zero–one does not establish comparable value. A mean of participants' weights can erase a disagreement about who bears the consequence or what may be traded at all.

### PSD.9:3 - Forces

| Force | Tension |
| --- | --- |
| Completeness and usability | Material values must remain visible, while an enormous hierarchy burdens elicitation and repeats consequences. |
| Measurement and meaning | Observable measures help comparison, while easily measured proxies can displace the actual concern. |
| Trade-offs and protection | Some sacrifices are legitimate within the question; others require a separate authority or are outside permissible compensation. |
| Individual and collective values | A common comparison is useful, while unlike participants need not share one value function. |
| Precision and honest incompleteness | Explicit scales and preference questions can clarify a choice, while unsupported weights create false precision. |

### PSD.9:4 - Solution

Recover the values behind the decision, organize them around consequences, and declare only the measurement and trade-off structure that the receiving comparison can support. Keep unresolved preferences and protected conditions visible rather than completing a score by assumption.

#### PSD.9:4.1 - Recover whose concern changes the comparison

Name the subject, affected people or Systems, configuration, horizon, and receiving question. Use `PSD.2`'s participation and concern account where it supplies relevant attributed concerns, duties, interests, missing voices, or representation limits. That input is not already a value model or a mandate to aggregate preferences.

For each material concern, ask who expresses or bears it, what consequence matters, and under what conditions. Recover an actual assignment, local system-role classification, or authority relation only where the concern's meaning or governing force depends on it. A title such as resident, manager, or expert does not establish representation or decision rights.

If a needed concern or binding condition is unavailable, use a qualified direct source or return the exact gap. Do not treat non-response as indifference. Distinguish participants' current statements from the analyst's proposed interpretation and from an established obligation.

#### PSD.9:4.2 - Distinguish ends, means, and repeated consequences

Ask “Why does this matter here?” to identify the consequence sought. Ask “How might it be achieved?” to expose possible means. “Provide training” may be one means; reliable performance in representative later Work may be the relevant end. The distinction is local to the question: a process experience can itself be valued when participants actually care about it.

Organize objectives only as far as the structure helps. For a small decision, a few attributed statements may be enough. A hierarchy or means–ends map is useful when several levels or overlaps would otherwise be lost.

Test apparent duplicates through their meaning and consequence path. Avoid counting one consequence twice under different names. But statistical correlation alone is not duplication: service loss and distribution of that loss can remain different values even when their observed measures covary. Conversely, statistical independence does not prove that a preference model may add the values.

Retain an objective only if it represents a material value, protected condition, or decision-changing distinction. When simplifying, state the lost distinction and check that it cannot reverse the intended comparison. Do not delete a concern merely because it is difficult to measure.

#### PSD.9:4.3 - Give each measure a usable meaning

For every consequential measure, state the characteristic, subject or participant tuple, scale and unit where applicable, direction of preference, horizon, source, and missingness rule. Distinguish a direct measure from a proxy and say what the proxy cannot establish.

Use `C.16` for measurement and `A.19` when a declared multi-characteristic space or reusable predicate is needed. A.19 supplies coordinate and scale meanings; it does not perform scoring, aggregation, comparison, or selection. A number missing its subject or scope is not repaired by placing it in a common column.

Keep raw consequence descriptions alongside any value transformation that the comparison uses. A performance scale and a value scale answer different questions. If an ordinal judgement is used, preserve its ordering without assuming equal intervals or averaging categories. If a numerical value function is used, state the consequence range, anchors, interpolation or shape, and the elicitation basis that makes the transformation meaningful.

#### PSD.9:4.4 - Separate conditions from compensable objectives

Identify which conditions are binding, which are aspirations, and which are uncertain claims requiring a competent result. Record the source and use of each condition. A participant's request for a minimum service level is a value claim; a separately established legal or safety requirement has its own governing basis.

Do not compensate for a failed protected condition by adding benefits elsewhere. If its meaning, applicability, or authority is disputed, retain that dispute and ask for the exact interpretation rather than choosing a convenient threshold. A comparison may proceed on an explicitly narrower slice while the whole-decision conclusion remains blocked.

Some thresholds are preference choices rather than prohibitions: an aspiration level, budget preference, or tolerated inconvenience. Say which they are and whose judgement they express. A threshold crossing is not automatically a decision or permission to act.

#### PSD.9:4.5 - Elicit trade-offs over consequences, not criterion labels

Before assigning weights, ask which concrete consequence profiles the value holder prefers and why. For an additive value model, a weight concerns the value of an improvement over a stated consequence range, not the abstract importance of the criterion's name. Changing that range can require elicitation again.

Test whether a proposed compensatory model fits the expressed preferences. If one consequence's value depends on another, retain that interaction or use a suitable model. If a participant refuses the trade-off, do not encode refusal as an extreme but negotiable weight unless that faithfully represents the judgement.

Several forms can be useful: qualitative preference statements, a priority order, threshold rules, an additive or non-additive value model, or an outranking relation that can preserve incomparability. Choose the least burdensome form that preserves the decision-changing distinction. The domain Method supplies its elicitation and validity conditions; naming MCDA does not satisfy them.

Keep each materially different value account attributable. A common account requires an explicit and legitimately governed way to combine or reconcile the judgements. Voting, averaging, or a sponsor's preference is not a default aggregation rule. Where several preference models remain compatible with the expressed judgements, retain that family rather than fitting one arbitrary point estimate.

#### PSD.9:4.6 - Return the account and its exact incompleteness

Return the attributed concerns and objectives; consequence meanings and measures; protected conditions and their sources; admitted trade-offs or preference relations; material interactions and dissent; unsupported transformations; and what would change the account.

`PSD.11` may use it only for the named comparison. The account can support a partial order or leave a comparison unresolved. Missing preference information is not automatically missing empirical evidence: a further experiment may estimate consequences without deciding how they should be valued.

Recognition needs only a material ambiguity, duplication, or unexplained trade-off. Consequential reliance additionally needs qualified measurements, faithful elicitation, a justified aggregation Method when used, direct authority for binding conditions, and the applicable domain assurance. A readable value table satisfies none of those stronger claims by itself.

### PSD.9:5 - Archetypal Grounding

#### PSD.9:5.1 - Two meanings of flood service

In the illustrative flood-pump engagement, a residents' association emphasizes property protection, while a separately heard group of mobility-constrained residents emphasizes reachable assistance. The board is the later choice owner, not an assumed representative of every value judgement.

The analyst replaces a generic “service quality” score with this account:

| Concern | Consequence representation | Trade-off or qualification boundary |
| --- | --- | --- |
| Reduce property loss. | A qualified loss estimate for the affected properties and flood conditions. | The estimate is not evidence of reachable assistance; its valuation and uncertainty remain explicit. |
| Keep assistance reachable. | Whether the defined assistance service can reach the named population under the relevant access conditions. | The expressed concern is retained. Any binding access or safety condition needs its direct competent basis; it is not inferred from participation. |
| Maintain pumping service. | Hours of unavailability for the specified pumping service over the season. | This operational measure does not cover all property or human consequences. |
| Limit resource use. | Resources required by each whole arrangement, including continuing obligations and transition. | A cost preference does not permit violation of a separately established protected condition. |

The analyst removes a second “reliability benefit” entry that merely repeats the same pumping-service hours. Reachable assistance stays separate even if failures often occur in the same storms. That is not duplicate value.

If the board adopts a trade-off between operating-service hours and budget units for a narrow analytical slice, the account names that value judgement, range, and limit. It does not present the slice as the residents' common value function. If the association and the other group reject a common trade-off, the return carries separate accounts and a stated disagreement; another hydraulic simulation cannot resolve that disagreement.

#### PSD.9:5.2 - Development directions do not share a universal improvement score

For the ninety-day service-organization case, a qualified strategy result gives reliability priority over throughput for the current horizon. That premise helps frame the comparison but does not supply numerical weights or a causal effect estimate.

| Proposed holder-specific input | What the value account may use | What it must not infer |
| --- | --- | --- |
| Human capability result for representative later Work. | The supported performance distinction and the person's relevant protected conditions. | Course attendance, assessment performance, retention, and transfer are not one interchangeable development value. |
| Organization result for positions, interfaces, and continuing service. | Contribution and service consequences for the named arrangement. | A local team's gain is not automatically a gain for the organization or another team. |
| AI/model evaluation for a named version and environment. | The qualified performance, resource, oversight, and failure distinctions. | A benchmark percentage is not a person's capability measure or the whole service's reliability. |

The adviser keeps those premises in their own meanings. A common service-level comparison is possible only after qualified domain results connect each direction to that same service and horizon. Without that connection, “human 4, organization 4, AI 4” is not a meaningful equal score. The return requests the missing consequence relation rather than normalizing the three numbers.

#### PSD.9:5.3 - Cheap non-use

Two qualified replacement parts have the same relevant consequences except for a directly comparable resource cost, and the authorized recipient's cost preference is already explicit. Reuse that account. An objectives hierarchy and a fresh weighting workshop would add no value distinction.

### PSD.9:6 - Bias-Annotation

**Scope:** value representation for one bounded comparison. **Lenses:** **Onto/Epist** separates concern, measure, preference, and obligation; **Prag** preserves decision relevance; **Gov** exposes representation and authority; **Did** makes trade-offs concrete.

Template bias imports irrelevant criteria. Proxy bias rewards what is easy to count. Splitting one objective into many criteria can change its apparent importance. Sponsor averaging can conceal who bears a loss. Counter these by returning to attributed consequences, inspecting overlaps, and retaining disagreement and missingness. Do not replace one template with a mandatory elaborate hierarchy.

### PSD.9:7 - Conformance Checklist

- [ ] Values are attributed to the relevant subjects and receiving comparison, with representation limits intact.
- [ ] Objectives and possible means remain distinct at the grain that changes the decision.
- [ ] Repeated consequences are not counted twice; correlation alone does not justify deletion.
- [ ] Measures retain subject, scale, unit, horizon, evidence, proxy limits, and missingness.
- [ ] Binding conditions, aspirations, and unresolved authority questions are distinguished.
- [ ] Value transformations and weights have declared ranges and an elicitation basis.
- [ ] Interactions and refusals to compensate are preserved.
- [ ] Any collective aggregation has an explicit basis; incompatible accounts remain visible otherwise.
- [ ] The return states partiality, dissent, direct-source gaps, and exact reopen conditions.
- [ ] A value account is not a comparison result, authorization, or claim of effect.

### PSD.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agrees safety is important, so give it twenty percent.” | Recover the actual condition, its source, and whether compensation is permitted. |
| “Equal weights are neutral.” | State the consequence ranges and inspect how criterion splitting changes the result. |
| “These two measures correlate, so one is redundant.” | Examine whether they represent the same valued consequence. |
| “Normalize everything to zero–one.” | Establish value meaning and admissible operations before any transformation. |
| “The workshop mean is the public preference.” | Preserve attribution and require an explicit aggregation basis. |
| “Collect more data to resolve the value dispute.” | Identify whether the missing input is evidence, preference, representation, or authority. |

### PSD.9:9 - Consequences

The comparison becomes open about what it values and what it cannot exchange. Simplifying the account can reduce burden without losing material distinctions. Some decisions remain partially ordered or disputed; that is a truthful result, although it may be less convenient than a single score.

### PSD.9:10 - Rationale

Value representation makes consequences decision-relevant without confusing description with preference or preference with permission. Concrete trade-off questions expose assumptions hidden by criterion labels. Preserving multiple admissible accounts lets later comparison show where a conclusion is shared and where it depends on a disputed judgement.

### PSD.9:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can objectives be concise without omitting what matters? | Inspect means–ends structure, relevance, overlaps, and sensitivity to simplification. | Retain an exhaustive descriptive hierarchy, or delete criteria by correlation alone. | **Adapt:** :4.2–:4.3 keep a small consequence-led account and test any lost distinction. More analyst attention is accepted where it prevents double counting; small clear cases remain short. | Marttunen et al.'s [2019 objectives-hierarchy study](https://doi.org/10.1016/j.ejor.2019.02.039) supplies the comparative methods and retrospective environmental cases. It supports disciplined simplification, not one optimal hierarchy or a statistical license to discard values. | Reopen when a removed distinction can reverse the comparison or a lighter structure preserves the same concerns. |
| Must incomplete preferences become one weighted score? | Match the preference model to the available judgements and preserve a family of compatible models when necessary. | Fit a single additive model or average participants' weights for convenience. | **Adapt:** :4.4–:4.6 retain protected conditions, explicit compensation assumptions, and distinct value accounts. The accepted trade-off is a possibly less decisive result for less invented precision. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) compares preference information, models, and recommendation forms, including robust ordinal regression. It is a best-known-line candidate for model–information fit, not evidence of a universally correct value system. | Reopen if new elicitation narrows the compatible models or a domain obligation changes admissible compensation. |
| Can common coordinates perform the value judgement? | Declare meanings and scales separately from preference, comparison, and selection. | Treat a dashboard or normalized vector as the decision model. | **Adopt:** :4.3 uses A.19 only for the declared space or predicate and leaves value elicitation here. The distinction adds little effort to an existing table and prevents a false consumer result. | Current `A.19`, `C.16`, and the direct comparison patterns supply the relevant typing and operation boundaries. They do not elicit the engagement's values or authorize a trade-off. | Reopen when the scale, predicate, consequence range, or receiving use changes. |

### PSD.9:12 - Relations

- `PSD.2` may supply the participation and concern account that changes the value question. That contribution is not already a weight set or a collective mandate.
- `PSD.11` consumes the value account only for the named comparison. The account does not silently scalarize or authorize its result.
- `C.16` governs measurements; `A.19` supplies a declared characteristic space or predicate when needed. Scoring, aggregation, comparison, and selection remain separate direct operations.
- Direct ethics, law, safety, governance, finance, and holder practices supply the particular conditions and claims they own. `A.15.9` helps obtain a missing qualified contribution without transferring that authority.
- If a required value or source premise is absent, stale, or incompatible, use a qualified direct result or return its exact gap. A completed model, candidate list, or workshop does not fill it by adjacency.

### PSD.9:End


<a id="psd-10"></a>
## PSD.10 - Represent Decision-Relevant Uncertainty and Evidence Limits

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** **bounded decision claims and unresolved discriminating questions**: what the evidence supports about the live alternatives, what could change that comparison, and which uncertainty cannot presently be resolved.

### PSD.10:1 - Problem frame

**Use this when** a point estimate, “high confidence” label, or model output makes a decision look more settled than its evidence permits. Also use it when a long uncertainty list does not say which unknown could reverse, narrow, defer, or invalidate the decision-support return.

Take one relied-on claim and ask: if this claim were different within its supported limits, what would change about these alternatives or their admissibility? State the supported claim and the remaining question together. The gain is a useful uncertainty account, not the impossible removal of all uncertainty.

The governed object is that decision-linked account. A claim about an uncertain consequence, an attributed belief, a model assumption, missing evidence, and a disputed value are different inputs. Their relevance to one decision does not turn them into one probability or a common confidence score.

**Do not use this pattern** when the only question is a source's provenance or currentness and no decision-support comparison changes; use `A.10` or the direct source practice. If the uncertainty account already supports the present use, reuse it. Direct domain practices retain their own measurement, forecasting, causal, safety, and evidential conclusions.

### PSD.10:2 - Problem

A numerical estimate can hide the conditions under which it is meaningful. An access model may estimate arrival time only when the road is open; a training study may concern an immediate test rather than later Work; an AI evaluation may concern a previous version or operating distribution. Averaging the results does not repair their missing applicability.

Conversely, a demand for certainty can stop every useful return. Some uncertainty cannot change the ordering, while another can show that all alternatives fail a protected condition. A useful account distinguishes those cases. It also separates a question that better evidence can answer from a disagreement about values or authority that evidence alone cannot settle.

### PSD.10:3 - Forces

| Force | Tension |
| --- | --- |
| Qualification and action | A decision needs bounded support, not complete knowledge, while an unsupported premise can make action indefensible. |
| Probability and ignorance | Probabilities can represent uncertainty well when justified, while invented distributions hide model disagreement or lack of knowledge. |
| Reduction and relevance | More information may narrow an estimate without changing any available decision. |
| Shared evidence and corroboration | Several sources can provide distinct support or merely repeat the same data and assumptions. |
| Stable comparison and changing conditions | Alternatives need a compatible basis, while source, holder, and environment changes can invalidate that basis. |

### PSD.10:4 - Solution

Connect each material uncertainty to the exact claim and decision it can change. Use a representation justified by the available knowledge, retain dependencies and limits, and return a bounded claim, discriminating question, narrowed use, or blocker.

#### PSD.10:4.1 - Start from a comparison that could change

Name the subject, configuration, horizon, receiving question, considered alternatives, and result currently being claimed. Ask which premise could change their consequences, relative standing, eligibility, or the need for a probe. If the alternatives themselves are unclear, return that candidate question.

Use `PSD.5`'s model account only where its evidence or assumptions bear on this same configuration and horizon. The model can expose an uncertainty without resolving it. A current qualified direct result can supply the same premise without requiring a model-building exercise.

Check both relative and absolute consequences. An uncertainty shared by all alternatives can leave their order unchanged yet show that none meets a required service or safety condition. Do not dismiss it as irrelevant merely because it is not a ranking discriminator.

#### PSD.10:4.2 - Represent what is unknown at its actual kind

Choose a form that answers the live question without claiming more knowledge than exists.

| Available basis | Useful representation | Limit that must remain visible |
| --- | --- | --- |
| Qualified stochastic model or elicited probabilistic judgement. | A distribution or probability statement tied to its event, population, conditions, and horizon. | Calibration, sampling, elicitation, model assumptions, and applicability still matter. Confidence in the analyst is not the event probability. |
| Supported bounds but no distribution. | An interval or set of admissible values. | An interval is not a uniform distribution; state what supports its endpoints and what lies outside its claim. |
| Several materially different models or future conditions. | Conditional claims under named models or scenarios. | Their count or frequency in an ensemble does not supply real-world likelihood. |
| A decisive absent result or unrepresented mechanism. | The exact missing claim and the comparison it prevents. | A blank cell is neither zero effect nor equal performance. |
| Incompatible interpretations, preferences, or authority claims. | Attributed alternatives and the unresolved interpretation or judgement. | Statistical uncertainty reduction alone cannot reconcile them. |

These are use choices, not a universal taxonomy of uncertainty. Different forms may coexist in one account. Distinguish a physical or behavioral variability claim from uncertainty about its model, data, or applicability whenever the distinction changes the return.

If a probability is useful but unsupported, state the conditional comparison it would enable and request the needed basis. Do not assign equal probabilities to scenarios simply to make an expected-value calculation run.

#### PSD.10:4.3 - Qualify the relied-on claims

For each decision-bearing source result, keep the claim, subject, supplying result kind, source edition or effective window, assumptions, evidence, intended use, exclusions, and material dissent recoverable. Use `A.10` for the actual bounded reliance question; its disposition does not establish the source claim's truth or authorize the decision.

Ask whether the evidence concerns the same holder, intervention, environment, and horizon. Separate observed results, forecasts, expert judgements, and unsupported extrapolations. An observation of a benefit is not automatically a causal effect; the direct causal or domain Method supplies that support.

Use an already-qualified result within its limit. If a consequential cross-practice result is still missing, `A.15.9` supports the smallest request or blocker. Do not ask another practice to “remove the uncertainty”; ask for the specific claim, bound, interpretation, or test that could change this comparison.

#### PSD.10:4.4 - Preserve dependency and model disagreement

Recover shared data, common causes, conditional assumptions, and other dependencies when they affect the consequence comparison. Evidence repeated by several models is not several independent confirmations. Expert or model aggregation needs its own justified Method; the number of voices alone does not determine a probability.

Keep incompatible assumptions separate until a direct result supports their combination. For example, a scenario with a failed access route and a scenario with a functioning route can test different claims; combining their most favorable outcomes produces no realizable case.

Where alternative models disagree, identify the overlapping proposition and what explains the difference: scope, input, representation, mechanism, or unresolved evidence. A new measurement may discriminate the models; sometimes the honest answer is that the present use must retain both. Do not turn disagreement into a narrow average solely because a downstream table expects one number.

#### PSD.10:4.5 - Form a discriminating question

Write the question in terms of its possible consequences for the current return:

> For this subject and horizon, establish whether this premise lies inside the region supporting alternative A, outside it, or remains unresolved; state the evidence and limits needed for that use.

The requested result may concern eligibility rather than ranking. It may also show that no available alternative works, that a different formulation is needed, or that only a reversible analytical use is supported.

Name a feasible observation, calculation, interpretation, or comparison that might answer the question, its supplying practice, and the relevant time or access limit. If no feasible inquiry can answer before the decision window closes, say so. Do not promise that more data will settle structural ignorance.

This pattern identifies decision-linked questions. `PSD.12` can later examine reversals and information priorities; `C.11` or the direct choice owner decides whether an actual next probe is worth its cost and authorized. A question with high uncertainty is not automatically the best probe.

#### PSD.10:4.6 - Return the strongest supported claim and no stronger

A short return states:

- what claim about which alternatives is supported, for which configuration and horizon;
- its uncertainty representation, source limits, and dependencies;
- what different answer could change the comparison, admissibility, or receiving use;
- the exact unanswered question or blocker; and
- what source, observation, candidate, value, or configuration change would reopen the account.

Return “unchanged within the tested bounds” only when those bounds cannot alter the stated result. Return a conditional or narrowed claim when support covers only part of the use. If a required protected-condition premise is unsupported, preserve the direct domain stop rather than compensating with confidence elsewhere.

Recognition may begin with one unexplained estimate. Consequential reliance requires the evidence and assurance demanded by the direct practice, including its independent checks when applicable. This pattern supplies no universal evidence score or acceptable uncertainty threshold.

When a relied-on source actually changes, revalidate the affected use. Use `G.11` for a currentness question and `A.10.1` when the changed claim must be traced through several actual uses. Do not discard unrelated claims merely because they share a source file.

### PSD.10:5 - Archetypal Grounding

#### PSD.10:5.1 - Which flood-pump uncertainty matters now?

In the illustrative pre-season inquiry, nominal permanent and mobile capacity meets the assumed inflow only with the stated units operating. The model omits arrival delay. The team cannot turn that conditional result into “mobile service is reliable”.

| Relied-on or proposed claim | Evidence limit | Decision-linked return |
| --- | --- | --- |
| Nominal mobile capacity is adequate. | The capacity calculation assumes operating units on site. | Use for capacity only. It does not discriminate the missing deployment arrangement. |
| Mobile units can serve the district after road loss. | No qualified arrival and deployment result exists for that condition. | Ask for the route-loss deployment result; M remains conditional for the service comparison. |
| The two technical models corroborate the inflow assumption. | They reuse the same inflow dataset. | Retain one shared evidence dependency, not two confirmations. |
| Pumping-service hours represent all affected residents' loss. | Reachable assistance and property protection have different meanings. | Return the missing consequence relation or keep separate accounts; a tighter inflow estimate will not settle the value question. |

If a direct deployment result later supports a bounded arrival range, the account changes only the affected claim and its uses. If the range still spans service failure, the result is a discriminating question for robustness, not an unconditional feasibility claim. If all arrangements share an unsupported power-supply assumption, that common uncertainty can invalidate all of them even while their relative order stays fixed.

#### PSD.10:5.2 - Development evidence with three different limits

For a ninety-day organization recommendation, suppose the adviser has an immediate human assessment, a queue model for the current team, and an offline AI benchmark. Each can inform a different bounded claim.

The human assessment does not establish retention or transfer to later service Work. The queue model does not establish the performance of a reallocated or mixed arrangement without its staffing and interaction premises. The benchmark does not establish current-version service reliability under the operating distribution and oversight arrangement.

The return names three possible supplier questions at their own grain: representative later-Work capability, changed-arrangement service consequences, and exact-version operating evaluation. Only questions that could change the live recommendation are pursued. Averaging the three “confidence” labels would repair none of these gaps.

#### PSD.10:5.3 - A bounded input to SensorCo's strategic commitment

SensorCo's illustrative twelve-month question concerns defending devices, offering an integrated service, licensing data, or exiting a segment as generic AI inspection prices fall. The strategy team owns the strategic comparison; the board separately holds commitment authority.

Suppose the integrated-service direction relies on an uncertain repeat-demand claim, while the licensing direction relies on a still-unqualified permission premise. The PSD return names the repeat-demand conditions that could alter the service comparison and the exact rights interpretation missing for licensing. It supplies neither the strategic facts nor a permission judgement by itself.

Under the decision-linked uncertainty relation, `STR.11` may use the supplied result only for this commitment and compatible horizon. A changed alternative, claim scope, demand question, evidence window, or commitment reopens that use. If the result is unavailable or incompatible, the strategic receiver uses a qualified direct source or keeps the exact gap; a MethodDescription or analogy is no substitute for the result.

#### PSD.10:5.4 - Cheap non-use

An analyst needs to recover which calibration edition a measurement cites, and no candidate comparison is being made. Use the source and evidence practice directly. A decision-linked uncertainty account would add no current result.

### PSD.10:6 - Bias-Annotation

**Scope:** uncertainties that can change a bounded decision-support return. **Lenses:** **Epist** separates evidence and belief; **Prag** tests action-changing relevance; **Arch** exposes dependencies; **Gov** preserves direct authority and protected conditions; **Did** makes an unknown into a useful question.

Precision bias favors a number over an honest set or gap. Confidence rhetoric can substitute reputation for evidence. Model averaging can conceal shared errors. Certainty seeking can consume the entire decision window. Counter these with exact conditional claims and an explicit account of what a different answer would change.

### PSD.10:7 - Conformance Checklist

- [ ] Each material uncertainty is linked to a claim, alternatives, configuration, horizon, and receiving use.
- [ ] The account tests eligibility and shared failure as well as ranking changes.
- [ ] Probabilities, intervals, scenarios, missing results, and disputes retain their different meanings.
- [ ] Every probability or bound has an adequate basis; scenario counts are not probabilities by default.
- [ ] Source, holder, intervention, and environment limits accompany relied-on evidence.
- [ ] Shared evidence, common causes, and incompatible model assumptions remain visible.
- [ ] Each proposed inquiry names a result that could change the return and a feasible limit or honest inability.
- [ ] The disposition is bounded, conditional, narrowed, or blocked as the actual support requires.
- [ ] Direct assurance, permission, and choice are not inferred from an uncertainty account.
- [ ] Changed sources reopen only affected uses, with their own subject judgements.

### PSD.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Confidence is eighty percent.” | Say whose judgement, about which proposition, under what evidence and probability interpretation. |
| Give three scenarios equal probability because three were drawn. | Retain scenario-conditional claims until a distribution is justified. |
| Average incompatible model outputs. | Locate the disputed proposition and keep the alternative assumptions or exact gap. |
| Discard uncertainty common to all candidates. | Check whether it changes absolute admissibility or shows that all fail. |
| Commission more data without a decision question. | State which possible answer could change the comparison or its use. |
| Replace missing holder evidence with another holder's success. | Request the exact transfer or applicability result; retain the blocker if it is unavailable. |

### PSD.10:9 - Consequences

The recipient can see what is known well enough for this decision and which unknown deserves attention. Some numerical precision is lost, but unsupported certainty is removed. The work can become smaller: once an uncertainty cannot change the bounded return, further refinement needs another justification.

### PSD.10:10 - Rationale

Uncertainty matters through its effect on a decision claim, not through its size alone. Preserving the source, representation, and dependency of each premise makes that effect inspectable. A bounded unknown can support useful inquiry without pretending to supply the missing fact or the eventual choice.

### PSD.10:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| When should uncertainty be probabilistic, and when should alternatives remain conditional? | Use qualified probabilistic analysis where its premises hold; retain multiple plausible conditions when decision-relevant probabilities or models are unsettled. | Predict-then-act under one agreed forecast, or reject all probabilistic reasoning whenever uncertainty is difficult. | **Adapt:** :4.1–:4.4 select the representation by the actual basis and test shared failure. Additional scenario work is accepted only when one forecast could conceal a material reversal. | Lempert et al.'s [2024 DMDU/IPCC analysis](https://doi.org/10.3389/fclim.2024.1380054) is the synthesis candidate for decision relevance despite low-confidence knowledge. It does not make scenarios equiprobable or provide a universal uncertainty taxonomy or local risk threshold. | Reopen when a qualified distribution becomes available, model disagreement changes, or an omitted future defeats the claimed bounds. |
| Which missing evidence deserves a question? | Connect elicitation, sensitivity, and information acquisition to the alternatives and consequences they can change. | Rank unknowns by variance or confidence alone. | **Adapt:** :4.5–:4.6 require a discriminating question before further inquiry. The practical trade-off is less general data collection for a more explicit decision boundary. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current decision-analysis connection among uncertainty, sensitivity, and information value. It is a synthesis, not validation of PSD's particular evidence or a universal probe rule. `A.10` supplies only bounded reliance; `C.11` retains actual local probe choice. | Reopen if another unknown can change eligibility, a model revision changes the discriminator, or no feasible inquiry fits the decision window. |

### PSD.10:12 - Relations

- `PSD.5` may supply model evidence and assumptions for the same configuration and horizon. Representation alone establishes neither the subject condition nor this uncertainty judgement.
- `PSD.11` may use the bounded claims and questions where they change its consequence comparison. Evidence neither entails that result nor authorizes the later decision.
- `STR.11` may use a supplied decision-linked uncertainty result only where it can change the strategic commitment comparison. The result carries its own scope and horizon; it imports neither the whole PSD practice nor strategic facts or authority.
- `A.10` governs claim-bound evidence and reliance; `A.15.9` governs a needed outside-practice request or use. `G.11` and, for several actual changed uses, `A.10.1` govern currentness and affected-use revalidation.
- `PSD.12` owns the distinct robustness and information-priority question. `C.11` or the direct decision owner governs an actual probe or choice. Missing, stale, or incompatible inputs remain exact gaps unless a qualified direct result supplies them.

### PSD.10:End


<a id="psd-11"></a>
## PSD.11 - Compare Consequences

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** an **inspectable consequence comparison** for exact alternatives, affected subjects, conditions, horizon, value accounts, and evidence, including the relations that hold and those that remain unresolved.

### PSD.11:1 - Problem frame

**Use this when** alternatives have been named or ranked but nobody can reconstruct what each would change, for whom, over what time, and under which assumptions. Also use it when a development direction looks attractive from one component's score while its service, transition, interaction, or protected-condition consequences remain absent.

Begin with one alternative and one consequence that matters. Trace the proposed change through its supported mechanism and conditions to the affected subject, then compare that same consequence for the other alternatives. The gain is a comparison that explains its result and its limits.

The governed object is the consequence comparison, not the future outcome or the authorized choice. A consequence claim may be a forecast, conditional model result, observation, or unsupported hypothesis. A table presents those claims; it does not make their predicted events occur.

**Do not use this pattern** when a current qualified comparison already covers the exact alternatives and receiving use. Use the direct domain Method for a single missing calculation or effect estimate. If the only remaining question is the authorized choice among adequate options, use `C.11` or the direct decision guidance.

### PSD.11:2 - Problem

A rank can hide an incomplete causal story. A larger pump does not by itself establish delivered flood service. A better-trained worker does not by itself remove a queue constrained by interfaces. A stronger model benchmark does not establish reliability of the deployed service arrangement.

Even accurate separate estimates can form a false comparison. Alternatives may use different baselines, populations, operating assumptions, or horizons. Shared benefits can be counted twice, losses shifted to excluded people, and an average used to hide a tail or distributional difference. The missing work is a consequence account on a compatible basis, not merely a more sophisticated ranking algorithm.

### PSD.11:3 - Forces

| Force | Tension |
| --- | --- |
| Common basis and real difference | Alternatives need comparable questions, while their mechanisms and affected subjects can genuinely differ. |
| Detail and affordability | Transition, distribution, and dependencies may reverse a conclusion, while exhaustive modeling can miss the decision window. |
| Multiple values and synthesis | A recipient needs a usable comparison without losing protected conditions or incompatible value accounts. |
| Prediction and evidence | A conditional model can inform a future choice without becoming an observed or causal result. |
| Precision and partiality | Numerical relations can clarify a comparison, while absent or incompatible evidence may leave no defensible total order. |

### PSD.11:4 - Solution

Build consequence claims for the same receiving question, align only the meanings that can be aligned, apply the declared comparison rule, and return the supported relation together with uncertainty, dissent, and exact gaps.

#### PSD.11:4.1 - Fix the comparison, not just its column names

Name the recipient question, subject or holder, current configuration, horizon, relevant affected subjects, and exact alternatives. Use `PSD.8`'s set only as the candidate family; generation supplies no ranking. A proposal missing a decisive premise remains conditional rather than silently joining the eligible set.

Use `PSD.9`'s value account only for this comparison. Keep its attributed values, protected conditions, scales, and unagreed trade-offs. Use `PSD.10`'s bounded claims and discriminating questions only where their evidence concerns the same configuration and horizon.

These inputs can come from current qualified direct sources. If one is absent, stale, or incompatible, return the exact missing premise or narrow the comparison. Do not infer a usable value account from a workshop or a qualified forecast from a diagram.

#### PSD.11:4.2 - Establish consequence paths at the needed grain

For each material alternative, connect the proposed change to intermediate conditions and the consequences that the value account actually uses. Identify who or what bears each consequence, when it appears, whether it persists, and which enabling conditions it needs.

Include transition burdens, delayed effects, and shifted losses when they can alter the comparison. Distinguish the present arrangement from an empty or ideal baseline. Use `C.11.CRC` when the missing input is specifically a finite change's contribution relative to the current configuration; reuse an already adequate contribution claim rather than reconstructing it.

Direct domain models and evidence supply effect estimates and mechanisms. A causal arrow or before–after difference is not sufficient causal support; use the direct causal or field guidance for a causal claim. A qualitative pathway can still identify a missing relationship without estimating its magnitude.

Do not extend a consequence beyond its qualified horizon without a stated model and source. If a short operating horizon excludes a material long-term lock-in or displaced loss, expose the exclusion and reopen the boundary where necessary.

#### PSD.11:4.3 - Construct a consequence account before aggregating

Keep each alternative's material consequence profile visible. For every relied-on entry, show the relevant subject, meaning, unit or category, condition or scenario, time, source, uncertainty, and missingness. A short parallel description can suffice; use a table when it makes repeated comparisons clearer.

Separate physical or service consequences from how they are valued. A budget estimate, hours of service loss, a probability distribution, and a consent condition do not become interchangeable because they occupy adjacent columns. A lower cost can be compared directly under its scale while a disputed value trade-off remains unresolved.

Where there is a distribution, preserve its event definition and dependence on the alternative and conditions. Expected values alone are insufficient when a tail, threshold, reversibility, or distribution across affected subjects can change the decision. Where no distribution is justified, retain conditional scenarios or bounds.

A missing value is unknown, not zero or equal to the competing alternative. A qualified narrower slice remains usable only with its excluded consequences explicit.

#### PSD.11:4.4 - Check dependencies and shared burdens

Ask whether consequences share a cause, depend on the same resource, overlap in their accounting, or change under combination. A human–tool arrangement needs a whole-arrangement result; adding a worker's effect to a tool's effect can omit coordination loss or count the same resolved case twice.

Use the dependence structure required by the selected model. Do not assume independent failures simply because separate estimates exist. Linearity can justify adding expected contributions without independence, but it does not justify duplicated quantities, unsupported causal contributions, or a joint tail probability.

Inspect whether a claimed dominance survives the common conditions. Different favorable assumptions for different alternatives produce no fair comparison. If a required correspondence or joint model is missing, keep the particular relation unresolved.

#### PSD.11:4.5 - Apply only an admitted comparison rule

State what “better”, “equivalent”, “dominated”, or “incomparable” means for this use. A coordinatewise comparison may establish that one alternative is no worse on every included coordinate and better on at least one. That conclusion remains limited to those coordinates, conditions, and admissible alternatives; it is not an overall recommendation.

Use the current value account for any compensatory score, priority rule, threshold, or outranking Method. Do not convert ordinal judgements to arithmetic, add a hidden tie-breaker, or adopt a group average to force closure. If several value models remain admissible, show which relations hold throughout them and which depend on the model.

Use `A.19.CPM` when its profile, comparator, admissibility, and evidence conditions obtain. Its set-valued comparison outcome remains distinct from the application and evidence account, a result episteme, selection, or permission. Use the appropriate direct comparison Method otherwise; a table alone does not assert a CPM application.

Distinguish three important outcomes. Two alternatives can be tied under a rule, incomparable because of supported conflicting consequences, or not yet comparable because a necessary input is missing. Preserve the difference. If no candidate meets a protected condition, return that failure rather than ranking the least nonconforming candidate as acceptable.

#### PSD.11:4.6 - Return the relation and what would change it

State the exact alternatives and question; common basis; consequence profiles and source limits; applied rule; supported relations; material value disagreement; excluded or unresolved comparisons; and the smallest change that could invalidate the result.

`PSD.12` may use this comparison and its evidence for the same configuration and horizon to test robustness. It does not inherit a robustness claim merely from a clean table. An authorized chooser or recommendation practitioner may consume the comparison, but this result supplies neither their judgement nor a programme, WorkPlan, performed Work, or realized effect.

Recognition begins when a rank lacks a recoverable consequence path. Assurance requires qualified direct models, evidence, source reliance, calculation or implementation checks, and the relevant domain protections. A replayable comparison can still be empirically wrong; independent support of its premises remains necessary.

### PSD.11:5 - Archetypal Grounding

#### PSD.11:5.1 - A flood-service comparison with no scenario-free winner

Continue the illustrative next-season case with N, F, M, and S: continue the present arrangement, change fixed capacity, obtain a mobile reserve arrangement, or use a staged combination.

Suppose a later qualified deployment analysis now provides the previously missing conditional operating results for M. A compatible resource estimate and service model provide the following hypothetical analytical slice. Costs are incremental budget units above the common continuing baseline; service loss is hours when the specified pumping service is unavailable. Lower is preferred on both measures for this slice. No scenario probability is supplied.

| Alternative | Incremental budget units | Service-loss hours with normal access | Service-loss hours with road loss |
| --- | --- | --- | --- |
| N — continuing baseline | 0 | 7 | 11 |
| F — fixed-capacity change | 8 | 2 | 3 |
| M — mobile-reserve arrangement | 5 | 1 | 9 |
| S — staged combination | Not yet qualified | Not yet qualified | Not yet qualified |

These figures are invented to demonstrate the comparison; they are not engineering, financial, safety, or investment advice. The current sources do not establish reachable assistance or all property-loss consequences. Those value and protected-condition questions remain outside this numerical slice and can block an overall recommendation.

Under normal access, M costs less and has fewer service-loss hours than F. Under road loss, F loses fewer service hours but costs more. Thus the slice establishes no condition-independent dominance between F and M. N uses fewer incremental resources but loses more service hours; zero incremental cost does not mean that the baseline has no continuing obligations or consequences.

S is not assigned zero or dropped as an inferior candidate. Its missing whole-arrangement result is returned as a gap. The inspector can reproduce the narrower relations while seeing why neither those relations nor the table supports a complete four-candidate recommendation.

#### PSD.11:5.2 - Compare whole development arrangements, not component scores

In the ninety-day organization case, a course assessment and an AI benchmark cannot be placed directly into one service-reliability ranking. Suppose the adviser obtains a qualified allocation and operations comparison for two whole arrangements: I, internal development with covered service duties, and H, a mixed human–tool arrangement with oversight and fallback.

The hypothetical supplier result gives ninety-day unplanned service-loss bounds of 12–18 hours for I and 8–20 hours for H, on the same service definition and operating conditions. Both retain their separately qualified resource and security conditions. No joint relation between the uncertain losses is supplied.

Those marginal bounds do not establish that H is always better, nor do they establish equality. H permits both a lower and a higher loss than I within the supplied bounds. The comparison returns an unresolved robust service ordering and asks which coordination or operating condition accounts for that difference. A joint model could provide a stronger relation, but it must be supplied rather than inferred from overlapping intervals.

The human capability result, organization-allocation result, and exact-version AI evaluation remain separate premises of that whole-arrangement comparison. No human learning effect is transferred to a model, and no model score stands for the organization's outcome.

#### PSD.11:5.3 - Cheap non-use

A current qualified comparison already covers two replacement arrangements, their transition costs, service consequences, and the recipient's value rule. Reuse it for the authorized choice. A second consequence table with the same content adds no new result.

### PSD.11:6 - Bias-Annotation

**Scope:** consequence comparisons for bounded decision-support use. **Lenses:** **Onto/Epist** separates alternative, forecast, observation, and result; **Arch** exposes interaction and distribution; **Prag** fixes the receiving question; **Gov** preserves conditions and authority; **Did** makes the comparison replayable.

Ranking bias prefers closure over partiality. Baseline bias compares change with an empty world. Aggregation bias hides losers and shared burdens. Model precision can conceal missing applicability. Counter these by exposing consequence paths, testing the common basis, and stating the exact relation actually supported.

### PSD.11:7 - Conformance Checklist

- [ ] Alternatives, subject, configuration, affected subjects, horizon, and receiving use are fixed for the comparison.
- [ ] Candidate, value, and uncertainty inputs are current and compatible or their gaps are returned.
- [ ] Each material consequence has a supported path, subject, timing, and uncertainty account.
- [ ] Transition, interaction, shared burdens, and displaced losses are included where they can change the result.
- [ ] Measures, value transformations, protected conditions, and evidence retain their different meanings.
- [ ] Missing entries are not zero, equal, or silently favorable.
- [ ] The comparison rule and admissible operations are explicit.
- [ ] Ties, supported incomparability, and inability to compare are distinguished.
- [ ] The result states supported relations, limits, dissent, and exact reopen conditions.
- [ ] Comparison does not establish robustness, recommendation, authorization, Work, or effect.

### PSD.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Compare a component's score with a whole arrangement's outcome. | Obtain consequence claims for the same receiving subject and use. |
| Use favorable conditions for each alternative. | Hold the comparison basis fixed or show explicit conditional branches. |
| Sum separately advertised benefits. | Recover overlap, interaction, and the qualified whole-arrangement result. |
| Treat overlapping uncertainty intervals as equality. | State what relation the bounds actually support and what joint information is missing. |
| Rank a failed protected condition by compensatory score. | Keep eligibility separate and return the failure. |
| Call an archive front a consequence comparison. | Recover the actual comparator, consequence profiles, conditions, and evidence. |

### PSD.11:9 - Consequences

A recipient can inspect why an alternative compares favorably and exactly where that conclusion stops. Partial comparisons remain useful, and missing domain results become precise requests. The cost is explicit consequence and dependence work; focus it on distinctions that could reverse the result rather than building a maximal model.

### PSD.11:10 - Rationale

A consequence comparison connects proposed actions to values through qualified claims about affected subjects. Keeping that chain visible prevents a ranking from silently deciding the model, value system, or protected conditions. Separate comparison and choice allow a well-supported partial answer to remain a valid result.

### PSD.11:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should alternatives be connected to consequences? | Use explicit outcome models with the conditions and dependencies needed by the decision. | Rank isolated attributes or tool outputs without a consequence path. | **Adapt:** :4.1–:4.4 reconstruct only decision-changing consequence paths and shared burdens. The added effort is accepted when an omitted interaction could reverse the comparison; a qualified existing account is reused. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current graphical-model and uncertainty line. It does not validate a local mechanism or establish causal effects from arrows. `C.11.CRC` supplies a missing finite configuration-relative contribution, not field calculations. | Reopen when a changed configuration, mechanism, affected subject, or horizon invalidates a consequence path. |
| What comparison is justified by conflicting or incomplete values? | Use a declared preference model and preserve its partial or model-dependent relations. | Impose one total weighted rank. | **Adapt:** :4.5–:4.6 retain ties, incomparability, and missing-input distinctions. The deliberately accepted trade-off is less rhetorical decisiveness for a truthful relation. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) is a comparison candidate for alternative preference and recommendation forms. Its finite-action methods do not supply local values, probabilities, or decision authority. | Reopen if elicitation or evidence changes the admitted model set or resolves a previously missing comparison. |
| Does generic candidate stewardship already compare the consequences? | Keep profile comparison, finite contribution, and archive/front stewardship distinct. | Treat C.18 as a general consequence-ranking Method. | **Adopt:** :4.2 and :4.5 use the exact C.11.CRC and A.19.CPM contributions when needed; the PSD consequence account retains its field question. No archive machinery is required for a small comparison. | Current `C.18` governs generation, archive, and front objects; `A.19.CPM` governs its admitted set-valued comparison; direct domain Methods supply consequence models. Their different result boundaries defeat the broader attribution. | Reopen when the current question actually becomes archive stewardship or a direct comparison contribution changes. |

### PSD.11:12 - Relations

- `PSD.8` supplies the alternative family, `PSD.9` the value and trade-off account, and `PSD.10` bounded evidence and uncertainty claims. Each is used only under compatible subject, configuration, horizon, and receiving conditions.
- `PSD.12` may consume the comparison's evidence to test robustness for that same use. The comparison does not entail the robustness result.
- `C.11.CRC` supplies a missing finite configuration-relative contribution claim. `A.19.CPM` supplies an admitted profile comparison only when its own conditions obtain. `C.18` retains its different archive/front and generation function.
- Direct engineering, operations, human-development, AI/model, financial, scientific, and other practices govern their own consequence and evidence results. `A.10` qualifies reliance; `A.15.9` supports a needed bounded outside contribution.
- `C.11` or the direct decision owner supplies the later choice. An unavailable, stale, or incompatible premise is replaced by a qualified direct result or remains a named gap, never filled by neighboring-pattern presence.

### PSD.11:End


<a id="psd-12"></a>
## PSD.12 - Test Robustness and Sensitivity

> **Type:** DPF pattern body
> **Status:** Candidate
>
> **Primary working result:** **robust regions, reversals, and information priorities** for one decision-support comparison: the conditions under which a claim holds, changes, or cannot be established, and the questions that could usefully change it.

### PSD.12:1 - Problem frame

**Use this when** a favored alternative depends on a forecast, weight, model, or threshold that might change, or when a precise ranking hides plausible reversals. Also use it when the recipient asks whether further information would improve the decision rather than merely improve the estimate.

Start with one claim: what exactly should remain true, under which changes? Vary the decision-bearing conditions within a justified range and inspect where the claim survives or fails. The gain is a bounded statement of stability and a useful next question, not the adjective “robust” applied to an entire project.

The governed object is that robustness account. **Sensitivity** describes how a result changes with inputs, assumptions, or models. **Robustness** says whether a declared performance, admissibility, or comparison condition continues to hold across specified variation. A sensitive magnitude can leave the preferred set unchanged; an insensitive average can hide a decisive threshold crossing.

**Do not use this pattern** when a current robustness result already covers the exact comparison and changes now in question. Use direct model validation for whether a model is adequate in the first place, and the authorized choice owner for the actual decision or probe. Stability inside a model does not validate the model or authorize action.

### PSD.12:2 - Problem

A one-point ranking can hide a narrow region of support. Small changes in a value trade-off can reverse it; a common-cause failure can defeat every alternative; a different model can change which conditions are even represented.

Sensitivity work can also miss the decision. A tornado chart may rank output variance rather than choice relevance. One-factor-at-a-time tests can miss interactions. Running thousands of similar scenarios can create an appearance of broad coverage, and their frequency can be mistaken for probability. More calculations do not by themselves support a stronger robustness claim.

### PSD.12:3 - Forces

| Force | Tension |
| --- | --- |
| Coverage and effort | Joint or structural changes can matter, while unrestricted scenario expansion consumes the available time. |
| Stability and truth | Repeated agreement supports only the tested model and region, not the omitted world. |
| Values and evidence | Better information can resolve a fact, while a disputed trade-off needs a value judgement or legitimate collective decision. |
| Flexibility and commitment | Staging can preserve options, while monitoring, lead time, reversibility, and later authority may be unavailable. |
| Information and action | A probe can change a decision, but it also costs time, resources, exposure, and foregone opportunity. |

### PSD.12:4 - Solution

Declare the claim and variation space, challenge it with the least costly tests that cover the live failure mechanisms, and return supported regions, reversals, and bounded information questions. Keep the actual later decision separate.

#### PSD.12:4.1 - State what is being tested

Recover the exact alternatives, consequence comparison, value basis, subject, configuration, horizon, and receiving use. Use `PSD.11`'s comparison and evidence only where they match those conditions. A qualified direct comparison can supply the same input.

Specify the test. It might ask whether one alternative remains no worse under a declared rule, whether every retained alternative meets a service threshold, whether a protected condition is ever violated, or whether the recommendation must remain conditional. Different tests can produce different answers.

Name the robustness criterion before interpreting results. Satisfactory performance across tested conditions, worst-case loss, regret relative to the best available alternative in each condition, and stability across compatible value models answer different questions. Do not change the criterion after seeing which candidate it favors. If the criterion or admissible trade-off is unresolved, return that question rather than presenting a universal winner.

#### PSD.12:4.2 - Bound the changes by evidence and the decision

Identify the uncertainties or judgement changes that could affect this test: input values, future conditions, model structures, consequence definitions, preference models, evidence qualification, candidate membership, or horizon. State why the selected variations are relevant and what they omit.

Ranges and scenarios need a basis. Distinguish observed bounds, elicited judgements, scientifically or operationally plausible cases, and deliberately extreme stress tests. A stress-test failure can reveal vulnerability without establishing the failure's probability.

Preserve dependencies and feasibility. Joint variations should describe possible or explicitly hypothetical conditions, not arbitrary combinations of incompatible endpoints. Changing a binding legal, safety, consent, or security condition is not an ordinary parameter perturbation; it creates a different authority or applicability question requiring its own result.

If a needed variation cannot be bounded, retain that coverage gap. “Across all plausible futures” is stronger than “across the three stated futures” and needs stronger support.

#### PSD.12:4.3 - Test locally, then expand where the failure can hide

Begin with a cheap discriminating test: a boundary value, an alternative value judgement, an omitted condition, or a direct challenge to one decisive assumption. Recompute the same comparison for all affected alternatives under that changed basis.

Use joint or global variation when interactions, nonlinearities, common causes, thresholds, or structural alternatives can change the result. A one-at-a-time test is insufficient for a claim about those combinations. Use the direct modeling and analysis Method to choose suitable tests, sampling, or proofs; this pattern mandates no universal algorithm or scenario count.

Keep empirical variability, model uncertainty, and value disagreement distinguishable. If a model change alters the meaning or comparability of an output, repair the comparison before treating the difference as another numerical sample.

A computational result is limited by the tested region and procedure. An analytical inequality may establish a whole region under its assumptions; a finite sample usually establishes only sampled behavior unless a further guarantee is justified. State that difference.

#### PSD.12:4.4 - Map holding regions and reversals

Report which condition holds in each relevant region, where alternatives exchange order, where a threshold is crossed, and where the comparison becomes unsupported. Include boundaries and ties when they can change the return.

Separate a genuine reversal from a different question. A new value rule, candidate, subject, or horizon may define another comparison rather than a parameter change inside the old one. Preserve the original basis so that the reader can see which happened.

Test omissions as well as numbers. A stable two-candidate result can be irrelevant if a material third candidate remains unexamined. A common failure can show that all current alternatives are inadequate. Return that candidate or formulation gap instead of calling the least bad option acceptable.

The result may be a robust retained set, a conditional preference, several non-dominated alternatives, a failure region, an unresolved boundary, or a blocker. No single preferred alternative is required.

#### PSD.12:4.5 - Connect the remaining uncertainty to information value

Ask what feasible observation, experiment, calculation, or interpretation could move the comparison across a material boundary. Distinguish “this factor changes the output a lot” from “this attainable result could change the decision”.

Where a qualified probabilistic and value model permits information-value analysis, include the possible decisions after the information, the informativeness of the actual probe, and its cost and delay. Perfect-information value can be an upper bound; it is not the value of an imperfect test. Information values from several sources are not automatically additive.

Where probabilities are not defensible, state the discriminating conditions and what a probe could resolve without inventing expected value. Some uncertainty will remain; a broad research programme is not the default response.

Use `C.11` or the direct decision owner for the actual choice of a next probe over the current options, budget, value, and cost. This pattern supplies information priorities and conditions, not probe authorization or a research WorkPlan. A preference or authority dispute may require an explicit judgement rather than more empirical data.

#### PSD.12:4.6 - Examine adaptive alternatives without assuming free flexibility

When a staged candidate is live, test what it actually preserves. The later observation must arrive early enough, be interpretable, and leave a feasible response within the remaining resources and authority. Include monitoring cost, lead time, temporary exposure, transition burdens, and irreversible loss of options where material.

A policy-failure condition is not automatically an action trigger. The future decision arrangement must determine what observation warrants reconsideration and who can act. If those premises are missing, return the candidate's specific adaptive-capability gap.

Do not favor a pilot solely because uncertainty is high. A probe can be unsafe, too slow, uninformative, or unable to change the relevant commitment. Conversely, a bounded information result can be more useful than a premature direction recommendation when its supported value justifies the delay.

#### PSD.12:4.7 - Return a bounded robustness account

Return the tested claim and comparison basis; the variation region and omissions; the method and evidence limits; supported holding regions and reversal conditions; unresolved comparisons or candidate gaps; information priorities and feasibility limits; and the observation that reopens the result.

`PSD.13` may use this evidence for the same configuration and horizon to compose a recommendation. Evidence does not entail that recommendation or the later receiving decision. An unavailable, stale, or incompatible robustness result can be replaced only by a qualified direct result or an explicit gap.

Recognition starts with a plausible reversal. Consequential assurance also requires qualified model and source use, correct analysis, adequate challenge coverage, and the direct domain's protection and independence requirements. Robustness to uncertain parameters does not cure an invalid model or missing safety result.

### PSD.12:5 - Archetypal Grounding

#### PSD.12:5.1 - An explicit reversal boundary for the pump comparison

Use the illustrative F and M slice from `PSD.11`: F costs 8 incremental budget units and loses 2 service hours with normal access or 3 with road loss; M costs 5 and loses 1 or 9 hours. N remains the baseline and S still has an unqualified whole-arrangement result. The following calculation tests only F against M; it does not close the wider candidate comparison.

For an illustrative analytical question, suppose a declared value model minimizes expected service-loss hours plus `lambda` times incremental budget units. Here `lambda` is an explicitly elicited value conversion, in service-hour-equivalent value per budget unit; it is not a measurement conversion or an unspoken public preference. Let `p` be the road-loss probability if a qualified probability model supports one.

Under those assumptions:

- F's value loss is `2 + p + 8*lambda`.
- M's value loss is `1 + 8*p + 5*lambda`.
- F has lower value loss precisely when `7*p > 1 + 3*lambda`; equality is a tie.

For `lambda = 0.5`, the reversal is at `p = 5/14`, approximately 0.357. At `p = 0.2`, F and M give 6.2 and 5.1 respectively, so M is better under this model. At `p = 0.6`, they give 6.6 and 8.3, so F is better. These are invented sensitivity settings, not a forecast.

The source comparison supplied no probability. Therefore the valid return is the conditional boundary, not a claim that either setting is likely. If a probability model cannot be qualified, retain the scenario comparison instead of assigning equal chances.

A different declared test asks whether modeled service loss is at most 4 hours in both stated access conditions. F satisfies that illustrative test; M fails it under road loss. This is a different robustness criterion, not a hidden replacement for the value model. The four-hour cut is an example, not a domain standard. F's result covers only those two modeled conditions.

The account returns the reversal boundary, the limited threshold result, the unresolved probability and value premises, and S's candidate gap. Reachable assistance, wider property consequences, and protected conditions still require their direct results. None of the calculations authorizes a pump investment.

#### PSD.12:5.2 - What would change a development recommendation?

In the illustrative ninety-day organization case, I is internal development with covered service duties and H is a mixed human–tool arrangement. The earlier supplier bounds, 12–18 and 8–20 service-loss hours, do not establish a robust ordering.

Suppose a qualified joint operating model now supplies two admissible conditions within those bounds:

| Condition | I: service-loss hours | H: service-loss hours | Supported comparison on this coordinate |
| --- | --- | --- | --- |
| Required handoff coverage is present. | 14 | 10 | H has less service loss. |
| The specified handoff coverage is absent. | 16 | 20 | I has less service loss. |

The robustness result locates a reversal in the whole arrangement's coverage condition. It does not attribute the difference solely to human learning or model quality. The useful next question is the feasibility and persistence of that exact coverage under the proposed allocation, not a generic demand for a higher AI benchmark or another course test.

If that result can be obtained within the decision window, the adviser can return it as an information priority with its cost and limits. If not, the recommendation remains conditional or retains both directions. A service model for another team or model version does not close this holder-specific boundary.

#### PSD.12:5.3 - Cheap non-use and honest stop

A current analysis already proves the same service comparison throughout the relevant parameter interval, and the only proposed new computation repeats interior points without challenging another assumption. Reuse the result. If the untested issue is instead a missing causal or safety premise, stop the robustness calculation and obtain that direct result; more parameter samples will not supply it.

### PSD.12:6 - Bias-Annotation

**Scope:** robustness and information questions for bounded decision support. **Lenses:** **Epist** distinguishes model stability from truth; **Prag** tests decision relevance; **Arch** exposes interactions and omitted alternatives; **Gov** preserves protected conditions and future authority; **Did** makes reversals and limits readable.

Winner-protection bias selects narrow ranges or convenient criteria. Scenario-count bias mistakes volume for coverage. Variance bias selects a probe that cannot change the decision. Flexibility bias assumes cost-free adaptation. Counter these by declaring the claim, criterion, region, and real response capability before interpreting the result.

### PSD.12:7 - Conformance Checklist

- [ ] The exact comparison, subject, configuration, horizon, and robustness claim are stated.
- [ ] The robustness criterion is explicit and not chosen after seeing the preferred winner.
- [ ] Variation ranges, scenarios, dependencies, and exclusions have a recoverable basis.
- [ ] Binding conditions are not silently relaxed as parameters.
- [ ] Tests address relevant interactions, structural differences, and omitted alternatives.
- [ ] Sampled behavior, analytical region claims, and unsupported extrapolation are distinguished.
- [ ] Holding regions, ties, reversals, failures, and gaps are reported at their actual scope.
- [ ] Information priorities concern attainable decision-changing results and include cost or feasibility limits.
- [ ] Adaptive claims account for observation, lead time, response feasibility, and later authority.
- [ ] The return supplies evidence for recommendation, not truth, authorization, Work, or effectiveness.

### PSD.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The winner is robust” after a few small perturbations. | State the claim, variation region, method, and untested failure mechanisms. |
| Count successful scenarios as a success probability. | Supply a qualified probability measure or report conditional coverage only. |
| Change one input at a time despite common-cause failure. | Test the relevant joint conditions under a justified dependence model. |
| Treat the largest output variance as the best information target. | Ask whether attainable information can change a decision or eligibility. |
| Recommend a pilot whenever evidence is thin. | Establish information value, safety, timing, reversibility, and response feasibility. |
| Change the robustness criterion to preserve the preferred option. | Show the different questions and return the criterion disagreement. |

### PSD.12:9 - Consequences

The recipient learns not only what currently compares favorably but where the conclusion can fail. A retained set or conditional recommendation can be more useful than a fragile winner. The cost is targeted recomparison and explicit coverage limits; stop when further work cannot change the declared return or when a different missing premise governs the next action.

### PSD.12:10 - Rationale

A decision-support result is strengthened by exposing its reversal conditions, not by defending one point estimate. Separating uncertainty, values, model structure, and response capability prevents robustness from becoming a general assurance label. Decision-linked information priorities keep remaining uncertainty useful without making inquiry endless.

### PSD.12:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can a comparison remain useful when future conditions or models are unsettled? | Stress-test declared performance and comparison claims across justified conditions; examine feasible adaptation where it matters. | Optimize one forecast or call an unspecified staged policy robust. | **Adapt:** :4.1–:4.4 and :4.6 return bounded holding and failure regions. Extra scenario and response analysis is accepted when a single forecast or assumed flexibility can conceal failure. | Lempert et al.'s [2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supplies the current robust-decision line; the [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) supplies pathway, timing, and failure-condition distinctions. Their applied domains do not supply universal thresholds, scenario probabilities, or local authority. | Reopen when an omitted condition, implementation lead time, or response constraint defeats the stated region. |
| Which sensitivity result should guide further inquiry? | Link local and joint sensitivity to the decision boundary and the value of attainable information. | Use output variance or a one-factor chart as a universal research priority. | **Adapt:** :4.3–:4.5 distinguish magnitude sensitivity, reversal, and probe value. More computation is justified only when the added question can change the bounded return; actual probe choice remains separate. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) is the synthesis candidate for sensitivity and information acquisition. Its formal approaches need their own model assumptions; `C.11` retains the local choice and probe-worthiness result. | Reopen when the feasible probe, decision window, dependency model, or costs change. |
| What if the value model, rather than the forecast, is incomplete? | Test relations across the models compatible with the expressed preferences. | Treat one fitted weight vector as uniquely known. | **Adapt:** :4.1–:4.4 retain value-dependent reversals instead of calling preference uncertainty factual noise. The deliberate trade-off is a possibly larger retained set. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) supplies robust ordinal regression as a best-known-line candidate for this question, not a requirement to use one algorithm or to collapse participants' values. | Reopen when elicitation or a legitimately governed value decision changes the compatible model set. |

### PSD.12:12 - Relations

- `PSD.11` may supply the consequence comparison and its evidence for the same configuration and horizon. Evidence enables this test but does not establish its result.
- `PSD.13` may consume robust regions, reversals, and information priorities as evidence for its recommendation. This neither entails the recommendation nor transfers the later choice authority.
- `A.10` governs bounded evidence reliance; direct domain and modeling practices govern the validity of claims, models, ranges, and tests. Changed actual source uses receive their direct revalidation rather than a blanket robustness assertion.
- `C.11` governs an actual local choice and the worth of another probe. Information priority, probe selection, WorkPlan, performed inquiry, and observed effect remain distinct results.
- Candidate formation, value elicitation, model repair, and follow-up remain their own questions when the test exposes a gap there. Missing or incompatible inputs require a qualified direct result or an exact stop, not an invented prerequisite lifecycle.

### PSD.12:End


# Part IV — Recommendation, Follow-up and the Development of Practice

<a id="psd-13"></a>
## PSD.13 - Prepare and Return a Decision-Support Recommendation

> **Type:** Method pattern (DPF)
> **Status:** Candidate
>
> **Primary working result:** a **decision-support recommendation account** for a named recipient, subject, horizon and receiving decision: the supported disposition, considered alternatives, reasons, source limits, material dissent, protected conditions, next use and reconsideration basis. The account may be a short return or a larger package; it informs the later decision without authorizing it.

### PSD.13:1 - Problem frame

**Use this when** analysis is available, or its decisive gap is known, but the recipient still cannot tell what the decision-support performer recommends and on what conditions. A score, workshop agreement or specialist answer is not yet a recommendation for this decision. The same need arises in an ordinary, non-contested request: “Which development direction should we consider over the next four months?”

Start with the receiving question and the strongest answer the available basis permits. Return a supported direction, retained or ranked set, bounded probe, smallest-result request, blocker or abstention. Do not force a single preferred action when the result actually supports a partial order or a missing-premise return.

Problem structuring and decision support is the wider practice. This pattern governs its **recommendation-composition and return branch**: turning qualified premises into advice usable by a particular recipient. It does not govern the recipient's choice, the specialist Methods that produced the premises, implementation, or proof that the advice caused an improvement.

The gain is practical: the recipient can distinguish what is recommended now, why, what remains unresolved, what must not be traded away, and what evidence would change the answer. A complete result can be two sentences when they identify one missing premise and the exact recommendation it prevents.

**Do not use this pattern** merely to reproduce an adequate recommendation, report one specialist result, or make a choice from an already adequate basis. Use the direct communication, supplying-practice or choice guidance instead. An unformed opportunity question needs opportunity construction before advice; an unsettled engagement question returns to `PSD.1`. Neither case requires a disagreement workshop unless formulation, participation or dissent actually changes the result.

### PSD.13:2 - Problem

A recommendation often becomes stronger while it travels. “This option performs better in this model” becomes “the best option”; “the group did not object” becomes “stakeholders agreed”; “the report was received” becomes “the decision was approved.” The lost conditions are precisely those the receiving decision needs.

Development advice adds a second failure. A plausible story can combine human learning, organization change and AI evaluation as if they supplied interchangeable evidence. A course catalogue then stands in for transfer into later Work, a position description for a whole-arrangement comparison, or a benchmark score for deployment safety.

The practitioner needs a positive composition rule, not just warnings. Which conclusion follows from these premises for this recipient? Which alternative remains live? Which missing result is worth requesting? When does declining to recommend supply the most useful answer?

### PSD.13:3 - Forces

| Force | Tension |
| --- | --- |
| Usable direction and warranted strength | The recipient needs an actionable answer; incomplete preferences or evidence may justify only a retained set or bounded question. |
| Synthesis and supplier ownership | Several results must become one account without absorbing their Methods, evidence limits or authority. |
| Clarity and material plurality | A short return is easier to use, but omitted dissent or an omitted alternative can reverse its meaning. |
| Timeliness and protected conditions | Delay has consequences, but urgency does not convert missing permission, consent or safety evidence into an admissible premise. |
| Professional judgement and recipient choice | An adviser should explain a reasoned position without making the recipient's values, mandate or commitment for them. |
| Continuity and changed conditions | An earlier recommendation may remain useful in part even when one configuration, source or assumption changes. |

### PSD.13:4 - Solution

Compose the recommendation at the strength and scope of its decision-bearing premises, then return it for the agreed use. The following moves express information dependencies, not a compulsory sequence of meetings or documents. Adequate existing results may close several needs at once.

#### PSD.13:4.1 - Recover the receiving use and the right to provide this advice

State who receives the answer, the exact subject or holder, the horizon, the question and the later decision or other Work that will use it. Recover the actual choice owner separately. A recipient may also be the choice owner when that authority is established; receiving an answer does not establish it.

Use an adequate `PSD.1` engagement result for the same subject and decision. Otherwise obtain the qualified direct facts or return the exact missing recipient, question, scope or authority premise. Do not infer the engagement from a title, course, department or tool output.

For development-direction advising, distinguish the recommending performer from the recipient at the grain of this application. The client, sponsor, holder, recipient and chooser may coincide in some respects and differ in others; recover only the differences that affect the advice, disclosure or later choice. A larger organization may contain both adviser and recipient. Merely naming two roles of one self-advisory actor does not create the distinct-performer engagement; direct domain and `C.11` guidance remain available.

Establish applicable professional scope, competence, material conflicts and permitted reliance before offering positive advice. For example, management-consultancy engagement and conflict conditions are informed by the [ICMCI competence framework v4.0, C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf). Human career-service consent and assessment limits come from the applicable professional source, such as the [NCDA 2024 Code of Ethics, A.2 and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395). These are different service conditions, not one universal profession or evidence that a proposed intervention works.

If a material mandate, competence, conflict or admissibility condition cannot be satisfied, return the scoped blocker or appropriate referral. A persuasive presentation cannot repair that condition. Existing emergency, safety or legal response duties retain their own direct authority and must not wait for completion of a PSD account.

#### PSD.13:4.2 - Recover what the available premises actually support

For every premise that can change the disposition, recover its claim, exact subject and configuration, source or supplier, applicable window, intended use, uncertainty and reliance limit. Inspect available results first; use `A.15.9` to reuse an adequate result or request the smallest missing one, and `A.10` to qualify the actual reliance. This pattern adds no second specialist-acquisition Method.

Read a comparison as a result over particular alternatives under particular values, evidence and assumptions. A `PSD.12` robustness result contributes only where it can change this recommendation for the same configuration and horizon. It neither entails the whole recommendation nor authorizes the later decision. Preserve the `PSD.9`–`PSD.11` comparison basis needed to interpret it.

Keep the live set and the compared subset explicit. A result about internal development and one mixed human–AI arrangement does not dispose of an external provider or a materially different probe. A gap about one candidate can prevent ranking that candidate while leaving an independent comparison usable. Do not narrow the set simply because evidence is easier to obtain for the familiar option.

Preserve material agreement, disagreement and affected-party concerns from `PSD.7` or a qualified direct account. Distinguish a factual objection, a value conflict, an authority condition and a question about representation; they call for different responses. Give the objection and its consequence enough prominence to survive the return. Attribution and disclosure must respect the applicable protection and confidentiality conditions.

For development opportunities, consume a qualified opportunity result: the problem or promise, dependencies, bounded reachability, uncertainty and next question. A search/archive entry, a fashionable technology or a candidate label supplies none of those by itself. Opportunity construction is a separate Method with an independently useful result; composing advice does not complete missing search, dependency or reachability work.

#### PSD.13:4.3 - Select the warranted recommendation disposition

Ask what the recipient can responsibly consider **now**, given the question, alternatives, protected conditions, comparison and consequence of delay. Explain the inference from the relied-on premises to the disposition. The six forms below are result branches, not stages to complete.

| Disposition | Positive basis and useful return | Boundary |
| --- | --- | --- |
| Retained or ranked set | Several directions remain live. Return the warranted order, partial order or trade-offs and the unresolved distinction that could narrow it. | A retained set is not consensus; an order valid under one scheme is not a universal ranking. |
| Supported direction | Qualified premises and a declared decision-support rule justify preferring one direction for this use. State the advantage and the conditions under which it holds. | Other candidates need an explicit disposition; protected conditions cannot disappear into a compensating score. |
| Bounded information-gaining probe | A specified uncertainty could change the advice, and a qualified probe is feasible and proportionate to the delay, burden and risk it introduces. Name the question, bounded exposure, useful evidence and stop. | Thin evidence alone does not justify a probe. The probe's authorization, WorkPlan and execution remain separate. |
| Smallest-result request or handoff | A named practice can supply the exact missing comparison, feasibility, interpretation or other result that would change the answer. State what is needed and which branch remains open. | Request the premise, not that the supplier take over the whole recommendation or choice. |
| Blocker | A missing, stale, incompatible, inadmissible or unauthorized premise prevents the requested responsible recommendation. Name the premise, affected use and what would resolve or reroute it. | State any still-usable partial result; do not convert uncertainty into either a confident negative or a positive recommendation. |
| Abstention | The recommendation premise itself fails, or the requested kind of advice cannot responsibly be supplied within the engagement. State the failed premise and the correct receiving account where one exists. | An abstention is not an adverse factual finding about the subject and is not abandonment of any obtaining professional duty. |

A mixed answer can be useful if its scopes are unmistakable: retain two directions, request one missing comparison, and block a stronger ranking. Do not present these as contradictory overall statuses.

The strength of each claim stays inside the narrowest material limit of the premises on which **that claim** depends. If one input supports only a particular AI configuration, the recommendation cannot silently extend it to another. If an unused source expires, it does not invalidate unrelated claims merely by appearing in the same bibliography.

When a total order is unwarranted, prefer an explicit partial answer to invented weights or probabilities. When the declared scheme does support one direction, do not conceal that conclusion behind an uninformative list. Explain why a serious remaining alternative loses for this use, and what would reverse that judgement.

#### PSD.13:4.4 - Make the recommendation account inspectable at the smallest useful size

The account is a claim-bearing result, not a mandatory template or new record kind. A short message may carry it; a consequential institutional matter may need a larger package and protected annex. Keep the following content recoverable wherever it can change reliance.

| Position | Decision-useful content |
| --- | --- |
| Receiving frame | Recipient, recommending performer, holder or subject, question, horizon, choice owner, receiving decision and next Work. |
| Candidate domain | Considered alternatives, compared subset, exclusions with their basis, retained alternatives and any candidate gap. |
| Relied-on premises | Exact results and relevant source editions or dates, configurations, qualification windows, evidence limits and supplying owners. |
| Comparison and inference | Scheme, material trade-offs, protected conditions, robust regions or reversals, and the reasoning that supports the disposition. |
| Unresolved content | Material uncertainty, dissent, evidence losses, unsupported extensions and what each prevents. |
| Return | One or more explicitly scoped dispositions and the next consideration, request, reroute or separately governed choice they support. |
| Reconsideration | The source, observation, configuration, threshold, authority, horizon or candidate change that could alter a specified claim or disposition. |

Put the disposition and its most important limit first. Keep the evidence and reasoning reachable without requiring the recipient to reconstruct the entire analysis. Where a protected annex limits access, the accessible return must still state the resulting reliance restriction; it must not hide that a decisive premise is unavailable to the recipient.

A threshold in this account needs a source and an owner for its meaning. “Reconsider when recovery evidence no longer supports the continuity condition” is useful only if the named evidence, condition and receiving question can be recovered. `PSD.14` designs how such evidence will be obtained and interpreted. If a positive recommendation depends on ongoing observation, an unassigned or infeasible observation obligation is a material limit now, not an administrative detail to repair after handoff.

#### PSD.13:4.5 - Return the advice without taking the later choice

Make the result available to the actual recipient in a form suited to the agreed use. For a receiving-use question, apply `A.2.9`: what should the recipient understand or do, what evidence is enough to judge that, and what smallest repair or stop follows? Explaining the conditional nature of a ranking may be necessary; obtaining agreement with it is not the same task.

Keep the communicative Work, recommendation content, carrier, recipient response and later effect distinct. Delivery establishes neither understanding nor reliance, consent, choice, implementation or effectiveness. A recorded acknowledgement may support receipt; it does not establish an authorized decision. A communication can perform an authorization only under its own actual performer, authority and institutional conditions.

The authority-holding System may later choose, reject, retain alternatives, commission a probe or reroute under `C.11` or its direct domain rule. A corporate organ may consume the recommendation and unresolved disagreement through `CGOV.11`; that organ, not this account, performs the authorization Work. Do not require a corporate-governance framework where the actual decision is personal or otherwise outside its subject.

Returning the advice closes this recommendation application, including an honest stop branch. Later premise refresh and a newly composed recommendation are later work. Any promised professional contact, referral or service closure remains governed by the actual relationship; closing this application neither invents nor cancels those duties.

### PSD.13:5 - Archetypal Grounding

The examples are hypothetical. Assumed specialist results illustrate the pattern; they assert no real public decision, client assessment or intervention effectiveness.

#### PSD.13:5.1 - A pump comparison that cannot yet choose an investment

An East-District authority asks a separate analysis team for advice on flood-pump investment for the coming season. Its receiving decision is whether and how to commit funds. The live candidates include a baseline `N`, fixed pumping `F`, mobile pumping `M` and staged combination `S`.

The qualified numerical slice concerns pumping-service loss and incremental cost, not the whole public consequence. In the stated model, `F` has loss 2 in normal access and 3 with road loss, at cost 8; `M` has loss 1 and 9, at cost 5. The baseline and staged alternative are not closed by this two-option comparison. Reachable assistance, property consequences and protected conditions still require their direct evidence and value judgements.

A sensitivity result supplies the conditional boundary `7p > 1 + 3λ` for `F` to have the lower weighted loss, where `p` is the assumed road-loss probability and `λ` the declared cost weight in this illustrative model. Neither value has been established for the actual investment question. With `λ = 0.5`, `p = 0.2` favours `M`, while `p = 0.6` favours `F`. This is evidence of a possible reversal, not evidence that either probability obtains.

The team returns:

> Retain fixed and mobile pumping for the current pumping-service/cost comparison. A whole-investment recommendation is blocked by the unqualified road-access basis, unresolved assistance and protection consequences, and the unclosed baseline/staged branches. Request the smallest consequence and access results needed to resolve those distinctions. The current model favours different options under different declared assumptions; it does not justify a preferred investment. Reconsider the affected comparison when those results or the authority's value and protection premises change.

A material objection about reachable assistance remains in the return, not buried below the numerical result. The authority can decide what further evidence to commission under its own mandate. Neither the request nor the conditional comparison authorizes spending, a public trade-off or an operational response.

#### PSD.13:5.2 - Development advice with a positive branch and an honest gap

A committee asks a separate advisory team which direction to consider for ninety-day service reliability. The holder is the service organization; the committee is recipient and, by the assumed mandate, choice owner. Internal development, an external provider and a mixed human–AI arrangement are live directions. Critical-service continuity, a security boundary and a bounded budget are protected.

An operations account, position/interface account and strategy priority are available, but none compares the whole obtaining arrangements. The first complete return is a smallest-result request: obtain the allocation comparison for this service, horizon and protected conditions. Until then, the adviser cannot rank the three directions. A published Method for obtaining that result is not the client-specific result.

For a separately stated continuation, suppose qualified allocation and security results now cover all three directions. They support a bounded mixed-arrangement probe, retain internal development, and exclude this provider configuration under the security condition. The probe evidence question, feasibility, exposure and stop are supplied rather than invented. The adviser can then recommend considering that probe first while retaining internal development; throughput remains uncertain and the protected conditions remain binding. These new premises, not a change of wording, permit the stronger answer.

This continuation does not promote an earlier I/H-only comparison into full-set closure. A different provider, a materially different probe, or model configuration B needs its own qualification. If the mixed result covered only configuration A, advice about B remains a request or blocker while independently qualified internal-development content can still be returned. The committee's later choice and probe WorkPlan are separate.

A material provider interest must be disclosed and treated under the engagement's conflict conditions before this positive advice is relied on. A sponsor wanting one supplier does not settle the holder's need or the committee's choice.

#### PSD.13:5.3 - Unlike holders and ordinary non-use

For a person asking a separate adviser about four months of engineering-management development, a course attendance record does not establish transfer into representative later Work. Without the relevant capability, intervention, resource, consent and transfer premises, return the exact missing-result request. When qualified premises support two directions but not their order, return a retained set and the discriminating question. The person's later choice remains theirs under the applicable conditions.

For an authorized team considering an AI scaffold or human–AI allocation, name the exact changed object, version, environment, evaluation validity, oversight and protected conditions. Use AI/security and, where relevant, organization-allocation results. A human learning study or a ranked recommender-system output does not establish those premises. If a known inadmissible configuration cannot meet the protected boundary, block that recommendation; if the evidence is merely absent, name the gap rather than claiming failure.

For a non-cultural population or lineage with no population-local recipient or chooser, abstain from attributing a recipient-owned development recommendation to it. Return population change to its evolutionary account. A separately authorized research team considering an intervention is a different recipient-owned case with scientific, safety and governance premises; naming that case establishes none of them.

For a chooser who already has an adequate option set and needs only to make their own decision, use direct domain or `C.11` guidance. Neither an adviser nor a PSD return package needs to be invented.

### PSD.13:6 - Bias-Annotation

A decisive-sounding answer can conceal uncertainty, but perpetual qualification can also conceal a warranted recommendation. Test both errors: what stronger claim is unsupported, and what useful claim is being withheld despite adequate premises?

Sponsor preference, provider interest and model convenience can shape the candidate domain before the recommendation is written. Inspect exclusions and unclosed branches, not just the displayed winner. Preserve material dissent without implying that every view has equal evidential support or that unanimity is required.

An available numerical score may dominate attention while a consent, continuity or access condition is left in prose. Keep non-compensable conditions visible at the point of disposition. Conversely, do not invent a protected condition from the adviser's personal preference.

### PSD.13:7 - Conformance Checklist

**Recognition** asks whether recommendation composition is the missing result: a named recipient needs an answer that combines qualified premises, and the account can change their next consideration. One direct input check and a short request or blocker can close a small use.

**Assurance** asks whether this particular disposition is warranted for its intended reliance. Consequential uses add the direct domain's evidence, competence, independence, consent, safety, security, institutional and validation conditions; the size of the account does not lower them.

| Check | Sufficient answer |
| --- | --- |
| Receiving use | Recipient, subject, horizon, recommending performer, receiving decision/Work and separate choice boundary are recoverable. |
| Premise fit | Every decision-bearing input fits its actual configuration, window and use, or its gap and consequence are explicit. |
| Candidate and comparison coverage | The live set, compared subset, retained alternatives, exclusions, scheme and material reversals are visible. |
| Warrant | The inference supports the stated disposition without inventing preferences, probabilities, authority or supplier results. |
| Conditions and dissent | Material protection, disagreement, evidence loss and professional restrictions survive the return. |
| Use and reconsideration | The recipient can find the next use and exact reason to reconsider; required observation is feasible or named as a limit. |
| Result boundaries | Recommendation, communication, later choice, WorkPlan, implementation and effect have not been substituted for one another. |

If one check fails, repair or narrow the affected claim, request the missing result, or return the honest stop. Do not erase independently usable content to make the account look uniform.

### PSD.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Copy the highest score into “we recommend” | Recover the candidate domain, preference/evidence conditions and decision-support inference; retain a partial order when that is all they support. |
| Make a stronger recommendation by omitting an inconvenient branch | State the compared subset and the unclosed alternative or objection, with its effect on the answer. |
| Treat a specialist answer as the whole advice | Preserve supplier scope and compose only the inference that this recipient's question still needs. |
| Use a probe as the default answer to uncertainty | Name the decision-changing question, feasible evidence, exposure, delay and stop before recommending the probe. |
| Turn delivery or agreement into authorization | Obtain the later choice and authority evidence separately; repair understanding without seeking manufactured consent. |
| Offer a universal development prescription | Recover holder-specific premises; return the smallest gap where human, organization and AI evidence differ. |
| Hide a blocker behind a long report | Lead with what cannot yet be responsibly recommended and the exact result that could change it. |

### PSD.13:9 - Consequences

The recipient gains a bounded answer that can be challenged, declined, acted on through the proper decision, or refreshed without reconstructing the entire engagement. Partial results and honest stops become usable outputs rather than signs that the analyst failed to choose.

The cost is explicit reasoning at the boundary between analysis and advice. Some requests cannot be closed with a single direction, and some attractive probes remain unsupported. This preserves the distinction between useful decision support and a persuasive but unwarranted prescription.

### PSD.13:10 - Rationale

Recommendation composition has work left after generic evidence, comparison and choice guidance. Evidence can support a claim without determining what to advise; a comparison can leave alternatives unresolved; a choice rule belongs to the later decision. This pattern connects those qualified results to one recipient's question and makes the supported disposition intelligible.

The six return forms avoid two extremes: treating every uncertainty as failure, and treating every engagement as a duty to name a winner. They do not replace domain decision rules. The narrowest-material-premise rule applies claim by claim so that one failed branch neither contaminates unrelated advice nor disappears inside an overall positive answer.

### PSD.13:11 - SoTA-Echoing

The practice question is **how to return useful advice from qualified analysis without manufacturing a complete order, professional competence or recipient choice**. The selected line combines explicit decision-analysis warrant with a source-bounded professional return. Its additional explanation costs effort; that cost is justified where a lost condition could change the next decision, and is reduced to a short return in a simple case.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| How does comparison become advice? **Adapt** structured preference-to-recommendation reasoning, preserving the actual problem and model conditions. | A single score is economical when a justified model covers the question. It fails when incomplete preferences or an unclosed candidate branch are silently filled in. Sections 4.2–4.4 require the scheme, inference and scope rather than banning scalar comparison. | [Greco, Słowiński and Wallenius (2025), *Fifty years of multiple criteria decision analysis*](https://doi.org/10.1016/j.ejor.2024.07.038), is a best-known-line synthesis of finite-action MCDA and different preference-to-recommendation procedures. It supplies neither this engagement's values nor universal superiority of one procedure. Reopen when a rival gives equally warranted advice with materially lower burden, or the finite-action/model assumptions cease to fit. |
| What must accompany technically supported organizational advice? **Adapt** explicit engagement, client involvement and conflict qualification. | A technically correct memo can suffice for a bounded analytical request. It is insufficient when reliance also depends on mandate or a material provider interest. Sections 4.1 and 5.2 keep those conditions with the advice. | [ICMCI v4.0 (2021), C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), is a substantive professional comparator, not a universal procedure or effectiveness study. Reopen on a changed applicable service rule or evidence that this qualification omits a material relationship condition. |
| What makes a human career return usable? **Adopt within that service** intelligible basis, consent and competent assessment use; retain referral where required. | Generic “best next course” advice is shorter but can conceal the person's receiving question and unsupported assessment. Sections 4.1, 4.5 and 5.3 retain these boundaries while leaving intervention and transfer evidence to their owners. | [NCDA Code of Ethics (2024), A.2, A.10 and E.1–2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), is a profession-specific normative comparator. It proves no learning effect and supplies no AI-holder assessment rule. Reopen when the actual service or applicable professional conditions change. |

### PSD.13:12 - Relations

- `PSD.1` supplies the bounded engagement question for the same subject and receiving decision. Its availability does not establish the particular mandate or impose temporal order.
- `PSD.7` supplies material shared and contested claims. They inform the recommendation without settling the later choice.
- `PSD.8`–`PSD.11` supply the candidate, value, uncertainty and comparison results needed to interpret the advice. `PSD.12` supplies robust regions, reversals and information priorities only where they can change this recommendation for the same configuration and horizon.
- `A.15.9` supplies inspect–reuse–request–qualify for external results; `A.10` governs their actual reliance. Holder practices retain facts, Methods, protected conditions and conclusion authority.
- `A.2.9` supplies receiving-use judgement and the distinction between communication and its institutional effects. `C.11` or the direct domain rule owns the later choice; WorkPlan, Work and effect remain separate.
- `PSD.14` uses this recommendation to establish which later decision, consequences, signposts and premise changes matter. It obtains later authorized decision and implementation evidence as distinct results; this recommendation supplies neither.
- `CGOV.11` may use the recommendation and unresolved disagreement for the named corporate matter. Only the authority-holding System supplies the authorization Work.
- Missing, stale, out-of-scope or incompatible contributions call for an adequate qualified direct result or the exact missing-result return. A neighboring pattern, profile or source being available does not supply a performed result or require a complete language traversal.

### PSD.13:End


<a id="psd-14"></a>
## PSD.14 - Prepare and Use a Decision Follow-up Arrangement

> **Type:** Method pattern (DPF)
> **Status:** Candidate
>
> **Primary working result:** a **follow-up arrangement and qualified current decision-support return**: what will be observed and interpreted, by whom and when, which recommendation or decision premise it can change, and what remains usable, must narrow, is blocked, needs a named contributor reopened, or warrants a later recommendation.

### PSD.14:1 - Problem frame

**Use this when** a recommendation or decision depends on conditions that may change, but nobody can yet say which observations matter, who will interpret them, or what result they should reopen. Also enter directly when a new source, configuration, observation or authority condition may have made existing advice stale.

A project may have a dashboard but no way to connect an alert to a particular assumption. An adviser may have promised to “check back” without establishing access to the receiving decision or its consequences. A revised AI evaluation may concern configuration B while the recommendation still relies on configuration A. In each case, more reporting alone does not close the gap.

Problem structuring and decision support is the wider practice. This pattern governs **follow-up of a structured decision and its supporting recommendation**. The regulated move is to design and use the connection from decision-significant observations to affected support results. Generic source currentness, domain operations, implementation control, strategy choice, professional service management and cultural continuation retain their own Methods.

The practical gain is a timely, bounded return: the advice still holds under stated conditions; a claim must narrow; a premise is missing; one contributor must revise its result; or a new recommendation is needed. The practitioner can preserve unaffected useful content without silently preserving an invalid whole.

**Do not use this pattern** when an existing adequate arrangement already covers the exact follow-up question and has no material change. Use it without redoing earlier framing or facilitation when the decision is already bounded and uncontested. Use the direct operation or emergency rule for an immediate operational response, and the direct currentness rule for a source-maintenance question that has no decision-support consequence.

### PSD.14:2 - Problem

A recommendation, a later authorized decision, implementation and observed consequences are different results. Yet follow-up often treats the recommendation as evidence of what was chosen and treats a plan as evidence of what was done. A missing report then looks like “no change,” and any later improvement looks like success of the advice.

The reverse failure is indiscriminate reopening. Every source revision, new observation or changed model version causes the whole engagement to restart, even when only one candidate or consequence claim relied on the changed premise. Useful independent results are delayed while the actual gap remains poorly specified.

Follow-up therefore needs both a designed observation arrangement and a claim-level return. A list of indicators is incomplete without an interpreting owner, a qualified receiving use, a timely route and an honest answer when access or evidence fails.

### PSD.14:3 - Forces

| Force | Tension |
| --- | --- |
| Timely warning and observation burden | Frequent data may detect changes sooner, but collection, interpretation and response have costs and can overwhelm the receiving work. |
| Focused learning and unexpected change | A targeted test can resolve a decisive question while overlooking a new concern outside the original model. |
| Continuity and justified revision | Stable advice avoids needless churn; preserving a conclusion after its premise fails creates false confidence. |
| Shared follow-up and differentiated authority | One arrangement connects observers, specialists, advisers and choosers without giving them each other's powers. |
| Trigger clarity and uncertain evidence | An explicit condition helps action, but a noisy measure or an unqualified threshold cannot decide the response. |
| Service continuity and a bounded engagement | Follow-up may require real client contact or referral while the completed recommendation application remains complete. |

### PSD.14:4 - Solution

Design follow-up around the claim or decision that could change, not around the data easiest to collect. Compare feasible arrangements, establish the necessary observation and interpretation work, and later return the smallest warranted change. Preparation may begin before recommendation delivery; actual observation and renewed advice remain later work.

#### PSD.14:4.1 - Recover the recommendation, decision and implementation separately

Name the receiving question, subject, horizon, recipient, choice owner, relevant alternatives, protected conditions and the recommendation's current disposition. An adequate `PSD.13` result supplies what was advised and why. If it is unavailable, stale or outside the present use, recover a qualified direct account or state the exact gap.

Then ask what is actually known about the later decision. Obtain evidence of the authority-holding System's authorized decision from that System or a qualified direct source, under the direct authority and `A.2.9` conditions. Distinguish a choice to commission a study, a choice of an intervention, rejection of the advice, and no established decision. A recommendation or its receipt proves none of them.

Recover implementation and consequence evidence only to the extent the current question needs it. A WorkPlan establishes intended work, not performance. An implementation report must support what was actually done, under which configuration and interval; an observation must identify what was observed and its limits. Whether the advice or action caused an effect requires the direct causal evidence and guidance, not chronology alone.

A useful current return can therefore be: “The recommendation remains conditional; the receiving decision is not yet established; no implementation consequence is claimed.” Unknown decision status must not be silently converted into continuation of a selected action.

#### PSD.14:4.2 - Name the premises and observations that can change the answer

For each material condition, connect the premise to the recommendation claim, compared alternative, model, protection condition or problem boundary that uses it. State what difference would change the current decision-support result and who can supply or interpret the needed evidence.

The observation may concern an expected consequence, an assumption, a new opportunity, a source's qualification, a participant's material objection, a protection breach or a changed authority condition. It need not be a numeric metric. A new affected group can reopen scope even while existing performance indicators remain favourable.

Use a small relation account such as the following; it is ordinary working content, not a prescribed register.

| Follow-up position | What must be recoverable |
| --- | --- |
| Current premise and receiving use | The exact claim, configuration, horizon and recommendation or decision-support result that relies on it. |
| Observation or source return | What evidence could test or change it, from which observation, supplier, participant or authoritative source. |
| Interpretation | Who can qualify the evidence, under what Method and uncertainty, and who judges its decision significance. |
| Signpost and reconsideration condition | The observable indication, the condition that makes reconsideration necessary, and the source of any threshold or protected limit. |
| Timing and access | When evidence is needed, delay in obtaining and interpreting it, access and disclosure conditions, and the effect of a missed observation. |
| Next result and owner | Which source, model, comparison, formulation or recommendation would change, and who retains the later choice or operational authority. |

A **signpost** is something watched because it can reveal a material change. A **reconsideration condition** states when that information requires a named question to be reopened. Neither is automatically a decision to change action. An operational rule may separately authorize a response to a defined signal; its authority and conditions must be established through that rule.

Choose timing from the consequence of late knowledge, not a universal calendar. If observation plus interpretation and authorized response would arrive after the relevant decision window, move the observation earlier, choose a feasible proxy with its limits, change the arrangement, or return that the promised follow-up is not adequate. Do not invent a threshold to make the table complete.

#### PSD.14:4.3 - Generate and compare follow-up arrangements

Consider genuinely different ways to obtain a useful return. Possibilities include a recipient-owned scheduled review using existing evidence, a targeted specialist test before a commitment, event-driven notification with qualified interpretation, or a coupled arrangement combining targeted tests with a limited route for unexpected changes. A justified one-off return with no continuing service may be enough for a short, low-consequence use.

Compare coverage of the material questions, detection and interpretation delay, uncertainty, participation, observer independence where required, effort, confidentiality, cost, and the feasible receiving response. Do not maximize the number or frequency of indicators. A technically precise observation is of little use if no authorized or competent receiver can act on its meaning in time.

Targeted monitoring tests a named question; broader observation can reveal unexpected change. Their balance is a design choice for this decision. The distinction is supported by the current environmental decision-support discussion in [Manley, Povak, Reynolds and Hessburg (2026), Discussion / “Change is inevitable, learning is critical”](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2026.1783129/full); it supplies neither a universal monitoring mix nor an effect guarantee for other domains.

Use a `PSD.16` conflict/facilitation-architecture result only if it constrains this design choice. For example, a material participant correction must reach the analyst before the comparison is used, or an observer cannot also carry an incompatible facilitation burden. The constraint does not choose the follow-up arrangement. Generate and compare alternatives that respect it; return to `PSD.16` only when the underlying interference itself needs a different decision.

Use `A.22` when the selected organization of independently identified constituents and obtaining relations is itself the subject of a structure claim. A proposed arrangement remains a design description until the required participants, access, assignments and relations are established. A diagram or a filled table does not establish the arrangement, its adequacy or its work.

#### PSD.14:4.4 - Establish a viable observation and return arrangement

Name who will observe, who will interpret, who receives the qualified result and who owns any resulting decision. Establish the assignments, capability, access, resources, timing and protection needed for those particular contributions. Several functions may be carried by one performer where suitable; distinguish them when competence, independence, workload or authority makes that difference material.

State what happens if the observer cannot obtain the evidence, the source becomes unavailable, the interpreting owner changes, or the evidence arrives too late. A failed observation is not a favourable observation. Return the gap and its effect on current reliance to the named receiver; use any existing authorized escalation or protection rule when it applies.

Where an actual professional service exists, fit contact, confidentiality, referral and closure to that service's conditions. The [NCDA 2024 Code, A.10 and B.1](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), for example, constrains continuity and information sharing in career services; it creates no AI-holder duty or universal follow-up contract.

Before relying on the arrangement, test the decisive connection at proportionate cost: can an example material observation be obtained, qualified, delivered and understood as the named reopen question in time? A prospective walkthrough can expose an assignment or interpretation gap; it proves neither later enactment nor empirical effectiveness. Use stronger domain validation when the consequence requires it.

Record whether the result is a proposed arrangement with conditions, an established arrangement ready for its bounded use, or a blocker. Do not promise observation that has no capable performer or permitted source. State the closing or review condition for the arrangement so that a bounded recommendation does not create indefinite unowned monitoring.

#### PSD.14:4.5 - Interpret actual observations before revising advice

When evidence arrives, first establish its subject, configuration, interval, provenance, Method, uncertainty and allowed use. A current source label alone is insufficient. Use `A.10` for the actual reliance and `A.15.9` to obtain a missing specialist interpretation without taking over that practice.

Compare the qualified evidence with the exact condition it was meant to test. Distinguish a change in the world, a changed source claim, an expired reliance window, a changed value judgement, a revised model and a merely changed representation. They can all matter, but they need different repairs.

A source changing from A to B does not establish that advice about A is now valid for B. Preserve the earlier result for its earlier subject and conditions; obtain qualification for the current one. Similarly, failure to observe a threshold crossing proves nothing unless the observation coverage and sensitivity support that inference.

Keep the observations and their interpretation distinct from the next decision. If an authorized owner supplies a changed action decision, recover it separately. If the adviser concludes that a different action should be considered, that is renewed advice, not implementation control.

#### PSD.14:4.6 - Return only the affected decision-support consequence

Trace the changed premise into the particular claim or disposition that relies on it. Preserve inspected independent results for their current conditions. If dependence or coverage remains unresolved, state that gap; do not label an uninspected branch unaffected.

| Current return | When it is warranted | What happens next |
| --- | --- | --- |
| Unchanged within stated conditions | Qualified evidence does not alter the relied-on premise, or the changed claim is outside the inspected use. | Retain that bounded advice and its current conditions; state the next material observation or end of use. This is not authority to continue an intervention. |
| Narrowed | A useful portion still has an adequate basis, but the previous scope, configuration, window or strength is no longer supported. | Return the surviving claim and the withdrawn scope explicitly. Do not relabel the narrowed result as the original whole. |
| Blocked for the affected use | A necessary premise, authority condition, observation or interpretation is unavailable or no longer adequate. | State what cannot responsibly be advised or relied on now, the missing basis and the receiver who can resolve or reroute it. Preserve separate usable content. |
| Reopen a named contributor | The changed evidence calls for a specific source, candidate, value, uncertainty, model, consequence, robustness or scope result. | Request that smallest result through its direct owner. The pending request is not the refreshed result. |
| Compose a later recommendation | Changed qualified premises require a different disposition or a newly composed answer to the receiving question. | Use `PSD.13` with the current premises and remaining gaps. Preserve the earlier recommendation occurrence and the separate later choice. |

These are scoped conclusions, not a universal status system or a five-step lifecycle. One event can leave an internal-development claim unchanged, narrow a mixed-arrangement claim to configuration A, block advice about B, and reopen its evaluation supplier. Only the affected combined recommendation needs recomposition.

Keep **continue, adjust, refresh and reframe** precise. Continuing reliance on unchanged advice is a decision-support return. Adjusting a selected action requires the competent owner and its authorized decision, even if the original formulation remains adequate. Refreshing a model or evidence invokes its supplier and does not itself change action. Reframing reopens the problem or boundary through `PSD.3` or `PSD.4` when the old question no longer covers the material situation.

For one known reliance question, use `A.10` and the direct subject guidance. If a changed source requires discovering and revalidating several actual receiving uses, use `A.10.1` for its bounded search, coverage, direct-reliance test and subject-result return. Citation or adjacency is not dependence. Use `G.11` for currentness, decay and scoped refresh planning/reporting when that is the live result; neither pattern supplies a new domain conclusion or recipient choice.

#### PSD.14:4.7 - Close the present return and preserve the next useful question

Return what was observed, how it was qualified, which premises and uses were affected, the current disposition, unresolved gaps and the next responsible receiver. Preserve enough of the prior recommendation, decision and evidence to distinguish a later reassessment from a claim that the earlier Work was different.

Close when this bounded follow-up question has a supported answer or an explicit blocker and its receiving use is clear. Continue an obtaining observation or service arrangement only under its own scope and end condition. A completed recommendation application does not become an indefinitely unfinished application merely because later follow-up exists.

When follow-up evidence can change the decision-support Method repertoire, supply the bounded case, conditions, failure or useful variation to `PSD.15`. Its owner still compares the repertoire and obtains its own result. One successful delivery, revised diagram or favourable outcome proves neither general Method effectiveness nor cultural continuation.

### PSD.14:5 - Archetypal Grounding

The examples are hypothetical. Proposed arrangements, assumed authorizations, observations and qualified supplier returns are named separately to make their different effects inspectable.

#### PSD.14:5.1 - Follow a blocked flood-pump recommendation without inventing a decision

The East-District analysis team has returned a conditional fixed/mobile pumping comparison and blocked a whole-investment recommendation. The road-access basis, reachable assistance and protection consequences, and baseline/staged branches remain unresolved. There is no established investment choice to “monitor.”

The follow-up question is which missing evidence can reach a renewed investment consideration before the coming season. A prior engagement-arrangement decision requires material participant corrections to reach the analyst before any comparison is treated as closed. The follow-up designer uses that constraint, not a prescribed meeting sequence.

Three arrangements are compared. An end-of-season review is inexpensive but too late for the receiving decision. Continuous pump telemetry gives frequent technical data but does not resolve deployment permission, affected residents' access or the unanalysed staged alternative. A bounded pre-decision evidence arrangement obtains targeted logistics and consequence results, admits material participant corrections through the facilitator, and gives the analyst an interpretation window before the authority next considers investment.

The third arrangement is selected in this illustration because the named logistics and consequence suppliers, facilitator and analyst have the required availability and access, and the authority's next consideration date is known. It costs a small additional interpretation meeting. If any decisive supplier cannot return in time, the arrangement reports that limitation and preserves the blocker; it does not quietly move the decision deadline or claim the authority has agreed.

In the continuation, the authority supplies qualified evidence that it has authorized an access study, not a pump purchase. The study's performer then returns evidence that the mobile deployment arrangement assumed in the earlier comparison is unavailable for the required flood-period window. The analyst does not substitute a guessed road-loss probability.

The current return is: preserve the earlier fixed-pump performance claim for its original conditions; narrow the earlier fixed/mobile comparison to the prior deployment basis; block its current investment use; reopen the exact mobile-deployment and consequence inputs. The assistance and staged-alternative gaps remain open. The authority's study decision is recorded separately from the unchanged absence of a qualified investment decision.

The arrangement also preserves a route for a newly identified affected group to raise a material access concern. That concern would reopen the boundary question rather than merely add another performance reading. No favourable pump metric can by itself close that question.

#### PSD.14:5.2 - One changed AI configuration need not restart all advice

For a ninety-day reliability question, a committee received advice to consider a bounded mixed human–AI probe while retaining internal development. Assume the advice relied on qualified whole-arrangement, security and evaluation results for configuration A. A separate supplied decision shows that the committee authorized only a bounded probe under specified continuity and oversight conditions.

The follow-up designer compares a monthly report, an automated outcome stream without specialist interpretation, and configuration-change notification combined with a targeted probe-evidence review. The monthly option is too slow for the reversible-probe decision window. The stream alone cannot establish that a new scaffold or tool environment is covered by the previous evaluation. The combined option is selected only after the configuration owner, evaluation supplier, adviser and committee have the necessary notification, access, interpretation and receiving arrangements.

Now a configuration-change notice identifies B. That notice is evidence of a changed object, not evidence of B's quality. The probe observation covers B, while the relied-on evaluation still covers A. The response is deliberately split:

| Inspected use | Current consequence |
| --- | --- |
| Internal-development claim whose premises did not use A's evaluation or the changed allocation | Remains usable for its named service and horizon. |
| Earlier mixed-arrangement recommendation for A | Retained as the earlier conditional result; it is not qualification of B. |
| Advice to extend the probe or deploy B | Blocked pending the exact B evaluation, security and allocation premises that can change that advice. |
| Need for renewed comparison | Reopen only the suppliers and comparison claims that actually use the changed configuration; compose a later recommendation when their qualified returns support one. |

The configuration notice does not choose a fallback, stop a service or revoke a permission. If an existing authorized continuity or safety rule governs B, its competent owner applies it separately; otherwise the choice or authority gap is returned promptly. The adviser must not keep an apparently positive recommendation by treating silence from the evaluation supplier as approval.

The same locality works with a human development premise. If an employee's available practice time changes, requalify the affected intervention and transfer claim rather than rewriting unrelated organization or AI evidence. Applicable client-contact conditions may require a conversation, but that conversation does not itself establish transfer or consent to a different intervention.

#### PSD.14:5.3 - Cheap use, missed observation and proper stop

A recipient has one short, reversible comparison whose evidence remains valid until a named review date. Existing assignments and access already provide the only observation that can change it. Retain that arrangement; no dashboard or recurring workshop is needed.

If the named observation is missed, the current answer is the scoped evidence gap and its effect on reliance, not “unchanged.” If the receiving decision has ended and no continuing evidence, service or protection obligation remains, close this follow-up use with its final qualified return. Do not manufacture ongoing monitoring.

A population without a population-local recipient or choice owner does not acquire either through a follow-up table. Preserve the abstention from that recommendation use. A research team's separately authorized intervention has its own decision, experimental Work and observation conditions.

### PSD.14:6 - Bias-Annotation

Confirmation bias favours observing only the consequences that made the recommendation attractive. Include the discriminating failure and an affordable route for material unexpected change. Avoid turning this into exhaustive surveillance: the receiving decision and possible loss still bound effort and access.

Automation bias can make an alert look like an interpreted result or authorized command. Separate collection, qualification, judgement and decision even when software assists several of them. A human label alone also proves neither competence nor independence.

Outcome bias can rewrite the earlier advice as obviously correct or wrong after the event. Judge the earlier recommendation against its then-current premises and intended use; judge the later return against the changed evidence. A causal effectiveness claim remains a separate question.

### PSD.14:7 - Conformance Checklist

**Recognition** asks whether an observation or changed premise can alter current decision support and whether the path to a useful return is missing. One existing adequate result or one clearly scoped gap can close a small case.

**Assurance** asks whether this arrangement can obtain and qualify the needed evidence in time, and whether the actual current return follows from it. Consequential uses require their direct observation, validation, competence, independence, protection and authority conditions. A prospective walkthrough tests design only; it does not replace evidence from enactment.

| Check | Sufficient answer |
| --- | --- |
| Distinct results | Recommendation, later authorized decision, intended work, implementation and observation are separately established or explicitly unknown. |
| Material observation | Each selected observation can change a named premise, claim, alternative, condition or boundary; any threshold has a qualified meaning. |
| Design choice | Feasible arrangements were compared by coverage, delay, burden and receiving use; a PSD.16 constraint did not preselect the answer. |
| Viability | Observation, interpretation and return have the necessary performers, access, resources, timing, protection and failure route. |
| Current evidence | The actual evidence fits its subject, configuration, interval and intended use; absence or silence is not favourable evidence. |
| Local consequence | Unchanged, narrowed, blocked, reopened-contributor and later-recommendation conclusions name their exact affected scopes and gaps. |
| Authority and closure | Operational change and recipient choice retain their direct authority; the follow-up return has a bounded continuation or end condition. |

### PSD.14:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Monitor implementation of what was merely recommended | Obtain the later decision and implementation evidence separately; state unknown status when they are absent. |
| Use an indicator list as the whole arrangement | Name its claim, interpreting owner, timing, receiving use and failure return. |
| Trigger an action automatically from a threshold | Establish the direct operational authority and response rule separately; otherwise return the qualified reconsideration question. |
| Rerun the whole engagement after every new version | Inspect changed claim content and actual reliance; preserve independently usable results and reopen only affected contributors. |
| Reuse an A-specific evaluation for configuration B | Retain the historical A result and obtain B's exact qualification. |
| Interpret a missed observation as no change | Return the gap and its consequence for reliance, with the responsible receiver. |
| Call later improvement proof that the advice worked | Obtain the direct causal or effectiveness result; chronology and satisfaction alone do not supply it. |
| Keep follow-up alive without an owner or end condition | Establish the actual service or observation obligation, or close with an honest bounded return. |

### PSD.14:9 - Consequences

The practitioner can react to a meaningful change without losing every previous result. The recipient sees what remains usable, what is unknown, which contributor should respond and whether a new recommendation is needed. Later decisions and operational responses remain attributable to their real owners.

The arrangement costs observation and interpretation effort and can expose a limitation before action is taken: no feasible way exists to watch a condition on which the advice depends. That is a useful result. A positive recommendation cannot honestly promise protection through follow-up that cannot be performed.

### PSD.14:10 - Rationale

The decision-support remainder is not generic monitoring or generic source refresh. It connects this recommendation's consequences, assumptions, alternatives, models, authority and problem boundary to a feasible observation-and-interpretation arrangement and a current advice return.

This connection must be designed before it is relied on, but design and use need not form a universal lifecycle. One changed observation can open the pattern directly. A proposal can stop at an infeasible observation condition; a later source can leave the answer unchanged; a changed boundary can require formulation work without first rerunning every calculation.

Locality is semantic rather than file-based. A shared file does not make all claims dependent, and separate documents do not make actually coupled claims independent. The stopping point is the last receiving question whose answer can change.

### PSD.14:11 - SoTA-Echoing

The practice question is **how to keep decision support useful under change without confusing observation with decision or causing indiscriminate recomputation**. The selected line designs decision-linked evidence and interpretation, combines targeted and unexpected-change coverage where warranted, and returns only the affected question. The trade-off is explicit observation and interpretation effort; lower-burden arrangements remain preferable when they cover the actual use.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| What should cause reconsideration? **Adapt** named signposts and switch/reconsideration conditions tied to the actual decision. | A fixed periodic review is adequate for slowly changing, covered conditions; alone it can miss a consequential change before the next decision. Sections 4.2–4.6 connect evidence, timing and affected result without treating a signal as automatic authority. | [Lynch et al. (2025), *RAD switch points and triggers for adaptation planning*](https://www.usgs.gov/publications/rad-resist-accept-direct-switch-points-and-triggers-adaptation-planning), is a current domain line using three natural-resource cases for iterative reevaluation. It supplies no universal threshold, response or institution. Reopen when a better-supported rival or changed decision window defeats this observation design. |
| Should follow-up only test the predicted outcome? **Adapt** a proportionate combination of targeted questions and observation for unexpected change. | Targeted tests are efficient for a specified uncertainty; broad surveillance can expose unanticipated change but adds burden and weakly identified signals. Sections 4.2–4.3 and 5.1 compare the mix instead of prescribing either alone. | [Manley et al. (2026), *Meeting the moment*, Discussion / “Change is inevitable, learning is critical”](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2026.1783129/full), is a contemporary environmental decision-support perspective distinguishing these monitoring uses, not a comparative effectiveness trial. Reopen on representative evidence that another mix covers the material questions with less burden or delay. |
| Does a returned recommendation end every relationship obligation? **Adapt** bounded service continuation and closure while keeping renewed advice a later application. | Ending all contact at delivery may fit a one-off analytical request but not an obtaining service duty; indefinite monitoring creates the opposite failure. Sections 4.4 and 4.7 require the actual relationship and end condition. | [ICMCI v4.0, C.1.1–2](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), is a professional comparator for assignment closure. [NCDA 2024, A.10](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), governs its own service continuity/referral. Neither establishes a universal contract. Reopen when the actual service or applicable duties change. |

### PSD.14:12 - Relations

- `PSD.13` supplies the recommendation's receiving decision, conditions, dissent, gaps and reopen basis. It supplies no evidence that the later decision or implementation occurred.
- `PSD.16` supplies only a constraint that changes follow-up design. This pattern still generates and compares its own alternatives.
- `PSD.3`–`PSD.4` receive a materially changed formulation or boundary question; `PSD.5` and `PSD.8`–`PSD.12` receive only the affected model, candidate, value, uncertainty, consequence or robustness question. Availability does not imply that every contributor must run again.
- `A.10` qualifies one reliance use; `A.15.9` obtains a bounded external result; `A.10.1` discovers and revalidates affected receiving uses of a changed source when its several-use condition holds. `G.11` governs currentness and scoped refresh planning/reporting, not the new domain result.
- `A.22` governs a selected-structure claim when made. It does not establish the proposed arrangement, participant assignment, observation, decision or effectiveness from a representation.
- `A.2.9`, `C.11` and direct domain authority distinguish actual authorization, recipient choice and their records. `A.15.2` and `A.15.1` distinguish intended from performed Work; causal claims retain their direct evidence requirements.
- `PSD.15` may use this bounded follow-up evidence when it can change a repertoire decision under the relevant conditions. Evidence neither authorizes nor entails the repertoire result.
- Strategy-direction follow-up, domain operations and professional service management retain their direct owners. A `STR.12` result may be considered only when its exact subject, claims, authority, evidence and effective conditions fit; no strategy framework is a blanket prerequisite.
- An unavailable, stale, out-of-scope or incompatible input requires a qualified direct result or the exact missing-result return. A profile, pattern body or available Method is not an actual observation or decision.

### PSD.14:End


<a id="psd-15"></a>
## PSD.15 - Develop and Refresh Problem-Structuring and Decision-Support Methods

> **Type:** Method pattern (DPF)
> **Status:** Candidate
>
> **Primary working result:** a **current decision-support Method repertoire** for named recurring uses, with the ways offered or retained as candidates, their comparative reasons, applicability and evidence limits, cultural lineage, source-to-claim basis, and conditions for refresh or withdrawal from a particular use.

### PSD.15:1 - Problem frame

**Use this when** a practice needs to change which problem-structuring and decision-support Methods it can responsibly offer for future engagements. A familiar workshop no longer covers a recurring participation difficulty. A new analytical technique seems promising, but its input assumptions differ from those of the existing repertoire. Follow-up exposes a repeatedly broken join between a material correction and the recommendation that should use it.

Start with the recurring difficulty and the repertoire decision: which way should remain available for which situation, which proposed change deserves a trial, and which use should be narrowed or withdrawn? A better source or a qualified failure can justify a small change; the practice need not redesign its entire repertoire.

Problem structuring and decision support is the wider practice. This pattern governs **development and maintenance of its reusable ways of working**. A repertoire here is a bounded set of Methods and separately identified candidate accounts with usable conditions and reasons, not a catalogue of schools, a software inventory, a training curriculum or an assertion about the whole discipline.

The gain is a practical choice for the next engagement: a practitioner can recover what a Method does, where it fits, what evidence supports that use, what alternative remains, and when to ask for another result. A small repertoire can be better than a comprehensive list that hides unsupported transfers.

**Do not use this pattern** merely to choose an adequate existing Method for one engagement; use `PSD.6`. Use `PSD.14` to respond to a changed premise in one current recommendation, and `PSD.16` for a conflict in the current work arrangement. Enter this pattern only when that evidence can change a reusable Method, applicability claim or repertoire offering. Changing a document, tool, source locator or one local performance does not by itself create a new Method.

### PSD.15:2 - Problem

Professional repertoires tend to harden around what their practitioners can already teach, facilitate or compute. New situations are then forced into the incumbent's assumptions: unclear values become invented weights, unequal participation becomes apparent agreement, and a dynamic uncertainty problem becomes one fixed scenario.

The opposite failure is uncontrolled combination. Each engagement adds another technique or software assistant, but nobody identifies the reusable action, the meaning of the joins, the evidence that transfers or the conditions that defeat it. The resulting collection is larger without being more useful.

Published applications and local successes can compound the problem. A reported use is evidence of that use, not proof of general superiority. A new edition may improve a description without changing a Method. A promising variant may deserve a trial without inheriting its parent's fit. The practitioner needs a repertoire-development decision that preserves these differences and still supports action.

### PSD.15:3 - Forces

| Force | Tension |
| --- | --- |
| Professional continuity and change | Familiar ways preserve skill and comparability; an incumbent can also hide a recurring failure. |
| Plurality and usable choice | Several Methods may be warranted, but an undifferentiated list shifts all selection work to the next practitioner. |
| Generality and representative conditions | Reuse needs stable guidance; participation, power, values, evidence and authority vary across engagements. |
| Experiment and protected interests | Trials can improve practice, but participants and receiving decisions must not bear unbounded methodological risk. |
| Method and supporting arrangement | Tools, expertise and organizational conditions affect performance without necessarily changing the reusable way. |
| Lineage and present warrant | Provenance makes a variant recoverable; it does not establish fit, effectiveness or cultural uptake. |

### PSD.15:4 - Solution

Develop the repertoire around recurring decision-support results and the conditions that make them possible. Recover the actual Methods, compare live alternatives, trial a consequential change at the grain of its claim, and retain a bounded offering with its source and evidence return. These are dependencies in reasoning, not a compulsory lifecycle for every engagement.

#### PSD.15:4.1 - Bound the repertoire question by the work it must serve

Name the practitioner group or service using the repertoire, the recurring situation, the receiving decision-support result, and the horizon over which the offering matters. The starting question might be: “How can our engagements preserve a late but material participant correction without losing the ability to produce a timely qualified recommendation?”

Recover only conditions that can change the answer: disputed or already formed question; participants and power; access to affected parties; values and protected conditions; alternatives; uncertainty; available evidence; technical and facilitation capability; decision authority; receiving Work; and follow-up need.

Use a `PSD.14` result only when its evidence can change this repertoire decision under the relevant configuration and horizon. A changed mobile-deployment premise may show that the existing follow-up Method worked by returning the correct blocker. It does not by itself demonstrate a defective Method. If a supplied result is missing, stale or incompatible, use a qualified direct account or name the precise gap.

Distinguish a missing input, a failure to enact the stated Method, a support or capability problem, and a defect in the reusable way itself. A practice cannot repair absent stakeholder access simply by adding another modelling technique. Conversely, more training cannot repair a Method rule that systematically excludes the required correction.

#### PSD.15:4.2 - Recover candidate ways of working and their contribution boundaries

State each serious candidate as a way of doing: its entry conditions, participant meanings, actions, input/result commitments, required joins, allowed variation, and stop. Use `A.3.1` for Method identification. Keep an unresolved proposal as a candidate account; an attractive name, complete document or parent Method does not admit it.

When several grounded occurrences or direct sources leave the reusable way genuinely unclear, `A.3.1.MR` can help recover candidate accounts. It is not the route for filling a missing design choice in a prospective recipe. Ask the designer to state the proposed action and its conditions.

Decompose a heavyweight school or package only far enough to compare contributions. The following contrasts are useful starting questions, not an exhaustive taxonomy or automatic assignment rule.

| Recurring difficulty | Contribution to recover | Condition that must not be silently supplied |
| --- | --- | --- |
| Participants formulate different problems | Ways to elicit, represent and challenge attributed interpretations; purposeful-activity or concern-mapping contributions where suitable. | Attendance or a shared map does not establish equal influence, representation or agreement. |
| Related decisions cannot be treated independently | Ways to expose connected choice areas, feasible combinations and commitments. | A diagram of dependencies does not establish feasibility or authorize commitments. |
| Values and trade-offs are incompletely stated | Ways to elicit value judgements and compare alternatives under the admitted preference information. | A preference model cannot create legitimate weights or permission to trade a protected condition. |
| Consequences depend on uncertain conditions | Qualified conditional modelling, uncertainty analysis, scenarios, robustness and information-priority work. | A scenario is not its probability; one robust region does not cover every model or value scheme. |
| Analysis does not become usable advice | Ways to compose and explain a source-bounded recommendation, dissent, limits and next use. | A score or specialist answer is not the whole recommendation or recipient choice. |
| Advice loses its basis after change | Ways to observe decision-significant conditions, interpret evidence and reopen the exact affected result. | A signpost, dashboard or missed observation is neither an authorized response nor evidence of no change. |

Soft Systems Methodology, SODA/cognitive mapping, Strategic Choice, MCDA, scenario and robust-decision approaches can contribute to different rows under their actual source conditions. A software platform may support several such contributions. None supplies a universal Method merely by appearing in the repertoire.

`PSD.6` supplies the engagement-level comparison and combination discipline. Preserve its joins: an attributed concern may become a candidate objective for examination, not automatically a numerical weight; a scenario may constrain a calculation without supplying a probability. If a proposed whole cannot recover its reusable action and joins, retain the bounded candidate or arrangement description rather than calling co-use a composite Method.

#### PSD.15:4.3 - Compare the incumbent with a serious alternative before designing a variant

Name the current offering, a plausible competing Method, and a bounded adaptation or combination only where each is live. Compare them against the same recurring result and the actual conditions, at comparable effort where possible.

Ask what each lets participants and practitioners do, what it leaves unresolved, and where it fails. In addition to analytical adequacy, consider meaningful challenge, unequal power, facilitation burden, interpretation skill, source qualification, time to a usable return and cost of maintaining the offering. State a deliberately accepted trade-off when the richer result costs more.

Do not infer that one Method is universally better because it produces a precise score, a satisfying workshop or more alternatives. A single well-qualified Method can remain the best offering for a narrow use. Plural formulations can be necessary elsewhere; a numerical comparison can still be necessary after them.

When a change is needed, state its mechanism: which reusable action, input condition, dependency, decision rule or stop changes, what remains, and why that difference could repair the failure. Distinguish this from a change in wording, display, software, local staffing or performance. The latter may require maintenance or a new fit check without identifying another Method.

For example, replacing a paper map with a digital map while preserving attribution, challenge and unresolved-claim rules may change support and access. Replacing the challenge rule with automatic aggregation of all statements changes the reusable way and can lose dissent. The same interface change can therefore have different repertoire consequences depending on what practitioners actually do.

Use current `ME.15` guidance when generic variant identity, derivation or non-variant maintenance is the live subquestion and its exact claims fit. The remaining PSD question is whether that way serves the professional decision-support use: how interpretation, participation, values, uncertainty, authority and follow-up contribute to a usable return. Generic variant maintenance does not answer that field judgement.

#### PSD.15:4.4 - Build a source-to-claim basis, not a popularity ranking

For every repertoire claim that can change later use, retain the source contribution and its actual limit. An instruction can describe a Method; a reported application can show that it was used; an observed interaction can illuminate a failure mechanism; a comparative study can support a bounded advantage. These are not interchangeable evidence.

A useful basis line says: **this source or qualified experience supports this action or applicability claim for these conditions; this uncertainty remains; this new observation would change the offering**. Include source edition, relevant locus, evidence window and original meaning where they matter. Recover contrary cases and the serious alternative, not only supportive citations.

The [2019 Smith and Shaw review](https://doi.org/10.1016/j.ejor.2018.05.003) provides an exploratory way to compare PSM characteristics; its classification is not an exhaustive admission rule. [Kogetsidis's 2025 application review](https://doi.org/10.1108/IJOA-08-2024-4746) and [2026 online review of Europe and beyond](https://doi.org/10.1108/EMJB-06-2025-0214) provide leads about reported applications. Their journal and search boundaries limit what they establish about practice outside that corpus. Do not rank Methods by the number or location of publications.

A recent decision-analysis synthesis such as [Borgonovo et al. (2026)](https://doi.org/10.1016/j.ejor.2025.05.023) can identify developments in value-focused thinking, graphical modelling, uncertainty, sensitivity and information acquisition. It does not substitute for the source of a particular Method or cover every adjacent decision-support family.

Obtain missing source interpretation, domain evidence or representative evaluation through `A.15.9`, preserving supplier authority, and qualify actual reliance through `A.10`. If the decisive source contribution cannot be recovered, keep that offering conditional or return the source gap. Neither a famous school nor a new source date repairs the missing claim.

#### PSD.15:4.5 - Trial the claimed improvement in representative engagements

Turn the proposed improvement into a question that can fail. Specify the Method or status-preserved candidate, the situation represented, participant and power conditions, required capability and support, the serious comparator, the expected result, the burden accepted, and the observation that would retain, narrow or reject the proposal.

Select evidence proportionate to the claim. A walkthrough can expose an impossible join. A constructed exercise can test whether practitioners preserve an objection through a calculation. An authorized field trial can test feasibility and use in a real engagement. Broader transfer or causal-effectiveness claims need stronger and appropriately designed evidence. Do not generalize the last two from the first two.

Observe the working mechanism as well as the output: who could contribute or challenge; which material statement entered the model; where meaning changed; what was withheld; how uncertainty and protected conditions reached the recommendation; and whether the receiver could use it. The distinction between technically valid models and what people do with them is central to [Franco et al.'s behavioural OR review (2021)](https://doi.org/10.1016/j.ejor.2020.11.031). It supports attention to intervention configuration and interaction, not one universal trial design.

Preserve competing explanations. Better results may reflect a more skilled facilitator, a different participant group, more time, an easier problem or changed support rather than the Method difference. Where those cannot be separated, report what the trial establishes and what remains unresolved; a useful feasibility result need not pretend to be a causal result.

Do not use a consequential live decision as an uncontrolled Method experiment. Establish the authority, consent, protection, observation and fallback conditions appropriate to the engagement. A prospective candidate can be investigated through a separate trial arrangement without claiming that an unadmitted candidate whole has already been enacted as a `U.Method`.

Retain disconfirming results. A richer Method that cannot run within the actual access or competence conditions may be a poor offering for that use even when its idealized output is better. Conversely, a failed local performance does not disprove the Method when a required condition was absent; it may instead defeat the offered applicability claim.

#### PSD.15:4.6 - Return a small current repertoire with differentiated dispositions

Decide what the practice can now offer, for which use and with which limits. Useful dispositions include retaining an established offering; narrowing its applicability; adding a separately identified variant for a qualified use; retaining a proposal for a bounded trial; requesting missing evidence; and withdrawing an offering from one use while preserving its history.

Keep identification separate from validation. An independently identified Method may still have unproved practical fit. A candidate account may have useful trial evidence without yet resolving its Method identity. State both rather than using one maturity label for every question.

For each action-changing entry, make the following recoverable in the simplest form that serves its next user.

| Repertoire position | Content needed for use |
| --- | --- |
| Recurring situation and receiving result | Who uses the offering, what difficulty it addresses, which result it provides, and the conditions that matter. |
| Method or candidate | Exact reusable action and status; entry, joins, allowed variation and stop; where the full description can be obtained. |
| Comparative reason | Incumbent or serious alternative, the gained capability or repaired failure, and the accepted effort or other loss. |
| Evidence and source basis | Claim-sized sources and relevant trials, their configurations and limits, defeating evidence and the next unresolved question. |
| Lineage | The actual source way or candidate, preserved and changed semantics, and the evidence for derivation; cultural links only where established. |
| Current offering | What is available for this use, conditional, retained for trial, narrowed or withdrawn; required performer/support conditions and source responsibility. |
| Refresh and exit | Which changed claim, failed condition or receiving need would reopen this entry, and what remains usable elsewhere. |

A repertoire may retain alternatives without ranking them. When the actual question is declaring a selector-facing set result over already identified members, use `G.5` with the exact members, outcome, ordering and basis it requires. Distinguish alternatives retained for later choice from members all included in one named joint use. A Method-family registry or selector declaration supplies neither field fit nor actual enactment and need not be rebuilt for every repertoire update.

Make the next use easy to find: which Method a practitioner should inspect for the named situation, which claim still needs evidence, or which use has been withdrawn. A large source map that gives none of these is not the promised repertoire.

#### PSD.15:4.7 - Preserve cultural lineage without inventing cultural continuation

Record where a reusable change came from when that relation matters: an identified source Method, a documented adaptation, a changed stopping rule, a taught practice, or another qualified source. Similar names, chronological succession and a shared diagram do not establish derivation.

Keep proposed derivation, observed local enactment, transmission to another practitioner, recognition, selection, retention and loss distinct. A source publication can make a description available without proving that anyone learned or enacted the Method. A successful trial can justify a restricted offering without showing that a professional community adopted it.

Use `C.36` for an actual cultural-evolution question. Supply `PSD.17` with the repertoire's qualified variant or local evidence only when it matters to that cultural-continuation decision. Name the practitioner population, engagement/community, place and period that the evidence actually covers, and mark the unobserved links. The receiving cultural decision is not entailed or authorized by the repertoire.

This boundary applies equally to new software support and AI-assisted practice. A tool release is not cultural uptake; widespread use of a tool is not evidence that the same Method was enacted by everyone. Teaching, service change and deliberate cultural intervention require their own work and authority.

#### PSD.15:4.8 - Refresh the affected offering and preserve an honest stop

Maintain a responsible source and use return for the current repertoire. Reopen an entry when new evidence, a source claim, changed Method semantics, participation or authority conditions, support, qualification window or receiving need can change its offering. A new publication date or a file rename alone is not such a change.

For a changed claim, identify its exact repertoire use and the consequence: preserved, narrowed, reopened for a new trial or source result, or withdrawn from that use. Preserve independent entries and the earlier evidence for its original conditions. If applicability remains unresolved, state the uncertainty rather than assigning an unsupported negative or positive status.

A changed service rule might restrict the human career-advising branch without changing organization or AI-domain truth. A new AI configuration may invalidate evidence for a software-assisted offering without changing the manual Method. If the reusable decision-support action itself changes, identify and assess that semantic change rather than hiding it as maintenance.

Use `A.10` for a known bounded reliance, and `A.10.1` when a changed source requires discovering and revalidating several actual receiving uses. Invoke `G.11` for an admitted currentness or refresh-planning/reporting object when its conditions obtain, such as a relied-on evidence or selected set; it does not supply the new repertoire judgement or make every local entry a refresh-orchestration problem.

Close this repertoire question when the relevant offerings, conditions, source/evidence gaps and next uses are clear. Withdraw only the defeated use, not recoverable history or other supported uses. A still-unqualified new proposal can remain visible without being offered as established practice.

### PSD.15:5 - Archetypal Grounding

The cases are hypothetical. They distinguish source description, proposed Method change, constructed trial, qualified offering and later cultural evidence; they assert no actual practice-wide improvement.

#### PSD.15:5.1 - A late correction changes an offering, not the whole school

A public decision-support practice serves flood-investment engagements. It maintains an identified one-session inquiry Method: elicit and attribute concerns, compare the admitted alternatives with qualified inputs, record material dissent, and close the session with a bounded return. The Method presumes that all decision-bearing contributions needed for that return are available within the session. The practice has nevertheless offered it as the sole inquiry option for these engagements, including ones in which necessary input can arrive later.

The `PSD.14` pump follow-up case supplies a changed mobile-deployment premise and the resulting blocker. That alone is not a Method defect: the follow-up correctly prevented an unsupported investment use. The practice retains that evidence at its actual scope.

A separate examination of the one-session offering finds the action-changing mismatch. Engagements in this service can receive a qualified access correction after the meeting, while the reusable closing rule provides no way to bring it into the same pending recommendation. The practice must not advertise that offering as sufficient for such engagements.

Three alternatives are considered. Keep the one-session Method but restrict it to uses with the necessary inputs already available; defer the whole engagement until every possible input arrives; or construct a bounded correction-and-return variant that keeps attribution and conditional analysis, permits a material qualified correction before the receiving recommendation closes, and reopens only the affected comparison.

The third proposal changes a reusable join and closing condition, not merely the calendar. Its candidate account records the parent, retained actions, changed rule, required facilitator/analyst availability and stop when a late contribution cannot be qualified in time. Independent Method identification remains separate from evidence of practical fit.

The practice runs a constructed exercise, not a public investment experiment. Both the incumbent and proposed rule are examined on the same two realistic situations: all required inputs available at the meeting, and a material access correction arriving afterward. Participants' access, analyst time and the receiving deadline are made explicit. The test is whether the correction changes the exact affected comparison while preserving dissent and independent usable claims.

In the illustration, the incumbent gives an adequate bounded return in the first situation but leaves the second correction outside its closed result. The proposed rule preserves the correction and exposes its unresolved consequence in the second situation, at the cost of a further qualified return and analyst/facilitator time. This exercise supports the proposed join's feasibility under those conditions, not superior public decisions or transfer to all engagements.

The repertoire result is deliberately differentiated:

| Offering | Current use and limit |
| --- | --- |
| Existing one-session Method | Retained for the stated input-ready situation. Its broader late-input offering is withdrawn; the Method and other evidence are not erased. |
| Correction-and-return proposal | Retained as a candidate for a protected field trial; its intended join and observed exercise behaviour are recoverable. Any Method identification and field-fit conclusion must be established separately. |
| Wait for every possible input | Not selected for this service's present question because its unbounded delay defeats a timely qualified return; a named indispensable missing input can still require waiting or a blocker. |

No pump is chosen. The staged alternative and assistance/protection questions in the original investment case remain with their direct owners. The repertoire entry does not claim that other practitioners have received, enacted or retained the proposed variant; those cultural links remain unproved.

#### PSD.15:5.2 - Non-contested development advice and a new software assistant

An advisory service already supports formed development questions without a dispute workshop. Its repertoire includes a source-bounded recommendation Method: recover the recipient, holder and horizon; inspect qualified specialist results; compare only live alternatives under the declared scheme; return a warranted direction, retained set, probe, request, blocker or abstention; and keep the recipient's choice separate.

A new drafting assistant formats the same qualified premises and flags missing fields. If the adviser still performs the same qualification, comparison and return, the changed object is support. The practice checks access, confidentiality, capability and output reliability for that support; it does not create a new Method merely because the model version changed.

A different proposal lets the assistant select a preferred development direction from its own generated ranking and omit unranked candidates. That changes the reusable comparison and stopping rule. The practice cannot import the manual Method's evidence or call the proposal a harmless implementation detail.

The immediate repertoire decision is to retain the manual offering and withhold the stronger automated offering pending an exact candidate account, comparison basis and representative evidence. A useful trial must include an absent whole-arrangement result, an unclosed provider alternative, and an evaluation that covers configuration A while the request concerns B. Success means the return preserves the correct gap and independently useful content, not merely that the text is fluent or shorter.

The trial also has to cover the actual human professional-service conditions where present. Human career-assessment evidence does not establish an AI-holder result, and an organization's allocation evidence does not establish a person's learning transfer. No generic development-direction score bridges those differences.

This is repertoire work, not a recommendation for a particular client, authorization to deploy the assistant, or proof of the full opportunity-construction Method. A human or organizational recipient still makes its own later choice.

#### PSD.15:5.3 - A source update and a cheap non-use

A new version of a relied-on methodological source changes the conditions under which a comparison procedure may be used. The practice identifies the exact applicability claim in its repertoire. The supported entry for complete input data remains; the incomplete-data branch is narrowed and its source question reopened. Other Methods that do not use that claim remain unchanged.

If the new source only changes layout or a locator while preserving the relied-on claims, update that description or access information under its direct guidance. If one current engagement simply needs an adequate existing Method, stop repertoire development and use `PSD.6`. Neither situation warrants a new professional Method.

A review reporting more published applications can justify looking for a promising candidate or an unexamined domain. It does not by itself change a local offering's evidence or justify retiring a less frequently published Method.

### PSD.15:6 - Bias-Annotation

School loyalty and novelty bias pull in opposite directions. Compare the strongest applicable incumbent and the smallest useful new proposal; do not protect either by choosing an easy example. A practice's available expertise is a real constraint, but it is not evidence that other Methods lack value.

Publication and success-reporting bias can hide failed, unpublished or culturally distant uses. Preserve the source search boundary and distinguish reported applications from representative evidence. A corpus dominated by particular journals cannot establish the absence of a practice elsewhere.

Combination bias treats more techniques as richer support. Inspect the meaning and cost of the joins. Automation bias treats a change in software as either automatically new or automatically harmless; recover whether reusable actions and stops actually changed.

### PSD.15:7 - Conformance Checklist

**Recognition** asks whether the missing result is a reusable repertoire offering rather than an engagement choice, one source update, a support repair or a current follow-up response. One corrected applicability line can be the complete useful result.

**Assurance** asks whether the offered Method or candidate and its claimed use are warranted by the actual source and trial evidence. A description can identify a way without proving fit; a constructed exercise can support feasibility without proving real-world effectiveness or transfer. Consequential trials and offerings retain their direct participant, competence, independence, safety, confidentiality and authority conditions.

| Check | Sufficient answer |
| --- | --- |
| Recurring use | Practitioner, situation, receiving result, material conditions and repertoire decision are bounded. |
| Method recovery | Actual reusable actions, joins and stops are recoverable; Method, candidate, description, support and local Work remain distinct. |
| Comparative development | A serious alternative and the changed mechanism or applicability claim are explicit, with effort and losses. |
| Source and evidence | Each action-changing offering has a claim-sized basis, qualification limits, contrary evidence and an honest gap where needed. |
| Trial claim | The comparator and representative conditions fit the claim; observation, feasibility, fit, causal effect and transfer are not conflated. |
| Current offering | Retained, narrowed, candidate, withheld or withdrawn uses are usable by the next practitioner and do not hide different outcomes. |
| Lineage and refresh | Derivation has a basis; unproved cultural links remain gaps; only affected offerings reopen and recoverable history remains. |

A failed check may narrow one offering or retain a candidate for investigation while other entries stay usable. Do not label the whole repertoire current merely because every row has a source link.

### PSD.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Treat one school as the permanent professional answer | Compare the actual contribution and assumptions against the recurring use and a serious alternative. |
| Turn every successful engagement into a new Method | Separate reusable semantics, one performance, support and applicability evidence. |
| Copy parent evidence to a hybrid | Identify the changed joins and trial the new claim under its own conditions. |
| Count papers, downloads or satisfied participants as general effectiveness | State what was observed and the source boundary; obtain the evidence needed for the stronger claim. |
| Offer a candidate as established because it has a complete description | Keep Method identification, trial status and fit claims separate. |
| Use participant agreement as proof that power and dissent were handled | Examine who could challenge, whose concerns entered the result, and what material disagreement remains. |
| Retire every entry after a source or tool update | Trace the changed claim to its actual offering and preserve independent uses. |
| Treat a repertoire or publication as cultural continuation | Establish transmission, receiving enactment, recognition, selection, retention or loss separately. |

### PSD.15:9 - Consequences

Future engagements gain a smaller, more discriminating starting point. Practitioners can reuse a Method for a supported situation, select an alternative, ask for a missing input or decline an unsupported extension. Changes become recoverable improvements or bounded experiments rather than accumulating workshop tricks.

The cost is maintaining meaningful applicability and evidence, not just names and editions. Some promising candidates remain unoffered, some broad claims narrow, and some local successes support only the conditions observed. That restraint leaves room for development without presenting uncertainty as established practice.

### PSD.15:10 - Rationale

The repertoire decision remains after Method identity, generic comparison, variant maintenance and set declaration have done their work. It asks which professional ways can help this practice structure problems and support decisions under actual participation, value, evidence, authority and follow-up conditions.

This is different from choosing a Method once. A future-use offering must preserve enough source, evidence, lineage and limits to survive transfer to another practitioner or engagement. It is also different from changing a culture: making a variant available does not establish the relations through which a community learns, enacts or retains it.

A changed premise can vindicate the incumbent's stop rather than defeat the Method. That is why development starts with the recurring failure or opportunity and the affected claim, not the mere fact that a recommendation changed.

### PSD.15:11 - SoTA-Echoing

The practice question is **how to develop a usable professional repertoire under heterogeneous situations and uneven evidence without turning either an incumbent school or each new technique into a universal answer**. The selected line is contribution-first comparison, explicit assumptions and joins, representative testing of the claimed change, and local source/evidence refresh. It accepts the cost of maintaining differentiated offerings; a simple established Method remains preferable when it covers the use at lower effort.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| How should unlike problem-structuring approaches enter the repertoire? **Adapt** explicit comparison of assumptions and contributions, with open family boundaries. | A familiar three-school catalogue is cheap to teach but hides differences that change participation and result use. Sections 4.1–4.3 compare the contribution rather than require a fixed membership list. | [Smith and Shaw (2019)](https://doi.org/10.1016/j.ejor.2018.05.003) is an exploratory conceptual comparator; [Kogetsidis (2025)](https://doi.org/10.1108/IJOA-08-2024-4746) is a later published-application line. Neither ranks Methods for this service. Reopen if a stronger account changes a load-bearing boundary or a representative case defeats the assumed fit. |
| Can current uptake evidence decide what to offer? **Reject that inference alone; adapt** reported applications as leads for candidates and source return. | A publication-frequency rule is inexpensive but confounds search coverage and visibility with practitioner use or worth. Sections 4.4, 4.7 and 5.3 preserve those distinctions. | [Kogetsidis (2026 online), Europe and beyond](https://doi.org/10.1108/EMJB-06-2025-0214), examines selected journals over 2010–2024. It is a current corpus-based comparator, not a census of practice or comparative effectiveness test. Reopen when new representative evidence changes the particular offering, not simply when another paper appears. |
| How should analytical advances change the repertoire? **Adapt** the specific value, model, uncertainty, sensitivity or information contribution needed by the use. | Adopting an entire analytical process can preserve coherence when its assumptions hold; importing it wholesale can require missing values, probability or evidence. Sections 4.2–4.4 retain exact inputs and joins. | [Borgonovo et al. (2026), decision analysis in OR](https://doi.org/10.1016/j.ejor.2025.05.023), is a contemporary synthesis of these contributions, explicitly not exhaustive of adjacent fields. It is not a Method-fit result for an engagement. Reopen on a materially better-supported analytical contribution or a failed input/return assumption. |
| What evidence warrants a Method improvement? **Adapt** examination of intervention configuration, interaction and outcomes at the claim's grain. | A technically valid output or favourable post-workshop rating is cheap to obtain but cannot alone identify the changed mechanism, comparative benefit or transfer. Sections 4.5 and 5.1 preserve trial type, comparator and confounding conditions. | [Franco et al. (2021), *Taking stock of behavioural OR*](https://doi.org/10.1016/j.ejor.2020.11.031), synthesizes different intervention-study questions and designs. It supplies no universal causal estimate or trial recipe. Reopen when a stronger representative design or counterexample changes the evidence required for the offering. |

### PSD.15:12 - Relations

- `PSD.14` supplies bounded follow-up evidence only when it can change the repertoire decision under the same relevant conditions and horizon. A local observation neither entails nor authorizes the repertoire result.
- `PSD.6` chooses and combines Methods for an engagement; this pattern develops and maintains the reusable offerings and their limits. It does not require a new repertoire cycle before every selection.
- `PSD.7`, `PSD.8`–`PSD.14` and `PSD.16` expose participation, alternative, comparison, recommendation, follow-up and arrangement requirements that a Method offering may need to preserve. Their available descriptions are not evidence of this particular Method's enactment or effectiveness.
- `A.3.1` governs Method identification; `A.3.1.MR` supplies candidate recovery only under its actual source/occurrence conditions; `A.3.2` governs a MethodDescription rather than admitting every multi-Method package.
- `ME.15` can supply qualified generic variant, derivation and non-variant maintenance guidance. Resemblance or shared repertoire vocabulary does not by itself establish a formal Method-specialization relation.
- `A.10` and `A.15.9` qualify and obtain exact source or specialist results. `A.10.1` and `G.11` apply to their respective affected-use and currentness questions, not as substitutes for the field repertoire decision.
- `G.5` declares a selector-facing result when that claim is live over identified members and grounds; it supplies neither a universal Method-family classification nor professional fit.
- `C.36` governs the cultural relation claims. `PSD.17` uses this repertoire as evidence or a variant for a separately bounded cultural decision; missing generation, transmission, receiving-enactment, recognition, selection, retention and loss links remain unproved.
- An unavailable, stale, out-of-scope or incompatible input calls for a qualified direct source or the exact gap. No sibling DPF, whole-language traversal or unperformed specialist result is implied by adjacency.

### PSD.15:End


<a id="psd-16"></a>
## PSD.16 - Reconcile Simultaneous Problem-Structuring and Decision-Support Work

> **Type:** Method pattern (DPF)
> **Status:** Candidate
>
> **Primary working result:** one **bounded conflict and facilitation-architecture decision**: which arrangement of inquiry, modelling, participation and decision return will be used for the named engagement, why it addresses the material interference, what burden or unresolved conflict remains, and what would reopen it.

### PSD.16:1 - Problem frame

**Use this when** useful activities in a decision-support engagement obstruct one another. An analyst needs stable assumptions while participants are still correcting the question. A facilitator cannot both handle a consequential objection and rebuild the displayed model. An evidence team qualifies one configuration while the advice recipient changes the configuration to be considered.

Start with the result at risk and the interference: “If we close this comparison now, this still-material contribution cannot enter it.” Recover only the relationships needed to understand that conflict, compare genuinely different arrangements, and decide the smallest warranted change within the applicable remit.

Problem structuring and decision support is the wider practice. This pattern governs a narrower subject: **the arrangement through which a named engagement's different kinds of work contribute to its result**. Here *facilitation architecture* means that arrangement of participation, modelling, inquiry, challenge and return—not a workshop agenda or a new institutional hierarchy. A diagram describes the arrangement; a reusable Method guides action; actual work enacts it.

The gain is a usable local decision without losing the value, evidence, participation or authority condition that made the conflict consequential. The result may retain the present arrangement with a stated limit, change it, or return the exact blocker to a competent owner. “Reconcile” does not require everyone to agree.

**Do not use this pattern** merely because two activities overlap in time. If they have no decision-relevant interference, continue them. Use `PSD.6` when the question is which Method fits, and `PSD.7` when a claim needs facilitated inquiry but the arrangement itself remains workable. Routine scheduling, specialist mediation, emergency command and decisions about the affected System retain their own Methods and authority.

### PSD.16:2 - Problem

A sensible script can conceal an unsound engagement. Its “elicit, model, compare, recommend” order says little about people correcting claims during modelling, technical evidence arriving during discussion, or a sponsor controlling both participation and the receiving decision.

The same display can also carry incompatible readings. A causal sketch supports exploration; a calculation supports a bounded consequence claim; the closing slide appears to authorize action. If their different uses are hidden, completing the slide can look like completing all three results.

Local repairs then export the difficulty. Moving inquiry outside the meeting frees analytical time but adds participation effort and delays correction. Adding a challenger can broaden discussion while reducing facilitation capacity. Freezing a model stabilizes computation while excluding a changed premise. The practitioner needs to expose and decide these consequences, not merely draw a cleaner sequence.

### PSD.16:3 - Forces

| Force | Tension |
| --- | --- |
| Closure and correction | A recipient needs a timely return, while new evidence or a material concern can invalidate part of it. |
| Analytical focus and participation | Detailed modelling needs concentrated effort; meaningful challenge needs attention when the interpretation is being formed. |
| Joint work and differentiated contributions | Working together can reveal important connections, while facilitation, technical judgement and choice have different conditions. |
| Local gain and transferred burden | Separation or parallelism can improve one contribution while adding delay, support effort or exclusion elsewhere. |
| Adaptation and continuity | The arrangement can change within an adequate Method's allowed variation; a change to its action or joins can instead require Method reselection. |
| Remit and consequence | A facilitator may change discussion conditions without having authority to change participation rights, protection, budgets or the eventual decision. |

### PSD.16:4 - Solution

Reconcile the engagement around the result and its necessary conditions. Preserve useful order where a real dependency warrants it; preserve overlap where the work actually overlaps. Change the relationship that causes the conflict rather than assuming that all activities must share one structure.

#### PSD.16:4.1 - Anchor the engagement and the result at risk

For an ongoing engagement, inspect a concrete occurrence: the objection that could not enter the model, the evidence received after a comparison closed, or the attention demand that stopped a participant's contribution. Distinguish an observed failure from a suspected mechanism. For a proposed engagement, use its intended-use case and proposed arrangement; name the later observation that would test it. A prospective design has no performed success to cite.

Recover the receiving question, subject, scope, horizon and decision boundary. Keep only participants, concerns, models and Method conditions that can change the arrangement decision. Existing `PSD.1`–`PSD.7` results can supply these inputs under the conditions in section 12; no complete earlier traversal is required.

Ask what a usable return must preserve. Examples include a materially different service concern, an interpretable model assumption, a qualified configuration-specific result, a workable challenge route, or the distinction between a recommendation and the recipient's choice. A deadline is a condition to address, not evidence that these requirements have been met.

If the supposed conflict concerns another subject or receiving decision, establish that separate boundary before joining the work. If an indispensable scope or authority premise is missing, obtain its qualified source or return that precise gap.

#### PSD.16:4.2 - Separate the structures that matter

Use `C.32.MWA` to synthesize the needed accounts without forcing them to line up. Begin in ordinary words. The following distinctions are useful when they change the decision; they are not a compulsory six-view dossier.

| Account | Example in a decision-support engagement | Distinction to preserve |
| --- | --- | --- |
| Reusable Method and its composition | Attributed inquiry contributes claims to conditional analysis under specified joins. | A Method's parts and necessary order are not the meeting's calendar or every activity performed there. |
| Work and its temporal relations | Interviews, model revision and evidence checking partly overlap; a particular calculation needs a particular input first. | Overlap does not establish parthood, causation or one composite Method. |
| Decision subject and affected Systems | Pumping equipment, access routes, service recipients and later operating arrangements. | A hierarchy among these subjects is not a hierarchy of inquiry Methods or participants. |
| Participation and authority | Residents contribute concerns; specialists qualify premises; a board receives advice and holds the investment choice. | Being present, having expertise, facilitating discussion and having permission to decide are different. |
| Descriptions and models | A concern map, a capacity model and a comparison note describe different claims for different uses. | Document sections and model nodes are not world-side parts, actors or authorizations. |
| Professional-cultural continuation | A community later reuses or rejects the engagement's facilitation variant. | A local choice or visible workshop does not establish transmission, uptake or effectiveness. |

State the correspondence that the current decision uses: for example, which participants can correct which model assumptions, which evidence can qualify which comparison, or which decision owner can change the receiving question. Preserve important losses in the description. A short map may omit timing details that the proposed arrangement now needs.

Use the direct FPF pattern when a stronger relation claim matters: `A.3.1` for Method identity, `B.1.5` for Method composition, and the applicable Work or authority pattern for those distinct claims. Do not infer a five-level Method stack from five activities. If a changed whole no longer supports its old identity, reidentify it rather than preserving a convenient label.

#### PSD.16:4.3 - Locate the interference and its actual consequence

Describe how one contribution defeats or weakens a condition needed by another. “Modelling and discussion happen together” is not yet a conflict. “The only modeller also controls the discussion, so a contested assumption is entered without its holder being able to correct it” names an interaction that can change the result.

Follow the conflict far enough to identify its receiving consequence. Does it exclude a material alternative, change an attributed value, invalidate evidence use, obscure dissent, prevent meaningful participation, or exceed the engagement's remit? Separate a technical limitation, a value difference, an evidence gap and an authority dispute; they have different returns.

Inspect what is actually shared: a person's attention, a model, a data basis, access to participants, a decision horizon or a rule for closing a claim. Do not solve an evidence gap by voting, or a value dispute by accelerating the model. Obtain the required specialist premise through an adequate existing result or the smallest `A.15.9` request.

For a suspected interaction, use the cheapest discriminating observation or rehearsal before imposing a costly redesign. Where a consequential condition is already unsupported, lower or stop only the relying claim. Unaffected inquiry can continue when its own conditions remain valid.

#### PSD.16:4.4 - Construct alternatives that change the relationship

Compare the incumbent with at least one materially different workable arrangement. Select alternatives from the conflict, not from a universal menu.

A local separation can reserve discussion time while calculation pauses. Parallel inquiry and modelling can use explicit exchange points for consequential changes. Separate contribution channels can preserve a protected or unavailable participant's input, provided a usable correction route exists. A simpler provisional model can support discussion while a specialist develops the stronger analysis elsewhere. A different allocation of modelling and facilitation can remove an attention conflict, if the required people and capabilities are available.

State what each arrangement preserves, what it cannot yet produce, and who bears the extra work, delay or loss. A jointly edited model is not always preferable; when inputs and meanings are stable, bounded expert analysis can be sufficient. Nor does fully serial work automatically preserve participation: someone may become unavailable while another contribution is completed.

When missing perspectives threaten a homogeneous group, a prepared content challenger alongside a separate facilitator is a possible arrangement. Make that contribution explicit and source-supported; allow the group to decline it. It does not confer representation or consent on behalf of absent people. Its preparation and facilitation burden may make another participation route preferable.

Test whether the proposed change stays within the selected Method's permissible variation. A change from spoken to confirmed written inquiry may preserve the Method; replacing participant confirmation with a sponsor's interpretation does not. Return a changed action, result or join to `PSD.6` rather than calling it a scheduling adjustment.

#### PSD.16:4.5 - Make the bounded decision and retain the residual

Compare alternatives against the actual result conditions: faithful participation and interpretation, valid model and evidence use, feasible support, timeliness and applicable authority. Keep protected conditions outside compensating trade-offs unless their competent source actually allows that treatment. More output or a shorter meeting does not compensate for unsupported representation or evidence.

Choose within the established facilitation or engagement-design remit. If a proposed change requires another person's resources, changes a participation obligation or alters the authorized receiving decision, obtain the owner's decision. Until then, return a conditional proposal or blocker, not an implemented arrangement. The `C.32.MWA` synthesis informs this choice; it does not supply its authority.

State the selected change, the material reason, the alternative not taken, what remains unchanged, the residual difficulty, and the limit on the next return. Keep an adequate incumbent when another arrangement brings no justified gain. If no available arrangement preserves the necessary conditions, narrow the result or stop its unsupported part.

This decision concerns how decision support is conducted. It does not select the pump, authorize organization change, deploy a model, or establish agreement with the eventual advice.

#### PSD.16:4.6 - Test the changed interaction and hand on its conditions

Test the interaction that justified the change. Can a corrected concern reach the comparison before it is relied on? Can the modeller identify the exact evidence version? Can the participant challenge the representation through the chosen channel? Can the separate facilitator actually sustain the discussion while analysis proceeds?

A rehearsal supports a prospective arrangement only at its tested scope. For a change used in ongoing work, inspect the resulting contribution and any burden moved elsewhere. A smoother meeting or a completed document alone is not evidence that the material conflict was resolved.

The first result can be a short decision note or spoken return with a recoverable basis. It makes the arrangement, scope, authority, retained conflict, missing result and next observation usable; it need not reproduce every model or conversation.

Carry only consequential constraints into follow-up. For example, a corrected service assumption must reach the named comparison owner; an observation about another configuration does not refresh this result. `PSD.14` still designs and compares its own follow-up alternatives. Evidence from this local variant may inform `PSD.17`, but cultural continuation requires its own observations.

Reopen when the receiving question, a material participant or premise, the model use, the arrangement's support, or the permitted decision changes; when the chosen exchange fails; or when a moved burden defeats another necessary condition.

#### PSD.16:4.7 - What changes in practice

The practitioner can say not only what the engagement does, but why its contributions can coexist without falsifying the return. A necessary sequence remains; a harmful coupling is changed; the unclosed part stays visible. The resulting decision is smaller and more useful than either a master lifecycle or an unbounded redesign of the whole engagement.

### PSD.16:5 - Archetypal Grounding

#### PSD.16:5.1 - A flood-pump inquiry cannot freeze away a service concern

This illustrative case continues the bounded attributed-inquiry and conditional-analysis Method. The board retains the investment choice; the engagement lead may arrange inquiry and model work within the agreed participation and resource conditions. The case supplies an available facilitator and analyst, not a general staffing requirement.

The analyst is preparing conditional comparisons; the working list includes fixed, mobile and staged pumping arrangements. The staged candidate still lacks a qualified consequence result. A separately consulted group has not yet corrected the rendering of its reachable-assistance concern. The current plan freezes the comparison before that correction can arrive. The facilitator is also expected to explain the calculations during the only discussion period. A finished comparison could therefore look complete while answering only the property-protection reading.

The relevant structures differ. Attributed inquiry and conditional analysis are Method contributions. Their actual work overlaps. The resident group, analyst and board have different participation and authority relations. A service-concern map and a hydraulic model preserve different claims. Investment implementation is later work, not a final level of the inquiry.

The lead compares three arrangements:

| Arrangement | What it can preserve | Consequence for this case |
| --- | --- | --- |
| Keep the early freeze and explain the completed model in one session. | Analytical stability and the existing timetable. | Cannot support a claim that the uncorrected service concern was considered. A narrower technical return remains possible. |
| Stop every analysis until every participation response is complete. | Allows those responses to precede analysis. | Delays independent calculations and still cannot promise that every person will respond. |
| Continue bounded analysis while the facilitator maintains inquiry; join material corrections before the affected comparison closes. | Existing qualified calculations, a real correction route and separate attention to discussion. | Requires coordination effort and a clearly limited return if the correction or its technical consequence remains unresolved. |

Under the supplied remit and available support, the lead selects the third arrangement. The facilitator obtains correction of the attributed concern through its agreed channel. The analyst identifies which consequence claims that correction could change and carries unaffected calculations forward. The next return distinguishes qualified calculations, unresolved service claims and the exact access question. If the correction arrives too late for a supported comparison, the brief retains that limitation instead of silently dropping the concern.

A short resulting decision is:

> Keep inquiry and conditional analysis in parallel, with the facilitator handling claim correction and the analyst handling the affected model use. Close each comparison only with its current service meaning and evidence limits visible. Preserve the mobile-access gap and any unanswered contribution in the board's return. The investment choice is unchanged and remains with the board.

The moved burden is explicit: the facilitator and analyst must reconcile the corrected meaning with the consequence account, and the board may receive a narrower answer. A test follows one corrected statement into the draft comparison and checks whether its dependent claim is revised or left explicitly open. That test does not establish road access, district-wide agreement or a superior pump.

If separate analytical support becomes unavailable, the lead must reconsider the arrangement—for example by pausing calculation during the material discussion. The staffing premise cannot be replaced by a role label.

#### PSD.16:5.2 - A non-contested advice question with a moving evidence basis

A committee asks a separate advisory team for a ninety-day service-development comparison. No disagreement about the question is reported. Internal development and a human–AI support arrangement are live candidates; the organization's allocation and AI evaluation results remain specialist inputs.

During preparation, the system owner changes the proposed AI configuration from A to B. The evaluation already supplied concerns A. Meanwhile, the allocation analysis can still answer an independent question about internal development. The original plan waits for one whole “evidence package” and then issues one complete comparison. Its all-or-nothing join either delays useful work or tempts the adviser to pass A's result into B's claim.

The team considers keeping a historical-A comparison, waiting for every B premise before any return, and separating the returns by their actual dependencies. The first does not answer the committee's now-B question. The second remains possible but withholds the independent allocation result. Within its agreed control of analysis and delivery, the team selects dependency-bounded returns: retain the qualified internal-development contribution; request the exact B qualification; keep the cross-candidate comparison open wherever B is material.

The arrangement names the configuration owner who reports a further change, the specialist result each claim can consume, the person assembling the comparison and the condition for closing it. It does not freeze the operating system, prevent its owner from changing B, or turn the available internal-development result into the recommended direction.

The test substitutes another A-only result at the receiving join. It must remain an A contribution or an unusable input for the B claim, while the independent contribution stays usable. A later adequate B result can close that particular gap. A further change of subject or horizon reopens only the affected use.

This is reconciliation without a disagreement workshop. The decision changes how qualified results can be returned together; it supplies no AI safety, human learning, organizational feasibility or deployment authority.

#### PSD.16:5.3 - Overlap without an architecture problem

Two analysts examine independent uncertainties for an unchanged question using adequate sources. Neither consumes the other's result, blocks participation or changes a shared condition. Their calendars overlap, but no material interference has been identified. Continue the work; there is no reason to manufacture a common Method, hierarchy or facilitation redesign.

### PSD.16:6 - Bias-Annotation

**Scope:** arrangements of problem-structuring and decision-support work for a named engagement. The pattern does not govern every concurrent project activity.

Watch for analytical capture: the easiest-to-compute account becomes the whole question. Watch also for participation romanticism: a joint session is credited with representation, expertise or agreement it did not establish. The repair is to trace the actual claim and contribution, including absent or protected participation, rather than treating either the model or the meeting as authoritative.

Architectural tidiness can hide moved burden. Inspect the participant, specialist or recipient who now pays for the proposed improvement. A successful local variant remains local evidence, not proof that a profession has adopted it.

### PSD.16:7 - Conformance Checklist

| Check | Passing observation |
| --- | --- |
| Recognizable conflict | A specific engagement result and an interaction that can defeat one of its material conditions are identified; concurrency alone is insufficient. |
| Truthful anchor | Observed work and suspected mechanisms are distinguished; a prospective arrangement has a realization and later-test condition. |
| Non-isomorphic structures | Only relevant Method, work, subject, participation/authority, model/description or cultural accounts are used; their important relations and losses remain explicit. |
| Real alternatives | The incumbent and a materially different arrangement are compared for the same receiving use, including support, effort and moved burden. |
| Bounded decision | The chosen change or retained arrangement follows the actual remit; missing authority or specialist evidence remains a conditional return or blocker. |
| Intact Method and source use | Changes outside a Method's permitted variation return to Method selection; a new configuration does not inherit an old premise without qualification. |
| Interaction test | The changed join, participation condition or attention arrangement is tested at its claimed scope; document completion is not its success measure. |
| Usable continuation | The next recipient can recover what changed, what remains open, the consequential follow-up constraint and the smallest reopen condition. |

### PSD.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better move |
| --- | --- | --- |
| Turn the agenda into the architecture. | A sequence hides actual overlap, shared attention and authority conditions. | Recover the relations that change the current result. |
| Solve the model and declare the engagement complete. | Technical closure can exclude an unanswered interpretation or participation condition. | Qualify the technical return and preserve the missing contribution. |
| Separate everything to remove friction. | Extra handoffs can increase delay, exclusion and inconsistent assumptions. | Compare the moved burden with the conflict actually removed. |
| Add a challenger and claim absent people were represented. | A prepared perspective does not establish their participation or consent. | Keep the source and representation limit; obtain an appropriate direct contribution where needed. |
| Reuse the nearest available evidence package. | Its subject, version or horizon can differ from the current claim. | Qualify each consequential join or return its exact gap. |
| Declare a new culture after one workshop. | Local enactment supplies no observation of later transmission or retention. | Return the local variant and evidence to the distinct cultural question. |

### PSD.16:9 - Consequences

The engagement can return useful partial results without hiding how its work was arranged. Participants' corrections, specialists' premises and decision owners' authority remain connected but distinct. Necessary order is preserved without forcing all modelling, inquiry and observation into that order.

The cost is explicit coordination and sometimes a narrower or later return. Separate roles require support; separate channels require usable joins. Some conflicts remain with a specialist or authority owner. The gain is not friction-free work, but a defensible arrangement whose remaining limits the recipient can use.

### PSD.16:10 - Rationale

Method choice and faithful facilitation do not by themselves settle whether their enactment can satisfy several conditions at once. The same adequate inquiry Method may fail under one allocation of attention or one result-closing rule and remain usable under another. Conversely, an apparent scheduling change can replace a Method's essential confirmation or evidence condition.

The pattern therefore starts at one threatened result, recovers selected relationships, and compares arrangements through their consequences. This distinguishes structural interference from an ordinary claim disagreement and avoids reopening the entire engagement after each correction.

The choice is proportionate. A single sufficient sequence is retained when it works; a coupled arrangement is warranted when the actual interaction changes the answer. The result carries its residual and test because an architecture description cannot demonstrate the work it proposes.

### PSD.16:11 - SoTA-Echoing

**Practice question:** how should a practitioner alter a decision-support engagement when modelling, participation and result closure constrain one another? The selected line is a situation-qualified arrangement with explicit interactions and local tests. It is compared with a sufficient ordered Method, expert-only analysis and more intensive participatory arrangements; none is universally preferred.

| Question and selected answer | Serious alternative, defect and decision | Source role, limits and changed locus | Reopen condition |
| --- | --- | --- | --- |
| Which order can guide this engagement? Preserve supported dependencies while inspecting the actual model-building and participation interactions. | A fixed sequence is useful when it fits. **Adapt** a multi-structure account where that sequence hides interference; accept the extra coordination cost only for the threatened result. | Franco, Hämäläinen, Rouwette and Leppänen's [2021 behavioural-OR review](https://doi.org/10.1016/j.ejor.2020.11.031), especially §5.2, is a best-known-line synthesis and counterweight to an all-linear or all-nonlinear story: it reports relatively linear engagement paths alongside more complex model-building paths and situated facilitation. Its heterogeneous studies do not validate one arrangement here. This changes 4.1–4.3 and the local test in 4.6. | New comparative evidence or a failed join shows that the selected arrangement loses a consequential result or imposes unnecessary coordination. |
| Must modelling be completed before participants can affect it? Couple the contributions when their interaction changes the model's receiving use; retain expert analysis for a sufficient bounded technical question. | Expert-led production avoids some interaction cost. Fully joint modelling can expose meaning while consuming scarce attention. **Adapt**, rather than universally select, facilitated modelling and inspect consequential interpretations at their joins. | Franco and Montibeller's [2010 review](https://doi.org/10.1016/j.ejor.2009.09.030) supplies the operative expert/facilitated contrast, not a universal superiority claim. Franco and Nielsen's [2018 four-workshop study](https://doi.org/10.1007/s10726-018-9577-7) supplies situated evidence about facilitator formulations shaping interaction, not guaranteed consensus. These comparison contributions change 4.3–4.4 and 5.1. | Actual participation, meaning or support conditions defeat the proposed coupling, or a cheaper direct analysis now closes the use. |
| What if a homogeneous group lacks a material perspective? Consider a prepared challenge with distinct facilitation, not an invented voice for absent people. | Asking the same participants to argue both sides may add no missing information. **Adapt** the conditional challenge arrangement; **reject** its use as substitute participation or a universal staffing rule. | Cunico, Zimmermann and Videira's [2024 study, online 2023](https://doi.org/10.1080/01605682.2023.2263101), §§3 and 7, offers a serious alternative through one exploratory group-model-building application. Preparation, facilitator workload and role ambiguity are explicit trade-offs; effectiveness does not transfer automatically. It bounds 4.4 and the corresponding anti-pattern. | Direct participation becomes feasible, adequate perspective sources are absent, or the changed role damages inquiry or exceeds available support. |
| Is one model, agenda or hierarchy enough to settle the arrangement? Retain different structures through their warranted relationships. | A single view is cheaper when it preserves the needed distinction. **Adopt** the current `C.32.MWA` synthesis when it does not; **reject** layout as proof of a practice relation. | `C.32.MWA` supplies the common obtaining/prospective and several-structure Method. Here the applied decision concerns modelling, participation, challenge and return conditions; the synthesis alone supplies neither professional premises nor decision authority. This governs 4.1–4.2 and 4.5. | A direct relation or domain contribution changes the synthesis, or the conflict no longer needs several structures. |

These comparisons support bounded moves, not a universal workshop design or evidence of institutional effectiveness. Source change reopens the affected move or limit; it does not require every otherwise adequate engagement to restart.

### PSD.16:12 - Relations

- **`PSD.1` and `PSD.4` → `PSD.16`:** the bounded engagement question and usable scope frame this arrangement decision only for the same subject and receiving decision. They create no temporal order.
- **`PSD.2` → `PSD.16`:** the participation and concern account supplies only the participants and concerns material here; inclusion settles neither formulation nor authority.
- **`PSD.3` → `PSD.16`:** plural formulations enter where their inquiry changes the candidate arrangements. Agreement is not required and dissent remains explicit.
- **`PSD.5` → `PSD.16`:** the multi-model account is used only where it discriminates arrangement alternatives or claims. A representation does not make its subject obtain.
- **`PSD.6` → `PSD.16`:** the engagement Method and limits apply only to the named situation and qualification window. Availability establishes neither fit, enactment nor cultural uptake.
- **`PSD.7` → `PSD.16`:** shared and contested claims preserve material agreement and disagreement in this decision; the account does not make the decision.
- **`PSD.16` → `PSD.14`:** the bounded arrangement decision supplies a follow-up design constraint only when it changes that design choice. The receiver still generates and compares its own alternatives.
- **`PSD.16` → `PSD.17`:** the local decision may supply evidence or a variant for a named cultural-continuation question. Visibility proves no generation, transmission, enactment, recognition, selection, retention or effectiveness; absent evidence leaves the corresponding link unproved.
- **Direct FPF and specialist returns:** `C.32.MWA` supplies the several-structure synthesis; `A.15.9` supports reuse or acquisition of the exact missing practice result; applicable Method, Work, authority and evidence patterns govern their own claims. If a required input is absent, stale, out of scope or incompatible, use a qualified direct result or retain the exact gap. Pattern adjacency and a MethodDescription supply no performed result.

### PSD.16:End


<a id="psd-17"></a>
## PSD.17 - Deliberately Continue and Change Problem-Structuring and Decision-Support Culture

> **Type:** Method pattern (DPF)
> **Status:** Candidate
>
> **Primary working result:** an **account of the current enacted decision-support culture and one bounded cultural-continuation decision**, with the affected practitioners and variants, authority, retained alternatives, later observations where obtained, and explicit evidence gaps.

### PSD.17:1 - Problem frame

**Use this when** a decision-support practice needs to change how its ways of working are passed on, recognized, chosen or kept alive across practitioners and engagements. A new team copies a recommendation format but loses its uncertainty and dissent. A capable facilitator leaves, and the remaining library does not preserve how to handle a contested contribution. A service rewards decisive-looking recommendations so consistently that honest blockers stop appearing in its examples.

The wider activity is problem structuring and decision support. This pattern governs **deliberate continuation or change of its enacted professional culture**: the relations through which particular Methods, practical judgement, descriptions and norms are generated, transmitted, recognized, selected, remembered, retained or lost. It does not treat a school name, profession, publication or software platform as one thing that acts.

Start with an ordinary sentence: “In our flood-advice service, new facilitators learn from case examples and observation; the examples retain the models but omit why an unresolved service concern limited the recommendation; we are deciding whether to change the receiving practice exercise.”

That sentence identifies a possible intervention, not proof of its cause or success. Recover the actual practitioners, work and sources far enough to decide whether to retain the arrangement, change it, branch to another variant, investigate, or stop.

The gain is continuity of usable practice without compulsory uniformity. A receiving practitioner can preserve the important judgement or make a justified adaptation; the service can see what the intervention changed and what it did not.

**Do not use this pattern** merely to select a Method for one engagement (`PSD.6`), update a repertoire offering (`PSD.15`), resolve one current work conflict (`PSD.16`), publish a document, or count participation. Enter the cultural question only when a generation, receiving-enactment, recognition, selection, memory, retention or loss relation matters. A client holder's capability development or a non-cultural population's evolution is not automatically the culture of decision-support practice.

### PSD.17:2 - Problem

A practice can preserve its visible forms while losing the reasons that made them useful. A concern map becomes a diagram to complete. A conditional comparison becomes an unconditional recommendation. A workshop's apparent agreement becomes a claim that affected people were represented. These changes can travel through teaching, templates, peer imitation, commissioning and recognition even when nobody intends them.

The reverse failure is to resist every variation in the name of fidelity. A receiving team faces different access, values, uncertainty or authority conditions, but is told to reproduce the original format. It may preserve the carrier while making the Method unusable.

Neither a new edition nor one successful engagement settles this problem. The practitioner needs to distinguish what was made available, what reached another person, what was actually done, what was selected and retained, and what consequence followed. A bounded intervention can then be chosen without pretending to control an entire discipline.

### PSD.17:3 - Forces

| Force | Tension |
| --- | --- |
| Continuity and adaptation | Important judgements must survive transfer, while a receiving situation may justify different actions or support. |
| Recognition and plural practice | Shared standards can make good work visible; one prestigious school or decisive-looking result can suppress warranted alternatives and dissent. |
| Reach and receiving enactment | Publication and digital support can reach many people without showing that they can use the Method. |
| Local authority and distributed culture | A service can change its own arrangements; other practitioners and institutions may choose differently. |
| Useful judgement and incomplete evidence | A bounded, reversible change may be warranted before long-term retention or causation can be established. |
| Memory and protected information | Cases can preserve practical meaning, but source qualification, confidentiality and participant protection can limit what may be shared. |

### PSD.17:4 - Solution

Begin with the enacted practice and the relation that needs attention. Compare a small set of materially different continuation options, choose only within the actual authority, and observe the receiving practice and decision-support consequences. Keep the intervention decision, its performance and the cultural observations separate.

#### PSD.17:4.1 - Name the current practice, population and intended consequence

Name the current decision-support Discipline as practiced here, not as a universal school label. Recover the particular Method or variant, the practitioner population, the engagement or community, the place and period, the relevant carriers, and the recurring result at risk.

For example, the relevant practice may be a municipal team's attributed inquiry and conditional comparison, carried through observed facilitation, concern maps, model explanations and bounded recommendation accounts. The question is whether another facilitation team can preserve those contributions in its receiving engagements. “The spread of PSMs” is too broad for that decision.

State the intended professional consequence. It might be that material dissent remains attributable; a missing premise stays visible; a receiving team can distinguish a conditional comparison from a full recommendation; or an unavailable participant contribution is not replaced by an invented consensus. Preserve any cost in time, access, capability or useful analytical independence.

Recover the deciding person or System and the intervention boundary. When a precise Agent claim is needed, `A.13` requires the actual System, a local agential kind and its criterion, evidence of classification, an obtaining assignment, and the relevant scope, situation and window. A team name or collection of practitioners supplies none of these by itself. Authority to change facilitation, training, commissioning or publication is a separate fact; it is not authority to choose the client's investment or to direct another community.

A short recognition account need not become a complete culture inventory. If the target is one receiving exercise, keep unrelated traditions, networks and institutional changes outside. If authority is missing, return the exact decision or permission question. If the cultural relation is not the problem, take the cheaper direct return.

#### PSD.17:4.2 - Recover what the evidence actually shows

Use `C.36` for the cultural relations and their distinctions. Begin with concrete practice evidence: the changed instruction, observed interaction, qualified account of learning, receiving enactment, selection decision, retained example or demonstrated loss. Label expert estimates and conjectures. A lack of a population study does not prohibit a useful bounded judgement.

The following questions help keep different claims apart. Open only those that can change the current decision.

| Relation at issue | Evidence to recover | What the evidence does not establish alone |
| --- | --- | --- |
| Variant generation | The proposed or actual difference in the reusable way, its source and conditions, or the changed teaching, recognition or memory arrangement. | A new name or file does not identify a new Method; a proposal is not an enacted variant. |
| Transmission | What contribution passed from which source through which carrier or interaction to which receiving practitioner, when and under what interpretation. | Sending or downloading a document does not prove understanding, skill or receiving enactment. |
| Receiving enactment | A bounded actual occurrence in which the receiving practitioner followed the identified Method, with its meaningful conditions and result limits. | Attendance, stated intention or a copied output does not prove that the Method was followed. |
| Recognition and selection | Who recognized which contribution under what criterion, and which practitioner or institution selected which variant for what use. | A local project choice, credential or endorsement does not prove population-wide selection or fitness. |
| Memory | A recoverable description, exemplar, explanation or other carrier that preserves the distinction needed for reuse. | An accessible archive does not show that practitioners retain the ability or habit of using it. |
| Retention or loss | Evidence over the stated interval and relevant opportunities that a contribution continued, changed or ceased to be usable or enacted. | Silence, a missing publication or no opportunity to use the Method does not by itself establish loss. |
| Mediation | The actual tool, platform, community or publication arrangement and the visibility, interpretation, recognition or selection relation it changes. | A prominent display, recommender output or high access count does not establish value, control or cultural success. |

Keep claim scope smaller than or equal to the observed population and period. A workshop account may show one useful adaptation. A review of published applications may reveal cases to inspect. Neither establishes how every practitioner in a country works.

The `PSD.15` repertoire supplies a variant, lineage or bounded evidence only when it changes this cultural decision. Its offering status is not evidence of transmission. The `PSD.16` arrangement result can similarly supply a local change or observation; resolution of one interference is not evidence that another team learned it. If either input is absent, stale, out of scope or incompatible, obtain the exact direct contribution or leave the corresponding link unproved.

For a claimed performed occurrence, first recover each actual performer's `A.13` basis and independently admit the occurrence through `A.15.1`: performance history, enacted Method, extent and the obtaining containing-System relation. Add `F.6` only when precise assignment-bound attribution is consumed. Missing attribution does not erase independently established Work. A case packet remains evidence or description, not the occurrence.

Do not demand a complete causal history before a small permitted intervention. Do require enough evidence to distinguish the live explanations. If a new facilitator drops a concern, the cause might be an incomplete example, a changed participation condition, lack of skill, time pressure or the reward for a quick positive answer. Each can require a different change.

#### PSD.17:4.3 - Compare continuation options at the affected relation

Compare retaining the present arrangement, changing one material relation, maintaining a separate branch, and stopping or reverting the proposed intervention. Treat these as options when they are genuinely live, not as four mandatory forms to complete.

| Option | Useful question | Typical decision-support consequence |
| --- | --- | --- |
| Retain the present arrangement | Is the apparent failure outside its promised use, or is the current way already adequate at lower effort? | Preserve a useful narrow Method and avoid disrupting practiced judgement. |
| Change one arrangement | Would a change to facilitation, teaching, peer discussion, commissioning, recognition or source presentation address the identified mechanism? | Make the missing participation, interpretation or qualified-return move available in receiving practice. |
| Keep a separate branch | Do different access, participant or evidence conditions warrant different supported ways? | Preserve plural practice without pretending that all variants fit the same engagement. |
| Stop or revert | Does the change remove a protected condition, exceed authority, create an unmanageable burden or fail its stated purpose? | Return to a qualified arrangement, narrow the offering, or leave the receiving result explicitly blocked. |

Make the mechanism and trade-off explicit. Replacing a template may improve access but leave tacit facilitation judgement unaddressed. A guided practice exercise may expose that judgement but require an experienced facilitator and protected material. Changing recognition to include a well-grounded blocker can make honest returns visible, but a new checklist can also become another ritual.

A bundle of teaching, exemplar and peer-feedback changes may be one usable arrangement. If it is tried as a bundle, do not later attribute the result to one component without evidence. If the reusable decision-support action itself changes, return that Method or variant question to `PSD.15`; cultural desirability does not admit a proposed Method.

Keep the receiver's circumstances in the comparison. Translation, remote participation, professional-service conditions, available expertise and the ability to challenge an interpretation can change the required arrangement. Copying the source faithfully is not sufficient if the receiving use cannot enact its essential distinctions.

#### PSD.17:4.4 - Choose a bounded intervention without taking another decision

State who can choose the intervention, which options are actually available, the intended participation or decision-return consequence, the protected conditions, the resources and period, and what would stop, narrow or redirect the attempt.

Use `C.11` when that deciding System already has a formed bounded choice and another observation can change it. If the problem or options are still unclear, obtain the missing formulation, alternative or field probe-design result first. A cultural label is not a shortcut around that work.

Keep the choice local. A team may change its own case discussion, mentor arrangement or presentation of examples under its remit. It cannot thereby compel another team to adopt a Method, expose protected client information, certify practitioners, or decide the client's investment. An invitation, a receiving team's agreement and a service-wide rule have different authority and participation consequences.

Use the best qualified judgement proportionate to the decision. A reversible exercise with non-sensitive material may proceed on a stated mechanism hypothesis and modest evidence. A consequential service change may require stronger capability, professional, participant-protection and governance results. Obtain them directly; the cultural account does not invent consent, safety or competence.

Retain the serious alternative and the expected loss. The useful return can be “try one receiving exercise for this cohort, keep the present route for experienced staff, and do not extend the change until an independent receiving use has been observed.” That is a completed bounded decision even though its later effect remains unknown.

#### PSD.17:4.5 - Perform and observe only the intervention that was chosen

Translate the decision into the actual teaching, facilitation, community, recognition or publication work needed. Keep proposed action and work planning separate from performance. A planned tutorial, a posted file and an actual guided exercise are different facts.

When performance is claimed, use the recovered `A.13` and `A.15.1` basis. An investigation of a proposed decision-support variant may enact an independently identified trial or teaching Method without pretending that the unadmitted candidate whole was already enacted as a `U.Method`.

Observe the receiving use that matters. Ask a receiving practitioner to reconstruct why a concern was retained, which premise limited a comparison, what remained outside the compared set, or why a blocker was the appropriate return. This is a possible intervention design, not a universal teaching recipe. Check whether it is suitable for the population and the professional situation.

Do not make participation in a real consequential decision an uncontrolled training experiment. Preserve the actual access, competence, confidentiality, challenge, source-use and fallback conditions. If sharing the original case would break them, use a qualified redacted or constructed case, or choose another route; acknowledge what that substitute cannot test.

Identify the actual changed object when a change is claimed. An amended example set, an altered display rule and a changed practitioner action are not the same transformation. Use `A.3.4` and the direct effect or Work-to-change predicate when those claims matter. A performed intervention, an observed value and a causal-effect claim remain distinct; a log or temporal succession supplies no missing relation.

#### PSD.17:4.6 - Test the receiving consequence and competing explanations

Compare the later observation with the intended consequence at the same scope. Preserve the actual result even when the intervention did not work as hoped.

| Professional consequence | A useful observation | An unsupported stronger inference |
| --- | --- | --- |
| Participation and dissent | A material affected concern can enter, be corrected and remain attributable in the receiving inquiry. | More attendees or fewer objections means equal influence or consensus. |
| Uncertainty and evidence | The practitioner preserves the relevant configuration, horizon, qualification and unclosed premise. | A complete model or fluent explanation means every input is adequate. |
| Recommendation return | The account preserves the compared subset, inference, dissent, limits and the appropriate direction, set, probe, request, blocker or abstention. | A signed-off report is necessarily useful advice or an authorized later choice. |
| Receiving use | The named receiver can recover what this result permits and where it must return. | Delivery, access or a positive reaction proves understanding, reliance, implementation or effect. |
| Continuation | The identified contribution appears in an independently observed later use under stated conditions. | One coached performance proves long-term retention or practice-wide adoption. |

Distinguish a useful local outcome from an explanation of why it occurred. An improved return might reflect the exercise, prior experience, a more skilled facilitator, additional time, a different problem, easier evidence or changed authority. Keep those alternatives live where the evidence cannot distinguish them.

When the next question is how this practice may develop, retain more than one serious hypothesis and an observation that could discriminate. For example, an explanation-rich case library may support later independent use, or its effect may disappear without a mentor. A later uncoached case can inform that distinction; it does not isolate every causal influence.

Use `B.5` and `B.5.2` for hypotheses and testable consequences, `C.28` for an actual causal claim, and `A.3.3` only if a state-space and transition-law claim is needed. An ordinary uncertainty about continuation does not require a mathematical cultural-evolution model.

Ask practitioners and affected participants what was preserved, excluded or made harder. Retain dissent about the intervention itself. Reflective examination of practice can reveal a harmed relationship or lost contribution that a report count misses; it does not replace direct evidence needed for a claimed effect.

#### PSD.17:4.7 - Return the cultural account and keep its limits usable

Return the smallest account that lets the next user act. It should make the following recoverable without copying the entire history:

- the current practice, Method or variant, population, place, period and carriers;
- the cultural relation that justified attention and the evidence or labelled estimate;
- the bounded decision, actual authority, retained alternative and accepted cost;
- what was proposed, performed or changed, stated separately;
- the later receiving-enactment and decision-support observations, or their explicit absence;
- the unproved transmission, recognition, selection, retention, loss or causal links;
- the next observation, responsible return, narrowing or stop.

A decision can close before the later observations exist. In that case the result states what remains to be observed; it does not report a successful cultural change. Conversely, an observation can establish a receiving use without establishing that this intervention caused it.

Update the `PSD.15` repertoire only when the cultural evidence changes a Method offering, applicability, lineage or refresh decision. Return a changed current interference to `PSD.16`, an affected recommendation to `PSD.13` or `PSD.14`, and a capability or domain-truth question to its qualified owner. These are exact returns, not instructions to traverse the whole language.

Preserve the useful narrow incumbent and the unselected branch. A variant can be inappropriate for one receiving use while remaining valuable elsewhere. A deliberate decision not to continue it in a named setting is different from an unexplained loss across the profession.

#### PSD.17:4.8 - Refresh the affected relation or stop

Reopen when a consequential carrier, Method, practitioner population, receiving condition, source claim, authority or observation window changes; when the intervention loses its necessary support; or when evidence defeats the expected consequence. Trace the change to the particular cultural and professional claims it can alter.

A departure may remove mentoring capacity without proving that the Method was forgotten. A software update may alter which examples are visible without changing the decision-support Method. A source correction may invalidate one taught inference while leaving the rest usable. State the actual consequence and retain independent claims.

Use `A.10` for the bounded source reliance, `A.10.1` when several actual receiving uses of a changed source must be found and requalified, and `G.11` when its currentness or refresh-planning conditions obtain. Publication and access remain with their direct patterns. Neither source freshness nor carrier availability proves cultural continuation.

Close when the named decision, observation and return are clear. Stop or revert the intervention when its protected condition fails, its cost defeats the intended use, or no warranted next action remains. Do not keep generating variants or collecting cultural metrics merely because the entire culture cannot be proved.

### PSD.17:5 - Archetypal Grounding

The following cases are hypothetical. Observations stated inside them are additional case facts, not claims about actual communities, measured effectiveness, or the enactment of earlier proposed arrangements.

#### PSD.17:5.1 - Another team must learn the qualified return, not just its format

In a municipal flood-advice service, `DecisionSupportTeam-East` uses the identified attributed-inquiry and conditional-analysis Method. Its practitioners work with residents, finance, operations, ecology and emergency-service participants on the 2027 flood-pump question. Concern maps, model explanations, workshop records and recommendation accounts carry the practice.

The cultural question concerns East's practitioners and the receiving `DecisionSupportTeam-West` in the service's East district and controlled online case environment during March–May 2027. East may change its facilitation and teaching arrangements. West may choose how to prepare for its own permitted engagements. The board retains the investment decision.

The current practice already preserves a qualified fixed/mobile comparison, the unclosed staged alternative, and the reachable-assistance and protection questions. The `PSD.16` continuation supplies a bounded arrangement and correction route; the `PSD.15` repertoire supplies its applicability and lineage limits. Neither proves that West received or enacted this practice. The proposed late-correction Method whole retained for trial in `PSD.15` is still a candidate; this case does not admit or deploy it.

East sends a permitted case packet. West confirms that the file arrived. In a preliminary practice discussion, West's draft turns the conditional fixed/mobile comparison into an overall investment recommendation. The material service concern appears only in an appendix. The packet is available, but the needed interpretation did not survive this use. That observation does not show that West can never learn the Method or that every recipient misunderstood it.

East and West consider the following alternatives.

| Arrangement | Comparative reason |
| --- | --- |
| Keep sending the existing packet | Cheap and adequate for already experienced practitioners; the observed interpretation gap remains for this receiving group. |
| Add one guided qualification exercise using an explanation-rich case packet | West must explain what the comparison supports, what remains unclosed and why. This may address the observed gap, at the cost of experienced facilitator time. |
| Keep separate receiving routes | Experienced staff continue with the compact packet; practitioners needing the explanation use the exercise. This preserves differentiated support but requires clear entry conditions. |
| Stop the transfer attempt for this case | Necessary if source qualification, protected information, receiving capability or facilitation support cannot be secured. |

Within their stated remits, they choose the guided exercise for this receiving group and retain the compact route for experienced staff. The exercise and its packet are tested as one arrangement. No claim is made that the packet alone causes the improvement.

The hypothetical performer and occurrence basis is explicit. Both teams are independently recognized coordinated service Systems with defined boundaries and coordination Methods. The service's local inquiry-steward kind requires goal-directed, condition-sensitive regulation of inquiry and practitioner preparation, including correcting or stopping an unsupported return. Prior evidence establishes that each team meets that criterion. Its directly declared steward-appointment relation has distinct obtaining East and West assignments for the stated service scope and March–May window. These `A.13` facts do not grant investment authority or assert an Agency Grade.

The case separately supplies the performance histories: East's 12 March, 09:00–11:00 inquiry followed the attributed-inquiry and conditional-analysis Method; the two teams' 20 March, 09:00–10:30 exercise followed an independently identified guided-qualification teaching Method; and West's 10 April, 09:00–11:00 receiving inquiry followed the attributed-inquiry and conditional-analysis Method. A locally declared work-within-service relation applies only when the entire occurrence lies inside the service's defined facilitation or practitioner-preparation operations; the supplied boundaries and histories establish it for these three occurrences. They therefore have an `A.15.1` basis independent of the packet or timetable. This case does not need an additional assignment-bound `F.6` attribution claim.

During the exercise, West identifies the exact limit: “The fixed/mobile calculation is usable for its stated assumptions. It does not close the staged alternative or establish reachable assistance. Return those gaps with the qualified calculation; do not name an overall investment choice.” The facilitator challenges a substituted unqualified access premise. West keeps it outside the supported comparison.

In the later April inquiry, an independently observed receiving use preserves a resident's corrected service concern and the same distinction between qualified calculation and missing access evidence. The recommendation account retains the staged alternative as unclosed. No pump purchase, district-wide agreement or improved flood outcome is inferred.

The cultural return is deliberately narrower than “the service adopted the Method”:

| Claim | Supported result or gap in this case |
| --- | --- |
| Generation and memory | A new receiving-exercise arrangement and explanatory packet are recoverable; their source and intended use are explicit. This is not admission of a new decision-support Method. |
| Transmission and receiving enactment | The teaching interaction conveyed the qualified-return distinction, and one later West inquiry enacted the identified Method under stated conditions. File delivery alone did not establish either. |
| Recognition and selection | The exercise feedback recognized preservation of the conditional comparison and honest gaps. West selected that way for the named April engagement; this is not selection by the whole service or profession. |
| Retention and loss | One later receiving use is observed. Continuation beyond that interval, use by other teams and loss elsewhere remain unproved. |
| Intervention consequence | The intended distinction appeared in the receiving return. The evidence does not isolate the contribution of the exercise from prior skill, added attention or other conditions, and supplies no investment-effect claim. |

The next decision is to retain the receiving arrangement for one further qualified cohort and observe an uncoached later use. If mentoring becomes unavailable, the route is reconsidered rather than offered unchanged. East keeps the existing qualified Method and the compact route; the still-unqualified late-correction proposal remains a separate `PSD.15` candidate.

#### PSD.17:5.2 - A library of polished advice can hide the honest return

A non-contested development-advising service is considering a change to its case library. The display currently promotes the most-viewed positive recommendations. The service suspects that this makes a decisive-looking answer easier to copy than a warranted request or blocker.

The access records show visibility, not learning or enactment. Two explanations remain live: the display may shape what newcomers imitate, or already familiar cases may simply receive more views. The first useful result is a bounded inquiry into that receiving use, not a claim that the software caused a cultural failure.

One proposed arrangement pairs a positive example with a qualified non-choice return and asks a receiving practitioner to explain the difference. Retaining the current display is the cheaper alternative; removing the automated promotion rule is a possible fallback. The service must establish its own deciding System, remit, professional conditions and permission before changing the live arrangement; the flood-service authority does not transfer.

The constructed non-choice example is specific. An available allocation result supports an independent internal-development claim. The AI evaluation covers configuration A, while the request concerns B, and an external-provider alternative remains unassessed. A generated ranking of internal development above human–AI support cannot become the whole recommendation. The receiving practitioner should preserve the independent allocation finding, request the exact B qualification for the affected comparison, and keep the provider alternative open.

This exercise tests whether the distinction can be reconstructed from the library arrangement. It establishes neither actual client use nor cultural retention. A later permitted receiving engagement would supply different evidence. If the source gap is in the library's content rather than its display, the exact source claim must be repaired; rearranging examples cannot qualify B.

The culture at issue is the advisers' way of handling evidence and returns. The human client's learning, an organization's allocation capability, an AI configuration's performance and a population's evolution remain separate subjects. Better teaching of their boundaries supplies none of those domain conclusions.

#### PSD.17:5.3 - Publication coverage and ordinary non-use

A review finds few published PSM applications in a region. The service may use that observation to look for practitioners or cases, but it cannot conclude that the practice is absent, lost or ineffective. The journal/search boundary is not the boundary of enacted culture. A local continuation decision can use qualified practitioner evidence without first commissioning a global survey.

If the only task is to correct a source locator, use the direct source or publication guidance. If the only question is which available Method fits tomorrow's engagement, use `PSD.6`. Neither requires a cultural intervention.

A non-cultural population or lineage does not become a deciding Agent because it changes over time. Return that subject question to its direct practice. A researcher may separately choose an authorized intervention with its own scientific and governance basis; that does not turn the observed population into the recipient or chooser of advice.

### PSD.17:6 - Bias-Annotation

Prestige and publication bias can make visible schools look like the whole field. Preserve the actual population and evidence window, including qualified practitioner accounts and unobserved links.

Intervention bias favors changing something that already works. Keep the narrow incumbent, a cheaper continuation and stopping in the comparison. Fidelity bias pulls the other way: preserving the exact format can destroy the intended use under different receiving conditions.

Consensus and positivity bias reward smooth meetings and decisive recommendations. Inspect whether a dissenting concern, qualified non-choice or refused transfer remains recognizable and usable. Do not punish practitioners merely for exposing a genuine source or authority gap.

Automation and observer bias can make access counts or watched performances look like independent adoption. Distinguish what the tool displayed, what the practitioner understood, what was enacted later, and what the evidence cannot establish.

### PSD.17:7 - Conformance Checklist

**Recognition** asks whether a relation through which decision-support practice continues or changes is the missing result. One sentence naming the practice, receiving population, affected relation and next choice can be enough.

**Assurance** asks whether the authority, performer, occurrence, source, cultural and effect claims needed by that choice are qualified at their own scope. More elaborate records do not supply missing evidence. A small reversible intervention may use an explicit expert judgement; a broader effect or population claim needs its own basis.

| Check | Sufficient answer |
| --- | --- |
| Current practice | The Method or variant, practitioner population, engagement/community, place, period and carriers are recognizable. |
| Cultural question | The generation, transmission, receiving-enactment, recognition, selection, memory, retention or loss relation that changes action is named. |
| Intervention choice | A real decider and separate authority basis support the bounded choice; a serious alternative, cost and stop remain visible. |
| Receiving meaning | Participation, dissent, uncertainty, qualified comparison and recommendation-use distinctions survive or their loss is reported. |
| Performance and consequence | Proposal, plan, performed Work, actual change, observation and causal effect are not substituted for one another. |
| Evidence limits | Source coverage, estimates, observed occurrences and unproved population or retention claims remain distinct. |
| Continuation or return | The result names what is retained, changed, narrowed, unproved or stopped and which direct question should reopen. |

A missing link can block a stronger claim while leaving a useful bounded decision intact. The checklist is not a requirement to prove every cultural relation before any professional improvement.

### PSD.17:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Announce cultural adoption from a new edition or course | Recover actual transmission, receiving enactment and the population/period covered; retain the rest as gaps. |
| Teach only the finished model or recommendation format | Preserve the interpretation, material dissent, qualification and stop that made the result usable. |
| Make every receiving practice copy the source exactly | Compare the necessary meaning with actual access, capability and participation conditions; qualify an adaptation or retain a separate branch. |
| Treat a team title as intervention authority | Recover the deciding System's agency basis and the separate permission or authority for the named change. |
| Call one project choice population selection | State who chose what locally and obtain separate evidence for selection and continuation across practitioners. |
| Infer causation from a better-looking result after training | Preserve rival explanations and the actual scope of the observation; test the stronger claim only when the decision needs it. |
| Use popularity or publication counts as a fitness score | State what the measurement observes and recover the professional consequence that matters. |
| Keep intervening until all cultural links are proved | Close the bounded decision with honest gaps, retained alternatives and a specific next observation or stop. |

### PSD.17:9 - Consequences

A practice can continue important judgement without freezing one school or format. It can maintain different receiving routes, make a bounded intervention, and recognize that a well-grounded request or blocker can be a successful professional return.

The cost is attending to receiving practice and retaining inconvenient evidence. Some apparent adoption remains visibility, some short-term success remains a local observation, and some changes must be narrowed or stopped. The result is still useful before long-term or population-wide claims are warranted.

### PSD.17:10 - Rationale

The domain problem remains after the general cultural relations are separated. Decision-support culture must preserve how practitioners handle participation, contested meaning, values, evidence, uncertainty, alternative comparison and the boundary between recommendation and later choice. A generic account of copying or selection does not determine which of those professional contributions is at risk or how to repair its receiving use.

The pattern therefore starts from enacted practice and an intended decision-return consequence. It uses `C.36` for the cultural question and the direct patterns for agency, Work, evidence, choice, change and effect. It adds the professional comparison between facilitation, teaching, community, recognition and source-presentation arrangements.

A small intervention can proceed on qualified judgement without claiming general effectiveness. Keeping that distinction allows practical continuation and honest learning rather than either unbounded cultural control or paralysis until a complete history is known.

### PSD.17:11 - SoTA-Echoing

The working question is **how to continue useful decision-support judgement across practitioners and engagements without confusing visibility, prescribed practice, local performance and cultural consequence**. The selected line combines a bounded enacted-practice account, attention to receiving interpretation, comparison of actual continuation arrangements and evidence at the grain of the claim. It accepts the cost of observing practice; dissemination alone remains appropriate when availability is the only result needed.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| What can application reviews establish about a current culture? **Adapt** their reported cases as leads while retaining the corpus boundary. | A publication-based diffusion account is cheap to construct but misses unpublished practice and does not distinguish availability, enactment or retention. Sections 4.1–4.2 and 5.3 keep those claims separate. | [Kogetsidis (2025)](https://doi.org/10.1108/IJOA-08-2024-4746) and [Kogetsidis (2026 online)](https://doi.org/10.1108/EMJB-06-2025-0214) are dated application-review comparators, not required inputs to every case. The latter examines selected journals over 2010–2024, not a census or cultural-effectiveness trial. Reopen when better evidence changes the named population, relation or continuation decision. |
| What should a receiving arrangement preserve? **Adapt** a practice-facing account of context, trust, stakeholder engagement, facilitation and reflective professional learning. | A portable recipe or final-output template is useful when its meaning is already shared; alone it can hide practical judgement and ethical consequences. Sections 4.3–4.6 and 5.1 expose those receiving conditions. | Yearworth's [*The Practice of Problem Structuring*](https://doi.org/10.1002/9781119744856.ch6) and [*Evaluation*](https://doi.org/10.1002/9781119744856.ch12), published in 2024, present this practice-facing and evaluation line in their chapter summaries. They do not establish the effectiveness of the exercise proposed here. Reopen if a stronger practice account or receiving observation defeats the assumed mechanism or burden. |
| Does new AI-assisted problem structuring establish a transferable culture? **Retain as a candidate comparison**, separating generated material, human validation and later use. | A large shared output can widen the material considered, but treating that output as shared understanding or enactment loses the receiving problem. Sections 4.2, 4.5 and 5.2 require the exact receiving consequence. | [Voltan and Kells (2026), GOSR](https://doi.org/10.1002/sres.70125), is a contemporary conceptual proposal for facilitation with GenAI-assisted sensemaking. Its limitations include absent participant feedback and further practical testing; it is not evidence of widespread adoption or a universal PSD Method. Reopen on qualified receiving-use evidence, a changed tool/source condition or a defeated interpretation premise. |
| How might digital mediation change continuation? **Adapt** separate hypotheses about social learning and the mediating arrangement. | Treating a library or recommender as a neutral pipe ignores which variants become visible; importing a model's optimum into a professional service overstates transfer. Sections 4.2, 4.6 and 5.2 keep mechanism hypotheses and observations distinct. | [Czaplicka, Baumann and Rahwan (2025)](https://doi.org/10.1098/rsif.2024.0686) studies a simplified cultural-accumulation model combining network-based learning and algorithmic mediation. It supplies possible mechanisms for investigation, not a PSD field result or a prescribed mixing ratio. Reopen when an empirical or model result changes the specific mediation hypothesis under its stated conditions. |

### PSD.17:12 - Relations

- `C.36` supplies the cultural-evolution and intervention distinctions. This pattern retains the professional participation, interpretation, uncertainty and decision-return question. `C.36.P` can restore cultural wording when a label still hides the relied-on subject or relation.
- `PSD.15` supplies qualified repertoire evidence or a variant only when it changes the cultural-continuation decision. It neither entails nor authorizes that decision; absent or incompatible input leaves the exact link unproved.
- `PSD.16` supplies qualified local arrangement evidence or a variant under the same condition. A resolved conflict is not proof of transmission, receiving enactment, selection, retention or effect.
- `PSD.6` retains engagement-level Method selection; `PSD.7`–`PSD.14` retain participation, comparison, recommendation and follow-up results. Cultural work returns only a changed question to its direct owner.
- `A.13` and `A.15.1` qualify actual performers and dated Work; `F.6` applies only to a separately needed assignment-bound attribution. `A.3.1` and `A.3.2` distinguish the Method from its description or a candidate.
- `C.11` supplies a formed bounded choice; `B.5`, `B.5.2`, `A.3.3` and `C.28` govern the actual hypothesis, dynamics or causal question when needed. `A.3.4` and the direct Work-to-change or effect relation govern their own claims.
- `A.15.9` obtains an exact missing practice result; `A.10`, `A.10.1` and `G.11` apply to the bounded reliance, affected uses and currentness questions. Missing evidence does not create a whole-language prerequisite.
- Publication, access, archive or selected-set treatment, capability development and holder-specific truth remain with their direct patterns and qualified sources. Neither a cultural account nor a shared carrier supplies those results.

### PSD.17:End


<a id="psd-advising-development-direction-advising"></a>
# Development-direction advising

> **Publication use:** a practice-use profile of the Problem Structuring and Decision Support DPF.
>
> **Practical result:** a source-bounded development-direction recommendation, or the exact opportunity, premise, comparison or engagement result still needed.

<a id="psd-advising-use-this-when"></a>
## Use this when

Use this profile when a person, organization or AI arrangement is considering what to develop next, a distinct recommending performer must help a named recipient, and the answer depends on several qualified practices. The recipient needs a useful direction, retained set, probe, request, blocker or abstention for a stated horizon. They do not need to be in a dispute.

Development-direction work also has an earlier, independently useful branch: constructing an opportunity when the worthwhile problem or possible contribution is not yet settled. Enter [Construct a Bounded Development Opportunity](#psd-opportunity-use-this-when) directly for that question. A person can use it to explore future engineering Work without appointing an adviser or asking for a final recommendation. Its result is an opportunity with dependencies and a next question, not advice by another name.

This profile connects opportunity construction, the relevant PSD contributions and direct supplier results. It is not one compulsory Method with eight stages. The developing holder, opportunity, recommendation and later choice remain different objects. Human development, organization change, strategy, operations, AI engineering, safety and other practices keep their substantive Methods and conclusion authority.

The smallest useful result may be two sentences: “The available comparison covers internal development and configuration A, not the external-provider direction. Obtain the provider comparison for the same result, security boundary and horizon before ranking all three.” That is a complete bounded return.

Do not invent this engagement when a chooser already has adequate alternatives and needs only their own decision rule, or when one qualified domain Method answers the whole question. Use the direct domain or C.11 guidance. A non-cultural population or lineage without a population-local recipient or chooser belongs to its evolutionary account; a separately authorized researcher considering an intervention is a different case.

<a id="psd-advising-enter-at-the-missing-result"></a>
## Enter at the missing result

The entries below are alternatives, not a work order. An adequate result can be reused; a material change can reopen one contribution without reopening the rest.

| Working question | Start here | First useful return |
| --- | --- | --- |
| What useful future contribution could be possible? | [Opportunity-construction Method](#psd-opportunity-use-this-when) | A candidate opportunity, dependencies, bounded reachability rationale and next question; no adviser is required. |
| Who is asking for what advice, and on what terms? | [Bound the advising engagement](#psd-advising-bound-the-advising-engagement), using PSD.1 | A recipient/holder/horizon question and service boundary, or the missing condition. |
| What facts about this holder could reverse the answer? | [Recover only the relevant holder premises](#psd-advising-recover-only-the-relevant-holder-premises) | Exact current configuration and decision-bearing facts or gaps. |
| Which specialist result is missing? | [Use the direct result-acquisition Method](#psd-advising-use-the-direct-result-acquisition-method) | An adequately qualified existing result, a smallest-result request or a blocker. |
| Which directions are actually live, and how do they compare? | [Keep a qualified live candidate set](#psd-advising-keep-a-qualified-live-candidate-set) and [Compare for this receiving use](#psd-advising-compare-for-this-receiving-use) | A bounded set, comparison, partial order or discriminating question. |
| What can the recipient responsibly consider now? | [Compose the bounded recommendation](#psd-advising-compose-the-bounded-recommendation) and [Return it for the agreed use](#psd-advising-return-it-for-the-agreed-use) | One or more explicitly scoped recommendation dispositions with basis and limits. |
| Has something changed that affects earlier advice? | [Reconsider only affected advice](#psd-advising-reconsider-only-affected-advice) | Retained, narrowed or blocked claims; an exact supplier return; or a later recommendation. |

A qualified opportunity supplies a candidate basis to PSD.8; PSD.9–PSD.12 supply comparison premises to PSD.13; PSD.14 handles an actual follow-up question. Each dependency applies only to the same relevant holder, configuration, use and horizon. Neither these links nor their order establishes performed Work, a composite Method, dispatch or authority.

<a id="psd-advising-bound-the-advising-engagement"></a>
## Bound the advising engagement

Write the question in ordinary terms: “For this recipient, what development direction should this holder consider within this horizon, and for what later use?” Identify the recommending performer separately from the recipient at the grain of this application. The recipient may also be the choice owner when that authority is established. Calling one self-advisory actor by two role names does not establish the distinct-performer relation.

Use [PSD.1](#psd-1) for the engagement question and authority boundary. Distinguish client, sponsor, developing holder, recommendation recipient and chooser only where the difference changes the advice, disclosure, protection or decision. An employer paying for a person's career service does not thereby become the recipient of every personal assessment; a sponsor preferring a provider does not settle the committee's choice.

Before positive advice, establish the applicable service scope, competence, conflicts, confidentiality, permitted reliance and referral or closure conditions. These are professional relationship questions in addition to generic permission. The [ICMCI competence framework v4.0, C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf) supports agreed engagement content, client involvement and disclosure of material interests in management consulting. It does not authorize every adviser or prove that advice works.

For human career services, apply the actual professional conditions for informed participation, assessment competence, intelligible interpretation and appropriate referral. [NCDA's 2024 Code of Ethics, A.2, A.10 and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395) is a bounded professional source, not a universal rule for organizations or AI holders. Determine its applicability and any additional local requirements; do not infer consent or a client's capacity from a signed form alone.

AI assisting an adviser and AI being the developing holder are different cases. Where the [ICMCI AI Code v1.0, §§1.2, 2.2, 3.1–3.4, 5.1–5.4 and 7](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf) applies, the consultant retains responsibility, checks material AI-assisted content, respects client-data restrictions and explains material AI use and its limits. An unverified generated memo cannot acquire professional warrant from the tool's availability. The actual client relationship governs these duties even when the holder is an organization or a person.

Return the missing mandate, competence, conflict treatment, consent or admissibility condition when it prevents the requested service. A blocker can complete this recommendation application while obtaining professional duties remain in force. Existing safety, legal or emergency duties keep their own direct authority.

Do not require participant mapping, facilitation or a contested-situation workshop merely to admit a formed question. Open PSD.2–PSD.7 only when a participant, boundary, formulation, model, Method choice or disagreement can change this result.

<a id="psd-advising-recover-only-the-relevant-holder-premises"></a>
## Recover only the relevant holder premises

Ask which fact, if different, would change a direction, protected condition, comparison or return. Recover that fact for the exact holder and configuration; do not build an exhaustive diagnosis as an entry fee.

| Developing holder | Premises that can matter | What cannot substitute |
| --- | --- | --- |
| Person | Representative later Work; current capability and evidence; access and expression conditions; target demand; resources; acceptable burden; intervention and transfer premises; consent and choice boundary. | A job title, course attendance, a generic competence inventory or another person's successful transition. |
| Organization | Needed contribution and receiving use; current Work and arrangement; positions and assignments; authority and interfaces; continuity; resources; candidate obtaining arrangements; strategy and protected conditions. | An organization chart, purchased platform, provider promise or one successful employee. |
| AI model, agent or composite arrangement | Exact changed object and version; data, scaffold, tools or allocation; environment; evaluation validity; oversight and escalation; safety/security; baseline and protected conditions. | A human learning study, a benchmark from another configuration, a product label or a ranked recommender output. |

Current HCD demand, diagnosis and profile results can identify human premises; they do not, by that fact, establish an intervention's retention or transfer. OCE and Operations results can characterize a contribution or arrangement; they do not automatically compare every way of obtaining it. An AI result qualified for model/scaffold A is not evidence for B merely because both have the same product name.

For every material premise, keep its claim, exact subject, configuration, supplier/source, qualification window, uncertainty and intended use recoverable. “Unknown” is useful when it says what cannot yet be inferred. Absence of evidence for one configuration is not evidence that every configuration is infeasible.

<a id="psd-advising-use-the-direct-result-acquisition-method"></a>
## Use the direct result-acquisition Method

Use [A.15.9 — Request and Use a Bounded Result from Another Practice](../../../_current-pattern-hosts/A.15.9-Request-and-Use-a-Bounded-Result-from-Another-Practice.md) as the single inspect–reuse–request–qualify Method, with [A.10](../../../_current-pattern-hosts/A.10-Evidence-Graph-Referring.md) for the actual reliance claim. The using activity supplies the exact result question and the effect of a missing premise. In advising this is the recipient's advice question; in independent opportunity construction it is the next dependency question, without an advising engagement. Neither entry adds a second specialist-acquisition procedure.

An available result closes the need only when it covers the same material subject, configuration, use and window. An available MethodDescription says how a result might be obtained; it is not that result. The supplying practice chooses its Method and retains authority for its conclusion.

For example, request “a comparison of internal development, a provider and mixed support for this recovery result, ninety-day horizon, security boundary and continuity condition,” not “an organization-development strategy.” For a person, request the missing representative-Work demand or transfer premise, not “the right course.” For an AI configuration, request the relevant evaluation or safety disposition, not a generic endorsement of AI.

Use an adequate independent result while another branch is unresolved. State whether a missing premise prevents one claim, one candidate's admission, a pairwise comparison or the requested whole-set recommendation. Do not make the whole packet unusable merely because one unrelated source is old.

<a id="psd-advising-keep-a-qualified-live-candidate-set"></a>
## Keep a qualified live candidate set

If the useful future contribution itself is unsettled, use the full [opportunity-construction Method](#psd-opportunity-construct-a-bounded-development-opportunity). It searches neighboring uses, distinguishes a niche, a proposed provision promise and a worthwhile problem, constructs directions and supports, and exposes dependencies and reachability. A technology label or archive entry cannot fill that result.

Once candidate opportunities or an adequate formed question exist, use [PSD.8](#psd-8) to make the advice-relevant alternatives explicit. Keep each direction's status explicit: a feasible direction under stated conditions, a conditional opportunity, a candidate probe or a fragment retained for combination. Keep ruled-out configurations and named gaps visible as such, not as eligible alternatives. Do not let an attractive but conditional opportunity enter a decision-ready set as if its dependencies had obtained.

Keep materially different development, access/support, provider, Method/platform, allocation, staged and no-change directions when they matter. These are generation possibilities, not compulsory options. Several labels for the same intervention provide no real breadth. A different way of supplying the same result is not automatically a different worthwhile problem.

[OCE.8](../ORGANIZATION-CHANGE-ENGINEERING-FIRST-EDITION-HUMAN-AI-ROBOTIC-AND-PROVIDER-WORK-ARRANGEMENT-AUTHORING-CAMPAIGN/OCE.8-Configure-Human-AI-Robotic-and-Provider-Work-Arrangements.md) can supply the organizational same-result arrangement comparison after the required result, receiving use, horizon and acceptance premise are stable enough. It returns a changed or unjustified result premise to its owner; it does not supply this profile's whole opportunity search.

Use C.18 only for an actual generation/archive/front question, with its declared generator, operators, descriptors and retention or comparison basis. Use C.19 only for an actual live pool with a current governing policy. Thin evidence creates neither a default exploration posture nor permission to exploit. A probe needs a useful discriminating question and its own feasible, protected and authorized execution basis; otherwise return a proposed probe question or request.

<a id="psd-advising-compare-for-this-receiving-use"></a>
## Compare for this receiving use

Use PSD.9–PSD.12 for values, uncertainty, consequences and robustness. State the exact candidate domain and compared subset, the receiving question, characteristics and scales, protected conditions, evidence and uncertainty, and the comparison rule that the result actually uses. Adequate current comparison results can be reused without running all four patterns.

C.16 supplies characterization; C.11.CRC preserves configuration-relative contribution; A.19.CPM supplies a comparison mechanism when its conditions hold. Consume a G.5 selector result only when its candidate domain, eligibility, Method, evidence, result kind and closure are actually established. A ranked list is not proof of that application.

Explain what the comparison can and cannot conclude. Preserve a partial order or non-dominated directions when the basis does not warrant a total ranking. If one direction is supported, explain its advantage over the strongest remaining rival and the conditions that could reverse it. Keep important value disagreement visible instead of manufacturing a shared weight.

Human consent and transfer, organization continuity and AI safety remain unlike premises. A protected condition cannot be compensated away by a favorable total score. Likewise, a comparison of internal development and one mixed arrangement does not rank an unexamined provider, another model version or a materially different probe.

When evidence is thin, first ask whether the missing distinction could change the answer and whether obtaining it is worth its burden and delay. A small exact request, a retained set or a blocker may be more useful than another elaborate model. A declared comparison is an input to advice, not the recipient's choice.

<a id="psd-advising-compose-the-bounded-recommendation"></a>
## Compose the bounded recommendation

Use [PSD.13](#psd-13) to return what the recipient can responsibly consider now. The following development-direction returns are alternative result branches, not a sequence.

| Return | When it is useful | Content that makes it more than a label |
| --- | --- | --- |
| Retained or ranked set | Several directions remain live and the current scheme supports their trade-offs, partial order or order. | The exact set and scheme, what preserves each direction, what remains unresolved and what could warrant narrowing. |
| Supported direction | Qualified premises justify preferring one direction for the named holder, use and horizon. | Its comparative advantage, the disposition of serious rivals, material limits and reversal conditions. |
| Bounded information-gaining probe | A specified uncertainty could reverse advice and the supplied probe basis supports proportionate information gain. | Question, possible distinguishing observations, exposure, feasibility, protected conditions and stop; choice and execution remain separate. |
| Smallest-result request or handoff | A supplying practice owns a premise that can change the answer. | Exact result needed, subject/configuration/window, affected claim and what would let advice resume. |
| Blocker | A missing, stale, inapplicable or unauthorized premise prevents the requested responsible recommendation. | What is missing, which stronger conclusion is blocked and which independent content remains usable. |
| Abstention | The requested recommendation premise fails or the service cannot responsibly supply that kind of advice. | The failed premise and appropriate receiving account or referral, without an invented adverse factual judgment about the holder. |

A mixed return can retain two directions, request a third direction's missing premise and block a complete ranking. Keep the scopes explicit; do not report mutually inconsistent overall statuses.

For this profile, the recommendation account makes seven things recoverable:

- the recommending performer, recipient, developing holder, question, horizon, choice owner and intended next use;
- the actual candidate domain, compared subset, exclusions and candidate gaps;
- each relied-on specialist result and relevant source edition, configuration, window and reliance limit;
- the declared comparison scheme, material trade-offs, protected conditions and inference to the return;
- uncertainty, dissent, evidence losses and unsupported extensions that can alter reliance;
- the supported disposition and the next consideration, request, reroute or separately governed choice;
- the exact observation, source, configuration, authority, horizon or policy change that would reopen a named claim.

This is content, not a mandatory form. A small blocker needs only the positions that explain its missing premise and receiving use. A consequential positive recommendation may need a protected annex and a fuller claim-to-premise account.

Keep each claim inside the narrowest material limit of the premises on which that claim depends. If evaluation covers configuration A, advice about B remains unsupported. If the internal-development comparison does not depend on that evaluation, it can remain usable. A shared bibliography is neither a dependence relation nor a reason to invalidate everything together.

<a id="psd-advising-return-it-for-the-agreed-use"></a>
## Return it for the agreed use

Lead with the disposition and its most important limit. Explain the evidence and reasoning at the recipient's level, including what the result does not authorize. If a decisive premise cannot be disclosed, state the resulting reliance restriction without revealing protected content.

For an actual receiving-use problem, use A.2.9 to ask what the recipient needs to understand or do, what evidence would show that the return serves that use, and what smallest repair is needed. Making a conditional recommendation intelligible is different from persuading the recipient to accept it.

Delivery completes the recommendation application; it proves neither understanding nor reliance, consent, choice, implementation or effectiveness. Acknowledgement is not a ChoiceResult. A programme, course, organization-change plan, assignment, provider commitment or performed Work needs its own content and authority.

The actual professional relationship may require further contact, disclosure, referral or service closure. Those duties do not disappear when this recommendation is delivered, and they do not arise merely because a profile mentions follow-up. Sales persuasion, psychotherapy, teaching and implementation remain different Methods with their own conditions.

<a id="psd-advising-reconsider-only-affected-advice"></a>
## Reconsider only affected advice

Use [PSD.14](#psd-14), A.10.1 and the direct currentness owner when a change can alter advice. Locate the changed premise and the claims that actually used it; preserve the earlier recommendation as an account of what was returned under its earlier basis.

| Changed premise | Bounded response |
| --- | --- |
| Human assessment no longer covers the target Work or current person | Remove that assessment's support from the affected capability or intervention claim; obtain the exact human-domain result. Preserve unrelated organization or AI claims. |
| AI model/scaffold A is replaced by B | Requalify B's evaluation, safety and contribution premises. Retain only claims whose basis survives the change. |
| Provider access or security condition changes | Reopen the affected provider or mixed-arrangement claim and any ranking that depended on it. Do not infer that internal development failed. |
| Consulting scope, conflict or disclosure conditions change | Revisit the affected service return and permitted reliance, not the truth of every domain result. |
| An opportunity's useful problem or support dependency changes | Return to the corresponding opportunity claim; reassess any retained stepping stone and dependent advice. |
| A changed observation crosses the advice's stated threshold | Use the qualified observation and interpretation to retain, narrow, block or reopen the affected contribution; compose another recommendation only when needed. |

Observation, interpretation, professional contact and renewed recommendation are distinct Work. If positive advice depends on future observations, establish who can obtain and qualify them, with what access, timing, burden and response opportunity. An infeasible observation obligation is a present limit on advice. “Review in three months” does not by itself make an effective follow-up arrangement.

The source-currentness responsibilities for this profile and its opportunity Method are specified in the [source-responsibility account](DEVELOPMENT-DIRECTION-SOURCE-RESPONSIBILITY.md). A change to the generation Method can require revising that Method; a changed fact about one holder normally requires only requalifying the affected application.

<a id="psd-advising-worked-uses-and-stopping-points"></a>
## Worked uses and stopping points

The examples below are constructed cases. Assumed specialist results illustrate what a warranted return would require; they are not results about actual clients, performed Work or demonstrated intervention effects.

<a id="psd-advising-a-ninety-day-service-reliability-question"></a>
### A ninety-day service-reliability question

A committee asks a separate advisory team which development direction the service organization should consider over ninety days. The committee is recipient and, under the case's assumed mandate, choice owner. The three live directions are internal development, an external provider and a mixed human–AI arrangement. Critical-service continuity, a security boundary and a capped reversible-probe budget are protected. The adviser discloses and resolves a material provider interest under the agreed engagement conditions before offering positive advice.

An operating account identifies the recovery contribution in question. Organization information describes relevant positions and interfaces. A qualified priority statement puts reliability before throughput for this horizon. None of those results compares the whole obtaining arrangements. The current OCE.8 Method is available to guide that comparison, but no adequate result for this client is supplied.

The first complete return is therefore:

> The available basis does not support ranking the three development directions for this ninety-day reliability use. Obtain the whole-arrangement comparison for the stated result and protected conditions, including provider access, continuity, recovery and security premises. The operating and position/interface accounts remain useful inputs.

The adviser first checks for an existing result covering that exact use through A.15.9. If one is adequate, no new supplier Work is needed. If not, the request goes to the organization-allocation and relevant specialist owners; they choose their Methods.

Now consider a separate hypothetical continuation. A qualified whole-arrangement comparison and security result cover the three named directions. They exclude the specified provider configuration because it cannot preserve the security boundary. Internal development remains feasible but does not resolve the mixed arrangement's key uncertainty: whether permitted AI assistance can reduce the recovery queue without imposing an unacceptable verification burden or weakening fallback.

The supplied probe account covers the exact mixed configuration, bounded exposure and resource budget. It makes the distinguishing observations recoverable: representative recovery evidence, verification burden and fallback performance under the protected continuity condition. It supports the probe as proportionate, not as proof of eventual improvement. Compared with committing directly to either development direction, the probe can resolve that specific uncertainty at the bounded cost while preserving internal development as an alternative. The advice can therefore be:

> Consider the bounded mixed-arrangement probe first, retaining internal development. The supplied allocation, probe-feasibility and security results support this information-gaining return for the ninety-day reliability question. Throughput effect is still uncertain. Preserve service continuity, security and the probe budget; reconsider when representative recovery evidence or a relied-on premise changes.

This is not whole-set closure from an internal/mixed-only comparison: the supplied security result explicitly disposes of this provider configuration. A different provider, another mixed configuration or a substantially different probe reopens its own premises. The committee's choice, any authorized probe WorkPlan and later Work remain separate.

<a id="psd-advising-a-person-considering-four-months-of-development"></a>
### A person considering four months of development

An engineer asks a separate career adviser whether to develop cross-functional management capability or pursue a specialist engineering direction over four months. The person is the developing holder and recommendation recipient; their own choice and the employer's separate assignment decisions must not be conflated.

The relevant input is representative later Work, not the management title. A qualified demand account might distinguish coordinating a cross-discipline review from supplying a difficult technical analysis. Current capability, accessible practice, time, consent, assessment limits and target-domain requirements can change which direction is plausible.

If only attendance and a course catalogue are available, return the missing intervention or transfer premise; do not prescribe the course or assert reachability. If qualified premises support both directions but not their order, retain them and name the distinguishing question, such as which representative Work the person can validly try within available support and time. The human branch uses current career information critically, as in [NCDG 2024, CD2 and CD3](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page); it does not infer learning transfer from career-information quality.

Before any separate advice request, the same person may independently use the [opportunity Method's human example](#psd-opportunity-a-person-exploring-future-engineering-work). That entry does not require the distinct adviser assumed here.

<a id="psd-advising-an-ai-or-composite-holder"></a>
### An AI or composite holder

An authorized team asks a separate recommending arrangement whether to modify a model, change a scaffold/tool configuration or alter human–AI Work allocation. Recover the exact object and version, intended environment, evaluation validity, oversight, protected conditions and receiving use. Model tuning, tool access and human–AI allocation are not interchangeable interventions.

Suppose a supplied evaluation supports scaffold A only in a bounded offline environment, while a proposed direction uses B with different tools. The correct return is a request for B's relevant evaluation and safety premises, not transfer of A's score. A separately adequate organization-allocation comparison can remain usable within its own assumptions.

If an applicable safety result excludes one configuration, exclude that configuration for the stated use. If evidence is merely missing, say so. A human course study supplies neither AI adaptation nor deployment safety. A recommender-system ranking can enter only as its separately qualified input; it is not the whole advice Method or deployment authority. Professional duties to human clients still apply where that service relationship actually exists.

<a id="psd-advising-a-population-without-a-recipient-and-an-inadmissible-engagement"></a>
### A population without a recipient, and an inadmissible engagement

A request to tell an unmanaged lineage which direction it should choose has no population-local recipient or chooser in this account. Abstain from that attribution and return variation, selection, reproduction, persistence and loss to the evolutionary source. Do not redescribe evolutionary change as recipient choice.

A research team may instead ask which authorized experimental intervention to consider. That is a separate recipient-owned question whose scientific, safety, ethical and governance premises must be established; the evolutionary countercase supplies none of them.

Likewise, a sponsor's instruction to conceal a material conflict or to rank a harmful unauthorized option cannot be repaired by a better score. Return the scoped blocker, referral or abstention required by the applicable professional and domain conditions.

<a id="psd-advising-recognition-assurance-and-practical-gain"></a>
## Recognition, assurance and practical gain

Recognition is inexpensive: another performer must help a named recipient make sense of qualified but incomplete development premises. A formed question can enter directly; a not-yet-formed opportunity can enter the independent Method. No institutional dispute, complete diagnosis or global candidate archive is required.

Assurance is use-specific. Check whether the material premises actually cover the holder, configuration and horizon, whether the comparison and recommendation follow from them, and whether service, protection and authority conditions permit the proposed reliance. High-consequence uses require their direct domain validation and independent assurance. A coherent profile, fluent explanation or available source does not establish those results.

In practice, a development request no longer silently becomes a course, staffing choice, organization-change programme or AI deployment. The recipient can see what is supported now, which alternatives remain, which exact result is missing, and what would change the advice. The developer of an opportunity can stop even earlier, with a useful possibility and a discriminating question.

The [source-responsibility account](DEVELOPMENT-DIRECTION-SOURCE-RESPONSIBILITY.md) separates contemporary decision-support and professional sources, historical generation anchors, exact supplier guidance and application-specific results. It also states the bounded update responsibility. This profile claims neither universal cross-holder effectiveness nor that publication of a supplying framework has already produced any particular client's evidence.


<a id="psd-opportunity-construct-a-bounded-development-opportunity"></a>
# Construct a Bounded Development Opportunity

> **Kind of account:** MethodDescription for one reusable opportunity-construction Method.
>
> **First useful result:** a candidate opportunity with a worthwhile problem or proposed promise, dependencies, bounded reachability rationale, uncertainty and a next discriminating question.

<a id="psd-opportunity-use-this-when"></a>
## Use this when

Use this Method when a person or team is exploring what useful future Work could become possible for a named holder, but the problem, contribution or development direction is not yet fixed. A new technology, an emerging use, a changed constraint or dissatisfaction with familiar options may prompt the inquiry. The useful result is a constructed possibility that another person can inspect, not a list of fashionable subjects.

This is the opportunity-construction branch within the broader [development-direction advising profile](#psd-advising-development-direction-advising). It governs how a possible direction is made meaningful and conditionally reachable. It does not govern another person's recommendation, a development intervention, strategic commitment, procurement or the eventual choice.

A separate adviser is not required. A person exploring future engineering Work can begin here and stop at an opportunity or exact next question. If another performer later gives advice to a named recipient, the profile's engagement, professional and choice boundaries apply then.

Do not use this Method to reopen an adequate option set merely because more ideas could be generated. Use the direct choice or comparison Method when the worthwhile result and live alternatives are already sufficient. Use a qualified specialist Method directly when it owns the whole question. An evolutionary account of a population without a recipient is not a development-direction choice; a researcher's intervention question needs its own science and authority basis.

A complete first return can be modest: “This contribution could address the named receiving-use problem, but only if access to these records and the required review support can be obtained. The next question is whether the data owner can provide that bounded access.” Missing feasibility does not have to erase the useful problem; it prevents a stronger reachability claim.

<a id="psd-opportunity-the-reusable-way-described"></a>
## The reusable way described

The Method identified under [A.3.1](../../../_current-pattern-hosts/A.3.1-U.Method.md) is: construct a bounded development opportunity by relating possible later Work to neighboring uses and technologies, distinguishing a useful problem from an offered promise, constructing materially different directions and supports, qualifying their dependencies, and returning the strongest supported reachability claim and next question.

Its generic participants are the person or arrangement conducting the inquiry, the developing holder or subject, possible receivers or users of the later contribution, and sources or suppliers of material premises. They are Method-side meanings, not actual assignments or Work participants. The inquiry performer may also be the developing person; no distinct recommendation recipient is an applicability condition.

The minimum applicability is a recognizable later-Work concern or aspiration, a holder or bounded candidate holder, a useful horizon, and enough context to ask what would matter and what is protected. Some of these may be provisional. If they cannot be made specific enough to distinguish a useful possibility from a slogan, return the missing frame before claiming an opportunity.

The invariant result is an opportunity account or an honest gap, rejection or stop. It preserves the distinctions among possible value, supplied evidence, conditional reachability, actual access/support, recommendation, choice, plan, Work and effect. Holder, horizon, search seeds, technologies, suppliers and presentation can vary without changing that way of doing. Removing source qualification, treating a candidate as a commitment, or changing the result into advice to a distinct recipient changes the identification question.

This is one identified U.Method, locally designated **PSD-DEVELOPMENT-OPPORTUNITY-CONSTRUCTION**. Under [A.3.2](../../../_current-pattern-hosts/A.3.2-U.MethodDescription.md), the claim-bearing account in this document is its MethodDescription, locally designated **PSD-DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-2026-09-02-E1**. Its C.2.1 identity uses these claims, that exact Method as EntityOfConcern, and the effective reference scheme expressed by the distinctions below. The designators are locators. This identification establishes no actual enactment, capability, permission, successful development or empirical effectiveness.

<a id="psd-opportunity-working-distinctions"></a>
## Working distinctions

| Ordinary term | Meaning in this Method | Nearest tempting overread |
| --- | --- | --- |
| Later Work | The future work or contribution whose usefulness is being explored, at a grain sufficient to identify a receiver, situation and horizon. | A Work family or future description is not a dated Work occurrence or a WorkPlan. |
| Niche | A tentative match between a possible contribution and a receiving use under particular conditions. It is ordinary working wording, not a new universal kind. | A market category, technical novelty or empty space in a map does not show that anyone needs the contribution. |
| Proposed provision promise | A statement of what could be offered to a receiver, under which conditions and acceptance expectations. An existing promise is read from its exact source; a proposal is marked as a proposal. | A proposed offer is not an actual commitment, provider capability, access, provision or fulfilment. |
| Worthwhile problem | A problem statement with a named affected use, an unsatisfactory or foregone result, its significance and the conditions under which addressing it could be worth the burden. | Enthusiasm, prestige, a supplier's claim or the phrase “there is a problem” is not enough to establish actual need or value. |
| Direction and support configuration | A materially different possible change, together with the capabilities, access, Methods, people, tools, resources and relations it would require. | A candidate configuration is not an obtaining arrangement or an authorized intervention. |
| Bounded reachability | A source-qualified claim about whether specified transitions toward the candidate contribution could be made within the stated horizon and protected conditions. | Plausibility, a drawn path or success for a different holder is not proof that this holder can get there. |
| Stepping stone | A candidate or retained intermediate possibility with an explicit later option or region it could open. | Something easy, novel or educational is not automatically a stepping stone, a current best option or a justified probe. |

When promise content itself becomes a relied-on claim, use [A.2.3](../../../_current-pattern-hosts/A.2.3-U.PromiseContent-Promise-Content.md); commitment, provider, access and fulfilment remain separate. When a claim needs an actual Problem or problematic-for relation, use its direct problem pattern and evidence. This Method can work with explicitly provisional problem statements without inventing those stronger relations.

<a id="psd-opportunity-prepare-the-smallest-useful-inquiry"></a>
## Prepare the smallest useful inquiry

State the holder, prospective later Work or concern, receiving situation, horizon, protected conditions and inquiry budget. Name what is known, what is merely suggested and which questions the inquiry may investigate. Include permissions needed for the inquiry itself; permission to read or ask is not permission to trial an intervention.

Do not demand a fully specified goal before discovery. “Explore a useful contribution to engineering handoffs in the next quarter” can be enough to begin if the possible receivers and stakes are recoverable. “Develop in AI” is not enough to end: it still needs a useful problem, contribution and dependency account.

A small reversible inquiry may use a few relevant source checks and conversations. A consequential commitment will need much stronger domain evidence, but that is not a reason to manufacture certainty during opportunity construction.

<a id="psd-opportunity-method"></a>
## Method

The six working sections unfold one reusable way. They express information dependencies and permit iteration; they are not six separately admitted submethods or a schedule. Return to the earliest changed claim, not automatically to the beginning.

<a id="psd-opportunity-1-recover-the-later-work-and-the-reason-to-explore"></a>
### 1. Recover the later Work and the reason to explore

Describe what the holder might contribute, for whom, in what situation and over what horizon. Distinguish the receiver's useful result from the holder's desired learning, status, product or technology use. Ask what would remain unsatisfactory if nothing changed, and whether the receiver actually cares about that difference.

Keep alternative formulations when they materially change the opportunity. One inquiry may concern recovering an acceptance premise; another may concern supporting shift handoffs. Those are not merely two implementations of one already accepted result. Use PSD.3 when competing formulations require substantive problem-structuring work.

Start from a qualified demand or problem account when one exists. If the reason to explore is only a supplier's enthusiasm, preserve it as a search lead, not as an established need. If the receiver says the proposed result is unnecessary, revise the contribution or reject that lead.

<a id="psd-opportunity-2-search-neighboring-technologies-uses-and-characteristics"></a>
### 2. Search neighboring technologies, uses and characteristics

Search from more than one direction. Work from an affected use toward possible support, from a technology toward unlike applications, and from a desired characteristic toward different ways of obtaining it. For each lead, record the source and the concrete difference that could matter.

| Search move | Question that changes a candidate |
| --- | --- |
| Neighboring use | Where does a comparable receiving difficulty occur, and what changes when users, scale, timing, environment or acceptance conditions differ? |
| Neighboring technology or Method | What other way could supply the contribution—manual, organizational, technical or mixed—and what does its source actually demonstrate? |
| Neighboring characteristic | Could a different latency, reliability, reversibility, accessibility, interpretability or burden create a useful contribution even without a new technology? |
| Combination or changed support | Could a known contribution become useful through different access, review, interfaces, resources or a bounded sequence of supported steps? |

Use explicit value questions to generate possibilities, rather than scoring only the first available products. Keeney's [2012 value-focused brainstorming](https://pubsonline.informs.org/doi/10.1287/deca.1120.0251) is a historical Method anchor for that move and for individual generation before group anchoring when a group is involved. It is not a requirement for a workshop, proof of current prevalence or a reachability theory.

Name the generation operation actually used—for example, substitute the receiving use, vary the required characteristic, combine two support contributions or remove an assumed technical constraint. Keep the search scope, source dates and stopping reason sufficient for the next use. Search time, idea count, novelty score and geographic distance from an archive are not evidence of practical value.

Stop widening when the inquiry has enough materially distinct leads to expose the decision-bearing unknowns at its chosen effort, or when a missing domain premise prevents useful further construction. State unsearched areas if their omission can change the return. Do not claim exhaustive search.

<a id="psd-opportunity-3-turn-a-lead-into-a-problem-and-a-proposed-promise"></a>
### 3. Turn a lead into a problem and a proposed promise

For each serious lead, connect four things in ordinary language: the receiving situation, the useful difference, the proposed contribution and the evidence or hypothesis linking them. Then ask whose facts or judgment can confirm whether that difference matters at the needed scale.

For example, “use a new model in engineering” may become “help a receiving engineer recover which acceptance conditions a supplied evidence package does not yet support.” The proposed promise concerns recoverable qualification information, not faster approval, higher quality or automatic acceptance. Those stronger benefits need separate evidence.

Keep the niche, problem and promise distinct. A niche names the possible fit. The problem explains why the missing or inadequate result matters. The proposed promise says what could be supplied and judged. A useful research opportunity need not be a commercial offer; it still needs a worthwhile question and an inspectable result.

Reject or revise a lead that has no supported worthwhile problem after proportionate inquiry. If value remains uncertain, retain a problem hypothesis with the exact confirming question, not a positive value claim. A provider's existing promise is evidence about what it offers, not that this receiver needs it or that it will be fulfilled.

<a id="psd-opportunity-4-construct-different-directions-with-their-supports"></a>
### 4. Construct different directions with their supports

Build materially different possibilities for addressing the problem or realizing the contribution. Change the intervention, the work performed, the distribution of contributions, the support, the timing or the proposed result where those differences matter. Distinguish a different result premise from a different way of obtaining one result.

A direction should say more than “train,” “buy,” “automate” or “hire.” State the prospective contribution, the holder change if any, necessary access and support, protected conditions and the transition that would have to become possible. One option may develop a capability; another may make an existing capability usable through better access; a third may obtain a qualified external contribution.

Use PSD.8 for the live alternative-construction question. Use direct HCD, OCE, AI, target-domain and other results for what the proposed changes would require. After one result/use/acceptance premise is stable, OCE.8 can compare whole organizational obtaining arrangements. Before that point, forcing every lead into the same-result comparison would conceal the still-open opportunity question.

Retain the obtaining baseline, a smaller repair, a staged direction or no change when they genuinely answer the inquiry. Do not count a fragment as a complete direction merely to populate a table, and do not discard a potentially useful contribution only because its supporting arrangement is not yet designed.

<a id="psd-opportunity-5-qualify-dependencies-and-bound-reachability"></a>
### 5. Qualify dependencies and bound reachability

Identify the premises whose absence would block the proposed transition or change its value. Typical dependencies concern holder capability, usable access, available support, resources and time, supplier contribution, acceptance, authority, safety or continuing Work. State who owns each premise and what result is adequate for this exact use.

Obtain or qualify those results through the [profile's single A.15.9 import](#psd-advising-use-the-direct-result-acquisition-method); do not perform an unqualified diagnosis or invent a supplier's answer. Inspect adequate existing results before requesting new ones.

For each material transition, state the relevant starting condition, the proposed change, the enabling premises, the evidence and uncertainty, and what could prevent completion within the horizon. Keep the joint condition visible: two individually feasible steps may compete for the same person's time, data access or budget. A chain is not feasible merely because each box sounds feasible.

Use the strongest honest wording:

| Basis | Reachability claim or return |
| --- | --- |
| Qualified premises cover the necessary transitions and their joint limits for this holder and horizon | State the bounded reachability supported by those premises, including residual uncertainty and protected conditions. This is not an observed effect. |
| A worthwhile candidate depends on a still-missing access, capability, support or resource result | Retain the conditional opportunity and state exactly which reachability claim cannot yet be made. Request that premise. |
| A qualified condition rules out the proposed transition | Reject or revise the affected direction for that use; preserve another direction whose basis is independent. |
| The path is only a metaphor, similarity or label | Return an unresolved candidate, not a reachable next step. Name the first fact needed to make the path meaningful. |

A person's capability envelope, an access/expression differential and a particular recovery test answer different questions. None alone selects an intervention or proves learning transfer. An AI benchmark, an organization allocation result and a provider promise have equally specific boundaries. Do not transfer one holder's mechanism or evidence to another by analogy.

A “zone of proximal development” label, curriculum sequence or archive path establishes none of the missing transitions. Use the exact direct human, AI, engineering or other feasibility result, or leave the claim conditional.

<a id="psd-opportunity-6-preserve-useful-stepping-stones-and-return-the-next-question"></a>
### 6. Preserve useful stepping stones and return the next question

For a stepping-stone claim, name the option or region it could open, the enabling transition and the evidence that supports that connection. Distinguish a candidate stepping stone from one whose retention is already justified under an applicable policy. A data-access inquiry can be a candidate stepping stone toward representative evaluation; it does not itself demonstrate capability or authorize use of the data.

If a generation archive is useful, use [C.18](../../../_current-pattern-hosts/C.18-Open-Ended-Search-Archive-and-Front-Stewardship.md) with this named generator, its operators, descriptors, source/lineage and retention basis. A retained archive can preserve exploration value beyond the current front. Front membership needs its own comparator and admissibility; neither archive nor front is a recommendation or permission.

Claim a changed possibility space only when it matters and the earlier and candidate generation conditions are recoverable. A newly visited region inside the same admissible space is not an expansion. If a new access relation, operator or building block makes a formerly unavailable region reachable, state that exact change and its evidence. C.18 and the direct causal owner govern any stronger claim; this Method does not infer it from novelty.

When choosing which opportunity or question to consider next, declare the receiving policy: relevant value, burden, delay, protected conditions and uncertainty. A partial comparison can be enough. An actual C.19 pool policy is used only when that pool and policy exist; there is no default explore/exploit setting.

Return the next discriminating question, not a generic call for more research. State what each plausible answer would retain, narrow, reject or open. A proposed probe needs its own feasibility, exposure, authority and execution results before it becomes a recommended or performed probe. If those are absent, end with the exact request.

<a id="psd-opportunity-what-the-opportunity-account-contains"></a>
## What the opportunity account contains

Use a short account when it carries the needed distinctions. These are content positions, not a new universal record kind or a requirement to fill every field.

| Position | Inspectable content |
| --- | --- |
| Receiving frame | Holder or bounded candidate holder, later Work, receiver/use, horizon and the reason the question matters. |
| Problem and proposed promise | Worthwhile problem or explicitly unconfirmed problem hypothesis; proposed contribution and acceptance expectations; any existing promise kept distinct. |
| Search and difference | Sources and search operations used, materially different directions, relevant unsearched areas and why each retained direction is not just a renamed alternative. |
| Supports and dependencies | Necessary capability, access, support, resources, authority and other premises, their supplying owners and qualification state. |
| Reachability | Supported transitions and joint conditions; unknown or ruled-out transitions; the strongest warranted conditional or positive claim. |
| Uncertainty and protection | What may reverse the opportunity, what is protected and which stronger conclusions remain unsupported. |
| Stepping stone or retention | Only when relevant: the later option/region, enabling transition, lineage and actual retention or comparison policy. |
| Next question and return | Exact discriminating question; what its answers would change; the smallest request, reconsideration trigger or separate next use. |

The account may return a qualified candidate, a conditional candidate with a missing premise, a rejected direction with its reason, or an unresolved frame. It can stop without a recommendation. A source bibliography, score or diagram alone is none of these results.

<a id="psd-opportunity-worked-case-a-new-model-without-a-settled-problem"></a>
## Worked case: a new model without a settled problem

This is a constructed example of the Method, not a report about an actual model, organization or performed Work. Its source packet stipulates the bounded facts described below; absent facts remain absent.

An engineering-services unit hears that a new model can process long technical records. No accepted development problem or target result has been selected. The inquiry concerns useful contributions to engineering handoffs within ninety days, under confidential-data, independent-acceptance and continuing-service conditions. Buying or deploying the model is not the inquiry's objective.

The inquiry searches in three directions. From the technology, it explores record retrieval and qualification support rather than assuming autonomous decision-making. From uses, it considers evidence acceptance and shift handoff. From characteristics, it considers traceability of limits and reduced recovery burden; a manual index and a clearer handoff structure remain serious non-model possibilities.

The case's receiving-use statements identify two different worthwhile concerns. An acceptance engineer needs to recover which claims an evidence package actually supports. Shift staff need a usable account of unresolved exceptions and who can take the next authorized action. These statements establish why the possible contributions matter in the example; they do not establish that the model can supply them.

| Account position | Opportunity A: recover the acceptance premise | Opportunity B: support shift Work |
| --- | --- | --- |
| Proposed contribution | Help the receiver identify supported claims, missing premises and qualification limits in a bounded incoming evidence package. | Help shift staff recover unresolved exceptions, relevant conditions and the next permitted handoff without losing continuing-service responsibilities. |
| Niche and proposed promise | Qualification support for an acceptance engineer; a proposed inspectable claim-to-premise account, not automatic approval. | Handoff support for the named shift situation; a proposed recoverable exception account, not autonomous dispatch or a guarantee of recovery. |
| Material direction/support | Compare an analyst using a manual index with an analyst using bounded model-assisted retrieval over the same permitted source set. Independent acceptance remains external. | Compare a clearer human handoff arrangement with bounded model-assisted summarization plus a capable receiving holder, review support and fallback. |
| Protected conditions | Confidentiality, source traceability, independent acceptance and tolerable checking burden. | Service continuity, understandable exceptions, sufficient holder support and a usable fallback within shift attention limits. |
| Presently missing premise | The data owner has not qualified access to representative records for this purpose, including what may be processed by the proposed tool. | No adequate result establishes the receiving holder's capability and support under representative shift conditions. |
| Reachability now | Conditional only. No representative model-assisted evaluation or provision claim follows until the permitted source/access basis and other necessary transitions are qualified. | Conditional only. A model demonstration or a classroom success cannot establish capability, support or transfer into this shift configuration. |
| First useful question | Can the data owner supply a permitted, representative source set and a purpose/tool-specific access disposition for a bounded qualification inquiry? | What capability, workload and support result would establish whether the receiving holder can use this exception account during representative shift Work? |

The two directions address different result premises. They are not forced into one OCE.8 comparison. If the unit later stabilizes Opportunity A's result, use and acceptance basis, OCE.8 can compare complete manual, provider or mixed obtaining arrangements for that same result. That later comparison cannot supply the earlier choice of useful problem.

The return is **two conditional opportunities with different missing premises**. It is not “adopt the new model.” The original trend-only lead is not retained as a third opportunity because it identifies no useful receiving result.

For the next inquiry, suppose the receiving policy favors a small information request that can close a major uncertainty without using protected records, spending the trial budget or burdening shift staff. Under that explicit policy, asking the data owner for a bounded access disposition is the useful next question. A possible later access probe is identified as a **candidate stepping stone** toward representative qualification work, not as an authorized probe or a proven development step.

An affirmative access disposition would open only the permitted evaluation possibility; it would not establish the model's usefulness, acceptance authority or the person's capability. A negative disposition would remove that processing route and reopen the manual or differently bounded contribution. An answer covering only public, non-representative samples would support only a narrow demonstration, not the original representative-use claim.

Both opportunities might later compete for the same review capacity. Their individual plausibility does not establish that they can be pursued together. The joint time/support question remains with its qualified owner before any combined reachability or plan claim.

A small archive is optional. If the unit retains these candidates for later inquiry, its record names this Method and the actual search operations, the two candidate accounts and their source lineage, the missing premises, and the retention reason: preserving distinct useful questions until their dependencies can be resolved. It claims no non-dominated front, expanded possibility space, performed trial or effectiveness.

<a id="psd-opportunity-a-person-exploring-future-engineering-work"></a>
## A person exploring future engineering Work

This is another prospective, constructed use. An engineer wants to explore a useful next contribution within four months without asking an external adviser for a recommendation. The holder is the person. The inquiry's source packet distinguishes two prospective Work families: technical evidence review and coordination of cross-discipline interface questions. No future assignment, promotion or learning effect is assumed.

The person searches neighboring applications of their technical experience, different characteristics of contribution and possible supports. Evidence review could emphasize identifying mismatches between claims and tests; interface coordination could emphasize recovering incompatible assumptions between specialists. The first is not renamed as the second merely because both involve reading documents.

A qualified demand statement in the case explains why each contribution could matter. For the evidence-review direction, access to a permitted example set is available, but the person's capability and the transfer from supported practice to representative Work remain unknown. For the coordination direction, access to the relevant participants and competent feedback support are not established. A job title and a course listing supply neither missing premise.

The first account retains two conditional opportunities. It names the particular evidence-review or coordination contribution, its prospective use, the four-month horizon, the relevant support and uncertainty, and the next question. For evidence review, that question is what bounded representative assessment can distinguish an absent capability from difficulty caused by the current support configuration. For coordination, the first question is whether an appropriate practice/feedback opportunity can actually be made available.

Current career information about these directions is qualified for accuracy, context and currency, following the human-only contribution of [NCDG 2024, CD2/CD3](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page). HCD and target-domain results still determine capability, intervention and transfer claims. The framework of career information does not make a course effective.

The person may stop here. There is no final advice episteme, no invented adviser and no compulsory institutional conflict. If a separate adviser is later engaged, the [profile's service and recipient conditions](#psd-advising-bound-the-advising-engagement) open then. If the person instead already has adequate alternatives and is ready to choose, direct domain or C.11 guidance is enough.

<a id="psd-opportunity-countercases-and-honest-lowering"></a>
## Countercases and honest lowering

A supplier proposes “AI transformation” to a small unit whose current receiving result is already adequate and whose users identify no worthwhile unmet contribution at the proposed scale. Novelty alone does not repair that missing problem. Reject the direction for this inquiry or change the question; an archive can retain a technical idea for another stated use without treating it as a present development opportunity.

A qualified dependency result may also defeat an otherwise worthwhile direction. If the only proposed processing route violates the protected data condition, reject that route for this use. If access has merely not been assessed, retain the conditional question. Forbidden, unknown and available are different results.

A course sequence described as “from beginner to leader” has no bounded reachability here until representative later Work, the actual holder, required transitions, support and transfer evidence are recoverable. Likewise, evidence that one AI version improved on one benchmark does not identify a reachable organization or human development path.

An opportunity is not a recommendation, and a recommendation is not a choice. An authorized commitment, WorkPlan, intervention, provider agreement or observed effect must be established separately even when the opportunity account is persuasive.

<a id="psd-opportunity-refresh-the-affected-opportunity"></a>
## Refresh the affected opportunity

Reconsider an opportunity when a relied-on problem, promise, source, holder configuration, dependency, protection, horizon or comparison policy changes. Map the change to the exact candidate claim and any retained stepping stone or downstream advice that used it. Preserve independent claims.

For example, suppose the data owner in the constructed model case later qualifies only a narrower source set. Retain the receiving need and the manual-index direction. Narrow the model-assisted candidate to the permitted set; remove the unsupported representative-use reachability claim and request the missing evidence if that broader use is still worth pursuing. No earlier actual Work is erased by this change of knowledge.

If the new source set also excludes the particular region that a candidate stepping stone was meant to open, revise or remove that retention rationale. Another retained candidate does not become invalid by association. If the proposed next question is no longer discriminating, choose a new one under the receiving policy.

A factual change in one application does not automatically change this reusable Method. Reopen the Method's claims when evidence or a stronger practice line shows that its search, problem/promise construction, dependency reasoning, reachability rule or stop omits a material action. The [source-responsibility account](DEVELOPMENT-DIRECTION-SOURCE-RESPONSIBILITY.md) names that bounded responsibility separately from application follow-up.

<a id="psd-opportunity-recognition-assurance-and-use-of-this-description"></a>
## Recognition, assurance and use of this description

Recognition asks whether the useful future contribution and its path are still being constructed. One concrete later-Work concern plus a material unknown is enough to enter. Recognition is not an assurance judgment that a proposed development will succeed.

Assurance asks whether each value and reachability claim follows from sources qualified for this holder and use, whether important alternatives and protected conditions survive, and whether missing transitions remain visible. A hypothesis can be useful without being a feasible intervention. Before consequential enactment, obtain the direct capability, access, safety, professional, resource, authority and evaluation results required by that use.

| Named use of this description | Claims provided here | What must come from elsewhere |
| --- | --- | --- |
| Prepare a bounded opportunity inquiry | Applicability, working distinctions, search/construction moves, inputs, stops and result content. | Actual performer, permissions, resources and any dated WorkPlan. |
| Conduct or explain opportunity construction | The reusable action, dependency qualification and honest return branches. | Actual Work, participant and source-use relations; observations and any produced-result claims. |
| Inspect a candidate opportunity | Problem/promise distinction, supports, reachability reasoning, uncertainty, next question and refresh. | The truth and adequacy of the exact specialist premises and any stronger empirical claim. |
| Continue into advice or choice | An inspectable candidate basis or gap. | The profile's distinct-performer engagement and recommendation; direct choice authority and rule. |

<a id="psd-opportunity-source-informed-design-and-its-limits"></a>
## Source-informed design and its limits

The working question is how to construct a useful possibility before the target result and its obtaining arrangement are settled. A short menu of available technologies is efficient when an adequate result premise already exists; it fails this use when nobody has established why the proposed contribution matters. This Method retains the useful menu as search input and adds problem/promise construction, dependencies and a bounded first return.

[Phillips's 2025 practitioner account of decision analysis](https://pubsonline.informs.org/doi/full/10.1287/deca.2025.0356) treats models as purpose-dependent support for exploring possible futures, using only the ingredients the situation needs. Its sections on requisite models, decision conferences and decision-analysis technology inform the non-compulsory inquiry and the separation between analytical exploration and the accountable person's decision. This is a contemporary practitioner synthesis, not empirical validation of this cross-holder Method.

Keeney's older generation anchor informs explicit value questions; the human career framework informs that branch's alternatives and information qualification. C.18 governs any archive/front and possibility-space claim. These contributions are not interchangeable and do not, separately or together, prove practical reachability for an actual holder.

The substantive addition here is the complete prospective construction: from neighboring-use search through a worthwhile problem and proposed contribution to support dependencies, bounded reachability and a discriminating return. An archive-only approach preserves candidates but still needs a generator and domain facts. A same-result arrangement Method is powerful after its result premise is stable; it cannot substitute for this earlier question. Conversely, once the opportunity question is settled, this Method should stop and let the exact next owner work.

What changes in practice is concrete: “we should develop in this promising area” becomes a candidate contribution whose value, dependencies and next question can be inspected. The account can preserve a worthwhile possibility while refusing an unsupported reachability or advice claim.


# Cross-pattern applications

These constructed applications show how several pattern results can serve one working question. Their people, organizations, dates, data and supplied results are illustrative premises, not reports about actual clients or proof of effectiveness. A real use must establish its own facts, authority and evidence. The slices may overlap or reopen one another; their reading order is not a project lifecycle.

## APP-PSD-01 — A flood-pump calculation is not the whole investment answer

### The question and the people who need the answer

In a constructed 2027 case, a municipal resilience office asks a separate inquiry team to help the East-District Infrastructure Committee before the next flood season. The committee, called the board below, owns the later funding decision. The inquiry team may arrange the agreed investigation and return advice; it does not acquire investment or deployment authority.

The broad difficulty could lead to pump renewal, distributed storage, changed demand management or acceptance of a bounded risk. The current pre-season inquiry concentrates on the district pumping arrangement, including permanent and mobile capacity, maintenance, staffing and safe access. That smaller boundary does not reject storage or demand measures, settle relocation rights or declare long-term watershed effects irrelevant.

Using [PSD.1](#psd-1), the team first returns:

> Prepare a pre-season recommendation about the district pumping arrangement for the board's funding consideration. Make affected service concerns, operating conditions, protected limits and material dissent visible. Return a narrower comparison or exact missing premise when the basis cannot support the whole investment question; the board retains the choice.

That is already a useful result. A missing recipient, horizon or authority boundary would stop a stronger engagement claim. Here those conditions are supplied by the example, while the problem formulation remains contested.

### Preserve the differences that can change an intervention

Operations and finance are readily available. Residents, emergency responders, maintenance contractors, downstream ecology staff and mobility-constrained people may experience different consequences. [PSD.2](#psd-2) distinguishes supported consequence paths from possible ones and from unknowns. One residents' association is not presumed to speak for every resident. An evening meeting that some people cannot attend is a participation limit, not evidence that they have no concern.

The resulting concerns support four different formulations through [PSD.3](#psd-3):

| Formulation | What changes in the inquiry |
| --- | --- |
| Capacity shortage | Examine inflow, available pumping capacity and reliability; added capacity becomes a serious direction. |
| Unequal protection | Examine where exposure and access burdens fall, including reachable assistance; an aggregate hydraulic result is insufficient. |
| Maintenance fragility | Examine spares, staffing, contracting and coordination; a maintenance or staged direction may address a different cause from pump count. |
| Unsafe deployment | Examine placement, traffic, worker and downstream conditions; a restraint or differently bounded direction may be necessary. |

The team does not vote for the one “real problem.” [PSD.4](#psd-4) keeps the next flood season, material downstream paths and deployment conditions inside the present inquiry. Long-term redesign and permanent relocation remain outside its present investment return, with their decision-bearing consequences visible. Evidence that no feasible pumping branch serves mobility-constrained residents, or that flood burden transfers beyond the assumed area, would reopen the boundary.

### Join inquiry and analysis without making one speak for the other

A capacity calculation, an access/deployment scenario and an attributed concern map answer different questions. Through [PSD.5](#psd-5), the team finds that nominal capacity is not yet the deciding uncertainty. The mobile branch has no qualified arrival-time claim when the main road is unavailable; the concern map also distinguishes property protection from reachable assistance.

[PSD.6](#psd-6) compares capacity analysis alone, a broad open-ended investigation and a bounded combination of attributed inquiry with conditional technical analysis. The bounded combination fits the pre-season return only while attribution can be checked and competent sources can qualify the technical premises. Its join requires the same intervention, service meaning and horizon. Counting how often a concern was mentioned does not produce a numerical value weight.

Through [PSD.7](#psd-7), a proposed sentence changes from “the pumps can protect the district” to a qualified nominal-capacity claim. The separately consulted group asks how assistance remains reachable when roads fail. That correction neither proves a pump inadequate nor disappears because the model does not represent it. The return preserves the two attributed service concerns and the unqualified access premise.

The actual inquiry and analysis can overlap. Suppose the proposed timetable freezes the model before a material service correction can reach the analyst. [PSD.16](#psd-16) compares keeping that freeze, stopping every calculation, and allowing bounded analysis while a supported facilitator maintains the correction channel. Under the case's supplied remit and available analyst/facilitator support, the third arrangement preserves independent calculations and permits the affected claim to be revised before it closes. If a correction or its consequence is still unresolved at the deadline, the board receives that limitation. No meeting order substitutes for the missing result.

### Use a numerical slice at its actual scope

[PSD.8](#psd-8) keeps no-new-purchase baseline `N`, fixed pumping `F`, mobile pumping `M` and staged combination `S` visible in the present pumping inquiry. Storage and demand-management leads have not been disposed of by this narrower set. The supplied numerical slice covers only `F` and `M`, on illustrative pumping-service-loss and incremental-cost scales:

| Direction | Loss with normal access | Loss with road loss | Incremental cost |
| --- | ---: | ---: | ---: |
| Fixed pumping, F | 2 | 3 | 8 |
| Mobile pumping, M | 1 | 9 | 5 |

These are model values, not monetary prices, measured municipal performance or a complete public-consequence account. Baseline, staged, assistance, protection and other material branches remain outside this calculation.

[PSD.9](#psd-9) keeps the declared value scheme separate from a participant's concern. [PSD.10](#psd-10) distinguishes an assumed road-loss probability from an established one. [PSD.11](#psd-11) can compare the stated consequences, and [PSD.12](#psd-12) exposes a possible reversal rather than hiding it.

In this deliberately stated weighted-loss model, let `p` be the assumed road-loss probability and `λ` the declared cost weight. The two totals are `2 + p + 8λ` for F and `1 + 8p + 5λ` for M. F is lower only when `7p > 1 + 3λ`. With `λ = 0.5`, `p = 0.2` favors M; `p = 0.6` favors F. Neither probability nor the weight has been established for the board's decision.

The result therefore identifies a decision-bearing uncertainty and a conditional comparison. It does not prove that a probability obtains, that assistance is reachable, that a protected condition can be traded away, or that F or M should be bought. More decimal places would not close those gaps.

### Return the useful comparison and the whole-question blocker together

Using [PSD.13](#psd-13), the team returns:

> Retain fixed and mobile pumping for the stated service-loss/cost comparison. Their order reverses under the declared assumptions. A whole-investment recommendation remains blocked by the unqualified access basis, unresolved assistance and protection consequences, and unclosed baseline, staged and other material branches. Obtain the smallest results that can resolve those distinctions. Keep the separately attributed service concern in the board's return; do not replace it with the calculation.

This is a completed bounded recommendation return, not a refusal to do useful work. The team asks the relevant operations/access and consequence owners for exact results for this configuration and flood-period window. The full direct patterns retain the method for qualifying those results. A qualified source closing access may leave the value disagreement untouched.

The board's decision to commission further inquiry would be another result. Funding an access study is not funding a pump, and receiving the recommendation is neither consent nor execution.

### A changed premise changes the right claim

The useful follow-up question is what evidence can reach the board before renewed consideration. [PSD.14](#psd-14) compares an end-of-season review, continuous pump telemetry and a bounded pre-decision evidence arrangement. Telemetry alone cannot settle deployment permission, reachable assistance or the staged alternative. The bounded arrangement is selected in this example only after supplier availability, access, interpretation time and the receiving date are supplied.

In a separate hypothetical continuation, the board authorizes an access study, not a pump purchase. A qualified return establishes that the mobile deployment arrangement assumed in the earlier calculation is unavailable during the required flood-period window. The analyst does not insert a guessed new probability.

The fixed-pump performance claim remains usable for its original conditions. The earlier F/M comparison remains an account of its earlier basis, but cannot support the present investment use. The exact mobile-deployment and consequence premises reopen; assistance, staged and other unclosed branches do not vanish. If a newly identified affected group changes the service meaning, the boundary question reopens as well.

The follow-up has returned an actionable distinction without making the board's choice. Missed observation would instead leave a scoped gap; silence would not mean the premise remained valid.

### Continue the professional practice only when that is the question

The same episode can expose a different need: another inquiry team may copy a recommendation's format while losing its limits. That is not another pumping calculation. [PSD.15](#psd-15) concerns a justified repertoire change, and [PSD.17](#psd-17) concerns continuation across practitioners.

The fuller constructed PSD.17 case supplies separate East and West teams, their relevant service assignments, the inquiry and teaching Methods, and distinct March–April occurrences. West's receipt of a permitted packet initially produces an overstrong investment recommendation. Under the case's teaching remit and available support, a guided qualification exercise is selected for that receiving group while the compact route remains for experienced practitioners.

In the exercise, West distinguishes the usable F/M calculation from the unclosed staged and assistance questions. One later independently observed West inquiry retains a corrected concern and the comparison's limits. This supports that bounded receiving use, not profession-wide adoption, long-term retention, a causal teaching effect or an improved flood outcome. The separate late-correction Method proposal remains a proposal; the teaching case does not deploy it.

These practice questions open only because the particular interpretation or working arrangement matters. They are not mandatory activities after every recommendation. The immediate practical gain remains simple: the board receives the useful calculation without losing the people, alternatives and conditions that prevent it from being the whole answer.

## APP-PSD-02 — Development-direction advice with unlike holder premises

### Two useful entries, not one compulsory advising process

The [development-direction profile](#psd-advising-development-direction-advising) connects qualified opportunity, holder, comparison and recommendation results. It is useful when a distinct recommending performer must help a named recipient. The developing holder, paying sponsor, recipient and chooser can differ. Their actual relationship determines what may be shared, relied on or decided.

There is also an earlier independent entry. A person or team can use [Construct a Bounded Development Opportunity](#psd-opportunity-construct-a-bounded-development-opportunity) to explore useful future work without asking anyone for a recommendation. Its account can end at a conditional opportunity and a discriminating question. Calling that result “advice” would introduce a different performer/recipient relation rather than merely change its title.

When advice is the question, [PSD.1](#psd-1) recovers the engagement and authority boundary. Applicable competence, conflict, confidentiality, informed participation and referral conditions remain professional questions, not a generic permission box. AI used by an adviser also differs from AI being developed. An available tool or fluent generated memo gives neither the service relationship nor its content a warrant.

### Begin before the target contribution is settled

Suppose an engineering-services unit hears that a new model can handle long records. “Adopt the model” is a search lead, not an accepted problem. Within a ninety-day inquiry, the unit explores neighboring uses, technologies and characteristics under confidentiality, independent-acceptance and service-continuity conditions.

The opportunity Method yields two different accounts:

| Candidate opportunity | Worthwhile receiving question | Dependency and first return |
| --- | --- | --- |
| Help an acceptance engineer recover which claims an evidence package supports. | Could a recoverable claim-to-premise account improve the qualification task without implying automatic acceptance? | Representative, permitted record access is not yet qualified. Retain manual indexing and bounded model-assisted retrieval as conditional directions; ask the data owner for the exact access disposition. |
| Help shift staff recover unresolved exceptions and the next permitted handoff. | Could an understandable exception account improve this receiving situation without autonomous dispatch or loss of fallback? | Representative holder capability, workload and review support are not established. Retain a clearer human handoff and a bounded model-assisted direction; request the relevant capability/support result. |

The opportunity return is not a ranking or an adoption recommendation. A positive access disposition would open only the permitted inquiry, not prove the model useful. A refusal would close that processing route, while a public-only sample would support only a narrow demonstration. A possible access probe is a candidate stepping stone toward representative evaluation, not permission to perform it.

The two receiving results differ. A same-result arrangement comparison becomes relevant only after one result, use and acceptance premise is stable enough. Forcing both accounts into one such comparison would hide the still-open choice of useful problem. A generation archive is optional and supplies no value, reachability or authority by itself.

The unit may stop here. If a distinct adviser is later asked which direction to recommend, these accounts enter [PSD.8](#psd-8) at their actual conditional strength.

### A person exploring four months of engineering development

An engineer considers technical evidence review and cross-discipline interface coordination. They can first conduct their own opportunity inquiry. The relevant future work is a contribution they might make, not a job title or course name.

In the example, demand statements explain why both contributions could matter. A permitted evidence set is accessible for the review direction, but capability and transfer into representative work remain unknown. The coordination direction lacks a confirmed opportunity to work with the relevant participants and obtain competent feedback. Neither course attendance nor another person's successful transition fills those gaps.

If the person asks a separate adviser for a recommendation, the return is:

> Retain the two directions as conditional possibilities. For evidence review, obtain the bounded representative assessment that can distinguish a capability limit from an access or support limit. For coordination, establish whether the relevant practice and feedback opportunity is actually available. Do not prescribe a course or claim a four-month transition from the present evidence.

The person's own choice remains separate from an employer's assignment decision. Human demand, assessment, intervention and transfer results retain their direct owners. Career information can help compare opportunities but does not establish a learning effect. If practice time later changes, reconsider the dependent intervention or reachability claim; unrelated organization or AI evidence remains as it was.

### An organization needs a ninety-day reliability recommendation

A committee asks a separate advisory team which direction to consider for a service organization: internal development, an external provider, or a mixed human–AI arrangement. The committee is recipient and, under the example's supplied mandate, later choice owner. Reliability has priority over throughput for this horizon. Critical-service continuity, security and a bounded reversible-probe budget are protected.

An operating account identifies the recovery contribution; a position/interface account explains the current arrangement; a priority statement identifies the receiving value. None compares all three ways of obtaining the required result. The adviser uses the [single A.15.9 import in the profile](#psd-advising-use-the-direct-result-acquisition-method) to look for an adequate existing result, then request only what remains missing.

The first complete return is a whole-set blocker and exact request:

> Obtain the whole-arrangement comparison for this recovery result, ninety-day horizon, security boundary and continuity condition, including the named provider configuration. The operating, interface and priority accounts remain useful, but do not support ranking the three directions.

The availability of OCE.8 guidance would not change that return. A Method for obtaining a comparison is not the client's comparison, and the supplier chooses how to produce and qualify its own result.

Now take a separate hypothetical continuation. Adequate whole-arrangement and security results cover the three named directions. They exclude the specified provider because it cannot preserve the security boundary. Internal development remains feasible; a bounded mixed-arrangement probe could resolve whether permitted assistance reduces the recovery queue without excessive verification burden or weakened fallback.

The supplied probe result covers the actual question, distinguishing observations, feasibility, exposure, available resources and stop conditions. Compared with immediate commitment, it supports obtaining that information at bounded cost while retaining internal development. A disclosed material provider interest has also been treated under the agreed service conditions. These are additional premises, not improvements in rhetoric.

Using [PSD.9](#psd-9) through [PSD.12](#psd-12) only where their comparison results are needed, the adviser makes the advantage, serious rival, uncertainty and protected conditions recoverable. Through [PSD.13](#psd-13), the return is:

> Consider the bounded mixed-arrangement probe first and retain internal development. The supplied arrangement, probe and security results support this information-gaining recommendation for the named reliability use. Throughput effect remains uncertain. Preserve continuity, security and the budget; reconsider when representative recovery evidence or a relied-on premise changes.

This does not close three directions from an internal/mixed-only comparison: the separate security result explicitly disposes of this provider configuration. Another provider or materially different probe would need its own basis. Delivery, committee consideration, a later authorized probe plan, actual work and observed effect remain distinct.

### An AI configuration changes while independent advice survives

A team considers model modification, a different scaffold/tool configuration and a changed human–AI allocation. The exact changed object matters: a human training result establishes none of the AI evaluation or deployment-safety premises, and an organization-allocation result does not by itself evaluate a model.

Suppose the committee in the reliability example later authorizes only a bounded probe for configuration A under stated continuity and oversight conditions. An appropriate follow-up arrangement exists: the configuration owner can report material changes, specialist suppliers can qualify them, the adviser has interpretation time, and the committee can receive the revised use consequence.

A notice now identifies configuration B. Observation from B arrives, but the relied-on evaluation still concerns A. [PSD.14](#psd-14) produces a split return:

| Dependent use | What follows now |
| --- | --- |
| Internal-development claim independent of A's evaluation and the changed allocation | Retain it within its original service and horizon. |
| Earlier recommendation concerning A | Preserve it as the earlier conditional advice; do not relabel it as evidence for B. |
| Advice to extend the probe or deploy B | Block that stronger return pending the exact B evaluation, safety/security and allocation premises that matter. |
| Observation and operational response | Use the actual competent owner and applicable continuity or safety rule; a notice alone does not choose fallback, stop service or revoke permission. |

If a generator, candidate archive or open-ended search is itself changing, its actual operators, descriptors, retained candidates and governing policy need their direct account. Calling the holder “OEE” or displaying a front does not supply the missing B result, a worthwhile opportunity or deployment authority.

The observation arrangement is not automatic monitoring created by this text. If an expected result is missed, report the resulting reliance gap. If the decision has ended and no continuing service or protection duty remains, close the follow-up rather than inventing another review cycle.

### A population without a recipient, and a separate research question

A non-cultural population or lineage has no population-local recipient or chooser in this application. Abstain from attributing a development recommendation to it. Variation, reproduction, selection, persistence and loss belong to the evolutionary account; they are not renamed as the population's choice.

A research team may separately ask which experimental intervention to consider. That is a recipient-owned inquiry only when its scientific question, exact subject, authority, safety and other applicable conditions are established. The population countercase supplies none of those premises. The return may therefore be an exact scientific or authorization question, not a recommended intervention.

### What remains the same across the branches

The useful common result is a qualified opportunity, comparison or recommendation with an exact next use. What differs is the premise required to support it. Human transfer, organizational obtaining arrangements, AI evaluation and scientific intervention are not one score or one development mechanism.

A supported direction should not be withheld merely because another branch remains uncertain. Equally, fluency, a method publication, a source bibliography or a favorable score cannot promote an unresolved branch. Follow the [profile](#psd-advising-development-direction-advising) for the full engagement and recommendation contract, the [opportunity Method](#psd-opportunity-construct-a-bounded-development-opportunity) for the earlier construction, and the direct patterns for their own results. The [source-responsibility account](DEVELOPMENT-DIRECTION-SOURCE-RESPONSIBILITY.md) keeps that profile's bounded source use separate from application-specific follow-up.

# Framework boundary, sources and refresh

## What this framework covers

Problem Structuring and Decision Support serves practitioners and assisting agents who help someone frame a question, conduct an inquiry, compare alternatives and receive a warranted result. The useful return may be an engagement question, several formulations, a model-use account, a comparison, a recommendation or an exact blocker. The recipient's later decision remains separately governed.

The framework also addresses the Methods and arrangements by which that professional help is developed, coordinated and continued. It does not promise that one technique, score, workshop or published description settles an actual client's problem. Its guidance is source-informed; the combined teaching cases are constructed demonstrations, not evidence that the whole pattern language has been implemented or is empirically superior.

| Recurring difficulty and characteristic failure | Useful result family and direct entry | Material connection |
| --- | --- | --- |
| The question, participants or scope are unclear; a sponsor's first story is treated as everyone's problem. | [PSD.1](#psd-1)–[PSD.4](#psd-4): a bounded engagement, participation and concern account, plural formulations and a revisable boundary. | These results qualify what later inquiry or comparison must answer. They are reused when adequate, not repeated before every calculation. |
| Models, Methods or discussions fail to make one another's contributions usable; an agenda, diagram or agreement stands in for warranted inquiry. | [PSD.5](#psd-5)–[PSD.7](#psd-7): complementary model claims, a usable inquiry Method and shared or contested meanings. | A join must preserve the question and limits of the supplying contribution. Material corrections reach the analysis or return they change. |
| Alternatives or their preferences are asserted before consequences, values and uncertainty justify them. | [PSD.8](#psd-8)–[PSD.12](#psd-12): a live candidate set, value account, uncertainty representation, consequence comparison and bounded robustness result. | A partial comparison remains partial. A missing candidate, protected condition or reversal can reopen the exact contributing question. |
| Advice, later action and professional change are confused; delivery is treated as choice, follow-up as automatic action, or publication as cultural uptake. | [PSD.13](#psd-13)–[PSD.17](#psd-17): a qualified recommendation, follow-up arrangement, justified repertoire change, reconciliation of simultaneous inquiry and bounded cultural-continuation decision. | Each use opens only when its own question is live. A recommendation does not require changing the professional repertoire or cultural arrangements. |

The four Parts arrange these recurring difficulties for reading. They do not assert a Method sequence, a hierarchy of professional importance or a partition of every real situation. Pattern numbers are stable addresses in this framework. An actual inquiry may use one pattern, return to an earlier result or need several contributions at once.

The [development-direction profile](#psd-advising-development-direction-advising) is a non-pattern use account connecting those contributions. [Construct a Bounded Development Opportunity](#psd-opportunity-construct-a-bounded-development-opportunity) describes a separately identified reusable Method and can be entered without an adviser. Both are reader support within this framework; neither adds a pattern or turns every cross-pattern use into one composite Method. The applications show their connections without replacing their full guidance.

## What remains with another practice

Use a direct source when it owns the whole current question. If a chooser already has an adequate option set and needs only their own decision, use [FPF C.11](../../../_current-pattern-hosts/C.11-Decision-Theory-Decsn-CAL.md) or the applicable domain decision rule. If an engagement needs just one missing specialist result, [FPF A.15.9](../../../_current-pattern-hosts/A.15.9-Request-and-Use-a-Bounded-Result-from-Another-Practice.md) gives the bounded inspect, reuse or request entry.

| Needed contribution | What PSD can do | What it does not supply |
| --- | --- | --- |
| Human capability demand, diagnosis, intervention or transfer | State which person's later Work and which advice premise need a qualified result; use the direct human-practice entry named in the development profile. | A diagnosis, effective curriculum, learning effect, occupational opportunity or demonstrated transfer from a course title or general guidance. |
| Organization, operating or provider arrangement | Specify the result, configuration, use, horizon and acceptance question to compare; retain independent alternatives when one premise fails. | This client's whole-arrangement comparison, implementation capacity or authority from a position description, operating account or published Method. |
| AI/model or other technical evaluation and safety | Keep configuration and use exact, request the decision-bearing result and reconsider only dependent advice after change. | Evidence for configuration B from A, deployment permission from an evaluation, or practical reachability from novelty or an archive label. |
| Physical, scientific, financial, legal, ethical, safety or governance facts and rules | Expose the premise, its owner, qualification window and effect on the return. | A local threshold, mechanism, permission, professional duty or protected condition by analogy with another field or holder. |
| An evolutionary population or lineage | Recognize the absence of a population-local recipient and choice owner in the represented case. | A development recommendation to that population. A researcher selecting an intervention has a separate question, scientific basis and authority. |

These are boundaries of this guidance, not declarations that the neighboring practices or all their results are unavailable. A published Method may be available while the application-specific result is still missing. Ask for the smallest result that can change the answer; do not wait for every neighboring framework to be packaged, and do not fill a gap with a same-named result from another subject.

A real application must qualify the relied-on content for its exact subject, configuration, receiving use and horizon. [A.10](../../../_current-pattern-hosts/A.10-Evidence-Graph-Referring.md) governs that reliance, while the direct subject practice governs the claim itself. Discovery, availability, evidence, applicability and authority are different questions.

## Where the source arguments live

Each pattern's SoTA-Echoing section owns its substantive comparison: the working question, selected move, serious rival, trade-off, source limits and observation that would reopen it. Use that argument before relying on a citation. The following map is a return aid, not a second source doctrine, a field census or independent confirmation of the sources it condenses.

| Source-informed contribution | Source line used and substantive limit | Return when the answer changes |
| --- | --- | --- |
| Engagement, participation and revisable framing | Smith and Shaw's 2019 PSM characterization and Kogetsidis's 2025 application review inform the continuing diverse PSM branch. Kelly and Gero 2022, Litster and colleagues 2024, and Nickel and colleagues 2024 inform non-equivalent frames and contextual revision. The bounded reviews and studies supply no universal ontology, representation guarantee or superior protocol. | [PSD.1](#psd-1), [PSD.2](#psd-2), [PSD.3](#psd-3) and [PSD.4](#psd-4): change the affected receiving-use, participation, formulation or boundary claim. |
| Model, Method and facilitation joins | Marttunen, Lienert and Belton 2017 provide the older critical PSM–MCDA combination anchor; Lami and Tavella 2019 supply an exploratory workshop contrast. Schwarzburg and colleagues 2024 distinguish confidence-related factors from validation. Franco and Greiffenhagen 2018 and Zimmermann and Curran 2023 contribute situated interaction evidence, not guaranteed consensus or general transfer. | [PSD.5](#psd-5), [PSD.6](#psd-6) and [PSD.7](#psd-7): requalify the particular claim, Method contribution, join or attributed meaning. |
| Alternative construction, values and comparison | Borgonovo and colleagues' 2026 decision-analysis synthesis and Greco, Słowiński and Wallenius's 2025 MCDA synthesis inform selective analytical contributions and preference-model fit. Keeney 2012 is a historical generation ingredient; Marttunen and colleagues 2019 inform disciplined objective simplification. These sources do not supply the engagement's values or warrant one total score. | [PSD.8](#psd-8), [PSD.9](#psd-9) and [PSD.11](#psd-11): revisit material alternatives, lost value distinctions or the actual comparison relation. |
| Uncertainty, adaptation and robustness | Lempert and colleagues 2024 connect low-confidence knowledge to decision-relevant inquiry. The 2019 DAPP account contributes pathway timing and failure conditions; the 2026 decision-analysis synthesis informs sensitivity and information acquisition. Scenario membership establishes no probability, and a formal method supplies no local threshold or authority. | [PSD.10](#psd-10) and [PSD.12](#psd-12): narrow the stated range, reopen a reversal or qualify a feasible information question. |
| Professional recommendation and development-direction use | PSD.13 uses NCDA 2024 within its profession and selected ICMCI v4.0 engagement clauses as a bounded older comparator. The profile's separate source account qualifies the used portions on 2 September 2026, including the ICMCI AI Code v1.0 of May 2026 for AI used by an adviser. That code is not AI-holder evaluation, and the older competence clauses are not represented as the complete latest standard. | [PSD.13](#psd-13) and the [profile source-responsibility account](DEVELOPMENT-DIRECTION-SOURCE-RESPONSIBILITY.md): revisit the exact applicable service or source condition. |
| Opportunity construction before a settled result | Phillips's 2025 practitioner synthesis informs selective future exploration; NCDG 2024 supplies a bounded human information/alternative contribution; historical value-focused generation is one ingredient. Their combination supports a prospective construction Method, not empirical proof that its opportunities are reachable or effective. | The [opportunity Method](#psd-opportunity-construct-a-bounded-development-opportunity) and its source-responsibility account: revise the changed search, dependency, reachability or next-question claim. |
| Follow-up under expected and unexpected change | Lynch and colleagues 2025 contribute domain-specific reconsideration triggers; Manley and colleagues 2026 contribute a perspective on targeted and broader observation. Their natural-resource settings do not set every client's monitoring mix, threshold or institutional response. | [PSD.14](#psd-14): reconsider the affected observation, interpretation, service obligation or recommendation use. |
| Professional Method development | PSM comparisons, Borgonovo and colleagues 2026 and Franco and colleagues' 2021 behavioural-OR synthesis inform contribution-specific repertoire and evidence questions. Kogetsidis's 2026 online review covers selected journals in 2010–2024; publication frequency is neither a practice census nor practical worth. | [PSD.15](#psd-15): change the specific offering, applicability or evidence claim, not the whole repertoire merely because a paper appeared. |
| Simultaneous inquiry | The older expert/facilitated contrast in Franco and Montibeller 2010, Franco and Nielsen's 2018 workshops, Franco and colleagues 2021 and Cunico and colleagues 2024 support bounded comparisons of interaction and challenge arrangements. They do not make one staffing or participation design universally best. | [PSD.16](#psd-16): requalify the actual interaction and local test; use C.32.MWA only when several structures need a joint synthesis. |
| Cultural continuation | Yearworth's 2024 chapter summaries inform a practice-facing account. Voltan and Kells 2026 remain a conceptual GenAI-assisted proposal requiring practical testing; Czaplicka, Baumann and Rahwan 2025 offer a simplified mediation model. Neither publication, generated output nor a modeled mechanism proves professional uptake or cultural effect. | [PSD.17](#psd-17): revise the exact population, receiving interpretation, mediation hypothesis or continuation claim. |

Publication years identify sources; they do not by themselves identify a qualification window or show that a claim is still reliable. Older anchors remain useful for the particular contribution named above, while later work can repair their limits. Currentness is bounded to the actual inspected claim and intended use. No table here guarantees continuous monitoring or validates a local case.

## Change only what the new basis changes

A user relying on this guidance should retain the source and condition behind each consequential premise. A maintainer taking responsibility for this framework should keep the changed claim, its direct source, affected pattern or support unit and revised limit recoverable. The [development-direction source-responsibility account](DEVELOPMENT-DIRECTION-SOURCE-RESPONSIBILITY.md) governs its two companion units; this map points to it instead of copying its qualification record.

When a source, configuration or receiving condition changes:

1. Identify the claim that used it and whether the new information concerns the same subject and use. A notice is not yet a replacement evaluation.
2. Choose the guidance for the changed premise and the result needed. With an unchanged source but changed actual conditions, use the direct subject guidance. For one already-known bounded source-reliance question, use [A.10](../../../_current-pattern-hosts/A.10-Evidence-Graph-Referring.md); for a materially changed source claim whose receiving uses still need discovery or closure across several uses, use [A.10.1](../../../_current-pattern-hosts/A.10.1-Revalidate-Affected-Uses-When-a-Relied-on-Source-Changes.md); for currentness or a scoped refresh-planning or reporting result, use [G.11](../../../_current-pattern-hosts/G.11-Telemetry-Driven-Refresh-and-Decay-Orchestrator.md) under its conditions. Ask the direct supplier for any missing subject result and keep independent supported content.
3. Return the strongest answer still supported: unchanged within scope, narrowed, blocked, returned to its contributor or replaced by later advice. Use PSD.14 when a decision-support follow-up question is live.
4. Revise the reusable pattern, Method or profile only when its own claim changes. A client-specific result, professional service duty or observed outcome retains its own owner and history.

For example, loss of a mobile pump's access premise reopens that branch, not independent fixed-option arithmetic. Loss of trained reviewers invalidates a staffing-dependent mixed probe, not an unrelated internal option or the tool evaluation within its own scope. A changed professional disclosure condition concerns the applicable service, even when the developing holder is not AI. An unsupported transfer from one learner or model configuration cannot be repaired by broadening the name of the original evidence.

Keep earlier source states recoverable when revising this guidance. An updated description does not rewrite past Work, earlier advice, prior choices or their evidence. Changes that alter a recurring problem, useful result, direct-owner boundary or whole-field promise need the corresponding content decision; changed links or presentation alone do not create a new practice or prove improvement.
