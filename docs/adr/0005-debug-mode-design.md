# ADR-0005: Debug Mode Design and Trigger Policy

**Status:** Accepted  
**Date:** 2025-05-15

## Context

To support user testing and diagnostic interaction, a Debug Mode was introduced for ChatGPT-based skill assessment sessions.  
This mode allows relaxed behavior such as meta commentary, format flexibility, and phase repetition.

## Decision

- Debug Mode can be activated **at any time**, regardless of the current session phase.
- It is triggered using:
  - `!debug` (standard)
  - `↑↑↓↓←→←→BA` (easter egg)
- To return to standard behavior, `!default` can be used.
- Mode switches are explicitly handled within `README_chat_default.md` and `README_chat_debug.md`.
- Trigger keyword `!mode?` is also supported to report the current mode.

## Consequences

- Users can diagnose and correct behavior issues during sessions without restarting
- ChatGPT can act more transparently when requested, aiding user understanding and design validation
- Prompts and constraints in Debug Mode must be explicitly relaxed to avoid contamination of normal assessments

## Future Considerations

- More detailed debug logging or replay functionality may be introduced
- Mode triggers may be centralized in a shared config or facilitator prompt
