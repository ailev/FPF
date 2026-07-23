# FPF Changelog

This changelog records user-observable FPF changes for returning readers,
agents, and dependent frameworks. The current specification remains
authoritative. See [CHANGELOG_CONTRACT.md](CHANGELOG_CONTRACT.md) for entry
semantics, evidence postures, and update rules.

## Unreleased

No entries yet.

## Public-source baseline - 2026-07-22

- **Basis kind:** `SourceSnapshot`
- **Range:** `d6af871b3e4e47c952d800a2a418c0634f180aaf` to
  `0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4`
- **Coverage:** `Partial`
- **Included scope:** the two public commits and affected `FPF-Spec.md` loci
  listed below
- **Excluded scope:** private DRRs, LATs, campaign carriers, landing audits,
  downstream uses, and earlier repository history
- **Boundary:** this baseline reconstructs bounded semantic and review effects
  from pinned public sources. It establishes no FPF edition relation,
  per-pattern Delta-Class, or compatibility result.

### Review your prior use

#### 2026-07-22-kind-reasoning-corrections - C.3.1 through C.3.A

- **Posture:** `SourceReconstruction`
- **Basis:** `6e7eeb93d7d6208877649ac999d52ab845640817` to
  `0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4`
- **Affected loci:** `C.3.1`, `C.3.2`, `C.3.3`, `C.3.4`, `C.3.5`, and `C.3.A`
- **Observation profile:** downstream kind declarations, candidate
  classifications, cross-context bridges, role masks, abstraction facets, and
  typed guards that use the C.3 cluster.
- **Operation:** `refined`
- **Per-pattern Delta-Class:** Not established from public sources
- **Semantic effect:** `ambiguity-resolving`,
  `admissibility-strengthened`
- **Before:** local kind and subkind reasoning was present, but kind,
  declaration episteme, candidate judgment, signature edition, and extension
  representation were not separated consistently across the cluster.
- **Now:** candidate classification is an exact four-input judgment over
  candidate, kind, signature edition, and context slice, with
  `true` / `false` / `unknown` outcomes. Extension representations do not
  create membership; cross-context bridges require target-side
  re-evaluation; role masks and `KindAT` facets are not kinds or guard inputs.
- **Preserved:** ordinary context-local kind/subkind reasoning remains
  available when its reference scheme is explicit; public `U.Kind` admission
  remains governed by `E.24.UK`.
- **Prior-use disposition:** Source reconstruction: `preserved` for
  context-local kind/subkind uses that already pin the reference scheme. Uses
  matching the detection list below require review.
- **Migration:** `ReviewRequired`
  - **Detect:** find C.3-dependent uses of `KindSignature`, `KindExtension`,
    membership booleans, `U.EntitySet`, `KindBridge`, `RoleMask`, `KindAT`, or
    C.3 guard macros. Flag implicit signature/context selection,
    `unknown` coerced to `false`, extension rows treated as ontology, source
    classification copied through a bridge, masks treated as kinds, or
    `KindAT` used as a guard input.
  - **Action:** separate kind, declaration episteme, candidate judgment, and
    extension representation. Pin candidate, kind, signature edition, and
    context slice; retain three-valued judgment; perform a new target-side
    judgment after a bridge; keep guard allow/refuse separate from
    classification truth.
  - **Verify:** every candidate-bearing use exposes all four judgment inputs
    and all three outcomes; missing evidence never becomes `false`; records
    and extension rows never create membership; bridge transport never copies
    source truth; `KindAT` is absent from guards; a work candidate is the exact
    work individual, not `U.Work`, a plan, or a log.
  - **Automation boundary:** text and schema search can find candidates;
    deciding the intended kind, signature edition, context slice, and bridge
    judgment requires semantic review.
- **Compatibility:** No compatibility claim; this entry identifies a bounded
  review scope.
- **Sources:** [before
  snapshot](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md),
  [after
  snapshot](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md),
  and [public commit
  `0990ff1`](https://github.com/ailev/FPF/commit/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4)
- **Unknowns:** official per-pattern Delta-Classes, an `E.4.PFR`
  compatibility relation, private rationale, and downstream uses outside the
  declared observation profile.

#### 2026-07-22-method-work-production - A.6.P.WMR and A.15.PROD

- **Posture:** `SourceReconstruction`
- **Basis:** `d6af871b3e4e47c952d800a2a418c0634f180aaf` to
  `6e7eeb93d7d6208877649ac999d52ab845640817`
- **Affected loci:** added `A.6.P.WMR` and `A.15.PROD`; the public commit also
  changes their method, work, transformation, publication, and wording
  neighbors.
- **Observation profile:** prose, prompts, schemas, agent rules, and dependent
  framework assertions that use generic method/work/production terms such as
  input, output, result, produced, completed, delivered, or accepted.
- **Operation:** `added`, `refined`
- **Per-pattern Delta-Class:** Not established from public sources
- **Semantic effect:** `ambiguity-resolving`,
  `admissibility-strengthened`, `admitted-use-added`
- **Before:** the parent snapshot had no dedicated `A.6.P.WMR` or
  `A.15.PROD` recovery route, so generic method/work/production relation
  language had to be resolved against neighboring patterns without these
  explicit checks.
- **Now:** `A.6.P.WMR` recovers exact relation claims at method/work
  boundaries. `A.15.PROD` treats production-work participation,
  entity-identity inception, and production completion as separate claims.
- **Preserved:** Work, Method, Transformation, production participation,
  identity inception, and completion remain distinct. The new patterns do not
  introduce universal Input, Output, Result, Work, or Production relations.
- **Prior-use disposition:** Source reconstruction: `transferred` for generic
  method/work/production boundary claims to the explicit `A.6.P.WMR` and
  `A.15.PROD` recovery routes; already direct, correctly governed relation
  claims remain usable.
- **Migration:** `ReviewRequired`
  - **Detect:** find generic Input, Output, Result, Work, or Production
    relations and claims where produced, completed, delivered, accepted,
    released, published, or available imply one another.
  - **Action:** recover the exact entity, related object, governor, and claim
    dimension; bind the claim to a direct relation, an exact `A.6.1` binding,
    or a local `A.15.PROD` / `A.6.RCD` claim. Split production participation,
    identity inception, and completion into separate assertions.
  - **Verify:** every reviewed claim reaches one explicit `A.6.P.WMR` exit;
    no universal relation was minted; factually unsupported, missing
    information, and missing governor remain distinct; completion, delivery,
    acceptance, release, publication, and availability do not imply one
    another without a governing relation.
  - **Automation boundary:** lexical search can identify candidate claims;
    selecting the entity, object, governor, and admissible relation requires
    semantic review.
- **Compatibility:** No compatibility claim; this entry identifies a bounded
  review scope.
- **Sources:** [before
  snapshot](https://github.com/ailev/FPF/blob/d6af871b3e4e47c952d800a2a418c0634f180aaf/FPF-Spec.md),
  [after
  snapshot](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md),
  and [public commit
  `6e7eeb9`](https://github.com/ailev/FPF/commit/6e7eeb93d7d6208877649ac999d52ab845640817)
- **Unknowns:** official per-pattern Delta-Classes, an `E.4.PFR`
  compatibility relation, private rationale, and downstream uses outside the
  declared observation profile.
