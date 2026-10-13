# Foundational Thinking DPF Suite

**Mathematical Thinking · Mathematical Modeling · Physical Thinking · Computational Thinking · Notational Engineering**

> Construct, justify and revise mathematical and physical accounts, algorithms, models and usable notations; use those results in further inquiry and work.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Date:** 12 October 2026
- **Status:** Eternal alpha. All five member DPFs are available and evolve with their methods, sources and uses.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

**Start with the [Suite Architectural Reference (Foundational)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md)** when you need to choose among these contributions or connect them. Open a DPF directly when you already know the contribution you need.

## Start from a connected problem

You may know formulas or individual operations and still be unable to connect them into an answer. The Suite helps make those connections: what information a construction must retain, what another method can do with its result, and where a changed question makes earlier work worth revisiting.

| What you need to do | Follow the worked connection |
| --- | --- |
| Split or change a calculation while keeping its answer meaningful | [Change a combining rule (MATH — MP-COMBINE-RESULTS - Change a rule so that separately obtained results can be combined)](MATHEMATICAL-PRACTICE-DPF.md#mp-combine-results---change-a-rule-so-that-separately-obtained-results-can-be-combined): expose the lost distinction, construct a summary and operation, prove their compatibility, then use and revise them. |
| Decide a question without reconstructing every hidden detail | [Obtain a sufficient answer (MMP — MMP-SUFFICIENT-ANSWER - Answer the working question before reconstructing every detail)](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-sufficient-answer---answer-the-working-question-before-reconstructing-every-detail): expose what reduction loses, bound its effect, interpret the result and obtain more where it changes the answer. |
| Decide whether another observation will improve an action | [Connect intervention, information and choice (MMP — MMP-INTERVENTION-AND-INFORMATION - Decide whether an observation will improve the next action)](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-intervention-and-information---decide-whether-an-observation-will-improve-the-next-action): derive the relevant consequences, compare the report's benefit with its burden, and make the subsequent choice depend only on timely information. |
| Replace expensive component models and still obtain a usable joint answer | [Replace and couple models (MMP — MMP-REPLACE-AND-COUPLE - Use cheaper models without losing the combined answer)](MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-replace-and-couple---use-cheaper-models-without-losing-the-combined-answer): retain the required responses, connect their meanings and error bounds, and refine only what prevents the answer. |
| Develop a physical prediction and decide which observation matters | [Connect physical accounts and observations (PHY — PH-PREDICT-AND-DISTINGUISH - Develop a physical prediction and the test it needs)](PHYSICAL-THINKING-DPF.md#ph-predict-and-distinguish---develop-a-physical-prediction-and-the-test-it-needs): constrain the law, derive a consequence, compare the observations that matter and revise the affected premise. |
| Construct an algorithm and adapt it when the required answer changes | [Keep construction and output consistent (CMP — CP-ANSWER-UNDER-LIMITS - Obtain the answer the work needs within available resources)](COMPUTATIONAL-THINKING-DPF.md#cp-answer-under-limits---obtain-the-answer-the-work-needs-within-available-resources): construct the recurrence, share results, use bounds where they reduce search, and revisit what may be discarded. |
| Carry a changed instruction through several expressions | [Keep meaning and change connected (NOT — NT-CHANGE-TOGETHER - Carry a changed request through several representations)](NOTATIONAL-ENGINEERING-DPF.md#nt-change-together---carry-a-changed-request-through-several-representations): recover references and interpretation, expose translation losses, and update the affected expressions. |
| Connect mathematics to changes in working methods | [Understand and change a construction (Foundational.Reference:3.2 in Foundational)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference32---understand-and-change-a-construction): retain the distinction a later operation uses and connect it to the general Methods of methodological development in Core. |
| Make reasoning available to other contributors and develop its next use | [Continue and distribute thinking (Foundational.Reference:3.5 in Foundational)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference35---continue-and-distribute-thinking): recover a missing relation, arrange explanation or support, change the work and preserve the method for further development. |


These examples use several patterns together. Their short sequences show dependencies; worked explanations give calculations and return points. Start at a later contribution when its inputs are available. Each DPF's Table of Contents also gives direct help for other questions.

The [vertical of ongoing work (Foundational.Reference:3.9 in Foundational)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference39---keep-the-vertical-visible-while-doing-the-work) asks a complementary question: what larger work is being performed through this action now, and what constituent abilities and resources make it possible? It helps locate a missing intermediate Method or capability even when the elementary operations and the intended whole are familiar.

## Use the publications

For use with an agent, follow [Using FPF (Using FPF and its DPF Suites)](../../USING-FPF.md). Copy this whole folder beside `FPF-Spec.md` in your project's reference folder. The root [ecosystem Readme (FPF Library)](../../Readme.md) gives the other files to copy and a paragraph for the agent's instructions. In GitHub, open an example above or a member link below.

## Constituent disciplines and publications

The Suite describes a composite field: constructing, justifying and developing mathematical and physical accounts, computational ways of obtaining results, modeling correspondences and operative expressions. A theorem, physical explanation, algorithm, interpreted model or usable notation can itself be the intended result. Each branch has its own questions and results; modeling and notation are also objects of development, not merely preparation for physical calculation. The field does not cover every form of intellectual work, all of mathematics or physics, or the whole of computer science.

The five DPFs describe its constituent knowledge and reusable practices. The publications themselves are not the discipline parts. Their connections concern what constructions mean, which operations are possible, what follows from them and what must change when their conditions change.

| Constituent DPF | Contribution to the field |
| --- | --- |
| [Mathematical Thinking (MATH)](MATHEMATICAL-PRACTICE-DPF.md) | Objects, operations, transformations and proof obligations; derive consequences and construct alternatives. |
| [Mathematical Modeling (MMP)](MATHEMATICAL-MODELING-PRACTICE-DPF.md) | Build and revise the correspondence between a subject question and a mathematical construction; combine or change models while preserving the needed answer. |
| [Physical Thinking (PHY)](PHYSICAL-THINKING-DPF.md) | Physical interactions, preparation and observation, admissible accounts and their limits; derive and test physical consequences. |
| [Computational Thinking (CMP)](COMPUTATIONAL-THINKING-DPF.md) | Algorithms, their meaning and correctness, resource demands and interaction; construct an effective way of obtaining a result. |
| [Notational Engineering (NOT)](NOTATIONAL-ENGINEERING-DPF.md) | Construct usable expression rules, interpretations, transformations and relations between representations, including temporal or embodied notation; make the intended operations performable and changes recoverable. |

The [Foundational Thinking DPF Suite Architectural Reference](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains this whole, its alternatives and limits, and supports selection and connected use of the Methods. It is a publication about the discipline and its language, not a sixth discipline.

## How the constituents form a whole

One entry is a physical question. A physical explanation constrains which model relations can describe a phenomenon and what an observation can distinguish. Mathematical construction supplies consequences and proof conditions. A computational construction must obtain the required result within its resource and interaction conditions. Modelling relates that result back to the question; notation lets the participants perform, inspect and alter the constructions without silently changing their meaning.

These relations support revision as well as forward calculation. A counterexample can change a mathematical construction; an observational mismatch can reopen a physical premise; non-identifiability can change the requested inference; a computational limit can require a different representation or algorithm. The affected expressions and dependent conclusions then need to change with the premise.

The whole makes a construction or consequence jointly interpretable, obtainable and revisable while retaining the different grounds on which its parts rest. Mathematical validity, physical adequacy, computational feasibility and the intelligibility of an expression are different conditions. None substitutes for the others, and each applies only where that kind of claim is made: a pure proof needs no invented physical validation. The [full account (Foundational.Reference:2.2 in Foundational)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference22---relations-that-form-the-field) explains how these conditions constrain and revise one another.

For example, predicting an oscillating system requires a physical account of the interactions, a model with stated idealizations, a mathematical consequence, a way to compute the needed approximation and an expression whose variables and units remain interpretable. A measurement that defeats the idealization returns to the physical and modelling premises; running the same algorithm more accurately cannot repair that defect. Conversely, a numerical error need not invalidate the physical law. The linked DPFs teach the distinct constructions and returns.

This is a field architecture, not a requirement to use all five DPFs for every task. A pure mathematical construction can be complete without a physical example. Algorithm construction can begin with a required witness or cost bound. Notation design can begin with an ambiguous score, diagram or gesture and finish with a usable reading procedure; using notation in music does not bring musical performance into this Suite. A question can also begin with a failed model correspondence or an unexplained physical observation. The constituent repertoires remain independently usable, and applications outside the field remain applications.

For example, replacing one supplied value by two sensor reads changes the meaning of an expression. The identity `q + q = 2*q` remains true, but `read() + read()` need not equal `2*read()`. Notation and computational interpretation expose which operation is intended; a measurement account supplies what a read means. This entry starts with expression use, not with a physical calculation awaiting its suppliers.

The field continues while the five kinds of constructive contribution and their relations remain available: deriving and warranting consequences, establishing their subject correspondence, forming physical accounts, obtaining results through effective operations, and constructing interpretable expressions. New theories, models, algorithms and notation can replace older ones when the affected grounds and couplings remain recoverable. Replacing a constituent requires an adequate contribution in these relations; merely removing its questions changes the field. A broader purpose or a new subject-specific field requires a fresh architecture judgement; a common word such as “model” or “thinking” is insufficient. [The Reference (Foundational.Reference:2.3 in Foundational)](FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md#foundationalreference23---the-whole-its-continuity-and-its-boundaries) develops the continuity rule and possible connections to larger fields.

## Related fields and Core

[FPF Core](../../FPF-Spec.md) supplies the general distinctions and Methods for inquiry, Method development, composition, qualification and continuation. This Suite supplies mathematical, physical, computational and notational constructions with their particular premises and grounds. Broad applicability does not make those constructions generic Core instructions.

Research Method Practice, Decision Design, Explanation Design, Financial Domain Modeling, Defense and Transmission Modeling, and Narrativization have their own subjects and Methods. They can use this Suite or supply a result it needs. Their complete fields are not absorbed under the broad word “thinking”. Find them through the [Library index (FPF Library)](../../Readme.md).

The [Engineering DPF Suite](../Engineering%20DPF%20Suite/README.md) supplies system realization, including instruments and software arrangements when those changes are needed. Human Capability Development supplies changes in human capability when those are needed. An intellectual result, the engineered means for obtaining or using it, and a person's ability to use it remain different contributions.

## The Reference and its editions

The Reference answers working questions about selection, combination, field structure and missing contributions. It leads to the full Methods and evidence. Its answers can also use outside suppliers without making those fields constituents of this Suite.

When a supplying Method changes, reconsider only the answers whose meaning or applicability can change. A Reference edition must distinguish available results, descriptions of Methods and contributions still missing. A date or an accessible title does not establish that an answer remains suitable. A known sufficient DPF contribution can be used directly without a Reference detour.

## Rights and citation

Copyright © 2026 Anatoly Levenchuk. This account and the author's DPF publications are licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/), except material carrying a separate notice. Cited sources retain their own rights. Independent authors choose the licenses for their own DPFs and LPFs.

Cite this account as: Anatoly Levenchuk. *Foundational Thinking DPF Suite*. [FPF repository](https://github.com/ailev/FPF). Include the date shown at the start of this file. For a method, also cite its DPF edition and PatternID.
