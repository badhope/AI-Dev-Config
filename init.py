#!/usr/bin/env python3
"""
AI-Dev-Config 资源库初始化脚本
AI-Dev-Config Resource Initialization Script

支持平台: Linux, macOS, Windows (WSL)
Python 版本: 3.6+
"""

import os
import re
import sys
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# 颜色定义
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

# 资源仓库定义
REPOS: Dict[str, str] = {
    "AI-SKILL": "https://github.com/badhope/AI-SKILL",
    "PromptHub": "https://github.com/badhope/PromptHub",
    "Mcp-Market": "https://github.com/badhope/Mcp-Market",
    "API-Market": "https://github.com/badhope/API-Market",
    "Global-Dev-Setup": "https://github.com/badhope/Global-Dev-Setup",
}

class Logger:
    @staticmethod
    def header(msg: str):
        print(f"\n{Colors.BLUE}{'='*50}{Colors.NC}")
        print(f"{Colors.BLUE}  {msg}{Colors.NC}")
        print(f"{Colors.BLUE}{'='*50}{Colors.NC}\n")
    
    @staticmethod
    def step(msg: str):
        print(f"{Colors.YELLOW}📦 {msg}{Colors.NC}")
    
    @staticmethod
    def success(msg: str):
        print(f"{Colors.GREEN}✅ {msg}{Colors.NC}")
    
    @staticmethod
    def error(msg: str):
        print(f"{Colors.RED}❌ {msg}{Colors.NC}")
    
    @staticmethod
    def info(msg: str):
        print(f"{Colors.CYAN}ℹ️  {msg}{Colors.NC}")


def run_command(cmd: List[str], cwd: Optional[str] = None, timeout: int = 300) -> tuple:
    """执行命令并返回 (success, output)"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, "命令执行超时"
    except Exception as e:
        return False, str(e)


def clone_repo(name: str, url: str, token: Optional[str], force: bool) -> bool:
    """克隆单个仓库（安全版本，避免 Token 在 URL 中暴露）"""
    # 验证仓库名称安全性
    if not re.match(r'^[a-zA-Z0-9_-]+$', name):
        Logger.error(f"仓库名称包含非法字符，跳过: {name}")
        return False
    
    target_dir = Path('resources') / name
    
    if target_dir.exists():
        if force:
            Logger.step(f"强制重新克隆 {name}...")
            import shutil
            shutil.rmtree(target_dir)
        else:
            Logger.success(f"{name} 已存在，跳过 (使用 --force 强制重新克隆)")
            return True
    
    Logger.step(f"克隆 {name}...")
    
    # 安全克隆 - 使用 Git credential helper 避免 Token 在 URL 中暴露
    if token:
        # 使用 Git credential helper 安全传递 Token
        cmd = [
            'git', '-c',
            f'credential.helper=!f() {{ echo username=x-access-token; echo password={token}; }}; f',
            'clone', '--depth', '1', url, str(target_dir)
        ]
        success, output = run_command(cmd)
    else:
        # 无 Token，直接克隆
        success, output = run_command(
            ['git', 'clone', '--depth', '1', url, str(target_dir)]
        )
    
    if success:
        Logger.success(f"{name} 克隆成功")
        return True
    else:
        Logger.error(f"{name} 克隆失败: {output}")
        
        # 尝试 SSH 方式
        Logger.info("尝试 SSH 方式...")
        ssh_url = url.replace('https://github.com/', 'git@github.com:')
        success, output = run_command(
            ['git', 'clone', '--depth', '1', ssh_url, str(target_dir)]
        )
        
        if success:
            Logger.success(f"{name} SSH 克隆成功")
            return True
        else:
            Logger.error(f"{name} SSH 克隆也失败")
            return False


def generate_index() -> bool:
    """生成资源索引文件"""
    index_file = Path('resources_index.json')
    
    index_data = {
        "generated": datetime.utcnow().isoformat() + 'Z',
        "version": "1.3.0",
        "resources": {}
    }
    
    for name, url in REPOS.items():
        repo_path = Path('resources') / name
        index_file_path = None
        
        # 确定索引文件路径
        if name == "AI-SKILL":
            index_file_path = repo_path / "skills" / "index.json"
        elif name == "PromptHub":
            index_file_path = repo_path / "index.json"
        elif name == "Mcp-Market":
            index_file_path = repo_path / "servers-index.json"
        elif name == "API-Market":
            index_file_path = repo_path / "api-database.json"
        elif name == "Global-Dev-Setup":
            index_file_path = repo_path / "tool_registry.json"
        
        index_data["resources"][name] = {
            "path": str(repo_path),
            "index_file": str(index_file_path.relative_to('.')) if index_file_path else None,
            "url": url,
            "status": "READY" if repo_path.exists() else "MISSING"
        }
    
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    Logger.success(f"资源索引已生成: {index_file}")
    return True


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='AI-Dev-Config 资源库初始化脚本',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python init.py                    # 默认初始化
  python init.py --token <token>   # 使用 GitHub Token
  python init.py --force           # 强制重新克隆
  python init.py --check           # 仅检查状态
        """
    )
    parser.add_argument('--token', '-t', help='GitHub Token')
    parser.add_argument('--force', '-f', action='store_true', help='强制重新克隆')
    parser.add_argument('--check', '-c', action='store_true', help='仅检查状态')
    parser.add_argument('--quiet', '-q', action='store_true', help='静默模式')
    
    args = parser.parse_args()
    
    # 仅检查模式
    if args.check:
        Logger.header("检查资源状态")
        for name in REPOS.keys():
            path = Path('resources') / name
            if path.exists():
                Logger.success(f"{name}: 已克隆")
            else:
                Logger.error(f"{name}: 未克隆")
        return
    
    # 初始化
    Logger.header("AI-Dev-Config 资源库初始化")
    
    # 创建资源目录
    Logger.step("创建资源目录...")
    Path('resources').mkdir(exist_ok=True)
    Logger.success("资源目录创建完成")
    
    # 克隆仓库
    Logger.step("开始克隆资源仓库...\n")
    
    success_count = 0
    fail_count = 0
    skip_count = 0
    
    for name, url in REPOS.items():
        target_dir = Path('resources') / name
        
        if target_dir.exists() and not args.force:
            Logger.success(f"{name} 已存在，跳过")
            skip_count += 1
            continue
        
        if clone_repo(name, url, args.token, args.force):
            success_count += 1
        else:
            fail_count += 1
    
    # 验证和生成索引
    if success_count > 0:
        Logger.step("验证资源...")
        all_valid = True
        for name in REPOS.keys():
            path = Path('resources') / name
            if path.exists() and any(path.iterdir()):
                Logger.success(f"{name} 验证通过")
            else:
                Logger.error(f"{name} 验证失败")
                all_valid = False
        
        if all_valid:
            generate_index()
    
    # 总结
    Logger.header("初始化完成")
    print(f"📊 统计:")
    print(f"   ✅ 成功: {success_count}")
    print(f"   ⏭️  跳过: {skip_count}")
    print(f"   ❌ 失败: {fail_count}")
    print()
    
    if fail_count == 0:
        Logger.success("所有资源已准备就绪！")
        print("下一步:")
        print("  1. 启动 AI 智能体")
        print("  2. 让智能体读取 AI-Dev-Config 仓库")
        print("  3. 智能体将自动加载配置并引导您")
    else:
        Logger.error(f"有 {fail_count} 个资源克隆失败")
        print("请检查网络连接后重新运行。")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n操作已取消")
        sys.exit(1)
