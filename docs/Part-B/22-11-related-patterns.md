## 11 · Related Patterns

* **Extends:** **B.5.2 Abductive Loop** (Step 2/3 operationalization). 
* **Driven by / feeds:** **B.5 Canonical Reasoning Cycle** (Abduction→Deduction→Induction), **B.4 Evolution Loop** (Observe/Refine). 
* **Uses:** **A.17/A.18** for characteristic discipline and **B.5 ADI ordering**. **May** refer to Context‑specific MAP‑Elites/novelty‑search implementations in the MethodDescription. **No operational gating is in scope here.** C.17 (Use‑Value / ValueGain, normative definition).
* **Respects:** **A.11** (no kernel growth beyond CHR template import + Method).
  

### B.5.3 — Role-Projection Bridge \[A]

**Context**

The FPF is built upon a small set of universal, domain-agnostic concepts (`U.Types`) like `U.System`, `U.Objective`, and `U.State`. This universality is the source of its power, allowing it to be applied to any domain, from thermodynamics to software engineering. However, practitioners in these domains do not speak in terms of `U.Types`; they use their own rich, specialized vocabularies. A thermodynamicist talks about a "Thermodynamic System" and its "Macrostate," not a `U.System` and its `U.State`.

**Problem**

How can FPF bridge this gap between its universal core and the specific language of a domain without either polluting the kernel with domain-specific terms or forcing experts to abandon their familiar vocabulary? A simple alias mechanism (e.g., a dictionary mapping `U.System` to "Thermodynamic System") is insufficient because:

1.  **It's brittle:** It assumes a one-to-one mapping, which often breaks down. A single domain concept can play multiple universal roles in different contexts.
2.  **It's semantically poor:** It only captures naming, not the rich constraints and relationships that a domain-specific concept entails. We can't express that a "Thermodynamic System" is a *special kind* of `U.System` with specific properties related to temperature and pressure.
3.  **It's not integrated:** The mappings live outside the formal model, making them difficult to govern, version, and use in automated reasoning.

**Forces**

| Force | Tension |
| :--- | :--- |
| **Universality vs. Specificity** | How to maintain a lean, universal kernel while accommodating the rich, specific terminologies of countless domains. |
| **Flexibility vs. Rigor** | How to allow a single entity to be viewed through multiple lenses (e.g., as a physical system and an economic asset) without creating ambiguity. |
| **Integration vs. Isolation** | How to incorporate domain knowledge into the formal model without hard-coding it into the FPF kernel, thereby preserving the Open-Ended Kernel principle (P-4). |

**Solution**

FPF solves this with the **Role-Projection Pattern**, a mechanism that creates a robust, semantically rich **Concept-Bridge** between the universal kernel and domain-specific vocabularies. This pattern is built on three core components:

**1. The `Role` Concept**

*   **Description:** FPF introduces a new universal type, `U.Role`. A `Role` is not a concrete thing but an **abstract, context-dependent role** that an entity can play. It represents the domain-specific *interpretation* of a universal concept.
*   **Example:** "Thermodynamic System" is not modeled as a new subtype of `U.System`. Instead, it is modeled as a `Role` that a `U.System` can *play* when it is being analyzed from a thermodynamic perspective.

**2. The `refinesType` Relation**

*   **Description:** Every `Role` **MUST** declare which universal `U.Type` it refines or specializes. This is done via the `refinesType` relation.
*   **Example:** The `ThermodynamicSystemRole` would have the relation `refinesType: U.System`. This creates a formal, unbreakable link to the kernel. It guarantees that any entity playing this role still inherits all the fundamental properties and invariants of a `U.System`. This is a many-to-one relationship: many different roles (e.g., `EconomicSystemRole`, `BiologicalSystemRole`) can all refine the same `U.System` type.

**3. The `plays_role_of` Relation**

*   **Description:** This relation connects a **concrete entity** in a model to a `Role`. It is the assertion that "this specific thing is currently playing that specific role."
*   **Example:** In a model of a steam engine, we would assert that our specific engine instance `plays_role_of: ThermodynamicSystemRole`. This assertion signals to all tools and reviewers that this engine should be interpreted as a `U.System` and that the rules and constraints associated with the `ThermodynamicSystemRole` now apply to it.

> **Didactic Note for Managers: From "Alias" to "Job Description"**
>
> The Role-Projection pattern is the difference between giving someone an alias and giving them a job description.
>
> *   **An Alias (the old way):** Simply says "Bob is also known as The Manager." It's just a name swap.
> *   **A Role (the FPF way):** Says "Bob `plays_role_of` Manager." This is much richer. It implies that Bob has specific responsibilities, authorities, and performance expectations that come with the "Manager" role. He might also play other roles, like "Mentor" or "Team Lead."
>
> Similarly, when we say a component `plays_role_of` "Sensor," we are not just renaming it. We are activating a rich set of expectations and rules that come with being a sensor (e.g., it must have an output port, it must have a defined accuracy, etc.). This makes our models smarter, safer, and more precise.

**Archetypal Grounding**

To illustrate the pattern in action, let's consider how we would bridge the domain of **classical thermodynamics** to the FPF kernel.

1.  **Define the Roles:** A domain expert creates a set of `Role`s, each refining a core `U.Type`:
    *   A `U.Role` named `ThermodynamicSystemRole` with `refinesType: U.System`. It might have a description: "A region of the universe under study, separated by a boundary."
    *   A `U.Role` named `MacrostateRole` with `refinesType: U.State`. Its description could specify that it is defined by variables (P, V, T, N).
    *   A `U.Role` named `ControlVolumeRole` with `refinesType: U.Boundary`.
    *   A `U.Role` named `FreeEnergyObjectiveRole` with `refinesType: U.Objective`.

2.  **Apply the Roles in a Model:** An engineer modeling a heat engine would then use these roles:
    *   They create an instance of `U.System` representing the engine and assert: `HeatEngine_Instance plays_role_of: ThermodynamicSystemRole`.
    *   They model the engine's state and assert: `EngineState_Instance plays_role_of: MacrostateRole`.
    *   They define the system's goal and assert: `EngineObjective_Instance plays_role_of: FreeEnergyObjectiveRole`.

**What this achieves:**

*   The model is now **semantically rich**. Tools can now understand that `HeatEngine_Instance` is not just any system, but one that should be analyzed using the laws of thermodynamics.
*   The model is **verifiable**. A tool could now check if an entity playing the `MacrostateRole` actually has attributes for Pressure and Temperature, enforcing domain-specific consistency.
*   The model remains **universally compatible**. Because `ThermodynamicSystemRole` refines `U.System`, the heat engine can still be reasoned about as a generic system in a wider context (e.g., in a model of the entire power plant).

**Conformance Checklist**

*   **CC-B5.3.1 (Role Grounding Mandate):** Every `U.Role` **MUST** be linked to exactly one universal `U.Type` via the `refinesType` relation. Orphaned roles are forbidden.
*   **CC-B5.3.2 (Explicit Role Assertion):** A domain-specific concept **SHALL NOT** be treated as a subtype of a `U.Type` directly. Its relationship **MUST** be expressed using the `plays_role_of` relation to a `U.Role`.
*   **CC-B5.3.3 (Multi-Role Flexibility):** A single entity **MAY** `play_role_of` multiple `Role`s simultaneously, even from different domains.
*   **CC-B5.3.4 (Semantic Integrity):** A `Role` **MAY** introduce additional constraints or required attributes that are more specific than those of the `U.Type` it refines, but it **SHALL NOT** contradict them.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Subtype Explosion"** | The list of system "types" in the project grows endlessly: `ThermodynamicSystem`, `EconomicSystem`, `SoftwareSystem`, etc. The ontology becomes bloated and unmanageable. | **CC-B5.3.2** forbids this. There is only one `U.System`. Different perspectives on it are modeled as `Role`s, which keeps the core ontology lean. |
| **The "Magic Synonym"** | A developer simply renames `U.System` to "Thermodynamic System" in their diagrams, but there are no formal rules or constraints attached. The term is just an alias. | The FPF pattern requires a formal `Role` with a `refinesType` link. This is a rich, structural connection, not just a cosmetic name change. |
| **The "One-Hat Fallacy"** | The model forces an entity to be only one thing. An asset can be a "Physical Component" or a "Financial Asset," but not both, leading to duplicated models. | **CC-B5.3.3** explicitly allows an entity to play multiple roles. A single server in your data center can simultaneously `play_role_of` "PhysicalComponent" (for Sys-CAL) and "DepreciableAsset" (for a financial architheory). |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Semantic Richness and Precision:** The pattern allows domain-specific constraints and rules to be formally integrated into the model, enabling much more powerful automated checking and reasoning. | **Increased Modeling Granularity:** It introduces a layer of indirection (`Entity → Role → U.Type`) that modelers must learn. *Mitigation:* Tooling can automate much of this, suggesting relevant roles based on the context or domain. |
| **Multi-Domain Integration:** The pattern provides a clean and robust mechanism for a single model to incorporate concepts from multiple, diverse domains without conflict. | - |
| **Preserves a Lean Kernel:** The FPF kernel remains small and universal, with all domain-specific complexity handled in a modular, plug-in fashion via `Role` libraries. | - |
| **Enhanced Traceability and Clarity:** The roles an entity plays are explicit assertions. This makes the model's intent clear and auditable. | - |

**Rationale**

The Role-Projection pattern is the cornerstone of FPF's approach to **universality with specificity**. It is a direct implementation of the **Open-Ended Kernel (P-4)** and **Plug-in Layering (P-5)** principles. By separating the timeless, universal concepts (`U.Types`) from their context-dependent, domain-specific interpretations (`Role`s), FPF achieves a powerful balance.

This approach is inspired by contemporary practices in both ontology engineering (e.g., the use of role concepts in foundational ontologies like UFO) and software architecture (e.g., aspect-oriented programming and role-based modeling), but it integrates them into a single, coherent pattern. It provides a formal, scalable, and semantically rich solution to the perennial problem of bridging the universal and the particular.

**Relations**

*   **Implements:** `ADR-003: Role-Projection Pattern and Concept-Bridge`.
*   **Enables:** The practical application of all architheories by providing the "glue" that connects them to the FPF kernel.
*   **Used By:** All other patterns in the reasoning cycle, as it provides the vocabulary for framing hypotheses and interpreting evidence in a domain-specific context.

| **B.6** | Characterisation Families (CHR‑use)      | \[A] | Templates referencing CHR architheories.                                            |
| **B.7** | Common Logic Suite (LOG‑use)             | \[A] | Modal & trust‑propagation rules (imports LOG‑CAL).                        |
