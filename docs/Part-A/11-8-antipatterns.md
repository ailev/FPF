## 8 · Anti‑patterns (and the fast fix)

| #      | Anti‑pattern          | Symptom                                    | Why it’s harmful                   | FPF fix (conceptual move)                                         |
| ------ | --------------------- | ------------------------------------------ | ---------------------------------- | ----------------------------------------------------------------- |
| **A1** | **Global role label** | “Alice is Lead Engineer” (nowhere)         | Meaning drifts; untestable         | **Always anchor to Context**: `Alice#LeadEngineer:ProjectPhoenix` |
| **A2** | **Role as part**      | BoM lists “Cooling Function”               | Category error (structure vs role) | Keep BoM structural; model `Pump#Cooling:ThermalMgmt`             |
| **A3** | **Document acts**     | “The SOP closed the ticket”                | Epistemes don’t enact Work         | Give the doc a **status role**; make a System enact the step      |
| **A4** | **Role chains**       | “Transformer assigned to be Agent”         | Collapses independent families     | Require **both roles** on Method step; one holder, two badges     |
| **A5** | **Hidden state**      | Acting while *Authorized? Active?* unclear | Safety & audit gaps                | Use RSG with **StateAssertions** gating enactment                 |
| **A6** | **Edition blur**      | Context “ITIL” with no version             | Sense slippage                     | Context card must carry **edition** (E.10.D1/F.1)                  |
| **A7** | **Bridge‑by‑name**    | Equating roles across Contexts by label       | Cross‑context drift                   | Use **F.9 Bridge** with CL & loss notes                           |
