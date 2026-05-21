#!/usr/bin/env bash
# Синхронизация design-system/ из Figma через MCP / API.
#
# Заглушка: в этой версии не реализован реальный pull из Figma.
# Будет дописан, когда:
#   - подключится Figma MCP (claude.ai Figma)
#   - команда определится, что именно вытаскиваем (только токены, или + компоненты + доку)
#
# Usage (планируемое):
#   bash scripts/sync-from-figma.sh [--tokens] [--components] [--docs]

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cat <<'EOF'
sync-from-figma.sh — заглушка.

Что должно произойти при реализации:
  1. Подключиться к Figma (через MCP или Figma API + token)
  2. Прочитать структуру библиотеки Окко
  3. Сгенерировать/обновить:
       design-system/tokens/*.md       — колор-, тайпо-, спейсинг-, моушн-токены
       design-system/components/*.md   — карточки компонентов
  4. Сохранить snapshot версии ДС и дату sync.

Сейчас ничего не сделано. Заполняй design-system/ вручную из шаблонов:
  design-system/components/_template.md   — шаблон компонента
  design-system/DESIGN_SYSTEM.md          — сводный документ

После заполнения запусти:
  bash scripts/pack-skills.sh
EOF
