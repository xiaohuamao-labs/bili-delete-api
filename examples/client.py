#!/usr/bin/env python3
"""B站稿件删除 API 客户端示例（只依赖 requests）.

用法:
    export BILI_API_KEY=your_key
    python client.py "SESSDATA=...; bili_jct=..." 123456789 [更多 aid...]
"""

import json
import os
import sys

import requests

BASE = os.environ.get("BILI_API_BASE", "https://api.example.com")
KEY = os.environ.get("BILI_API_KEY", "")


def delete(cookie: str, aids: list[str]) -> dict:
    resp = requests.post(
        f"{BASE}/v1/delete",
        headers={"X-API-Key": KEY, "Content-Type": "application/json"},
        json={"cookie": cookie, "aids": aids},
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    cookie, aids = sys.argv[1], sys.argv[2:]
    result = delete(cookie, aids)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
