## 9 · Worked Examples (informative)

> Each mini‑case states the artifact, assigns **F**, and notes interactions with **G/R**. Examples are deliberately cross‑disciplinary to stress transdisciplinary comparability.

### 9.1 · Research hypothesis (physics)

**Artifact.** Short note proposing a new scaling law; clear vocabulary; scope “low‑Reynolds flows in microchannels.”
**F.** **F3** (controlled narrative with per‑claim acceptance in prose).
**G/R.** G is a narrow physical envelope; R is initially low (hypothesis).
**Next ΔF.** Recast acceptance as predicates over variables → **F4**; encode a simple simulation harness → **F5**.

### 9.2 · API specification (software)

**Artifact.** REST API doc with request/response schemas and explicit pre/postconditions; invariants like “idempotent under retry.”
**F.** **F4** (first‑order constraints).
**G/R.** G = stated resource model; R improves via conformance tests (independent).
**Next ΔF.** Reference implementation and executable test suite with declared Standards → **F5**; model‑check idempotence under failure injection → **F6**.

### 9.3 · Safety controller (cyber‑physical)

**Artifact.** Controller with plant model; safety distance invariant and braking envelope defined and verified in a hybrid model checker.
**F.** **F6** (hybrid formalism with obligations checked).
**G/R.** G = operating envelope (speed ranges, road conditions); R increases via track tests and simulation coverage.
**Next ΔF.** Encode key invariants in HOL and prove monotonicity → **F7**; migrate safety property into dependent types in the control kernel → **F8**.

### 9.4 · Decision policy (management)

**Artifact.** Escalation policy: if risk score ≥ θ and budget slack ≤ β, escalate to committee; otherwise defer.
**F.** **F3→F4** depending on phrasing. If the thresholds and variables are typed and the rule is predicate‑like, rate **F4**.
**G/R.** G = organizational scope (which portfolios, time windows); R entails retrospective calibration (did escalations match outcomes?).

### 9.5 · Verified algorithm (theory/software)

**Artifact.** Sorting function implemented with a dependent type ensuring output is ordered and a permutation of input; proof included.
**F.** **F8** (dependent/constructive proof).
**G/R.** G = data types and preconditions; R (empirical) is irrelevant; VA lane suffices (proof stands).

### 9.6 · ML classifier (data/ML)

**Artifact.** Training pipeline fully specified; metrics defined; OOD detection configured; no formal invariants.
**F.** **F5** (executable algorithmic semantics).
**G/R.** G = data distributions and deployment envelope; R grows with validation/monitoring.
**Next ΔF.** Add formal constraints for safety (e.g., monotonicity in features) → **F4/F6** for those aspects; certified post‑processing may achieve **F7** for a slice.

### 9.7 · Meta‑specification (method description)

**Artifact.** A guideline on how to review specs; it includes checklists and litmus tests.
**F.** **F3–F4** depending on whether checks are predicates.
**Interaction.** Its F does **not** lift the F of the reviewed artifacts; it only affects **R** via better CL (clearer alignments and fewer losses).
