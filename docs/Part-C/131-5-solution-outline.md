## 5 · Solution Outline (Normative)

**S1 — Exported objects.** C.16 **exports** four intensional constructs to be used by any architheory:

1. **`U.DHCMethodRef`** — the *binding* of **one `U.Characteristic`** to **one Scale form**, with declared **polarity** and a conceptual **compatibility claim** (what counts as “same‑scale” for comparison). It is an *intensional specification*, not a record layout.
2. **`U.Measure`** — an *assertion* that a **subject** occupies a **Coordinate** (or **Level**, if discrete) on that Scale; the measure **references** its template and carries a **conceptual pointer to evidence** (`U.EvidenceStub`).
3. **`U.Unit`** — the *unit kind* associated with the Scale where applicable (physical quantities, normalized “points”, “stars”, “%”); unit coherence is part of comparability conditions.
4. **`U.EvidenceStub`** — a *conceptual locator* of grounds for the asserted value (type, identifier, brief summary, optional integrity notion); sufficiency criteria are **conceptual** (see §9, later).

**S2 — Comparability stance.** C.16 states **conceptual comparability** conditions: *same Characteristic*, *compatible Scale type and parameters*, *unit coherence* for interval/ratio; **no** forced coercions for nominal/ordinal; any score‑producing gauge **must be monotone** w\.r.t. template polarity. (Details: §7–§8 in later parts.)

**S3 — Evidence stance.** A measure that, by its template, **requires** evidence, is **inadmissible** without a meaningful `U.EvidenceStub`. C.16 defines **what it means conceptually** for evidence to “connect” the subject, the Characteristic, and its symbolic description; mechanisms are out of scope. (Details: §9 in later parts.)

**S4 — RSG framing (open‑endedness).** Readiness, calibration, and revision of metric notions are expressed as **RSG node moves with checklists** (e.g., “characteristic anchored”, “Scale typed”, “Unit coherent”, “Gauge declared”), allowing **re‑entry** when distinctions change; there is no terminal “lifecycle”. (Details: §10, later.)

---

### 5.1 · Lexical Discipline & Registers (Normative)

**L1 — Canon.** Use **Characteristic / Scale / Level / Coordinate / Score / Unit / Gauge** in **Tech** register; their `U.*` counterparts in **Formal**; narrative labels (e.g., *axis*, *points*, *stars*) are **didactic only** at first‑mention mapped to canon (E.10). 
**L1‑bis — “metric”.** The noun *metric* is **not** a Tech‑register canonical token for measurables; use **Characteristic / Scale / Coordinate / Score / Gauge**. It **may** appear in the architheory title and in the Formal names `U.DHCMethodRef` / `U.Measure`. Do not use *metric* as a synonym for **Characteristic** or **Score** in normative prose.
**L2 — Intension vs Description.** Keep **intensional objects** (`U.DHCMethodRef`, `U.Characteristic`) distinct from **descriptions** (rubrics, exemplars) and from **claims** (`U.Measure`). No collapsing of names across these layers.
**L3 — No synonym sprawl.** In normative clauses do **not** substitute *dimension/axis/property/feature* for **Characteristic**; A.17 governs canonicalization. (C.16 inherits A.17’s rename policy.)
**L4 — Bridge‑only unification.** Cross‑vocabulary sameness appears only via **F.9 Bridges** with **CL** and **loss notes**; C.16’s lexicon is the *source* side for measurement rows.
**L5 — “Metric” in registers.** In **Tech/Formal** avoid the noun *metric* as a primitive; use `U.DHCMethodRef` / `U.Measure` / **Score**. In **Plain** register *metric* MAY denote “a Template+Measure family” on first mention, with an explicit pointer to canonical terms.
