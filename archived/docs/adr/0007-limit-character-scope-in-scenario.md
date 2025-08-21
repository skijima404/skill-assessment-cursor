# ADR 0007: Limit Character Scope and Facilitation Roles in Scenario

**Status:** Accepted  
**Date:** 2025-05-15

## Context
In the current Product Owner (PO) assessment scenario (`roles/po/scenario.md`), the `Scope` section describes the structure of the roleplay session (Onboarding → Sprint 0 → Sprint Planning) and mentions that the Scrum Master will facilitate the session. However, no explicit rule is defined regarding which characters may appear, who may speak first, or whether non-core characters such as sponsors should appear.

This lack of definition leads to ambiguous behavior in ChatGPT-driven sessions. For example, ChatGPT may assume freedom to include optional characters like the Sponsor or allow them to initiate conversations. While some variation adds realism, too much can overwhelm the learner, especially at the beginning of a session.

## Decision
We will enforce the following constraints and conventions in each `scenario.md`:

1. **Explicit Character Declaration**
   - Each scenario must define which characters are *in scope* for the session.
   - Characters not intended to appear must be noted as such (e.g., "Sponsor: not present in this session").

2. **Facilitator Declaration**
   - The facilitator character (usually Scrum Master) must be explicitly defined in the scenario.

3. **Opening Scene Structure**
   - The first utterance in the session must come from the facilitator.
   - The facilitator should provide a **contextual handoff** to the PO, such as acknowledging late joining or initial preparation by the team.

4. **Optional File**: `opening_snippet.md`
   - If needed, the introductory exchange can be isolated into its own file and referenced by prompt logic.

5. **Prompt Guardrails**
   - The `facilitator_prompt.md` must enforce these constraints unless `debug` mode explicitly overrides them.
   - ChatGPT must not introduce characters not listed in `scenario.md`.

## Consequences
- Ensures consistent learner experience across sessions.
- Reduces confusion in the opening phase by narrowing expected participant scope.
- Provides a foundation for more advanced, varied scenarios in future sessions while keeping the core experience controlled.
- Enables reliable prompt behavior even when using external character files or shared team definitions.

## Related
- Scenario: `roles/po/scenario.md`
- Prompt control: `shared/facilitator_prompt.md`
- Characters: `roles/po/characters/collaborative_team.md`