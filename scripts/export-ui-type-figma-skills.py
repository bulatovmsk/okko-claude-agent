#!/usr/bin/env python3
"""Build standalone Figma Agent instructions from canonical Rail references."""
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
OUTPUT = ROOT / "figma-agent-skills"


def read(relative):
    text = (SKILLS / relative).read_text(encoding="utf-8-sig")
    # Standalone instructions cannot depend on repo-local reference links.
    return re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", text)


def export():
    OUTPUT.mkdir(exist_ok=True)
    sections = [
        ("Разбор концепта", "concept.md"),
        ("Общие правила", "common.md"),
        ("Выбор радиуса по минимальной стороне — beta", "radius.md"),
        ("iOS", "ios.md"),
        ("Android", "android.md"),
        ("Web", "web.md"),
        ("Карта существующей библиотеки — снимок", "current-library.md"),
        ("Слоты и Custom при программном редактировании", "figma-mechanics.md"),
    ]
    core = """# Skill: сборка UI Type Rail Okko

Создай Rail по концепту дизайнера любой детализации: вайрфрейм, текст, изображение или подробный макет. Общий запрос охватывает все 14 размеров iOS/Android/Web, включая Desktop. Явное ограничение пользователя имеет приоритет.

Эта инструкция самостоятельна для Figma Agent. Используй доступные ему средства чтения, импорта связанных компонентов и редактирования Figma. Имена инструментов Codex и локальные пути не требуются. При отсутствии нужной возможности сообщи точное ограничение, сохранив уже сделанную независимую работу.

Разбери концепт, найди реальные компоненты и зависимости, собери варианты и проверь результат по следующим правилам. Новых переменных и токенов не создавай. Сначала проверь живую библиотеку: приведённые ID и измерения являются датированным снимком.

"""
    core += "\n\n".join("## " + title + "\n\n" + read("build-ui-type/references/" + path) for title, path in sections)
    guide = """# Skill: сетки Rail Okko

Создавай и обновляй нативные Layout Guide styles в рабочей библиотеке UI Type. Используй возможности Figma Agent; новые компоненты, коллекции переменных и токены для сеток не создавай. Проверяй существующие стили перед созданием дублей.

Сохраняй iOS guides без отдельного запроса на изменение. На Web нужны подписи breakpoint=320, breakpoint=375, breakpoint=768, breakpoint=1024, breakpoint=1440, breakpoint=1920 над примерами и значения в названиях общих стилей. 440 — только «Пример растяжения». Один стиль применяется к полному экранному фрейму и растягивается; автоматическое переключение стиля по ширине не предполагается.

Проверь назначенный стиль, число колонок, padding, gutter, правую полосу и привязки к существующим переменным. Gutter Android 8/12 не заменяет межкарточный gap 6/8. Обычный экспорт не показывает нативные сетки: проверяй свойства и включённые guides в редакторе.

"""
    guide += read("rail-layout-guides/references/guides.md")
    results = {"ui-type-builder.md": core, "rail-layout-guides.md": guide}
    for filename, content in results.items():
        (OUTPUT / filename).write_text(content.rstrip() + "\n", encoding="utf-8")
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    with zipfile.ZipFile(dist / "ui-type-figma-agent.zip", "w", zipfile.ZIP_DEFLATED) as bundle:
        for filename in results:
            bundle.write(OUTPUT / filename, filename)
    print("Exported 2 standalone instructions and dist/ui-type-figma-agent.zip")


if __name__ == "__main__":
    export()
