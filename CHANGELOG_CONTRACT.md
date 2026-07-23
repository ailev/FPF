# FPF Changelog Contract

This file defines the repository-level contract for `CHANGELOG.md`. It governs
a change-history publication carrier. It does not amend FPF Core, establish
that two FPF objects are editions of one another, establish compatibility, or
replace a DRR, LAT, landing result, prior-use replay, or governing pattern.

`FPF-Spec.md` remains authoritative for current FPF semantics. The changelog
helps a returning reader find either an accepted edition note or a bounded
public-source comparison and know which use is admissible.

## 1. Scope and object boundary

Record a candidate change when it affects at least one of these:

- the interpretation, kind, scope, relation, normative force, or admitted use
  of an FPF pattern;
- a stable PatternID, public name, alias, split, merge, deprecation,
  supersession, or removal;
- a prior-edition use that readers, agents, or dependent frameworks may need to
  inspect;
- an FPF publication or access carrier in a way that changes discovery,
  source return, or bounded use.

Keep these objects distinct:

- the FPF edition or pattern episteme under concern;
- a semantic-delta or receiving-use result episteme;
- a provisional comparative review unit;
- a publication occurrence;
- `CHANGELOG.md` as a publication carrier.

Do not use the changelog as:

- a copy of commit subjects, campaign status, DRR rationale, or LAT evidence;
- a second specification beside `FPF-Spec.md`;
- proof that downstream users migrated;
- a compatibility, permission, gate, work, or semantic-acceptance decision.

## 2. Authority model

The changelog has two disjoint publication lanes. Lane names are local
publication-contract values, not new FPF kinds.

| Lane | Governing use | Admissible claims | Explicitly blocked |
| --- | --- | --- | --- |
| `AcceptedEditionNote` | User-facing semantic and exact-use migration history | values projected from exact accepted owner results | inferred semantics, inferred compatibility, inferred migration |
| `ProvisionalSourceComparison` | `E.17.ID.CR` bounded comparison over pinned public sources | source-direct observations and candidate bounded lifts | official semantic effect, Delta-Class, prior-use disposition, compatibility, migration necessity, semantic acceptance |

The lanes are rendered under separate top-level headings. A provisional unit
never appears under an accepted migration heading.

Publication does not change a claim's posture. Promotion creates a new accepted
unit and a relation to the provisional unit; it never edits a published
candidate claim into acceptance.

## 3. Direct owners

The changelog projects or references values owned elsewhere:

| Value | Direct owner |
| --- | --- |
| Current FPF semantics | current governing FPF pattern episteme |
| Per-pattern Delta-Class | governing `E.15` change or decision result |
| Prior-use disposition | exact governing prior-use replay/result under `E.8` and `E.19` |
| Edition and compatibility relations | `C.2.1` and `E.4.PFR` owner records |
| Exact receiving-use migration | accepted receiving-use result |
| Bounded source contrast | `E.17.ID.CR` comparative review unit |
| Publication | accountable role-assignment performing a context-recognized `A.2.9` publication SpeechAct |

A Product Steward publication act selects exact publication-unit and projection
digests. It does not replace the result that owns each semantic value.

Git commits, PR review, and merge are carriers or evidence of work. They create
no semantic, edition, compatibility, migration, or deontic authority by
themselves. An explicit PR utterance may evidence the publication act only when
an accepted repository context policy says so and names the lane and units.

## 4. Basis and coverage

Each published section names its basis:

- `Edition` only when an accepted FPF edition and its `FPFFormMap` can be
  referenced;
- `SourceSnapshot` for an immutable commit or content digest when no accepted
  edition relation is available to the changelog.

A commit range is not called an FPF edition by convenience.

Each section also declares coverage:

- `Complete` for a bounded comparison scope whose structural candidates all
  received a disposition;
- `Partial` with excluded or unexamined scope;
- `Unknown` with the missing basis.

Coverage applies only to the stated comparison scope. It does not mean that
every consequence in every dependent framework has been found.

## 5. Claim posture

Posture belongs to each claim, not to an entry as a whole:

| Posture | Admissible use |
| --- | --- |
| `SourceDirect` | report a fact directly inspectable at an exact pinned source anchor |
| `CandidateInference` | state one bounded, falsifiable interpretive lift with its weakest link and blocked downstream claims |
| `AcceptedInGoverningResult` | project one claim from an exact accepted owner result and cite the claim ref |

A citation does not promote one posture to another. A reviewed or merged
`CandidateInference` remains a candidate.

## 6. Publication-unit invariant

Every entry is one bounded publication unit and keeps visible:

1. one primary EntityOfConcern or non-claim-bearing subject named by value;
2. one carried publication move;
3. one outside-work and blocked-overread boundary;
4. exact immutable source anchors;
5. one publication lane;
6. claim-level postures.

If one entry would carry independently governed claims about several primary
EntitiesOfConcern, split it. A campaign, commit, topic phrase, or list of
PatternIDs is not one EntityOfConcern by aggregation. Presentation may group
several child entries under a non-claim-bearing index heading.

## 7. Accepted edition-note entry

Use this form only when exact accepted owner results exist:

```markdown
#### <DeltaID> - <short title>

- **Publication lane:** `AcceptedEditionNote`
- **Primary EntityOfConcern:** <exact ref>
- **EntityOfConcern governor:** <direct pattern/relation ref>
- **Carried move:** <one semantic-delta or exact-use migration projection>
- **Outside boundary:** <work, gate, reliance, or other claim not carried>
- **Basis:** <exact edition or source-snapshot refs>
- **Affected loci:** <PatternIDs, relation refs, and stable source anchors>
- **Operation:** <one or more bounded operation labels>
- **Per-pattern Delta-Class:** <one PatternID -> owner-result ref -> value per row>
- **Semantic claims:**
  - `[AcceptedInGoverningResult]` <claim> - <exact owner claim ref>
- **Before / now / preserved / no-longer-admissible:** <owner-backed claims>
- **Prior-use disposition:** <exact use probe -> owner result -> E.19 value>
- **Migration:** <one exact receiving use and accepted disposition>
- **Compatibility:** <exact E.4.PFR relation ref, or `Not established by owner`>
- **Sources:** <owner-result refs and immutable public source anchors>
- **Coverage and blockers:** <bounded scope>
```

An accepted semantic-delta unit and an accepted receiving-use unit are separate
when their primary EntitiesOfConcern differ.

### Accepted migration dispositions

For one exact receiving use, project exactly one owner-backed value:

- `NoChangeNeededForContinuedUse`
- `ReviewNeededForContinuedUse`
- `ActionNeededForContinuedUse`
- `UseNoLongerAdmitted`
- `UnknownWithBlocker`

The value states what is technically necessary if the reader chooses to
continue that exact use. It does not command the reader to continue and does
not create an `A.2.8` obligation or recommendation-as-duty.

When the disposition carries action, review, or a blocker, include:

- `Detect`: how to find the affected exact use;
- `Action` or `Inspect`: what to change or examine;
- `Verify`: how to check the resulting use;
- `Automation boundary`: what tooling can and cannot decide.

## 8. Provisional source-comparison entry

Use this form when only pinned source publications are available:

```markdown
#### <ComparisonID> - <short title>

- **Publication lane:** `ProvisionalSourceComparison`
- **Primary EntityOfConcern:** <one exact pattern episteme or governed relation>
- **EntityOfConcern governor:** <direct pattern/relation ref>
- **Carried move:** bounded comparison over pinned source publications
- **Outside boundary:** semantic acceptance, Delta-Class, prior-use,
  compatibility, migration necessity, work, gate, and reliance remain outside
- **Reviewed sources:** <exact before and after anchors>
- **Compared alternatives:** <the source publications kept distinct>
- **Shared review frame:** <one bounded contrastive question>
- **World-contact policy:** `review-only; non-executive`
- **Direct observations:**
  - `[SourceDirect]` <inspectable fact> - <exact anchor>
- **Candidate bounded lift:**
  - `[CandidateInference]` <falsifiable interpretation>
- **Weakest link:** <what the source pair cannot establish>
- **Blocked downstream claims:** <explicit list>
- **Review aid:** `ReviewSuggested`
  - **Detect:** <how to find candidate affected uses>
  - **Inspect:** <what distinction to inspect>
  - **Verify if changed:** <how to check a voluntary repair>
  - **Automation boundary:** <what tooling cannot decide>
- **Promotion requires:** <exact owner result or decision needed>
- **Coverage and exclusions:** <bounded scope>
```

`ReviewSuggested` is advisory. It is not `ReviewRequired`, a migration
disposition, a release gate, or a deontic commitment.

A provisional entry must not contain:

- an official semantic-effect enum value;
- a per-pattern Delta-Class;
- `preserved`, `improved`, `transferred`, `intentionally retired`, or
  `regressed` as an `E.19` disposition;
- an `E.4.PFR` compatibility conclusion;
- `NoChangeNeededForContinuedUse`,
  `ReviewNeededForContinuedUse`, or
  `ActionNeededForContinuedUse`;
- wording that says the Product Steward accepted the candidate interpretation.

## 9. Orthogonal accepted values

Keep these questions separate in the accepted lane.

### Per-pattern Delta-Class

Project the existing `E.15` value for each affected PatternID. Do not create one
aggregate Delta-Class for a multi-pattern change.

### Operation

Operation labels describe edit shape:

`introduce`, `rename-label`, `rekey-identifier`, `split`, `merge`,
`move-responsibility`, `refine`, `generalise`, `constrain`, `strengthen`,
`weaken`, `replace`, `add-relation`, `remove-relation`, `retype-relation`,
`reorient-relation`, `deprecate`, `supersede`, `remove`, and
`publication-only`.

Several operations may apply. An operation establishes neither semantic effect
nor compatibility.

### Semantic effect

An accepted owner result may project:

`InterpretationPreserving`, `AmbiguityResolving`,
`AdmissibilityStrengthened`, `AdmissibilityWeakened`, `AdmittedUseAdded`,
`AdmittedUseRemoved`, `MixedOrIncomparable`, or `Unknown`.

`InterpretationPreserving` is relative to its declared observation profile. It
never means universal equivalence of natural-language editions.

### Prior-use disposition

Project the exact `E.19` value for one exact prior-edition use probe:

`preserved`, `improved`, `transferred`, `intentionally retired`, or
`regressed`.

`transferred` requires the named neighboring pattern whose Solution carries the
needed action and result. Missing basis, unsupported historical residue, and
unexamined scope receive no disposition.

### Compatibility

Compatibility is directional and use-bounded. Cite the exact `E.4.PFR`
relation record. Do not replace it with `breaking: true` or infer it from a
version number.

## 10. Reader-facing order

Render the human carrier in this order:

1. `Accepted edition notes`
   1. `Action needed for continued use`
   2. `Review needed for continued use`
   3. `No change needed for continued use`
   4. `Editorial and carrier changes`
   5. `Unknown with blocker`
2. `Provisional public-source comparisons`
   1. `Review suggested`
   2. `Source-direct observations`
   3. `Unresolved candidate impact`

An empty lane stays visible when its absence matters to interpretation.

## 11. Update, publication, and promotion

1. A contributor or agent inventories exact structural candidates from pinned
   sources. Structural detection decides no meaning.
2. The author selects one primary EntityOfConcern and one lane per publication
   unit.
3. The provisional route produces only bounded `E.17.ID.CR` comparison claims.
   The accepted route projects only exact owner results.
4. Every in-scope structural candidate receives a semantic, carrier-only,
   reverted, provisional, or unresolved structural disposition.
5. An independent reviewer checks source fidelity, lane integrity, claim
   posture, EntityOfConcern, carried move, outside boundary, and coverage.
6. A deterministic renderer may generate human and machine views from the same
   lane-discriminated records. It adds no claims.
7. The Product Steward performs an explicit publication act that selects the
   lane, publication-unit refs, source-record digest, and projection digests.
8. Later semantic acceptance creates a new accepted unit linked to the
   provisional unit. It does not mutate the provisional unit.

Hooks and AI agents may inventory, draft, reconcile, validate, and render. They
may not accept semantic claims, establish compatibility, or perform the
terminal publication act.

### Bootstrap carrier status

Until FPF accepts and installs a structured ledger, validator, and renderer,
`CHANGELOG.md` is a hand-authored public prototype. It is the sole public
carrier for its listed provisional units, not evidence that the proposed
production process or machine source already exists. Do not create a manually
maintained parallel YAML truth.

## 12. Corrections

Do not silently rewrite a published claim. Add a dated correction or
supersession unit that names:

- the earlier publication-unit ID;
- the corrected claim;
- the governing correction result when the corrected claim is accepted;
- the new effective source basis;
- the relation to the prior unit.

The effective-current view may hide superseded text from the short path, but
the append-only relation remains recoverable.

## 13. Versioning

Until FPF adopts a whole-framework compatibility contract, use a calendar label
plus immutable source and content digests for whole-FPF changelog sections.
Keep the existing `E.15` per-pattern version and Delta-Class rules.

A future whole-FPF SemVer policy requires a separate decision defining the
compatibility boundary behind major, minor, and patch.

## 14. Review checklist

A changelog change is ready for its proposed publication lane when:

- the basis is immutable and labelled `Edition` or `SourceSnapshot`;
- lane and claim-level postures are explicit;
- each publication unit has one primary EntityOfConcern, one carried move, and
  one outside-work boundary;
- public source anchors resolve;
- coverage and excluded scope are explicit;
- provisional and accepted units are rendered separately;
- every provisional bounded lift states its weakest link, blocked downstream
  claims, and promotion requirement;
- no provisional unit carries an accepted-only value;
- every accepted semantic value has its exact owner-result and claim ref;
- every accepted migration unit names one exact receiving use;
- every accepted affected PatternID has its own owner-backed Delta-Class
  projection;
- generated prose adds no FPF requirement absent from its source;
- promotion and correction preserve append-only history.
