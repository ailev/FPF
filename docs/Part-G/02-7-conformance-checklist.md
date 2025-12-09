## 7) Conformance Checklist (normative)

1. **Context declared.** `CG‑Spec` is published **in** a `U.BoundedContext`; no global claims.
2. **Comparator set explicit.** Every permitted comparison/aggregation is named and typed; anything else **abstains by default**.
3. **CHR‑bound.** All compared quantities reference **CHR.Characteristic ids** with declared **Scale/Unit/Polarity**; guard macros attached.
4. **Minimal evidence published.** Per characteristic: **KD‑CAL lanes**, carriers, freshness, Bridge/CL allowances, and **failure behavior** are declared.
5. **Γ‑fold stated.** Default **weakest‑link**, or an alternative with proof obligations (monotonicity, boundary).
6. **CL penalties** routed to R_eff only; F is invariant; **publish Φ(CL)/Φ_plane policy‑ids in SCR** for any penalised claim.
7. **No illegal ops.** Ordinal **SHALL NOT** be averaged/subtracted; unit mismatches **SHALL** fail fast (MM‑CHR).
8. **Design/run split.** **AcceptanceStubs** provide templates in **G.0**; all **context‑local thresholds live only in CAL.Acceptance (G.4)**; nothing is hidden in CHR or code paths; manifests are externally inspectable.
9. **UTS‑ready.** Name Cards minted/reused with twin labels; Bridges carry **CL** and loss notes.
10. **RSCR wired.** Tests exist for refusal paths, unit/scale checks, threshold semantics, and CL→R_eff routing.
11. **Lifecycle set.** Refresh cadence and decay policy declared; deprecations follow **F.13–F.14** with lexical continuity notes.
12. **describedEntity present.** `GroundingHolon`, `ReferencePlane`, and a minimal `referenceMap` are recorded.
13. **Pre‑flight numeric gates.** Any numeric comparison/aggregation **MUST** cite a `CG‑Spec` entry with lawful **SCP/Γ‑fold** and **MinimalEvidence** satisfied; cross‑Context reuse requires **Bridge + CL** with penalties routed to **R_eff only** (never F).
14. **Partial‑order stance.** `ComparatorSet` SHALL NOT force total orders where only partial orders are lawful; **no scalarisation of partial orders**. Use Pareto/Lexicographic/medoid/median as lawful.
15. **Illumination discipline.** If Illumination is used, publish `ArchiveRef`, `InsertionPolicy`, and `Edition`; **exclude from dominance by default**; any promotion into dominance **MUST** cite a named lens/policy‑id and be recorded in provenance.
16. **Freshness/PathSlice.** Freshness windows are published and enforced; PathSlice identifiers are recorded in SCR when freshness gates influence gating/selection.
17. **ATS harness exposure.** Exports **MUST** provide inputs for **AH‑1..AH‑4** (tier/gate/lane/lexical checks per E.11) over EvidenceGraph paths and crossings; any failure is **blocking** for publication.

**Guards as in C.20:**
* **CC‑G0‑Φ.** **Φ(CL)** (and **Φ\_plane**, if used) **MUST** be **monotone, bounded, table‑backed**; publish policy ids; **R\_eff ≥ 0** by construction.
* **CC‑G0‑Unknowns.** **Unknowns propagate tri‑state** {pass|degrade|abstain} to **Acceptance**; **no silent coercions**.
* **CC‑G0‑CSLC.** **Scale/Unit/Polarity legality** MUST be proven (MM‑CHR/CSLC) **before** any aggregation; **no mean on ordinals; no unit mixing**.
**Registry hooks.** Every CG‑Spec entry declares Lifecycle/DRR and **RSCR triggers for Φ‑table, SCP, Γ‑fold, Bridge edits** (parity re‑runs required).

### 8) Consequences (informative)

* **Lawful comparability.** Teams know *exactly* what can be compared/aggregated and under which evidence minima.
* **Auditable trust.** Γ‑fold and CL routing make **R_eff** computation transparent to selectors and reviewers.
* **Frictionless downstream.** G.1–G.5 consume a single spec; CHR/CAL avoid hidden thresholds; dispatch is explainable.
* **Local first, portable later.** Context‑local semantics are primary; Bridges make portability deliberate and costed.

### 9) Worked micro‑example (indicative)

CG‑Frame: R&D Portfolio Decisions
Scope: ObjectKinds={Project}, TaskKinds={SelectPortfolio}
describedEntity: ⟨GroundingHolon=R&D, ReferencePlane=world⟩

ComparatorSet = {
  ParetoDominance,
  LexicographicMin(SafetyClass),
  AffineSum(CostUSD_2025)
}

Characteristics = \[
  SafetyClass : scale=ordinal,  polarity=↑, levels={D,C,B,A,AA},
  CostUSD_2025 : scale=ratio,   polarity=↓, unit=USD_2025,
  Readiness : scale=nominal,    polarity="="
]

 SCP:
  SafetyClass   → ORD_COMPARE_ONLY; aggregator=LexiMin; coordinate=Isotonic(order‑only) // no means
  CostUSD_2025  → UNIT_CHECK; aggregator=Sum; unit_alignment=USD_2025; polarity=↓
  Readiness     → equality_only; aggregator=None; ordering via Bridge only (CL≥2 with loss note)

MinimalEvidence:
  SafetyClass  → lanes={LA}, carriers={test_reports}, freshness≤18mo,
                  failure={abstain if lanes/carriers missing; refuse if mean() attempted}
   CostUSD_2025 → lanes={LA,VA}, carriers={ERP,audit}, freshness≤12mo,
                  failure={refuse if unit misaligned; sandbox if carrier missing}

  Readiness    → lanes={VA}, carriers={process_docs}, freshness≤12mo,
                  failure={abstain for ordering unless Bridge(CL≥2)}

Γ‑fold := weakest‑link across lanes
CL‑Routing: CL=2 (Marketing→Engineering) → multiplicative penalty on R_eff; F invariant

AcceptanceStubs:
  AC_SafetyGate: SafetyClass ≥ B
  AC_Budget: Σ CostUSD_2025 ≤ Envelope

RSCR:
* refuse mean(SafetyClass)
* fail on (USD + Readiness)
* verify AC_Budget on worked examples
