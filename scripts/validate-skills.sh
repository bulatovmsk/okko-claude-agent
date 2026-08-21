#!/usr/bin/env bash
# Проверяет все repo-scoped skills валидатором Codex skill-creator.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="${CODEX_SKILLS_DIR:-$ROOT/.agents/skills}"
VALIDATOR="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py"

if [ ! -d "$SKILLS_DIR" ]; then
  echo "Не найдена папка .agents/skills" >&2
  exit 1
fi

python3 "$ROOT/scripts/design_system_knowledge.py" validate
python3 "$ROOT/scripts/design_system_knowledge.py" generate --check

for skill_dir in "$SKILLS_DIR"/*; do
  [ -d "$skill_dir" ] || continue

  if [ -f "$VALIDATOR" ] && python3 -c 'import yaml' >/dev/null 2>&1; then
    python3 "$VALIDATOR" "$skill_dir"
  else
    test -f "$skill_dir/SKILL.md"
    rg -q '^name: [a-z0-9-]+$' "$skill_dir/SKILL.md"
    rg -q '^description: .+' "$skill_dir/SKILL.md"
    echo "Базовая проверка пройдена: $(basename "$skill_dir")"
  fi
done
