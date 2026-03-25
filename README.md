# 🦀 OpenClaw Skills 合集 — 零成本 AI 工具包

> **让 AI 更普惠，让隐私更安全**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Release](https://img.shields.io/badge/release-v1.0-green.svg)](https://github.com/xueer/openclaw-skills)

---

## 📦 合集内容

本合集包含两个实用 Skill，解决 AI 使用的两大核心问题：

| Skill | 功能 | 适用场景 |
|-------|------|----------|
| 🆓 **free-token** | 免费大模型 Token 整合 | 零成本使用 DeepSeek/阿里云/OpenRouter 等主流模型 |
| 📧 **cloudflare-email-setup** | 免费自定义域名邮箱 | 隐私注册、专业形象、多账号管理 |

---

## 🚀 快速安装

### 方式一：一键安装（推荐）

```bash
# 克隆技能仓库
git clone https://github.com/xueer/openclaw-skills.git ~/.openclaw/workspace/agents/xueer/skills-release

# 运行安装脚本
cd ~/.openclaw/workspace/agents/xueer/skills-release
./install.sh
```

### 方式二：手动安装

```bash
# 复制技能到 OpenClaw 目录
cp -r free-token ~/.openclaw/workspace/agents/xueer/skills/
cp -r cloudflare-email-setup ~/.openclaw/workspace/agents/xueer/skills/
```

### 方式三：通过 OpenClaw 市场

```bash
# 在 OpenClaw 中运行
/plugin marketplace add xueer/openclaw-skills
/plugin install free-token
/plugin install cloudflare-email-setup
```

---

## 📖 使用指南

### Skill 1: free-token — 免费大模型 Token

**解决什么问题？**
- 大模型 API 太贵，用不起
- 不知道有哪些免费渠道
- 多个账号管理麻烦

**核心功能：**
```bash
/free-token              # 查看所有免费渠道和剩余额度
/free-token setup        # 交互式配置向导
/free-token check        # 检查各平台剩余额度
/free-token rotate       # 手动切换到下一个账号
/free-token status       # 查看当前使用的账号和平台
```

**免费额度总览：**

| 平台 | 免费额度 | 推荐度 |
|------|----------|--------|
| DeepSeek | 每天几百万 tokens | ⭐⭐⭐⭐⭐ |
| 阿里云百炼 | 100 万 tokens 永久 | ⭐⭐⭐⭐⭐ |
| OpenRouter | 每天 50 次请求 | ⭐⭐⭐⭐ |
| 豆包 | 每日免费额度 | ⭐⭐⭐⭐ |
| Cloudflare AI | 每天 100 次 | ⭐⭐⭐ |

**快速配置：**
```bash
# 1. 复制配置模板
cd ~/.openclaw/workspace/agents/xueer/skills/free-token
cp accounts.json.example accounts.json

# 2. 编辑配置，填入 API Key
vim accounts.json

# 3. 获取免费 API Key
# DeepSeek: https://platform.deepseek.com
# 阿里云：https://bailian.console.aliyun.com
# OpenRouter: https://openrouter.ai

# 4. 测试配置
python3 scripts/check-quota.py
```

**详细文档：** [free-token/README.md](./free-token/README.md)

---

### Skill 2: cloudflare-email-setup — 免费自定义域名邮箱

**解决什么问题？**
- 注册账号不想用个人邮箱
- 想要专业形象的商务邮箱
- 需要多账号管理但怕麻烦
- 担心隐私泄露

**核心功能：**
```bash
/cf-email setup              # 交互式配置向导
/cf-email add <域名>         # 添加新域名邮箱转发
/cf-email list               # 查看所有已配置的域名
/cf-email status <域名>      # 查看某个域名的转发状态
/cf-email test <邮箱>        # 发送测试邮件
/cf-email remove <域名>      # 移除域名配置
```

**免费域名渠道：**

| 渠道 | 免费期限 | 推荐度 | 链接 |
|------|----------|--------|------|
| EU.org | 永久 | ⭐⭐⭐⭐⭐ | https://nic.eu.org |
| Freenom | 1 年 | ⭐⭐⭐ | https://www.freenom.com |
| PP.UA | 1 年 | ⭐⭐⭐ | https://nic.ua |

**快速配置：**
```bash
# 1. 运行配置向导
/cf-email setup

# 2. 输入域名（没有就先注册免费的）
# EU.org: https://nic.eu.org (永久)
# Freenom: https://www.freenom.com (1 年)

# 3. 输入目标邮箱（Gmail/QQ/Outlook）

# 4. 自动完成 DNS 配置

# 5. 等待 DNS 传播（最多 24 小时）

# 6. 验证配置
/cf-email status yourdomain.com
```

**使用场景：**
- **专业形象** → `admin@yourdomain.com`
- **隐私保护** → `signup@yourdomain.com`
- **多账号管理** → `work@` / `personal@` / `shopping@`
- **临时用途** → `temp-20260326@yourdomain.com`

**详细文档：** [cloudflare-email-setup/README.md](./cloudflare-email-setup/README.md)

---

## 🔧 依赖要求

- OpenClaw v1.0+
- Python 3.8+
- 以下 Python 库（check-quota.py 需要）：
  ```bash
  pip install requests dnspython
  ```

---

## 📁 文件结构

```
openclaw-skills/
├── README.md                           # 本文件
├── install.sh                          # 安装脚本
├── LICENSE                             # MIT 许可证
├── free-token/                         # 免费 Token Skill
│   ├── skill.md                        # Skill 定义
│   ├── README.md                       # 使用指南
│   ├── accounts.json.example           # 配置模板
│   └── scripts/
│       └── check-quota.py             # 额度检查脚本
└── cloudflare-email-setup/             # 邮箱转发 Skill
    ├── skill.md                        # Skill 定义
    ├── README.md                       # 使用指南
    └── scripts/
        └── check-dns.py               # DNS 配置检查
```

---

## 💡 最佳实践

### 1. 配合使用效果更佳

```
注册 AI 账号流程：
1. 用 cloudflare-email-setup 创建临时邮箱
   → temp-ai@yourdomain.com

2. 用这个邮箱注册 DeepSeek/阿里云/OpenRouter

3. 用 free-token 管理所有免费 Token

4. 零成本使用大模型！
```

### 2. 安全建议

- ✅ 不要在公开场合暴露自定义域名邮箱
- ✅ 定期查看 Cloudflare Analytics 监控异常
- ✅ 重要账号使用专用前缀（如：banking@）
- ✅ 免费 Token 账号分散注册，避免封号风险

### 3. 多账号管理

```bash
# Token 账号轮换
/free-token rotate

# 邮箱别名管理
/cf-email add temp-shopping@yourdomain.com
/cf-email list
```

---

## 🐛 故障排查

### free-token 常见问题

**Q: API Key 无效？**
```
A: 检查：
   1. Key 是否正确复制（无空格）
   2. 账号是否完成实名认证
   3. 免费额度是否已激活
   4. 运行 /free-token check 查看状态
```

**Q: 额度用完怎么办？**
```
A: 
   1. 切换到备用账号：/free-token rotate
   2. 等待次日刷新（DeepSeek/OpenRouter）
   3. 注册新账号
```

### cloudflare-email-setup 常见问题

**Q: 收不到转发邮件？**
```
A: 
   1. 检查 DNS 配置：/cf-email dns-check yourdomain.com
   2. 查看垃圾邮件文件夹
   3. 确认目标邮箱已验证
   4. 检查 Cloudflare Analytics
```

**Q: 免费域名被回收？**
```
A: 
   - Freenom 需要每年手动续期
   - 设置提醒：/cf-email reminder add yourdomain.tk 30
   - 或改用 EU.org（永久免费）
```

---

## 📝 更新日志

### v1.0 (2026-03-26)
- 🆕 初始版本发布
- 🆕 free-token Skill：整合 5 大免费大模型平台
- 🆕 cloudflare-email-setup Skill：Cloudflare 邮箱转发自动化
- 🆕 配套脚本：额度检查、DNS 验证

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](./LICENSE) 文件了解详情。

---

## 🙏 致谢

- [OpenClaw](https://openclaw.ai) - 强大的 AI 智能体框架
- [Anthropic](https://anthropic.com) - Skills 设计理念启发
- [ECC](https://github.com/affaan-m/everything-claude-code) - 工程实践参考
- [Cloudflare](https://cloudflare.com) - 免费邮箱转发服务
- [DeepSeek](https://deepseek.com) - 免费大模型额度
- [阿里云](https://aliyun.com) - 百炼平台免费 Token

---

## 📬 联系方式

- **作者**: 学而 (@xueer)
- **项目主页**: https://github.com/xueer/openclaw-skills
- **问题反馈**: https://github.com/xueer/openclaw-skills/issues

---

*让 AI 更普惠 🌍 | 让隐私更安全 🔐*
