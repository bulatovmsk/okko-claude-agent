#!/usr/bin/env bash
# Выгружает JSON-структуру одной или нескольких нод из Figma в .figma-cache/<fileKey>/<nodeId>.json
#
# Usage:
#   bash scripts/figma-fetch-node.sh <fileKey> <nodeId> [<nodeId> ...]
#
# Example:
#   bash scripts/figma-fetch-node.sh rMcDm5qGp4CXkXXddEbcMh 28934:239837 24233:7754 31214:29705

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ $# -lt 2 ]; then
  echo "Usage: bash scripts/figma-fetch-node.sh <fileKey> <nodeId> [<nodeId> ...]" >&2
  exit 2
fi

FILE_KEY="$1"
shift

# Собираем ids в формате 1:2,3:4,...
IDS="$(IFS=,; echo "$*")"

OUT_DIR="$ROOT/.figma-cache/$FILE_KEY"
mkdir -p "$OUT_DIR"

echo "→ Запрашиваю ноды: $IDS"
RESPONSE_FILE="$OUT_DIR/_response.json"

bash "$ROOT/scripts/figma-api.sh" "/v1/files/$FILE_KEY/nodes?ids=$IDS" > "$RESPONSE_FILE"

# Разносим каждую ноду в отдельный файл
for node_id in "$@"; do
  safe_id="${node_id//:/-}"
  out_file="$OUT_DIR/${safe_id}.json"
  if command -v jq >/dev/null 2>&1; then
    jq --arg id "$node_id" '.nodes[$id]' "$RESPONSE_FILE" > "$out_file"
    echo "  ✓ $out_file"
  else
    # Без jq — просто копируем полный response
    cp "$RESPONSE_FILE" "$out_file"
    echo "  ✓ $out_file (jq не установлен — сохранён полный response)"
  fi
done

echo ""
echo "Готово. Файлы в $OUT_DIR/"
