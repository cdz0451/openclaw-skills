# free-token Skill — 免费大模型 Token 整合方案

📚 **让大模型使用零成本！**

---

## 快速开始

### 1. 安装
```bash
# 复制配置模板
cp accounts.json.example accounts.json

# 编辑配置，填入你的 API Key
vim accounts.json
```

### 2. 获取免费 API Key

**推荐顺序**（按额度从大到小）：

1. **DeepSeek**（首选，额度最大）
   - 网址：https://platform.deepseek.com
   - 额度：每天几百万 tokens
   - 无需实名

2. **阿里云百炼**（稳定，永久额度）
   - 网址：https://bailian.console.aliyun.com
   - 额度：100 万 tokens 永久
   - 需要实名

3. **OpenRouter**（模型最全）
   - 网址：https://openrouter.ai
   - 额度：每天 50 次免费请求
   - 无需实名

4. **豆包**（字节系）
   - 网址：https://www.doubao.com
   - 额度：每日免费
   - 需要字节账号

5. **Cloudflare AI**（部署友好）
   - 网址：https://dash.cloudflare.com
   - 额度：每天 100 次
   - 无需实名

### 3. 使用命令

```bash
# 检查所有账号额度
/free-token check

# 查看使用状态
/free-token status

# 手动切换账号
/free-token rotate

# 完整配置向导
/free-token setup
```

---

## 配置示例

编辑 `accounts.json`：

```json
{
  "accounts": {
    "deepseek": [
      {
        "name": "我的 DeepSeek 账号",
        "apiKey": "sk-your-actual-key-here",
        "dailyLimit": 5000000
      }
    ],
    "aliyun": [
      {
        "name": "阿里云主账号",
        "apiKey": "sk-your-aliyun-key",
        "remaining": 1000000
      }
    ]
  },
  "currentProvider": "deepseek",
  "autoRotate": true
}
```

---

## 自动化

### 每日额度检查
在 crontab 中添加：
```bash
0 7 * * * python3 /root/.openclaw/workspace/agents/xueer/skills/free-token/scripts/check-quota.py
```

### OpenClaw Hooks
在 `.openclaw/hooks/SessionStart.js` 中添加：
```javascript
// 会话开始时检查额度
const quota = await checkFreeTokenQuota();
if (quota.remainingRatio < 0.2) {
  notify("⚠️ Token 额度低于 20%，建议切换账号");
}
```

---

## 省钱技巧

1. **优先级策略**
   - 日常对话 → DeepSeek
   - 复杂推理 → 阿里云百炼
   - 代码生成 → DeepSeek-Coder
   - 创意写作 → 豆包

2. **多账号轮换**
   - 使用不同邮箱注册
   - 开启自动轮换（低于 20% 自动切换）

3. **配合 Token 压缩**
   - 启用上下文压缩（compaction）
   - 减少无效 Token 消耗

---

## 常见问题

**Q: API Key 哪里获取？**
> 各平台控制台 → API Key 管理 → 创建新 Key

**Q: 额度用完怎么办？**
> 1. 切换到备用账号
> 2. 等待次日刷新
> 3. 注册新账号

**Q: 如何验证配置是否正确？**
> 运行 `/free-token check` 查看各平台状态

---

## 文件结构

```
free-token/
├── skill.md                    # Skill 定义
├── README.md                   # 本文件
├── accounts.json.example       # 配置模板
├── accounts.json               # 你的配置（需自行创建）
├── scripts/
│   └── check-quota.py         # 额度检查脚本
└── quota-report.json          # 检查报告（自动生成）
```

---

## 更新日志

- **2026-03-25 v1.0**: 初始版本
  - 支持 5 大免费平台
  - 额度检查脚本
  - 自动轮换功能

---

## 相关链接

- [Skill 文档](./skill.md)
- [阿里云百炼文档](https://help.aliyun.com/zh/model-studio/)
- [DeepSeek API 文档](https://platform.deepseek.com/api-docs/)
- [OpenRouter 文档](https://openrouter.ai/docs)
- [Token 省钱攻略](../token-saver/)

---

*让 AI 更普惠 🌍*
