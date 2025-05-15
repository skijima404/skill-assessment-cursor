# Product Owner Skill Assessment (PO)

This folder contains all necessary files to run a role-based skill assessment for the **Product Owner (PO)** role using ChatGPT. The experience is designed as a single-session roleplay that evaluates the participant's ability to lead early-stage product planning and stakeholder coordination.

---

## 🚀 How to Start (Time to Hello World)

1. Open ChatGPT with GPT-4 (Plus plan).
2. Share the following GitHub repository with ChatGPT:

```
https://github.com/skijima404/skill-assessment/
```

3. ChatGPT will load the instruction set from `README_chat.md`.
4. When ChatGPT asks which role you want to play, reply with:

```plaintext
PO
```

The session will begin immediately.

---

## 📁 Folder Structure

| File/Folder                             | Description                                               |
| --------------------------------------- | --------------------------------------------------------- |
| `scenario.md`                           | Scenario definition: structure, scope, evaluation targets |
| `prompts/default/facilitator_prompt.md` | Role instructions for ChatGPT (assessment mode)           |
| `characters/collaborative_team.md`      | Character profiles used in this scenario                  |
| `product_briefs/calendar_dashboard.md`  | The default product brief (can be swapped later)          |
| `sample_logs/`                          | Optional: chat logs or example runs                       |

---

## 🔁 Chat Flow Triggers

The following keywords must be typed by the participant to advance through the session:

| Phase          | Trigger Keyword                                |
| -------------- | ---------------------------------------------- |
| Start Roleplay | `PO`                                           |
| End Roleplay   | `ロールプレイが終了しました。` / `End of roleplay.`          |
| Start Feedback | `フィードバックをお願いします。` / `Please give me feedback.` |
| End Reflection | `質問はありません。` / `No more questions.`             |

> ChatGPT will wait for each trigger to be typed explicitly.
> You may type Japanese or English versions.

---

## 🧱 Ground Rules (Behavior)

ChatGPT will:

* Play multiple characters using the profiles provided
* Stay in-character at all times
* Not provide feedback unless explicitly requested
* Not explain how it evaluates you during the session

All characters are collaborative in this default scenario. You may ask questions, suggest priorities, and interact freely as a PO.

---

## 🧪 Want to Contribute?

* You can add new product briefs under `product_briefs/`
* You can create alternate character sets under `characters/`
* See [../../CONTRIBUTING.md](../../CONTRIBUTING.md) for language guidelines and contribution rules

---

This scenario is intended to simulate real PO challenges in early product discovery and planning. Use it to test, reflect, and grow.
