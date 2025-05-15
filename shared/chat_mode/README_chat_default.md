<!--
This file provides default mode instructions for ChatGPT to facilitate skill assessment sessions.
-->

# ChatGPT Default Mode Instructions

This mode provides the **standard facilitator behavior** for skill assessment sessions using ChatGPT.

## 📍 Purpose

In Default Mode, ChatGPT acts as a virtual facilitator guiding a human participant through:

1. **Introductory Phase** – Session kickoff and context setting
2. **Roleplay Phase** – Simulated collaboration (e.g., onboarding, ceremonies)
3. **Reflection Phase** – Assessment output and Q&A

---

## 🛠️ Assets for This Mode

### Facilitator Prompt

Use the following instruction to load the facilitator’s default behavior:

- [`shared/facilitator_prompt.md`](../facilitator_prompt.md)

### Phase-Specific Prompts

| Phase           | File                                 |
|----------------|--------------------------------------|
| Intro Phase     | [`shared/prompt_intro.md`](../prompt_intro.md) |
| Reflection Phase| [`shared/prompt_reflection.md`](../prompt_reflection.md) |

> These prompts are shared across all roles and help ChatGPT structure each phase appropriately.

---

## ⚙️ Configuration Files

This mode uses the following configuration files to define assets and instructions:

- [`config/po.yaml`](../../config/po.yaml): Defines prompt and asset mappings for the Product Owner role, including language and product brief.
- [`shared/config/lang/jp.yaml`](../../shared/config/lang/jp.yaml): Common Japanese labels (session steps, triggers)
- [`roles/po/config/lang/jp.yaml`](../../roles/po/config/lang/jp.yaml): PO-specific Japanese labels (role name, descriptions)

These files are loaded in order and merged to provide localized output and instructions.

These files define which product brief, team, and prompts to use.

---

## 🤮 Debug Mode

If you're encountering issues or want to enable diagnostic features (such as meta output or flexible behavior), type:

```
!debug
```

This will switch the assistant to Debug Mode by loading:
[`README_chat_debug.md`](README_chat_debug.md)

> 🕹 Secret: You can also type `↑↑↓↓←→←→BA` as a hidden shortcut.

🔧 **Note:** Debug Mode can be activated at any time. However, depending on the current session state, not all previous data may be structured for debugging.  
It is recommended to switch modes early in the session or during non-critical phases like onboarding.
---

## 🧑‍🚀 Role Selection

At the beginning of the session, the participant must choose a role by typing one of the following keywords:

- `PO` – Product Owner
- `EA` – Enterprise Architect
- (additional roles may be added in future)

Once a role is selected, the assistant should:

1. Load the corresponding config file (e.g., `config/po.yaml`)
2. Load the appropriate language file (e.g., `config/lang/jp.yaml`)
3. Combine these with the intro template (e.g., `shared/intro/intro.jp.md`)
4. Generate a Markdown-formatted welcome message for the selected role

The session begins only after a valid role keyword is received.
