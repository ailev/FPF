---
type: "fpf-knowledge-page"
context:
  - "FPF"
page_type: "fpf-knowledge-page"
mode: "canonical-generated"
title: "Boundary Statements"
part: "[[00_Hubs/FPF - Preface (non-normative)]]"
parents:
  - "[[00_Hubs/FPF - Preface (non-normative)]]"
source_file: "FPF-Spec.md"
source_lines:
  - 1054
  - 1072
status: "generated"
generated_on: "2026-08-02"
generated: true
---


Most of the time, teams can use fast compressed speech. "The service guarantees it." "The model is synced." "The dashboard proves it." "The interface is stable." "The process is compliant." In ordinary conversation, people often infer enough to continue.

That changes when the sentence crosses into an API, contract, safety case, evaluation protocol, dashboard used for commitment, SLO, SLA, compliance text, model card, dataset sheet, reproducibility checklist, or operational gate. At that point language is not merely communication. It can become system-relevant.

The danger is that one sentence may try to do several jobs at once:

- define a term or condition;
- say what a mechanism admits;
- assign a commitment or permission;
- claim evidence or work effect;
- publish a view or decision;
- move responsibility across a boundary.

If those jobs remain bundled, the sentence becomes hard to check. Later disagreement is then resolved by authority or politics rather than by the pattern that governs the claim.

FPF's boundary discipline, especially around the [[A_Kernel Architecture Cluster/06_Signature Stack & Boundary Discipline/00_A.06 - Signature Stack & Boundary Discipline|A.6]] family, repairs such cases by separating claim kinds. A contract line, interface statement, API schema, compliance note, or safety-case sentence can be unpacked into definition, admissibility, commitment, evidence, work effect, publication, and decision components as needed. The point is not to force every document into a heavy form. The point is to keep boundary language from changing system behavior without an inspectable claim.
