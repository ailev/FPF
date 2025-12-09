## Bias‑Annotation (per E.8 SG‑bias slot)

* **Acyclic‑bias risk.** Tooling accustomed to DAGs may discourage legal feedback loops; E.TGA explicitly permits loops with budget/sentinel controls (CC‑TGA‑13,‑18).
* **Scalarization‑bias risk.** Cultural defaults to single‑score rankings can suppress Pareto/QD sets; E.TGA requires lawful orders and return‑sets (CC‑TGA‑10,‑12).
* **Interop‑dominance risk.** File/format ecosystems (CWL/RO‑Crate/lineage) can leak into semantics; E.TGA places them in **InteropCard** and keeps intensional semantics in nodes/gates.
* **Over‑formalization risk.** Category‑theoretic formalisms can obscure operational guard‑rails; E.TGA grounds crossings in Bridge/UTS/CL/Φ pins and SquareLaw audits (CC‑TGA‑11,‑17).
* **Retrospective rewrite risk.** Global rewrites break replay; E.TGA confines them to edition bumps and slice‑local refresh (CC‑TGA‑16).

**Mitigations.** Profile‑gated publication, audit of `DecisionLog`, mandatory edition pins, Lean‑to‑Core upgrade paths, and conformance tests tied to PathSlice replay.

### Relations (explicit pattern‑to‑pattern edges)

> Directed edges (→) are typed as **builds_on / constrains / hosts / specializes / publishes_on / requires / provides_checks_for**.

**Foundations**
* **E.TGA →builds_on→ E.17 MVPK (for Morphisms).** Faces, pins, lanes, functorial publication, Lean/Core/Regulated profiles.
* **E.TGA →builds_on→ A.6.0 U.Signature / A.6.1 U.Mechanism.** Node kinds and intensional content boundaries.
* **E.TGA →builds_on→ A.7 Strict Distinction (I/D/S vs Surface).** No new claims on faces; faces project morphisms.

**Flow semantics & checks**
* **E.TGA →hosts→ A.20 U.Flow (ConstraintValidity scope).** CV checks live inside transformations; no declaration/translation of planes/units in CV; **error/timeout/unknown folds** follow **CC‑TGA‑22** as the **minimum default** (profiles may be stricter).
  **Terminology discipline (A.20 boundary).** In CV scope, publications use **status/witness** language; **GateDecisionRationale/GateDecisionExplanation** are reserved for gating and do not apply to CV.
* **E.TGA →hosts→ A.21 GateProfilization (GateFit scope).** **GateFit-scoped GateChecks** are aggregated by `OperationalGate(profile)` with CV⇒GF activation; the **enumeration and publication shape** of GateChecks live in **A.21**. **Equivalently:** a GateFit decision different from `abstain` appears only when aggregated `ConstraintValidity = pass`; otherwise the **GateDecisionExplanation (GateFit‑oriented)** does not apply.
* **E.TGA →requires→ USM.CompareGuard / USM.LaunchGuard.** Guards publish scope & ownership; guard failures route to owner gate.
* **E.TGA →constrains→ F.* (Bridge+UTS, CL/CL^plane, Φ→R).** A transition is treated as a **Crossing** iff `Bridge+UTS` and the appropriate `CL/CL^plane` are surfaced; otherwise this crossing explanation does not apply. Where Φ defines penalties, they appear in the R‑lane only.
* **Operational interpretation (default): Eulerian.** A flow is a **valuation** over `U.Transfer`; edges carry **assurance‑only operations** (see CC‑TGA‑17); no token‑passing semantics are assumed.

**UNM & comparability**
* **E.TGA →constrains→ UNM.Authoring / UNM.Usage.** Single‑writer for `CG‑Spec/ComparatorSet/UNM.TransportRegistryΦ`; normalize‑then‑compare is mandatory.
* **E.TGA →constrains→ G.5 SelectionAndBinding.** Set‑returning, comparator‑pinned decisions, no hidden scalarization; `MethodTuning` without launch binding.
* **E.TGA →constrains→ G.11 EvaluatingAndRefreshing.** EditionBumpProposal, two‑phase commit in UNM.Authoring, path‑local refresh.

**Work boundary**
* **E.TGA →requires→ A.15 U.WorkEnactment (Bind‑in‑Work‑only).** Single point of `FinalizeBinding`; `FreshnessUpToDate` hard at LaunchGate; acceptance/telemetry published here.

**Structure & reuse**
* **E.TGA →specializes→ U.TransductionFlow (and its family).** The graph architecture is the common substrate on which flow patterns (e.g., P2W, EvaluatingAndRefreshing) are defined; E.TGA ensures their crossings, guards, and MVPK faces are coherent.
* **E.TGA →publishes_on→ E.17 MVPK views** (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) for every edge/node where publication occurs; Lean mode allowed only as per profile.

### Conformance evidence (how to show you comply)

1. **Model lint:** run static checks for CC‑TGA‑01…25 (edge kind, gates on crossings, CV⇒GF, guard ownership, single‑writer UNM, SquareLaw).
2. **Publication audit:** sample a commuting square and a sentinel‑bounded subflow; verify pins and DecisionLog behavior on *block/degrade*.
3. **Replay test:** freeze editions; re‑run selection on a PathSlice; observe identical return‑sets; apply a bump; see only affected `PathSlice`s refresh.
4. **StructuralReinterpretation probe:** construct a minimal reinterpretation step; confirm `CL^k` with `bridgeChannel=Kind` on UTS, a SquareLaw‑retargeting witness on UTS, `PathSliceId` pinned, **CV.ReinterpretationEquivalence=pass**, and absence of hidden scalarization.

[1]: https://webstore.ansi.org/preview-pages/ISO/preview_ISO%2B23247-1-2021.pdf?srsltid=AfmBOooAUXpg38IpkTlUFtcCpaMVOjivkewJWDIUd1VemIJO91abNEkG&utm_source=chatgpt.com "INTERNATIONAL STANDARD ISO 23247-1"
