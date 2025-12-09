## 9 · Worked Examples (multi‑architheory)

**9.1 Enactment — process vs activity (two context of meaning).**

* Use `BPMN_2_0:process` and `PROV_O_2013:activity` as **SenseCell**s.
* In a Concept‑Set row, code the provisional relation `⋈` (overlap), not an equality.
* Role Descriptions later reference **the specific SenseCell**, not “an anchor”.

**9.2 Roles — behavioural mask vs access status.**

* `BPMN_2_0:participant` vs `NIST_RBAC_2004:role`.
* Mark `⟂` (incompatible) in the Concept‑Set row to prevent conflation.
* Any cross‑use requires E.10.U9 with explicit loss policy.

**9.3 Services & evidence.**

* `ITIL4_2020:service` / `ITIL4_2020:service‑level‑objective` with KD‑CAL cells `SOSA_SSN_2017:observation`.
* References in acceptance patterns point to **SenseCell**s; provenance stays within the PROV Context.

---
