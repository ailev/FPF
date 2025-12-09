## 10) Relations (wiring)

**Builds on:** A.4, A.10; **B.1/B.3/B.4**; **A.17–A.19/C.16**; **C.17–C.19**; **F.1–F.3/F.7–F.9/F.13–F.15/F.17–F.18**; **E.5.1–E.5.3** (no tool lock‑in); **E.10**.
**Publishes to:** G.1 (generator guards), G.2 (harvesting policy & CL), G.3 (required CHR), G.4 (acceptance/evidence), G.5 (eligibility gates).
**Constrains:** any LOG implementation via CAL/CHR legality and evidence minima.

### 11) Author’s quick checklist

1. Write the **Frame Charter** (Context, USM scope, describedEntity).
2. Enumerate the **ComparatorSet**; bind **SCP** with guard macros and AggregationSpecs.
3. Bind **Characteristics\[]** to **CHR** ids; ensure Scale/Unit/Polarity are declared (reuse or mint in UTS).
4. Publish **MinimalEvidence** per characteristic (KD‑CAL lanes, carriers, freshness, Bridge/CL allowances, failure behavior).
5. State Γ‑fold and CL‑Routing; **default Γ‑fold = weakest‑link**; if overriding, attach CAL proofs (monotonicity, boundary behavior). Record **Φ(CL)/Φ_plane** **policy ids**; penalties → **R_eff only**.
6. Publish to **UTS** with Name Cards, twin labels, Bridges (+loss notes); register **RSCR** tests.
7. Set **refresh/decay**; log changes to **DRR/SCR**; maintain lexical continuity on deprecations.
