## 9) Mini conformance checklist (cross‑E–F; author’s quick use)

1. **Declare** `AutonomyBudgetDecl` (scope, budgets, AdmissibilityConditionsId, overrides).
2. **Gate** steps with `requiresAutonomyBudget`.
3. **Emit** an `AutonomyLedgerEntry` for each admitted Work.
4. **Enforce SoD** on override SpeechActs; **block on depletion**.
5. **Publish** UTS autonomy fields for any autonomy‑bearing Role/Method/Service.

*(These five are sufficient for a working test harness in Part F.)*
