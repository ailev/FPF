## 7 · Conformance (normative)

This section defines what it means to **use F correctly** in KD‑CAL. All “**SHALL**/**MUST**/**SHOULD**/**MAY**” statements here are normative.

### 7.1 · Declaration & Semantics

* **CC‑F‑1 (Declaration).** Every normative `U.Episteme` **SHALL** declare exactly one value for `U.Formality` (**F ∈ {F0…F9}**, or a context‑defined sub‑anchor that maps to one of these).
* **CC‑F‑2 (Ordinality).** F is an **ordinal Characteristic**: implementations **MUST NOT** perform arithmetic on F; only comparisons and thresholds are valid.
* **CC‑F‑3 (Polarity).** The polarity of F is **up**: a larger F value denotes **strictly greater or equal** expressive rigor than a smaller one.
* **CC‑F‑4 (No proxies).** Contexts **MUST NOT** introduce alternative “formality modes/tiers” as surrogates for F. If additional labels are desired, they **SHALL** be published as named **sub‑anchors** of F (see §4.3).

### 7.2 · Locality, Extensibility, and Anchors

* **CC‑F‑5 (Local extensibility).** A bounded context **MAY** introduce intermediate anchors (e.g., F6.5) and domain‑named anchors (e.g., “F4‑OCL”), **provided that** (a) the global F0…F9 order is preserved, and (b) each sub‑anchor is explicitly mapped to a parent anchor.
* **CC‑F‑6 (Anchor conservation).** Sub‑anchors **SHALL NOT** redefine the global meaning of their parent anchor (e.g., anything under F8 remains **proof‑grade**).

### 7.3 · Composition & Granularity

* **CC‑F‑7 (Weakest‑link fold).** For any composite episteme (theory, spec, model), the effective Formality **F\_composite** along any essential support path **SHALL** be computed as the **minimum** F of its essential parts on that path.
* **CC‑F‑8 (Granularity rule).** If different parts of an episteme carry different F values, the **episteme‑level F** is the **minimum** over all **essential** parts (non‑essential/illustrative parts are excluded).
* **CC‑F‑9 (No averaging).** Implementations **MUST NOT** average or otherwise combine F values numerically; the min rule suffices.

### 7.4 · Orthogonality & Non‑Interference

* **CC‑F‑10 (Orthogonality to G/R).** Changes in scope/envelope (G) or evidence (R) **SHALL NOT** alter F unless the **expression form** of the claims changes. Conversely, raising F **SHALL NOT** be interpreted as raising R or broadening G.
* **CC‑F‑11 (Notation‑agnostic).** Changing notations or carriers (Symbol side) **does not** change F if the claim graph and its formal content are preserved. Any translation loss is accounted for by **CL** penalties in R, not by altering F.

### 7.5 · Bridges & Cross‑Context Use

* **CC‑F‑12 (Bridges keep F stable).** When a claim is used across bounded contexts via a Bridge, the original F value **SHALL** be preserved in attribution. If the receiving context requires a different expression form, it **MUST** produce a **new episteme** (with its own F).
* **CC‑F‑13 (CL is for trust, not F).** Any mismatch across contexts **SHALL** be handled via Congruence Level (CL) and its effect on R; CL **MUST NOT** be used to down‑rate F.

### 7.6 · Traceability & Change

* **CC‑F‑14 (Observable basis).** An assigned F **SHALL** be justifiable by observable content (e.g., presence of predicates/invariants for F4; mechanized proofs for F7+).
* **CC‑F‑15 (ΔF disclosure).** A **ΔF** move (raising or, if justified by discovered error, lowering F) **SHALL** be recorded as a content change to the episteme. Whether a context versions that change is outside this pattern’s scope.

---
