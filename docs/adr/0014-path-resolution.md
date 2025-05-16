# ADR-0014: Use Absolute Raw URLs Instead of Relative Paths for ChatGPT Access

## Status
Accepted

## Context
During development of the PO Skill Assessment toolkit, we observed inconsistent behavior in ChatGPT when loading linked Markdown files from GitHub. Specifically, files such as `characters/collaborative_team.md` or `shared/evaluation_criteria.md` were interpreted differently—or not at all—despite being correctly linked via relative paths in `config/po.yaml` or `README.md`.

Investigation revealed the root cause: **relative paths resolve through GitHub's `blob/` interface**, resulting in HTML-rendered pages rather than the raw Markdown source. ChatGPT cannot reliably extract structured content from these HTML pages.

As a result, in some runs, ChatGPT failed to load expected character profiles or evaluation criteria, instead defaulting to fallback behavior. This created unintended variability—while interesting, it undermined consistency and debuggability.

## Decision
We will **avoid relative paths** and instead use **absolute `https://raw.githubusercontent.com/...` URLs** for all file references intended for ChatGPT ingestion. This includes:

- `README.md` pointers for ChatGPT entry points
- `config/po.yaml` paths to assets (product briefs, characters, prompts, etc.)
- All cross-file references within Markdown documents

## Consequences
- ChatGPT will always receive clean, predictable Markdown source content.
- Reduces surprise behavior such as unintended team or prompt swaps.
- Requires discipline in maintaining raw URLs instead of GitHub-relative links.
- Slightly increases maintenance overhead when renaming or moving files.

## Bonus Outcome
The incident highlighted an unexpected benefit: when paths were misaligned, ChatGPT generated *entirely different teams*, producing a kind of "multiverse onboarding" experience. While accidental, this sparked creative ideas for future training modes or challenge variants.