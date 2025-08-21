# ADR-0013: Split Routing and Prompt Files; Redefine Chat Entry Structure

## Status

Accepted

## Context

As the number of system prompts and routing logic files grew, the previous directory structure under `shared/` became increasingly overloaded. Initially, files like `README_chat.md` and `README_chat_default.md` carried both explanatory and functional logic, including implicit routing and prompt initialization.

Additionally, the term "chat" was being overloaded across:

* Mode initialization (debug/default)
* Prompt loading
* Human-facing explanations

This created ambiguity around the roles of `README_chat.md`, `README_chat_debug.md`, and `role_router.md`.

## Decision

We decided to **restructure the shared assets** by introducing clear folder-based separation of responsibilities:

### 1. `shared/chat_landing/`

* Contains human-readable entrypoints, such as:

  * `README_chat.md`
  * `README_chat_default.md`
  * `README_chat_debug.md`
* These serve as the **landing pages** for ChatGPT interactions, not as logic controllers

### 2. `shared/router/`

* Contains logic routers like `role_router.md`
* These are used by GPT to determine initial configuration and role routing

### 3. `shared/prompts/`

* Now holds actual behavior prompts:

  * `prompt_intro.md`
  * `prompt_roleplay.md`
  * `prompt_reflection.md`
  * `prompt_report_generation.md`
  * `facilitator_prompt.md`

## Consequences

* `README_chat.md` and its variants are now **purely landing documents** and may include links or explanations but **no routing logic**
* All GPT-controlled branching happens via `shared/router/role_router.md`
* Prompt responsibilities are cleanly scoped and now reside in `shared/prompts/`
* The term "chat mode" is avoided in structural logic; replaced with clearer roles: landing, router, prompt

---

Created: 2025-05-16
Status: Accepted
Authors: Sachiko Kijima, AssistA
