# Contributing to the Skill Assessment Repository

Thank you for your interest in improving this skill assessment framework!  
This repository is designed to support role-based skill assessments (starting with Product Owner), powered by ChatGPT.

This document outlines how to contribute new content or modify existing materials in a consistent and scalable way.

---

## 🗣️ Language Policy

All files that provide instruction to ChatGPT — such as:

- `prompts/`
- `characters/`
- `product_briefs/`

must be written in **English** as the base language.

You may include Japanese annotations for clarification, but the primary structure, terminology, and tone should be written in English.

### Why English?

- ChatGPT understands and responds more reliably to English prompts
- Technical and organizational terms like “Servant Leader,” “Non-functional Requirements,” “KPI alignment” are best handled in English
- Enables future international reuse and easier prompt engineering

> 💡 If you wish to adapt this content for another language, we recommend using **ChatGPT as your IDE** — ask it to translate and rewrite the materials while preserving structure and instructional clarity.
（他言語で利用したい場合は、ChatGPTをIDEのように活用し、構造を保ったまま翻訳・リライトを依頼する方法を推奨します）


---

## 🗂️ Directory Structure Guidelines

- `shared/`: Common templates and instructional files (shared across all roles)
- `roles/<role_name>/`: Role-specific scenarios and components
  - `prompts/`: Instructions for ChatGPT per interaction mode (e.g., assessment vs advice mode)
  - `characters/`: Stakeholder personas with tone and values
  - `product_briefs/`: Business/product context for the scenario
  - `scenario.md`: Main roleplay flow
  - `sample_logs/`: (Optional) Example interactions for reference

Each `role/` directory includes its own `README.md` for how to run and evaluate the role.

---

## 🧩 Contribution Principles

- Ensure any character or prompt added is consistent in tone and realistic in behavior
- Avoid adding ChatGPT instructions in Japanese only
- Maintain modularity: scenarios should be reusable with different characters or product briefs
- Use markdown formatting with clear headers and bullet points for readability

---

## ✅ Suggested Workflow

1. Fork the repository
2. Create or modify files under the appropriate role directory
3. Use English as the default for prompts and context
4. Submit a pull request with a summary of your changes
5. We’ll review for consistency and clarity

---

Thank you again for your contribution!