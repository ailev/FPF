#!/usr/bin/env python3
"""Generate an Obsidian-native knowledge graph from an FPF-Spec.md source.

The monolithic source is intentionally not bundled with this repository. Pass
an explicit path to FPF-Spec.md from an upstream checkout or temporary copy.

Design:
- H1 sections become hub/index pages.
- H2 sections become actual knowledge pages.
- H3+ sections remain inside their H2 page.
- Known FPF ids become wiki-links.
- YAML frontmatter carries parent, page_type, mode, source lines, status,
  normativity, terms, and extracted relations.

Run from the FPF repo root:
    scripts/build_fpf_obsidian_graph.py --source /path/to/FPF-Spec.md --out FPF-Spec --clean
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)\s*$")
CODE_FENCE_RE = re.compile(r"^\s*(```|~~~)")
ID_START_RE = re.compile(
    r"^(?P<id>[A-Z](?:\.[A-Za-z0-9][A-Za-z0-9-]*)+)\s*(?:[-–—:]|$)\s*(?P<title>.*)$"
)
ID_RE = re.compile(r"(?<![\w/`|#])([A-Z](?:\.[A-Za-z0-9][A-Za-z0-9-]*)+)(?![\w/`-])")
BACKTICK_ID_RE = re.compile(r"`([A-Z](?:\.[A-Za-z0-9][A-Za-z0-9-]*)+)`")
U_TERM_RE = re.compile(r"(?<![\w/`])U\.[A-Za-z][A-Za-z0-9]*(?:\.[A-Za-z][A-Za-z0-9]*)?(?![\w/`])")
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
REL_LABEL_RE = re.compile(r"^(Builds on|Coordinates with|Used by|See also|Depends on|Extends|Related):\s*(.*)$", re.I)
BOLD_REL_LABEL_RE = re.compile(r"^\s*-\s+\*\*(Builds on|Coordinates with|Used by|See also|Depends on|Extends|Related):\*\*\s*(.*)$", re.I)
BULLET_RE = re.compile(r"^\s*-\s+(.*)$")
FRONTMATTER_STATUS_RE = re.compile(r"^>\s*\*\*Status:\*\*\s*(.+)$", re.M)
FRONTMATTER_NORM_RE = re.compile(r"^>\s*\*\*Normativity:\*\*\s*(.+)$", re.M)
BAD_FILENAME_CHARS = '<>:"/\\|?*'
MAX_NAME = 170
INDEX_DIR = "00_Index"
HUBS_DIR = "00_Hubs"


@dataclass
class Heading:
    level: int
    text: str
    line: int


@dataclass
class Page:
    kind: str
    heading: Heading
    start: int
    end: int
    body: list[str]
    page_name: str = ""
    parent_hub: str = ""
    fpf_id: str = ""
    title: str = ""
    page_type: str = ""
    status: str = "generated"
    normativity: str = ""
    terms: list[str] = field(default_factory=list)
    relations: dict[str, list[str]] = field(default_factory=dict)


def clean_title(text: str) -> str:
    return text.replace("**", "").replace("__", "").strip()


def safe_name(text: str) -> str:
    s = clean_title(text).replace("\u00a0", " ")
    # Normalize Unicode dash-like characters in filenames. Obsidian can handle
    # them, but git/status output may show bytes such as \342\200\221 for
    # U+2011 non-breaking hyphen, which is hard to read and type.
    s = s.translate(str.maketrans({
        "\u2010": "-",  # hyphen
        "\u2011": "-",  # non-breaking hyphen
        "\u2012": "-",  # figure dash
        "\u2013": "-",  # en dash
        "\u2014": "-",  # em dash
        "\u2212": "-",  # minus sign
    }))
    s = re.sub(r"[`*_]+", "", s)
    s = "".join("-" if c in BAD_FILENAME_CHARS else c for c in s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    return (s[:MAX_NAME].rstrip(" .") or "Untitled")


def titled_id_folder(id_part: str, title: str = "") -> str:
    """Folder segment for an FPF id part, with optional owning-page title."""
    prefix = pad_id_part(id_part)
    return f"{prefix}_{safe_name(title)}" if title else prefix


def part_title_from_hub(root_id: str, parent_hub: str) -> str:
    """Extract title from an H1 hub like 'Part B - Trans-disciplinary Reasoning Cluster'."""
    clean = safe_name(parent_hub)
    m = re.match(r"Part ([A-Z])\s*-\s*(.+)$", clean)
    if m and m.group(1) == root_id:
        return m.group(2).strip()
    return ""


def root_id_folder(root_id: str, root_to_part_title: dict[str, str]) -> str:
    """Root folder for an FPF letter, named from the actual H1 Part title.

    Example:
    Part A - Kernel Architecture Cluster -> A_Kernel Architecture Cluster
    Part G - Discipline SoTA Patterns Kit -> G_Discipline SoTA Patterns Kit
    """
    root = safe_name(root_id)
    part_title = root_to_part_title.get(root_id, "")
    return f"{root}_{safe_name(part_title)}" if part_title else root


def id_parent(prefix_id: str) -> str:
    parts = prefix_id.split(".")
    return parts[0] if len(parts) == 2 else ".".join(parts[:-1])


def build_id_order_maps(pages: list[Page]) -> tuple[dict[tuple[str, str], int], dict[str, int], set[str]]:
    """Return source-order indexes for every tree entry.

    The order is contextual: inside folder C.2, the C.2 page itself and
    immediate child entries C.2.1, C.2.P, C.2.2 are sorted together by their
    original source line.
    """
    prefix_start: dict[str, int] = {}
    exact_start = {page.fpf_id: page.start for page in pages if page.fpf_id}
    exact_ids = set(exact_start)
    descendant_prefixes: set[str] = set()

    for page in pages:
        if not page.fpf_id:
            continue
        parts = page.fpf_id.split(".")
        for depth in range(2, len(parts) + 1):
            prefix_id = ".".join(parts[:depth])
            prefix_start[prefix_id] = min(prefix_start.get(prefix_id, page.start), page.start)
            if prefix_id != page.fpf_id and prefix_id in exact_ids:
                descendant_prefixes.add(prefix_id)

    children: dict[str, list[str]] = defaultdict(list)
    for prefix_id in prefix_start:
        children[id_parent(prefix_id)].append(prefix_id)

    entry_order: dict[tuple[str, str], int] = {}
    folder_parents = set(children) | exact_ids
    for parent in folder_parents:
        entries = list(children.get(parent, []))
        if parent in exact_start:
            entries.append(parent)
        entries = sorted(set(entries), key=lambda x: (exact_start.get(x, prefix_start.get(x, 10**12)), x))
        for idx, entry_id in enumerate(entries):
            entry_order[(parent, entry_id)] = idx
    return entry_order, prefix_start, descendant_prefixes


def ordered_id_folder(prefix_id: str, title: str, entry_order: dict[tuple[str, str], int]) -> str:
    """Folder segment ordered by source position while preserving id information."""
    last_part = prefix_id.split(".")[-1]
    source_order = f"{entry_order.get((id_parent(prefix_id), prefix_id), 0):02d}"
    id_label = pad_id_part(last_part)
    prefix = source_order if source_order == id_label else f"{source_order}_{id_label}"
    clean = safe_name(title) if title else ""
    return f"{prefix}_{clean}" if clean else prefix


def folder_part_count_for_page(page: Page, descendant_prefixes: set[str]) -> int:
    parts = page.fpf_id.split(".")
    if len(parts) < 2:
        return 0
    has_descendants = page.fpf_id in descendant_prefixes
    # Top-level pages, including .0 intro pages, get their own source-ordered
    # folder so the Part tree has only numbered folders at the root. Pages with
    # descendants also get their own folder so the page and its descendants read
    # top-down inside it.
    if len(parts) == 2 or has_descendants:
        return len(parts) - 1
    # Leaf children live in their parent folder.
    return len(parts) - 2


def prefix_folder_for_page(
    page: Page,
    id_to_title: dict[str, str],
    root_to_part_title: dict[str, str],
    entry_order: dict[tuple[str, str], int],
    descendant_prefixes: set[str],
) -> str:
    """Return source-ordered folder path for a generated FPF page."""
    parts = page.fpf_id.split(".")
    if len(parts) < 2:
        return ""
    segments = [root_id_folder(parts[0], root_to_part_title)]
    for depth in range(2, folder_part_count_for_page(page, descendant_prefixes) + 2):
        prefix_id = ".".join(parts[:depth])
        owner_title = id_to_title.get(prefix_id, "")
        segments.append(ordered_id_folder(prefix_id, owner_title, entry_order))
    return "/".join(segments)


def source_ordered_page_base(
    page: Page,
    entry_order: dict[tuple[str, str], int],
    descendant_prefixes: set[str],
    unprefixed_order: dict[int, int],
) -> str:
    """Filename base prefixed for reading order within its tree folder."""
    if not page.fpf_id:
        return f"{unprefixed_order.get(id(page), 0):02d}_{safe_name(page.title)}"

    parts = page.fpf_id.split(".")
    folder_count = folder_part_count_for_page(page, descendant_prefixes)
    if folder_count >= len(parts) - 1:
        parent_for_order = page.fpf_id  # owner page inside its own folder
    elif len(parts) == 2:
        parent_for_order = parts[0]
    else:
        parent_for_order = ".".join(parts[: folder_count + 1])
    order = entry_order.get((parent_for_order, page.fpf_id), 0)
    return f"{order:02d}_{display_id(page.fpf_id)} - {safe_name(page.title)}"


def unprefixed_folder(parent_hub: str) -> str:
    """Route unprefixed H2 pages by the parent H1 found from source lines.

    These are not automatically appendices. If they sit under a Part H1, they
    are Part pages without FPF ids, so keep them in that Part's tree and use
    source-order filename prefixes instead of hiding them in _unprefixed/.
    """
    clean = safe_name(parent_hub)
    low = clean.lower()
    if "readme" in low:
        return "00-readme"
    if "preface" in low:
        return "00-preface"
    m = re.match(r"Part ([A-Z])\s*-\s*(.+)$", clean)
    if m:
        return f"{m.group(1)}_{safe_name(m.group(2))}"
    m = re.match(r"Cluster ([A-Z])\b", clean)
    if m:
        return f"{m.group(1)}"
    return "00-unprefixed/" + clean


def pad_id_part(part: str) -> str:
    """Zero-pad numeric FPF id parts for filesystem sorting."""
    return f"{int(part):02d}" if part.isdigit() else safe_name(part)


def display_id(fpf_id: str) -> str:
    """Filesystem-facing id with numeric parts padded: A.1.1 -> A.01.01.

    Part-local .0 intro pages keep their canonical short id: A.0, G.0.
    """
    parts = fpf_id.split(".")
    if len(parts) == 2 and parts[1].isdigit() and int(parts[1]) == 0:
        return fpf_id
    return ".".join(pad_id_part(part) for part in parts)




def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list(values: list[str], indent: int = 2) -> list[str]:
    if not values:
        return [" " * indent + "[]"]
    return [" " * indent + "- " + yaml_quote(v) for v in values]


def wiki(page: str, alias: str = "") -> str:
    return f"[[{page}|{alias}]]" if alias and alias != page else f"[[{page}]]"


def parse_headings(source: Path) -> tuple[list[str], list[Heading]]:
    lines = source.read_text(encoding="utf-8", errors="replace").splitlines()
    headings: list[Heading] = []
    in_code = False
    for n, line in enumerate(lines, 1):
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        text = m.group(2).strip()
        # The source contains table rows accidentally shaped like H1 headings: "# | ...".
        if text.startswith("|"):
            continue
        headings.append(Heading(len(m.group(1)), text, n))
    return lines, headings


def h1_page_type(title: str) -> str:
    low = clean_title(title).lower()
    if low.startswith("part "):
        return "fpf-part"
    if low.startswith("cluster "):
        return "fpf-cluster"
    if "table of content" in low:
        return "fpf-toc"
    if "readme" in low:
        return "fpf-readme-hub"
    return "fpf-hub"


def h2_page_type(page: Page) -> str:
    if page.fpf_id:
        if re.match(r"^[A-K](\.|$)", page.fpf_id):
            return "fpf-pattern"
        return "fpf-section"
    low = page.title.lower()
    if "glossary" in low:
        return "fpf-glossary"
    if "index" in low:
        return "fpf-index-section"
    if "readme" in low:
        return "fpf-readme-section"
    return "fpf-knowledge-page"


def split_id_title(text: str) -> tuple[str, str]:
    t = clean_title(text).replace("—", "-").replace("–", "-")
    m = ID_START_RE.match(t)
    if not m:
        return "", t
    return m.group("id"), (m.group("title").strip() or m.group("id"))


def next_line(heading: Heading, headings: list[Heading], stop_levels: set[int], line_count: int) -> int:
    later = [h.line for h in headings if h.line > heading.line and h.level in stop_levels]
    return min(later) - 1 if later else line_count


def extract_relations(body: list[str]) -> dict[str, list[str]]:
    rels: dict[str, set[str]] = defaultdict(set)
    in_rel = False
    current = "related"
    for line in body:
        hm = HEADING_RE.match(line)
        if hm:
            ht = hm.group(2).lower()
            in_rel = "relations" in ht or "see also" in ht
            current = "related"
            continue
        bold = BOLD_REL_LABEL_RE.match(line)
        if bold:
            current = normalize_relation(bold.group(1))
            for ref in extract_ids(bold.group(2)):
                rels[current].add(ref)
            continue
        if not in_rel:
            continue
        bm = BULLET_RE.match(line)
        if not bm:
            continue
        item = bm.group(1)
        label = REL_LABEL_RE.match(item)
        if label:
            current = normalize_relation(label.group(1))
            item = label.group(2)
        for ref in extract_ids(item):
            rels[current].add(ref)
    return {k: sorted(v) for k, v in rels.items() if v}


def normalize_relation(label: str) -> str:
    return label.lower().replace(" ", "_").replace("-", "_")


def extract_ids(text: str) -> list[str]:
    refs = set(BACKTICK_ID_RE.findall(text)) | set(ID_RE.findall(text))
    return sorted(r for r in refs if "." in r and not r.startswith("U."))


def enrich(page: Page) -> None:
    first = "\n".join(page.body[:100])
    m = FRONTMATTER_STATUS_RE.search(first)
    if m:
        page.status = m.group(1).strip()
    m = FRONTMATTER_NORM_RE.search(first)
    if m:
        page.normativity = m.group(1).strip()
    text = "\n".join(page.body)
    page.terms = sorted(set(U_TERM_RE.findall(text)))[:120]
    page.relations = extract_relations(page.body)


def build_pages(lines: list[str], headings: list[Heading]) -> tuple[list[Page], list[Page]]:
    h1s = [h for h in headings if h.level == 1]
    h2s = [h for h in headings if h.level == 2]
    hubs: list[Page] = []
    pages: list[Page] = []
    for h in h1s:
        end = next_line(h, headings, {1}, len(lines))
        title = clean_title(h.text)
        hubs.append(Page("hub", h, h.line, end, lines[h.line:end], title=title, page_type=h1_page_type(title)))
    for h in h2s:
        end = next_line(h, headings, {1, 2}, len(lines))
        parent = max((x for x in h1s if x.line < h.line), key=lambda x: x.line, default=None)
        fid, title = split_id_title(h.text)
        page = Page("page", h, h.line, end, lines[h.line:end], parent_hub=clean_title(parent.text) if parent else "", fpf_id=fid, title=title)
        page.page_type = h2_page_type(page)
        enrich(page)
        pages.append(page)
    return hubs, pages


def assign_names(hubs: list[Page], pages: list[Page]) -> tuple[dict[str, str], dict[str, str]]:
    used: Counter[str] = Counter()
    hub_by_title: dict[str, str] = {}
    id_to_page: dict[str, str] = {}
    id_to_title = {page.fpf_id: page.title for page in pages if page.fpf_id}
    entry_order, _prefix_start, descendant_prefixes = build_id_order_maps(pages)

    unprefixed_by_hub: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        if not page.fpf_id:
            unprefixed_by_hub[page.parent_hub].append(page)
    unprefixed_order: dict[int, int] = {}
    for siblings in unprefixed_by_hub.values():
        for idx, page in enumerate(sorted(siblings, key=lambda x: x.start)):
            unprefixed_order[id(page)] = idx

    root_to_part_title = {}
    for hub in hubs:
        m = re.match(r"Part ([A-Z])\s*-\s*(.+)$", safe_name(hub.title))
        if m:
            root_to_part_title[m.group(1)] = m.group(2).strip()
    for hub in hubs:
        base = f"{HUBS_DIR}/FPF - {safe_name(hub.title)}"
        used[base] += 1
        hub.page_name = base if used[base] == 1 else f"{base} ({used[base]})"
        hub_by_title[hub.title] = hub.page_name
    for page in pages:
        folder = (
            prefix_folder_for_page(page, id_to_title, root_to_part_title, entry_order, descendant_prefixes)
            if page.fpf_id
            else unprefixed_folder(page.parent_hub)
        )
        base = source_ordered_page_base(page, entry_order, descendant_prefixes, unprefixed_order)
        rel = f"{folder}/{base}" if folder else base
        used[rel] += 1
        page.page_name = rel if used[rel] == 1 else f"{rel} ({used[rel]})"
        if page.fpf_id:
            id_to_page[page.fpf_id] = page.page_name
    return hub_by_title, id_to_page


def frontmatter(page: Page, source_name: str, hub_by_title: dict[str, str], id_to_page: dict[str, str]) -> str:
    out = ["---"]
    out.append(f"type: {yaml_quote(page.page_type)}")
    out.append("context:")
    out += yaml_list(["FPF"])
    out.append(f"page_type: {yaml_quote(page.page_type)}")
    out.append(f"mode: {yaml_quote('canonical-generated' if page.kind == 'page' else 'index-generated')}")
    if page.fpf_id:
        out.append(f"fpf_id: {yaml_quote(page.fpf_id)}")
    out.append(f"title: {yaml_quote(page.title)}")
    if page.parent_hub:
        parent_page = hub_by_title.get(page.parent_hub, page.parent_hub)
        out.append(f"part: {yaml_quote(wiki(parent_page))}")
        out.append("parents:")
        out += yaml_list([wiki(parent_page)])
    out.append(f"source_file: {yaml_quote(source_name)}")
    out.append("source_lines:")
    out.append(f"  - {page.start}")
    out.append(f"  - {page.end}")
    out.append(f"status: {yaml_quote(page.status)}")
    if page.normativity:
        out.append(f"normativity: {yaml_quote(page.normativity)}")
    if page.terms:
        out.append("terms:")
        out += yaml_list(page.terms)
    for rel, refs in sorted(page.relations.items()):
        out.append(f"{rel}:")
        vals = [wiki(id_to_page[r], r) if r in id_to_page else r for r in refs]
        out += yaml_list(vals)
    out.append(f"generated_on: {yaml_quote(date.today().isoformat())}")
    out.append("generated: true")
    out.append("---")
    return "\n".join(out) + "\n\n"


def demote_headings(body: list[str]) -> list[str]:
    result = []
    for line in body:
        m = HEADING_RE.match(line)
        if not m:
            result.append(line)
            continue
        lvl = len(m.group(1))
        text = m.group(2).strip()
        if lvl == 2:
            result.append("# " + text)
        else:
            result.append("#" * max(2, lvl - 1) + " " + text)
    return result


def split_table_row(line: str) -> list[str]:
    text = line.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]

    cells: list[str] = []
    buf: list[str] = []
    in_wikilink = False
    i = 0
    while i < len(text):
        if text.startswith("[[", i):
            in_wikilink = True
            buf.append("[[")
            i += 2
            continue
        if in_wikilink and text.startswith("]]", i):
            in_wikilink = False
            buf.append("]]")
            i += 2
            continue
        if text[i] == "|" and not in_wikilink:
            cells.append("".join(buf))
            buf = []
        else:
            buf.append(text[i])
        i += 1
    cells.append("".join(buf))
    return cells


def strip_wikilink_aliases_in_table_line(line: str) -> str:
    if not line.lstrip().startswith("|"):
        return line
    return re.sub(
        r"\[\[([^\]\|#]+(?:#[^\]\|]+)?)\|[^\]]+\]\]",
        lambda match: f"[[{match.group(1)}]]",
        line,
    )


def is_table_separator(line: str) -> bool:
    if "|" not in line:
        return False
    cells = split_table_row(line)
    return len(cells) >= 2 and all(re.fullmatch(r"\s*:?-{3,}:?\s*", cell or "") for cell in cells)


def render_table_row(cells: list[str], is_separator: bool = False) -> str:
    if is_separator:
        rendered = []
        for cell in cells:
            c = cell.strip()
            rendered.append(c if re.fullmatch(r":?-{3,}:?", c) else "---")
        return "| " + " | ".join(rendered) + " |"
    return "| " + " | ".join(cell.strip() for cell in cells) + " |"


def remove_empty_table_columns_from_block(block: list[str]) -> list[str]:
    rows = [split_table_row(line) for line in block]
    separator_rows = {i for i, line in enumerate(block) if is_table_separator(line)}
    width = max((len(row) for row in rows), default=0)
    if width <= 1:
        return block
    for row in rows:
        row.extend([""] * (width - len(row)))

    content_row_indexes = [i for i in range(len(rows)) if i not in separator_rows]
    empty_columns = set()
    for col in range(width):
        if all(rows[row_idx][col].strip() == "" for row_idx in content_row_indexes):
            empty_columns.add(col)
    if not empty_columns:
        return block

    keep = [col for col in range(width) if col not in empty_columns]
    if not keep:
        return block
    cleaned = []
    for idx, row in enumerate(rows):
        kept_cells = [row[col] for col in keep]
        cleaned.append(render_table_row(kept_cells, idx in separator_rows))
    return cleaned


def remove_empty_table_columns(lines: list[str]) -> list[str]:
    """Remove markdown table columns that are empty in every content row."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if i + 1 < len(lines) and "|" in lines[i] and is_table_separator(lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].strip() and "|" in lines[j]:
                j += 1
            out.extend(remove_empty_table_columns_from_block(lines[i:j]))
            i = j
        else:
            out.append(lines[i])
            i += 1
    return out


def linkify_line(line: str, id_to_page: dict[str, str]) -> str:
    protected: list[str] = []
    in_table = line.lstrip().startswith("|")

    def hold(value: str) -> str:
        protected.append(value)
        return f"@@P{len(protected)-1}@@"

    def protect(match: re.Match[str]) -> str:
        return hold(match.group(0))

    def linked_ref(ref: str) -> str:
        # Markdown table cells use raw pipes as column separators. Avoid aliases
        # inside tables so generated wiki-links do not create phantom columns.
        return wiki(id_to_page[ref]) if in_table else wiki(id_to_page[ref], ref)

    # Protect existing Markdown links first. Generated links are also stored as
    # placeholders so the later plain-id pass cannot re-link inside them.
    line = re.sub(r"\[\[[^\]]+\]\]", protect, line)
    line = re.sub(r"\[[^\]]+\]\([^\)]+\)", protect, line)

    def repl_backtick(match: re.Match[str]) -> str:
        ref = match.group(1)
        return hold(linked_ref(ref)) if ref in id_to_page else match.group(0)

    line = BACKTICK_ID_RE.sub(repl_backtick, line)

    def repl_plain(match: re.Match[str]) -> str:
        ref = match.group(1)
        if ref not in id_to_page:
            return ref
        # Avoid turning source constructs such as `[B.2.P: note]` into
        # malformed triple-bracket links (`[[[...]]`).
        prefix = " " if match.start() > 0 and match.string[match.start() - 1] == "[" else ""
        return prefix + linked_ref(ref)

    line = ID_RE.sub(repl_plain, line)
    for i, value in enumerate(protected):
        line = line.replace(f"@@P{i}@@", value)
    return strip_wikilink_aliases_in_table_line(line)


def render_page(page: Page, source_name: str, hub_by_title: dict[str, str], id_to_page: dict[str, str]) -> str:
    body_lines = remove_empty_table_columns(demote_headings(page.body))
    body = [linkify_line(x, id_to_page) for x in body_lines]
    return frontmatter(page, source_name, hub_by_title, id_to_page) + "\n".join(body).rstrip() + "\n"


def render_hub(hub: Page, pages: list[Page], source_name: str) -> str:
    children = [p for p in pages if p.parent_hub == hub.title]
    out = [frontmatter(hub, source_name, {}, {})]
    out.append(f"# {hub.title}\n")
    out.append(f"Source lines: `{hub.start}-{hub.end}` in `{source_name}`.\n")
    out.append("## Pages\n")
    for p in children:
        label = p.fpf_id or p.title
        out.append(f"- {wiki(p.page_name, label)} — {p.title}")
    out.append("\n## Table\n")
    out.append("| ID | Page | Type | Lines |")
    out.append("|---|---|---|---|")
    for p in children:
        out.append(f"| {p.fpf_id} | {wiki(p.page_name)} | {p.page_type} | {p.start}-{p.end} |")
    return "\n".join(out).rstrip() + "\n"


def render_master_index(hubs: list[Page], pages: list[Page], source_name: str) -> str:
    out = ["---", 'type: "fpf-index"', "context:", '  - "FPF"', 'page_type: "master-index"', 'mode: "index-generated"', 'title: "FPF - Index"', f"source_file: {yaml_quote(source_name)}", f"generated_on: {yaml_quote(date.today().isoformat())}", "generated: true", "---", "", "# FPF - Index", "", "## Hubs", ""]
    for hub in hubs:
        count = sum(1 for p in pages if p.parent_hub == hub.title)
        out.append(f"- {wiki(hub.page_name)} — {count} pages")
    out += ["", "## Pages", "", "| ID | Page | Parent | Lines |", "|---|---|---|---|"]
    hub_name = {h.title: h.page_name for h in hubs}
    for p in pages:
        parent = wiki(hub_name[p.parent_hub]) if p.parent_hub in hub_name else ""
        out.append(f"| {p.fpf_id} | {wiki(p.page_name)} | {parent} | {p.start}-{p.end} |")
    return "\n".join(out) + "\n"


def render_relation_index(pages: list[Page], id_to_page: dict[str, str]) -> str:
    out = ["---", 'type: "fpf-index"', "context:", '  - "FPF"', 'page_type: "relation-index"', 'mode: "index-generated"', 'title: "FPF - Relation Index"', f"generated_on: {yaml_quote(date.today().isoformat())}", "generated: true", "---", "", "# FPF - Relation Index", "", "| Relation | Source | Target | Resolved |", "|---|---|---|---|"]
    for p in pages:
        for rel, refs in sorted(p.relations.items()):
            for ref in refs:
                target = wiki(id_to_page[ref]) if ref in id_to_page else ref
                out.append(f"| {rel} | {wiki(p.page_name)} | {target} | {'yes' if ref in id_to_page else 'no'} |")
    return "\n".join(out) + "\n"


def render_term_index(pages: list[Page]) -> str:
    term_pages: dict[str, list[Page]] = defaultdict(list)
    for p in pages:
        for term in p.terms:
            term_pages[term].append(p)
    out = ["---", 'type: "fpf-index"', "context:", '  - "FPF"', 'page_type: "term-index"', 'mode: "index-generated"', 'title: "FPF - Term Index"', f"generated_on: {yaml_quote(date.today().isoformat())}", "generated: true", "---", "", "# FPF - Term Index", ""]
    for term in sorted(term_pages):
        links = ", ".join(wiki(p.page_name, p.fpf_id or p.title) for p in term_pages[term][:25])
        more = f" (+{len(term_pages[term]) - 25} more)" if len(term_pages[term]) > 25 else ""
        out.append(f"- `{term}` — {links}{more}")
    return "\n".join(out) + "\n"


def validate(out_dir: Path, hubs: list[Page], pages: list[Page], id_to_page: dict[str, str]) -> dict:
    page_names = {f"{INDEX_DIR}/FPF - Index", f"{INDEX_DIR}/FPF - Relation Index", f"{INDEX_DIR}/FPF - Term Index"} | {h.page_name for h in hubs} | {p.page_name for p in pages}
    broken = []
    for path in out_dir.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target not in page_names:
                broken.append({"file": path.name, "target": target})
    unresolved = []
    for p in pages:
        for rel, refs in p.relations.items():
            for ref in refs:
                if ref not in id_to_page:
                    unresolved.append({"source": p.page_name, "relation": rel, "target": ref})
    return {
        "hubs": len(hubs),
        "pages": len(pages),
        "ids": len(id_to_page),
        "markdown_files": len(list(out_dir.rglob("*.md"))),
        "broken_links_count": len(broken),
        "broken_links_sample": broken[:50],
        "unresolved_relations_count": len(unresolved),
        "unresolved_relations_sample": unresolved[:50],
    }


def build(source: Path, out_dir: Path, clean: bool) -> dict:
    lines, headings = parse_headings(source)
    hubs, pages = build_pages(lines, headings)
    hub_by_title, id_to_page = assign_names(hubs, pages)
    if clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for page in pages:
        path = out_dir / f"{page.page_name}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_page(page, source.name, hub_by_title, id_to_page), encoding="utf-8")
    for hub in hubs:
        path = out_dir / f"{hub.page_name}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_hub(hub, pages, source.name), encoding="utf-8")
    index_dir = out_dir / INDEX_DIR
    index_dir.mkdir(parents=True, exist_ok=True)
    (index_dir / "FPF - Index.md").write_text(render_master_index(hubs, pages, source.name), encoding="utf-8")
    (index_dir / "FPF - Relation Index.md").write_text(render_relation_index(pages, id_to_page), encoding="utf-8")
    (index_dir / "FPF - Term Index.md").write_text(render_term_index(pages), encoding="utf-8")
    report = validate(out_dir, hubs, pages, id_to_page)
    report.update({"source": source.name, "out_dir": out_dir.name, "generated_on": date.today().isoformat()})
    (index_dir / "FPF - Validation Report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Obsidian graph from FPF-Spec.md")
    parser.add_argument("--source", required=True, help="Path to the upstream FPF-Spec.md source")
    parser.add_argument("--out", default="FPF-Spec")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()
    source = Path(args.source).resolve()
    out_dir = Path(args.out).resolve()
    if not source.exists():
        raise SystemExit(f"source not found: {source}")
    report = build(source, out_dir, args.clean)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
