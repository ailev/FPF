# **C.13 — Compose‑CAL (Constructional Mereology)**
*(architheory pattern; structural rung of the FPF ladder)*
**Status.** Normative architheory \[A]; notation‑agnostic; imports Kernel only.

### 1 Intent

Provide a single, generative calculus for part–whole structure so that **all** structural relations in FPF are *constructed* (not merely declared) from three primitives and thereby inherit extensional identity by design. The calculus is hidden from day‑to‑day users behind relation aliases; its artefacts are traces that witness how a whole arises from its parts.

Also known as *“Γₘ mereology”*, *“constructor‑based composition”*.

**Layer.** *calculus.*
**Depends on.** Kernel only (no upward imports).
**Consumed by.** CT2R‑LOG (B.3.5) Working‑Model alias logic and any architheory that needs part–whole semantics. Compose‑CAL does **not** import alias definitions; it merely emits traces that others may reference.

Compose‑CAL introduces a **single construction operator Γₘ** with exactly three constructors—**sum**, **set**, **slice**—sufficient to build structural wholes, collections‑as‑wholes, and aspects **without** extending the Kernel’s type set. No “parallel” or “temporal slice” constructor is added. Every construction yields a **trace** that serves as the witness for structure. Human‑facing relations such as *ComponentOf*, *MemberOf*, *AspectOf* are defined elsewhere as **Working‑Model aliases** and are *grounded* in these traces; Compose‑CAL itself remains purely generative and extensional.


### 2 Problem frame & Problem

FPF presents a unified structural backbone used across disciplines. Historically, sub‑relations like *ComponentOf* or *MemberOf* were **declared** directly. This maximised usability but provided no generative guarantee that a new subtype was extensionally well‑behaved or reducible to common mereology.

Declared lists of part‑of sub‑relations **scale poorly** and **lack identity guarantees**. Engineers ask for a *single dial* (“is x part of y?”), while ontologists need a principled foundation that (a) avoids Kernel bloat and (b) proves that wholes are nothing over and above their parts. Adding yet another bespoke relation (e.g., *PortionOf*) should not entail schema surgery or ad‑hoc rules.

### 3 Forces

* **Parsimony (C‑5).** Add no core types if composition suffices; keep the constructor set minimal.
* **Minimal Kernel (P‑1).** Generativity must live in a plug‑in calculus, not in Kernel axioms.
* **Cognitive asymmetry.** Everyday users want “one part‑of query”; specialists accept complexity backstage.
* **Trans‑disciplinary unification.** Every architheory that needs mereology should reuse one *generative* basis.
* **Green‑field strictness.** With no legacy to break, we can require grounding for new structural edges.


---

# C.16 (MM‑CHR) — Measurement & Metrics Characterization (Architheory)  \[A]
