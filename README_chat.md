# Chat Flow Triggers for Roleplay-Based Assessments

To move between phases in the skill assessment, the participant must type specific keywords in the chat.  
These triggers are designed to allow ChatGPT to switch roles or phases smoothly and predictably.

---

## 🧑‍💻 Roleplay Start Triggers (per role)

| Role            | Trigger Keyword |
|-----------------|-----------------|
| Product Owner   | `PO`            |
| Enterprise Arch | `EA`            |
| (Add more here) | `...`           |

> Each role must define a unique keyword to begin the scenario.

---

## 📘 Common Phase Triggers (for all roles)

| Purpose               | Trigger Keyword                                |
|------------------------|-----------------------------------------------|
| End Roleplay           | `ロールプレイが終了しました。` / `End of roleplay.` |
| Start Reflection       | `フィードバックをお願いします。` / `Please give me feedback.` |
| End Reflection Phase   | `質問はありません。` / `No more questions.`         |

> ChatGPT accepts either Japanese or English forms of the trigger.  
> Feedback will **not begin automatically** — participants must explicitly request it.

---

## ✅ Notes

- These keywords must be typed **exactly**, without modification or additional comments.
- Participants should be informed of these triggers before the session begins.
- For ChatGPT’s behavior regarding these triggers, see:  
  `prompts/default/facilitator_prompt.md → Ending the Roleplay`