#!/usr/bin/env python3
"""Refresh a standalone Figma skill fallback and package library guidelines."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "figma-guidelines"
MARKER = "<!-- GENERATED GUIDELINES FALLBACK -->"
FILES = ("overview.md", "tokens.md", "components.md", "layouts.md",
         "platforms.md", "anti-patterns.md")


def package():
    skill = BASE / "skills/ui-type-rail-build.md"
    workflow = skill.read_text(encoding="utf-8").split(MARKER, 1)[0].rstrip()
    fallback = "\n\n".join((BASE / "ui-type" / name).read_text(encoding="utf-8").rstrip()
                             for name in FILES)
    skill.write_text(workflow + "\n\n" + MARKER +
                     "\n\n# Резервный справочник правил\n\n"
                     "Используй, если библиотечные Guidelines недоступны в контексте. "
                     "Не заменяет реальные компоненты или проверку их наличия.\n\n" +
                     fallback + "\n", encoding="utf-8")
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    archive = dist / "okko-ui-type-figma-guidelines.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(BASE.rglob("*.md")):
            bundle.write(path, path.relative_to(BASE).as_posix())
    print("Updated standalone skill and " + archive.name)


if __name__ == "__main__":
    package()
