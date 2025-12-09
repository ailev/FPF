## 7 · Minimal Generality & Domain Anchoring (MG·DA) — names neither parochial nor vacuous

> **Principle (MG·DA).** A minted name is **as general as necessary and no more**, and its **head noun is anchored to the object‑of‑talk**. First classify the **NameToken (name of a concept: term, lexical unit) itself** using **`LEX.TokenClass`**, then apply the guardrails corresponding to that class: kernel tokens must unify **across domains**; discriminator/context tokens must make the **domain legible** *from the name itself*. Names too general to have obvious domain are **banned**. 

### 7.1 `LEX.TokenClass` (meta‑lexical; not a USM Scope)
**Definition.** `LEX.TokenClass : NameToken → {KernelToken | ContextToken | DiscriminatorToken}`.  
This is a **Characteristic on NameTokens** (symbols), used by the LEX registry and MG·DA lints.
It is **not** a USM scope and carries **no** truth/validity semantics.

### 7.2 `KernelToken` — Minimal Generality (MG‑K)
**MG‑K1 (Tri‑domain witness, MUST).** Maintain a DRR/Glossary note with **≥ 3 heterogeneous arenas** where the invariants hold (e.g., manufacturing, healthcare, cloud ops). If you cannot, narrow to a Context name or move qualifiers into **RCS** (Role Characterisation Space).
**MG‑K2 (No parochial nouns, MUST).** Kernel names **MUST NOT** contain domain nouns (*Ticket, Microservice, Patient, Developer*). Such nouns belong in **Context** or as **RCS Characteristics**.
**MG‑K3 (No vacuity, MUST).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use existing kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).
**MG‑K4 (Intent over mechanism, MUST).** Kernel type/role names encode **intent**, not mechanism. Mechanisms (algorithms, hardware form, recipe flavors) live in **RCS** or **Capability**.
**MG‑K5 (Notation independence, SHOULD).** The intensional meaning is separable from any one notation/toolchain.
**MG‑K6 (Refactoring safety, MUST).** If a name fails MG, do **not** mutate it silently. Record a DRR and apply F.13 **Lexical Continuity & Deprecation** (aliases; Bridges for Cross‑context mappings).

### 7.3 `DiscriminatorToken` / `ContextToken` — Domain Anchoring (DA‑D)
**DA‑D1 (Object‑of‑talk anchoring, MUST).** The head noun names the **object being classified** (e.g., *Sense*, *Context*, *Role*, *Bridge*, *Characteristic*). Readers can answer “**X of what?**” without external context.
**DA‑D2 (Characteristic, not axis, MUST).** Enumerated properties are named as **Characteristic**  within a **CharacteristicSpace** (MM‑CAL). Avoid spatial metaphors (*axis, dimension, plane, lane, tier, layer*) unless the metaphor is a **pattern‑defined primitive** in this spec.
**DA‑D3 (Enum clarity, MUST).** If the term denotes an enumeration, (a) the value set is **small and closed**, (b) membership criteria are obvious from the definition, (c) the **object‑of‑talk** is explicit in the name (e.g., `SenseFamily`, not bare *Family*, *RowPlane* or overly general *Facet*).
**DA‑D4 (Anti‑recipe, MUST).** Do not bake *how‑to* or local methods into discriminator names; those belong in `U.Method/MethodDescription` or **Capability**.
**DA‑D5 (Mapping discipline, MUST).** Cross‑context readings go through a **Bridge** (F.9). Discriminator names must not suggest global identity.
**DA‑D6 (Register discipline, SHOULD).** Keep normative tokens stable; synonyms live in **Plain** register only and must not appear in constraints/tests.
**DA‑D7 (Ban generic combinators, MUST).** Reject vague composites like *NameUseMode*, *NamingScope*, *RowFacet/RowPlane/RowLane*. Each candidate must pass **DA‑D1** and **DA‑D3** (object‑anchored head and explicit **CharacteristicSpace**).

### 7.4 Global tests (apply after 7.2/7.3)
**MG·DA‑T1 (Three‑arena witness).** If **`LEX.TokenClass`(t)=KernelToken**, you **MUST** provide the tri‑domain witnesses (7.2‑MG‑K1). Otherwise this is **SHOULD** (document at least one contrasting arena).
**MG·DA‑T2 (Object‑of‑talk).** The head noun uniquely signals the subject area; avoid free‑floating metaphors. **MG·DA‑T3 (Anti‑recipe).** Remove mechanism/implementation words; relocate to Method/Capability/RCS.
**MG·DA‑T4 (Enum clarity).** For enumerations, list the closed value set and its CharacteristicSpace.
**MG·DA‑T5 (Collision & Uniqueness, MUST).** Before merge, run a **full‑text search** over the corpus and the **Reserved‑Names registry**. The candidate **MUST NOT** collide with any existing token used in another sense anywhere in FPF. If a collision exists, either rename or raise a DRR to deprecate the prior token.
**MG·DA‑T6 (Teaching swap).** In didactic prose (E.10.D2), the term can be swapped in **without caveats**. 
**MG·DA‑T7 (Intensional ground, MUST).** The definition card states the intensional criterion for membership explicitly; reviewers can check membership without reading external narrative.

### 7.5 Compatibility with USM (how tokens and scopes meet)
**USM applies to acts, not tokens.** Mint/rename/use are **LexicalActs** that carry a USM scope. `LEX.TokenClass` constrains **where** a token may be used via an **AllowedScopes** policy:
**Conformance rule.** For any usage `u` of a token `t`: `LEX.TokenClass(t)=c  ⇒  USM.Scope(u) ∈ AllowedScopes(c).`

The LEX registry defines `AllowedScopes(c)` (e.g., `KernelToken` usage in normative kernel constraints is allowed; in Plain register outside a glossary is restricted; Context emissions of `KernelToken` require a Bridge/alias, etc.).

**Audit.** Violations are flagged as **SCR‑LEX‑Sxx** (see acceptance tests below).

### 7.6 Metaphor guidance (non‑binding heuristics)
Prefer **object‑anchored heads** to metaphors. If a metaphor is unavoidable, ensure it is (a) explicitly defined by a pattern here, and (b) unambiguous within the **NameClass**. Example families (use sparingly):
* **Progression metaphors** (*level, tier, ladder*): only where a **gate/upgrade** is defined by the pattern.  
* **Separation metaphors** (*lane, track*): only where parallel, non‑interfering flows are enforced by rules.  
* **Grouping metaphors** (*family, class*): only for **small, closed enumerations** attached to a clearly named object‑of‑talk (e.g., `SenseFamily` rather than bare *Family*).

### 7.7 Short‑form and acronym discipline
**SF‑1 (First expansion, MUST).** On first use, expand the term; place the short‑form in parentheses (e.g., “Minimal Generality & Domain Anchoring (**MG·DA**)”).  
**SF‑2 (Uniqueness, MUST).** Register short‑forms in the **Reserved‑Names** list; run the collision check (7.4‑MG·DA‑T5).  
**SF‑3 (Form, SHOULD).** Prefer typographic separators (**MG·DA**) to fused acronyms (**MGDA**). Use the fused form only in code or identifiers where punctuation is disallowed, and only after registration.

### 7.8 Examples (illustrative, canonical)
Prefer **`U.Service`** (promise) over *BusinessService*; **`U.Capability`** over *Function*; **`U.Dynamics`** over *NaturalProcess*; **`U.WorkPlan`** over *ScheduleProcess*.  
Do **not** mint *ETLService* at kernel level—model ETL as `MethodDescription`; the **Service** is “data delivered under acceptance.”

### 7.9 Acceptance & regression checks (LEX/USM)
**SCR‑LEX‑S01 (TokenClass declaration).** Every normative token has a declared `LEX.TokenClass`.
**SCR‑LEX‑S02 (Collision & uniqueness).** Full‑text + Reserved‑Names check passes (no other meaning in FPF).
**SCR‑LEX‑S03 (Object‑of‑talk anchoring).** Heads name the object classified (DA‑D1).
**SCR‑LEX‑S04 (CharacteristicSpace).** Enumerations declare their value set and space (DA‑D2/3).
**SCR‑LEX‑S05 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
**SCR‑LEX‑S06 (Slot/Ref suffix discipline).** Any token with suffix **`…Slot`** or **`…Ref`** is either (a) a **SlotKind**/**RefKind** declared under A.6.5, or (b) a episteme field whose type is a RefKind; no ValueKind or other type class may end with these suffixes.
**RSCR‑LEX‑E01 (Banned generics).** Reject tokens matching the banned combinators list (DA‑D7).
**RSCR‑LEX‑E02 (Metaphor hygiene).** If a metaphor is used, show the pattern that defines it; otherwise rename.
**RSCR‑LEX‑E03 (Strategy token minting).** Reject new Kernel tokens named **Strategy**/**Policy** as kinds; model them as **lenses/flows/compositions** inside **G.5** or as **…Description/…Spec** in Contexts. (Prevents kernel overloading; aligns with C.22 “no minted Strategy head”.)
