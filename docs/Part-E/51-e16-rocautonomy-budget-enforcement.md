## E.16 — RoC‑Autonomy: Budget & Enforcement \[A]

**Intent.** Make any claim of autonomous behavior testable and enforceable via a published **AutonomyBudgetDecl**, **Guarded enactment**, **Override SpeechActs with SoD**, and a **Work‑anchored AutonomyLedger**. 
**Rule (summary).** If a Role/Method/Service claims autonomy, authors **MUST**: (i) publish an `AutonomyBudgetDecl` with `AdmissibilityConditionsId` and `OverrideProtocolRef`; (ii) gate Method steps with `requiresAutonomyBudget`; (iii) write a `AutonomyLedgerEntry` on every admitted Work; (iv) block on depletion until a `ResumeAutonomy` SpeechAct passes SoD; (v) surface autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.15; B.3; E.8; E.10; E.11; F.4; F.6; F.15; F.17.
**Coordinates with:** A.13 (Agential Role), C.9 (Agency‑CHR), C.24 (Agent‑Tools‑CAL) where applicable; G.4–G.5–G.8–G.9–G.10 (method authoring/selection/shipping).

### 1) Problem Frame

Autonomy‑claiming **performers** (*RoleAssignments* over services/robots/teams operating without continuous human direction) must **stay within declared limits** (safety, risk, resource, remit) and **yield** to governance when required. Without a uniform rule, “autonomy” drifts into tacit norms, cannot be benchmarked or audited, and undermines selection (Part G) and publication (Part F).

### 2) Problem

* **Opaque autonomy.** Patterns assert “autonomous” behavior with no **budget** or **enforcement**.
* **Un‑gated execution.** Methods can execute beyond authority or risk limits.
* **Ad‑hoc overrides.** No standard **SpeechAct** for pausing/de‑scoping; SoD is unclear.
* **Non‑portable publication.** **UTS (Unified Term Sheet)** rows cannot surface autonomy‑critical data for parity or selection.

### 3) Forces

| Force                          | Tension                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ |
| **Creativity vs Safety**       | Exploration autonomy vs hard constraints and override duties             |
| **Locality vs Comparability**  | Context‑local rules vs cross‑context selection (G‑suite)                 |
| **Simplicity vs Auditability** | Lightweight authoring vs ledger‑grade evidence                           |
| **Autonomy vs SoD**            | Helpful self‑action vs separation‑of‑duties and human‑in‑the‑loop points |

### 4) Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** a Role/Method/Service **claims autonomous operation** (any phrasing that implies unsupervised decision or actuation).

**E.16‑S1 (Autonomy Budget — mandatory).**
Any autonomy claim **MUST** publish an **AutonomyBudgetDecl** as a *named, versioned* object in the **same `U.BoundedContext`**:

```
AutonomyBudgetDecl {
  id, version
  scope: ClaimScope (G)                              // where this budget applies
  budget: {                                          // all typed via MM‑CHR (C.16)
    action_tokens?     : Unitful quota / rate
    decision_tokens?   : Unitful quota / rate
    risk_envelope?     : CHR vector with acceptance bands
    resource_caps?     : set of unitful caps (Γ_work categories)
    time_window?       : Γ_time window & cadence
  }
  AdmissibilityConditionsId : policy-id                          // Aut-Guard policy naming gates & penalties
  overrideProtocolRef : Episteme                     // SpeechAct & SoD for pause/resume/escalate
  telemetrySpecRef? : Episteme                       // what to emit into AutonomyLedger
  editionPins : { RoleRef?, MethodDescRef?, CHR refs, ... } 
}
```

**E.16‑S2 (Guarded enactment — Green‑Gate).**
A **Method step** that *requires* autonomy **MUST** list `requires: [RoleX]` **and** `requiresAutonomyBudget: AutonomyBudgetDecl.id`. A **Work** instance is admissible *iff* at enactment time:

* the performer’s **RoleAssignment** is valid and in an **enactable** RSG state (A.2.5);
* the budget accounting for the **AutonomyBudgetDecl** indicates **tokens/limits remaining** for *this* budget in the declared **Γ_time** window (derived from the AutonomyLedger);
* all **guard checks** defined by `AdmissibilityConditionsId` evaluate to **pass** (e.g., risk ≤ band, resource ≤ cap).

Failing any gate **blocks** enactment (no “soft warnings” on Core surface).

**E.16‑S3 (Autonomy Ledger).**
All admissible Work **MUST** record **AutonomyLedger entries**:

```
AutonomyLedgerEntry {
  workId, performedBy: RoleAssignmentId
  budgetId, version, time
  deltas: { action_tokensΔ?, decision_tokensΔ?, riskΔ?, resourceΔ? }
  guardVerdicts: { name → pass|fail }
  pathIds: { PathId, PathSliceId }                  // for G‑suite parity/refresh
}
```

The ledger is **evidence**: attach to `U.Work` (A.15.1) and fold under **Γ_work** and **Γ_time** for reporting.

**E.16‑S4 (Overrides — SpeechActs & SoD).**
Every budget **MUST** reference an **OverrideProtocolRef** that defines canonical **SpeechActs**:

* **PauseAutonomy(budgetId)** — immediate stop of autonomy‑gated steps;
* **ResumeAutonomy(budgetId)** — resume after conditions;
* **NarrowAutonomy(budgetId, Δscope)** — apply stricter limits;
* **Escalate(budgetId)** — handover to a declared **SupervisorRole**.

**SoD:** The override caller **MUST NOT** be the same **RoleAssignment** that is consuming the budget (enforce `⊥` in the Context). All overrides are **Work** (SpeechActs) with **ledger entries** (zero or negative deltas as per policy).

**E.16‑S5 (Depletion behavior).**
When a budget **depletes** (no tokens / envelope exceeded / cap breached):

* **Block** further autonomy‑gated steps in the **same Γ_time window**;
* Emit **DepletionNotice** (SpeechAct), and either **Escalate** or **Park** per policy;
* Only a **ResumeAutonomy** SpeechAct from an admissible Role (per SoD) may reopen the gate.

**E.16‑S6 (Publication in UTS).**
UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy **MUST** include:

* `AutonomyBudgetDeclRef` (id & version);
* `Aut-Guard policy-id`;
* `OverrideProtocolRef`;
* declared **Scope (G)** and **Γ_time** window;
* edition pins for the referenced Role/Method/CHR.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18/C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

### 5) Archetypal grounding (Tell‑Show‑Show; human‑centric)

**Show‑A (U.System — mobile robot).**
`Robot_R7#NavigatorRole:Warehouse_2026` executes `Navigate_v3`.
`AutonomyBudgetDecl`: `action_tokens=10 k steps/day`, `risk_bands={maxSpeed ≤ 1.2 m/s, minDist ≥ 0.5 m}`, `resource_caps={battery ≥ 20%}`; `AdmissibilityConditionsId=Aut‑Guard‑R7‑v1`; override via `PAUSE`, `RESUME`, `ESCALATE` SpeechActs by `FloorSupervisorRole ⊥ NavigatorRole`. Ledger entries decrement `action_tokens`, track `minDist`. Depletion at 0 tokens halts autonomous moves and pages supervisor.

**Show‑B (U.Service — autonomous deploy).**
`DeployerRole` performs step “Promote to prod” under `AutonomyBudgetDecl` with `decision_tokens=3/day`, `risk_envelope={error‑budget burn ≤ 2% / day}`, guard “all pre‑deploy checks pass”. Overrides only by `CABChair#AuthorizerRole ⊥ DeployerRole`.
→ **Edit:** use `risk_bands` for consistency: `risk_bands={error‑budget burn ≤ 2% / day}`.

### 6) Conformance Checklist (SCR — E.16‑CC)

| ID            | Requirement                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E.16‑CC‑1** | Any autonomy claim **MUST** reference an **AutonomyBudgetDecl** in the same `U.BoundedContext`.                                                                             |
| **E.16‑CC‑2** | **Method steps** that depend on autonomy **MUST** name the `AutonomyBudgetDecl.id` and **MUST** be Green‑Gated by the budget’s guards at enactment.                         |
| **E.16‑CC‑3** | A **Work** admitted under autonomy **MUST** carry an **AutonomyLedgerEntry** with deltas and guard verdicts.                                                                |
| **E.16‑CC‑4** | **Overrides** are **SpeechActs** with SoD enforced (`⊥` between consumer and overrider roles); each override creates a ledger entry.                                        |
| **E.16‑CC‑5** | **Depletion** **MUST** block autonomy‑gated steps until a **ResumeAutonomy** SpeechAct passes SoD and guard checks.                                                         |
| **E.16‑CC‑6** | **UTS rows** for autonomy‑bearing Roles/Methods/Services **MUST** include `AutonomyBudgetDeclRef`, `Aut-Guard policy-id`, `OverrideProtocolRef`, `Scope (G)`, and `Γ_time`. |

### 7) Consequences

* **Testability.** Autonomy is measurable (tokens/envelopes), audit‑ready (ledger), and stoppable (SpeechActs).
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

### 8) Rationale & E‑/F‑/G‑links

* **E.8** — follows the pattern template (Context → Problem → Forces → Solution → Grounding → CC → Consequences).
* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, no “validity/process/actor/agent‑as‑noun” language; new lexical rule **L‑AUTO** added in edits below.
* **E.11 (ATS)** — authoring‑tier gates who may **mint** budgets/guards vs who may **use** them (diff below).
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** Role Assignment & Enactment (Green‑Gate), **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.
