# Lessons Learned from Building a ChatGPT-Based Application

## 1. Introduction

In this project, we set out to create a structured, phase-based skill assessment experience using ChatGPT—not as a backend tool, but as the runtime itself. Our goal was to simulate role-based learning (e.g., Product Owner assessments) with prompts, scenarios, and feedback—all within a single conversational environment.

This document summarizes what worked, what didn’t, and what we ultimately learned about developing ChatGPT-native applications.

---

## 2. What Worked Well

### ✅ Prompt Modularization by Phase

Each prompt (intro, roleplay, reflection) was separated into its own file. This made the system composable, testable, and easy to maintain.

### ✅ File-Based Injection

Manually injecting a prompt (by pasting or fetching a markdown file) proved to be the **most reliable way to control state and behavior**. Trigger words were too ambiguous; file loading was explicit.

### ✅ Markdown Output

Having ChatGPT output results in markdown (e.g., assessment reports) was seamless and highly readable. Great for copy-pasting or Git-based review.

### ✅ Memory = Rich Reflection

Running the reflection phase in the same session as roleplay allowed for detailed, memory-rich feedback. This only worked when prompt injection was used to reset mode.

---

## 3. What Didn't Work (or Required Trade-Offs)

### ❌ Internet Fetch Instability

ChatGPT’s access to external URLs (e.g., raw GitHub markdown) is unreliable. Sometimes links load, sometimes they don’t. Not ideal for automated systems.

### ❌ Completion Bias / Over-Helpfulness

Even in facilitator mode, ChatGPT tends to fill in gaps when user prompts are vague. Questions like "What else should we consider?" often lead to unintended coaching behavior.

### ❌ Memory Drift Over Long Sessions

Even well-injected prompts begin to fade after long conversations. Unless re-injected, ChatGPT can drift from its intended behavior (especially between phases).

### ❌ Routing Logic Complexity

Trying to auto-route based on trigger words and state tracking created fragile and hard-to-debug flows. It added more complexity than value at this stage.

---

## 4. Design Principles We Settled On

* **Embrace Fuzziness**: ChatGPT is not a backend. It's a conversational agent. Treat its flexibility as a feature, not a flaw.
* **File = Mode Switch**: Prompt injection via file = most reliable way to change behavior.
* **MVP Simplicity > Architectural Elegance**: Overdesign led to fragility. Simpler workflows ran better.
* **State = Injection**: If you need it to behave a certain way, re-inject the prompt. Repetition is not a bug—it’s necessary.

---

## 5. Takeaways for Other Developers

* ⚠️ Don’t expect full app-like determinism. ChatGPT will always infer, adapt, and sometimes surprise you.
* 📙 Structure your prompts like components. Keep them readable and reusable.
* ♻️ Redundancy is good. Reinforce behavior phase-by-phase.
* ✨ Use markdown output generously. It works really well for structured content.
*
