## 7 · Conformance Checklist (normative)

**CC‑A2.3‑1 (Type).**
`U.Service` **IS** an `U.Episteme` (a consumer‑facing promise on a carrier). It is **not** a `U.System`, **not** a `U.Method/MethodDescription`, **not** a `U.Work`, and **not** a `U.WorkPlan`.

**CC‑A2.3‑2 (Context).**
Every Service **MUST** be declared **inside** a `U.BoundedContext`. Names and meaning are **local**; cross‑context reuse requires a Bridge (`U.Alignment`).

**CC‑A2.3‑3 (Role kinds, not people/systems).**
`providerRole` and (if used) `consumerRole` **MUST** be **role kinds** (see A.2). Actual performers at run‑time are `U.RoleAssignment`s.

**CC-A2.3-4 (Acceptance).**
`acceptanceSpec` **MUST** be present and **MUST** define how delivered `U.Work` is judged (pass/fail/graded) against declared targets (SLO/SLA-like), and **MUST** declare **Claim scope (G)** where relevant (operating conditions, populations, locales). Every verdict binds to an explicit **Γ_time** window.

**CC‑A2.3‑5 (Access).**
If consumers must request/obtain the service through an interface, `accessSpec` **MUST** reference the MethodDescription that defines eligibility and invocation rules (API/desk/SOP). If the service is ambient (e.g., compressed air on a manifold), accessSpec **MAY** be omitted, but the eligibility condition **MUST** be stated in the context.

**CC‑A2.3‑6 (Unit of delivery).**
If performance is counted/charged, `unitOfDelivery` **SHOULD** be declared (e.g., “request”, “kWh”, “case”).

**CC‑A2.3‑7 (No actuals on Service).**
Resource/time **actuals** and incident logs **MUST** attach to `U.Work` only (A.15.1). Services carry no actuals.

**CC‑A2.3‑8 (Capability requirement).**
If the context requires provider abilities, it **MUST** express them as `bindsCapability(providerRole, Capability)` in the context, not by stuffing capabilities into the Service object.

**CC‑A2.3‑9 (Versioning & timespan).**
Services **MAY** carry `version`/`timespan`. A `U.Work` that claims/fulfils a Service **MUST** record which Service version it used.

**CC‑A2.3‑10 (Lexical rule).**
Unqualified uses of *service* (server/team/API/process/ticket) **MUST** be disambiguated per **L‑SERV** (E.10), mapping to `System`/`U.RoleAssignment`/`Method[Spec]`/`Work` as appropriate.

**CC‑A2.3‑11 (No mereology).**
Do **not** place a Service in PBS/SBS or treat it as a part/component. Structural assemblies live in PBS/SBS; Service is a promise.

**CC‑A2.3‑12 (Plan–run split).**
Windows and calendars belong to `U.WorkPlan` (A.15.2). Fulfilment evidence belongs to `U.Work` (A.15.1).

**CC-A2.3-13 (Scope lexicon & guards).**
Deprecated labels *applicability/envelope/generality/validity* **MUST NOT** appear as scope characteristics in guards or conformance blocks. Use **`U.ClaimScope (G)`** for epistemes and **`U.WorkScope`** for capabilities (A.2.6/A.2.2). Scope-sensitive guards **MUST** use **ScopeCoverage** with explicit **Γ_time** selectors.

**CC-A2.3-14 (Bridges & CL).**
Cross-context mappings via Bridges keep **F/G** stable; **CL** penalties apply to **R**. A mapping **MAY** recommend **narrowing** the mapped **Claim scope (G)** as best practice (A.2.6/B-line).
