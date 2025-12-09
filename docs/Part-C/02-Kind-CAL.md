# C.3 · **Kind‑CAL — Kinds, Intent/Extent, and Typed Reasoning**  \[A]

> **One‑line summary.** Establishes **`U.Kind`** as the **minimal, context‑local intensional carrier** of “what a statement is about,” separates **intent** (KindSignature + its own **F**) from **extent** (*which* instances belong to the kind **in a given Context slice**), and situates **typed reasoning** alongside **USM Scope (G)** and **F–G–R** without conflation. Details of the core objects and operations live in **C.3.1–C.3.5**; guard shapes are standardized in **C.3.A**.

---


---

## 6 · Core Concepts (informative summary; authoritative norms live in C.3.1–C.3.5)  \[I]


> This section fixes the **Standard** of terms used in C.3 and points to the sub‑patterns for complete mechanics. All “**SHALL/MUST**” statements here are normative.

**Editorial note.** This section is **informative**. It restates manager‑level takeaways and **points to** the canonical, normative rules in **C.3.1–C.3.5**. Where this section summarizes a rule, treat the cited sub‑pattern (and rule ID) as the **source of truth**.


### 6.1 · `U.Kind` & `U.SubkindOf (⊑)`  \[A]

**Definition.** `U.Kind` is a **context‑local intensional object** naming a “kind of thing” that claims may quantify over.
**Order.** `U.SubkindOf (⊑)` is a **partial order** (reflexive, transitive, antisymmetric). We write `k₁ ⊑ k₂`.

**Summary of norms** *(authoritative text: **C.3.1 K‑01–K‑02**)*.
— Contexts treat `⊑` as a partial order and document any computed meets/joins if they provide them.
— Kinds do not carry Scope; Scope remains on claims/capabilities (USM).

> *Full treatment:* **C.3.1** (definitions, invariants, examples).

---

### 6.2 · **KindSignature** (intent) & **F**  \[A]

**Definition.** `KindSignature(k)` is the **intent**: predicates/invariants/Standards that define the kind in the Context. Its expression rigor has an explicit **`U.Formality`** (C.2.3).

**Summary of norms** *(authoritative text: **C.3.2 K‑03–K‑04**)*.
— `KindSignature(k)` declares its F (C.2.3). Claim‑level F does **not** auto‑inherit; weakest‑link applies on the claim’s own support paths.
— If a signature change alters membership, treat it as a content change (Contexts may version kinds).

> *Full treatment:* **C.3.2** (signature/intent with F; relation to claims).

---

### 6.3 · **Extension** & **MemberOf** (extent in a slice)  \[A]

**Definition.** `Extension(k, slice) ⊆ EntitySet(slice)` = set of instances that belong to `k` **in the given `U.ContextSlice`**. `MemberOf(e, k, slice)` is the membership predicate: `e ∈ Extension(k, slice)`.

**Summary of norms** *(authoritative text: **C.3.2 K‑05–K‑08**)*.
— Membership is deterministic for a fixed `(k, slice)` (no hidden “latest”).
— If `k₁ ⊑ k₂`, then `Extension(k₁,slice) ⊆ Extension(k₂,slice)` for all slices.
— Definedness may be bounded; outside it, guards fail closed.
— Keep **Scope (G)** and **MemberOf** as distinct guard predicates.

> *Full treatment:* **C.3.2** (extent semantics, examples, authoring hints).

---

### 6.4 · **KindBridge** & **`CL^k`** (type‑congruence)  \[A]

**Summary of norms** *(authoritative text: **C.3.3 KB‑01–KB‑12**)*.
— A KindBridge states Contexts/versions, kind mapping/rules, preserved order links, **`CL^k`** anchors, loss notes, and definedness.
— No inversions of preserved subkind links; collapses must be declared.
— When classification depends on a KindBridge, apply a monotone penalty **Ψ(`CL^k`)** to **R** (scope‑bridge **Φ(CL)** applies separately). **F** and **G** remain unchanged.
— Chaining uses weakest‑link on **`CL^k`**.

> *Full treatment:* **C.3.3** (bridge shape, anchors, examples).

---

### 6.5 · **RoleMask** (adaptation without cloning)  \[A]

**Definition.** `U.RoleMask(kind, Context)` is a **named binding** that carries constraints (optional **narrowing** of membership), vocabulary/notation aliases, and intended use for local procedures—**without** creating a new Kind.

**Summary of norms** *(authoritative text: **C.3.4 RM‑01–RM‑08**)*.
— Masks are registered/versioned; constraints are observable/deterministic at guard time.
— Do not treat masks as kind synonyms; promote frequently reused constraint masks to explicit subkinds (`⊑`).


> *Full treatment:* **C.3.4** (mask taxonomy, guard discipline, promotion rule).

---

### 6.6 · **KindAT (K0…K3)** — *informative facet*  \[I]

**Status.** A **facet** attached to `U.Kind`, not a Characteristic: no algebra, **never** used in guards or composition.

**Anchors (intentional view).**
**K0** Instance; **K1** Behavioral pattern; **K2** Formal kind/class; **K3** Up‑to‑Iso.

**Use.** Helps plan **ΔF/ΔR** and forecast bridge style (e.g., K3↔K3 suggests up‑to‑iso mapping). Do **not** conflate AT with **G** or **R**.

> *Full treatment:* **C.3.5** (manager heuristics, anti‑misuse).

---

### 6.7 · Quick examples (two‑characteristic awareness)  \[I]

**E‑Sketch 1 — Policy over `Vehicle`.**
Claim: “For all `x ∈ Vehicle`: brakeDistance(x) ≤ 50 m (dry), ≤ 40 m (wet).”
– **describedEntity:** `Vehicle` (Kind, typically K2) — *what* we quantify over.
– **Scope (G):** `{surface∈{dry,wet}, speed≤50, rig=v3, Γ_time=rolling 180d}` — *where* the claim holds.
– **Extent in slice:** which instances the lab currently classifies as `Vehicle` (via `MemberOf`).
Typed checks happen **before** Scope intersection; **G** is not widened by “abstract wording.”

**E‑Sketch 2 — API rule over `AuthenticatedRequest`.**
Producer A emits `Request`; consumer B expects `AuthenticatedRequest`.
– If `Request ⊑ AuthenticatedRequest` **does not** hold, add an **adapter** or adopt a **subkind**; do **not** force fit by widening **G**.
– Scope remains independent (API version, Γ\_time policy); evidence/freshness sits in **R**.


---

# C.3.1 · **U.Kind & SubkindOf (Core)**  \[A]

> **One‑line summary.** Defines **`U.Kind`** as a **minimal, context‑local intensional carrier** for “what a claim is about,” and **`U.SubkindOf (⊑)`** as a **partial order** over kinds. **Kinds do not carry Scope.** Scope remains on **claims/capabilities** (USM). This core pattern supplies only identity, locality, and ordering; **intent & membership** (`KindSignature`, `Extension/MemberOf`) are specified in **C.3.2**, bridges & congruence in **C.3.3**, masks in **C.3.4**, and the AT facet in **C.3.5**.

---


---

# C.3.2 · **KindSignature (+F) & Extension/MemberOf**  \[A]

> **One‑line summary.** Specifies the **intent and extent** of kinds: (**i**) a **`KindSignature(k)`** (the intensional definition of kind `k`) that **declares its own Formality F**; (**ii**) an **`Extension(k, slice) ⊆ U.EntitySet(slice)`** and the **membership predicate** `MemberOf(e, k, slice)` that are **deterministic per `U.ContextSlice`**; (**iii**) **monotonicity** of extension under `SubkindOf`; (**iv**) a **definedness policy** that fails **closed** outside its domain. **Kinds still carry no Scope** (that rule lives in C.3.1); Scope stays on **claims/capabilities** (USM). This pattern gives managers and reviewers the **observable basis** to check “what counts as a member here and now” without entangling applicability (G) or assurance (R).

---


---

# C.3.3 · **KindBridge & CL^k — Cross‑context Mapping of Kinds**  \[A]

> **One‑line summary.** Defines **`KindBridge`** as the normative mechanism for moving **kinds** (their **intent** and selected **subkind‑of** links) between bounded contexts (“Contexts”). A bridge declares **how a source kind maps to a target kind**, which parts of the **`⊑`** order are preserved or collapsed, and publishes a **type‑congruence level `CL^k`** with **loss notes** and a **definedness area**. **`CL^k` penalties apply only to Reliability (R)** when a claim depends on Cross‑context classification; **F** (formality) and **G** (Claim scope) remain unchanged. Scope translation continues to use the **USM Bridge + CL** channel; **KindBridge** is a **separate, parallel channel** for describedEntity.

---


---

## 5 · Solution — The **KindBridge** object (overview)

A **KindBridge** connects **source** Context **A** and **target** Context **B** for a set of kinds. It declares:

1. **Mapping of kinds**: either to named target kinds or via **signature translation** rules.
2. **Order preservation**: which `⊑` links are preserved (monotone), which are **collapsed**, and which are **unknown** (not claimed).
3. **Type‑congruence `CL^k`**: reuses the **same anchors/labels** as **CL** (Part B) but applies to kind intent/order (not to Scope). *Gloss:* higher `CL^k` ⇒ closer preservation of kind intent and declared `⊑` links.
4. **Loss notes**: human‑readable list of invariants and subkinds **not preserved**.
5. **Definedness area**: the subset of `U.ContextSlice` characteristics where the mapping is **intended** to be used (e.g., certain Standards/versions).
6. **Determinism**: fixed versions + mapping rules ⇒ deterministic result (no “latest”).

**Effect on assurance.** When a **claim** in B depends on classification that goes through this bridge, **reduce R** by a monotone penalty **Ψ(`CL^k`)**. **Do not** change **F** or **G**.

---


---

# C.3.4 · **RoleMask — Contextual Adaptation of Kinds (without cloning)**  \[A]

> **One‑line summary.** Defines **`U.RoleMask(kind, Context)`** as a **context‑local adaptation** of a `U.Kind` that (a) adds **constraints** and/or **vocabulary bindings**, and (b) may **narrow** membership **deterministically** within a `U.ContextSlice`, **without creating a new kind**. RoleMasks are catalogued, versioned, and guard‑addressable; frequent, stable constraint masks **SHOULD be promoted** to explicit **subkinds**. Cross‑context use of a RoleMask requires a **KindBridge** (for kinds) and, when needed, a **MaskAdapter** (for mask constraints). All penalties route to **R**; **F/G** remain unchanged.

---


---

## 5 · Solution — **RoleMask** (overview)

A **RoleMask** is a **named, versioned binding** `U.RoleMask(kind, Context)` that:

1. **Adds constraints** (entity‑level predicates only),
2. **Binds vocabulary/notation** (aliases, field maps) for the Context/process,
3. **May declare context expectations** (selectors over `U.ContextSlice`, e.g., jurisdiction, API version). **These are enforced via USM Scope guards** (A.2.6) and **do not** change mask membership.
4. **May narrow membership**: `Extension_mask(k, s) ⊆ Extension(k, s)` (entity‑level narrowing only),
5. **Never creates a new kind**; identity stays with `k`.
6. **Is guard‑addressable** and **deterministic** (no “latest”).

**Mask types (declared):**

* **Constraint mask** — adds constraints; may narrow membership;
* **Vocabulary mask** — aliases only; no membership change;
* **Composite mask** — both.

**Separation discipline.**

* **Entity‑level predicates** (e.g., “hasABS(x)”) → **mask membership** (narrowing).
* **Context conditions** (e.g., “jurisdiction=EU”, “API=v2.3”) → **USM Scope** guards (intersection), **not** mask membership.
  Masks **may carry both kinds** of information, but guards must route them into the **right channel**.

---


---

# C.3.5 · **KindAT — Intentional Abstraction Facet for Kinds (K0…K3)**  \[I/A]

> **One‑line summary.** Defines **KindAT** as an **informative facet** attached to `U.Kind` that classifies the **intentional abstraction stance** of a kind—**K0 Instance**, **K1 Behavioral Pattern**, **K2 Formal Kind/Class**, **K3 Up‑to‑Iso**—to **guide ΔF/ΔR planning, bridge expectations, catalog/search, and refactoring**. **KindAT is not a Characteristic**: it has **no algebra**, **no thresholds**, and **MUST NOT** appear in guards or composition math. All assurance remains in **F–G–R**; typed semantics remain in **C.3.1–C.3.4**.

---


---

# C.3.A · **Typed Guard Macros for Kinds + USM (Annex)**  \[A/I]

> **One‑line summary.** Provides **normative guard macros** that combine **USM Scope** (A.2.6) with **Kind‑CAL** (C.3.x) so authors can gate state changes and compositions that **quantify over kinds** without conflating **describedEntity** (Kinds) with **applicability** (Scope **G**) or **assurance** (**R**). Includes **decision trees, anti‑patterns, and examples** (informative). **AT (KindAT)** is **never** used in guards.

---
