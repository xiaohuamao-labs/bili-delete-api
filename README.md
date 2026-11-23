# B站稿件批量删除 API

> by 小玲依 · maintained by [小花猫](https://github.com/xiaohuamao-labs)

B 站创作中心的「删除稿件」被人机验证（极验 v3）挡着，手动一条条点非常痛苦。
本项目提供一个**纯协议、无浏览器**的删除接口：传入登录态和 aid，直接完成验证与删除。

- 不需要开浏览器、不需要模拟点击、不需要人工过滑块
- 服务端纯 API 实现（Python，无 GUI）
- 单条删除约 **1~3 秒**

## 能力

| 接口 | 说明 |
|---|---|
| `POST /v1/validate` | 只完成一次极验验证，返回 `validate`（调试/自测用） |
| `POST /v1/delete` | 删除指定 aid 的稿件（可批量） |
| `GET /healthz` | 健康检查 |

## 快速开始

```bash
curl -X POST https://api.example.com/v1/delete \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "cookie": "SESSDATA=...; bili_jct=...",
    "aids": ["123456789"]
  }'
```

返回：

```json
{
  "ok": true,
  "results": [
    {"aid": "123456789", "code": 0, "message": "0", "elapsed": 1.8}
  ]
}
```

Python 客户端见 [`examples/client.py`](examples/client.py)，cURL 见 [`examples/curl.sh`](examples/curl.sh)。

## 鉴权

所有 `/v1/*` 接口都需要 `X-API-Key`。Key 按接入方单独签发。

## 接入 / 定制

接口不公开注册。需要接入、批量脚本、或定制（多账号、定时任务、结果落库）请联系：

- 微信 / 闲鱼：`luguoxiaohuamao`
- 站点：[zjcx.teai.cc](https://zjcx.teai.cc)

## 免责声明

- 仅用于删除**自己账号**下的稿件，需本人登录态（`SESSDATA`）
- 删除不可逆，调用前请自行确认 `aid`
- 本项目不存储、不转发任何 Cookie；请在可信网络内使用
- 请遵守 B 站用户协议与相关法律法规

---

<sub>Made with 🐾 by 小玲依</sub>
