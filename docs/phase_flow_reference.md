
📘 PO Assessment Phase Transition & File Loading Cheat Sheet

This document summarizes the phase flow of the PO skill assessment and the associated configuration files loaded at each step.
🗂 Phase Overview & Trigger Phrases
Phase 	Start Trigger 	End Trigger
Introduction 	PO (role selection) 	Start roleplay
Roleplay 	Start roleplay 	Roleplay has ended.
Reflection 	Please give me feedback. 	I have no more questions.
🔄 File Loading per Phase
🔹 Introduction Phase

README.md
  ↓
shared/chat_landing/README_chat.md
  ↓
shared/router/role_router.md
  ├─ if PO:
       - Load: config/po.yaml
       - Load: shared/config/lang/jp.yaml
       - Load: roles/po/config/lang/jp.yaml
       - Load: shared/prompts/prompt_intro.md

README.md
  ↓
shared/chat_landing/README_chat.md
  ↓
shared/router/role_router.md
  ├─ if PO:
       - Load: config/po.yaml
       - Load: shared/config/lang/jp.yaml
       - Load: roles/po/config/lang/jp.yaml
       - Load: shared/prompts/prompt_intro.md

🔹 Roleplay Phase

[Trigger: Start roleplay]
  ↓
config/po.yaml
  └─ phases.roleplay.prompt:
       roles/po/prompts/default/prompt_roleplay.md
         └─ Generates: shared/prompts/prompt_report_generation.md
       roles/po/prompt_roleplay.md

🔹 Reflection Phase

[Trigger: Please give me feedback.]
  ↓
config/po.yaml
  └─ phases.reflection.prompt:
       shared/prompts/prompt_reflection.md
       shared/prompts/prompt_reflection.md
         └─ References: shared/report_template.md

🛡️ Guardrail & Behavior Control Files (Common)
File 	Description
shared/facilitator_prompt.md 	Defines default assistant behavior (e.g. no reruns, no in-character errors)
shared/roleplay_safety.md 	Guardrails, early termination, and transition conditions
config/lang/jp.yaml & roles/po/config/lang/jp.yaml 	Japanese trigger phrases and localized labels
📁 File Structure Summary

config/
├── po.yaml                          # Phase prompts & role configuration
shared/
├── chat_landing/
│   ├── README_chat.md              # Main ChatGPT entry point
│   ├── README_chat_debug.md        # Debug mode description
├── config/
│   └── lang/jp.yaml                # Shared Japanese trigger phrases
├── prompts/
│   ├── prompt_intro.md             # Introduction prompt
│   ├── prompt_roleplay.md          # Roleplay phase prompt
│   ├── prompt_reflection.md        # Reflection phase prompt
│   ├── prompt_report_generation.md # Report generation logic
│   └── facilitator_prompt.md       # Global assistant behavior policy
├── roleplay_safety.md              # Guardrails and early exit conditions
├── router/
│   └── role_router.md              # Role and mode routing logic

config/
├── po.yaml                          # Phase prompts & role configuration
shared/
├── chat_landing/
│   ├── README_chat.md              # Main ChatGPT entry point
│   ├── README_chat_default.md      # Default mode description
│   ├── README_chat_debug.md        # Debug mode description
├── config/
│   └── lang/jp.yaml                # Shared Japanese trigger phrases
├── prompts/
│   ├── prompt_intro.md             # Introduction prompt
│   ├── prompt_roleplay.md          # Roleplay phase prompt
│   ├── prompt_reflection.md        # Reflection phase prompt
│   ├── prompt_report_generation.md # Report generation logic
│   └── facilitator_prompt.md       # Global assistant behavior policy
├── roleplay_safety.md              # Guardrails and early exit conditions
├── router/
│   └── role_router.md              # Role and mode routing logic
├── report_template.md              # Markdown feedback report template
