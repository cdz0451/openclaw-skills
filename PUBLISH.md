# 🚀 OpenClaw Skills 发布指南

## 发布到 OpenClaw 技能市场

### 前置准备

1. **GitHub 仓库**
   ```bash
   # 创建新仓库
   gh repo create xueer/openclaw-skills --public --source=. --remote=origin
   
   # 或手动创建后推送
   git init
   git remote add origin https://github.com/xueer/openclaw-skills.git
   ```

2. **提交文件**
   ```bash
   git add .
   git commit -m "feat: 初始版本发布 - 免费 Token + 免费邮箱 Skill"
   git push -u origin main
   ```

### 方式一：通过 OpenClaw CLI 发布

```bash
# 1. 登录 OpenClaw 市场
openclaw marketplace login

# 2. 验证 marketplace.json
openclaw marketplace validate ./marketplace.json

# 3. 发布技能包
openclaw marketplace publish ./skills-release

# 4. 验证发布
openclaw marketplace list --author xueer
```

### 方式二：手动提交到市场索引

1. **Fork 官方市场索引**
   ```bash
   git clone https://github.com/openclaw/marketplace-index.git
   cd marketplace-index
   ```

2. **添加技能条目**
   ```bash
   # 编辑 skills/cdz0451/openclaw-skills.json
   # 复制 marketplace.json 内容
   ```

3. **提交 PR**
   ```bash
   git add skills/xueer/
   git commit -m "add: xueer/openclaw-skills"
   git push
   # 创建 Pull Request
   ```

### 方式三：直接分享仓库

最简单的方式，用户直接克隆：

```bash
# 用户安装命令
git clone https://github.com/xueer/openclaw-skills.git
cd openclaw-skills/skills-release
./install.sh
```

---

## 推广文案

### 简短版（Twitter/Telegram）

```
🦀 OpenClaw Skills 合集发布！

🆓 free-token — 免费大模型 Token
• 整合 DeepSeek/阿里云/OpenRouter 等 5 大平台
• 每天几百万 tokens 随便用
• 多账号自动轮换

📧 cloudflare-email-setup — 免费自定义邮箱
• 零成本拥有专业域名邮箱
• 隐私保护、多账号管理
• Cloudflare 官方转发

一键安装：
git clone https://github.com/xueer/openclaw-skills.git
cd openclaw-skills/skills-release && ./install.sh

#OpenClaw #AI #FreeToken #Privacy
```

### 详细版（公众号/博客）

**标题**：《零成本使用大模型！OpenClaw Skills 合集发布，含免费 Token+ 免费邮箱》

**核心卖点**：
1. 💰 **完全免费** — 整合官方免费渠道，合法合规零成本
2. 🔧 **开箱即用** — 一键安装脚本，3 分钟配置完成
3. 📚 **文档完善** — 每个 Skill 配详细使用指南
4. 🔐 **隐私安全** — 自定义域名邮箱，注册不暴露个人邮箱
5. 🔄 **持续更新** — MIT 开源，欢迎贡献

**适用人群**：
- AI 开发者/学生（预算有限）
- 隐私保护意识强的用户
- 需要多账号管理的运营人员
- OpenClaw 用户

---

## 版本管理

### 语义化版本

```
主版本。次版本.修订号
  ↑      ↑      ↑
  |      |      └─ 向下兼容的问题修正
  |      └─ 向下兼容的功能新增
  └─ 不兼容的 API 修改
```

### 发布流程

1. **更新版本号**
   ```bash
   # 更新 marketplace.json 和 package.json
   "version": "1.0.1"
   ```

2. **更新 CHANGELOG**
   ```markdown
   ## [1.0.1] - 2026-03-27
   ### Fixed
   - 修复 xxx 问题
   
   ### Added
   - 新增 xxx 功能
   ```

3. **打 Tag 发布**
   ```bash
   git tag -a v1.0.1 -m "Release v1.0.1"
   git push origin v1.0.1
   ```

4. **创建 GitHub Release**
   ```bash
   gh release create v1.0.1 --title "Release v1.0.1" --notes-file CHANGELOG.md
   ```

---

## 用户反馈收集

### Issue 模板

创建 `.github/ISSUE_TEMPLATE/bug-report.md`：
```markdown
---
name: 🐛 Bug 报告
about: 报告一个问题
title: '[Bug] 简短描述'
---

**Skill 名称**
free-token / cloudflare-email-setup

**问题描述**
清晰简洁地描述问题

**复现步骤**
1. ...
2. ...
3. ...

**期望行为**
清晰简洁地描述期望发生什么

**环境信息**
- OpenClaw 版本：
- Python 版本：
- 操作系统：

**截图**
如适用，添加截图
```

### 讨论区

启用 GitHub Discussions，分类：
- 💡 Ideas - 功能建议
- ❓ Q&A - 使用问题
- 📢 Announcements - 发布通知

---

## 数据统计

### 追踪指标

- ⭐ GitHub Stars
- 📦 安装次数（通过 install.sh 统计）
- 🐛 Issue 数量
- 💬 Discussion 活跃度
- 🔀 Fork 数量

### 统计脚本

```bash
# 在 install.sh 中添加（可选，需用户同意）
curl -s "https://api.example.com/track?skill=free-token&action=install" > /dev/null 2>&1 &
```

---

## 后续计划

### v1.1 计划
- [ ] 添加更多免费 Token 渠道（智谱、MiniMax）
- [ ] 支持自动注册免费域名
- [ ] Web Dashboard 监控额度和邮件
- [ ] 批量操作优化

### v2.0 计划
- [ ] 新 Skill：token-saver（Token 压缩优化）
- [ ] 新 Skill：multi-account-manager（统一账号管理）
- [ ] 新 Skill：privacy-guide（隐私保护指南）

---

*祝发布顺利！🎉*
