#!/usr/bin/env bash
# Тонкий wrapper над Figma REST API.
# Подгружает .env и делает GET-запрос с X-Figma-Token.
#
# Usage:
#   bash scripts/figma-api.sh <path-with-leading-slash>
#
# Example:
#   bash scripts/figma-api.sh "/v1/files/$FIGMA_LIB_IOS_KEY/nodes?ids=28934:239837"
#   bash scripts/figma-api.sh "/v1/files/$FIGMA_LIB_IOS_KEY/variables/local"
#   bash scripts/figma-api.sh "/v1/images/$FIGMA_LIB_IOS_KEY?ids=28934:239837&format=png&scale=2"

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT/.env"

if [ ! -f "$ENV_FILE" ]; then
  echo "❌ Не найден $ENV_FILE. Скопируй .env.example в .env и заполни." >&2
  exit 1
fi

# shellcheck disable=SC1090
set -a
source "$ENV_FILE"
set +a

if [ -z "${FIGMA_TOKEN:-}" ]; then
  echo "❌ FIGMA_TOKEN не задан в .env" >&2
  exit 1
fi

if [ $# -lt 1 ]; then
  echo "Usage: bash scripts/figma-api.sh <path-with-leading-slash>" >&2
  echo "Example: bash scripts/figma-api.sh /v1/files/\$FIGMA_LIB_IOS_KEY/nodes?ids=28934:239837" >&2
  exit 2
fi

PATH_ARG="$1"

curl --silent --show-error --fail \
  -H "X-Figma-Token: $FIGMA_TOKEN" \
  "https://api.figma.com${PATH_ARG}"
