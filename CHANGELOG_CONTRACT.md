# FPF Changelog Contract

This file defines the repository-level contract for `CHANGELOG.md`. It governs
the change-history publication carrier only. It does not amend FPF Core, decide
that two FPF objects are editions of one another, establish compatibility, or
replace a DRR, LAT, landing review, or governing pattern.

`FPF-Spec.md` remains authoritative for current FPF semantics. A changelog
entry helps a returning reader find an accepted change or a bounded
public-source reconstruction and decide what to inspect next.

## 1. Scope

Record a change when it affects at least one of these:

- the interpretation, kind, scope, relation, normative force, or admitted use
  of an FPF pattern;
- a stable PatternID, public name, alias, split, merge, deprecation,
  supersession, or removal;
- a prior-edition use that readers, agents, or dependent frameworks may need to
  review;
- an FPF publication or access carrier in a way that changes discovery,
  source return, or bounded use.

Do not use the changelog as:

- a copy of commit subjects, campaign status, DRR rationale, or LAT evidence;
- a second specification beside `FPF-Spec.md`;
- proof that downstream users migrated;
- a release, compatibility, permission, or acceptance decision.

## 2. Basis and coverage

Each published section names its basis:

- `Edition` only when an accepted FPF edition and its `FPFFormMap` can be
  referenced;
- `SourceSnapshot` for an immutable commit or content digest that has no
  accepted edition relation available to the changelog.

A commit range is not called an FPF edition by convenience.

Each section also declares coverage:

- `Complete` for a bounded comparison scope whose candidates have all received
  a disposition;
- `Partial` with the excluded or unexamined scope;
- `Unknown` with the missing basis.

Coverage applies only to the stated comparison scope. It does not mean that
every consequence in every dependent framework has been found.

## 3. Epistemic posture

Every entry carries one local publication posture. These labels are not new FPF
kinds.

| Posture | Admissible changelog use |
| --- | --- |
| `AcceptedInGoverningResult` | Project semantic, prior-use, and migration values from an exact accepted result and cite it. |
| `SourceReconstruction` | Reconstruct a bounded semantic effect and review migration from exact pinned before/after sources. Declare the observation profile, receiving use, evidence, and remaining scope. |
| `SourceDirect` | Report only facts directly inspectable in pinned public sources when a useful bounded reconstruction cannot yet be made. |
| `CandidateInference` | Keep a reviewable draft under `Unreleased`. Do not present it as settled history. |

A citation does not promote `CandidateInference` to `SourceReconstruction` or
`AcceptedInGoverningResult`. A merged `SourceReconstruction` accepts that
bounded changelog reading as publication content; it does not create an FPF
Core claim, compatibility relation, or per-pattern Delta-Class.

## 4. Reader-facing order

Within a section, render entries in this order:

1. `Action required`
2. `Review your prior use`
3. `No migration action`
4. `Editorial and carrier changes`
5. `Unresolved impact`

The first four headings require the corresponding accepted migration or
carrier-only result, except that `Review your prior use` may contain a
`SourceReconstruction` with a bounded `ReviewRequired` migration. Put raw
`SourceDirect` facts and reconstructions without an exact receiving use under
`Unresolved impact`.

## 5. Semantic entry

Use this form for a material FPF change:

```markdown
#### <DeltaID> - <short title>

- **Posture:** <AcceptedInGoverningResult | SourceReconstruction | SourceDirect | CandidateInference>
- **Basis:** <exact from/to edition or source-snapshot refs>
- **Affected loci:** <PatternIDs, relation refs, and stable source anchors>
- **Observation profile:** <the exact readings or receiving uses in scope>
- **Operation:** <one or more bounded operation labels>
- **Per-pattern Delta-Class:** <owner-result refs and projected values, or Not established>
- **Semantic effect:** <bounded accepted or source-reconstructed effect, or Unknown>
- **Before:** <accepted earlier claim or bounded source-direct observation>
- **Now:** <accepted current claim or bounded source-direct observation>
- **Preserved:** <accepted or source-reconstructed invariant, or Not established>
- **Prior-use disposition:** <accepted or explicitly source-reconstructed value, or Not established>
- **Migration:** <disposition plus Detect, Action, Verify, and Automation boundary, or Unknown>
- **Compatibility:** <exact E.4.PFR relation record ref, or No compatibility claim>
- **Sources:** <governing result refs and immutable public source refs>
- **Unknowns:** <unexamined scope and the result needed to close it>
```

Do not omit a required field because its value is unavailable. Use
`Not established` or `Unknown` and state the missing owner or source.

For a carrier-only change, use the short route:

```markdown
#### <DeltaID> - <short title>

- **Posture:** <posture>
- **Basis:** <exact source refs>
- **Affected carriers:** <paths or access surfaces>
- **Operation:** <operation>
- **FPF Core impact:** None
- **Reader impact:** <discovery or access change>
- **Sources:** <immutable source refs>
```

## 6. Orthogonal change descriptions

An entry keeps these questions separate.

### Per-pattern Delta-Class

Project the existing `E.15` value for each affected PatternID. Do not create
one aggregate Delta-Class for a multi-pattern change.

### Operation

Operation labels describe the edit shape. Common labels include:

`added`, `label-renamed`, `identifier-rekeyed`, `split`, `merged`,
`responsibility-moved`, `refined`, `generalised`, `constrained`, `replaced`,
`deprecated`, `removed`, and `publication-only`.

Several operations may apply. An operation does not establish semantic effect
or compatibility.

### Semantic effect

Project a bounded effect from an accepted result or an exact
`SourceReconstruction`:

`interpretation-preserving`, `ambiguity-resolving`,
`admissibility-strengthened`, `admissibility-weakened`,
`admitted-use-added`, `admitted-use-removed`, `mixed`, or `unknown`.

`interpretation-preserving` is always relative to a declared observation
profile. It never means universal equivalence of natural-language editions.

A `SourceReconstruction` must bind the effect to:

- immutable before and after sources;
- exact affected loci;
- a declared observation profile;
- source-supported `Before`, `Now`, and `Preserved` claims;
- the weakest link and unexamined scope.

It may not generalise from the named profile to all downstream FPF uses.

### Prior-use disposition

Use the `E.19` vocabulary:

`preserved`, `improved`, `transferred`, `intentionally retired`, or
`regressed`.

An `AcceptedInGoverningResult` entry projects the exact governing value. A
`SourceReconstruction` may use one of these values only for a named prior use
whose old and new handling are both inspectable; prefix the claim with
`Source reconstruction`. Missing basis and unexamined scope are not a sixth
disposition.

### Compatibility

Compatibility is directional and use-bounded. Cite the exact `E.4.PFR`
compatibility relation record. Do not replace it with a changelog-local
`breaking: true` flag or infer it from a version number.

### Migration

Name one exact receiving use. Record whether it requires no action, review, or
an action, and include:

- how to detect the affected old use;
- what to change or inspect;
- how to verify the result;
- what automation can and cannot decide.

Use `Unknown` when no exact receiving use can be named. A
`SourceReconstruction` may publish `ReviewRequired` with the four fields above;
it may not publish `ActionRequired` or `NoAction` without an accepted owner.

## 7. Update rule

1. A contributor may draft a `CandidateInference` beside an intended material
   change.
2. A contributor or deterministic tool compares sources and emits structural
   candidates by PatternID, section, relation, and stable reference. That
   comparison does not decide meaning.
3. The contributor reconciles intended and observed changes. For a
   `SourceReconstruction`, the contributor names the observation profile and
   writes a falsifiable `Before` / `Now` / `Preserved` account plus
   `Detect` / `Action` / `Verify` migration guidance.
4. Every in-scope structural candidate receives a semantic, carrier-only,
   reverted, or unresolved disposition.
5. A reviewer checks exact old and new sources, affected loci, reconstruction
   bounds, owner-result references when present, and unexamined scope.
6. A semantic entry becomes `AcceptedInGoverningResult` only through the exact
   accepted FPF result that owns its claims. Otherwise it remains visibly
   `SourceReconstruction` after publication.
7. The publisher binds immutable source refs and renders the human changelog
   from the same reviewed content.

Git hooks and AI agents may inventory, draft, reconcile, validate, and render.
They may not accept semantic claims, establish compatibility, or perform the
terminal publication decision.

## 8. Corrections

Do not silently rewrite a published semantic claim. Add a dated correction or
supersession entry that names:

- the earlier DeltaID;
- the corrected claim;
- the governing correction result;
- the new effective source basis.

The effective-current view may hide superseded text from the short path, but
the append-only relation remains recoverable.

## 9. Versioning

Until FPF adopts a whole-framework compatibility contract, use a calendar label
plus immutable source and content digests for whole-FPF changelog sections.
Keep the existing `E.15` per-pattern version and Delta-Class rules.

A future whole-FPF SemVer policy requires a separate decision that defines the
compatibility boundary behind major, minor, and patch.

## 10. Review checklist

A changelog change is ready for publication when:

- the basis is immutable and labelled as `Edition` or `SourceSnapshot`;
- each material claim has the correct posture and owner;
- each `SourceReconstruction` declares a bounded observation profile and
  weakest link;
- every affected PatternID has its own Delta-Class projection or
  `Not established`;
- operation, semantic effect, prior-use, compatibility, and migration are not
  collapsed into one label;
- every named receiving use has one migration disposition with detection,
  action, verification, and automation boundary, or `Unknown`;
- public source anchors resolve;
- coverage and unexamined scope are explicit;
- generated prose adds no FPF requirement absent from its sources.
