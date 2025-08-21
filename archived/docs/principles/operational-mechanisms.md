# 📊 Operational Mechanisms

## 📘 Core Principles (from README)

### 8. If You Can't Debug It, It's Broken
* **Rationale**: ChatGPT doesn't expose its internal state.
* **Implication**: Show active file loads, prompt source indicators, and trigger messages. Create reproducible states.

### 9. Use Configuration Files to Define Modes
* **Rationale**: ChatGPT behavior changes with prior input and structure.
* **Implication**: Externalize role, scenario, and language choices into YAML. Let the assistant read them at runtime.

---

## 🧭 Supplemental Guidance

### 🔍 Configuration File ≠ Guaranteed Load
- **Rationale**: Even when you define a config file, ChatGPT may not automatically load or interpret it as intended. It might rely on cached expectations or prior completions.
- **Implication**:
  - Avoid assuming that defining a file is sufficient.  
  - Use *explicit prompting* to load config content into memory at runtime.
    - e.g., `Here is the config YAML. Please read and follow this.`
    - Reinforce key expectations in the current prompt context.

### 🗂️ Local > Remote, Manual > Automatic
- **Rationale**: ChatGPT handles pasted local content more reliably than remote fetches or embedded code references.
- **Implication**:
  - Prefer local file content pasted into the chat over dynamic links or URLs.
  - Avoid “just refer to this file”—instead, insert the file’s contents into the conversation explicitly.
  - If you must use HTTP: clearly state expected status, format, and fallback behavior.

### 📌 Runtime ≠ Compilation
- **Rationale**: Unlike code execution environments, ChatGPT doesn't “compile” configurations. It responds to what it sees *in this moment*.
- **Implication**:
  - Treat config files more like runtime context declarations.
  - Repetition and restatement are not bugs—they're part of state control.

---

## 🧠 Conceptual Insight: Structured Prompts as Domain Language

Designing prompt-based systems with ChatGPT is like revisiting structured programming—  
but with the **domain expressiveness of DDD**:

- Every prompt is both **code** and **contract**
- Context is not global—it's explicitly passed, reloaded, or reasserted
- The assistant is a *collaborator*, not a *compiler*

And most importantly:

> When we structure prompts using Markdown, YAML, or pseudo-code,  
> we are building a **ubiquitous language**—one that both humans and the AI can understand.

This is where **Domain Knowledge truly shines**:

- The better the domain is modeled in the prompt,
- The more *coherent* and *meaningful* the output becomes
- Prompts become readable even by non-engineers—and writable by them too

In this way, prompt design is not just about control—  
It's about creating a shared language between humans and machines.