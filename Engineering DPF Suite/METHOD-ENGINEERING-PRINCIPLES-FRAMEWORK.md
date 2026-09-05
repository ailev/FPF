# Method Engineering Principles Framework

> A domain pattern language for choosing, constructing, describing, testing, and improving Methods and their supporting arrangements.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 5 September 2026
- **Status:** Eternal alpha: a working framework with source-grounded guidance and bounded worked applications. The PLUS-ME production account is prospective guidance, not a report of recurring successful production.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

Begin with a difficulty in the practice you want to improve: which way of working, description, trial, or supporting arrangement needs to change?

Use the Table of Contents below to search by a familiar term or working question and find the relevant PatternID. Open the pattern and apply its Problem frame, Solution, worked cases, and checklist to your own Method Engineering task. Start with the smallest result that changes the current decision; follow another pattern when that result needs its contribution.

The Readme offers selected practical entries, including guidance for connected use of several patterns. The Preface explains the distinctions that recur across the framework. The full Table of Contents also serves questions outside the examples; pattern bodies supply the working moves, conditions, and stops.


# Table of Contents

Search the Keywords & Search Queries column for the difficulty, subject, or result you recognize. Each row explains the pattern's contribution and links to its full body. The Readme offers selected starting examples; use the complete index for other working questions.

`ME.*` is this framework's PatternID namespace. Numbers are stable addresses; the Parts give reader order and do not prescribe Work order.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Method Engineering Principles Framework Readme](#method-engineering-principles-framework-readme) | Start from a recognizable Method-related difficulty and choose one direct pattern or a small cooperating set. |
| [Citation](#citation) | Cite this framework or one pattern with its author, title, release date, and publication address. |
| [Preface](#preface) | Understand the distinctions that keep Method, description, Work, support, evidence, and culture connected without collapsing them. |
| [PLUS-ME profile](#plus-me--pattern-language-unfolding-situational-method-engineering) | Understand the production and situated-use profile, its source choices, worked application, costs and alternatives. |
| [Production MethodDescription](#production-methoddescription--engineer-a-source-grounded-methoddescription-in-pattern-language-form) | Use the bounded reusable action, source-profile variation, results and stops without inferring performed Work or Method parts. |
| [Cross-Pattern Application](#cross-pattern-application) | Follow a release case from an ambiguous methodology label to a bounded architecture decision and separate support results. |
| [Framework Boundary and Refresh](#framework-boundary-and-refresh) | Check scope, example forms, source limits, external-result use, edition identity, and reopen conditions. |

**Part I - Method Focus, Architecture History, Repertoire, Situational Criteria, and Recovery**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [ME.1 - Choose and Reopen the Project Method-of-Interest](#me1---choose-and-reopen-the-project-method-of-interest) |  | *Keywords:* Method of interest, process, project, case, workflow, methodology, capability, tool, support. *Queries:* "What needs to change when the team says its methodology is failing?" "Is the blocking question about a Method, its description, the Work, or surrounding support?" Select the smallest Method-related focus and the condition for reopening it or returning to the owning practice. | FPF A.15.6, C.11 |
| 2 | [ME.19 - Recover Why and How a Professional Method Architecture Differentiated](#me19---recover-why-and-how-a-professional-method-architecture-differentiated) |  | *Keywords:* professional history, Method differentiation, lineage, institutional change, tools, regulation, diffusion, causal explanation. *Queries:* "Why did this profession acquire these different Methods and arrangements?" "Which sequence, rival explanation, and observations support the historical account?" Recover how the architecture differentiated and which historical claims can inform a current choice; qualify causal reliance separately from a descriptive sequence. | ME.1; FPF C.28, A.10 |
| 3 | [ME.2 - Recover a Reusable Method Repertoire and Its Lineages](#me2---recover-a-reusable-method-repertoire-and-its-lineages) |  | *Keywords:* Method repertoire, method base, reusable practice, source edition, family, variant, lineage, provenance. *Queries:* "What usable Methods and candidate accounts are hidden across our manuals, tools, and remembered practice?" "Which reuse and derivation claims have a recoverable source?" Build an inspectable repertoire with identities, status, applicability, source references and return conditions, and supported lineage, including gaps that change the receiving choice. | ME.1; FPF A.3.1, G.5, G.11 |
| 4 | [ME.18 - Reconstruct a Candidate Method Account from Observed Work](#me18---reconstruct-a-candidate-method-account-from-observed-work) |  | *Keywords:* tacit practice, observed Work, logs, interviews, reconstruction, rival accounts, evidence programme, uncertainty. *Queries:* "What way of working can we reconstruct from incomplete and conflicting records?" "Which additional observations would change the candidate account?" Combine evidence around the unresolved claims when ordinary Method recovery is insufficient; return a qualified candidate account, its alternatives, and the exact remaining evidence need. | ME.1, ME.2; FPF A.3.1.MR, A.10 |
| 5 | [ME.3 - Build Situational Method Requirements and Fit Criteria](#me3---build-situational-method-requirements-and-fit-criteria) |  | *Keywords:* situational Method Engineering, requirements, applicability, fit criteria, constraints, capability, authority, evidence timing. *Queries:* "What must this Method contribute in this project situation?" "Which limits concern the Method and which concern performers, support, or the domain result?" State decision-relevant criteria and their evidence needs so later comparison and validation can judge the required contribution under the actual conditions. | ME.1, ME.2; FPF C.11, A.10 |
| 6 | [ME.4 - Recover Methods and Decision-Relevant Contributions from Documentary Packages and Corpora](#me4---recover-methods-and-decision-relevant-contributions-from-documentary-packages-and-corpora) |  | *Keywords:* documentary corpus, source-local recovery, methodology package, handbook, standard, Method content, contribution, source role. *Queries:* "Which useful contributions are hidden in this source or plural library?" "What is an asserted Method, a candidate account, or neighboring tool, support and cultural material?" Recover a bounded source-local dossier at the depth the receiving use needs; preserve single-source exits and keep returned Work-recovery accounts distinct. | ME.1, ME.2, ME.3; FPF A.3.1, C.2.1 |

**Part II - Individual Qualification and Method-Architecture Alternatives**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 7 | [ME.5 - Qualify Individual Methods, Candidate Accounts, and Local Connections](#me5---qualify-individual-methods-candidate-accounts-and-local-connections) |  | *Keywords:* Method qualification, candidate account, local connection, applicability, minimum conditions, evidence, rejection. *Queries:* "Which individual candidate is usable for this bounded result?" "Can one unmet condition settle the choice before an architecture comparison is needed?" Qualify each Method, account, or local connection against the receiving criteria and retain its actual epistemic status, unresolved premise, and reason to keep or reject it. | ME.2, ME.3, ME.4; FPF A.3.1, A.10 |
| 8 | [ME.6 - Compare Method-Architecture Alternatives and Simultaneous Enactment Conflicts](#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) |  | *Keywords:* Method architecture, simultaneous Work, project view, process view, case view, allocation, support, conflict, trade-off. *Queries:* "How do plausible Methods interact when their enactment overlaps?" "Which alternative changes provisional-result use, authority, shared capacity, or burden?" Compare materially different Method, Work, allocation, description, support, and cultural structures while keeping the receiving result and serious alternatives visible. | ME.3, ME.5; FPF C.32.MWA, A.19, C.11 |
| 9 | [ME.7 - Resolve a Proposed Method Whole into Obtaining Relations or a Candidate Account](#me7---resolve-a-proposed-method-whole-into-obtaining-relations-or-a-candidate-account) |  | *Keywords:* Method whole, composition, direct relation, candidate design, invariant, variation, realization, trial. *Queries:* "Does the proposed Method whole already exist through obtaining relations?" "What can we specify and test while it is still a proposal?" Return the supported direct relations or a prospective candidate-whole account with the conditions, realization WorkPlan, and bounded test needed to settle its status. | ME.5, ME.6; FPF A.3.1, A.22, A.15.2 |

**Part III - Method Descriptions, Representations, and Enactment Support**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 10 | [ME.8 - Author a MethodDescription for Named Uses](#me8---author-a-methoddescription-for-named-uses) |  | *Keywords:* MethodDescription, procedure, manual, description content, planner, performer, review use, applicability, stops. *Queries:* "Which Method claims does this user need for this action?" "What must the description preserve from the Method or candidate account?" Author a use-bounded description with actionable content, conditions, evidence limits, source references, and return conditions; retain the distinction between an admitted Method and a prospective account. | ME.2, ME.3, ME.7; FPF A.3.1, A.3.2, C.2.1 |
| 11 | [ME.9 - Compose Complementary Method Representations for Their Uses](#me9---compose-complementary-method-representations-for-their-uses) |  | *Keywords:* complementary representations, MethodDescription, view, viewpoint, diagram, text, task-specific profile, exposure, omission. *Queries:* "How should performers, method engineers, support builders, and assessors see different claims about the same Method?" "Which omissions or conflicts across those uses need a shared decision?" Relate complete use-bounded representation selections and preserve their direct source, result, reliance, loss, and return positions. | ME.8; FPF C.37, C.2.1, E.17.0, C.29, E.24.PUB, A.22 |
| 12 | [ME.22 - Compare Method Descriptions by Content and Representation](#me22---compare-method-descriptions-by-content-and-representation) |  | *Keywords:* description revision, content versus form, representation comparison, comprehension, application, confounding, causal attribution. *Queries:* "Did the new guide add needed content, improve its presentation, or change both?" "What does this comparison justify for the same receiving use?" Compare the smallest informative contrasts, retain losses and evidence limits, and return a bounded revision decision rather than a claim of Method effectiveness. | ME.8; ME.9 for cross-use relations; FPF A.6.3.RT, C.37, A.10 |
| 13 | [ME.10 - Build a Method Base and Enactment-Support Arrangement](#me10---build-a-method-base-and-enactment-support-arrangement) |  | *Keywords:* method base, retrieval, edition selection, tailoring, enactment support, tool, permission, confidential material, feedback. *Queries:* "Can named users find and use the right Method material for their actual tasks?" "Which smallest configuration repairs a failed retrieval, comparison, tailoring, or support task?" Build and test the support arrangement against named user actions, mandatory conditions, current editions, and explicit stops. | ME.8; ME.9 when complementary representations are allocated to unlike named Method actions; FPF C.37, A.22, A.13, A.15.1, A.2.8.PER |

**Part IV - Trial and Separate Coherence, Fit or Transfer, and Worth Decisions**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 14 | [ME.11 - Trial the Method in Representative Work](#me11---trial-the-method-in-representative-work) |  | *Keywords:* Method trial, representative Work, discriminating case, performer, support conditions, observation, evidence. *Queries:* "What happened when this Method was tried in actual Work?" "Which trial conditions would test the claimed contribution and expose its limits?" Plan and observe representative or discriminating enactment and return occurrence-level evidence for the later coherence, fit, transfer, and practical-worth decisions. | ME.3, ME.7, ME.10; FPF A.13, A.15.1, A.10 |
| 15 | [ME.12 - Verify Method and MethodDescription Coherence](#me12---verify-method-and-methoddescription-coherence) |  | *Keywords:* verification, coherence, description mismatch, missing stop, inconsistent representation, obsolete edition, correction. *Queries:* "Which relied-on Method claim fails to agree with its description, representation, or supporting material?" "Where is the smallest correction that restores the named use?" Locate the expected agreement, the conflicting evidence, and the maintained result that owns the claim; return a bounded coherence result and repair target. | ME.8–ME.11; FPF A.10, B.3 |
| 16 | [ME.13 - Validate Situational Fit and Transfer](#me13---validate-situational-fit-and-transfer) |  | *Keywords:* validation, situational fit, transfer, adaptation, changed conditions, capability, support, domain result. *Queries:* "Does this Method fit the situation in which we need it?" "Which claim survives when the project, industry, performer, or support conditions change?" Compare original and receiving conditions with actual Work evidence, identify relevant adaptations, and return the supported fit or transfer claim and its limits. | ME.3, ME.11; FPF A.10, G.11 |
| 17 | [ME.14 - Evaluate Practical Worth Against Current Alternatives](#me14---evaluate-practical-worth-against-current-alternatives) |  | *Keywords:* practical worth, alternatives, burden, coordination cost, tooling, opportunity cost, trade-off, replace, stop. *Queries:* "Is this Method worth its total burden compared with current alternatives?" "Who receives the benefit and who bears capability, support, exposure, or recovery costs?" Compare keeping, revising, replacing, branching, and stopping under the actual situation, with explicit consequences and the evidence that can change the choice. | ME.11–ME.13; FPF A.19, C.11, A.10 |

**Part V - Variants, Introduction into Practice, and Cultural Continuation**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 18 | [ME.15 - Maintain Method Variants, Provenance, and Reuse](#me15---maintain-method-variants-provenance-and-reuse) |  | *Keywords:* Method variant, reusable semantics, provenance, branching, version, adaptation, lineage, reuse. *Queries:* "Did this change alter a reusable way of working or only its description and support?" "Which applicability and evidence claims belong to the resulting branch?" Identify meaningful variants and maintain their derivation, status, and reuse conditions; return other changes to the description, Work, or support subject they actually affect. | ME.2, ME.8–ME.14; FPF A.3.1, G.11 |
| 19 | [ME.16 - Introduce, Observe, and Revise a Method in Practice](#me16---introduce-observe-and-revise-a-method-in-practice) |  | *Keywords:* introduction into practice, adoption, authorized Work, capability development, assistance, observation, revision, contribution. *Queries:* "What changed when this Method was introduced into a real practice?" "Which observed result supports revising the Method, its description, or the surrounding arrangements?" Follow the bounded introduction from intended changes through actual Work and later use, and qualify any causal claim about the outside result. | ME.10, ME.11, ME.14, ME.15; FPF A.13, A.15.1, C.28 |
| 20 | [ME.17 - Deliberately Continue and Change Method-Engineering Culture](#me17---deliberately-continue-and-change-method-engineering-culture) |  | *Keywords:* Method Engineering culture, practitioner population, generation, transmission, recognition, selection, memory, retention, loss. *Queries:* "Which cultural relation should deliberately continue or change across this practitioner population?" "What observations distinguish transmission or retention from publication and local use?" Define a bounded cultural claim, compare serious explanations, and choose the next authorized intervention or informative observation with an explicit return. | ME.15, ME.16; FPF C.20, C.36, G.11 |

**Part VI - Pattern-Language Production and Situated Use**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 21 | [ME.21 - Reconcile and Allocate Source Contributions after Exact Subtraction](#me21---reconcile-and-allocate-source-contributions-after-exact-subtraction) |  | *Keywords:* conceptual synthesis, semantic allocation, source roles, exact subtraction, merge, split, unresolved remainder. *Queries:* "What should survive from these partly agreeing sources, and where should it live?" "Is the needed answer already supplied?" Produce one justified Method-content allocation with its current supplier, conditions, source return and candidate limits. | ME.4; FPF F.0.1, F.1, F.0.2, E.4.DPF; ME.5/ME.7 for identity or composition |
| 22 | [ME.23 - Architect a Problem-First MethodDescription Pattern Language](#me23---architect-a-problem-first-methoddescription-pattern-language) |  | *Keywords:* pattern-language architecture, problem-first entry, MethodDescription, profile, material relation, specialization, parthood. *Queries:* "How should these description contributions form a useful language?" "Which relation changes the next answer without inventing Method parts?" Allocate bodies by their subjects and independent results, preserve inherited answers and direct-description exits, and state material dependencies and loss. | ME.8, ME.21; FPF A.3.2, B.1.5, A.22, E.8, E.11.PFP |
| 23 | [ME.24 - Falsify and Refresh Source-to-Pattern Coverage by Reconstruction](#me24---falsify-and-refresh-source-to-pattern-coverage-by-reconstruction) |  | *Keywords:* source coverage, reconstruction, missing condition, held-out contribution, source change, affected refresh, unavailable basis. *Queries:* "Can this language reconstruct the action and stop it promises from the source?" "What must return when one premise changes?" Expose a missing or misallocated contribution and its repair destination; retain independently supported results and widen the question when the dependency boundary is unknown. | ME.4, ME.21, ME.23; ME.12/ME.15 for known repair; FPF F.0.2, G.11 |
| 24 | [ME.20 - Use Pattern-Language Knowledge to Continue Situated Method Engineering](#me20---use-pattern-language-knowledge-to-continue-situated-method-engineering) |  | *Keywords:* PLUS-ME, situated use, pattern language, unfolding, next result, changed condition, CGUS, chooser, performer. *Queries:* "Which pattern contribution can supply the Method Engineering result needed now?" "What becomes blocked, unknown or worth reconsidering after this new fact?" Continue or stop at the bounded useful result; formalize CGUS only when its own question requires it and keep an ongoing-Work decision separate. | Direct ME result for the current question; FPF E.11.PUA, E.11.PUR, A.22.CGUS, A.15.7 when applicable |

# Method Engineering Principles Framework Readme

## Practical entries

This framework helps method engineers, domain practitioners, team leads, tool and platform builders, educators,
and practice-development owners change a Method without losing the Work and result for which that Method matters.
It covers Method focus, repertoire and architecture, descriptions and representations, enactment support, trial,
separate assurance decisions, variants, introduction into practice, and cultural continuation.

Begin from the costly difficulty in the receiving practice. Do not begin from a methodology label, a package
chapter, or an assumed lifecycle. The entries below are selected examples, not a catalogue or coverage boundary.
If none fits, use the Table of Contents or search the pattern titles and working questions. Pattern bodies contain
the authoritative moves, worked cases, stops, and evidence limits.

### ME-FOCUS — Find the smallest Method Engineering subject that can change the receiving result

- **Situation:** A project says its methodology, process, workflow, framework, or way of working must change,
  while the actual difficulty may concern one Method, relations among several Methods, a candidate account,
  description, capability, support arrangement, authority, source, tool, or the receiving domain result itself.
- **Question:** What is the smallest accurately identified Method Engineering subject? What history, repertoire,
  situational criteria, package contribution, or reconstruction from observed Work does that decision need?
- **First useful result or honest blocker:** A Method-focus result, or a decision to return the problem to its owning practice
  because no Method decision is needed. Follow it only when needed with an account of Method differentiation, an
  inspectable repertoire, a scoped candidate account, situational criteria, or a package dossier that keeps the
  kinds of its contributions distinct. Otherwise identify the unresolved identity, missing source or evidence,
  or unclear receiving use.
- **Start with:** `ME.1`. Use `ME.19` when the present architecture is treated as natural, `ME.2` for a reusable
  repertoire, `ME.18` only when ordinary candidate recovery cannot support the decision, `ME.3` for situational
  criteria, and `ME.4` when a documentary source or plural corpus bundles unlike contributions.
- **Stop or return:** Stop at the first result that changes the current decision. Return to the owning domain
  when no Method decision is needed; reopen when the receiving problem, subject, constraints, sources, or
  observed contribution changes.

### ME-ARCHITECTURE — Qualify candidates and compare Method architectures without inventing a whole

- **Situation:** Several individually plausible Methods or candidate accounts may be co-used, connected, or
  assembled, but their Work overlap, allocation, evidence, descriptions, support, permission, authority, and
  cultural consequences can differ across serious alternatives.
- **Question:** Which subjects are individually usable, which structures and direct relations change the
  decision, and does the proposed whole already obtain or remain a prospective account?
- **First useful result or honest blocker:** Individual qualifications that retain each candidate’s status, a Method-architecture
  decision comparing materially different alternatives, and either supported obtaining relations or a prospective
  candidate-whole account with a WorkPlan for realization and testing. Otherwise identify the missing relation or
  evidence.
- **Start with:** `ME.5` for cheap individual qualification, `ME.6` when interactions among qualified subjects
  change the receiving decision, and `ME.7` only when the identity or obtaining relations of a proposed whole
  remain a live question.
- **Stop or return:** Stop with an individual or relation-only result when no whole is needed. A selected
  proposal, diagram, list, WorkPlan, or package does not create a Method or make proposed relations obtain.

### ME-DESCRIBE-SUPPORT — Make Method material usable for named decisions and Work

- **Situation:** A Method or candidate account exists, yet people cannot find the current edition, distinguish
  status, see the claims needed by their action, relate complementary representations, tailor a branch, use a
  tool safely, give feedback, or stop before support overreaches.
- **Question:** Which Method claims do users need for each action, and how should the Method-specific profile
  relate the complete representation rows for those uses? What is the smallest configuration that lets named
  users retrieve, compare, or tailor Method material, obtain enactment support, and give feedback as required?
- **First useful result or honest blocker:** A MethodDescription for named uses, or improved candidate content. For one action,
  obtain the result from the pattern that governs it. For different Method actions, produce a complete ME.9
  profile: one complete C.37-bearing row per action and a separate cross-use result covering the shared source,
  correspondences, conflicting omissions, edition relations, decisions to keep representations separate, and
  returns that affect several rows. Add a tested support configuration for named user tasks. If this cannot be
  completed, identify what is missing: a direct result, cross-use relation, reliance or receiving result,
  admission, relation, collection premise, access condition, capability, Work occurrence, or task result.
- **Start with:** `ME.8` for use-bounded description content. Use `C.37` or a direct pattern and stop when one
  action needs no Method-specific cross-use profile. Use `ME.9` when a current MethodDescription or candidate
  account needs complementary use-bounded rows related across different Method actions, and `ME.10` when named
  users must obtain and use the material through a configured support arrangement.
- **Stop or return:** Stop when the named action works or the exact defect is known. Keep the Method,
  descriptions, representations, C.37 claim groups, collections, editions, Systems, Work, permission,
  authority, capability, support configuration, and results separate.

### ME-TRIAL-CHANGE — Trial, judge, revise, introduce, and continue a Method under bounded evidence

- **Situation:** A Method or candidate account is ready for actual Work, but coherence, situational fit,
  transfer, practical worth, variant identity, introduction into practice, and cultural continuation are being
  treated as one success claim.
- **Question:** What did representative Work establish, which separate decision can use it, what reusable Method
  semantics or surrounding subjects changed, and is the live boundary one project or a practitioner population?
- **First useful result or honest blocker:** Occurrence-level trial evidence; separate coherence, fit or transfer,
  and practical-worth results; a maintained variant lineage or non-variant maintenance return; a typed
  introduction decision; or a bounded cultural-continuation decision with explicit gaps.
- **Start with:** `ME.11` for actual trial Work; `ME.12`, `ME.13`, and `ME.14` for their separate judgments;
  `ME.15` when reusable Method semantics may have changed; `ME.16` for a bounded introduction attempt; and
  `ME.17` only for generation, transmission, recognition, selection, memory, retention, or loss in a population.
- **Stop or return:** Stop at the first decision needed now. One successful trial, publication, course, local
  adoption, or project result does not establish effectiveness, transfer, organizational retention, or culture.

### PLUS-ME — Continue Method Engineering through pattern-language knowledge

- **Situation:** Several Method-architecture questions remain connected, and new facts can change which result is needed next.
- **Question:** Which pattern contribution can supply that result now, and which earlier claims or uses must change after the new fact?
- **First useful result or honest blocker:** A bounded continuation with its supporting knowledge, available/blocked/unknown action, first missing fact, and stop or return; during ongoing Work, a separate A.15.7 decision names chooser and performer.
- **Start with:** ME.20's working question and result-return table. Use an already sufficient MethodDescription or matching earlier result directly.
- **Stop or return:** Stop at the first useful result or missing condition. Return only the affected qualification, whole, architecture, description, support, source, or publication question. Add a durable result or formal CGUS only when its own use requires it.

### ME-PLUS-PRODUCE — Engineer source-grounded Method-description knowledge as a pattern language

- **Situation:** Unlike sources partly agree, and recurring users need a language that preserves the useful actions, conditions, differences and source returns.
- **Question:** What should be recovered and allocated, which claims belong together, and can the resulting language reconstruct what its receiving use needs?
- **First useful result or honest blocker:** One justified allocation, bounded description comparison, useful language relation or reconstruction/refresh result; or the source, Method identity, missing condition or unbounded coverage claim that prevents it.
- **Start with:** The [production MethodDescription](#production-methoddescription--engineer-a-source-grounded-methoddescription-in-pattern-language-form) for the connected account. Enter ME.21, ME.23 or ME.24 at the missing result; use ME.4 for documentary recovery and ME.22 for an actual content/representation comparison question.
- **Stop or return:** Stop with a sufficient direct source or one-Method description. Preserve candidate status and independently supported results; return only affected claims unless the dependency boundary cannot be recovered.

### ME-CARD-01 — Develop a Method and its supporting arrangements without losing the receiving problem

- **Situation:** A project wants to improve practice, but a local operation, methodology label, incumbent
  framework, tool, or provider arrangement is already being treated as the Method.
- **Question:** Which Method-related result is needed now, and how can the team change it while keeping the
  receiving Work, result, evidence, authority, and support boundaries visible?
- **First useful result or honest blocker:** The smallest truthful focus, architecture, support, trial, or
  continuation result that changes the current decision; or the named missing identity, relation, Work, or evidence.
- **Start with:** `ME.1`; then use only the pattern whose result is missing. This entry connects the selected
  general questions, but dependencies among results do not prescribe calendar order or one Method lifecycle.
- **Stop or return:** Return to the owning domain when the Method is not the problem. Stop before inventing a
  Method, performed Work, authority, support success, causal effect, transfer, or cultural continuation.

Recover the receiving problem and choose the Method-related subject before redesign. Explain the architecture
only as far as the decision needs; recover repertoire, criteria, and package contributions without preselecting
a whole. Qualify subjects, compare serious Method and Work structures, and preserve candidate status. Describe
and represent claims for named uses; test support through named user tasks.

Check construction, description, and support coherence through `ME.12` against their available basis, including
before a trial. Require actual Work evidence for enactment or observed-contribution claims; judge fit, transfer,
and worth separately. Maintain variants by reusable semantics. Separate bounded introduction from cultural
continuation across a population. Stop at the first useful result and reopen from changed evidence.

The connected reader route is `ME.1`, `ME.19`, `ME.2`, `ME.18`, `ME.3`, `ME.4`, `ME.5`–`ME.10`, and
`ME.11`–`ME.17`. It follows R7’s account connecting Method, description, Work, capability, instrument, variant, and culture.
The route explains the subject and its result dependencies; one project can use only the results it needs,
in the Work order its situation requires. This is one selected example, not a catalogue or prescribed workflow.
Use the Table of Contents or search when the current difficulty does not match it.

## Citation

If you use this framework, please cite:

```text
Levenchuk, Anatoly. Method Engineering Principles Framework.
5 September 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title, for example: Method Engineering Principles Framework, ME.9 - Compose Complementary Method Representations for Their Uses. Retain the release date, and include a permanent link or stored copy when the exact wording matters.

# Preface

Method Engineering begins when a Method's identity, architecture, selection, description, support, trial,
change, or continuation blocks a decision. A domain project merely using a Method remains in its owning domain.
The Method becomes the Method Engineering subject only when a decision about that Method or its relations
is needed.

This edition fixes its transdisciplinary dependency in [FPF dependency and compatibility](#fpf-dependency-and-compatibility). The depended-on FPF patterns retain authority over common identities, relations, evidence, structures, Work, comparison, publication, currentness, and cultural claims; this framework retains only Method Engineering moves that change specialist action. Domain Methods, evidence, quantities, legal and safety authority, and consequences remain with the practice that owns them. The patterns return results to engineering, management, learning, music and dance, administration, finance, or another receiving practice without taking over that practice's decision.

## Method, MethodDescription, WorkPlan, and Work remain distinct

A Method is a reusable way of doing. A MethodDescription is an episteme about one admitted Method. A candidate
Method account can be improved, compared, and tested while its candidate status remains explicit. A WorkPlan is
about intended Work. Admit an occurrence as Work only after establishing when it happened, who performed it, which admitted Methods
they enacted, which Systems and relations it relied on, and its conditions and results.

These distinctions prevent a familiar failure: a team writes a complete playbook, schedules a trial, publishes
it in a repository, and then reports that the Method exists and was enacted. Each claim needs its own basis.
Tools, prompts, repositories, providers, capability, permission, authority, descriptions, support structures,
and results likewise keep their own identities.

## Several structures and several views can coexist

A Method decision may depend on a Method composition structure, a Method unfolding, simultaneous Work, an
allocation structure, a subject-and-support arrangement, a description structure, or cultural relations. These
structures need not be isomorphic. Name the structure and relation that changes the decision. Do not call every
connected arrangement a graph: a mathematical graph is one possible lens only after its nodes, edges, semantics,
and use are selected.

Project, process, and case views can expose different claims about the same Work. A project viewpoint may expose
dates, allocations, authorities, and decision slots. A process viewpoint may expose recurring input/result and
coordination correspondences. A case viewpoint may expose the changing evidence, exception, and next decision.
The views do not create three Work occurrences, identify three Methods, or make a WorkPlan into performed Work.

## Reader route and result dependencies do not prescribe Work order

The publication begins with focus and recovery because later decisions need a truthful subject. It then moves
through individual qualification and architecture, description and support, and trial and change. This order
helps a reader find prerequisites. It is not a lifecycle. Repertoire recovery, description, support repair,
trial planning, and source refresh can overlap; a known support or evidence defect can be repaired without
traversing every earlier pattern.

Use the smallest entry whose result can change the decision. Follow a dependency only when the receiving result
actually consumes it. Stop early when an individual qualification, non-Method return, exact gap, or bounded
repair already resolves the working difficulty.

## Status, evidence, and assurance decisions are preserved

Identification, qualification, selection, trial, and effectiveness are different claims. A candidate account
does not become a Method because it is coherent, selected for trial, represented well, supported by a tool, or
used in Work. A successful occurrence establishes only the observations and results supported by that occurrence.

`ME.12` checks coherence among the claims on which a use relies. `ME.13` checks bounded fit or transfer. `ME.14` judges
practical worth against current alternatives. The results can disagree. A Method can be coherent yet poorly fit,
fit one situation yet fail transfer, or produce a useful result whose burden makes another alternative preferable.

## What this publication foregrounds and leaves outside

The framework foregrounds choosing and recovering the Method Engineering subject; qualifying candidates and
comparing architectures; authoring and comparing descriptions and configuring enactment support; obtaining actual
trial evidence and making separate judgments; maintaining variants, introducing Methods into practice and
changing cultural continuation; and producing and using connected pattern-language knowledge. The last family
is the PLUS-ME profile, not a restriction of the general framework.

It does not contain domain Methods, operating procedures, curricula, legal or safety decisions, software tools,
repository designs, statistical identification procedures, or complete organizational-change programmes. Use
their direct Methods and authorities. Open a neighbouring DPF only when its specialist result is needed; the
Method Engineering framework does not assume that a sibling edition is available merely because its discipline
is named.

## Why these Method Engineering questions stay separate

A practitioner often receives a proposed Method as a package: a procedure, a diagram, a tool, a training course and a success story. The costly failure is to change the whole package without knowing which contribution is missing. Method Engineering separates the questions because their useful results and grounds differ. A truthful description may still describe an unsuitable Method; a suitable Method may have poor support; a well-supported trial may still leave practical worth unresolved.

The gain is not a complete framework traversal. It is an appropriately bounded answer that the owning practice can use: a qualified candidate, an architecture alternative, usable description content, a support correction, trial evidence or a separate change decision. The EC-417 application illustrates how these questions connect without creating a Method from a project label. Direct domain work remains outside until a Method-related question actually blocks it.

This separation is also a protection against familiar biases. Source prestige does not admit a Method, a familiar package does not define its parts, and a successful demonstration does not settle fit, causal contribution or worth. Check the subject, receiving use, relied-on conditions and first useful result before accepting a more ambitious account. If a known direct answer already settles the difficulty, stop there.

The cost is maintaining several answers and their dependencies instead of one undifferentiated success claim. Keep them separate only where a difference changes selection, action or reconsideration. ME.1 supplies the smallest subject; ME.5–ME.7 supply qualification and architecture; ME.8–ME.10 supply description and support; ME.11–ME.17 separate evidence, judgments and maintenance. ME.19 can explain why a professional architecture differentiated without treating that history as a justification of its present worth.

## PLUS-ME — Pattern-Language Unfolding Situational Method Engineering

PLUS-ME is a profile of the broader, representation-neutral Method Engineering framework. Use it when recurring Method Engineering questions benefit from connected pattern-language knowledge, or when that knowledge must be produced and maintained from unlike sources. It is not a requirement to describe every Method as patterns. ME.22's content/representation comparison is a general Method Engineering contribution and can be used outside this profile.

### Situation, problem and first gain

A Method engineer has a handbook, current research, an existing pattern library and a returned account of local practice. They partly agree, but neither chapter boundaries nor a ready-made process tells the engineer which reusable actions, conditions and unresolved claims should survive. Later, a new fact can change the useful next question or the basis of an earlier answer.

The first gain can be very small: one justified source allocation, one description comparison, a language relation that prevents a wrong continuation, or a localized reconstruction failure. An already sufficient source passage, MethodDescription or prior result is an ordinary exit. A language becomes worthwhile when maintaining these connected answers saves consequential repeated reconstruction; its existence alone establishes no such gain.

Several forces remain in tension: source fidelity and a usable synthesis; reusable knowledge and situation-specific judgment; enough preserved context and affordable reading; local repair and hidden cross-pattern dependence. The profile keeps serious alternatives visible. A direct description or small synthesis note may be cheaper. A stable source-processing sequence may be appropriate. Neither is excluded by the ability to unfold use under changing conditions.

### Production and situated use are different contributions

The production side engineers source-grounded Method-description knowledge in pattern-language form. ME.4 recovers documentary contributions; ME.21 reconciles and allocates them; ME.23 architects the useful language; ME.24 challenges promised coverage and localizes refresh. ME.5/ME.8 supply Method qualification and one-Method description content when needed. ME.22 is used when an actual revision question requires separating content and form.

The situated-use side, ME.20, starts from the result needed now and follows only a contribution whose conditions support that use. A practitioner can use a finished language without performing its production Method. An author can repair one allocation without enacting all other production actions. The profile connects these uses; it does not merge their subjects into one Method.

The profile account concerns this arrangement of knowledge and uses. Its material relations include a description relying on an allocated claim, a reconstruction finding returning to that allocation, an alternative description supplying the same receiving use, and a source change invalidating a dependent current-use premise. Those relations matter because they change what may be used or must be reconsidered. They are not merely hyperlinks or positions in the publication.

A body may describe one Method, part of a description, or a neighboring evidence or maintenance question. Several bodies can concern the same Method; one source contribution can support several bodies. A source chapter, pattern, action row or publication Part is not automatically a part Method. Use ME.5/ME.7 and B.1.5 for an actual whole-and-part claim. Real smaller Methods can be parts when the whole-forming relations support that account; a holonic interpretation is not supplied by layout alone.

### Production MethodDescription — Engineer a source-grounded MethodDescription in pattern-language form

The subject of this description is one reusable production Method: use role-qualified source contributions and current suppliers to engineer actionable Method-description knowledge as a pattern language, retain the grounds of its allocation, and challenge and refresh its promised source coverage. The result can contain several one-Method descriptions and neighboring contributions. Call that whole result one MethodDescription only when its exact subject and substantive claims satisfy A.3.2.

This production Method is treated as non-composite here: no part-Method set is established. The following actions and result dependencies explain its prospective performance; they are not an admitted decomposition into smaller Methods. The Method's identification does not establish that it has already succeeded in recurring production practice.

**Inputs and applicability.** Start with a named receiving practice and use, inspectable source contributions, their roles and limits, and the relevant current FPF/DPF supply. Documentary claims enter through ME.4. Observations, artifacts, logs and interviews about dated Work first require an A.3.1.MR recovery result; use ME.18 only for its remaining consequential evidence question. A returned candidate account retains rival explanations and gaps. If the receiving use or required source cannot be established, the first useful result is that exact blocker.

**Reusable action.** Select source depth by the question; recover source-local meaning; compare current supply and serious alternatives; reconcile the surviving contributions without inventing Method identities; allocate their useful claims; describe the needed Methods; organize independently useful pattern questions and material relations; then attempt the reconstruction the language promises. Preserve a direct-source remainder where it is sufficient and recoverable. Each action consumes only the results it actually needs. A missing condition can return the work to that question before the rest is complete.

**Source-profile variation.** Use the profile that matches each source and receiving claim:

| Source situation | Useful treatment and limit |
| --- | --- |
| A plural library or a serious current alternative may change what is worth recovering | Start with SoTA comparison, then recover the selected contributions deeply enough for their receiving use. |
| A maintained synthesis must remain reconstructable | Recover its action-bearing content source-locally before filtering against current supply. Complete recovery does not make every assertion normative. |
| A recoverable earlier comparison bounds the changed question | Inspect the gap and its dependents. Without that baseline or a defensible impact boundary, widen recovery. |
| A mixed corpus includes documentary sources and accounts of Work | Choose documentary depth per source; preserve separately returned Work accounts and their evidence limits. Keep source assertions about Work separate from recovered occurrence evidence and from Method admission. |

F.0.1/F.1/F.0.2 govern source meaning, selection and conceptual synthesis. ME.21 consumes their results for the Method-specific allocation: reuse current supply, add or amend the professional contribution, retain a direct-source or unresolved remainder, or return a genuinely general question to FPF. The useful output states what changed and why, rather than merely listing source destinations.

**Results and stops.** The complete result for the selected use is an actionable language with identifiable description subjects, conditions, material relations, recoverable source decisions and an affected-refresh route. A smaller completed allocation, comparison or reconstruction result can be used independently without claiming that the whole language is complete. Stop a dependent use when its required basis is missing; preserve independently supported results. Do not promise corpus-complete coverage from a sample or gap-only pass.

**Variation and identity.** Source order, source profiles, tools, reader entries and representations may vary while preserving this reusable action and its source/evidence discipline. A change to the whole action, required allocation and source-return discipline, language result, reconstruction obligation or dependency direction reopens the Method identity through ME.5/ME.15. Changing a description or publishing tool does not by itself create a Method variant.

**Enactment boundary.** A prospective action description is not a dated Work occurrence or a WorkPlan. An account of an actual production attempt identifies its performers, conditions, support and observed results. During ongoing Work, A.15.7 supplies a separate next-action decision that names the chooser and performer. ME.11 can obtain trial evidence; ME.13 and ME.14 separately judge transfer and worth. The constructed application below makes the description inspectable but does not supply those empirical results.

### Unfolding a use, including a changed situation

A practitioner recognizes the current difficulty, asks which result is missing and tests the conditions for the contribution that could supply it. An available earlier result may already suffice. New observations can change a current judgment, expose another missing result or make the present use stop. This is ordinary ME.20 use without an obligatory formal graph.

When a formal continuation answer is needed, A.22.CGUS supplies the stronger structural and case-judgment semantics. Identify its constituents, relations, constraints and use frame; preserve the difference between currently available, blocked and unknown continuations, including evaluation errors. A completed condition that does not satisfy a rule is not an unknown condition. A graph view alone supplies none of these judgments.

Changing facts within the same use frame requires a fresh applicable judgment. Changing the question, governing conditions or stop rule can require reidentifying the frame itself. Thus the situation is reconsiderable at each working move; its boundary is not mechanically reset after every action. Local order can still be required. The profile's acausal emphasis means that one global causal or calendar route is not prescribed in advance, not that causes, agents, planning or causal inquiry disappear.

This differs from relying on one up-front assembled method package, but it is not a claim that all earlier SME required that package. Intention-sensitive, evolutionary and continuous-composition lines already provide important alternatives. PLUS-ME's particular choice is the relation between source-grounded pattern knowledge, independently qualified Method semantics and situated result use.

### Worked connected application — H, L and W

This is a constructed application, not a report of completed empirical validation. A Method engineer wants a small language for reviewing and adapting a Method description.

Handbook H, edition 3, §4, supports reuse of an earlier review after a display-only change. Paper L, edition 1, §2, limits that reliance to matching reviewed claims, question and qualification window. A returned MR account W, version 2, reports that a team shortened a warning; it preserves two rival explanations, harmless redundancy and a missed condition. The new language must not turn that report into an admitted shortcut Method.

**First use.** ME.4 preserves H and L source-locally; W remains a separately returned candidate account. ME.21 reuses ME.12's existing coherence contribution and carries L's narrower condition into the description. Tool-specific layout instructions remain at H. The allocation produces a conditional reuse answer and an unresolved W remainder, not a new Method count.

If that one description settles the receiving use, ME.8 is sufficient and the engineer stops. For recurring allocation, review and source-return questions, ME.23 connects independently useful entries: the review relies on the allocated condition, and a missing coverage relation returns to the affected source decision. This arrangement does not establish three parts of a review Method.

ME.22 compares earlier prose A with revised prose B that adds the matching-condition and source-return stop, then compares B with a table C preserving those same claims. Merely comparing A with C could not separate the added content from the new presentation. Textual comparison can reveal that A lacks a needed stop. A claim that C helps readers more than B needs an appropriate comparison of their actual use; the table's appearance is not that evidence.

ME.24 reconstructs the promised reliance answer. A topic entry and source citation are insufficient if the condition cannot be recovered. Its first result names the missing condition or confirms recoverability only for this bounded case.

**Changed condition, supplied only after the first answer.** H becomes available only as excerpts. A new receiving use requires rechecking an argument outside them, and the retained allocation contains only its locator, not the argument. The recheck now has an unavailable basis. Return that dependent use to source recovery, use a separately justified sufficient basis, or narrow or stop it. Keep the earlier result with its historical basis, L's independently supported condition and W's unresolved status. Another pattern that copied the missing premise is affected even if its file did not change.

ME.20 continues from this newly missing result. If only source availability changed, reconsider the current judgment. If the reader instead asks whether publication is authorized, identify that new use and its required result. A prior review is not publication authorization. In actual Work, the chooser and performer remain explicit.

A useful answer to this case preserves the first action, condition and stop, distinguishes the three source roles, makes no invented part Method, and localizes reconsideration without losing another dependent use. A rehearsal of these answers tests the explanation. It does not measure production cost, human performance, transfer or causal superiority.

### Practical checks, recurring failures and costs

Recognition and assurance answer different questions. First identify the missing result and a plausible contribution. Then check only the claims on which the actual use relies, with the evidence and independence that their conclusion needs. Do not treat finding the right heading, obtaining a graph path or reading all patterns as assurance.

For a production result, ask whether the receiving action and stop are recoverable; whether sources and candidate evidence retain their roles; whether each merge, split and omission has a reason; whether the language keeps Method identity separate from body allocation; and whether a changed premise has an identifiable return. When the promised use spans several patterns, challenge at least the material relation on which that use depends. Broaden a check when the dependency boundary is unknown, not merely because the language is large.

The recurring failures have distinct repairs. A chapter copied as a Method returns to recovery and qualification. A tidy graph that loses a condition returns to description content. A comparison that changes both content and form returns a bundled result, not a form advantage. A coverage table that counts topics returns to reconstruction. A source-access failure stops a required new recheck; it does not retrospectively falsify everything derived from the source.

Source familiarity, preference for a neat architecture and enthusiasm for pattern languages can bias all these judgments. Preserve the rival account and the cheaper direct route. AI-assisted recovery or comparison retains its model, input and interaction limits when they matter to the claimed result; fluency does not replace source access or independent use evidence.

The practical benefit is reusable source decisions and more local reconsideration. The burden is additional initial reading and maintenance of the few dependencies needed for return. In one bounded comparison with two clean-context AI readers, both the full situated-use body and a truthful entry-only alternative supported the required continuation. After a changed condition, the full-body reader reused its return guidance without another source opening; the entry-only reader reconstructed that boundary from two further source passages. This is a local reconstruction benefit, not a measured total-effort, correctness or human-performance advantage. The full body also requires its upfront reading and maintenance. Whole-production effectiveness remains unestablished. Use a simpler account when maintaining the language does not repay its burden.

### Architectural Rationale and source comparison

Method Engineering keeps SME's situation dependence and deliberate construction of reusable ways of working. PLUS-ME changes neither premise. It selects one profile in which patterns expose problems, forces, actionable contributions and useful relations, while Method identity and composition remain separately governed. The reuse unit is therefore not indiscriminately a source slice: it can be an independently qualified smaller Method, a description contribution or a neighboring non-Method answer.

This explains the distinct production results. Recovery must remain faithful even when allocation later rejects a proposal. Description comparison must not be replaced by either a cross-use representation profile or a judgment of Method worth. Language architecture must make material relations useful without creating parthood. Reconstruction must be able to find a missing contribution before a contradictory maintained claim and its owner are already known. ME.4, ME.21, ME.22, ME.23 and ME.24 keep these differences actionable; none requires an obligatory pipeline.

The following sources supply specific questions and alternatives, not a proof that this profile is universally best:

| Source and role | Contribution and limit in this profile |
| --- | --- |
| Ralyté, Deneckère and Rolland, [generic SME and Map, 2003](https://doi.org/10.1007/3-540-45017-3_9) — historical anchor | On-the-fly construction and intention-sensitive navigation are prior art. Do not contrast PLUS-ME with an exclusively up-front history of SME. |
| Gottschalk et al., [continuous composition and enactment, 2022/2023](https://doi.org/10.1007/s10270-022-01018-9) — implemented contemporary alternative | Continuous situation-specific composition already joins construction with enactment. This profile changes the useful knowledge and return arrangement, not by itself its effectiveness. |
| Wilke et al., [Method Engineering review, 2024](https://doi.org/10.1016/j.procir.2024.06.001) | Diverse definitions and adaptation routes justify checking the live field before extraction. One database review does not settle a universal Method ontology. |
| Stacey et al., [Methods as engineering knowledge, 2025](https://doi.org/10.1017/dsj.2025.9) | Preserve use conditions and practitioner knowledge around procedural guidance. These questions do not automatically become mandatory fields or Method parts. |
| Doellken, Nelius and Matthiesen, [ACAP analysis, 2024](https://doi.org/10.1080/09544828.2024.2320018) | Distinguish attention, comprehension, application and performance in a description's use. The sheet-metal-design study does not establish a universal measure or isolate every content contribution. ME.22 adapts the distinction. |
| Veloso, Varajão and Moreira, [Method selection in information systems, 2026](https://doi.org/10.1007/s11301-026-00601-4) | Interacting project, team, organizational, Method and environment conditions can change selection. Their synthesis and focus groups do not establish PLUS-ME effectiveness. |

[Alexander et al.'s A Pattern Language (1977)](https://www.patternlanguage.com/bookstore/pattern-language.html) supplies the historical problem-first, connected-guidance idea. [Minsky's frame account (1974)](https://web.mit.edu/dxh/www/marvin/web.media.mit.edu/~minsky/papers/Frames/frames.html) connects situation knowledge, expectations and adaptation. The architectural analogy drawn here concerns those knowledge-use roles; historical descent of pattern languages from frame systems is not established by it. Declarative and case-management approaches, including [CMMN 1.1](https://www.omg.org/spec/CMMN/1.1/About-CMMN), remain operational comparison targets, not the ontology adopted by this language.

The selected alternative is a profile within Method Engineering because its general qualification, architecture, representation and assurance questions remain shared. A separate framework would need a different justified field promise. A prose-only synthesis remains a serious lower-maintenance option; a fixed route remains legitimate under stable conditions. Reopen the profile choice when current supply removes a distinct result, reconstruction fails for a promised use, source conditions change, or the maintenance burden defeats the practical gain.

### Relations and scope of the whole account

General Method Engineering remains directly available through ME.1–ME.19, with ME.22 available for non-pattern description comparisons. ME.20 supplies situated use; ME.21/ME.23/ME.24 add the production questions explained here. The documentary branch of ME.4 supplies both ordinary single-source and plural-source recovery.

FPF retains authority over Method and episteme identity, whole-forming relations, conceptual synthesis, representations, structures, CGUS, Work, evidence, next-action decisions and framework publication. An actual new general result returns to its FPF owner after professional and corpus-specific filling is removed. Local evidence can inform that return without making FPF normatively dependent on the local profile.

Professional and local profiles may specialize conditions, select use-bounded claims or reuse a contribution. These are different relations; overlap is not automatically a lattice and reuse does not merge identities. A formal mathematical or structural claim uses its applicable FPF governor. No sibling DPF, Guide corpus expansion or particular software tool is a prerequisite to an independently supported direct Method Engineering result.


# Part I - Method Focus, Architecture History, Repertoire, Situational Criteria, and Recovery

## ME.1 - Choose and Reopen the Project Method-of-Interest

>
> **Primary working result:** a **Method-focus result** that selects one Method, an established family or explicitly local grouping, a set of Method relations, or a non-Method return for one project decision. The result preserves every Method or candidate-account status and names one observation that would reopen the focus.

### ME.1:0 - Use This When

Use this pattern when a project says that its “methodology”, “process”, “workflow”, or “way of working” must change, but the decision subject is still ambiguous. The live concern may be one Method, several related Methods, an established Method family, a temporary comparison grouping, or something else such as a tool, capability, support arrangement, description, resource, or project System.

Begin with the result that is missing, late, unsafe, or too costly and the representative Work in which that result matters. Recover the Methods and candidate accounts already visible there before choosing the level of focus.

The first useful move is to compare four possible focus classes: one Method; an established family or project-local grouping; named Method relations; and a non-Method return. The practical gain is that later repertoire, qualification, or architecture Work receives the smallest subject it can act on without inventing a Method or a composite.

Do not use ME.1 merely because one tool failed, one practitioner lacks capability, one document is incomplete, or one project, process, or case view is inconvenient. Return that question to its direct subject unless changing a Method would change the receiving result.

### ME.1:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| Method | A reusable way of obtaining or preserving a result, identified under `A.3.1` for the relevant participant meanings, applicability, and limits. |
| candidate Method account | An episteme that states a possible reusable way of doing while one or more Method-identification conditions remain open. The account is not the Method. |
| established Method family | Identified Methods connected by an independently governed family classification or membership basis. Shared use or resemblance is insufficient. |
| project-local grouping | A temporary set of identified Methods and candidate accounts collected by a stated criterion for one comparison or selector use. Its label creates no family or membership fact. |
| Method-relation focus | Named Methods and candidate accounts plus the relation kinds whose truth could change the project decision. It need not contain a composite whole. |
| project, process, or case view | A description of Work produced from a viewpoint that foregrounds selected questions. Several such views can concern the same Work and do not create that Work or its Methods. |
| non-Method return | A result that redirects the decision to the actual subject, relation, and next useful question while naming what observation would reopen Method Engineering. |

### ME.1:1 - Problem Frame

Project teams encounter Methods through handbooks, standards, stage models, issue trackers, training, job titles, toolchains, and remembered practice. These can reveal useful Methods, but their visible boundaries rarely coincide with Method identity.

The same Work can also be described through project, process, and case viewpoints. One view may foreground deadlines and resource commitments, another recurring controls, and another the state and exceptions of one case. These views can reveal different Method questions. They describe the same Work; changing the view does not create another Work occurrence or Method.

### ME.1:2 - Problem

A focus chosen too broadly turns every artifact and supporting System into a Method part. A focus chosen too narrowly optimizes one operation while the receiving result still depends on several Methods or a support relation. A familiar label can also turn a project-local shortlist into an alleged professional family.

The project then asks the wrong downstream question. It builds a repertoire for a tool problem, qualifies a candidate account as though it were an identified Method, or compares “architectures” that are only differently drawn views of the same Work.

### ME.1:3 - Forces

| Force | Tension |
| --- | --- |
| Affordable entry | A project needs a quick focus, while Method identity and family membership cannot be assigned by convenience. |
| Several useful grains | One operation may be actionable, while relations among several Methods may control the result. |
| Familiar labels | Project, process, case, agile, model-based, or AI wording aids conversation, while it can hide the actual subject. |
| Established and local plurality | A maintained family can support reuse, while a local grouping can remain useful without pretending to be one. |
| Reopening | The first focus must guide action now, while new Work evidence may reveal a tool, capability, or relation problem instead. |

### ME.1:4 - Solution

Select the smallest focus class whose subject and status are supported and whose change could alter the receiving result. Keep the rejected focus options and one observable reopen condition in the result.

#### ME.1:4.1 - Pattern-Use Unfolding

1. **Name the receiving result and decision.** State the result at risk, who will use it, the relevant situation and interval, and what decision the focus will enable.
2. **Recover representative Work.** Identify the Work occurrence or intended Work that exposes the difficulty. Use `A.15.6` to keep the project System, use, Work, Method, support, and development subjects distinct.
3. **Inspect the views already in use.** For each project, process, case, lifecycle, stage, or workflow description, state its viewpoint, the questions it exposes, what it coarsens, and which same Work it describes.
4. **Recover Method-status candidates.** List Methods already identified under `A.3.1`, candidate Method accounts, established family facts, local groupings, related Methods, and support or capability alternatives. Preserve their statuses.
5. **Form materially different focus options.** Include each plausible one-Method, plurality, relation, and non-Method branch. A renamed package or differently drawn view is not another focus option.
6. **Test family and relation claims.** Use `G.5` for any maintained family or selector claim and the applicable relation pattern for each direct relation. When no identified whole and obtaining relations exist, retain a relation focus or local grouping rather than a composite.
7. **Choose and record.** Use `C.11` or a domain decision Method to select one focus for the receiving decision. State rejected options, evidence limits, next useful result, and the observation that reopens the focus.

#### ME.1:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use boundary | Receiving result and decision, situation, interval, project System or other subject, and decision authority when a choice is asserted. |
| representative Work | Actual or intended Work relevant to the decision, with its result and participant meanings. |
| views used | Each viewpoint and view, the Work described, question foregrounded, important loss, and whether it changes the focus. |
| Method-status inventory | Identified Methods, candidate accounts, established family facts, local groupings, related Methods, and non-Method alternatives. |
| options and choice | Four focus classes considered, selected class and subject, rejected options, basis, and unresolved claims. |
| continuation | Next result needed and one observable reopen condition. |

#### ME.1:4.3 - What Changes in Practice

The project stops asking which named methodology should replace another. It first decides whether the live subject is one Method, a governed family or local grouping, relations among several Methods, or a non-Method condition. Downstream Work becomes smaller, and a useful plurality can remain plural without being packaged as a fictitious composite.

### ME.1:5 - Archetypal Grounding — EC-417 Release Focus

In the EC-417 release scenario, eight of twenty releases reopened. The package is commonly called the “release methodology”, so the first proposal is to replace it as one Method.

Three existing views describe the same release Work:

| Viewpoint and view | Question exposed | Boundary |
| --- | --- | --- |
| project view | Whether provisional integration at `D-21` and signed evidence at `D-8` can reach `D0` with available people and rig time | Its schedule positions do not identify Methods. |
| process view | Which evidence checks, approvals, and stops recur | Repeated descriptions do not create one process-Method or whole. |
| case view | Which evidence, mismatch, exception, and authority state belongs to one release | The case description is not the Work or a Method. |

The status inventory contains four identified Methods: `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, and `M-Release-Authorize`. It also contains candidate accounts `C-Evidence-Reconcile-Internal`, `C-Evidence-Reconcile-Supplier`, and `C-AI-Trace-Review`. `C-EC-Release-v2` is only a proposed-whole account. The PLM, CI, test rig, AI provider, safety capability, and supplier responsibility are support, System, capability, access, or assignment subjects rather than Method candidates by position.

| Focus option | Result |
| --- | --- |
| one Method: `C-EC-Release-v2` | rejected because the whole is not identified as a Method |
| established release-Method family | rejected because no governed family membership is supplied |
| project-local `LG-EC417-ReleaseMethods` grouping | retained only as a comparison locator; no family claim |
| candidate account: `C-AI-Trace-Review` | not selected as the current focus because its bounded trace suggestions govern neither evidence reconciliation nor release authority; candidate-account status is preserved |
| relations among the four Methods and two reconciliation accounts | selected because evidence timing, result use, allocation, and authority relations change the release decision |
| test-rig support decision | retained as a rival non-Method return, but current evidence does not make it the sole focus |

The first result is therefore a Method-relation focus. It creates no fifth Method and no composite. Reopen to a test-capability focus if two of the next three comparable delays occur while required evidence is complete and the rig is unavailable.

### ME.1:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| package bias | The boundary of a standard, methodology, or tool suite becomes one Method boundary. | Recover the receiving result, Work, Methods, accounts, and support subjects before choosing focus. |
| management-view bias | Project, process, or case descriptions become competing kinds of Work or Methods. | State the viewpoint and keep all applicable views connected to the same Work. |
| family-language bias | A local shortlist is presented as an established professional family. | Name its criterion and bounded use and retain unresolved family status. |
| composite bias | Co-use of several Methods becomes a whole Method. | Select a relation focus until whole identity and obtaining relations are separately supported. |

### ME.1:7 - Conformance Checklist

- [ ] The opening names a receiving result, representative Work, and current decision.
- [ ] Every Method and candidate account keeps its prior status.
- [ ] An established family cites an independent classification or membership basis.
- [ ] A project-local grouping states its criterion, use, and non-family status.
- [ ] Project, process, and case views name their viewpoints and the same Work they describe.
- [ ] The options include a non-Method return whenever a tool, capability, support arrangement, description, resource, or System could be decisive.
- [ ] The selected focus states rejected focus options, uncertainty, next useful result, and an observable reopen condition.
- [ ] No package position, view, or shared use creates a Method, family, relation, or composite.

### ME.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The process failed, so change the Method.” | Identify the result, Work, view, Method, and non-Method conditions before selecting the subject. |
| “These methods are our family.” | Use a local grouping unless governed membership is independently established. |
| “The tracker shows the real process.” | Treat the tracker content as a case, project, or process view with stated coverage and loss. |
| “Several contributors imply one composite.” | Return a Method-relation focus and send a proposed whole to ME.7 only when that later question is live. |
| “Choose the smallest item.” | Choose the smallest *decision-changing* subject, which may be a relation focus rather than one operation. |

### ME.1:9 - Consequences

Method Engineering begins with a decision-usable subject instead of a fashionable label. Later repertoire and criteria Work can remain narrow, while a relation focus exposes genuine coordination questions without pre-committing to a whole.

The cost is a short recovery of Work, views, statuses, and non-Method alternatives. Some projects will stop before Method Engineering because the useful answer concerns a support System, capability, description, or resource.

### ME.1:10 - Rationale

The focus determines which claims are admissible in later Method use. Preserving the difference among a Method, family, local grouping, relation focus, and non-Method subject prevents downstream qualification or architecture prose from silently upgrading an unsupported object.

R7 supplies a connected Method/Work/description/capability/tool synthesis. R10 supplies the sharper example that project, process, and case management can be viewpoints on the same Work. ME.1 retains both contributions by using views to discover questions while grounding focus in the actual subjects and relations.

### ME.1:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.15.6`, `C.11`, `A.3.1`, and `G.5` | Project-relative subject recovery, bounded choice, Method identity, and family/selector discipline. | These patterns do not choose the Method Engineering focus for the project. |
| R7 Methodology guide, especially R7.2 and R7.5 | Connected treatment of Method, Work, descriptions, mastery, tools, variants, and Method change. | Maintained synthesis supplies questions and examples, not current project identity evidence. |
| R10 Systems Management, R10.7:1–2 | Project, process, and case management as different viewpoints and views on Work. | A view can expose a question but does not create Work or a Method. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Method-ecosystem and element distinctions that help locate a candidate focus. | Source elements are prompts, not FPF kinds or Method parts. |
| Bender, [embedded-analytics process selection](https://doi.org/10.1007/s10257-024-00675-1) | Current context-specific selection evidence. | One application population does not establish a universal focus taxonomy. |

Reopen the affected rule when a current source or representative use exposes another materially different focus class, or when project/process/case views cannot preserve one Work while revealing the needed Method questions.

### ME.1:12 - Relations

- `A.15.6` distinguishes project subjects and routes a Method-of-interest question here.
- `A.3.1` governs Method identity; `G.5` governs maintained family and selector results; `C.11` governs the bounded focus choice.
- ME.2 may organize a repertoire for a one-Method, plurality, or relation focus. ME.3 may state criteria at that same level of focus.
- ME.5 receives identified Methods and candidate accounts without changing their status. ME.6 receives a several-structure question; ME.7 receives one proposed whole only when that question is live.
- ME.19 may explain an identified Method, established family inclusion, or named relations. A local grouping label is not its explanandum.

### ME.1:End

## ME.19 - Recover Why and How a Professional Method Architecture Differentiated

>
> **Primary working result:** a **differentiation account** with a dated sequence, named pressure/response/variation/selection links, serious rivals, diagnostic observations, and graded claims. When a receiving decision needs causal reliance, ME.19 also returns one separate `C.28` causal-use support result; the downstream architecture decision remains a third episteme.

### ME.19:0 - Use This When

Use this pattern when an identified Method, independently established family inclusion, or named relations among Methods are treated as natural or inevitable and a present decision depends on how that differentiation arose. Typical questions concern why a variant appeared, why one contribution separated from another, why a provider or profession retained a form, or why a relation changed under pressure.

Begin by bounding the exact Method, established family inclusion, or relation change to explain and the decision that will use the account. Decide immediately whether the receiver needs only a dated descriptive account or intends to rely on a causal conclusion.

The first useful result can be a descriptive stop: a dated sequence with source and evidence limits. When causal reliance is live, name the causal-use question, claim kind, causality-ladder rung, and required support before constructing the explanation.

Do not use a project-local grouping label as a professional-family fact. Do not use ME.19 for decorative history, chronology, popularity ranking, or present architecture choice alone.

### ME.19:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| explanandum | One identified Method, established family inclusion, or named Method relation and the differentiation that the present decision needs explained. |
| differentiation account | An episteme containing dated description, link claims, rivals, diagnostic observations, grades, limits, and reopen conditions. It does not select today's architecture. |
| descriptive sequence | Dated source editions, Work evidence, variants, disappearances, and decision points with no causal-use claim. |
| link claim | A proposed relation among pressure or environmental change, affected actor or carrier, response or variation, selection/retention, and Method or relation change. |
| rival | A materially different account such as constraint, provider/tool availability, regulation, authority, diffusion/fashion, recording artifact, redesign, or survivorship bias. Rivals may coincide. |
| causal-use support result | A separate `C.28` result that states the question, claim kind, rung, actual support-component refs, threat screen, verdict, supported/unsupported uses, limits/window, and reopen. |
| non-causal observation or hypothesis | A separately named descriptive result that may justify a bounded probe without licensing a causal claim. |
| downstream architecture decision | A separate authorized choice that cites only support allowed by the causal verdict and keeps its own criteria, authority, stops, and burden. |

### ME.19:1 - Problem Frame

Professional Method histories combine source editions, institutions, tools, regulation, local Work, deliberate redesign, diffusion, fashion, retention, and loss. R7's evolutionary language usefully prompts questions about variants and selection. Process-tracing research adds discipline for within-case sequence, rivals, and diagnostic observations.

For causal reliance on either contribution, use C.28. A plausible sequence can support description and hypothesis while leaving an interventional claim unsupported. The pattern therefore separates differentiation, causal support, and current choice.

### ME.19:2 - Problem

Chronology is often narrated as cause: a pressure appears, a practice changes, and the account says “therefore”. Search frequency or institutional prominence is treated as adoption evidence. Surviving versions hide abandoned variants. A project-local label is promoted into a professional family.

The downstream decision then consumes a causal premise that no identified result supports, or a useful descriptive account is discarded because it cannot prove causality.

### ME.19:3 - Forces

| Force | Tension |
| --- | --- |
| Useful history | Dated differentiation can expose alternatives and assumptions, while decorative chronology adds no decision value. |
| Diagnostic depth | Within-case observations can discriminate rivals, while narrative confidence does not supply identification or estimation. |
| Evolutionary language | Variation, selection, retention, and loss organize inquiry, while analogy can overstate causal mechanism. |
| Causal cost | Some decisions need causal reliance, while many can stop with description or a non-causal trial hypothesis. |
| Present authority | History can inform a choice, while it neither selects today's architecture nor grants decision authority. |

### ME.19:4 - Solution

Recover dated differentiation and rivals first. Apply the full `C.28` causal-use assessment only when another decision needs a causal conclusion, and return every result with its own identity and use limit.

#### ME.19:4.1 - Pattern-Use Unfolding

1. **Bound the explanandum.** Identify one Method under `A.3.1`, an independently established family inclusion, or named Method relations and the differentiation to explain. A local grouping can supply candidates and questions, not the family fact.
2. **Name causal use or choose a descriptive stop.** State the receiver's exact question. If causal reliance is needed, name `CausalUseClaimKind`, target `CausalityLadderRung`, comparator or intervention where applicable, and the link claims. Otherwise return dated description without causal vocabulary.
3. **Establish the dated descriptive sequence.** Recover source editions, Work evidence, variant appearances and disappearances, abandoned forms, and decision points. A timeline is an index, not an explanation.
4. **Propose explicit link claims.** Name the pressure or environmental change, affected actor or carrier, response or variation, selection or retention process, and resulting Method or relation change. Use *mechanism* only in a source-local sense unless an `A.6.1` `U.Mechanism` is separately identified.
5. **Generate serious rivals.** Include at least one demand or constraint account and applicable provider/tool, regulation, authority, diffusion/fashion, recording-artifact, deliberate-redesign, or survivorship accounts.
6. **Derive and collect diagnostic observations.** Before choosing observations that are easy to collect, state which dated records, version differences, decisions, Work evidence, interviews, abandoned variants, negative cases, or cross-setting contrasts are expected under each link and rival. Preserve provenance and independence. Grade observations without making the whole chain certain.
7. **Run the complete `C.28` boundary when needed.** Issue one identifiable support result with question ref, claim kind, rung, actual evidence-path/data-regime and specialist-result refs, common-threat-screen ref, verdict, supported/unsupported causal uses, limits/window, and reopen. Raw observations or source names are not support-component results. A missing identification, bound, or estimate required for this named causal-use question, or an unresolved live threat to that use, lowers the verdict. Do not commission an estimate merely because another kind of causal question would need one.
8. **Return distinguishable results.** Grade differentiation claims as observed, source-supported, inferred, expert-estimated, contradicted, or missing and retain rivals. Keep the causal result separate. A downstream choice cites only causal reliance allowed by the verdict and retains its own authority. An `unsupported` or `undecided` result may not serve as positive causal evidence; a separately named non-causal observation or hypothesis may still support a bounded trial.

#### ME.19:4.2 - Record the Results

| Result | Required content |
| --- | --- |
| differentiation account | Explanandum, dated sequence, source editions and Work evidence, link claims, rivals, diagnostic observations, grades, limits, and reopen. |
| optional causal-use support result | Question ref, claim kind, rung, actual support-component refs, threat-screen ref, verdict, supported/unsupported uses, limits/evidence window, and reopen. |
| optional non-causal observation or hypothesis | Separate identity, descriptive basis, bounded design use, inferences this result does not support, and reopen. |
| downstream handoff | The result and its allowed use supplied to another decision, which retains its own authority. |

#### ME.19:4.3 - What Changes in Practice

Practitioners can use history without turning it into inevitability. A dated account can reveal forgotten variants and serious rivals; a causal stop can prevent unsupported reliance; and a current architecture decision can still authorize a reversible probe from a separate non-causal observation.

### ME.19:5 - Archetypal Grounding

#### ME.19:5.1 - Descriptive Stop

This is a constructed design-office history, not a report about a real organization. The office must reconcile names and source editions after drawing signoff differentiated. For this case, independent A.3.1 identification and ME.15 variant qualification have already established common Method `M-Signoff-0` and local variants `M-Signoff-E` and `M-Signoff-M`. All return approve/reject for a drawing, but the electrical variant requires clearance and harness-revision checks, while the mechanical variant requires load-case and fit checks; each withholds approval when its required check is absent. Those reusable differences are not inferred from separate form names. No professional-family or composite-Method claim is made.

The explanandum is this local differentiation and its documented timing. The receiver needs to distinguish the introduction of the different checks from their later representation in separate electronic forms. It does not need a claim that one pressure caused the split or that either variant is better.

The case premises also admit `ElectricalReviewer-E` and `MechanicalReviewer-M` as Agents for their respective checking under A.13, and their 9 and 18 April occurrences `WE7` and `WM4` as Work under A.15.1. The Work enacts `M-Signoff-E` and `M-Signoff-M`, respectively; E1 and M1 are the instructions used, not the enacted Methods. The bounded source set contains these case facts:

| Date and source | Recoverable fact and limit |
| --- | --- |
| 15 January 2024, signoff instruction S3 | One common signoff account covers both drawing types and checks that required evidence is present. S3 contains neither variant's distinct test-and-withhold rule. A source omission alone does not prove that nobody already performed such checks. |
| 4 March, exception log X2; 11 March, proposal P1 | X2 records two returned drawings, one lacking an electrical-clearance check and one lacking the mechanical load case. P1 cites these exceptions and proposes the two domain-specific rules. It also retains the alternative of common signoff with expert escalation; the record does not show that the exceptions alone determined the choice. |
| 2 April, approval A14 and instructions E1/M1 | A14 approves the two local variants for their respective drawing types. E1 and M1 state the different required checks and failure returns. The common-with-escalation proposal is not selected in A14, but the deliberation minutes are missing. |
| 9 and 18 April, signoff Work WE7/WM4 and their annotated results | ElectricalReviewer-E follows E1 in WE7 and withholds approval for missing clearance evidence; MechanicalReviewer-M follows M1 in WM4 and withholds it for a missing load case. The records support these two enactments before electronic-form separation, not population-wide use or the first-ever occurrences. |
| 6 May, PLM migration note T2 and form edition F2 | Separate electronic forms and approval-record names are introduced. T2 says they carry the existing E1/M1 rules. It supplies no new variant semantics and no evidence that the forms caused earlier Work. |

Before inspecting the April records, the office has two serious explanations. **R-demand** says domain-specific omissions prompted the proposal and selection of different rules; it predicts a problem record, a response proposal, and distinct checks before the form migration. **R-carrier** says the apparent split is only a naming or recording effect of that migration; it predicts unchanged checks beneath the new names. R-carrier is initially plausible because the searchable PLM history starts with F2 and makes the split look like a May event.

Comparing E1/M1 and WE7/WM4 with S3 and T2 is diagnostic: different reusable checks and their enactments are recorded in April, before F2. This contradicts R-carrier's strong claim that only names changed in May. It fits R-demand, but the missing deliberation minutes and absence of a comparable office without those exceptions prevent treating the complete demand–selection link as established causality. A weaker carrier contribution to later retention remains possible and untested; rejecting the naming-only account does not prove its rival.

`DA-Signoff-Differentiation-1` returns these grades and limits:

| Claim | Grade and allowed use |
| --- | --- |
| The common and domain-specific instructions differ in the named required checks and stops. | **Source-supported** by S3/E1/M1; Method identity and variant qualification remain the separate case premises. |
| Separate rules were approved by 2 April and enacted in the two named April Work occurrences. | **Source-supported** by A14 and WE7/WM4. This is a documented bound, not an exact origin date or evidence of universal uptake. |
| The March exceptions were a stated reason for proposing the variants. | **Source-supported** by P1; that stated reason is not a causal-effect result. |
| The split was merely a May renaming with no earlier semantic difference. | **Contradicted** by the April instructions and Work records. |
| Demand caused selection over common signoff with escalation, or the carrier caused later retention. | **Missing causal support**; retain the distinct hypotheses and missing deliberation/continuation evidence. |

The receiving source-reconciliation decision can now keep E1 and M1 as different variant descriptions, keep S3 as the common predecessor account, and link F2 as their later form without dating Method differentiation from form creation. It leaves the exact first occurrence and reasons for selection unresolved. No `C.28` result is created because no causal reliance is taken. Reopen the relevant date, relation, or link claim if an earlier instruction, the missing deliberation record, or contrary Work evidence appears; do not choose today's architecture from this history alone.

#### ME.19:5.2 - Causal-Use Branch and Non-Causal ME.6 Consumption

The EC-417 release scenario records a cadence/evidence mismatch near several reopenings. Four result identities remain separate:

- `DA-EC417-CadenceDifferentiation-1` is a partial descriptive account: the retained co-occurrences do not fill the dates, variants, and selection history needed for a complete differentiation account;
- `CUR-EC417-CadenceEffect-1` is the causal-use support result;
- `DC-EC417-CadenceMismatch-1` is a non-causal timing/co-occurrence hypothesis; and
- `AD-EC417-B2-Trial-1` is the receiving ME.6 architecture decision.

The causal-use question `CUQ-EC417-CadenceEffect-1` asks: “Would entering provisional-evidence reconciliation at `D-21`, rather than waiting for signed evidence at `D-8`, reduce mismatch-related reopenings in EC-417-like releases for this team, supplier, and change class?” Its `causalUseClaimKind` is `causalEffectClaim`; its target rung is `interventionalActionRung`.

The actual support-component refs are `evidencePathRefs=[EP-EC417-BundleSequence-20, EP-EC417-RigAvailability-20, EP-EC417-QuarterlyCadence-2]` and `empiricalDataRegimeRefs=[EDR-EC417-NaturalReleaseHistory]`. No identification or estimate result exists.

Common threat screen `CTS-EC417-CadenceEffect-1` records:

| Threat-screen field | Result |
| --- | --- |
| `causalUseQuestionRef` | `CUQ-EC417-CadenceEffect-1` |
| `interventionWellDefinedOrConsistency` | `liveThreat` |
| `temporalOrdering` | `clear` |
| `exchangeabilityOrConfounding` | `liveThreat` |
| `positivityOrOverlap` | `liveThreat` |
| `interferenceOrSpillover` | `liveThreat` |
| `selectionCensoringOrMissingness` | `liveThreat` |
| `measurementErrorOrConstructShift` | `liveThreat` |
| `transportToTarget` | `liveThreat` |
| `routedThreatRefs` | `[]` |
| `resultingSupportBoundary` | `unsupported` |

Every live threat lowers the causal-support verdict because no specialist result closes it. The C.28 verdict is `unsupported`. `supportedUse`: no interventional causal reliance; use this result only as a stop against that reliance. `unsupportedUse`: claiming that cadence mismatch caused the reopenings or that B2 will reduce them. The evidence window is the named twenty releases and two earlier cases for this team, supplier, and change class. Reopen only on a governed comparison or replayable identification or bound that varies reconciliation timing while rig, approver capacity, outcome definition, and evidence access are controlled or explicitly modeled.

`DC-EC417-CadenceMismatch-1` separately retains only the observed timing/co-occurrence as a trial hypothesis and design constraint. `AD-EC417-B2-Trial-1` consumes that non-causal result, capacity, confidentiality, authority, and reversibility to select only a bounded B2 trial. `SafetyReviewer-17` performs `W-SafetyEvidenceDecision-17` under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17` for the evidence-condition result; `ReleaseDecider-17` separately performs `W-ReleaseDecision-17` under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17` for branch entry and release disposition. The architecture decision does not cite `CUR-EC417-CadenceEffect-1` as positive causal evidence.

### ME.19:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| chronology bias | Earlier and later events become cause and effect. | Return the descriptive sequence first and open C.28 only for a named causal use. |
| survival bias | Current variants hide abandoned or excluded alternatives. | Seek abandoned variants, negative cases, and source gaps before grading links. |
| fashion-metric bias | publication count, search frequency, or institutional promotion becomes adoption or effectiveness evidence. | Treat it as a possible diffusion indicator with scope and rivals, not a causal result. |
| family-label bias | A local grouping becomes a professional family explanandum. | Require independent family membership or explain named Methods and relations instead. |
| history-authority bias | A differentiation account chooses today's architecture. | Keep current decision criteria, authority, causal boundary, and trial stops in the downstream pattern. |

### ME.19:7 - Conformance Checklist

- [ ] The explanandum is an identified Method, established family inclusion, or named Method relation change.
- [ ] The receiving decision and exact causal use or descriptive stop are explicit.
- [ ] The dated sequence precedes explanation and keeps source editions, Work evidence, variants, disappearances, and decision points recoverable.
- [ ] Every link claim names pressure/change, affected actor or carrier, response/variation, selection/retention, and resulting Method or relation change.
- [ ] Serious rivals and diagnostic observations are derived before convenient collection.
- [ ] Differentiation claims carry grades and limits.
- [ ] Any causal-use result contains the complete current `C.28` identity, support, threat, verdict, use, window, and reopen fields.
- [ ] Raw observations and source names are not presented as specialist support results.
- [ ] Differentiation, causal support, non-causal hypothesis, and downstream architecture decision remain separate.
- [ ] An `unsupported` or `undecided` result supplies no positive causal premise.

### ME.19:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The pressure came first, so it caused the Method change.” | State a link claim, rivals, diagnostic observations, and the C.28 result required by the receiving use. |
| “The timeline is the explanation.” | Treat it as an index and test explicit links and rivals. |
| “Process tracing proves the causal effect.” | Use it for within-case diagnosis; apply C.28 for the named causal use and lower the verdict when identification, a bound, or estimation required for that use is missing. |
| “Unsupported means the history is useless.” | Retain descriptive sequence and a separately named non-causal hypothesis within their use boundaries. |
| “The history tells us what to implement.” | Send bounded results to a separate authorized architecture decision. |

### ME.19:9 - Consequences

Professional Method history becomes decision-usable without being made causally stronger than its evidence. Forgotten variants and rivals remain available, while current architecture choices can distinguish causal reliance from a reversible probe based on non-causal observations.

The cost is explicit result separation and threat screening. Some elegant origin stories will end as descriptive accounts, and some causal questions will remain unsupported until a stronger design or bound exists.

### ME.19:10 - Rationale

Differentiation history, causal support, and present choice have different subjects and truth conditions. A dated sequence can be accurate while its causal explanation is unsupported; an unsupported causal claim can coexist with a useful non-causal design constraint; and neither supplies present authority.

R7's evolutionary synthesis is retained as a connected source of variant, transmission, fashion, retention, and loss questions. Process-tracing sources strengthen rival and diagnostic-observation discipline. C.28 states what support a causal use needs, keeping a plausible narrative separate from identification or estimation.

### ME.19:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| R7 Methodology guide, especially R7.5:15 and R7.5:19 | Variant generation, transmission, fashion, retention, loss, and evolutionary prompts. | Analogies and search-frequency examples generate hypotheses and rivals; they are not diagnostic or causal evidence. |
| Stacey et al., [Methods as a form of engineering knowledge](https://doi.org/10.1017/dsj.2025.9) | Attention to Method knowledge, variation, loss, and engineering context. | Conceptual history supplies no project causal verdict or current architecture authority. |
| Collier, [Understanding Process Tracing](https://doi.org/10.1017/S1049096511001429) | Within-case descriptive sequencing, rivals, and diagnostic observations. | Does not replace identification, estimation, transport, or FPF ontology. |
| Mahoney, [The Logic of Process Tracing Tests](https://doi.org/10.1177/0049124112437709) | Weak, necessary-condition, and strongly discriminating test logic. | Grades observations; it does not make the whole chain certain. |
| Current FPF `C.28` | Causal-use question, rung, support components, common threat screen, verdict, use boundary, limits, and reopen. | C.28 states evidence support only; downstream choice and authority remain separate. |

Reopen when a current source changes the diagnostic logic or causal-use rules, when a representative history cannot keep differentiation and causal support separate, or when a downstream use repeatedly needs a missing result field.

### ME.19:12 - Relations

- `A.3.1` governs Method identity; `G.5` governs established family or selector claims; a local grouping label supplies neither.
- `A.10` governs source and evidence paths; `C.27` governs temporal-claim adequacy; `C.28` governs causal-use support.
- ME.2 may retain variants and lineages without inheriting causal truth.
- ME.6 may consume the differentiation account, causal-use verdict, or separately named non-causal observation only within each result's use boundary and keeps its own authority.
- Cultural continuation and professional-history uses remain separate from one current project architecture decision.

### ME.19:End

## ME.2 - Recover a Reusable Method Repertoire and Its Lineages

>
> **Primary working result:** one **inspectable Method repertoire for a named use** that keeps identified Methods, candidate Method accounts, MethodDescriptions, source contributions, family or local-grouping claims, variants, supported lineage relations, evidence limits, source editions, and missing positions distinct.

### ME.2:0 - Use This When

Use this pattern when a one-Method, plurality, or Method-relation focus needs alternatives, variants, evidence, and provenance that another practitioner can inspect and reuse. Typical uses include comparing several Methods, forming a project proposal, locating a variant, or checking whether a familiar source contribution still supports the current question.

Begin with the named comparison or proposal use, the focus result or equivalent subject statement, and the practical result the project needs. Search primary Method Engineering sources and sources from the practice that owns that result. Keep exact editions and status visible while assembling the smallest repertoire that can support the use.

The first useful result is a set of status-preserving entries with claim-bearing source material, supported relations, evidence limits, currentness, and explicit missing positions. An honest gap is part of the repertoire when it changes comparison or proposal work.

Do not treat a bibliography, repository, package outline, observed Work, or list of popular names as a Method repertoire by itself. Co-listing supplies neither Method identity nor an established family, and documented lineage supplies neither superiority, causation, composition, nor present applicability.

### ME.2:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| named-use repertoire | The smallest inspectable result that exposes subjects, statuses, claim-bearing sources, relations, limits, and gaps for one comparison or proposal use. It is not every item in a repository. |
| identified Method | A reusable world-side way of doing already identified under `A.3.1`. Repertoire inclusion does not repeat or strengthen that identity. |
| candidate Method account | A provisional claim-bearing episteme about a possible Method. Repertoire inclusion preserves its unresolved identity conditions. |
| MethodDescription | A description of one already identified Method under `A.3.2`, kept distinct from that Method, candidate accounts, and Work occurrences. |
| source contribution | The exact claim, distinction, procedure cue, evidence item, or representation taken from a named source edition for the current use, together with its limit. |
| established family relation | A classification or membership relation supported under its independent governor. A family label or repertoire row does not establish it. |
| project-local grouping | A named set assembled for one local comparison or selector use, with its criterion and unresolved family status explicit. |
| variant claim | A claim that two practices, accounts, descriptions, or editions differ in a named way. Calling them variants does not decide whether they are the same Method. |
| supported lineage relation | A source-backed relation such as edition succession, documented derivation, adoption, or adaptation between exact subjects. It records provenance, not causal effect or merit. |
| missing position | A subject, relation, edition, evidence item, or provenance link needed by the named use but not currently supported. |

### ME.2:1 - Problem Frame

A project rarely receives a clean inventory of Methods. It receives old procedure editions, package sections, conference descriptions, local checklists, tool configurations, retrospective accounts, and claims that one practice “came from” another. The most familiar names can hide the best-supported contribution, while a well-stocked repository can hide a decisive gap.

Method Engineering sources encourage reuse from method bases and situational construction. Engineering-design sources add intended use, representation, procedure, tool, and ecosystem questions. Those source lines improve search and recovery, but their local elements are not automatically FPF kinds. The repertoire must therefore preserve what each source actually contributes while keeping Method, account, description, Work, family, grouping, and lineage claims separate.

### ME.2:2 - Problem

Three shortcuts make a repertoire unusable. First, every package item is called a Method. Second, co-listing or a common ancestor is called an established Method family. Third, the newest source edition silently replaces older evidence even when the current use still relies on an earlier claim or the changed edition has not been checked.

The resulting list appears complete but cannot answer which alternatives are identified Methods, which are only accounts, why a relation is believed, what changed between editions, or which missing position blocks the next decision.

### ME.2:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse | A repertoire should save future search, while a universal catalogue accumulates irrelevant and stale entries. |
| Breadth | Important alternatives may sit outside Method Engineering literature, while undirected collection becomes a bibliography. |
| Stable reference | Exact identities and editions aid replay, while practices and descriptions continue to change. |
| Lineage | Provenance explains where a contribution came from, while ancestry is easily overread as causation, quality, or family membership. |
| Honest incompleteness | Missing positions should remain visible, while teams are tempted to fill them with plausible names or inferred relations. |
| Local comparison | A temporary grouping can make a decision tractable, while its label can be mistaken for a world-side family. |

### ME.2:4 - Solution

Build the repertoire around one receiving use. Recover exact subjects and source contributions, qualify every relation by its own evidence, and record unsupported positions as gaps instead of filling them with guesses.

Recognition is cheap: a source or repository entry is worth inspecting when it may supply a relevant alternative, contribution, or missing relation. Assurance begins only when a decision relies on the row; then its subject status, exact source edition, evidence, relation basis, currentness, and limit must support that use.

#### ME.2:4.1 - Pattern-Use Unfolding

1. **Bind the repertoire use.** Name the focus, receiving result, decision, situation family, and what the next comparison or proposal must inspect. State what would make an entry relevant.
2. **Search both source lines.** Search primary Method Engineering sources for reusable approaches and source organization, and search the problem-owning practice for Methods, accounts, variants, evidence, and current operating constraints. Record exact source editions or dates and the claim-bearing passages or artifacts used.
3. **Recover subjects before grouping them.** Cite the existing `A.3.1` identity result for every identified Method. Keep provisional material as a candidate Method account. Attach a MethodDescription only to its already identified Method. Keep tools, roles, capabilities, support arrangements, evidence, and Work occurrences under their actual kinds.
4. **Extract contributions with limits.** For every useful source, state the contribution used, the subject it concerns, its evidence or status, its scope, and what it does not establish. A package position or source vocabulary does not determine the FPF kind.
5. **Record relations independently.** Separate established family membership, project-local grouping, variant claims, input/result relations, and supported lineage relations. For lineage, name both exact subjects, the relation claimed, and the source that supports it. Leave same-Method identity, causal effect, superiority, and composition open unless their own governors settle them.
6. **Pin editions and currentness.** Distinguish the publication or artifact edition from the current project's decision to rely on it. Note supersession, changed meaning, evidence windows, and the observation that requires refresh. Use a broader `G.2` SoTA pack only when the use needs refreshable multi-source synthesis rather than a small question-relative source set.
7. **Expose missing positions.** List absent alternatives, unknown editions, unsupported ancestry, missing evidence, unresolved family status, and contributions whose source meaning cannot yet be recovered. Say which next use each gap blocks or merely weakens.
8. **Return the bounded repertoire.** Publish the subject inventory, source-contribution rows, relation rows, currentness limits, and gaps for the named use. Stop when the next decision can inspect the live alternatives and uncertainties without guessing their status.

#### ME.2:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| repertoire use | Focus, receiving result, situation family, consuming comparison or proposal, relevance criterion, and scope. |
| subject inventory | Exact Method identities, candidate-account refs, MethodDescription refs, and unlike supporting subjects kept outside the Method rows. |
| source contributions | Exact source/artifact edition, claim-bearing contribution, subject, evidence/status, scope, and limit. |
| relations | Established family basis if any, local grouping criterion, variant claims, supported lineage relations, and other decision-bearing relations with truth status. |
| currentness | Publication/artifact edition, current reliance window, supersession or change cue, and refresh observation. |
| missing positions | Missing subject, provenance, relation, edition, evidence, or source meaning and its effect on the named use. |
| stop and next use | What the repertoire supports now, what it does not establish, and which gap or source change reopens it. |

#### ME.2:4.3 - What Changes in Practice

Teams stop searching a repository as though every file were a reusable Method. They can compare identified Methods alongside promising accounts without promoting either, trace a proposal to exact contributions without asserting composition, and stop with a useful gap instead of inventing a complete lineage.

### ME.2:5 - Archetypal Grounding — EC-417 Release-Evidence Repertoire

The EC-417 project needs an inspectable repertoire for a Method-relation comparison around one safety-relevant controller release. The relevance criterion is narrow: an entry must contribute to verification, integration, supplier evidence, release authority, or evidence reconciliation for the named receiving result. The following identifiers and editions are local scenario records; they are not population evidence.

| Subject and status | Claim-bearing basis and edition | Supported relations or lineage | Use limit or missing position |
| --- | --- | --- | --- |
| `M-HW-Verify`, identified Method | existing `A.3.1` identity result; hardware-verification procedure `HV-6`; EC-417 verification records | its verification result is an established input to release authorization for this use | no supported lineage to another Method and no general effectiveness claim beyond the cited use window |
| `M-SW-Integrate`, identified Method | existing `A.3.1` identity result; firmware-integration procedure `FI-4.8`; integration records | description edition `FI-4.8` succeeds `FI-4.7`; this is document-edition lineage, not a claim that the Method became a different or better Method | transfer beyond controller firmware `4.8` and the named toolchain is untested |
| `M-Supplier-Approve`, identified Method | existing `A.3.1` identity result; supplier pinout-approval procedure `H17-3`; signed approvals and missing-approval stops | signed or explicitly missing approval supplies an input/stop to the release decision; `H17-3` documents an adaptation from `H17-2` | whether the documented adaptation changed Method identity is unresolved |
| `M-Release-Authorize`, identified Method | existing `A.3.1` identity result; release checklist `RC-17.3`; named authorization results | consumes verification, evidence-state, and authority conditions for EC-417 | no family relation with the other three Methods is established |
| `C-Evidence-Reconcile-Internal`, candidate Method account | eight internal cases in evidence dossier `ER-EC417-12+1` | documented derivation from the eight internal occurrences and their artifact traces | `A.3.1` identity and transfer to supplier-originated changes remain open |
| `C-Evidence-Reconcile-Supplier`, candidate Method account | four supplier-originated cases plus the held-out thirteenth case in `ER-EC417-12+1` | documented derivation from those cases; the held-out case supports the supplier branch without proving a Method | `A.3.1` identity, population scope, and relation to the internal account remain open |
| `C-AI-Trace-Review`, human-governed candidate Method account | AI trace prompt `ATP-2`, confidentiality rule, human-decision record set `HDR-TraceAcceptReject-17`, and decision-result set `RES-TraceAcceptReject-17` | `ATP-2` contributes prompt-and-guard description content to the candidate account; `HDR-TraceAcceptReject-17` evidences the bounded human Work set `W-TraceAcceptReject-17` performed by `TraceReviewer-17` and links each occurrence to its corresponding result in `RES-TraceAcceptReject-17`; the candidate account is documented as derived from `ATP-2`, `HDR-TraceAcceptReject-17`, and `RES-TraceAcceptReject-17`; the AI provider remains a separate System | no evidence of autonomous authority, effectiveness, or transfer outside the named information boundary; none of these relations establishes Method identity, family membership, causation, superiority, applicability, or composition |

For the `D-21` through `D0` use window, the project relies on the exact editions in the table. Use those editions until the project explicitly changes its reliance decision. A revision of `HV-6`, `FI-4.8`, `H17-3`, `RC-17.3`, `ER-EC417-12+1`, or `ATP-2`, a changed operating status, or evidence outside its stated case window reopens the affected source-use row rather than the entire repertoire automatically.

The existing project-local locator `LG-EC417-ReleaseMethods` contains only the four identified Methods for the bounded release comparison. Its criterion is contribution of a verification, integration, supplier-approval, or authorization result to EC-417. The three candidate accounts remain adjacent repertoire entries with their own statuses; a wider source-inspection list does not silently add them to the Method grouping. Family status remains unresolved. No family membership, fifth Method, or composite Method follows.

Description-side material stays separate. Existing `A.3.2` results identify `HV-6`, `FI-4.8`, `H17-3`, and `RC-17.3` as MethodDescriptions of the four already identified Methods. The stage table, bundle records, AI prompt, and evidence grades remain other claim-bearing epistemes or artifacts. They are not additional Methods. The two reconciliation records and the AI review record remain candidate accounts, so no `A.3.2` MethodDescription is asserted for them.

Proposed-whole account `C-EC-Release-v2` is recorded outside the repertoire membership table as an architecture subject. It cites contributions from the four Methods and three accounts, but that source relation establishes neither a whole Method nor `methodPartOf`.

The repertoire stops honestly with four missing positions: no established Method family covers the local grouping; no source establishes a Method-lineage relation among the four identified Methods; the same-Method or distinct-Method relation between the two reconciliation accounts is unresolved; and the AI account lacks transfer and effectiveness evidence. Those gaps do not prevent ME.5 from qualifying individual subjects or ME.6 from comparing named structures. They prevent family, ancestry, superiority, and composite claims.

### ME.2:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| repository-completeness bias | A large collection is treated as a complete repertoire. | Bind relevance to one use and list missing positions explicitly. |
| package-kind bias | Sections, tools, roles, and artifacts are all called Methods. | Recover each subject's actual kind or provisional status before grouping. |
| lineage-progress bias | A later edition or descendant is assumed better or more effective. | Record only the supported provenance relation; evaluate worth and causality separately. |
| family-by-co-listing bias | Entries under one heading become a Method family. | Cite the independent family basis or call the result a project-local grouping. |
| freshness-by-date bias | The newest publication is assumed applicable to the current use. | Separate source edition, source-use currentness, evidence window, and applicability. |

### ME.2:7 - Conformance Checklist

- [ ] The repertoire has one named comparison or proposal use and a relevance criterion.
- [ ] Every Method cites an existing `A.3.1` identity result; every provisional subject remains a candidate account.
- [ ] MethodDescriptions attach only to already identified Methods and remain distinct from those Methods.
- [ ] Every source contribution names an exact source or artifact edition, subject, contribution used, evidence/status, scope, and limit.
- [ ] Established family relations, project-local groupings, variant claims, and lineage relations are recorded separately.
- [ ] Every lineage claim names both subjects, the relation, and the supporting source without implying causation, superiority, or composition.
- [ ] Publication/artifact edition and current project reliance are distinguishable.
- [ ] Missing alternatives, provenance, relations, editions, evidence, or source meanings remain visible.
- [ ] The stop states what the repertoire supports and which claims remain unavailable.

### ME.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The repository contains 40 Methods.” | Reclassify exact entries; count only Methods already identified under `A.3.1`. |
| “These practices share a history, so they form one family.” | Separate the supported lineage relation from the independently governed family question. |
| “Version 3 supersedes version 2, so it is better.” | Record edition succession and compare the decision-bearing contribution under its own evidence. |
| “We observed the procedure, so the Method belongs in the repertoire.” | Keep the observation as occurrence evidence or a candidate account until Method identification. |
| “A blank row makes the repertoire incomplete and unusable.” | Name the missing position and whether it blocks, weakens, or does not affect the receiving use. |

### ME.2:9 - Consequences

The project gains reusable alternatives with recoverable provenance, bounded evidence, and visible gaps. Later qualification and architecture comparison can inspect the same subjects without repeating search or inheriting false family and composition claims.

The cost is a smaller catalogue. Some lineages remain partial, and the newest source may be unusable until its changed meaning or applicability is checked.

### ME.2:10 - Rationale

A repertoire becomes reusable when its users can distinguish statuses and trace provenance. Source lineage can explain where an edition, account, or variant came from, but it cannot answer whether a Method exists, whether two Methods form a family or whole, whether one caused an outcome, or whether the latest variant is preferable. Those questions have different subjects and governors.

R7's connected Method, Work, description, variant, capability, and tool distinctions prevent source organization from becoming ontology. The Method Engineering literature supplies strong search and reuse practices; FPF supplies the status and relation boundaries needed to carry their contributions across projects.

### ME.2:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Henderson-Sellers and Ralyté, [Situational Method Engineering: State-of-the-Art Review](https://opus.lib.uts.edu.au/handle/10453/13456) | Method-base lineage, reusable source material, situational construction, and explicit Method Engineering traditions. | Source-local fragments and construction terms do not determine FPF kinds, family membership, or composition. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Method ecosystem, core idea, representation, procedure, intended use, tool, and adaptation questions. | The elements guide source recovery; they are not an imported ontology or universal repertoire schema. |
| Current FPF `G.2`, `G.5`, and `G.11` | Refreshable SoTA sourcing when needed, truthful family or local set results, and edition/currentness discipline. | These patterns do not identify repertoire Methods or turn co-listing and lineage into selection, family, or merit. |
| R7 Methodology guide | Connected treatment of Methods, descriptions, Work, variants, capability, tools, and several representations. | The guide supplies problem-owning synthesis, not current project identity or lineage evidence. |

Reopen when a decision-relevant source or artifact changes, a missing position becomes available, an `A.3.1` result changes a subject's status, a family or lineage relation gains or loses support, or the named comparison requires an alternative outside the current relevance boundary.

### ME.2:12 - Relations

- ME.1 or an equivalent result supplies a one-Method, plurality, or Method-relation focus and its statuses. ME.2 may also start from another receiving use that meets the same conditions.
- `A.3.1` governs Method identity; `A.3.2` governs MethodDescriptions. Repertoire inclusion changes neither.
- `G.2` supplies a broader refreshable SoTA pack only when that heavier source result is needed; `G.11` governs currentness; `G.5` supplies governed family or selected-set results when their entry conditions hold.
- ME.4 may recover decision-relevant entries from a heavyweight package. ME.18 may supply scoped candidate accounts. Use either only when its result is needed.
- ME.3 may use the repertoire to expose situational criteria; ME.5 receives identified Methods and candidate accounts with their source limits; ME.6 receives only named structures and relation questions.
- ME.7 may cite repertoire contributions for a proposed-whole account, but citations create neither a whole Method nor obtaining composition.

### ME.2:End

## ME.18 - Reconstruct a Candidate Method Account from Observed Work

>
> **Primary working result:** a **claim-to-evidence dossier** with scoped candidate Method accounts, contradictions and rivals, a held-out result, evidence limits, and the next receiving use—or a justified lowering when the evidence supports only Work description, a local workaround, tool behavior, or an unresolved grouping.

### ME.18:0 - Use This When

Use this pattern only after `A.3.1.MR` has recovered an ordinary candidate account or honest lower result and a named receiving decision still cannot be made without a larger evidence programme. Typical triggers are heterogeneous settings, disputed variants, tacit cues or judgments, incomplete records, consequential use, or a need for a stronger held-out application.

Begin with the receiving decision and the few candidate-account claims whose uncertainty changes it. Select evidence forms for those claims rather than collecting every available trace or interview.

The first useful result is a claim-to-evidence matrix and sampling decision. It states what would support, contradict, split, or lower each claim and why the selected evidence form can distinguish those outcomes. This makes the specialist burden visible before the study grows.

Use the larger evidence programme only when ordinary candidate recovery is insufficient for the named decision. No observation, interview, log, or synthesis backdates a Method into past Work, promotes a log into a MethodDescription, or admits a Method without `A.3.1`.

### ME.18:0.1 - Working Distinctions

| Evidence or result | Contribution retained here | Boundary |
| --- | --- | --- |
| occurrence observation and artifacts | overt actions, results, versions, coordination, and traces for one Work occurrence | observed recurrence does not identify a Method by itself |
| Critical Decision Method (CDM) probe | recalled critical-incident cues, options, judgments, and counterfactual reflections | recall and interviewer effects remain visible; CDM supplies no event-log claim |
| event-log analysis | recorded recurrence, sequence, deviation, and conformance relative to declared log semantics | tool traces describe recorded events, not intent, tacit contribution, or a MethodDescription |
| contextual observation or protocol elicitation | coordination, workarounds, or otherwise inaccessible reasoning when their particular risk is named | these moves are selected separately; CDM and process-mining sources do not support them by proxy |
| expert synthesis | claim-to-evidence matrix, decision-relevant sampling, contradiction-by-scope rule, held-out discriminator, and stopping rule | disclose the synthesis rather than attributing it to the specialist sources |
| candidate Method account | a scoped episteme about a possible reusable way of doing | Method identification remains with `A.3.1` |

### ME.18:1 - Problem Frame

Ordinary records show only part of practice. Logs favor tool-visible events, procedures favor intended behavior, interviews favor memorable episodes, and successful outcomes can hide competent minority variants or recovery Work. A stronger reconstruction therefore needs several evidence forms and an explicit account of which claim each supports.

More evidence is not automatically better. The programme earns its cost only when its combined result changes candidate-account content, scope, rivals, or the receiving decision beyond what `A.3.1.MR` already returned.

### ME.18:2 - Problem

A trace-only reconstruction turns log regularity into a Method. An interview-only reconstruction turns confident recall into recurrence. A majority-vote synthesis erases variants and failure cases. An expanding study collects material without a stopping decision.

The resulting account looks rich yet cannot say which claim each item supports, what would contradict it, or whether a held-out case behaves as the account predicts.

### ME.18:3 - Forces

| Force | Tension |
| --- | --- |
| Tacit contribution | Important cues and judgments may be absent from records, while elicitation can distort them. |
| Heterogeneity | Several performers and settings improve discrimination, while indiscriminate sampling raises cost. |
| Contradiction | Variants may be real, while some disagreement is error or incomplete evidence. |
| Tool visibility | Event logs are precise about recorded fields, while invisible coordination and intent remain outside them. |
| Held-out use | A new case tests the account, while retrofitting after observation destroys discrimination. |
| Specialist burden | Consequential decisions may justify a programme, while ordinary recovery needs an affordable stop. |

### ME.18:4 - Solution

Organize evidence around decision-changing claims, keep evidence forms distinct, resolve contradiction by scope, and use a held-out discriminator before returning scoped accounts or a lower result.

#### ME.18:4.1 - Pattern-Use Unfolding

1. **Name the receiving decision and unresolved claims.** Include only intended result, entry conditions, reusable operations or invariants, cues and decisions, participants and capabilities, information and artifacts, support, variation, recovery, and stop claims that can change the decision.
2. **Build the claim-to-evidence matrix.** For each claim, state what observation could support, contradict, split, or lower it and why the evidence form can distinguish those outcomes for that claim.
3. **Sample for decision-relevant variation.** Select cases that differ in success or failure, routine or exceptional conditions, performer, setting, and tool or provider. Add a disconfirming case when the emerging account explains only the convenient sample. Use no universal participant count.
4. **Keep evidence forms distinct.** Use occurrence observation/artifacts for overt actions and results; CDM for recalled critical-incident cognition; event-log analysis for recorded recurrence and deviation. Select contextual or protocol evidence only for a named gap and risk.
5. **Keep occurrence and candidate layers separate.** Record each Work occurrence before abstracting an account. Preserve missing fields, observer effects, recall limits, tool coverage, and source access.
6. **Resolve contradiction by scope, not vote.** Compare performer, setting, outcome, and evidence form. Correct a supported error; otherwise split variants, narrow applicability, retain rivals, or lower the claim.
7. **Use a held-out discriminator.** Before inspecting the held-out case, state what each serious account predicts about cues, decisions, variation, and result. Record surprise and revision rather than retrofitting.
8. **Stop or lower.** Stop when the receiving decision can distinguish the accounts and each load-bearing claim has adequate trace or an explicit uncertainty disposition. Return no candidate account when the evidence supports only a Work description, local workaround, tool behavior, or unresolved grouping.

#### ME.18:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| receiving boundary | Decision, situation, consequence, candidate accounts, and unresolved claims. |
| claim-to-evidence matrix | Claim, discriminating observation, selected evidence form, support/contradiction/split/lowering rule, and stopping use. |
| sample and occurrences | Decision-relevant variation, each Work occurrence, source access, missing fields, and evidence-form limits. |
| synthesis | Scoped accounts, retained variants/rivals, contradiction disposition, and attribution of each synthesis move. |
| held-out result | Predictions made before inspection, observed result, surprise, revision, and remaining uncertainty. |
| return | Account(s) or lower result, evidence limits, next receiving use, and reopen condition. |

#### ME.18:4.3 - What Changes in Practice

Teams stop equating a discovered sequence or interview narrative with the Method. They spend specialist effort only where a receiving decision needs it, know which evidence form supports which claim, and can retain two scoped variants instead of averaging them into a misleading universal account.

### ME.18:5 - Archetypal Grounding

#### ME.18:5.1 - Ordinary `A.3.1.MR` Stop

A maintenance team has six source-traceable calibration Work records using the same released instruction, input schema, equipment configuration, decision authority, and result meaning. One failed record contains an explicit missing-input stop already described by the candidate account. The receiving decision needs only a source-traceable account for comparing two instructions; no tacit cue, disputed variant, consequential transfer, or held-out prediction changes that decision.

`A.3.1.MR` returns the candidate account, rival, gaps, and distinguishing question. ME.18 is not entered. More interviews and process mining would add cost without changing the next move.

#### ME.18:5.2 - Genuine Escalation: EC-417 Evidence Reconciliation

The EC-417 decision cannot determine whether internal and supplier-originated evidence reconciliation are one account or scoped variants from ordinary records alone. The reconstruction uses a twelve-case development sample plus one held-out case:

- four firmware-only and four internal harness-plus-firmware releases accepted versioned provisional pinout evidence before safety closure;
- four supplier-originated releases required signed evidence at closure;
- four reconciliation boards were observed;
- CDM probes involved two supplier, two software, one hardware, and one safety practitioner; and
- a thirteenth supplier-originated change was reserved unseen for the held-out discriminator.

| Evidence move | Scenario contribution | Limit retained |
| --- | --- | --- |
| observation and artifacts | overt evidence versions, board records, integration bundles, approval states, and closure results | no population estimate or tacit-cue claim |
| CDM probes | cues, considered options, judgments about provisional versus signed evidence, and counterfactual reflections in critical incidents | retrospective recall and interviewer effects remain |
| event-log analysis | recorded recurrence and deviations in evidence-version, integration, approval, and closure events | log fields do not establish intent or a reusable Method |
| disclosed expert synthesis | twelve-plus-one sample, internal/supplier scope split, contradiction rule, held-out discriminator, and stop | not attributed to CDM or process-mining sources |

Before inspecting the thirteenth case, the team recorded three rival predictions:

| Account or rival | Cues and decision predicted | Variation and result predicted |
| --- | --- | --- |
| `C-Evidence-Reconcile-Internal` applied beyond its observed scope | internally controlled versioned evidence would be the decisive cue; the internal reconciliation role could decide the branch without a distinct supplier approval | supplier origin would not change the branch; closure could proceed from the internal reconciliation result without signed supplier approval |
| `C-Evidence-Reconcile-Supplier` | supplier-owned configuration and restricted geometry would be decisive; supplier responsibility and signed approval would remain required for closure | reversible early integration could occur, but a signed-delta comparison and affected verification would precede either closure or an explicit missing-approval stop |
| `R-Rig-Capacity-Only` | rig unavailability, rather than evidence origin, would trigger the hold and next-slot decision | the same branch would occur for internal and supplier changes and would clear when rig access returned |

The held-out case then showed **cues** of supplier-owned geometry, restricted provider access, and available rig capacity; the **decision** allowed reversible early integration but withheld closure pending signed supplier approval; the **variation** required a signed-delta comparison and one affected verification; and the **result** was truthful closure after signed approval arrived at `D-8`. No load-bearing observation surprised the supplier-scoped account. The available rig contradicted the capacity-only rival for this case, and the retained supplier-approval requirement contradicted the internal-account extrapolation.

The resulting disposition is to keep `C-Evidence-Reconcile-Internal` for the eight internal cases, keep and narrow `C-Evidence-Reconcile-Supplier` to supplier-owned configuration with the signed-evidence branch, and retain rig availability as a support condition rather than the account that explains this split. The scope split is not decided by majority count. One held-out supplier case leaves transfer to other suppliers, other configuration classes, and missing-approval situations uncertain; neither account is admitted as a Method, and no effectiveness or population claim is made.

### ME.18:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| trace bias | Recorded sequence becomes the Method or its complete description. | State log semantics and combine only with evidence needed for the claims. |
| interview bias | Memorable explanations become recurrence or causal evidence. | Keep CDM claims to cues, options, judgments, and reflections with recall limits. |
| majority bias | The largest variant erases a competent minority or setting-specific branch. | Resolve contradictions by performer, setting, outcome, and evidence form. |
| method-brand bias | Using a named evidence Method lends authority to the whole synthesis. | Attribute each sourced move and disclose the project synthesis separately. |
| programme bias | More cases are collected because the study is open. | Tie sampling and stop to the receiving decision and load-bearing claims. |

### ME.18:7 - Conformance Checklist

- [ ] `A.3.1.MR` has already returned an ordinary result, and a named receiving decision justifies the larger burden.
- [ ] The first useful result is a claim-to-evidence matrix and decision-relevant sampling choice.
- [ ] Observation/artifacts, CDM, event-log analysis, contextual/protocol evidence, and expert synthesis keep distinct contributions and limits.
- [ ] Each Work occurrence is recorded before candidate-account abstraction.
- [ ] Contradictions are resolved by scope or retained, not averaged by vote.
- [ ] A held-out discriminator states predictions before inspection and records surprise/revision.
- [ ] Scoped variants and rivals remain visible.
- [ ] The result can lower to Work description, local workaround, tool behavior, or unresolved grouping.
- [ ] No evidence form identifies a Method, creates a MethodDescription, backdates Work, or establishes causality by itself.

### ME.18:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Mine the log and recover the Method.” | Recover only recorded events; use the claim matrix to identify missing intent, tacit, and context evidence. |
| “Interview experts until their stories converge.” | Sample for decision-relevant variation and preserve contradiction, recall limits, and minority variants. |
| “Use every evidence form.” | Select only forms whose possible results can change a claim or the receiving decision. |
| “The held-out case fits after we revised the account.” | Record predictions before inspection and report surprise rather than retrofitting. |
| “The reconstructed account is now an admitted Method.” | Return the account and send Method identity to `A.3.1`. |

### ME.18:9 - Consequences

For consequential decisions, practitioners reconstruct candidate accounts claim by claim, make the sources traceable, and can retain variants. The receiving decision gains stronger accounts or an honest lower result rather than a single fluent reconstruction.

The cost is specialist sampling, evidence access, and analysis. Some evidence will remain unusable for the desired claim, and a well-run programme can still return no Method candidate.

### ME.18:10 - Rationale

No single evidence form covers overt action, recorded recurrence, recalled judgment, tacit coordination, and cross-setting variation. Their non-isomorphism is useful only when each is connected to a claim and a receiving decision. The matrix, scope rule, held-out discriminator, and stop make that combination testable without claiming a universal research protocol.

### ME.18:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.3.1.MR` | Ordinary several-occurrence recovery, rival accounts, source-to-claim trace, held-out question, and honest lowering. | ME.18 begins only when a named decision needs a larger programme. |
| Klein, Calderwood, and MacGregor, [Critical Decision Method](https://doi.org/10.1109/21.31053) | Retrospective critical-incident probes for cues, options, judgments, and counterfactual reflections. | CDM supplies no event-log, recurrence, population, or causal result. |
| IEEE Task Force, [Process Mining Manifesto](https://www.tf-pm.org/resources/manifesto) | Discovery, monitoring, and conformance analysis over recorded event logs. | Event-log regularity establishes neither intent, tacit contribution, Method identity, nor causality. |
| Ordinary observation and artifacts | Overt occurrence evidence and result traces. | Observation supplies only what its access, scheme, and window support. |

The claim matrix, decision-relevant sampling, contradiction-by-scope rule, held-out application, and combined stop are the bounded DPF synthesis. Reopen when a current evidence Method changes one of those moves, or when representative uses show that the extra burden does not improve account scope or the receiving decision.

### ME.18:12 - Relations

- `A.3.1.MR` supplies the ordinary floor and specialist-exit question; ME.18 does not replace it.
- `A.15.1` governs any claimed Work occurrence; `A.10` governs evidence paths and provenance; `A.3.1` alone governs Method identification.
- ME.2 may add returned accounts provisionally to a repertoire. ME.5 may qualify an account without changing its status.
- Later description, support, trial, or architecture patterns consume only the scoped account, evidence limit, and next use their entry conditions admit.
- ME.19 uses different Work: it explains differentiation and may return a causal-use support boundary; evidence reconstruction here supplies no causal conclusion by itself.

### ME.18:End

## ME.3 - Build Situational Method Requirements and Fit Criteria

>
> **Primary working result:** one **situational Method-criteria result** that states the receiving Work and result, required Method contributions, performer capabilities, technical and organizational conditions, allowable variation, non-negotiable conditions, burden limits, evidence needs, and truthful acceptance or stop observations without selecting or admitting a Method.

### ME.3:0 - Use This When

Use this pattern when a Method, an established-family or project-local grouping choice, or a proposed Method/Work/support structure may fail in the project's situation. Enter when the practical question concerns the receiving result, performer capabilities, technical or organizational conditions, variability, evidence, authority, or acceptable burden and those conditions are not yet explicit enough for individual qualification or architecture comparison.

Begin with the situation family, intended or current Work, receiving professional result, and the level of the Method decision. State the contributions that a Method or several Methods must make without preselecting which candidate supplies them. Place every resulting criterion with the Method, description, performer capability, covering Work assignment, permission relation, decision-authority relation, performed Work, decision result, support/access relation, responsibility, cultural subject, or receiving result it actually concerns.

The first useful result is a bounded set of criteria with subjects, allowed variation, evidence needs, satisfaction observations, and stops. A criterion can be ready for later use even when no candidate currently meets it.

Do not use this pattern as a generic product-requirements template. Criteria do not identify, admit, select, qualify, or compose a Method or establish present or future fit. Product acceptance, Method identity, individual qualification, and architecture choice remain separate results.

### ME.3:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| situation family | The recurring class of receiving Work and conditions for which criteria are intended, with important variation and exclusions explicit. |
| receiving Work and result | The dated Work occurrence or intended occurrence and the professional result it must produce or preserve. They are not the Method. |
| required Method contribution | A reusable action, result, or preserved condition needed from one Method or from named Method relations, stated before assigning it to a candidate. |
| criterion subject | The actual object or relation constrained by a criterion: Method/account content, MethodDescription, performer capability, covering Work assignment, permission relation, decision-authority relation, performed Work, decision result, support/access, responsibility, cultural relation, or another domain subject. |
| performer capability | An ability needed to enact or judge a contribution. It is distinct from responsibility, access, assignment, permission, and decision authority. |
| Work assignment | A named assignment occurrence whose holder is one admitted System and whose scope and window cover specified Work. The assignment alone establishes neither permission, decision authority, performed Work, nor a decision result. |
| permission relation | An independently supported relation permitting a named System to perform a specified act within a stated subject, scope, window, and basis. It does not create an assignment, prove performance, or confer decision authority beyond that exact permission. |
| decision-authority relation | An independently supported direct relation under which a named System may issue a named decision result. Its subject, decision scope, window, basis, and evidence for reliance are explicit; assignment, performed Work, capability, responsibility, access, and acceptance need separate evidence. |
| allowable variation | A range or branch that may change while the receiving result and non-negotiable conditions remain protected. |
| burden limit | A bound on time, attention, capacity, delay, coordination, cost, or another named burden at its actual participant, scope, and window. |
| evidence need | The observation or record required before a later decision may rely on criterion satisfaction. It is not satisfaction by itself. |
| acceptance or stop observation | The observable condition under which the criterion can be passed to a later decision or must stop that route. It does not accept a Method or product by itself. |

### ME.3:1 - Problem Frame

Situational Method Engineering asks practitioners to fit a way of working to its context. Engineering-design research adds useful questions about a Method's goal, procedure, rationale, framing, mindset, intended use, representation, tool, and ecosystem. A project also faces domain constraints that do not belong inside the Method: protected information, performer capability, authority, shared capacity, evidence timing, reversibility, and the acceptance conditions of the receiving result.

When these unlike claims are placed in one “method requirements” list, description content becomes a Method part, culture becomes a performer property, authority becomes skill, and product requirements become proof of Method fit. A useful criteria result keeps the connected situation visible while returning each claim to its actual subject.

### ME.3:2 - Problem

A universal checklist invites premature scoring. It may reward a well-written MethodDescription even when performers lack capability, declare a Method unsuitable because a provider arrangement fails, or hide an architecture-level peak-load conflict inside an individual candidate score.

The project then appears to have objective fit criteria, but nobody can say what must change: the Method account, the description, the support System, the covering Work assignment, a permission or decision-authority relation, the Work arrangement, or the receiving result's own acceptance rule.

### ME.3:3 - Forces

| Force | Tension |
| --- | --- |
| Comparability | Shared questions help compare alternatives, while different subjects need different criteria and evidence. |
| Situation specificity | Local constraints change the decision, while a one-project list may overfit and block reuse. |
| Candidate neutrality | Criteria should expose viable alternatives, while familiar candidates can be smuggled into the wording. |
| Flexibility | Professional Work must adapt, while non-negotiable safety, evidence, authority, and burden bounds must hold. |
| Clarity | Source-side content prompts reveal omissions, while they can be mistaken for universal Method parts. |
| Economy | Cheap observable stops save effort, while high-consequence claims need stronger evidence. |

### ME.3:4 - Solution

Build criteria from the receiving situation outward. State required contributions and conditions, assign each criterion to its actual subject, preserve allowed variation, and defer every fit or selection verdict to the pattern that evaluates the relevant subject or structure.

Recognition is cheap: recurring Work, a changed constraint, or one plausible capability, access, authority, evidence, or burden failure is enough to expose a criterion question. Assurance is later and row-specific: the named observation, edition, and window must support satisfaction before qualification or architecture work may rely on that row.

#### ME.3:4.1 - Pattern-Use Unfolding

1. **Bound the situation family.** Name representative Work, receiving result, affected subjects, decision window, recurrence expected, important variants, and ordinary exclusions. Keep project, process, and case views as descriptions of the same Work when they are used.
2. **State required contributions before candidates.** Describe the reusable actions, results, or preserved conditions that one Method or named Method relations must contribute. Do not write a familiar candidate's current procedure as the requirement unless that exact feature is independently non-negotiable.
3. **Use source prompts without importing kinds.** Ask what goal, procedure, rationale, framing, mindset, intended use, representation, tool, scope, and adaptation conditions a source makes visible. Place the answer with its actual subject. A stated mindset may be description content; an obtaining capability or cultural relation needs separate evidence.
4. **Recover conditions around enactment.** State performer capabilities, technical and organizational conditions, inputs, support/provider access, responsibility, covering Work assignments, permission and decision-authority relations, evidence timing, reversibility, and other Work or result constraints. Keep these conditions distinct from one another and from the performed Work and its decision result.
5. **Separate variation from invariants.** Name lawful branches, substitutions, timing ranges, and local adaptations. Mark non-negotiable result, safety, confidentiality, authority, or evidence conditions explicitly.
6. **Set burdens at the right level.** Attach time, attention, capacity, delay, meeting, or cost limits to a participant, Work scope, and window. Keep individual burden distinguishable from combined peak demand and burden transferred to another participant or period.
7. **Name evidence and observations.** For every decision-changing criterion, state what record or observation a later evaluation needs, its edition or window when material, and what would count as satisfied, failed, or unknown. Do not turn the requested evidence into a fit verdict.
8. **State acceptance, stop, and reopen rules.** Say when the criteria set is adequate for its next use, which missing fact stops that route, and which situation or source change requires rebuilding it. A stop may route to capability, support, authority, product, or Work redesign rather than Method selection.
9. **Return without selecting.** Publish the criteria by subject and decision level. Send individual subject questions to ME.5 and combined structure questions to ME.6 only when their own entry conditions hold.

#### ME.3:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use and situation family | Receiving Work/result, decision level, scope, window, representative variations, and exclusions. |
| required contributions | Candidate-neutral Method contributions and the result or preserved condition each must support. |
| criterion rows | Criterion ID, actual subject/relation, requirement or bound, allowed variation, non-negotiable status, and decision level. |
| capability, assignment, permission, and authority | Required performer capabilities; separate responsibility and access conditions; covering Work assignments; permission and direct decision-authority relations; and evidence for each. |
| technical and organizational conditions | Inputs, support/provider conditions, evidence timing, reversibility, coordination, and other situated constraints. |
| burden limits | Participant, Work scope, time window, bound, measurement basis, and transferred-burden warning. |
| evidence and disposition | Required observation or record and the condition for `satisfied`, `failed`, or `unknown` in later use, without a fit or selection verdict. |
| stop and reopen | Missing fact or failed non-negotiable that stops a route, adequate-next-use condition, and situation/source change that reopens the set. |

#### ME.3:4.3 - What Changes in Practice

Teams stop asking whether a methodology “fits the context” as one opaque question. They can see whether the live issue is a Method contribution, a description gap, missing capability, covering assignment, permission, decision authority, provider access, Work timing, receiving-result condition, or combined burden. Later qualification and architecture comparison receive explicit conditions instead of a precomputed winner.

### ME.3:5 - Archetypal Grounding — EC-417 Situational Criteria

The situation family is a safety-relevant controller change combining firmware and supplier-originated harness geometry under a fixed release calendar. The intended Work produces one released change with traceable affected requirements, implementation revisions, verification results, evidence status, and human release authority. Some cases have signed supplier evidence before integration; others have only versioned provisional evidence until later. AI support may suggest trace links but may not receive confidential geometry or decide release.

Three views describe the same release Work. The project view exposes dates, allocations, and authority; the process view exposes recurring supplier-evidence, integration, verification, and release-result correspondences; the case view exposes how new evidence changes the next decision for one release. These views help find criteria. They create neither additional Work nor a Method.

Required Method contributions are stated without selecting an architecture: produce the affected hardware verification result; integrate the implementation against an explicitly versioned evidence state; produce signed supplier approval or an explicit missing-approval stop; and return release, withhold, or next-slot authorization under named human authority. Evidence reconciliation and trace review are additional candidate contributions, not pre-admitted Methods.

The case admits three human Systems and keeps their decision Work, assignments, permissions, authority, and results explicit:

| Admitted human System | Performed decision Work and result | Covering Work assignment | Independently obtaining permission or direct decision-authority relation |
| --- | --- | --- | --- |
| `TraceReviewer-17` | named `W-TraceAcceptReject-17` occurrences issue one accept/reject result for each AI trace suggestion | `ASG-TraceReview-17` covers that Work for EC-417 from `D-21` through `D0` | `PERM-TraceAcceptReject-17` permits subject `TraceReviewer-17` to accept or reject EC-417 AI trace suggestions in that window, on the basis of `TraceReviewCharter-17`; reliance requires a current matching entry in `DecisionRightsRegister-17` and the linked human-decision record |
| `SafetyReviewer-17` | `W-SafetyEvidenceDecision-17` issues accept/reject of the evidence conditions for B2 entry, safety closure, or recovery | `ASG-SafetyReview-17` covers that Work from `D-21` through the next authorized slot | `AUTH-SafetyEvidence-17` is the direct decision-authority relation for subject `SafetyReviewer-17`, that evidence-decision scope, and that window, on the basis of `SafetyDecisionCharter-17`; reliance requires a current matching `DecisionRightsRegister-17` entry and linked safety-decision record |
| `ReleaseDecider-17` | `W-ReleaseDecision-17` issues the branch-entry and release, withhold, or next-slot decision results | `ASG-ReleaseDecision-17` covers that Work from the `D-21` checkpoint through the next authorized slot | `AUTH-ReleaseDecision-17` is the direct decision-authority relation for subject `ReleaseDecider-17`, selection of `A` or authorization of at most three `B2` trials and the named release disposition, and that window, on the basis of `ReleaseDecisionCharter-17`; reliance requires a current matching `DecisionRightsRegister-17` entry and linked release-decision record |

Assignments, permission relations, and authority relations each need their own basis. Each performed Work occurrence and decision result also needs its own record; none is established by an assignment, permission, or authority relation alone. Responsibility, access, capability, assignment, permission, authority, performed Work, and decision result therefore remain separately testable. The AI provider is a separate System and is holder or subject of none of these assignments or relations.

| Criterion | Actual subject and decision level | Requirement, variation, and bound | Evidence needed and truthful stop |
| --- | --- | --- | --- |
| `SC-TRACE-01` | EC-417 receiving result and its requirement/implementation/verification correspondence | every affected safety requirement links to one or more named current implementation revisions and one or more named verification results; every correspondence link remains inspectable, while representation format may vary | versioned trace record; an affected requirement with no current implementation-revision link or no verification-result link is `failed` and stops safety closure |
| `SC-CONF-01` | supplier-geometry information and AI-provider access relation | confidential supplier geometry stays outside the AI provider; using no AI is allowable | access configuration and handling record; any provider exposure is `failed` and stops the AI-supported route |
| `SC-ASSIGN-01` | the three admitted human Systems, their decision Work, and `ASG-TraceReview-17`, `ASG-SafetyReview-17`, and `ASG-ReleaseDecision-17` | every performed decision-Work occurrence has a named System that matches the holder, Work scope, and window of its covering assignment | assignment and Work records; a missing assignment, holder mismatch, uncovered Work, or out-of-window occurrence is `failed` without erasing the Work occurrence |
| `SC-AUTH-01` | `PERM-TraceAcceptReject-17`, `AUTH-SafetyEvidence-17`, `AUTH-ReleaseDecision-17`, and the governed decision results | every AI suggestion receives `TraceReviewer-17` accept/reject within the permission scope; safety and release decisions remain within their named subjects, scopes, windows, and bases; the AI provider has no release authority | current matching `DecisionRightsRegister-17` entries plus linked human, safety, and release decision records; missing permission or authority, an unnamed result, an out-of-scope decision, or authority delegated to the AI provider is `failed` |
| `SC-EVID-01` | provisional and signed hardware-evidence inputs, their relation, and the safety-closure guard | provisional evidence may be used before closure only with explicit edition and uncertainty; signed evidence supersedes it for safety-closure reliance, while the provisional edition, uncertainty, earlier Work use, and relation to the later signed evidence remain traceable | version/uncertainty fields, earlier-use record, signed supplier evidence, and inspectable provisional-to-signed relation; missing signed evidence at closure stops release |
| `SC-REV-01` | integration Work and the implementation state | rollback remains possible within one hour until `D-1`; the project may choose a signed-first or provisional-first branch before entry | replayable rollback demonstration for the current toolchain; inability to restore within one hour is `failed` for an early-integration route |
| `SC-CAP-01` | hardware-verification and safety-evidence capabilities of the named performers | hardware verification and safety evidence judgment require current capability for the named controller, rig, and safety scope; capability grants neither assignment, permission, nor release authority | current capability evidence for each named performer; the separate assignment, permission, and decision-authority conditions must also hold, and missing capability stops the contribution that needs it |
| `SC-TECH-01` | PLM/CI support, pinout schema, test-rig access, and their relations to Work | the evidence version used by integration remains recoverable; required verification has a named rig/access route; equivalent tools are allowed when they preserve the same result and evidence conditions | configuration, schema-edition, and access records; an unknown input edition or unavailable verification route is `unknown` and blocks reliance |
| `SC-BURDEN-01` | safety-engineer allocation on the peak safety day | safety demand stays at or below `0.40` of an eight-hour day (`3.20 h`); burden shifted to another performer remains visible rather than disappearing | allocation and time estimate for the selected day; demand above `0.40` is `failed` for the proposed structure, not proof that any one Method is unfit |
| `SC-BOARD-01` | each joint-board Work occurrence | each board lasts at most 45 minutes; one or two boards are allowable when the evidence and burden criteria remain satisfied | calendar and actual-duration record; a planned board above 45 minutes fails the coordination-burden criterion |
| `SC-STOP-01` | `W-ReleaseDecision-17`, its covering assignment, `AUTH-ReleaseDecision-17`, and the receiving result | no release occurs without signed evidence, required verification, a covering assignment, and the direct release-decision authority relation; delay to a later authorized slot is allowable | release record citing evidence, assignment, authority relation, and decision result; any missing non-negotiable yields withhold or next-slot, not silent waiver |

The criteria leave serious alternatives open. A signed-first alternative may wait for supplier evidence; a provisional-first alternative may integrate earlier and reconcile later; preparation may sit with the safety engineer or with the supplier-configuration role. ME.3 does not choose among them. A later individual qualification may apply contribution, capability, access, and evidence criteria to each identified Method or candidate account. A later architecture comparison must inspect combined peak demand, timing, covering assignments, permission and decision-authority relations, provider access, and burden transfer. Passing one row or staying below `0.40` does not establish fit of the whole proposed structure.

The criteria set is adequate for its next use when every non-negotiable row has an observable test, the remaining variations are explicit, and unknowns are routed to their actual subject. It stops the current route immediately on missing signed evidence at closure, confidential geometry exposure, a missing or mismatched covering assignment, permission, or direct decision-authority relation, unavailable required capability or verification route, rollback beyond one hour for an early-integration proposal, peak safety demand above `0.40`, or a joint board above 45 minutes. Reopen when the change class, supplier information boundary, evidence timing, toolchain, performer assignment, release authority, capacity window, or receiving-result acceptance rule changes.

### ME.3:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| universal-checklist bias | One source model becomes the criterion set for every situation. | Use source models as prompts and build only decision-changing situated rows. |
| candidate-shaped criteria | Requirements restate the familiar candidate's current procedure. | State the contribution or protected condition before assigning a candidate. |
| description-reification bias | Goal, rationale, framing, or mindset text becomes a world-side Method part or capability fact. | Place each answer with the description, account, capability, or cultural subject it actually concerns. |
| capability-assignment-authority collapse | A capable System is assumed assigned and authorized, or an authority holder is assumed capable and assigned. | Record capability, responsibility, access, assignment, permission, authority, performed Work, and decision result separately. |
| scalar-fit bias | Unlike safety, evidence, burden, and authority rows collapse into one score. | Preserve non-negotiable stops, unknowns, and decision levels. |
| local-burden blindness | A passing individual estimate hides a combined peak or burden moved to another participant. | Attach burden to participant, scope, and window; route combined structures to ME.6. |

### ME.3:7 - Conformance Checklist

- [ ] The criteria name a situation family, receiving Work/result, decision level, scope, window, variations, and exclusions.
- [ ] Required Method contributions are stated before candidate assignment.
- [ ] Every criterion names its actual subject or relation rather than hiding it under “method fit”.
- [ ] Method/account content, MethodDescription, performer capability, responsibility, support/access, covering Work assignment, permission relation, decision-authority relation, performed Work, decision result, culture, and receiving-result claims remain distinct.
- [ ] Capability, assignment, permission, and decision authority imply none of one another; an assignment or authority relation does not prove performed Work or its decision result.
- [ ] Allowable variation and non-negotiable conditions are explicit.
- [ ] Every burden limit names participant, Work scope, time window, bound, and measurement basis.
- [ ] Every decision-changing row names evidence and `satisfied | failed | unknown` observations.
- [ ] The result states acceptance-for-next-use, stop, and reopen conditions without selecting or admitting a Method.
- [ ] Individual and combined structure questions are routed to different later results.

### ME.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Our five Method Content Theory fields are the Method requirements.” | Use the five fields as source questions, then place each answer with its actual subject. |
| “The product requirement proves this Method fits.” | Keep the receiving-result condition separate and evaluate the Method contribution later. |
| “The team is experienced, so assignment, authority, and access are covered.” | Record capability, responsibility, provider access, covering assignment, permission, direct decision authority, performed Work, and decision result as separate conditions with evidence. |
| “Candidate A satisfies more criteria, so it wins.” | Preserve non-negotiable failures, unknowns, and trade-offs; use the applicable decision Method after qualification. |
| “Each Method stays within its burden, so the architecture fits.” | Compare combined peak demand, overlap, and transferred burden in ME.6. |

### ME.3:9 - Consequences

The project obtains criteria that say what must hold and where, rather than a generic context score. Missing capability can trigger preparation, an access failure can trigger support redesign, a product stop can withhold release, and an architecture burden can remain open without blaming an individual Method.

The cost is more explicit subject placement and fewer easy rankings. Some criteria remain unknown until evidence or a candidate account is available, and a complete criteria set still makes no selection.

### ME.3:10 - Rationale

A fit claim is bounded by a particular use, subject, situation, evidence basis, and time. Criteria are inputs to that later claim, not the claim itself. Returning every condition to its actual subject prevents a well-written description from standing in for capability, a provider arrangement from standing in for a Method, or one management view from standing in for the Work.

Method Content Theory and the design-method ecosystem line are complementary because they ask different source-side questions. R7 keeps Method, Work, description, mastery, tool, culture, and variants connected without identifying them. R10's project, process, and case views show why several descriptions of the same Work may expose different requirements while creating no new Work or Method.

### ME.3:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Daalhuizen and Cash, [Method Content Theory](https://doi.org/10.1016/j.destud.2021.101018) | Goal, procedure, rationale, framing, and mindset questions and their alignment. | Static content questions from a bounded initial population are prompts, not FPF kinds, universal criteria, capability facts, or effectiveness evidence. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Intended use, scope, representation, procedure, tool, ecosystem, and adaptation conditions. | The conceptual elements complement rather than replace Method Content Theory and FPF subject placement. |
| Tsai, Zdravkovic, and Söder, [situational Method Engineering in a digital business ecosystem](https://doi.org/10.1007/s10270-022-01068-z) | Empirical action-research evidence for situational requirements, construction, and selection in an ecosystem. | One action-research setting does not establish a universal criterion set or cross-domain fit. |
| Bender, [context-specific embedded-analytics process selection](https://doi.org/10.1007/s10257-024-00675-1) | Context-specific requirement and selection questions with practical constraints. | The application population and source-local process terms do not determine Method identity or general applicability. |
| Current FPF `A.3.1` and `A.15.6`, with R7 and R10 | Method identity/applicability, project-relative subject recovery, and the connected Method/Work/view/description/capability distinction. | Criteria change none of those identity facts, and project/process/case views create neither Work nor Methods. |

Reopen when a source model changes a decision-bearing prompt, a later evaluation exposes a criterion whose subject or decision level was wrong, a recurring architecture failure can be prevented by one affordable criterion, or the situation family, receiving result, variation, evidence window, performer, support, authority, or burden regime changes.

### ME.3:12 - Relations

- ME.1 or an equivalent result supplies the Method, family/local-grouping, or relation focus. ME.2 may supply inspectable alternatives and source limits. When equivalent content already exists, ME.1 and ME.2 need not be applied first.
- `A.3.1` governs Method identity and applicability. ME.3 criteria identify or admit no Method.
- R7 and `A.15.6` keep Method, Work, description, capability, tool/support, subject, and viewpoints distinct while situational criteria are built.
- ME.5 qualifies one identified Method or candidate account against applicable rows without turning the criteria into admission or whole fit.
- ME.6 compares combined Method, Work, allocation, support, authority, description, subject, capability, or cultural structures when several-structure relations change the decision.
- `C.11` or the applicable domain decision Method may consume later qualification and architecture results. The ME.3 criteria set itself selects nothing.

### ME.3:End

## ME.4 - Recover Methods and Decision-Relevant Contributions from Documentary Packages and Corpora

>
> **Primary working result:** a **Method-recovery dossier** whose entries retain their existing kinds or ordinary statuses, provenance, source meaning, viewpoint, bounded use, and decision-bearing relations. For qualification, ME.5 receives only identified Methods and individually scoped candidate Method accounts; ME.7 receives a proposed-whole account when whole identity and relations are the question.

### ME.4:1 - Problem Frame

**Use this when.** A methodology, standard, body of knowledge, maintained synthesis, reference model, or tool suite mixes reusable ways of doing with descriptions, Systems, capabilities, evidence, authority, and support. The receiving decision needs contributions from one package or several documentary sources, but their chapters and component lists do not establish Method structure.

Begin with one receiving decision and the exact source edition or snapshot. For several sources, keep each source's role and recovery scope visible. Recover only contributions and dependency slices that can change the decision; completeness is relative to this boundary.

The first useful result is a source-traceable Method-recovery dossier. Identified Methods and individually scoped candidate accounts can proceed to ME.5 with their support and evidence limits. A proposed whole proceeds to ME.7 when its identity and relations are the question. Tools, descriptions, capability, authority, and other useful contributions remain available under their actual kinds.

**Ordinary non-use.** Do not decompose an already precise Method to populate a library or inventory material whose presence cannot change the receiving decision. If records, interviews, traces, or observations are offered as evidence from which a reusable way must be reconstructed, use A.3.1.MR; enter specialist ME.18 only when its additional evidence programme is needed. A document can contain both prescribed guidance and testimony about performance: route the selected contribution by its use, not by its file extension.

#### ME.4:1.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| documentary source boundary | The exact package, edition, snapshot, or bounded corpus from which the receiving use recovers claims. It establishes no Method whole. |
| documentary role | How this source may contribute now: for example, a current comparator, maintained synthesis, normative statement, historical account, Method claim, or worked example. These are source-use descriptions, not FPF kinds. |
| recovery profile | How much source-local recovery the use needs. It differs from what the source is evidence for. |
| dossier entry | One source-traceable contribution retaining its existing kind or ordinary unresolved status. |
| source meaning | What the selected source says or uses the contribution to do, before local adaptation or cross-source comparison. |
| bounded use | The receiving decision, scope, conditions, and claim for which the contribution is recovered. |
| decision-bearing relation | A direct relation whose truth changes whether or how the contribution can be used. |
| provenance-preserving dependency slice | The smallest set of source claims, descriptions, inputs/results, support, evidence references, and relations needed to judge one Method or candidate account. |
| navigation section | An open reading aid, such as “Methods and accounts” or “Systems and support”; membership creates no type. |

Heavyweight packages connect concerns through publication, pedagogy, institutional history, tools, or viewpoints. Their visible organization may differ from Method, Work, subject, description, capability/provider/support, allocation, or cultural structures.

Method Content Theory and design-Method element research contribute questions about goal, procedure, rationale, framing, mindset, representation, intended use, and tools. Keep the answers with the Method, candidate account, description, capability, support relation, cultural claim, or other subject they actually concern. Several sources can ask similar questions without giving the same answer.

### ME.4:2 - Problem

The common decomposition error copies package headings into a Method library. A role becomes a Method, a checklist becomes a component, a tool becomes a participant Method, and adjacency becomes `methodPartOf`. The opposite error extracts a procedure alone and loses the rationale, input/result correspondence, authority, evidence, or support condition that makes it usable.

A later qualification then appears precise but cannot be replayed from the source and cannot distinguish a Method defect from missing access, capability, evidence, or authority.

### ME.4:3 - Forces

| Force | Tension |
| --- | --- |
| Recoverability | A later decision needs source meaning and provenance, while copying the whole package hides the load-bearing slice. |
| Ontological precision | Entries have unlike kinds, while one local dossier must remain readable. |
| Package cohesion | Source relations can matter, while package position and visual nesting supply no relation by themselves. |
| Affordability | A complete inventory feels safe, while decision-irrelevant entries add cost and false completeness. |
| Adaptation | A source contribution may be useful under changed conditions, while adaptation must not rewrite what the source claimed. |

### ME.4:4 - Solution

Build a source-traceable dossier around the receiving decision. Recover each documentary contribution in its own source meaning, preserve unlike kinds, and prepare only the downstream subjects whose question is current.

#### ME.4:4.1 - Pattern-Use Unfolding

1. **Bound the receiving use and sources.** Name the decision, relevant viewpoint, scope, and exclusions. For each documentary source give its exact edition or snapshot, source-return locator, role in this use, selected recovery profile, and currentness or reopening condition. One package normally needs one compact source/use statement, not a separate register.
2. **Choose how much to recover.** Use the profiles below. A maintained source's source-local recovery and comparison with current alternatives answer different questions; do not let the comparison erase a source contribution before it has been understood.
3. **Read source meaning before placement.** For each selected contribution retain the source term and locator, difficulty or opportunity, asserted reusable action or change, first useful result or blocker, and receiving use. Keep its original status, limits, purpose, and explicit or implied relations. A source ambiguity remains an ambiguity.
4. **Preserve the subject and evidence role.** Distinguish identified Methods, individually scoped candidate accounts, MethodDescriptions or other epistemes, Systems and support/access, capabilities and assignments, inputs/results/premises, and direct relations. A source's report of evidence is recovered as that report, not as independently established Work or effectiveness. Send a new question about a reusable way in occurrence evidence to A.3.1.MR; specialist ME.18 follows only under its entry condition.
5. **Record intended use and possible loss.** Say what the receiving use proposes to keep, change, reject, or leave unresolved and what source meaning or context would be lost. These are source-local recovery dispositions. Do not yet assert cross-source sameness, perform semantic merging, allocate a remainder to a supplier, or design the resulting pattern language.
6. **Recover direct relations and small dependency slices.** Retain supported production/use, schema correspondence, provider access, allocation, responsibility, authority, or other relevant relations. A line, container, chapter, lane, or local section supplies no relation. Attach only the source claims, conditions, and returns needed for the next judgement.
7. **Prepare the actual downstream subjects.** ME.5 receives only identified Methods and individually scoped candidate Method accounts, each with the smallest slice needed to judge contribution, inputs/results, applicability, burden, capability, support, authority/access, and evidence. ME.7 receives a proposed-whole account when whole identity and relations are the question; retain its proposed semantics, participant statuses, relation boundary, and source slices. Other kinds remain in the dossier or accompany those subjects without becoming Methods.
8. **Return the dossier or the first blocking gap.** Use open navigation sections when they help retrieval. Stop when the receiving decision can recover its subjects and source basis. If edition, role, receiving use, a needed current comparator, source return, kind, relation, or evidence is missing, name the affected contribution and the missing basis. Do not manufacture corpus completeness.

#### ME.4:4.1.1 - Select the Recovery Profile Per Source

For an ordinary package, the default is **decision-bounded recovery**: inspect only source claims and dependency slices that can change the receiving decision. This default needs neither maintained-synthesis status nor a prior supplier comparison. Select a specialized profile below only when its condition holds; naming a profile does not itself add a recovery operation or a record.

| Profile | Select when | Recovery and limit |
| --- | --- | --- |
| SoTA-first | Current alternatives can change which contributions the receiving decision needs. | Establish the relevant current comparison through ME.2 or the direct source route, then recover its decision-bearing claims. “Recent” alone is not a qualification. |
| Full source-local | An accepted maintained synthesis must remain reconstructable within a named scope. | Recover every decision-bearing contribution in that scope before later filtering. Preserve unsupported or non-selected material through source returns; do not import the source ontology or every chapter as a Method. |
| Gap-only | An exact earlier source/supplier comparison and its affected gap or delta are recoverable. | Recover that gap and its dependencies. Widen or stop if the baseline, scope, or source meaning has changed. A missing keyword is not a gap definition. |
| Mixed | The bounded corpus contains sources with different roles or recovery needs. | Apply the appropriate profile separately to each documentary source. Route occurrence evidence separately and retain the limits of any returned candidate account, specialist dossier, or lower result. |

“Full” is not an instruction to extract all possible knowledge from a source. The receiving decision sets the completeness boundary. A change from source-local recovery to cross-source reconciliation is a new question, not the final unspoken step of ME.4.

#### ME.4:4.2 - Record the Result

| Dossier position | Required content |
| --- | --- |
| recovery boundary | Receiving decision, source set and exact editions/snapshots, viewpoint, scope, and exclusions. |
| source/use statement | Per source: locator, role, recovery profile, receiving use, and currentness or reopening condition; combine this with the boundary for one ordinary package. |
| entries | Local reference, source locator and meaning, difficulty/opportunity, asserted action/change, first result/blocker, existing kind or unresolved status, bounded use, and loss. |
| direct relations | Related subjects, relation, source or evidence basis, truth status, and unresolved condition. |
| occurrence-evidence return, when current | A.3.1.MR or ME.18 result with its own candidate statuses, rival, gaps, held-out question/result, and evidence limits; otherwise the named missing result. Raw observations are not reclassified as documentary Method entries. |
| navigation | Open local sections used only for finding contributions. |
| downstream subjects | Identified Methods and individually scoped accounts with dependency slices for ME.5; a proposed-whole account with its identity/relation boundary for ME.7 when needed. |
| stop and return | Missing source, role, use, comparator, kind, relation, evidence, or the next receiving question. |

Keep these distinctions in the dossier already being used; they are not a requirement for one file or row per field. A short one-source result can carry the source/use statement in its opening sentence.

#### ME.4:4.3 - What Changes in Practice

Practitioners can reuse a Method, retain a candidate account, cite a description, require a capability, preserve an authority stop, or depend on a System without importing a package as a Method whole. A plural dossier also shows why each source was inspected and how far its contribution reaches. Later qualification stays small and source-recoverable; later reconciliation can distinguish a real disagreement from unlike source roles.

### ME.4:5 - Archetypal Grounding — EC-417 Release Assurance Package

Source/use boundary for this constructed case: the EC-417 package snapshot specified below, used as documentary Method guidance for the changed release decision; recover the decision-bearing slice, and return when that package, receiving use, or a relied-on condition changes. This one sentence supplies the ordinary one-source contract.

The EC-417 team receives a “release assurance methodology” containing a stage table, release checklist, supplier procedure, AI prompt, PLM and CI instructions, test-rig guidance, role descriptions, and stored evidence bundles. The receiving decision is whether its Method contributions and candidate reconciliation accounts can support a changed release arrangement.

The dossier uses open sections but preserves unlike kinds:

| Local section | Recovered entries and statuses | Decision-bearing slice |
| --- | --- | --- |
| Methods and candidate accounts | identified `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, `M-Release-Authorize`; candidate `C-Evidence-Reconcile-Internal`, `C-Evidence-Reconcile-Supplier`, `C-AI-Trace-Review`, and proposed whole `C-EC-Release-v2` | Each Method or account keeps its source claims, required inputs/results, support, evidence, and limits. |
| descriptions, representations, and source claims | stage table, release checklist, supplier procedure, AI prompt, bundle records | These epistemes may describe or evidence a Method/account; none is promoted by its section. |
| Systems, support, and access | PLM, CI, test rig, AI provider, and provider-access condition | Availability and access are separate from Method identity and fit. |
| capabilities and assignments | safety competence, supplier-configuration responsibility, and release-authority assignment | Capability, responsibility, and authority are checked for the receiving use. |
| inputs, results, premises, and evidence | pinout schema, evidence bundle, verification result, confidentiality premise, and dated records | Each item keeps its direct kind and use. |
| relations | production/use, schema correspondence `A-17`, provider access, allocation, responsibility, and authority | Each relation is independently stated; no section or package edge supplies parthood. |

Two example dependency slices show why the full package is neither copied nor discarded:

- `M-HW-Verify` travels with its change input, verification-result meaning, rig condition, hardware capability, procedure provenance, and evidence window.
- `C-Evidence-Reconcile-Supplier` travels with the supplier procedure, signed-evidence condition, supplier-configuration responsibility, closure authority, four observed source cases, and the unresolved `A.3.1` identification question.

The supplier procedure's four reported cases remain a documentary source claim and evidence return in this recovery. Inspecting the underlying occurrence records to reconstruct a reusable way is a separate A.3.1.MR question; it does not silently occur inside ME.4.

The four identified Methods and the three individually scoped candidate accounts are potential ME.5 subjects for this use. PLM, rig, competence, authority, schema, evidence, and descriptions remain in their slices under their own kinds. `C-EC-Release-v2` remains a proposed-whole candidate account and may later be resolved by ME.7; its presence in the package creates neither a fifth Method nor `methodPartOf` facts.

#### ME.4:5.1 - Two Documentary Roles and an Interview

This constructed case concerns a change to the release-assurance arrangement. Handbook H, edition 3, section 4, is an accepted maintained synthesis for reconstructing the supplier-evidence practice. Comparison C, edition 2, section 2, is the current comparator for the same receiving decision. Interview I, recorded on day D1, is offered as evidence about what happened during one release. These are local scenario references, not external studies.

| Source/use statement | Source-local contribution retained | Result and return |
| --- | --- | --- |
| H/3 §4; maintained synthesis; full source-local within the supplier-evidence practice; return if that section or the receiving scope changes. | Missing supplier evidence can stop release. The source proposes reconciliation before authorization and names a signed-evidence result. It also names supplier access and authorization conditions. | Recover the reusable-way claim at its existing status with those conditions; preserve access and authority as different subjects. Return to H/3 §4 for its meaning. |
| C/2 §2; current comparator; SoTA-first for this decision; return if a rival or the comparison basis changes. | A separately reviewed evidence bundle is proposed to reduce reliance on one supplier account. Its first result is a reviewed bundle or a named evidence gap. The claim's tested reach is limited to the comparison's cases. | Retain this alternative and its limits separately from H. Do not decide that two differently supported activities are one Method or that either replaces the other. |
| I/D1; occurrence evidence, not a third documentary recovery profile. | The interview reports one release episode but does not yet distinguish a reusable way from a one-off response. | For the one-occurrence question use A.15.1. If several occurrences create a candidate-recovery question, use A.3.1.MR; keep a record-only lower result when that is all the evidence supports. ME.18 is not an automatic next step. |

The first result is the two-source documentary dossier plus the honest occurrence-evidence return, not a merged release Method. A later semantic comparison must decide whether the two documentary contributions overlap, conflict, or complement one another.

If C's full argument becomes unavailable but a page-located excerpt remains, retain the excerpt and reopen only entries whose receiving use depends on the missing context. H's independent source-local result remains usable. Do not turn unavailable support into proof that C was false, or continue a gap-only recovery without its baseline.

### ME.4:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| source-taxonomy bias | Goal, procedure, rationale, framing, mindset, representation, role, or tool becomes a universal Method component kind. | Use those terms as source questions and place each returned claim with its actual subject. |
| diagram-containment bias | A box or lane is read as composition or parthood. | Require the direct relation and its evidence independently. |
| package-authority bias | Institutional or standards status becomes Method identity, fit, or effectiveness. | Separate source authority from the receiving claim and evidence. |
| procedure-only bias | A reusable action is extracted without rationale, applicability, input/result, support, or authority. | Carry the smallest dependency slice that can change qualification. |

### ME.4:7 - Conformance Checklist

- [ ] The dossier names one receiving decision and an exact documentary source boundary, with each relied-on edition or snapshot recoverable.
- [ ] Each source has a use-changing role, recovery profile, source return, and currentness/reopening condition; the one-source case needs only a compact statement.
- [ ] Occurrence-evidence recovery remains with A.3.1.MR and conditional ME.18; returned evidence limits and lower results are preserved.
- [ ] Source-local recovery stops before cross-source sameness, semantic merging, supplier allocation, or pattern-language design.
- [ ] Every selected entry retains its source locator, source meaning, existing kind or unresolved status, bounded use, and loss.
- [ ] Navigation sections can be added, split, or omitted; membership in one does not establish a type.
- [ ] Every direct relation has a source or evidence basis independent of layout.
- [ ] Identified Methods and candidate accounts are distinguishable from descriptions, Systems, capabilities, assignments, evidence, and relations.
- [ ] Every ME.5 subject carries the smallest provenance-preserving dependency slice needed for judgement.
- [ ] Missing source access, kind, relation, or evidence remains visible.
- [ ] No package, chapter, list, view, or section creates Method candidacy, family membership, composition, or `methodPartOf`.

### ME.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Six local sections become six ontology kinds. | Call them open navigation and keep each entry's existing kind. |
| Everything actionable becomes a Method candidate. | Require a reusable way-of-doing account; keep support, capability, evidence, and authority under their direct kinds. |
| The package is reduced to a procedure. | Recover rationale, framing, intended use, inputs/results, support, evidence, and authority only where they change the receiving decision. |
| The whole package is copied for provenance. | Attach a bounded dependency slice to each Method/account and retain a source return to the package edition. |
| Unknown relation is inferred from adjacency. | Record the relation as unresolved and state what observation or source would settle it. |

### ME.4:9 - Consequences

The package becomes selectively reusable while its provenance and the kinds of its contributions remain explicit. Later qualification can inspect one Method or account together with the dependencies that make its use meaningful.

The cost is explicit kind and relation recovery. Some familiar package headings will disappear from the action path, while important support, authority, or evidence conditions may become more visible than the source's headline procedure.

### ME.4:10 - Architectural Rationale

A heavyweight package is a publication and practice carrier, not evidence that its visible organization is a Method structure. Preserving unlike kinds lets several useful representations coexist without forcing one-to-one correspondence among Method, Work, subject, description, capability/provider/support, allocation, and cultural structures.

The dossier is deliberately open. Its value lies in tracing source contributions to the receiving decision and retaining their dependency slices, not in a fixed number of sections or a universal element taxonomy.

### ME.4:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Daalhuizen and Cash, [Method Content Theory](https://doi.org/10.1016/j.destud.2021.101018) | Goal, procedure, rationale, framing, and mindset as questions that prevent procedure-only recovery. | Static content variables and initial study population do not define FPF kinds, Method parts, or cross-domain effectiveness. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Core idea, representation, procedure, intended use, tool, ecosystem, and adaptation prompts. | Source elements remain questions and source claims, not a universal dossier ontology. |
| Stacey et al., [Methods as a form of engineering knowledge](https://doi.org/10.1017/dsj.2025.9) | Current comparison of engineering-Method knowledge and the placement of representations, framing, and rationale. | Conceptual comparison supplies no project Method identity or package parthood. |
| Current FPF `A.3.1`, `A.3.2`, `B.1.5`, and `F.18` | Method identity, MethodDescription membership, composition law, and name recovery. | The DPF adds the decision-bounded dossier and dependency-slice Method. |

Reopen when a current source or package case exposes a decision-bearing contribution that cannot retain its kind, provenance, role, and relation in the open dossier; when a source profile hides material receiving conditions; or when the ordinary one-package result acquires burden that its use does not need.

### ME.4:12 - Relations

- A.3.1.MR governs candidate recovery from occurrence evidence; ME.18 supplies its specialist continuation only when needed. Documentary claims about evidence remain distinct from those recovery results.
- Cross-source reconciliation and allocation consume the dossier later. ME.4 preserves the inputs and return paths but does not settle that next semantic question.
- `A.3.1` governs Method identity; `A.3.2` governs MethodDescription claims; `B.1.5` governs Method composition; `F.18` governs durable name claims.
- ME.1 supplies the focus and receiving decision when package recovery is the chosen next result. ME.2 may supply an inherited repertoire or source lineage.
- ME.5 receives identified Methods and individually scoped candidate accounts with provenance-preserving dependency slices. It does not receive the local navigation sections as types or a proposed whole merely because the package presents one.
- ME.6 receives only a several-structure synthesis question that remains after individual qualification.
- ME.7 receives a proposed whole account when its identity and relations must be resolved.

### ME.4:End

# Part II - Individual Qualification and Method-Architecture Alternatives

## ME.5 - Qualify Individual Methods, Candidate Accounts, and Local Connections

>
> **Primary working result:** one **status-preserving individual qualification** for each selected Method or candidate Method account, plus only those local input/result, schema-correspondence, or adapter-feasibility claims that can be judged without choosing a whole architecture.

### ME.5:0 - Use This When

Use this pattern when a project has one or more Methods identified under `A.3.1`, candidate Method accounts, and situational criteria, but it still does not know which subjects are individually usable for the bounded result. Use it before a several-structure comparison when a weak subject can be rejected cheaply on its own.

Begin with one Method or candidate account, its status, the contribution it is expected to make, and the criteria that matter for that contribution. Keep whole-level allocation, synchronization, composition, and compatibility questions outside the individual result.

The first useful result says one of the following: an identified Method is qualified or not qualified for the bounded use; a candidate account is retained or excluded while its Method-identification question remains open; or a local connection claim is supported, unsupported, or unresolved independently of a whole synthesis.

Do not use qualification wording to admit a candidate account as a Method, to establish compatibility or parthood, or to declare a Method architecture fit.

### ME.5:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| identified Method subject | A Method already identified under `A.3.1`; ME.5 judges bounded use without repeating identity. |
| candidate-account subject | An episteme about a possible Method whose unresolved identity conditions remain visible throughout qualification. |
| individual contribution | The result or preserved condition attributable to this subject under the stated use, not the success of a whole arrangement. |
| local connection | An input/result, schema-correspondence, or adapter-feasibility claim whose truth does not depend on choosing one whole synthesis. |
| individual qualification | A bounded result covering contribution, applicability, inputs/results, attributable time or burden, capability, support, authority/access, evidence, source limits, and stop. |
| architecture question | A claim about combined allocation, timing, composition, Work overlap, provider arrangement, authority distribution, or another several-structure relation. It belongs to ME.6 when live. |

### ME.5:1 - Problem Frame

Method-selection literature correctly emphasizes situation and fit, but real project candidates arrive at unlike epistemic states. One is an identified Method with known use evidence, another is a candidate account recovered from Work records, and a third phrase refers only to a tool or support condition.

Individual qualification can save architecture effort by rejecting a candidate that cannot produce the required result or cannot meet one non-negotiable condition. It becomes misleading when it averages several Methods and support arrangements into one fit score or upgrades an account through confident language.

### ME.5:2 - Problem

Three errors recur. First, a retained candidate account is called a qualified Method. Second, one independently feasible schema mapping is called compatibility of the whole package. Third, a combined peak-load or authority conflict is hidden inside separate “passes” for each Method.

The project then believes the architecture problem is solved even though no result states how the individually plausible subjects work together.

### ME.5:3 - Forces

| Force | Tension |
| --- | --- |
| Cheap rejection | Individual defects should stop early, while whole conflicts must remain visible for ME.6. |
| Status preservation | Candidate accounts need useful assessment, while qualification cannot identify their Methods. |
| Comparable questions | A common set of questions aids choice, while not every question applies to every subject. |
| Evidence proportionality | A bounded use may need little evidence, while safety, authority, or high burden can require stronger support. |
| Local connections | A schema or adapter can be tested independently, while its placement and maintenance belong to a whole synthesis. |

### ME.5:4 - Solution

Qualify one subject at a time against the bounded receiving use. Preserve status, expose unsupported conditions, and route only genuinely combined questions to ME.6.

#### ME.5:4.1 - Pattern-Use Unfolding

1. **State the subject and status.** Name the identified Method or candidate account and cite the identity or account basis already available. Reject unlike support facts as qualification subjects.
2. **Bind the use.** State the receiving Work or result, situation family, scope, time window, non-negotiable criteria, acceptable variation, and decision that will consume the qualification.
3. **Recover the individual contribution.** Name the input, result or preserved condition, procedure or invariant as far as known, applicability, and important source meaning. Do not credit the subject with another Method's result.
4. **Check attributable conditions.** Inspect timing and burden attributable to this subject; performer capability; support and provider access; authority or responsibility; evidence; and source or transfer limits.
5. **Test local connections only.** Check an input/result handoff, schema correspondence, or adapter feasibility when it can be supported independently. Record its scope and failure case.
6. **Return the truthful branch.** An identified Method is qualified or not qualified for the bounded use. A candidate account is retained or excluded *as an account*, with unresolved identification conditions unchanged. A local connection is supported, unsupported, or unresolved.
7. **Choose the stop.** Stop after one usable Method, one retained account, or several independently usable subjects when no whole question remains. Enter ME.6 only when a several-structure choice can change the decision.

#### ME.5:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| subject and status | Method identity or candidate-account reference and the status that remains after qualification. |
| bounded use | Receiving result or Work, situation, scope, window, criteria, and consuming decision. |
| contribution | Inputs, result or preserved condition, known procedure/invariant, applicability, and variation. |
| attributable conditions | Time/burden, capability, support/provider access, authority/responsibility, evidence, and source limits attributable to this subject. |
| local connections | Independently tested input/result, schema, or adapter claims with scope and status. |
| verdict and stop | Qualified/not-qualified Method or retained/excluded account, open identity conditions, remaining whole question, and next action. |

#### ME.5:4.3 - What Changes in Practice

Teams stop scoring a methodology bundle as one object. They can reject one Method, retain a promising account without admitting it, and prove one schema mapping without calling the whole arrangement compatible. ME.6 then receives only the genuinely combined timing, allocation, support, authority, or composition questions.

### ME.5:5 - Archetypal Grounding — EC-417 Individual Stops

The EC-417 dossier supplies four identified Methods and several candidate accounts. The bounded use is a safety-relevant release arrangement in which signed evidence must exist before safety closure, confidential supplier geometry must stay outside the AI provider, and decision Work remains with admitted human Systems under separate covering assignments and permission or direct decision-authority relations.

| Subject and prior status | Individual result | ME.5 return |
| --- | --- | --- |
| `M-HW-Verify`, identified Method | accepts the affected change and pinout version; produces a verification result with named rig and hardware capability conditions | qualified for the bounded use |
| `M-SW-Integrate`, identified Method | accepts explicitly versioned provisional or signed pinout evidence; its integration record preserves the exact edition, any provisional uncertainty, and the edition actually used; later signed evidence supersedes a provisional edition only for safety-closure reliance while the earlier use and provisional-to-signed relation remain traceable; software remains reversible until `D-1` | qualified under the evidence-version, history, closure-reliance, and reversibility conditions |
| `M-Supplier-Approve`, identified Method | produces signed supplier approval or the explicit missing-approval stop; requires supplier-configuration responsibility and evidence access | qualified under the named access and responsibility conditions |
| `M-Release-Authorize`, identified Method | consumes the safety result and named evidence conditions; admitted human System `ReleaseDecider-17` performs `W-ReleaseDecision-17` under covering assignment `ASG-ReleaseDecision-17` and independently supported direct relation `AUTH-ReleaseDecision-17`; returns release, withhold, or next-slot authorization | qualified for the bounded Work, assignment, and authority scope; none proves the others |
| `C-Evidence-Reconcile-Internal`, candidate account | eight internal cases support an account in which the versioned provisional edition, uncertainty, and earlier integration use remain traceable through reconciliation to later signed evidence before closure | retained as a candidate account; `A.3.1` identification remains open |
| `C-Evidence-Reconcile-Supplier`, candidate account | four supplier-originated cases and one held-out supplier case support a signed-evidence branch | retained as a candidate account; `A.3.1` identification remains open |
| `C-AI-Trace-Review`, candidate account | the account specifies a trace-suggestion contribution; `TraceReviewer-17` performs the accept/reject Work under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17`, while the AI provider holds neither | retained as a human-governed candidate account |

The `provider-default AI proposal` is rejected at the ME.5 entry boundary rather than qualified: no identified Method or candidate Method account has been supplied for it. It would disclose confidential geometry and names no admitted human decision performer, covering assignment, or permission/authority relation, so those facts prevent treating it as a candidate account for this use.

Local schema correspondence `A-17` maps signed or explicitly provisional pinout-version fields to the integration bundle and preserves the exact edition and uncertainty used. Five stored bundles support that mapping for the named schema editions. The mapping preserves the provisional basis after later signed evidence becomes the safety-closure basis. This is a local connection result, not whole compatibility.

Two honest stops are now available. A project needing only hardware verification can stop with the qualified `M-HW-Verify`; no architecture comparison is required. A project investigating supplier reconciliation can stop with the retained `C-Evidence-Reconcile-Supplier` account and its open `A.3.1` question. EC-417 continues to ME.6 only because the combined safety allocation, board timing, evidence routing, and recovery burden differ among whole alternatives.

### ME.5:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| fit-score bias | Unlike contribution, capability, authority, evidence, and burden claims collapse into one number. | Return the decision-changing conditions and truthful branch instead of an opaque total. |
| candidate-upgrade bias | “Qualified candidate” is read as identified Method. | Repeat the account status in the verdict and state the open `A.3.1` condition. |
| compatibility bias | One feasible handoff or schema mapping becomes whole fit. | Call it a bounded local connection and route combined questions to ME.6. |
| decomposition bias | Each support System, role, or evidence item is evaluated as a Method candidate. | Accept only identified Methods and candidate Method accounts as qualification subjects. |

### ME.5:7 - Conformance Checklist

- [ ] Every subject is an identified Method or a candidate Method account and keeps that status.
- [ ] The qualification names one receiving use, scope, situation, window, and consuming decision.
- [ ] Contribution, inputs/results, applicability, attributable burden, capability, support, authority/access, evidence, and source limits are checked as applicable.
- [ ] No subject receives credit for another Method or whole arrangement's result.
- [ ] Local connection claims are independently testable and bounded.
- [ ] A candidate-account verdict preserves unresolved `A.3.1` identification conditions.
- [ ] Whole allocation, synchronization, composition, provider, and architecture questions remain explicit rather than hidden in individual verdicts.
- [ ] The result states whether to stop, reject, retain, or enter ME.6.

### ME.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “This account fits, so it is a Method.” | Retain or exclude the account and send identity to `A.3.1`. |
| “All individual Methods pass, so the architecture is compatible.” | State the unresolved combined structure and use ME.6 only when it changes the decision. |
| “The adapter works, so integration is solved.” | Bound the adapter-feasibility result; compare placement, versioning, responsibility, and failure in ME.6. |
| “Use the same checklist for every subject.” | Ask only applicable questions but preserve the common result positions needed by the decision. |
| “More evidence is always safer.” | Select evidence by consequence and claim; stop when the bounded decision can be made honestly. |

### ME.5:9 - Consequences

Weak subjects fail early, promising accounts remain usable without ontological promotion, and local handoffs become inspectable. Architecture comparison is smaller because it receives only retained subjects and unresolved combined questions.

The cost is refusal to publish one convenient compatibility score. A project may receive several qualified individual results and still have no acceptable synthesis.

### ME.5:10 - Rationale

Individual suitability and whole architecture answer different questions. A Method can be usable alone yet overload a shared Agent when combined with others. A candidate account can be useful evidence for design while still failing Method identification. Keeping the individual and architecture results separate protects both cheap stops and escalation when combined questions remain.

### ME.5:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Henderson-Sellers and Ralyté, [Situational Method Engineering review](https://opus.lib.uts.edu.au/handle/10453/13456) | Situational construction, selection, and adaptation questions. | Source-local fragment and process ontologies do not determine FPF subject status. |
| Daalhuizen and Cash, [Method Content Theory](https://doi.org/10.1016/j.destud.2021.101018) | Goal, procedure, rationale, framing, and mindset questions relevant to individual content and use. | These variables do not become universal qualification dimensions or Method parts. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Intended use, scope, representation, procedure, tool, ecosystem, and adaptation conditions. | Conceptual elements guide questions; current project evidence supplies the verdict. |
| Current FPF `A.3.1`, `C.18`, and `G.5` | Method identity, candidate generation when needed, and bounded family/selector results. | ME.5 adds status-preserving individual qualification and the local-connection boundary. |

Reopen when a current source or use shows that an individual question cannot be judged without a named whole structure, or when a repeated ME.6 finding can be prevented by one affordable individual check.

### ME.5:12 - Relations

- ME.3 or an applicable domain result supplies situational criteria; ME.4 or another lawful route supplies identified Methods/accounts and dependency slices. Neither named predecessor is compulsory when equivalent content exists.
- `A.3.1` alone governs Method identification. ME.5 does not admit Methods.
- ME.6 receives retained subjects only when combined Method, Work, allocation, support, description, subject, or cultural structures change the decision.
- ME.7 resolves a proposed whole; ME.5 qualification supplies no whole identity, compatibility, or `methodPartOf` fact.
- `C.11` or the applicable domain decision Method consumes the bounded individual results when a choice is live.

### ME.5:End

## ME.6 - Compare Method-Architecture Alternatives and Simultaneous Enactment Conflicts

>
> **Primary working result:** a **Method-architecture decision episteme** that names the few decision-changing structures, their direct relations and truth statuses, materially different alternatives, moved burdens, selected or rejected synthesis, and a realization or reconsideration test. It may truthfully stop with relations among several Methods and no composite whole.

### ME.6:0 - Use This When

Use this pattern when individually plausible Methods or candidate accounts could be combined or co-used in materially different ways and the receiving result depends on their composition, Work overlap or order, allocation, subject/support arrangement, descriptions, provider access, or cultural relations.

Begin with the obtaining or possible-future practice and one result at risk. Name the exact structures and relations that can change the decision. Do not call them all a graph: a mathematical graph is one possible representation only when its nodes, edges, semantics, and use are selected. In ordinary cases use the exact names—Method structure, Work structure, allocation structure, subject/support structure, description structure, or cultural relation.

The first useful result compares at least two serious syntheses and exposes both local gains and burdens moved across participants, scopes, Systems, or times. It can select one bounded trial, preserve an incumbent, request a probe, or stop with a relation-only result.

Do not repeat ME.5. If the only question is whether a named relation or Method composite is actually supported, clarify that claim through `C.30` or `B.1.5` and stop; there is no ME.6 comparison to complete until a materially different arrangement could change the decision. Do not invent a rival just to enter this pattern. Do not treat project, process, case, lifecycle, table, or diagram views as architecture alternatives unless their underlying proposed relations actually differ.

### ME.6:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| Method structure | Identified Methods and direct composition, specialization, family, participation, or other selected Method relations with stated truth status. |
| Work structure | Admitted or intended Work and direct parthood, overlap, order, result-use, or transformation relations. Work order does not by itself establish Method composition. |
| allocation structure | Responsibility, authority, capability demand, provider dependence, shared capacity, and burden distribution relevant to the alternatives. |
| subject/support structure | Project Systems, enabling Systems, resources, access, provider, and support relations whose configuration changes the result. |
| description structure | Epistemes, views, schema correspondences, version relations, and losses used by the decision. Description order is not Work order. |
| cultural relation | Recognition, transmission, selection, retention, or loss of a Method variant. A chosen project option is not cultural continuation. |
| simultaneous multigrain contribution | Several Methods or Work occurrences contribute at different grains during overlapping intervals without becoming parts of one composite Method. |
| genuine first–then condition | One direct Work, result-use, transformation, evidence, configuration, or authority relation makes a later occurrence or decision depend on an earlier result or condition. |
| architecture alternative | A possible-future synthesis whose named relations differ materially. Until realized or independently shown to obtain, it remains proposed. |

### ME.6:1 - Problem Frame

R7 presents a connected account of Methods, Work, descriptions, capability, tools, variants, and simultaneous contribution at several grains. R10 shows that project, process, and case management can produce different views of one Work. Together they warn against one universal stack: several useful structures can coexist without lining up one-for-one.

A project still needs decisions. It must choose which provisional results may be used, which Work may overlap, where authority stays, which support arrangement is acceptable, and where burden moves. The comparison must preserve the several structures while remaining small enough to act on.

### ME.6:2 - Problem

A one-stack account turns Method composition, Work order, organization, capability, provider support, and description layers into one hierarchy. An account built from views treats different depictions of the same relations as different architectures. A local-optimization account celebrates faster integration while moving preparation, assurance, maintenance, or recovery burden to another Agent or interval.

The decision then asserts an obtaining architecture before its relations exist, or misses a genuine first–then guard because “everything is concurrent”.

### ME.6:3 - Forces

| Force | Tension |
| --- | --- |
| Useful pluralism | Several structures expose different conflicts, while too many views bury the choice. |
| Overlap and order | Simultaneous contribution can shorten feedback, while evidence, configuration, or authority may require a real order. |
| Local and total burden | One participant can gain time, while another inherits peak load, access, or recovery Work. |
| Truth status | Proposed relations are useful for design, while they cannot be reported as obtaining architecture. |
| Composite temptation | Co-use invites a memorable whole name, while no Method whole exists without identity and obtaining relations. |

### ME.6:4 - Solution

Select only structures that change the decision, state their direct relations and truth statuses, compare serious syntheses on one bounded basis, and return an architecture decision with explicit realization or reconsideration conditions.

#### ME.6:4.1 - Pattern-Use Unfolding

1. **Bound the practice and result.** State whether the account concerns obtaining practice or a possible-future trial, the result at risk, configuration, situation, window, and decision authority.
2. **Load retained subjects.** Bring in identified Methods, candidate accounts, and individually supported local connections. Preserve every status and unresolved condition.
3. **Select decision-changing structures.** Name each Method, Work, allocation, subject/support, description, capability/provider, or cultural structure needed. Omit a structure whose possible values cannot change the choice.
4. **State relations and truth.** For every load-bearing relation, record its kind, subjects, obtaining, proposed, contradicted, or unresolved status, evidence, and receiving use. Record correspondences and losses across descriptions without making them identities.
5. **Build serious alternatives.** Create at least two syntheses that differ in one or more named relations. Preserve the feasible incumbent. A different view or label is not another alternative.
6. **Compare enactment and burden.** Distinguish simultaneous multigrain contribution from genuine first–then Work; compare combined peak demand, provider/access dependencies, authority, responsibility, evidence creation and loss, failure routes, and burdens moved across scopes or times.
7. **Choose without upgrading truth.** Use `C.11` or an applicable domain decision Method. Return the selected synthesis, rejected alternatives, accepted losses, conditions, live rivals, and any causal-use boundary. A bounded trial decision can select proposed content without asserting that its ArchitectureRelations obtain.
8. **Realize or reconsider.** Name implementation and trial Work separately, the observations that could support or defeat proposed relations, recovery or stop, and the condition for preserving, narrowing, or reopening the decision.

#### ME.6:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| decision boundary | Obtaining or possible-future practice, result, situation, configuration, window, authority, and use. |
| retained subjects | Methods, candidate accounts, local connections, and unchanged status. |
| selected structures | Exact structure names, direct relations, truth statuses, correspondences, losses, and evidence. |
| alternatives | At least two serious syntheses and the named relations by which they differ. |
| comparison | Simultaneous and first–then conditions, allocation, capacity, provider/access, authority, failure routes, evidence, moved burdens, and causal-use limits as applicable. |
| decision | Selected/rejected synthesis, basis and rule, accepted losses, preserved constraints, and remaining rivals. |
| continuation | Realization/test Work, stop or recovery, observations, and reconsideration condition. |

#### ME.6:4.3 - What Changes in Practice

Teams stop choosing a Method stack or a preferred diagram. They choose which direct relations should hold for one result, which structures expose the conflict, and who carries the burden. Co-used Methods can remain plural; a proposed architecture can guide a trial without being reported as already real.

### ME.6:5 - Archetypal Grounding

#### ME.6:5.1 - Cheaper Clarification: Several Methods, No Composite

In a safety-relevant release, `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, and `M-Release-Authorize` are identified Methods. Hardware verification and software integration can contribute during overlapping intervals from differently versioned evidence. Supplier approval produces a signed result later. Release authorization uses the safety result and signed-evidence condition.

The selected structures are:

| Structure | Direct relation and truth |
| --- | --- |
| Method structure | Four Methods are co-used; no `methodPartOf` or composite-Method relation is shown to obtain. |
| Work structure | Some verification and integration Work may overlap; bounded Work set `W-TraceAcceptReject-17` contains one human accept/reject occurrence for every AI suggestion used by the branch; signed evidence and accepted safety result are genuine first–then guards for release authorization. |
| description structure | project, process, and case views describe the same release Work while foregrounding schedule, recurring controls, and one release's state; none is an architecture alternative. |
| allocation structure | admitted Systems `TraceReviewer-17`, `SafetyReviewer-17`, and `ReleaseDecider-17`; their decision Work; covering assignments `ASG-TraceReview-17`, `ASG-SafetyReview-17`, and `ASG-ReleaseDecision-17`; permission `PERM-TraceAcceptReject-17`; and direct authorities `AUTH-SafetyEvidence-17` and `AUTH-ReleaseDecision-17` remain separate; shared capacity can constrain later alternatives. |

`ARS-EC417-RelationOnly-1` records the smaller clarification: retain the four Methods and their direct result-use, permission, and authority relations without naming a composite. The question here is only whether co-use supports a Method-whole claim. `B.1.5` supplies the composition test; where an architecture claim is made, `C.30` distinguishes the claimed structure from obtaining relations. No composite is established by the evidence shown, and no rival arrangement is at issue. Stop with that clarification, not a completed ME.6 comparison. A later choice about provisional supplier evidence opens the genuine alternatives in :5.3; their comparison can also end without creating a Method whole.

#### ME.6:5.2 - Simultaneous Multigrain Contributions with Local First–Then Relations

In a separate five-day Method Engineering case, `ME-W0` is the bounded project adaptation Work. `ME-W1` repertoire-recovery Work, `ME-W2` candidate-account formation Work, `ME-W3` description/tool-proposal Work, and `ME-W4` evaluation Work are parts at the next finer grain; trial Work `ME-W7` is part of `ME-W4`. During the same five-day interval, continuing product-engineering Work `ME-W5` and repository-maintenance Work `ME-W6` overlap `ME-W0` but are not its parts.

The repertoire-recovery Method contributes through `ME-W1`, candidate-account formation through `ME-W2`, description/tool proposal through `ME-W3`, and trial/evaluation Methods through `ME-W7` and `ME-W4`. Product-engineering and repository-maintenance Methods contribute concurrently through `ME-W5` and `ME-W6`. These are contributions at whole-Work, part-Work, nested trial-Work, and separate overlapping-Work grains, not one level sequence.

Two case-local first–then relations remain inside that simultaneous interval: `ME-W1` precedes `ME-W2`, and `ME-W3` precedes the relevant evaluation decision in `ME-W4`. Temporal overlap across the other grains erases neither relation. It establishes neither a universal Method stack nor `methodPartOf`; a teaching tree that presents recovery before evaluation is a description view, not the Work structure.

#### ME.6:5.3 - Possible-Future Alternatives: A, B, and B2
The EC-417 release scenario later asks how to handle provisional supplier evidence. Three alternatives differ by Work order and allocation:

| Alternative | Work and allocation structure | Capacity and consequence |
| --- | --- | --- |
| A | wait for signed evidence before software integration; one final board | prospective pre-entry alternative; under baseline signed evidence at `D-8`, misses the `D-21` integration slot |
| B | integrate from an explicitly versioned provisional edition at `D-21`, preserve that basis and uncertainty, and reconcile it to signed evidence at `D-8`; safety engineer performs all `2.00 h` signed-delta preparation | on the `D-8` peak day: `2.00 + 0.33 + 2.07 = 4.40 h`, or `0.55` of an eight-hour day; exceeds the `0.40` limit |
| B2 | same Work order and evidence-history rule as B; supplier-configuration role performs `1.60 h` of preparation and safety performs `0.40 h` | on `D-8`: `0.40 + 0.33 + 2.07 = 2.80 h`, or `0.35`; the separate `D-21` board makes per-release safety burden `3.13 h` rather than B's `4.73 h` |

The first 20-minute board is on `D-21`; the second is on `D-8`. They occur on different days. The peak-day comparison and per-release burden are separate measures. Each board remains below the 45-minute meeting limit. Under B or B2, signed evidence supersedes the provisional edition only for safety-closure reliance; the provisional edition, uncertainty, use in `D-21` integration Work, and relation and delta to the signed evidence remain traceable.

`CUR-EC417-CadenceEffect-1` returns `unsupported` for the interventional claim that earlier reconciliation reduces reopenings. `AD-EC417-B2-Trial-1` therefore consumes no positive causal premise. It consumes separately named non-causal `DC-EC417-CadenceMismatch-1`, the capacity comparison, confidentiality, the covering trace/safety/release assignments, `PERM-TraceAcceptReject-17`, the two independently supported direct authority relations, and reversibility to choose only three bounded B2 trials.

At the `D-21` pre-entry checkpoint, `ReleaseDecider-17` performs the branch decision under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17`, after the required safety-evidence decision under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17`. B2 entry also requires `TraceReviewer-17` to perform `W-TraceAcceptReject-17` under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17` for every AI suggestion used by the branch.

Before entry, choose A when signed evidence is already available or when versioned provisional evidence, supplier preparation, confidentiality, the trace-review assignment or permission, or a safety/release assignment or authority condition for B2 is absent. Once early B2 integration has occurred, A is no longer a possible history for that release.

Missing signed evidence at `D-8` withholds release and starts recovery R. Preserve the performed integration record, exact provisional edition, uncertainty, and earlier use. When signed evidence arrives, record its relation and delta to the provisional edition, re-baseline, and repeat the comparison and affected verification. Retain or roll back/repeat early integration. Record `1.60 h` supplier plus `2.80 h` safety burden and any additional rework separately. Move only to the next authorized slot after repeated decision Work under the covering assignments and authority relations. Every repeated AI suggestion again requires the trace-review Work, assignment, and permission. Signed evidence supersedes provisional evidence for closure reliance without erasing the provisional history.

The architecture decision remains prospective. Implementation and the three trial releases are later Work. If signed evidence becomes available at `D-21`, sensitivity selects A prospectively; it does not rewrite a past B2 release.

### ME.6:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| universal-stack bias | Method, Work, support, allocation, description, and culture become one level sequence. | Name each selected structure and direct relation separately. |
| visual-representation bias | A diagram or mathematical graph is treated as the architecture. | State the structure and relation semantics first; choose a representation only for a named use. |
| concurrency bias | Overlap erases result-use, evidence, configuration, or authority guards. | Identify genuine first–then conditions directly. |
| local-efficiency bias | Reduced effort in one role hides burden moved to another role or interval. | Show combined peak and total burdens with receiving scopes. |
| trial-as-reality bias | A selected possible-future synthesis is reported as obtaining practice. | Keep decision, implementation Work, trial Work, observations, and relation truth distinct. |

### ME.6:7 - Conformance Checklist

- [ ] The result names one obtaining or possible-future practice, receiving result, and decision boundary.
- [ ] Every Method and candidate account keeps its prior status.
- [ ] Every selected structure can change the decision and is named by its actual structure or relation kind.
- [ ] Project, process, case, lifecycle, table, diagram, and mathematical representations remain views unless their underlying relations differ.
- [ ] Method composition, Method unfolding, Work parthood, Work overlap, first–then guards, allocation, support, description, and cultural relations remain separate.
- [ ] At least two serious alternatives differ in named relations and include the feasible incumbent when applicable.
- [ ] Combined capacity, covering assignments, permission, authority, provider/access, evidence, failure routes, and moved burdens are visible where material.
- [ ] Causal-use results are consumed only within their verdict boundary.
- [ ] A possible-future decision asserts no obtaining ArchitectureRelation.
- [ ] The result states realization/test Work, stop or recovery, and reconsideration condition.

### ME.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “All methods are layers in one stack.” | Select and name the actual Method, Work, allocation, support, description, and cultural structures. |
| “These two diagrams are alternatives.” | Compare the underlying relation sets; if they are the same, keep them as views. |
| “Work overlaps, so the Methods compose.” | State Work overlap and require independent Method identity and composition evidence. |
| “B2 saves 1.60 hours.” | Name the role and interval from which burden leaves and the role or interval that receives it. |
| “The trial choice proves the architecture.” | Keep proposed relations, decision, trial Work, observations, and later obtaining claims distinct. |
| “Recovery means switching to the earlier alternative.” | Preserve already-performed Work and define a separate post-entry recovery branch. |

### ME.6:9 - Consequences

Architecture choices become precise enough to implement and reconsider without forcing one universal decomposition. Genuine guards survive concurrency, co-use survives without a fictitious composite, and moved burden is visible before local optimization is accepted.

The cost is explicit recovery of several structures and their truth statuses. Some attractive alternatives will remain only proposed, and a clean relation-only stop may be more truthful than a new Method whole.

### ME.6:10 - Rationale

Method organization, dated Work, subject arrangement, allocation, descriptions, provider support, and cultural continuation answer different questions. Treating them as isomorphic loses either useful simultaneous contribution or real dependency. Selecting only decision-changing structures preserves R7's connected synthesis without turning it into one stack.

R10's project/process/case example adds a practical test: when several views concern the same Work, their labels do not create architecture alternatives. The alternatives begin only where proposed direct relations differ.

### ME.6:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| R7 Methodology guide | Simultaneous multigrain contribution, Method/Work/description/capability/tool distinctions, and several representations. | Stack and tree metaphors are prompts; use exact structures and relations in the receiving case. |
| R10 Systems Management, R10.7:1–2 | Complementary project, process, and case viewpoints on one Work. | View plurality supplies no new Work, Method, or architecture alternative. |
| Current FPF `C.32.MWA`, `C.30`, `A.22`, and `B.1.5` | Several-structure synthesis, architecture truth, selected structure, and Method composition. | ME.6 supplies the specialist Method-architecture comparison and bounded decision. |

Reopen when a representative use exposes another non-isomorphic structure that can reverse the decision, a moved burden remains systematically hidden, or an alternative cannot be realized without changing the selected relation set.

### ME.6:12 - Relations

- ME.5 supplies individually qualified Methods/accounts and whole-independent local connections; it supplies no whole compatibility result.
- `A.22`, `C.30`, `C.32.MWA`, and `B.1.5` govern selected structures, architecture truth, several-structure synthesis, and Method composition.
- `C.11` or the applicable domain decision Method governs the bounded choice; `C.28` governs any causal conclusion consumed.
- ME.7 resolves one proposed Method whole. A relation-only ME.6 result may stop without entering ME.7.
- ME.19 may supply a differentiation account and separate causal-use result. ME.6 consumes only the causal reliance allowed by its verdict and keeps its own decision authority.

### ME.6:End

## ME.7 - Resolve a Proposed Method Whole into Obtaining Relations or a Candidate Account

>
> **Primary working result:** either a bounded composition result whose whole, participants, and load-bearing relations are independently supported, or a **prospective candidate Method account** with proposed relation sets, guards, variation, recovery, stops, and a realization/test WorkPlan. Writing the account creates neither the Method nor an obtaining architecture.

### ME.7:0 - Use This When

Use this pattern when a proposal already names an intended Method whole—often a methodology, operating model, playbook, integrated process, or local way of working—and the next decision needs to know what can truthfully be said about that whole now.

Begin with the proposal's intended result, participants, relation claims, guards, burdens, unresolved conditions, and selection reason. Recover the whole semantics needed for identification before choosing the result branch.

The first useful result is deliberately two-branched. If the whole and participant Methods are identified and the required relations are shown to obtain, record the bounded composition result. Otherwise return the strongest prospective account or lower claim that the evidence supports, together with the Work that could realize and test it.

Do not require prior performance of ME.6 when equivalent proposal content is already available. Do not treat a coherent description, selected architecture, WorkPlan, tool implementation, or successful first trial as Method construction or identification by itself.

### ME.7:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| proposed Method whole | A claim that several contributions form one reusable Method for a stated use. It may be no more than a candidate account. |
| whole semantics | Intended result or preserved condition, reusable procedure or invariant, applicability, participants, permitted variation, bounds, and reidentification rule. |
| participant status | Whether each named participant is an identified Method, candidate account, other kind, or unresolved subject. |
| obtaining composition result | A result about an identified whole and identified participant Methods whose required `B.1.5` relations are independently shown to obtain for the bounded claim. |
| prospective candidate account | An episteme proposing a possible reusable whole while identity or relation conditions remain unresolved. |
| relation set | Named proposed or obtaining composition, order, result-use, allocation, support, authority, or other relations. Their truth statuses remain explicit. |
| realization/test WorkPlan | A plan for later Work that could implement the proposal and return observations. It is not performed Work or evidence that the Method exists. |

### ME.7:1 - Problem Frame

Method Engineering often produces coherent proposals before the proposed practice exists. Situational Method Engineering and design-Method research offer useful construction and adaptation moves, while FPF keeps the proposed account, world-side Method, MethodDescription, WorkPlan, performed Work, and obtaining relations distinct.

A proposed whole can still be valuable. It can state an invariant, guards, variants, participant roles, stops, and a bounded trial. The error is reporting possible-future content as already obtaining.

### ME.7:2 - Problem

One failure declares a whole whenever a document gives several steps a shared name. Another refuses to state anything useful until a mature Method has already been identified. A third treats participant co-use, Work order, or a successful tool integration as `methodPartOf` evidence.

The first error overclaims, the second prevents learning, and the third confuses several relation structures. ME.7 needs a positive lower branch that supports realization while keeping uncertainty explicit.

### ME.7:3 - Forces

| Force | Tension |
| --- | --- |
| Useful proposal | A project needs a coherent possible-future account, while coherence does not identify a Method. |
| Composition evidence | Participant Methods and relations may be supported unevenly, while one missing load-bearing relation can defeat the whole claim. |
| Variation | A reusable Method permits bounded variation, while unlimited adaptation destroys reidentification. |
| Trialability | A WorkPlan can make uncertainty testable, while planned or performed Work does not backdate Method existence. |
| Honest lowering | A lower result must remain actionable, while it cannot hide unresolved identity or relation claims. |

### ME.7:4 - Solution

Recover the proposed whole's semantics, test whole and participant identity separately from relation truth, and return the strongest branch the evidence supports.

#### ME.7:4.1 - Pattern-Use Unfolding

1. **Name the receiving use.** State the result or preserved condition, situation family, intended users or performers, consuming decision, configuration or edition, and time window.
2. **Recover whole semantics.** State the reusable operations or invariant, entry and exit, applicability, participants, permitted variation, bounds, stops, and reidentification rule. If these cannot be stated, return the missing-account question.
3. **Preserve participant statuses.** Identify each Method under `A.3.1` where supported. Keep candidate accounts and other subjects at their existing statuses.
4. **Name the relation sets.** State every load-bearing proposed or obtaining relation, including Method composition, Work order or overlap, result use, allocation, support/provider access, authority, and description correspondence as applicable. Do not infer one relation from another.
5. **Test the positive branch.** Record an obtaining composition only when the whole and parts are identified as Methods and the required `B.1.5` relations are shown to obtain within the bounded claim.
6. **Return the prospective branch when needed.** State the candidate whole, participant statuses, proposed relation sets, guards, adapters, alternatives, recovery, variation points, burdens, unresolved conditions, and realization/test WorkPlan.
7. **Lower independently.** When whole semantics, identity, or one relation remains too weak even for a useful candidate, return the supported fragment, relation claim, WorkPlan question, or stop. Do not pad the account to look complete.
8. **Define continuation.** Name the later Work, observations, acceptance and failure conditions, authority, and reconsideration rule that can change the result branch.

#### ME.7:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use and whole semantics | Intended result/preserved condition, situation, operations or invariant, applicability, participants, variation, bounds, and reidentification. |
| participant account | Each subject, kind or status, identity basis or open condition, and proposed contribution. |
| relation sets | Each direct relation, truth status, evidence, guard, and receiving use. |
| branch verdict | Obtaining composition result, prospective candidate account, or lower return with decisive reason. |
| prospective content | Guards, adapters, alternatives, recovery, stops, burdens, and variation points when the lower branch applies. |
| continuation | Realization/test WorkPlan, later Work and observations, authority, acceptance/failure, and reconsideration condition. |

#### ME.7:4.3 - What Changes in Practice

Practitioners can write and test a coherent proposed Method without pretending that documentation created it. A positive composition claim becomes stronger because its identity and relation evidence are explicit; a prospective account remains useful because it carries guards, variation, recovery, and a testable continuation.

### ME.7:5 - Archetypal Grounding — `C-EC-Release-v2`

The EC-417 project proposes `C-EC-Release-v2` as a whole for safety-relevant release coordination. Its account states:

| Whole position | Proposed content |
| --- | --- |
| intended result | a release-authorizable evidence and integration state for one safety-relevant change |
| situation family | internal or supplier-originated hardware/software changes with versioned provisional or signed pinout evidence |
| invariant | provisional evidence may support reversible early integration, but signed evidence and repeated checks are required before safety closure and release authorization |
| participants | identified `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, and `M-Release-Authorize`; candidate reconciliation accounts remain separate |
| permitted variation | pre-entry A when signed evidence or B2 entry conditions differ; B2 for bounded early integration; post-entry recovery R after a failed B2 closure |
| bounds and stops | confidentiality, human authority, `D-8` safety peak at or below `0.40`, signed evidence before closure, and reversibility until `D-1` |
| reidentification | preserve the intended result, invariant, participant-status boundary, evidence-version guard, authority, and A/B2/R branch meanings |

The four participant Methods are identified, but the proposed whole is not. Their co-use and the proposed order do not establish that they are Method parts. The relation sets therefore remain proposed:

- provisional-evidence integration at `D-21` and signed-evidence reconciliation at `D-8`;
- signed evidence and accepted safety result before release authorization;
- supplier preparation responsibility for `1.60 h` under B2;
- separate safety and release authority;
- PLM, rig, and provider-access conditions; and
- description correspondences from evidence version through integration bundle and verification result.

ME.7 returns a prospective candidate account and WorkPlan, not an obtaining composition. The trial WorkPlan covers at most three B2 releases.

Before each entry, `SafetyReviewer-17` performs `W-SafetyEvidenceDecision-17` under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17` to accept or reject the named evidence conditions; `ReleaseDecider-17` then performs `W-ReleaseDecision-17` under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17` to decide branch entry and release, withhold, or next-slot disposition. Neither decision or authority relation substitutes for the other.

The B2 trace condition consumes the single `PERM-TraceAcceptReject-17` occurrence grounded in APP-ME-01, section 5; filled baseline exercise `PEX-TraceAcceptReject-17-01` connects `W-TraceAcceptReject-17-01` to that grant, while `EV-PEX-TraceAcceptReject-17-01` remains separate evidence. Every additional used suggestion would require a distinct dated Work, result, currentness check, and exercise relation rather than another empty grant schema.

Missing signed evidence after early integration triggers recovery R. In R, preserve the performed-integration record and evidence history. Repeat the evidence comparison and affected verification when evidence arrives by `D0` while the existing evidence and reversibility guards still hold. Record whether early integration is retained, rolled back, or repeated, and the added burden. If closure remains unresolved at `D0`, the release result is withhold/next-slot and this R occurrence ends as a failed B2 trial.

`ASG-TraceReview-17` and `PERM-TraceAcceptReject-17` also end at `D0`; continuing safety or release relations extend neither. The trial WorkPlan therefore contains no post-`D0` AI suggestion, trace-review Work, assignment, permission, result, or exercise, and claims no other later Work. Unresolved R may motivate later planning, but this case asserts no post-`D0` recovery WorkPlan, PlanItem, planned endpoints, qualification/currentness result, readiness, assignment, permission/authority, or later Work.

When later non-AI recovery needs coordination, the project may create a new `A.15.2` WorkPlan; `A.15.2` itself does not require planning before every otherwise valid later Work. Planned or unplanned Work would still need its separate qualification/currentness, readiness, assignment, permission/authority, and `A.15.1` occurrence as applicable. These stops preserve all earlier Work and evidence history. A is only a pre-entry alternative.

Acceptance observations include whether each trial respects confidentiality and authority, remains below the `D-8` capacity bound, preserves evidence/version correspondence, and reaches a truthful release or recovery result by `D0`. An attempted post-`D0` AI-supported continuation, or an assertion of later Work without a separately admitted `A.15.1` dated Work occurrence, is an explicit stop and failed trial observation. The withhold/next-slot result preserves earlier Work and may motivate planning; it creates neither a recovery WorkPlan nor later Work. Those observations may support, narrow, split, or reject the account. They do not by themselves identify the whole; `A.3.1` remains the identity owner.

### ME.7:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| document-whole bias | Shared title and ordered sections become one world-side Method. | Recover whole semantics, identity, and relations independently. |
| co-use bias | Several Methods used in one project become participant parts of a composite. | Require identified whole/parts and obtaining `B.1.5` relations. |
| trial-success bias | One successful Work occurrence identifies a reusable Method whole. | Use trial observations as later evidence and keep `A.3.1` separate. |
| unlimited-adaptation bias | Every changed proposal keeps the same identity. | State permitted variation, bounds, and reidentification rule. |
| architecture-decision bias | Selecting a proposed relation set makes it obtain. | Preserve proposal truth until realization and evidence support a stronger claim. |

### ME.7:7 - Conformance Checklist

- [ ] The proposed whole has an intended result or preserved condition, situation, reusable operations/invariant, applicability, participants, variation, bounds, and reidentification rule.
- [ ] Whole identity and every participant status are independently stated.
- [ ] Method composition, Work order/overlap, result use, allocation, support, authority, and description relations are not inferred from one another.
- [ ] The positive branch requires identified whole and parts plus obtaining `B.1.5` relations.
- [ ] The prospective branch preserves proposed truth and names guards, adapters, alternatives, recovery, stops, burdens, and unresolved conditions.
- [ ] WorkPlan, performed Work, observations, MethodDescription, and Method identity remain distinct.
- [ ] The result can lower below a candidate whole when load-bearing semantics or relations are missing.
- [ ] Continuation names later Work, observations, authority, acceptance/failure, and reconsideration.

### ME.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “We wrote the method.” | Say that a candidate account or MethodDescription was written; identify the Method separately. |
| “The architecture was selected, so its relations obtain.” | Keep the decision and proposed relations separate from realization evidence. |
| “All participants passed ME.5, so they form a whole.” | Test whole identity and `B.1.5` composition independently. |
| “A failed trial falls back into the earlier history.” | Preserve performed Work and define a separate recovery branch. |
| “Wait for perfect proof before saying anything.” | Return a prospective account or lower relation claim with explicit tests and stops. |

### ME.7:9 - Consequences

Projects can move from architecture proposal to realization and learning under explicit identity and relation conditions. Strong composition claims are recoverable, while weaker proposals remain actionable without treating their Methods or relations as established.

The cost is a visible open identity or relation question. Some proposed methodologies will remain candidate accounts after useful trials, and some will split into several Methods or a relation structure instead of maturing as one whole.

### ME.7:10 - Rationale

Construction and description can change epistemes and WorkPlans immediately; they do not create a reusable way of doing in the world by assertion. The two-branch result preserves this difference while letting possible-future content guide real Work.

ME.7 does not depend on applying ME.6 first. ME.6 is one common source of proposed relation sets, but any equivalent content can enter ME.7 directly.

### ME.7:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Henderson-Sellers and Ralyté, [Situational Method Engineering review](https://opus.lib.uts.edu.au/handle/10453/13456) | Construction and adaptation of Methods for situations. | Source-local fragment, process, role, and assembly concepts do not establish FPF identity or composition. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Intended use, procedure, representation, tool, ecosystem, and adaptation conditions for a coherent proposal. | Conceptual completeness does not prove world-side Method existence or relations. |
| Current FPF `A.3.1`, `A.22`, `B.1.5`, and `C.32.MWA` | Method identification, selected structures, Method composition, and several-structure synthesis. | ME.7 adds the truthful whole-versus-prospective-account resolution and realization continuation. |

Reopen when a representative proposal cannot be expressed through the positive/prospective/lower branches, when variation repeatedly defeats reidentification, or when a positive composition claim cannot be distinguished from Work order or co-use.

### ME.7:12 - Relations

- `A.3.1` governs whole and participant Method identification; `B.1.5` governs any Method-composition claim.
- ME.6 commonly supplies proposed relation sets and architecture alternatives, but it is not a compulsory predecessor.
- ME.5 supplies individual qualifications without whole identity or compatibility.
- Later realization, identification, description, support, trial, and assurance patterns consume only the branch and truth status returned here.
- A prospective account, WorkPlan, selected architecture, or trial result supplies no obtaining ArchitectureRelation or `methodPartOf` fact by itself.

### ME.7:End

# Part III - Method Descriptions, Representations, and Enactment Support

## ME.8 - Author a MethodDescription for Named Uses

>
> **Primary working result:** one `U.MethodDescription` edition and a use-coverage account for one admitted `U.Method`; or, when Method admission is absent, improved candidate-account content that keeps its candidate status.

### ME.8:0 - Use This When

Use this pattern when an identified Method needs claims that people can use for planning, enactment, comparison, review, revision, publication, or teaching. Start from one named use: who needs to do or decide what, which Method claims that use consumes, and what can remain outside the edition.

The first useful result is a short use-coverage row. It names the Method or candidate account, the receiving use, the claims needed now, the claims deliberately omitted, and the stop. That row prevents a documentation project from expanding before its practical question is clear.

Do not use this pattern merely to publish, diagram, approve, schedule, or record Work. A `U.MethodDescription` is the claim-bearing episteme whose exact `EntityOfConcern` is one Method already admitted under `A.3.1`; its code, diagram, form, carrier, approval, WorkPlan, and dated Work remain different things. If the proposed whole is still a candidate account, improve that account without classifying it as a `U.MethodDescription` for the whole.

### ME.8:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| admitted Method | One reusable way of doing whose identity has been established under `A.3.1`. | A shared title, coherent document, WorkPlan, or successful occurrence does not establish it. |
| `U.MethodDescription` | One C.2.1 episteme about that Method whose claims say something substantive about how the Method is carried out. | Membership is not a completeness, approval, currentness, publication, or effectiveness result. |
| candidate account | Claims about a possible Method whose identity or obtaining relations remain unresolved. | It can be improved and used prospectively without being renamed a MethodDescription. |
| named use | A particular planning, enactment, comparison, audit, revision, publication, or teaching need with a receiver and stop. | A generic wish to “document the method” is not yet a use boundary. |
| use-coverage account | A C.2.1 account that states which Method claims an edition exposes for each named use and which it omits. | It does not prove that the claims are true enough for the use or that anyone used them. |
| representation and publication | A `C.29` correspondence, `E.24.PUB` form or publication occurrence, and carrier through which claims may be expressed or made available. | Form and availability do not decide MethodDescription membership. |

### ME.8:1 - Problem Frame

A working group often has too much material rather than too little: procedures, diagrams, code, examples, approval notes, logs, training slides, and tacit explanations. Different users need different portions. A planner needs applicability, preconditions, parameters, bounds, and stops; a performer needs the actionable claims for the current situation; a reviewer may need provenance, changed claims, and declared evidence limits.

Without a use boundary, authors either copy everything into one manual or reduce the Method to one convenient representation. Both moves hide whether the episteme actually describes an admitted Method and whether its claims are sufficient for the receiving use.

### ME.8:2 - Problem

A document can look complete while saying little about the way of doing. Conversely, a small claim set can be a valid MethodDescription yet be unsafe for a consequential enactment use. Teams also copy calendars, assignees, tool states, observed results, and approval decisions into the description as if adjacency turned them into Method semantics.

The result is difficult to reuse and difficult to challenge. Readers cannot tell which claims belong to the Method, which belong to one Work occurrence, which are evidence or policy, and which omissions require a return.

### ME.8:3 - Forces

| Force | Tension |
| --- | --- |
| Use fitness | Each receiving use needs enough claims, while one universal description becomes expensive and opaque. |
| Stable subject | Several editions and forms may describe the same Method, while a candidate or changed Method must not inherit that identity by typography. |
| Practical brevity | The first useful edition should be small, while hidden preconditions or stops can make it misleading. |
| Representation plurality | Text, code, diagrams, tables, and formal models may all help, while none determines MethodDescription membership. |
| Evidence limits | Claims may cite evidence and source limits, while the description must not become the evidence or assurance result. |
| Revision | A use may require a new edition, while editing a description does not by itself change the Method. |

### ME.8:4 - Solution

Author claims for named uses, keep the described Method stable, and return gaps instead of filling them with neighboring objects.

#### ME.8:4.1 - Pattern-Use Unfolding

1. **Name the receiving use.** State the reader or consuming system, the action or decision, the situation and qualification window, and the stop. Replace “complete documentation” with the smallest question that changes work.
2. **Establish the subject branch.** Name the admitted `U.Method` and effective `U.ReferenceScheme`. If admission is absent, keep the subject as a candidate account and author only improved candidate content.
3. **Select the needed Method claims.** For the named use, consider the transformation or enactment concern, generic participant meanings, applicability, preconditions, intended effects or preserved conditions, bounds, parameters, variation, internal composition, evaluation conditions, and stops. Include only positions that change the use.
4. **Separate neighboring claims.** Keep planned assignments and dates in a `U.WorkPlan`; actual performers, temporal extent, participation, and results with dated `U.Work`; operation declarations with `A.6.1`; evidence reliance with `A.10`; capability with `A.2.2`; approval, permission, and authority with the patterns that define those claims. Cite them when the use depends on them without absorbing them into Method semantics.
5. **Write one claim-bearing edition.** Identify the episteme by its claim content, exact Method as `EntityOfConcern`, and effective scheme. State which claims were added, retained, narrowed, or removed when another edition is being revised.
6. **Record use coverage and omissions.** For each named use, list the claims exposed, claims deliberately omitted, unresolved claims, and the return condition. An omission is acceptable when the receiver does not rely on it; otherwise it is a gap.
7. **Choose expression and publication separately.** Select text, code, diagrams, a mathematical lens, publication form, and carrier only after the claims are stable enough for the use. When different named Method-related actions require complementary governed representations of the current MethodDescription or candidate account, ME.9 returns a complete Method representation profile: one complete C.37-bearing row per action plus the cross-use correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. Use the FPF pattern governing any other represented entity.
8. **Test the receiving use at claim level.** Ask whether the receiver can locate the applicable claims, distinguish conditions and stops, and identify every relied-on omission. Return a description correction, a candidate-account correction, or the missing neighboring result. Do not report Method fit, effectiveness, Work, or assurance from this check.

#### ME.8:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| subject | Admitted Method and identity basis, or candidate account and unresolved admission condition. |
| named use | Receiver, action or decision, situation, qualification window, and stop. |
| claim set | Method-side claims included in this edition and their effective scheme. |
| use coverage | Needed claims, exposed claims, deliberate omissions, gaps, and return condition for each use. |
| neighboring objects | Any WorkPlan, Work, representation, operation declaration, evidence path, capability, permission, authority, publication, or carrier relied on, each kept under its own kind. |
| edition disposition | MethodDescription edition, improved candidate-account content, or lower stop with the decisive missing condition. |

#### ME.8:4.3 - What Changes in Practice

Authors stop treating “the method document” as one undifferentiated object. They can issue a small edition for one use, explain why it is enough, and name the exact gap when it is not. Readers can distinguish a claim about a reusable way of doing from a plan, an observed occurrence, a tool presentation, or an approval fact.

### ME.8:5 - Archetypal Grounding - EC-417

#### ME.8:5.1 - Stop at the Candidate Whole

`C-EC-Release-v2` is a prospective account of a possible release-coordination whole. Its intended result, alternatives A, B2, and R, guards, authority boundaries, confidentiality, reversibility, and D0 stop make it useful, but the whole is not admitted as a `U.Method`. ME.8 may improve those claims for a selection or trial-planning use; it does not return a `U.MethodDescription` for that candidate whole.

This stop changes practice immediately: users can still compare the candidate with alternative A or R and plan a bounded trial, while every downstream statement preserves candidate status.

#### ME.8:5.2 - A Bounded Description of an Admitted Constituent Method

For the admitted constituent `M-HW-Verify`, suppose the named use is preparing safety-verification Work for one EC-417 release. A description edition can state the applicable safety-relevant change family, the distinction between provisional and signed evidence, the comparison and affected-verification actions, the signed-before-closure bound, confidentiality conditions, and the mismatch or stale-edition stop. The use-coverage account says that it exposes those Method claims but omits dates, assignees, actual evidence versions, actual verification results, and release authority decisions.

The planner may cite that edition when constructing a WorkPlan. Supply separate claims about the Work schedule, the assignment of `SafetyReviewer-17`, the required capability, closure authorization, and whether verification occurred whenever the plan or later Work relies on them.

### ME.8:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| document identity bias | A titled document becomes the Method or its complete description. | Establish Method admission and identify the claim-bearing episteme separately. |
| completeness bias | More sections are assumed to make the edition adequate for every use. | Name uses and expose only the claim positions they consume. |
| execution bias | Code, a checklist, or executable syntax becomes evidence that Work happened. | Keep representation, WorkPlan, Work, and result claims separate. |
| policy absorption | Approval, permission, or authority is written as Method semantics. | Cite the separate policy or relation only where the receiving use needs it. |
| candidate laundering | A useful prospective account is called a MethodDescription. | Improve the account but do not call it a `U.MethodDescription` until `A.3.1` admits the Method. |

### ME.8:7 - Conformance Checklist

- [ ] Each `U.MethodDescription` result names one `A.3.1`-admitted Method as its exact `EntityOfConcern`.
- [ ] A candidate whole remains a candidate account when Method admission is absent.
- [ ] Every named use has a receiver, action or decision, situation, qualification window, and stop.
- [ ] Included claims say something substantive about the Method as a way of doing.
- [ ] Use coverage distinguishes exposed claims, deliberate omissions, unresolved gaps, and return conditions.
- [ ] WorkPlan, dated Work, actual participants and results, operation declarations, evidence, capability, permission, authority, representation, publication, and carrier claims remain separate.
- [ ] Representation choice does not decide MethodDescription membership.
- [ ] The result says only whether this edition covers the named claim need; it does not infer Method fit, effectiveness, assurance, or actual use.

### ME.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Write the complete method once.” | Split the request into named uses and record coverage and omissions for each. |
| “The workflow diagram is the MethodDescription.” | Identify the claim-bearing episteme first; treat the diagram as one representation of selected claims. |
| “Add the project schedule so the description is actionable.” | Keep the reusable Method claims in the description and put dates and intended assignments in the WorkPlan. |
| “The procedure passed review, so the claims are adequate everywhere.” | Record the exact review or policy claim separately and evaluate each receiving use under its own conditions. |
| “The candidate account is detailed enough to count.” | Detail does not replace Method admission; return improved candidate content. |

### ME.8:9 - Consequences

Method descriptions become smaller, more reusable, and easier to compare because their subject and receiving uses are explicit. Candidate accounts remain useful without losing their truth status, and missing claims return to the right owner.

The cost is plurality: one Method may have several editions, use-coverage rows, and representations. Projects must also maintain links to neighboring plans, evidence, policy, and publication results instead of copying them into one manual.

### ME.8:10 - Rationale

Description adequacy is use-relative, while MethodDescription membership is not. Separating those questions allows a small episteme to describe an admitted Method without pretending to satisfy every receiver. It also lets a rich candidate account remain prospectively useful without turning description quality into Method identity.

The claim-first order prevents representation and publication choices from selecting ontology. It preserves the connection from R7 among Method, description, Work, capability, instrument, variant, and culture while giving one practitioner a concrete first move.

### ME.8:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| ISO/IEC/IEEE 24774:2021, [process-description elements](https://www.iso.org/standard/78981.html) | Adopt the discipline of describing purpose, outcomes, activities, tasks, information items, roles, and views only where the receiving description use needs them. | Description-side conformance does not establish process performance or FPF kinds. Practitioners still recover the admitted Method and each neighboring claim separately. |
| Daalhuizen and Cash, [Method content theory](https://doi.org/10.1016/j.destud.2021.101018) | Adapt the focus on content that helps a user understand and use a Method. | The source does not make one universal completeness schema. ME.8 uses named-use coverage and explicit omissions instead. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Adopt intended use, procedure, representation, tools, and adaptation conditions as recurring authoring questions. | Conceptual elements do not prove Method identity, obtaining relations, Work, or effectiveness. The EC-417 slices preserve those stops. |
| Current FPF `A.3.1`, `A.3.2`, `C.2.1`, `C.29`, and `E.24.PUB` | Adopt exact Method identity, MethodDescription membership, episteme identity, representation correspondence, and publication separation. | These patterns supply the identity and boundary rules; ME.8 contributes the practitioner method for authoring a use-bounded edition and returning an honest lower result. |

Reopen the pattern when a representative user cannot state the named use without a universal field catalogue, when candidate status is repeatedly lost, or when a current source supports a more useful claim-selection move at comparable effort.

### ME.8:12 - Relations

- `A.3.1` supplies Method admission; `A.3.2` defines `U.MethodDescription` membership and its boundary from plans, Work, representations, and publication.
- ME.7 can supply an admitted whole or a prospective candidate account. ME.8 preserves the branch it receives.
- ME.18 can supply claim content and evidence limits for a candidate account; it does not admit the Method or create the description.
- ME.9 consumes ME.8's current MethodDescription or candidate-account claims only when several unlike named Method-related actions require a Method-specific profile. It returns one complete C.37-bearing row per action and a separate cross-use result for their source correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. For one action, use C.37 or the pattern that governs it; for another represented entity, use that entity’s governing FPF pattern.
- `A.15.2`, `A.15.1`, `A.10`, `A.2.2`, `C.29`, and `E.24.PUB` define or constrain the neighboring plan, Work, evidence, capability, representation, and publication claims that ME.8 keeps separate.

### ME.8:End

## ME.9 - Compose Complementary Method Representations for Their Uses

>
> **Primary working result:** a Method representation profile for one MethodDescription or candidate Method account. Each row carries one complete `C.37` same-use claim group for one receiving System and exact Method-related action or decision; the profile relates those rows across Method uses while retaining the Method repertoire, cross-use correspondences, omissions, edition relations, keep-separate decisions, and return conditions.

### ME.9:0 - Use This When

Use this pattern when a current MethodDescription or candidate Method account must support several unlike Method-related actions or decisions, and the practitioner needs to relate their use-specific representation selections without pretending that one text, diagram, table, model, or view is the Method for every user. Begin with one ordinary question: which exact action or decision must this receiving System perform, and which Method claim must become visible for it?

The first useful result is one complete row in a Method representation profile. Name the Method or candidate status and current source edition, then the receiver, exact action, and required Method claims. For those claims, include the direct subject result, exact relied-on claim, applicable evidence-use and reliance boundary, and receiving result. State exposure and loss, the `select`, `decline`, or `unresolved` disposition, and the return condition. The complete row embeds one `C.37` claim group; do not retain a second standalone copy for the same use.

Use `C.37` or the applicable direct pattern and stop when only one action is current and no Method-specific cross-use profile is needed. Do not use ME.9 to select representations for an arbitrary entity, format unchanged content, establish publication or access, or create a collection or selected structure. ME.9 begins only when the missing result is the Method-specific organization of independently governed, use-bounded selections around one MethodDescription or candidate account.

### ME.9:0.1 - Working Distinctions

| Position | What it contributes | What it does not establish |
| --- | --- | --- |
| Method representation profile | A Method-specific ensemble relating complete use-bounded rows to one MethodDescription or candidate account and recording cross-use correspondences, omissions, edition relations, and keep-separate decisions. | A new Method, MethodDescription edition, integrated view, collection, selected structure, or universal representation taxonomy. |
| embedded `C.37` same-use claim group | One receiver and exact action or decision; direct subject result; exact claim; optional A.2.4 first-use classification; material A.10 path and disposition; receiving result; exposure and loss; row disposition; return trigger. | The cross-use Method profile, subject-side direct results, reliance truth, authorization, capability, Work, or support-configuration choice. |
| MethodDescription or candidate account | The current Method claims and status from which representation needs are recovered. | That every claim is admitted, current, applicable, enacted, or supported by one representation. |
| `C.2.1` episteme | Claim-bearing content about a named `EntityOfConcern` under an effective scheme. | View conformance, mathematical correspondence, publication, reliance, or receiving permission. |
| `E.17.0` view result | An episteme that satisfies one stated viewpoint through its own conformance relation. | Conformance to another viewpoint, identity of the viewed entity, or fitness for another action. |
| `C.29` mathematical-lens result | A declared formal object and correspondence used to inspect selected aspects. | That an ordinary node-link diagram is a mathematical graph or that visual layout supplies an obtaining relation. |
| `E.24.PUB` publication result | A publication occurrence, form, and carrier for one selected episteme edition and audience use. | Truth, availability to every user, reliance, or actual Method use. |
| `A.22` selected structure | Independently identified constituents, selected obtaining relations, applied constraints, named use frame, and selection-use basis. | A structure inferred from colocation, diagram layout, profile membership, or a Method label. |

### ME.9:1 - Problem Frame

Method material serves unlike actions. A performer needs actions, inputs, results, guards, and stops. A method engineer compares contribution and variation. A support builder needs tool, resource, permission, and feedback positions. An assessor needs evidence, qualification windows, uncertainty, and reopen conditions. Project, process, and case viewpoints may expose different claims about the same independently admitted Method-related Work when each viewpoint can change the same exact action.

One representation rarely serves every action without hiding something. The Method Engineering problem is to relate several use-specific selections while preserving Method identity, candidate status, description currentness, WorkPlan versus Work, the direct authority of every selected result, and the limits of every carried claim.

### ME.9:2 - Problem

Teams often place Method representations on one page and call the result an integrated Method view. The page then hides which receiver and action each item supports, which direct result identifies it, which exact claim is relied on, what it omits, whether a reliance or receiving result exists, and whether the subject is a Method, candidate account, WorkPlan, or admitted Work.

The opposite failure declares one canonical Method representation for every user. Performers, assessors, and support builders then reconstruct missing distinctions independently, so inconsistent guards, stale evidence, borrowed authority, and hidden omissions enter action without a return condition.

### ME.9:3 - Forces

| Force | Tension |
| --- | --- |
| Method-content coherence | Rows must return to one current MethodDescription or candidate account, while every receiver/action pair keeps its own selection and limits. |
| User-action fit | A representation should expose the claim that changes one action, while adding every available claim raises burden and hides stops. |
| Status preservation | Plans, candidate claims, and observed Work can help explain a Method, while representation cannot promote their status. |
| View discipline | Project, process, and case viewpoints can illuminate one Work occurrence, while viewpoint names alone establish neither a view nor co-use for another action. |
| Formal precision | A mathematical lens can expose a Method relation or unfolding, while a node-link appearance can overstate correspondence or graph structure. |
| Reliance proportionality | Reversible orientation may need only a direct result and visible limit, while consequential use may require an exact A.10 path and disposition. |
| Maintenance cost | A persisted profile can aid reuse and refresh, while every temporary presentation need not create a second C.37 account, collection, structure, or edition. |

### ME.9:4 - Solution

Build a Method representation profile from the current MethodDescription or candidate account. For every current receiver/action pair, recover direct subject results first, invoke `C.37` once, and embed its complete same-use claim group in the owning profile row. Then relate the rows only through Method-specific cross-use questions: shared source claims, unlike omissions, edition relations, correspondence among uses, and decisions to keep representations separate.

**Local mantra.** *One receiver, one action, one C.37 claim group. Recover the direct result and exact claim; state reliance, receiving result, exposure, loss, disposition, and return. Relate rows through the Method profile without inventing a whole.*

#### ME.9:4.1 - Pattern-Use Unfolding

1. **Name one Method-related use.** State the receiving System, exact Method Engineering decision or enactment-support action, situation, qualification window, and stop. Another action starts another `C.37` invocation even when the user, carrier, or Method is unchanged.
2. **Fix the Method subject and source account.** Name the admitted Method or candidate status and the current MethodDescription or candidate-account edition. Use ME.8 when the needed Method claims are absent or not current enough.
3. **Recover the claims needed by the action.** Select only the needed purpose, input/result, performer, capability, tool or resource, action or Work specification, variation point, guard, evidence, authority, support, feedback, or stop claims. Keep their actual subjects and statuses.
4. **Recover every candidate through its direct governor.** Use `C.2.1` for the claim-bearing episteme, `E.17.0` for a view with its own conformance relation, `C.29` for a mathematical lens and correspondence, `E.24.PUB` for publication, and `A.22` for a selected structure. A title, layout, Method label, carrier, or profile row supplies none of those results.
5. **Embed one complete `C.37` claim group.** For the receiver and exact action, state the direct subject result and exact claim; add A.2.4 first-use classification when current; add the exact A.10 path and `RelianceDisposition` when reliance is material; name the direct receiving result; state what is exposed, withheld, lost, transformed, or uncertain; mark the row `select`, `decline`, or `unresolved`; and name the return trigger. If a direct pattern already supplies the complete one-result/one-use answer and limits, take that direct exit instead of duplicating C.37.
6. **Compose the Method profile without flattening.** Connect the completed rows to one MethodDescription or candidate account. Record cross-use correspondences, conflicting omissions, edition dependencies, and keep-separate decisions. Shared profile membership creates no composite Method, super-view, collection, selected structure, or new description edition.
7. **Handle WorkPlan and Work as supporting subjects.** Preserve WorkPlan or Work status. Project, process, and case candidates may be co-recorded inside one row only when each has its own `E.17.0` conformance result, concerns the same independently admitted Work, and can change the same exact action. A candidate for another action belongs in another row.
8. **Run the smallest user-action probe.** Ask the named receiver to retrieve the required claim, distinguish the relevant status or alternative, perform the bounded interpretation or decision, and stop at the declared condition. Return the profile and observed gap, or reopen ME.8, C.37, the direct subject governor, the receiving-result owner, ME.10 support configuration, or the owning Method decision.

#### ME.9:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| Method subject | Admitted Method or candidate status and current MethodDescription or candidate-account edition. |
| use boundary | Receiving System, exact Method-related action or decision, situation, qualification window, and stop. |
| required Method claims | Exact purpose, input/result, action, variation, evidence, support, authority, or stop positions needed by the action. |
| direct subject result | Independently governed `C.2.1`, `E.17.0`, `C.29`, `E.24.PUB`, `A.22`, or other direct result; explicit lower or failed result when it does not obtain. |
| exact use claim | The precise claim this action would carry from that direct result. |
| evidence and reliance | Optional A.2.4 first-use classification; when material, exact A.10 path, decision-use relation, currentness boundary, `RelianceDisposition`, and stop. |
| receiving result | Direct choice, gate, permission, authorization, acceptance, task, or domain result that permits, declines, or leaves the use unresolved. |
| exposure and loss | Method claims and distinctions exposed or preserved, and those omitted, withheld, transformed, or uncertain. |
| row disposition | `select`, `decline`, or `unresolved` for this exact action, with any narrowed use. |
| status boundary | Method, candidate account, MethodDescription, WorkPlan, Work, representation, view, publication, structure, reliance, and receiving-result statuses preserved. |
| return | User-action observation, failure owner, correction target, and reconsideration trigger. |
| profile relation | Cross-use correspondence, conflict, edition relation, omission, or keep-separate decision contributed by this row. |

#### ME.9:4.3 - What Changes in Practice

Practitioners stop asking one artifact to be the Method for every user and stop treating a profile as authority by colocation. A performer can receive an action-and-stop representation, an assessor an evidence-and-limit representation, and a method engineer a comparison or variation representation. Each row shows its own direct basis and exact permitted use, while the Method profile shows how those unlike selections return to one current source account.

### ME.9:5 - Archetypal Grounding - EC-417 Method Material for Four Uses

The EC-417 team holds candidate whole `C-EC-Release-v2`, its current candidate-account edition, and trial WorkPlan `WP-EC417-B2-Trial-1`. ME.8 has supplied the bounded claims needed for the proposed B2 trial: purpose, A/B/B2/R alternatives, evidence entry, Work order, allocations, authority, confidentiality, recovery, and stops. ME.9 does not admit the candidate as a Method or turn the WorkPlan into Work.

The Method representation profile embeds four complete, use-bounded rows:

| Use boundary and receiving result | Direct result, exact claim, and reliance | Exposure and loss | `C.37` disposition and return |
| --- | --- | --- | --- |
| `ReleaseDecider-17` must decide A, B2, R, or withhold for the bounded trial. The ME.9 allocation result permits the decision table to contribute to that decision; the eventual C.11 or direct Method-architecture result alone chooses. | `C.2.1` identifies the current decision-table episteme. Exact claim: the table states the current alternative, evidence-timing, peak-burden, authority, entry, and closure distinctions for this candidate edition. A.2.4 classifies its intended decision-evidence use. A.10 path `P-ME9-EC417-Decision-1` carries that claim and currentness window with `RelianceDisposition=pass`. | Exposes alternative and guard distinctions; omits detailed performer instructions and any proof that B2 will succeed. | `select` for bounded alternative comparison only. Return if the candidate edition, evidence entry, authority, window, A.10 disposition, or receiving decision changes. |
| `SafetyReviewer-17` must prepare and check the bounded B2 delta before trial release. The ME.9 allocation result permits the action-and-guard episteme for preparation; actual permission, Work, and task success remain with their direct owners. | `C.2.1` identifies the current action-and-guard episteme. Exact claim: it states the B2 inputs, required checks, confidentiality, peak bound, signed-before-closure guard, and rollback stop. A.2.4 classifies the intended preparation use. A.10 path `P-ME9-EC417-Safety-1` carries the current-edition and signed-evidence premises with `RelianceDisposition=pass` for the named preparation window. | Exposes checks and stops; omits portfolio dates and authority not needed to read the preparation steps. | `select` for preparation and checking only. Return on stale edition, changed confidentiality or guard, missing permission or authority, failed A.10 path, or a different action. |
| `SupportBuilder-17` must configure retrieval and tailoring support for the B2 trial. The ME.9 allocation result permits the support-task episteme as an input; ME.10 alone compares and tests support configurations. | `C.2.1` identifies the support-task episteme. Exact claim: it names users, required Method claims, PLM/CI Systems, permissions, task results, and stops. A.10 path `P-ME9-EC417-Support-1` carries the current source and allocation premises with `RelianceDisposition=pass` for this configuration decision. | Exposes task inputs and relation gaps; omits provider capability, actual access, performed task Work, and configuration superiority. | `select` as a profile input, not as the support arrangement. Return those omitted facts to ME.10 and their direct owners; reopen if the task set or source edition changes. |
| `MethodEngineer-17` must decide which findings from completed trial `W-EC417-B2-1` require reopening the candidate before further evaluation. No directly governed receiving result has yet been recovered for that exact decision; the separate ME.11–ME.14 judgments do not choose the reopen premises by themselves. | `A.15.1` independently admits the one Work. The project reading would expose allocation and occupied decision slots, the process reading the performed verification sequence and its correspondence to recurring check positions, and the case reading the evidence history, observed conditions, and next-decision changes. The candidate epistemes `E`, viewpoint editions `P`, and their fixed rules are not identified in this case. Without them, none of the three required direct judgments that `EpistemeViewpointConformanceRelation(E,P)` obtains can yet be made. A.2.4 classification and A.10 path `P-ME9-EC417-Trial-1` cannot supply those missing conformance judgments or the missing receiving outcome. | The three intended readings keep unlike claims about the same Work visible; they omit proof of Method identity, transfer, worth, future effectiveness, conformance, and permission to use the claims in the reopen decision. Profile membership supplies none of those results. | `unresolved` for the reopen action. Return to the exact `E`/`P` owners for the three `E.17.0` judgments and to the direct decision owner for its predicate and actual outcome; reconsider this row only after both bases are available. A reading for another action starts another row. |

The four rows are inputs to ME.9, not yet its Method-specific result. ME.9 returns cross-use profile `MRP-EC417-CrossUse-1`:

| Profile position | Cross-use result |
| --- | --- |
| shared Method source | All four rows return to candidate `C-EC-Release-v2` and the same current candidate-account edition; none promotes that candidate to an admitted Method. |
| cross-use correspondences | The B2 alternative, evidence-entry boundary, confidentiality condition, recovery path, and stop claims occur in different action-specific forms across decision, preparation, support, and reopen uses. Their correspondence lets a source change be traced across rows without making the representations identical. |
| conflicting omissions | The decision row omits performer instructions; the preparation row omits portfolio timing and unused authority; the support row omits actual access, capability, task Work, and configuration superiority; the reopen row omits Method identity, transfer, worth, and future-effectiveness claims. These omissions remain explicit and are not repaired by unioning the rows. |
| edition relations | Every row depends on the named candidate-account edition. The reopen row additionally refers to admitted Work `W-EC417-B2-1` and three still-unresolved candidate-episteme/viewpoint-edition conformance questions; the other rows do not silently inherit those Work-dependent claims. |
| keep-separate decisions | The decision table, action-and-guard episteme, support-task episteme, three candidate readings, their viewpoint editions, each direct conformance judgment, and the receiving decision retain their own governors and statuses. The profile creates no integrated super-view, collection, selected structure, or new MethodDescription edition. |
| cross-use return | A changed candidate status, source edition, B2 alternative, evidence-entry boundary, or recovery/stop claim reopens every affected row and this profile relation. A changed support task reopens the support row. The unresolved reopen row returns only when exact Work identity, the three direct `E.17.0` judgments, their claims, the A.10 disposition, and the governed receiving outcome are available; later change to any of those bases reopens it. |

The fourth row keeps the R10 relation explicit without awarding view status early: project, process, and case are three intended viewpoint-governed readings of one independently admitted Work, not three Work objects. Each becomes a `U.View` only through its own positive `E.17.0` judgment against an exact viewpoint edition, and co-recording them is useful only when each can change the same exact reopen decision. The profile does not make an integrated super-view.

A timeline, dependency network, state-transition drawing, or other node-link material is a mathematical-lens result only when `C.29` identifies the formal object, mapping, preserved and lost structure, admitted use, and stop. Ordinary node-link material is not a mathematical graph by appearance or vocabulary.

### ME.9:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| artifact-as-Method bias | A diagram or playbook becomes the Method itself. | Return every row to the admitted Method or candidate account and current description edition. |
| use-boundary collapse | One selection is reused for another action because the user, carrier, or Method is unchanged. | Give every receiver/action pair one complete embedded C.37 claim group and another row for another action. |
| layer borrowing | Publication, provenance, evidence classification, or profile membership is treated as reliance or permission. | Keep direct subject result, optional A.2.4 classification, material A.10 reliance, and receiving result separately recoverable. |
| viewpoint reification | Project, process, and case become three different Work objects. | Hold one admitted Work and one exact action fixed; apply each viewpoint conformance separately. |
| plan-as-work bias | A representation of intended enactment is reported as performed Work. | Preserve WorkPlan status and return the failed or absent Work-dependent result. |
| graph metaphor bias | Any connected Method material is called a graph. | Reserve mathematical graph claims for an actual `C.29` result; call ordinary material a diagram, table, map, or other direct kind. |
| integrated-view bias | Profile colocation creates one authoritative super-view or new MethodDescription edition. | Keep rows separate and change the edition, collection, structure, or view only through its direct owner. |

### ME.9:7 - Conformance Checklist

- [ ] The profile names one admitted Method or candidate status and one current MethodDescription or candidate-account edition.
- [ ] Every row names one receiving System and exact Method-related action or decision, qualification window, and stop.
- [ ] Every row carries one complete C.37 claim group: direct subject result, exact claim, applicable A.2.4/A.10 layers, receiving result, exposure and loss, disposition, and return.
- [ ] The same use is realized once: embedded in the profile row or retained standalone, never both.
- [ ] Each representation kind is established by its direct FPF governor rather than by layout, title, carrier, or profile membership.
- [ ] Method, candidate account, MethodDescription, WorkPlan, Work, representation, view, publication, carrier, reliance, receiving result, and selected structure remain distinct.
- [ ] Project, process, and case candidates concern the same independently admitted Work and are co-recorded only when each can change the same exact action.
- [ ] A mathematical-lens claim states the formal object, correspondence, intended use, and loss boundary under `C.29`; ordinary node-link material is not called a mathematical graph.
- [ ] Failed or missing direct results return the lower episteme and named gap rather than borrowing support from another layer.
- [ ] The smallest user-action probe records success, gap, or return without claiming publication, access, capability, enactment, fit, transfer, worth, or authority.

### ME.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “This diagram is the Method.” | Name the Method or candidate account, current description edition, direct subject result, exact claim, and use boundary. |
| “Everyone should use the canonical process map.” | Make another row for every receiver/action pair and expose only its required Method claims and stops. |
| “The project, process, and case views show different Work.” | Apply their viewpoint criteria to one admitted Work and co-record them only for the same exact action. |
| “The current publication proves this row may be used.” | Record publication as auxiliary fact; require the direct subject, reliance when material, and receiving results. |
| “The planned trial is already visible as performed process Work.” | Retain a WorkPlan representation until Work exists and satisfies the direct view or Work criterion. |
| “Combine all views into one Method structure.” | Keep rows separate unless direct composition and `A.22` selection-use results independently obtain. |
| “The graph proves the workflow order.” | Identify a mathematical graph and correspondence under `C.29`, or keep the drawing as a non-mathematical episteme. |

### ME.9:9 - Consequences

Method material becomes usable for unlike actions without multiplying Methods or hiding the source edition. A practitioner can recover why each row is selected, declined, or unresolved, what exact claim it carries, what it omits, and which change requires return. The profile adds the Method-specific cross-use account without copying the common representation-selection move.

The cost is explicit row and profile maintenance. Some attractive artifacts remain lower epistemes or fail a view, lens, publication, reliance, receiving-result, or structure rule. Another action requires another row. A change to required Method claims may reopen ME.8 or the description edition rather than being patched independently in several representations.

### ME.9:10 - Rationale

MethodDescriptions combine action, purpose, inputs and results, variation, evidence, support, and stop claims that different users consume differently. `C.37` governs transdisciplinary selection and co-use for one receiver and one action. ME.9 keeps the subject-specific remainder: connecting those complete use-bounded rows to one MethodDescription or candidate account and maintaining Method repertoire, cross-use correspondences, omissions, edition relations, and keep-separate decisions.

This preserves the R7 synthesis of Method, description, Work, instrument, capability, variant, and culture without assigning ME.9 ownership of general representation selection. It also preserves the R10 insight that project management, process management, and case management provide different viewpoints on the same Method-related Work when their conformance criteria obtain. Their distinctions change what a user can see about the same Work; they do not define three Methods.

### ME.9:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| ISO/IEC/IEEE 24774:2021, [process-description views and elements](https://www.iso.org/standard/78981.html) | Adopt explicit intended views and description elements for different Method users. | View-oriented description conformance does not create performed Work or import a universal ontology. ME.9 relates Method claims to named uses and leaves view identity to its direct governor. |
| Daalhuizen and Cash, [Method content theory](https://doi.org/10.1016/j.destud.2021.101018) | Adapt the separation of Method content from the forms through which users encounter it. | Method-content roles guide the profile; no single content form is made canonical. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Adopt representation, intended use, tool, and adaptation as distinct Method questions. | A tool or representation does not become the Method or evidence of enactment. The EC-417 profile keeps these claims separate. |
| FPF `C.37`, `C.2.1`, `E.17.0`, `C.29`, `E.24.PUB`, `A.22`, and `C.13` in this edition's named dependency state | Reuse use-bounded representation selection, episteme, view, mathematical-lens, publication, structure, and collection results. | These patterns retain authority over common representation kinds, use-bounded claim groups, reliance and receiving-result separation, and direct predicates. ME.9 contributes only the MethodDescription/candidate-account profile, cross-use relations, Method-specific omissions, and return paths. |

Reopen when a representative Method user cannot perform the named action without hidden reconstruction; when a Method-content role or MethodDescription practice changes the profile action; when project, process, and case criteria cease to preserve one Work; when a row no longer carries the complete current C.37 claim group; or when the FPF dependency state changes the consumed representation-selection result. Migrate common representation work to FPF while retaining only the Method-specific profile and return paths.

### ME.9:12 - Relations

- ME.8 supplies the current MethodDescription or candidate-account claims and their use boundary; ME.9 relates complete use-bounded representation rows to the Method-specific uses that consume them.
- `C.37` governs one receiver, one exact action or decision, direct-result and reliance layers, exposure and loss, row disposition, co-use, and return. ME.9 embeds that complete claim group once per profile row and adds only the cross-use Method profile.
- `C.2.1` identifies claim-bearing epistemes; `E.17.0` governs viewpoint conformance; `C.29` governs mathematical-lens use; `E.24.PUB` governs publication; `A.22` governs selected structures; `C.13` governs material collection treatment. ME.9 cannot borrow one result from another.
- `A.15.2` governs WorkPlan and `A.15.1` governs performed Work. A Method representation may rely on either as a supporting subject without changing its status or making ME.9 their general representation owner.
- ME.10 takes the direct exit when one owning result already supplies a complete one-result/one-use answer. It consumes ME.9 rows only when complementary governed representations must be allocated to unlike Method-related actions; those rows already carry their applicable C.37 claim groups.

### ME.9:End

## ME.22 - Compare Method Descriptions by Content and Representation


### ME.22:1 - Problem frame

**Use this when.** A Method description appears more useful after revision, but its content and its form both changed. You need to decide which revision to retain without crediting new instructions to a new layout, or treating a readable description as evidence that the described Method works.

The working reader is a Method engineer comparing descriptions, pattern languages or other inspectable representations for a named reader and action. Start by asking: **what answer or action should improve, and what changed in the material available to that reader?**

The first useful result is a bounded comparison: the earlier and proposed answers, the content and representation differences, what the evidence supports, and the next repair or selection. One local contrast can be enough. If the problem is simply choosing a representation for one action, use C.37; if several unlike Method uses need complementary representations, use ME.9. Use ME.14 when the question is the practical worth of the Method itself.

### ME.22:2 - Problem

A new pattern language often adds examples, stops and source returns while changing headings and navigation. Readers then answer better, and the gain is attributed entirely to the language form. Conversely, a terse table can look worse because essential content was removed, not because tables are unsuitable.

The same confusion occurs with a checklist, diagram, executable description or AI-supported presentation. A comparison that changes subject, content, tools and task together can support a useful bundle choice, but it cannot isolate the contribution of one change.

### ME.22:3 - Forces

| Force | Tension |
| --- | --- |
| Useful revision and explained gain | The team needs a decision now, while attributing a gain requires a comparison that can distinguish its sources. |
| Equivalent information and different affordances | A form can expose the same claims differently, while an added edge or omitted warning can change the content. |
| Fresh use and learning | A reader needs enough domain knowledge, while seeing another answer can teach the tested result. |
| Proportional evidence and consequential claims | A small desk comparison can settle a local correction; population, transfer and causal claims require more. |
| Better description and better Method | Understanding guidance is valuable, while enactment and domain performance remain separate observations. |

### ME.22:4 - Solution

Compare the description change at the receiving use, separate the available contrasts, and report only the difference that the observations warrant.

#### ME.22:4.1 - Fix the comparison question

Name the reader or consuming system, the Method or candidate account, the intended action or decision, and the result and stop the description should let the reader recover. Keep the task facts, relevant source conditions, tools and opportunity to act comparable.

State the content that must survive: the relied-on action claims, relations, applicability, uncertainty, result, stop and source-return information. Then state the representation difference, such as notation, arrangement, salience, navigation or interaction. Do not call a new condition or an unsupported diagram edge a form-only change.

Use A.6.3.RT for a changed representation scheme, or the applicable same-regime wording, narrative or coarsening result. Its preservation and loss answer helps establish the comparison inputs; it does not demonstrate improved performance. If the Method's reusable semantics also changed, retain the ME.15 identity/variant question and bound the description comparison accordingly.

#### ME.22:4.2 - Choose the smallest informative contrasts

When only content changed in a fixed form, compare those two versions. When only form changed and the relevant content is preserved, compare those two forms.

When both changed and the receiving decision needs their separate contributions, use:

| Variant | Content | Form | What its comparison can address |
| --- | --- | --- | --- |
| A | Prior | Prior | The earlier usable answer and its limits. |
| B | Added or revised | Prior | B against A: the content difference in the prior form. |
| C | Same revised content as B | Proposed | C against B: the form difference at the revised content. |
| D, conditional | Prior | Proposed | Complete the crossed comparison if content/form interaction or transfer of the form effect across contents matters. |

The three-variant arrangement gives two local contrasts. It does not identify an interaction. Four cells make that question inspectable but supply neither replication nor causal identification by themselves.

If a cell cannot be constructed without changing another load-bearing feature, say so. A bundle comparison may still support a local choice. Do not describe it as an isolated content or form result.

#### ME.22:4.3 - Observe the receiving use

Ask the reader to obtain the first useful result, not to rate which document looks better. Recover:

- the applicable action or decision and the answer actually given;
- the result, stop or missing condition the reader identifies;
- unsupported inferences or lost distinctions that change the answer;
- the source returns needed to support or correct it; and
- the observed burden when time, source openings, attempts or other relevant effort were actually recorded.

These are candidate observations, not one universal score. Select those that can change this comparison. A source-opening count does not measure comprehension; shorter reading does not prove lower total effort; recognizing a prescribed action does not establish its correct enactment.

Choose readers and allocation to variants in proportion to the claim. A fresh probe withholds the other answers and the author's preferred conclusion when they would teach the task. Repeated-reader comparisons retain learning and order effects instead of calling the reader fresh. In AI probes, keep the model, supplied context and available tools recoverable when they affect inference. Generalizing from a few AI answers to human performance is another unanswered question.

#### ME.22:4.4 - When testing a changed-condition return

Use this probe when the comparison needs to establish how a reader responds to a new fact. First retain the reader's initial answer. Then disclose the changed source, missing fact or altered receiving use. Ask what must change and what remains usable.

A good return revisits the dependent claim rather than repeating the whole task or preserving an invalid assumption. Compare the actual revised answer, its source returns and its stop. If the changed condition changes the comparison question or available action set, identify that new question; do not present the two answers as observations under identical conditions.

#### ME.22:4.5 - Return a bounded revision result

State the inspected variants, the content/form contrasts they actually support, observations, losses, uncertainty and next decision. Distinguish a demonstrated local difference, no distinguishing result in this probe, an unavailable contrast and a confounded comparison.

Return a content correction to ME.8, a contradicted maintained claim to ME.12, and selection evidence to C.37 or ME.9. Use ME.11 for representative enactment evidence and ME.14 for a Method-worth decision. A causal claim needs its own justified research design and inference basis; neither this table nor an attractive explanation supplies it.

An ordinary comparison can remain short prose. When another decision will rely on it, retain the candidate versions, receiving use, observations and inference limits as an identifiable account, with the source conditions that reopen it.

### ME.22:5 - Archetypal Grounding

#### ME.22:5.1 - Added stop information versus a table

This is a constructed comparison, with explicit text rather than an assumed reader study.

The receiving action is deciding whether an earlier review may support a current description revision.

**A, earlier prose:** “Reuse the previous review for a display-only change.”

**B, revised prose:** “For a display-only change, reuse the previous review only while the reviewed claims, question and qualification window still match. If a required source argument cannot be recovered for a new recheck, stop that recheck and return to its source; preserve unrelated earlier results.”

**C, the same revised content in a table:**

| Condition | Action |
| --- | --- |
| The change is display-only, and reviewed claims, question and qualification window still match | Reuse the previous review only under this full condition. |
| A required source argument cannot be recovered for a new recheck | Stop that recheck and return to its source. |
| An earlier result is unrelated to the missing argument | Preserve that result. |

Initially, the facts say that the change is display-only, the claims and question are unchanged, and the qualification window is current. All variants can support reuse. The later condition says that a new recheck needs an argument outside the available excerpts and that the retained dossier contains only its locator.

B and C explicitly support the local stop and preservation answer; A does not contain that distinction. This establishes a content-coverage difference in the constructed texts. It does not show that an actual reader preferred or used C more effectively than B. A reader comparison would still be needed for that form claim.

The useful authoring decision is to retain the missing stop information and withhold the table-superiority claim.

#### ME.22:5.2 - A graph that adds a claim

A proposed graph draws an unconditional edge from “review complete” to “publish”. The prose requires a separate publication decision. The graph has added a consequential claim; it is not another form of the same content. Repair the edge and its condition before testing a pure form contrast, or compare the changed bundle with that difference explicit.

### ME.22:6 - Bias-Annotation

Authors tend to know the omitted condition and may answer correctly from memory. Readers who see all variants can learn it too. Separate text inspection, fresh reading, repeated reading and actual enactment evidence.

The constructed examples expose content and inference boundaries. They contain no measured time saving, error rate or Method-effectiveness result.

### ME.22:7 - Conformance Checklist

- The receiving reader, subject, action, result and stop are fixed sufficiently for the comparison.
- Content changes and representation changes are stated, including added or lost relations.
- Every claimed contrast is supported by the available variants and conditions.
- Reader learning, tool differences and other material confounds remain visible.
- When a changed-condition return is tested, an initial answer precedes disclosure of that condition.
- Observed burden is distinguished from estimated or unmeasured burden.
- The result returns to the proper content, selection, trial or worth decision.

### ME.22:8 - Common Anti-Patterns and How to Avoid Them

| Misstep | Repair |
| --- | --- |
| Better answers prove that the new form is better. | Check whether the new form also supplied new content or tools. |
| A four-cell table is treated as a causal study. | Establish sampling, allocation, repetition and inference separately when that claim is needed. |
| A reader sees the changed condition before giving the initial answer. | Run the initial and changed-condition probes separately. |
| A diagram is declared equivalent because its labels match. | Inspect edges, polarity, conditions, uncertainty and source return. |
| No difference in one probe is called universal equivalence. | Retain the local no-distinguishing-result conclusion and its sensitivity limits. |

### ME.22:9 - Consequences

A useful revision can be retained without overstating why it helped. Content defects and representation defects receive different repairs, and later selection or worth decisions receive evidence with usable limits.

The cost is preparing informative contrasts and observing the actual task. When that cost cannot change the decision, take the sufficient direct result or an honestly bounded bundle comparison.

### ME.22:10 - Architectural Rationale

ME.8 asks whether a description exposes the claims a use needs. ME.9 organizes complementary representations across uses. ME.12 checks agreement and repair ownership. None of those results alone answers which difference between revised descriptions explains an observed improvement.

This pattern joins established representation-preservation and validation Methods around that professional revision question. It does not replace experimental design, produce a universal representation ranking or merge description usability with Method performance.

### ME.22:11 - SoTA-Echoing

[ACAP analysis (Doellken, Nelius and Matthiesen, 2024)](https://doi.org/10.1080/09544828.2024.2320018) distinguishes attention, comprehension, application and performance when investigating design-method difficulties. Adopt that separation; the evaluated sheet-metal-design setting and interpretive analysis do not justify universal metrics or causal attribution to each content element.

[NIST's factorial-design account](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3331.htm) supplies the established crossed-factor idea. Adapt it to the contrasts the Method-description decision needs; do not claim a new experimental theory. C.37, A.6.3.RT and ME.9 retain their representation results.

The serious cheaper alternative is direct claim inspection plus the existing representation selection. In the review-reuse example it already identifies the missing stop information; no reader experiment is necessary for that content defect. Use the fuller comparison only when a material form, learning, burden or interaction question remains. Reopen the result on a changed task, source condition, candidate content, reader population or hidden confound.

### ME.22:12 - Relations

- ME.8 supplies the description and receiving use; A.6.3.RT supplies representation-preservation and loss.
- C.37 and ME.9 consume bounded evidence for one-action selection and cross-use representation profiles.
- ME.12 receives a contradicted-claim correction; ME.15 distinguishes description revision from Method variation.
- ME.11 supplies actual trial evidence; ME.13 and ME.14 separately judge transfer/fit and practical worth.
- ME.23 can use the comparison when choosing a pattern-language representation; ME.24 supplies reconstruction failures that may motivate another comparison.

### ME.22:End

## ME.10 - Build a Method Base and Enactment-Support Arrangement

>
> **Primary working result:** a tested configuration that covers a bounded set of named-user tasks, or a truthful lower result: several retained candidates, a stated split boundary, or a missing priority or test. Method material, user Systems, participating Systems, relations, Work, results, and gaps remain separate. An A.22 selected structure is returned only when its independent selection-use basis exists.

### ME.10:0 - Use This When

Use this pattern when Method material exists but named user Systems still cannot reliably find the current edition, distinguish status, compare alternatives, tailor a branch, use a needed tool or automation, give feedback, or stop at the right boundary. A named user may be human, automated, biological, organizational, computational, or mixed; performance, capability, permission, and authority still require their own governed facts. Begin with the failed or at-risk user task, not with a repository or platform design.

The first useful result is a bounded task-set and gap table: one row for each named user and use, with the actual material or aid, receiving Work or decision, use relation, task, mandatory or optional criterion, evidence status, qualification window, and stop. Several rows do not become one Work occurrence or one EntityOfConcern. A small manual arrangement can be enough; a curated Method Base is added only when its collection and current-edition discipline change a named task.

“Method Base and enactment-support arrangement” is a Plain practice name for the separately identified Method or candidate accounts, descriptions, representations, collections, editions, Systems, direct relations, assignments, permissions, authority, capabilities, constraints, user Work, and results configured for the named uses. It is not one FPF technical kind and does not make a repository, interface, provider, tool, prompt, or proposed organization a Method, actor, authority, capability, Work occurrence, or selected `U.Structure`.

Do not use this pattern to decide whether a Method is fit or effective, to perform the receiving domain Work, or to develop user capability. It configures and tests the way Method material is obtained and used for bounded tasks; those neighboring judgments remain separate.

### ME.10:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| bounded task set | A finite set of rows, each naming one user System, material or aid, receiving Work or decision, use relation, task criterion, evidence status, window, and stop. | It is not a plural Work occurrence or a new whole. Each task, Work occurrence, and relation keeps its own identity. |
| configuration candidate | One identified combination of material, Systems, relations, conditions, and stops proposed for some or all rows in the bounded task set. | A candidate can be sufficient, insufficient, untested, failed, or non-dominated for the stated use without becoming a selected A.22 structure. |
| Method Base | A Plain maintained boundary for a project-level entry collection together with its separately identified edition account, publication occurrence, and retrieval use. | It is not one technical kind. A folder, catalogue, repository, or publication alone does not establish collection membership, currentness, or usability. |
| enactment-support arrangement | Plain name for the identified material, Systems, conditions, and relations chosen to help named users carry out specified Method-related tasks. | It is not a generic `SupportRelation`, one product-shaped object, or an automatically selected structure. |
| named-user task Work | Independently admitted dated Work in which a user System actually performs the retrieval, comparison, tailoring, tool, automation, feedback, or other named task. | This is an ordinary descriptive phrase, not another `U.Work` subtype. A click trace, access grant, planned task, or tool output alone does not establish the Work or its result. |
| direct System-use relation | A domain relation whose actual Work and System participants, predicate, extent, and use are explicit. | It creates no entitlement, capability, assignment, permission, authority, or task success unless those predicates independently obtain. |
| proposed organization | A recoverable proposal for constituents, relations, constraints, and use frame. | It is not a selected A.22 `U.Structure` until the selection-use basis obtains. |
| task result | An observation-bounded result for one performed user task. | It does not prove Method fit, effectiveness, transfer, or general holder capability. |

### ME.10:1 - Problem Frame

Method descriptions and representations do not reach practice by their existence alone. A user may find an obsolete edition, miss candidate status, choose the wrong branch, expose confidential material to a provider, or accept a tool suggestion beyond their authority. The material can be correct while the surrounding user task fails.

The practical question is therefore specific: which named users need which Method-related tasks, under what conditions, which criteria and stops are mandatory for the bounded use, and what smallest supported change would cover them or expose an unresolved choice? Repositories, search, prompts, automation, training, provider access, permissions, and feedback matter only through their contribution to those tasks and their own governed relations.

### ME.10:2 - Problem

One failure treats a Method Base as a folder and declares success when files are uploaded. Another builds a platform before observing a user task. A third lets tool integration stand in for access, assignment, capability, permission, authority, or performed Work. A fourth groups all components under a convenient label and calls the proposal a selected structure.

These shortcuts hide the actual failure. Users cannot tell whether the wrong edition, missing relation, denied access, unsuitable representation, absent assignment, missing permission, authority boundary, capability gap, or untested task caused it. Repairs then grow around the platform rather than around Work.

### ME.10:3 - Forces

| Force | Tension |
| --- | --- |
| User-task value | A small configuration may solve the problem, while platform ambitions encourage premature breadth. |
| Current material | Users need trustworthy status and editions, while publication and collection membership do not establish currentness by themselves. |
| Tool assistance | Search, PLM, CI, prompts, and automation can reduce burden, while outputs and interfaces must not acquire authority. |
| Organizational precision | Relations and constraints may need an A.22 structure, while a proposal must remain useful before selection facts exist. |
| User and provider boundaries | Human and non-human user Systems and provider Systems can contribute differently, while vague “support” wording can merge performance, service, capability, permission, authority, and result. |
| Testing | Actual user Work is needed to test the arrangement, while a successful bounded task proves neither general capability nor Method effectiveness. |

### ME.10:4 - Solution

Build a bounded set of named-user task criteria, compare candidate configurations against that same set, test the retained route or routes, and repair the first defeated material, relation, condition, or task. Return several candidates, a stated split boundary, or a missing priority or test whenever the current basis does not justify one winner.

Use a cheap ordinary task-and-gap row for a small reversible case. When success depends on a Work or WorkPlan performer-support configuration, interruption, handoff, stale state, support loss, or recovery, apply the current `A.15.8` branch and probe rather than redefining it here. When several criteria, missing evidence, or incomparability make the configuration choice non-trivial, consume current `A.19.CPM` comparison results and `A.19.SelectorMechanism` selected-set semantics rather than forcing one route. ME.10 specializes these patterns for Method material through two content branches.

In the direct branch, take the `C.37` direct exit when one owning direct result already returns the complete one-result/one-use selection and limits. When the ME.10 task row itself owns that use, embed the complete same-use claim group once in the row: receiver and exact action, direct subject result and exact claim, applicable evidence/reliance layers, receiving task result, exposure and loss, disposition, and return. Do not open ME.9 or retain a duplicate standalone C.37 account.

In the profile branch, consume one complete ME.9 profile when complementary governed representations must be allocated to unlike named Method-related actions. That profile contains one complete C.37-bearing row per action and a separate Method-specific cross-use result stating shared source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return conditions.

Both branches preserve Method and candidate status, the ME.8 source account, Method Base collection and edition facts, retrieval and tailoring particulars, provider and AI boundaries, named-use task rows, and their return paths. Neither a C.37 row nor the ME.9 cross-use result selects the support configuration.

If the task set, comparison basis, or observable test cannot be recovered, return `missing-task-set`, `missing-configuration-basis`, or `missing-task-test`. If retained candidates require an absent priority or decision, return `unresolved-configuration-choice[...]`; do not improvise a platform or call a local minimum the arrangement.

#### ME.10:4.1 - Pattern-Use Unfolding

1. **Construct the bounded task set.** For each named user System and use, name the actual Method, candidate account, description, representation, aid, or other support result to be retrieved or used; the receiving Work or decision; the use relation; and the Work task. Mark each criterion mandatory or optional for this configuration decision and state pass, failure, qualification window, and stop observations. A user System may be human, automated, biological, organizational, computational, or mixed.
2. **Select only the needed Method content and branch by use.** Identify the admitted Method or status-preserved candidate account and its current ME.8 MethodDescription or candidate-account edition.

   **Direct branch:** when one owning direct result already returns the complete one-result/one-use selection and limits, retain that result with its receiver, exact action, named Method source, direct subject result, exact claim, exposure and loss, preserved status boundary, receiving task result, disposition, and return; take the C.37 direct exit. When the ME.10 task row owns that same use, embed those complete C.37 claims once in the task row. Do not create an ME.9 row or a duplicate standalone C.37 account, and do not report their absence as a gap.

   **Profile branch:** when complementary governed representations serve unlike named actions, consume one complete ME.9 profile. Require one complete C.37-bearing row for every action, then require the separate cross-use result that returns all rows to the same Method source and records correspondences, conflicting omissions, edition relations, keep-separate decisions, and changes that reopen several rows. If the source account, a direct result, reliance or receiving layer, one action row, or the cross-use result is missing, stale, or for another action set, return that exact gap instead of importing colocated artifacts as a profile.
3. **Identify the participating Systems and current relations.** Keep the project, users, provider, repository, tools, and automation as independently identified Systems where applicable. State actual access or provision, assignment, permission, authority, capability, publication, and direct System-use relations separately; return a missing relation rather than inferring it from configuration.
4. **Construct candidates against the same task set.** Compare at least two materially different routes, or state why no smaller route could meet the rows. For every candidate, map every mandatory and optional task criterion, stop, burden, risk, and required relation. Include cross-task effects such as shared currentness, duplicated maintenance, conflicting confidentiality, latency, provider exposure, or incompatible authority. A per-task minimum does not automatically make their union a smallest shared configuration.
5. **Keep evidence status distinct.** For each candidate-and-criterion cell record ordinary evidence status: observed pass, observed failure, untested, insufficient because a declared feature or relation is absent, or unknown because information is missing. These phrases are task-account content, not new FPF kinds. Do not convert `untested` into `insufficient`, or a pass by one route into failure by another.
6. **Compare and retain without forcing a winner.** A small reversible case may use an ordinary comparison row when explicit yes/no coverage and burden make the order clear. When comparison is multi-criteria, partial, evidence-gated, or otherwise non-trivial, use `A.19.CPM` and, when selection is required, `A.19.SelectorMechanism`; preserve incomparability, `degrade`, `abstain`, and a selected set. Claim one smallest sufficient route only when it covers every mandatory criterion, violates no stop, and the declared comparison and selection basis supports a singleton. Otherwise retain the alternatives and missing priority or evidence, or split the arrangement by a stated task, user, confidentiality, authority, or maintenance boundary.
7. **Configure only a justified test route or retained set.** Set the retrieval and selection aids, status and provenance cues, tailoring rules, tool or automation behavior, provider boundary, decision boundary, feedback receiving use, and stop conditions supported for the declared tasks. Choosing a candidate for bounded testing is not an A.22 structure selection and does not erase other retained candidates.
8. **Add a curated Method Base only when needed.** Identify the project or namespace, collection purpose, current entry-disposition rule, admitted entry kinds, return conditions, edition policy, and continuity. Institute membership only through the identified granted-permission occurrence, admitted Work, operation application, result binding, and direct belongs-to predicate required by the local declaration. A label, folder, record, result token, or publication occurrence creates no membership.
9. **Select an A.22 structure only when organization changes the action.** Identify independently admitted constituents, the identified obtaining relation occurrences selected, applied constraints, and named use frame. Then identify the selecting System, Method, dated selection Work, and direct participation or operation-binding facts. If those neighboring facts are missing, keep the proposed organization and return `missing-selection-basis`.
10. **Keep editions and reliance accounts separate.** Maintain a C.2.1 episteme about the Method Base edition and, when a receiving decision needs it, a separate named-use episteme that states the identified Systems, Work, capabilities, and direct relations relied on. Use C.13 only when a materialized construction account changes the receiving use. Publication and actual access remain separate results.
11. **Choose and run task probes.** Cover every materially different mandatory task family with a representative row or state why one observed row covers several; add at least one discriminating condition for each live weakness that can change the configuration decision. For a simple case, admit and observe each actual task Work directly. When configuration or recovery under interruption, handoff, changed performer, stale state, or support loss matters, apply one `A.15.8` actual-Work or present-WorkPlan branch at a time and use its weakest decision-changing probe. Admit performed probe Work separately. Do not call convenience statistically representative or merge several Work foci into one.
12. **Repair, recompare, and rerun only the affected position.** Change the material, System, relation, constraint, access condition, assignment, permission, authority, capability input, edition fact, provider boundary, feedback path, or user step that defeated a criterion. Preserve unaffected collection, proposal, candidate, and task facts. Rerun the same criterion. If the bounded task set, candidate universe, criteria, scope, evidence status, or window changes, make a new comparison or selection use rather than reusing the prior minimum.
13. **Return the bounded result and next use.** Report per-task evidence status, supported configuration, retained candidate set, split boundary, failed task, changed position, rerun result, or named missing premise. State whether it can feed a representative Method trial, a description or representation correction, a collection repair, another user-task repair, or later capability development. Reopen only the affected row, configuration comparison, or directly governed result.

#### ME.10:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| bounded task set | One row per named user System and use: material or aid, receiving Work or decision, use relation, Work task, mandatory or optional criterion, pass and failure observations, qualification window, and stop. |
| Method material | Admitted Method or candidate status and current MethodDescription or candidate-account edition. Direct branch: one complete one-result/one-use answer, or one ME.10 task row embedding the applicable C.37 group once, with receiver/action, direct subject result, exact claim, applicable evidence/reliance layers, receiving result, exposure and loss, disposition, status boundary, provenance, currentness, and return. Profile branch: one complete ME.9 profile containing those complete action rows plus its separate cross-use result for shared source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. A missing ME.9 result is a gap only when the profile branch is required. |
| participating Systems and relations | Independently identified Systems and the access, provision, assignment, permission, authority, capability, publication, direct-use, and other relations that obtain or remain missing. |
| candidate universe | Candidate configurations and their coverage of the same task rows, stops, burdens, risks, cross-task effects, and required relations. |
| evidence matrix | Per candidate and criterion: observed pass, observed failure, untested, insufficient by a declared missing feature or relation, or unknown from missing information; source and window for each observation. |
| comparison and choice | Cheap ordinary comparison or cited A.19 comparison and selected-set basis; retained candidates, singleton justification, unresolved priority or evidence, abstention, or stated split boundary. |
| configured route | Retrieval, comparison, tailoring, tool or automation, provider, feedback, and decision conditions chosen for testing or supported for the bounded task set. |
| optional collection | Collection identity and purpose, entry rule, identified membership occurrences, edition, publication, and any construction account, each separately identified. |
| optional structure | Constituents, selected relations, constraints, use frame, selection-use basis, or proposed organization plus the named missing fact. |
| test selection | Representative coverage of the materially different task rows, discriminating changed conditions, any A.15.8 actual-Work or WorkPlan branch, and pass or failure observations chosen before Work. |
| observed Work | Each admitted user or probe Work occurrence, direct System interaction actually used, observation, task result, evidence status, and gap. |
| repair and rerun | Failed criterion, smallest changed position, preserved facts, rerun result, and any new comparison required by a changed task set or basis. |
| return | Supported configuration, retained candidate set, split boundary, bounded task pass, named defect, missing priority or test, non-overread, next use, and reopen condition. |

#### ME.10:4.3 - What Changes in Practice

Teams stop measuring progress by uploaded files, platform features, or one locally successful task. They can show which named uses a configuration covers, which are untested or incompatible, why one route is supported or several remain, and which edition, relation, condition, permission, authority, capability input, or Work result must change.

The same discipline makes automation safer. A user System or provider may be human or non-human and may retrieve, compare, or propose; performed Work, consumed output, permission, authority, capability, evidence status, and result remain visible and separately testable.

### ME.10:5 - Worked Build and Test Replays

#### ME.10:5.1 - Minimal One-Task Manual Replay

This small constructed replay shows the cheap branch without claiming field evidence. Assume that the named Method and MethodDescription editions are admitted and that the two retrieval occurrences are independently admitted under A.15.1; an actual use must supply those bases rather than inherit them from the example.

`CalibrationEngineer-5` must retrieve the current description of admitted Method `M-Calibrate-Sensor-B` for planned calibration Work. The pass criterion is: return `MD-Calibrate-Sensor-B-v4`, its current status, applicability to sensor family B, and the stop for an unknown serial class. The failure criterion is return of another edition or omission of status, applicability, or stop.

This is one receiver and one exact action. Candidate `REP-Cal-B-Retrieval-1` is a `C.2.1` episteme constituted by the maintained index row. Its exact use claim is that v4 is the current family-B description and carries the unknown-serial stop for this retrieval. It exposes currentness, applicability, the stop, and publication link; it withholds a stable audit digest and makes no capability, permission, authority, Work, or calibration-result claim. The ME.10 task row is the owning domain result for this use and carries the receiving task criterion, observation, and return. That one embedded realization supplies the complete one-result/one-use selection boundary, so the `C.37` direct exit applies: no ME.9 profile row and no duplicate standalone C.37 account are created. If a later decision relies on the retrieved content as evidence, its exact A.10 path and disposition must be added for that later use.

The initial shared-folder route contains v3 and v4 but exposes neither currentness nor applicability. In `W-ME10-Retrieve-Cal-B-0`, the user retrieves v3; the task returns `task-fail[wrong-edition]` without changing either edition or admitting a capability claim.

| Candidate configuration | Criterion coverage and burden | Disposition |
| --- | --- | --- |
| Rename v4 to “FINAL” and leave both files in the folder | Cheap, but the label supplies no governed currentness relation, applicability, or stop and obscures why v3 remains. | Insufficient for the declared criterion. |
| Add one manually maintained index row naming the Method, v4, currentness basis, family-B applicability, unknown-serial stop, and publication link | Covers every current criterion with one new episteme and no new platform. The folder remains a carrier; the index does not become the Method, publication occurrence, Work, or authority. | Retain as the only currently supported sufficient configuration for this one-task set; this does not exclude the untested portal. |
| Build a search portal with automated recommendations | Could add later functions, but no present criterion requires them and their provider, access, suggestion-use, and authority relations are ungrounded. | Untested and larger than this one-task need; do not claim failure. |

The repair adds only the retained index row and its maintained currentness cue. In `W-ME10-Retrieve-Cal-B-1`, the same user retrieves v4, sees family-B applicability, and stops on an unknown serial class. The receiving task result is `task-pass` for this exact retrieval action, so the use-bounded row disposition is `select` inside the stated v4/family-B window. Return if the source edition, currentness cue, applicability, unknown-serial stop, or task observation changes.

For the bounded set containing only this task, the currently supported set is the singleton containing the index row: the rename route is insufficient by its declared missing features, while the portal remains untested and is not ruled out as logically insufficient. This establishes neither unique sufficiency nor multi-task minimality, Method fit, general user capability, a selected A.22 structure, or worth in another project.

#### ME.10:5.2 - Two-Task Trade-off with Two Retained Candidates

Extend the constructed case with a second mandatory action. `CalibrationEngineer-5` must retrieve the current description for planned family-B calibration Work. Computational user System `AuditService-2` must use the exact v4 edition in `ReleaseAudit-7` under a stable digest and audit currentness record. These are different receiver/action pairs, so they require different use-bounded claim groups even when one maintained source could realize both. No `AuditService-2` task Work has yet occurred.

The Method-specific problem is now cross-use allocation of complementary governed representation results. The ME.9 profile branch applies. Each row below embeds the applicable complete `C.37` group and preserves admitted Method `M-Calibrate-Sensor-B` and current ME.8 result `MD-Calibrate-Sensor-B-v4` as its source. The rows select for their own actions; they do not yet constitute the ME.9 cross-use result or select a support configuration.

| ME.9 row and exact action | Direct result, exact claim, and reliance | Exposure and loss | Receiving result, disposition, and return |
| --- | --- | --- | --- |
| `MRP-Cal-B-Retrieve-1`: `CalibrationEngineer-5` retrieves material for planned family-B calibration Work. Qualification window: the currentness cue is checked at retrieval and remains usable only for that v4 family-B use through the planned Work. | `REP-Cal-B-Retrieval-1` is the directly governed `C.2.1` index episteme. Exact claim: v4 is current for family B and carries the unknown-serial stop and publication link. A.2.4 classifies the intended status-evidence use. A.10 path `P-Cal-B-Retrieve-v4` carries that currentness/applicability premise with `RelianceDisposition=pass` inside the stated window. | Exposes current edition, family-B applicability, stop, and link; omits the stable audit digest and audit currentness record, which this action does not require. | `task-pass` from `W-ME10-Retrieve-Cal-B-1`; `select` for this retrieval action. Return to ME.8 for changed source claims, `C.2.1` or A.10 for a failed direct result, or this row when the use, window, disposition, or observation changes. Stop if the edition or cue changes, applicability no longer covers family B, or the serial class is unknown. |
| `MRP-Cal-B-Audit-1`: `AuditService-2` uses the exact edition in `ReleaseAudit-7`. Qualification window: at audit start the currentness record must identify v4 and the stable digest must identify the exact v4 bytes used by that audit run. | `REP-Cal-B-Audit-1` is a governed `C.2.1` audit-register episteme tied to a separately identified `E.24.PUB` publication result. Exact claim: the named digest and record bind the audit use to the current v4 edition. A.2.4 classifies the intended audit-evidence use. A.10 path `P-Cal-B-Audit-v4` returns `RelianceDisposition=abstain` until the digest/currentness pair is checked inside the audit window; missing, stale, out-of-window, or mismatched values stop before reliance. | Exposes edition identity, stable digest, and audit currentness record; omits the human applicability explanation and unknown-serial stop, which this action does not consume. Publication does not supply reliance or the task result. | `missing-task-test[AuditService-2]`; no audit task Work exists and no `task-pass` is claimed. The row is `unresolved`, not failed. Return to ME.8 for changed source claims, `C.2.1`, `E.24.PUB`, or A.10 for a failed direct result, or this row when its use, window, stop, task observation, or disposition changes. |

ME.9 now returns cross-use profile result `MRP-Cal-B-Retrieve-Audit-1` rather than treating row colocation as composition:

| Profile position | Cross-use result |
| --- | --- |
| shared Method source | Both rows return to admitted Method `M-Calibrate-Sensor-B` and current MethodDescription `MD-Calibrate-Sensor-B-v4`. |
| cross-use correspondence | The retrieval currentness cue and the audit digest/currentness pair must designate the same exact v4 edition. Matching the label `v4` is insufficient; a changed edition reopens both rows and this correspondence. |
| conflicting omissions | Retrieval needs family-B applicability and the unknown-serial stop but omits the stable digest. Audit needs the digest and audit-currentness record but omits the human applicability explanation and serial-class branch. Combining the presentations does not erase either omission or prove consistency. |
| edition relations | The retrieval row is qualified for the planned family-B Work window; the audit row is qualified only for the named `ReleaseAudit-7` run after its digest/currentness check. A serial-class change can reopen retrieval alone; a digest mismatch can reopen audit alone. |
| keep-separate decision | `REP-Cal-B-Retrieval-1`, `REP-Cal-B-Audit-1`, their C.37 dispositions, and their receiving task results remain separate. The profile creates no super-representation, common task pass, publication, or support arrangement. |
| profile return | Retain retrieval as `select` and audit as `unresolved`; return `missing-task-test[AuditService-2]` and the unchecked digest/currentness relation. Reopen both rows only when their shared source identity or correspondence changes. |

The configurations below compare how those two governed results and the explicit cross-use relation could be supplied and maintained. `C.37` does not choose among them, and the ME.9 profile does not rank them; ME.10 retains that configuration decision.

| Candidate configuration | Engineer retrieval row | Audit-service row | Cross-task burden and disposition |
| --- | --- | --- | --- |
| Manual index row only | Observed pass in `W-ME10-Retrieve-Cal-B-1`. | Insufficient: the editable row supplies no stable publication digest or audit currentness record. | Exclude for the two-task mandatory set. |
| One signed read-only register supplies separate retrieval and audit presentations | Untested for the engineer; its declared retrieval presentation can expose applicability and the stop. | Untested for `AuditService-2`; its declared audit presentation can expose the digest and currentness record. | One maintained source for two governed results, but the case lacks approval-latency evidence. Retain. |
| Manual retrieval index plus a signed audit log | The existing retrieval pass remains relevant to the index route. | Untested for `AuditService-2`; its declared design can expose the audit record. | Lower expected retrieval delay but duplicated currentness maintenance and an untested consistency relation. Retain. |

The last two candidates cover the declared features differently, but the case supplies neither audit-task evidence nor a priority between approval latency and duplicated currentness maintenance. The audit profile row therefore remains `unresolved`, the cross-use profile returns its unchecked correspondence and `missing-task-test[AuditService-2]`, and reliance stops; retain both candidates with `unresolved-configuration-choice[approval-latency-vs-duplicate-currentness-maintenance]`. If a receiving decision authorizes a split, name the user/task boundary, currentness owners, and consistency relation; do not call the union globally minimal.

#### ME.10:5.3 - EC-417 B2 Bounded Task Set and Evidence

The EC-417 B2 material exists, but `TraceReviewer-17`, `SafetyReviewer-17`, and `ReleaseDecider-17` need support for three distinct tasks. The bounded set is fixed before evaluating configurations:

| Task row | Mandatory pass and stop observations |
| --- | --- |
| retrieval by `TraceReviewer-17` | Recover `MBE-EC417-B2-1`, candidate status, prompt episteme `ATP-2`, confidentiality boundary, and D0 stop. |
| tailoring by `SafetyReviewer-17` | Use the non-confidential fixture, preserve signed-before-closure, reject a stale edition, and stop on missing permission or authority. |
| branch selection by `ReleaseDecider-17` | Distinguish A, B2, and R and stop when assignment, permission, authority, confidentiality, or reversibility is absent. |

The receiving relations remain direct: `TraceReviewer-17` retrieves the edition and prompt episteme for trace-review preparation; `SafetyReviewer-17` uses the tailoring aid in named tailoring Work; `ReleaseDecider-17` uses the selection aid in named branch-selection Work. None is release Work or the release decision.

| Candidate configuration | Evidence against the same three rows | Disposition for this case |
| --- | --- | --- |
| Published files and manual lookup only | The case supplies no performed task evidence for current status, `ATP-2`, D0, stale-edition rejection, signed-before-closure, or A/B2/R stops through this route. | Untested. Do not call it failed or insufficient from absent task evidence alone. |
| Bounded PLM retrieval and selection aids plus the non-confidential CI tailoring fixture | The case supplies one observed pass for each of the three declared rows through the identified PLM and CI Systems. | Supported configuration for these three tests; no claim of global minimality or parity superiority. |
| Add an AI-provider route and feedback path | The case supplies no AI-provider interaction, used suggestion, review of such a suggestion, feedback Work, or feedback receiving use. No mandatory row currently requires this branch. | Outside the supported pass and untested; retain as named gaps, not features. |

The configured PLM/CI route includes the Method Base edition and status cues, PLM retrieval and branch-selection aids, the CI fixture and stale-edition rejection, `ATP-2`, and the confidentiality, signed-evidence, assignment, permission, authority, reversibility, and D0 stops. The manual and AI routes lack parity evidence, so this table does not select the globally smallest arrangement. It identifies the only configuration currently supported across the bounded three-task set. It is not an A.22 selected structure.

#### ME.10:5.4 - Three Performed Tasks and Their Bounded Reach

| User Work | System interaction and observed result | Result boundary |
| --- | --- | --- |
| `W-MESUP-EC417-Retrieve-1` by `TraceReviewer-17` | The user retrieves `MBE-EC417-B2-1` through `SYS-EC417-PLM-1` and recovers candidate status, `ATP-2`, the confidentiality boundary, and the D0 stop. The local `SupportSystemUsedInWork@EC417` occurrence obtains for that Work-System pair and interaction interval. | The result establishes this retrieval task only; it creates no general access entitlement, capability, or authority. |
| `W-MESUP-EC417-Tailor-1` by `SafetyReviewer-17` | The user applies the tailoring aid with a non-confidential `SYS-EC417-CI-1` fixture, recovers signed-before-closure, and rejects the stale edition. Its separate direct System-use occurrence obtains. | The result establishes this tailoring observation only; it does not perform release Work or approve closure. |
| `W-MESUP-EC417-Select-1` by `ReleaseDecider-17` | The user applies the selection aid through `SYS-EC417-PLM-1` to distinguish pre-entry A, bounded B2, and post-entry R and stops B2 when a named assignment, permission, authority, confidentiality, or reversibility condition is absent. Its separate direct System-use occurrence obtains. | The result establishes this bounded selection task only; the tool does not make the release decision or acquire authority. |

`RES-MESUP-EC417-B2-1` therefore returns `task-pass` for these three Work occurrences and the observed retrieval and status, tailoring and stale-edition, branch-selection, and stop results. No AI-provider interaction, used AI suggestion, review of such a suggestion, feedback SpeechAct, or feedback receiving use is part of that pass. Retrieving `ATP-2` is not provider use.

No repair and rerun occurrence is asserted for EC-417 because the case supplies three passes, not a performed failed task. If a later task fails, apply step 12 and add its Work and rerun rather than rewriting these histories. The minimal one-task replay supplies the filled failure-repair-rerun branch; the two-task extension supplies the unresolved-trade-off branch.

#### ME.10:5.5 - Proposed Organization, Not a Selected Structure

`PSO-EC417-B2-Use-1` is a case-local proposal designator. Its four candidate A.22 groups remain disjoint:

1. the identified collection, entries, edition, aids, prompt episteme, Systems, and three Work occurrences;
2. two instituted entry-membership occurrences and the three direct PLM and CI System-use occurrences;
3. current-edition, status, confidentiality, signed-before-closure, assignment, permission, authority, reversibility, and D0 constraints; and
4. the use frame for retrieval, comparison, tailoring, and bounded PLM and CI use for `WP-EC417-B2-Trial-1`.

The case supplies no selecting System, enacted selection Method, dated structure-selection Work, or direct participation or operation-binding facts. `ESA-EC417-B2-1` returns `missing-selection-basis` and designates no selected `U.Structure`. This gap does not erase the three task observations.

#### ME.10:5.6 - Collection and Edition Remain Subordinate Results

`MBC-EC417-B2-1` identifies the project collection and its entry-disposition rule. Two admitted curator Work occurrences, their permissions and operation applications, positive result bindings, and identified `MethodBaseEntryBelongsTo@Project` predicates establish membership for the candidate-account and WorkPlan epistemes. The collection, membership episodes, assertion or evidence accounts, optional construction account, edition, publication occurrence, and named-use reliance episteme remain separate results.

Those facts make the named material eligible for the three user tasks; they do not show that the tasks succeeded. Conversely, the three task passes do not prove general capability, select the proposed structure, admit `C-EC-Release-v2` as a Method, perform release Work, or establish Method fit or effectiveness.

### ME.10:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| task-set omission bias | One visible task defines the arrangement while another mandatory use remains invisible. | Build one row per named user and use, then compare every candidate against the same bounded set. |
| forced-winner bias | A local minimum or one observed pass becomes the single arrangement despite incomparability. | Preserve retained candidates, missing priorities, abstention, or a stated split boundary. |
| evidence-status bias | No test evidence is reported as failure or insufficiency. | Separate observed pass, observed failure, untested, feature-level insufficiency, and missing information. |
| repository bias | Uploading files is reported as a usable Method Base. | Test the declared task rows and retain the collection predicates separately. |
| platform bias | Feature breadth replaces the failed task set. | Include an element only for a named criterion, stop, cross-task dependency, or directly supported relation. |
| tool-authority bias | A recommendation or branch display becomes a decision or permission. | Keep tool interaction, user Work, permission, authority, and result separate. |
| structure-selection bias | A complete proposal table becomes an A.22 selected structure. | Require the selecting System, Method, Work, and participation or binding facts. |
| success inflation | One task pass becomes capability or Method-effectiveness evidence. | Bound the result to observed Work and return neighboring claims separately. |

### ME.10:7 - Conformance Checklist

- [ ] A bounded task set names one user System and exact action per row, the actual material or aid, receiving Work or decision, use relation, mandatory or optional criterion, pass and failure observations, window, and stop.
- [ ] Human, automated, biological, organizational, computational, and mixed users remain possible; performer, capability, permission, and authority claims use their direct governors.
- [ ] In the direct branch, one owning direct result or ME.10 task row supplies the complete one-result/one-use selection and limits. Its receiver/action, direct subject result, exact claim, exposure and loss, receiving task result, disposition, and return remain recoverable; no ME.9 row or duplicate standalone C.37 account is created.
- [ ] In the profile branch, every consuming action recovers one complete row with its embedded C.37 claim group, required Method claims, direct governed result, applicable evidence/reliance layers, receiving result, exposure and loss, status boundary, disposition, and return.
- [ ] The same branch also recovers one ME.9 cross-use result that names the shared Method source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and changes that reopen several rows. Row colocation is not that result.
- [ ] Neither C.37, an action row, nor the ME.9 cross-use result is treated as selecting the support configuration, admitting a Method, publishing material, establishing access, capability, authority, Work, or task success.
- [ ] Every candidate configuration is checked against the same task rows, stops, burdens, risks, cross-task effects, and evidence window.
- [ ] Observed pass, observed failure, untested, feature-level insufficiency, missing information, and an unresolved use-bounded row are not substituted for one another.
- [ ] A singleton is returned only from a declared comparison and selection basis; otherwise retained candidates, abstention, a split boundary, or a missing priority or test is explicit.
- [ ] A simple task uses the cheap branch; configuration or recovery testing reuses A.15.8, and non-trivial comparison or selection reuses A.19 rather than copying their kernels.
- [ ] Project, user, provider, repository, tool, and automation Systems and their access, assignment, permission, authority, capability, publication, direct-use, Work, and task-result facts remain separate.
- [ ] A curated collection has a project or namespace, purpose, current rule, identified membership predicates, edition policy, and return conditions.
- [ ] An A.22 selected-structure result has all four discriminator groups plus an actual selection-use basis; otherwise the result remains a proposal and returns the named missing fact.
- [ ] Each positive task result rests on independently admitted Work and the direct relations actually observed.
- [ ] Provider or AI use, review, feedback, capability, fit, effectiveness, transfer, and authority are claimed only when their own facts obtain.

### ME.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The Method Base is the repository.” | Identify the collection, membership rule, edition, publication, access, task set, and observed uses separately. |
| “The profile row chose the support arrangement.” | Use the row only for its exact representation/action claim group; compare and select support configurations in ME.10. |
| “C.37 selected the representation, so the task passed.” | Keep use-bounded disposition separate from performed Work and the receiving task result. |
| “The PLM route passed, so manual lookup is insufficient.” | Record PLM as observed pass and manual lookup as untested unless a declared missing feature proves insufficiency. |
| “Choose the smallest arrangement for each task and combine them.” | Check shared currentness, maintenance, confidentiality, latency, authority, and provider effects; return a retained set or stated split when the union has no supported order. |
| “The interface gives users access.” | Establish the actual access relation and relevant permission; an interface is only one System or presentation element. |
| “The AI supported the decision.” | Name provider interaction, consumed suggestion, reviewing Work, permission, authority, result, and evidence separately, or return the missing branch. |
| “All components are listed, so the structure is selected.” | Keep a proposed organization until A.22 selection-use facts obtain. |
| “Three users passed, so the team is capable.” | Report the three Work-task observations and evaluate capability under `A.2.2` only when its holder, Work family, envelope, measures, and window are present. |
| “Feedback is available through the form.” | Require actual feedback Work or SpeechAct and a named receiving use before claiming feedback occurred or was used. |

### ME.10:9 - Consequences

Method material becomes usable through declared task coverage and observed Work rather than through platform completion claims. Repairs are smaller because the defeated task row, edition, representation-use claim, relation, constraint, permission, authority, capability input, interaction, or Work result is visible. A useful result may be one supported configuration, several retained candidates, a stated split, or a missing priority or test.

The cost is maintaining separate accounts of the uses and their participants. Direct subject results, use-bounded rows, collections, editions, publications, Systems, relations, user Work, criteria, evidence status, and results must be maintained separately. Some sophisticated features remain untested; some choices remain set-valued; and a proposed organization may remain unselected even when all bounded tasks pass.

### ME.10:10 - Rationale

Enactment assistance is relational and work-bound. A repository can hold material; a representation can expose a claim; a tool can return a value; a provider can offer a service; a user System can perform Work; a policy can institute permission; an assignment or authority relation can obtain. None substitutes for the others.

Current FPF supplies the generic one-receiver/one-action representation-selection discipline in `C.37`, configuration-and-recovery in `A.15.8`, and comparison and set-valued selection in `A.19.CPM` and `A.19.SelectorMechanism`. ME.10 specializes those moves for Method material and adds the bounded task-set bridge across Method or candidate status, ME.8 results, Method Base collection and edition facts, retrieval, tailoring, provider and AI particulars, and their receiving uses.

The direct branch remains cheap. When one owning result already returns the complete one-result/one-use answer and limits, ME.10 retains it without an ME.9 row or duplicate C.37 account. When the ME.10 task row owns that same use, it embeds the complete C.37 claim group once. ME.10 opens ME.9 only when unlike named actions require Method-specific allocation of complementary governed representations. It then consumes both the complete action rows and ME.9's separate cross-use result for source correspondence, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. Neither C.37 nor that ME.9 profile result selects the support configuration.

The residual orchestration is DPF synthesis qualified for this edition, not evidence of universal superiority: construct task rows from named Method-material uses, choose the cheap or governed comparison and recovery branch, and route observed gaps to their direct owners. Its current evidence is limited to the constructed one-task and two-task replays plus bounded EC-417 observations. Reopen when an unlike Method-material task defeats this routing, a current FPF dependency changes, or direct mature practice supplies a better domain specialization.

### ME.10:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Daalhuizen and Cash, [Method content theory](https://doi.org/10.1016/j.destud.2021.101018); Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Adopt user-relevant content, representation, tools, adaptation conditions, and intended-use questions. | These inputs help construct task rows; they do not establish task Work, configuration adequacy, or one selected arrangement. |
| Gericke et al., [method ecosystems](https://doi.org/10.1017/dsj.2020.21) | Adapt attention to interacting Methods, actors, tools, representations, and organizational conditions. | The position paper identifies no universal platform or selected structure. Practitioners keep Systems, relations, task criteria, and evidence status explicit. |
| Stacey et al., [Methods as engineering knowledge](https://doi.org/10.1017/dsj.2025.9) | Adopt maintained knowledge, provenance, retrieval, and use as engineering concerns. | Knowledge maintenance, publication, and availability do not establish actual user Work, task coverage, fit, or effectiveness. |
| Inkermann, [AI-supported design-Method use](https://doi.org/10.1017/pds.2026.10419) | Adopt explicit AI contribution, criteria, provider-to-output traceability, transparency, responsibility, and feedback questions. | The framework is exploratory. It supplies no autonomous authority, effectiveness, or general configuration-selection claim; EC-417 keeps provider use and feedback untested. |
| Current FPF `C.37` | Reuse one receiver/action boundary, direct-result and reliance layers, exposure and loss, use-bounded disposition, direct exit, embedded-or-standalone realization, and return. | ME.10 embeds the group once in an owning task row or consumes it as an action row inside a complete ME.9 profile. ME.9's cross-use result remains separate. C.37 does not choose a support configuration or establish Method, access, capability, authority, Work, or task success. |
| Current FPF `A.15.8` | Reuse its actual-Work versus present-WorkPlan branches, separately identified performers and supports, weakest decision-changing probe, continuation or recovery observation, and direct-relation repair. | ME.10 supplies Method-material task rows and domain-specific inputs. It uses a cheap direct task test when recovery configuration is not the live question. |
| Current FPF `A.19.CPM` and `A.19.SelectorMechanism` | Reuse explicit criteria, evidence-gated comparison, incomparability, abstention, and set-valued selection for non-trivial configuration choices. | ME.10 supplies the configuration candidates and Method-material criteria; it does not redefine comparison or selection, hide scalarization, or force a singleton. |
| Current FPF `A.22`, `A.2.2`, `A.2.8.PER`, `A.6.REL`, `A.6.1`, `A.13`, `A.15.1`, `C.2.1`, `C.13`, and `E.24.PUB` | Reuse structure selection, capability, permission, direct-relation, operation-application, performer and Work-admission, episteme, collection-account, and publication boundaries. | ME.10 retains only its Method Base, named-use configuration, task-set, and result-routing specialization. |
| Residual ME.10 DPF synthesis | Combine named Method-material uses into a bounded task set, choose the cheap or governed comparison and recovery branch, preserve evidence status, and return the supported configuration, retained set, split, or gap to its direct owner. | This is qualified expert synthesis, not a replacement for C.37, A.15.8, or A.19 and not proof of general effectiveness. Return `missing-task-set`, `missing-configuration-basis`, `missing-task-test`, or `unresolved-configuration-choice[...]` when the move cannot justify a stronger result. |

Reopen when a mandatory action cannot be represented without a different use boundary; a complete C.37 group no longer fits its owning task or ME.9 action row; the ME.9 cross-use correspondence, omission, edition, keep-separate, or multi-row return is missing or defeated; an unlike task defeats the residual specialization; current C.37, A.15.8, or A.19 changes the consumed move; actual provider or feedback Work changes a gap; a selection-use basis establishes the proposed A.22 structure; or a collection, edition, or reliance problem gains an independent practitioner use and stop that may justify a separate pattern.

### ME.10:12 - Relations

- ME.8 supplies use-bounded MethodDescription or candidate-account content. In the direct branch, ME.10 retains one complete one-result/one-use answer or embeds the applicable C.37 claim group once in its owning task row; it creates neither an ME.9 row nor a duplicate standalone C.37 account. In the profile branch, ME.9 supplies one complete C.37-bearing row per unlike named action and a separate Method-specific cross-use result that relates the rows without flattening them. ME.10 consumes that complete profile as input to its own support-configuration comparison.
- `C.37` governs use-bounded representation selection and co-use. It does not select the support configuration, establish Method status, publication or access, capability, authority, Work, task result, or arrangement adequacy.
- `A.15.8` governs generic actual-Work or present-WorkPlan performer-support configuration and recovery probes. ME.10 supplies Method-material-specific users, tasks, supports, criteria, and repair returns.
- `A.19.CPM` governs non-trivial comparison results; `A.19.SelectorMechanism` governs set-valued selection. ME.10 does not turn a configuration pass into a forced winner.
- `A.22` defines selected structures and their discriminators; a retained candidate, proposal label, colocation, or selected test route establishes none of them.
- `A.2.2` defines capability; `A.2.8.PER` defines granted permission and exercise; `A.13`, `A.15.1`, and `F.6` define or constrain performer, Work admission, and assignment-bound attribution claims.
- `A.6.1` defines reusable operation declarations, applications, and result bindings; a result designator or record does not make an application occur.
- `C.2.1`, `C.13`, and `E.24.PUB` define or constrain the separate episteme, collection account, edition and publication, and carrier claims used here.
- A later representative Method trial consumes only tested task conditions and named gaps; coherence, fit, worth, capability development, and cultural continuation remain neighboring practices.

### ME.10:End

# Part IV - Trial and Separate Coherence, Fit or Transfer, and Worth Decisions

## ME.11 - Trial the Method in Representative Work

>
> **Primary working result:** occurrence-level trial evidence and explicit missing-evidence positions for the separate ME.12 coherence, ME.13 fit or transfer, and ME.14 practical-worth decisions. A candidate Method account remains a candidate; only independently admitted Work is reported as having occurred, and only independently admitted Methods as having been enacted.

### ME.11:0 - Use This When

Use this pattern when a Method or candidate Method account is ready for a trial in actual Work and the next decisions need observations from named situations rather than another plan, demonstration, or document review. Begin with one trial question: what must be learned from actual Work for a later coherence, fit, transfer, or worth decision?

The first useful result is a trial-slice row. It names the subject and its status, the situation-selection reason, the planned task, the Work that actually occurred, actual performers and enacted admitted Methods, relied-on Systems and capabilities, observations, gaps, and the later decision that may use them. A row that returns `missing-performed-work` is useful when the trial remains only planned.

Here *trial* is Plain practice wording for intentionally selected Work and observation. It is not a new subtype of `U.Work`, a Method admission, an evaluation result, or a claim that the situation statistically represents a population.

Do not use this pattern to declare description coherence, situational fit, transfer, practical worth, capability, causal contribution, or general effectiveness. ME.11 makes later judgments possible; ME.12, ME.13, and ME.14 make those judgments under their own questions and evidence.

### ME.11:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| trial question | One evidence question whose answer can change a named later decision. | “Try the method” is not yet a bounded question. |
| representative situation | A situation selected because stated characteristics match the named current-use question. | The word does not imply random sampling, population coverage, or transfer. |
| discriminating situation | A situation selected because one changed condition can expose a claimed limit, burden, or failure. | Difference alone is insufficient; state which claim the changed condition can test. |
| WorkPlan | Intended performers, tasks, Methods, situations, observations, and stops. | A plan, script, simulation description, or scheduled demonstration is not performed Work. |
| admitted Work | One dated Work occurrence admitted under `A.15.1` from its actual performers, action history, enacted Method, temporal extent, and required containing-System relation. | A report, trace, attendance record, or output can support the claim but does not create the occurrence. |
| candidate-account trial branch | Actual Work is admitted separately while claims in a candidate Method account are compared with observations. | The candidate whole is not said to have been enacted. Only separately admitted constituent Methods may obtain in `enactsMethod` relations. |
| capability input | A claim about a holder System, Work family or result class, operating envelope, measures, qualification or currentness window, and evidence used for reliance. | Training, availability, assignment, permission, authority, or one success does not substitute for it. |
| trial evidence | Occurrence-level observations, source relations, burdens, adaptations, results, and gaps qualified for named later uses. | It is not itself coherence, fit, transfer, worth, contribution, or causal proof. |

### ME.11:1 - Problem Frame

Method trials are often easiest to describe after the fact: a team used some material, produced a result, and reported value. That compression hides what Method was admitted, which Work occurred, who performed it, which support conditions were present, what changed, and which conclusions the observations can support.

Convenient success cases also miss the situations that matter most. A Method may look usable in a familiar task and fail when feedback is closed-loop, information is incomplete, capability is stale, or a required relation is absent. Representative and discriminating situations therefore serve different purposes and must be selected for an explicit later question.

### ME.11:2 - Problem

A planned trial can be reported as performed Work. A candidate whole can be reported as enacted because some constituent activities occurred. Training completion can be reported as capability, tool logs as Work, immediate self-reports as lasting results, and one favourable occurrence as evidence of transfer or effectiveness.

These moves produce a positive story but weak evidence. Later reviewers cannot recover the actual occurrence, compare situations, separate Method claims from support conditions, or find the missing evidence that should stop a broader judgment.

### ME.11:3 - Forces

| Force | Tension |
| --- | --- |
| Real Work | Natural Work exposes practical burdens, while uncontrolled conditions complicate attribution. |
| Deliberate discrimination | Changed conditions can reveal a limit, while an artificial stress case may not answer the current-use question. |
| Status preservation | Candidate claims need testing, while useful Work must not be reported as enactment of an unidentified Method whole. |
| Observability | Later decisions need traceable observations, while instrumentation and reporting can burden or distort Work. |
| Capability | Performer ability can change the result, while training or one success invites premature capability claims. |
| Failure value | Failure can localize a correction, while teams and sponsors are biased toward a favourable trial narrative. |
| Evidence reach | Several occurrences can strengthen a local account, while they still may not establish contribution, causality, transfer, or practical worth. |

### ME.11:4 - Solution

Select situations from the later evidence questions, arrange and observe actual Work, preserve every subject's status, and return occurrence-level evidence with explicit gaps and limits on the conclusions it supports.

#### ME.11:4.1 - Pattern-Use Unfolding

1. **Name the later decisions and trial questions.** Separate the questions that may feed ME.12 coherence, ME.13 situational fit or transfer, and ME.14 practical worth. Do not hide several conclusions inside “does the Method work?”.
2. **Preserve the subject branch.** Identify the admitted Method under `A.3.1`, or keep the proposed whole as a candidate account. In the candidate branch, state which candidate claims are being compared and which constituent Methods, if any, are separately admitted and may be enacted.
3. **Select one representative situation.** Name the intended-use characteristics that matter to the question: task purpose, development phase, technical or domain conditions, performer population, holder capabilities, participating Systems, direct relations, constraints, and qualification window. State why this situation covers the current question without claiming population representativeness.
4. **Select a discriminating situation when the decision needs one.** Change or seek one condition whose outcome can show whether a live claim holds in that situation: unfamiliar technical coupling, another domain, missing support relation, changed capability envelope, stale material, or another named alternative. State the claim that could fail. Do not require every trial to contain an artificial stress case.
5. **Write the WorkPlan without backdating Work.** State intended tasks, performers, admitted Methods, support conditions, observation points, protected conditions, burdens to record, stop rules, and the later use of each observation. Keep simulation and demonstration as planned or separately typed activities unless independently admitted Work occurs.
6. **Check capability and support inputs separately.** When reliance on capability changes interpretation, identify the holder System, Work family or result class, operating envelope, measures, qualification or currentness condition, and evidence. Recover only ME.10 material, access, tool, provider, feedback, and decision conditions supported for the relevant task rows; preserve retained candidates, split boundaries, untested conditions, and gaps rather than treating them as configured inputs.
7. **Admit only Work that occurred.** For each occurrence, recover every actual performer System and its A.13 basis, the action history, at least one admitted Method actually followed, temporal extent, and required containing-System relation under `A.15.1`. Add assignment attribution, System use, operation binding, affected referent, resource use, or result relations only when their own predicates obtain.
8. **Record conditions and departures.** For each Work occurrence, record the situation, relied-on Systems and direct relations, holder capabilities used in interpretation, deviations from the WorkPlan, adaptations, burdens, stops, domain results, and observations. Keep the domain result, report, log, and evidence-use relation separate from Work.
9. **Qualify the evidence reach.** Distinguish direct observation, participant report, source interpretation, observed association, contribution claim, and causal claim. Return the strongest supported level and name missing comparison, temporal, capability, relation, or alternative evidence.
10. **Return evidence by later use.** Send contradicted description or relation claims to ME.12, situation comparisons and an unlike-situation result to ME.13, and results, burdens, alternatives, side effects, and evidence limits to ME.14. Return `missing-performed-work`, `missing-method-admission`, `missing-capability-basis`, `missing-direct-relation`, or the named missing premise when a required condition is absent.

#### ME.11:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| trial use | Later decision, bounded trial question, qualification window, and stop. |
| subject status | Admitted Method, or candidate account plus each separately admitted constituent Method whose enactment is claimed. |
| situations | Representative and any discriminating situation, selection criteria, matched conditions, changed conditions, and claim each can test. |
| plan baseline | Intended Work, performers, Methods, support conditions, observations, burdens, protected conditions, and stop rules. |
| actual Work | Each admitted Work occurrence, actual performers, enacted admitted Methods, temporal extent, containing System, and deviations from plan. |
| relied-on conditions | Holder capabilities, Systems, Agent-performed Work, direct relations, access, assignments, permissions, authority, tools, providers, and support conditions that actually obtain or remain missing. |
| observations | Domain results, burdens, adaptations, failures, participant reports, direct observations, and their source or evidence-use relations. |
| reach and gaps | Supported observation level, unsupported contribution or causal overreads, missing evidence, and conditions that would reopen the slice. |
| return | Occurrence-level evidence routed separately to ME.12, ME.13, and ME.14, or a supported lower result. |

#### ME.11:4.3 - What Changes in Practice

Teams stop calling a scheduled exercise or positive report “the trial”. They can point to the actual Work, the admitted Method that was enacted, the conditions on which the result depended, and the named later question each observation can answer.

A failed or incomplete occurrence remains useful. It can expose a description defect, a representation difficulty, a missing support relation, a capability condition, or a situation boundary without being inflated into a universal verdict on the Method.

#### ME.11:4.4 - Minimal Constructed Trial Replay

The following is a constructed teaching replay, not field evidence. It shows the smallest result that lets later checks reuse the same Work without turning the trial into their conclusion.

`M-Unit-Review-1` is admitted for reviewing temperature-sensor calibration reports before release. Its current description tells the reviewer to identify every source unit, normalize values, compare them with the declared tolerance, and stop on an unresolved mismatch. `WP-ME11-1` plans two review tasks for the same week. `S-Rep-1` is a current same-unit report of the ordinary kind. `S-Disc-1` keeps the product, decision, reviewer, description, and support fixed but introduces a Celsius/Kelvin mismatch; it is selected because the live claim is that the Method lets this reviewer expose a unit mismatch before release.

The interpretation relies on `CAP-R17-1`: holder `Reviewer-17`; calibration-report-review Work family; temperature-sensor-report envelope; measure “four of four seeded unit cases detected with description edition 4”; current through day D30; qualification record `QR-R17-1`. The qualification, assignment, permission to inspect the report, and release authority remain different facts. The trial also records description edition 4 and the manually retrieved conversion table as ME.10 support inputs.

Two occurrences then happen and are admitted separately. `W-Rep-1` is performed by `Reviewer-17` inside `Calibration-Team-A` from 10:03 to 10:10, enacts `M-Unit-Review-1`, accepts the same-unit report, and records seven minutes of review burden. `W-Disc-1` is performed by the same System in the same containing System from 11:14 to 11:26, enacts the same admitted Method, detects the mixed-unit condition during normalization, stops the release decision, and returns the report for correction; it records twelve minutes and one conversion-table lookup. The WorkPlan, two Work occurrences, domain decisions, timing record, and observation account remain separate.

| Later use | Evidence returned | Stop retained |
| --- | --- | --- |
| ME.12 coherence | The two occurrences identify the description edition and the operations actually followed; neither exposed an internal contradiction in this slice. | ME.11 does not conclude that the whole MethodDescription or Method construction is coherent. |
| ME.13 fit or transfer | The matched pair records one changed situation condition and the resulting task observations for one current holder. | One discriminating occurrence establishes no transfer to another holder, domain, tool, or qualification window. |
| ME.14 practical worth | The domain decisions, seven- and twelve-minute burdens, lookup, and stop are available for comparison with named alternatives. | A task pass establishes neither net worth nor causal contribution. |

If `W-Disc-1` had not occurred, return `missing-performed-work`; if its enacted-Method relation or relied-on capability basis were absent, return that missing premise. A favourable plan, simulated trace, or qualification record cannot replace the occurrence.

### ME.11:5 - Archetypal Grounding - SSFD Workplace Projects

The automotive SSFD programme supplies reports and review evidence about actual workplace projects without supplying a universal effectiveness claim. More than 300 engineers participated in a three-year transfer programme; training was followed by supported four-to-six-month workplace projects. Seventy-two of the first 100 reviewed project reports recorded SSFD use, and 41 contained enough detail for deeper analysis. Across those 41, the study reports 95 examples of evidenced individual benefits while distinguishing direct and indirect contribution.

The published paper is an evidence source, not an occurrence registry. A local application may admit a particular project Work occurrence only when its records recover the actual performer Systems and A.13 bases, action history, enacted admitted Method, temporal extent, and containing-System relation required by A.15.1. Otherwise retain the published project account as report evidence and return the missing occurrence or performer basis. The slices below show how the reported evidence can distinguish between possible answers to the later questions; they do not admit Work by citation.

#### ME.11:5.1 - Preserve the Status Branch

Before using the replay, establish whether SSFD is an admitted Method for the current FPF use. If it is, each supported project occurrence may be tested for its own obtaining `enactsMethod` relation. If it is not, admit the workplace Work independently, retain the SSFD account as a candidate, and name only separately admitted constituent Methods as enacted. The report statement “used SSFD” does not perform either admission automatically.

#### ME.11:5.2 - Representative and Discriminating Slices

| Slice | Reported project facts used | Evidence returned | Stop retained |
| --- | --- | --- | --- |
| Project 11 | The report concerns functional analysis of a new by-wire steering system and records 48 failure modes for four system functions, 44 new requirements and design rules, 44 test cases for individual systems, and 33 requirements and test cases for the overall system. | One bounded application account for checking whether description, representation, and support claims were usable in that project situation, plus the reported results and burdens available from the source. | Do not infer that this project caused or preceded Project 32, that every programme participant had the same capability, or that the reported benefits came from SSFD alone. |
| Project 32 | The report exposes difficulty representing the relation between a closed-loop sensor and controller. | A discriminating representation difficulty for ME.12 and an ME.13 unlike-situation comparison. ME.12 can return it to ME.9 only when several unlike Method-related actions are current, the owning action has a complete C.37-bearing row, and the profile's shared source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return are recoverable. Otherwise the difficulty stays with C.37 or the direct FPF representation governor. | Do not turn the difficulty into general Method failure or claim that Project 11 supplies the counterfactual. |
| 41-report evidence set | The review identifies 95 examples of evidenced individual benefits across business results, process improvement, and product-development-team capability improvement, while separating direct and indirect contribution. | Bounded report and review evidence for later comparison of results, burdens, and evidence strength in ME.14. | Counts and source classifications do not establish causality, universal superiority, transfer, or current capability for every participant. |

The useful ME.11 result is therefore not “SSFD works”. It is a set of reported workplace-project accounts, situation and support conditions, observed representation difficulties, reported results and burdens, evidence-source qualifications, and explicit gaps for three separate later judgments.

#### ME.11:5.3 - APP-ME-01 Early Stop

In `APP-ME-01`, the three-release statement remains a WorkPlan. The three named-user retrieval, tailoring, and selection-support occurrences from ME.10 establish only those support tasks; they do not perform a release or enact the candidate whole `C-EC-Release-v2`.

Add a release trial occurrence only after its release Work, actual performers and their A.13 bases, enacted admitted constituent Methods, participating Systems, Agent-performed Work, relied-on capabilities and direct relations, conditions, domain result, burdens, deviations, temporal extent, containing System, and authority facts are recovered. Until then return `missing-performed-work`. Even after a release is admitted, keep `C-EC-Release-v2` as a candidate and send the occurrence evidence separately to ME.12–ME.14.

### ME.11:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| plan-completion bias | A scheduled or demonstrated task is recorded as trial Work. | Admit each actual Work occurrence separately; otherwise return `missing-performed-work`. |
| candidate-laundering bias | Constituent activity is reported as enactment of the candidate whole. | Preserve the candidate account and name only separately admitted enacted Methods. |
| success-selection bias | Convenient positive occurrences stand in for the intended situation family. | State representative criteria and add a discriminating situation when the later question needs one. |
| instrument bias | Logs, reports, or telemetry are treated as the Work or result. | Keep the occurrence, result, record, and evidence-use relation separate. |
| capability inflation | Training or one success becomes a holder capability claim. | Require the A.2.2 holder, Work family, envelope, measures, window, and evidence. |
| causal inflation | Reported benefit or association becomes Method-caused effect. | State the observation level and missing comparison or causal basis. |
| trial-judgment collapse | One trial record decides coherence, fit, transfer, and worth at once. | Route evidence to ME.12, ME.13, and ME.14 as separate receiving uses. |

### ME.11:7 - Conformance Checklist

- [ ] One later decision and bounded trial question are stated before the trial design.
- [ ] The Method is admitted, or the proposed whole remains a candidate account throughout.
- [ ] Every claimed enacted Method is independently admitted; no candidate whole is said to be enacted.
- [ ] Representative criteria are named, and every discriminating situation states the claim it can distinguish.
- [ ] WorkPlan, demonstration, simulation, report, trace, result, and actual Work remain separate.
- [ ] Each admitted Work occurrence has actual performers, action history, enacted Method, temporal extent, and a containing-System relation.
- [ ] Capability, System use, assignment, permission, authority, support, operation binding, and result relations are asserted only from their own bases.
- [ ] Conditions, deviations, adaptations, burdens, observations, and domain results are recorded per occurrence.
- [ ] Direct observation, self-report, association, contribution, and causality are not merged.
- [ ] The result routes evidence and gaps separately to ME.12, ME.13, and ME.14 and claims none of their judgments.

### ME.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The rehearsal ran, so the Method was trialled.” | Recover actual Work and its enacted admitted Method; otherwise keep the rehearsal at its supported status. |
| “The team enacted the candidate Method.” | Admit the Work, preserve the candidate account, and name only admitted constituent Methods whose enactment relations obtain. |
| “Everyone was trained, so capability was controlled.” | Record training separately and recover the holder capability input actually used in interpretation. |
| “The log proves the task occurred and succeeded.” | Use the log as evidence for independently admitted Work and a separately established task result. |
| “Most reports were favourable, so the Method transfers.” | Send the occurrence evidence and situation differences to ME.13; do not make the transfer judgment here. |
| “Reported benefit proves the Method caused the outcome.” | Record the report and its contribution category, then return the missing causal basis. |

### ME.11:9 - Consequences

Trial Work produces inspectable evidence. Failures and missing premises survive as useful results, and later assurance decisions can compare the same occurrences without changing their identity or truth status.

The cost is more explicit occurrence recovery and narrower conclusions. Projects must record performer, Method, situation, capability, support, direct relations, burdens, and source limits, and they may finish a costly trial with a precise gap instead of a favourable verdict.

### ME.11:10 - Rationale

Actual Work is the shared empirical base, but coherence, fit, transfer, worth, capability, contribution, and causality are different claims. Keeping them separate lets the same occurrence inform several decisions without allowing one decision to inherit another's conclusion.

Representative and discriminating situations are paired because typical-use evidence and boundary-finding evidence answer different questions. Their selection is decision-relative; it does not create statistical representativeness or a universal situation taxonomy.

### ME.11:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | Adopt workplace projects, varied application situations, reported limitations, later report analysis, and separation of direct and indirect contribution as trial-design and evidence-recording cues. | One automotive OEM, SSFD used within a broader methodology, and retrospective reports establish neither SSFD-only causality nor universal transfer. |
| Tsai, Zdravkovic, and Söder, [DBE-design Method action research](https://doi.org/10.1007/s10270-022-01068-z) | Adopt repeated plan-perform-evaluate cycles in an operating health-services ecosystem as an unlike-domain replay of actual validation actions. | The evaluation is ex ante and case-specific; it establishes neither long-term effect nor transfer to the other elicited domains. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Adopt explicit alternative Methods, several industry situations, participant Work, activities, and immediate value reports as a bounded comparison input. | Immediate self-report establishes neither long-term product results, causal superiority, nor the effectiveness of recombined variants. |
| Current FPF `A.3.1`, `A.15.1`, `A.2.2`, and `A.10` | Adopt independent Method admission, Work occurrence admission, capability qualification, and evidence-use relations. | ME.11 contributes the practitioner move for situation selection and occurrence-level trial evidence; it does not redefine those claims or make the downstream judgments. |

Reopen the pattern when practitioners cannot select a discriminating situation without a universal trial taxonomy, when actual Work cannot be distinguished from demonstrations or records, when the candidate branch repeatedly loses status, or when current field evidence supports a stronger trial-selection move without broadening the later judgments.

### ME.11:12 - Relations

- ME.7 supplies an admitted Method or a status-preserved candidate account and may supply a realization or trial plan; it does not supply performed Work.
- ME.8 supplies MethodDescription content or candidate-account content for the trial question. ME.10 supplies supported material and task conditions or a retained configuration set, split boundary, or gap; ME.11 consumes only the obtaining support inputs and preserves every unresolved status. Neither pattern establishes trial Work or its result.
- ME.18 may supply a reconstructed candidate account and a trial question while preserving the candidate branch.
- `A.3.1` governs Method admission; `A.15.2` keeps the WorkPlan separate; `A.15.1` governs each Work occurrence; `A.2.2` governs capability inputs; `A.10` governs relied-on evidence paths.
- ME.12 consumes evidence for construction and description coherence, ME.13 consumes situation comparisons for fit or transfer, and ME.14 consumes results, burdens, alternatives, and evidence strength for practical worth. None of those conclusions is returned by ME.11.

### ME.11:End

## ME.12 - Verify Method and MethodDescription Coherence

>
> **Primary working result:** a verified bounded claim, one correction returned to the maintained result that owns the contradicted claim, or a named gap. Construction, MethodDescription, representation, support, and trial-evidence claims remain separately governed; coherence establishes neither situational fit nor practical worth.

### ME.12:0 - Use This When

Use this pattern when Method construction commitments, a MethodDescription, a selected representation, an enactment-support result, or trial evidence no longer agree well enough for a named use. Begin with the possible contradiction and the decision it blocks: which maintained claim may be wrong, incomplete, stale, or unsupported?

The first useful result is a coherence-finding row. It names the claim being checked, its maintained owner and edition, the comparison basis, the observed agreement or defect, the one result to reconsider, and the stop. A truthful `owner-not-recoverable` or `missing-comparison-basis` result is better than declaring the whole Method incoherent.

Here *coherence* is Plain practice wording for checking whether claims relied on for the declared use agree where they should. It is not a new FPF relation, Method admission, fit result, effectiveness result, or universal consistency proof.

Do not use this pattern to decide whether the Method fits another situation, transfers, is worth keeping, caused a result, or is preferable to alternatives. ME.13 owns fit and transfer; ME.14 owns practical worth. A favourable trial can supply evidence for ME.12 without making its conclusion.

### ME.12:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| construction commitment | A maintained ME.7 requirement, component decision, operation declaration, or obtaining-relation claim about the Method under construction. | It is not a sentence in a later description merely because the sentence refers to it. |
| MethodDescription claim | A claim in one ME.8 edition for a named use, including coverage, omission, correspondence, evidence limit, or stop. | Description agreement does not admit a Method or establish that Work occurred. |
| Method representation profile | An ME.9 result for several unlike Method-related actions. It contains one complete C.37-bearing row per action and a separate cross-use result naming the shared Method source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and changes that reopen several rows. | It does not select a representation for an arbitrary entity, make row colocation a composition result, or establish view, mathematical-lens, publication, or structure conformance by itself. |
| support claim | One ME.10 task, configuration, A.22 proposal or selection position, collection, membership, edition, publication, direct-relation, test, or reliance claim. | A repository or successful tool task cannot repair a contradiction in another maintained result by being convenient. |
| trial evidence | ME.11 occurrence-level observations and gaps qualified for a named later use. | An observation can bear on a claim. Any correction belongs in the maintained result that owns that claim. |
| coherence finding | A bounded agreement, contradiction, missing-information, failed-declared-conformance, or currentness result about one named claim. | “The Method is coherent” is too broad unless every claim relied on and its qualification window are actually in scope. |
| maintained owner | The result whose claim must change if the finding is sustained: ME.7, ME.8, ME.9, one exact ME.10 result, or another named governor. | The file that displays a claim is not necessarily its owner. |
| declared conformance | A conformance claim with its named scheme, criteria, represented entity, use, and qualification window. | Passing description-side conformance does not establish Method fit, Work performance, or worth. |

### ME.12:1 - Problem Frame

A Method can be internally plausible while its description omits a required stop, a representation hides a relation needed by its use, or a support route serves an obsolete edition. Trial Work can expose the mismatch, but the mismatch still has to be located. Otherwise every defect is blamed on “the Method”, or every observed failure is pushed into the document that happens to be easiest to edit.

The practical question is narrower: which claim was relied on, what should it agree with, what evidence bears on that agreement, and which maintained result owns the smallest correction?

### ME.12:2 - Problem

Coherence checks often collapse several questions. Construction conformance is treated as document completeness; description consistency is treated as practical fit; a failed representation is repaired by changing Method semantics; a stale support edition is called a Method defect; or one trial success is taken to verify the whole package.

This makes correction expensive and unsafe. Several maintained results are changed together, the original contradiction becomes unrecoverable, unaffected claims lose their evidence status, and later fit or worth decisions inherit a verdict that ME.12 never established.

### ME.12:3 - Forces

| Force | Tension |
| --- | --- |
| Local correction | A small owner-specific repair preserves working claims, while a package-wide rewrite feels safer. |
| Construction and description | They must correspond for relied-on uses, while they remain different results with different tests. |
| Representation | A representation must expose what its use needs, while omission can be deliberate for another use. |
| Trial evidence | Actual Work can reveal contradictions, while failure can also come from situation, capability, support, or another direct relation. |
| Conformance | Named schemes can make checks repeatable, while scheme passage can be mistaken for practical adequacy. |
| Currentness | Editions and sources change, while a once-valid claim may remain syntactically consistent and practically stale. |
| Candidate status | Candidate accounts benefit from correction, while coherence must not launder them into admitted Methods. |

### ME.12:4 - Solution

Check one claim relied on for the named use against its declared basis, classify the result, and return any correction only to the maintained result that owns the defeated claim. Recheck the repaired claim while preserving every unaffected status and open question.

#### ME.12:4.1 - Pattern-Use Unfolding

1. **Name the blocked use and possible contradiction.** Identify the reader or decision, the claim needed, its qualification window, and what would count as agreement, contradiction, missing information, or a stop. Do not begin with “verify the Method”.
2. **Preserve the subject and status branch.** Identify the admitted Method under `A.3.1`, or keep the proposed whole as a candidate account. Keep Work, WorkPlan, description, representation, support, evidence, publication, and structure claims at their current statuses.
3. **Recover the maintained claim and owner.** Record the claim text or predicate, owning result, edition or occurrence, source or construction basis, intended use, and currentness condition. If ownership cannot be recovered, return `owner-not-recoverable` before editing several carriers.
4. **Check construction claims at ME.7.** Test construction requirements, component decisions, operation declarations, and obtaining-relation claims separately. Cite the governing FPF predicate where needed rather than recreating its admission test. A failed construction claim returns to that exact ME.7 result.
5. **Check MethodDescription claims at ME.8.** Test coverage, internal consistency, correspondence with admitted Method claims, navigation for the named use, stated evidence limits, omissions, stops, and any declared description-side conformance. Do not make section count or scheme passage a proxy for useful coverage.
6. **Check representation-use results at the right owner.** For one action, recover its complete C.37-bearing use result and stop without ME.9. For several unlike Method-related actions, recover the complete ME.9 profile: shared Method source, one complete action row each, cross-use correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. Test the contradicted action row and whether the profile relation still holds. The direct FPF governor owns view, mathematical-lens, publication, and structure conformance; if a governed result fails, return that lower result and reopen only the affected use row and cross-use relations that actually depended on it.
7. **Check support results at ME.10.** Locate the exact task row, evidence status, configuration result, support-purpose claim, proposed or selected A.22 position, constituent, relation, constraint, use frame, collection rule, participant meaning, membership predicate and episode, grant, exercise, Work basis, operation declaration and application, result binding, account, edition, publication occurrence, direct relation, reliance episteme, or named-user test. Return a repair only to the defeated position.
8. **Use trial evidence to check the maintained claim.** From ME.11, recover the actual Work occurrence, performer, enacted admitted Method, situation, capability and support conditions, direct relations, result, burden, observation source, and evidence reach. Ask which named claim the observation bears on. A success or failure does not by itself identify the owner.
9. **Classify the finding.** Distinguish: `agreement-within-window`; `contradicted-claim`; `missing-information`; `failed-declared-conformance`; `stale-source-or-edition`; and `owner-not-recoverable`. Do not turn uncertainty into contradiction or a local defect into a whole-Method verdict.
10. **Select one correction owner.** Return the smallest correction to ME.7 construction, ME.8 description, one direct C.37 use row, one complete ME.9 Method representation profile, one exact ME.10 result, or the direct governor of a lower representation result. If one observation defeats several independent claims, create separate findings with separate owners; do not copy one vague correction into every upstream result.
11. **Repair and repeat the same check.** Preserve unaffected claims, statuses, evidence, and windows. Recheck the repaired claim against the same basis. If the use, subject, source, edition, or criteria changed, start a new coherence use instead of calling the old check passed.
12. **Return the bounded result and non-use.** State the verified claim, correction or gap, owner, affected downstream uses, preserved claims, and reopen condition. Say explicitly that fit, transfer, worth, capability, contribution, causality, admission, and publication remain separate.

#### ME.12:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| coherence use | Blocked decision, reader, relied-on claim, qualification window, agreement and stop conditions. |
| subject status | Admitted Method or candidate account, plus separately identified Work, WorkPlan, description, representation, support, and evidence results in scope. |
| maintained claim | Claim or predicate, owner, edition or occurrence, source or construction basis, intended use, and currentness. |
| comparison basis | Construction requirement, description claim, selected representation rule, support premise, trial evidence, or declared conformance criterion actually used. |
| finding | Agreement, contradiction, missing information, failed declared conformance, stale source or edition, or missing owner; include the evidence reach. |
| repair routing | One maintained result to reconsider, smallest correction, unaffected claims and statuses, and downstream uses that must be rechecked. |
| rerun | Same-check result after repair, or the changed use or basis that requires a new check. |
| return | Verified bounded claim, corrected claim, or named gap; non-use and reopen condition. |

#### ME.12:4.3 - What Changes in Practice

Teams stop repairing the nearest document or declaring the whole Method inconsistent. They can identify the defeated claim, distinguish construction from description, representation, support, and evidence, and send one correction to its maintained owner.

The correction becomes cheaper to review and safer to reuse. Unaffected claims keep their status, and later fit and worth judgments receive a precise repaired input rather than a package-wide confidence label.

#### ME.12:4.4 - Minimal Constructed Coherence Replay

Continue the constructed ME.11 trial of admitted `M-Unit-Review-1`. Construction result `CCR-UR-1` states that unit identification and normalization precede tolerance comparison. MethodDescription edition 4 says the same and exposes the unresolved-mismatch stop.

Only one current action is at issue: `Reviewer-17` must use the flow representation to guide pre-release unit review. Direct use result `C37-UR-Flow-4` therefore takes the C.37 exit rather than opening ME.9. It returns to that Method and description edition, requires unit identification, normalization before tolerance comparison, the comparison branch, and the unresolved-mismatch stop, and uses governed representation result `REP-UR-Flow-4`.

Exact claim: that representation exposes those operations in order for the named review action. A.2.4 classifies the intended preparation use; A.10 path `P-UR-Flow-4` carries the current-edition premise with `RelianceDisposition=pass` for the review window. Receiving task criterion `UR-PreRelease-Guide-4` permits use only while those claims remain exposed. The row omits unrelated support-edition detail, preserves Method, description, representation, and Work status, is `select` for that action, and returns a missing exposure to the direct representation governor and this use row.

ME.10 supplies the current conversion table used in `W-Disc-1`.

The trial evidence records that `Reviewer-17` normalized the Celsius/Kelvin values before comparison and stopped the release decision. Inspection of `REP-UR-Flow-4`, however, shows identification followed directly by tolerance comparison; the normalization operation is absent. The finding is not “the Method is incoherent”. The construction claim, description claim, support edition, and observed Work agree within this slice. The contradicted claim is the `C37-UR-Flow-4` exposure claim for its exact action; no ME.9 profile exists or is needed for this one-use case.

Return `CORR-C37-UR-1`: revise governed representation result `REP-UR-Flow-4` and its direct use row to expose normalization and the unresolved-mismatch branch, or narrow the row's action, required claim, and omission account. Preserve `M-Unit-Review-1`, MethodDescription edition 4, `W-Disc-1`, its task result, and the conversion-table support result. Recheck the same exposure claim after repair. Do not infer fit or worth from the successful Work occurrence.

| If the observed defect were instead... | Owner to reconsider | Result not to change automatically |
| --- | --- | --- |
| The admitted construction omitted any normalization requirement while the named problem required one. | The exact ME.7 construction or requirement result. | ME.8 and every affected direct C.37 use row or complete ME.9 profile until their own action claims and dependent cross-use relations are checked against the changed construction. |
| MethodDescription edition 4 reversed the declared operation order while construction and Work supported the original order. | The exact ME.8 description claim and edition. | Method identity and the Work occurrence. |
| The retrieved conversion table used a stale scale while construction, description, and representation were correct. | The exact ME.10 edition, retrieval, or named-user task result. | ME.7 construction and every unaffected direct C.37 use row or complete ME.9 profile. |
| The source cannot show which of those positions is wrong. | `owner-not-recoverable` with the missing comparison basis. | All maintained results until evidence distinguishes them. |

### ME.12:5 - Archetypal Grounding - Representation Difficulty in SSFD

The SSFD workplace evidence reports that Project 32 had difficulty representing the relation between a closed-loop sensor and controller. This is a useful coherence trigger because the difficulty may concern Method semantics, a MethodDescription claim, a selected representation, support material, or a situation-specific applicability boundary.

The report does not by itself identify which maintained result owns the defect. First recover the exact receiving action, Method source, direct governed result and claim, applicable evidence/reliance layer, receiving result, exposure and omission, disposition, and return.

If the evidence concerns only one sensor-controller representation, ME.9 is not invoked: inspect C.37 and the direct FPF representation governor. If several unlike Method-related actions are current, require a complete ME.9 profile with one complete action row each and an explicit cross-use result for shared source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return.

If the facts locate a failed exposure claim, return the owning row and only the cross-use relations that depended on it; if they locate a construction or description contradiction, return it to ME.7 or ME.8. If the report cannot distinguish the owner, return `owner-not-recoverable` rather than calling SSFD incoherent.

Project 11 records a different application and many reported results. It is neither the counterfactual for Project 32 nor proof that the same representation claim was coherent there. The 41-report set and its 95 reported benefit instances concern later evidence use; they do not erase the Project 32 difficulty or establish practical worth inside ME.12.

#### ME.12:5.1 - APP-ME-01 Early Stop

`C-EC-Release-v2` remains a candidate account and the three-release statement remains a WorkPlan. ME.12 may check current description, representation, ME.10 task, collection, edition, reliance, permission, application, Work, result-binding, and proposed-organization claims against their own bases. It must not verify planned releases as performed Work or call the candidate whole coherent as a Method.

For every correction, name the exact maintained position. A stale method-base edition returns to that edition result. A failed viewpoint rule returns the lower episteme and failed `E.17.0` rule to their direct governor. Recheck its complete C.37-bearing action row when that use relied on it; when the row belongs to an ME.9 profile, recheck only the cross-use correspondences, omissions, edition relations, keep-separate decisions, and multi-row returns that depended on the failed result. A missing A.22 selection-use basis remains the already named gap. Do not turn three successful support tasks into release evidence.

### ME.12:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| package-coherence bias | One local contradiction becomes a verdict on the whole Method package. | Bound the claim, use, owner, and window before checking. |
| document-owner bias | The document displaying a claim is edited even when construction or support owns it. | Recover the maintained result and direct governor. |
| success-verifies-all bias | One favourable Work occurrence verifies construction, description, representation, and support together. | Ask which named claim the observation actually bears on. |
| conformance-as-performance bias | Description-side conformance becomes fit or effectiveness. | Keep scheme passage inside the declared description use. |
| repair-fanout bias | The same correction is copied into every upstream carrier. | Route each contradicted claim to one owner; create separate findings only for separate claims. |
| source-authority bias | A published report is treated as direct admission and owner identification. | Preserve the evidence path and return missing occurrence or owner facts. |

### ME.12:7 - Conformance Checklist

- [ ] The blocked use and one claim relied on for that use are named.
- [ ] The Method is admitted or the proposed whole remains a candidate account.
- [ ] Construction, MethodDescription, representation, support, Work, and evidence results retain separate identities and statuses.
- [ ] The claim owner, edition or occurrence, intended use, source, and currentness window are recoverable.
- [ ] Trial evidence is qualified, and the claim's maintained owner remains explicit.
- [ ] Agreement, contradiction, missing information, failed declared conformance, staleness, and missing owner are not merged.
- [ ] Every correction returns to one maintained result and preserves unaffected claims.
- [ ] A repaired claim is rechecked against the same basis, or a changed basis starts a new use.
- [ ] No coherence result is overread as fit, transfer, worth, contribution, causality, capability, admission, or publication.

### ME.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The trial failed, so rewrite the Method.” | Locate the contradicted claim and rule out situation, capability, support, and relation gaps first. |
| “The standard checklist passed, so the Method is coherent.” | State the declared conformance use and every claim outside its scope. |
| “Fix the diagram and the description together.” | Determine whether one or two independent claims are contradicted and route each separately. |
| “Project 32 proves SSFD is inconsistent.” | Treat the reported representation difficulty as evidence that opens an owner-specific check. |
| “No contradiction was observed, so coherence is proven.” | Return agreement only for the claims, evidence, and window actually checked. |

### ME.12:9 - Consequences

Coherence work becomes a repair-routing practice rather than a package-wide verdict. A practitioner can see which claim failed, why it failed, what remains valid, and which downstream decisions need the repaired result.

The cost is explicit ownership and comparison recovery. Some checks end with a missing owner or missing basis, and a team may have to preserve several plausible defect locations instead of choosing the easiest file to edit.

### ME.12:10 - Rationale

Method construction, description, representation, support, and trial evidence are coupled by use but are not interchangeable. Their claims can agree, disagree, or become stale independently. Returning each correction to one maintained owner protects that independence and keeps coherence separate from Method admission and effectiveness assessment.

The same evidence may support several checks, but its use relation is different in each. Treating evidence as a common source rather than a common verdict lets later fit and worth decisions reuse it without inheriting ME.12's scope.

### ME.12:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Ralyté, Koutsopoulos, and Stirna, [verification, validation, and evaluation of modeling methods](https://doi.org/10.1007/s10270-025-01304-2) | Keep verification, validation, and evaluation questions separate and use evidence to locate the claim under check. | The source is modeling-Method focused and does not supply one universal FPF owner map or prove practical worth. |
| [ISO/IEC/IEEE 24774:2021](https://www.iso.org/standard/78981.html) | Use description elements, rules, views, and declared description-side conformance as selectable comparison bases. | The standard does not make description conformance a Method admission, fit, or performance result and is not imported as FPF ontology. |
| Cash, Daalhuizen, and Hekkert, [method efficacy and effectiveness](https://doi.org/10.1016/j.destud.2023.101204) | Preserve the difference between internal or use-side adequacy questions and practical effect questions. | The contribution does not supply a universal coherence score or make one successful occurrence decisive. |
| Current FPF `A.3.1`, `A.10`, `C.2.1`, `E.17.0`, `A.22`, and the direct governors cited by the maintained claim | Reuse Method admission, claim-bound evidence, episteme and edition identity, view conformance, structure selection, and direct predicate tests. | ME.12 contributes owner-specific comparison and correction routing; it does not redefine those identities or predicates. |

Reopen the pattern when practitioners cannot identify one maintained owner without changing the architecture, when repeated findings require a distinct independent coherence problem, when a source supplies a stronger owner-discrimination method, or when a governing FPF predicate changes the repair route.

### ME.12:12 - Relations

- ME.7 supplies construction commitments and obtaining-relation results; ME.8 supplies MethodDescription claims and use coverage; C.37 supplies one-action representation-use results; ME.9 supplies complete Method representation profiles for several unlike Method-related actions, with their action rows and separate cross-use result; ME.10 supplies task, support, collection, edition, publication, relation, test, and reliance results. Each remains the owner of its own claim, while a lower representation result remains with its direct FPF governor.
- ME.11 supplies occurrence-level observations and gaps. It neither identifies the correction owner automatically nor establishes coherence.
- ME.13 consumes coherent-enough claims and situation evidence for fit or transfer. ME.14 consumes results and evidence limits for practical worth. Neither conclusion is returned by ME.12.
- `A.3.1` governs Method admission; `A.10` governs claim-bound evidence use; `C.2.1` governs episteme and edition identity; `E.17.0` governs view conformance; `A.22` governs selected structures. Cite the direct governor for every other predicate checked.
- ME.15 receives a variant question only when a proposed repair changes reusable Method semantics; a document, representation, support, or local Work correction alone does not identify a Method variant.

### ME.12:End

## ME.13 - Validate Situational Fit and Transfer

>
> **Primary working result:** a bounded fit, failure, applicability, transfer, or missing-evidence result for an admitted Method; or bounded situation evidence about a candidate proposal whose status remains unchanged. A change in reusable Method semantics returns a variant question instead of being hidden inside a transfer claim.

### ME.13:0 - Use This When

Use this pattern when actual Work has supplied evidence in one or more situations and a practitioner must decide whether an admitted Method fits a named receiving situation, where its applicability stops, or whether a supported claim transfers from a source situation family. Begin with the source and receiving situations and the claim whose truth could change between them.

The first useful result is a situation-comparison row. It names the Method or candidate status, source and receiving situation families, actual Work used as evidence, matched and changed conditions, holder capabilities, Systems and direct relations, adaptations, domain results, semantic changes, evidence reach, and the bounded result or missing premise.

Here *fit* and *transfer* are Plain practice names for two different decisions. Fit concerns a Method and a bounded situation or situation family. Transfer concerns whether a supported claim survives a stated move from source to receiving conditions. Neither word creates a universal FPF predicate or statistical generalization.

Do not use this pattern to infer practical worth, causal contribution, general effectiveness, capability, or cultural adoption. A Method can fit and still be a poor choice against current alternatives. ME.14 owns that comparison. An account is never enacted, and a candidate whole remains a candidate even when separately admitted Work succeeds.

### ME.13:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| source situation family | The bounded set of source conditions under which the relied-on Method claim has evidence. | A project label or industry name is insufficient; state the decision-relevant conditions. |
| receiving situation family | The bounded set of conditions in which the practitioner wants to rely on the claim. | It is not “everywhere else” or a population inferred from one case. |
| representative source slice | Actual source Work selected because its stated characteristics bear on the current claim. | Convenience or success alone does not make it representative. |
| discriminating unlike situation | A receiving or held-out situation whose changed condition can expose a limit in the claim. | Difference is useful only when the claim it can defeat is stated. |
| matched condition | A condition held comparable enough for the declared decision, with its evidence basis. | Unrecorded sameness is not a control and does not establish causality. |
| adaptation | A change made in performing or supporting Work for the receiving situation. | If reusable Method semantics change, the result opens an ME.15 variant question; it is not evidence for unchanged transfer. |
| situational fit | A bounded result that the admitted Method is usable for the named situation and decision under stated conditions and limits. | Fit establishes neither superiority, worth, causal contribution, nor general effectiveness. |
| transfer result | A bounded result about whether a source-supported claim survives the named change in conditions. | One receiving occurrence rarely supports a broad situation family; return the narrower result or missing evidence. |

### ME.13:1 - Problem Frame

Methods are often moved by name: a team says that a Method worked in one project, industry, or organization and applies it to another. The label hides the conditions that mattered—project purpose, development phase, technical problem, performer capability, support Systems, direct relations, adaptations, and the domain result being judged.

The opposite error is equally common. Any adaptation or local failure is treated as evidence that the Method cannot transfer, even when the changed condition, support defect, or altered Method semantics has not been identified. A useful validation result must show what stayed the same, what changed, what actual Work occurred, and what claim survives.

### ME.13:2 - Problem

A favourable source case can be generalized without a discriminating receiving situation. A candidate account can be called enacted. Training or expert help can be hidden inside “same conditions”. A changed representation or operation can be called tailoring even though reusable Method semantics changed. Immediate self-report can become lasting transfer, and fit can become worth.

These shortcuts produce confident but unreplayable applicability claims. Practitioners cannot tell which condition matters, whether the same Method was used, whether the evidence came from actual Work, or what result should be revised after a failure.

### ME.13:3 - Forces

| Force | Tension |
| --- | --- |
| Local usefulness | A narrow fit result can guide current Work, while sponsors often ask for broad transfer. |
| Unlike situations | Difference can reveal a boundary, while too many simultaneous changes defeat interpretation. |
| Method identity | Adaptation may be necessary, while semantic change can create a different variant. |
| Natural Work | Workplace evidence has practical relevance, while conditions and contribution are less controlled. |
| Capability and support | They can determine outcomes, while their presence is easily attributed to the Method. |
| Positive and negative evidence | Success and failure both matter, while selective reporting favours one direction. |
| Decision speed | Teams need a bounded answer, while missing Work or comparability must remain a reason to stop. |

### ME.13:4 - Solution

Compare actual source and receiving Work through a decision-relative situation account, include one condition capable of defeating the claim, preserve Method semantics and status, and return only the fit or transfer result supported by that comparison.

#### ME.13:4.1 - Pattern-Use Unfolding

1. **Name the decision, subject, and status.** State whether the question concerns fit in one receiving situation, an applicability boundary, or transfer of one supported claim. Identify the `A.3.1`-admitted Method, or preserve the candidate account and name only separately admitted constituent Methods whose enactment is claimed.
2. **Bound the source and receiving situation families.** Record project purpose, development phase, technical or domain problem characteristics, performer population, holder capabilities, participating Systems, Agent-performed Work, direct relations, constraints, support conditions, qualification window, and the domain result relevant to the claim.
3. **Recover source Work and evidence.** Use ME.11 evidence only for actual Work whose performers, enacted admitted Method, temporal extent, containing System, conditions, deviations, burdens, adaptations, results, and evidence path are recoverable. A report can support the account but does not admit Work by citation.
4. **Select a receiving or held-out situation that can discriminate.** Select or seek one named condition change capable of defeating the claim: technical coupling, project phase, domain, performer or capability envelope, support relation, organizational condition, information availability, authority boundary, or another named condition. State why it matters. If minimality matters, name the alternatives, ordering criterion, and basis for treating one change as smaller or weaker; otherwise record concurrent changes and unknowns without ranking them.
5. **Separate matched, changed, and unknown conditions.** Do not call conditions controlled unless the basis supports it. Record concurrent changes and missing facts; use `missing-comparability-basis` when the comparison cannot distinguish the claimed boundary.
6. **Recover receiving Work independently.** Admit the receiving Work occurrence and every claimed enacted Method under their direct governors. Preserve WorkPlan, simulation, demonstration, report, training, and support tasks as separate results. If receiving Work did not occur, return `missing-performed-work` rather than a transfer claim.
7. **Track adaptations and Method semantics.** Record changes to operations, dependencies, roles, stops, representations, support, and local Work. Ask whether reusable Method semantics stayed within the admitted Method. If they changed, return `variant-question[...]` to ME.15 and evaluate the unchanged and changed branches separately.
8. **Compare domain results and evidence reach.** Compare the result relevant to the fit claim together with burdens, deviations, failures, and limitations needed to interpret it. Distinguish direct observation, report, association, contribution, and causality. Do not use immediate self-report as long-term transfer without the missing time evidence.
9. **Classify the bounded result.** Return `fit-within[...]`, `failure-within[...]`, `applicable-if[...]`, `transfer-supported-between[...]`, `transfer-not-supported`, `missing-performed-work`, `missing-comparability-basis`, or the named missing premise. Plain labels may be used, but the situation, claim, evidence, and window must remain inspectable.
10. **Route a defeated claim by result kind.** Return a failure directly only to the ME.3 situational requirement, ME.6 architecture decision, ME.7 construction result or admitted Method claim, or ME.15 applicability or variant entry that the evidence contradicts. When the evidence may contradict an ME.8 description, ME.9 Method representation profile row, or ME.10 support claim, return the bounded observation to ME.12; ME.12 identifies and rechecks the maintained correction owner, including the direct governor of any lower representation result. Do not reopen every carrier.
11. **State non-transfer and reopen conditions.** Name the populations, domains, capability envelopes, support arrangements, times, alternatives, and causal claims not covered. Reopen when one condition crosses the declared boundary, Method semantics change, evidence currentness expires, or a new unlike situation defeats the claim.

#### ME.13:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| validation use | Fit, applicability, or transfer question; receiver; decision; claim; qualification window; stop. |
| subject status | Admitted Method, or candidate account plus separately admitted enacted constituent Methods. |
| source situation | Situation-family conditions, actual Work, performers, capability inputs, Systems, Agent-performed Work, direct relations, adaptations, domain results, burdens, and evidence reach. |
| receiving situation | The same positions for actual receiving or held-out Work, including missing facts. |
| discrimination | Condition selected to challenge the claim, why it matters, matched conditions, changed conditions, and unknowns. |
| semantic continuity | Preserved Method semantics, local Work or support changes, and any reusable semantic change returned as a variant question. |
| comparison | Result differences, burdens and deviations needed for interpretation, evidence strength, and unsupported contribution or causal claims. |
| return | Bounded fit, failure, applicability, transfer, or missing-evidence result; direct ME.3, ME.6, ME.7, or ME.15 return, or a bounded ME.12 observation for a possible ME.8 description, ME.9 Method representation profile-row, or ME.10 support contradiction; non-transfer and reopen conditions; unaffected results preserved. |

#### ME.13:4.3 - What Changes in Practice

Teams stop transferring a Method by title or rejecting it after an unexplained local failure. They can show the source conditions, receiving conditions, actual Work, semantic continuity, one discriminating change, and the exact claim that survived or failed.

A narrow result such as “Fits this decision for this holder and support window; transfer untested” can support a decision to use the Method now while protecting later teams from a universal claim.

#### ME.13:4.4 - Minimal Constructed Fit Replay

Continue the constructed ME.11 evidence for admitted `M-Unit-Review-1`. The immediate decision is whether the Method fits pre-release review of temperature-sensor reports for `Reviewer-17` through day D30 when mixed Celsius/Kelvin inputs may occur. It is not yet a decision about another reviewer, product family, tool, or organization.

`W-Rep-1` and `W-Disc-1` are actual Work in `Calibration-Team-A`. The same reviewer, capability input `CAP-R17-1` with qualification record `QR-R17-1`, MethodDescription edition 4, manually retrieved conversion table, release boundary, and containing System are recorded. The discriminating change is the Celsius/Kelvin mismatch in `S-Disc-1`; it can defeat the claim that the Method exposes a unit mismatch before the release decision. In `W-Disc-1`, the reviewer normalizes values, detects the mismatch, stops release, and returns the report. ME.12 has separately corrected direct use result `C37-UR-Flow-4` and its governed representation result `REP-UR-Flow-4`, which had omitted normalization for that named use.

Return `fit-within[Reviewer-17, temperature-sensor reports, edition 4, manual conversion table, through D30]` for the named release-review decision. Also return `transfer-not-tested` for other holders, product families, support routes, qualification windows, or organizations. The two occurrences do not establish causal superiority or practical worth.

If the reviewer had changed the reusable operation from unit normalization to an approximation rule absent from `M-Unit-Review-1`, preserve the observed Work but return `variant-question[approximation-rule]` to ME.15. Do not call the changed branch successful transfer of the unchanged Method.

### ME.13:5 - Archetypal Grounding - SSFD Situation Boundaries

The SSFD workplace evidence supplies varied actual-project reports and a decision-relevant unlike-situation probe. Project 11 concerns functional analysis of a new by-wire steering system and reports 48 failure modes, 44 requirements and design rules, 44 individual-system test cases, and 33 overall-system requirements and test cases. Project 32 reports difficulty representing the relation between a closed-loop sensor and controller.

Use Project 11 as a source situation only after the SSFD Method or candidate status, relevant Work evidence, performer and capability facts, support conditions, and relied-on claim are recovered. Use Project 32 as a discriminating unlike situation because the closed-loop relation can challenge a representation or applicability claim. Do not infer that Project 11 caused or preceded Project 32, that the same performers and capabilities were present, or that a difficulty establishes whole-Method failure.

A defensible result may be narrow: Project 11 supplies bounded evidence for one functional-analysis situation; Project 32 defeats or leaves unsupported a broader representation claim until the owner-specific ME.12 correction and receiving Work basis are recovered. The 41-report set broadens the evidence pool but does not establish transfer across every project stratum or causal contribution by SSFD alone.

#### ME.13:5.1 - Unlike-Domain and Current-Alternative Probes

The Digital Vaccine action-research case supplies performed validation actions in an operating health-services ecosystem and three plan-perform-evaluate cycles. Use it to replay the ME.13 architecture in another domain, not to claim that SSFD transfers to health services. Its evaluation is ex ante and case-specific.

The sustainable-design workshops supply bounded applications of The Natural Step, Whole System Mapping, and Biomimicry across consumer electronics, furniture, and clothing. They can expose industry and activity differences, but immediate participant self-reports do not establish long-term transfer. The Halogen case shows that practitioner skill, project demands, and organization can accompany cyclic Method adaptation; if reusable semantics changed, route the result to ME.15 instead of expanding one fit claim.

#### ME.13:5.2 - APP-ME-01 Early Stop

`C-EC-Release-v2` remains a candidate account. The three support-use Work occurrences from ME.10 do not perform a release and cannot support release fit or transfer. Before any such result, recover one actual release Work occurrence, its performers, separately admitted enacted constituent Methods, capability inputs, Systems, Agent-performed Work, direct relations, support conditions, domain result, burdens, deviations, authority facts, and a performed held-out release situation.

Until then return `missing-performed-work` and `missing-held-out-situation`. Preserve the candidate branch and the unsupported `CUR-EC417-CadenceEffect-1`; no cadence or transfer claim becomes supported by planning three releases.

### ME.13:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| label-transfer bias | The same Method name is treated as evidence of the same Method and conditions. | Recover Method status, semantics, actual Work, and situation positions. |
| success-generalization bias | One favourable occurrence becomes a situation-family claim. | Return the narrow fit result and name transfer evidence still missing. |
| uncontrolled-sameness bias | Unrecorded capability, support, and organizational conditions are called matched. | Separate matched, changed, and unknown positions with their bases. |
| adaptation laundering | Changed reusable semantics are called local tailoring. | Return an ME.15 variant question and preserve both branches. |
| failure-totalization bias | One difficulty becomes whole-Method failure. | Identify the claim, situation boundary, and repair owner actually defeated. |
| fit-as-worth bias | Usability in one situation becomes a keep or adoption decision. | Send results, burdens, alternatives, and evidence limits to ME.14. |
| account-enactment bias | A candidate account is said to be enacted in receiving Work. | Admit Work and enacted constituent Methods separately; preserve candidate status. |

### ME.13:7 - Conformance Checklist

- [ ] The decision is explicitly fit, applicability, or transfer for one claim.
- [ ] The Method is admitted or the proposed whole remains a candidate account.
- [ ] Source and receiving situation families name decision-relevant conditions rather than labels alone.
- [ ] Actual source and receiving Work, performers, enacted admitted Methods, capability inputs, Systems, direct relations, results, and evidence paths are recoverable or returned as gaps.
- [ ] One changed condition is selected because it can expose a limit in the claim.
- [ ] Matched, changed, and unknown conditions are separate.
- [ ] Adaptations are recorded, and reusable semantic change opens a variant question.
- [ ] Direct observation, self-report, association, contribution, and causality are not merged.
- [ ] The result is bounded by holder, situation, support, time, and evidence.
- [ ] Fit is not overread as practical worth, general effectiveness, capability, or cultural adoption.

### ME.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “It worked in automotive, so it transfers to health services.” | Replay the comparison architecture in the unlike domain; do not join Method, population, or history. |
| “Project 32 proves the Method failed.” | Identify the representation or applicability claim and the missing receiving evidence first. |
| “We tailored it, therefore it transferred.” | Check whether reusable semantics changed; if so, return a variant question. |
| “The workshop participants liked it, so transfer is established.” | Preserve immediate self-report and return missing long-term Work and result evidence. |
| “The candidate was enacted successfully.” | Admit the Work and enacted constituent Methods, not the candidate account. |

### ME.13:9 - Consequences

Fit and transfer claims become inspectable and narrow enough to guide real decisions. Practitioners can see which conditions matter, what actual Work supports the result, whether the same Method persisted, and where another situation must reopen the claim.

The cost is that many plausible transfers end as missing evidence or a smaller applicability envelope. Adaptation may also create a variant-maintenance obligation.

### ME.13:10 - Rationale

Transfer is not a property carried by a Method name. It is a claim about preserved reliance across a stated change in conditions, supported by actual Work and bounded evidence. A discriminating unlike situation is valuable because it can defeat the claim; it need not resemble a statistically representative sample.

Separating semantic continuity from local Work and support changes protects Method identity. It also lets a failure improve the applicability account without forcing rejection of the Method in situations for which evidence remains valid.

### ME.13:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | Adopt workplace-project strata, reported applications and limitations, later report analysis, and the Project 11 to Project 32 unlike-situation probe. | One automotive OEM, retrospective reports, and SSFD use within a broader methodology establish neither SSFD-only causality nor general transfer. |
| Schønheyder and Nordby, [design-Method use and evolution in professional practice](https://doi.org/10.1016/j.destud.2018.04.001) | Adopt project demands, practitioner skill sets, organization, and cyclic adaptation as conditions that can change a fit or variant decision. | One multidisciplinary design firm supplies no universal situation taxonomy, causal result, or admitted variant family. |
| Tsai, Zdravkovic, and Söder, [DBE-design Method action research](https://doi.org/10.1007/s10270-022-01068-z) | Adopt repeated plan-perform-evaluate cycles in an operating health-services ecosystem as an unlike-domain replay of the comparison method. | The evaluation is ex ante and case-specific; it does not prove long-term effect or transfer to the other elicited domains. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Adopt several Methods, industries, activities, and immediate participant reports as bounded situation-comparison inputs. | Immediate self-report establishes neither long-term product results nor causal superiority or transfer of recombined variants. |
| Current FPF `A.3.1`, `A.15.1`, `A.2.2`, and `A.10` | Reuse Method admission, actual Work admission, holder-dependent capability, and claim-bound evidence. | ME.13 contributes the source-to-receiving situation comparison and semantic-continuity return; it does not redefine those governors. |

Reopen the pattern when a stronger field method changes which situation dimensions test the limits of the claim, when practitioners cannot separate semantic adaptation from local Work, when transfer decisions repeatedly require another independent result, or when governing FPF identities change the comparison.

### ME.13:12 - Relations

- ME.11 supplies occurrence-level source and receiving evidence and explicit gaps. It does not make the fit or transfer conclusion.
- ME.12 consumes any bounded observation that may contradict an ME.8 description, ME.9 Method representation profile row, ME.10 support claim, or directly governed lower representation result; it identifies and rechecks the maintained correction owner. Passing coherence does not establish fit.
- ME.14 consumes fit, failure, applicability, burdens, alternatives, and evidence limits for a separate practical-worth decision.
- ME.15 owns reusable Method variants, provenance, applicability entries, and retirement. A semantic change returns there; a local Work, support, description, or representation change alone need not create a variant.
- `A.3.1` governs Method admission, `A.15.1` each Work occurrence, `A.2.2` capability inputs, and `A.10` claim-bound evidence. Cite the direct governor for every System, Agent-performed Work, relation, permission, authority, or result claim relied on.
- ME.16 may later consume a bounded fit or transfer result when introducing a Method in practice; it does not inherit a causal or worth conclusion.

### ME.13:End

## ME.14 - Evaluate Practical Worth Against Current Alternatives

>
> **Primary working result:** `keep`, `revise`, `replace`, `branch`, or `stop` for one named Method decision. The result makes current alternatives, domain results, burdens, capability and System demands, side effects, opportunity costs, reversibility, evidence strength, and trade-offs explicit. It states what the selected action preserves or reopens and the qualification window. A bounded `XRI-14` evidence result may enter `SYSE.15` without transferring this decision or a broader claim.

### ME.14:0 - Use This When

Use this pattern when an admitted Method or status-preserved candidate has trial evidence and a practitioner must decide what to do relative to current alternatives. Begin with the decision and alternative set: keep the present Method, revise it, replace it, branch by situation, or stop the Method change or use.

The first useful result is a practical-worth comparison row. It names the Method or candidate status, decision situation and receiver, one current alternative, evidence-bearing Work, domain results, burdens, capability and System demands, direct relations, side effects, opportunity cost, reversibility, evidence strength, unresolved trade-off, and the action the row can support. Include the status quo, stopping, or the next best use of scarce Work when it can change the decision.

Here *practical worth* is Plain practice wording for the situated judgment that a Method-related course is worth keeping, changing, replacing, branching, or stopping relative to named alternatives. It is not a universal score, Method admission, fit result, causal attribution, or organization-wide adoption decision.

Do not use this pattern when no current alternative or decision receiver is named, or when the only evidence is conformance, familiarity, one favourable occurrence, or Method popularity. ME.12 coherence and ME.13 fit can inform the comparison but cannot substitute for it.

### ME.14:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| current alternative | A feasible Method, variant, support change, status quo, stop, or next-slot course available to the named decision within its window. | A historical example or impossible ideal is not a current alternative unless it changes the decision. |
| domain result | The result in the receiving practice that the Method-related Work is intended to help produce or protect. | A Method task pass, conformance result, or positive report is not automatically the domain result. |
| burden | Time, cognitive, coordination, resource, maintenance, transition, or evidence burden observed or credibly estimated for the alternative. | Burden is not one scalar unless an explicitly defined aggregation is justified for the decision. |
| capability demand | The holder, Work family or result class, operating envelope, measures, qualification window, and evidence required for reliance. | Training completion, title, assignment, permission, authority, or one success does not establish capability. |
| side effect | A result outside the primary intended result that may help or harm the decision. | An unobserved possibility remains a risk or gap, not an effect. |
| opportunity cost | The named alternative Work, investment, learning, evidence, or receiving result displaced by the choice. | “Cost” without the forgone course is not yet an opportunity-cost claim. |
| reversibility | The conditions, time, information, and retained alternatives needed to undo or branch the choice. | A reversible tool setting does not make changed Method semantics, lost evidence, or organizational commitment reversible. |
| evidence strength | The qualified reach of observations, reports, comparisons, contribution or causal claims for this cell and window. | It is not a confidence adjective detached from source, use, and missing basis. |
| practical-worth decision | A bounded `keep`, `revise`, `replace`, `branch`, or `stop` result with reasons, unresolved trade-offs, and what that action preserves or reopens. | It transfers neither as universal Method rank nor as authority to implement the decision. |

### ME.14:1 - Problem Frame

A Method can be coherent and fit a situation yet still demand too much capability, coordination, tooling, confidentiality exposure, recovery Work, or opportunity cost relative to another course. Conversely, a burdensome Method can be worth keeping where it prevents a consequential failure that a lighter alternative misses.

Teams often hide that choice in one score or in Method familiarity. The score erases who bears the burden, which Systems and direct relations are required, what evidence supports each result, and whether an alternative should be retained for another situation. Practical worth must therefore remain a situated comparison with visible trade-offs.

### ME.14:2 - Problem

Conformance can become value, fit can become superiority, one positive trial can become effectiveness, and immediate participant preference can become long-term worth. A new Method may be compared with an undefined status quo, while stopping or spending the same effort elsewhere is omitted. Capability, support, authority, confidentiality, recovery, and maintenance demands disappear into a weighted total whose assumptions cannot be recovered.

The resulting decision is hard to challenge and harder to revise. Later evidence cannot show which cell changed, a non-dominated alternative is discarded, and a local `keep` becomes an organization-wide adoption claim.

### ME.14:3 - Forces

| Force | Tension |
| --- | --- |
| Decision closure | A team needs an action, while weak or incomparable evidence may justify a set, branch, or stop. |
| Multiple consequences | Domain results and burdens differ in kind and bearer, while one score promises simplicity. |
| Current alternatives | A new Method invites comparison with an idealized baseline, while real alternatives have their own gaps and transition costs. |
| Evidence asymmetry | The incumbent has history and the candidate has focused trials, while neither evidence base is automatically stronger. |
| Capability and support | They may enable value, while their cost and currentness can dominate the decision. |
| Reversibility | Experimentation benefits from recoverable choices, while semantic, organizational, or evidence changes can create lock-in. |
| Local and wider use | A situated branch may be valuable, while sponsors seek one universal winner. |

### ME.14:4 - Solution

Compare feasible current alternatives in the named decision situation using separate consequence and evidence positions, preserve incomparability and branch conditions, and return one bounded action with its result-specific follow-up: no repair return for `keep`, one named maintained result for `revise`, `replace`, or `branch`, and the stopped use plus unresolved trade-off for `stop`.

#### ME.14:4.1 - Pattern-Use Unfolding

1. **Name the decision and receiver.** State who will use the result, which Method or candidate account is under decision, the receiving practice and domain result, qualification window, authority boundary, and the action that `keep`, `revise`, `replace`, `branch`, or `stop` would change. The evaluation result supplies no permission or authority by itself.
2. **Construct the current alternative set.** Include feasible Methods or variants, a support or capability change when it can address the same problem, the status quo, and stopping or the next-slot use of scarce Work when material. Preserve admission and candidate status for every alternative.
3. **State decision characteristics before comparing.** Name domain results, burdens, capability demands, Systems, Agent-performed Work, direct relations, side effects, adaptability, opportunity costs, reversibility, evidence strength, and any additional situation-specific characteristic. State non-compensable stops and who bears each consequence.
4. **Assemble evidence by alternative.** Use ME.11 actual Work and qualified observations; ME.12 corrections or gaps; and ME.13 fit, failure, applicability, or transfer limits. Recover each evidence source, receiving use, situation, window, and missing basis. Do not turn absence of evidence for one alternative into evidence of inferiority.
5. **Preserve the receiving result and Method contribution boundary.** Record the domain result separately from Method task completion, support use, report, or self-assessment. Distinguish direct observation, association, contribution, and causal claim. If contribution is unknown, compare the observed bundle and return the missing attribution basis.
6. **Compare capability, System, Work, and relation demands explicitly.** For every alternative, name holder-capability inputs, participating Systems, Agent-performed Work, direct relations, assignments, permissions, authority, access, provider and confidentiality boundaries, maintenance, recovery, and evidence Work that changes the decision. Do not let availability or assignment substitute for capability.
7. **Keep trade-offs visible.** Show where one alternative improves a domain result but increases burden, side effect, exposure, or opportunity cost. Use current `A.19.CPM` for non-trivial multi-criteria comparison and `A.19.SelectorMechanism` when a set-valued selection is needed. Do not invent a total order or scalar winner.
8. **Test branch and reversibility options.** Ask whether alternatives serve different situation families, whether a reversible trial can close the strongest evidence gap, and what information, retained material, capability, support, or rollback Work a branch requires. A branch must name its situation discriminator.
9. **Return the strongest supported action.** `keep` retains the present course for the named window; `revise` names the ME.2 repertoire choice, ME.3 requirement, ME.6 architecture decision, ME.7 construction result, or ME.15 repertoire entry to reconsider; `replace` names the selected alternative and transition conditions; `branch` names the situation discriminator and retained alternatives; `stop` names the stopped use or change, what happens to current Work, and the unresolved trade-off. If evidence cannot distinguish between the possible actions, return the retained set and next probe.
10. **Route each action according to its kind.** A `revise`, `replace`, or `branch` result reopens only the contradicted ME.2 repertoire choice, ME.3 requirement, ME.6 architecture decision, ME.7 construction result, or ME.15 repertoire entry. `keep` adds no repair return. `stop` preserves the unresolved trade-off and stopped use without inventing a correction owner. If the comparison exposes a possible ME.8 description, ME.9 Method representation profile-row, ME.10 support, or directly governed lower representation contradiction, return the bounded evidence to ME.12; ME.12 identifies and rechecks the maintained correction owner. A worth result does not rewrite that owner automatically.
11. **Package a bounded cross-product evidence result only when needed.** `XRI-14` may supply `SYSE.15` with the situated Method-worth evidence positions and limits needed for an engineering Method-repertoire decision. It transfers neither the ME.14 action, authority, Method rank, causal claim, nor evidence beyond its source-use conditions.
12. **State refresh conditions.** Reopen when alternatives, domain consequences, capability or support demands, direct relations, evidence reach, costs, reversibility, situation fit, or the receiving decision window changes.

#### ME.14:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| worth use | Decision receiver, Method or candidate subject, receiving practice and domain result, action, authority boundary, qualification window, and stop. |
| alternatives | Current feasible alternatives, status quo, stop or next-slot course, statuses, situation branches, and exclusions. |
| characteristics | Domain results, burdens and bearers, capability demands, Systems, Agent-performed Work, direct relations, side effects, adaptability, opportunity costs, reversibility, evidence strength, and non-compensable stops. |
| evidence matrix | Per alternative and characteristic: observation or estimate, source, situation and window, evidence reach, missing basis, and whether it is comparable. |
| trade-offs | Non-dominated positions, conflicts, incomparability, branch discriminators, sensitivity to missing evidence, and reversible probes. |
| decision | `keep`, `revise`, `replace`, `branch`, `stop`, or retained set plus next probe; reasons, unresolved risks, transition or rollback conditions. |
| action follow-up | For `revise`, `replace`, or `branch`: one contradicted ME.2, ME.3, ME.6, ME.7, or ME.15 result; for `keep`: no repair return; for `stop`: stopped use and unresolved trade-off; possible ME.8 description, ME.9 Method representation profile-row, ME.10 support, or lower representation contradiction as bounded evidence to ME.12; unaffected results preserved. |
| cross-product result | When used, bounded `XRI-14` fields, receiving `SYSE.15` use, source-use conditions, non-transfer, and reopen condition. |

#### ME.14:4.3 - What Changes in Practice

Teams stop asking whether a Method is “best” in the abstract. They can see what it changes in the receiving practice, what it demands from people and Systems, which side effects and opportunities matter, what the evidence actually reaches, and why several alternatives may remain.

This also makes stopping constructive. A `stop` can protect scarce Work or avoid an unrecoverable commitment while retaining the evidence and conditions needed to reopen the decision later.

#### ME.14:4.4 - Minimal Constructed Worth Replay

Continue the constructed temperature-sensor review case. The decision is how `Calibration-Team-A` should review reports through day D30. Alternative `ALT-M` uses admitted `M-Unit-Review-1`, description edition 4, the repaired representation, and the manual conversion table. Alternative `ALT-L` uses the current lightweight checklist that verifies tolerance but has no explicit unit-normalization step. `ALT-S` stops the proposed Method change and keeps the present release hold until another comparison is run.

The same qualified `Reviewer-17` performed two admitted `ALT-M` occurrences: seven minutes on the ordinary same-unit report and twelve minutes plus one table lookup on the mixed-unit report; both decisions were correct and the mixed-unit release was stopped. A separate constructed matched replay of `ALT-L`, admitted as `W-L-Rep-1` and `W-L-Disc-1` under the same holder, team, report pair, and window, took five and six minutes. It accepted the ordinary report but failed to expose the mixed-unit mismatch. The replay supplies no causal claim beyond these occurrences and no evidence about another holder or automated support route.

| Position | `ALT-M` | `ALT-L` | `ALT-S` |
| --- | --- | --- | --- |
| domain result | Correct decisions in both observed reports; mixed-unit release stopped. | Correct ordinary decision; mixed-unit mismatch not exposed. | No additional report released; mixed-unit risk remains contained but current release Work stops. |
| burden | Seven and twelve minutes; one lookup; current capability and table required. | Five and six minutes; lower observed burden. | Delay and missing release result; no new review burden. |
| side effect and opportunity | More explicit trace and stop; consumes review time. | Faster but leaves the named unit hazard exposed. | Preserves safety while displacing release and comparison Work. |
| reversibility | Checklist and representation can be reverted while evidence is retained. | Already current; reverting loses no transition Work but retains the exposed hazard. | Reopen after the missing comparison or support basis is supplied. |
| evidence strength | Two constructed teaching occurrences, not field evidence. | Two constructed teaching occurrences, not field evidence. | Consequence follows from the stated stop; downstream cost is unmeasured. |

Return `branch`: require `ALT-M` for reports whose sources can use different unit systems; retain `ALT-L` only for the bounded same-unit situation while a discriminating audit continues. The discriminator is recoverable source-unit variability, not reviewer preference. Also retain `ALT-S` as the stop when that variability cannot be recovered. Reopen the ME.2 repertoire or ME.15 applicability entry, not Method identity, and collect field evidence before extending the branch beyond D30.

This result does not show that `ALT-M` is universally superior or caused every correct decision. It demonstrates why lower burden alone cannot compensate for a declared release stop.

### ME.14:5 - Archetypal Grounding - Field Evidence and Alternatives

The SSFD study reports 95 examples of evidenced individual benefits across 41 detailed workplace-project reports and distinguishes direct and indirect contribution. Those reports can supply domain-result, process, capability, burden, and evidence-strength positions for a worth comparison. They do not by themselves supply a common current alternative, comparable counterfactual Work, SSFD-only causality, or one universal decision.

Project 11 supplies substantial reported outputs from one by-wire steering application; Project 32 supplies a representation difficulty. Preserve both. A practical-worth result may retain SSFD for one situation, revise its representation or support for another, or return missing alternative evidence. Do not average the difficulty and benefit counts into a score.

The sustainable-design study supplies three families of separate workshop observations: The Natural Step, Whole System Mapping, and Biomimicry across 23 workshops, more than 172 qualified respondents, 27 companies, and three industries. Companies chose which workshops they took; most received two or more, order varied, and participants could differ.

The source reports immediate participant-perceived value of activities and mindsets and warns against theoretical-only recommendations. It does not itself supply one named receiver's feasible current-alternative set, a common decision, matched alternative Work, or a counterfactual basis.

For an ME.14 use, establish those positions locally, preserve explicit incomparability and the missing counterfactual basis, and retain voluntary-participation selection bias, unmatched timing, immediate self-report, long-term, causal, transfer, and recombination limits before returning a worth action.

The Halogen case can supply evidence about project demands, practitioner skill sets, organization, and cyclic adaptation. It can justify a `branch` or variant question when conditions differ, but one firm's history does not make its repertoire universally preferable.

#### ME.14:5.1 - APP-ME-01 Early Stop

For EC-417, compare A, B2, revised B2, and the stop or next-slot alternative only when the comparison addresses the same named decision and keeps burden, confidentiality, holder capabilities, project, user, provider, repository, PLM and CI Systems, Agent-performed Work, direct relations, recovery, side effects, reversibility, and evidence limits explicit. The three ME.10 support tasks establish their bounded task observations only; the three-release WorkPlan supplies no release-worth evidence.

Keep `C-EC-Release-v2` as a candidate. Preserve the missing A.22 selection basis, untested AI-provider and feedback branches, and unsupported `CUR-EC417-CadenceEffect-1`. Until release Work and a current alternative have evidence, return `missing-performed-work` and `missing-alternative-evidence`; do not issue `keep` from support-task success.

#### ME.14:5.2 - Bounded `XRI-14` for `SYSE.15`

Supply `XRI-14` only when `SYSE.15` has a compatible engineering Method-repertoire decision and the following positions are recoverable:

| `XRI-14` position | Required boundary |
| --- | --- |
| source decision | ME.14 subject and status, receiving practice, domain result, situation family, alternative set, qualification window, and exact action considered. |
| evidence | Actual Work and sources, domain results, burdens, capability and System demands, Agent-performed Work, direct relations, side effects, opportunity costs, reversibility, evidence reach, and gaps per alternative. |
| supported statement | The smallest situated worth statement that bears on the named `SYSE.15` repertoire-account decision. |
| non-transfer | No transfer of the ME.14 `keep`/`revise`/`replace`/`branch`/`stop` action, implementation authority, universal Method rank, causal claim, or evidence outside the stated source-use conditions. |
| reopen | Changed Method or candidate status, engineering situation, alternatives, evidence, capability or platform conditions, direct relations, or receiving repertoire use. |

`SYSE.15` remains responsible for the engineering Method repertoire and compatibility claims. `XRI-14` supplies evidence for that decision; it does not direct `SYSE.15` to take an ME.14 action.

### ME.14:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| one-score bias | Unlike results, burdens, and evidence are collapsed into one ranking. | Keep cells and non-compensable stops visible; use A.19 for non-trivial comparison. |
| incumbent-evidence bias | Long history is treated as strong comparable evidence while candidate trials are discounted, or vice versa. | Qualify each source, situation, window, and gap symmetrically. |
| fit-as-worth bias | A fit result becomes `keep`. | Add current alternatives, receiving consequences, burdens, and opportunity costs. |
| success-as-causality bias | A favourable occurrence is attributed to the Method. | State association, contribution, causal basis, and missing counterfactual separately. |
| omitted-stop bias | Only active Method alternatives are compared. | Include status quo, stop, or next-slot Work when it changes the decision. |
| capability-free bias | Training, expertise, tool support, and maintenance appear costless. | Record holder capability and support demands with bearers and currentness. |
| universal-winner bias | A local branch or keep becomes organization-wide adoption. | Bound the situation discriminator, window, receiver, and non-transfer. |

### ME.14:7 - Conformance Checklist

- [ ] One decision receiver, Method or candidate subject, receiving practice, domain result, action, and qualification window are named.
- [ ] The alternative set contains only current feasible courses and includes status quo, stop, or next-slot Work when material.
- [ ] Admission and candidate status are preserved for every Method-related alternative.
- [ ] Domain results, burdens, capability demands, Systems, Agent-performed Work, direct relations, side effects, opportunity costs, reversibility, and evidence strength remain separate positions.
- [ ] Evidence from ME.11–ME.13 retains its situation, use, window, and missing basis.
- [ ] Missing evidence is not converted into inferiority, and one favourable occurrence is not converted into causality.
- [ ] Trade-offs, non-dominated alternatives, branch discriminators, and non-compensable stops remain visible.
- [ ] The result is `keep`, `revise`, `replace`, `branch`, `stop`, or a retained set with a decision-changing probe.
- [ ] A `revise`, `replace`, or `branch` result names one contradicted ME.2, ME.3, ME.6, ME.7, or ME.15 result; `keep` adds no repair return; `stop` preserves the unresolved trade-off and stopped use.
- [ ] A possible ME.8 description, ME.9 Method representation profile-row, ME.10 support, or directly governed lower representation contradiction returns as bounded evidence to ME.12 rather than bypassing its owner-specific check.
- [ ] Any `XRI-14` transfer states its exact source-use conditions and non-transfer boundary.

### ME.14:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “It passed verification, so keep it.” | Compare receiving results and current alternatives; coherence is only one input. |
| “Users preferred it, so it is worth adopting.” | Preserve immediate self-report, alternative set, long-term gaps, and decision boundary. |
| “The weighted score selected a winner.” | Expose characteristics, weights or order assumptions, incomparability, and non-compensable stops. |
| “The candidate has no evidence, so the incumbent wins.” | Return the evidence asymmetry and choose a reversible probe or retained set. |
| “SYSE.15 must adopt the ME.14 winner.” | Transfer only bounded `XRI-14` evidence; the receiving repertoire decision remains with SYSE.15. |

### ME.14:9 - Consequences

Practical-worth decisions become revisable accounts rather than Method rankings. Teams can act while retaining branch conditions, evidence gaps, and stop alternatives, and later evidence can reopen the exact comparison position that changed.

The cost is resisting a convenient scalar answer. Some decisions retain several alternatives or require another probe, and the team must name burdens, capability and support demands, side effects, and opportunity costs that were previously hidden.

### ME.14:10 - Rationale

Worth is relational: a Method-related course is worth something for a receiver, situation, domain result, alternative set, and time. Coherence and fit can be necessary inputs to the decision, but they do not settle it. A visible trade-off is more actionable than a score whose composition and evidence reach are hidden.

The five actions distinguish maintenance from change. `Keep` preserves a situated course and adds no repair return; `revise`, `replace`, and `branch` reconsider only one contradicted ME.2, ME.3, ME.6, ME.7, or ME.15 result; `stop` protects against unsupported or dominated continuation while preserving the unresolved trade-off and stopped use without inventing a correction owner. None supplies implementation authority.

### ME.14:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Cash, Daalhuizen, and Hekkert, [method efficacy and effectiveness](https://doi.org/10.1016/j.destud.2023.101204) | Keep practical effect and use conditions separate from internal coherence and one universal Method score. | The source does not make one trial sufficient or supply a universal worth aggregation. |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | Adopt workplace results, varied applications, reported limitations, later review, and the distinction between direct and indirect contribution as evidence positions. | One automotive OEM, retrospective reports, and SSFD within a broader methodology establish neither isolated causality nor universal superiority. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Adopt immediate participant-reported component-value observations from three families of separate workshops across activities, companies, and industries as bounded evidence inputs. | The publication supplies no common receiver, feasible current-alternative set, matched alternative Work, or counterfactual basis; company choice, order, participant differences, voluntary selection, unmatched timing, immediate self-report, long-term effects, causality, transfer, and recombination remain limits. Establish the local decision and comparison basis before returning a worth action. |
| Schønheyder and Nordby, [design-Method use and evolution in professional practice](https://doi.org/10.1016/j.destud.2018.04.001) | Adopt project demands, skill sets, organization, adaptation, and cyclic evolution as possible branch and burden conditions. | One firm supplies no universal repertoire or causal effect. |
| Current FPF `A.19.CPM`, `A.19.SelectorMechanism`, `A.2.2`, `A.10`, and direct governors for Work and relations | Reuse non-totalizing comparison, set-valued selection, capability, evidence, Work, and relation semantics. | ME.14 contributes the Method-specific worth characteristics, five-way action, result-specific follow-up, and bounded cross-product evidence result; it does not redefine the generic kernels. |

Reopen the pattern when a field comparison adds a decision-changing consequence or alternative, when practitioners cannot act without a universal score, when `XRI-14` loses its bounded receiving use, or when current FPF comparison and selection semantics change the returned action.

### ME.14:12 - Relations

- ME.11 supplies actual Work, observations, results, burdens, adaptations, and evidence gaps. ME.12 supplies coherence corrections; ME.13 supplies fit, failure, applicability, and transfer limits. None supplies the practical-worth action.
- For `revise`, `replace`, or `branch`, ME.2 can receive a contradicted repertoire choice, ME.3 a contradicted requirement, ME.6 a contradicted architecture decision, ME.7 a contradicted construction result, and ME.15 a contradicted repertoire entry. `keep` adds no repair return; `stop` preserves the unresolved trade-off and stopped use.
- A possible ME.8 description, ME.9 Method representation profile-row, ME.10 support, or directly governed lower representation contradiction returns as bounded evidence to ME.12, which identifies and rechecks the maintained correction owner.
- `A.19.CPM` and `A.19.SelectorMechanism` govern non-trivial comparison and selected-set semantics. `A.2.2` governs capability inputs; `A.10` evidence use; `A.15.1` actual Work; direct governors remain authoritative for Systems, Agent-performed Work, relations, assignments, permissions, authority, access, and results.
- `XRI-14` can supply only bounded Method-worth evidence to a compatible `SYSE.15` repertoire-account decision. It transfers neither action nor authority and does not join Method Engineering and Systems Engineering products.
- ME.16 may consume the resulting bounded decision when introducing or revising a Method in practice; later observations can reopen ME.14 without retroactively changing the evidence used here.

### ME.14:End

# Part V - Variants, Introduction into Practice, and Cultural Continuation

## ME.15 - Maintain Method Variants, Provenance, and Reuse

>
> **Primary working result:** a maintained repertoire of admitted Method variants and separately status-preserved candidate lineages, with derivation, preserved and changed reusable semantics, applicable situations, descriptions and support editions, evidence, selection uses, currentness, and retirement conditions. For every non-variant change, the changed object, separately governed maintained result, exact affected claim or edition, and next maintenance, reconsideration, or stop action are visible.

### ME.15:0 - Use This When

Use this pattern when a Method has been adapted, branched, recombined, or revised and future users must know whether they face the same Method, a reusable variant, a candidate proposal, or only a changed description, representation, tool, prompt, publication, support result, or local Work occurrence. Begin with the reusable way of doing that may have changed: which operation, dependency, role in the way of doing, entry or stop rule, or other reusable Method semantic is different?

For a first pass, write two lines: what reusable way of doing changed, if any; and, if none did, which object changed, which maintained result and exact claim or edition it affects, and what to maintain, reconsider, or stop. Continue into the fuller row only when later selection, reuse, comparison, or retirement needs it.

The first useful result is a variant-lineage row. It names the parent Method or candidate, the proposed child and status, preserved semantics, changed semantics, derivation basis, applicable situation claim, supporting and defeating evidence, descriptions and support editions, current selection uses, currentness, retirement condition, and the next decision. If the visible change is not a Method variant, the row instead names the changed object, the separately governed maintained result, the exact claim or edition affected, and the next maintenance, reconsideration, or stop action.

Here *variant* is Plain practice wording for a Method whose reusable semantics differ in a way relevant to a named use while its derivation from another Method remains useful. The label alone does not admit a `U.Method`, establish provenance, or prove fit, worth, reuse, or superiority.

Do not use this pattern merely because a file, diagram, MethodDescription edition, prompt, tool, publication form, support configuration, team, project, or dated Work occurrence changed. Maintain those results under their own patterns unless the change also alters reusable Method semantics.

### ME.15:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| reusable Method semantics | The repeatable operations, dependencies, entry and stop rules, roles in the way of doing, transformation commitments, or other claims that distinguish how the Method is carried out and when it applies. | A wording, layout, carrier, tool, or local performance difference is not automatically semantic change. |
| admitted variant | An independently admitted Method whose changed and preserved reusable semantics and derivation are recoverable for the maintained use. | Derivation from an admitted parent does not admit the child. |
| candidate lineage | A status-preserved sequence or family of candidate accounts whose proposed semantic changes and derivations are tracked without Method admission. | A well-documented candidate does not become a MethodDescription or enacted Method. |
| derivation claim | The evidence-bearing claim that one Method or candidate arose through identified changes from another. | Similarity of names, files, or outcomes does not establish derivation. |
| preserved semantics | Reusable Method claims intentionally retained across the derivation. | “Mostly the same” is insufficient when the receiving use depends on the omitted difference. |
| changed semantics | Reusable Method claims added, removed, reordered, constrained, generalized, specialized, or recomposed in the proposed child. | A local departure in one Work occurrence remains a deviation until reusable semantics are recovered. |
| applicability entry | A bounded claim about situations, capability and support conditions, evidence, and stops for selecting or rejecting a variant. | It is not practical worth, organization-wide adoption, or a selection command. |
| edition and support link | The MethodDescription, representation, method-base edition, publication, tool, prompt, or support result currently used for a variant. | These results can change without changing variant identity and can serve several variants only when their claims permit it. |
| retirement condition | A named evidence, currentness, source, use, or replacement condition under which an entry stops being offered for the maintained selection use. | Retirement from one repertoire use does not erase the Method, its history, or every other use. |

### ME.15:1 - Problem Frame

Method adaptation leaves many visible traces: a team edits a checklist, adds a tool, changes a diagram, rewrites a prompt, or performs the Work differently. Some traces express a reusable change in the way of doing; others are only descriptions, support configurations, local departures, or evidence. Treating every trace as a Method variant floods the repertoire with false identities. Treating none as a variant hides meaningful branches and makes later fit and worth evidence impossible to bind to the semantic branch they concern.

The practical question is whether reusable Method semantics differ for the named use, what derivation is supported, and which status, applicability, evidence, and currentness claims can be maintained while keeping candidate accounts distinct from admitted Methods.

### ME.15:2 - Problem

Version numbers, filenames, team names, tool stacks, and project histories become variant identifiers. A successful local adaptation is generalized without an admitted reusable Method. Candidate recombinations inherit parent admission. A new MethodDescription edition is mistaken for a new Method, while a real change to operation order or stop conditions is hidden as documentation maintenance.

The resulting repertoire cannot guide selection. Users cannot tell which semantics changed, whether evidence applies to parent or child, what support edition is current, which situation claim is supported, or when an entry should be retired.

### ME.15:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse | Stable variant identities help later selection, while premature naming creates spurious Methods. |
| Local adaptation | Work must respond to situations, while one local departure need not be reusable semantics. |
| Provenance | Derivation helps explain and compare variants, while similarity and chronology can be mistaken for evidence. |
| Evidence | Fit and worth results should follow the right semantics, while evidence often bundles Method, support, capability, and organization. |
| Currentness | Users need current entries and editions, while retirement from one use must not erase history. |
| Candidate continuity | Proposed changes need traceability, while detailed lineage can launder candidate status. |
| Recombination | Components can inspire new Methods, while untested hybrids do not inherit component admission or worth. |

### ME.15:4 - Solution

Identify variants only through changed reusable Method semantics, preserve admission or candidate status independently, and maintain derivation, applicability, evidence, editions, selection uses, currentness, and retirement as separate claims.

#### ME.15:4.1 - Pattern-Use Unfolding

1. **Name the maintenance use.** Identify the practitioner or decision that needs the repertoire, the Method family or candidate lineage in scope, the situation and qualification window, and what selection, reuse, comparison, or retirement action the entry must support.
2. **Recover each subject and status.** Identify every `A.3.1`-admitted Method and every candidate account separately. A parent Method, candidate child, MethodDescription, representation, support configuration, and Work occurrence keep different identities and statuses.
3. **Recover the semantic baseline.** From the parent or earlier candidate, record the reusable operations, dependencies, entry and stop rules, roles in the way of doing, required relations, and applicability claims that matter to the maintenance use. Do not use a file diff as the semantic baseline.
4. **Classify the observed change.** Separate changed reusable Method semantics from description wording, representation, publication, tool, prompt, support, capability, organizational System or selected structure, assignment, permission, authority, and local Work deviations. For every non-semantic change, name the changed object, the separately governed maintained result, the exact claim or edition affected, and the next maintenance, reconsideration, or stop action. A complete ME.9 Method representation profile is the maintained result only when several unlike Method-related actions have one complete C.37-bearing row each and the profile records their shared Method source, correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. One action remains with C.37 and its direct governor. Name a direct predicate and its participants only when the disposition relies on that obtaining relation; otherwise assert no path or relation occurrence.
5. **Construct the proposed child account.** State preserved semantics, changed semantics, reason for change, intended situations, required capability and support conditions, prohibited overreads, and the evidence or trial needed. If no reusable semantic difference remains, maintain an edition, support, or Work result rather than a variant.
6. **Establish derivation without inheriting admission.** Record the source Method or candidate, change Work or source account, changed positions, chronology when relevant, and evidence supporting the derivation claim. Then admit the proposed child independently under `A.3.1` or keep it as a candidate.
7. **Bind evidence to the right semantics and situation.** Attach ME.11 trial observations, ME.12 corrections, ME.13 fit or transfer results, and ME.14 worth decisions only to the Method or candidate semantics, situation, support, capability, alternative set, and window they actually concern. Parent evidence does not automatically cover the child.
8. **Maintain descriptions, Method representation profiles, and support relations separately.** Name current ME.8 MethodDescription editions, complete ME.9 profiles, ME.10 method-base and support results, publications, tools, prompts, and any exact access or use relation that serves the variant use. For every ME.9 profile retain the shared MethodDescription or candidate-account source, one complete C.37-bearing row per unlike action, cross-use correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return. A one-action representation stays with C.37 and its direct FPF governor. A changed result, edition, or relation does not by itself change variant identity.
9. **State applicability and selection uses.** Record supported situations, defeated situations, missing evidence, capability and support conditions, current alternative set, and the receiving decision that may use the entry. Use A.19 selected-set semantics for a non-trivial repertoire choice; the entry itself selects nothing.
10. **Maintain currentness and retirement.** State source, evidence, edition, situation, and qualification windows; superseding or defeating evidence; review trigger; and what retirement means for this use. Preserve historical and other-use access when the Method or candidate still matters elsewhere.
11. **Return the maintained repertoire and non-variant dispositions.** Report admitted variants, candidate lineages, applicability and evidence gaps, current entries, retired entries, and the smallest repertoire claim reopened by defeated applicability, evidence, currentness, or retirement evidence. For every non-variant, report the changed object, separately governed maintained result, exact affected claim or edition, and next maintenance, reconsideration, or stop action. Do not assign repair authority or invent a relation when the governing result and next action are sufficient.

#### ME.15:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| maintenance use | Practitioner or receiver, repertoire decision, situation, qualification window, and stop. |
| subject and status | Parent and child Methods or candidate accounts; separate descriptions, representations, support results, Work, and evidence. |
| semantic baseline | Reusable operations, dependencies, entry and stop rules, roles in the way of doing, relations, and applicability claims relevant to the use. |
| change classification | Changed reusable semantics; for each non-variant, the changed object, separately governed maintained result, exact affected claim or edition, and next maintenance, reconsideration, or stop action. |
| derivation | Parent, proposed child, change basis, chronology when material, preserved semantics, changed semantics, and evidence reach. |
| admission branch | Independent Method admission or status-preserved candidate account and missing admission basis. |
| applicability and evidence | Situations, capability and support conditions, trials, coherence, fit or transfer, worth, alternatives, gaps, and qualification windows bound to the right semantics. |
| edition and support links | Current descriptions; complete ME.9 Method representation profiles with shared source, one complete C.37-bearing row per unlike action, cross-use correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row return; method-base editions, publications, tools, prompts, and support results for each maintained use. |
| currentness and retirement | Current selection uses, source and evidence windows, defeating conditions, retirement meaning, retained history, and reopen trigger. |
| return | Maintained admitted-variant repertoire and candidate lineages; non-variant dispositions in the same four-part shape; the smallest defeated repertoire claim when one exists; and limits on what the repertoire establishes. |

#### ME.15:4.3 - What Changes in Practice

Teams stop using version labels and project names as Method identities. They can show which reusable semantics changed, which evidence belongs to which branch, why a child is admitted or still a candidate, and which description or support edition serves each use.

The repertoire becomes smaller and more useful. Local departures can remain Work evidence, descriptions can evolve without multiplying Methods, and real semantic branches receive applicability, evidence, currentness, and retirement conditions.

#### ME.15:4.4 - Minimal Constructed Variant Replay

Continue the temperature-sensor review chain. `M-Unit-Review-1` is admitted with reusable semantics: identify every source unit, normalize values, compare with declared tolerance, and stop on an unresolved mismatch. ME.14 retained it for reports whose sources can use different unit systems.

A team proposes an approximation rule for missing conversion metadata: infer a likely scale from sensor range, mark the inference, and continue only when the tolerance decision is unchanged under both plausible scales. This is not merely a new checklist. It changes the reusable operation and stop conditions, so create candidate account `C-M-Unit-Review-Approx-1` derived from `M-Unit-Review-1`. Preserve identification, explicit normalization when metadata exists, tolerance comparison, and unresolved-mismatch stop; add the bounded inference operation and a two-scale invariance stop.

Do not admit the candidate from parent status. Link candidate-account content `CA-M-Unit-Review-Approx-Content-1`, proposed representation `C-REP-Approx-1` of that candidate account, and the same conversion-table support result only as candidate-serving material; none is a `U.MethodDescription` for the candidate whole. Return trial needs for missing-metadata reports, capability conditions for the reviewer, and comparison against stopping or metadata recovery. Until independent admission and evidence exist, the repertoire contains admitted `M-Unit-Review-1` plus candidate lineage `C-M-Unit-Review-Approx-1`; no Work is said to enact the candidate whole.

If the team only updates the diagram to show the already-required normalization step, first identify its exact action. For one action, maintain the complete C.37-bearing use row and the diagram under its direct governor; ME.9 is not invoked. When that row belongs to a complete ME.9 profile for several unlike actions, also maintain only the cross-use correspondences, conflicting omissions, edition relations, keep-separate decisions, and multi-row returns affected by the diagram change. Neither case creates a variant. If the team replaces the manual table with a verified tool while operations and stops remain unchanged, maintain the ME.10 support result and no variant.

### ME.15:5 - Archetypal Grounding - Adaptation and Recombination

The Halogen design-practice case reports conscious cyclic evolution and adaptation of Methods across safety-critical projects, practitioner skill sets, and organization of design activity. Use the evidence to recover proposed semantic changes, local Work deviations, situation conditions, and lineage candidates. The source concerns one 52-person multidisciplinary firm and does not supply a universal variant family or automatic Method admission.

When reusable semantics can be recovered and a Method is independently admitted, maintain the variant with its derivation and applicability. When interviews, observations, or documents show only local departures or cannot distinguish changed Method semantics from changed support, capability, or organization, maintain a candidate lineage or return the missing semantic basis.

The sustainable-design study reports activity- and mindset-level observations from separate workshops using The Natural Step, Whole System Mapping, or Biomimicry. Companies chose workshops, order varied, and participants could differ, so the publication supplies neither one current-alternative decision nor matched Work across the three Method families. Those immediate participant reports can motivate recombination candidates, but a preferred component set is not an admitted hybrid Method. Record the proposed preserved and changed semantics, parent contributions, situations, and trials needed; do not inherit worth or transfer from the source Methods.

#### ME.15:5.1 - APP-ME-01 Candidate Lineage

Maintain editions of `C-EC-Release-v2` as a candidate lineage until `A.3.1` admits a Method with recoverable reusable semantics. Keep the four admitted constituent Methods, their descriptions, representations, PLM and CI Systems, prompts, support arrangements, release Work, and local deviations separate.

A changed release document, cadence, tool integration, AI prompt, or method-base edition does not create a `C-EC-Release-v2` variant by itself. A proposed semantic change must name the changed reusable operation, dependency, entry or stop rule, or another Method claim and preserve the candidate branch. Unsupported `CUR-EC417-CadenceEffect-1` remains unsupported.

### ME.15:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| file-version bias | Every document or repository version becomes a Method variant. | Compare reusable Method semantics; for an edition-only change, name the maintained result, exact edition claim, and next maintenance or stop action. |
| local-deviation bias | One Work departure becomes a reusable Method. | Recover repetition, intended reuse, semantic account, and independent admission; otherwise keep Work evidence. |
| inherited-admission bias | A child or hybrid inherits parent Method status. | Admit every proposed Method independently or preserve candidate status. |
| tool-identity bias | A new prompt, tool, or platform becomes the variant. | Ask which reusable operations or stops changed; maintain support when none did. |
| evidence-smearing bias | Parent fit or worth evidence is attached to every descendant. | Bind evidence to semantics, situation, support, capability, alternative set, and window. |
| lineage-as-worth bias | Detailed provenance is treated as evidence that the branch should be selected. | Keep derivation, applicability, and practical worth as separate claims. |
| retirement-erasure bias | Retirement from one repertoire use deletes history and other uses. | State the retired selection use and preserve the Method, lineage, and evidence where still needed. |

### ME.15:7 - Conformance Checklist

- [ ] One maintenance and selection use, receiver, situation, window, and stop are named.
- [ ] Every parent and child is independently admitted as a Method or preserved as a candidate account.
- [ ] Reusable Method semantics are recovered before variant identity is claimed.
- [ ] Preserved and changed semantics are explicit and decision-relevant.
- [ ] Description, representation, publication, tool, prompt, support, capability, organization, and local Work changes remain separately governed.
- [ ] Derivation has an evidence basis and does not transfer admission.
- [ ] Trial, coherence, fit or transfer, and worth evidence is bound to the right semantics, situation, conditions, alternatives, and window.
- [ ] Current description and support editions are linked without defining variant identity.
- [ ] Applicability, missing evidence, selection use, currentness, and retirement conditions are recoverable.
- [ ] Recombination candidates inherit neither parent admission nor parent worth.

### ME.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Version 2.1 is a new Method variant.” | Show the changed reusable Method semantics or maintain an edition only. |
| “The team adapted it, so the variant is admitted.” | Preserve the Work evidence and candidate account until independent admission. |
| “The AI prompt defines the new Method.” | Recover the way of doing and support relation; a prompt can serve but not identify the Method by itself. |
| “The hybrid inherits evidence from all three parent Methods.” | Trial the proposed semantics and bind evidence to the hybrid's own situation and status. |
| “Retired means obsolete everywhere.” | Name the selection use and defeating condition; preserve other supported uses and history. |

### ME.15:9 - Consequences

Variant repertoires show the reusable semantic differences and the evidence for each branch. Practitioners can select among stable admitted Methods and visible candidate branches without confusing package change with Method change.

The cost is more disciplined status and provenance work. Some attractive adaptations remain candidate lineages, and teams must keep descriptions, support editions, evidence, and selection uses linked without letting any one of them define identity.

### ME.15:10 - Rationale

Reuse depends on knowing what way of doing is being reused. Files and tools can carry or support that way, and Work can reveal changes, but only reusable semantic change distinguishes a Method variant for the maintained use. Derivation does not supply the child's Method admission; that admission is checked independently.

Maintaining applicability, evidence, currentness, and retirement with the variant prevents a static family tree. The result is a repertoire for decisions rather than a genealogy or archive alone.

### ME.15:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Schønheyder and Nordby, [design-Method use and evolution in professional practice](https://doi.org/10.1016/j.destud.2018.04.001) | Adopt cyclic evolution, project demands, practitioner skill sets, organization, and observed adaptation as inputs to variant and applicability maintenance. | One multidisciplinary design firm supplies neither a universal variant taxonomy nor independent admission or causal effect. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Adopt activity- and mindset-level observations across three Methods and industries as evidence that can motivate bounded branch or recombination questions. | Immediate self-report does not establish long-term results, hybrid-Method admission, or the worth of recombined variants. |
| Gericke et al., [method ecosystems](https://doi.org/10.1017/dsj.2020.21), and Stacey et al., [Methods as engineering knowledge](https://doi.org/10.1017/dsj.2025.9) | Adopt maintained Method ecology, content, representation, use, and change questions for the repertoire account. | Position and knowledge contributions do not show that one repository, support stack, or variant organization works universally. |
| Current FPF `A.3.1`, `A.3.1.MR`, `C.2.1`, `A.10`, `G.5`, `G.11`, and A.19 selected-set semantics | Reuse Method admission, candidate recovery, edition identity, evidence use, registered Method-family candidate sets, and non-forced selection. ME.15 itself records local source, evidence, situation, qualification-window, defeating-evidence, and retirement claims. Invoke G.11 only when the entry participates in a G.11-admitted shipped pack, evidence or selected set, archive or front, publication/currentness object, dependency on a reused A.6.RCD predicate definition or derived relation kind, or another condition named by G.11. | ME.15 contributes Method-variant semantic classification, derivation, applicability, and local maintenance. It neither redefines those governors nor turns every repertoire-entry currentness or retirement question into refresh orchestration. |

Reopen the pattern when practitioners cannot distinguish reusable semantic change from local Work or support change, when a mature source supplies a stronger variant identity and retirement method, when a new case demonstrates an independently useful lineage problem not covered here, or when current FPF Method and repertoire semantics change the result.

### ME.15:12 - Relations

- ME.11 supplies actual adaptation and deviation evidence; ME.12 supplies corrections tied to exact contradicted claims and maintained results; ME.13 supplies applicability, fit, failure, and transfer limits; ME.14 supplies bounded practical-worth and branch decisions. None identifies a variant without changed reusable Method semantics.
- ME.8 maintains descriptions; C.37 maintains one-action representation-use results; ME.9 maintains complete Method representation profiles for several unlike Method-related actions, including their action rows and separate cross-use result; ME.10 maintains method-base editions, publications, tools, prompts, and support results. A lower representation remains with its direct FPF governor. Changes to any of these results do not automatically change Method identity, and a non-variant disposition names the changed object, maintained result, exact affected claim or edition, and next action.
- `A.3.1` governs Method admission. `A.3.1.MR` can recover a candidate Method from Work evidence under its conditions. `C.2.1` governs episteme and edition identity; `A.10` evidence use; `G.5` registered Method-family candidate sets; A.19 comparison and selected-set semantics.
- ME.15 records local source, evidence, situation, qualification-window, defeating-evidence, currentness, and retirement claims. Open `G.11` refresh orchestration only for one of its named shipped packs, evidence or selected sets, archives or fronts, publication/currentness objects, dependencies on reused A.6.RCD predicate definitions or derived relation kinds, or another G.11-admitted condition.
- `A.3.4` governs any separate claim that one continuing carrier, organizational System, selected structure, or other subject actually changed across a bounded occurrence. A semantic difference, derivation account, edition relation, or local Work deviation does not by itself establish a `U.Transformation`.
- ME.16 consumes a maintained admitted variant or status-preserved candidate entry when attempting a bounded introduction. ME.17 uses either an independently admitted Method Engineering Method with actual enactment or a status-preserved candidate or observed-practice branch without Method or enactment inflation; neither inherits admission or worth from the repertoire.

### ME.15:End

## ME.16 - Introduce, Observe, and Revise a Method in Practice

>
> **Primary working result:** an introduction account that identifies each changed subject and keeps its kind explicit. It records the introduction strategy and its status, separately identified candidate accounts and descriptions, and any WorkPlan. It distinguishes admitted introduction Work from admitted later Work; both enact only independently admitted Methods. The account names assignment, permission, authority, access, use, enactment, and other direct-relation predicates, participants, and relied-on occurrences. It also contains decision-relevant observation positions, separate target and strategy adaptation records, an optional C.28-governed causal-use result, and one bounded `keep`, `revise`, `branch`, `replace`, or `stop` decision.

### ME.16:0 - Use This When

Use this pattern when an admitted Method variant or a status-preserved candidate account is ready for a bounded introduction attempt in a real practice and the team must learn which intended Method-related conditions were actually established after people and Systems worked. Begin by separating the Method-related target and direct-relation claims; the introduction strategy and its status; the descriptions and any WorkPlan used to guide it; performed introduction Work; later Work and observations; and the outside result that motivated the attempt.

For a first pass, write one plain row: what the team tried to establish, what Work it actually performed, what was later observed or failed, which maintained claim that observation affects, and what to do next. Add typed subjects, relation predicates, adaptation detail, or causal apparatus only where the decision relies on them.

The first useful result is an introduction-observation row. It names each changed subject or direct-relation occurrence; the introduction strategy, its status, description, and any separate WorkPlan; the bounded setting and period; authorized introduction Work; later actual Work or failed entry; decision-relevant observations; any target or introduction-strategy adaptation; evidence reach; the particular maintained claim or edition affected; the next receiving action; and residual uncertainty.

Here *introduction* is Plain practice wording for authorized performed Work intended to establish named Method-related conditions in a bounded setting. The Work can be completed even when access, usability, later enactment, fit, or an outside result fails. Actual availability, usability, or change comes only from later observations and, when a continuing subject is claimed to have changed, the required A.3.4 result.

Do not use this pattern to develop capability implicitly. When current capability is adequate and no relevant change is required or asserted, retain its `A.2.2` basis and currentness without demanding development. Omit capability detail that cannot change the decision. Consume a named `E.23.CDI` or domain capability-development result only when capability change is required. If it is missing or stale, name the missing result or governing pattern, the receiving Agent when one is current, and the next development or stop action. Use ME.17 when the primary question is a bounded population-level transmission, recognition, selection, memory, retention, loss, or other cultural claim.

### ME.16:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| introduction target | One named changed subject or one direct-relation claim: for example an admitted Method selection, a separately identified description episteme, support System, capability bearer and capability result, particular Work occurrence, domain entity, organizational System, selected structure, or assignment, permission, authority, access, use, or enactment predicate with named participants. | A mixed list of nouns does not state which things exist, which claims are maintained, or which relations obtain. |
| candidate account and description | Claim-bearing content about a proposed Method or local change, with candidate status retained, plus any separately identified description or representation. | A candidate account is not a Method, MethodDescription of the candidate whole, Work, or relation occurrence. |
| bounded setting | The place, period, practitioner population, Work family, identified organizational System or selected structure when one is relied on, participating Systems, obtaining relations, and protected conditions. | A company, team, or discipline label alone does not identify an organizational System or structure. |
| introduction Method, candidate account, description, plan, and Work | Retain the proposed way of establishing named conditions as a candidate introduction account until A.3.1 admits its Method. Before admission, keep claim-bearing content as that account or another honestly named description episteme; it is not a `U.MethodDescription`. After admission, use `U.MethodDescription` only when A.3.2 classifies an episteme whose one `EntityOfConcern` is that admitted Method. Keep any WorkPlan and authorized performed Work separate in both branches. Performed Work may enact only independently admitted Methods. | A strategy label, candidate account, description episteme, plan, announcement, publication, training invitation, or available tool establishes neither Method admission nor enactment, performed Work, or success. |
| later practice Work | Actual Work after the introduction in which an admitted Method is enacted, or in which candidate claims are compared while only independently admitted constituent Methods are enacted. | Availability, attendance, access, or one tool interaction does not establish enactment; a candidate account is never enacted. |
| capability-development input | An independently governed result naming holder, Work family, baseline, target, intervention, representative transfer Work, evidence, and currentness. | ME.16 can rely on the result; it does not perform or certify capability development. |
| observation position | One decision-relevant observation about acceptability or rejection, appropriateness or fit, feasibility, enactment or fidelity, burden or cost, reach, sustainment, an outside result, or a named changed subject or relation. | Each position has its own subject, claim, evidence, receiving action, and stop; no favourable result fills the others. |
| adaptation record | What changed, when, whether planned or reactive, the deciding Agent and named authorization predicate with participants, the affected level, why and under which conditions, and whether the modification changed the Method-related target or the introduction strategy, its recorded status, description, WorkPlan, support, or only a local-use condition. | A modification of the introduction strategy is not a modification of the target Method-related subject; an adaptation does not by itself change the status or kind of any account, description, plan, Method, or Work. |
| contribution or causal-use claim | A separately governed claim that one change participated in or caused an observed result under named conditions. | Temporal order, participant report, association, or a before/after difference supplies no causal reliance by itself. |
| revision decision | `keep`, `revise`, `branch`, `replace`, or `stop` for this bounded attempt and the particular maintained claims or editions affected. | It grants no authority for the next change and creates no adoption lifecycle. |

### ME.16:1 - Problem Frame

Method introductions bundle many subjects, descriptions, relation occurrences, and Work. A new procedure or description arrives with capability development, expert assistance, a tool, changed assignments, management attention, templates, review forums, and new Work. Later results are then attributed to “the Method”, while failures are blamed on resistance or capability. Neither conclusion shows what actually changed.

The practical question is more demanding: which named subjects and direct-relation occurrences were intended to change; which accounts and descriptions stated the target proposal; what status the introduction strategy and its description had; which separate WorkPlan coordinated intended Work; what authorized introduction Work and later Work occurred or failed; what was observed at each decision-relevant position; what outside result followed; and whether any contribution or causal reliance has a current C.28 basis.

### ME.16:2 - Problem

A rollout plan can be reported as adoption. Training can be reported as capability. Tool availability can be reported as use. A manager's sponsorship can be reported as permission or authority. Later Work can be merged with the introduction Work, and a favourable domain result can be assigned to the Method without an alternative or contribution basis.

When several positions are compressed into one intervention label, the team cannot revise locally. It either repeats the whole programme or rejects it, even when the defect lies in one description, support relation, capability condition, assignment, permission, authority boundary, or outside-result assumption.

### ME.16:3 - Forces

| Force | Tension |
| --- | --- |
| Real practice | Natural Work reveals use and consequences, while many conditions change together. |
| Intervention clarity | Separate intended changes make learning possible, while programmes prefer one headline. |
| Capability | New Work may need development, while ME.16 must not smuggle training in as capability. |
| Authority and participation | Local change needs authorization and actual performers, while sponsorship and attendance are weaker facts. |
| Time | Later observation is needed, while waiting too long can make sources and alternatives stale. |
| Contribution | A decision needs a plausible account, while causal isolation is often unavailable. |
| Revision locality | One defeated claim should reopen one result, while bundled rollout invites whole-programme repair. |

### ME.16:4 - Solution

Build a typed account of the target subjects, accounts and descriptions, the introduction strategy and its status, any separate WorkPlan, actual Work occurrences, and named relied-on relations. Perform the bounded introduction attempt, observe later Work and decision-relevant outcomes separately, distinguish target adaptations from introduction-strategy adaptations, invoke C.28 only for a causal reliance, and revise only the maintained claim the evidence contradicts.

#### ME.16:4.1 - Pattern-Use Unfolding

1. **Name the outside result and bounded decision.** Identify the receiving practice, intended outside result, admitted Method or candidate-account status, setting, period, population, qualification window, and what `keep`, `revise`, `branch`, `replace`, or `stop` will change.
2. **Build the typed target-and-strategy account.** Name changed target subjects separately: admitted Methods; A.3.2-classified MethodDescriptions or other claim-bearing epistemes; representations; Systems; capability bearers and capability results; particular Work occurrences; domain entities; identified organizational Systems or selected structures. Keep candidate target accounts and descriptions separate.

   If A.3.1 has admitted the introduction Method, name it and identify a `U.MethodDescription` only when A.3.2 classifies an episteme whose one `EntityOfConcern` is that Method. Otherwise retain a candidate introduction account and identify its claim-bearing material as a candidate account, description episteme, or other named episteme with status, claims, and maintained result; do not classify it as `U.MethodDescription`. Identify any WorkPlan separately; neither the plan nor performed Work admits or enacts the candidate.

   For every relied-on assignment, permission, authority, access, use, enactment, or other direct relation, name the predicate, participant meanings, participants, and obtaining basis. Omit unclaimed positions.
3. **Recover each maintained result and receiving action.** For every target, introduction-strategy object, and observation position, record its maintained result, particular claim or edition, current status, evidence, source and qualification window, observation that would support or defeat it, receiving Agent or governing pattern when one is current, and next maintenance, reconsideration, or stop action. A result is not an actor.
4. **Select the capability branch.** Omit capability detail that cannot change the attempt, interpretation, or decision. When the decision does rely on capability, recover the `A.2.2` basis: holder, Work family, envelope, measures, qualification window, evidence, and currentness. If existing capability is adequate and no relevant capability change is required or asserted, retain it as a reliance or observation condition; no development result is needed. A missing capability basis returns that `A.2.2` question, not an automatic development prescription. Only when a capability-change claim is needed, consume a compatible `E.23.CDI` or domain development result naming holder, Work family, baseline, target, intervention, representative transfer Work, evidence, and currentness. If that required result is missing or stale, name the gap and the next governing development decision or stop; ME.16 does not fill it.
5. **Bound authorization and protected conditions.** Identify the change decision-making Agent, A.13 basis, and the named assignment, permission, or authority predicate with participants and scope that permits each intended change. Name participating Systems, confidentiality and safety stops, and protected conditions. Expertise, sponsorship, project position, ownership, tool control, assignment, permission, and authority are not interchangeable bases.
6. **Plan decision-relevant observations before intervention.** Select only positions that can change the decision: acceptability or rejection; appropriateness or fit; feasibility; enactment or fidelity; burden or cost; reach; sustainment; changes to named targets or to the introduction strategy; and the outside result. Keep acceptability as a stakeholder observation, formal fit or transfer with ME.13, actual enactment with A.15.1, bounded reach as observed participation, and a population-level continuation question with ME.17. Preserve ME.11 trial, ME.13 fit, and ME.14 worth questions as distinct inputs or later uses.
7. **Plan separate target and introduction-strategy adaptation records.** First classify every planned or observed modification as a change to the Method-related target or a change to the way it is introduced. Record what changed, when, planned or reactive status, deciding Agent and named authorization predicate, affected level, reason and conditions.

   For a target change, name the affected Method semantics, description, support, capability input, fit claim, cultural question, or local-use condition. For an introduction-strategy change, name the admitted introduction Method or candidate introduction account, its admissibly classified description episteme, and any separate WorkPlan claim.

   Return each modification to its own maintained result or local stop: ME.15 for admitted Method semantics or candidate lineage; ME.8 only for a `U.MethodDescription` whose Method is admitted by A.3.1 and whose episteme is classified by A.3.2; the candidate account, another named episteme, or a local ME.16 stop for pre-admission description content; ME.10 for support; A.15.2 for a WorkPlan; ME.13 for fit; or ME.17 for a population cultural question.
8. **Perform and admit introduction Work.** Recover actual performers and A.13 bases, the independently admitted Method enacted by the introduction Work, action history, temporal extent, containing System, named changed subjects, used Systems, and relied-on relation occurrences. Record the result as an attempt intended to establish named conditions. A completed failed attempt remains Work even if access, usability, or later enactment did not result. A candidate introduction Method is not enacted; name only the admitted constituent Methods actually followed.
9. **Observe later actual Work, failed entry, and non-use.** Admit later Work independently. Record which admitted Method was enacted, or preserve candidate status and name only separately admitted constituent Methods. Also record failed entry, rejection, non-use, workaround, adaptation, support demand, and burden when observed; absence of a record is not automatically non-use.
10. **Compare every selected position.** For each target, introduction-strategy object, and decision-relevant observation, state supported change, no change, uncertainty, inapplicability, or missing evidence. State the particular maintained claim or edition and next action. If a continuing subject is claimed to have changed, use A.3.4; a before/after table or performed Work alone does not establish that transformation.
11. **Apply the causal-use branch only when relied on.** Ask whether the ME.16 decision relies on a causal or contribution claim. If no, return observations or association and stop causal reliance. If yes, use current C.28 for the bounded causal-use question, supported use, unsupported stronger use, population and conditions, validity threat, and reopen trigger. Name a contribution relation or compound claim only with its predicate, participants, applicability, and obtaining basis. C.28 settles causal support; ME.16 still makes the bounded revision decision.
12. **Decide and return observations.** Return `keep`, `revise`, `branch`, `replace`, `stop`, or a retained set with one decision-changing next probe. Send an observation to ME.8 only for an A.3.2-classified `U.MethodDescription` about an A.3.1-admitted Method. Before admission, return candidate-strategy content to its candidate account, another honestly named episteme, or a local stop. Send other observations to ME.15, ME.10, A.15.2, ME.13, ME.17, a named capability-development result, another admissible maintained result, or a receiving Agent only when the particular claim or edition and next action are stated; otherwise keep the observation as a local decision or stop.
13. **State non-use and refresh.** The result establishes neither organization-wide adoption, cultural selection or retention, general effectiveness, causal superiority, nor authorization for another setting. Reopen when the setting, population, target, introduction-strategy or description status, separate WorkPlan, capability and support conditions, named authorization basis, alternative, outside result, evidence window, or maintained claim changes.

#### ME.16:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| introduction use | Receiving practice, outside result, target admitted-Method or candidate-account status, setting, population, period, qualification window, decision, and stop. |
| changed subjects | Named admitted Method, claim-bearing episteme, representation, System, capability bearer and result, Work occurrence, domain entity, organizational System, or selected structure actually claimed. |
| candidate accounts and descriptions | Candidate status, proposed claims, separately identified descriptions and representations, and missing admission basis. |
| relied-on relations | Named predicate, participant meanings, participants, applicability, obtaining basis, interval when material, and unsupported overread for every assignment, permission, authority, access, use, enactment, or other relied-on relation. |
| maintained results and receiving actions | Maintained result, particular claim or edition, status, evidence, source and window, supporting or defeating observation, receiving Agent or governing pattern when current, and next action or stop. |
| capability branch | Omit when decision-irrelevant. Otherwise retain the current A.2.2 basis for adequate existing capability without a development requirement, or return the missing capability basis. When a capability-change claim is needed, consume the compatible development result with holder, Work family, baseline, target, intervention, transfer Work, evidence and currentness; if required but missing or stale, name that development gap and next governing decision or stop. |
| introduction strategy | Admitted introduction Method or status-preserved candidate introduction account; its maintained result; a candidate description episteme before admission, or a `U.MethodDescription` only after A.3.1 admission and A.3.2 classification; any separately governed WorkPlan; intended conditions, version and window, evidence, and strategy modification kept separate from target modification. |
| introduction and later Work | Separately admitted actual Work, performers, enacted admitted Methods, history, extent, containing Systems, changed subjects, relation occurrences, results, failed entry, non-use, and gaps. |
| decision-relevant observations | Selected acceptability/rejection, appropriateness/fit, feasibility, enactment/fidelity, burden/cost, reach, sustainment, target-change, and outside-result positions, each with its own subject, claim, evidence, disposition, and next action. |
| adaptation | Target or introduction-strategy classification; what changed and which target, strategy, description, or separate WorkPlan it changed; the recorded kind and status of each affected item; when; planned/reactive status; deciding Agent and named authorization predicate; affected level; reason and conditions; maintained result; and receiving action or stop. |
| causal-use branch | `no`: observation or association with no causal reliance; or `yes`: C.28 question, supported use, unsupported stronger use, conditions, validity threat, residual uncertainty, and reopen trigger. |
| return | `keep`, `revise`, `branch`, `replace`, `stop`, or retained set; particular maintained claim or edition affected; local decision, named receiver, or stop; decision-changing next observation; bounded non-use and reopen condition. |

#### ME.16:4.3 - What Changes in Practice

Teams stop reporting that a Method was “rolled out” and start distinguishing the Method-related target, the introduction strategy and its status, its description, any separate WorkPlan, performed introduction Work, later Work, named relied-on relations, and separate observations. An introduction attempt can be completed without establishing the intended conditions. A favourable outside result can remain useful without filling every observation position or becoming causal proof.

Revision becomes local. A stale target description, unsuitable target variant, failed support relation, missing capability result, weak introduction strategy, stale strategy description, unworkable WorkPlan, or local-use adaptation can be reconsidered through its own maintained claim or edition without repeating or rejecting the entire programme.

#### ME.16:4.4 - Minimal Constructed Introduction Replay

`Calibration-Team-B` wants to reduce mixed-unit release escapes. It selects admitted target Method `M-Unit-Review-1` from ME.15 for a D30–D60 bounded attempt; candidate target `C-M-Unit-Review-Approx-1` remains outside. The changed target subjects are MethodDescription edition 4, its repaired representation, verified conversion-table System `ConversionTable-B`, and the assigned pre-release review Work. Separate claim-bearing results state the intended local selection and support conditions. No new organizational System or selected structure is inferred from the team label.

The introduction strategy is separately admitted Method `M-Introduce-Unit-Review-1`: configure the description and representation, establish and check table access, brief the reviewer on the changed distinctions, and observe one review. `MethodDescription-Intro-B-1` has that admitted Method as its one `EntityOfConcern`, and A.3.2 classifies it as a `U.MethodDescription`; `WorkPlan-Intro-B-1` separately schedules this bounded use. Neither episteme is the target Method or the later review Work.

`CDI-R22-1` names holder `Reviewer-22`, calibration-report-review Work, the mixed-unit report envelope, baseline detection results, target four-of-four seeded unit cases, supervised practice and representative transfer Work, qualification evidence, and currentness through D60. ME.16 consumes this result; it neither treats attendance as capability nor performs the development.

`MethodEngineer-B` is independently admitted as an Agent for local Method-configuration Work. Assignment occurrence `ASG-Intro-B-1(MethodEngineer-B, W-Intro-B-1)` covers only D30–D60. Permission occurrence `PERM-Intro-B-1(MethodEngineer-B, configure, MethodDescription-4, Representation-4, ConversionTable-B)` permits the three named configuration actions. Release authority remains with `ReleaseDecider-B`; neither assignment nor permission transfers it to the reviewer, engineer, or tool.

Authorized `W-Intro-B-1` is admitted as Work performed by `MethodEngineer-B` inside containing System `Calibration-Team-B`; it enacts `M-Introduce-Unit-Review-1`, configures the selected target description and representation, establishes access to `ConversionTable-B`, briefs the reviewer, and records the assignment and authority boundary. The Work is intended to establish those local conditions. If access configuration fails, the introduction Work still occurred but the support condition did not obtain. If the briefing or sequence proves unusable while the target Method remains adequate, the affected result belongs to `M-Introduce-Unit-Review-1`, `MethodDescription-Intro-B-1`, or `WorkPlan-Intro-B-1`, not to `M-Unit-Review-1`.

Later `W-B-Review-1` is independently admitted as Work performed by `Reviewer-22`; it enacts `M-Unit-Review-1`, detects a seeded Celsius/Kelvin mismatch, stops the release recommendation, and records fourteen minutes and one lookup. The observation positions remain separate: the reviewer accepts the local use; appropriateness is supported only for the named report family; table access and completion show bounded feasibility; the recorded operations support enactment for this Work occurrence; fourteen minutes and one lookup are burden observations; reach is one holder and one Work occurrence; sustainment is unknown; and one corrected report is the outside result. No adaptation occurred in this replay.

Return `keep` for the D30–D60 attempt because the intended local conditions and later Work are observed, not because the target or introduction Method is claimed to have caused the avoided release. `causalUse=no`: keep the mismatch detection and corrected report as observations with residual association and stop causal reliance. A later claim that either Method caused fewer release escapes must open C.28.

If table access failed, return the contradicted ME.10 support claim and next support action. If the introduction sequence or briefing failed, return the observation to the maintained claim in `M-Introduce-Unit-Review-1`, `MethodDescription-Intro-B-1`, or `WorkPlan-Intro-B-1` and keep the target result separate. If `CDI-R22-1` expired, name that result and stop pending its governing development decision; if later Work changed reusable target or introduction semantics, reopen ME.15 for the affected Method.

In a separate constructed no-development case, the same admitted review Method is introduced to `Reviewer-23` by repairing the conversion-table lookup path. The current `A.2.2` basis `CAP-R23-1` identifies that holder, calibration-report-review Work, the mixed-unit envelope, the required detection measure, representative evidence, and a qualification window covering the attempt. It supports adequate existing capability; no capability change is required or claimed. The engineer repairs and checks the lookup path under separately supported configuration permission, and the independently admitted later review Work uses it successfully. Return `keep` for this bounded support change and preserve `CAP-R23-1` as a reliance condition. No CDI result is missing merely because none was supplied, and no training is commissioned. If the capability basis later expires, return its currentness question to `A.2.2`; if the Work envelope instead changes so that development is needed, open that separately governed question. This case changes neither the reliance on `CDI-R22-1` nor its expiry stop in the preceding case.

### ME.16:5 - Archetypal Grounding - Workplace Introduction and Revision

The SSFD programme reports a three-year intervention involving more than 300 engineers, training followed by supported four-to-six-month workplace projects, expert assistance, 72 reports recording SSFD use, and 41 reports supporting deeper analysis. Use this account to distinguish the target, strategy, performed Work, observations, adaptations, and outside results; it is not evidence from an isolated causal experiment.

Treat training followed by supported four-to-six-month workplace projects and expert assistance as a source-described candidate introduction strategy unless independent A.3.1 admission is available. Keep that candidate introduction account, its available description epistemes and separate plans, the SSFD target Method or candidate account, capability evidence, project Systems, performed Work, later reports, named assignment or use relations, target adaptations, strategy adaptations, burdens, and domain results separate.

Before admission, none of the candidate-strategy descriptions is a `U.MethodDescription` or an ME.8 return; observations return to the candidate account, another named episteme, or a local stop.

Record acceptability or rejection, appropriateness or fit, feasibility, enactment or fidelity, burden or cost, reach, and sustainment only where the source supports each position. The reports do not admit the candidate introduction Method or make every modification a target-Method change. The bounded ME.16 decision can use observations or association without C.28; any claim that SSFD or its introduction strategy caused the reported benefits needs a current C.28 result.

The Digital Vaccine case supplies three sequential action-research cycles in an operating health-services ecosystem. For each cycle, record the Method-related target, the introduction strategy and its status, its separately identified description, and any separate WorkPlan. Then record prioritization, performed introduction or validation Work, observation, target adaptation, strategy adaptation, and revision for the bounded concern. The evaluation remains ex ante and case-specific and establishes neither Method admission, long-term effect, nor transfer to the other elicited domains.

The Halogen and methodology-spread studies add observed adaptation, project demands, practitioner skills, identified organizational conditions where recoverable, drivers, and barriers. For each adaptation record whether it changed the Method-related target, the introduction strategy, its description, a separate WorkPlan, support, or local use, while preserving the recorded kind and status of each. Also record when, planned or reactive status, deciding Agent and authorization basis, affected level, reason, and conditions. Neither source proves a universal sequence or one causal driver of spread.

Implementation-science comparators sharpen this account without supplying its domain ontology. Proctor et al. motivate separate acceptability, appropriateness, feasibility, enactment/fidelity, burden/cost, reach, and sustainment questions. FRAME motivates recording changes to the Method-related target. FRAME-IS supplies the separate question of what changed in the introduction strategy itself. Updated CFIR motivates context and determinant questions; the 2021 MRC framework motivates iterative refinement around key uncertainty and decision usefulness. ME.16 retains the target-versus-strategy distinction while rejecting health-specific entities, a maturity ladder, phase gate, compulsory adoption sequence, and any inference from those taxonomies to FPF Method admission, Work, relation, capability, authority, or culture.

#### ME.16:5.1 - APP-ME-01 Early Stop

The EC-417 three-release statement remains a WorkPlan. Do not report introduction, release enactment, later revision, cadence effect, or receiving result until the introduction strategy is identified and actual introduction Work and release Work are admitted with performers, enacted admitted constituent Methods, capability inputs, Systems, named Agent-performed Work occurrences, relation occurrences, assignments, permissions, authority, conditions, target and strategy adaptations, burdens, deviations, and domain results.

The ME.10 support-use task observations may supply identified support baselines and gaps. They do not establish an introduction Method, release Work, AI-provider use, feedback Work, capability, or Method fit. Preserve `C-EC-Release-v2` as a target candidate and `CUR-EC417-CadenceEffect-1` as unsupported. The application has no supplied `A.2.2` capability basis, so a receiving decision that relies on capability returns that missing basis first. If a current adequate basis is supplied and no capability change is needed, retain it without requiring development. Name `E.23.CDI` or a domain development result and next action only for an actually needed capability change; do not invent capability or prescribe development from the gap alone.

### ME.16:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| rollout-compression bias | Target subjects, introduction strategy, descriptions, plans, relations, Work, and observations become one “introduction”. | Keep the typed target account, strategy and its status, description, any separate WorkPlan, performed Work, named direct relations, and observations distinct. |
| success-presupposition bias | Completed introduction Work is said to make the Method available and usable. | State the intended conditions; later observations may return success, failure, uncertainty, or missing evidence. |
| training-as-capability bias | Attendance or expert help becomes a holder capability. | Recover the A.2.2 capability basis and currentness. A capability-change claim additionally needs its compatible development result; preserve adequate existing capability without inventing a development need. |
| availability-as-use bias | Published material or a configured tool becomes later enactment. | Admit actual Work and the named `enactsMethod` or use relation independently. |
| authorization compression | Expertise, sponsorship, project position, ownership, assignment, permission, and authority become interchangeable. | Name the predicate, participants, scope, and positive basis for each relied-on relation. |
| outside-result attribution bias | A favourable domain result fills every observation position and becomes causal proof. | Compare each selected position; use C.28 only when the decision relies on causality. |
| adaptation-smearing bias | A local workaround silently changes the target, introduction strategy, descriptions, WorkPlan, support, and fit together. | Classify the modification as target or introduction-strategy change and return only the maintained account, description, WorkPlan claim, support claim, fit claim, or local decision actually affected. |
| lifecycle bias | Introduction, reach, and later use become compulsory adoption stages. | Keep ME.16 independently enterable and use ME.17 only for a bounded population-level cultural question. |

### ME.16:7 - Conformance Checklist

- [ ] Target subjects; either the admitted introduction Method with an A.3.2-classified MethodDescription or the candidate introduction account with its description episteme; a separately governed WorkPlan; performed Work; and named relied-on relations are separated by kind. No pre-admission description is classified as `U.MethodDescription`.
- [ ] Every organizational claim names the organizational System, selected structure, constituent organization, or relation organization actually relied on.
- [ ] Every observation position names its maintained result and particular claim or edition, receiving Agent or governing pattern when current, and next action or stop.
- [ ] Introduction Work is stated as an authorized attempt intended to establish named conditions; a failed attempt is recordable without contradiction.
- [ ] Decision-relevant capability keeps its A.2.2 basis and currentness, or returns the missing basis. Adequate existing capability without a needed change requires no development result. Only a needed capability-change claim consumes a compatible development result or returns its missing/stale basis with a next governing action or stop; irrelevant capability detail is omitted.
- [ ] Assignment, permission, authority, access, use, enactment, and other relations name predicates, participants, scope, and obtaining basis.
- [ ] Later Work is independently admitted; candidate accounts are not enacted, and only independently admitted Methods may fill an enactment claim.
- [ ] Decision-relevant acceptability/rejection, appropriateness/fit, feasibility, enactment/fidelity, burden/cost, reach, sustainment, target-change, and outside-result observations remain separate.
- [ ] Every adaptation distinguishes target change from introduction-strategy change and records the affected target, strategy and status, identified description episteme, separate WorkPlan, support or local-use condition; time and planned/reactive status; deciding Agent and authorization; level, reason and conditions; maintained result; and receiving action or stop.
- [ ] The causal-use question is explicit: `no` stops at observation or association; `yes` uses C.28 and preserves supported and unsupported uses, validity threat, and residual uncertainty.
- [ ] ME.13 receives a bounded fit or transfer question, ME.17 a bounded population-level cultural question, and ME.15/ME.10/A.15.2 only an observation contradicting one particular maintained claim or edition. ME.8 receives such an observation only for an A.3.2-classified `U.MethodDescription` about an A.3.1-admitted Method; pre-admission content returns to its candidate account, another named episteme, or a local stop.
- [ ] The result claims no adoption lifecycle, maturity ladder, phase gate, general effectiveness, causal superiority, or authority outside its boundary.

### ME.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “We trained everyone and rolled out the Method.” | Name the actual training or development result, introduction Work, later Work, and every unobserved position. |
| “The tool was available, so the Method was used.” | Recover actual performer Work, enacted Method, direct tool-use relation, and result. |
| “Management sponsored it, so the team was authorized.” | Recover assignment, permission or authority, Agent basis, and scope separately. |
| “Results improved after launch, so the Method caused them.” | State timing, alternatives, covarying changes, contribution basis, and residual uncertainty. |
| “Several projects used it, so the culture adopted it.” | Use ME.17 only when a named cultural relation and population evidence exist. |

### ME.16:9 - Consequences

Method introductions become observable interventions. Teams can learn from use, non-use, adaptation, and outside consequences while keeping the target, introduction strategy and its status, description, any separate WorkPlan, support, capability, authority, identified organizational Systems or selected structures, Work, and domain changes distinct.

The cost is a more explicit baseline and observation design. Some programmes end with bounded association and residual causal uncertainty, and a capability gap can stop introduction even when training was delivered.

### ME.16:10 - Rationale

An intervention can change several subjects, relations, and descriptions at once. Learning requires each claimed change to retain its own subject, governor, baseline, evidence, and receiving use. Otherwise the intervention label becomes a substitute for both Work and explanation.

Separating the Method-related target from the introduction strategy, its status and description, any separate WorkPlan, capability development, and cultural continuation prevents ME.16 from becoming an adoption lifecycle. It remains the practice for introducing one bounded Method-related change, observing later Work and consequences, and revising the particular maintained claim or edition defeated by evidence.

### ME.16:11 - SoTA-Echoing

| Source | Disposition and contribution | Transfer limit and practitioner implication |
| --- | --- | --- |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | **Adopt:** training, expert assistance, four-to-six-month workplace projects, later report analysis, application variety, limitations, and direct/indirect contribution as separate introduction and observation positions. | One automotive OEM, retrospective reports, and SSFD within a broader methodology establish neither isolated causality nor universal transfer or capability. |
| Tsai, Zdravkovic, and Söder, [DBE-design Method action research](https://doi.org/10.1007/s10270-022-01068-z) | **Adapt:** prioritization followed by three plan-perform-evaluate cycles as a naturalistic revision structure. | The evaluation is ex ante and case-specific and does not establish long-term organizational effect, causal superiority, or transfer. |
| Schønheyder and Nordby, [design-Method use and evolution in professional practice](https://doi.org/10.1016/j.destud.2018.04.001), and Hiort af Ornäs et al., [drivers and barriers in methodology spread](https://www.designsociety.org/publication/36298/the_spread_of_product_development_methodology_exploring_drivers_and_barriers_in_swedish_industry) | **Adapt:** observed modifications, project and skill conditions, identified organizational conditions where recoverable, drivers, and barriers as observation and revision questions. | One firm and one interview study supply neither a universal programme nor causal proof of spread. |
| Proctor et al., [Outcomes for Implementation Research](https://doi.org/10.1007/s10488-010-0319-7) | **Adapt:** keep acceptability/rejection, appropriateness/fit, feasibility, enactment/fidelity, burden/cost, reach, and sustainment as decision-relevant observation positions distinct from the outside result. | **Reject:** health-service/client ontology, adoption as an FPF cultural fact, a compulsory outcome set, and any automatic stage order. Use only positions that can change the bounded decision. |
| Stirman, Baumann, and Miller, [FRAME](https://doi.org/10.1186/s13012-019-0898-y) | **Adapt:** for a Method-related target, record what changed, when, planned/proactive or unplanned/reactive status, decider and authority, affected level, reason and conditions, and whether Method semantics, description, support, or local use changed. | **Reject:** fidelity labels as Method identity or admission, and do not import healthcare intervention kinds. Return each target modification to its particular maintained claim or local decision. |
| Miller et al., [FRAME-IS](https://doi.org/10.1186/s13012-021-01105-3) | **Adapt:** distinguish modifications to the introduction strategy from modifications to the Method-related target; for the strategy, record the changed component or function, nature, timing, participants in the modification decision, rationale, and scope. | **Reject:** healthcare intervention and implementation-strategy ontology, automatic Method admission, and a compulsory reporting module. Record the introduction strategy's status and keep its description, any WorkPlan, performed Work, and affected maintained result separate. |
| Damschroder et al., [updated CFIR](https://doi.org/10.1186/s13012-022-01245-0) | **Adapt:** ask which context and determinant observations can explain anticipated or actual success or failure. | **Reject:** a universal determinant inventory, success score, maturity ladder, or inference from a determinant label to an obtaining FPF relation. |
| Skivington et al., [2021 MRC complex-intervention framework](https://doi.org/10.1136/bmj.n2061) | **Adapt:** identify key uncertainty, context interaction, refinement, stakeholder perspective, and comparative resource/outcome consequence; permit repeat, reconsider, or stop. | **Reject:** a compulsory phase sequence or gate. The source neither admits FPF Methods and Work nor supplies causal support; C.28 remains conditional. |
| Current FPF `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `A.13`, `A.2.2`, `E.23.CDI`, `A.3.4`, `A.10`, `C.28`, and direct relation governors | **Adopt:** Method admission, MethodDescription identity, WorkPlan identity, Work admission, Agent basis, capability, capability development, bounded transformation, evidence, causal-use boundary, and relation semantics. | ME.16 contributes the typed attempt, later observations, target-versus-strategy adaptation record, conditional causal branch, and local revision decision; it does not redefine those governors. |

Reopen the pattern when practitioners cannot separate target subjects and accounts, introduction strategy and status, description, any separate WorkPlan, performed Work, relation occurrences, observations, and receiving actions; when stronger cross-domain evidence changes the observation or adaptation positions; when repeated introductions reveal an independent organizational-change problem; or when current FPF Method, description, plan, Work, relation, capability, evidence, or causal-use semantics change the action.

### ME.16:12 - Relations

- ME.1 supplies the Method-of-interest and outside result. ME.15 supplies an admitted variant or status-preserved candidate lineage with applicability and currentness. A candidate account is not enacted; later Work may enact only independently admitted constituent Methods.
- ME.15 governs admitted Method semantics and candidate lineage, provenance, evidence, applicability, currentness, and retirement claims for both target and introduction accounts. ME.8 governs only an A.3.2-classified `U.MethodDescription` whose one `EntityOfConcern` is an A.3.1-admitted Method; pre-admission description content remains in its candidate account, another named episteme, or a local stop. A.15.2 governs the separate introduction WorkPlan; ME.10 particular support claims; ME.13 bounded fit and transfer questions; and ME.17 bounded population-level cultural questions. Return an observation only with the contradicted admissible maintained claim or edition plus the next action.
- `E.23.CDI` or a domain capability-development pattern governs capability change. `A.2.2` governs the relied-on capability result; ME.16 records it as an input, observation, or named gap.
- `A.3.1` governs admission of both target and introduction Methods, and `A.3.2` governs `U.MethodDescription` membership. A WorkPlan and performed Work neither admit nor enact a candidate Method. `A.13` governs precise Agent claims and `A.15.1` every introduction and later Work occurrence. Assignment, permission, authority, access, use, enactment, and other direct relations retain their own named predicates, participants, applicability, and obtaining tests.
- `A.3.4` governs a claimed actual bounded change to a continuing subject. Introduction Work, a before/after account, an adaptation record, or a decision label does not by itself identify a `U.Transformation`.
- `A.10` governs evidence use. When the ME.16 decision relies on a causal or contribution claim, `C.28` governs the bounded causal-use question, supported and unsupported uses, conditions, validity threats, and reopen trigger. Without that reliance, ME.16 stops at observation or association.
- Proctor, FRAME, FRAME-IS, updated CFIR, and MRC supply bounded comparator questions only. FRAME and FRAME-IS support the target-versus-introduction-strategy distinction; none creates FPF health ontology, adoption lifecycle, maturity ladder, phase gate, Method admission, Work occurrence, relation occurrence, capability, authority, or culture claim.

### ME.16:End

## ME.17 - Deliberately Continue and Change Method-Engineering Culture

>
> **Primary working result:** a bounded cultural account that retains the admitted-Method or status-preserved candidate/observed-practice branch. It names one testable generation, transmission, recognition, selection, memory, retention, or loss predicate with participants and applicability. It distinguishes the claim about that cultural relation, the episteme stating the claim, the evidence, and the observations at named intervals. It identifies participating subjects and a named authorization predicate, and records at least two serious development hypotheses, one discriminating observation, separate consequences, and a `continue`, `revise`, `branch`, `replace`, `stop`, or `unknown` decision.

### ME.17:0 - Use This When

Use this pattern when a group intends to continue or change how a bounded population generates, transmits, recognizes, selects, remembers, retains, or loses Method Engineering practice—not merely improve one Method, publish an edition, teach one person, or change one project choice. Begin with one value and one testable cultural predicate: what is said to be transmitted, selected, remembered, or otherwise changed; which participant meanings and applicability condition make that claim testable; and what positive and discriminating negative cases are possible?

For a first pass, say in ordinary language what is being passed, selected, remembered, or lost; by whom and for whom; which identified card, rule, Work occurrence, System, or direct relation may matter; two plausible explanations; and which next observation would distinguish them. If that already supports `continue`, `revise`, `branch`, `replace`, `stop`, or `unknown`, stop. Add predicate, claim-episteme, occurrence-identity, structure, or architecture apparatus only when a later decision must rely on it.

The first useful result is a cultural-intervention row. It names the C.20-recognized Discipline or smaller unresolved practice boundary. For the subject, it uses either an admitted Method Engineering Method with an independently grounded A.15.1 `enactsMethod` occurrence, or a status-preserved candidate lineage or source-described observed practice without claiming Method admission or enactment. The row records one testable cultural predicate and named participants, the lightest truthful A.6.RCD disposition, and separate claim, evidence and named-interval observations. It identifies participating cards, descriptions, publications, Systems, teaching or tutoring Work, rules, fields, forums, assignments, permissions, or authority relations. It records two rival hypotheses and a distinguishing observation, bounded authorization, separate consequences, gaps, and the next decision.

Here *culture* is Plain practice wording for bounded claims about how a population generates, transmits, recognizes, selects, remembers, retains, changes, or loses practice. A school label, framework edition, repository, training event, local Method choice, repeated task, or institutional publication does not establish those claims together.

Do not use this pattern for a bounded introduction whose primary result is target changes, later Method use, and outside consequences; use ME.16. Do not infer cultural adoption, retention, relation occurrence identity, selected structure, architecture, or authority from attendance, publication, tool access, one successful project, an organization label, or a stated preference.

### ME.17:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| Method Engineering Discipline boundary | A C.20-recognized Discipline when that result exists; otherwise a named bounded practice, collective, or population under C.36 with the Discipline claim unresolved. | A field name, school label, package, organization, or edition does not establish a Discipline. |
| admitted-Method branch | One independently A.3.1-admitted Method Engineering Method or variant plus a particular dated Work occurrence for which the A.15.1 `enactsMethod` predicate obtains. | Presence, teaching, a candidate account, or a source label establishes neither Method admission nor enactment. |
| candidate or observed-practice branch | A status-preserved candidate lineage or source-described observed practice, its candidate account or source claim, honestly named card, template, description episteme, or other claim-bearing material, and independently supported Work facts. A claim-bearing item is a `U.MethodDescription` only when one A.3.1-admitted Method is its `EntityOfConcern` and A.3.2 classifies the episteme. | This branch makes no Method or enactment claim until A.3.1 and A.15.1 independently succeed; candidate or source material does not return to ME.8 merely because Work used it. |
| bounded population | Identified transmitting, receiving, recognizing, selecting, remembering, retaining, generating, or losing participants for the named predicate, place, and period. | “The organization”, “the community”, or “users” is insufficient without participant meanings and a boundary. |
| cultural predicate and disposition | The transmitted, selected, recognized, remembered, retained, generated, or lost value; participant meanings; applicability; positive test; discriminating negative or failed case; and the lightest truthful A.6.RCD result. | A convenient relation label does not create a direct relation kind or obtaining occurrence. |
| claim, evidence, and occurrence | The world-side direct relation or bounded relation-bearing claim; a separate claim episteme; evidence and reliance; and observations at named intervals. Use A.6.REL occurrence identity only when later work must distinguish occurrences. | A claim episteme, identifier, evidence item, or later report neither creates nor reidentifies a world-side occurrence. |
| participating subjects | Identified cards, descriptions with their recorded kind and status, publication occurrences, repositories or other Systems, teaching/tutoring/event Work, decision-rule epistemes, fields, forums, assignments, permissions, authority, and other direct relations actually relied on. | A bundle word does not establish selected structure; A.22 applies only to one selected organization whose constituents and obtaining relations change the decision, and C.30 only to a current architecture question. |
| bounded authorization | One named assignment, permission, or authority predicate with Agent, action or changed subject, scope, and positive basis that permits the intervention. | Ownership, project position, assignment, permission, authority, and expertise are not interchangeable. |
| development hypotheses and probe | At least two non-equivalent explanations of how the cultural predicate may obtain or fail, their testable consequences, and one proportionate next observation that can change the five-way decision. | A chosen carrier change and later activity do not discriminate explanations; preserve `unknown` when the probe cannot. |
| practitioner or constructed-Method consequence | A separately observed change in practitioner Work, understanding, burden, result, or a constructed Method. | It is not the cultural claim and does not prove that claim caused the consequence. |

### ME.17:1 - Problem Frame

Method Engineering culture is easy to claim from visible carriers. A specification has editions, a card set is taught, a Method is placed in a checklist, or a community uses a shared label. These facts may support generation, institutional selection, publication, memory, local use, or a candidate transmission claim, but they do not all support the same predicate, population, occurrence, or history.

Deliberate change is harder. An authorized team may change its own cards or rules, yet have no authority over a field or individual practitioners. Later participants may perform Work with those subjects without demonstrating long-term recognition or retention. A useful intervention must therefore derive one testable cultural claim, separate its episteme and evidence, compare named intervals without assuming occurrence continuity, distinguish serious explanations, and select one informative next change or observation.

### ME.17:2 - Problem

Training is called adoption. Publication is called institutional memory and practitioner retention at once. A mandatory field is called Method enactment. Individual card selection is reported as population cultural selection. Several cases, organizations, and time periods are combined into one diffusion story. Authorization to edit project material becomes authority over the practice.

These compressions make cultural claims impossible to falsify. The team cannot tell which relation changed, whether the intended population received or selected anything, what consequence followed, who was authorized to intervene, or what evidence would justify continuation.

### ME.17:3 - Forces

| Force | Tension |
| --- | --- |
| Cultural continuity | Practice needs carriers and memory, while preserved artifacts can outlive actual use and recognition. |
| Deliberate intervention | A team can change identified cards, descriptions, rules, Systems, Work occurrences, or direct relations within authorization, while it rarely controls the whole population or field. |
| Relation specificity | Generation, transmission, recognition, selection, retention, memory, and loss interact, while each needs different participants and evidence. |
| Local Work | Individual choices and enactments are observable, while they do not automatically aggregate into a cultural relation. |
| Time | Transmission can be observed quickly, while retention and loss require later intervals. |
| Consequences | Cultural change should matter to practitioners or constructed Methods, while consequence and causal relation remain separate. |
| Case variety | Institutional, organizational, and project cases illuminate different relations, while joining their histories invents a population. |

### ME.17:4 - Solution

Bound the practice, choose the truthful subject-status branch, derive one testable cultural predicate, separate the world-side claim from its episteme and evidence, name the actual participating subjects and authorization, compare rival hypotheses, perform one informative bounded intervention, and compare later claims and consequences without inventing occurrence continuity or causality.

#### ME.17:4.1 - Pattern-Use Unfolding

1. **Bound the practice and Discipline claim.** Use a current C.20 result when Method Engineering is recognized as a Discipline for this use. Otherwise name the smaller practice, collective, population, place, and period under C.36 and keep the Discipline claim unresolved.
2. **Choose the subject-status branch.** For the admitted-Method branch, name an A.3.1-admitted Method Engineering Method or variant and independently ground the A.15.1 `enactsMethod` occurrence in a particular dated Work occurrence. For the candidate branch, name the status-preserved candidate lineage or source-described observed practice, its candidate account or source claim, honestly named card, template, description episteme, or other claim-bearing material, and actual Work facts. Assert no Method or enactment until their governors succeed, and no `U.MethodDescription` membership until one admitted Method is the episteme's `EntityOfConcern` and A.3.2 classifies it.
3. **Derive the cultural claim before naming a relation.** State the value said to be generated, transmitted, recognized, selected, remembered, retained, or lost; participant meanings; applicability; positive test; and a discriminating negative or failed case. If a current direct predicate states the claim, use it and stop. Otherwise use A.6.RCD for the lightest truthful local compound claim, reusable predicate definition, or relation-kind question. A label or C.36 category alone is not an obtaining relation.
4. **Separate the world claim, episteme, evidence, and intervals.** Record the direct relation or bounded relation-bearing claim, the separate claim episteme, its evidence and reliance, and observations at named intervals. Compare later claims or intervals. Open A.6.REL occurrence identity only when a later use must distinguish one obtaining occurrence from another; do not assume that repeated participants make it the same occurrence.
5. **Name every participating subject.** Identify the cards, descriptions with their recorded kind and status, publication occurrences, repositories or other Systems, teaching, tutoring or event Work, decision-rule epistemes, fields, forums, assignments, permissions, authority, and other direct relations actually relied on. Select an A.22 structure only when one organization of identified constituents, obtaining relations, constraints, and use frame changes the decision; open C.30 only for a current architecture claim.
6. **Recover authorization.** Name the change decision-making Agent, A.13 basis, assignment, permission, or authority predicate, participants, permitted change, scope, positive basis, and protected conditions. Return `missing-change-authorization` when the intended intervention exceeds it. Ownership, project position, expertise, assignment, permission, and authority do not substitute for one another.
7. **Name one intended consequence separately.** State the practitioner Work, understanding, burden, result, constructed-Method position, or other consequence expected to change. Record its subject, baseline, observation, evidence, and causal non-use separately from the cultural claim.
8. **Generate rival development hypotheses and one discriminating probe.** Keep at least two serious non-equivalent hypotheses about how the predicate may obtain or fail, with testable consequences, using B.5/B.5.2 when a durable abductive result is needed. Name one proportionate observation that can change `continue`, `revise`, `branch`, `replace`, or `stop`; return `unknown` when it cannot discriminate. Use A.3.3 only for a real state-space and transition-law claim, C.27 for an interval or persistence claim, C.28 only when the decision relies on causality, A.15.7 for the next action during ongoing Work, and C.11 only after a chooser and OptionSet exist.
9. **Compare bounded alternatives and select an informative intervention.** Include retaining current subjects, changing one named subject or direct relation, branching for part of the population, replacing the current means, and stopping or reverting when material. Preserve burdens, exclusion risks, authorization, reversibility, and evidence gaps. State why the selected intervention and observation discriminate the live hypotheses.
10. **Perform the authorized change.** Admit the intervention Work, performers, enacted admitted Method, action history, temporal extent, containing System, changed subjects, used Systems, named direct relations, and result. A plan or published edition does not establish Work or a transformation.
11. **Observe later claims and consequences separately.** At a named later interval, apply the same predicate definition to the stated participants or a deliberately changed population and record positive, negative, inapplicable, unknown, or missing-information. Keep later Work, non-use, burden, adaptation, rejection, and consequences separate. A favourable consequence establishes neither the cultural predicate nor causality.
12. **Record other cultural claims only when independently supported.** Generation, recognition, selection, memory, retention, loss, or transmission beyond the primary predicate needs its own value, participant meanings, applicability, test, evidence, interval, and truthful disposition. Return the rest as gaps rather than a cultural-maturity score.
13. **Decide, return observations, and refresh.** Return `continue`, `revise`, `branch`, `replace`, `stop`, a retained set, or `unknown`, with the hypothesis-discriminating next observation. Return an observation to ME.15 or ME.10 only when it contradicts one particular maintained claim or edition. ME.8 receives an observation only when one admitted Method is the episteme's `EntityOfConcern` and A.3.2 classifies it as a `U.MethodDescription`; candidate or source material returns to its candidate account, source claim, another named episteme, or a local stop. State authorization and population limits, unresolved predicates, causal uncertainty, and reopen conditions for changed subject status, predicate, population, interval, evidence, hypothesis, or consequence.

#### ME.17:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| practice boundary | C.20 Discipline result or bounded practice/population under C.36, unresolved claim, place, period, and qualification window. |
| subject-status branch | Admitted Method Engineering Method plus independently grounded `enactsMethod` Work occurrence; or candidate lineage/source-described observed practice plus its honestly named claim-bearing materials and Work facts with no Method or enactment inflation; description kind, status, maintained result, and missing admission or classification basis. |
| cultural predicate | Value, participant meanings, participants, applicability, positive test, discriminating negative or failed case, and lightest truthful A.6.RCD disposition. |
| claim, evidence, and interval observations | World-side relation or bounded claim; separate claim episteme; evidence and reliance; named intervals; later positive, negative, inapplicable, unknown, or missing-information result; A.6.REL occurrence identity only when consumed. |
| participating subjects | Identified cards, descriptions with their recorded kind and status, publications, Systems, teaching/tutoring/event Work, rules, fields, forums, assignments, permissions, authority, and other direct relations; conditional A.22 structure or C.30 architecture only when independently established. |
| authorization | Change Agent and A.13 basis, named assignment, permission, or authority predicate and participants, permitted change, scope, positive basis, and protected conditions. |
| intended consequence | Practitioner or constructed-Method subject, baseline, expected change, observation, evidence, and causal non-use. |
| hypotheses and probe | At least two serious hypotheses, testable consequences, one decision-changing observation, selected intervention, and why it discriminates; `unknown` when it does not. |
| performed change | Admitted intervention Work, performers, enacted admitted Method, history, extent, containing System, changed subjects, used Systems, named direct relations, and result. |
| separate consequences | Practitioner and constructed-Method observations, non-use, burden, adaptation, rejection, contribution reach, causal uncertainty, and missing evidence. |
| return | `continue`, `revise`, `branch`, `replace`, `stop`, retained set, or `unknown`; particular maintained claim or edition returned when contradicted; ME.8 only for a qualifying `U.MethodDescription`, and candidate/source material to its own account, claim, named episteme, or local stop; population and authorization limits; next discriminating observation and reopen conditions. |

#### ME.17:4.3 - What Changes in Practice

Teams stop calling every publication, teaching session, mandated field, or repeated use “culture”. They can identify one testable cultural predicate and value, use an admitted-Method or candidate branch without laundering status, and separate the world claim from its episteme, evidence, intervals, participating subjects, and consequences.

Interventions become smaller and more informative. Rival explanations remain visible, one next observation can change the bounded decision, and `unknown` survives when evidence cannot discriminate. A project can improve a bounded transmission claim without asserting retention, selection, occurrence continuity, or causality.

#### ME.17:4.4 - Minimal Constructed Transmission Replay

`Calibration-Method-Engineering-Practice-B` is a bounded project practice; no C.20 Discipline recognition is claimed. Admitted Method Engineering Method `M-ME-One-Defect-One-Result-1` says: for each trial finding, identify the changed object, separately governed maintained result, particular contradicted claim or edition, and next maintenance or stop action, then rerun the relevant check. Two method engineers and four calibration reviewers are independently admitted under A.13 for the named practice-session Work family. Their dated practice-session Work independently satisfies A.15.1 `enactsMethod` for this admitted Method; the card and teaching event do not.

The value under test is that four-part defect-disposition rule. Local compound predicate `CAL-TransmissionPredicate-1` applies from method engineers as transmitting participants to one reviewer as receiving participant during D30–D60 when the reviewer later applies the rule correctly to both seeded defects without a transmitter choosing the maintained result. A positive case is an independently admitted review-practice Work occurrence meeting that test. A discriminating negative is a completed occurrence that merges two separately governed results or cannot name the next action. A.6.RCD stops at this local compound claim; no reusable predicate definition or relation kind is admitted. The claim episteme records each reviewer result and evidence; no later use needs relation-occurrence identity under A.6.REL.

The participating subjects remain separately identified: one-page card `CAL-Decision-Card-1`; two paired teaching Work occurrences; coached-practice Work; two seeded-finding epistemes; and each reviewer's later Work. The card has admitted Method `M-ME-One-Defect-One-Result-1` as its one `EntityOfConcern`, and A.3.2 classifies it as a `U.MethodDescription`. Permission `PERM-CAL-CARD-EDIT-1(ME-Agent-B1, ME-Agent-B2, edit, CAL-Decision-Card-1)` permits the two engineers to edit that project card. Assignment `ASG-CAL-TEACH-1` assigns the paired sessions. Neither predicate authorizes changing the wider field or a reviewer's later Method choice.

Two hypotheses remain live. `H-CAL-1` says the explicit description-versus-representation contrast on the card is sufficient for the bounded positive cases; it predicts correct handling of a new equivalent defect without coaching. `H-CAL-2` says coached feedback supplies the decisive discrimination and the card alone is insufficient; it predicts errors or requests for help in the uncoached case. Current results—three positive cases and one negative merger—do not discriminate them. The selected intervention is to revise only the worked contrast and then give every reviewer one equivalent uncoached case before further coaching; this is informative because the result separates card legibility from immediate coaching dependence. No causal conclusion is used; if the team later relies on either hypothesis as causal, it must open C.28.

Return `revise`: retain the bounded positive claims for three reviewers, preserve the fourth as a negative case, and keep the population-wide transmission claim `unknown`. Record each review occurrence as Work and each correct disposition as a separate practitioner consequence. The next observation is the uncoached equivalent case. This result establishes neither long-term retention, cultural selection, causal superiority, occurrence continuity, nor transfer to another plant.

### ME.17:5 - Archetypal Grounding - MeCaMinD Transmission

The MeCaMinD record enters through the candidate/observed-practice branch. The source describes movement-design practices and later facilitation Work but does not establish A.3.1 Method admission or an A.15.1 enactment occurrence for a candidate whole. The value under test is the novices' recoverable way of using selected movement-design cards to prepare and run a 45-minute session. The transmitting participants are the core team and teachers; the receiving participants are five novice facilitators; the interval covers card development through the August 2023 school.

Local compound predicate `MEC-TransmissionPredicate-1` is positive for one novice only when, under the named observed conditions, their later admitted facilitation Work contains a recoverable session plan and performed session using the candidate practice; the discriminating negative is carrier access followed by an unusable plan or inability to perform the session. A.6.RCD stops at this bounded claim, and no relation kind or occurrence identity is admitted.

Keep the participating subjects separate: candidate card content, card layout, reduced card set, Game Board System, prior self-study Work used by most novices, teaching Work, tutoring Work, novice background, later facilitation Work, and each local tailoring decision. The project-designers' reported position supports a bounded historical account of changes to project cards and the Game Board, not a recovered assignment, permission, or authority predicate for another intervention and not authority over the wider field or novice choices. The adaptation record says that after trials the core team changed content and layout, reduced the set, and added the Game Board; the source supports project-level decisions and reasons related to overload and use, but does not establish that reusable Method semantics changed.

Two hypotheses remain live. `H-MEC-1` says revised cards and the Game Board make the candidate practice recoverable before tutoring; it predicts a usable session plan after self-study and carrier access. `H-MEC-2` says teaching, tutoring, background, and local tailoring supply indispensable support; it predicts weak or incomplete plans before those Work occurrences even with the same cards and board. The reported later facilitation Work is a positive bounded observation, while information overload and reliance on the Game Board are discriminating negatives against a card-only claim.

Return `branch`: retain the reported five-novice claim only for the combined observed conditions and keep card-only transmission `unknown`. The selected next intervention is to revise one card associated with information overload; the proportionate probe is an equivalent planning task after self-study and carrier access but before tutoring, repeated after tutoring while recording participant background and local tailoring. It is informative because the two hypotheses predict different pre-tutoring results. Performing that new revision stops at `missing-change-authorization` until a named permission or authority predicate and its participants are recovered. Keep the probe noncausal; a causal reliance on carrier or tutoring effects opens C.28. The case establishes neither Method admission, long-term retention, wider recognition or selection, nor adoption beyond the five facilitators.

#### ME.17:5.1 - Separate Organizational-Selection Replay

The telecom SRA record is a different population, organizational System, and history and also enters through the candidate/observed-practice branch unless independent FPF Method admission is supplied. The value under test is the requirement that feature pre-study decisions include a performed security risk assessment. The selecting participant is the named telecom organizational System, the selected value is that requirement, and the receiving loci are its bounded feature-prestudy decisions during the reported period. Local compound predicate `SRA-SelectionPredicate-1` is positive only when the current decision rule requires a named security-assessment Work result and the sampled feature decision actually designates such a result; the discriminating negative is a completed mandatory field with no recoverable assessment Work. A.6.RCD stops at this local claim, with no relation kind or occurrence identity admitted.

Distinguish the mandatory security-impact field, definition-of-done rule episteme, release checklist, SRA-forum Work and System, training Work, expert-help Work, stale source-description epistemes and templates, reorganizations, tool linkage, and appointed-guardian assignments. Candidate or source labels do not turn those materials into `U.MethodDescription`. None of these subjects alone establishes organizational selection or enactment.

Two hypotheses remain live. `H-SRA-1` says mandatory fields, definition of done, and checklist are sufficient to select the practice for feature pre-studies; it predicts completed fields backed by actual assessment Work even without forum or expert intervention. `H-SRA-2` says forum review, training, expert help, current descriptions, tool linkage, and guardian assignments are needed to turn nominal compliance into performed assessment; it predicts empty, copied, or unsupported fields where those conditions are absent. Later use and non-use in a 45-feature release, 41 respondent reports, forum use across eight projects, identified risks, requests for help, stale material, and reorganization effects supply positive and negative observations but do not isolate either hypothesis.

Return `revise` with a bounded proposal: for one release, require each mandatory field to designate the assessment Work result for that feature decision and record whether forum review, training, expert help, current material, tool linkage, and a guardian assignment were present. This probe is informative because it distinguishes nominal field completion from performed assessment and exposes which support conditions covary with positive cases. The historical source reports an implementation basis but does not state the assignment, permission, or authority predicate authorizing this new change, so performing the proposal stops at `missing-change-authorization` until that assignment, permission, or authority relation is recovered. Any causal conclusion about the added linkage or support conditions requires C.28.

Preserve the gaps: not every engineer used the practice; some found it not worthwhile; several conditions covary; no universal transfer follows. Do not join this population, predicate, source-described practice, or consequence history to MeCaMinD.

#### ME.17:5.2 - Essence Institutional Boundary

The Essence record supports bounded institutional claims only: contributor organizations generated and revised language content; OMG selected formal editions; issue-handling Work, specifications, and machine-readable material supplied publication subjects; retained formal versions and the 2.0 beta can support an institutional-memory claim when its value, participants, predicate, and interval are stated. These claims enter the candidate/observed-practice branch unless independent Method admission and enactment evidence are supplied.

The source does not establish recurring practitioner enactment, population recognition or selection in practice, long-term retention, practical superiority, improved results, or fitness for every Method family. A complete ME.17 intervention additionally needs two serious hypotheses, a change to one participating subject permitted by a named assignment, permission, or authority predicate, and a later decision-changing observation. Without those, keep the supported institutional claims and stop.

#### ME.17:5.3 - APP-ME-01 Missing Basis

EC-417 supplies no C.20 recognition, bounded Method Engineering population, admitted Method Engineering Method with actual enactment, or derived cultural predicate and evidence. Its candidate release, candidate accounts, description epistemes, support results, WorkPlan, and task observations do not establish culture. Because no admitted Method is identified as the descriptions' `EntityOfConcern`, they are not `U.MethodDescription` and do not return to ME.8. A status-preserved candidate branch may carry those identified accounts, epistemes, and Work facts, but it asserts neither Method nor enactment. Return the missing value, participants, predicate, authorization, rival hypotheses, and discriminating observation; use MeCaMinD, SRA, and Essence only for the unlike claims each source supports.

### ME.17:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| candidate-enactment bias | A source-described candidate or observed practice becomes an admitted Method and enactment occurrence. | Use the candidate branch until A.3.1 and A.15.1 independently succeed. |
| relation-label bias | “Transmission”, “selection”, or “memory” substitutes for value, participants, applicability, and obtaining predicate. | Apply A.6.RCD and state a positive plus discriminating negative case. |
| claim-as-occurrence bias | A claim episteme, identifier, or later report creates or preserves a world-side relation occurrence. | Separate claim, evidence, interval observations, and conditional A.6.REL identity. |
| carrier-bundle bias | Cards, teaching, tutoring, repository, rules, fields, and forums become one unnamed subject. | Name every actual subject and direct relation used; select a structure or architecture only when its governor applies. |
| authorization inflation | Ownership, project position, assignment, permission, authority, and expertise become interchangeable. | Name the assignment, permission, or authority predicate, participants, permitted change, scope, and positive basis. |
| single-explanation bias | A carrier change and later activity are treated as explanation and proof. | Keep at least two serious hypotheses, testable consequences, and one discriminating observation; preserve `unknown`. |
| consequence-as-relation bias | Successful practitioner Work proves every cultural claim. | Observe the named cultural predicate and the practitioner or constructed-Method consequence separately; use C.28 only for causal reliance. |
| maturity-score bias | Missing cultural claims are averaged into one adoption stage. | Return supported claims and explicit gaps without a scalar cultural verdict or lifecycle. |

### ME.17:7 - Conformance Checklist

- [ ] A C.20 Discipline result is used, or a smaller C.36 practice and population boundary is named with the Discipline claim unresolved.
- [ ] The subject branch is honest: admitted Method plus independently grounded enactment, or candidate/observed practice plus honestly named candidate accounts, source claims, cards, templates, description epistemes, and Work facts without Method, `U.MethodDescription`, or enactment inflation.
- [ ] One value, participant meanings, applicability condition, obtaining predicate, positive case, and discriminating negative or failed case are explicit.
- [ ] A.6.RCD returns the lightest truthful disposition; A.6.REL occurrence identity is opened only when later use must distinguish occurrences.
- [ ] The world-side claim, claim episteme, evidence and reliance, and named-interval observations remain separate.
- [ ] Cards, descriptions with their recorded kind and status, publications, Systems, teaching/tutoring/event Work, rules, fields, forums, assignments, permissions, authority, and other direct relations are separately identified as subjects.
- [ ] A.22 is used only for one selected structure and C.30 only for a current architecture question.
- [ ] Authorization names the assignment, permission, or authority predicate, participants, permitted change, scope, positive basis, and protected conditions.
- [ ] At least two serious hypotheses, their testable consequences, one decision-changing observation, the selected intervention, and why it is informative are present.
- [ ] C.27 is used only for a temporal adequacy claim, A.3.3 only for a transition law, C.28 only for causal reliance, A.15.7 only during ongoing Work, and C.11 only after a chooser and OptionSet exist.
- [ ] Later claims or intervals are compared without automatically reidentifying one occurrence across them.
- [ ] Practitioner or constructed-Method consequences, non-use, burden, adaptation, and rejection remain separate from the cultural predicate.
- [ ] `unknown` is retained when available observations cannot discriminate the hypotheses.
- [ ] Separate cases, populations, organizational Systems, histories, predicates, and effects are not joined.
- [ ] Any return to ME.15 or ME.10 names one particular contradicted maintained claim or edition. ME.8 receives only an episteme whose one `EntityOfConcern` is an A.3.1-admitted Method and which A.3.2 classifies as `U.MethodDescription`; candidate/source material returns to its own account, claim, another named episteme, or a local stop. Population spread alone triggers no return.

### ME.17:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The standard has stable editions, so the culture retains it.” | State the retained value, participants, applicability, predicate, interval, positive and negative cases; seek practitioner retention separately. |
| “Five novices used the cards, so the field adopted them.” | Keep the candidate/observed-practice branch, bounded claims, and local Work; leave wider recognition, selection, and retention open. |
| “The practice became mandatory, so everyone enacted a Method.” | Separate rule epistemes, organizational selection claims, training Work, individual Work and non-use, Method admission, and enactment. |
| “The project designers may change practitioner choices.” | Name the assignment, permission, or authority predicate and the project subjects it permits them to change. |
| “The later result proves our carrier change worked.” | Keep rival hypotheses and a discriminating observation; use C.28 only when a causal statement will be relied on. |
| “These cases show one adoption path.” | Keep every population, predicate, interval, intervention, and consequence separate. |

### ME.17:9 - Consequences

Accounts of cultural change identify testable relations and the evidence for them. Teams can make bounded authorized interventions and learn whether transmission, selection, memory, retention, or another named relation changed without claiming the rest.

The cost is patience and narrower conclusions. Long-term retention and loss need later observation, and visible carriers or successful local Work may still leave population-level relations unresolved.

### ME.17:10 - Rationale

Cultural continuity and change require testable predicates, not a bundle of labels. A card can participate in one transmission claim without being recognized, selected, or retained by a whole population. That claim also does not establish that the population enacts a Method described on the card; enactment concerns independently admitted Methods in actual Work. A mandatory field can participate in an organizational selection claim while training Work, later practitioner Work, Method admission, and enactment remain separate.

Separating subject status, world claim, claim episteme, evidence, interval observations, authorization, and consequence prevents candidate laundering and invented occurrence continuity. Rival hypotheses and one informative probe make deliberate change possible without fictitious authority or causality, while institutional, organizational, and project cases contribute without being merged into one history.

### ME.17:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Waern et al., [Moving with method: using cards in movement-based design](https://doi.org/10.1093/iwc/iwaf006) | Adapt separate card content and layout, reduced set, Game Board, prior self-study, teaching, tutoring, novice background, local tailoring, five-novice Work, information overload, and bounded project-change basis into rival transmission hypotheses and a discriminating probe. | The source supplies a candidate/observed-practice branch, not FPF Method admission or enactment. Five novices in one school establish neither carrier-only transmission, long-term retention, causality, wider adoption, nor authority over facilitator choices. |
| Ardi, Sandahl, and Gustafsson, [security risk assessment in a large organization](https://doi.org/10.1007/s42979-023-01968-x) | Adapt mandatory fields, definition of done, checklist, forum, training, expert help, current or stale material, reorganization, tool linkage, and guardian questions into unlike selection hypotheses and one performed-Work probe. | One enterprise and covarying changes establish neither future authorization for a named change, universal causality, transfer, Method admission, nor universal enactment. |
| `SRC-DOMAIN-CULTURAL-CONTINUATION-CASES-2001-2026` Essence record and [OMG Essence editions](https://www.omg.org/spec/Essence) | Adopt only separately stated contributor generation, institutional selection, publication, and edition-memory claims whose value, participants, predicate, and interval are recoverable. | Publication and institutional selection do not establish Method admission, practitioner enactment, recognition, retention, superiority, or broad fitness. |
| Current FPF `C.20`, `C.36`, `A.6.RCD`, `A.6.REL`, `A.3.1`, `A.3.2`, `A.13`, `A.15.1`, `B.5`, `B.5.2`, `A.10`, `C.27`, `C.28`, `A.3.3`, `A.15.7`, `C.11`, A.19, `A.22`, and `C.30` | Reuse Discipline and cultural questions, relation-claim derivation, conditional occurrence identity, Method, MethodDescription, Agent, and Work claims, abductive hypotheses, evidence, conditional temporal/causal/dynamics/steering/choice questions, non-forced selection, and conditional structure or architecture claims. | ME.17 contributes the two status branches, testable-predicate intervention boundary, hypotheses, probe, separate interval and consequence observations, and bounded continuation decision. It does not redefine or automatically activate those governors. |

Reopen the pattern when a field case supplies decision-changing evidence for another named cultural predicate, when practitioners cannot derive a testable claim or bound authorization and population, when repeated probes reveal an independent measurement problem, or when current C.20, C.36, A.6.RCD, or A.6.REL semantics change the action.

### ME.17:12 - Relations

- ME.15 supplies either an admitted Method Engineering variant or a status-preserved candidate lineage. ME.16 can supply bounded introduction and later-practice observations. The admitted-Method branch still needs independent A.15.1 enactment; the candidate branch preserves its candidate/source accounts and description epistemes under their own maintained results and asserts neither Method nor enactment. Neither input establishes a cultural predicate.
- `C.20` governs Discipline recognition and `C.36` the bounded cultural-evolution question. `A.6.RCD` derives the needed bounded relation-bearing claim and stops at the lightest truthful disposition. `A.6.REL` supplies occurrence identity only when a later use must distinguish obtaining occurrences.
- `A.3.1` governs Method admission, `A.3.2` `U.MethodDescription` membership, `A.13` precise Agent bases, `A.15.1` intervention and receiving Work plus a named `enactsMethod` occurrence, and `A.10` evidence and reliance. Candidate accounts, source labels, carriers, descriptions without that membership basis, and teaching events substitute for none of them.
- `B.5` and `B.5.2` govern durable hypothesis generation and consequences. `C.27` applies only to a temporal adequacy question, `A.3.3` only to a real state-space and transition-law claim, `C.28` only to causal reliance, `A.15.7` only to a next action in ongoing Work, and `C.11` only after a chooser and OptionSet exist.
- A.19 comparison and selected-set semantics govern non-trivial alternatives. `A.22` applies only when one selected organization of identified constituents, obtaining relations, constraints, and use frame changes the decision; `C.30` only when an architecture claim is current.
- `A.3.4` governs any separate claim that a continuing card, description, System, selected structure, organizational System, or other subject underwent one actual bounded change. Intervention Work and a revised edition do not establish that `U.Transformation` by themselves.
- Description, publication, teaching, tool, support, rule, field, forum, assignment, permission, authority, Work, and direct-relation changes retain their direct governors. Return an observation to ME.15 or ME.10 only when it contradicts one particular maintained claim or edition. ME.8 receives an observation only for an A.3.2-classified `U.MethodDescription` whose one `EntityOfConcern` is an A.3.1-admitted Method; candidate/source material returns to its candidate account, source claim, another named episteme, or a local stop. A cultural claim or population spread alone contradicts none of them.

### ME.17:End

# Part VI - Pattern-Language Production and Situated Use

## ME.21 - Reconcile and Allocate Source Contributions after Exact Subtraction


### ME.21:1 - Problem frame

**Use this when.** You have recovered useful Method-related material from several sources, but still have to decide which contributions belong together and where they should be used. A handbook, research paper and account recovered from practice may use the same words for different actions, or different words for the same useful move.

The working reader is a Method engineer building or revising descriptions, a repertoire or a pattern language. Begin with one disputed allocation: **which recovered contribution should this description or pattern carry, and what would be lost by placing it there?**

The first useful result is one justified allocation. For example: “Use the existing coherence-checking Method; keep this source's narrower qualification window with the affected description claim; leave the observed shortcut as a candidate account.” Stop there if it settles the receiving decision.

Use an already sufficient F.0.2 synthesis or existing pattern result directly when no Method-content allocation remains. ME.4 recovers documentary contributions; A.3.1.MR, and conditionally ME.18, recover accounts from Work evidence. ME.21 starts from their results, not from an unread corpus or raw observations.

### ME.21:2 - Problem

Recovered material rarely arrives in reusable units. One chapter mixes a Method, a tool recommendation and a permission condition. Two sources agree on the main action but disagree on when its result may be reused. A practice account records a shortcut without establishing that the shortcut is a reusable Method.

A vocabulary crosswalk or chapter-to-pattern table does not decide these differences. Premature merging hides conditions; excessive splitting creates duplicate accounts; assigning every remainder to a new pattern turns source coverage into a publishing quota. Later users then cannot explain why a contribution was included or which source change requires repair.

### ME.21:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse and fidelity | Shared guidance saves reconstruction, while a source-local difference may change the action or stop. |
| Existing supply and useful remainder | FPF and ME already provide much of the answer, while a specialized condition or constructive move can remain. |
| Small allocation and connected account | One decision may need one row, while several dependent allocations need an inspectable explanation together. |
| Source authority and Method identity | A respected source can support a claim without admitting every listed step as a Method. |
| Convergence and disagreement | Similar contributions can share a description, while incompatible meanings need a contrast or an unresolved question. |

### ME.21:4 - Solution

Reconcile meanings before assigning destinations. Preserve every difference that changes the receiving Method use, and make the allocation's source return recoverable.

#### ME.21:4.1 - Work one allocation

1. **Name the receiving use and contribution.** Identify the description, Method question or pattern-language use being changed. Take the recovered source claim together with its difficulty or opportunity, proposed action, result, conditions and source location.
2. **Keep the input roles distinct.** A documentary claim remains what that source asserts. A returned MR account keeps its candidate, rival and evidence limits. A current FPF/DPF result keeps its declared scope. A source's report that work occurred is not independent occurrence evidence.
3. **Resolve only the meaning difference that matters.** Use F.0.1 when a source expression is ambiguous, F.1 when the source cut is insufficient, and F.0.2 when cross-source synthesis is needed. Consume its provisional synthesis, contrast or unresolved-inquiry result, including its locator, source edition and receiving disposition; do not replace that result with a similarity score.
4. **Subtract the current answer by value.** Open the current FPF/ME supplier that appears to cover the contribution. Compare the practitioner question, action, first result, applicability and stop. Use the supplier directly if it answers those positions. When a source adds a warranted Method-specific condition or move, retain that remainder and explain its receiving use.
5. **Decide whether the contributions can share an account.** Compare reusable action, participant meanings, preconditions, result, variation and stop. Merge supported common content while retaining different conditions. Split incompatible actions or statuses. Keep an unresolved alternative when the evidence cannot distinguish them. ME.5 and ME.7 settle any Method or whole claim needed by the allocation.
6. **Assign the contribution and its remainder.** State what is reused from current supply; what is added to or changes a Method description or pattern; what remains direct source material; and what is unresolved. Return a transdisciplinary question to FPF only after the Method-, corpus- and publication-specific content has been removed.
7. **Make the decision usable and revisable.** Give the reader the contribution, reason, destination, retained difference, source return and next action. If a later user will cite the allocation, keep a stable local locator with its edition. Name the source or supplier change that reopens it.

A one-contribution answer is enough. Expand to several allocations only when their overlap, omissions or shared conditions change the language or receiving decision.

#### ME.21:4.2 - Preserve what the destination cannot carry

A pattern may present the reusable action and still leave a worked derivation, local convention, dataset or detailed instruction at its source. State what remains there and how to recover it. A promised self-contained use cannot depend on an undisclosed omission.

When contributions merge, retain the reason that their common action is usable under the resulting conditions. When they split, preserve the action-changing difference and the relation between the resulting accounts. Shared terminology, publication order and apparent granularity are not sufficient reasons for either decision.

The allocation concerns source contributions and their uses. It is not a Method-composition result. Actual Method parts are independently identified Methods related through B.1.5; a pattern body, tool, source fragment or source-recovery step is not a part by position.

#### ME.21:4.3 - A compact retained answer

For a reusable allocation, this amount of information is normally enough:

| Position | Question answered |
| --- | --- |
| Receiving use | Which Method-description or pattern-language question does this allocation settle? |
| Source contribution and role | What is being carried from which passage, edition or returned account? |
| Current supply | Which existing result answers the reusable part, under what limits? |
| Reconciliation | What is shared, different, merged, split or still unresolved, and why? |
| Destination and remainder | What changes in the receiving description or pattern, and what remains elsewhere? |
| Return | Which changed premise reopens the allocation, and where should the reader return? |

Use ordinary prose instead of a table when it is clearer. A retained allocation is a claim-bearing account about the named allocation question; its claim content, subject and effective reference scheme determine its C.2.1 identity. Its locator is a recovery aid, not a Method identity or an acceptance decision.

### ME.21:5 - Archetypal Grounding

#### ME.21:5.1 - One review action, two conditions and a candidate shortcut

This is a constructed case. A Method engineer is preparing guidance for reusing an earlier review of a Method description.

- Handbook H, edition 3, §4, says to reuse the earlier review when only the description's display changes.
- Paper L, edition 1, §2, says that reuse also depends on the same reviewed claims, question and qualification window.
- Returned account W, version 2, reports a team that reused a review after shortening a warning. It retains two rival explanations: the warning was redundant, or the team missed an important condition.

The documentary dossier preserves H and L separately. W remains candidate evidence. Current ME.12 already supplies the coherence check and owner-specific correction; ME.15 distinguishes a description change from changed reusable Method semantics.

The engineer's allocation is:

| Contribution | Allocation and practical reason |
| --- | --- |
| Recheck a relied-on claim against its prior basis | Reuse ME.12. The sources do not require another general coherence Method. |
| Reuse the earlier review for a display-only change | Carry it as a conditional use of that result: the relied-on claims, question and qualification window must still match. H's shorthand does not erase L's limit. |
| Shortening the warning | Retain W's rival accounts and the missing comparison. Do not create an admitted “shortcut Method” from one reported occurrence. |
| Layout instructions for the handbook's publishing tool | Keep them in H. They do not belong in the reusable Method claim. |

The first useful result is the conditional reuse answer, not a new pattern count. A description author can now state the condition and the exact return to ME.12.

#### ME.21:5.2 - A changed source does not erase a former result

Later, H is available only as excerpts. The retained dossier contains merely a locator for the argument used by the allocation, and a new receiving use requires checking that argument. Return that recheck as unavailable and lower the dependent use. Preserve the earlier result with its historical basis, L's independently supported condition and unrelated allocations. Reopen only what relied on the missing argument.

If the complete argument had already been preserved with a suitable basis, loss of current website access alone would not establish that the earlier claim was wrong.

### ME.21:6 - Bias-Annotation

A source familiar to the engineer can become the vocabulary into which every other source is translated. Counter this by stating each source's action-changing meaning before merging. A desire for a neat language can also make every contribution look like a new Method; retain the non-Method and unresolved material that the receiving use actually needs.

The worked case illustrates allocation decisions. It does not establish the effectiveness of review reuse in an external project.

### ME.21:7 - Conformance Checklist

- The receiving use and the contribution being allocated are recognizable.
- Source assertions, recovered candidate accounts, current supply and occurrence evidence retain their different roles.
- Current supply was compared at the action, result, condition and stop that matter.
- Every merge or split preserves its semantic reason; unresolved differences remain visible.
- The destination states the useful change and the direct-source or instructional remainder.
- Method identity and composition claims have their own basis.
- A changed premise leads to an identifiable reconsideration or stop.

### ME.21:8 - Common Anti-Patterns and How to Avoid Them

| Misstep | Repair |
| --- | --- |
| One source chapter becomes one Method or pattern. | Recover the contributions and decide their subjects before allocation. |
| Similar wording is treated as the same action. | Compare participants, result, conditions and stops; retain a contrast when they differ. |
| “Already covered by FPF” removes the specialized useful move. | Show the current answer and the remaining domain filling at the same receiving use. |
| A source gap is treated as a false claim. | Preserve the unresolved inquiry and state the source action that could settle it. |
| A source-reference list stands in for an allocation. | State what changes in the receiving description or pattern and why. |

### ME.21:9 - Consequences

The engineer gains a language or description whose source decisions can be challenged and repaired locally. Reuse is more selective: some material disappears from the new body because a current supplier already answers it, while useful differences survive instead of being averaged away.

The cost is retaining the few source and dependency facts needed for later reconsideration. For a one-off question that F.0.2 or a direct source already closes, another allocation account adds no value.

### ME.21:10 - Architectural Rationale

Source recovery answers what the material says. Conceptual synthesis answers what a cross-source comparison warrants. ME.21 uses those results to settle a Method-specific distribution: what reusable action and condition belong in which description or pattern, and what must stay outside.

Keeping this result separate from ME.4 lets documentary recovery remain faithful even when a later allocation rejects a source proposal. Keeping it separate from Method admission prevents a placement decision from creating a Method. Retaining one small allocation before a corpus-wide map keeps the first useful result affordable.

### ME.21:11 - SoTA-Echoing

The current best-known approach for this question combines source-local conceptual comparison with Method-content and use analysis. F.0.2 supplies the former; ME.4, ME.5, ME.8 and the other direct ME results supply their professional subjects. In the H/L/W case, the added allocation preserves a usable conditional review answer, rejects an unsupported shortcut-Method identification and leaves tool instructions at their source. A generic synthesis note can be sufficient when it already contains those destinations and returns.

[Daalhuizen and Cash's Method Content Theory (2021)](https://doi.org/10.1016/j.destud.2021.101018) supplies questions about goal, procedure, rationale, framing and mindset. [Stacey et al. (2025)](https://doi.org/10.1017/dsj.2025.9) reinforces the need to retain the knowledge and use conditions around procedural guidance. Adopt these as source questions; do not turn their different models into a universal field schema or FPF parthood test.

The professional allocation is a local synthesis, not a claim of priority over SME or conceptual synthesis. Reopen it when current supply makes a separate result unnecessary, a source difference defeats a merge, or maintaining the allocation costs more than the source reconstruction it saves.

### ME.21:12 - Relations

- ME.2 supplies repertoire and lineage; ME.4 supplies documentary recovery.
- A.3.1.MR and conditionally ME.18 supply recovered Work accounts with their limits.
- F.0.1/F.1/F.0.2 govern source meaning, selection and conceptual synthesis; E.4.DPF governs framework-contribution subtraction.
- ME.5/ME.7 qualify the Method claims; ME.8 describes one admitted Method for a named use.
- ME.23 uses the allocation to architect a language; ME.24 challenges its recoverability and refresh reach.
- ME.12 and ME.15 receive contradicted claims and variant or non-variant maintenance questions.

### ME.21:End

## ME.23 - Architect a Problem-First MethodDescription Pattern Language


### ME.23:1 - Problem frame

**Use this when.** The Method-related content has been recovered and allocated, but one linear description does not give recurring users the independent problem entries, neighboring decisions or source returns they need. You must decide which patterns and relations will make that content usable as a language.

The working reader is a Method engineer or domain-framework author. Start with a user's question, such as “May I reuse this review after the source changed?”, and name the first useful result. Then identify the smallest body or cooperating set that can supply it.

The first useful result is a small language-architecture answer: the user's problem entry, each needed contribution and its subject, the material relation between them, and the stop or return. One direct MethodDescription can be the correct answer. Use ME.8 without a language when it already serves the use; use E.11.PFP alone when only public arrangement or navigation is missing.

### ME.23:2 - Problem

Source order, a procedure diagram or a repository taxonomy can become the pattern architecture without a separate decision. Every chapter is then treated as a Method part, every pattern as a MethodDescription, and every link as the next step in Work.

The opposite failure is a bag of useful patterns with no explanation of when they contribute together. A user must reconstruct prerequisites, alternatives, conflicts and source returns from private authoring notes. A whole-framework introduction can hide the same problem when it gives only labels and no practical answer.

### ME.23:3 - Forces

| Force | Tension |
| --- | --- |
| Independent entry and connected use | A pattern should work from its own problem, while some results depend on neighboring contributions. |
| Reusable Method and broader language | One Method can need several descriptions; a language can concern several independent Methods and decisions. |
| Useful relation and invented order | Links help users continue, while adjacency does not establish time order, parthood or permission. |
| Shared explanation and repetition | Profiles need coherent reasons and shared conditions without copying each body's Solution. |
| Progressive structure and first use | A formal structure can support later reliance, while an ordinary reader often needs only a clear question, action and return. |

### ME.23:4 - Solution

Build the language from the questions it must answer and the results those answers consume. Keep Method semantics, pattern relations and publication arrangement distinct.

#### ME.23:4.1 - Select the smallest useful language

1. **Name the receiving uses.** For each materially different use, state the reader, recognizable difficulty, first useful result and stop. Begin with one; add another only when it needs a different action or boundary.
2. **Recover the allocated content.** Use ME.21's source allocations or an already sufficient equivalent result. Preserve current suppliers, unresolved candidates and direct-source remainder. Do not infer a new Method from a source heading.
3. **Identify what each body describes or governs.** Use ME.8 for claims about how one admitted Method is performed. Keep neighboring selection, evidence, permission, architecture, representation and source-return questions under their own subjects. A body can cite those results without absorbing them.
4. **Compare the direct alternative.** Try a direct description or existing pattern entry for the same use. Retain a new body or language relation only when it adds a warranted action, result, boundary or saved source reconstruction at acceptable burden.
5. **Assign the contributions to bodies.** Give each body its own recognizable problem, useful move, worked case and stop. Put shared conditions and the reasons for the selected combination in the profile's whole account; use exact returns to inherited body answers.
6. **Name the material relations.** State in ordinary language which result another use consumes, what condition enables that use, what is an alternative, what conflicts and where a failed or missing result returns. Apply the defining FPF relation when a stronger relation claim is needed.
7. **Provide direct reader entries.** A reader should reach the relevant full body from a problem question without reading the complete production account. Whole-use explanation remains available for choosing, combining or adapting the language.
8. **Challenge the proposed arrangement.** Use ME.24 to attempt reconstruction and a changed-source return. Use ME.22 only when a material claim about content or representation advantage remains. Keep a direct-description or smaller-language answer when it is sufficient.

The list is an authoring aid. It does not prescribe the order of every user's Work.

#### ME.23:4.2 - Keep the described wholes separate

A MethodDescription has one admitted Method as its exact subject. A source-grounded language may publish such a description across several bodies when their bounded claims jointly describe that Method. State that subject and the claims included; do not infer membership from a coherent book or a shared title.

A profile account concerns the selected pattern/Method arrangement for its declared uses. It can include several MethodDescriptions and neighboring results. A separately addressable description of the production Method excludes independent situated-use and general profile-relation claims. Sharing a carrier does not merge those epistemes.

Method parthood is another claim. Independently identify the proposed whole and smaller Methods, then use B.1.5 for their whole-forming relations, joins, bounds and failure conditions. In the absence of that result, a useful action/result architecture remains prospective. Do not make the pattern inventory stand in for the missing composition.

#### ME.23:4.3 - Make each relation say something useful

Use the relation that changes the receiving action. The following are common questions, not a required universal relation catalogue:

| Relationship question | Useful statement |
| --- | --- |
| Result dependency | This description review consumes the qualification of these claims; if it is missing, return to that qualification. |
| Alternative | Either representation can serve this action under its stated loss limits; choosing one does not prove the other false. |
| Source support | This assertion relies on this recovered passage for the named use; changed or unavailable basis reopens that reliance. |
| Conflict | These candidate conditions cannot both govern the same selected use; retain the conflict for the owning decision. |
| Reuse or specialization | This profile reuses the general action and adds this source-specific condition. |
| Method composition | This independently admitted Method is a part of that whole under the B.1.5 result. |
| Publication grouping | These bodies are shown together to help discovery; their display order makes no stronger relation claim. |

A formal CGUS is appropriate only when that structure is itself needed. A.22.CGUS supplies the constituents, selected obtaining relations, applied constraints and named use frame, as well as potential branching and case-judgement requirements. Plain alternatives and conditions do not automatically admit that structure. ME.20 supplies ordinary situated continuation and its optional formal branch.

A changed fact can change a continuation judgement under the same frame. A changed question, admissible action or stop can require reidentification. The user or capable system assesses the new situation; a pattern or graph is not the executor. During ongoing Work, A.15.7 supplies the next-action decision.

#### ME.23:4.4 - Explain the profile at its own scope

Use all twelve substantive E.8 functions for the connected account: working situation, problem, forces, selected solution, grounding, bias, practical checks, recurring failure, consequences, Architectural Rationale, source comparison and relations. E.11.PFP governs where readers reach those answers. An inherited answer can be cited precisely; shared whole conditions and profile-specific consequences still need an explanation.

Distinguish relations across scales. A specialization narrows conditions while retaining the relevant general claims. A bounded-use projection selects claims for a reader. Reuse can connect several profiles. Method composition establishes actual parts. A publication group provides navigation. There is no fixed maximum number of scales, and overlap does not establish a mathematical lattice; use C.29 only for that qualified representation.

### ME.23:5 - Archetypal Grounding

#### ME.23:5.1 - From a review paragraph to three independent questions

This is a constructed case. An engineer has an admitted Method for checking a Method-description claim against its source and qualification basis. A use-bounded ME.8 description of that Method already explains the checking action. The new language must additionally help recurring users decide how unlike source contributions were allocated and what to revisit after a source change.

The proposed arrangement is:

| Reader's question | Contribution | Material connection |
| --- | --- | --- |
| What did we decide to carry from these sources? | ME.21's allocation answer | The review can cite the allocated claim and its retained conditions. |
| Do the relied-on claims still agree with their maintained basis? | ME.12's coherence answer | A contradiction returns to the maintained claim that owns it. |
| What promised source contribution can no longer be recovered? | ME.24's reconstruction answer | A missing allocation or source relation returns to that affected question before dependent reuse. |

These are independently useful entries. Their colocation does not make these pattern subjects parts of one review Method. The ME.8 description retains its one-Method subject; the profile explanation concerns the broader arrangement.

For a user who already has the needed allocation and only one contradictory claim, direct ME.12 use is enough. A user investigating an unexplained coverage loss starts with ME.24. The language is useful because the first result and return are visible at either entry, not because all three rows are traversed.

#### ME.23:5.2 - A source-change return

The allocation relied on an argument now unavailable for a required new recheck. The earlier answer remains preserved, but the dependent current-use claim has no recoverable basis. The reader returns only that claim and its source relation. A separately supported allocation and review remain usable.

If the user's question changes from reviewing the description to authorizing publication, it is another receiving use. The language points to the applicable publication result; a completed review is not that authorization.

### ME.23:6 - Bias-Annotation

A procedure-shaped source encourages a fixed workflow; a graph tool encourages graph-shaped explanations. Start with the actual questions and their result dependencies before choosing either form.

The worked arrangement demonstrates language and identity distinctions. It is not evidence that every Method engineer benefits from the same grouping or that the resulting profile is an enacted composite Method.

### ME.23:7 - Conformance Checklist

- The language begins from recognizable uses and first results.
- Each body has a recoverable subject, practical contribution and ordinary stop.
- Every MethodDescription claim identifies its one admitted Method.
- Each material relation states what it changes in use and retains its own governing basis.
- Direct descriptions and sufficient existing entries remain available.
- The whole/profile account explains shared conditions and reasons without replacing the full bodies.
- Reconstruction and changed-condition use can return a localized failure or an honest wider gap.

### ME.23:8 - Common Anti-Patterns and How to Avoid Them

| Misstep | Repair |
| --- | --- |
| One pattern equals one chunk equals one Method part. | Identify the body subject and qualify Method parthood separately. |
| Every link means “do this next”. | State the result, condition, alternative or return actually meant. |
| A profile is called one MethodDescription because it has one title. | Identify its exact subject and separate broader arrangement claims. |
| Twelve headings replace a whole explanation. | Answer the content questions at the declared scope, using inherited answers where sufficient. |
| A complete reading route becomes compulsory before first use. | Provide a direct question-to-body entry and an affordable stop. |

### ME.23:9 - Consequences

The language supports problem-first reuse and makes its connections inspectable. Users can select a small contribution, follow only a necessary dependency and revisit affected claims after change.

The cost is maintaining the cross-pattern explanation and relations. A direct description is preferable when that extra structure does not change recurring action or save meaningful reconstruction.

### ME.23:10 - Architectural Rationale

A source-to-language architecture lies between source allocation and situated use. It must show how independently useful descriptions and neighboring results contribute together while preserving their different subjects. ME.8 alone does not decide that whole arrangement; E.11.PFP alone does not supply its Method-specific content.

The selected structure can be useful without an admitted composite Method or a formal CGUS. Progressive exactness lets ordinary users act from a clear result and stop while preserving a path to the stronger claims when a later use needs them.

### ME.23:11 - SoTA-Echoing

Alexandrian pattern languages provide the historical problem-first, relational and generative idea. [Ralyté, Deneckère and Rolland's SME Map (2003)](https://doi.org/10.1007/3-540-45017-3_9) already supports on-the-fly construction; [continuous SME composition and enactment](https://doi.org/10.1007/s10270-022-01018-9) is a serious implemented alternative. Adopt their adaptive-use pressure, not a claim that unfolding begins here.

Current E.8/E.11.PFP supply individual and whole-account form; A.3.1/A.3.2/B.1.5, A.22.CGUS and ME.20 supply the separate identities and use results. This pattern adds the Method-specific language arrangement after source allocation.

Against the cheaper direct description in the worked case, the language adds independently reachable allocation and reconstruction questions. It earns that cost only when those questions recur or change action. No general advantage over prose, a method base or a fixed suitable route follows from the architecture. Reopen when a direct entry becomes sufficient, a relation loses its basis, or changed use makes the grouping burdensome.

### ME.23:12 - Relations

- ME.21 supplies semantic allocation; ME.5/ME.7 and ME.8 supply Method qualification and description.
- E.8 and E.11.PFP govern body and whole-account form; C.2.1 governs retained account identity.
- B.1.5 governs actual Method composition; A.22 and A.22.CGUS govern selected and unfolding structures.
- ME.22 supplies a bounded description comparison when representation claims matter.
- ME.24 tests reconstruction and affected refresh; ME.20 supports situated use without requiring production.
- ME.9 and C.37 retain representation selection; ME.15 retains Method-variant and non-variant maintenance.

### ME.23:End

## ME.24 - Falsify and Refresh Source-to-Pattern Coverage by Reconstruction


### ME.24:1 - Problem frame

**Use this when.** A Method-description language claims to preserve useful source contributions, but you need to find out whether a user can actually recover the promised action, conditions and source basis. Use it again when a source or use changes and you must identify the affected repair without discarding supported work.

The working reader is a Method engineer maintaining a source-grounded description or pattern language. Begin with one promise: **which source contribution should a user be able to reconstruct for this action, and what would count as a consequential loss?**

The first useful result is one reconstruction answer: the contribution recovered, a deliberate omission with a usable return, or the missing or contradicted element and its next repair. A known one-claim contradiction already owned by ME.12 needs no additional reconstruction exercise.

### ME.24:2 - Problem

A source-to-pattern map can appear complete because every chapter has a destination. Yet the language may omit a stop, merge rival Method accounts, lose an evidence limit or hide the material relation that makes a continuation usable.

Refresh adds another risk. A changed source prompts either a complete rewrite or an unjustified claim that only one sentence is affected. Neither response follows the actual dependency. Earlier valid results can be erased merely because current source access changed, while a defeated premise can remain in use because its paragraph still exists.

### ME.24:3 - Forces

| Force | Tension |
| --- | --- |
| Coverage and reconstruction | A map locates material, while a user needs the action and its conditions, not a matching heading. |
| Full source promise and bounded use | A maintained synthesis may promise source-complete recovery; a local question may require one contribution only. |
| Falsification and confirmation | One lost condition can defeat a claim, while several successful cases do not prove universal completeness. |
| Local repair and hidden dependence | Preserving unaffected results saves work, while an unrecoverable dependency boundary requires a wider inquiry. |
| Current access and retained evidence | A source can become unavailable without making an earlier supported result false. |

### ME.24:4 - Solution

Attempt the promised reconstruction, retain the exact loss or success at its tested scope, and follow changed premises to the claims and uses that depend on them.

#### ME.24:4.1 - Make the coverage claim testable

State the source edition or bounded corpus, the candidate language edition, the receiving use and the contribution that should survive. Include the intended action, first result, applicability, stop and source/evidence qualifications that can change that use.

Choose the source cut by the promise. A source-complete extraction commitment needs its stated full recovery basis; a gap-only claim needs a recoverable prior baseline and a bounded delta. F.1 can select a question-relative source cut, but it does not replace an exhaustive domain review when that is what the claim requires.

Keep the candidate's allocation and source returns available. An absent or stale baseline is a result to return, not a reason to assume that the visible subset is complete.

#### ME.24:4.2 - Reconstruct in the direction the question needs

From a source contribution, try to recover its usable meaning through the language. Follow the actual reader entry and full bodies. Can the reader obtain the action and result, recognize the condition or stop, and recover the source basis or retained instructional remainder?

From a promised language answer, return to its supporting sources and allocations. Does the cited material support that action and status, or only a similar topic? A pattern that combines sources must retain the reason for the combination and the differences that affect use.

One direction may settle the question. Use both when the language claims source coverage and the risk includes unsupported additions. A held-out passage or a source condition omitted from the authoring route can expose a loss that the destination map misses.

#### ME.24:4.3 - State the reconstruction result

Use the smallest accurate disposition:

| Result | Practical consequence |
| --- | --- |
| The contribution is recovered within the named scope. | Retain that bounded coverage claim and its source conditions. |
| A warranted specialization preserves the source contribution under narrower conditions. | State the narrower use and what broader use is not supplied. |
| Instructional or source-local detail is deliberately omitted but recoverable. | Give the source return; do not promise a self-contained use that depends on the omitted detail. |
| An action, condition, relation, source qualification or return is missing. | Name the failed promise and the smallest content or relation repair. |
| The language contradicts the supported source or merges incompatible claims. | Return the contradicted claim or allocation to ME.12 or ME.21. |
| The basis is unavailable or too weak for the required reconstruction. | Keep the question unresolved, retain the usable remainder and name the missing source action. |

These are ordinary result descriptions, not a universal status taxonomy. An omission becomes a defect when it blocks a promised use; an irrelevant source detail does not have to become a pattern.

A positive reconstruction concerns the inspected claim and use. It does not establish Method identity, effectiveness, transfer or complete coverage of an uninspected corpus.

#### ME.24:4.4 - Follow a changed premise

1. **Name the changed source or use fact.** Distinguish changed content, changed qualification window, unavailable access, defeated evidence and a different receiving question.
2. **Recover what relied on it.** Identify the allocation, Method/candidate claim, description, pattern relation or reader use that consumed the changed premise.
3. **Classify the resulting change at its owner.** ME.21 handles allocation; ME.8 description content; ME.12 a contradicted maintained claim; ME.15 a reusable Method variant or a non-variant change; ME.23 the language arrangement. Use the direct source, evidence or access result where that is the actual question.
4. **Retain independent results.** State why an unaffected result's relied-on basis still holds. A different file or nearby paragraph alone does not establish independence.
5. **Repeat the affected reconstruction.** Compare the repaired action, condition, result and source return with the same promised use. If the promise itself changes, identify the narrowed or different use rather than report the original test passed.

If the dependency boundary cannot be recovered, widen the affected inquiry. Localized refresh is a conclusion about dependence, not a default limit on effort.

#### ME.24:4.5 - Keep the first use light

For one contribution, a short answer can name the failed promise, supporting or missing passage, affected destination, retained results and next action. Retain a more detailed account only when another user must repeat, compare or rely on it. Its C.2.1 identity follows its claims, named coverage question and effective reference scheme, not a map identifier alone.

A cold-reader reconstruction is appropriate when author familiarity could supply the missing answer or a changed condition must be recognized without a hint. Obtain the initial answer before disclosing that condition. A desk reconstruction remains useful evidence, but it is not a fresh-reader or actual-enactment result.

### ME.24:5 - Archetypal Grounding

#### ME.24:5.1 - A covered topic with a missing stop

This constructed case starts with handbook H, edition 3, §4: “Reuse an earlier review for a display-only change.” Paper L, edition 1, §2, adds the condition that reviewed claims, question and qualification window must still match. The reconciled contribution also requires a new source-dependent recheck to stop if its required argument cannot be recovered.

A candidate language has a “Reuse review” entry and cites H and L, but its body says only “reuse the prior review for display changes”. The destination map marks H §4 and L §2 as covered.

Reconstruction finds the reusable action but not the qualification window or source-return stop. The topic is present; the promised decision is not fully recoverable. Return a description-content correction to the body carrying that answer. The correct narrower conclusion is that the action is recoverable while its conditions are missing, not that the entire language has failed.

After repair, the body states the matching-claim/question/window condition and the local source stop. Repeat the same use: the reader can now distinguish permitted reuse from a recheck lacking its basis. This is a constructed content check, not a measurement of review effectiveness.

#### ME.24:5.2 - Change one source without rewriting the repertoire

The later facts are:

| Retained contribution | Basis after the change |
| --- | --- |
| A1, the use of H's argument in a new recheck | H is now available only as excerpts; the retained dossier has a locator but not the required argument. |
| A2, a narrower condition supplied independently by paper L | L remains available and its relied-on claim is unchanged. |
| A3, an unresolved shortcut from returned MR account W | W retains its rival explanations and evidence gap; the H argument was not its basis. |

Return A1's new recheck as unavailable and lower only the dependent current use. Keep its earlier result with the historical basis; do not infer falsity from lost access. Retain A2's condition and A3's uncertainty. If another pattern copied A1's assumption, it is affected even if its file did not change.

The repair is either to recover the required argument, use a separately justified sufficient basis, or narrow the current use. A full repertoire rewrite would add no supported correction to A2 or A3.

#### ME.24:5.3 - When gap-only is not justified

A team has no recoverable earlier allocation and cannot tell which source claims the language relied on. It cannot prove that only a newly changed paragraph matters. Return the missing baseline and broaden recovery through ME.4/ME.21. Do not call the language source-complete or all other results unaffected.

### ME.24:6 - Bias-Annotation

Authors can reconstruct a missing condition from memory and mistake that success for a property of the language. Use the actual accessible reader route and retain which information was supplied externally.

A coverage percentage can reward destinations while hiding a decisive lost stop. Treat counted items as a discovery aid unless their relation to the receiving use is established. Constructed cases and small reader probes retain their limited scope.

### ME.24:7 - Conformance Checklist

- The source/language editions, receiving use and coverage promise are identifiable.
- The reconstruction tests actionable meaning, conditions, stops and source qualifications, not topic presence alone.
- Unsupported additions and deliberate omissions are distinguished from missing promised content.
- The result states its tested scope and evidence limits.
- Every changed premise has an affected claim or an honest unresolved impact boundary.
- Preserved results retain their own supporting basis.
- The repaired or narrowed use receives an affected reconstruction before closure.

### ME.24:8 - Common Anti-Patterns and How to Avoid Them

| Misstep | Repair |
| --- | --- |
| Every source chapter has a pattern, so coverage is complete. | Reconstruct the action and conditions a user must recover. |
| One successful example establishes the whole corpus. | Limit the conclusion to the inspected promise and state untested scope. |
| Missing access erases a previously supported result. | Separate current recheck needs from retained evidence and historical claims. |
| Only the changed file is affected. | Follow the premises used by other claims and relations. |
| A vague “refresh needed” report causes a whole rewrite. | Name the missing contribution, owning result and next source or repair action. |

### ME.24:9 - Consequences

Coverage becomes a challengeable claim about useful reconstruction. Source changes can lead to small, justified repairs while leaving supported work available.

The cost is preserving the basis and dependence needed to make that judgment. Where those facts are absent, a wider recovery is the honest result. The Method saves work only when its localized return costs less than the repeated reconstruction it avoids.

### ME.24:10 - Architectural Rationale

ME.12 begins with a potentially contradicted claim and locates its owner. This pattern can start earlier: a promised source contribution is missing, and the language may not yet expose the claim or relation that should own it. Reconstruction finds that loss and supplies the repair question.

Combining falsification with affected refresh keeps the original promise and its change history connected. ME.15 still decides whether reusable Method semantics changed; a missing description condition is not automatically a new Method variant.

### ME.24:11 - SoTA-Echoing

[Riehle, Harutyunyan and Barcomb's pattern-discovery and validation work](https://arxiv.org/abs/2107.06065) uses established research Methods rather than treating the “rule of three” as sufficient validation. Adopt the need for explicit evidence and discriminating cases; source reconstruction is only one bounded check, not a substitute for their empirical programme or for domain trials.

Current F.0.2 and ME.21 preserve source meanings and allocation, while ME.12/ME.15 and G.11 retain their correction and refresh results. Compared with a chapter-to-pattern map, the H/L case exposes a missing qualification condition that changes the review decision. Compared with a full reread, the A1/A2/A3 case retains L's condition and W's unresolved account while returning the one unavailable recheck.

These examples justify the useful form of the result, not a general claim of faster maintenance. Reopen when a lost dependency defeats localization, a source promise changes, a direct correction makes reconstruction unnecessary, or observed maintenance burden outweighs its benefit.

### ME.24:12 - Relations

- ME.4 supplies documentary recovery; A.3.1.MR and conditionally ME.18 retain Work-evidence recovery.
- ME.21 supplies allocations and unresolved source differences; F.0.2 supplies conceptual-synthesis results.
- ME.8/ME.12 receive description and coherence repairs; ME.15 distinguishes variants from other maintained changes.
- ME.23 receives a failed language relation or entry; ME.20 lets a user continue from the next needed result.
- ME.22 can compare description revisions when the content/form question remains.
- ME.11, ME.13 and ME.14 retain enactment, transfer and worth questions beyond source reconstruction.

### ME.24:End

## ME.20 - Use Pattern-Language Knowledge to Continue Situated Method Engineering

>
> **Primary working result:** a bounded Method-architecture continuation: the result needed now, the relevant pattern knowledge, the available, blocked, or unknown continuation, and the smallest return after a decision-relevant change.

### ME.20:1 - Problem Frame

**Use this when.** You are engineering a Method or its relations, several questions remain connected, and current facts can change which question should be answered next. A pattern language can help, but its contents page does not tell you whether to qualify a candidate, resolve a whole, compare arrangements, repair a description, or stop.

Start by asking: **Which Method-architecture result do we need now, and what fact could change that need?** For example: “We can review the candidate description, but cannot yet claim that its proposed Methods form one whole. Which result should we obtain, and what stays valid when the missing evidence arrives?”

The first useful answer can be spoken: “Review these unchanged claims through ME.5; keep the whole claim unresolved under ME.7; publication remains blocked by its separate condition. Reopen the whole claim when its missing relation basis arrives.” During ongoing Work, the deciding System uses A.15.7 to choose the actual next action and names its performer and feedback condition.

The practical gain is continuity across Method Engineering questions. Each new fact returns to the result it can change; the practitioner need not restart qualification, comparison, description, and support work together or reconstruct their boundaries from a reading sequence.

**Ordinary non-use.** If one current MethodDescription already states the applicable action, conditions, result, and stop, use it directly. If one existing pattern or result answers the whole current question, use that answer and stop. A single action does not need a PLUS-ME account, alternative set, CGUS, or durable result. Before Work begins, use the actual architecture, planning, or work-entry question; A.15.7 governs only an ongoing-Work choice.

This is the situated-use branch of PLUS-ME, a pattern-language profile within representation-neutral Method Engineering. It does not recover and reconcile an entire source corpus or construct the complete language.

### ME.20:2 - Problem

A Method engineer receives knowledge in different forms: candidate accounts, source dossiers, qualified contributions, architecture proposals, descriptions, and review results. A convenient pattern sequence can hide the distinction between a result that exists, a claim still awaiting support, and a next action that somebody must choose.

When one condition changes, two errors follow. The practitioner may carry a stale composition or authority claim into the next action, or reopen every result because “the situation changed.” Both lose useful work: the first by relying beyond its basis, the second by repeating unaffected judgements.

### ME.20:3 - Forces

| Force | Tension |
| --- | --- |
| Useful entry | A narrow pattern gives an answer quickly, while a connected Method question may depend on another result's status. |
| Continuity and change | Earlier results save work, while changed applicability, evidence, or authority can invalidate a particular use. |
| Method and representation | A language explains Methods and choices, while its grouping and reader order establish neither Method composition nor Work order. |
| Potential and present | Several continuations may be meaningful across situations, while the present situation may allow only one or none. |
| Knowledge and action | An assistant can retrieve or recommend guidance, while another System may choose, authorize, and perform the action. |
| Proportionate effort | A brief answer often suffices; a later comparison or reliance may need an addressable result and a checkable basis. |

### ME.20:4 - Solution

Keep the current Method question connected to the result that answers it. Obtain the narrow pattern contribution, expose only the continuations whose conditions matter now, and after a substantive result check which earlier claims or uses actually changed.

#### ME.20:4.1 - Find the Missing Method-Architecture Result

Name the receiving problem and the result it needs. Distinguish an unavailable result from an available result that is not currently applicable. Use the following returns only when their question is present; they are alternatives, not a prescribed sequence.

| Current difficulty | Direct contribution to use | First result retained here |
| --- | --- | --- |
| The relevant alternatives or source editions are unknown. | ME.2; ME.4 for documentary recovery, A.3.1.MR and conditional ME.18 for occurrence-evidence recovery. | A bounded repertoire, dossier, candidate account, or honest gap, with its source and status. |
| One Method or individually scoped candidate needs qualification. | ME.5 and the applicable A.3.1 identity question. | The individual qualification or unresolved identity condition; not a verdict on a whole. |
| Several possible arrangements differ in relations, combined demand, or burden. | ME.6. | The compared arrangements and architecture decision, preserving proposed versus obtaining relations. |
| A proposed Method whole lacks supported identity or composition. | ME.7 with A.3.1 and B.1.5. | An obtaining composition result, prospective account, or lower return. |
| The way is understood but its description cannot support the named use. | ME.8; ME.9 only when several unlike Method uses need a cross-use representation profile. | The description/account or representation result with its omitted claims and use boundary. |
| A description, support arrangement, or earlier result is contradicted. | ME.12 for the correction question; ME.10 for a support configuration; ME.15 when reusable variation changes. | The corrected, narrowed, or still-unresolved result and its affected consumers. |
| The content question is settled and the question is publication or release. | The applicable E.11.PFP, E.4.PFIP, publication, and release Methods. | Their own result or blocker; content review does not supply publication authority. |

Retrieve the selected pattern through E.11.PUA/PUR and read its Solution and boundary. If a current result already answers this question, reuse it under the defining pattern and stop. A title match or search result is not a substitute for that check.

#### ME.20:4.2 - Make the Present Continuation Usable

1. **Carry the result boundary forward.** In ordinary language name the Method, candidate account, proposed relation, description, or other subject under decision. Retain which claims are established, proposed, contradicted, or unresolved and which source or result supports them.
2. **Expose only relevant continuations.** For each live alternative state the result it could obtain, the condition it needs, the facts known now, and whether it is available, blocked, or unknown. Name the first missing fact or rule. Do not add alternatives merely to make the account branch.
3. **Keep material relations readable.** State a prerequisite result, local order, alternative, conflict, support condition, check, or return when it changes this use. Two nearby patterns can remain an unordered neighborhood. Use each relation's direct governor; a connecting arrow, contents order, or shared profile supplies no relation by itself.
4. **Return the live choice to A.15.7.** During ongoing Work, the deciding System uses the available facts and the domain Method's limits to choose the next action. That result names the chooser, intended performer, and stop or feedback; establish capability, access, permission, or authority only when the action needs it. If Work is blocked by a missing performer, support, or continuation-state relation, use A.15.8's actual-Work configuration branch before returning to choice. An assistant's recommendation is input to that choice. Before Work, use the actual architecture, planning, readiness, or fixed-option decision instead.
5. **Observe a result before updating its consequences.** An expectation remains an expectation until the result is obtained or independently supported. Use the direct result and Work/evidence patterns when those claims matter. Choosing an action, changing a plan, performing Work, and learning a fact remain separate.
6. **Check the decision-relevant delta.** After a substantive result, or before relying on possibly stale information, use §4.3. Reopen the smallest affected question, retain results whose defining conditions still match, and stop when the receiving use has its result or honest blocker.

The method does not require a log of every thought. “No decision-relevant change; continue using this result within its stated window” is sufficient when a continuity statement is needed. If no later use needs that statement, no additional record is required.

#### ME.20:4.3 - Localize a Situation Change

Compare the new fact with the claims and uses currently being relied on. Check applicability or preconditions; alternatives; constraints or interfaces; resources or capability; assignment, access, permission, or authority; evidence/currentness; expected result, stop, or risk; and the decision-relevant situation boundary. Inspect only positions whose possible change could alter the next result or action.

| What changed | What to reopen | What is not changed merely by this observation |
| --- | --- | --- |
| A fact, evidence item, test outcome, or qualification window. | The affected result's reliance/currentness and the current continuation judgement; obtain the first missing basis or stop. | The Method, completed Work, and an independently unchanged potential structure. |
| A claim supporting a proposed whole or a participant relation. | The exact ME.7 identity/composition question; ME.6 if the architecture alternatives or chosen arrangement are affected. Preserve individual ME.5 results whose basis still holds. | All participant identities or all source recovery merely because one relation is unresolved. |
| Reusable action, applicability, required contribution, permitted variation, or reidentification rule of a Method. | A.3.1/B.1.5 and the affected Method Engineering result, including ME.15 when variant identity is current. | Earlier performed Work or an automatic new description/publication edition. |
| A formal CGUS constituent, selected obtaining relation occurrence, applied constraint, or named use frame. | A.22 structure identity. A changed locus binding or potential-continuation row separately reopens CGUS membership. | A case judgement cannot silently stand in for the changed structure or membership test. |
| The instructions or intended-work content, with the represented Method still unchanged. | ME.8/ME.12 for description correction; A.15.2 for a changed WorkPlan. | Method identity or evidence that the planned action was performed. |
| The audience, relied-on claim, or publication/use boundary. | The affected representation, source-use, or publication question and its direct consumers. | Unaffected content or independently qualified uses. |

These are different change questions, not a universal event classification. For example, learning that evidence is missing does not prove that the claimed relation is false. If the reach of the change cannot be bounded, name that uncertainty and widen the relevant question; do not claim unaffectedness from the absence of a visible text edit.

#### ME.20:4.4 - Retain Only What Another Use Needs

An ordinary continuation answer needs the current difficulty, selected knowledge, available/blocked/unknown action, first missing fact, and stop or return. Retain an existing result by reference when it already carries the needed claims.

Only when another turn must cite, compare, audit, or rely on the connected answer, keep a Situated Method-Architecture Result as an ordinary C.2.1 episteme. Its content includes the architecture claims and statuses in use, their source/result returns, the current continuations and conditions, the affected-delta answer, and the next return. This is a descriptive result name, not a new root kind or mandatory register.

Its EntityOfConcern is the exact architecture question or proposed set being considered, or an independently qualified selected structure when that is actually the subject. Do not use a fictitious CGUS as the concern of an ordinary proposal. A changed ClaimGraph, EntityOfConcern, or effective ReferenceScheme changes episteme identity under C.2.1; any continuity between results needs its own meaningful basis.

The profile/language episteme, a description of one Method, a selected structure, a continuation judgement, a next-action decision, a WorkPlan, performed Work, and evidence retain their separate identities. One result may cite another; that does not merge their subjects or claims.

#### ME.20:4.5 - Open Formal CGUS Only for Its Own Use

The plain alternatives-and-conditions answer often suffices. Use A.22.CGUS when an independently selected structure must be qualified, persisted, compared, published, or more strongly relied on. A structure requires its constituents, selected obtaining relations, applied constraints, and named use frame; its CGUS membership requires at least two potential continuations across allowed cases. Zero or one currently enabled continuation is compatible with that potential branching.

For a Method-architecture continuation use, the local frame name PLUS-ME-Situated-Architecture-Continuation denotes this question: which continuation can obtain the next bounded Method-architecture result or honest stop? Its admissible actions are to select a continuation, retain alternatives, request the first missing fact, or stop. The stop is the first decision-usable result or a missing condition that prevents it. Naming this frame does not establish the structure or choose the action.

Use A.22.CGUS's complete basis for each formal judgement, retaining condition evaluation separately from an obtaining relation. The formal continuation outcomes are enabled, disabled, unknown, or error. A completed negative condition evaluation has the outcome notSatisfied; derive its continuation effect from the declared required polarity. An execution or evaluation failure remains error; return the affected test before relying on its result. Missing evidence can leave the condition evaluation unknown. Keep structure identity, membership, case judgement, description adequacy, and later reliance separately checkable.

### ME.20:5 - Archetypal Grounding

#### ME.20:5.1 - Continue a Release-Method Proposal Across Two Turns

This constructed case concerns ongoing Method-architecture work on proposal P. Whole Method W and participant Methods M1 and M2 have independent identity results, and the participant qualifications remain current. P proposes a construction of W using both participants, but the claimed methodPartOf(M2,W) is unresolved: its cited procedure has not been checked for a required contribution or an admitted alternative in W's construction. A description review can inspect the independent participant claims now. Publication is blocked because no publication decision has been obtained.

The Method engineer needs the description-review result now while keeping the whole claim visible for the next meeting. The continuation answer is:

| Current question | Relevant knowledge and condition | Answer now |
| --- | --- | --- |
| May the retained participant claims be reviewed? | ME.5 results remain applicable; review does not presuppose the unresolved whole. | Available: review those claims while preserving their statuses. |
| May P's proposed composition of W be described as obtaining? | W and participant identities are available, but ME.7/B.1.5 still need the exact required relations. | Unknown: recover the basis of methodPartOf(M2,W). |
| May this candidate be published? | The applicable publication decision has not been obtained. | Blocked: content review supplies no replacement for that decision. |

The engineer uses A.15.7 to choose the available bounded review. The review lead will perform it; the engineer is the chooser in this case. The feedback condition is a review result or new evidence that changes the whole claim. Because the next meeting will rely on these distinctions, the engineer retains one situated result about P's architecture question, citing the existing ME.5 results rather than copying them. No formal CGUS is needed for this use.

Before the next choice, the relevant procedure is inspected. Its construction rule places M2 outside W: M2 supplies optional advice but is neither required nor an admitted construction alternative. That changes the proposed composition claim, not the independently established identity of W, M1, or M2.

The engineer returns the affected composition question to ME.7. The proposed relation set is not supported as W's obtaining composition; retain the useful support relation and return P for correction or another proposed arrangement. The participant ME.5 results remain supported; the bounded review and publication blocker remain as before. The new situated result changes the composition-claim and return content. It does not backdate a new Method, change completed review Work, or announce a new structure from one new fact. If another proposed arrangement changes W's reusable semantics, that later proposal needs its own identity question.

What changed in practice is small but consequential: one changed source claim reopens one whole-account decision and its dependent uses, while available independent review continues.

#### ME.20:5.2 - A Sufficient Direct Description

The current approved description already says: inspect the named evidence field; if the signed supplier result is absent, retain the release hold and return to the supplier. The field is absent and no competing action is admissible. Use that description and its stop directly. There is no extra PLUS-ME result, choice dossier, formal structure, or invented second alternative.

#### ME.20:5.3 - An Assistant Recommends from Stale Facts

An assistant retrieves a relevant review pattern and recommends sending the candidate to the reviewer. Its recommendation uses yesterday's access statement. The current question is whether that reviewer can inspect the restricted evidence today; the assistant has neither that access nor publication authority.

Keep the recommendation as a recommendation. Ask the access holder to refresh the decision-bearing fact. If access is unknown, the evidence-dependent review continuation is unknown; if access is denied, it is blocked. A permitted review of unrelated public claims may remain available if the same review Method allows that narrower result.

The deciding engineer uses A.15.7 for the next action, the access holder supplies the access answer, and the permitted reviewer performs any selected review. Confidence in retrieval supplies none of those relations. If no safe narrower review is available, stop at the missing access result. No performed review or publication follows merely from the recommendation.

### ME.20:6 - Bias-Annotation

Method engineers may favor explicit architectures and overlook a sufficient direct description. Start with the non-use test. Pattern-language enthusiasts may attribute capability to the language itself; retain the acting and deciding Systems only where those claims matter. Automation can amplify old source assumptions, so inspect currentness before a confident recommendation enters action.

The cases emphasize documentary Method Engineering and review. They establish no empirical advantage across domains, human readers, or AI systems. A high-consequence decision may need stronger evidence than these constructed continuations supply.

### ME.20:7 - Conformance Checklist

- The current question is about a Method, its relations, or its description; a sufficient direct result is used without a profile wrapper.
- The next needed result and its supplying pattern are explicit; established, proposed, contradicted, and unresolved claims retain their statuses.
- Every exposed continuation has a relevant condition and current basis, or an honest missing fact.
- During ongoing Work, A.15.7 supplies the action choice; the chooser, intended performer, and any material authority/access/capability relation remain distinguishable.
- A substantive change reopens its affected Method Engineering result and dependent uses; unaffectedness is checked against the retained basis.
- Formal CGUS, persistent results, and Work claims are opened only for a use that needs them and satisfy their own direct rules.
- The answer states the first useful result or blocker and the next stop or return, without treating reader order as Work order.

### ME.20:8 - Common Anti-Patterns and How to Avoid Them

| Failure invited by the working situation | Repair |
| --- | --- |
| Follow the next contents entry after finishing a pattern. | Recover the result needed by the current Method question and its actual prerequisites. |
| Reopen every Method result because one source changed. | Trace the changed claim to its dependent result and uses; widen only when the reach cannot be established. |
| Carry an unresolved whole through a successful participant review. | Preserve the individual results and return whole identity/composition to ME.7. |
| Treat a recommended action as current, permitted, and performed. | Refresh its action-changing basis and separate the choice, authority, performer, and observed result. |
| Build a CGUS to describe one required action. | Use the direct MethodDescription and stop; potential branching and a named formal use must justify CGUS. |

### ME.20:9 - Consequences

The practitioner can continue Method Engineering without rereading the whole repertoire or treating every local change as a new Method. Missing basis remains visible at the result that needs it, so independent useful work can continue without claiming that blocked work has become possible.

The cost is maintaining a few explicit result-to-use connections when they matter across turns. A poor or stale pattern language cannot be repaired by this continuation method; the missing content must return to source recovery, qualification, architecture, or authoring.

### ME.20:10 - Architectural Rationale

General pattern use and live Work steering already exist. The Method Engineering contribution is the connection between a current professional question, the distinct result that can answer it, and the smallest affected return when that result's basis changes. The table in §4.1 and the two-turn case make that connection usable without copying the full qualification, composition, representation, or steering Methods.

A direct MethodDescription is preferable when it already supplies the action and stop. A fixed route is useful when its dependencies remain sufficient. For a changing plurality of questions, reconstructing the returns from separate patterns can hide an unresolved whole or repeat unaffected qualification. This method keeps those returns visible at a cost proportionate to the present decision.

Pattern-language form supplies problem-oriented knowledge, not a replacement chooser. Local first–then dependencies can still matter. Neither situational use nor the word unfolding claims that Methods have no causal assumptions or that all actions can occur in any order.

### ME.20:11 - SoTA-Echoing

| Source line and comparison use | Retained or adapted contribution | Boundary and practical consequence |
| --- | --- | --- |
| Gottschalk, Yigitbas, Nowosad, and Engels, [Continuous situation-specific development of business models](https://doi.org/10.1007/s10270-022-01018-9), online 2022, journal issue 2023; an implemented contemporary SME comparator. | Adapt continuous interaction between supplied knowledge, situation-specific composition, and enactment. | Their repositories, fragment metamodel, and business-model case do not establish FPF Method parts or a universal process. ME.20 uses direct Method/result identities and can stop without repository or structure construction. |
| Hoppenbrouwers and colleagues, [Agile Service Development: A Rule-Based Method Engineering Approach](https://doi.org/10.1007/978-3-642-19997-4_17), 2011; historical declarative/agile SME anchor. | Retain rules and constraints as an alternative to prescribing one complete development route. | Declarative and on-the-fly Method Engineering are prior ideas, not novelty claims here. Each current continuation still needs its facts and an acting/deciding System. |
| Christopher Alexander, [The Origins of Pattern Theory](https://christopher-alexander-ces-archive.org/article/the-origins-of-pattern-theory-the-future-of-the-theory-and-the-generation-of-a-living-world/), OOPSLA 1996 address published in 1999; historical lineage. | Retain context-sensitive use of a connected pattern language and the contribution of generative order. | Pattern order can be meaningful without being a universal Work sequence. This tradition supplies neither current FPF identity nor a claim that causality disappears. |
| Stacey and colleagues, [Methods as a form of engineering knowledge](https://doi.org/10.1017/dsj.2025.9), 2025; recent engineering-knowledge comparator. | Retain explicit how-to knowledge together with the knowledge needed to interpret and use it. | Their treatment of Method knowledge does not settle FPF's world-side Method/episteme boundary. It supports exposing the needed knowledge and result, not importing a definition by vocabulary. |
| Current E.11.PUA/PUR, A.15.7, A.22.CGUS, A.3.1/B.1.5, and ME.5–ME.9; direct working comparators. | Reuse pattern use and result reuse, live choice, potential/current continuation separation, Method identity/composition, and professional result contracts. | The new contribution is limited to the question-to-result return and situation-delta localization across Method Engineering uses. If direct use supplies that same result more cheaply, take the direct exit. |

These sources support a bounded synthesis, not a claim that PLUS-ME invented continuous or pattern-based SME. Reopen the affected source or action when a current alternative supplies the same result with less reconstruction, a source change alters a load-bearing distinction, or use evidence reveals a missed dependency or unnecessary burden. Claims of human or AI superiority require their own comparative evidence.

### ME.20:12 - Relations

- ME.2 and ME.4 supply documentary knowledge; A.3.1.MR and conditional ME.18 supply occurrence-evidence recovery results.
- ME.5, ME.6, and ME.7 keep individual qualification, alternative architecture, and whole resolution distinct. ME.8–ME.10 supply description, cross-use representation, and support results; ME.12 and ME.15 carry the applicable correction or variant return.
- E.11.PUA/PUR govern the actual pattern-use and recommendation questions, including reuse of a matching earlier result. A.15.7 governs live next-action choice; A.15.2/A.15.5 and C.11 retain their other entry conditions.
- A.22.CGUS governs structure and continuation judgements. C.2.1 governs a retained result episteme. A.3.1/A.3.2/B.1.5 and A.15 keep Method, description, composition, plan, Work, and result claims distinct.
- E.11.PFP and E.4.PFIP supply publication-form and publication-preservation work when that question becomes current; a situated continuation grants neither publication nor release.

### ME.20:End

# Cross-Pattern Application

## APP-ME-01 — Choose the Smallest Method-Engineering Result Needed for Release EC-417

The team must release engineering change `EC-417`, but signed supplier pinout evidence is expected thirteen days after the target software-integration slot. The team calls the difficulty its “release methodology”. That label hides several possible subjects: relations among Methods, test-rig support, evidence currentness, human decision authority, and allocation of supplier and safety Work. Choosing the wrong subject can delay the release, overload the safety engineer, expose confidential geometry to an AI provider, or turn an observed timing association into an unsupported causal claim.

Use this application when a receiving-Work difficulty is described as one methodology problem while several unlike practice objects may be responsible. The practical gain is the smallest truthful Method Engineering result that changes the present decision. Do not run the whole route when one known capability or support defect, one source-currentness repair, or one individual qualification already answers the question.

The first move is to name the receiving result and ask which result is needed now. Continue only when an unresolved relation changes the release choice:

| Current question | Smallest useful result | Stop or continue |
| --- | --- | --- |
| Is the difficulty a Method, a candidate account, a family or local grouping, a relation, or a non-Method subject? | `ME.1` focus result | Stop with the non-Method return when capability, support, evidence access, or another subject owns the difficulty. |
| Which identified Methods and candidate accounts are current enough to inspect? | `ME.2` repertoire with exact identity, edition, evidence-window, and input/result refs | Stop when the bounded repertoire answers the question; enter `ME.18` only for a named account-recovery gap that ordinary recovery cannot close. |
| What must the selected subject contribute in this situation? | `ME.3` criteria with actual subjects, evidence, and stops | Stop with the criteria set when no comparison or qualification is needed. |
| What unlike contributions are bundled under “release methodology”? | `ME.4` kind-preserving dossier | Stop after recovery when package navigation, not subject fitness or architecture, is the problem. |
| Can one identified Method or candidate account serve the bounded Work? | `ME.5` individual qualification with status preserved | Stop with that individual result; continue only when interactions among subjects change the decision. |
| What changed, and may the observed change support causal reliance? | `ME.19` differentiation account plus the separate `C.28` causal-use result | Stop when description is enough or the causal-use result is `unsupported`; do not promote chronology into evidence. |
| Which arrangement of Work, allocation, evidence, support, permission, and authority satisfies the receiving constraints? | `ME.6` architecture decision over named structures | Stop with a relation-only or no-composite result when no whole question remains. |
| Does the proposed whole already obtain? | `ME.7` whole-or-account result | Record obtaining relations only when identity and relation evidence support them; otherwise stop with a prospective candidate account and WorkPlan. |

EC-417 continues beyond the early returns because evidence timing, Method relations, allocation, support, authority, and recovery burden jointly change the release decision. All identifiers, dates, observations, capacities, and outcomes below are scenario assumptions for this worked decision.

### 1. Bound the EC-417 receiving result and three viewpoint-governed readings of one Work

The project must release engineering change `EC-417`: controller firmware `4.8` together with harness revision `H-17`. The receiving result is one released controller change whose affected safety requirements, implementation revisions, supplier pinout, verification results, evidence status, and release authority are traceable.

The release is day `D0`. The target software-integration slot is `D-21`; signed supplier pinout is expected at `D-8`; software remains reversible until `D-1`. An AI provider may propose requirement-to-test links. It has no release authority and cannot receive confidential supplier geometry.

Project, process, and case readings are intended to describe the same release Work. A current episteme counts as a view only after a separate `E.17.0` judgment against an exact viewpoint edition:

| Intended viewpoint | Candidate description would expose | Boundary |
| --- | --- | --- |
| project | dates, allocations, boards, authorities, and release slots | schedules do not create a Method or a second Work |
| process | recurring supplier-evidence, integration-bundle, verification, and authorization correspondences | recurrence does not identify one process-Method or composite whole |
| case | the changing evidence, mismatch, exception, and next decision of this release | the case description is neither the Work nor a Method |

The three readings expose different Method and support questions. This application reports none of their epistemes as a current `U.View` until the exact candidate episteme, viewpoint edition, fixed rules, and positive `E.17.0` judgment are available. Any Method, relation, capability, allocation, or authority claim still needs its own identity or evidence.

### 2. Choose the subject before redesigning it

`ME.1` compares materially different subjects:

| Focus option | Disposition |
| --- | --- |
| `C-EC-Release-v2` as one Method | reject as a focus assumption; it is a proposed-whole candidate account, not an identified Method |
| an established release-Method family | reject because no governed family relation is supplied |
| project-local locator `LG-EC417-ReleaseMethods` | retain for comparison of the four identified Methods only; it creates no family |
| `C-AI-Trace-Review` | keep as a candidate account but do not select as the focus because trace suggestions govern neither evidence reconciliation nor release authority |
| relations among four identified Methods and two evidence-reconciliation accounts | select because evidence timing, result use, allocation, and authority relations change the release decision |
| test-rig capability/support | retain as a non-Method rival; current evidence does not make it the sole subject |

The selected Method-relation focus contains identified Methods `M-HW-Verify`, `M-SW-Integrate`, `M-Supplier-Approve`, and `M-Release-Authorize`, plus candidate accounts `C-Evidence-Reconcile-Internal` and `C-Evidence-Reconcile-Supplier`. No fifth Method, submethod, established family, or composite whole is asserted.

Reopen to the test-rig capability/resource decision if two of the next three comparable delays occur while required evidence is complete and the rig is unavailable. That observation changes the subject rather than merely lowering a Method score.

### 3. Separate observed differentiation, causal support, and today's decision

The twenty-release window records eight reopened releases. Six of those eight had a late supplier-pinout/integration-bundle mismatch before rig reservation. The rig was available in seven of the eight reopened releases; two rig-outage cases elsewhere in the window completed under the same procedure when backup capacity appeared. Two earlier comparable quarterly-cadence releases reconciled the same versioned input before their safety boards and did not reopen.

`DA-EC417-CadenceDifferentiation-1` retains a partial descriptive account of the counts and timing/co-occurrences above. This application does not supply the dated source editions, variant appearances, selection decisions, and diagnostic rival comparison needed to complete the differentiation history. Keep that reconstruction gap; these observations neither complete ME.19's historical result, choose B2, nor identify a causal effect. ME.19:5.1 supplies a filled constructed signoff history to show that separate operation, not evidence about EC-417.

The receiving causal-use question is `CUQ-EC417-CadenceEffect-1`: would entering provisional-evidence reconciliation at `D-21`, rather than waiting for signed evidence at `D-8`, reduce mismatch-related reopenings in EC-417-like releases for this team, supplier, and change class? `CUR-EC417-CadenceEffect-1` records `causalUseClaimKind = causalEffectClaim` and target rung `interventionalActionRung`.

Its actual components are:

- `evidencePathRefs = [EP-EC417-BundleSequence-20, EP-EC417-RigAvailability-20, EP-EC417-QuarterlyCadence-2]`;
- `empiricalDataRegimeRefs = [EDR-EC417-NaturalReleaseHistory]`;
- no identification result and no estimate result;
- common threat screen `CTS-EC417-CadenceEffect-1`, with `causalUseQuestionRef = CUQ-EC417-CadenceEffect-1`.

The threat screen keeps intervention consistency, confounding/exchangeability, overlap, interference, missingness/selection, measurement, and target transport as live threats; temporal ordering alone is clear. `routedThreatRefs = []`: no specialist result closes a live threat. The C.28 verdict is therefore **`unsupported`**.

No positive interventional causal reliance is supported. The observed timing and co-occurrence remain in separate non-causal result `DC-EC417-CadenceMismatch-1` as a trial hypothesis and design constraint. Unsupported uses include the claims that cadence mismatch caused the reopenings or that B2 will reduce them. Reopen only when a governed comparison or replayable identification/bound result varies reconciliation timing while rig availability, approver capacity, outcome definition, and evidence access are controlled or explicitly modeled.

Today's architecture decision remains separate. `AD-EC417-B2-Trial-1` may consume the non-causal mismatch result, capacity calculation, the covering trace/safety/release assignments, `PERM-TraceAcceptReject-17`, the two independently supported direct authority relations, and reversibility to choose a bounded trial. It may not consume the `unsupported` causal-use result as positive evidence.

### 4. Recover candidate accounts only when ordinary Method recovery is insufficient

Ordinary `A.3.1.MR` recovery suffices for `M-HW-Verify` and `M-SW-Integrate`. The evidence-reconciliation question enters `ME.18` because oral version judgments and supplier/internal workarounds are absent from the records and the receiving decision needs a stronger account.

The evidence programme keeps its moves distinct:

- occurrence observation and artifacts record overt evidence handling;
- Critical Decision Method probes recover recalled cues, options, judgments, and counterfactual reflections;
- event-log comparison records recurrence and deviation;
- the twelve-plus-one sample, claim-to-evidence matrix, contradiction-by-scope rule, and held-out discriminator are the bounded expert synthesis.

Four firmware-only and four internal harness-plus-firmware releases accepted versioned provisional pinout evidence before safety closure. Four supplier-originated releases required signed evidence at closure. Four boards were observed. CDM probes involved two supplier, two software, one hardware, and one safety practitioner.

The thirteenth supplier-originated case is reserved unseen. Before inspection, the internal account predicts that explicit version/uncertainty plus later reconciliation is sufficient; the supplier account predicts that supplier-originated geometry will require the signed-evidence branch; the rig-capacity rival predicts that progress follows rig availability. The held-out case presents supplier-originated geometry, the signed-evidence cue, a decision to wait for the signed branch, the expected branch variation, and a completed result. It supports the supplier account without a load-bearing surprise, contradicts neither account outside its scope, and leaves transfer unresolved.

`C-Evidence-Reconcile-Internal` and `C-Evidence-Reconcile-Supplier` remain scoped candidate Method accounts. No occurrence, interview, event regularity, majority pattern, or held-out fit admits either as a Method or proves effectiveness, population frequency, or causality.

### 5. Build the repertoire and criteria without preselecting an architecture

`ME.2` returns an inspectable repertoire for the relation comparison:

| Subject | Exact current inputs for this replay | Source use | Limit |
| --- | --- | --- | --- |
| `M-HW-Verify` | A.3.1 identity result `IDR-HW-Verify-17`; description edition `MD-HW-Verify-4.2`; evidence window `EW-HW-Verify-EC397-416` covering `EC-397` through `EC-416`; established input/result relation `IR-HW-Verify-17` | accepts the named harness/pinout edition and returns `VR-EC417-H17` | no established family or Method-lineage relation follows from co-listing |
| `M-SW-Integrate` | A.3.1 identity result `IDR-SW-Integrate-17`; description edition `MD-SW-Integrate-4.8`; evidence window `EW-SW-Integrate-EC397-416` covering `EC-397` through `EC-416`; established input/result relation `IR-SW-Integrate-17` | consumes the named firmware, harness, and evidence edition and returns an integration record that preserves edition, uncertainty, and use | no evidence-reconciliation or whole-Method identity follows |
| `M-Supplier-Approve` | A.3.1 identity result `IDR-Supplier-Approve-17`; description edition `MD-Supplier-Approve-H17.3`; evidence window `EW-Supplier-Approve-12` covering the twelve preceding supplier-originated releases; established input/result relation `IR-Supplier-Approve-17` | consumes the supplier revision and evidence bundle and returns signed approval or the explicit missing-approval stop | supplier transfer beyond the named source window remains open |
| `M-Release-Authorize` | A.3.1 identity result `IDR-Release-Authorize-17`; description edition `MD-Release-Authorize-2026Q3`; evidence window `EW-Release-Authorize-20` covering the named twenty releases; established input/result relation `IR-Release-Authorize-17` | consumes the named evidence, verification, assignment, and authority results and returns release, withhold, or next-slot authorization | it does not perform the safety-evidence decision or create release authority |
| `C-Evidence-Reconcile-Internal` | candidate-account edition `CA-ER-Internal-1`; source window `EW-ER-Internal-8` covering four firmware-only and four internal harness-plus-firmware releases | derived from those eight internal cases and their artifacts | Method identity and supplier transfer remain open |
| `C-Evidence-Reconcile-Supplier` | candidate-account edition `CA-ER-Supplier-1`; source window `EW-ER-Supplier-4+1` covering four supplier cases plus the held-out thirteenth case | derived from that bounded source set | Method identity, population scope, and relation to the internal account remain open |
| `C-AI-Trace-Review` | candidate-account edition `CA-AI-Trace-Review-1`; exact source contents `ATP-2`, `HDR-TraceAcceptReject-17`, and `RES-TraceAcceptReject-17` | `ATP-2` contributes prompt-and-guard description content; `HDR-TraceAcceptReject-17` documents the one dated human Work occurrence in this filled case, `W-TraceAcceptReject-17-01`, and identifies its distinct exercise-evidence carrier `EV-PEX-TraceAcceptReject-17-01`; `RES-TraceAcceptReject-17` records its result `RES-TraceAcceptReject-17-01`; the AI provider and its input suggestion remain separate Systems/content | no autonomous authority, effectiveness, transfer, Method identity, family, causation, superiority, applicability, or composition claim |

The four Methods alone remain in local comparison locator `LG-EC417-ReleaseMethods`; the three accounts are adjacent repertoire entries with preserved statuses. The values in the table are pinned for reliance from `D-21` through `D0`. For an identified Method, rely on its current A.3.1 identity result, description edition, evidence window, and only each established relation needed by the use. For a candidate account, rely on its current account edition, named source contents or source window, preserved status and limits, and only already-established relations needed by the use; missing Method identity or a generic input/result relation remains an open limit, not a required field. If a required value is absent or has changed, stop repertoire reliance and reopen only that `ME.2` entry.

At `D0` this application ends its reliance window and claims no later source-revalidation result. Unresolved R may motivate later planning, but this application asserts no post-`D0` recovery WorkPlan, PlanItem, intended performance, planned start/end, performer condition, qualification/currentness result, readiness result, assignment, permission/authority, or later Work occurrence.

When later non-AI recovery needs coordination, the project may create a new `A.15.2` WorkPlan; `A.15.2` itself makes no plan prerequisite for every later Work. Such a plan would be an episteme about possible Work: it would neither make an ME.2 input current nor establish readiness, assignment, permission/authority, or an `A.15.1` dated Work occurrence. Absence of a plan neither establishes nor prohibits later Work; any later planned or unplanned Work still needs its own independently governed occurrence and conditions.

This application ends with withhold/next-slot. `C-EC-Release-v2` stays outside the membership table as a proposed-whole architecture subject; missing family, Method-lineage, account-identity, and AI-transfer positions remain reasons to stop.


`ME.3` states candidate-neutral contributions and locates every condition with its actual subject. The case separately names the Systems, performed decision Work and results, covering assignments, and independently obtaining permission or direct decision-authority relations:

| Human System and performed decision Work | Covering assignment | Permission or direct decision-authority relation |
| --- | --- | --- |
| `TraceReviewer-17`; bounded set `W-TraceAcceptReject-17` returns accept/reject for each AI suggestion actually used; this filled case contains `W-TraceAcceptReject-17-01` | `ASG-TraceReview-17`, `D-21` through `D0` | exact grant occurrence `PERM-TraceAcceptReject-17` and its currentness result `CUR-PERM-TraceAcceptReject-17-D21-D0`; the register entry is evidence, and the dated Work-to-grant exercise is a separate relation |
| `SafetyReviewer-17`; `W-SafetyEvidenceDecision-17` returns accept/reject for B2 entry, closure, or recovery evidence | `ASG-SafetyReview-17`, `D-21` through the next authorized slot | `AUTH-SafetyEvidence-17`: subject `SafetyReviewer-17`, named evidence-decision scope and that window, basis `SafetyDecisionCharter-17`; reliance needs the matching register entry and linked safety-decision record |
| `ReleaseDecider-17`; `W-ReleaseDecision-17` returns branch-entry and release/withhold/next-slot decisions | `ASG-ReleaseDecision-17`, `D-21` through the next authorized slot | `AUTH-ReleaseDecision-17`: subject `ReleaseDecider-17`, selection of A or at most three B2 trials and the release disposition in that window, basis `ReleaseDecisionCharter-17`; reliance needs the matching register entry and linked release-decision record |

The baseline B2 branch relies on one filled `A.2.8.PER` grant occurrence rather than inferring permission from a charter or register:

| Grant field | Filled case value |
| --- | --- |
| relation and beneficiary participant | `PERM-TraceAcceptReject-17 : GrantedPermissionRelation@Context`; `PermissionBeneficiarySlot` selects `beneficiarySystemRoleAssignmentRef=ASG-TraceReview-17`. `TraceReviewAssignment` is declared as a `U.SystemRoleAssignment` species; occurrence `ASG-TraceReview-17` has admitted System `TraceReviewer-17` as holder, `HumanTraceReviewer` as assigned kind, and covers `W-TraceAcceptReject-17-01` within `D-21` through `D0`. |
| permitted-action participant | `PermittedActionSpecificationSlot=ACT-TraceAcceptReject-EC417-e1`: inspect one non-confidential provider-generated requirement-to-test-link suggestion for `EC-417` and return accept or reject. It grants no safety-closure or release decision. |
| instituting act and grantor assignment | At `D-22 16:00`, admitted System `EngineeringAssuranceLead-17` performs speech act `SA-GrantTraceAcceptReject-17` under `ASG-TracePermissionGrantor-17 : TracePermissionGrantorAssignment`, a declared `U.SystemRoleAssignment` species whose holder is that System and whose assigned kind is `TracePermissionGrantor`; the act records `institutes.permissions=PERM-TraceAcceptReject-17`. The assignment grounds the holder and kind but neither acts nor supplies decision authority by form. |
| policy, scope, and window | `grantValidityPolicyRef=TraceReviewCharter-17-e1`; its predicate admits the exact grantor assignment and speech act for `scope=CS-EC417-AITraceSuggestions`. `validityWindow=D-21 00:00..D0 23:59`; the policy is not single-use. |
| currentness and ending | `CUR-PERM-TraceAcceptReject-17-D21-D0` checks the exact participants, instituting act, grantor assignment, policy edition, ClaimScope, and window and records no revocation or supersession at each EC-417 trace-decision checkpoint through `D0`. `DRE-TraceAcceptReject-17-e1` in `DecisionRightsRegister-17` carries evidence for that result; it neither institutes nor equals the grant. `revocationOrSupersessionRef=absent`; the occurrence expires at `D0` and has no carry-forward. |

The occurrence identity is the tuple `SA-GrantTraceAcceptReject-17`, beneficiary assignment ref `ASG-TraceReview-17`, action-specification edition `ACT-TraceAcceptReject-EC417-e1`, policy edition `TraceReviewCharter-17-e1`, ClaimScope `CS-EC417-AITraceSuggestions`, and the `D-21..D0` effective interval. A change in any member ends or splits the occurrence.

Only one provider suggestion is used in the filled case: `AI-TraceSuggestion-EC417-01`. At `D-21 10:00..10:20`, admitted System `TraceReviewer-17` performs `W-TraceAcceptReject-17-01` under `ASG-TraceReview-17`; the Work instantiates `ACT-TraceAcceptReject-EC417-e1` within the grant scope and returns `RES-TraceAcceptReject-17-01=accept`. `PEX-TraceAcceptReject-17-01 : PermissionExerciseRelation@Context` connects that dated Work to the exact `PERM-TraceAcceptReject-17` occurrence, with `beneficiarySystemRoleAssignmentRef=ASG-TraceReview-17`, `exerciseScope=CS-EC417-AITraceSuggestions`, and `exerciseInterval=D-21 10:00..10:20`. `EV-PEX-TraceAcceptReject-17-01` is the ledger evidence about this exercise and remains distinct from the exercise relation. No second suggestion, Work result, or exercise is asserted; every later used suggestion would require its own dated Work, result, currentness check, and Work-to-grant exercise relation.

Assignment, permission/authority relation, performed Work, and decision result imply none of one another. Capability, responsibility, access, currentness, readiness, and evidence remain separate as well. The AI provider holds none of the human assignments or relations. `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17` end at `D0`; continuing safety or release assignments and authority extend neither trace relation. For this worked application, after `D0` no new AI suggestion is requested, accepted, or used, and no later trace-review assignment, permission, Work, result, or exercise is claimed. Every earlier trace-review occurrence and result remains in the evidence history.

The ME.2 discussion above states the future-recovery boundary for this application: unresolved R may motivate planning, but no post-`D0` recovery WorkPlan is asserted, and a later plan would establish none of currentness, readiness, assignment, permission/authority, or Work.

| Criterion | Actual subject and bound | Evidence or stop |
| --- | --- | --- |
| trace correspondence | released result: each affected safety requirement links to one or more named current implementation revisions and one or more named verification results; every correspondence link is inspectable | versioned trace record; absence of either required link kind stops safety closure |
| confidentiality | supplier geometry and AI-provider access relation | geometry remains outside the provider; any exposure stops the AI-supported route |
| decision-Work assignments | the three admitted human Systems and their three baseline `ASG-*` occurrences | every performed occurrence matches its covering assignment's holder, Work scope, and window; missing or mismatched assignment fails without erasing the Work |
| permission and decision authority | `PERM-TraceAcceptReject-17`, `AUTH-SafetyEvidence-17`, `AUTH-ReleaseDecision-17`, and their governed results | APP section 5 records the grant participants and grounds once; `CUR-PERM-TraceAcceptReject-17-D21-D0` supports pre-Work currentness, `PEX-TraceAcceptReject-17-01` relates dated Work to that grant, and `EV-PEX-TraceAcceptReject-17-01` remains evidence about the exercise; missing, out-of-scope, circularly supported, or AI-provider authority fails |
| evidence state | provisional/signed evidence inputs, their relation, and safety-closure guard | signed evidence supersedes the explicit provisional edition only for safety-closure reliance; provisional uncertainty, earlier Work use, and the provisional-to-signed relation remain traceable; missing signed evidence stops closure |
| reversibility | integration Work and implementation state | rollback within one hour until `D-1`; failure stops an early-integration route |
| capability/support | named hardware/safety capabilities, PLM/CI edition recovery, pinout schema, and rig access | missing capability, unknown input edition, or unavailable verification route blocks the contribution that relies on it |
| peak burden | safety-engineer allocation on the selected peak day | at most `0.40` of an eight-hour day, or `3.20 h`; transferred burden remains visible |
| board burden | each joint-board Work occurrence | at most 45 minutes per board |
| release stop | `W-ReleaseDecision-17`, `ASG-ReleaseDecision-17`, `AUTH-ReleaseDecision-17`, and receiving result | missing signed evidence, required verification, covering assignment, or direct authority relation yields withhold or next-slot, never silent waiver |

These criteria admit no Method and select no alternative. Signed-first, provisional-first, supplier-preparation, and safety-preparation variants remain serious possibilities.

### 6. Recover package contributions and qualify individual subjects

The incumbent “release methodology” mixes unlike material. `ME.4` returns open navigation sections while preserving kinds:

- Methods: the four identified Methods;
- candidate accounts: the two reconciliation accounts, `C-AI-Trace-Review`, and proposed whole `C-EC-Release-v2`;
- descriptions and source claims: stage table, release checklist, supplier procedure, AI prompt, bundle records, and evidence grades;
- Systems/support/access: PLM, CI, test rig, AI provider, and provider-access relation;
- capabilities/assignments: safety competence, supplier-configuration responsibility, and `ASG-TraceReview-17`, `ASG-SafetyReview-17`, and `ASG-ReleaseDecision-17`;
- permissions/authority: `PERM-TraceAcceptReject-17`, `AUTH-SafetyEvidence-17`, and `AUTH-ReleaseDecision-17`, distinct from the assignments, performed Work, and decisions;
- inputs/results/premises: pinout schema, evidence bundle, verification result, and confidentiality premise;
- relations: production/use, schema correspondence, provider access, allocation, responsibility, permission, and authority.

These are dossier navigation sections, not technical kinds or Method components. Only identified Methods and candidate accounts travel to individual qualification, each with the dependency slice needed to judge it.

`ME.5` returns status-preserving individual results:

| Subject | Individual return |
| --- | --- |
| `M-HW-Verify` | qualified to accept the affected change/pinout version and produce the verification result under named rig and hardware-capability conditions |
| `M-SW-Integrate` | qualified to produce an integration record that preserves the exact provisional or signed edition, uncertainty, and earlier-use history; later signed evidence supersedes provisional only for closure reliance; one-hour reversibility still applies |
| `M-Supplier-Approve` | qualified to produce signed approval or the explicit missing-approval stop under named access and supplier responsibility |
| `M-Release-Authorize` | qualified to return release, withhold, or next-slot authorization when `ReleaseDecider-17` performs `W-ReleaseDecision-17` under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17`; Work, assignment, and authority remain separate |
| two reconciliation accounts | retained as scoped candidate accounts; `A.3.1` identity remains open |
| `C-AI-Trace-Review` | retained as a human-governed candidate account that specifies a trace-suggestion contribution; `TraceReviewer-17` performs accept/reject Work under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17` |

The provider-default AI proposal is rejected at entry because it supplies neither an identified Method nor a candidate Method account, would expose confidential geometry, and names no admitted human performer, covering assignment, or permission/authority relation.

Local schema correspondence `A-17` maps signed or explicitly provisional pinout-version fields to the integration bundle, preserves the exact edition and uncertainty used, and is supported on five stored bundles for the named editions. Later signed evidence does not erase a provisional basis. It is one local connection, not whole compatibility.

Another project needing only hardware verification can stop with the individual qualification of `M-HW-Verify`; it does not need a package-recovery or architecture-comparison result. A project whose only useful result is the bounded qualification of `C-Checklist-Reconcile` can retain that subject as a candidate account with A.3.1 identity still open and stop without calling it a Method. A project investigating supplier reconciliation can likewise stop with the retained supplier account. EC-417 continues because combined evidence timing, allocation, support, authority, and recovery burden change the release decision.

### 7. Compare A, B, B2, and R across the structures that change the decision

The alternatives share the receiving result but arrange Work and burden differently:

| Alternative | Work and evidence arrangement | Allocation and stop |
| --- | --- | --- |
| `A` | use signed evidence before integration and hold one final reconciliation board | choose prospectively at `D-21` when signed evidence is available or early-integration entry conditions are absent; under baseline `D-8` availability it misses the target slot by thirteen days |
| `B` | integrate from an explicit provisional edition at `D-21`, preserve its uncertainty and use, and reconcile it to signed evidence at `D-8`; safety engineer performs all signed-delta preparation | `D-8` safety demand is `2.00 + 0.33 + 2.07 = 4.40 h`, or `0.55`; reject under the `0.40` peak-day limit |
| `B2` | same Work order and evidence-history rule as B, but supplier-configuration role performs `1.60 h` of signed-delta preparation | `D-8` safety demand is `0.40 + 0.33 + 2.07 = 2.80 h`, or `0.35`; moved supplier burden remains explicit |
| `R` | after B2 entry and missing signed evidence at closure, preserve performed integration plus the provisional edition, uncertainty, and earlier use; on signed evidence, record the relation/delta, re-baseline, repeat comparison and affected verification, then retain, roll back, or repeat integration | withhold release; signed evidence supersedes provisional only for closure reliance; known minimum burden is `1.60 h` supplier plus `2.80 h` safety, with affected verification/integration rework recorded separately |

The provisional board occurs on `D-21`; the signed-evidence board occurs on `D-8`. Both last 20 minutes and therefore remain under the separate 45-minute limit. They do not occur on the same day. Per-release safety effort is `4.73 h` for B and `3.13 h` for B2 after the separate `D-21` board is included. The selected `D-8` peak-day result and per-release totals answer different burden questions.

`ME.6` keeps several structures distinct:

- **Method relations:** the four identified Methods are co-used; every composition/order relation for `C-EC-Release-v2` remains proposed;
- **Work relations:** A is signed-first; B/B2 are provisional-first then signed reconciliation; each B2 branch that uses AI suggestions contains bounded human Work set `W-TraceAcceptReject-17` with one accept/reject occurrence per used suggestion; R can occur only after B2 entry, retains already-performed Work, and repeats that trace-review Work for every repeated AI suggestion;
- **allocation:** B overloads the safety engineer, while B2 transfers `1.60 h` and stays within the peak bound; admitted Systems `TraceReviewer-17`, `SafetyReviewer-17`, and `ReleaseDecider-17`, their three covering assignments, trace permission `PERM-TraceAcceptReject-17`, and the two direct authority relations remain separate;
- **subject/support/permission/authority:** the three decision Systems and their Work remain distinct from their assignments, the trace permission, and the two direct authority relations; supplier configuration, PLM, test rig, and AI provider retain separate responsibility/access/support relations;
- **description correspondence:** checklist order corresponds only partially to Work overlap and branch stops;
- **cultural relation:** retention of a weekly-integration practice remains a later cultural-continuation question.

`AD-EC417-B2-Trial-1` selects only a prospective three-release B2 trial under `ASG-TraceReview-17`, `ASG-SafetyReview-17`, `ASG-ReleaseDecision-17`, `PERM-TraceAcceptReject-17`, `AUTH-SafetyEvidence-17`, `AUTH-ReleaseDecision-17`, capacity, confidentiality, evidence, and reversibility conditions. It consumes `DC-EC417-CadenceMismatch-1` as a non-causal rationale and treats the causal-use verdict as `unsupported`. A remains a pre-entry alternative. R is a post-entry recovery and can never become a retrospective A occurrence. No obtaining ArchitectureRelation or `methodPartOf` fact is asserted.

### 8. Return a proposed-whole account and a bounded trial

`ME.7` receives `C-EC-Release-v2` with:

- intended result: a traceable safety-relevant release under named evidence and authority conditions;
- reusable invariant: reconcile the exact provisional or signed evidence edition with the integration bundle before safety closure;
- participants and contributions: the four identified Methods, two reconciliation accounts, the three admitted decision Systems, their decision Work/results and covering assignments, and separately governed support/capability/permission/authority subjects;
- inputs/results: pinout/evidence state, implementation revision, verification result, signed approval or stop, and release authorization;
- variation: signed-first A or bounded provisional-first B2 before entry; post-entry recovery R;
- bounds: confidentiality, human AI-suggestion decision, evidence edition/uncertainty/history, signed-before-closure reliance, peak burden, board duration, rollback, covering assignments, and named permission/authority relations;
- reidentification rule: the account changes when its receiving result, invariant, participant contribution, evidence branch, or authority/stop rule changes materially.

The four participant Methods are identified, but the proposed whole is not. The result is therefore a prospective candidate Method account, proposed relation sets, guards, adapters, fallbacks, stops, variation points, and a trial WorkPlan. Writing or selecting that account creates neither a world-side Method, obtaining composition, ArchitectureRelation, nor MethodDescription.

At `D-21`, `ReleaseDecider-17` performs `W-ReleaseDecision-17` under `ASG-ReleaseDecision-17` and `AUTH-ReleaseDecision-17`, after `SafetyReviewer-17` performs the needed evidence decision under `ASG-SafetyReview-17` and `AUTH-SafetyEvidence-17`. B2 entry also requires `TraceReviewer-17` to perform accept/reject Work under `ASG-TraceReview-17` and the current `PERM-TraceAcceptReject-17` for every AI suggestion actually used by the branch. The filled baseline is `W-TraceAcceptReject-17-01` and `PEX-TraceAcceptReject-17-01` from section 5; any additional used suggestion would require a distinct dated Work, result, currentness check, and exercise relation.

The decision chooses A before integration if signed evidence is already available or if versioned provisional evidence, supplier preparation, confidentiality, the trace-review assignment or permission, or a safety/release assignment or authority condition for B2 is absent. Under the baseline `D-8` assumption and with every B2 entry condition satisfied, it may authorize only three B2 releases.

Each B2 occurrence must keep confidential geometry outside the provider, record `TraceReviewer-17` accept/reject for every AI suggestion under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17`, hold its boards on the named days, stay at or below `3.20 h` peak safety effort, obtain signed evidence before closure, and reach the target slot or record why it did not. A confidentiality, assignment, permission, or authority breach stops B2 immediately.

If signed evidence is missing at `D-8`, withhold release and enter R. R preserves the performed integration record, provisional edition, uncertainty, and earlier decision use. If signed evidence arrives by `D0` while the existing evidence and reversibility guards still hold, the team records its relation and delta to provisional, re-baselines the bundle, repeats the comparison and affected verification, and records whether early integration was retained, rolled back, or repeated.

If closure is still unresolved at `D0`, `ReleaseDecider-17` returns withhold/next-slot and this application's R occurrence ends as a failed B2 trial. The application claims no comparison, verification, decision, or AI-supported Work after `D0`; no new AI suggestion is requested, accepted, or used. Under the section 5 boundary, unresolved R may motivate planning but no post-`D0` recovery WorkPlan or later Work is asserted.

If later non-AI recovery needs coordination, the project may create a new `A.15.2` WorkPlan; this application imposes no general plan prerequisite and does not exclude otherwise valid unplanned Work. Whether planned or unplanned, later Work would need its own ME.2 qualification/currentness results, readiness, assignments, permission/authority, and `A.15.1` occurrence as applicable.

These boundaries do not rewrite any earlier Work or evidence basis. Signed evidence supersedes provisional only for safety-closure reliance. Two capacity, mismatch, or recovery failures revise or reject B2 before any fourth release.

### 9. Configure and test the enactment-support arrangement before claiming that a Method Base works

The B2 material now exists, but that does not show that a person can find the current edition, distinguish candidate from admitted content, tailor the live branch, or stop before a tool overreaches. `ME.10` therefore starts from three named user tasks rather than from a repository or platform design. The bounded support use `USE-EC417-B2-Support-1` asks whether `TraceReviewer-17`, `SafetyReviewer-17`, and `ReleaseDecider-17` can use the B2 material for `WP-EC417-B2-Trial-1` under the existing confidentiality, evidence, assignment, permission, authority, reversibility, and `D0` conditions.

#### 9.1 Fix the same three task rows before comparing support configurations

| User task | Mandatory observation and stop | Configuration evidence |
| --- | --- | --- |
| retrieval by `TraceReviewer-17` | recover `MBE-EC417-B2-1`, candidate status, prompt episteme `ATP-2`, the confidentiality boundary, and the `D0` stop | one performed retrieval through `SYS-EC417-PLM-1` |
| tailoring by `SafetyReviewer-17` | use a non-confidential fixture, preserve signed-before-closure, reject a stale edition, and stop on missing permission or authority | one performed tailoring task through `SYS-EC417-CI-1` |
| branch selection by `ReleaseDecider-17` | distinguish pre-entry A, bounded B2, and post-entry R; stop B2 when assignment, permission, authority, confidentiality, or reversibility is absent | one performed selection task through `SYS-EC417-PLM-1` |

Published files and manual lookup are candidate configurations with no performed task evidence for these three rows, so those configurations remain untested rather than failed. Adding an interaction with `SYS-EC417-AIProvider-1` and feedback Work or a feedback receiving relation also remains untested: no mandatory row needs either, and this support test contains no provider interaction, used AI suggestion, human review of such a suggestion, feedback Work, feedback SpeechAct, or feedback receiving use. The bounded PLM/CI candidate configuration is the only one with one observation for every current row. This makes it supported for the three rows; it does not make it globally smallest or superior to every alternative.

#### 9.2 Admit the two entry epistemes to the Method Base

`MBC-EC417-B2-1` is the project Method Base entry collection for this support purpose and window. It keeps its project namespace, current entry-disposition rule, and continuity condition. The two candidate entries are separate C.2.1 epistemes:

- `ECA-EC417-C-Release-v2-1` states the explicit candidate status and current account of `C-EC-Release-v2`;
- `ERP-EC417-WP-B2-1` is about WorkPlan `WP-EC417-B2-Trial-1`, not about performed release Work.

Entry membership is an instituted relation, not a folder listing. `SYS-EC417-MB-PermissionGrantor-1`, its obtaining grantor assignment `RA-EC417-MB-PermissionGrantor-1`, and admitted permission-granting SpeechAct `SA-EC417-MB-PermissionGrant-1` ground exact permission `PERM-MBENTRY-EC417-1` for curator assignment `RA-EC417-MB-Curator-1`, action specification `PAS-EC417-MB-AdmitRemove-1`, scope `SCOPE-EC417-MB-Entries-1`, and the `D-21` through `D0` window. `AG-EC417-MB-Curator-1` and the obtaining curator assignment supply the A.13 performer core; the permission itself creates neither Work nor a result.

`MECH-EC417-MB-EntryDisposition-1` declares reusable operation `settleEntryDisposition(entry, collection, admissionWork) -> entryDisposition`. Its closed local value kind contains exactly `MBEDV-EC417-Admit`, `MBEDV-EC417-Remove`, and `MBEDV-EC417-Stop`; display words, records, plans, and assertions are not those values. A completed application requires the curator to identify the entry episteme, the collection, the entry-disposition rule, and the admission question; check kind and status, provenance, purpose fit, applicability, return condition, and current membership; and then perform one observable branch-closing act. Without that act there is inspection Work but no completed application or result binding.

At `D-21 10:00–10:08`, admitted Work `W-MBA-EC417-ECA-1` applies the operation to the candidate-account episteme. At `10:10–10:18`, admitted Work `W-MBA-EC417-ERP-1` applies it to the WorkPlan episteme. Each Work has its own performance history, extent, `WorkContainedInEC417MethodEngineering` occurrence, A.13 core, A.15.1 admission, post-admission assignment attribution, and `PERM-MBENTRY-EC417-1` exercise. Applications `APPL-MBENTRY-EC417-ECA-1` and `APPL-MBENTRY-EC417-ERP-1` end only at their pair-specific positive approval acts; terminal bindings `RB-MBENTRY-EC417-ECA-ADMIT-1` and `RB-MBENTRY-EC417-ERP-ADMIT-1` carry exact value `MBEDV-EC417-Admit`.

Those facts institute `MBB-EC417-ECA-1` and `MBB-EC417-ERP-1` as the two `MethodBaseEntryBelongsTo@Project` episodes. Each episode is identified by its exact entry, collection, and maximal continuous interval. A repeated positive result during an open episode creates no second membership; removal requires its own permitted negative application and result. No such removal obtains through `D0`.

#### 9.3 Test actual use and keep the structure gap separate

The collection makes the two epistemes eligible for the support use. Three separately admitted Work occurrences establish whether the named tasks succeeded:

| Performed user Work | Direct System use and observed result | Boundary |
| --- | --- | --- |
| `W-MESUP-EC417-Retrieve-1`, `TraceReviewer-17`, `10:30–10:42` | `SSUW-EC417-Retrieve-PLM-1` relates that Work to `SYS-EC417-PLM-1`; the user retrieves `MBE-EC417-B2-1` and recovers candidate status, `ATP-2`, confidentiality, and the `D0` stop | no general access entitlement, capability, or authority follows |
| `W-MESUP-EC417-Tailor-1`, `SafetyReviewer-17`, `10:42–10:55` | `SSUW-EC417-Tailor-CI-1` relates that Work to the non-confidential `SYS-EC417-CI-1` fixture; the user preserves signed-before-closure and rejects the stale edition | this neither performs release Work nor approves closure |
| `W-MESUP-EC417-Select-1`, `ReleaseDecider-17`, `10:55–11:08` | `SSUW-EC417-Select-PLM-1` relates that Work to `SYS-EC417-PLM-1`; the user distinguishes A, B2, and R and applies the named B2 stops | the aid neither makes the release decision nor acquires authority |

Each `SupportSystemUsedInWork@EC417` occurrence requires the independently admitted Work, one exact admitted System, an actual input/output interaction, and use of the returned value in that task. Colocation, access, a click trace, or tool output is insufficient. Each Work keeps its own enacted support-use Method, performer core, containing-System relation, assignment, and post-admission attribution.

`RES-MESUP-EC417-B2-1` returns `task-pass` only for these three Work occurrences and their retrieval/status, tailoring/stale-edition, branch-selection, and stop observations. This support test includes no `SupportSystemUsedInWork@EC417` occurrence with `SYS-EC417-AIProvider-1`; retrieving `ATP-2` is not provider use. No feedback occurrence `SA-MESUP-EC417-FB-1` is asserted. A later failed task would need its own repair and rerun Work rather than a rewrite of these histories.

`PSO-EC417-B2-Use-1` remains a proposed organization whose four A.22 candidate groups stay separate: identified constituents; the two membership episodes and three direct PLM/CI-use occurrences; current-edition, status, confidentiality, signed-evidence, assignment, permission, authority, reversibility, and `D0` constraints; and the named support-use frame. The case has no selecting System, enacted selection Method, dated structure-selection Work, or direct participation or operation-binding basis. `ESA-EC417-B2-1` therefore returns `missing-selection-basis` and designates no selected `U.Structure`. That gap does not erase the task pass.

The membership episodes, their IBA assertion or evidence epistemes, optional construction account `MBCA-EC417-B2-1`, edition episteme `MBE-EC417-B2-1`, publication occurrence `PUB-MBE-EC417-B2-1`, named-use reliance episteme, proposed organization, selection-gap episteme, and task result remain distinct. Membership and publication do not prove usability; three task passes do not prove a general holder capability, Method fit, effectiveness, release performance, or selection of the proposed structure.

#### 9.4 Stop separately at the remaining Method Engineering questions

| Pattern question | EC-417 result or stop |
| --- | --- |
| ME.8 | `C-EC-Release-v2` remains a candidate account. Improve that account or a description of one admitted constituent Method; do not return a `U.MethodDescription` for the candidate whole. |
| ME.9 | Invoke ME.9 only for Method representation profile `MRP-EC417-B2-Review-1`, because two unlike actions must be related without becoming one view. Both return to candidate `C-EC-Release-v2` and current candidate-account episteme `ECA-EC417-C-Release-v2-1`. Preparation row `C37-EC417-B2-Prepare-1` has receiver `SafetyReviewer-17` and exact action ‘prepare and check the bounded B2 delta before release’; direct subject result `ERP-EC417-WP-B2-1` is a `C.2.1` episteme about proposed allocation and order, evidence entry, confidentiality, recovery, and stops while preserving WorkPlan status. A.2.4 classifies that preparation use, and A.10 path `P-APP-EC417-Prepare-1` returns `pass` in its current-edition window. The direct receiving governor is ME.6 decision `AD-EC417-B2-Trial-1`: its predicate compares A, B, and B2 against the receiving, capacity, confidentiality, assignment, permission, authority, evidence, and reversibility conditions; its actual outcome selects no more than three prospective B2 trials under those conditions. The preparation row is therefore `select` only as input to preparation and checking; the decision grants neither performed Work nor any assignment, permission, or authority. The row for reopening the candidate, `C37-EC417-B2-Reopen-1`, has receiver `MethodEngineer-17` and exact later action ‘decide which findings from performed trial Work reopen the candidate’. In this application the three-release statement remains WorkPlan `WP-EC417-B2-Trial-1`: no corresponding release Work has yet been admitted, no exact candidate-episteme/viewpoint-edition pair has been tested under `E.17.0`, and no direct receiving governor has returned a predicate and outcome for that reopen action. A.2.4 classification or an A.10 path cannot replace those missing results, so this row is `unresolved`. The cross-use profile records the shared evidence-entry, confidentiality, recovery, and stop correspondences, the selected preparation row, and the blocked reopen row; it keeps WorkPlan, any later Work, both actions, candidate readings, conformance judgments, and receiving results separate. It creates no super-view, Method admission, fit, transfer, worth, publication, or mathematical graph. |
| ME.10 | Keep `task-pass`, `missing-selection-basis`, instituted memberships, edition/publication results, and the provider/feedback gaps separate. A missing applicable collection rule, permission grant or exercise, admitted curator Work, completed entry-disposition application, or positive result binding returns that missing membership premise. A missing support System, direct System-use relation, constraint, dated user Work occurrence, failed task, or missing task result preserves the collection facts and returns that named support defect. |
| ME.10–ME.14 and ME.16 capability input | The current application supplies assignments and authority facts but no A.2.2 capability record for a person, AI System, team, or other holder. Any decision that needs holder, Work family, envelope, measures, qualification window, currentness, and evidence returns that missing input. Its absence alone does not establish a need for capability development. |
| ME.11 | The three-release statement remains a WorkPlan. Add a release only after the corresponding dated release Work occurrence, its performers, enacted constituent Methods, Systems, capabilities, relied-on relations, conditions, domain result, burdens, deviations, and authority facts obtain. The Work does not enact the candidate whole. |
| ME.12–ME.14 | ME.12 returns each correction to the maintained result it can affect. ME.13 stays on the candidate branch and cannot claim transfer before a performed held-out release situation. ME.14 compares A, B2, revised B2, and stop or next-slot while preserving burden, confidentiality, capabilities, Systems, Work, relations, recovery, side effects, reversibility, and evidence limits. `CUR-EC417-CadenceEffect-1` remains `unsupported`. |
| ME.15 | Maintain editions of `C-EC-Release-v2` as a candidate lineage until A.3.1 independently admits a Method with changed reusable semantics. Constituent Methods, descriptions, tools, and prompts remain separate. |
| ME.16 | For each release that actually occurs, keep Method or candidate changes separate from description, PLM/CI/AI Systems, support Work, access, capability, assignment, permission, authority, release Work, and release-result changes. Retain decision-relevant adequate existing capability on its current A.2.2 basis without requiring development; return that missing basis when needed. Only a required capability-change claim consumes an independently obtained development result or returns its missing/stale result and next governing action. Omit capability detail that cannot change the decision. |
| ME.17 | EC-417 supplies no C.20 Discipline recognition, bounded Method Engineering population, enacted Method Engineering variant, or cultural-relation evidence. Return those gaps; use the MeCaMinD, SRA, and Essence cases only for their separately evidenced transmission, organizational-selection, and institutional relations. |

### 10. Apply sensitivity without rewriting past Work

If signed supplier pinout is available at `D-21`, the prospective choice reverses to A before integration. A then reaches the target slot with one final board and avoids the provisional board, later signed-delta preparation, and post-entry recovery exposure. B2 remains only if another named conflict justifies its extra branch.

This sensitivity changes the current prospective decision. It does not relabel earlier B2 Work as A, erase a recovery occurrence, or prove that either alternative is generally better.

### Result and stop

The application returns:

- one selected Method-relation focus and a named non-Method reopen observation;
- an inspectable status-preserving repertoire and situated criteria set;
- a kind-preserving package dossier and individual qualifications;
- two scoped candidate reconciliation accounts with held-out limits;
- differentiation account `DA-EC417-CadenceDifferentiation-1`;
- `unsupported` causal-use result `CUR-EC417-CadenceEffect-1` and separate non-causal `DC-EC417-CadenceMismatch-1`;
- architecture decision `AD-EC417-B2-Trial-1`, with A pre-entry, B rejected on peak demand, B2 selected only for bounded trial, and R post-entry;
- proposed-whole account `C-EC-Release-v2` and its trial WorkPlan, with no obtaining composition claim;
- two instituted Method Base entry-membership episodes for the candidate-account and WorkPlan epistemes, with collection, edition, publication, construction-account, evidence, and reliance results kept separate;
- bounded support result `RES-MESUP-EC417-B2-1=task-pass` for exactly three performed PLM/CI user tasks;
- separate `ESA-EC417-B2-1=missing-selection-basis`, AI-provider-use, feedback, and holder-capability gaps; and
- candidate-status, same-Work/viewpoint, trial, coherence, fit or transfer, worth, lineage, introduction, and cultural-continuation stops for ME.8–ME.17.

Stop before release when signed evidence, verification, confidentiality, capability/support, named human authority, peak capacity, board duration, or rollback conditions fail. At `D0`, if R has not closed successfully, issue withhold/next-slot, close this application's R occurrence, and stop all AI-supported continuation; do not claim later Work merely because a next slot or continuing safety/release authority exists. Preserve all earlier Work and evidence history. Later non-AI recovery may use a new WorkPlan when coordination needs one; none is asserted here, and absence of a plan alone does not prohibit otherwise valid later Work. A plan would not itself establish the separate currentness, readiness, assignment, permission/authority, or dated-Work results.

Stop this enactment-support use at the current failed task, missing task result, missing membership premise, unresolved A.22 selection basis, capability gap, missing provider interaction, missing feedback Work, or missing feedback receiving relation. Membership does not repair a failed task; a task pass does not select a structure or prove a capability. Stop Method Engineering at any earlier useful result when no whole question remains. Reopen only the affected result when its subject, source edition/currentness, evidence window, authority, burden window, support task, System use, receiving criterion, trial observation, or relation truth changes.

The application establishes no causal effect, Method identity for any candidate account, effective composite Method, universal lifecycle, cross-domain transfer, general holder capability, selected A.22 support structure, AI-provider use or feedback return inside the support test, positive release Work, or broad cultural continuation. It supplies only the bounded support-use facts and pattern stops stated above.

# Framework Boundary and Refresh

## Intended use and ordinary non-use

Use this framework when a Method-related identity, architecture, description, support, evidence, change, or
continuation question blocks a practitioner decision. Use one pattern or a small cooperating set. Do not use it
merely because a project performs domain Work by a known Method, publishes a document, installs a tool, schedules
training, or wants a generic process diagram.

Return to the owning domain when the missing result concerns its subject, quantities, consequences, safety,
law, authority, or direct Method. A Method Engineering result can request and use such a specialist return; it
does not replace it.

## PatternID and reader order

`ME.*` is this framework's PatternID namespace. The numbers are stable addresses, not steps. The Parts provide
a reader route over six problem families. Logical dependencies in the Table of Contents mean only that one
result may consume another. Actual Work can overlap, branch, repeat, omit a result, or begin from a later pattern
when its inputs already exist.

## Practical-example declaration

| Semantic key | Public form |
| --- | --- |
| `ME-FOCUS` | Ordinary practical entry |
| `ME-ARCHITECTURE` | Ordinary practical entry |
| `ME-DESCRIBE-SUPPORT` | Ordinary practical entry |
| `ME-TRIAL-CHANGE` | Ordinary practical entry |
| `PLUS-ME` | Ordinary practical entry |
| `ME-PLUS-PRODUCE` | Ordinary practical entry |
| `ME-CARD-01` | Ordinary practical entry |


## Source use and currentness

R7 supplies the connected Method, description, Work, capability, instrument, variant, and culture synthesis at the source scope recovered for this framework. R10 supplies the project, process, and case viewpoints on one Work. These bounded uses do not claim coverage of every Guide contribution or of a later expanded corpus. Such a promise requires its own source-local recovery and reconstruction; it is not a prerequisite to an independently supported Method Engineering result.

Direct Method Engineering sources contribute situation-responsive construction, Method content and ecosystems, representation, verification, validation, evaluation, efficacy, effectiveness, professional Method evolution, organizational introduction, and transmission cases. Their findings remain limited to the studied firm, ecosystem, telecom enterprise, OEM, workshop family, Method family, or institutional publication record. Claims of universal transfer, causal effect, long-term retention, or superiority need further evidence. Each pattern states the exact source use and reopening condition for its claims.

Refresh only the affected pattern when a governing FPF distinction changes, a direct source changes practitioner action or case facts, a worked case can no longer support its branch, or replay exposes a missing independently useful Method Engineering move. A new source does not reopen the entire framework by default. ME.24 follows the changed premise through affected claims and uses; unknown dependency reach widens the question rather than licensing a claim that everything else is unaffected.

## FPF dependency and compatibility

**Depended-on state.** This edition selects **First Principles Framework (FPF) — Core Conceptual Specification, Version September 2026**, status **Normative kernel, eternal alpha**, at the current-pattern state of **2026-09-05**. The exact depended-on units are the FPF PatternIDs cited in this edition's Table of Contents dependencies and in each pattern's SoTA and Relations sections. Read `Current FPF` in each imported body as this selected dependency state, not an instruction to substitute whichever revision is newest when the reader opens it.

**Direct uses.** The dependency supplies transdisciplinary Method and episteme identities; use-bounded representation selection and co-use; direct relation and selected-structure governors; evidence and causal-use boundaries; Work, WorkPlan, performer, capability, permission, publication, comparison, selection, currentness, and cultural-continuation results. Each ME pattern names the exact subset it consumes. `C.37` retains authority over one receiver/action claim groups, their direct-result, reliance, receiving-result, exposure/loss, disposition, and return positions. ME.9 retains only the MethodDescription or candidate-account profile that relates those complete rows across Method uses; ME.10 retains only the Method-material task-set and support-configuration specialization. Common episteme, view, mathematical-lens, publication, structure, collection, and representation-use results remain with their FPF governors.

**Compatibility and migration.** This Method Engineering edition remains an account bound to the stated FPF state. A later compatible FPF change leaves unaffected ME results reusable. A changed relied-on Solution, predicate, kind, relation, or result form reopens only the consuming ME pattern and this dependency relation; migrate that dependency explicitly and issue a revised edition or migration account before claiming compatibility. Until that explicit revision, the stated dependency remains in force.

**Authority direction.** FPF does not depend on this DPF for the validity of its transdisciplinary results. A transdisciplinary discovery returns to FPF for its own architecture, review, and edition decision; Method Engineering keeps only the specialist remainder. Domain DPF results remain optional specialist returns with their producer's scope, evidence, authority, and stop.

## Representative case coverage

Use the cases below to examine different questions. They do not establish one shared entity history or a
universal evidence chain. For each case, limit the Method Engineering question and conclusion to what its
observations can support.

| Case | What it lets a practitioner inspect | Boundary retained |
| --- | --- | --- |
| H/L/W source-to-language application | source-local recovery, semantic allocation, description comparison, language relations, reconstruction and an affected source-change return | constructed application; no measured whole-production effectiveness, total-effort advantage or general transfer follows |
| EC-417 release decision | Method focus, candidate reconstruction, situational criteria, architecture alternatives, a prospective whole, and a named-user support test | constructed scenario; no Method identity, causal effect, transfer, effectiveness, or culture follows |
| SSFD in one automotive OEM | actual workplace projects, changed application situations, reported limitations, later observations, and impact evidence | the Method was used with a broader methodology; contribution and transfer remain bounded |
| sustainable-design Method workshops | comparison of three Methods and their components across many professional workshops | immediate self-report does not establish long-term product results or recombined-variant effectiveness |
| Halogen professional design practice | cyclic Method adaptation under changing project demands, practitioner skill, and organization | one multidisciplinary firm does not establish population frequency, causal improvement, or universal transfer |
| Digital Vaccine health-services ecosystem | situation-responsive Method construction and an unlike-domain ex-ante evaluation replay | one operating ecosystem and ex-ante evaluation do not establish long-term effect or transfer |
| MeCaMinD cards and Game Board | generation and progressive changes to the carrier, followed by enactment by five novice facilitators | qualitative sessions with several purposes do not establish long-term retention or causal superiority |
| security-risk assessment in one telecom enterprise | organizational selection through definition-of-done, release-checklist, forum, training, and later use/non-use observations | several interventions covary; no isolated cause or outside-enterprise transfer is established |
| OMG Essence editions | institutional generation, formal selection, publication, issue handling, machine-readable carriers, and memory across editions | publication and institutional selection do not establish recurring enactment, broad recognition, retention, or effectiveness |

The pattern bodies state which case they consume and the exact result or stop. A later reader should not join the
cases into one population, project history, or stronger evidence claim merely because they appear in one table.

## External result use

The framework can consume domain results from Systems Engineering, Human Capability Development, Organization
Change, Operations Management, Music and Dance Practice Engineering, Administration, finance, safety, law,
research, or another practice. It preserves the producer's scope, evidence, authority, and stop. A sibling DPF
may offer a reusable route when available; otherwise use the direct Method and source that can truthfully return
the needed specialist result.

## Edition return

**Method Engineering Principles Framework, 5 September 2026** designates the authored twenty-four-pattern framework episteme: its Readme, Table of Contents, Preface with the PLUS-ME profile and bounded production-MethodDescription, six Parts, the H/L/W worked application, the imported EC-417 cross-pattern application, framework boundary, and the exact pattern-body and application sources selected by the deterministic assembly. The edition name designates that claim-bearing framework account; a file is one carrier of it.

`METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md` is one generated all-in-one Markdown presentation carrier for the edition. The carrier presents the selected reader form. Publication occurrence, actual access or use, currentness beyond the stated dependency and source windows, Suite membership, another product's availability, source authority, and Work authority each need their own basis.

## Publication boundary

Pattern bodies are the authoritative working references. The Readme, Preface, Table of Contents, Card, and
cross-pattern application help readers enter and combine them; they do not replace their conditions or stops.
Repository paths, campaign state, review correspondence, source-set digests, and landing evidence are excluded
from this practitioner publication.
