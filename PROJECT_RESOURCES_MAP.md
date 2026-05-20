# Project Resources Mapping

> **Complete guide: Which resources to use for different project types**

---

## 🎯 How to Use This Guide

When user specifies a project type, you MUST:

1. **Identify project category** - Match user's description to a project type below
2. **Extract required resources** - Get the complete resource list for that project
3. **Check what exists** - Verify which resources are already configured
4. **Configure missing** - Download and configure any missing resources
5. **Initialize context** - Start tracking project progress

---

## 🤖 AI Agent Projects

### Full AI Agent Development

**Description**: Building intelligent agents with LLM, tool use, memory, and autonomous capabilities

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `ai-agent-developer` template, Python 3.10+, Docker, Git | 🔴 Required |
| **Skills** | `ai-agent-development`, `langchain-usage`, `prompt-engineering` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |
| **Tools** | `postgresql`, `redis` | 🟡 Recommended |
| **Prompts** | `agent-system-prompt`, `tool-use-prompt` | 🔴 Required |
| **APIs** | `openai` or `claude` or `qwen` | 🔴 Required |

**Optional Enhancements**:
- Browser automation: `puppeteer`, `playwright`
- Search: `tavily`, `brave-search`
- Cloud storage: AWS S3, Azure Blob

### Conversational AI / Chatbot

**Description**: Building chatbots with natural language understanding

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `ai-ml-developer` template, Python 3.10+, Node.js | 🔴 Required |
| **Skills** | `llm-integration`, `conversation-design` | 🔴 Required |
| **Tools** | `filesystem`, `mongodb` | 🔴 Required |
| **Prompts** | `chat-prompt-template` | 🔴 Required |
| **APIs** | LLM API (OpenAI/Claude/etc.) | 🔴 Required |

### RAG (Retrieval Augmented Generation)

**Description**: Building knowledge base Q&A systems

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `data-science` template, Python 3.10+, Vector DB | 🔴 Required |
| **Skills** | `rag-implementation`, `vector-search` | 🔴 Required |
| **Tools** | `filesystem`, `postgresql` (with pgvector) | 🔴 Required |
| **Prompts** | `rag-prompt-template` | 🔴 Required |
| **APIs** | LLM API, Embedding API | 🔴 Required |

---

## 🌐 Web Development Projects

### Full-Stack Web Application

**Description**: Complete web application with frontend and backend

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `fullstack-developer` template, Node.js, Docker | 🔴 Required |
| **Skills** | `fullstack-development`, `api-design`, `code-review` | 🔴 Required |
| **Tools** | `filesystem`, `github`, `postgresql` or `mongodb` | 🔴 Required |
| **Prompts** | `fullstack-prompt`, `code-explanation` | 🟡 Recommended |
| **APIs** | Database APIs, Auth APIs | 🔴 Required |

### Frontend Only

**Description**: Single-page applications, static sites, React/Vue apps

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `frontend-developer` template, Node.js, npm/yarn | 🔴 Required |
| **Skills** | `react-development` or `vue-development`, `css-layout` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |
| **Prompts** | `frontend-prompt`, `ui-design-prompt` | 🟡 Recommended |

### Backend API Only

**Description**: REST/GraphQL API development

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `backend-developer` template, Python/Node.js, Docker | 🔴 Required |
| **Skills** | `api-design`, `database-design`, `security-best-practices` | 🔴 Required |
| **Tools** | `filesystem`, `github`, `postgresql` or `mongodb` | 🔴 Required |
| **Prompts** | `api-design-prompt`, `code-review-prompt` | 🟡 Recommended |
| **APIs** | Database driver APIs | 🔴 Required |

---

## 📊 Data Engineering Projects

### Data Pipeline

**Description**: ETL pipelines, data processing, streaming

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `data-engineering` template, Python 3.10+, Spark | 🔴 Required |
| **Skills** | `etl-development`, `spark-programming`, `data-quality` | 🔴 Required |
| **Tools** | `filesystem`, `postgresql`, `mongodb`, `kafka` | 🔴 Required |
| **Prompts** | `data-pipeline-prompt` | 🟡 Recommended |
| **APIs** | Data source APIs, Storage APIs | 🔴 Required |

### Data Science / ML

**Description**: Machine learning, statistical analysis, visualization

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `data-science` template, Python 3.10+, Jupyter | 🔴 Required |
| **Skills** | `ml-modeling`, `data-visualization`, `statistics` | 🔴 Required |
| **Tools** | `filesystem`, `postgresql` | 🔴 Required |
| **Prompts** | `ml-prompt-template`, `data-analysis-prompt` | 🟡 Recommended |
| **APIs** | ML model APIs, Data APIs | 🟡 Recommended |

### Big Data Processing

**Description**: Large-scale data processing with Hadoop/Spark

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `big-data-engineer` template, Hadoop, Spark, Kafka | 🔴 Required |
| **Skills** | `hadoop-administration`, `spark-optimization` | 🔴 Required |
| **Tools** | `filesystem`, `postgresql`, `kafka`, `hive` | 🔴 Required |
| **Prompts** | `big-data-prompt` | 🟡 Recommended |

---

## 📱 Mobile Development Projects

### Cross-Platform App

**Description**: Flutter or React Native applications

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `mobile-developer` template, Flutter/React Native SDK | 🔴 Required |
| **Skills** | `flutter-development` or `react-native-development` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |
| **Prompts** | `mobile-ui-prompt` | 🟡 Recommended |
| **APIs** | Backend API, Push notification API | 🔴 Required |

### Native iOS/Android

**Description**: Native mobile app development

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `mobile-developer` template, Xcode/Android Studio | 🔴 Required |
| **Skills** | `ios-development` or `android-development` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |

---

## ☁️ DevOps / Cloud Projects

### Container Orchestration

**Description**: Kubernetes, Docker Swarm, microservices

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `devops-engineer` template, Docker, Kubernetes, Helm | 🔴 Required |
| **Skills** | `kubernetes-deployment`, `docker-optimization`, `ci-cd-pipeline` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |
| **Prompts** | `devops-prompt`, `kubernetes-prompt` | 🟡 Recommended |

### Cloud Infrastructure (AWS/GCP/Azure)

**Description**: Infrastructure as Code, cloud resource management

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `cloud-native-developer` template, Terraform, CLI tools | 🔴 Required |
| **Skills** | `terraform-development`, `aws-services`, `security-best-practices` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |
| **Prompts** | `iac-prompt`, `cloud-architecture-prompt` | 🟡 Recommended |

---

## 🎮 Game Development Projects

### Indie Game

**Description**: 2D/3D game development

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `game-developer` template, Unity/Unreal/Godot | 🔴 Required |
| **Skills** | `game-design`, `unity-development` or `godot-development` | 🔴 Required |
| **Tools** | `filesystem`, `github` | 🔴 Required |
| **Prompts** | `game-design-prompt` | 🟡 Recommended |

---

## 🔐 Security Projects

### Security Audit

**Description**: Security testing, vulnerability assessment

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `security-engineer` template, Kali Linux tools | 🔴 Required |
| **Skills** | `penetration-testing`, `vulnerability-assessment` | 🔴 Required |
| **Tools** | `filesystem`, `owasp-zap`, `nmap` | 🔴 Required |
| **Prompts** | `security-audit-prompt` | 🟡 Recommended |

### Security Development

**Description**: Building secure applications

| Resource Type | Required Resources | Priority |
|--------------|-------------------|----------|
| **Environment** | `security-engineer` template | 🔴 Required |
| **Skills** | `secure-coding`, `cryptography`, `auth-implementation` | 🔴 Required |
| **Tools** | `filesystem`, `sonarqube` | 🔴 Required |
| **Prompts** | `secure-coding-prompt` | 🟡 Recommended |

---

## 🏗️ Other Specialized Projects

### Blockchain / Web3

| Resource Type | Required Resources |
|--------------|-------------------|
| **Environment** | `blockchain-developer` template, Node.js, Solidity |
| **Skills** | `smart-contract-development`, `web3-integration` |
| **Tools** | `filesystem`, `github`, `hardhat` |
| **APIs** | Blockchain node API, Oracle API |

### IoT (Internet of Things)

| Resource Type | Required Resources |
|--------------|-------------------|
| **Environment** | `iot-developer` template, Python, Arduino/C++ |
| **Skills** | `embedded-systems`, `mqtt-protocol` |
| **Tools** | `filesystem`, `github` |
| **APIs** | IoT platform API, Message broker API |

### Embedded Systems

| Resource Type | Required Resources |
|--------------|-------------------|
| **Environment** | `embedded-developer` template, C/C++, cross-compiler |
| **Skills** | `c-programming`, `hardware-interfacing` |
| **Tools** | `filesystem`, `github` |
| **APIs** | Hardware SDK APIs |

### QA / Testing

| Resource Type | Required Resources |
|--------------|-------------------|
| **Environment** | `qa-engineer` template, Python, testing frameworks |
| **Skills** | `test-automation`, `performance-testing` |
| **Tools** | `filesystem`, `github`, `selenium`, `playwright` |
| **Prompts** | `test-case-prompt` |

---

## 🔄 Quick Reference: Resource Priority Levels

| Symbol | Meaning | Action Required |
|--------|---------|----------------|
| 🔴 | Required | MUST configure before starting development |
| 🟡 | Recommended | Should configure for better results |
| 🟢 | Optional | Configure if needed for specific features |

---

## 📋 Resource Configuration Checklist

When starting any project, follow this checklist:

```
项目: [项目名称]
类型: [项目类型]

□ 环境配置 (Global-Dev-Setup)
  □ [ ] 模板: [选择的模板]
  □ [ ] 基础工具: Git, Docker
  □ [ ] 项目特定工具: [列出]

□ AI 技能 (AI-SKILL)
  □ [ ] 核心技能 1
  □ [ ] 核心技能 2
  □ [ ] 推荐技能

□ MCP 工具 (Mcp-Market)
  □ [ ] 必需工具
  □ [ ] 推荐工具

□ 提示词 (PromptHub)
  □ [ ] 系统提示词
  □ [ ] 任务提示词

□ API (API-Market)
  □ [ ] 主要 API
  □ [ ] 辅助 API
```

---

## 💡 Tips for Resource Selection

1. **Start with Required** - Always configure required resources first
2. **Add Recommended** - Then add recommended resources
3. **Check Existing** - Don't reconfigure already configured resources
4. **Consider Scale** - Larger projects may need more resources
5. **Plan for Growth** - Leave room for optional enhancements

---

*This mapping is a starting guide. Adjust based on specific project requirements.*
