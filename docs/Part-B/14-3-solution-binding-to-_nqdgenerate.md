## 3 · Solution — **Binding to Γ_nqd.generate (C.18)**

**Method name (Plain/Unified Tech).** *NQD‑Generate* — a **U.Method** that, given (i) a **HypothesisSpace** and (ii) a **CharacteristicSpace** with a **CoverageGrid**, returns a *finite*, **non‑dominated** set of candidate hypotheses that maximize **Quality** (per‑component) while maintaining **Diversity** and encouraging **Novelty**.

**Minimal signature.**

* **Inputs (declared in MethodDescription):**
 `HypothesisSpace`, `CharacteristicSpace`, `Seeds?`, `Budget (time/compute)`, `EmitterPolicy` (**E/E-LOG policy id**), `QualityMeasures (Q components)`, `NoveltyMetric`, `CoverageGrid/Granularity`, `CellCapacity K? (default=1)`, `EpsilonDominance ε? (default=0)`, `TieBreakPolicy? (S/I)`, `DedupThreshold?`, `Policy(TimeWindow)`, `DeterminismSeed?`
 
* **Outputs:**
  CandidateSet = {h_i: (desc_i, Q_i, N_i, D_i:=ΔDiversity_P(h_i | Pool), S_i, I_i, UseValue_i?), genealogy_i?, provenance_i (including **DHCMethodRef.edition** and **policyId** from E/E-LOG)} where `Q_i` is a vector and `provenance_i` captures generator settings and evaluation sources. If Use‑Value is present, include the objective id / acceptanceSpec, counterfactual method (if predicted), and model edition per C.17. Note: S and I are tie-breakers only unless promoted by explicit Context policy; Use-Value is informative for decision lenses and SHALL NOT enter the dominance set.

**Strategy (notation‑neutral).**

1. **Seeding.** Initialize with seeds (known solutions, random draws, or prior L0 artifacts).
2. **Iterated illumination.** Propose variations, evaluate **Q** (per‑component); maintain up to **K** elites per cell (or descriptor bucket); compute **N/D/S/I** on the fly; deduplicate by `DedupThreshold` in **CharacteristicSpace**.
3. **Budget‑bounded loop.** Iterate until budget or coverage‑convergence; return the **(ε‑)Pareto front** over `{Q₁…Q_k, D, N, ΔDiversity_P}` (do **not** collapse to a single scalar). Illumination is excluded from the dominance set by default; Surprise and Illumination act only as tie-breakers unless a Context policy explicitly promotes them. **Use-Value** may appear as a **side note** for decision discussions **but MUST NOT be mixed into NQD dominance set**.   
4. **Traceability.** Emit a **Design Rationale Record (DRR)**: grids/metrics versions, seed(s), policy and `TimeWindow`, which cells were filled, why items were dominated (list **Characteristics**), and how the final set was produced (including `ε`, `K`, and dedup). (Lightweight DRR is permitted per B.4 guidance.)
5. **Algorithmic freedom (informative).** Implementations MAY use MAP‑Elites/illumination, novelty search with local competition, Bayesian/surrogate‑assisted search, or deterministic enumerations; ε‑dominance or knee‑point thinning MAY be used *after* recording the full front in provenance.

> **No kernel growth.** This is a *Method* (C.4 Method‑CAL) plus a CHR import; **no new Γ‑operator** is added (per **A.11**).
