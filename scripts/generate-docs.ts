/**
 * FPF Documentation Generator
 *
 * Parses FPF-Spec.md and generates a browsable folder structure
 * following the specification's logical organization.
 *
 * Usage: bun run scripts/generate-docs.ts
 */

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "fs";
import { join } from "path";

const SPEC_FILE = "FPF-Spec.md";
const OUTPUT_DIR = "docs";

interface PartConfig {
  id: string;
  title: string;
  description: string;
  linePattern: RegExp;
  subsections?: {
    name: string;
    file: string;
    patterns: string[]; // Patterns to match section starts
  }[];
}

// Configuration matching the README structure
const PARTS_CONFIG: PartConfig[] = [
  {
    id: "A",
    title: "Kernel Architecture Cluster",
    description: "The immutable ontological core.",
    linePattern: /^#\s*\*?\*?Part\s+A\s*[–—-]/i,
    subsections: [
      {
        name: "Ontology",
        file: "01-Ontology.md",
        patterns: ["A.0", "A.1", "A.2 Role", "U.Holon", "U.System", "U.Episteme", "BoundedContext"]
      },
      {
        name: "Transformation",
        file: "02-Transformation.md",
        patterns: ["A.3", "Transformer", "U.Method", "U.Work", "A.15"]
      },
      {
        name: "State Space",
        file: "03-State-Space.md",
        patterns: ["A.17", "A.18", "A.19", "A.20", "Characteristic", "Scale", "Dynamics", "U.Dynamics"]
      },
      {
        name: "Core Principles",
        file: "04-Core-Principles.md",
        patterns: ["A.4", "A.5", "A.6", "A.7", "A.8", "A.9", "A.13", "A.14"]
      }
    ]
  },
  {
    id: "B",
    title: "Trans-disciplinary Reasoning Cluster",
    description: "The logic of composition and trust.",
    linePattern: /^#\s*\*?\*?Part\s+B\s*[–—-]/i,
    subsections: [
      {
        name: "Γ Algebra",
        file: "01-Gamma-Algebra.md",
        patterns: ["B.1", "B.1.", "Γ_sys", "Γ_epist", "Γ_work", "aggregat"]
      },
      {
        name: "Assurance",
        file: "02-Assurance.md",
        patterns: ["B.3", "F-G-R", "Trust", "evidence"]
      },
      {
        name: "Evolution",
        file: "03-Evolution.md",
        patterns: ["B.2", "B.4", "B.5", "evolution", "transition"]
      }
    ]
  },
  {
    id: "C",
    title: "Architheory Specifications",
    description: "Pluggable domain-specific calculi (CAL), logics (LOG), and characterizations (CHR).",
    linePattern: /^#\s*\*?\*?Part\s+C\s*[–—-]/i,
    subsections: [
      {
        name: "KD-CAL (Knowledge Dynamics)",
        file: "01-KD-CAL.md",
        patterns: ["C.2", "KD-CAL", "KD‑CAL", "Episteme", "U.Episteme"]
      },
      {
        name: "Kind-CAL (Typed Reasoning)",
        file: "02-Kind-CAL.md",
        patterns: ["C.3", "Kind-CAL", "Kind‑CAL", "U.Kind", "KindBridge", "RoleMask"]
      },
      {
        name: "Compose-CAL & Measurement",
        file: "03-Compose-Measurement.md",
        patterns: ["C.13", "C.16", "Compose", "MM-CHR", "Measurement"]
      },
      {
        name: "Creativity & NQD-CAL",
        file: "04-Creativity-NQD.md",
        patterns: ["C.17", "C.18", "C.19", "NQD", "Creativity", "Novelty"]
      },
      {
        name: "Discipline & Problem CHR",
        file: "05-Discipline-Problem.md",
        patterns: ["C.20", "C.21", "C.22", "C.23", "C.24", "C.25", "Discipline", "Problem", "Q-Bundle"]
      }
    ]
  },
  {
    id: "D",
    title: "Multi-scale Ethics & Conflict-Optimisation",
    description: "Multi-scale ethics (from agent to planetary). Bias audits and trust-aware mediation.",
    linePattern: /^#\s*\*?\*?Part\s+D\s*[–—-]/i
  },
  {
    id: "E",
    title: "FPF Constitution and Authoring Cluster",
    description: "The governance of the framework itself.",
    linePattern: /^#\s*\*?\*?Part\s+E\s*[–—·-]/i,
    subsections: [
      {
        name: "The 11 Pillars",
        file: "01-Eleven-Pillars.md",
        patterns: ["E.2", "E.3", "Pillar", "Principle"]
      },
      {
        name: "Lexical Rules & Guard-Rails",
        file: "02-Lexical-Rules.md",
        patterns: ["E.10", "E.11", "LEX", "Lexical", "Guard"]
      },
      {
        name: "Human-Centric Model",
        file: "03-Human-Centric.md",
        patterns: ["E.14", "E.15", "E.16", "Human", "Authoring"]
      },
      {
        name: "Multi-View Publication Kit",
        file: "04-MultiView-Publication.md",
        patterns: ["E.17", "E.18", "MultiView", "MVPK", "View", "TGA"]
      }
    ]
  },
  {
    id: "F",
    title: "The Unification Suite",
    description: "Techniques for aligning vocabularies across disciplines using SenseCells, Concept-Sets, and Alignment Bridges.",
    linePattern: /^#\s*\*?\*?Part\s+F\s*[–—-]/i,
    subsections: [
      {
        name: "Contextual Lexicon & Domain Survey",
        file: "01-Context-Domain.md",
        patterns: ["F.0", "F.1", "F.2", "F.3", "Context", "Domain", "Term", "Sense"]
      },
      {
        name: "Naming & Role Discipline",
        file: "02-Naming-Roles.md",
        patterns: ["F.4", "F.5", "F.6", "Naming", "Role"]
      },
      {
        name: "Concept-Sets & Alignment",
        file: "03-Concept-Alignment.md",
        patterns: ["F.7", "F.8", "F.9", "Concept", "Alignment", "Bridge"]
      },
      {
        name: "Status & Method Harmonisation",
        file: "04-Status-Method.md",
        patterns: ["F.10", "F.11", "F.12", "Status", "Method", "Service"]
      },
      {
        name: "Lexical Evolution & Control",
        file: "05-Lexical-Evolution.md",
        patterns: ["F.13", "F.14", "F.15", "F.16", "Deprecation", "Continuity", "SCR"]
      },
      {
        name: "UTS Blocks & Name Cards",
        file: "06-UTS-NameCards.md",
        patterns: ["F.17", "F.18", "UTS", "Name Card", "Twin"]
      }
    ]
  },
  {
    id: "G",
    title: "Discipline SoTA Architheory Kit",
    description: "Tools for harvesting \"State of the Art\" (SoTA) knowledge, benchmarking methods, and creating selector-ready portfolios of solutions.",
    linePattern: /^#\s*\*?\*?Part\s+G\s*[–—-]/i
  }
];

// Find line numbers for Part boundaries
function findPartBoundaries(lines: string[]): Map<string, { start: number; end: number }> {
  const boundaries = new Map<string, { start: number; end: number }>();
  const partStarts: { id: string; line: number }[] = [];

  // Find Preface
  for (let i = 0; i < lines.length; i++) {
    if (/^#\s*\*?\*?Preface/i.test(lines[i])) {
      partStarts.push({ id: "Preface", line: i });
      break;
    }
  }

  // Find all Part starts
  for (const config of PARTS_CONFIG) {
    for (let i = 0; i < lines.length; i++) {
      if (config.linePattern.test(lines[i])) {
        partStarts.push({ id: config.id, line: i });
        break;
      }
    }
  }

  // Sort by line number
  partStarts.sort((a, b) => a.line - b.line);

  // Calculate boundaries
  for (let i = 0; i < partStarts.length; i++) {
    const current = partStarts[i];
    const next = partStarts[i + 1];
    boundaries.set(current.id, {
      start: current.line,
      end: next ? next.line - 1 : lines.length - 1
    });
  }

  return boundaries;
}

// Extract content for a Part and optionally split into subsections
function extractPartContent(
  lines: string[],
  start: number,
  end: number,
  subsections?: PartConfig["subsections"]
): { main: string; sections: Map<string, string> } {
  const fullContent = lines.slice(start, end + 1).join("\n");
  const sections = new Map<string, string>();

  if (!subsections || subsections.length === 0) {
    return { main: fullContent, sections };
  }

  // Find H1/H2 section boundaries within this part
  interface Section {
    line: number;
    heading: string;
    endLine: number;
  }

  const sectionHeadings: Section[] = [];
  for (let i = start; i <= end; i++) {
    const line = lines[i];
    if (/^#{1,2}\s+/.test(line)) {
      sectionHeadings.push({ line: i, heading: line, endLine: end });
    }
  }

  // Set end lines
  for (let i = 0; i < sectionHeadings.length - 1; i++) {
    sectionHeadings[i].endLine = sectionHeadings[i + 1].line - 1;
  }

  // Assign sections to subsection files
  for (const subsection of subsections) {
    const matchedContent: string[] = [];

    for (const section of sectionHeadings) {
      const headingText = section.heading;
      const matches = subsection.patterns.some(pattern => {
        const regex = new RegExp(pattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
        return regex.test(headingText);
      });

      if (matches) {
        const content = lines.slice(section.line, section.endLine + 1).join("\n");
        matchedContent.push(content);
      }
    }

    if (matchedContent.length > 0) {
      sections.set(subsection.file, matchedContent.join("\n\n---\n\n"));
    }
  }

  return { main: fullContent, sections };
}

// Generate documentation
function generateDocs(lines: string[]): void {
  // Clean output directory
  if (existsSync(OUTPUT_DIR)) {
    rmSync(OUTPUT_DIR, { recursive: true });
  }
  mkdirSync(OUTPUT_DIR, { recursive: true });

  const boundaries = findPartBoundaries(lines);
  const nav: string[] = [];

  nav.push("# FPF Documentation\n");
  nav.push("> Browsable documentation generated from FPF-Spec.md\n");
  nav.push("## Parts\n");

  // Extract and write Preface
  const prefaceBounds = boundaries.get("Preface");
  if (prefaceBounds) {
    const prefaceDir = join(OUTPUT_DIR, "00-Preface");
    mkdirSync(prefaceDir, { recursive: true });
    const prefaceContent = lines.slice(prefaceBounds.start, prefaceBounds.end + 1).join("\n");
    writeFileSync(join(prefaceDir, "README.md"), prefaceContent);
    nav.push("- [Preface](./00-Preface/README.md)");
    console.log("  Created: 00-Preface/README.md");
  }

  // Process each Part
  for (const config of PARTS_CONFIG) {
    const bounds = boundaries.get(config.id);
    if (!bounds) {
      console.log(`  Warning: Part ${config.id} not found`);
      continue;
    }

    const partDirName = `Part-${config.id}`;
    const partDir = join(OUTPUT_DIR, partDirName);
    mkdirSync(partDir, { recursive: true });

    const { main, sections } = extractPartContent(
      lines,
      bounds.start,
      bounds.end,
      config.subsections
    );

    // Create Part README (full content)
    writeFileSync(join(partDir, "README.md"), main);
    console.log(`  Created: ${partDirName}/README.md (${(main.length / 1024).toFixed(0)}KB)`);

    // Create subsection files if configured
    if (config.subsections && sections.size > 0) {
      const partIndex: string[] = [];
      partIndex.push(`# Part ${config.id}: ${config.title}\n`);
      partIndex.push(`${config.description}\n`);
      partIndex.push("## Sections\n");
      partIndex.push("- [Full Part Content](./README.md)\n");

      for (const subsection of config.subsections) {
        const content = sections.get(subsection.file);
        if (content && content.trim().length > 100) {
          writeFileSync(join(partDir, subsection.file), content);
          partIndex.push(`- [${subsection.name}](./${subsection.file})`);
          console.log(`  Created: ${partDirName}/${subsection.file} (${(content.length / 1024).toFixed(0)}KB)`);
        }
      }

      // Write index
      writeFileSync(join(partDir, "INDEX.md"), partIndex.join("\n"));
    }

    nav.push(`- **[Part ${config.id}: ${config.title}](./${partDirName}/README.md)**`);
  }

  // Write main navigation
  nav.push("\n---\n");
  nav.push("*Generated by `bun run generate-docs`*");
  writeFileSync(join(OUTPUT_DIR, "README.md"), nav.join("\n"));
  console.log("\nCreated: docs/README.md (main navigation)");
}

// Main
async function main() {
  console.log("FPF Documentation Generator\n");
  console.log("Reading FPF-Spec.md...");

  const specPath = join(process.cwd(), SPEC_FILE);

  if (!existsSync(specPath)) {
    console.error(`Error: ${SPEC_FILE} not found in current directory`);
    process.exit(1);
  }

  const content = readFileSync(specPath, "utf-8");
  const lines = content.split("\n");
  console.log(`  Read ${lines.length.toLocaleString()} lines (${(content.length / 1024 / 1024).toFixed(1)}MB)\n`);

  console.log("Generating docs with consolidated structure...\n");
  generateDocs(lines);

  console.log("\nDone! Browse the docs/ folder to read the specification.");
}

main().catch(console.error);
