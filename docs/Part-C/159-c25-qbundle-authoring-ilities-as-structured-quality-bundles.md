## C.25 — **Q‑Bundle: Authoring “‑ilities” as Structured Quality Bundles**  \[D]

**Status & placement.** Part C (measurement/comparability); **Definitional pattern \[D]** reusing Core patterns (**A.2.6 USM**; **A.6.1 Mechanism**; **C.16 MM‑CHR / A.18 CSLC**). Intended as a **lightweight authoring aid** for Contexts; it adds no new kernel types.  (A.6.1; A.2.6 § 6.2; C.16/A.18). 

### 1 · Problem frame
Provide a **minimal, uniform shape** for engineering “‑ilities” so authors either (a) declare a **single CHR characteristic** (when truly measurable on one scale), or (b) publish a **structured bundle** that keeps **measures** (CHR) distinct from **scope** (USM set) and **mechanism/status** slots. This prevents conflation of **set‑algebra** (scope) with **numeric measurement** (CHR) and keeps assurance math stable.  (A.2.6 § 6.2; C.16).

### 2 · Problem (recurring)
*‑ilities* are often treated as if they were **single metrics**, while in practice many are **composites** whose evaluation depends on (i) **declared context‑of‑use** (Scope), (ii) **one or more CHR measures** (SLIs/SLOs), and (iii) **supporting mechanisms/statuses**. Collapsing these into “one number” invites illegal arithmetic and breaks USM locality.  (A.2.6; C.16).

### 3 · Forces
**Locality vs comparability.** Scope must remain **context‑local** (USM) while measures remain **legally comparable** (CSLC). 
**Mechanism vs measure.** Presence of a mechanism (A.6.1) is not itself a measurement, yet may gate admissibility and influence **R**.  (A.6.1; C.16/A.18).

### 4 · Solution — Q‑Bundle normal form (Tell → Show → Show; E.8 order)
**Definition.**  
`Q‑Bundle := ⟨ Name, Carrier, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence? ⟩`

**Fields (conceptual; reuse existing types).**
* **Name.** The quality family label (e.g., *Availability*, *Resilience*).  
* **Carrier.** `U.System | U.Service | U.Episteme` (what bears the quality).  
* **ClaimScope / WorkScope.** **USM** set(s) over `U.ContextSlice` (where the claim holds / where the capability can deliver). **Set‑valued; not CHR.**  (A.2.6 § 6.2).  
* **Measures[CHR].** One or more **CHR Characteristics bound to one Scale each** (e.g., `AvailabilityRatio[%]`, `RTO[min]`). **These are the measurable slots.** (C.16/A.18).  
* **QualificationWindow.** Time policy used by guards (point/window/rolling).  
* **Mechanisms / Status.** References to **A.6.1 U.Mechanism** realizations (e.g., redundancy policy, audit/trace) or certification/status flags. **Not measurements.** (A.6.1).  
* **Evidence (optional).** Anchors/stubs per A.10 or C.16 to justify measures/mechanisms.

**Conformance (minimal).**
1) If a publisher intends to use an “‑ility” as a **single measurement axis**, they **MUST** bind it to a **named `U.Characteristic` + CSLC Scale** and cite that axis in guards/UTS; otherwise publish a **Q‑Bundle**. (C.16/A.18).  
2) **Scope** remains **USM set‑valued**; guards use **membership/coverage** (“Scope covers TargetSlice”), never ordinal/averaging on G. (A.2.6 § 6.2).  
3) **Mechanisms/Status** MAY gate admissibility but **MUST NOT** be conflated with **Measures**; penalties from Bridges/planes route to **R** only. (A.6.1; Part B).

### 5 · Micro‑catalogue (worked mini‑sketches)
**Availability (often Q‑CHR).**  
*Scope:* observation window + region/tier (USM). *Measure:* `AvailabilityRatio[%]` (CHR). *Mechanisms:* redundancy/failover (A.6.1). **Guard:** Scope covers TargetSlice ∧ SLI/SLO satisfied.  

**Resilience (Q‑CMP).**  
*Scope:* disruption scenarios (USM). *Measures:* `MTTR`, `RTO`, `RPO` (CHR set). *Mechanisms:* drills/restore runbooks. **Guard:** scenario‑specific gates; **R** absorbs penalties from crossings.  

**Security (Q‑MECH/Q‑CMP).**  
*Scope:* trust zones/attack classes (USM). *Measures:* time‑to‑patch, coverage proportions (CHR). *Mechanisms/Status:* control sets, certs. **Guard:** policy/mechanism present ∧ measures thresholds ∧ Scope match.

### 6 · Relations
**Builds on.** **A.2.6** (USM scope algebra, set‑valued; no CSLC), **A.6.1** (mechanism intensions and guards), **C.16/A.18** (measurement legality: one Characteristic ↔ one Scale).  
**Coordinates with.** **B.3** (R/CL penalties only), **A.15** (Method–Work gates use Scope + Measures + Windows).

### 7 · Consequences (brief)
* **No category errors.** Authors cannot “average scope” or treat mechanisms as measurements.  
* **Portable comparisons.** Numbers compare on CHR Scales; scope composes by set algebra.  
* **Cleaner gates.** Admission checks become `Scope covers TargetSlice ∧ Measures met ∧ Window valid`.

### 8 · Quick authoring checklist (lintable)
* If the term is an **‑ility**, choose: **CHR axis** (bind to Characteristic+Scale) **or** **Q‑Bundle**.  
* Ensure any scope is **USM** (set over `U.ContextSlice`); no “G‑levels.”  
* Cite mechanisms/status separately; route crossings’ penalties to **R** only.
