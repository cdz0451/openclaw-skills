# 更新日志

所有重要变更将记录在此文件中。

本项目的版本遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范。

---

## [1.0.0] - 2026-03-26

### ✨ 新增

#### free-token Skill
- 整合 5 大免费大模型平台（DeepSeek/阿里云/OpenRouter/豆包/Cloudflare）
- 多账号轮换功能（自动切换 + 手动切换）
- 额度监控脚本（check-quota.py）
- 配置模板和详细文档
- 支持每日额度自动刷新提醒

#### cloudflare-email-setup Skill
- Cloudflare Email Routing 自动化配置
- DNS 配置检查脚本（check-dns.py）
- 免费域名注册指南（EU.org/Freenom/PP.UA）
- 多开储备方案（单域名多前缀/多域名/子域名）
- 故障排查指南

### 📚 文档
- 完整 README.md（中英文）
- 使用指南（每个 Skill 独立文档）
- 发布指南（PUBLISH.md）
- marketplace.json 市场元数据
- install.sh 一键安装脚本

### 🔧 技术
- Python 3.8+ 兼容
- 依赖最小化（requests, dnspython）
- MIT 开源许可证
- 符合 OpenClaw Skill 规范

---

## 即将推出

### v1.1 计划
- [ ] 添加更多免费 Token 渠道（智谱 AI、MiniMax、月之暗面）
- [ ] 支持自动注册免费域名脚本
- [ ] Web Dashboard 监控额度和邮件转发
- [ ] 批量配置优化

### v2.0 计划
- [ ] 新 Skill：token-saver（Token 压缩优化）
- [ ] 新 Skill：multi-account-manager（统一账号管理）
- [ ] 新 Skill：privacy-guide（隐私保护最佳实践）
- [ ] 新 Skill：auto-learn（自动学习笔记生成）

---

## 版本说明

### 版本号格式
```
主版本。次版本.修订号
  ↑      ↑      ↑
  |      |      └─ 向下兼容的问题修正
  |      └─ 向下兼容的功能新增
  └─ 不兼容的 API 修改
```

### 发布周期
- **修订号**：随时发布（Bug 修复）
- **次版本**：每月发布（新功能）
- **主版本**：按需发布（重大变更）

---

## 贡献者

感谢所有为本项目做出贡献的开发者！

- [@xueer](https://github.com/xueer) - 初始版本

---

*查看详细变更记录：[GitHub Releases](https://github.com/xueer/openclaw-skills/releases)*
