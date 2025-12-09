## 10 · Micro‑examples (illustrative, one‑liners)

1. **Participant vs Agent (workflow vs provenance)**
   *Cells:* `BPMN:Participant` ↔ `PROV:Agent` • *senseFamily:* Role • *Kind:* ⋂ (overlap) • *CL:* 2 • *Loss:* participation vs attribution scopes differ • *Use:* **Naming‑only** (“actor”).

2. **Process (design) vs Activity (run)**
   *Cells:* `BPMN:Process` ⇄ᴅʀ `PROV:Activity` • *senseFamily:* Method ↔ Execution • *Kind:* **Design‑spec ↔ Run‑trace** • *CL:* 2 • *Loss:* graph vs event; concurrency vs temporalization • *Use:* **Explanation‑only**.

3. **Observation vs SLO check**
   *Cells:* `SOSA:Observation` →ᴍᴇᵃ `ITIL:SLO‑fulfilment` • *senseFamily:* Measurement → Status • *Kind:* Measure‑of • *CL:* 2 • *Loss:* sampling window; target definition • *Use:* **Explanation‑only**.

4. **Subtype across OWL and curated taxonomy**
   *Cells:* `OWL:SubClassOf` ≈ `TaxonomyX:is‑a` • *senseFamily:* Type‑structure • *Kind:* ≈ • *CL:* 3 *(only if TaxonomyX is acyclic & anti‑symmetric)* • *Loss:* profile differences • *Use:* **Type‑structure** rows allowed.

5. **Accuracy (metrology vs data‑quality)**
   *Cells:* `ISO80000:accuracy` ⋂ `ISO25024:accuracy` • *senseFamily:* Measurement • *Kind:* overlap • *CL:* 2 • *Loss:* instrument vs dataset perspective • *Use:* **Naming‑only** row “accuracy”; methods stay context‑local.
