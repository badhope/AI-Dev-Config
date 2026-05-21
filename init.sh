#!/bin/bash

# ============================================
# AI-Dev-Config 资源库初始化脚本
# AI-Dev-Config Resource Initialization Script
# ============================================

set -e  # 遇到错误立即退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数
print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}  AI-Dev-Config 资源库初始化${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

print_step() {
    echo -e "${YELLOW}📦 $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# 定义资源仓库
declare -A REPOS
REPOS=(
    ["AI-SKILL"]="https://github.com/badhope/AI-SKILL"
    ["PromptHub"]="https://github.com/badhope/PromptHub"
    ["Mcp-Market"]="https://github.com/badhope/Mcp-Market"
    ["API-Market"]="https://github.com/badhope/API-Market"
    ["Global-Dev-Setup"]="https://github.com/badhope/Global-Dev-Setup"
)

# GitHub Token (可选，用于私有仓库或提高速率限制)
GITHUB_TOKEN=""

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --token|-t)
            GITHUB_TOKEN="$2"
            shift 2
            ;;
        --force|-f)
            FORCE_MODE=true
            shift
            ;;
        --help|-h)
            echo "用法: $0 [选项]"
            echo "选项:"
            echo "  --token, -t <token>  GitHub Token (可选)"
            echo "  --force, -f          强制重新克隆已存在的仓库"
            echo "  --help, -h          显示此帮助信息"
            exit 0
            ;;
        *)
            print_error "未知参数: $1"
            exit 1
            ;;
    esac
done

# 主函数
main() {
    print_header
    
    # 检测 GitHub Token 是否可用
    if [ -n "$GITHUB_TOKEN" ]; then
        print_info "使用 GitHub Token 进行认证"
    fi
    
    # 检测是否在中国大陆（使用中国镜像）
    detect_china_mirror() {
        # 检测方法1: 检查网络延迟
        if ping -c 1 -W 2 github.com > /dev/null 2>&1; then
            return 1  # 可以访问 GitHub
        fi
        
        # 检测方法2: 检查 DNS 解析
        if nslookup github.com > /dev/null 2>&1; then
            return 1  # 可以访问
        fi
        
        return 0  # 可能在中国大陆，使用镜像
    }
    
    CHINA_MIRROR=false
    if detect_china_mirror; then
        print_info "检测到可能在中国大陆，启用镜像加速..."
        CHINA_MIRROR=true
    fi
    
    # 创建资源目录
    print_step "创建资源目录..."
    mkdir -p resources
    cd resources
    print_success "资源目录创建完成"
    
    # 克隆仓库
    print_step "开始克隆资源仓库..."
    echo ""
    
    SUCCESS_COUNT=0
    FAIL_COUNT=0
    SKIP_COUNT=0
    
    for name in "${!REPOS[@]}"; do
        # 验证仓库名称安全性
        if [[ ! "$name" =~ ^[a-zA-Z0-9_-]+$ ]]; then
            print_error "仓库名称包含非法字符，跳过: $name"
            ((FAIL_COUNT++))
            continue
        fi
        
        repo_url="${REPOS[$name]}"
        
        if [ -d "$name" ]; then
            if [ "$FORCE_MODE" = true ]; then
                print_step "强制重新克隆 $name..."
                rm -rf "$name"
            else
                print_success "$name 已存在，跳过 (使用 --force 强制重新克隆)"
                ((SKIP_COUNT++))
                continue
            fi
        fi
        
        print_step "克隆 $name..."
        
        # 安全克隆 - 避免在 URL 中暴露 Token
        clone_success=0
        
        if [ -n "$GITHUB_TOKEN" ]; then
            # 使用安全的方式传递 Token - Git credential helper
            if git -c credential.helper="!f() { echo username=x-access-token; echo password=$GITHUB_TOKEN; }; f" clone --depth 1 "$repo_url" "$name" 2>&1; then
                clone_success=1
            fi
        else
            # 无 Token，直接克隆
            if git clone --depth 1 "$repo_url" "$name" 2>&1; then
                clone_success=1
            fi
        fi
        
        if [ "$clone_success" -eq 1 ]; then
            print_success "$name 克隆成功"
            ((SUCCESS_COUNT++))
        else
            print_error "$name 克隆失败"
            
            # 尝试使用 SSH 方式
            print_info "尝试 SSH 方式..."
            ssh_url="${repo_url/https:\/\/github.com\//git@github.com:}"
            if git clone --depth 1 "$ssh_url" "$name" 2>/dev/null; then
                print_success "$name SSH 克隆成功"
                ((SUCCESS_COUNT++))
            else
                print_error "$name 克隆失败，请手动检查"
                ((FAIL_COUNT++))
            fi
        fi
        echo ""
    done
    
    # 验证克隆结果
    print_step "验证资源..."
    echo ""
    
    VALIDATION_PASSED=true
    for name in "${!REPOS[@]}"; do
        if [ -d "$name" ]; then
            # 检查是否为空仓库
            if [ -z "$(ls -A "$name" 2>/dev/null)" ]; then
                print_error "$name 是空仓库"
                VALIDATION_PASSED=false
            else
                print_success "$name 验证通过"
            fi
        else
            print_error "$name 未找到"
            VALIDATION_PASSED=false
        fi
    done
    
    # 生成资源索引
    print_step "生成资源索引..."
    
    INDEX_FILE="resources_index.json"
    cat > "$INDEX_FILE" << 'EOF'
{
  "generated": "TIMESTAMP_PLACEHOLDER",
  "resources": {
    "AI-SKILL": {
      "path": "resources/AI-SKILL",
      "index_file": "skills/index.json",
      "status": "READY"
    },
    "PromptHub": {
      "path": "resources/PromptHub", 
      "index_file": "index.json",
      "status": "READY"
    },
    "Mcp-Market": {
      "path": "resources/Mcp-Market",
      "index_file": "servers-index.json",
      "status": "READY"
    },
    "API-Market": {
      "path": "resources/API-Market",
      "index_file": "api-database.json",
      "status": "READY"
    },
    "Global-Dev-Setup": {
      "path": "resources/Global-Dev-Setup",
      "index_file": "tool_registry.json",
      "status": "READY"
    }
  }
}
EOF
    
    # 替换时间戳
    sed -i "s/TIMESTAMP_PLACEHOLDER/$(date -u +%Y-%m-%dT%H:%M:%SZ)/" "$INDEX_FILE"
    
    print_success "资源索引已生成: $INDEX_FILE"
    
    # 返回上级目录
    cd ..
    
    # 总结
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}  初始化完成！${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
    echo -e "📊 统计:"
    echo -e "   ✅ 成功: $SUCCESS_COUNT"
    echo -e "   ⏭️  跳过: $SKIP_COUNT"
    echo -e "   ❌ 失败: $FAIL_COUNT"
    echo ""
    
    if [ $FAIL_COUNT -eq 0 ]; then
        print_success "所有资源已准备就绪！"
        echo ""
        echo "下一步:"
        echo "  1. 启动 AI 智能体"
        echo "  2. 让智能体读取 AI-Dev-Config 仓库"
        echo "  3. 智能体将自动加载配置并引导您"
    else
        print_error "有 $FAIL_COUNT 个资源克隆失败"
        echo ""
        echo "请手动处理失败的资源，然后重新运行此脚本。"
    fi
    
    echo ""
}

# 运行主函数
main
