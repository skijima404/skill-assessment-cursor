# 📘 PO Assessment Phase Transition & File Loading Cheat Sheet

This document summarizes the **phase flow** of the PO skill assessment and the **associated configuration files** loaded at each step.

---

## 🗂 Phase Overview & Trigger Phrases

| Phase        | Start Trigger              | End Trigger                 |
| ------------ | -------------------------- | --------------------------- |
| Introduction | `PO` (role selection)      | `Start roleplay`            |
| Roleplay     | `Start roleplay`           | `Roleplay has ended.`       |
| Reflection   | `Please give me feedback.` | `I have no more questions.` |

---

## 🔄 File Loading per Phase

### 🔹 Introduction Phase

```plaintext
README.md
  ↓
shared/chat_mode/README_chat.md
  ↓
shared/chat_mode/README_chat_default.md
  ↓
shared/facilitator_prompt.md
config/po.yaml
  └─ phases.introduction.prompt: shared/prompt_intro.md
  └─ language_files:
        - shared/config/lang/jp.yaml
        - roles/po/config/lang/jp.yaml
```

---

### 🔹 Roleplay Phase

```plaintext
[Trigger: Start roleplay]
  ↓
config/po.yaml
  └─ phases.roleplay.prompt:
       roles/po/prompt_roleplay.md
```

---

### 🔹 Reflection Phase

```plaintext
[Trigger: Please give me feedback.]
  ↓
config/po.yaml
  └─ phases.reflection.prompt:
       shared/prompt_reflection.md
         └─ References: shared/report_template.md
```

---

## 🛡️ Guardrail & Behavior Control Files (Common)

| File                                                   | Description                                                                 |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| `shared/facilitator_prompt.md`                         | Defines default assistant behavior (e.g. no reruns, no in-character errors) |
| `shared/roleplay_safety.md`                            | Guardrails, early termination, and transition conditions                    |
| `config/lang/jp.yaml` & `roles/po/config/lang/jp.yaml` | Japanese trigger phrases and localized labels                               |

---

## 📁 File Structure Summary

```plaintext
config/
├── po.yaml                          # Phase prompts & role configuration
shared/
├── chat_mode/
│   ├── README_chat.md              # Mode router
│   ├── README_chat_default.md      # Default mode definition
├── config/
│   └── lang/jp.yaml                # Shared Japanese trigger phrases
├── prompt_intro.md                 # Introduction prompt
├── prompt_reflection.md            # Reflection phase prompt
├── report_template.md              # Markdown feedback report template
├── facilitator_prompt.md           # Global assistant behavior p
```
