## 13 · Reasoning primitives (judgement schemas)

> **All judgements are conceptual.** They license or forbid specific *thinking moves*—not API calls, not workflows.

### 13.1 Bridge declaration

`⊢ Bridge(σA@RA, σB@RB) : ⟨senseFamily, kind, dir, CL, Loss, scope⟩`

*Reading:* There exists a declared Bridge between SenseCells `σA` and `σB` with stated attributes.

---

### 13.2 Substitution licence (senseFamily‑preserving)

`Bridge(σA,σB): ⟨senseFamily f, kind∈{≈,⊑,⊒}, dir A→B, CL≥2, Loss L⟩ ⊢ A↠B @f (Role Assignment & Enactment-eligible)`

*Reading:* A **Substitution Bridge** on the same senseFamily with **CL≥2** licenses **Role-Assignment/Enactment-level** substitution **in the stated direction**. (Type-structure requires **CL=3**.)

---

### 13.3 Naming‑only licence

`Bridge(σA,σB): ⟨kind∈{≈,⊑,⊒,⋂}, CL≥1⟩ ⊢ A⇝B (Naming‑only)`

*Reading:* A Bridge with **CL≥1** supports using a shared label in prose or Concept-Set **Naming-only** rows, without structural or Role Assignment & Enactment commitments.

---

### 13.4 Prohibition by kind

`Bridge(σA,σB): ⟨kind=⊥⟩ ⊢ ¬(A↠B) ∧ ¬(row(A,B))`

*Reading:* **Disjoint** forbids substitution and rows; only contrastive teaching is allowed.

---

### 13.5 Interpretation embargo

`Bridge(σA,σB): ⟨kind∈{⇄ᴅʀ,→ᴍᴇᵃ,→ᴅᵉᵒ}⟩ ⊢ Explanation‑only`

*Reading:* **Interpretation Bridges** never license substitution or rows.

---

### 13.6 Weakest‑link rule for rows

`row R uses {Bridge_i} ⊢ scope(R) = min_i(scopeAllowed(Bridge_i)) ∧ CL(R)=min_i(CL_i)`

*Reading:* The **row scope** and **row CL** are bounded by the weakest participating Bridge.

---

### 13.7 Direction guard

`Bridge kind=⊑ with dir A→B ⊢ ¬(B↠A)`

*Reading:* Narrower→Broader does **not** invert; only A may substitute into B under the stated scope.

---

### 13.8 SenseFamily purity

`Bridge scope=Role Assignment & Enactment-eligible ⊢ senseFamily(A)=senseFamily(B) ∧ stance(A)=stance(B)`

*Reading:* Role Assignment & Enactment-level substitution requires **same senseFamily** and same stance (run-time or design time).

---

### 13.9 Loss accumulation

`A↠B with Loss L₁ ∧ B↠C with Loss L₂ ⊢ A↠C allowed only if same senseFamily ∧ CL=min(CL₁,CL₂) ∧ Loss ⊇ (L₁∪L₂)`

*Reading:* Chained substitution is rarer; if used, **accumulate Loss** and respect the **minimum CL**. When in doubt, avoid chaining across Contexts.

---
