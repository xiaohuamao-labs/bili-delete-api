#!/usr/bin/env bash
# 批量删除示例
set -euo pipefail

BASE="${BILI_API_BASE:-https://api.example.com}"
KEY="${BILI_API_KEY:?请先导出 BILI_API_KEY}"
COOKIE="${BILI_COOKIE:?请先导出 BILI_COOKIE（含 SESSDATA / bili_jct）}"

# 健康检查
curl -s "$BASE/healthz"

# 删除一条
curl -s -X POST "$BASE/v1/delete" \
  -H "X-API-Key: $KEY" \
  -H "Content-Type: application/json" \
  -d "{\"cookie\": \"$COOKIE\", \"aids\": [\"123456789\"]}"

# 批量（一次最多建议 50 条）
curl -s -X POST "$BASE/v1/delete" \
  -H "X-API-Key: $KEY" \
  -H "Content-Type: application/json" \
  -d "{\"cookie\": \"$COOKIE\", \"aids\": [\"123456789\", \"987654321\"]}"
