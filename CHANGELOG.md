# FPF Change History

This carrier keeps two authority lanes separate:

- **Accepted edition notes** project exact accepted owner results.
- **Provisional public-source comparisons** are bounded review aids over pinned
  public sources.

The current specification remains authoritative. See
[CHANGELOG_CONTRACT.md](CHANGELOG_CONTRACT.md) for the authority model,
claim postures, publication-unit contract, and update rules.

## Unreleased

No entries yet.

## Public-source baseline - 2026-07-22

- **Basis kind:** `SourceSnapshot`
- **Range:** `d6af871b3e4e47c952d800a2a418c0634f180aaf` to
  `0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4`
- **Coverage:** `Partial`
- **Included scope:** the eight pattern source comparisons below
- **Excluded scope:** private DRRs, LATs, campaign carriers, landing audits,
  accepted owner results, downstream uses, and earlier repository history
- **Publication boundary:** source comparison establishes no FPF edition
  relation, accepted semantic effect, per-pattern Delta-Class, `E.19`
  prior-use disposition, `E.4.PFR` compatibility, or exact-use migration
  necessity.

### Accepted edition notes

No owner-backed edition notes are published in this baseline. This means the
required accepted result references were unavailable to this public comparison;
it does not mean that no material semantic changes occurred.

### Provisional public-source comparisons

Every entry below is an `E.17.ID.CR` bounded comparative review unit. Its review
aid is advisory. `ReviewSuggested` is not a migration result, release gate, or
obligation.

#### C.3 local-kind reasoning

This heading groups six independent publication units for navigation. It
carries no aggregate semantic or migration claim.

##### PSC-2026-07-C3.1 - Local kind and subkind reasoning

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `C.3.1` pattern episteme at the later source
  snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme; `C.3.1` for
  its current claims
- **Carried move:** bounded comparison of the two `C.3.1` source publications
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `C.3.1`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L43828-L43952)
  and [later `C.3.1`
  publication](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md#L43831-L43980)
- **Compared alternatives:** the earlier and later `C.3.1` publications,
  retained as distinct source epistemes
- **Shared review frame:** how the two source publications separate local kind
  identity, `U.SubkindOf`, signature editions, judgments, and extension
  representations
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` The later source says `U.SubkindOf` obtaining is tested
    over aligned candidate/slice judgments under an exact reference-scheme
    edition.
  - `[SourceDirect]` The later source says a changed `KindSignature` edition
    prompts a separate kind-continuity decision and does not retroactively
    rewrite old judgments.
- **Candidate bounded lift:**
  - `[CandidateInference]` Downstream uses that infer a subkind relation or kind
    continuity from labels, declaration continuity, or extension rows may need
    inspection against the later source.
- **Weakest link:** the source pair shows changed published claims but does not
  establish the intended accepted delta or any actual prior downstream use.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find local subkind assertions derived from labels, diagrams, or
    extension rows without an exact reference-scheme and signature alignment.
  - **Inspect:** separate the kinds, declaration editions, obtaining relation,
    candidate judgments, and extension representation.
  - **Verify if changed:** the obtaining argument uses exact aligned inputs;
    `unknown` is not treated as a counterexample or proof; old judgments retain
    their actual declaration edition.
  - **Automation boundary:** search can find candidate labels and extension
    tables; it cannot decide kind continuity or relation obtaining.
- **Promotion requires:** an exact accepted semantic-delta result for `C.3.1`
  and, for any migration claim, one accepted result for the exact receiving use
- **Coverage and exclusions:** only the two linked `C.3.1` source slices;
  private rationale and downstream use evidence are excluded

##### PSC-2026-07-C3.2 - Kind intent, judgment, and extension

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `C.3.2` pattern episteme at the later source
  snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme; `C.3.2` for
  its current claims
- **Carried move:** bounded comparison of the two `C.3.2` source publications
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `C.3.2`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L43953-L44153)
  and [later `C.3.2`
  publication](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md#L43981-L44206)
- **Compared alternatives:** the earlier and later `C.3.2` publications,
  retained as distinct source epistemes
- **Shared review frame:** how kind declaration, one candidate judgment, and an
  optional extension representation are separated
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` The title changed from `KindSignature (+F) &
    Extension/MemberOf` to `Kind Intent, Membership Judgment, and Extension`.
  - `[SourceDirect]` The later source defines
    `J(candidate, kind, signatureEdition, slice)` with
    `true`, `false`, and `unknown` results and says extension rows do not create
    membership.
- **Candidate bounded lift:**
  - `[CandidateInference]` Uses that model classification as a Boolean,
    database membership row, or guard decision may need inspection against the
    later four-input, three-valued account.
- **Weakest link:** the source comparison does not establish which earlier
  readings were admitted or relied upon.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find `MemberOf`, membership booleans, implicit `current`
    signatures/slices, or `unknown` coerced to `false`.
  - **Inspect:** identify the exact candidate, local kind, signature edition,
    context slice, and separate guard disposition.
  - **Verify if changed:** all four judgment inputs and all three outcomes stay
    representable; evidence, records, and extension rows do not manufacture
    criterion satisfaction.
  - **Automation boundary:** schema and text search can locate candidate
    representations; semantic review selects the intended inputs and criterion.
- **Promotion requires:** an exact accepted semantic-delta result for `C.3.2`
  and one accepted receiving-use result for any migration claim
- **Coverage and exclusions:** only the two linked `C.3.2` source slices

##### PSC-2026-07-C3.3 - Cross-context kind bridging

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `C.3.3` pattern episteme at the later source
  snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme; `C.3.3` for
  its current claims
- **Carried move:** bounded comparison of the two `C.3.3` source publications
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `C.3.3`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L44154-L44389)
  and [later `C.3.3`
  publication](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md#L44207-L44417)
- **Compared alternatives:** the earlier and later `C.3.3` publications,
  retained as distinct source epistemes
- **Shared review frame:** whether a cross-context bridge carries a source
  classification result into the target context
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` The later source defines `KindBridge` between exact source
    and target local kinds under pinned reference-scheme editions.
  - `[SourceDirect]` It says target classification is a fresh four-input
    `C.3.2` judgment; neither a source result nor bridge assertion creates
    target truth.
- **Candidate bounded lift:**
  - `[CandidateInference]` Uses that copy source classification truth through a
    bridge may need target-side reevaluation.
- **Weakest link:** the source pair establishes the later boundary, not the
  validity or invalidity of any named downstream bridge use.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find cross-context classification reuse based on same spelling,
    mapping rows, or a source-side result.
  - **Inspect:** pin source/target kinds, signature and reference-scheme
    editions, bridge predicate, losses, and the target candidate/slice.
  - **Verify if changed:** a separate target-side judgment exists; bridge
    congruence affects receiving reliance without rewriting F or claim scope.
  - **Automation boundary:** tools can locate mappings; they cannot establish
    bridge obtaining or target truth.
- **Promotion requires:** an accepted semantic-delta result for `C.3.3` and an
  accepted result for each exact receiving bridge use
- **Coverage and exclusions:** only the two linked `C.3.3` source slices

##### PSC-2026-07-C3.4 - RoleMask declarations

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `C.3.4` pattern episteme at the later source
  snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme; `C.3.4` for
  its current claims
- **Carried move:** bounded comparison of the two `C.3.4` source publications
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `C.3.4`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L44390-L44613)
  and [later `C.3.4`
  publication](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md#L44418-L44612)
- **Compared alternatives:** the earlier and later `C.3.4` publications,
  retained as distinct source epistemes
- **Shared review frame:** whether a local mask is a kind, classification
  occurrence, or declaration episteme for one use
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` The later source defines `RoleMask` as a `C.2.1`
    declaration episteme over an exact base kind and signature edition.
  - `[SourceDirect]` It says applying the mask yields a separate
    `true`/`false`/`unknown` judgment and creates neither a kind nor a direct
    membership relation.
- **Candidate bounded lift:**
  - `[CandidateInference]` Uses that treat a mask as a cloned kind, scope, or
    classification fact may need inspection.
- **Weakest link:** no exact downstream mask use or accepted prior-use replay is
  present in the public source pair.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find `RoleMask` values used as type/kind identifiers, membership
    facts, scope definitions, or unqualified cross-context adapters.
  - **Inspect:** separate base kind, base signature edition, mask declaration,
    masked judgment, scope, and any bridge/adapter.
  - **Verify if changed:** the mask remains a declaration; application preserves
    three values and guard refusal remains separate from `unknown`.
  - **Automation boundary:** references can be inventoried mechanically;
    declaration meaning and bridge applicability require semantic review.
- **Promotion requires:** an accepted semantic-delta result for `C.3.4` and an
  accepted result for each exact receiving mask use
- **Coverage and exclusions:** only the two linked `C.3.4` source slices

##### PSC-2026-07-C3.5 - KindAT editorial facet

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `C.3.5` pattern episteme at the later source
  snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme; `C.3.5` for
  its current claims
- **Carried move:** bounded comparison of the two `C.3.5` source publications
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `C.3.5`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L44614-L44776)
  and [later `C.3.5`
  publication](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md#L44613-L44771)
- **Compared alternatives:** the earlier and later `C.3.5` publications,
  retained as distinct source epistemes
- **Shared review frame:** whether `KindAT` has classification, algebraic,
  assurance, or guard force
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` The later source calls `KindAT` an informative editorial
    facet and says it is not a Characteristic.
  - `[SourceDirect]` It says `KindAT` has no algebra or threshold, never appears
    in guards or composition, and changes neither kind nor classification.
- **Candidate bounded lift:**
  - `[CandidateInference]` Uses that score, compose, or gate on `KindAT` may
    need inspection as an editorial-planning use instead.
- **Weakest link:** source wording alone does not identify any actual receiving
  guard, score, or composition that relied on the earlier publication.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find `KindAT` in guard predicates, numeric scores, thresholds,
    composition rules, or classification results.
  - **Inspect:** recover the actual kind, signature, classification, F-G-R, or
    assurance owner needed by that use.
  - **Verify if changed:** `KindAT` remains only a catalog/planning tag and is
    absent from guards and composition.
  - **Automation boundary:** search can identify occurrences; it cannot select
    the correct replacement governor.
- **Promotion requires:** an accepted semantic-delta result for `C.3.5` and an
  accepted result for each exact receiving use
- **Coverage and exclusions:** only the two linked `C.3.5` source slices

##### PSC-2026-07-C3.A - Typed guard macros

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `C.3.A` pattern episteme at the later source
  snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme; `C.3.A` for
  its current claims
- **Carried move:** bounded comparison of the two `C.3.A` source publications
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `C.3.A`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L44777-L45504)
  and [later `C.3.A`
  publication](https://github.com/ailev/FPF/blob/0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4/FPF-Spec.md#L44772-L45232)
- **Compared alternatives:** the earlier and later `C.3.A` publications,
  retained as distinct source epistemes
- **Shared review frame:** how declaration compatibility, exact candidate
  classification, scope, bridges, masks, and guard disposition remain separate
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` The later source separates declaration-level checks from
    candidate-use checks and requires the exact four-input judgment only when a
    candidate-bearing use is current.
  - `[SourceDirect]` It preserves `true`, `false`, and `unknown` while
    allow/refuse is a separate guard disposition; `KindAT` never enters a guard.
- **Candidate bounded lift:**
  - `[CandidateInference]` Guards that collapse classification, scope, bridge,
    mask, and action disposition into one Boolean may need inspection.
- **Weakest link:** the public sources contain no inventory of actual guards or
  accepted results for their receiving uses.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find guards that invent wildcard candidates, coerce `unknown` to
    `false`, use `KindAT`, or treat a capability row, plan, or log as actual
    Work.
  - **Inspect:** separate declaration compatibility, candidate judgment, scope,
    bridge/mask conditions, and action disposition.
  - **Verify if changed:** fail-closed refusal retains the consumed
    classification value; actual Work uses an independently grounded dated Work
    individual.
  - **Automation boundary:** guard schemas can be linted structurally; intended
    candidate identity, Work occurrence, and bridge validity require review.
- **Promotion requires:** an accepted semantic-delta result for `C.3.A` and an
  accepted result for each exact guard use
- **Coverage and exclusions:** only the two linked `C.3.A` source slices

#### Method, work, and production language

This heading groups two independent publication units for navigation. It
carries no aggregate semantic or migration claim.

##### PSC-2026-07-A6P-WMR - Exact relation recovery

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `A.6.P.WMR` pattern episteme in the later
  source snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme;
  `A.6.P.WMR` for its current claims
- **Carried move:** bounded comparison of the parent `A.6.P` source before the
  addition and the added `A.6.P.WMR` publication
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `A.6.P` publication without an
  `A.6.P.WMR` child](https://github.com/ailev/FPF/blob/d6af871b3e4e47c952d800a2a418c0634f180aaf/FPF-Spec.md#L14704-L15533)
  and [added `A.6.P.WMR`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L15627-L16099)
- **Compared alternatives:** the earlier `A.6.P` family publication and the
  later family with the distinct `A.6.P.WMR` child
- **Shared review frame:** how generic input, output, result, deliverable, and
  handoff wording reaches one exact relation-bearing claim
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` `A.6.P.WMR` is absent as a child heading in the earlier
    `A.6.P` slice and present in the later source.
  - `[SourceDirect]` The added pattern requires the exact entity, related
    object, direct relation or non-assertability result, orthogonal claim
    dimensions, and direct governor.
  - `[SourceDirect]` It rejects a universal input, output, result, production,
    deliverable, or handoff relation family.
- **Candidate bounded lift:**
  - `[CandidateInference]` Boundary claims expressed only through generic role
    words may benefit from review through the new explicit recovery route.
- **Weakest link:** addition of the route does not establish that generic prior
  claims were valid, transferred, or actually used.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find generic input, output, result, outcome, deliverable, or
    handoff claims at method/work boundaries.
  - **Inspect:** recover the exact entity, related object, claim dimensions,
    direct relation and governor, or one exact non-assertability reason.
  - **Verify if changed:** every positive claim reaches a direct relation,
    exact operation binding, or admitted local claim; unsupported fact, missing
    information, and missing governor stay distinct.
  - **Automation boundary:** lexical search finds candidate wording; it cannot
    decide which relation obtains or manufacture a missing governor.
- **Promotion requires:** an accepted semantic-delta result for `A.6.P.WMR`
  and an accepted result for each exact receiving boundary claim
- **Coverage and exclusions:** pattern addition only; no accepted transfer or
  compatibility claim

##### PSC-2026-07-A15-PROD - Production claim branches

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** the `A.15.PROD` pattern episteme in the later
  source snapshot
- **EntityOfConcern governor:** `C.2.1` for the pattern episteme;
  `A.15.PROD` for its current claims
- **Carried move:** bounded comparison of the earlier `A.15` family and the
  added `A.15.PROD` publication
- **Outside boundary:** accepted semantics, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** [earlier `A.15` family without an
  `A.15.PROD` child](https://github.com/ailev/FPF/blob/d6af871b3e4e47c952d800a2a418c0634f180aaf/FPF-Spec.md#L23201-L25415)
  and [added `A.15.PROD`
  publication](https://github.com/ailev/FPF/blob/6e7eeb93d7d6208877649ac999d52ab845640817/FPF-Spec.md#L25922-L26308)
- **Compared alternatives:** the earlier `A.15` family publication and the
  later family with the distinct `A.15.PROD` child
- **Shared review frame:** how production-work participation, entity-identity
  inception, and production completion are kept as separate claims
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` `A.15.PROD` is absent as a child heading in the earlier
    `A.15` family and present in the later source.
  - `[SourceDirect]` The added pattern defines three separate branches with
    branch-specific primary EntitiesOfConcern.
  - `[SourceDirect]` It says inception and completion entail neither each other
    nor delivery, acceptance, release, publication, or availability.
- **Candidate bounded lift:**
  - `[CandidateInference]` Uses where `produced`, `completed`, `delivered`,
    `accepted`, `released`, `published`, or `available` imply one another may
    benefit from branch-specific review.
- **Weakest link:** the source pair identifies a new recovery route but contains
  no accepted result about any exact downstream production claim.
- **Blocked downstream claims:** semantic effect; per-pattern Delta-Class;
  `E.19` disposition; compatibility; migration necessity; semantic acceptance
- **Review aid:** `ReviewSuggested`
  - **Detect:** find one production sentence that carries work participation,
    first entity existence, completion, or later lifecycle status together.
  - **Inspect:** select exactly one current branch, its exact objects, criterion
    or boundary, direct governors, and missing facts.
  - **Verify if changed:** each branch has its own claim episteme and
    EntityOfConcern; evidence for one branch does not answer another; lifecycle
    statuses stay independent.
  - **Automation boundary:** text search can flag compressed verbs; it cannot
    establish work identity, inception, completion, or later status.
- **Promotion requires:** an accepted semantic-delta result for `A.15.PROD`
  and an accepted result for each exact receiving production claim
- **Coverage and exclusions:** pattern addition only; no accepted prior-use or
  compatibility claim
