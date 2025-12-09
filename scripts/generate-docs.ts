/**
 * FPF Documentation Generator
 *
 * Parses FPF-Spec.md and generates a browsable folder structure
 * for easier navigation on GitHub and locally.
 *
 * Usage: bun run scripts/generate-docs.ts
 */

import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "fs";
import { join, dirname } from "path";

const SPEC_FILE = "FPF-Spec.md";
const OUTPUT_DIR = "docs";

interface Section {
  title: string;
  slug: string;
  level: number;
  lineStart: number;
  lineEnd: number;
  content: string;
  part?: string;
}

interface Part {
  id: string;
  title: string;
  sections: Section[];
}

// Clean title for use as filename
function slugify(text: string): string {
  return text
    .replace(/^\*\*|\*\*$/g, "") // Remove bold markers
    .replace(/[·—–\-:]/g, "-")   // Replace separators with dash
    .replace(/\[.*?\]/g, "")      // Remove [A], [D], etc.
    .replace(/\(.*?\)/g, "")      // Remove parenthetical notes
    .replace(/[^\w\s-]/g, "")     // Remove special chars
    .trim()
    .replace(/\s+/g, "-")         // Spaces to dashes
    .replace(/-+/g, "-")          // Multiple dashes to single
    .replace(/^-|-$/g, "")        // Trim leading/trailing dashes
    .toLowerCase()
    .substring(0, 60);            // Limit length
}

// Extract part letter from section title (e.g., "A.1" -> "A")
function extractPartLetter(title: string): string | null {
  const match = title.match(/^[*\s]*([A-G])\./);
  return match ? match[1] : null;
}

// Check if line is a Part header
function isPartHeader(line: string): { id: string; title: string } | null {
  // Match patterns like "# Part A –", "# **Part C —"
  const match = line.match(/^#\s*\*?\*?Part\s+([A-G])\s*[–—-]\s*(.+)/i);
  if (match) {
    return { id: match[1].toUpperCase(), title: match[2].replace(/\*\*/g, "").trim() };
  }
  return null;
}

// Check if this is the Preface section
function isPrefaceHeader(line: string): boolean {
  return /^#\s*\*?\*?Preface/i.test(line);
}

// Check if this is ToC or title (to skip)
function isSkippableHeader(line: string): boolean {
  return /^#\s*(First Principles Framework|Table of Content)/i.test(line);
}

// Parse the spec file and extract structure
function parseSpec(content: string): { preface: Section | null; parts: Map<string, Part> } {
  const lines = content.split("\n");
  const parts = new Map<string, Part>();
  let preface: Section | null = null;

  // Initialize parts A-G
  const partTitles: Record<string, string> = {
    A: "Kernel Architecture Cluster",
    B: "Trans-disciplinary Reasoning Cluster",
    C: "Architheory Specifications",
    D: "Multi-scale Ethics & Conflict-Optimisation",
    E: "FPF Constitution and Authoring Cluster",
    F: "The Unification Suite",
    G: "Discipline SoTA Architheory Kit"
  };

  for (const [id, title] of Object.entries(partTitles)) {
    parts.set(id, { id, title, sections: [] });
  }

  // First pass: find all H1/H2 heading positions
  interface Heading {
    line: number;
    level: number;
    text: string;
    raw: string;
  }

  const headings: Heading[] = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const h1Match = line.match(/^#\s+(.+)/);
    const h2Match = line.match(/^##\s+(.+)/);

    if (h1Match) {
      headings.push({ line: i, level: 1, text: h1Match[1], raw: line });
    } else if (h2Match) {
      headings.push({ line: i, level: 2, text: h2Match[1], raw: line });
    }
  }

  // Second pass: assign sections to parts
  let currentPart: string | null = null;
  let prefaceStart: number | null = null;
  let prefaceEnd: number | null = null;

  for (let i = 0; i < headings.length; i++) {
    const heading = headings[i];
    const nextHeading = headings[i + 1];
    const lineEnd = nextHeading ? nextHeading.line - 1 : lines.length - 1;

    // Skip title and ToC
    if (isSkippableHeader(heading.raw)) {
      continue;
    }

    // Check for Preface
    if (isPrefaceHeader(heading.raw)) {
      prefaceStart = heading.line;
      // Find where preface ends (next Part header)
      for (let j = i + 1; j < headings.length; j++) {
        if (isPartHeader(headings[j].raw)) {
          prefaceEnd = headings[j].line - 1;
          break;
        }
      }
      if (prefaceEnd === null) prefaceEnd = lineEnd;

      preface = {
        title: "Preface",
        slug: "preface",
        level: 1,
        lineStart: prefaceStart,
        lineEnd: prefaceEnd,
        content: lines.slice(prefaceStart, prefaceEnd + 1).join("\n")
      };
      continue;
    }

    // Check for Part header
    const partInfo = isPartHeader(heading.raw);
    if (partInfo) {
      currentPart = partInfo.id;
      const part = parts.get(currentPart);
      if (part) {
        part.title = partInfo.title;
      }
      continue;
    }

    // Try to determine part from section number (e.g., "A.1", "B.2.3")
    const partLetter = extractPartLetter(heading.text);
    if (partLetter) {
      currentPart = partLetter;
    }

    // If we have a current part, add this section
    if (currentPart && heading.level <= 2) {
      const part = parts.get(currentPart);
      if (part) {
        const sectionContent = lines.slice(heading.line, lineEnd + 1).join("\n");

        // Only add if it has meaningful content (more than just the heading)
        if (sectionContent.trim().split("\n").length > 1) {
          part.sections.push({
            title: heading.text.replace(/^\*\*|\*\*$/g, "").trim(),
            slug: slugify(heading.text),
            level: heading.level,
            lineStart: heading.line,
            lineEnd: lineEnd,
            content: sectionContent,
            part: currentPart
          });
        }
      }
    }
  }

  return { preface, parts };
}

// Generate the docs folder structure
function generateDocs(preface: Section | null, parts: Map<string, Part>): void {
  // Clean and create output directory
  if (existsSync(OUTPUT_DIR)) {
    rmSync(OUTPUT_DIR, { recursive: true });
  }
  mkdirSync(OUTPUT_DIR, { recursive: true });

  const nav: string[] = [];
  nav.push("# FPF Documentation\n");
  nav.push("> Generated from FPF-Spec.md - browse the specification by parts\n");
  nav.push("## Navigation\n");

  // Write preface
  if (preface) {
    const prefaceDir = join(OUTPUT_DIR, "00-Preface");
    mkdirSync(prefaceDir, { recursive: true });
    writeFileSync(join(prefaceDir, "README.md"), preface.content);
    nav.push(`- [Preface](./00-Preface/README.md)`);
    console.log(`  Created: 00-Preface/README.md`);
  }

  // Write each part
  const partOrder = ["A", "B", "C", "D", "E", "F", "G"];

  for (const partId of partOrder) {
    const part = parts.get(partId);
    if (!part || part.sections.length === 0) continue;

    const partDirName = `Part-${partId}`;
    const partDir = join(OUTPUT_DIR, partDirName);
    mkdirSync(partDir, { recursive: true });

    // Create part index
    const partIndex: string[] = [];
    partIndex.push(`# Part ${partId}: ${part.title}\n`);
    partIndex.push(`## Sections\n`);

    nav.push(`- **[Part ${partId}: ${part.title}](./${partDirName}/README.md)**`);

    // Write each section
    for (let i = 0; i < part.sections.length; i++) {
      const section = part.sections[i];
      const fileName = `${String(i + 1).padStart(2, "0")}-${section.slug || "section"}.md`;
      const filePath = join(partDir, fileName);

      writeFileSync(filePath, section.content);
      partIndex.push(`  - [${section.title}](./${fileName})`);
      console.log(`  Created: ${partDirName}/${fileName}`);
    }

    // Write part README
    writeFileSync(join(partDir, "README.md"), partIndex.join("\n"));
    console.log(`  Created: ${partDirName}/README.md`);
  }

  // Write main navigation
  writeFileSync(join(OUTPUT_DIR, "README.md"), nav.join("\n"));
  console.log(`\nCreated: ${OUTPUT_DIR}/README.md (main navigation)`);
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
  console.log(`  Read ${content.length.toLocaleString()} characters\n`);

  console.log("Parsing structure...");
  const { preface, parts } = parseSpec(content);

  let totalSections = preface ? 1 : 0;
  for (const part of parts.values()) {
    totalSections += part.sections.length;
  }
  console.log(`  Found ${totalSections} sections across ${parts.size} parts\n`);

  console.log("Generating docs folder...");
  generateDocs(preface, parts);

  console.log("\nDone! Browse the docs/ folder to read the specification.");
}

main().catch(console.error);
