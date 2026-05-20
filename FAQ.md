# Frequently Asked Questions (FAQ)

> **Common questions and answers about AI-Dev-Config**

---

## 🎯 General Questions

### Q1: What is AI-Dev-Config?

**A:** AI-Dev-Config is a configuration system that transforms any AI agent into a "Master Planner" - an intelligent development assistant that can:
- Configure development environments automatically
- Find and load appropriate skills, tools, and prompts
- Track project progress with persistent context
- Coordinate resources from 5 external repositories

---

### Q2: Is AI-Dev-Config a project to develop, or a tool to use?

**A:** It's a **tool to use** for developing other projects.

- ✅ **Default**: Use it to assist development of other projects
- ❌ **Only when explicitly requested**: Develop AI-Dev-Config itself

---

### Q3: What AI models/agents can use this?

**A:** Any AI agent that can:
- Read files from a repository
- Follow instructions in markdown
- Execute shell commands (optional)
- Maintain conversation context

**Tested with:**
- Claude (Anthropic)
- GPT-4 (OpenAI)
- Local LLMs with sufficient context
- Custom AI agents

---

### Q4: Do I need to clone all 5 resource repositories?

**A:** No! Clone only what you need:

| If you need... | Clone this |
|----------------|------------|
| Development skills | AI-SKILL |
| Prompt templates | PromptHub |
| Tool integration | Mcp-Market |
| Third-party APIs | API-Market |
| Environment setup | Global-Dev-Setup |

**Or use the init script to clone all at once:**
```bash
./init.sh
```

---

## 🚀 Getting Started

### Q5: How do I start using AI-Dev-Config?

**A:** Follow these steps:

1. **Give the repository URL to your AI agent**
   ```
   https://github.com/badhope/AI-Dev-Config
   ```

2. **AI agent reads the configuration**
   - Reads README.md
   - Reads IDENTITY.md
   - Reads WORKFLOW.md
   - etc.

3. **AI agent greets you and asks what you want**
   ```
   ✅ AI-Dev-Config Loaded!
   What would you like to do?
   1. Start a new project
   2. Continue previous project
   ...
   ```

4. **You respond and the work begins!**

---

### Q6: What if the AI agent doesn't understand the configuration?

**A:** Try these steps:

1. **Explicitly tell the AI to read specific files:**
   ```
   Please read IDENTITY.md and WORKFLOW.md first
   ```

2. **Provide the files directly:**
   ```
   Here's the IDENTITY.md content: [paste content]
   ```

3. **Use a different AI model:**
   - Some models have better instruction-following capabilities

---

### Q7: Can I use this without internet access?

**A:** Partially:

- ✅ **Can use**: If resources are pre-cloned locally
- ❌ **Cannot use**: If need to clone repositories or access APIs

**Solution:** Clone all resources beforehand:
```bash
./init.sh
```

---

## 📦 Resources

### Q8: What's in each resource repository?

**A:**

| Repository | Content | Size |
|------------|---------|------|
| AI-SKILL | 2,677+ AI skills | ~50MB |
| PromptHub | 80+ prompt templates | ~1MB |
| Mcp-Market | 438+ MCP servers | ~30MB |
| API-Market | 14,405+ API entries | ~20MB |
| Global-Dev-Setup | 187+ tools, 19 templates | ~5MB |

---

### Q9: How do I find a specific skill/tool/API?

**A:** Use the index files:

**For skills:**
```python
import json
with open('resources/AI-SKILL/skills/index.json') as f:
    skills = json.load(f)
    # Search for what you need
```

**Or use commands:**
```
/skill code-review
/tool browser
/api weather
```

---

### Q10: Can I add my own resources?

**A:** Yes! You can:

1. **Add to existing repositories** (if you have access)
2. **Create your own resource repository**
3. **Modify the configuration to point to your repos**

---

## 🔧 Configuration

### Q11: How do I change the AI's identity?

**A:** Edit `IDENTITY.md`:

```markdown
## 👤 Core Identity

**Name**: [Your Custom Name]

**Responsibilities**:
- [Your custom responsibilities]
```

---

### Q12: Can I customize the workflow?

**A:** Yes! Edit `WORKFLOW.md`:

- Add/remove phases
- Change the order
- Add custom checks
- Modify decision trees

---

### Q13: How do I add a new project type?

**A:** Add to `PROJECT_RESOURCES_MAP.md`:

```markdown
## My Custom Project

| Resource Type | Required Resources |
|--------------|-------------------|
| **Environment** | my-custom-template |
| **Skills** | my-custom-skill |
| **Tools** | my-custom-tool |
```

---

## 📊 Context & Memory

### Q14: Why is context so important?

**A:** Context ensures:
- ✅ Continuity between conversations
- ✅ No repeated work
- ✅ Clear progress tracking
- ✅ User doesn't need to repeat themselves

---

### Q15: What if context is lost?

**A:** Recovery options:

1. **Ask AI to restore:**
   ```
   /load
   ```

2. **Manually remind:**
   ```
   We were working on [project], at step [X]
   ```

3. **Start fresh:**
   ```
   /restart
   ```

---

### Q16: How long is context kept?

**A:** Depends on:
- AI model's context window
- Conversation length
- Whether you save explicitly

**Best practice:** Save frequently:
```
/save
```

---

## 🌐 Internationalization

### Q17: Is Chinese fully supported?

**A:** Yes! Core documents have Chinese versions:
- README.zh.md
- IDENTITY.zh.md
- WORKFLOW.zh.md
- CONTEXT_MANAGEMENT.zh.md

---

### Q18: Can I add other languages?

**A:** Yes! Create:
- README.[lang].md
- IDENTITY.[lang].md
- etc.

And update the language switcher in README.md.

---

## 🛡️ Security

### Q19: Is my data/API key safe?

**A:** AI-Dev-Config:
- ✅ Never stores real API keys
- ✅ Uses environment variables
- ✅ Shows only placeholders in examples
- ✅ Doesn't send data externally

**Your responsibility:**
- Use environment variables for secrets
- Don't paste real keys in chat
- Review generated code before running

---

### Q20: Can I use this in a corporate environment?

**A:** Yes, but check:
- [ ] Corporate policy allows external repositories
- [ ] No restricted data in project context
- [ ] Approved tools only
- [ ] Security review completed

---

## 🚨 Troubleshooting

### Q21: Resource clone failed. What do I do?

**A:** Try these:

1. **Check network:**
   ```bash
   ping github.com
   ```

2. **Use SSH:**
   ```bash
   git clone git@github.com:badhope/AI-SKILL.git
   ```

3. **Use mirror (China):**
   ```bash
   git clone https://github.com.cnpmjs.org/badhope/AI-SKILL.git
   ```

4. **Manual download:**
   - Download ZIP from GitHub
   - Extract to resources/

---

### Q22: AI keeps forgetting context. Help!

**A:** Possible causes:

1. **Context window full:**
   - Use `/save` frequently
   - Start new conversation and `/load`

2. **AI model limitation:**
   - Use model with larger context
   - Summarize older context

3. **Configuration not followed:**
   - Remind AI to read IDENTITY.md
   - Show EXAMPLE_CONVERSATIONS.md

---

### Q23: Tool installation failed. What now?

**A:** Check:

1. **Permissions:**
   ```bash
   sudo [command]
   ```

2. **System requirements:**
   - Check OS version
   - Check available disk space

3. **Alternative installation:**
   - Use Docker
   - Use different package manager

4. **Skip if not critical:**
   - Mark as ❌
   - Continue with alternatives

---

## 🎓 Advanced

### Q24: Can I use multiple AI agents with this?

**A:** Yes! Each agent can:
- Use the same AI-Dev-Config
- Work on different projects
- Share cloned resources

**Note:** Context is per-conversation, not shared.

---

### Q25: How do I extend this for my team?

**A:** Options:

1. **Fork the repository:**
   - Add team-specific configurations
   - Add internal resources

2. **Create internal version:**
   - Host on internal Git server
   - Add company-specific templates

3. **Use as template:**
   - Create new repo from this
   - Customize for team needs

---

### Q26: Can I automate the entire workflow?

**A:** Partially:

**Automatable:**
- Resource cloning
- Environment setup
- Tool installation
- Progress tracking

**Requires human:**
- Requirement decisions
- Architecture choices
- Code review
- Testing approval

---

## 📝 Contributing

### Q27: How do I contribute improvements?

**A:**

1. Fork the repository
2. Make improvements
3. Test thoroughly
4. Submit pull request

**Areas for contribution:**
- New project templates
- Additional examples
- Bug fixes
- Documentation improvements
- Translation improvements

---

### Q28: Can I report bugs or request features?

**A:** Yes! Create an issue on GitHub:
- Describe the problem/feature
- Provide steps to reproduce
- Include context/environment info

---

## 💡 Tips & Tricks

### Q29: What's the fastest way to start?

**A:**
```bash
# 1. Clone and init
git clone https://github.com/badhope/AI-Dev-Config
cd AI-Dev-Config
./init.sh

# 2. Tell AI to read config
# 3. Start working!
```

---

### Q30: Any productivity tips?

**A:**

1. **Use commands:**
   ```
   /status, /next, /progress
   ```

2. **Save frequently:**
   ```
   /save
   ```

3. **Use templates:**
   - Don't start from scratch
   - Customize existing templates

4. **Batch operations:**
   - Install multiple tools at once
   - Load multiple skills together

5. **Keep context concise:**
   - Summarize when needed
   - Focus on current step

---

*More questions? Check TROUBLESHOOTING.md or create an issue on GitHub.*
