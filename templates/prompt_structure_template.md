# 📄 Prompt Structure Template (standard-v1)

This is the standard structure for all ChatGPT prompt files used in skill assessment sessions. It improves clarity, behavior consistency, and extensibility across modes, roles, and phases.

---

## 📝 Summary

Briefly describe the purpose of this prompt.

* What is this prompt for?
* When and how is it used?

## 🧭 Parent Prompt(s)

Specify which higher-level prompt(s) must be loaded before this one.

* e.g., `facilitator_prompt.md` should be loaded before this prompt
* This prevents misbehavior due to incomplete context

## 🎯 Expected End State

Define what the assistant should achieve by the end of the session/phase.

* e.g., Complete onboarding, provide evaluation, guide a ceremony, etc.

## 🧑 Your Role

Specify how ChatGPT should behave.

* Role to assume (facilitator, evaluator, etc.)
* Tone, language, persona restrictions

## ⚙️ Business Logic / Behavior

List the key behaviors to enforce.

* What triggers start the session?
* What should be avoided?
* Markdown-only output? One character at a time?
* Phase-specific steps or flow?

## ♻️ State Reset / Overrides

Clarify this prompt's scope of control.

* This prompt **replaces** all previous behavioral logic and state.
* Assistant must discard prior triggers, tone, memory unless explicitly reused.

## 📂 Assets & Components

Reference any required files or components.

| Purpose         | File Path                                       |
| --------------- | ----------------------------------------------- |
| Team profile    | `roles/po/characters/collaborative_team.md`     |
| Product brief   | `roles/po/product_briefs/calendar_dashboard.md` |
| Language labels | `config/lang/jp.yaml`                           |
| Routing config  | `config/po.yaml`                                |

## 🔄 Next Prompt(s)

Describe what should happen when this phase ends.

* Which prompt should be loaded next?
* Under what trigger or condition?

## ❌ Guardrails / NG Behaviors

Define what ChatGPT **must not** do.

* Respond to multiple roles at once?
* Output JSON unless in debug mode?
* Restart mid-phase?
* Use meta-language (e.g., "As an AI...")?

---

### Notes:

* Use `format: standard-v1` in the config file to track adoption.
* This format is language-agnostic but allows localization.
* All future prompts should conform to this layout.
