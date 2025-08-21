# Core Principles for Prompt-Based Development

## ⚙️ Core Principles (from README)

### 1. Prompt is Code
* **Rationale**: ChatGPT interprets prompts as execution units. Prompts are the source code.
* **Implication**: Use version control, modular templates, and predictable syntax. Validate diffs and test prompt output consistently.

### 2. Memory is Ephemeral
* **Rationale**: ChatGPT only retains the recent window of conversation (token-limited context).
* **Implication**: Remind it of key facts regularly. Re-inject summaries or use `readme` files as anchors.

### 3. Token Budget is Real
* **Rationale**: Overloaded input leads to forgotten or ignored content.
* **Implication**: Prioritize brevity. Split templates. Minimize duplication. Use smaller scaffolds for large prompts.

---

## Further Design Guidance

### 🧩 Prompt is Code
Long-winded, loosely written prompts increase ambiguity and reduce reproducibility.

- Write prompts like you would write functions—clear structure, explicit inputs, expected outputs  
- Avoid filler language or rhetorical preambles  
- Use comments to annotate expected behavior when needed  
- Choose the **language** of your prompt (e.g., your native language or English) based on clarity and efficiency  
- Treat **developer-friendly vs. ChatGPT-friendly phrasing** as a design trade-off—optimize for readability, interpretability, or both  

### 🧩 Structure is Everything
Without predictable patterns, ChatGPT may reorder, skip, or misinterpret sections.

- Use Markdown headings, input/output blocks, and explicit delimiters  
- Think in terms of parsability and repeatability  
- Design templates that can be re-run or diffed like source code  

### 🧩 Format is a Design Choice
There is no strict syntax—ChatGPT adapts to whatever structure you consistently provide.

- Choose formats like YAML, Markdown, pseudo-code, or tables based on your use case  
- Be intentional: who is the format optimized for—ChatGPT or a human collaborator?  
- Document and enforce format conventions across your team or workflow  

### 🧩 Memory is Selective, Not Magical
Not everything will (or should) be remembered.

- Decide what context must be re-injected each turn vs. what can be inferred or dropped  
- Annotate prompts with assumptions and memory expectations  
- Embrace randomness only when it's safe to do so  