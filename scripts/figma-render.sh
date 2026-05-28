#!/usr/bin/env bash
# Запрашивает у Figma рендер ноды (PNG/SVG/PDF), скачивает результат локально.
#
# Usage:
#   bash scripts/figma-render.sh <fileKey> <nodeId> [<scale>] [<format>]
#
# Example:
#   bash scripts/figma-render.sh rMcDm5qGp4CXkXXddEbcMh 28934:239837
#   bash scripts/figma-render.sh rMcDm5qGp4CXkXXddEbcMh 28934:239837 2 png

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ $# -lt 2 ]; then
  echo "Usage: bash scripts/figma-render.sh <fileKey> <nodeId> [<scale=2>] [<format=png>]" >&2
  exit 2
fi

FILE_KEY="$1"
NODE_ID="$2"
SCALE="${3:-2}"
FORMAT="${4:-png}"

OUT_DIR="$ROOT/.figma-cache/$FILE_KEY/renders"
mkdir -p "$OUT_DIR"

safe_id="${NODE_ID//:/-}"
out_file="$OUT_DIR/${safe_id}@${SCALE}x.${FORMAT}"

echo "→ Запрашиваю рендер: $NODE_ID (${FORMAT}, ${SCALE}x)"

# 1) Получаем подписанный URL рендера
RESPONSE="$(bash "$ROOT/scripts/figma-api.sh" "/v1/images/$FILE_KEY?ids=$NODE_ID&format=$FORMAT&scale=$SCALE")"

if ! command -v jq >/dev/null 2>&1; then
  echo "❌ Установи jq: brew install jq" >&2
  exit 1
fi

ERR="$(echo "$RESPONSE" | jq -r '.err // empty')"
if [ -n "$ERR" ]; then
  echo "❌ Figma error: $ERR" >&2
  echo "$RESPONSE" >&2
  exit 1
fi

URL="$(echo "$RESPONSE" | jq -r --arg id "$NODE_ID" '.images[$id] // empty')"

if [ -z "$URL" ] || [ "$URL" = "null" ]; then
  echo "❌ Не получил URL рендера для $NODE_ID" >&2
  echo "$RESPONSE" >&2
  exit 1
fi

# 2) Скачиваем
curl --silent --show-error --fail --output "$out_file" "$URL"
echo "  ✓ $out_file"
