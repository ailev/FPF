## 8 · Evidence relations & operators (Service ⇄ Work)

To keep the promise → evidence path explicit:

### 8.1 Core relations

* **`claimsService(Work, Service)`** — the Work instance **intends** to fulfil the Service (pre‑verdict).
* **`fulfilsService(Work, Service)`** — the Work instance **meets** the Service’s `acceptanceSpec` (post‑verdict: pass).
* **`acceptanceVerdict(Work)`** → {`pass`, `fail`, `partial`, context‑specific grades} — computed by applying `acceptanceSpec` to Work facts.
* **`usesAccess(Work, MethodDescription)`** — consumer Work that invokes the service via its `accessSpec` (when applicable).

> **Invariant:** `fulfilsService(W,S)` ⇒ `claimsService(W,S)` and `acceptanceVerdict(W)=pass`.
> **Invariant:** A Work can claim/fulfil **multiple** Services only if the context declares a counting policy (no silent double‑counting).

### 8.2 Service performance operators

Let `W(S, T)` be the set of Work that `claimsService(·,S)` within time window `T`. Let `W✓(S, T)` be those with `fulfilsService`.

* **Delivered units:** `delivered(S, T) = |W✓(S, T)|` (or sum per `unitOfDelivery`).
* **Rejection rate:** `rejectRate(S, T) = 1 − |W✓| / |W|` (declare handling of `partial`).
* **Lead time:** average/percentile of `duration(Work)` or of request→completion delta (declare definition).
* **Availability/Uptime:** computed from Work/telemetry events per the context’s definition (declare availability source).
* **Cost‑to‑serve:** sum of `Γ_work` over `W✓` per resource category (A.15.1).

All metrics are **functions of Work evidence**; the Service object is never the bearer of actuals.
Aggregation across time uses `Γ_time` policies (union vs convex hull) chosen by the KPI owner.

---
