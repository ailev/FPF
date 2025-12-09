## 6.2 Twin‑Register Discipline (Tech / Plain)

**Plain twin (LEX).** A registry entry pairing the **authoritative Tech label** with a **display‑only Plain label** for one `U.Type` **in one `U.BoundedContext`**; governed by **PTG (Plain Twin Governance; in the LEX registry)** and referenced by `Twin‑Map ID (LEX)`. *“Plain twin” ≠ the **Plain register** (the register is where twins may be used; the twin is the 1:1 mapping).*
**Convention.** In this spec, **Plain** (capitalized) names the register; **plain twin** (lowercase) names the 1:1 mapping entry.

> **Rule R‑0 (Registers).** Every Kernel and Architheory concept has a **Tech label** (the testable semantic token) and an optional **Plain label** (didactic synonym). The **Tech label is authoritative**; the Plain label is permitted *only* in expository text and must map 1:1 to the Tech meaning inside the current **Context**.

### 6.2.1 Allowed pairs (normative table; examples)

| **Tech (authoritative)** | **Plain (didactic)**                        | **Notes & guards**                                                                           |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `U.System`               | system, machine, team                        | “Service” **never** stands for `U.System`; reserve **Service** for `U.Service` (see L‑SERV). Avoid “service‑instance” as a Plain twin; prefer “system instance” if needed. |
| `U.Episteme`             | body of knowledge, document, dataset, model | Pair must respect **Carrier vs Content** (A.7).                                              |
| `U.Method`               | how‑to, procedure (abstract)                | Do **not** call this “process” (L‑PROC).                                                     |
| `U.MethodDescription`    | recipe, SOP, playbook, code, spec‑text      | If testable, call out **Spec** explicitly per E.10.D2 (I/D/S).                               |
| `U.Work`                 | run, execution, activity, job, case         | Never use “process” or “procedure” here.                                                     |
| `U.Role`                 | role, hat, mask                             | Always **context‑indexed** per D.CTX.                                                        |
| `U.Service`              | promise, offering, external Standard        | Never equate to provider system or API (L‑SERV).                                             |
| `U.Capability`           | ability, capacity (within bounds)           | Separate from Role/Method/Work; must carry **envelope & measures**.                          |
| `U.Dynamics`             | law of change, model of evolution           | Not a capability or a method.                                                                |

**R‑1 (Plain first‑use).** At first use in a section, show **Tech label** and (optionally) the Plain twin: *“…a `U.Method` (the **how‑to**), described by a `U.MethodDescription` (the **recipe**) …”*
**R‑2 (No unpaired Plain in CC).** Conformance Checklists must use **Tech labels** only.

Domains can mint aliases inside their `U.BoundedContext` glossary; all aliases must map 1:1 to a Tech label (**SenseCell** row in the Context’s **Concept-Set Table**), and if exported across Contexts, via an **Alignment Bridge** (with **CL/Loss**).

 Make “plain twins” (reader‑friendly labels) **safe by construction**, not just style. The plain twin must **not** change kind, scope, or reader expectations versus the canonical Tech name; it is **display‑only** and **context‑local**.

* **Tech name (tech)** — the canonical, kernel‑conformant label used in **normative** clauses (e.g., `U.RoleAssignment`, `TransformerRole`).
* **Plain twin (plain)** — a didactic **display alias** permitted in **expository** prose and UI surfaces **inside one `U.BoundedContext`**.

> **Principle:** *Meaning lives in the Tech name; the plain twin may never move meaning.* (Locality is enforced by `U.BoundedContext` and Bridges.)

### 6.2.2 Plain Twin Safety constraints (normative)

**CC‑TWIN‑1 · One‑to‑one & local.**
Each Tech name has **at most one** plain twin **per `U.BoundedContext`**; the same plain twin **MUST NOT** point at more than one Tech name in the same Context.

**CC‑TWIN‑2 · Sense‑equivalence proof.**
A plain twin **MUST** bind to the **same SenseCell** as its Tech name in that Context (F.3/F.7). Authors **MUST** record at least one **counter‑example test** showing how the twin could be misread and why it still passes **in this Context** (SenseCell notes).

**CC‑TWIN‑3 · Head‑term discipline (HND).**
The plain twin **MUST** preserve the **head term** of the Tech name, or append an explicit bracketed head on **first use**:

* Roles keep **“(role)”**, Services keep **“(service)”**, Methods keep **“(method)”**, Work keeps **“(work record)”**, Capability keeps **“(capability)”**.
  *Examples:*
  `TransformerRole` → “**Transformer (role)**”,
  `U.Service` → “**Service (service)**”,
  `U.Work` → “**work (work record)**”.

**CC‑TWIN‑4 · Kind‑consistent.**
A plain twin **MUST NOT** map across **Kinds** (C.3). If the twin’s everyday reading could denote a different Kind (e.g., *Tradition* = organization, corpus, domain), it is **forbidden** unless qualified by a bracketed head and **Context gloss** on first use (see CC‑TWIN‑7).

 **CC‑TWIN‑5 · Ambiguity stop‑list.**
The following base nouns are **reserved** and **MUST NOT** be used as unqualified plain twins: *Tradition, service, process, function, model, system, method, standard, library, dataset, evidence, activity, task, action*.
They are allowed **only** with an explicit head per **CC‑TWIN‑3** and a **Context gloss** (CC‑TWIN‑7). *(This list MAY be extended in the registry.)*

**CC‑TWIN‑6 · No cross‑context by label.**
Plain twins are **not portable**. Reuse in another `U.BoundedContext` requires a **Bridge** with CL and loss notes; names alone carry no authority.

**CC‑TWIN‑7 · First‑use gloss.**
At first occurrence in a document or screen, a plain twin **MUST** be shown as **“Plain twin \[Tech name] — Context gloss”**, e.g.:
“**Transformer (role)** \[**TransformerRole**] — *mask borne by a system to enact a method step in OR\_2025*”.

**CC‑TWIN‑8 · Normative surface ban.**
Plain twins **MUST NOT** appear in **Conformance Checklists, predicates, type signatures, or acceptance clauses**. Only Tech names are normative. (Plain twins are strictly didactic.)

**CC‑TWIN‑9 · Twin budget.**
**At most one** plain twin per Tech name per Context. Synonym piles are prohibited (control vocabulary sprawl; see F.14).

**CC‑TWIN‑10 · Registry entry & DRR.** 
Every plain twin **MUST** have a **registry entry** (in the LEX registry) recording: `tech`, `plain`, `context`, `head`, **SenseFidelity = {3,2,1,0}**, ambiguity notes, counter‑examples, DRR id. Any change requires a **DRR**. 

**CC‑TWIN‑11 · Tests.**
 Twin entries **MUST** pass the **Twin Harness** (see F.15): *Head term*, *Kind consistency*, *SenseCell match*, *Stop‑list compliance*, and *First‑use gloss*.
