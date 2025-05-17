# Architecture Decision Records (ADR)

This directory documents the architecture decisions made during the development and maintenance of this repository.

ADR (Architecture Decision Record) is a lightweight way to capture the context and rationale behind key design choices.  
These records help future contributors understand why the current structure exists and how to expand it consistently.

## Format

- Each ADR is stored as a Markdown file: `NNNN-title.md`
- Status is one of: `Proposed`, `Accepted`, `Superseded`, `Deprecated`, or `Rejected`
- A date is included to track when the decision was made
- ADRs are sorted in ascending order

## ADR Index

| ID    | Title                                          | Status   | Date       |
|-------|------------------------------------------------|----------|------------|
| 0001  | Chat Mode Structure and Prompt Organization    | Accepted | 2025-05-15 |
| 0002  | Role Folder Guidelines    | Accepted | 2025-05-15 |
| 0003  | Placement of Phase-Specific Prompts (Intro and Reflection)  | Accepted | 2025-05-15 |
| 0004  | Separation of Application-Level and Phase-Specific Prompts  | Accepted | 2025-05-15 |
| 0005  | Debug Mode Design and Trigger Policy  | Accepted | 2025-05-15 |
| 0006  | Separation of Configuration and Localization Files  | Accepted | 2025-05-15 |
| 0007  | Limit Character Scope and Facilitation Roles in Scenario  | Accepted | 2025-05-15 |
| 0008  | Prompt Structure Design for Skill Assessment  | Accepted | 2025-05-16 |
| 0009  | Session State Reset Strategy  | Accepted | 2025-05-16 |
| 0010  | Separate Session Strategy for Reflection Phase  | Accepted | 2025-05-16 |
| 0011  | Trigger-Based Reflection Activation via ChatGPT Session Reset  | Accepted | 2025-05-16 |
| 0012  | Treating Report Generation as a Resettable Closure Phase
 | Rejected | 2025-05-16 |
| 0013  | Split Routing and Prompt Files; Redefine Chat Entry Structure  | Accepted | 2025-05-16 |
| 0014  | Use Absolute Raw URLs Instead of Relative Paths for ChatGPT Access  | Accepted | 2025-05-16 |
| 0015  | Smart Strict Mode and Resource-Level Load Policies  | Accepted | 2025-05-17 |



> To add a new ADR, create a Markdown file under `docs/adr/` and register it in this table.