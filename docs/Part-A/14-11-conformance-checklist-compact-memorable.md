## 11 · Conformance checklist (SCR) — compact, memorable

> **Pass these and your RoleAssignments are sound.**

**Anchoring & locality**

1. **CC‑CTX‑1.** Every `role` reference names a **role defined in the same `U.BoundedContext`** as the assignment.
2. **CC‑CTX‑2.** No cross‑Context equivalence is assumed by label; relations across Contexts live only in **Bridges** (F.9).

**Eligibility & families**
3\. **CC‑ELIG‑1.** Behavioral roles (`Agential/Transformer/Observer/Speech`) **MUST** bind **`U.System`** holders.
4\. **CC‑ELIG‑2.** Status roles (`Epistemic‑Status/Normative/Service‑Governance`) **MUST** bind **`U.Episteme`** holders.

**Role algebra (in‑Context)**
5\. **CC‑ALG‑1.** `≤` permits substitution for `requiredRoles`.
6\. **CC‑ALG‑2.** `⊥` forbids overlapping windows on the same holder.
7\. **CC‑ALG‑3.** `⊗` expands to conjunctive checks at performance time.

**Time & gating**
8\. **CC‑WIN‑1.** Historic RoleAssignments are never deleted; windows are **closed**, not erased.
9\. **CC‑ENACT‑1.** Every `U.Work` has `performedBy = some U.RoleAssignment`.
10\. **CC‑ENACT‑2.** At the `U.Work` timestamp, an **enactable** `RSG` state is asserted for that assignment (via **StateAssertion**).
11\. **CC‑ENACT‑3.** If state flips to non‑enactable (e.g., **Suspended**), enactment is blocked until an **Active** assertion reappears.

**Strict distinction & category hygiene**
12\. **CC‑SD‑1.** No Role in a BoM/structure tree; roles do not participate in mereology.
13\. **CC‑SD‑2.** Epistemes never enact Work; only Systems do.

**Traceability**
14\. **CC‑TRC‑1.** From any `U.Work`, reviewers can trace **performedBy → RoleAssignment → Role → (RCS,RSG) → Context** and retrieve supporting **StateAssertion** evidence.

---
