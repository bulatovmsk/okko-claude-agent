#!/usr/bin/env bash
# Синхронизирует, проверяет и упаковывает Codex skills по одному в dist/*.zip.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT/.agents/skills"
DIST_DIR="$ROOT/dist"

bash "$ROOT/scripts/sync-skill-references.sh"
bash "$ROOT/scripts/validate-skills.sh"

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

for skill_dir in "$SKILLS_DIR"/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  (
    cd "$SKILLS_DIR"
    zip -qr "$DIST_DIR/$skill_name.zip" "$skill_name" -x '*/.DS_Store'
  )
  echo "Собран dist/$skill_name.zip"
done

echo "Готово: $(find "$DIST_DIR" -maxdepth 1 -name '*.zip' | wc -l | tr -d ' ') skills"
