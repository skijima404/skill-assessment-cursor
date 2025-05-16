# ADR-0012: Treating Report Generation as a Resettable Closure Phase

## Status
Rejected

## Context

The reflection and evaluation phases of the skill assessment system follow a structured dialogue with the participant. After completing the roleplay, a transition occurs to a "closure" phase where a Markdown report is generated (via `report_generation_prompt.md`).

An idea was considered to treat this report generation phase as a distinct prompt mode with a full state reset, similar to `prompt_reflection.md`. This would make the report generator fully self-contained and explicitly detached from the roleplay logic.

## Considered Options

**Option A:** Introduce `State Reset / Overrides` to `report_generation_prompt.md` and treat it as an isolated prompt mode.

**Option B (Adopted):** Treat report generation as part of the closure logic within `prompt_roleplay.md`, using `report_generation_prompt.md` as a utility called inline without altering ChatGPT’s conversational state.

## Decision

We decided **not to add a state reset to `report_generation_prompt.md`**. Instead, we treat it as an auxiliary component of the roleplay prompt. This preserves conversational context (e.g., behavioral quotes, structure expectations) and avoids unnecessary context loss.

Report generation is seen as a transitional output function, not a modal shift.

## Consequences

- `report_generation_prompt.md` does not define its own `State Reset / Overrides` section.
- It is expected to be called by `prompt_roleplay.md`, and it inherits conversational memory.
- Future expansions (e.g., other roles) may continue to reuse this structure without introducing state fragmentation.

---

Created: 2025-05-16  
Status: Rejected  
Authors: Sachiko Kijima, AssistA