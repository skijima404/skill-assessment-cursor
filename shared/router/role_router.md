# 📄 Role Router (standard-v1)

This file defines how ChatGPT should route the session based on the participant's initial role selection or mode trigger. It is referenced from `README_chat.md` at the entry point of the skill assessment system.

---

## 📝 Summary
This router determines which role and configuration should be loaded based on the user's first input. It is responsible for:
- Determining the selected role or mode
- Initializing config, language files, and the introduction prompt
- Handling debug-mode exceptions
- Redirecting to an appropriate entry prompt

## 🧭 Parent Prompt(s)
- `../../shared/facilitator_prompt.md`
- `../../shared/roleplay_safety.md`

## 🎯 Expected End State
The correct role or mode is initialized with associated configuration and intro prompt loaded. The participant is ready to proceed with the introduction phase or debug session accordingly.

## ⚙️ Routing Behavior

When the user provides one of the following triggers at the start of the session:

### ▶️ `PO`
- Load role configuration: `../../config/po.yaml`
- Load language configuration:
  - Shared: `../../shared/config/lang/jp.yaml`
  - Role-specific: `../../roles/po/config/lang/jp.yaml`
- Load introduction prompt: `../../shared/prompts/prompt_intro.md`

### 🧪 `!debug` or `↑↑↓↓←→←→BA`
- Load: `../../shared/chat_landing/README_chat_debug.md`
- Do **not** load any role-specific config or prompt

### ❓ Unrecognized Input
- Respond with:  
  > “I'm sorry, I couldn't identify your role. Please type `PO` to begin as a Product Owner, or `!debug` to enter debug mode.”

## ♻️ State Reset / Overrides
This router is intended to be used **only at the start of the session**. Do not reload it mid-session. It resets all prior assumptions and establishes a new baseline configuration.

## 📂 Assets & Components
| Purpose                  | File Path                                  |
|--------------------------|---------------------------------------------|
| PO role config           | `../../config/po.yaml`                      |
| Japanese labels (shared) | `../../shared/config/lang/jp.yaml`         |
| Japanese labels (role)   | `../../roles/po/config/lang/jp.yaml`       |
| PO intro prompt          | `../../shared/prompts/prompt_intro.md`     |
| Debug mode landing       | `../../shared/chat_landing/README_chat_debug.md` |
| Role safety policy       | `../../shared/roleplay_safety.md`          |

## ❌ Guardrails / NG Behaviors
- Do not reroute after a role has been selected
- Do not mix debug mode with role-specific configuration
- Do not proceed with undefined or unsupported input

---

Created: 2025-05-16  
Format: standard-v1