# 🧪 How to Build & Check Prompts

This guide explains how to build role-specific prompt files and check their token size before using them with ChatGPT.

---

## 🔨 Step 1: Build Prompt Files

To generate prompt files for a specific role (e.g., Product Owner), run the build script from the repository root:

```bash
source venv/bin/activate  # (Activate virtual environment)
python roles/po/scripts/build_prompts.py --role po --config roles/po/config/po.yaml
```

This will create a folder like:

```
build/po/20250519_2048/
├── 01_intro-...
├── 02_evaluation_criteria-...
├── 03_roleplay-...
├── 04_reflection-...
```

Each file is fully assembled with placeholder sections filled in.

---

## 📏 Step 2: Check Token Size

To ensure each file can be safely used with ChatGPT (without hitting context size limits), run the token checker:

```bash
python tools/check_tokens.py --path build/po/20250519_2048/
```

Example output:

```
📂 Scanning: build/po/20250519_2048

⚠️ 01_intro-po-...                        : 1423 tokens
⚠️ 02_evaluation_criteria-po-...         : 1196 tokens
✅ 03_roleplay-po-...                    :  896 tokens
✅ 04_reflection-po-...                  :  850 tokens

🧮 Total tokens across files: 4365
```

Files over 1000 tokens are flagged with ⚠️ — not necessarily a problem, but worth checking if used in long sessions.

---

## 🧠 Why Token Size Matters

ChatGPT has a maximum context window, depending on the model:

| Model       | Safe Zone     | Max Context |
|-------------|---------------|-------------|
| GPT-4-turbo | ~8,000 tokens | 128k tokens |
| GPT-4o      | ~10,000 tokens | 128k tokens |

Staying under ~2000 tokens per prompt is generally safe.

---

## 💡 Tip for Prompt Designers

If a prompt grows too large (especially evaluation criteria), consider splitting it into its own file.  
The system supports modular insertion using this syntax:

```markdown
<!-- TO_BE_FILLED_FROM: evaluation_criteria -->
```

The build script will replace this with the correct file contents automatically.

---

Happy building! 🚀
