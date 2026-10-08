"""Regenerate the article catalog in README.md from articles.csv.

Add a row to articles.csv (newest articles get the lowest `order`), then run:

    python scripts/build_readme.py

Only the text between the CATALOG markers in README.md is rewritten.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/atonyhonesto"

THEMES = [
    ("motorsports-sports", "🏎️ Motorsports & Sports Technology"),
    ("ai-ml", "🤖 AI, Machine Learning & Agents"),
    ("cloud-data-integration", "☁️ Cloud, Data & Integration"),
    ("software-architecture", "🧱 Software Architecture & Engineering Practice"),
    ("engineering-tools", "🛠️ Simulation, Engineering Tools & Hardware"),
]


def load() -> list[dict]:
    with open(ROOT / "articles.csv", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    rows.sort(key=lambda r: int(r["order"]))
    return rows


def line(r: dict) -> str:
    parts = [f"[{r['title']}]({r['linkedin_url']})"]
    if r["deep_dive"]:
        parts.append(f"[📊 deep dive]({r['deep_dive']}/README.md)")
    if r["companion_repo"]:
        parts.append(f"[💻 code]({GITHUB}/{r['companion_repo']})")
    return "- " + " · ".join(parts)


def render(rows: list[dict]) -> str:
    out = [f"**{len(rows)} articles**, newest first within each theme.", ""]
    known = {key for key, _ in THEMES}
    unknown = sorted({r["theme"] for r in rows} - known)
    if unknown:
        raise SystemExit(f"Unknown theme(s) in articles.csv: {unknown}")
    for key, label in THEMES:
        items = [r for r in rows if r["theme"] == key]
        if not items:
            continue
        out.append("<details>")
        out.append(f"<summary><b>{label}</b> ({len(items)})</summary>")
        out.append("")
        out.extend(line(r) for r in items)
        out.append("")
        out.append("</details>")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(r"(<!-- CATALOG:START -->\n).*?(<!-- CATALOG:END -->)", re.S)
    if not pattern.search(text):
        raise SystemExit("CATALOG markers not found in README.md")
    new = pattern.sub(lambda m: m.group(1) + render(load()) + m.group(2), text)
    count = len(load())
    new = re.sub(r"articles-\d+-", f"articles-{count}-", new)  # keep the badge count honest
    readme.write_text(new, encoding="utf-8")
    print(f"README.md catalog rebuilt ({count} articles)")


if __name__ == "__main__":
    main()
