#!/usr/bin/env bash
# Синхронизация токенов mobile/web из файла "🦖 Tokens [mobile & web]" (vztN8doGwBZOCbpDf2PhKR).
#
# Что обновляет:
#   spacing       → design-system/tokens/spacing.md          (NUMBER vars, через Plugin API)
#   corner-radius → design-system/tokens/corner-radius.md    (NUMBER vars, через Plugin API)
#   typography    → design-system/tokens/typography.md       (TEXT styles, через REST)
#   all           → всё подряд (default)
#
# Spacing и corner-radius — это NUMBER variables, REST их не отдаёт (403). Сам скрипт
# подготавливает скелет файлов и оставляет маркеры VARDEFS_FROM_PLUGIN_API, которые
# скил `design-figma-libraries` заполняет через use_figma (figma.variables.*) и temp TEXT-узел.
#
# Usage:
#   bash scripts/figma-sync-tokens.sh                # all
#   bash scripts/figma-sync-tokens.sh typography
#   bash scripts/figma-sync-tokens.sh spacing
#   bash scripts/figma-sync-tokens.sh corner-radius

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

TARGET="${1:-all}"
FILE_KEY="vztN8doGwBZOCbpDf2PhKR"

if [ ! -f "$ROOT/.env" ]; then echo "❌ нет .env (нужен FIGMA_TOKEN)"; exit 1; fi
set -a; source "$ROOT/.env"; set +a
if [ -z "${FIGMA_TOKEN:-}" ]; then echo "❌ FIGMA_TOKEN не задан"; exit 1; fi

CACHE="$ROOT/.figma-cache/tokens-sync"
mkdir -p "$CACHE"

sync_typography() {
  echo "→ Синхронизирую typography…"
  echo "  • /styles"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/styles" > "$CACHE/styles.json"
  # дозапрос нод стилей (пачкой)
  python3 "$ROOT/scripts/_figma_sync_lib.py" typography_fetch "$CACHE"
  # парсинг + генерация md
  python3 "$ROOT/scripts/_figma_sync_lib.py" typography "$CACHE" "$ROOT/design-system/tokens/typography.md"
  echo "  ✓ design-system/tokens/typography.md"
}

sync_spacing() {
  echo "→ Синхронизирую spacing…"
  echo "  • node 2280:155798 (Spacing page)"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/nodes?ids=2280:155798&depth=4" > "$CACHE/spacing.json"
  python3 "$ROOT/scripts/_figma_sync_lib.py" spacing "$CACHE" "$ROOT/design-system/tokens/spacing.md"
  echo "  ✓ design-system/tokens/spacing.md"
}

sync_corner_radius() {
  echo "→ Синхронизирую corner-radius…"
  echo "  • node 2287:157374 (Corner-radius page)"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/nodes?ids=2287:157374&depth=4" > "$CACHE/corner-radius.json"
  python3 "$ROOT/scripts/_figma_sync_lib.py" corner_radius "$CACHE" "$ROOT/design-system/tokens/corner-radius.md"
  echo "  ✓ design-system/tokens/corner-radius.md"
}

case "$TARGET" in
  typography)      sync_typography ;;
  spacing)         sync_spacing ;;
  corner-radius)   sync_corner_radius ;;
  all)             sync_typography; sync_spacing; sync_corner_radius ;;
  *) echo "Usage: $0 [typography|spacing|corner-radius|all]" >&2; exit 2 ;;
esac

echo ""
echo "─── diff ──────────────────────────────────────────────"
git --no-pager diff --stat -- design-system/tokens/ 2>/dev/null || true
echo "───────────────────────────────────────────────────────"

if grep -lq 'VARDEFS_FROM_PLUGIN_API' "$ROOT/design-system/tokens/"*.md 2>/dev/null; then
  echo ""
  echo "⚠  Есть маркеры VARDEFS_FROM_PLUGIN_API — NUMBER-переменные нужно вписать через use_figma + Plugin API."
  echo "   Параметры: fileKey='$FILE_KEY' · коллекции FLOAT-переменных."
fi
