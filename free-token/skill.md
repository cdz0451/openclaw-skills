# free-token — 免费大模型 Token 整合方案

**版本**: 1.0  
**作者**: 学而  
**创建日期**: 2026-03-25  
**分类**: 工具类 / 成本优化

---

## 核心功能

一键获取和配置所有免费大模型 Token 渠道，实现"零成本"使用主流大模型。整合阿里云、DeepSeek、豆包、OpenRouter 等平台的免费额度，支持多账号轮换和自动监控。

---

## 使用方式

### 命令触发
```bash
/free-token              # 查看所有免费渠道和剩余额度
/free-token setup        # 交互式配置向导
/free-token check        # 检查各平台剩余额度
/free-token rotate       # 手动切换到下一个账号
/free-token status       # 查看当前使用的账号和平台
```

### Hooks 自动触发
- **SessionStart**: 检查当前账号额度，低于阈值时提醒切换
- **Daily (07:00)**: 自动刷新每日免费额度（DeepSeek 等）
- **PreRequest**: 请求前自动选择最优平台（基于额度+延迟）

---

## 免费渠道总览

| 平台 | 免费额度 | 有效期 | 是否需要实名 | 支持模型 |
|------|----------|--------|--------------|----------|
| **阿里云百炼** | 100 万 tokens | 永久 | ✅ | 通义千问全系 |
| **DeepSeek** | 每天几百万 tokens | 每日刷新 | ❌ | DeepSeek-V3/R1 |
| **豆包 (字节)** | 每天免费额度 | 每日刷新 | ✅ | 豆包/ Doubao-Pro |
| **OpenRouter** | 每天 50 次 | 每日刷新 | ❌ | 全平台模型 |
| **腾讯云混元** | 新用户额度 | 限时 | ✅ | 混元全系 |
| **Cloudflare AI** | 每天 100 次 | 每日刷新 | ❌ | 多模型 |

---

## 配置步骤

### 1. 阿里云百炼（推荐首选）

**领取步骤**:
1. 访问 https://bailian.console.aliyun.com
2. 注册阿里云账号并完成实名认证
3. 进入「模型广场」→ 选择任意模型
4. 点击「免费试用」激活 100 万 tokens 额度

**API 配置**:
```bash
# 获取 API Key
# 控制台 → API Key 管理 → 创建新 Key

# 测试调用
from dashscope import Generation
response = Generation.call(
    model='qwen-plus',
    messages=[{'role': 'user', 'content': 'Hello'}]
)
print(response.output.text)
```

**配置到 OpenClaw**:
```json
{
  "model": "dashscope/qwen-plus",
  "apiKey": "sk-xxxxxxxx"
}
```

---

### 2. DeepSeek（额度最大）

**领取步骤**:
1. 访问 https://platform.deepseek.com
2. 注册账号（无需实名）
3. 新用户自动获得免费额度
4. 每日免费额度自动刷新

**API 配置**:
```bash
# API Base: https://api.deepseek.com
# API Key: 控制台获取

# 测试调用
curl https://api.deepseek.com/v1/chat/completions \
  -H "Authorization: Bearer sk-xxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**配置到 OpenClaw**:
```json
{
  "model": "deepseek/deepseek-chat",
  "apiKey": "sk-xxxxxxxx",
  "baseUrl": "https://api.deepseek.com"
}
```

---

### 3. 豆包（字节）

**领取步骤**:
1. 访问 https://www.doubao.com
2. 登录字节系账号（抖音/头条）
3. 进入开发者平台领取免费额度

**配置到 OpenClaw**:
```json
{
  "model": "volcengine/doubao-pro-4k",
  "apiKey": "xxxxxxxx"
}
```

---

### 4. OpenRouter（模型最全）

**领取步骤**:
1. 访问 https://openrouter.ai
2. 注册账号（无需实名）
3. 新用户每天免费 50 次请求
4. 充值 10 credits 后解锁每天 1000 次

**API 配置**:
```bash
# API Base: https://openrouter.ai/api/v1
# 兼容 OpenAI 格式

curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer sk-or-xxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/llama-3-70b-instruct",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**配置到 OpenClaw**:
```json
{
  "model": "openrouter/meta-llama/llama-3-70b-instruct",
  "apiKey": "sk-or-xxxxxxxx",
  "baseUrl": "https://openrouter.ai/api/v1"
}
```

---

### 5. Cloudflare AI（零成本部署）

**领取步骤**:
1. 注册 Cloudflare 账号
2. 开通 Workers AI（免费额度每天 100 次）
3. 创建 API Token

**配置到 OpenClaw**:
```json
{
  "model": "cloudflare/@cf/meta/llama-3-8b-instruct",
  "apiKey": "xxxxxxxx",
  "accountId": "your-account-id"
}
```

---

## 多账号轮换策略

### 账号池配置
```json
{
  "accounts": {
    "aliyun": [
      {"name": "主账号", "apiKey": "sk-xxx", "remaining": 850000},
      {"name": "备用 1", "apiKey": "sk-xxx", "remaining": 920000}
    ],
    "deepseek": [
      {"name": "主账号", "apiKey": "sk-xxx", "dailyLimit": 5000000},
      {"name": "备用 1", "apiKey": "sk-xxx", "dailyLimit": 5000000}
    ],
    "openrouter": [
      {"name": "主账号", "apiKey": "sk-or-xxx", "dailyRequests": 50}
    ]
  },
  "currentProvider": "deepseek",
  "currentAccount": 0,
  "autoRotate": true,
  "rotateThreshold": 0.1
}
```

### 自动切换逻辑
```python
# 伪代码：额度检查 + 自动切换
def check_and_rotate():
    current = get_current_account()
    remaining_ratio = current.remaining / current.limit
    
    if remaining_ratio < 0.1:  # 低于 10% 自动切换
        next_account = get_next_account()
        switch_to(next_account)
        notify("已自动切换到新账号")
```

---

## 监控与告警

### 额度监控脚本
```python
#!/usr/bin/env python3
# scripts/check-quota.py

import requests
import json

PLATFORMS = {
    "aliyun": {
        "url": "https://bailian.console.aliyun.com/api/quota",
        "headers": {"Authorization": "Bearer {api_key}"}
    },
    "deepseek": {
        "url": "https://api.deepseek.com/user/status",
        "headers": {"Authorization": "Bearer {api_key}"}
    },
    "openrouter": {
        "url": "https://openrouter.ai/api/v1/auth/key",
        "headers": {"Authorization": "Bearer {api_key}"}
    }
}

def check_all_accounts():
    results = {}
    for platform, config in PLATFORMS.items():
        for account in get_accounts(platform):
            try:
                response = requests.get(
                    config["url"],
                    headers={"Authorization": config["headers"]["Authorization"].format(api_key=account["apiKey"])}
                )
                quota = parse_quota(response.json())
                results[f"{platform}:{account['name']}"] = quota
            except Exception as e:
                results[f"{platform}:{account['name']}"] = {"error": str(e)}
    
    save_results(results)
    return results

if __name__ == "__main__":
    check_all_accounts()
```

### 告警阈值
- 🟢 **> 50%**: 正常
- 🟡 **20-50%**: 提醒
- 🔴 **< 20%**: 告警，建议切换
- ⚠️ **< 5%**: 紧急，自动切换

---

## 最佳实践

### 1. 优先级策略
```
日常对话 → DeepSeek（额度最大）
复杂推理 → 阿里云百炼（qwen-max）
代码生成 → DeepSeek-Coder 或 OpenRouter
创意写作 → 豆包 或 OpenRouter
```

### 2. 成本优化组合
```
主用：DeepSeek（免费额度最大）
备用：阿里云百炼（100 万永久）
补充：OpenRouter（模型最全）
应急：豆包/Cloudflare
```

### 3. 账号管理技巧
- 使用不同邮箱注册多个账号
- 手机号接码平台可用于验证
- 定期清理未使用账号
- 记录每个账号的注册日期（便于续费）

---

## 故障排查

### 常见问题

**Q: API Key 无效？**
```
A: 检查：
   1. Key 是否正确复制（无空格）
   2. 账号是否完成实名认证
   3. 免费额度是否已激活
   4. API 调用格式是否正确
```

**Q: 额度用完怎么办？**
```
A: 
   1. 切换到备用账号
   2. 等待次日刷新（DeepSeek/OpenRouter）
   3. 注册新账号
   4. 考虑付费（阿里云约¥0.008/1K tokens）
```

**Q: 如何最大化免费额度？**
```
A:
   1. 多平台分散使用
   2. 多账号轮换
   3. 优先使用每日刷新的平台
   4. 开启 Token 压缩（参考 token-saver skill）
```

---

## 扩展阅读

- [阿里云百炼文档](https://help.aliyun.com/zh/model-studio/)
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs/)
- [OpenRouter 文档](https://openrouter.ai/docs)
- [Token 省钱攻略](../token-saver/)

---

## 更新日志

- **2026-03-25 v1.0**: 初始版本，整合 5 大免费平台
- TODO: 添加自动注册脚本
- TODO: 添加额度监控 Dashboard
- TODO: 支持更多平台（智谱、MiniMax 等）

---

*本 Skill 遵循"合法合规使用"原则，请勿滥用免费额度。*
