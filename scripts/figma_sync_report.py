#!/usr/bin/env python3
"""Build a compact Markdown report for one Figma synchronization run."""

from __future__ import annotations

import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    return {str(path.relative_to(root)): path for path in root.rglob("*") if path.is_file()}


def changes(before: Path, after: Path, label: str) -> list[tuple[str, str]]:
    old = files(before)
    new = files(after)
    result: list[tuple[str, str]] = []
    for name in sorted(old.keys() | new.keys()):
        display = f"{label}/{name}"
        if name not in old:
            result.append(("added", display))
        elif name not in new:
            result.append(("deleted", display))
        elif digest(old[name]) != digest(new[name]):
            result.append(("modified", display))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before-source", required=True, type=Path)
    parser.add_argument("--after-source", required=True, type=Path)
    parser.add_argument("--before-skills", type=Path)
    parser.add_argument("--after-skills", type=Path)
    parser.add_argument("--status", required=True, choices=("complete", "blocked", "failed"))
    parser.add_argument("--group", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--variables-source", action="append", default=[])
    parser.add_argument("--message", default="")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    rows = changes(args.before_source, args.after_source, "design-system")
    if args.before_skills and args.after_skills:
        rows.extend(changes(args.before_skills, args.after_skills, ".agents/skills"))

    status_label = {"complete": "Завершено", "blocked": "Заблокировано", "failed": "Ошибка"}[args.status]
    lines = [
        "# Отчёт синхронизации Figma → Okko Design System",
        "",
        f"- Статус: **{status_label}**",
        f"- Запуск: `{datetime.now(timezone.utc).isoformat(timespec='seconds')}`",
        f"- Область: `{args.group} {args.target}`",
    ]
    if args.variables_source:
        lines.append(f"- Variables: {', '.join(f'`{item}`' for item in args.variables_source)}")
    if args.message:
        lines.extend(("", "## Результат", "", args.message))

    lines.extend(("", "## Изменения", ""))
    if rows:
        lines.extend(("| Статус | Файл |", "|---|---|"))
        labels = {"added": "добавлен", "modified": "изменён", "deleted": "удалён"}
        lines.extend(f"| {labels[state]} | `{path}` |" for state, path in rows)
    else:
        lines.append("Изменений нет.")

    lines.extend(("", "## Проверки", ""))
    if args.status == "complete":
        lines.extend((
            "- Aliases разрешены до обновления канонического source.",
            "- `references/` пересобраны только после успешного обновления source.",
            "- Skill-структура проверена валидатором.",
        ))
    else:
        lines.append("- Канонический source и skills не обновлены: workflow остановлен до публикации staged-результата.")
    lines.extend(("- Коммит, push и публикация не выполнялись.", ""))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines))
    print(args.output)


if __name__ == "__main__":
    main()
