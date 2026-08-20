#!/usr/bin/env bash
# Синхронизация токенов из двух файлов:
#   • 🦖 Tokens [mobile & web]  (vztN8doGwBZOCbpDf2PhKR)  → spacing / corner-radius / typography
#   • 🦍 Tokens [tv]            (Zn2JrOHhSURjCuUEp6JcI8)  → spacing-tv / corner-radius-tv / typography-tv
#
# Spacing и corner-radius — NUMBER variables. Скрипт готовит staged-скелеты с маркерами,
# а sync-from-figma.sh заполняет их из Variables REST API или Figma MCP dump,
# детерминированно разрешая alias chains до публикации source.
#
# Usage:
#   bash scripts/figma-sync-tokens.sh                # all (mobile/web + tv)
#   bash scripts/figma-sync-tokens.sh typography
#   bash scripts/figma-sync-tokens.sh spacing
#   bash scripts/figma-sync-tokens.sh corner-radius
#   bash scripts/figma-sync-tokens.sh typography-tv
#   bash scripts/figma-sync-tokens.sh spacing-tv
#   bash scripts/figma-sync-tokens.sh corner-radius-tv
#   bash scripts/figma-sync-tokens.sh all-mw         # только mobile/web
#   bash scripts/figma-sync-tokens.sh all-tv         # только tv

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

TARGET="${1:-all}"
FILE_KEY="vztN8doGwBZOCbpDf2PhKR"
TV_FILE_KEY="Zn2JrOHhSURjCuUEp6JcI8"
DESIGN_SYSTEM_DIR="${FIGMA_SYNC_DESIGN_SYSTEM_DIR:-$ROOT/design-system}"

needs_rest=false
case "$TARGET" in
  typography|typography-tv|all-mw|all-tv|all) needs_rest=true ;;
esac

if [ "$needs_rest" = true ]; then
  if [ ! -f "$ROOT/.env" ]; then echo "❌ нет .env (нужен FIGMA_TOKEN для typography)"; exit 1; fi
  set -a; source "$ROOT/.env"; set +a
  if [ -z "${FIGMA_TOKEN:-}" ]; then echo "❌ FIGMA_TOKEN не задан"; exit 1; fi
fi

CACHE="$ROOT/.figma-cache/tokens-sync"
CACHE_TV="$ROOT/.figma-cache/tokens-tv-sync"
mkdir -p "$CACHE" "$CACHE_TV"

# ── mobile & web ──────────────────────────────────────────

sync_typography() {
  echo "→ Синхронизирую typography (mobile/web)…"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/styles" > "$CACHE/styles.json"
  python3 "$ROOT/scripts/_figma_sync_lib.py" typography_fetch "$CACHE"
  python3 "$ROOT/scripts/_figma_sync_lib.py" typography "$CACHE" "$DESIGN_SYSTEM_DIR/tokens/typography.md"
  echo "  ✓ $DESIGN_SYSTEM_DIR/tokens/typography.md"
}

sync_spacing() {
  echo "→ Синхронизирую spacing (mobile/web)…"
  python3 "$ROOT/scripts/_figma_sync_lib.py" spacing "$CACHE" "$DESIGN_SYSTEM_DIR/tokens/spacing.md"
  echo "  ✓ $DESIGN_SYSTEM_DIR/tokens/spacing.md"
}

sync_corner_radius() {
  echo "→ Синхронизирую corner-radius (mobile/web)…"
  python3 "$ROOT/scripts/_figma_sync_lib.py" corner_radius "$CACHE" "$DESIGN_SYSTEM_DIR/tokens/corner-radius.md"
  echo "  ✓ $DESIGN_SYSTEM_DIR/tokens/corner-radius.md"
}

# ── tv ────────────────────────────────────────────────────

sync_typography_tv() {
  echo "→ Синхронизирую typography (tv)…"
  bash "$ROOT/scripts/figma-api.sh" "/v1/files/$TV_FILE_KEY/styles" > "$CACHE_TV/styles.json"
  python3 "$ROOT/scripts/_figma_sync_lib.py" typography_tv_fetch "$CACHE_TV"
  python3 "$ROOT/scripts/_figma_sync_lib.py" typography_tv "$CACHE_TV" "$DESIGN_SYSTEM_DIR/tokens/typography-tv.md"
  echo "  ✓ $DESIGN_SYSTEM_DIR/tokens/typography-tv.md"
}

sync_spacing_tv() {
  echo "→ Синхронизирую spacing (tv)…"
  python3 "$ROOT/scripts/_figma_sync_lib.py" spacing_tv "$CACHE_TV" "$DESIGN_SYSTEM_DIR/tokens/spacing-tv.md"
  echo "  ✓ $DESIGN_SYSTEM_DIR/tokens/spacing-tv.md"
}

sync_corner_radius_tv() {
  echo "→ Синхронизирую corner-radius (tv)…"
  python3 "$ROOT/scripts/_figma_sync_lib.py" corner_radius_tv "$CACHE_TV" "$DESIGN_SYSTEM_DIR/tokens/corner-radius-tv.md"
  echo "  ✓ $DESIGN_SYSTEM_DIR/tokens/corner-radius-tv.md"
}

case "$TARGET" in
  typography)         sync_typography ;;
  spacing)            sync_spacing ;;
  corner-radius)      sync_corner_radius ;;
  typography-tv)      sync_typography_tv ;;
  spacing-tv)         sync_spacing_tv ;;
  corner-radius-tv)   sync_corner_radius_tv ;;
  all-mw)             sync_typography; sync_spacing; sync_corner_radius ;;
  all-tv)             sync_typography_tv; sync_spacing_tv; sync_corner_radius_tv ;;
  all)                sync_typography; sync_spacing; sync_corner_radius; \
                      sync_typography_tv; sync_spacing_tv; sync_corner_radius_tv ;;
  *) echo "Usage: $0 [typography|spacing|corner-radius|typography-tv|spacing-tv|corner-radius-tv|all|all-mw|all-tv]" >&2; exit 2 ;;
esac

if [ -z "${FIGMA_SYNC_DESIGN_SYSTEM_DIR:-}" ]; then
  echo ""
  echo "─── diff ──────────────────────────────────────────────"
  git --no-pager diff --stat -- design-system/tokens/ 2>/dev/null || true
  echo "───────────────────────────────────────────────────────"
fi

if [ "${FIGMA_SYNC_DEFER_ALIASES:-false}" != true ] && grep -lq 'VARDEFS_FROM_PLUGIN_API' "$DESIGN_SYSTEM_DIR/tokens/"*.md 2>/dev/null; then
  echo ""
  echo "⚠  Есть маркеры VARDEFS_FROM_PLUGIN_API — NUMBER-переменные нужно вписать через use_figma + Plugin API."
  echo "   fileKey mobile/web = '$FILE_KEY' · fileKey tv = '$TV_FILE_KEY' · коллекции FLOAT-переменных."
fi
