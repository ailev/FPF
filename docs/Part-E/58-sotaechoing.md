## SoTA‑Echoing (post‑2015, multi‑Tradition)

> Each item states **Adopt / Adapt / Reject**, and why. Vendor/tool tokens are kept as *informative*, not normative.

1. **Applied category theory (compositional open systems).**
   **Adopt.** Monoidal composition and wiring justify “nodes as morphisms, edges as carriers” and functorial publication of faces; they also provide algebraic laws for joining subflows. (Fong & Spivak, *Seven Sketches in Compositionality*, 2019).

2. **Operads / wiring diagrams / hypergraph categories.**
   **Adopt/Adapt.** Typed ports and decorated cospans model interfaces and “Bridge” junctions; we adapt the operadic composition to require CL/Φ pins on every crossing (publication‑level requirement not present in the math). (Spivak, *Operads of Wiring Diagrams*, 2021; Baez & Fong, *A Compositional Framework for Passive Linear Circuits*, 2015).

3. **Open‑graph/string‑diagram rewriting.**
   **Adapt.** Rewriting systems capture subflow refactors, but E.TGA binds rewrites to edition bumps and sentinel scopes rather than global rewrites, to preserve auditability and replay. (Bonchi et al., *Graphical Linear Algebra*, 2019; Kissinger—survey lineage).

4. **Publication discipline & artefact portability.**  
**Adopt.** Edition‑pinning and immutable registries echo contemporary reproducibility practice; E⃗ stays explicit and compositional at the publication layer.

5. **Reproducibility & content addressability.**  
   **Adopt.** Edition‑pinning and immutable registries echo modern content‑addressable reproducibility (conceptual); E⃗ stays explicit and compositional at the publication layer.

6. **TAMP/MPC (integrated planning and control).**
   **Adopt/Adapt.** The budgeted Selection↔Planning loop follows contemporary TAMP practice; MPC‑style freshness/constraint checks motivate **FreshnessUpToDate** as a hard LaunchGate module and “bind‑in‑Work‑only”. (Garrett, Lozano‑Pérez, Kaelbling, *Integrated Task and Motion Planning*, 2021; Rawlings et al., MPC updates).

7. **Quality‑Diversity (QD) search.**
   **Adopt.** QD (e.g., CMA‑ME, 2020) justifies **set‑return** and archive semantics in `U.SelectionAndBinding`; E.TGA bans covert scalarization that would collapse archives to single “bests”.

8. **Profunctor optics (modular projections).**
   **Adopt/Adapt.** Optics motivate view/projection discipline behind MVPK faces; we adapt by forbidding MVPK faces from introducing new claims (they are pure projections, not transformations). (Pickering, Gibbons, Wu, **Profunctor Optics**, 2019).

*Cross‑tradition note.* Items 1–3 (category‑theoretic), 4–5 (publication/reproducibility concepts), 6 (controls/robotics), 7 (evolutionary search), and 8 (PL/semantics) jointly anchor E.TGA across multiple traditions, per E.8.
