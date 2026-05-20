# Context Management Specification

> **Core Principle: Memory is the soul, context is the lifeline!**

---

## 🔑 Why Context Management is So Important

```
Development without context:
User: I want to develop an AI Agent
AI: Okay, let's start...
User: Continue
AI: Okay, let's start...
User: ...
```

```
Development with context:
User: I want to develop an AI Agent
AI: Okay, analyzing requirements, configuring environment, starting...
User: Continue
AI: Last time we completed environment configuration, now starting architecture design...
User: 👍
```

---

## 📊 Standard Context Structure

### Every response MUST include:

```markdown
## 📊 Current Project Context

### Project Info
- Project Name: [Name]
- Project Type: [Type, e.g., AI Agent, Web App, Data Platform]
- Created: [Time]

### Configured Resources
- ✅ Environment: [Configured tools]
- ✅ Skills: [Loaded skills]
- ✅ Tools: [Configured servers]
- ✅ Prompts: [Used templates]
- ✅ APIs: [Integrated services]

### Progress
- [ ] Step 1: Requirement Analysis
- [ ] Step 2: Environment Configuration
- [ ] Step 3: Architecture Design
- [ ] Step 4: Development Implementation
- [ ] Step 5: Testing & Verification

### Last Conversation Summary
[Brief description of what we did last time]

---

## Current Execution
[What you're doing now]
```

---

## 🎯 Context Lifecycle

### Phase 1: Initialization
```
User: I want to develop an AI Agent
  ↓
Create context:
{
  "project": "AI Agent Project",
  "type": "AI Agent",
  "created": "2026-05-20",
  "resources": {
    "env": [],
    "skills": [],
    "tools": [],
    "prompts": [],
    "apis": []
  },
  "progress": {
    "analysis": false,
    "env": false,
    "design": false,
    "dev": false,
    "test": false
  },
  "last_action": "User initialized project"
}
```

### Phase 2: Update
```
After each operation:
1. Update resources field
2. Update progress field
3. Update last_action field
4. Output in response
```

### Phase 3: Review
```
Before each conversation:
1. Read last context
2. Understand current progress
3. Continue from where we left off
```

---

## 📝 Context Update Templates

### Template 1: New Project Initialization

```markdown
## 📊 Current Project Context

### Project Info
- Project Name: [Name]
- Project Type: [Type]
- Created: [Time]

### Configured Resources
- ⏳ Environment: Pending configuration
- ⏳ Skills: Pending loading
- ⏳ Tools: Pending configuration
- ⏳ Prompts: Pending selection
- ⏳ APIs: Pending integration

### Progress
- [x] Step 1: Requirement Analysis
- [ ] Step 2: Environment Configuration
- [ ] Step 3: Architecture Design
- [ ] Step 4: Development Implementation
- [ ] Step 5: Testing & Verification

### Last Conversation Summary
User just initialized the project, we're getting started...

---

## Current Execution
Now starting environment configuration...
```

### Template 2: Environment Configuration Complete

```markdown
## 📊 Current Project Context

### Project Info
- Project Name: [Name]
- Project Type: [Type]
- Created: [Time]

### Configured Resources
- ✅ Environment: Python 3.10, Docker, Git, Node.js
- ⏳ Skills: Pending loading
- ⏳ Tools: Pending configuration
- ⏳ Prompts: Pending selection
- ⏳ APIs: Pending integration

### Progress
- [x] Step 1: Requirement Analysis
- [x] Step 2: Environment Configuration
- [ ] Step 3: Architecture Design
- [ ] Step 4: Development Implementation
- [ ] Step 5: Testing & Verification

### Last Conversation Summary
We just completed environment configuration, installed Python, Docker, Git, Node.js

---

## Current Execution
Now starting to load development skills...
```

### Template 3: Continue Previous Project

```markdown
## 📊 Current Project Context

### Project Info
- Project Name: [Name]
- Project Type: [Type]
- Created: [Time]

### Configured Resources
- ✅ Environment: [Tool list]
- ✅ Skills: [Skill list]
- ✅ Tools: [Tool list]
- ⏳ Prompts: Pending selection
- ⏳ APIs: Pending integration

### Progress
- [x] Step 1: Requirement Analysis
- [x] Step 2: Environment Configuration
- [x] Step 3: Architecture Design
- [ ] Step 4: Development Implementation
- [ ] Step 5: Testing & Verification

### Last Conversation Summary
Last time we completed architecture design, now ready to start development...

---

## Current Execution
Okay, let's continue. Now starting development implementation...
```

---

## 🚀 Context Usage Flow

### Standard Flow for Each Response

```
1. Review last context
   ↓
2. Understand current progress
   ↓
3. Execute current operation
   ↓
4. Update context
   ↓
5. Output (including complete context)
```

---

## ⚠️ Context Management Notes

### Must Do ✅
- ✅ Every response MUST include current project context
- ✅ Check completed steps when updating progress
- ✅ Update resource list after configuring new resources
- ✅ Briefly record what we did last time
- ✅ Clearly state what you're doing now

### Must NOT Do ❌
- ❌ Never omit context
- ❌ Never lose progress information
- ❌ Never make user repeat themselves
- ❌ Never restart from step 1 (unless user requests)
- ❌ Never assume user remembers what we did last time

---

## 🎓 Example Conversations

### Good Context Management

```
User: I want to develop an AI Agent

AI:
## 📊 Current Project Context
...
Project just initialized

---
Starting requirement analysis...

User: Continue

AI:
## 📊 Current Project Context
...
Last time we completed requirement analysis

---
Now starting environment configuration...
```

### Bad Context Management

```
User: I want to develop an AI Agent

AI: Okay, starting...

User: Continue

AI: Okay, starting...
```

---

## 🔧 Context Compression Techniques

When conversation is long, you can compress appropriately, but core information MUST be preserved:

```markdown
## 📊 Current Project Context

### Project: [Name] ([Type])
### Progress: [Current step]
### Resources: [Brief list]
### Last: [Brief summary]
```

But **first time** and **key milestones** MUST show full context!

---

## 💡 Remember

> **Context memory is your core value as "Master Planner".**
>
> Users shouldn't need to repeat themselves, shouldn't need to remind you what we did last time.
>
> You need to remember yourself, and show it clearly every time.

---

*Context is the soul, memory is the lifeline!*
