# 🦀 OpenClaw Skills — Zero-Cost AI Toolkit

> **Making AI Accessible | Privacy Protected**

[English](#english) | [中文](#中文)

---

## 📦 What's Included / 合集内容

**Two essential Skills for AI users:**

| Skill | Purpose | Use Case |
|-------|---------|----------|
| 🆓 **free-token** | Free LLM Token integration | Use DeepSeek/Alibaba/OpenRouter for free |
| 📧 **cloudflare-email-setup** | Custom domain email forwarding | Privacy protection, professional image |

---

## 🚀 Quick Start / 快速开始

### Install / 安装

```bash
# Clone repository / 克隆仓库
git clone https://github.com/cdz0451/openclaw-skills.git

# Run installer / 运行安装脚本
cd openclaw-skills/skills-release
./install.sh
```

### Requirements / 环境要求

- OpenClaw v1.0+
- Python 3.8+
- `pip install requests dnspython`

---

## 📖 Usage / 使用指南

### Skill 1: free-token

**Commands:**
```bash
/free-token              # Check all free quotas
/free-token setup        # Interactive setup wizard
/free-token check        # Check remaining quota
/free-token rotate       # Switch to next account
/free-token status       # Show current account
```

**Free Platforms:**

| Platform | Free Quota | Rating |
|----------|------------|--------|
| DeepSeek | Millions/day | ⭐⭐⭐⭐⭐ |
| Alibaba Bailian | 1M tokens (permanent) | ⭐⭐⭐⭐⭐ |
| OpenRouter | 50 requests/day | ⭐⭐⭐⭐ |
| Doubao | Daily free quota | ⭐⭐⭐⭐ |
| Cloudflare AI | 100 calls/day | ⭐⭐⭐ |

**Get API Keys:**
- DeepSeek: https://platform.deepseek.com
- Alibaba: https://bailian.console.aliyun.com
- OpenRouter: https://openrouter.ai

---

### Skill 2: cloudflare-email-setup

**Commands:**
```bash
/cf-email setup          # Interactive setup
/cf-email add <domain>   # Add domain forwarding
/cf-email list           # List all domains
/cf-email status <domain># Check domain status
/cf-email test <email>   # Send test email
```

**Free Domain Options:**

| Provider | Duration | Rating | Link |
|----------|----------|--------|------|
| EU.org | Permanent | ⭐⭐⭐⭐⭐ | https://nic.eu.org |
| Freenom | 1 year | ⭐⭐⭐ | https://www.freenom.com |
| PP.UA | 1 year | ⭐⭐⭐ | https://nic.ua |

**Use Cases:**
- **Professional**: `admin@yourdomain.com`
- **Privacy**: `signup@yourdomain.com`
- **Multi-account**: `work@` / `personal@` / `shopping@`

---

## 📁 File Structure / 文件结构

```
openclaw-skills/
├── README.md              # This file / 本文件
├── CHANGELOG.md           # Release notes / 更新日志
├── LICENSE                # MIT License
├── install.sh             # Installer / 安装脚本
├── marketplace.json       # Market metadata
│
├── free-token/            # Free Token Skill
│   ├── skill.md
│   ├── README.md
│   ├── accounts.json.example
│   └── scripts/check-quota.py
│
└── cloudflare-email-setup/# Email Forwarding Skill
    ├── skill.md
    ├── README.md
    └── scripts/check-dns.py
```

---

## 🔧 Troubleshooting / 故障排查

### free-token Issues

**Q: Invalid API Key?**
```
A: Check:
   1. Key copied correctly (no spaces)
   2. Account verified (real-name for Alibaba)
   3. Free quota activated
   4. Run: /free-token check
```

**Q: Quota exhausted?**
```
A: 
   1. Switch account: /free-token rotate
   2. Wait for daily reset (DeepSeek/OpenRouter)
   3. Register new account
```

### cloudflare-email Issues

**Q: Not receiving forwarded emails?**
```
A: 
   1. Check DNS: /cf-email dns-check yourdomain.com
   2. Check spam folder
   3. Verify destination email
   4. Check Cloudflare Analytics
```

**Q: Free domain reclaimed?**
```
A: 
   - Freenom requires annual renewal
   - Use EU.org for permanent domain
```

---

## 📊 Stats / 核心数据

| Metric | Value |
|--------|-------|
| Skills | 2 |
| Free Platforms | 5+ |
| Scripts | 2 |
| Documentation | 8 pages |
| Total Size | 56KB |
| License | MIT |

---

## 🤝 Contributing / 贡献

1. Fork the repo
2. Create feature branch: `git checkout -b feature/AmazingFeature`
3. Commit: `git commit -m 'Add AmazingFeature'`
4. Push: `git push origin feature/AmazingFeature`
5. Open Pull Request

---

## 📄 License / 许可证

MIT License - See [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgments / 致谢

- [OpenClaw](https://openclaw.ai) - AI Agent Framework
- [Anthropic](https://anthropic.com) - Skills Design Philosophy
- [ECC](https://github.com/affaan-m/everything-claude-code) - Engineering Reference
- [Cloudflare](https://cloudflare.com) - Free Email Forwarding
- [DeepSeek](https://deepseek.com) - Free LLM Quota

---

## 📬 Contact / 联系方式

- **Author**: 大志 (@cdz0451)
- **GitHub**: https://github.com/cdz0451/openclaw-skills
- **Issues**: https://github.com/cdz0451/openclaw-skills/issues

---

*Making AI Accessible 🌍 | Privacy Protected 🔐*

---

# 中文文档

## 📦 合集内容

本合集包含两个实用 Skill，解决 AI 使用的两大核心问题：

| Skill | 功能 | 适用场景 |
|-------|------|----------|
| 🆓 **free-token** | 免费大模型 Token 整合 | 零成本使用 DeepSeek/阿里云/OpenRouter 等主流模型 |
| 📧 **cloudflare-email-setup** | 免费自定义域名邮箱 | 隐私注册、专业形象、多账号管理 |

---

## 🚀 快速安装

```bash
# 克隆仓库
git clone https://github.com/cdz0451/openclaw-skills.git

# 运行安装脚本
cd openclaw-skills/skills-release
./install.sh
```

**环境要求：**
- OpenClaw v1.0+
- Python 3.8+
- `pip install requests dnspython`

---

## 📖 使用指南

### Skill 1: free-token — 免费大模型 Token

**核心命令：**
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

**获取 API Key：**
- DeepSeek: https://platform.deepseek.com
- 阿里云：https://bailian.console.aliyun.com
- OpenRouter: https://openrouter.ai

---

### Skill 2: cloudflare-email-setup — 免费自定义邮箱

**核心命令：**
```bash
/cf-email setup          # 交互式配置向导
/cf-email add <域名>     # 添加域名邮箱转发
/cf-email list           # 查看所有已配置的域名
/cf-email status <域名>  # 查看转发状态
/cf-email test <邮箱>    # 发送测试邮件
```

**免费域名渠道：**

| 渠道 | 期限 | 推荐度 | 链接 |
|------|------|--------|------|
| EU.org | 永久 | ⭐⭐⭐⭐⭐ | https://nic.eu.org |
| Freenom | 1 年 | ⭐⭐⭐ | https://www.freenom.com |
| PP.UA | 1 年 | ⭐⭐⭐ | https://nic.ua |

**使用场景：**
- **专业形象** → `admin@yourdomain.com`
- **隐私保护** → `signup@yourdomain.com`
- **多账号管理** → `work@` / `personal@` / `shopping@`

---

## 🔧 故障排查

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

### cloudflare-email 常见问题

**Q: 收不到转发邮件？**
```
A: 
   1. 检查 DNS 配置：/cf-email dns-check yourdomain.com
   2. 查看垃圾邮件文件夹
   3. 确认目标邮箱已验证
   4. 检查 Cloudflare Analytics
```

---

## 📊 核心数据

| 指标 | 数值 |
|------|------|
| Skill 数量 | 2 个 |
| 免费平台 | 5+ 个 |
| 脚本工具 | 2 个 |
| 文档页数 | 8 页 |
| 总大小 | 56KB |
| 许可证 | MIT |

---

## 📬 联系方式

- **作者**: 大志 (@cdz0451)
- **GitHub**: https://github.com/cdz0451/openclaw-skills
- **Issues**: https://github.com/cdz0451/openclaw-skills/issues

---

*让 AI 更普惠 🌍 | 让隐私更安全 🔐*
