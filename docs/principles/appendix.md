# 📅 Appendix

### 🛠️ Tools
These tools support prompt development, testing, and iteration:

- `tiktoken`: for estimating and controlling token usage
- Obsidian: for managing prompt files as markdown knowledge base
- VSCode (with Markdown preview and diff): for visual editing and change tracking
- Markdown previewers and linters: to ensure structure and consistency

---

### ⚠️ Anti-patterns
Common pitfalls to avoid when designing for ChatGPT:

- Overlong system prompts (dilutes focus)
- Nested logic and conditionals (ChatGPT ≠ interpreter)
- Vague or inconsistent instructions
- Assuming state without reinforcing it
- Letting structure drift across iterations

---

### 📁 Sample Scaffolds
Reusable templates that promote consistency and reproducibility:

- `intro.md` – onboarding and context setting
- `roleplay.md` – interactive scenario prompts
- `reflection.md` – post-session evaluation & learning

---

## 💡 ChatGPT as IDE

> The most powerful way to write prompts is *with* ChatGPT, not *for* ChatGPT.

Treat ChatGPT as a **collaborative development environment**:

- Write prompt drafts directly in conversation  
- Ask for clarity feedback: *“Is this structure intuitive?”*  
- Let it suggest alternative phrasings, structures, or flows  
- Use it as a **pair programmer** for prompt refinement  

This is the fastest, most accurate, and most human-centered way to build effective prompt systems.

---

### 🧠 Memory-Aware Development

Working with ChatGPT means constantly managing its limited in-session memory:

- Identify what the assistant should *actively hold* in memory (roles, tone, context)  
- Push everything else—like rationale, history, or configuration—into **external memory as Markdown files**  
- Treat your ADRs (Architecture Decision Records) as **externalized memory** that GPT can reload when needed  

> Don’t force ChatGPT to remember decisions.  
> Let it **reference** them like a developer would read the docs.

---

### 🧩 VSCode + Extension Integration

Using ChatGPT inside VSCode with extensions (e.g., [CodeGPT](https://marketplace.visualstudio.com/items?itemName=DanielSanMedium.dscodegpt)) allows:

- Inline prompt development  
- Code and scaffold review without context-switching  
- ADR and documentation previews in parallel  

This workflow pairs perfectly with the principle of “externalizing memory”:

- Keep decisions in `docs/adr/`  
- Keep context-light scaffolds in `prompts/`  
- Let ChatGPT assist with code, not carry the entire project in memory

---

### 🧠 Cognitive Load Management for ChatGPT

ChatGPT, like a human collaborator, performs best when **cognitive load is managed carefully**.

This applies to **both modes** of interaction:

- 🧑‍💻 **As a Pair Programmer** during prompt development
- 🧩 **As a Runtime Assistant** in live application workflows

#### 📌 Design Implications:

- Avoid overloading a single prompt with too many unrelated topics
- Split responsibilities across distinct phases or files (`intro.md`, `scenario.md`, etc.)
- Reintroduce important context after long outputs or topic changes
- When switching contexts (e.g., from design to testing), *signal it clearly*
- Allow "mental reset" opportunities with summary or checkpoint prompts

> Manage the assistant's cognitive load like you would your own—  
> because under the hood, it's solving a cognitive task too.