## 13 · Acceptance Tests (SCR/RSCR stubs)

**SCR — Static discipline checks**

* **SCR‑DCTX‑S01.** No occurrence of the token **anchor** in normative sections.
* **SCR‑DCTX‑S02.** All formal uses of “Context” resolve to **`U.BoundedContext`**.
* **SCR‑DCTX‑S03.** Pattern headers contain **Problem Frame** instead of “Context”.
* **SCR‑DCTX‑S04.** All semantic references use the forms in Sec. 5.
* **SCR‑DCTX‑S05.** No “domain context” strings; Domain appears only as family metadata.
* **SCR‑DCTX‑S06.** No is‑a or containment relations between contexts outside **E.10.U9**.

**RSCR — Regression discipline checks**

* **RSCR‑DCTX‑E01.** Adding a new family or edition does not introduce “domain context” or context hierarchies.
* **RSCR‑DCTX‑E02.** Refactors of E.10.U1/U.2/U.7/U.9 do not re‑introduce “anchor”.
* **RSCR‑DCTX‑E03.** Multilingual updates follow D‑CTX‑7 (split/merge rationale recorded informatively).
  