# Foundational Thinking DPF Suite

**Construct, justify and revise models, mathematical and physical accounts, algorithms and notation.** Use this Suite when familiar formulas or operations do not yet connect into the answer you need, or a changed question makes an earlier construction inadequate.

A theorem, physical explanation, algorithm, interpreted model or usable notation can itself be the result. These methods also help develop new ways of working. They do not cover all intellectual activity, all mathematics and physics, or the whole of computer science.

Framework and method links open readable text on fpf.tools; **Markdown** links open the repository source. GitHub previews can truncate large files. Check the [displayed source edition](https://fpf.tools/status) when the version matters.

## How this Suite is organized and why

**[Read the Foundational Thinking Architectural Reference](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md).** It explains why mathematics, physics, modeling, algorithms and notation have distinct frameworks, how their results constrain one another, and how they contribute to inquiry and further development. Read it for the overall design and its alternatives; use a familiar sufficient method directly when that is all your task needs.

## Choose an entry


The following entries contain worked connections, not just pointers to smaller operations. Start from the contribution whose inputs are available; an example's presentation order is not a prescribed project sequence.

| What you need to do | Follow the worked connection |
| --- | --- |
| Combine separately calculated results—for example, obtain an overall mean from departments of different sizes | [Change a combining rule (MATH — MP-COMBINE-RESULTS)](https://fpf.tools/MATH/mathematical-thinking---readme/practical-entries/mp-combine-results---change-a-rule-so-that-separately-obtained-results-can-be-combined): expose the lost distinction, construct a summary and operation, prove their compatibility, then use and revise them. |
| Decide a question without reconstructing every hidden detail | [Obtain a sufficient answer (MMP — MMP-SUFFICIENT-ANSWER)](https://fpf.tools/MMP/mathematical-modeling---readme/practical-entries/mmp-sufficient-answer---answer-the-working-question-before-reconstructing-every-detail): expose what reduction loses, bound its effect, interpret the result and obtain more where it changes the answer. |
| Decide whether another observation will improve an action | [Connect intervention, information and choice (MMP — MMP-INTERVENTION-AND-INFORMATION)](https://fpf.tools/MMP/mathematical-modeling---readme/practical-entries/mmp-intervention-and-information---decide-whether-an-observation-will-improve-the-next-action): derive the relevant consequences, compare the report's benefit with its burden, and make the subsequent choice depend only on timely information. |
| Replace expensive component models and still obtain a usable joint answer | [Replace and couple models (MMP — MMP-REPLACE-AND-COUPLE)](https://fpf.tools/MMP/mathematical-modeling---readme/practical-entries/mmp-replace-and-couple---use-cheaper-models-without-losing-the-combined-answer): retain the required responses, connect their meanings and error bounds, and refine only what prevents the answer. |
| Develop a physical prediction and decide which observation matters | [Connect physical accounts and observations (PHY — PH-PREDICT-AND-DISTINGUISH)](https://fpf.tools/PHY/physical-thinking---readme/practical-entries/ph-predict-and-distinguish---develop-a-physical-prediction-and-the-test-it-needs): constrain the law, derive a consequence, compare the observations that matter and revise the affected premise. |
| Construct an algorithm and adapt it when the required answer changes | [Keep construction and output consistent (CMP — CP-ANSWER-UNDER-LIMITS)](https://fpf.tools/CMP/computational-thinking---readme/practical-entries/cp-answer-under-limits---obtain-the-answer-the-work-needs-within-available-resources): construct the recurrence, share results, use bounds where they reduce search, and revisit what may be discarded. |
| Change a requirement consistently in a formula, an operation diagram and a table | [Keep meaning and change connected (NOT — NT-CHANGE-TOGETHER)](https://fpf.tools/NOT/notational-engineering---readme/practical-entries/nt-change-together---carry-a-changed-request-through-several-representations): recover references and interpretation, expose translation losses, and update the affected expressions. |
| Connect mathematics to changes in working methods | [Understand and change a construction (Foundational.Reference:3.2)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference32---understand-and-change-a-construction): retain the distinction a later operation uses and connect it to the general Methods of methodological development in Core. |
| Make reasoning available to other contributors and develop its next use | [Continue and distribute thinking (Foundational.Reference:3.5)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference35---continue-and-distribute-thinking): recover a missing relation, arrange explanation or support, change the work and preserve the method for further development. |

The [Foundational Thinking Architectural Reference](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) helps choose and combine contributions when no single entry suffices. Its [vertical of ongoing work (Foundational.Reference:3.9)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference39---keep-the-vertical-visible-while-doing-the-work) helps locate missing intermediate methods, abilities or resources between a local action and its larger purpose.

## Frameworks in this Suite

| Framework | What you can work on | Patterns | Text, M characters |
| --- | --- | ---: | ---: |
| [Mathematical Thinking (MATH)](https://fpf.tools/MATH) · [Markdown](MATHEMATICAL-PRACTICE-DPF.md) | Construct mathematical objects, operations and alternatives; derive consequences and meet proof obligations. | 20 | 0.480 |
| [Mathematical Modeling (MMP)](https://fpf.tools/MMP) · [Markdown](MATHEMATICAL-MODELING-PRACTICE-DPF.md) | Relate a subject question to mathematics; infer, predict, compare interventions, design observations and revise or combine models. | 17 | 0.575 |
| [Physical Thinking (PHY)](https://fpf.tools/PHY) · [Markdown](PHYSICAL-THINKING-DPF.md) | Construct and test physical accounts; select interactions and idealizations, derive consequences and distinguish them by observation. | 10 | 0.305 |
| [Computational Thinking (CMP)](https://fpf.tools/CMP) · [Markdown](COMPUTATIONAL-THINKING-DPF.md) | Construct algorithms that obtain the required answer within correctness, resource and interaction conditions. | 15 | 0.371 |
| [Notational Engineering (NOT)](https://fpf.tools/NOT) · [Markdown](NOTATIONAL-ENGINEERING-DPF.md) | Design expressions, interpretations and transformations that make operations usable and changes recoverable. | 8 | 0.221 |

**Patterns** counts full pattern bodies. **Text, M characters** measures each complete Markdown framework, including its embedded Architectural Reference, in millions of Unicode characters with spaces and original line breaks, rounded to three decimals. These are scope indicators, not a required reading load.

## Connect the contributions

Predicting an oscillating system can require a physical account, a model with stated idealizations, a mathematical consequence, an algorithm for the approximation and notation whose variables and units remain interpretable. A measurement that defeats the idealization returns to the physical and modeling premises; computing more accurately cannot repair that defect. Conversely, a numerical error need not invalidate the physical law.

These are different grounds for a connected result: mathematical validity, physical adequacy, computational feasibility and intelligibility of expression. Each matters only where that claim is made. A pure proof needs no invented physical test, and a notation problem need not start with a physical question. For example, `q + q = 2*q` remains an identity, while `read() + read()` need not equal `2*read()` when each call obtains a new value.

The Reference explains [how the contributions constrain one another (Foundational.Reference:2.2)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference22---relations-that-form-the-field) and [what preserves or changes the field (Foundational.Reference:2.3)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference23---the-whole-its-continuity-and-its-boundaries). The connected methods remain independently usable.

## Develop and use new ways of thinking

A useful construction can make a new question approachable; an unexplained observation, counterexample or successful new tool can reveal the next question. This Suite supplies the subject-specific constructions. [FPF Core](https://fpf.tools/FPF) supplies general methods for inquiry, methodological development and continuing development. Merely finishing a calculation does not establish that wider continuation.

Research Method Practice, Decision Design, Explanation Design and Narrativization retain their own subjects in the [DPF catalogue](../). They are not absorbed into this Suite because they involve thinking. [Engineering](../Engineering%20DPF%20Suite/) supplies realization of instruments and other systems; [Human Capability Engineering](../Human%20Capability%20Engineering%20DPF%20Suite/) supplies changes in people's capabilities. Obtaining an intellectual result, constructing its means and learning to obtain it are different contributions.

## Reading, use and reuse

Read [Using FPF Library](../../USING-FPF.md) before applying the methods, with or without an AI assistant. Start from the contribution your work needs; the order of files is not a project sequence. Read a selected pattern's conditions, explanation and worked cases. A checklist helps inspect a result; it does not replace the method.

Anatoly Levenchuk, with AI-assisted development and review. These publications continue to evolve; check the edition when relying on a particular result. Original content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), subject to the [licensing terms](../../LICENSING.md). For a method, cite its framework, edition and complete PatternID.

[All domain frameworks](../) · [FPF Library](../../)
