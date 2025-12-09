## A.2.3 · `U.Service` \[D]

### 1 · Context

Across domains the word **service** is used for many different things: a server or **provider**, an **API**, a **procedure**, a **run**, a **department**, even a **product bundle**. Such polysemy is productive in everyday speech but toxic in a normative model. FPF needs a **single, minimal, trans‑disciplinary meaning** that stays stable from cloud computing to public administration and manufacturing utilities.

In the Role–Method–Work alignment, **service** must say something **external‑facing** and **consumer‑oriented**, yet remain separate from *how* the provider does it (Method/MethodDescription) and *what actually happened* (Work).

> Intuition: a **service** is the promise you advertise and are judged by; **work** is what you do to keep that promise; **method/spec** is how you know what to do.

#### Lexical note (L‑SERV)

The words *service/service‑level/service use/service access* are **ambiguous** across domains. In the kernel we reserve **`U.Service`** for the unified concept below. Other senses (department, server, microservice binary, help‑desk ticket, etc.) **must** be mapped via `U.RoleAssignment` to roles (`…#ServiceProviderRole:Context`), to **`U.System`**, **`U.Method/MethodDescription`**, or **`U.Work`**, inside the appropriate `U.BoundedContext`. (A short lexical rule **L‑SERV** will be added to E.10 alongside L‑FUNC/L‑PROC/L‑SCHED/L‑ACT.)

---

### 2 · Problem

Without a first‑class `U.Service`, models drift into five recurring errors:

1. **Provider = Service.** Calling the **system** or **team** “the service” collapses structure with promise.
2. **API = Service.** Treating an **interface/endpoint** as the service hides the consumer‑oriented promise (effect + acceptance).
3. **Process = Service.** Mapping a **procedure/Method** (or a WorkPlan) to “service” confuses recipe/schedule with the external commitment.
4. **Run = Service.** Logging **Work** as “a service” erases the Standard/promise layer and breaks SLA reasoning.
5. **Business ontology lock‑in.** Large domain schemes (e.g., “business service” stacks) are imported wholesale, losing FPF’s universality and comparability across contexts.

---

### 3 · Forces

| Force                                       | Tension                                                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **External promise vs internal capability** | Service must be consumer‑facing, while capability is provider‑internal.                                       |
| **Specification vs execution**              | Service is a **specifiable** obligation; value is **realised** only by runs of Work.                          |
| **Universality vs domain richness**         | One kernel meaning must cover IT, utilities, healthcare, public services—without absorbing domain taxonomies. |
| **Measurability vs privacy**                | Consumers need SLO/SLA and outcomes; providers want implementation freedom (Method autonomy).                 |
| **Stability vs evolution**                  | Services version and change without invalidating prior Work evidence.                                         |

---

### 4 · Solution — The unified concept `U.Service`

**Definition (normative).**
Within a `U.BoundedContext`, a **`U.Service`** is an **externally oriented commitment**: a **context‑local promise** that a provider **Role** will make a **specified external effect** available to eligible consumers through a **declared access** and **declared acceptance criteria** (SLO/SLA‑like targets). A `U.Service` does **not** prescribe *how* the provider fulfils it (that is `U.Method/MethodDescription`), nor is it the **execution** (that is `U.Work`).

* **Type:** `U.Episteme` (a spec/Standard on a carrier).
* **Scope:** design‑time concept; judged at run‑time by evidence from `U.Work`.
* **Time stance:** design-time concept; judged at run-time by evidence from `U.Work`.
* **Orientation:** consumer‑facing (“what you can rely on”), as opposed to capability (“what we can do”).

#### 4.1 · Core structure (minimal fields)

```
U.Service {
  context        : U.BoundedContext,   // where the promise is meaningful
  purpose        : Text/Episteme,      // the externally observable effect/value
  providerRole   : U.Role,             // role kind that may provide it (not a person/system)
  consumerRole?  : U.Role,             // optional role kind allowed to consume
  claimScope?    : U.ClaimScope,       // where the promise holds (G) — operating conditions/populations/locales
  accessSpec?    : U.MethodDescription,       // how consumers may request/use (interface/eligibility)
  acceptanceSpec : U.Episteme,         // targets: SLO/SLA, quality/throughput/latency/accuracy…
  realizationSpec?: P(U.MethodDescription),   // typical internal specs used by providers (non-binding)
  unitOfDelivery?: Episteme,           // how delivered units are counted/measured
  version?       : SemVer/Text,
  timespan?      : Interval
}
```

* `providerRole` and `consumerRole` are **role kinds**; the actual performers are **RoleAssignings** at run‑time.
* `acceptanceSpec` defines **what counts as fulfilled** (the test).
* `accessSpec` is **how to ask** (eligibility, protocol, counter, desk, API).
* `realizationSpec` is only informative in the kernel (“typical methods”); providers retain **Method autonomy**.

#### 4.2 · What `U.Service` is **not**

* **Not a provider:** use `System#ServiceProviderRole:Context` `U.RoleAssignment`.
* **Not a method/recipe:** that is `U.Method/MethodDescription`.
* **Not a run/incident/ticket:** that is `U.Work`.
* **Not a schedule:** that is `U.WorkPlan`.
* **Not a capability:** capability is **provider‑intrinsic ability**; service is **outward promise**. A service may **require** certain capabilities, but it **is not** the capability.
* **Not a scope label:** do **not** use *applicability*, *envelope*, *generality*, or *validity* as **scope characteristics**; declare **Claim scope (G)** or **Work scope** explicitly where needed (A.2.6).

#### 4.3 · Position in the enactment chain

* **Design‑time:**
  The context **declares Claim scope (G)** for acceptance (operating conditions, populations, locales) per A.2.6.
  The context may assert: `bindsCapability(ServiceProviderRole, Capability)`.
  Providers choose `Method/MethodDescription` to realise the service.

* **Run‑time:**
  A **consumer** performs `Work` (e.g., a request/visit) — `performedBy: ConsumerRoleAssigning`.
  The **provider** performs `Work` to fulfil the service — `performedBy: ProviderRoleAssigning`.
  Delivered `Work` instances are evaluated against `acceptanceSpec` and **counted** via `unitOfDelivery`.
  SLA/SLO outcomes are therefore functions over **Work evidence**, not over the Service object itself.

> **Memory hook:** *Service promises, Method describes, Work proves.*

---

### 5 · Archetypal grounding (engineer‑manager friendly)

| Domain                    | **`U.Service` (promise)**                                 | Provider & Consumer (as Roles)                                   | Access (how to ask)                  | Fulfilment (Work)                        | Typical acceptance targets                  |
| ------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------ | ---------------------------------------- | ------------------------------------------- |
| **Cloud/IT**              | “**Object Storage**: durable PUT/GET of blobs up to 5 TB” | `CloudTeam#ServiceProviderRole`, `BackupJob#ServiceConsumerRole` | `S3_API_Spec_vX` (`MethodDescription`)      | Each PUT/GET run; data durability checks | Availability ≥ 99.9%, durability 11×9       |
| **Manufacturing Utility** | “**Compressed air** at 8 bar in Zone B”                   | `Maintenance#Provider`, `LineB#Consumer`                         | Manifold access rules (`AccessSpec`) | Compressor cycles & delivery logs        | Pressure window, purity class, flow ceiling |
| **Public Service**        | “**Passport issuance** within 20 days”                    | `Agency#Issuer`, `Citizen#Applicant`                             | Portal/desk SOP (`AccessSpec`)       | Case handling runs                       | Lead time ≤ 20 days, defect ≤ 1%            |

**Key takeaway:** the **same kernel object** models S3, a plant utility, and a government service: a **promise with access and acceptance**. Everything else (APIs, compressors, clerks, workflows, tickets) is mapped via **Role/Method/Work**.

---

### 6 · Mapping the common “service” picture to FPF (didactic bridge)

The popular service diagrams (provider ↔ access ↔ use ↔ capability/activity) map to FPF as follows:

* **Agent (as Service Provider)** → `System#ServiceProviderRole:Context` (`U.RoleAssignment`).
* **Service Agreement / SLA** → `U.Service.acceptanceSpec` (+ optional `WorkPlan` for windows).
* **Operating conditions / “where the promise holds”** → `claimScope : U.ClaimScope (G)` (or embedded in `acceptanceSpec`) per A.2.6.
* **Service Presence / Access** → `accessSpec : MethodDescription` (interface/eligibility); actual endpoints are **systems** playing interface roles.
* **Individual Service Use** → **consumer and provider `U.Work`** instances linked to the `U.Service` they fulfil.
* **Service‑Enabled Capability / Activity** → effects on the consumer side: either a **Capability** gained/used, or **Work** performed; do **not** reify as a new kernel type.

(Where a domain needs richer structures—catalogs, exposure layers, charging, entitlement—model them **in the domain context** and relate them to `U.Service` via `U.RoleAssignment` and alignment bridges.)
