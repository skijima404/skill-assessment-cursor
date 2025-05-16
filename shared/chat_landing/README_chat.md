<!--
This file is intended to be used by ChatGPT to guide role-based assessment behavior.
It serves as the entry point to load various operation modes.
-->

# Skill Assessment - ChatGPT Instruction Router

Welcome to the Skill Assessment Repository.

This file acts as the **entry point** for ChatGPT.  
It helps the assistant determine which **role** and **mode** to operate in before loading specific instructions.

---

## 🧭 Step 1: Choose a Role

Supported roles:

- [Product Owner (PO)](../../roles/po/README.md)
- [Enterprise Architect (EA)](../../roles/ea/README.md) ← *Coming soon*

---

## 🛠 Step 2: Choose a Mode

Each mode defines how the assistant should behave (tone, restrictions, formatting, etc.).

| Mode       | Description                              |
|------------|------------------------------------------|
| [Default](README_chat_default.md) | Standard facilitator behavior for roleplay |
| [Debug](README_chat_debug.md)     | Debugging mode with relaxed constraints |
| [Reflection](README_chat_reflection.md) | Post-assessment feedback and Q&A (TBD) |

---

## 🔁 How to use

To begin, ChatGPT should load this file and then follow the selected mode’s instruction file.  
Each mode will guide the assistant through the required:

- Facilitator prompt
- Phase-specific instructions (intro, roleplay, reflection)
- Assets to reference (e.g., scenario, evaluation criteria)

---

## 📌 Note

This file should be loaded by ChatGPT prior to any specific instruction file.  
It ensures proper mode setup and consistent behavior across sessions.

