## 10 · Migration notes (quick wins)

1. **Name the promises.** List 5–15 consumer‑facing promises your context lives by; reify each as `U.Service` with `acceptanceSpec` and, if needed, `accessSpec` and `unitOfDelivery`.
2. **Separate provider from service.** Keep systems/teams as `U.System`; make them providers via `…#ServiceProviderRole:Context`.
3. **Wire evidence.** Ensure every relevant `U.Work` has `claimsService` (and `fulfilsService` post‑verdict).
4. **Choose metrics.** For each Service, define 2–4 KPIs and the **exact** Work-based formulas (availability, lead-time, rejection rate, cost-to-serve), and declare the **Claim scope (G)** and **Γ_time** policy used for each KPI.
5. **Bridge domains.** If a business ontology already exists (“business/technical/internal service”), keep it in its own context and map to `U.Service` via Bridges.
6. **Tidy language.** Apply **L‑SERV**: ban “service” as a synonym for server/team/process/ticket in kernel narratives; map them explicitly.

---
