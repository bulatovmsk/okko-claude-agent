#!/usr/bin/env python3
"""Собирает code.js плагина Okko Doc Builder из черновиков Markdown.

Черновики остаются источником правды: правим .md, запускаем сборку, получаем code.js.
Плагин Figma не умеет читать локальные файлы, поэтому контент встраивается в код.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent

SOURCES = {
    "guide": DOCS / "guide-select-web.md",
    "passport": DOCS / "passport-select-web.md",
}

# Мета-секции черновика, которые не являются частью документа в Figma.
EXCLUDE_TITLES = {
    "Секция, которой в черновике нет",
    "Что нужно, чтобы паспорт стал достоверным",
}

INLINE_PATTERNS = [
    (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"),  # ссылки -> текст
    (re.compile(r"\*\*([^*]+)\*\*"), r"\1"),  # жирный
    (re.compile(r"`([^`]+)`"), r"\1"),  # код
    (re.compile(r"\*([^*]+)\*"), r"\1"),  # курсив
]

HEADING = re.compile(r"^(#{2,3})\s+(.*)$")
IS_SEPARATOR_ROW = re.compile(r"^[\s:\-|]+$")
# Маркеры достоверности в конце заголовка не попадают в имя фрейма Figma.
TRAILING_MARKERS = re.compile(r"[\s\u2705\u26a0\ufe0f\u2753]+$")


def clean(text: str) -> str:
    for pattern, repl in INLINE_PATTERNS:
        text = pattern.sub(repl, text)
    return text.strip()


def split_row(line: str) -> list[str]:
    # В таблицах экранированный \| не является границей ячейки.
    guard = line.strip().strip("|").replace("\\|", "\x00")
    return [clean(cell.replace("\x00", "|")) for cell in guard.split("|")]


def parse(markdown: str) -> list[dict]:
    sections: list[dict] = []
    current: dict | None = None
    lines = markdown.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        fence = line.strip().startswith("```")
        if fence:
            i += 1
            buffer = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buffer.append(lines[i])
                i += 1
            i += 1
            if current is not None:
                current["blocks"].append({"type": "code", "text": "\n".join(buffer).rstrip()})
            continue

        heading = HEADING.match(line)
        if heading:
            level, title = heading.group(1), clean(heading.group(2))
            if level == "##":
                title = TRAILING_MARKERS.sub("", title)
                if title in EXCLUDE_TITLES:
                    current = None
                else:
                    current = {"title": title, "blocks": []}
                    sections.append(current)
            elif current is not None:
                current["blocks"].append({"type": "h3", "text": title})
            i += 1
            continue

        if current is None or not line.strip() or line.strip() == "---":
            i += 1
            continue

        if line.startswith(">"):
            buffer = []
            while i < len(lines) and lines[i].startswith(">"):
                buffer.append(lines[i].lstrip(">").strip())
                i += 1
            current["blocks"].append({"type": "note", "text": clean(" ".join(buffer))})
            continue

        if line.startswith("|"):
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].startswith("|"):
                raw = lines[i].strip()
                if not IS_SEPARATOR_ROW.match(raw):
                    rows.append(split_row(raw))
                i += 1
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                current["blocks"].append({"type": "table", "rows": rows})
            continue

        if line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(clean(lines[i][2:]))
                i += 1
            current["blocks"].append({"type": "bullets", "items": items})
            continue

        buffer = [line.strip()]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].startswith(("#", "|", "- ", ">", "```"))
        ):
            buffer.append(lines[i].strip())
            i += 1
        current["blocks"].append({"type": "p", "text": clean(" ".join(buffer))})

    return sections


def main() -> None:
    content = {}
    stats = []
    for key, path in SOURCES.items():
        sections = parse(path.read_text(encoding="utf-8"))
        if not sections:
            raise SystemExit(f"Не разобрано ни одной секции: {path}")
        content[key] = {"sections": sections}
        blocks = sum(len(s["blocks"]) for s in sections)
        stats.append(f"{key}: {len(sections)} секций, {blocks} блоков")

    payload = json.dumps(content, ensure_ascii=False, indent=2)
    template = (HERE / "plugin-template.js").read_text(encoding="utf-8")
    if "__CONTENT_JSON__" not in template:
        raise SystemExit("В шаблоне нет плейсхолдера __CONTENT_JSON__")

    (HERE / "code.js").write_text(
        template.replace("__CONTENT_JSON__", payload), encoding="utf-8"
    )
    print("Собрано:", "; ".join(stats))
    print("Файл:", HERE / "code.js")


if __name__ == "__main__":
    main()
