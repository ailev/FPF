---
name: fpf-navigation
description: Specialized workflow for navigating the massive FPF-Spec.md document without exceeding context limits. Use when answering questions or making edits to the Foundation Pattern Framework (FPF) specification document.
---
# FPF Specification Navigation Skill

<instructions>
You are interacting with the Foundation Pattern Framework (FPF) specification document. This file is extremely large (~1.5M tokens). **NEVER attempt to read the entire file without limits.**

The canonical location for this file is assumed to be:
`~/Documents/fpf-docs/FPF-Spec.md`

Follow this strict two-phase workflow to navigate the document:

### Phase 1: Load Context & Table of Contents
When starting a new investigation into FPF, always load the introduction and Table of Contents (TOC) first to ground yourself in the available patterns.
The TOC and intro exist entirely before "Part A - Kernel Architecture Cluster".

1. Find the line number where Part A begins:
   `grep -n "^# Part A" ~/Documents/fpf-docs/FPF-Spec.md`
2. Use the `read_file` tool with `start_line=1` and `end_line={LINE_NUMBER_MINUS_ONE}` to ingest the preamble and TOC. (Note: tools like `read_file` or `replace` require absolute paths, so expand `~` to your home directory when using them).
3. Analyze the TOC to identify the exact Pattern IDs (e.g., `E.10.D2`, `A.6.B`) relevant to the user's query.

### Phase 2: Surgical Section Extraction
Once you know the exact Pattern ID you need to investigate, use the following robust AWK script via `run_shell_command`. 

This script dynamically detects the heading level (e.g., `##` vs `###`) of your target pattern and extracts the entire section, including all child sub-sections, stopping only when it reaches the next sibling or parent heading.

*Copy and paste this exact command, replacing `TARGET_ID` with your pattern (e.g., `E.10.D2`):*
```bash
awk -v tgt="TARGET_ID" '
BEGIN { flag=0; lvl=0 }
/^#+ / {
    match($0, /^#+/)
    cur_lvl = RLENGTH
    if (!flag && index($0, tgt)) {
        flag = 1
        lvl = cur_lvl
        print
        next
    }
    if (flag && cur_lvl <= lvl) {
        exit
    }
}
flag { print }
' ~/Documents/fpf-docs/FPF-Spec.md
```

### Phase 3: Recursive Dependency Loading (MANDATORY)
FPF patterns operate in a strict dependency graph. You cannot safely apply a pattern without understanding the foundational rules it relies upon.

1. Once you extract your target pattern using Phase 2, look at its **"Builds on:"** list (usually located at the top of the pattern description or in the TOC).
2. You **MUST** repeat Phase 2 to extract and read all primary dependencies listed in "Builds on:".
3. Evaluate constraints from the bottom up. (e.g., If `E.10.D2` builds on `A.7`, any solution you propose must explicitly comply with `A.7`'s Strict Distinction rules first).

### Constraints
- Never make blind edits. If asked to modify a pattern, you must load the complete section into context using Phase 2 before using the `replace` tool.
- If a section contains sub-sections (e.g., `### E.10.D2:1`), extracting the top-level heading (`## `) using the methods above will safely include all sub-sections.
</instructions>