# Engineering DPF Suite

> Methods for difficult engineering decisions, explained as patterns you can use with your colleagues and AI assistants.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 3 September 2026
- **Status:** Eternal alpha: already used in project analyses and development programmes, and revised as the methods and their evidence improve.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

You may be choosing an architecture, trying to make a working method reproducible, reorganizing a team, or deciding what to develop next. The Suite helps you find a useful way to tackle that particular difficulty and produce an answer you can act on.

A **DPF**, or **Domain Principle Framework**, collects methods for a field as a language of patterns. Each pattern explains a recurring difficulty, a way to address it, the result to obtain, and the conditions that affect its use. The methods are connected: one can help you discover or supply what another needs.

[FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) supplies the common concepts used across fields. The DPFs bring in the field's methods, competing approaches, examples and source evidence. This combination lets a team discuss technical choices, ways of working and organizational consequences in a shared language.

## Start with the problem in front of you

Describe the situation in ordinary words. For example:

> “We can buy a controller, commission one, or build it ourselves. How do we compare the alternatives, including the work and cost that each leaves to us?”

Open [SYSE.24 - Choose How the Project Will Obtain a Needed Engineering Result](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse24---choose-how-the-project-will-obtain-a-needed-engineering-result). It helps you compare complete ways to obtain the result: equipment alone, integration work, operating support, capability, access and eventual replacement can all change the choice. Your first useful result may be a defensible comparison or a precise question to put to a supplier.

Use a pattern's **Problem frame** to check that it fits. Its **Solution** gives the working moves; the example shows how they fit a case, and the checklist helps inspect your result. Bring in another pattern when you need its answer. You can begin from a result your project already has.

You can read this way yourself, use a pattern in a working meeting, or ask an AI assistant to help apply it. There is no need to read all five frameworks before starting.

## Choose a DPF

These are the five complete DPF publications in this download. Their tables of contents provide the full pattern lists and searchable working questions.

| What you are trying to do | Open | A result it can help you obtain |
| --- | --- | --- |
| Bring about or change an engineered system, from its intended use to working integration and continued development. | [Systems Engineering](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — 41 patterns | A system boundary, architecture decision, comparison of ways to obtain a result, integration plan, or justified release decision. It also covers general Platform Engineering and a substantial software delivery and reliability profile. |
| Choose, explain, test or improve a way of working. | [Method Engineering](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — 19 patterns | An explicit method, a useful description of it, a support arrangement, or evidence about fit, transfer and practical value. |
| Change how an organization contributes, assigns work and enables people and other performers to act. | [Organization Change Engineering](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — 17 patterns | A compared organizational arrangement, clarified assignments and authority, a supported change, or a decision about its consequences. |
| Work out what the problem is, compare possible directions, or prepare a recommendation. | [Problem Structuring and Decision Support (PSD)](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md) — 17 patterns | Several useful problem formulations, decision alternatives, a comparison under uncertainty, or a recommendation with its grounds and limits. |
| Create, perform, teach or develop music and dance practices. | [Music and Dance Practice Engineering](MUSIC-AND-DANCE-PRACTICE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — 22 patterns | A performance or practice design, a useful observation, a transmission method, or a choice about the practice's next development. |

The word *engineering* includes physical equipment, factories, laboratories, buildings, robots and software, as well as the means needed to develop them. A platform can be a manufacturing or laboratory platform. The software profile addresses its particular delivery and reliability difficulties.

When your question crosses these fields, open the [Suite Reference](ENGINEERING-DPF-SUITE-REFERENCE.md). It provides a more detailed question index and worked cases.

## Looking for development recommendations?

Open PSD's [Development-direction advising profile](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-advising-development-direction-advising). It connects the methods used to advise a person, an organization or another developing system. The facts and development methods differ by subject; the profile helps you obtain the relevant inputs and turn them into advice.

If you have not yet formed useful opportunities, start with [Construct a Bounded Development Opportunity](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-opportunity-construct-a-bounded-development-opportunity). If the alternatives and comparison are already adequate, [PSD.13](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-13) may be enough to prepare the recommendation.

For example, “What should our engineering team learn or change over the next four months?” calls for evidence about the work it needs to perform, present limits, feasible alternatives and opportunity costs. A course is one possible response. The inquiry can also reveal a method, tooling or organizational change that would help more. The Reference explains [how to connect advice with those domain results](ENGINEERING-DPF-SUITE-REFERENCE.md#how-do-we-recommend-a-development-direction).

## Work with an AI assistant

Give the assistant access to FPF Core and the relevant DPF files. Tell it about the actual project, the decision you face, your constraints and the evidence available. Ask it to read the patterns it uses.

A useful starting request is:

> Help me work through this situation using FPF and the relevant Engineering DPFs: [describe the situation]. Identify the question we need to answer now, select the pattern that fits it, and help produce the next usable result. Explain the reasoning in ordinary engineering language, show the PatternIDs you used, and say which missing facts could change the answer.

Inspect the answer against the pattern and your project evidence. You and the other participants supply observations, specialist judgement and the authority to make real decisions. The assistant can help search, compare, draft and question the reasoning.

## What to read next

| You need... | Use... |
| --- | --- |
| A quick introduction and a first attempt with the Suite | This README. |
| A precise starting pattern, or a worked example involving several fields | [Engineering DPF Suite Reference](ENGINEERING-DPF-SUITE-REFERENCE.md). |
| The method itself, its example, checks and source discussion | The selected DPF's pattern body. Its Readme gives examples within that field. |
| An explanation of a shared FPF concept or general reasoning method | [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). |
| A programme of study, exercises and feedback to build your abilities | An instructional Guide or a separately designed development programme. The Reference is organized for lookup while you work. |

The README introduces the Suite. The Reference helps you find and combine methods. Full pattern bodies remain the place to inspect what a method asks you to do.

## Development previews

Operations Management and Human Capability Development also have partial working publications. They are separate previews and are not included in this five-DPF download.

The Operations preview covers OPS.1–OPS.11: operating work, admission, exceptional-case continuation, local priority or commitment revision, queue and buffer coordination, constraint treatment, capacity under variability, and coordination across operating structures. The Human Capability Development preview covers HCD.1, HCD.3, HCD.4 and HCD.11–HCD.14: demand from later work, diagnosis of a limiting target, a capability profile, performance assessment, unfamiliar transfer, retention and tool dependence, and evidence-led revision of a development arrangement. A citation marked *preview* identifies this narrower source; it does not point to a missing file in this download.

Until the needed preview or later publication is available to you, obtain the particular operating or development result from an appropriate specialist. For a complete learning programme, also obtain its design and the development methods to be used. To judge a person's performance, transfer or retention, apply the relevant methods and obtain observations of that person. Publication updates are announced through the [FPF repository](https://github.com/ailev/FPF).

## Sources, revisions and citation

The DPFs bring together useful research and practitioner approaches, including disagreements and known limits. Source discussions explain what an approach contributes and where its evidence stops. The methods continue to change as better answers become available.

For consequential decisions, keep the publication date and the evidence behind the result you used. Revisit the affected conclusion when the situation or a relied-on source changes.

To cite the collection:

```text
Levenchuk, Anatoly. Engineering DPF Suite.
3 September 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular method, cite its DPF, PatternID, title and the date shown in that publication.
