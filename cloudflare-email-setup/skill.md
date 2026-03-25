# cloudflare-email-setup — Cloudflare 免费邮箱转发自动化

**版本**: 1.0  
**作者**: 学而  
**创建日期**: 2026-03-26  
**分类**: 工具类 / 账号管理

---

## 核心功能

一键配置 Cloudflare Email Routing，实现：
- 📧 **免费自定义域名邮箱** — 把 `admin@yourdomain.com` 转发到你的 Gmail/QQ 邮箱
- 🔐 **完全隐私** — Cloudflare 不存储邮件内容，只负责转发
- 💰 **零成本** — 免费域名 + 免费转发，一分钱不花
- 📊 **投递分析** — 查看转发成功率、丢弃邮件统计
- 🎣 **钓鱼检测** — 自动过滤垃圾邮件

---

## 使用方式

### 命令触发
```bash
/cf-email setup              # 交互式配置向导
/cf-email add <域名>         # 添加新域名邮箱转发
/cf-email list               # 查看所有已配置的域名
/cf-email status <域名>      # 查看某个域名的转发状态
/cf-email test <邮箱>        # 发送测试邮件
/cf-email remove <域名>      # 移除域名配置
```

### Hooks 自动触发
- **SessionStart**: 检查域名 DNS 配置是否正确
- **Daily (08:00)**: 检查转发成功率，告警异常域名
- **Weekly (周日 20:00)**: 提醒免费域名续期（如有即将过期）

---

## 快速开始

### 方案 A：已有域名

**前提条件**：
- 你 already 拥有一个域名（任何注册商）
- 域名 DNS 已托管到 Cloudflare（免费）

**配置步骤**：
```bash
# 1. 运行配置向导
/cf-email setup

# 2. 按提示输入
- 域名：yourdomain.com
- 目标邮箱：your-gmail@gmail.com
- 前缀：admin（可选，默认 catch-all）

# 3. 自动配置 DNS 记录
# Skill 会自动创建 MX、TXT、CNAME 记录

# 4. 验证配置
/cf-email status yourdomain.com
```

### 方案 B：注册免费域名

**免费域名渠道**：

| 渠道 | 免费期限 | 后缀 | 备注 |
|------|----------|------|------|
| **Freenom** | 1 年 | .tk/.ml/.ga/.cf/.gq | 需每年续期 |
| **EU.org** | 永久 | .eu.org | 审核较慢（1-4 周） |
| **PP.UA** | 1 年 | .pp.ua | 需短信验证 |
| **Dynamic DNS** | 永久 | dyndns 子域名 | 适合测试 |

**推荐：EU.org（永久免费）**
```bash
# 1. 访问 https://nic.eu.org
# 2. 注册账号
# 3. 申请域名（如：yourname.eu.org）
# 4. 等待审核（1-4 周）
# 5. 审核通过后，托管到 Cloudflare
# 6. 运行 /cf-email setup
```

**备选：Freenom（快速但需续期）**
```bash
# 1. 访问 https://www.freenom.com
# 2. 搜索可用域名
# 3. 选择 12 个月免费
# 4. 注册并验证邮箱
# 5. 托管到 Cloudflare
# 6. 运行 /cf-email setup
```

---

## Cloudflare Email Routing 配置详解

### 步骤 1：登录 Cloudflare
```
1. 访问 https://dash.cloudflare.com
2. 登录账号
3. 选择你的域名
```

### 步骤 2：启用 Email Routing
```
1. 左侧菜单 → Email → Email Routing
2. 点击 "Get started"
3. 点击 "Enable"
```

### 步骤 3：添加目标邮箱（Destination）
```
1. 点击 "Add destination"
2. 输入你的个人邮箱（Gmail/QQ/Outlook）
3. Cloudflare 会发送验证邮件
4. 点击验证链接确认
```

### 步骤 4：创建转发规则

**方式 A：Catch-all（推荐）**
```
所有发送到 @yourdomain.com 的邮件都转发到目标邮箱
- 前缀：*（或留空）
- 动作：Send to → 选择已验证的目标邮箱
```

**方式 B：指定前缀**
```
只转发特定前缀的邮件，如：
- admin@yourdomain.com → your-gmail@gmail.com
- contact@yourdomain.com → your-gmail@gmail.com
- noreply@yourdomain.com → 丢弃
```

### 步骤 5：配置 DNS 记录

Cloudflare 会自动创建以下记录：

| 类型 | 名称 | 内容 | 说明 |
|------|------|------|------|
| **MX** | @ | mx1.mail.cloudflare.com | 邮件交换记录 |
| **MX** | @ | mx2.mail.cloudflare.com | 备份邮件交换 |
| **TXT** | @ | v=spf1 include:_spf.mx.cloudflare.com ~all | SPF 防伪造 |
| **CNAME** | _dmarc | _dmarc.mx.cloudflare.com | DMARC 验证 |

**手动配置（如自动失败）**：
```bash
# MX 记录
优先级：1
名称：@
值：mx1.mail.cloudflare.com

优先级：1
名称：@
值：mx2.mail.cloudflare.com

# TXT 记录
名称：@
值：v=spf1 include:_spf.mx.cloudflare.com ~all

# CNAME 记录
名称：_dmarc
值：_dmarc.mx.cloudflare.com
```

---

## 多开储备方案

### 场景：需要多个备用邮箱

**方案 A：单域名多前缀**
```
一个域名创建多个转发地址：
- admin@yourdomain.com → gmail-1@gmail.com
- contact@yourdomain.com → gmail-2@gmail.com
- support@yourdomain.com → outlook@outlook.com
```

**方案 B：多域名 Catch-all**
```
注册多个免费域名，每个都配置 catch-all：
- domain1.tk → gmail-1@gmail.com
- domain2.ml → gmail-2@gmail.com
- domain3.ga → proton@proton.me
```

**方案 C：域名 + 子域名组合**
```
主域名：yourdomain.com → gmail-1@gmail.com
子域名：mail.yourdomain.com → gmail-2@gmail.com
子域名：temp.yourdomain.com → outlook@outlook.com
```

### 批量配置脚本
```bash
#!/bin/bash
# scripts/batch-setup.sh

DOMAINS=("domain1.tk" "domain2.ml" "domain3.ga")
TARGET_EMAIL="your-gmail@gmail.com"

for domain in "${DOMAINS[@]}"; do
    echo "配置 $domain ..."
    python3 scripts/configure-email.py --domain $domain --target $TARGET_EMAIL
done
```

---

## 自动化脚本

### DNS 配置检查
```python
#!/usr/bin/env python3
# scripts/check-dns.py

import dns.resolver
import json

def check_email_routing(domain):
    """检查域名的 Email Routing DNS 配置"""
    results = {
        "domain": domain,
        "mx_records": [],
        "spf_record": None,
        "dmarc_record": None,
        "status": "unknown"
    }
    
    # 检查 MX 记录
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            results["mx_records"].append(str(mx.exchange))
    except Exception as e:
        results["mx_records"] = ["ERROR: " + str(e)]
    
    # 检查 SPF 记录
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for txt in txt_records:
            txt_str = str(txt)
            if 'v=spf1' in txt_str:
                results["spf_record"] = txt_str
    except Exception as e:
        results["spf_record"] = "ERROR: " + str(e)
    
    # 检查 DMARC 记录
    try:
        dmarc_records = dns.resolver.resolve(f'_dmarc.{domain}', 'CNAME')
        for dmarc in dmarc_records:
            results["dmarc_record"] = str(dmarc.target)
    except Exception as e:
        results["dmarc_record"] = "ERROR: " + str(e)
    
    # 判断状态
    mx_ok = any('cloudflare' in mx for mx in results["mx_records"])
    spf_ok = results["spf_record"] and 'cloudflare' in results["spf_record"]
    dmarc_ok = results["dmarc_record"] and 'cloudflare' in results["dmarc_record"]
    
    if mx_ok and spf_ok and dmarc_ok:
        results["status"] = "✅ 配置正确"
    else:
        results["status"] = "❌ 配置不完整"
    
    return results

if __name__ == "__main__":
    import sys
    domain = sys.argv[1] if len(sys.argv) > 1 else "yourdomain.com"
    result = check_email_routing(domain)
    print(json.dumps(result, indent=2))
```

### 测试邮件发送
```python
#!/usr/bin/env python3
# scripts/test-forwarding.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_email(to_address, subject="Cloudflare Email Forwarding Test"):
    """发送测试邮件到自定义域名邮箱"""
    msg = MIMEMultipart()
    msg['From'] = "test@example.com"
    msg['To'] = to_address
    msg['Subject'] = subject
    
    body = """
    这是一封测试邮件。
    
    如果你收到这封邮件，说明 Cloudflare Email Forwarding 配置成功！
    
    测试时间：2026-03-26
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # 这里只是示例，实际需要使用真实 SMTP 服务器
    print(f"测试邮件已发送到：{to_address}")
    print("请检查你的目标邮箱是否收到转发邮件")

if __name__ == "__main__":
    import sys
    to_email = sys.argv[1] if len(sys.argv) > 1 else "admin@yourdomain.com"
    send_test_email(to_email)
```

---

## 故障排查

### 问题 1：收不到转发邮件

**检查清单**：
```
□ DNS 记录是否正确（MX/TXT/CNAME）
□ 目标邮箱是否已验证
□ 垃圾邮件文件夹（可能被误判）
□ Cloudflare Email Routing 是否已启用
□ 域名是否已托管到 Cloudflare
```

**解决步骤**：
```bash
# 1. 检查 DNS
/cf-email dns-check yourdomain.com

# 2. 查看转发日志
# Cloudflare Dashboard → Email → Analytics

# 3. 发送测试邮件
/cf-email test admin@yourdomain.com
```

### 问题 2：DNS 记录无法自动创建

**原因**：
- 域名未托管到 Cloudflare
- DNS 权限不足
- 已有冲突的 MX 记录

**手动解决方案**：
```bash
# 1. 登录域名注册商后台
# 2. 修改 Nameserver 为 Cloudflare：
#    - ns1.your-domain.cloudflare.com
#    - ns2.your-domain.cloudflare.com
# 3. 等待 DNS 传播（最多 24 小时）
# 4. 重新运行 /cf-email setup
```

### 问题 3：免费域名被回收

**常见于 Freenom**：
- 忘记续期（免费域名需每年手动续期）
- 长期未使用（90 天无活动可能被回收）

**预防措施**：
```bash
# 1. 设置续期提醒
/cf-email reminder add yourdomain.tk 30

# 2. 定期检查状态
/cf-email status yourdomain.tk

# 3. 使用永久免费域名（EU.org）替代
```

---

## 最佳实践

### 1. 邮箱命名规范
```
推荐前缀：
- admin@ — 通用管理
- contact@ — 联系邮箱
- support@ — 客服支持
- noreply@ — 不回复（可配置丢弃）
- temp-xxx@ — 临时用途（可定期清理）

避免前缀：
- info@ — 容易收到垃圾邮件
- sales@ — 容易被标记为营销
```

### 2. 安全建议
```
□ 不要在公开场合暴露自定义域名邮箱
□ 定期查看 Cloudflare Analytics 监控异常
□ 启用 Cloudflare 的钓鱼检测
□ 重要账号使用专用前缀（如：banking@）
```

### 3. 多账号管理
```
用途分类：
- 主邮箱：admin@ → 日常使用
- 注册邮箱：signup@ → 网站注册
- 临时邮箱：temp-xxx@ → 一次性使用
- 工作邮箱：work@ → 工作相关

每个分类使用独立前缀，便于管理和追踪泄露源
```

---

## 扩展阅读

- [Cloudflare Email Routing 官方文档](https://developers.cloudflare.com/email-routing/)
- [免费域名注册指南](../free-domains/)
- [多账号管理 Skill](../multi-account-manager/)
- [隐私保护最佳实践](../privacy-guide/)

---

## 更新日志

- **2026-03-26 v1.0**: 初始版本
  - 支持 Cloudflare Email Routing 自动化配置
  - DNS 检查脚本
  - 多开储备方案
  - 故障排查指南

---

*让邮箱更自由，让隐私更安全 📧*
