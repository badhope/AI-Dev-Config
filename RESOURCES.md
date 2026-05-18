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

## 🔧 How to Access Resources (Step-by-Step for AI)

### When user asks you to use a resource, follow these exact steps:

#### Step 1: Clone the repository (if not already local)
```bash
git clone --depth 1 https://github.com/badhope/AI-SKILL.git
git clone --depth 1 https://github.com/badhope/PromptHub.git
git clone --depth 1 https://github.com/badhope/Mcp-Market.git
git clone --depth 1 https://github.com/badhope/API-Market.git
```

#### Step 2: Read the index file to find what you need

| Repository | Index File | What it contains |
|------------|-----------|-----------------|
| AI-SKILL | `skills/index.json` | All skill names, categories, paths |
| PromptHub | `index.json` | All prompt names, categories |
| Mcp-Market | `servers-index.json` | All MCP server names, categories, languages |
| API-Market | `api-database.json` | All API names, categories, quality scores |

#### Step 3: Navigate to the specific resource
```
Example: User wants a code review skill
1. Read AI-SKILL/skills/index.json
2. Find skill with name containing "code-review"
3. Navigate to the skill's path (e.g., skills/development/code-review/)
4. Read the SKILL.md or README.md in that directory
5. Apply the skill content to the user's task
```

```
Example: User needs a browser MCP server
1. Read Mcp-Market/servers-index.json
2. Find server with name "puppeteer" or category "browser"
3. Navigate to the server's directory
4. Read README.md for installation instructions
5. Provide the user with install commands
```

```
Example: User needs a weather API
1. Read API-Market/api-database.json
2. Search for APIs with category "weather"
3. Return top results with quality scores
4. Generate integration code template
```

---

## 📋 Resource Loading Strategy

### On-Demand Loading
```
When user needs specific resource:
1. Check if repository is already cloned locally
2. If not, clone with --depth 1 (shallow clone for speed)
3. Read the index file to locate the resource
4. Navigate to the specific resource path
5. Read and apply the content
```

### Update Strategy
```
If repository already exists locally:
1. Run git pull to get latest changes
2. Re-read the index file
3. Proceed with the task
```

---

## ⚡ Quick Reference

| User Needs | Your Action |
|------------|------------|
| "帮我做个代码审查" | Clone AI-SKILL → read index → find code-review skill → apply |
| "找个浏览器自动化工具" | Clone Mcp-Market → read servers-index → find puppeteer → provide install guide |
| "项目需要天气接口" | Clone API-Market → read api-database → search weather → return top APIs |
| "给我一个开发提示词" | Clone PromptHub → read index → find development prompts → return |
| "初始化一个新项目" | Clone the target repo → scan structure → detect tech stack → recommend resources |

---

*All resources are maintained by badhope and updated regularly.*
