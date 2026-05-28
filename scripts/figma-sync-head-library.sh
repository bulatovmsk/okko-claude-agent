#!/usr/bin/env bash
# Синхронизация данных Okko Head Library (HYB1u9ysALVWtVWKoagiDH) в design-system/.
#
# Что обновляет:
#   colors        → design-system/tokens/colors.md
#                   - Часть A (Variables): структура primitives/semantic/brand
#                     значения hex semantic-токенов оставляет маркером VARDEFS_FROM_MCP,
#                     которые потом заполняются вызовом MCP get_variable_defs из Claude.
#                   - Часть B (Styles): опубликованные FILL-стили + их стопы
#   icons         → design-system/components/icons.md
#                   Парсит Main Pack (29361:322), переписывает «Категории» и «Полный список».
#                   Раздел «Правила выбора модификатора» НЕ трогает.
#   illustrations → design-system/components/illustrations.md
#                   Парсит 3 ноды и переписывает целиком.
#   all           → всё подряд (default)
#
# Usage:
#   bash scripts/figma-sync-head-library.sh                # all
#   bash scripts/figma-sync-head-library.sh colors
#   bash scripts/figma-sync-head-library.sh icons
#   bash scripts/figma-sync-head-library.sh illustrations

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

TARGET="${1:-all}"
FILE_KEY="HYB1u9ysALVWtVWKoagiDH"

if [ ! -f "$ROOT/.env" ]; then echo "❌ нет .env (нужен FIGMA_TOKEN)"; exit 1; fi
set -a; source "$ROOT/.env"; set +a
if [ -z "${FIGMA_TOKEN:-}" ]; then echo "❌ FIGMA_TOKEN не задан"; exit 1; fi

CACHE="$ROOT/.figma-cache/head-sync"
mkdir -p "$CACHE"

# ──────────────────────────────────────────────────────────────────────
# colors
# ──────────────────────────────────────────────────────────────────────
sync_colors() {
  echo "→ Синхронизирую цвета…"

  echo "  • /styles"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/styles" > "$CACHE/styles.json"

  echo "  • node 32102:23149 (Color Tokens, full depth)"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/nodes?ids=32102:23149" > "$CACHE/palette.json"

  python3 "$ROOT/scripts/_figma_sync_lib.py" colors "$CACHE" "$ROOT/design-system/tokens/colors.md"
  echo "  ✓ design-system/tokens/colors.md"
}

# ──────────────────────────────────────────────────────────────────────
# icons (Main Pack)
# ──────────────────────────────────────────────────────────────────────
sync_icons() {
  echo "→ Синхронизирую иконки Main Pack…"
  echo "  • node 29361:322 (depth=2)"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/nodes?ids=29361:322&depth=2" > "$CACHE/icons.json"
  python3 "$ROOT/scripts/_figma_sync_lib.py" icons "$CACHE" "$ROOT/design-system/components/icons.md"
  echo "  ✓ design-system/components/icons.md (раздел «Правила выбора модификатора» сохранён)"
}

# ──────────────────────────────────────────────────────────────────────
# illustrations
# ──────────────────────────────────────────────────────────────────────
sync_illustrations() {
  echo "→ Синхронизирую иллюстрации…"
  echo "  • nodes 39089:10560, 39101:215, 39104:349 (depth=3)"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/nodes?ids=39089:10560,39101:215,39104:349&depth=3" > "$CACHE/illustrations.json"
  python3 "$ROOT/scripts/_figma_sync_lib.py" illustrations "$CACHE" "$ROOT/design-system/components/illustrations.md"
  echo "  ✓ design-system/components/illustrations.md"
}

case "$TARGET" in
  colors)        sync_colors ;;
  icons)         sync_icons ;;
  illustrations) sync_illustrations ;;
  all)           sync_colors; sync_icons; sync_illustrations ;;
  *) echo "Usage: $0 [colors|icons|illustrations|all]" >&2; exit 2 ;;
esac

echo ""
echo "─── diff ──────────────────────────────────────────────"
git --no-pager diff --stat -- design-system/ 2>/dev/null || true
echo "───────────────────────────────────────────────────────"

if grep -q 'VARDEFS_FROM_MCP' "$ROOT/design-system/tokens/colors.md" 2>/dev/null; then
  echo ""
  echo "⚠  В colors.md есть маркеры VARDEFS_FROM_MCP — resolved hex semantic-токенов нужно вписать через MCP get_variable_defs."
  echo "   Параметры: nodeId='32102:23149' (вся страница Color Tokens), fileKey='$FILE_KEY'."
fi
