# ADR-0011: Trigger-Based Reflection Activation via ChatGPT Session Reset

## Status
Accepted

## Context

The skill assessment system requires separating the roleplay phase from the reflection phase to ensure clean state transitions. In practice, this means starting a new ChatGPT session for the reflection phase, avoiding unintended behavior carryover from previous prompts or instructions.

To activate the correct behavior in the new session, we adopt a **trigger-based model**, where a predefined message from the user (e.g., `フィードバックをお願いします。`) causes ChatGPT to switch into a reflection mode. This mechanism mirrors the assistant behavior already in place within the PO skill assessment project, where triggers like `PO`, `ロールプレイが終了しました。`, and `フィードバックをお願いします。` cause structured behavior changes based on previously defined memory.

## Decision

We will use **trigger phrases** to control session behavior transitions, especially across separately initiated ChatGPT sessions.

- The reflection phase will begin only when the user types:

```
フィードバックをお願いします。
```

- This trigger instructs ChatGPT to load behavior as defined in `prompt_reflection.md`
- The instruction and trigger behavior will be documented in:
- `README_chat.md` (for users)
- `report_template.md` (as post-report guidance)

This pattern allows the system to take advantage of ChatGPT's conversational context handling while enabling clean resets and modular design.

## Consequences

- All reflection-phase prompts will depend on this trigger-based initialization
- Users must understand that they need to start a new session after roleplay ends
- This approach is platform-dependent and assumes behavior consistent with current ChatGPT session memory and routing capabilities
- If ChatGPT’s behavior changes in future versions, this method may require adjustment

---

Created: 2025-05-16  
Authors: Sachiko Kijima, AssistA