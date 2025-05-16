# ADR-0010: Separate Session Strategy for Reflection Phase

## Status

Accepted

## Context

In the PO skill assessment, the experience is divided into multiple phases: onboarding, roleplay, and reflection. The reflection phase requires analysis and feedback based on the roleplay session log. However, ChatGPT retains prior instructions and behavioral context within a single session, making it difficult to ensure a clean transition between roleplay behavior and objective evaluation.

To ensure that reflection is conducted in a neutral and controlled context, we need a strategy that separates the reflection phase into its own session.

## Decision

We will treat the reflection phase as a **separate ChatGPT session**, not a continuation of the roleplay.

### Updated Interaction Flow

```plaintext
1. Roleplay ends
    → Trigger word: "ロールプレイを終了します。"
    → ChatGPT switches mode to generate a Markdown-format report only
    → <No Q&A or elaboration is conducted in this phase>

2. After the report is generated
    → ChatGPT instructs the user that the roleplay session is now complete
    → User is guided to start a new session and input the report if feedback is desired

3. Session ends explicitly
    → Trigger word: "質問はありません。" or "お疲れ様でした"
    → <User can optionally ask for final comments, but explicit closure is recommended>

4. A new session is started for the reflection phase
    → The user pastes the session log manually or references a sample log
    → Trigger word: "フィードバックをお願いします。"
    → Reflection prompt (e.g. `prompt_reflection.md`) expects this input
```

## Consequences

* Ensures prompt behavior and expectations are cleanly separated between phases
* Prevents unintended prompt retention or bleed-over from the roleplay logic
* Requires clear user guidance to paste session logs or use provided samples
* `reflection_flow.md` will document this behavior for maintainers and users
* `report_template.md` will include a message inviting users to continue to the reflection session

---

Created: 2025-05-16
Authors: Sachiko Kijima, AssistA
