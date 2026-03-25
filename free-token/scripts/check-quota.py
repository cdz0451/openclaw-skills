#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
free-token 额度检查脚本
检查各平台免费 Token 剩余额度
"""

import requests
import json
import os
from datetime import datetime

# 配置文件路径
CONFIG_PATH = os.path.expanduser("~/.openclaw/workspace/agents/xueer/skills/free-token/accounts.json")
OUTPUT_PATH = os.path.expanduser("~/.openclaw/workspace/agents/xueer/skills/free-token/quota-report.json")

# 各平台额度查询 API
PLATFORMS = {
    "aliyun": {
        "name": "阿里云百炼",
        "quota_url": "https://bailian.console.aliyun.com/api/v1/account/quota",
        "models": ["qwen-plus", "qwen-max", "qwen-turbo"]
    },
    "deepseek": {
        "name": "DeepSeek",
        "quota_url": "https://api.deepseek.com/v1/user/status",
        "models": ["deepseek-chat", "deepseek-coder"]
    },
    "openrouter": {
        "name": "OpenRouter",
        "quota_url": "https://openrouter.ai/api/v1/auth/key",
        "models": ["meta-llama/llama-3-70b-instruct", "anthropic/claude-3-haiku"]
    },
    "doubao": {
        "name": "豆包",
        "quota_url": "https://ark.cn-beijing.volces.com/api/v3/account/quota",
        "models": ["doubao-pro-4k", "doubao-lite-4k"]
    },
    "cloudflare": {
        "name": "Cloudflare AI",
        "quota_url": "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/usage",
        "models": ["@cf/meta/llama-3-8b-instruct", "@cf/mistral/mistral-7b-instruct-v0.1"]
    }
}


def load_accounts():
    """加载账号配置"""
    if not os.path.exists(CONFIG_PATH):
        print(f"⚠️  配置文件不存在：{CONFIG_PATH}")
        print("请先运行 /free-token setup 进行配置")
        return None
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_aliyun_quota(api_key):
    """检查阿里云百炼额度"""
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(
            PLATFORMS["aliyun"]["quota_url"],
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return {
                "remaining": data.get("remaining_tokens", 0),
                "total": data.get("total_tokens", 0),
                "used": data.get("used_tokens", 0)
            }
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def check_deepseek_quota(api_key):
    """检查 DeepSeek 额度"""
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(
            PLATFORMS["deepseek"]["quota_url"],
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return {
                "remaining": data.get("data", {}).get("balance", 0),
                "daily_limit": data.get("data", {}).get("daily_limit", 0),
                "daily_used": data.get("data", {}).get("daily_used", 0)
            }
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def check_openrouter_quota(api_key):
    """检查 OpenRouter 额度"""
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(
            PLATFORMS["openrouter"]["quota_url"],
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return {
                "limit": data.get("data", {}).get("limit", 0),
                "usage": data.get("data", {}).get("usage", 0),
                "is_free_tier": data.get("data", {}).get("is_free_tier", False)
            }
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


def check_all_accounts():
    """检查所有账号额度"""
    accounts = load_accounts()
    if not accounts:
        return None
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "platforms": {}
    }
    
    for platform, config in accounts.get("accounts", {}).items():
        platform_results = []
        
        for account in config:
            quota = None
            
            if platform == "aliyun":
                quota = check_aliyun_quota(account["apiKey"])
            elif platform == "deepseek":
                quota = check_deepseek_quota(account["apiKey"])
            elif platform == "openrouter":
                quota = check_openrouter_quota(account["apiKey"])
            # 其他平台按需扩展
            
            platform_results.append({
                "name": account.get("name", "未命名"),
                "quota": quota,
                "status": "ok" if quota and "error" not in quota else "error"
            })
        
        results["platforms"][platform] = platform_results
    
    # 保存结果
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    return results


def print_report(results):
    """打印额度报告"""
    if not results:
        print("❌ 无法获取额度信息")
        return
    
    print("\n" + "=" * 60)
    print("📊 免费 Token 额度报告")
    print(f"更新时间：{results['timestamp']}")
    print("=" * 60)
    
    for platform, accounts in results["platforms"].items():
        platform_name = PLATFORMS.get(platform, {}).get("name", platform)
        print(f"\n🔹 {platform_name}")
        print("-" * 40)
        
        for account in accounts:
            status_icon = "✅" if account["status"] == "ok" else "❌"
            print(f"  {status_icon} {account['name']}")
            
            quota = account.get("quota", {})
            if "error" in quota:
                print(f"      错误：{quota['error']}")
            else:
                if "remaining" in quota:
                    remaining = quota.get("remaining", 0)
                    total = quota.get("total", quota.get("daily_limit", 0))
                    if total > 0:
                        percent = (remaining / total) * 100
                        bar = "█" * int(percent / 10) + "░" * (10 - int(percent / 10))
                        print(f"      额度：[{bar}] {remaining:,.0f} / {total:,.0f} ({percent:.1f}%)")
                    else:
                        print(f"      余额：{remaining:,.0f}")
                elif "limit" in quota:
                    limit = quota.get("limit", 0)
                    usage = quota.get("usage", 0)
                    remaining = limit - usage
                    print(f"      请求：{usage} / {limit} (剩余 {remaining})")
    
    print("\n" + "=" * 60)
    print("💡 提示：额度低于 20% 时建议切换账号")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    print("🔍 正在检查各平台额度...")
    results = check_all_accounts()
    print_report(results)
    print(f"📁 报告已保存：{OUTPUT_PATH}")
