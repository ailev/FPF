## 10 · Migration playbook — turning messy language into ULR‑clean prose *(informative)*

> A pragmatic **three‑pass** routine. Works with plain text, diagrams, or models; no tools required.

### Pass 0 — *Pre‑flight (2 minutes per page)*

0.1 **Name the Context card** you’re writing in (title, edition, scope note).
0.2 For every new or renamed token, **declare `LEX.TokenClass`** ∈ {KernelToken, ContextToken, DiscriminatorToken}.
0.3 Run **MG·DA pre‑check** (anchored head noun; no metaphor heads; if enum → declare its **CharacteristicSpace**).
0.4 Run **collision/uniqueness**: full‑text grep + Reserved‑Names registry (see § 7). If collides → rename or DRR deprecate.

### Pass 1 — *Harvest in the Context*

1.1 **Underline overloaded words** (*process, service, function, workflow, ticket, approval, spec, plan,* …).
1.2 For each, write a **one‑line intent** in Plain register (what object‑of‑talk is meant).
1.3 Mark any cross‑Context reuse candidates.

### Pass 2 — *Map to Core anchors (mechanical)*

2.1 Replace underlined words via **§ 9 L‑rules** table:
 • recipe → **`U.Method` / `U.MethodDescription`**
 • scheduled run → **`U.Work` / `U.WorkPlan`**
 • promise → **`U.Service`**
 • ability → **`U.Capability`**
 • actor‑mask → **`…Role / RoleAssignment`**
 • document/evidence carrier → **`Episteme`** with **`EvidenceRole/RequirementRole`**
2.2 Apply **LEX.Morph** (§ 8): suffix gates (`…Role/…Work/MethodDescription/Service`), casing, reserved prefixes.
2.3 Pass **I/D/S layer** check: types/roles on I; recipes/docs on D; actuals on runs.
2.4 Attach **Context tags** on first use; set **twin labels** (Tech/Plain) in the local Glossary.

### Pass 3 — *Stitch & publish*

3.1 Add **safe rewrites** for any anti‑patterns you found (use § 9.2 quick table).
3.2 If sameness is needed across Contexts, create a **Bridge** (F.9) with relation kind, **CL**, and loss notes.
3.3 Publish a one‑page **UTS** (F.17) for the Context (columns: Context, Tech label, Plain label, Kernel anchor, Warnings).
3.4 Log a short **DRR** when renames/aliases occur (F.13), linking to grep results that motivated the change.

---
