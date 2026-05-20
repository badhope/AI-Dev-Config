# Intent Correction Rules

> **Speech-to-intent correction rules for AI agents**

---

## 🎯 Purpose

This document provides intent correction rules to help AI agents better understand user speech patterns, especially when there may be pronunciation errors or ambiguous expressions.

---

## 🔍 Common Pronunciation Errors and Corrections

### English to English

| Input | Correction | Context |
|-------|------------|---------|
| "code review" | code review | Correct as-is |
| "cold review" | code review | Common mispronunciation |
| "code rev" | code review | Abbreviation |
| "PRD document" | PRD document | Correct as-is |
| "PDR document" | PRD document | Common reversal |
| "OKR goal" | OKR goal | Correct as-is |
| "OCR goal" | OKR goal | Pronunciation confusion |
| "SEO audit" | SEO audit | Correct as-is |
| "CEO audit" | SEO audit | Pronunciation confusion |
| "API integration" | API integration | Correct as-is |
| "API intergration" | API integration | Typo correction |
| "Docker" | Docker | Correct as-is |
| "Doc ker" | Docker | Pronunciation split |
| "Python" | Python | Correct as-is |
| "Pi thon" | Python | Pronunciation split |
| "JavaScript" | JavaScript | Correct as-is |
| "Java Script" | JavaScript | Pronunciation split |

### Chinese to English Mapping

| Chinese Input | English Translation | Context |
|---------------|--------------------|---------|
| "代码审查" | code review | Code review |
| "代码检查" | code review | Code inspection |
| "PRD文档" | PRD document | Product requirements document |
| "产品需求文档" | PRD document | Product requirements document |
| "OKR目标" | OKR goal | OKR objectives |
| "目标管理" | OKR goal | Goal management |
| "SEO审计" | SEO audit | SEO audit |
| "搜索引擎优化" | SEO audit | Search engine optimization |
| "API接口" | API integration | API integration |
| "应用程序接口" | API integration | Application programming interface |
| "安装Docker" | install Docker | Install Docker |
| "容器化" | Docker/Kubernetes | Containerization |
| "Python环境" | Python environment | Python environment |
| "Python开发" | Python development | Python development |
| "前端开发" | frontend development | Frontend development |
| "后端开发" | backend development | Backend development |
| "全栈开发" | fullstack development | Full-stack development |
| "人工智能" | AI development | Artificial intelligence |
| "机器学习" | machine learning | Machine learning |
| "数据科学" | data science | Data science |
| "开发环境" | development environment | Development environment |
| "环境配置" | environment configuration | Environment configuration |

---

## 🧠 Intent Inference Rules

### Rule 1: Project Type Detection

**Keywords for AI/ML Projects:**
- AI, artificial intelligence, machine learning, ML, deep learning
- Agent, intelligent agent, AI agent
- Data science, data analysis, big data
- Neural network, model, training

**Keywords for Web Development:**
- Website, web app, frontend, backend, fullstack
- React, Vue, Angular, Next.js, Node.js
- HTML, CSS, JavaScript, TypeScript
- API, REST, GraphQL

**Keywords for Mobile Development:**
- Mobile app, iOS, Android
- Flutter, React Native, Swift, Kotlin

**Keywords for DevOps:**
- Docker, Kubernetes, container
- CI/CD, pipeline, automation
- Cloud, AWS, Azure, GCP
- Infrastructure, deployment

---

### Rule 2: Action Detection

**Action Keywords:**
- "开发", "创建", "构建", "make", "build", "create", "develop" → Development
- "配置", "安装", "setup", "install", "configure" → Configuration
- "修复", "调试", "debug", "fix", "repair" → Debugging
- "审查", "审核", "review", "audit" → Review
- "优化", "改进", "optimize", "improve" → Optimization
- "设计", "架构", "design", "architecture" → Design

---

### Rule 3: Context Awareness

**When user says "继续" or "continue":**
- Look for previous context
- Continue from last recorded progress
- If no context exists, ask for clarification

**When user says "新项目" or "new project":**
- Start fresh context
- Ask for project name and type
- Initialize new project flow

**When user says "帮我" or "help me":**
- User needs assistance
- Analyze what they need help with
- Provide options or ask clarifying questions

---

## 📝 Common User Expressions and Intent Mapping

| User Expression | Detected Intent | Recommended Action |
|----------------|----------------|-------------------|
| "我要开发一个AI应用" | Start AI project | Go to Phase 1 (Requirement Confirmation) |
| "帮我配置开发环境" | Configure environment | Go to Global-Dev-Setup |
| "安装Python" | Install tool | Search Global-Dev-Setup for Python |
| "继续之前的项目" | Continue project | Restore context and continue |
| "代码审查一下" | Code review | Go to AI-SKILL for code-review |
| "写个PRD" | Write PRD | Go to AI-SKILL for prd-writer |
| "需要一个API" | API integration | Go to API-Market |
| "浏览器自动化" | Browser automation | Go to Mcp-Market for puppeteer |
| "数据库连接" | Database integration | Go to Mcp-Market for database |
| "优化一下" | Optimization | Ask for specific area to optimize |

---

## ⚠️ Ambiguity Handling

### When intent is unclear:
1. Ask clarifying questions
2. Provide options for user to choose from
3. Reference previous conversation history
4. Make reasonable assumptions based on context

### Example: User says "我需要帮助"
**Response:**
```
## 🤔 Could you be more specific?

I'd be happy to help! Could you tell me what you need help with?

Options:
1. 🎯 Start a new project
2. 🔧 Configure development environment
3. 🛠️ Install a specific tool
4. 📋 Review code or documents
5. 🤔 Something else

Please let me know!
```

---

## 💡 Best Practices

1. **Listen carefully** - Pay attention to keywords and context
2. **Be proactive** - Ask clarifying questions when unsure
3. **Use context** - Reference previous conversations
4. **Provide options** - Give user clear choices
5. **Be flexible** - Handle variations in user expressions

---

*Intent correction is an ongoing learning process. Update these rules based on user feedback.*
