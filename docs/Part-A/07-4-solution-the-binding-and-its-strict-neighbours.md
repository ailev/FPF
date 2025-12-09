## 4 · Solution — the binding and its strict neighbours

### 4.1 Canonical definition (notation‑free)

**`U.RoleAssignment`** is a **context‑local** binding:

```
RoleAssignment ::= 〈holder: U.Holon, role: U.Role, context: U.BoundedContext, window?: U.Window〉
```

**Invariants (normative).**

* **RA‑1 (Locality).** `role` **MUST** be defined in `context` (its meaning is exactly the one recorded in that Context’s RoleDescription/RoleSpec).
* **RA‑2 (No role‑of‑role).** `holder` **MUST** be a `U.Holon` (System, Episteme, or composite). Assigning roles **to roles** is forbidden.
* **RA‑3 (Eligibility by role family).**

  * **Behavioural / Agential / Constructor roles**: `holder` **MUST** be a `U.System`. Only systems can enact Methods and produce Work.
  * **Epistemic‑status / Normative‑status roles** (e.g., *Evidence*, *Standard*, *Requirement*): `holder` **MUST** be a `U.Episteme`.
  * **Service‑governance roles** (e.g., *ServiceOffering*, *SLO‑Clause* as status carriers): holder is typically a `U.Episteme`; execution still requires a System in a behavioural role.
    *(Contexts may refine eligibility, but cannot weaken these families.)*
* **RA‑4 (Window discipline).** If `window` is present, enactments (below) **MUST** occur within it; if absent, interpret as “open‑ended from assignment time”.
* **RA‑5 (Separation).** A RoleAssignment confers **the capacity/authorization to act** (or the status to be recognised), but it is **not behaviour** (no Work implied), **not capability** (intrinsic ability lives elsewhere), and **not structure** (may never appear in a BoM).
 
  Never use "appointment" as a synonym to "assignment".

**Didactic read.** Think **badge** (*who wears which mask, where, when*). The rules for the mask live **in the room** (Context).

**Two assignment modes**
A RoleAssignment can be:
(a) Authoritative — issued by an authority or policy in the Context (often via a SpeechAct Work); it can open the Green‑Gate for steps that require explicit authorization.
(b) Observational — an evidence‑backed classification that the holder occupies a Role in this Context (e.g., “Moon as SatelliteRole:IAU_2006”). Observational assignments never by themselves open operational Green‑Gates; they can gate decisions and analysis.

### 4.2 Role Enactment (distinct from the assignment)

**`U.RoleEnactment`** captures the *run‑time* fact that **a specific piece of Work** was performed under **a specific Role Assignment**:

```
RoleEnactment ::= 〈work: U.Work, by: U.RoleAssignment〉
```

**Invariants.**

* **RE‑1 (Actor reality).** `by.holder` **MUST** be a `U.System`. (Epistemes never enact Work.)
* **RE‑2 (Temporal fit).** `work.window` **MUST** overlap `by.window` (or `by.window` is open and contains `work.window`).
* **RE‑3 (Method gate).** For the `MethodStep` realised by `work`, `by.role` **MUST** satisfy the step’s `requiredRoles` in that **same Context** (directly or via `≤` specialization inside the Context).
* **RE‑4 (Traceability).** Every `U.Work` **MUST** reference exactly one `U.RoleEnactment` (hence a determinate RoleAssignment) as its performer.

*Reading:* **Assignments authorize; enactments happen.** That single sentence prevents months of muddled logs.

Role Enactment is the occurrence of `U.Work` performed by a `holder` while a valid `U.RoleAssignment` for the required Role is in an enactable state of its RoleStateGraph (A.2.5) within the same Context. Enactment is generic: it includes operational work (e.g., actuation) and communicative work (speech acts such as approvals).

### 4.3 Role Characterisation Space (RCS) & Role State Graph (RSG)

These are **intensional facets** of a **Role**, not containers “inside” the Role. They are **recorded in** the **RoleDescription** (or **RoleSpec** once harnessed), per E.10.D2.

* **RCS (Role Characterisation Space).** A set of named characteristics that parameterise how the Role is understood in a Context (e.g., *AgencyLevel ∈ {None, Assisted, Delegated, Autonomous}*; *SafetyCriticality ∈ {SC0…SC3}*).
* **RSG (Role State Graph).** A directed graph of **named states** (nodes) and **admissible transitions** (edges) for the Role **within the Context** (e.g., *{Eligible → Authorized → Active → Suspended → Revoked}*).

  * Each **state** has a **Conformance Checklist** (set of observable cues) supporting **Evaluations** (“X ∈ *Authorized*@context in W”).
  * RSG governs **role state transitions**, independent of any Work instance.

**Discipline.** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, **never** “Role **contains** its states.”

---

### 4.4 Shorthand & reading

Use the canonical compact form in prose and diagrams:

```
Holder#Role:Context@Window
```

Examples:

* `PLC_17#Transformer:PipelineOps@2025‑04‑01..2025‑06‑30`
* `ISO_26262v2018#NormativeStandard:AutoSafetyCase` *(status role on an Episteme; no enactment)*

*The shorthand is didactic; the semantics are those of §§4.1–4.3.*

---

### 4.5 Independence of role families (no chains)

Role families (e.g., **Agential**, **Constructor/Transformer**, **Observer/Measurer**, **Status**) are **independent**. A Context may state that *`Surgeon ≤ Clinician`* **within the same family**, but **MUST NOT** model “Transformer is an Agent” by chaining RoleAssignments. When a holder must satisfy **both** an Agential and a Transformer requirement, the **MethodStep** **requires both** roles; the holder **wears two badges**, not a badge‑of‑a‑badge.
