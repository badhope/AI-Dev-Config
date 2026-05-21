# Troubleshooting Guide

> **Solutions to common problems**

---

## 🛠️ Resource Repository Issues

### Problem 1: Git Clone Failed

**Symptoms:**
- `git clone` command fails
- Timeout errors
- Network unreachable

**Solutions:**

1. **Check network connection**
   ```bash
   ping github.com
   ```

2. **Try SSH instead of HTTPS**
   ```bash
   # Instead of:
   git clone https://github.com/badhope/AI-SKILL.git
   
   # Try:
   git clone git@github.com:badhope/AI-SKILL.git
   ```

3. **Use GitHub token (securely)**
   ```bash
   # Option 1: Use Git credential helper (RECOMMENDED)
   git -c credential.helper="!f() { echo username=x-access-token; echo password=YOUR_TOKEN_HERE; }; f" clone https://github.com/badhope/AI-SKILL.git
   
   # Option 2: Use SSH (MOST SECURE)
   git clone git@github.com:badhope/AI-SKILL.git
   ```

4. **Manual download**
   - Visit: `https://github.com/badhope/[REPO]/archive/main.zip`
   - Extract and place in `resources/[REPO]/`

5. **Ask user to provide locally cloned version**

---

### Problem 2: Index File Not Found

**Symptoms:**
- JSON file read error
- File does not exist

**Solutions:**

1. **Check file path**
   ```bash
   ls -la resources/[REPO]/
   ```

2. **Re-clone if corrupted**
   ```bash
   rm -rf resources/[REPO]
   git clone https://github.com/badhope/[REPO].git resources/[REPO]
   ```

3. **Fetch from GitHub raw**
   - Use web fetch to get raw content
   - `https://raw.githubusercontent.com/badhope/[REPO]/main/[INDEX_FILE]`

---

### Problem 3: Repository Not Cloned

**Symptoms:**
- Directory doesn't exist
- Empty directory

**Solutions:**

1. **Run initialization script**
   ```bash
   # Bash
   ./init.sh
   
   # Python
   python3 init.py
   ```

2. **Manual clone**
   ```bash
   mkdir -p resources
   cd resources
   git clone --depth 1 https://github.com/badhope/[REPO].git
   ```

---

## 💻 Environment Configuration Issues

### Problem 4: Tool Installation Failed

**Symptoms:**
- Installation command fails
- Permission denied
- Package not found

**Solutions:**

1. **Check permissions**
   ```bash
   # Use sudo if needed
   sudo apt install [package]
   
   # Or use user installation
   pip install --user [package]
   ```

2. **Check system requirements**
   ```bash
   # Check OS version
   uname -a
   
   # Check architecture
   uname -m
   ```

3. **Try alternative installation**
   ```bash
   # For Python
   pip3 install [package]
   python3 -m pip install [package]
   
   # For Node.js
   npm install -g [package]
   yarn global add [package]
   ```

4. **Use Docker alternative**
   ```bash
   docker run --rm [image] [command]
   ```

5. **Check mirror sources (China)**
   ```bash
   # pip
   pip install [package] -i https://pypi.tuna.tsinghua.edu.cn/simple
   
   # npm
   npm install [package] --registry=https://registry.npmmirror.com
   ```

---

### Problem 5: Python Version Issue

**Symptoms:**
- Python not found
- Wrong Python version
- Module import errors

**Solutions:**

1. **Check Python version**
   ```bash
   python3 --version
   python --version
   which python3
   ```

2. **Install specific version**
   ```bash
   # Ubuntu/Debian
   sudo apt install python3.10
   
   # macOS
   brew install python@3.10
   
   # Windows (use python.org installer)
   ```

3. **Use virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install [package]
   ```

---

### Problem 6: Docker Not Available

**Symptoms:**
- Docker command not found
- Docker daemon not running

**Solutions:**

1. **Install Docker**
   ```bash
   # Ubuntu/Debian
   curl -fsSL https://get.docker.com | sh
   
   # macOS
   brew install --cask docker
   ```

2. **Start Docker daemon**
   ```bash
   sudo systemctl start docker
   sudo dockerd &
   ```

3. **Use alternative (Podman)**
   ```bash
   podman run [image] [command]
   ```

---

## 🤖 AI Agent Issues

### Problem 7: API Key Not Set

**Symptoms:**
- "API key not found" error
- Authentication failed

**Solutions:**

1. **Set environment variable**
   ```bash
   export OPENAI_API_KEY="sk-..."
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```

2. **Use .env file**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=sk-..." > .env
   
   # Load in Python
   from dotenv import load_dotenv
   load_dotenv()
   ```

3. **Check API key validity**
   - Verify key format
   - Check expiration
   - Verify permissions

---

### Problem 8: Model Not Available

**Symptoms:**
- "Model not found" error
- Quota exceeded

**Solutions:**

1. **Check available models**
   ```python
   import openai
   models = openai.Model.list()
   ```

2. **Use alternative model**
   ```python
   # Instead of gpt-4
   model="gpt-3.5-turbo"
   
   # Or claude-3-haiku
   model="claude-3-haiku-20240307"
   ```

3. **Wait for quota reset**
   - Check rate limits
   - Implement retry logic
   - Consider upgrading plan

---

## 📊 Context Management Issues

### Problem 9: Context Lost

**Symptoms:**
- AI doesn't remember previous conversation
- Starting from scratch
- User has to repeat information

**Solutions:**

1. **Restore from last known state**
   ```
   User: Continue the [project name] project
   
   AI: I see context was lost. Based on what we discussed:
   - Project: [name]
   - Type: [type]
   - Last step: [step]
   
   Can you confirm this is correct?
   ```

2. **Request context recovery**
   ```
   ⚠️ Context lost. Please remind me:
   1. Project name?
   2. Project type?
   3. What step were we at?
   ```

3. **Start fresh (if necessary)**
   ```
   Say "New project" to start fresh
   ```

---

### Problem 10: Progress Tracking Error

**Symptoms:**
- Progress seems wrong
- Resources marked incorrectly
- Duplicate work

**Solutions:**

1. **Verify current state**
   ```
   /status
   ```

2. **Manual correction**
   ```
   User: We're actually at step 3, not step 2
   
   AI: Corrected! Progress updated to Step 3/5
   ```

3. **Reset if needed**
   ```
   /restart
   ```

---

## 🌐 Network Issues

### Problem 11: Slow Network

**Symptoms:**
- Long clone times
- Timeouts
- Partial downloads

**Solutions:**

1. **Use shallow clone**
   ```bash
   git clone --depth 1 [url]
   ```

2. **Use mirrors (China)**
   ```bash
   # GitHub mirror
   git clone https://github.com.cnpmjs.org/[repo].git
   
   # pip mirror
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

3. **Resume interrupted clone**
   ```bash
   git clone --depth 1 [url]
   cd [repo]
   git fetch --unshallow
   ```

---

### Problem 12: Proxy Issues

**Symptoms:**
- Connection refused
- SSL errors
- Certificate problems

**Solutions:**

1. **Set proxy**
   ```bash
   export http_proxy="http://proxy:8080"
   export https_proxy="http://proxy:8080"
   ```

2. **Disable SSL verification (not recommended)**
   ```bash
   git config --global http.sslVerify false
   ```

3. **Use SSH instead**
   ```bash
   git clone git@github.com:user/repo.git
   ```

---

## 📁 File System Issues

### Problem 13: Permission Denied

**Symptoms:**
- Cannot create directory
- Cannot write file
- Access denied

**Solutions:**

1. **Check permissions**
   ```bash
   ls -la [directory]
   ```

2. **Fix permissions**
   ```bash
   chmod 755 [directory]
   chmod 644 [file]
   ```

3. **Use sudo if necessary**
   ```bash
   sudo mkdir [directory]
   sudo chown $USER:$USER [directory]
   ```

---

### Problem 14: Disk Full

**Symptoms:**
- No space left
- Write failed
- Clone failed

**Solutions:**

1. **Check disk space**
   ```bash
   df -h
   ```

2. **Clean up**
   ```bash
   docker system prune -a
   rm -rf ~/.cache/*
   apt clean
   ```

3. **Remove unnecessary repos**
   ```bash
   rm -rf resources/[unused-repo]
   ```

---

## 🔧 Development Issues

### Problem 15: Dependency Conflict

**Symptoms:**
- Import error
- Version mismatch
- Module not found

**Solutions:**

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Check Python path**
   ```bash
   python3 -c "import sys; print(sys.path)"
   ```

3. **Force reinstall**
   ```bash
   pip install --force-reinstall [package]
   ```

---

### Problem 16: Build Failed

**Symptoms:**
- Compilation error
- Missing headers
- Build tool not found

**Solutions:**

1. **Install build essentials**
   ```bash
   # Ubuntu/Debian
   sudo apt install build-essential
   
   # macOS
   xcode-select --install
   ```

2. **Install dependencies**
   ```bash
   sudo apt install [dev-package]
   ```

3. **Use pre-built binaries**
   ```bash
   # Instead of building from source
   # Use pip wheel, npm package, etc.
   ```

---

## 🚨 Emergency Procedures

### Context Complete Loss

```
1. Ask user for project details
2. Reinitialize context
3. Verify resource status
4. Resume from appropriate step
```

### Complete System Failure

```
1. Document current state
2. Identify failure point
3. Attempt recovery
4. If unrecoverable:
   - Start fresh project
   - Learn from failure
   - Document for future
```

---

## 📞 Getting Help

If you encounter an issue not covered here:

1. **Check documentation**
   - README.md
   - Project-specific docs

2. **Check resources**
   - GitHub Issues
   - Community forums

3. **Ask for help**
   - Provide error message
   - Provide context
   - Provide steps to reproduce

---

*This troubleshooting guide is a living document. Update as new issues are discovered.*
