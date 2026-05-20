# AI Usage Guide

> **How to effectively use badhope development resource ecosystem**

---

## 🎯 Overview

This configuration center provides five core resources to help AI agents complete various development tasks:

| Resource Type | Count | Purpose |
|--------------|-------|---------|
| **AI-SKILL** | 2,677+ skills | Professional AI task skills library |
| **PromptHub** | 80+ prompts | Optimized prompt templates |
| **Mcp-Market** | 438 servers | Extended tool integration |
| **API-Market** | 14,405+ APIs | Third-party service integration |
| **Global-Dev-Setup** | 187+ tools | Development environment configuration |

---

## 🚀 Quick Decision Flow

### When user makes a request, AI should follow this flow:

```
User Request
    ↓
[1] Understand task type
    ↓
┌─────────────────────────────────────┐
│ Type A: Need professional skills?   │
│   → Use AI-SKILL                   │
│                                     │
│ Type B: Need optimized prompts?    │
│   → Use PromptHub                  │
│                                     │
│ Type C: Need extended tools?       │
│   → Use Mcp-Market                 │
│                                     │
│ Type D: Need third-party APIs?     │
│   → Use API-Market                 │
│                                     │
│ Type E: Need dev environment setup?│
│   → Use Global-Dev-Setup           │
│                                     │
│ Type F: Complex task (multi-resource)?│
│   → Combine multiple resources     │
└─────────────────────────────────────┘
    ↓
[2] Load corresponding resource
    ↓
[3] Execute task
```

---

## 📚 Detailed Usage Guide

### Type A: Need Professional Skills → AI-SKILL

**Scenario**: User needs to complete a specific domain professional task

**Example Requests**:
- "Help me write a code review skill"
- "I need an SEO audit tool"
- "Create a PRD document"

**Steps**:
```python
# 1. Clone repository
git clone --depth 1 https://github.com/badhope/AI-SKILL.git

# 2. Read index
# Read skills/index.json

# 3. Search for relevant skills
# Find skills matching user needs

# 4. Read skill file
# Read skills/[category]/[skill-name]/SKILL.md

# 5. Apply skill to task
```

**Decision Tree**:
```
User requirement contains keywords?
├─ "code" + "review" → code-review
├─ "product" + "requirement" → prd-writer
├─ "SEO" + "audit" → seo-auditor
└─ "OKR" + "goal" → okr
```

---

### Type B: Need Optimized Prompts → PromptHub

**Scenario**: User needs specific scenario optimized prompts

**Example Requests**:
- "Give me a code explanation prompt"
- "Need an email reply template"
- "Create product copy prompt"

**Steps**:
```python
# 1. Clone repository
git clone --depth 1 https://github.com/badhope/PromptHub.git

# 2. Read index
# Read index.json

# 3. Search for relevant prompts
# Search by category or keyword

# 4. Return prompt content
# Provide complete prompt template and usage instructions
```

**Decision Tree**:
```
Prompt category?
├─ Development → Development-related prompts
├─ Writing → Writing-related prompts
├─ Business → Business-related prompts
├─ Life → Life-related prompts
└─ Creative → Creative-related prompts
```

---

### Type C: Need Extended Tools → Mcp-Market

**Scenario**: Need to integrate external tools to extend AI capabilities

**Example Requests**:
- "Need browser automation tool"
- "I want to connect to PostgreSQL database"
- "Need a GitHub MCP server"

**Steps**:
```python
# 1. Clone repository
git clone --depth 1 https://github.com/badhope/Mcp-Market.git

# 2. Read index
# Read servers-index.json

# 3. Search for relevant MCP servers
# Find matching servers

# 4. Read server documentation
# Read servers/[server-name]/README.md

# 5. Provide installation and usage guide
# Return complete configuration instructions
```

**Decision Tree**:
```
Tool type?
├─ Browser → puppeteer, playwright
├─ Database → postgresql, mongodb, redis
├─ Search → tavily, brave-search
├─ Git → github, gitlab
└─ File → filesystem, file-tools
```

---

### Type D: Need Third-Party APIs → API-Market

**Scenario**: Need to integrate external API services

**Example Requests**:
- "Project needs weather API"
- "Want a translation API"
- "Need map service"

**Steps**:
```python
# 1. Clone repository
git clone --depth 1 https://github.com/badhope/API-Market.git

# 2. Read index
# Read api-database.json

# 3. Search for relevant APIs
# Search by category or keyword

# 4. Evaluate API quality
# Check quality_score and auth_type

# 5. Return integration code
# Generate API integration code template
```

**Decision Tree**:
```
API category?
├─ Weather → HeFeng Weather, OpenWeatherMap
├─ Translation → Baidu Translation, Youdao Translation
├─ Maps → Amap, Google Maps
├─ AI/ML → OpenAI, Cohere, Anthropic
└─ Finance → Stocks, Currency Conversion
```

---

### Type E: Need Development Environment → Global-Dev-Setup ⭐

**Scenario**: User needs to set up development environment or install tools

**Example Requests**:
- "Help me install Python environment"
- "Set up an AI development environment"
- "I need to install Docker"

**Steps**:
```python
# 1. Clone repository
git clone --depth 1 https://github.com/badhope/Global-Dev-Setup.git

# 2. Read tool registry
# Read tool_registry.json

# 3A. If user needs specific tool:
#    - Search for tool
#    - Get installation commands
#    - Return commands (consider using China mirrors)

# 3B. If user needs complete environment:
#    - Find environment template (e.g., ai-ml-developer)
#    - Get all tools in template
#    - Generate installation script
```

**Environment Template Quick Find**:
```
User role/scenario?
├─ AI/ML Development → ai-ml-developer
├─ AI Agent Development → ai-agent-developer
├─ Full-stack Development → fullstack-developer
├─ Frontend Development → frontend-developer
├─ Backend Development → backend-developer
├─ DevOps → devops-engineer
├─ Data Engineering → data-engineering
└─ Mobile Development → mobile-developer
```

**Mirror Selection Strategy**:
```python
# Auto-select mirror based on user location
if user_location == "China":
    # Use China mirrors
    pip_mirror = "https://pypi.tuna.tsinghua.edu.cn/simple"
    npm_mirror = "https://registry.npmmirror.com"
    docker_mirror = "https://docker.mirrors.ustc.edu.cn"
else:
    # Use official sources
    pip_mirror = "https://pypi.org/simple"
    npm_mirror = "https://registry.npmjs.org"
    docker_mirror = "https://registry-1.docker.io"
```

---

### Type F: Complex Task (Multi-Resource Combination)

**Scenario**: User needs involve multiple aspects

**Example Requests**:
- "I want to develop an AI application that needs environment, tools and APIs"
- "Help me build a data processing platform"

**Workflow**:
```python
# 1. Analyze requirements
# Break down into multiple subtasks

# 2. Combine resources
# - Use Global-Dev-Setup to configure environment
# - Use AI-SKILL to get development skills
# - Use Mcp-Market to integrate required tools
# - Use API-Market to connect third-party services

# 3. Generate complete solution
# Provide one-stop solution
```

---

## 🎯 Intelligent Recommendation System

### Automatic Recommendation Based on User Description

**Scenario Recognition Keywords**:
| Keyword Combination | Recommended Resource | Recommended Template |
|--------------------|---------------------|---------------------|
| "Python" + "development" | Global-Dev-Setup | python-developer |
| "React" + "frontend" | Global-Dev-Setup | frontend-developer |
| "AI" + "machine learning" | Global-Dev-Setup | ai-ml-developer |
| "Agent" + "intelligent" | Global-Dev-Setup | ai-agent-developer |
| "Docker" + "container" | Global-Dev-Setup | devops-engineer |
| "code review" | AI-SKILL | code-review |
| "PRD" + "document" | AI-SKILL | prd-writer |
| "API" + "integration" | Mcp-Market | Select by type |
| "weather" + "API" | API-Market | weather category |
| "prompt" + "optimization" | PromptHub | development category |

---

## 🔧 Common Task Templates

### Task 1: New Project Initialization

```python
# 1. Analyze project requirements
project_type = detect_project_type(user_description)

# 2. Select environment template
env_template = get_template(project_type)

# 3. Get required tools
tools = get_template_tools(env_template)

# 4. Get required skills
skill = find_skill(project_type)

# 5. Generate initialization script
generate_install_script(tools, user_os, user_region)
```

### Task 2: Add New Feature

```python
# 1. Analyze feature requirements
feature = parse_feature_request(user_description)

# 2. Determine required resources
required_resources = []

if feature.needs_api:
    api = search_api_market(feature.api_requirements)
    required_resources.append(api)

if feature.needs_tools:
    tools = search_mcp_market(feature.tool_requirements)
    required_resources.extend(tools)

if feature.needs_skill:
    skill = search_ai_skill(feature.skill_requirements)
    required_resources.append(skill)

# 3. Return resources and usage guide
return required_resources
```

### Task 3: Debugging and Troubleshooting

```python
# 1. Analyze problem type
problem_type = classify_problem(user_description)

# 2. Search for relevant skills
skill = search_ai_skill(f"{problem_type} troubleshooting")

# 3. Search for relevant tools
tools = search_mcp_market(problem_type)

# 4. Return diagnostic steps and tools
return diagnostic_guide(skill, tools)
```

---

## 📋 Output Format Specifications

### Standard Resource Return Format

```markdown
## Recommended Resources

### 1. [Resource Name]
- **Type**: [Resource Type]
- **Purpose**: [Brief description]
- **Access**: [How to obtain]
- **Usage**: [How to use]

### 2. [Resource Name]
...
```

### Installation Command Return Format

```markdown
## Installation Guide

### System Requirements
- OS: Linux/macOS/Windows
- Permissions: Administrator privileges required

### Installation Steps

#### Step 1: [Action]
```bash
[command]
```

#### Step 2: [Action]
```bash
[command]
```

### Verify Installation
```bash
[verification command]
```

### Common Issues
Q: [Question]
A: [Answer]
```

---

## 🎓 Learning and Optimization

### Continuous Improvement Mechanism

```python
# 1. Record usage
log_resource_usage(
    user_request=original_request,
    resources_used=selected_resources,
    success_rate=outcome,
    user_feedback=feedback
)

# 2. Analyze patterns
pattern = analyze_usage_patterns()

# 3. Optimize recommendations
optimize_recommendations(pattern)

# 4. Update knowledge base
update_resource_knowledge(pattern)
```

---

## ⚠️ Notes

### Resource Selection Principles

1. **Precise Matching**: Prioritize resources that best match user needs
2. **Quality First**: Choose resources with high ratings and complete documentation
3. **Ease of Use**: Prioritize resources that are easy to integrate and use
4. **Timeliness**: Pay attention to resource update dates and versions
5. **Security**: Ensure resources come from reliable sources with no security risks

### Mirror Selection

```python
# Auto-detect user region
def get_mirror_strategy(user_location):
    if user_location in ["CN", "China", "中国"]:
        return {
            "pip": "https://pypi.tuna.tsinghua.edu.cn/simple",
            "npm": "https://registry.npmmirror.com",
            "docker": "https://docker.mirrors.ustc.edu.cn",
            "go": "https://goproxy.cn,direct",
            "huggingface": "https://hf-mirror.com"
        }
    else:
        return {
            "pip": "https://pypi.org/simple",
            "npm": "https://registry.npmjs.org",
            "docker": "https://registry-1.docker.io",
            "go": "https://proxy.golang.org,direct",
            "huggingface": "https://huggingface.co"
        }
```

---

## 🔗 Resource Links

- **AI-SKILL**: https://github.com/badhope/AI-SKILL
- **PromptHub**: https://github.com/badhope/PromptHub
- **Mcp-Market**: https://github.com/badhope/Mcp-Market
- **API-Market**: https://github.com/badhope/API-Market
- **Global-Dev-Setup**: https://github.com/badhope/Global-Dev-Setup

---

*This guide is designed to help AI agents use the badhope development resource ecosystem more efficiently.*
*Resources are continuously updated, please check for the latest versions regularly.*
