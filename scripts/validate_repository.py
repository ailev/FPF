#!/usr/bin/env python3
"""Validate the portable FPF projection and bundled skill packages."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "FPF-Spec"
REPORT_PATH = GRAPH / "00_Index" / "FPF - Validation Report.json"
README_PATH = ROOT / "Readme.md"
SKILLS = ROOT / "skills"


def main() -> int:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(not (ROOT / "FPF-Spec.md").exists(), "root FPF-Spec.md must remain absent")
    require(not (ROOT / "FPF-Spec-original").exists(), "the monolithic source must not be bundled")

    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read validation report: {exc}")
        report = {}

    markdown_files = sorted(GRAPH.rglob("*.md"))
    require(report.get("source") == "FPF-Spec.md", "report source must be portable")
    require(report.get("out_dir") == "FPF-Spec", "report output path must be portable")
    require(report.get("broken_links_count") == 0, "generated graph contains broken wiki-links")
    require(report.get("markdown_files") == len(markdown_files), "report Markdown count does not match disk")

    fpf_ids: list[str] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        require(text.startswith("---\n"), f"missing frontmatter: {path.relative_to(ROOT)}")
        require("[[[" not in text, f"malformed triple-bracket link: {path.relative_to(ROOT)}")
        match = re.search(r'^fpf_id: "([^"]+)"', text, re.MULTILINE)
        if match:
            fpf_ids.append(match.group(1))

    require(report.get("ids") == len(fpf_ids), "report FPF ID count does not match generated pages")
    require(len(fpf_ids) == len(set(fpf_ids)), "generated FPF IDs are not unique")

    readme = README_PATH.read_text(encoding="utf-8")
    for raw_target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme):
        if raw_target.startswith(("http://", "https://", "#")):
            continue
        target = unquote(raw_target).split("#", 1)[0]
        require((ROOT / target).exists(), f"README link does not exist: {raw_target}")

    skill_paths = sorted(SKILLS.glob("*.skill/SKILL.md"))
    require(len(skill_paths) == 3, "expected exactly three FPF skill packages")
    for skill_path in skill_paths:
        package = skill_path.parent
        expected_name = package.name.removesuffix(".skill")
        skill_text = skill_path.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
        require(frontmatter is not None, f"missing skill frontmatter: {skill_path.relative_to(ROOT)}")
        if frontmatter:
            name = re.search(r"^name:\s*(\S+)\s*$", frontmatter.group(1), re.MULTILINE)
            description = re.search(r"^description:\s*(.+)$", frontmatter.group(1), re.MULTILINE)
            require(name is not None and name.group(1) == expected_name, f"skill name mismatch: {expected_name}")
            require(description is not None and bool(description.group(1).strip()), f"missing skill description: {expected_name}")

        metadata_path = package / "agents" / "openai.yaml"
        require(metadata_path.exists(), f"missing OpenAI metadata: {expected_name}")
        if metadata_path.exists():
            metadata = metadata_path.read_text(encoding="utf-8")
            for key in ("display_name", "short_description", "default_prompt"):
                require(re.search(rf"^\s+{key}:\s*.+$", metadata, re.MULTILINE) is not None, f"missing {key}: {expected_name}")
            require(f"${expected_name}" in metadata, f"default prompt does not invoke ${expected_name}")

    help_result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_fpf_obsidian_graph.py"), "--help"],
        check=False,
        capture_output=True,
        text=True,
    )
    require(help_result.returncode == 0 and "--source SOURCE" in help_result.stdout, "generator must require --source")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "markdown_files": len(markdown_files),
                "fpf_ids": len(fpf_ids),
                "broken_links": report.get("broken_links_count"),
                "skill_packages": len(skill_paths),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
