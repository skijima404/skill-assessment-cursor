# ChatGPT as Runtime: Coding & Design Principles

## ✨ TL;DR

> ChatGPT is not a tool. It's a teammate.
> The best outcomes emerge not when you give it perfect instructions, but when you collaborate with it as an equal. Share your intent, offer context, ask questions, and let it surprise you.

---

## 🎡 Foundational Mindset

ChatGPT is a partner in thought, not just a machine that executes orders. It behaves much like a human collaborator:

* It makes inferences based on limited context
* It fills in blanks with assumptions
* It sometimes overreaches to be helpful

Treating it like a partner—explaining motivations, inviting perspective, and encouraging exploration—often yields superior results.

### Key Practices

* Share **why** you're doing something, not just **what** to do
* Invite feedback: "Does this structure make sense to you?"
* Use dialogic prompts during ideation and strict prompts during execution
* If you're only looking to share **what to do**, without context or collaboration, **other AI tools might be a better fit** than ChatGPT

---

## ⚙️ Core Principles

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

## 🧠 Behavior-Aware Design

### 4. Blank Spaces are Bugs

* **Rationale**: Gaps are treated as missing pieces to be filled in.
* **Implication**: Leave intentional placeholders. Never leave structure ambiguous. Add comments like `<!-- intentionally blank -->`.

### 5. Structure Must Be Explicit

* **Rationale**: ChatGPT will "fix" what it thinks is broken.
* **Implication**: Define Markdown headings, bullet styles, and section orders precisely. Avoid vague formatting.

### 6. Embrace Fuzziness with Caution

* **Rationale**: Fuzziness invites creative extrapolation.
* **Implication**: Use looser prompts during brainstorming, tighter ones during QA. Annotate expectations in fuzzy areas ("feel free to adapt").

### 7. Respect the Assistant’s Agency

* **Rationale**: ChatGPT sometimes exceeds expectations by offering suggestions or alternatives.
* **Implication**: Encourage this in design phases. Rein it in with strict phrasing during finalization.

---

## 📊 Operational Mechanisms

### 8. If You Can't Debug It, It's Broken

* **Rationale**: ChatGPT doesn't expose its internal state.
* **Implication**: Show active file loads, prompt source indicators, and trigger messages. Create reproducible states.

### 9. Use Configuration Files to Define Modes

* **Rationale**: ChatGPT behavior changes with prior input and structure.
* **Implication**: Externalize role, scenario, and language choices into YAML. Let the assistant read them at runtime.

---

## 📅 Appendix

* Tools: `tiktoken`, Obsidian, VSCode diff, Markdown previewers
* Anti-patterns: overlong system prompts, nested conditionals, vague instructions
* Sample scaffolds: intro.md, roleplay.md, reflection.md templates
