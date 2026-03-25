# cloudflare-email-setup Skill — 免费自定义域名邮箱

📧 **零成本拥有专业邮箱，隐私安全又体面！**

---

## 快速开始

### 3 分钟配置完成

```bash
# 1. 运行配置向导
/cf-email setup

# 2. 输入你的域名
# 如：yourdomain.com

# 3. 输入目标邮箱
# 如：your-gmail@gmail.com

# 4. 自动完成 DNS 配置
# 等待 DNS 传播（最多 24 小时）

# 5. 验证配置
/cf-email status yourdomain.com
```

---

## 免费域名获取

**没有域名？先注册一个免费的！**

| 渠道 | 期限 | 推荐度 | 链接 |
|------|------|--------|------|
| **EU.org** | 永久 | ⭐⭐⭐⭐⭐ | https://nic.eu.org |
| **Freenom** | 1 年 | ⭐⭐⭐ | https://www.freenom.com |
| **PP.UA** | 1 年 | ⭐⭐⭐ | https://nic.ua |

**推荐 EU.org（永久免费）**：
```
1. 访问 https://nic.eu.org
2. 注册账号
3. 申请域名（如：yourname.eu.org）
4. 等待审核（1-4 周）
5. 审核通过后托管到 Cloudflare
6. 运行 /cf-email setup
```

---

## 使用场景

### 场景 1：专业形象
```
注册账号、商务联系用：
admin@yourdomain.com
contact@yourdomain.com

比 gmail 小尾巴体面多了！
```

### 场景 2：隐私保护
```
网站注册、订阅用：
signup@yourdomain.com
temp-xxx@yourdomain.com

避免暴露个人邮箱，防止泄露
```

### 场景 3：多账号管理
```
不同用途用不同前缀：
- work@ → 工作邮件
- personal@ → 私人邮件
- shopping@ → 购物订单
- social@ → 社交媒体

泄露了也知道是谁干的
```

### 场景 4：临时邮箱
```
一次性用途：
temp-20260326@yourdomain.com

用完可删除，干净利落
```

---

## 配置检查

```bash
# 检查 DNS 配置
/cf-email dns-check yourdomain.com

# 查看转发状态
/cf-email status yourdomain.com

# 发送测试邮件
/cf-email test admin@yourdomain.com
```

---

## 多开方案

### 单域名多前缀
```
一个域名创建无限个别名：
- admin@yourdomain.com
- contact@yourdomain.com
- support@yourdomain.com
- noreply@yourdomain.com
```

### 多域名 Catch-all
```
注册多个免费域名：
- domain1.tk → gmail-1@gmail.com
- domain2.ml → gmail-2@gmail.com
- domain3.ga → outlook@outlook.com
```

### 批量配置
```bash
# 批量设置多个域名
python3 scripts/batch-setup.sh \
  --domains domain1.tk,domain2.ml,domain3.ga \
  --target your-gmail@gmail.com
```

---

## 故障排查

### 收不到邮件？
```
□ 检查 DNS 配置：/cf-email dns-check yourdomain.com
□ 查看垃圾邮件文件夹
□ 确认目标邮箱已验证
□ 检查 Cloudflare Analytics
```

### DNS 记录错误？
```
手动配置 DNS：
MX: mx1.mail.cloudflare.com
MX: mx2.mail.cloudflare.com
TXT: v=spf1 include:_spf.mx.cloudflare.com ~all
CNAME: _dmarc → _dmarc.mx.cloudflare.com
```

### 域名被回收？
```
Freenom 需要每年续期！
设置提醒：/cf-email reminder add yourdomain.tk 30
或改用 EU.org（永久）
```

---

## 文件结构

```
cloudflare-email-setup/
├── skill.md                    # Skill 完整定义
├── README.md                   # 本文件
└── scripts/
    └── check-dns.py           # DNS 配置检查
```

---

## 相关链接

- [Skill 完整文档](./skill.md)
- [Cloudflare Email Routing 官方文档](https://developers.cloudflare.com/email-routing/)
- [EU.org 注册](https://nic.eu.org)
- [Freenom 注册](https://www.freenom.com)

---

*让邮箱更自由 📧*
