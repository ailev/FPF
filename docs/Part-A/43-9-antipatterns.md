## 9 · Anti‑patterns (and the right move)

* **“The microservice **is** the service.”**
  A microservice binary is a `U.System`. Make it a provider via `System#ServiceProviderRole:Context`; keep the **promise** in `U.Service`.

* **“The API **is** the service.”**
  The API is typically `accessSpec : MethodDescription` (and systems playing interface roles). The **service** is the promise judged by `acceptanceSpec`.

* **“Our **process** is the service.”**
  Process/recipe is `U.Method/MethodDescription`; schedule is `U.WorkPlan`. The service is **what is promised to the consumer**.

* **“The **ticket** is the service.”**
  A ticket/case is `U.Work` (and perhaps a `WorkPlan` item). Evidence and outcomes sit on Work, not on Service.

* **“Attach cost to the service.”**
  Actual cost/time attach to `U.Work` only (A.15.1). Service metrics are computed **from** Work.

* **“Put service under BoM.”**
  Services are not structural parts. Keep PBS/SBS clean.

* **“Hard‑code people into the service.”**
  Name **role kinds** in `U.Service`; run‑time performers are `U.RoleAssignment`s.

---
