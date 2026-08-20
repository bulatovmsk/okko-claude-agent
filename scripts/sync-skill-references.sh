#!/usr/bin/env bash
# Обновляет бандлованные references внутри repo-scoped Codex skills.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="${CODEX_SKILLS_DIR:-$ROOT/.agents/skills}"
DS_DIR="${DESIGN_SYSTEM_DIR:-$ROOT/design-system}"

if [ ! -d "$SKILLS_DIR" ] || [ ! -d "$DS_DIR" ]; then
  echo "Не найдены .agents/skills или design-system" >&2
  exit 1
fi

sync_design_system() {
  local skill_name="$1"
  local refs="$SKILLS_DIR/$skill_name/references"

  mkdir -p "$refs"
  for section in components tokens platforms brand; do
    rm -rf "$refs/$section"
    if [ -d "$DS_DIR/$section" ]; then
      cp -R "$DS_DIR/$section" "$refs/$section"
    fi
  done

  rm -f "$refs/DESIGN_SYSTEM.md"
  cp "$DS_DIR/DESIGN_SYSTEM.md" "$refs/DESIGN_SYSTEM.md"
}

for skill_name in \
  design-ds-librarian \
  design-ds-auditor \
  design-layout-helper \
  design-platform-mobile \
  design-platform-tv; do
  sync_design_system "$skill_name"
done

DOC_REFS="$SKILLS_DIR/design-doc-writer/references"
mkdir -p "$DOC_REFS"
rm -f "$DOC_REFS/STRUCTURE.md"
rm -rf "$DOC_REFS/section-templates"
cp "$DS_DIR/guidelines/STRUCTURE.md" "$DOC_REFS/STRUCTURE.md"
cp -R "$DS_DIR/guidelines/section-templates" "$DOC_REFS/section-templates"

find "$SKILLS_DIR" -name '.DS_Store' -delete
echo "References обновлены в .agents/skills"
