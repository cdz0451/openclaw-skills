#!/bin/bash
# OpenClaw Skills 安装脚本
# 自动安装 free-token 和 cloudflare-email-setup

set -e

echo "🦀 OpenClaw Skills 安装程序"
echo "================================"
echo ""

# 检测 OpenClaw 安装目录
OPENCLAW_DIR="${OPENCLAW_DIR:-$HOME/.openclaw/workspace/agents/xueer}"
SKILLS_DIR="$OPENCLAW_DIR/skills"

# 检查目录是否存在
if [ ! -d "$OPENCLAW_DIR" ]; then
    echo "❌ 错误：OpenClaw 目录不存在：$OPENCLAW_DIR"
    echo "请确认 OpenClaw 已正确安装"
    exit 1
fi

# 创建 skills 目录（如不存在）
mkdir -p "$SKILLS_DIR"

echo "✅ OpenClaw 目录：$OPENCLAW_DIR"
echo ""

# 安装 free-token
echo "📦 安装 free-token Skill..."
if [ -d "./free-token" ]; then
    cp -r ./free-token "$SKILLS_DIR/"
    echo "✅ free-token 安装完成"
else
    echo "⚠️  警告：free-token 目录不存在，跳过"
fi

# 安装 cloudflare-email-setup
echo "📦 安装 cloudflare-email-setup Skill..."
if [ -d "./cloudflare-email-setup" ]; then
    cp -r ./cloudflare-email-setup "$SKILLS_DIR/"
    echo "✅ cloudflare-email-setup 安装完成"
else
    echo "⚠️  警告：cloudflare-email-setup 目录不存在，跳过"
fi

# 安装 Python 依赖
echo ""
echo "📦 安装 Python 依赖..."
pip3 install requests dnspython -q
echo "✅ Python 依赖安装完成"

# 创建配置模板
echo ""
echo "📝 创建配置模板..."

# free-token 配置
if [ -f "$SKILLS_DIR/free-token/accounts.json.example" ]; then
    if [ ! -f "$SKILLS_DIR/free-token/accounts.json" ]; then
        cp "$SKILLS_DIR/free-token/accounts.json.example" "$SKILLS_DIR/free-token/accounts.json"
        echo "✅ free-token 配置模板已创建"
    else
        echo "⚠️  free-token 配置已存在，跳过"
    fi
fi

# 设置脚本权限
echo ""
echo "🔧 设置脚本权限..."
chmod +x "$SKILLS_DIR/free-token/scripts/check-quota.py" 2>/dev/null || true
chmod +x "$SKILLS_DIR/cloudflare-email-setup/scripts/check-dns.py" 2>/dev/null || true
echo "✅ 脚本权限设置完成"

# 完成
echo ""
echo "================================"
echo "🎉 安装完成！"
echo ""
echo "下一步："
echo ""
echo "1️⃣  配置 free-token（免费 Token）"
echo "   cd $SKILLS_DIR/free-token"
echo "   vim accounts.json  # 填入你的 API Key"
echo ""
echo "   获取免费 API Key："
echo "   • DeepSeek: https://platform.deepseek.com"
echo "   • 阿里云：https://bailian.console.aliyun.com"
echo "   • OpenRouter: https://openrouter.ai"
echo ""
echo "2️⃣  配置 cloudflare-email-setup（免费邮箱）"
echo "   /cf-email setup  # 在 OpenClaw 中运行"
echo ""
echo "   获取免费域名："
echo "   • EU.org: https://nic.eu.org (永久)"
echo "   • Freenom: https://www.freenom.com (1 年)"
echo ""
echo "3️⃣  查看使用指南"
echo "   cat $SKILLS_DIR/free-token/README.md"
echo "   cat $SKILLS_DIR/cloudflare-email-setup/README.md"
echo ""
echo "================================"
echo ""
