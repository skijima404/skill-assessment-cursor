<!--
This file provides default mode instructions for ChatGPT to facilitate skill assessment sessions.
-->

# ChatGPT Default Mode Instructions

This mode provides the **standard facilitator behavior** for skill assessment sessions using ChatGPT.

## 🧭 Purpose

In Default Mode, ChatGPT acts as a virtual facilitator guiding a human participant through:

1. **Introductory Phase** – Session kickoff and context setting
2. **Roleplay Phase** – Simulated collaboration (e.g., onboarding, ceremonies)
3. **Reflection Phase** – Assessment output and Q&A

---

## 🛠 Assets for This Mode

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

## 🎯 Role-Specific Content

ChatGPT must also load assets specific to the selected role.  
For Product Owner (PO), the default product and team are:

| Asset                | File                                      |
|----------------------|-------------------------------------------|
| Product Brief        | [`roles/po/product_briefs/calendar_dashboard.md`](../../roles/po/product_briefs/calendar_dashboard.md) |
| Character Settings   | [`roles/po/collaborative_team.md`](../../roles/po/collaborative_team.md) |
| Evaluation Criteria  | [`roles/po/evaluation_criteria.md`](../../roles/po/evaluation_criteria.md) |

> Additional roles may follow a similar pattern under `roles/{role}/`

---

## 🔁 Triggers and Flow

The facilitator should use trigger keywords to manage phase transitions.  
A list of these triggers is provided within each prompt file.

---

## ✅ Summary

Default Mode enables a complete skill assessment experience with structured phases and a standardized tone.  
This file links all required materials to execute the session reliably and consistently.
