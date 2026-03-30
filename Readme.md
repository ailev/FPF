# First Principles Framework (FPF) - Core Conceptual Specification

> Operating system for thought for engineering, research, and mixed human/AI teams.

**Author:** Anatoly Levenchuk (with AI-agents assistance)  
**Version:** March 2026  
**Status:** Normative kernel, "eternal alpha" - already used in working projects and development programmes, while still evolving.

FPF helps when the bottleneck is no longer raw ideation, but coordination.

It turns a vague multi-actor problem into:
- a bounded-context map and a stable shared vocabulary,
- explicit decision criteria, route guards, and comparison characteristics,
- a small portfolio of lawful alternatives or next routes,
- an evidence / test gap list, gates, and auditable hand-offs,
- a durable working form such as a UTS, a DRR, or another route-specific output form,
- aligned outputs for engineers, managers, researchers, and auditors.

Use FPF when:
- work is split across specialists, teams, or AI agents;
- the real-world oracle is slow, expensive, noisy, or risky;
- different audiences need different views of the same underlying work;
- your current vocabulary is breaking down;
- you need state-of-the-art (SoTA) work as a managed portfolio, not a leaderboard snapshot.

Do not start here when:
- one person or one team can solve the task end-to-end,
- the vocabulary is already stable,
- feedback is fast and cheap,
- the cost of semantic drift is low,
- or you mainly need a quick answer, not durable shared artefacts.

## Start here

FPF is a core conceptual specification and pattern language with multiple entry routes for engineering, research, and mixed human/AI teams. It is most useful when the hard part is coordination, vocabulary stability, explicit trade-offs, and clean hand-offs.

Choose your first route by the first honest burden, not by document order.
If you are new to FPF, read the route title and opening sentence first; use the pattern IDs only after you know the route matches your situation.

A first practical session should usually leave:
- a map of who means what and where the hand-offs are;
- explicit decision criteria, comparison characteristics, or route guards;
- a small alternative set when selection is part of the burden;
- a visible list of missing evidence or tests before commitment;
- a starter UTS (a structured term sheet for unstable or overloaded vocabulary), a starter DRR (a short decision-rationale record), or another route-specific output form.

If you first need to decide whether FPF fits your situation, start with `E.1-E.2`.
If you need to write or review patterns, start with `E.8` and `E.19`.

Use this repository as a route menu, not as one universal starter trunk:

1. **Project alignment**  
   Use this when: the team keeps mixing up responsibilities, working method, plans, and what actually happened.  
   You will leave with: a clean separation between responsibility, method, plan, and actual execution, plus a first work sheet or alignment frame.  
   Start with: `A.1.1`, then `A.15`, then `A.15.2 / A.15.3`, then `B.5.1`. Add `F.11` when method/work vocabulary itself must be aligned across contexts, and `F.9` where bridge discipline matters. Land on `F.17 (UTS)`.

2. **Partly-said / language-state discovery**  
   Use this when: you have a serious cue, concern, or emerging idea that is too important to ignore but too early to present as a settled claim, requirement, or work record.  
   You will leave with: a short preservation-and-routing note or cue pack that says what was noticed, how mature it is, and who should receive it next.  
   Start with: `C.2.2a`, then `C.2.LS / C.2.4-C.2.7`, then `A.16 / A.16.1 / A.16.2`, then `B.4.1 / B.5.2.0`, and only then move into the relevant endpoint owner.

3. **Boundary unpacking**  
   Use this when: contract, API, protocol, compliance, or SLA language is mixing rules, gates, duties, and evidence in one blurred boundary story.  
   You will leave with: a Claim Register, meaning a split list of rules, gates, duties, and evidence claims.  
   Start with: `A.6`, then `A.6.B`, then `A.6.C`. When the boundary text hides overloaded quality language or generic doing-words, continue with `A.6.P`, then `A.6.Q` or `A.6.A`.

4. **Lawful comparison / selection**  
   Use this when: you need to compare alternatives honestly, keep a disciplined shortlist live, or make a selection without hiding the comparison logic.  
   You will leave with: declared characteristics, a comparison frame, and sometimes a shortlist or acceptable option set rather than one forced winner.  
   Start with: `A.19:0`, then `A.17-A.19`, then `G.0`, then `A.19.CPM` and `A.19.SelectorMechanism`, and then `G.5`.

5. **Generator / state-of-the-art / portfolio kit**  
   Use this when: your first deliverable is a reusable search / harvest / portfolio scaffold, not a one-off recommendation.  
   You will leave with: a reusable kit that names scope, schools of thought, variants, and shortlist-ready outputs.  
   Start with: `A.0`, then `G.0`, then `G.1`, then `G.2` and `G.5`. When creative search or explore/exploit policy is already central, add `B.5.2.1` and `C.17-C.19` early.

6. **Same-entity rewrite / explanation / comparative reading**  
   Use this when: the main job is to restate, explain, re-render, repair, or compare something already written or published without quietly changing what it is about.  
   You will leave with: a rewrite, explanation note, repair note, or bounded comparison note that keeps the object of talk stable.  
   Start with: `A.6.3.CR` for same-entity retextualization, `A.6.3.RT` for representation-scheme transition, `E.17.EFP` for explanation-facing rendering, `E.17.ID.CR` for bounded comparative reading, and `E.17.AUD.LHR / E.17.AUD.OOTD` for local repair and authored-unit stability.

The older `A.0 -> A.1-A.3 -> B.3 -> F.17 -> E.9` chain is not the universal default anymore. Use `B.3` when assurance / trust / evidence transport is already part of the present burden, and use `E.9 (DRR)` when normative change or durable canon rationale must actually be published.

FPF is not:
- a shrink-wrapped project methodology;
- a quick-answer cheat sheet;
- a demand to read the whole specification linearly before doing useful work.

## What stays outside this front door

- fuller route explanations live in `Preface` and `Part J`, not in the opening screen;
- longer step-by-step walkthroughs live in `I.2`, not in this README;
- advanced internal maps, AI-assistant prompt recipes, and extended examples appear later in this README or in "monolith" FPF-Spec.md in this repo; you do not need them before choosing your first route.

## One-minute example

A vague project question:

> "Should we buy, fine-tune, or build an agent stack for our platform?"

Without FPF, this often becomes one overloaded discussion with mixed vocabularies, hidden trade-offs, and premature convergence on a single option.

With FPF, the work becomes a disciplined route:

`problem framing`
-> `bounded contexts` (product / infrastructure / safety / evaluation)
-> `decision criteria` (cost / latency / controllability / risk / time-to-value)
-> `portfolio of alternatives` (buy / fine-tune / build / hybrid)
-> `evidence and test gaps`
-> `starter DRR` (a short decision record with reasons, assumptions, and open issues)
-> `starter UTS` (a shared term sheet for risky or overloaded terms)
-> `aligned outputs` for engineering / management / research / assurance

Result: one underlying body of reasoning, cleaner hand-offs between specialists, and a decision that can be reviewed, revised, and published without semantic drift.

## Overview

The **First Principles Framework (FPF)** is a structured framework for thinking and coordinating work. It is written more like a technical specification than like a management book: there are named patterns, definitions, and review rules. Its job is to help teams model complex work, make reasoning inspectable, and keep decisions stable across engineering, research, and management.

This repository contains the **core specification**. Tooling belongs in tool-specific layers; worked examples, exercises, and guided learning paths belong in the pedagogical companion.

Use the spec as a reference model and route map, not as a linear textbook.

FPF is not a specific methodology such as Agile or Waterfall, and it is not a static encyclopedia. It is closer to an architecture for reasoning: a set of reusable patterns and working forms that help teams turn tacit thinking into shared, reviewable work.

FPF is not mainly about making one model smarter. It is about making collective reasoning usable: clear local contexts, explicit hand-offs, reviewable decision records, and outputs that different audiences can trust.

## What problem FPF solves

FPF is most useful when strong local reasoning is no longer the main bottleneck. It is for situations where the hard part is coordinating specialised people and AI agents, keeping meaning stable across hand-offs, making trade-offs explicit, and presenting the same underlying work to engineers, managers, researchers, and auditors without semantic drift.

In plain language: FPF turns raw intelligence into work that is easier to align, review, evolve, and delegate.

It also helps teams create local zones of closure inside an open world, so a real decision can be made even when the outside remains uncertain.

Illustrative example: a platform team is deciding whether to buy, fine-tune, or build an agent stack. FPF helps separate product, safety, infrastructure, and evaluation contexts; define decision criteria; keep several options live long enough to compare them honestly; make missing evidence explicit; and publish one view for engineers and another for management without changing the underlying reasoning.

## What you get after one pass

A first practical pass through FPF should leave you with concrete artefacts, not just better intuitions:
- a map of bounded contexts, hand-offs, and responsibility boundaries;
- explicit decision criteria and trade-off characteristics;
- a small portfolio of alternatives instead of premature convergence;
- a visible evidence / test gap list before commitment;
- a starter DRR (a short decision record with reasons, assumptions, and open questions);
- a starter UTS (a shared term sheet for unstable or overloaded domain language);
- aligned outputs for engineering, management, research, and assurance / audit readers.

## Where FPF earns its keep

FPF tends to pay off when several of these are true:

- work is split across specialised people, teams, copilots, or AI agents;
- the real-world oracle is delayed, noisy, expensive, or risky;
- different audiences need aligned outputs from the same underlying work;
- trade-offs between speed, quality, risk, novelty, and compliance must be made explicitly rather than hidden in one opaque score;
- existing categories are breaking down and you need to grow new concepts from first principles instead of reusing local folklore.

### Three ways to use FPF

1. **Human-only.** Use FPF as a reading, writing, and review discipline even with no AI in the loop. People can map contexts, separate systems / roles / method descriptions / methods / work, and produce shared term sheets and decision records directly.
2. **Mixed team.** Use FPF as a coordination layer across specialised people, teams, copilots, and AI agents. This is the mode where local working frames, hand-offs, decision gates, and audience-specific outputs matter most.
3. **AI assistant.** Use FPF as an attached reference file or indexed reference for an assistant. In this mode, the spec is attached as a file rather than pasted into the prompt window; the dedicated section below shows the concrete loading pattern.

### Why FPF when AI-agents keep getting stronger?

- **Because coordination, not raw generation, becomes the bottleneck.** Stronger LLMs reduce local reasoning scarcity, but they do not remove the need for selection, auditability, safe delegation, and shared understanding across people, agents, time, and viewpoints.
- **Because local working frames still matter.** FPF keeps teams from pretending that product, safety, operations, and research all use one universal vocabulary.
- **Because many real projects cannot just loop until tests pass.** In product, field engineering, strategy, marketing, safety, or open-ended research, the real-world oracle is delayed, noisy, expensive, or risky. FPF aims to catch anti-patterns before contact with the world.
- **Because the same framework can serve both humans and AI.** AI agents can read the specification directly; humans can learn the same working model through didactic layers and the pedagogical companion.
- **Because FPF pays off past a complexity frontier.** It matters most when the problem becomes simultaneously compositional, collaborative, temporal, assurance-heavy, and generative.

### FPF as an Operating System for Thought

Using the OS metaphor, FPF:

- **Provides a common runtime for reasoning and iteration.**
- **Treats local working frames as stable hand-off units.**
- **Separates systems, roles, method descriptions, methods, plans, and executed work.**
- **Keeps claims tied to scope, carriers, and evidence.**
- **Turns tacit thought into structured artefacts instead of leaving it implicit.**
- **Lets one underlying body of work be published differently for engineering, management, research, and assurance.**
- **Stays extensible through domain-specific packs instead of hard-coding one discipline's worldview.**

For most readers, the practical point is simpler than the internal vocabulary: FPF gives mixed human/AI teams a shared way to specialise locally, hand work off cleanly, and keep different outputs about the same work coherent.

Loaded as a file into an AI assistant that can read files directly or through retrieval over an indexed copy, FPF can act as a disciplined reasoning scaffold for mixed human/AI work. It steers the model toward first-principles and state-of-the-art-oriented reasoning instead of generic marketing / management / pop-psychology boilerplate - but it will not think instead of you, and without good questions you can still get very confident, well-structured nonsense.

## Who is this for?

- **Engineers and systems engineers** building reliable physical or cyber-physical systems.
- **Researchers** constructing trustworthy knowledge and theories.
- **Platform teams** designing AI-agent / human-in-the-loop work systems.
- **Safety, assurance, and regulatory leads** who need auditable boundaries, evidence, and controlled delegation.
- **Managers and product leaders** orchestrating collective intelligence, budgets, and evolutionary cycles.

## Core ideas (plain language first)

FPF is built on a small kernel of non-negotiable ideas. New readers do not need the internal pattern names immediately; the point of this section is to explain what the framework buys you before you dive into its internal map.

1. **Local meaning, explicit translation.** Terms live inside bounded contexts: local working frames with their own meanings. Cross-context reuse is never obvious; it needs an explicit bridge.
2. **One underlying reality, many aligned outputs.** Engineering, management, research, and assurance outputs should be projections of the same underlying work, not disconnected documents.
3. **Separate systems, roles, method descriptions, methods, plans, and executed work.** Descriptions, capabilities, plans, and actual occurrences are not the same thing.
4. **Trust has structure and grounding.** A claim should say how formal it is, where it applies, what evidence supports it, and which carriers or systems anchor it.
5. **Composition matters across scales.** The same logic should survive when parts are aggregated into wholes.
6. **Keep search wide before selection.** In open-ended work, diversity of options matters before choosing a winner.
7. **Build from first principles when categories break.** FPF is not only for organising the current state of the art; it is also for growing new abstractions.

## What to expect (and what not to expect)

### Reasonable expectations

- **A coordination fabric for mixed human/AI teams.** FPF helps specialised people and agents participate in one engineering or research effort through bounded contexts, bridges, shared artefacts, and multiple publication forms / views.
- **A way to push some mistakes left, before expensive contact with the world.**
- **A way to keep engineering, management, research, and assurance outputs coherent.**
- **A co-thinker biased toward state-of-the-art and first-principles reasoning.** When loaded into an AI-agent or chat, FPF gives you sharper questions, better comparisons, and far less generic boilerplate.
- **A backbone for disciplines and organisations.** FPF can serve as a structured way to model a discipline or organisation with explicit contexts, roles, calculi, and state-of-the-art packs rather than one more methodology slide-deck.
- **A machine for first-principles synthesis.** Use it not only to recall current best practice, but to grow new Second Principles Framework (SPF) when existing categories are misleading.
- **A kernel for development programmes.** It can also act as a kernel for engineer-manager development and research skill-building.

### Unreasonable expectations

- **I will just read it once and form my opinion.** The spec reads like OS source code, not like a popular book; it is meant to be used with tools, not consumed in one sitting.
- **This is a plug-and-play tool for all work projects.** Today FPF is a research-grade framework that already helps in real projects as an MVP, but it is not yet a shrink-wrapped product; you still need to adapt, localise, and extend it for your discipline and organisation.
- **It works without good framing and always gives the right answer.** AI-agent+FPF will not think instead of you. Without good questions, explicit problem frames, and minimal rational literacy you can still get confident nonsense - just more structured nonsense.
- **A stronger AGI / LLM makes FPF unnecessary.** As models get stronger, the bottleneck often moves from local reasoning to coordination, selection, safe delegation, and cross-role auditability.
- **Adoption should be decided only by transferable benchmark wins from other organisations.** Frameworks such as Agile or Copilot-like practices are often adopted as architectural bets under high variation. FPF is similar: the justification is usually logical fit to your coordination / problem structure, not a neat benchmark that transfers unchanged across organisations.
- **If I ignore first principles, FPF will fix everything.** FPF amplifies whatever style of thinking you bring: if you use it to chase fashion, it will help you catalog fashion; if you use it to chase first principles, it will help you do that more systematically.

## How to approach this repository

There are six practical newcomer routes above, plus a few orientation options around them:

1. **If you want the why:** start with **E.1-E.2** (Vision / Mission + Pillars).
2. **If you want the first practical route:** choose the route block above whose opening sentence sounds most like your current burden, not the code sequence that happens to appear first.
3. **If you already chose a route and want more detail:** move to the fuller route tables and route cards in **Preface** and **J.4**; longer walkthroughs belong in **I.2**.
4. **If you want to write or review patterns:** start with **E.8** and **E.19**.
5. **If your real situation is still partly said:** use route `2` above in full detail - `C.2.2a`, `C.2.LS / C.2.4-C.2.7`, `A.16 / A.16.1 / A.16.2`, `B.4.1 / B.5.2.0`, then the relevant endpoint owner.
6. **If you want a compact internal map:** use the simplified cluster map below.

<details>
<summary>Advanced: simplified internal map of the specification</summary>

The specification is divided into clusters. The map below is intentionally simplified and focuses on the main semantic blocks. Think of it as source code for an evolvable reasoning architecture, not as an expert system and not as a tutorial; Parts **H-K** then provide glossary, annexes, indexes, and navigation aids. If you only need to choose your first route, you can skip this block.

### Part A: Kernel Architecture Cluster
The immutable ontological core.
- **Ontology:** Holons, Systems, Epistemes, and Bounded Contexts.
- **Transformation:** the transformer quartet - system bearing TransformerRole, MethodDescription, Method, Work.
- **State Space and boundaries:** Characteristics, Scales, Dynamics, and the signature-stack / boundary-discipline family.

### Part B: Trans-disciplinary Reasoning Cluster
The logic of composition and trust.
- **Aggregation and emergence:** cross-scale composition and reasoning.
- **Assurance:** trust, evidence, canonical evolution, pre-abductive routing, abductive prompting.
- **Bridge use:** how reasoning moves across contexts without silent collapse.

### Part C: Kernel Extension Specifications
Pluggable domain-specific calculi, logics, and characterisation families.
- **Extension families:** Sys / KD / Kind / Method / LOG / CHR.
- **Additional burden families:** measurement, creativity, NQD, explore / exploit policy, discipline health, problem typing, method-maturity, agentic tool-use, and quality-bundle patterns.

### Part D: Multi-scale Ethics & Conflict-Optimisation
- Multi-scale ethics from agent to planetary scope.
- Conflict topology, trust-aware mediation, and bias / ethical-assurance overlays.

### Part E: The FPF Constitution and Authoring Guides
The governance of the framework itself.
- **Vision, pillars, and guard-rails.**
- **Didactic architecture, authoring protocol, lexical law, and human-facing working-model discipline.**
- **Multi-view publication, transduction-graph architecture, review gates, and DRR-based evolution governance.**

### Part F: The Unification Suite
Techniques for aligning vocabularies across disciplines and specialised agents.
- **Concept-sets, local naming, and role descriptions.**
- **Mint / reuse discipline, bridges, status mappings, and method-quartet harmonisation.**
- **Human-facing publication forms such as UTS.**

### Part G: Discipline State-of-the-Art (SoTA) Patterns Kit
Tools for harvesting state-of-the-art knowledge and building governed portfolios.
- **CG-Spec and CG-Frame authoring.**
- **State-of-the-art harvesting and synthesis.**
- **Lawful characteristic / calculi authoring, selector / dispatcher patterns, shipping-ready publication forms, and refresh discipline.**

### Parts H-K: Glossary, annexes, and navigation aids
Glossary, extended tutorials, indexes, migration notes, and other navigation support around the core clusters.

</details>

## Using FPF with an AI assistant

This is one of the three practical modes above, not the default identity of FPF. If you are working human-only or in a mixed team, you can skip this section and still use the framework fully.

The Core itself remains tool-agnostic; attaching the file or using retrieval over an indexed copy is simply the most convenient current way to expose the spec to an assistant. In practice the spec is too large to paste cleanly as a prompt, so treat it as an attached file or indexed corpus.

The highest-leverage first sessions are concrete. Ask for plain-language outputs first; pull internal FPF names only when they add precision or help you navigate the spec.

AI-agent+FPF will not solve everything automatically: you remain the principal, and the model is an agent that follows your problem framing and constraints.

If you are new to FPF, start with prompt `1` or `5` below. The later examples assume more internal FPF vocabulary.

### A starter prompt that usually works

> You have the FPF specification as a file.  
> Help me structure [project / problem / programme].  
> Use plain language for an engineer-manager.  
> Propose: (1) bounded contexts / specialisations, (2) decision criteria, (3) key alternatives, (4) hand-offs, and (5) missing evidence or tests before commitment.  
> Introduce internal FPF names only when they add precision.

In practice the most productive usage is to treat FPF as a design kit and reference model: ask for bounded-context maps, decision criteria, option portfolios, structured reasoning artefacts, publication forms, and hand-off contracts for your domain, then iterate.

Below are example prompts; adapt them to your domain and language.

### 1. Turn a vague project into measurable decision criteria

**Goal:** get a step-by-step chain from vague idea to measurable characteristics, indicators, scoring, and decision criteria.  
**Prompt:**
> You have the FPF specification loaded as a file.  
> We are starting work on [brief description of project], design has not yet begun.  
> Propose a step-by-step chain for characterising the objects of our project, normalising measurements, defining indicators, scoring alternatives, and choosing design decisions.  
> Include steps that I may have forgotten.  
> Write in the language of engineer-managers, not in FPF jargon.

Typical follow-ups:
- "Now take object [X] from this chain and work it through in detail: list 10-15 characteristics, their scales, indicators, and a rough dashboard format for decision-makers."
- "Show how this chain maps to the principles-to-work route for this project."

### 2. Build a disciplined vocabulary for a domain (UTS, shared term sheet)

**Goal:** build a disciplined vocabulary for a niche field using FPF Part F.  
**Prompt:**
> You have the FPF specification loaded.  
> Produce a Unified Term Sheet (UTS) block for the core terms of [your domain]: at least 10 rows.  
> Use the term-sheet discipline from Part F (especially F.17 / F.18): distinguish Tech vs Plain names, show SenseCells for 2-3 key bounded contexts, and flag risky aliases.

Follow-up for quantitative structure:
- "For the same domain, propose a Q-bundle that captures the quality of [your object / work system] and produce a UTS block for its characteristics (CHR) and indicators."

### 3. Design better names for ambiguous roles, programmes, and artefacts (Name Cards)

**Goal:** design better names for roles, programs, and artefacts when existing labels are misleading.  
**Prompt:**
> Using the naming-card discipline (F.18), develop a complete Name Card for what to call [current name of an entity] in the following situation:  
> [short narrative of current practice and complaints about the existing name]  
> Do not assume current names are correct; perform an honest search on the local Pareto-front of candidate names and explain trade-offs.

### 4. Make the route from principles to work explicit (P2W / E.TGA graph)

**Goal:** make from principles to work explicit for a concrete project.  
**Prompt:**
> Using E.TGA and TEVB, unpack the canonical P2W flow for my situation [describe your project].  
> Give the list of nodes (P1...Pn), their Kinds, and explain each node in engineer-manager language.

Follow-up:
- "Now build a mini Flow specification table for this P2W graph".

### 5. Organise a mixed team of humans and AI agents

**Goal:** turn a set of people, copilots, and specialised agents into a disciplined work architecture.  
**Prompt:**
> We have the FPF specification loaded as a file.  
> We need to organise a mixed team of humans and AI agents for [project / programme].  
> Propose a bounded-context map: contexts, local vocabularies, roles, bridges, hand-off artefacts, decision gates, and where human approval is required.  
> Keep the final answer practical for engineers / managers and avoid FPF jargon.

Typical follow-ups:
- "Now define autonomy budgets, allowed tools, escalation paths, and publication forms / views for each context / agent."
- "Show which bridges are high-risk because translation loss or ambiguity is likely."

### 6. Harvest competing schools of thought and build a portfolio (state-of-the-art pack)

**Goal:** use Part G to organise a frontier discipline around first principles.  
**Prompt:**
> We are searching for the state of the art in [discipline].  
> Using G.2 and G.4, extract: (a) TraditionCards for competing schools of thought; (b) OperatorCards for their main operators / update rules; (c) a first draft of a state-of-the-art pack and selector-ready portfolio. This is expected to be a long text, therefore start with only TraditionCards.

## Citation

If you use FPF, please cite:

```
Levenchuk, Anatoly. First Principles Framework (FPF).
GitHub repository: https://github.com/ailev/FPF
```
