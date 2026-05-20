# Command Reference

> **All available commands for AI-Dev-Config**

---

## 🎯 Quick Commands

These commands can be used in conversation with the AI agent:

| Command | Description | Example |
|---------|-------------|---------|
| `/help` | Show all available commands | `/help` |
| `/status` | Show current project status | `/status` |
| `/context` | Display full context block | `/context` |
| `/progress` | Show progress (X/5) | `/progress` |
| `/resources` | List configured resources | `/resources` |
| `/next` | What's the next step? | `/next` |
| `/restart` | Start fresh (with confirmation) | `/restart` |
| `/init` | Initialize resources | `/init` |
| `/check` | Run all checks | `/check` |
| `/save` | Save current context | `/save` |
| `/load` | Load saved context | `/load` |
| `/template` | Show available templates | `/template` |
| `/skill` | Search AI-SKILL | `/skill code-review` |
| `/tool` | Search Mcp-Market | `/tool browser` |
| `/api` | Search API-Market | `/api weather` |
| `/prompt` | Search PromptHub | `/prompt chat` |

---

## 📋 Command Details

### `/help`

Show all available commands with descriptions.

```
User: /help

AI:
## 📚 Available Commands

| Command | Description |
|---------|-------------|
| /help | Show this help |
| /status | Show project status |
| ... | ... |
```

---

### `/status`

Show current project status including:
- Project name and type
- Current progress
- Configured resources
- Last action
- Next action

```
User: /status

AI:
## 📊 Project Status

### [Project Name] | AI Agent | Progress: 2/5

**Environment:**
- ✅ Python 3.10
- ✅ Docker
- ⏳ Node.js

**Skills:**
- ✅ ai-agent-development
- ⏳ langchain-usage

**Last:** Completed environment setup
**Next:** Install Node.js, then load skills
```

---

### `/context`

Display the full context block.

```
User: /context

AI:
## 📊 Current Project Context

### Project Info
- Name: MyProject
- Type: AI Agent
- Created: 2026-05-20

### Configured Resources
- ✅ Environment: Python, Docker, Git
- ✅ Skills: ai-agent-development
- ⏳ Tools: filesystem (pending)
- ⏳ Prompts: None
- ⏳ APIs: None

### Progress
- [x] Requirement Analysis
- [x] Environment Configuration
- [ ] Architecture Design
- [ ] Development
- [ ] Testing

### Last Action
Completed Python and Docker installation

### Next Action
Install Node.js and configure filesystem tool
```

---

### `/progress`

Show just the progress bar.

```
User: /progress

AI:
## 📈 Progress: 🟩🟩⬜⬜⬜ (2/5)

- ✅ Requirement Analysis
- ✅ Environment Configuration
- ⏳ Architecture Design (Current)
- ⬜ Development
- ⬜ Testing
```

---

### `/resources`

List all configured resources.

```
User: /resources

AI:
## 📦 Configured Resources

### Environment (Global-Dev-Setup)
- ✅ Python 3.10.12
- ✅ Docker 24.0.5
- ✅ Git 2.40.0
- ⏳ Node.js (pending)
- ❌ PostgreSQL (not needed)

### Skills (AI-SKILL)
- ✅ ai-agent-development
- ✅ prompt-engineering
- ⏳ langchain-usage (pending)

### Tools (Mcp-Market)
- ✅ filesystem
- ⏳ github (pending)

### Prompts (PromptHub)
- ✅ agent-system-prompt
- ⏳ tool-use-prompt (pending)

### APIs (API-Market)
- ✅ OpenAI API
- ⏳ Weather API (pending)
```

---

### `/next`

Show what the next step is.

```
User: /next

AI:
## ➡️ Next Step

**Current:** Environment Configuration (2/5)
**Next:** Architecture Design (3/5)

**Actions Required:**
1. Complete Node.js installation
2. Load langchain-usage skill
3. Configure github MCP tool
4. Start architecture design

Ready to continue? (Y/N)
```

---

### `/restart`

Restart the project from scratch.

```
User: /restart

AI:
⚠️ This will clear all progress and start fresh.

**Current Project:** MyProject
**Progress:** 2/5

Are you sure you want to restart?
- Yes, restart
- No, keep current progress
- Save and restart
```

---

### `/init`

Initialize all resource repositories.

```
User: /init

AI:
## 🚀 Initializing Resources

Checking repositories...

□ AI-SKILL... ✅ Already cloned
□ PromptHub... ✅ Already cloned
□ Mcp-Market... ⏳ Cloning...
□ API-Market... ✅ Already cloned
□ Global-Dev-Setup... ✅ Already cloned

✅ All resources initialized!
```

---

### `/check`

Run all verification checks.

```
User: /check

AI:
## ✅ Running Checks

### Document Checks
- ✅ README.md exists
- ✅ IDENTITY.md exists
- ✅ WORKFLOW.md exists
- ✅ All documents valid

### Resource Checks
- ✅ AI-SKILL cloned
- ✅ PromptHub cloned
- ✅ Mcp-Market cloned
- ✅ API-Market cloned
- ✅ Global-Dev-Setup cloned

### Index Checks
- ✅ skills/index.json valid
- ✅ index.json valid
- ✅ servers-index.json valid
- ✅ api-database.json valid
- ✅ tool_registry.json valid

### Environment Checks
- ✅ Python 3.10+ installed
- ✅ Git installed
- ✅ Docker installed

**All checks passed!**
```

---

### `/template`

Show available development templates.

```
User: /template

AI:
## 📋 Available Templates

### AI Development
- `ai-ml-developer` - AI/Machine Learning
- `ai-agent-developer` - AI Agent
- `data-science` - Data Science

### Web Development
- `fullstack-developer` - Full-stack
- `frontend-developer` - Frontend
- `backend-developer` - Backend

### DevOps
- `devops-engineer` - DevOps
- `cloud-native-developer` - Cloud

### Other
- `mobile-developer` - Mobile
- `game-developer` - Game
- `blockchain-developer` - Blockchain

Usage: Select a template or say "use [template-name]"
```

---

### `/skill [query]`

Search AI-SKILL for skills.

```
User: /skill code-review

AI:
## 🔍 Skills Found: "code-review"

### 1. code-review
- **Category:** development
- **Description:** Professional code review skill
- **Path:** skills/development/code-review/SKILL.md

### 2. code-review-advanced
- **Category:** development
- **Description:** Advanced code review with security focus
- **Path:** skills/development/code-review-advanced/SKILL.md

Load a skill? (1/2)
```

---

### `/tool [query]`

Search Mcp-Market for tools.

```
User: /tool browser

AI:
## 🔍 Tools Found: "browser"

### 1. puppeteer
- **Description:** Browser automation with Puppeteer
- **Language:** TypeScript
- **Path:** servers/puppeteer/

### 2. playwright
- **Description:** Browser automation with Playwright
- **Language:** Python
- **Path:** servers/playwright/

Configure a tool? (1/2)
```

---

### `/api [query]`

Search API-Market for APIs.

```
User: /api weather

AI:
## 🔍 APIs Found: "weather"

### 1. OpenWeatherMap
- **Quality:** ⭐⭐⭐⭐⭐ (95)
- **Auth:** API Key
- **Category:** Weather

### 2. WeatherAPI
- **Quality:** ⭐⭐⭐⭐ (85)
- **Auth:** API Key
- **Category:** Weather

Use an API? (1/2)
```

---

### `/prompt [query]`

Search PromptHub for prompts.

```
User: /prompt chat

AI:
## 🔍 Prompts Found: "chat"

### 1. chat-assistant
- **Category:** AI
- **Description:** General chat assistant prompt

### 2. chat-customer-service
- **Category:** Business
- **Description:** Customer service chat prompt

Use a prompt? (1/2)
```

---

## 🔧 Admin Commands

### `/save`

Save current context to file.

```
User: /save

AI:
## 💾 Saving Context

Context saved to: .ai-dev-config/context.json

✅ Context saved successfully!
```

---

### `/load`

Load saved context from file.

```
User: /load

AI:
## 📂 Loading Context

Context loaded from: .ai-dev-config/context.json

**Project:** MyProject
**Progress:** 2/5
**Last Action:** Environment setup

✅ Context restored!
```

---

## 💡 Usage Tips

1. **Combine commands**: You can use multiple commands in one message
   ```
   /status
   /next
   ```

2. **Natural language**: Commands are optional, you can just ask naturally
   ```
   "What's the status?" → Same as /status
   "What's next?" → Same as /next
   ```

3. **Shortcuts**: Some commands have shortcuts
   ```
   /s → /status
   /p → /progress
   /r → /resources
   /n → /next
   ```

---

*Commands make interaction faster and more efficient.*
