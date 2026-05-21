#!/usr/bin/env bash
# Упаковывает каждый Skill из skills/ в отдельный zip,
# подкладывая в references/ актуальную выжимку из design-system/.
#
# Usage: bash scripts/pack-skills.sh
# Output: dist/<skill-name>.zip — готово к загрузке в claude.ai (Settings → Features → Skills → Upload)

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
DS_DIR="$ROOT/design-system"
DIST_DIR="$ROOT/dist"

if [ ! -d "$SKILLS_DIR" ]; then
  echo "❌ Не найдена папка skills/" >&2
  exit 1
fi
if [ ! -d "$DS_DIR" ]; then
  echo "❌ Не найдена папка design-system/" >&2
  exit 1
fi

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

# Skills, которым нужна выжимка ДС (компоненты/токены/платформы/бренд) в references/
SKILLS_WITH_DS_REFS=(
  "okko-ds-librarian"
  "okko-ds-auditor"
  "okko-layout-helper"
  "okko-platform-tv"
  "okko-platform-mobile"
)

# Skills, которым нужна выжимка гайдлайнов (STRUCTURE.md + section-templates) в references/
SKILLS_WITH_GUIDELINES_REFS=(
  "okko-doc-writer"
)

for skill_path in "$SKILLS_DIR"/*/; do
  skill_name="$(basename "$skill_path")"
  echo "→ Сборка $skill_name"

  # Готовим временную копию skill'а
  tmp_dir="$DIST_DIR/_tmp/$skill_name"
  mkdir -p "$tmp_dir"
  cp -R "$skill_path"/. "$tmp_dir/"

  # Если skill — из списка тех, кому нужна выжимка ДС, кладём её
  if [[ " ${SKILLS_WITH_DS_REFS[*]} " == *" $skill_name "* ]]; then
    mkdir -p "$tmp_dir/references"
    # Копируем подпапки ДС (без удаления README.md внутри references/)
    for sub in components tokens platforms brand; do
      if [ -d "$DS_DIR/$sub" ]; then
        rm -rf "$tmp_dir/references/$sub"
        cp -R "$DS_DIR/$sub" "$tmp_dir/references/$sub"
      fi
    done
    # И сводный DESIGN_SYSTEM.md
    if [ -f "$DS_DIR/DESIGN_SYSTEM.md" ]; then
      cp "$DS_DIR/DESIGN_SYSTEM.md" "$tmp_dir/references/DESIGN_SYSTEM.md"
    fi
  fi

  # Если skill — из списка тех, кому нужны гайдлайны, кладём их
  if [[ " ${SKILLS_WITH_GUIDELINES_REFS[*]} " == *" $skill_name "* ]]; then
    mkdir -p "$tmp_dir/references"
    if [ -f "$DS_DIR/guidelines/STRUCTURE.md" ]; then
      cp "$DS_DIR/guidelines/STRUCTURE.md" "$tmp_dir/references/STRUCTURE.md"
    fi
    if [ -d "$DS_DIR/guidelines/section-templates" ]; then
      rm -rf "$tmp_dir/references/section-templates"
      cp -R "$DS_DIR/guidelines/section-templates" "$tmp_dir/references/section-templates"
    fi
  fi

  # Валидация: SKILL.md должен существовать
  if [ ! -f "$tmp_dir/SKILL.md" ]; then
    echo "  ⚠️  Пропускаю $skill_name — нет SKILL.md" >&2
    rm -rf "$tmp_dir"
    continue
  fi

  # Упаковываем
  (cd "$DIST_DIR/_tmp" && zip -qr "../${skill_name}.zip" "$skill_name")
  echo "  ✓ dist/${skill_name}.zip"
done

# Чистим временные файлы
rm -rf "$DIST_DIR/_tmp"

echo ""
echo "Готово. Файлы в $DIST_DIR:"
ls -1 "$DIST_DIR" | sed 's/^/  /'
echo ""
echo "Загрузка: claude.ai → Settings → Features → Skills → Upload"
