# Resource Repository Mapping

> **External Resource Guide for AI Assistants**
> 
> This file maps where to find skills, prompts, MCP servers, and APIs.

---

## 📦 Resource Overview

| Resource Type | Repository | Content Scale | Access Method |
|--------------|------------|---------------|---------------|
| **Skills** | [AI-SKILL](https://github.com/badhope/AI-SKILL) | 2,677+ skills | On-demand clone |
| **Prompts** | [PromptHub](https://github.com/badhope/PromptHub) | 80+ prompts | Direct read |
| **MCP Servers** | [Mcp-Market](https://github.com/badhope/Mcp-Market) | 438 servers | On-demand clone |
| **APIs** | [API-Market](https://github.com/badhope/API-Market) | 14,405+ APIs | Query database |

---

## 🎯 AI-SKILL Repository

**URL**: `https://github.com/badhope/AI-SKILL`

**Content**: 2,677+ production-ready skills across 11 platforms

**Categories**:
- Development (frontend, backend, fullstack)
- Writing (content creation, editing)
- Analysis (data, business, competitive)
- Product (PRD, OKR, management)
- Communication (internal comms, email)

**Usage**:
```python
# Search skills
skills = search_skill(query="code-review", limit=10)

# Load specific skill
skill = load_skill("code-review")
```

**Local Path**: `/workspace/AI-SKILL`

---

## 📝 PromptHub Repository

**URL**: `https://github.com/badhope/PromptHub`

**Content**: 80+ prompts across 5 categories

**Categories**:
- Development
- Writing
- Business
- Life
- Creative

**Platform Support**:
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google (Gemini)
- ByteDance (Doubao)
- Alibaba (Qwen)
- Baidu (Wenxin)

**Usage**:
```python
# Get prompt by name
prompt = get_prompt("Python Developer", category="development")

# Search prompts
prompts = search_prompt("Python", limit=10)
```

**Local Path**: `/workspace/PromptHub`

---

## 🔌 Mcp-Market Repository

**URL**: `https://github.com/badhope/Mcp-Market`

**Content**: 438 MCP servers across 22 categories

**Popular Categories**:
- Browser Automation (puppeteer, playwright)
- Database (sqlite, postgresql, mongodb)
- Search (brave-search, tavily, exa)
- Git (git, github, gitlab)
- File System (filesystem, file-tools)
- AI Integration (any_chat_completions, needle)

**Usage**:
```python
# Search MCP servers
servers = search_mcp(query="browser", limit=10)

# Install MCP server
result = install_mcp("puppeteer")

# Get install commands
cmds = get_mcp_install_command("puppeteer")
```

**Local Path**: `/workspace/Mcp-Market`

---

## 🌐 API-Market Repository

**URL**: `https://github.com/badhope/API-Market`

**Content**: 14,405+ public APIs across 60 categories

**Database Files**:
- `api-database.json` - Full API database
- `search-index.json` - Search index
- `quality-report.json` - Quality ratings

**Categories**:
- Development (code validation, documentation)
- Data (weather, finance, geolocation)
- AI/ML (translation, sentiment analysis)
- Media (images, video, audio)
- Communication (email, SMS, chat)

**Usage**:
```python
# Search APIs
apis = search_api(query="weather", limit=10)

# Get API details
api = get_api_details("openweathermap.org")

# Generate integration code
code = generate_api_code("openweathermap.org", language="python")
```

**Local Path**: `/workspace/API-Market`

---

## 🔧 Local Development Assistant

**Path**: `/workspace/dev-assistant`

**Components**:
- `main.py` - CLI entry point
- `modules/` - Core modules
  - `mcp_manager.py` - MCP integration
  - `api_manager.py` - API integration
  - `skill_manager.py` - Skill integration
  - `prompt_manager.py` - Prompt integration

**Usage**:
```bash
# Initialize project
python main.py init https://github.com/user/repo

# Generate code
python main.py generate python class --name MyClass

# Search resources
python main.py mcp search --query browser
python main.py api search --query weather
python main.py skill search --query code-review
```

---

## 📋 Resource Loading Strategy

### On-Demand Loading
```
When user needs specific resource:
1. Check if already cloned locally
2. If not, clone from GitHub
3. Load required content
4. Cache for future use
```

### Batch Operations
```
For multiple independent tasks:
1. Group similar requests
2. Execute in parallel
3. Cache results
```

### Update Strategy
```
Before using cached resource:
1. Check last update time
2. If > 24 hours, git pull
3. Update local cache
```

---

## ⚡ Quick Reference

| Need | Action | Command/API |
|------|--------|-------------|
| Code review skill | Load from AI-SKILL | `load_skill("code-review")` |
| Python dev prompt | Get from PromptHub | `get_prompt("Python Developer")` |
| Browser automation | Install MCP | `install_mcp("puppeteer")` |
| Weather API | Search API-Market | `search_api("weather")` |
| New project | Use dev-assistant | `python main.py init <repo>` |

---

*All resources are maintained by badhope and updated regularly.*
