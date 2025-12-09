## 15 · Conformance Criteria (normative “CC‑F18”)

> These are **language‑level** obligations for authors and reviewers. They ensure every unified name is **local‑first**, **bridge‑aware**, and **teachable**.

**CC‑F18‑1 (Context first).** Every unified name **SHALL** be grounded in **local senses** that were harvested and clustered **inside named Contexts** (“context of meaning”) prior to unification. No name may be minted from free‑floating glosses or Cross‑context intuition. Use F.1–F.3 first.

**CC‑F18‑2 (Bridge‑only sameness).** Claims of sameness across Contexts **SHALL** be expressed only via explicit **Bridges** with a stated congruence and loss note. Mere spelling similarity never licenses a unified name. Use F.9.

**CC‑F18‑3 (Twin‑register naming).** Each unified concept **SHALL** carry **two labels**—a **Unified Tech** label (used in Core prose) and a **Plain** label (used for teaching). Labels are chosen per the naming discipline of F.5 and the register rules of **E.10**.

**CC‑F18‑4 (Neutrality of the Tech label).** The **Unified Tech** label **SHALL NOT** be borrowed wholesale from any single source Context where that borrowing would re‑import that Context’s private distinctions. Prefer a **neutral** term; **Cross‑context reuse occurs only via the UTS row and explicit Bridges**. (See F.5 “allowed/forbidden forms”.)

**CC‑F18‑5 (One concept per row, one Tech label per row).** A unified concept **SHALL** be captured as **one Concept‑Set row** in the **UTS**. Exactly **one Unified Tech label** is normative for that row; additional legacy strings are aliases in Annex (budgeted). Use F.7 with F.17.

**CC‑F18‑6 (SenseCell citations).** For each unified name, the **SenseCells** (Context × Local‑Sense) that justify it **SHALL** be cited in the UTS row with **Context name + edition**. Omit edition only if the Context has a single stable edition. See F.17 §6.

**CC‑F18‑7 (Sheet‑level coverage).** Within a thread’s UTS, the **set of rows** carrying unified names **SHALL** collectively cite **≥ 3 distinct Contexts**, ensuring breadth of evidence. Coverage is a property of the **sheet**, not of every single row. See F.17 §6 constraint.

**CC‑F18‑8 (No global words).** In Core text, **“Context” always means `U.BoundedContext`**; **discipline columns** may be used in teaching layouts but **is not** a bearer of meaning. Do not write context‑free claims of sameness. See E.10 and F.17 §5.

**CC‑F18‑9 (Didactic primacy).** A unified name **SHALL** be teachable on **one page**: its **UTS row** + a short narrative that a careful reader can replay (F.16 template). If it cannot be taught concisely, the naming attempt is premature.

**CC‑F18‑10 (No lifecycle connotations).** Names **SHALL NOT** encode imagined “maturity stages” or time‑ordering unless those are part of the concept’s intension. Stages belong in **state‑space** and dynamics narratives, not in names. (See A‑series CHR patterns.)

**CC‑F18‑11 (Strict distinction guard).** Names **SHALL** respect **A.7 Strict Distinction**: do not collapse **Role ↔ Method ↔ Work** or **Status ↔ Description** into one word. Align with F.11/F.12 where relevant.

**CC‑F18‑12 (Change control via F.13).** Renames, splits, merges, and retirements **SHALL** follow F.13’s lexical continuity rules; the UTS remains the canonical public surface for these changes.

**CC‑F18‑13 (Lexical Pareto discipline).** When a Name Card uses **NQD‑CAL (C.18)** to score label candidates, the **chosen Unified Tech label** **SHALL** lie on the **Pareto frontier** of the lexical Q‑tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` (per **C.16** ordinal discipline and P1’s NQD‑front definition), unless an explicit exception is recorded. If authors deliberately select a dominated candidate (e.g., to honour legacy regulation or user muscle memory), the Name Card’s notes **MUST** state the reason for stepping off the frontier.

**CC-F18-13 (NQD-front surfaced, with honest diversity).**  
When a Name Card is in **MintNew** mode, the **candidate label set** and the resulting **NQD-front of non-dominated label candidates** over the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` **SHALL** be explicitly recorded on the Card (at least as a small table or list), together with the NQD evidence hooks (`DescriptorMapRef`, `DistanceDefRef`, and a brief `Diversity_P` / coverage summary).  
Each candidate **SHALL** carry a **head-term family** tag; morphological or prepositional variants built on the same head (e.g. “X plane”, “plane of X”, “planar X”) **MAY NOT** be counted as distinct for Diversity_P. The Card **SHALL** indicate how many distinct head-term families are represented on the NQD-front.  
An NQD-front with fewer than **three** head-term families is permitted **only** if the Card records why no lexically more diverse alternatives survived the SemanticFidelity / AliasRisk filters (e.g., very narrow domain, frozen legacy idiom).

**CC-F18-14 (Selection from the front only).**  
The **Unified Tech** and **Plain** labels published on the UTS row for a unified concept **SHALL** be drawn from the currently recorded **NQD-front** on the Name Card. Publishing a Tech/Plain pair that is **not** on that front (or that is dominated with respect to the declared lexical Q-axes plus NQD) is **non-conformant**, except in explicit **DocumentLegacy** mode as defined in §5.1.

**CC-F18-15 (Mode declaration).**  
Every Name Card **SHALL** declare its `CardMode ∈ {MintNew, DocumentLegacy}`. For Core-surface naming of **U.Types** and other canonical FPF concepts, **MintNew** is the default; **DocumentLegacy** is permitted only when recording pre-existing external names and MUST (i) cite the legacy source, and (ii) either attach an NQD-front over viable FPF variants or record a short rationale why NQD search is out-of-scope.
