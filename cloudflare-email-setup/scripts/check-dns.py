#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cloudflare Email Routing DNS 配置检查脚本
"""

import dns.resolver
import json
import sys
from datetime import datetime

# Cloudflare Email Routing 所需 DNS 记录
CLOUDFLARE_EMAIL_CONFIG = {
    "mx_records": [
        "mx1.mail.cloudflare.com",
        "mx2.mail.cloudflare.com"
    ],
    "spf_contains": "_spf.mx.cloudflare.com",
    "dmarc_contains": "_dmarc.mx.cloudflare.com"
}


def check_mx_records(domain):
    """检查 MX 记录"""
    results = []
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        for mx in mx_records:
            results.append({
                "priority": mx.preference,
                "exchange": str(mx.exchange).rstrip('.'),
                "is_cloudflare": 'cloudflare' in str(mx.exchange).lower()
            })
    except dns.resolver.NoAnswer:
        return [{"error": "No MX records found"}]
    except dns.resolver.NXDOMAIN:
        return [{"error": "Domain not found"}]
    except Exception as e:
        return [{"error": str(e)}]
    
    return results


def check_spf_record(domain):
    """检查 SPF 记录"""
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        for txt in txt_records:
            txt_str = str(txt).strip('"')
            if 'v=spf1' in txt_str:
                return {
                    "record": txt_str,
                    "is_cloudflare": CLOUDFLARE_EMAIL_CONFIG["spf_contains"] in txt_str
                }
        return {"error": "No SPF record found"}
    except Exception as e:
        return {"error": str(e)}


def check_dmarc_record(domain):
    """检查 DMARC 记录"""
    try:
        dmarc_records = dns.resolver.resolve(f'_dmarc.{domain}', 'CNAME')
        for dmarc in dmarc_records:
            target = str(dmarc.target).rstrip('.')
            return {
                "record": target,
                "is_cloudflare": CLOUDFLARE_EMAIL_CONFIG["dmarc_contains"] in target
            }
        return {"error": "No DMARC record found"}
    except dns.resolver.NXDOMAIN:
        # 尝试 TXT 记录
        try:
            txt_records = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
            for txt in txt_records:
                txt_str = str(txt).strip('"')
                if 'v=DMARC1' in txt_str:
                    return {
                        "record": txt_str,
                        "type": "TXT"
                    }
        except:
            pass
        return {"error": "No DMARC record found"}
    except Exception as e:
        return {"error": str(e)}


def check_email_routing(domain):
    """完整检查 Email Routing 配置"""
    print(f"\n🔍 检查域名：{domain}")
    print("=" * 60)
    
    results = {
        "domain": domain,
        "timestamp": datetime.now().isoformat(),
        "checks": {}
    }
    
    # 检查 MX 记录
    print("\n📬 检查 MX 记录...")
    mx_results = check_mx_records(domain)
    results["checks"]["mx"] = mx_results
    
    if any(r.get("is_cloudflare") for r in mx_results if "error" not in r):
        print("  ✅ MX 记录配置正确（Cloudflare）")
    else:
        print("  ❌ MX 记录未配置或不是 Cloudflare")
        if mx_results:
            for r in mx_results:
                if "error" not in r:
                    print(f"     当前：{r.get('exchange', 'unknown')}")
    
    # 检查 SPF 记录
    print("\n🛡️  检查 SPF 记录...")
    spf_result = check_spf_record(domain)
    results["checks"]["spf"] = spf_result
    
    if spf_result.get("is_cloudflare"):
        print("  ✅ SPF 记录配置正确")
        print(f"     {spf_result.get('record', '')}")
    elif "error" in spf_result:
        print(f"  ❌ {spf_result['error']}")
    else:
        print("  ❌ SPF 记录存在但不是 Cloudflare 配置")
    
    # 检查 DMARC 记录
    print("\n📋 检查 DMARC 记录...")
    dmarc_result = check_dmarc_record(domain)
    results["checks"]["dmarc"] = dmarc_result
    
    if dmarc_result.get("is_cloudflare"):
        print("  ✅ DMARC 记录配置正确")
        print(f"     {dmarc_result.get('record', '')}")
    elif "error" in dmarc_result:
        print(f"  ❌ {dmarc_result['error']}")
    else:
        print("  ⚠️  DMARC 记录存在但不是 Cloudflare 配置（可能使用自定义）")
    
    # 总体判断
    print("\n" + "=" * 60)
    mx_ok = any(r.get("is_cloudflare") for r in mx_results if "error" not in r)
    spf_ok = spf_result.get("is_cloudflare", False)
    dmarc_ok = dmarc_result.get("is_cloudflare", False)
    
    if mx_ok and spf_ok and dmarc_ok:
        print("🎉 配置状态：✅ 完全正确，可以正常使用 Email Routing")
        results["status"] = "ok"
    elif mx_ok and spf_ok:
        print("⚠️  配置状态：🟡 基本可用，建议补充 DMARC 记录")
        results["status"] = "warning"
    else:
        print("❌ 配置状态：不完整，Email Routing 可能无法正常工作")
        results["status"] = "error"
    
    print("=" * 60)
    
    # 保存报告
    report_path = f"/tmp/cloudflare-email-check-{domain.replace('.', '_')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n📁 报告已保存：{report_path}")
    
    return results


def print_setup_guide(domain):
    """打印配置指南"""
    print(f"\n📖 {domain} 配置指南")
    print("=" * 60)
    print("""
1. 登录 Cloudflare Dashboard
   https://dash.cloudflare.com

2. 选择你的域名 → Email → Email Routing

3. 点击 "Enable" 启用 Email Routing

4. 添加目标邮箱（Destination）
   - 输入你的 Gmail/QQ/Outlook 邮箱
   - 点击验证链接

5. 创建转发规则
   - Catch-all: 所有邮件转发到目标邮箱
   - 或指定前缀：admin@, contact@ 等

6. 确认 DNS 记录已自动创建
   - MX: mx1.mail.cloudflare.com, mx2.mail.cloudflare.com
   - TXT: v=spf1 include:_spf.mx.cloudflare.com ~all
   - CNAME: _dmarc → _dmarc.mx.cloudflare.com

7. 等待 DNS 传播（最多 24 小时）

8. 发送测试邮件验证
""")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python3 check-dns.py <域名>")
        print("示例：python3 check-dns.py yourdomain.com")
        sys.exit(1)
    
    domain = sys.argv[1].lower().strip()
    
    # 移除协议和前缀
    if domain.startswith("http://"):
        domain = domain[7:]
    if domain.startswith("https://"):
        domain = domain[8:]
    if domain.endswith("/"):
        domain = domain[:-1]
    
    check_email_routing(domain)
    print_setup_guide(domain)
