# Best Practices

> **Guidelines for effective use of AI-Dev-Config**

---

## 🎯 Core Principles

### 1. Always Start with Context

**❌ Wrong:**
```
User: Continue
AI: Okay, let's continue...
```

**✅ Right:**
```
User: Continue
AI:
## 📊 Project Context
### [Project] | AI Agent | Progress: 2/5
...
---
Continuing from where we left off...
```

---

### 2. Never Assume, Always Verify

**❌ Wrong:**
```
AI: I'll install Docker now...
[Assumes Docker is not installed]
```

**✅ Right:**
```
AI: Let me check if Docker is installed...
[Checks first]
→ Docker is already installed!
→ Skipping installation
```

---

### 3. Ask Before Major Actions

**❌ Wrong:**
```
AI: Installing Python, Node.js, Docker, PostgreSQL...
[Installs everything without asking]
```

**✅ Right:**
```
AI: I need to install:
- Python 3.10
- Node.js 20
- Docker

Proceed? (Y/N)
```

---

### 4. Update Context After Every Action

**❌ Wrong:**
```
AI: Python installed successfully!
[Context not updated]
```

**✅ Right:**
```
AI: Python installed successfully!

## 📊 Context Updated
- Environment: ✅ Python 3.10 | ⏳ Node.js | ⏳ Docker
- Progress: 2/5 → 2/5 (still configuring)
```

---

## 📋 Communication Best Practices

### Clear and Structured

**✅ Use:**
- Headers for sections
- Bullet points for lists
- Tables for comparisons
- Code blocks for commands
- Status icons (✅/⏳/❌)

**❌ Avoid:**
- Wall of text
- Unstructured paragraphs
- Missing status indicators

---

### Progressive Disclosure

**✅ Start Simple:**
```
AI: I found 5 relevant skills:
1. code-review (Recommended)
2. code-review-advanced
3. security-audit
...

Show details for all? (Y/N)
```

**❌ Overwhelming:**
```
AI: Here are all 50 skills with full descriptions...
[Too much information at once]
```

---

### Confirm Understanding

**✅ Repeat Back:**
```
User: I want to build a chatbot with RAG

AI: Let me confirm:
- Project type: AI Agent
- Main feature: Chatbot with RAG
- Technology: LangChain (recommended)

Is this correct?
```

---

## 🔧 Resource Management Best Practices

### Check Before Clone

**✅ Right:**
```python
if not exists("resources/AI-SKILL"):
    clone("AI-SKILL")
else:
    print("AI-SKILL already exists")
```

**❌ Wrong:**
```python
clone("AI-SKILL")  # May fail or duplicate
```

---

### Use Appropriate Mirrors

**✅ For China users:**
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
npm install --registry=https://registry.npmmirror.com
```

**✅ For Global users:**
```bash
pip install
npm install
```

---

### Verify After Install

**✅ Right:**
```bash
# Install
pip install package

# Verify
python -c "import package; print(package.__version__)"
```

---

## 📊 Context Management Best Practices

### Complete Information

**✅ Include all:**
```markdown
## 📊 Project Context

### Project Info
- Name: [Required]
- Type: [Required]
- Created: [Required]

### Resources
- Environment: [Required]
- Skills: [Required]
- Tools: [Required]
- Prompts: [Required]
- APIs: [Required]

### Progress
- [All 5 steps]

### Last Action
[Required]

### Next Action
[Required]
```

---

### Consistent Format

**✅ Use same template every time:**
```
## 📊 Project Context
### [Name] | [Type] | Progress: X/5
- Environment: ...
- Skills: ...
...
```

**❌ Don't change format:**
```
# Project: Name
Type: Type
Progress: X out of 5
[Inconsistent formatting]
```

---

## 🚀 Performance Best Practices

### Shallow Clone

**✅ Fast:**
```bash
git clone --depth 1 https://github.com/badhope/AI-SKILL.git
```

**❌ Slow:**
```bash
git clone https://github.com/badhope/AI-SKILL.git
# Downloads entire history
```

---

### Parallel Operations

**✅ When possible:**
```python
# Clone multiple repos in parallel
await asyncio.gather(
    clone("AI-SKILL"),
    clone("PromptHub"),
    clone("Mcp-Market")
)
```

---

### Cache Results

**✅ Cache:**
```python
# Cache index file
if not cache.exists("skills_index"):
    cache["skills_index"] = load_index()

skills = cache["skills_index"]
```

---

## 🛡️ Security Best Practices

### Never Hardcode Secrets

**❌ Wrong:**
```python
API_KEY = "sk-xxxxx"  # Never do this!
```

**✅ Right:**
```python
import os
API_KEY = os.environ.get("OPENAI_API_KEY")
```

---

### Validate User Input

**✅ Right:**
```python
project_name = input("Project name: ")
if not is_valid_name(project_name):
    raise ValueError("Invalid project name")
```

---

### Sanitize Commands

**✅ Right:**
```python
import shlex
safe_cmd = shlex.quote(user_input)
subprocess.run(f"echo {safe_cmd}", shell=True)
```

---

## 📝 Documentation Best Practices

### Keep Updated

**✅ Update docs when:**
- Adding new features
- Changing behavior
- Fixing bugs
- Adding new resources

---

### Use Examples

**✅ Show, don't just tell:**
```markdown
### How to use

```python
# Example usage
result = search_skill("code-review")
```
```

---

### Link Related

**✅ Cross-reference:**
```markdown
See also:
- [WORKFLOW.md](./WORKFLOW.md) for process
- [RESOURCES.md](./RESOURCES.md) for resources
```

---

## 🔄 Recovery Best Practices

### Save Progress Frequently

**✅ After each major step:**
```python
save_context()
```

---

### Provide Recovery Options

**✅ Right:**
```
⚠️ Context lost. Options:
1. Restore from last save
2. Describe current state
3. Start fresh
```

---

### Learn from Errors

**✅ Right:**
```python
try:
    install_tool(name)
except Exception as e:
    log_error(e)
    suggest_alternative(name)
```

---

## 🎓 Learning Best Practices

### Start Small

**✅ Recommended path:**
```
1. Simple project first
2. Learn the workflow
3. Gradually increase complexity
```

---

### Use Templates

**✅ Right:**
```
Start with: ai-agent-developer template
Then customize as needed
```

---

### Ask Questions

**✅ Right:**
```
AI: I'm not sure about X. Can you clarify?
```

**❌ Wrong:**
```
AI: [Assumes and proceeds incorrectly]
```

---

## 📊 Quality Metrics

### Track These

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Context accuracy | 100% | Every response has context |
| Resource hit rate | >90% | Found what was needed |
| User satisfaction | High | User feedback |
| Error rate | <5% | Errors / Total actions |
| Recovery rate | >95% | Recovered / Lost contexts |

---

## ✅ Self-Check Before Each Response

```
□ Context included?
□ Progress updated?
□ Resources status correct?
□ Last action noted?
□ Next action clear?
□ User confirmation asked (if needed)?
□ No assumptions made?
□ No secrets exposed?
□ Format consistent?
□ Links working?
```

---

*Following these best practices ensures smooth, efficient, and secure development.*
