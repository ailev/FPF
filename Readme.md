# First Principles Framework (FPF) — Core Conceptual Specification

> **An Operating System for Thought**  
> *Architecting transdisciplinary reasoning for systems, epistemes, and communities.*

**Version:** December 2025  
**Primary Author:** Anatoly Levenchuk (with LLM assistance)  
**Status:** Normative kernel, "eternal alpha" — already used in working projects and increasingly acting as an MVP for working development programmes, while still evolving as a research framework.

## 📖 Overview

The **First Principles Framework (FPF)** is a rigorous, transdisciplinary architecture for thinking, written in human- and machine-readable pseudo-code (the informal "language of technical standards" with multiple "May", "Should", "Must"). It provides a generative pattern language to model complex systems, manage knowledge evolution, and ensure auditable assurance across engineering, research, and management domains. Internally, FPF also serves as a conceptual data schema for rational work that you look at, resonate with, and mine for patterns than a narrative textbook. 

FPF is not a specific methodology (like Agile or Waterfall) nor a static encyclopedia. It is an **episteme of method** — a structured specification of how to think — packaged as a set of architecture decision records (ADRs) and patterns that can be executed by humans and LLMs and consumed as pseudo-code by LLMs. It bridges the gap between **rigorous assurance** (audits, proofs) and **open-ended creativity** (innovation, novelty) by treating them as complementary engines within a single evolution.
 

### 🧠 FPF as an "Operating System for Thought"

Using the OS metaphor:

* **Runs "applications of thought".** FPF provides a canonical reasoning cycle (abduction–deduction–induction, `B.5`) and a canonical evolution cycle (`B.4`) that act as a generic *runtime* for research and engineering tasks.
* **Isolates processes and manages their interaction.** `U.BoundedContext` gives an "address space of meaning"; alignment bridges, congruence levels, and Concept-Set tables (`F.9`, `F.17`) define controlled concept exchange between contexts instead of global terminology soup.
* **Creates and terminates thought processes.** The holon → role → method → work chain makes "a process of thinking" explicit: from intention, through role assignment and method choice, to concrete Work records.
* **Manages memory and protects meaning.** `U.BoundedContext`, Evidence Graphs and context passports keep track of *where* statements hold, under which editions and planes, so that reasoning remains auditable instead of becoming folklore. 
* **Prepares resource management.** `Γ_work` (Gamma, composition operator) and the planned Resrc-CAL describe how time, money, energy, and other resources flow through work streams.
* **Provides a "conceptual file system" and I/O.** Cards, tables, records (RSR/RSCR, F-cluster) are the conceptual "files" and journals through which thinking interacts with the world, independently of any specific notation or tool. This is how FPF supports "thinking by modelling": you externalise thought into structured artefacts instead of keeping everything in your head. 
* **Uses a micro-kernel architecture.** At the core is a minimal transdisciplinary set of types and Γ-operators; domain-specific calculi, logics, CHR-packs and SoTA-packs (`Part C`, `Part G`) plug in like drivers and services above the micro-kernel.

Loaded as a file into an LLM, FPF acts as a *bias-assistant* or "grimoire": it steers the model toward first-principles, SoTA-oriented reasoning instead of generic marketing/management/pop-psychology boilerplate — but it will not think instead of you, and without good questions you can still get very confident, well-structured nonsense. 

## 🎯 Who is this for?

*   **Engineers** building reliable physical or cyber-physical systems (`U.System`).
*   **Researchers** constructing trustworthy knowledge and theories (`U.Episteme`).
*   **Managers** orchestrating collective intelligence, budgets, and evolutionary cycles.

## 🔑 Key Concepts & Commitments

FPF is built on a micro-kernel of non-negotiable principles. If you are new, start with these core ideas:

1.  **Holonic Foundation (`A.1`):** Everything is a `U.Holon`—simultaneously a whole and a part. We strictly distinguish between physical actors (**Systems**) and knowledge artifacts (**Epistemes**).
2.  **Contextual Meaning (`A.1.1`, `F.0.1`):** Meaning is local. A term like "Service" or "Process" is defined strictly within a `U.BoundedContext`. Cross-context communication happens only via explicit **Bridges** with declared translation loss.
3.  **Strict Distinction (`A.7`):** We never confuse the map with the territory.
    *   **Role** (Assignment/Mask) $\neq$ **Method** (Recipe) $\neq$ **Work** (Execution/Occurrence).
    *   Documents do not "act"; only Systems enact Work.
4.  **Trust & Assurance Calculus (`B.3`):** Trust is not a feeling; it is a computed tuple **$\langle F, G, R \rangle$**:
    *   **F (Formality):** How rigorously is it expressed?
    *   **G (Claim Scope):** Where does it apply? (Set-valued over context slices).
    *   **R (Reliability):** How well is it supported by evidence?
5.  **Evolution & Creativity (`B.4`, `C.18`):** Systems must evolve. FPF operationalizes the "Bitter Lesson" by favoring general, scalable search methods (**NQD**: Novelty-Quality-Diversity) over hand-tuned heuristics, governed by explicit **Explore-Exploit policies**.
6.  **Universal Aggregation ($\Gamma$):** A single algebra (`B.1`) governs how parts combine into wholes, ensuring invariants like "Weakest-Link" reliability are preserved across scales.

## ✅ What to expect (and what not to expect)

### Reasonable expectations

* **A SoTA-biased co-thinker.** When loaded into an LLM, FPF acts as a bias-assistant for strong engineering and research thinking: you still think, but you get sharper questions, better comparisons and far less "pop-management / pop-psychology fluff" (and definitely not an astrologer in disguise).
* **A DDD-style backbone for disciplines.** FPF can serve as the *DDD (domain-driven design) for science/engineering*: a way to model a discipline (or organisation) with explicit contexts, roles, calculi, and SoTA-packs rather than one more "methodology slide-deck".
* **A long-term atlas of first principles.** Reading the specification end-to-end is not required; it is closer to a dense atlas for first-principles reasoning mastery that you browse, query and mine via your favorite LLMs.
* **A kernel for development programmes.** In practice FPF already feeds programmes for engineer-manager development and research skill-building.

### Unreasonable expectations

* **"I'll just read it once and form my opinion."** The spec reads like OS source code, not like a popular book; it is meant to be *used* with tools, not consumed in one sitting.
* **"This is a plug-and-play tool for all work projects."** Today FPF is a research-grade framework that already helps in real projects as an MVP, but it is not yet a shrink-wrapped product; you still need to adapt, localise, and extend it for your discipline and organisation. 
* **"It works without 'spells' and always gives the right answer."** LLM+FPF will not think instead of you. Without good questions, explicit problem frames, and minimal rational literacy you can still get confident nonsense—just more structured nonsense.
* **"If I ignore first principles, FPF will fix everything."** FPF amplifies whatever style of thinking you bring: if you use it to chase fashion, it will help you catalog fashion; if you use it to chase first principles, it will help you do that more systematically.


## 📂 Repository Structure

```
FPF/
├── FPF-Spec.md          # The full specification (single file, 3.2MB)
├── Readme.md            # This file
├── package.json         # Bun configuration
├── scripts/
│   └── generate-docs.ts # Generates browsable docs from spec
└── docs/                # Generated browsable documentation
    ├── README.md        # Navigation index
    ├── 00-Preface/      # Preface section
    ├── Part-A/          # Kernel Architecture Cluster
    ├── Part-B/          # Trans-disciplinary Reasoning Cluster
    ├── Part-C/          # Architheory Specifications
    ├── Part-D/          # Multi-scale Ethics & Conflict-Optimisation
    ├── Part-E/          # FPF Constitution and Authoring Cluster
    ├── Part-F/          # The Unification Suite
    └── Part-G/          # Discipline SoTA Architheory Kit
```

### Browsing the Specification

**Option 1: Browse the `docs/` folder** — Each Part is split into readable sections for easy GitHub navigation.

**Option 2: Read the full `FPF-Spec.md`** — Load the complete specification into an LLM or use a markdown viewer.

**Option 3: Regenerate docs** — If the spec is updated, run:
```bash
bun run generate-docs
```

---

## 📑 Specification Structure

The specification (FPF-Spec.md) is divided into clusters of patterns:

### **Part A: Kernel Architecture Cluster**
The immutable ontological core.
*   **Ontology:** Holons, Systems, Epistemes, and Bounded Contexts.
*   **Transformation:** The `Transformer` quartet (Agent, Method, Description, Work).
*   **State Space:** Characteristics, Scales, and Dynamics.

### **Part B: Trans-disciplinary Reasoning Cluster**
The logic of composition and trust.
*   **$\Gamma$ Algebra:** How to aggregate systems (`Γ_sys`), knowledge (`Γ_epist`), and resources (`Γ_work`).
*   **Assurance:** The `F-G-R` calculus and evidence graphs.
*   **Transduction Graph Architecture (E.TGA):** Eulerian graphs of flows and "from principles to work" (P2W) paths that make architectures of reasoning and work explicit.
*   **Evolution:** The canonical loops for observing, refining, and deploying updates.

### **Part C: Architheory Specifications**
Pluggable domain-specific calculi (CAL), logics (LOG), and characterizations (CHR).
*   **Sys-CAL:** Physics and conservation laws.
*   **KD-CAL:** Knowledge dynamics and truth-maintenance.
*   **NQD-CAL:** Novelty, Quality, and Diversity search.
*   **Kind-CAL:** Typed reasoning and taxonomy.

### **Part D: Ethics & Conflict-Optimisation**
*   Multi-scale ethics (from agent to planetary).
*   Bias audits and trust-aware mediation.

### **Part E: Constitution & Authoring**
The governance of the framework itself.
*   **The 11 Pillars:** Constitutional invariants (e.g., *Cognitive Elegance*, *Didactic Primacy*).
*   **Guard-Rails:** DevOps Lexical Firewall, Notational Independence.
*   **MVPK:** Multi-View Publication Kit for generating consistent views/documents.

### **Part F: The Unification Suite**
Techniques for aligning vocabularies across disciplines using **SenseCells**, **Concept-Sets**, and **Alignment Bridges**.

### **Part G: Discipline SoTA Kit**
Tools for harvesting "State of the Art" (SoTA) knowledge, benchmarking methods, and creating selector-ready portfolios of solutions.

> *"A principle that works in only one world is local folklore; a first principle architects every world."* — **Pattern A.8**

## 🚀 Using FPF with LLMs (Worked Prompt Examples)

FPF is designed to be loaded as a file into an LLM (ChatGPT, Gemini, local models with RAG, etc.) and then *asked to think with you* about concrete projects. There is no magic "prompt library" for FPF: what matters is your ability to have a rational conversation with the model about real problems, not memorise incantations. LLM+FPF will not "solve everything automatically": you remain the principal, the model is an agent that follows your problem framing and constraints.

In practice the most productive usage is not "summarise the spec", but "treat the spec as a grimoire": ask for concrete chains, patterns, UTS blocks, P2W paths and Q-bundles for your domain and iterate.

Below are example prompts that have been used in practice; adapt them to your domain and language.

### 1. Characterisation & indicators for a new project

**Goal:** get a step-by-step chain from “vague idea” to measurable characteristics, indicators, scoring and decision criteria.
**Prompt:** 
> You have the FPF specification loaded as a file.  
> We are starting work on <brief description of project>, design has not yet begun.  
> Propose a step-by-step chain for characterising the objects of our project, normalising measurements, defining indicators, scoring alternatives, and choosing design decisions.  
> Include steps that I may have forgotten.  
> Write in the language of engineer-managers, not in FPF jargon.*

Typical follow-ups:
* “Now take object <X> from this chain and work it through in detail: list 10–15 characteristics, their scales, indicators, and a rough dashboard format for decision-makers.”
* “Show how this chain maps to P2W in E.TGA for this project.”

### 2. UTS (Unified Term Sheet) for a domain

**Goal:** build a disciplined vocabulary for a niche field using FPF Part F.
**Prompt:**
> You have the FPF specification loaded.  
> Produce a Unified Term Sheet (UTS) block for the core terms of <your domain>: at least 10 rows.  
> Use F.17 and F.18: distinguish Tech vs Plain names, show SenseCells for 2–3 key bounded contexts, and flag risky aliases.

Follow-up for quantitative structure:
* “For the same domain, propose a Q-bundle that captures the quality of <your object/process> and produce a UTS block for its characteristics (CHR) and indicators.”

### 3. Naming via F.18 (Name Cards)

**Goal:** design better names for roles, programs, artefacts when existing labels are misleading.
**Prompt:**
> Using F.18, develop a complete Name Card for what to call <current name of an Entity> in the following situation:  
> <short narrative of current practice and complaints about existing name>  
> Do not assume current names are correct; perform an honest search on the local Pareto-front of candidate names and explain trade-offs.

### 4. P2W (from principles to work) paths with E.TGA

**Goal:** make “from principles to work” explicit for a concrete project.
**Prompt:**
> Using E.TGA and TEVB, unpack the canonical P2W flow for my situation <describe your project>.  
> Give the list of nodes (P1…Pn), their Kinds, and explain each node in engineer-manager language.

Follow-up:
* “Now build a mini Flow specification table for this P2W graph”.

### 5. SoTA harvesting & discipline packs

**Goal:** use Part G to organise a frontier discipline around first principles.
**Prompt:**
> We are in search for SoTA of <discipline>.
> Using G.2 and G.4, extract: (a) TraditionCards for competing schools of thought; (b) OperatorCards for their main operators / update rules; (c) a first draft of a SoTA Pack and selector-ready portfolio. This is expected to be a long text, therefore start with only TraditionCards.
