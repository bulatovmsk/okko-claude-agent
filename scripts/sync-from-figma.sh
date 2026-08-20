#!/usr/bin/env bash
# Staged workflow: fetch → resolve aliases → update source → rebuild skills → report.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HEAD_KEY="HYB1u9ysALVWtVWKoagiDH"
MW_KEY="vztN8doGwBZOCbpDf2PhKR"
TV_KEY="Zn2JrOHhSURjCuUEp6JcI8"

usage() {
  echo "Usage:" >&2
  echo "  bash scripts/sync-from-figma.sh head [colors|icons|illustrations|all] [options]" >&2
  echo "  bash scripts/sync-from-figma.sh tokens [typography|spacing|corner-radius|typography-tv|spacing-tv|corner-radius-tv|all-mw|all-tv|all] [options]" >&2
  echo "  bash scripts/sync-from-figma.sh all [options]" >&2
  echo "" >&2
  echo "Options:" >&2
  echo "  --variables-dir DIR  JSON dumps from Figma MCP or Variables REST API" >&2
  echo "  --report FILE        Markdown report path" >&2
  echo "  --keep-stage         Keep temporary staged files for diagnostics" >&2
}

if [ $# -lt 1 ]; then
  usage
  exit 2
fi

GROUP="$1"
shift
TARGET="all"
if [ $# -gt 0 ] && [[ "$1" != --* ]]; then
  TARGET="$1"
  shift
fi

VARIABLES_DIR="${FIGMA_VARIABLES_DIR:-}"
REPORT_PATH=""
KEEP_STAGE=false
while [ $# -gt 0 ]; do
  case "$1" in
    --variables-dir)
      [ $# -ge 2 ] || { usage; exit 2; }
      VARIABLES_DIR="$2"
      shift 2
      ;;
    --report)
      [ $# -ge 2 ] || { usage; exit 2; }
      REPORT_PATH="$2"
      shift 2
      ;;
    --keep-stage)
      KEEP_STAGE=true
      shift
      ;;
    *)
      echo "Неизвестная опция: $1" >&2
      usage
      exit 2
      ;;
  esac
done

case "$GROUP:$TARGET" in
  head:colors|head:icons|head:illustrations|head:all) ;;
  tokens:typography|tokens:spacing|tokens:corner-radius|tokens:typography-tv|tokens:spacing-tv|tokens:corner-radius-tv|tokens:all-mw|tokens:all-tv|tokens:all) ;;
  all:all) ;;
  *) usage; exit 2 ;;
esac

RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"
if [ -z "$REPORT_PATH" ]; then
  REPORT_PATH="$ROOT/.figma-cache/reports/$RUN_ID.md"
elif [[ "$REPORT_PATH" != /* ]]; then
  REPORT_PATH="$ROOT/$REPORT_PATH"
fi

STAGE="$(mktemp -d "${TMPDIR:-/tmp}/okko-figma-sync.XXXXXX")"
BEFORE="$STAGE/before"
WORK="$STAGE/work"
mkdir -p "$BEFORE" "$WORK" "$STAGE/variables"
cp -R "$ROOT/design-system" "$BEFORE/design-system"
cp -R "$ROOT/.agents/skills" "$BEFORE/skills"
cp -R "$ROOT/design-system" "$WORK/design-system"
cp -R "$ROOT/.agents/skills" "$WORK/skills"

cleanup() {
  if [ "$KEEP_STAGE" = true ]; then
    echo "Staged-файлы сохранены: $STAGE"
  else
    rm -rf "$STAGE"
  fi
}
trap cleanup EXIT

VARIABLE_SOURCES=("")

make_report() {
  local status="$1"
  local message="$2"
  local after_source="$3"
  local after_skills="$4"
  local args=(
    --before-source "$BEFORE/design-system"
    --after-source "$after_source"
    --before-skills "$BEFORE/skills"
    --after-skills "$after_skills"
    --status "$status"
    --group "$GROUP"
    --target "$TARGET"
    --message "$message"
    --output "$REPORT_PATH"
  )
  local source
  for source in "${VARIABLE_SOURCES[@]}"; do
    if [ -n "$source" ]; then
      args+=(--variables-source "$source")
    fi
  done
  python3 "$ROOT/scripts/figma_sync_report.py" "${args[@]}" >/dev/null
  echo "Отчёт: $REPORT_PATH"
}

has_figma_token() {
  [ -f "$ROOT/.env" ] || return 1
  (
    set -a
    # shellcheck disable=SC1091
    source "$ROOT/.env"
    set +a
    [ -n "${FIGMA_TOKEN:-}" ]
  )
}

needs_rest=false
case "$GROUP:$TARGET" in
  head:*|all:all|tokens:typography|tokens:typography-tv|tokens:all-mw|tokens:all-tv|tokens:all) needs_rest=true ;;
esac

if [ "$needs_rest" = true ] && ! has_figma_token; then
  make_report blocked "Не найден локальный FIGMA_TOKEN, необходимый для выбранных REST-источников. Staged-изменения не применялись." "$WORK/design-system" "$WORK/skills"
  exit 1
fi

find_variable_dump() {
  local key="$1"
  local alias="$2"
  local candidate
  if [ -n "$VARIABLES_DIR" ]; then
    for candidate in "$VARIABLES_DIR/$key.json" "$VARIABLES_DIR/$alias.json"; do
      if [ -f "$candidate" ] && python3 -m json.tool "$candidate" >/dev/null 2>&1; then
        echo "$candidate"
        return 0
      fi
    done
  fi

  if has_figma_token; then
    candidate="$STAGE/variables/$key.json"
    if bash "$ROOT/scripts/figma-api.sh" "/v1/files/$key/variables/local" > "$candidate" 2>/dev/null; then
      echo "$candidate"
      return 0
    fi
    rm -f "$candidate"
  fi
  return 1
}

HEAD_VARIABLES=""
MW_VARIABLES=""
TV_VARIABLES=""

need_head_variables=false
need_mw_variables=false
need_tv_variables=false
case "$GROUP:$TARGET" in
  head:colors|head:all|all:all) need_head_variables=true ;;
esac
case "$GROUP:$TARGET" in
  tokens:spacing|tokens:corner-radius|tokens:all-mw|tokens:all|all:all) need_mw_variables=true ;;
esac
case "$GROUP:$TARGET" in
  tokens:spacing-tv|tokens:corner-radius-tv|tokens:all-tv|tokens:all|all:all) need_tv_variables=true ;;
esac

if [ "$need_head_variables" = true ]; then
  if ! HEAD_VARIABLES="$(find_variable_dump "$HEAD_KEY" head)"; then
    make_report blocked "Не получен variable dump Head Library. Передай его через --variables-dir; source не обновлён." "$WORK/design-system" "$WORK/skills"
    exit 1
  fi
  VARIABLE_SOURCES+=("$HEAD_VARIABLES")
fi
if [ "$need_mw_variables" = true ]; then
  if ! MW_VARIABLES="$(find_variable_dump "$MW_KEY" mobile-web)"; then
    make_report blocked "Не получен variable dump Tokens mobile/web. Передай его через --variables-dir; source не обновлён." "$WORK/design-system" "$WORK/skills"
    exit 1
  fi
  VARIABLE_SOURCES+=("$MW_VARIABLES")
fi
if [ "$need_tv_variables" = true ]; then
  if ! TV_VARIABLES="$(find_variable_dump "$TV_KEY" tv)"; then
    make_report blocked "Не получен variable dump Tokens TV. Передай его через --variables-dir; source не обновлён." "$WORK/design-system" "$WORK/skills"
    exit 1
  fi
  VARIABLE_SOURCES+=("$TV_VARIABLES")
fi

run_fetch() {
  case "$GROUP" in
    head)
      FIGMA_SYNC_DEFER_ALIASES=true FIGMA_SYNC_DESIGN_SYSTEM_DIR="$WORK/design-system" bash "$ROOT/scripts/figma-sync-head-library.sh" "$TARGET" || return 1
      ;;
    tokens)
      FIGMA_SYNC_DEFER_ALIASES=true FIGMA_SYNC_DESIGN_SYSTEM_DIR="$WORK/design-system" bash "$ROOT/scripts/figma-sync-tokens.sh" "$TARGET" || return 1
      ;;
    all)
      FIGMA_SYNC_DEFER_ALIASES=true FIGMA_SYNC_DESIGN_SYSTEM_DIR="$WORK/design-system" bash "$ROOT/scripts/figma-sync-head-library.sh" all || return 1
      FIGMA_SYNC_DEFER_ALIASES=true FIGMA_SYNC_DESIGN_SYSTEM_DIR="$WORK/design-system" bash "$ROOT/scripts/figma-sync-tokens.sh" all || return 1
      ;;
  esac
}

if ! run_fetch; then
  make_report failed "Получение или преобразование Figma-данных завершилось ошибкой. Staged-изменения не применялись." "$WORK/design-system" "$WORK/skills"
  exit 1
fi

apply_variables() {
  local target="$1"
  local input="$2"
  python3 "$ROOT/scripts/figma_variables.py" --input "$input" --design-system-dir "$WORK/design-system" --target "$target"
}

resolve_all_variables() {
  case "$GROUP:$TARGET" in
    head:colors|head:all|all:all) apply_variables colors "$HEAD_VARIABLES" || return 1 ;;
  esac
  case "$GROUP:$TARGET" in
    tokens:spacing) apply_variables spacing "$MW_VARIABLES" || return 1 ;;
    tokens:corner-radius) apply_variables corner-radius "$MW_VARIABLES" || return 1 ;;
    tokens:all-mw|tokens:all|all:all)
      apply_variables spacing "$MW_VARIABLES" || return 1
      apply_variables corner-radius "$MW_VARIABLES" || return 1
      ;;
  esac
  case "$GROUP:$TARGET" in
    tokens:spacing-tv) apply_variables spacing-tv "$TV_VARIABLES" || return 1 ;;
    tokens:corner-radius-tv) apply_variables corner-radius-tv "$TV_VARIABLES" || return 1 ;;
    tokens:all-tv|tokens:all|all:all)
      apply_variables spacing-tv "$TV_VARIABLES" || return 1
      apply_variables corner-radius-tv "$TV_VARIABLES" || return 1
      ;;
  esac
}

if ! resolve_all_variables; then
  make_report failed "Не удалось разрешить aliases или сформировать token-таблицы. Staged-изменения не применялись." "$WORK/design-system" "$WORK/skills"
  exit 1
fi

if rg -n '<!--[[:space:]]*VARDEFS_FROM_(MCP|PLUGIN_API)' "$WORK/design-system" >/dev/null; then
  make_report blocked "После разрешения aliases остались незаполненные маркеры. Staged-изменения не применялись." "$WORK/design-system" "$WORK/skills"
  exit 1
fi

if ! DESIGN_SYSTEM_DIR="$WORK/design-system" CODEX_SKILLS_DIR="$WORK/skills" bash "$ROOT/scripts/sync-skill-references.sh"; then
  make_report failed "Не удалось пересобрать skill references. Source и skills не обновлены." "$WORK/design-system" "$WORK/skills"
  exit 1
fi
if ! CODEX_SKILLS_DIR="$WORK/skills" bash "$ROOT/scripts/validate-skills.sh"; then
  make_report failed "Валидация staged skills не прошла. Source и skills не обновлены." "$WORK/design-system" "$WORK/skills"
  exit 1
fi

rsync -a --delete "$WORK/design-system/" "$ROOT/design-system/"
rsync -a --delete "$WORK/skills/" "$ROOT/.agents/skills/"

make_report complete "Данные получены, aliases разрешены, source и skill references обновлены и проверены. Run-specific diff записан в отчёт." "$ROOT/design-system" "$ROOT/.agents/skills"
