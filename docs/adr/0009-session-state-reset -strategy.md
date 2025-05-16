# ADR-0009: Session State Reset Strategy

## Status

Accepted

## Context

The skill assessment system uses phase- and mode-specific prompts to guide ChatGPT behavior. However, ChatGPT retains context from previous prompts unless explicitly cleared. This creates a risk where behavioral rules or tone from prior phases or modes persist, resulting in unintended or inconsistent responses.

Examples of such risks include:

* Roleplay phase rules bleeding into the reflection phase
* Debug mode conflicting with onboarding expectations
* Assistant retaining prior triggers, tone, or constraints

To prevent these issues and ensure clear phase transitions, a consistent state reset strategy is needed.

## Decision

We will adopt a default rule that **each session phase or mode begins with a complete state reset**, followed by **explicit reloading of the required prompts only**.

### Key Rules

* Previous prompt state (tone, role, triggers, constraints) must be discarded at each phase or mode transition.
* Prompt files such as `facilitator_prompt.md`, `prompt_intro.md`, `prompt_reflection.md` must be explicitly reloaded at each entry point.
* Phase or mode transitions (e.g., onboarding → reflection, default → debug) always start with a full reset.
* Prompts should include a section like `# ♻️ State Reset / Overrides` to clarify that they override prior logic.

### Example: Phase Transition Sequence

```text
User input: "PO" → Reset state → Load facilitator_prompt.md + prompt_intro.md
User input: "ロールプレイを終了します。" → Reset state → Load prompt_reflection.md
User input: "!debug" → Reset state → Load readme_chat_debug.md → Load debug-mode prompts
```

## Consequences

* All phase entry points must include explicit prompt loading, not rely on previous state.
* Prompt structure templates will include the `# ♻️ State Reset / Overrides` section.
* `config/po.yaml` and related files may include flags like `reset_before_prompt: true` to assist future automation or validation.
* Fewer misinterpretations or cross-phase behavior bugs are expected.

---

Created: 2025-05-16
Authors: Sachiko Kijima, AssistA
