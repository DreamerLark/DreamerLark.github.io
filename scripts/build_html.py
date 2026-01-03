#!/usr/bin/env python3
"""Convert Markdown pages to simple standalone HTML for GitHub Pages.

This script keeps HTML pages in sync with their Markdown sources so Pages
deployment does not rely on Jekyll. It is intentionally dependency-light
and only requires the `markdown` package.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import markdown


STYLE = dedent(
    """
    :root { color-scheme: light; }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        max-width: 960px;
        margin: 2rem auto;
        padding: 0 1rem 3rem;
        line-height: 1.6;
        color: #222;
        background: #fff;
    }
    h1, h2, h3, h4 { color: #111; }
    a { color: #0366d6; text-decoration: none; }
    a:hover { text-decoration: underline; }
    nav {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-bottom: 1.5rem;
    }
    nav a {
        padding: 0.35rem 0.65rem;
        border-radius: 6px;
        background: #f6f8fa;
        border: 1px solid #e1e4e8;
        color: #0366d6;
    }
    pre {
        background: #f6f8fa;
        padding: 1rem;
        border-radius: 8px;
        overflow-x: auto;
    }
    code {
        background: #f6f8fa;
        padding: 0.2rem 0.35rem;
        border-radius: 4px;
    }
    table { border-collapse: collapse; }
    table, th, td { border: 1px solid #e1e4e8; }
    th, td { padding: 0.5rem 0.75rem; }
    """
)

NAV = dedent(
    """
    <nav>
      <a href="./index.html">主页（HTML）</a>
      <a href="./codex.html">Codex 学习记录（HTML）</a>
      <a href="./README.html">README（HTML）</a>
      <a href="./index.md">主页（Markdown）</a>
      <a href="./codex.md">Codex（Markdown）</a>
      <a href="./README.md">README（Markdown）</a>
      <a href="https://github.com/DreamerLark">GitHub 主页</a>
    </nav>
    """
)

TEMPLATE = dedent(
    """\
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>{title}</title>
      <style>
    {style}
      </style>
    </head>
    <body>
    {nav}
    <main>
    {body}
    </main>
    </body>
    </html>
    """
)


def extract_title(markdown_text: str, default: str) -> str:
    """Use the first H1 heading as the page title when available."""
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return default


def strip_front_matter(text: str) -> str:
    """Remove leading YAML front matter if present."""
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                return "\n".join(lines[idx + 1 :])
    return text


def render_page(md_path: Path) -> None:
    text = strip_front_matter(md_path.read_text(encoding="utf-8"))
    title = extract_title(text, md_path.stem)
    body_html = markdown.markdown(text, extensions=["fenced_code", "tables", "toc"])

    output_path = md_path.with_suffix(".html")
    output_path.write_text(
        TEMPLATE.format(
            title=title,
            style=STYLE,
            nav=NAV,
            body=body_html,
        ),
        encoding="utf-8",
    )
    print(f"Generated {output_path}")


def main() -> None:
    pages = ["index.md", "codex.md", "README.md"]
    for page in pages:
        md_file = Path(page)
        if md_file.exists():
            render_page(md_file)


if __name__ == "__main__":
    main()
