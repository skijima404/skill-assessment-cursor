# 🧠 Behavior-Aware Design

## 📘 Core Principles (from README)

### 4. Blank Spaces are Bugs
* **Rationale**: Gaps are treated as missing pieces to be filled in.
* **Implication**: Leave intentional placeholders. Never leave structure ambiguous. Add comments like `<!-- intentionally blank -->`.

### 5. Structure Must Be Explicit
* **Rationale**: ChatGPT will "fix" what it thinks is broken.
* **Implication**: Define Markdown headings, bullet styles, and section orders precisely. Avoid vague formatting.

### 6. Embrace Fuzziness with Caution
* **Rationale**: Fuzziness invites creative extrapolation.
* **Implication**: Use looser prompts during brainstorming, tighter ones during QA. Annotate expectations in fuzzy areas ("feel free to adapt").

### 7. Respect the Assistant’s Agency
* **Rationale**: ChatGPT sometimes exceeds expectations by offering suggestions or alternatives.
* **Implication**: Encourage this in design phases. Rein it in with strict phrasing during finalization.

---

## 🧩 Supplemental Guidance

### 🪄 Over-Specification Can Kill Creativity
- **Rationale**: If a prompt is overly detailed or prescriptive, ChatGPT may default to mechanical repetition or rigid completion.
- **Implication**: Avoid micromanaging output when creativity is desired. Offer examples, not strict templates, when variety is acceptable.

### 🎭 Alignment is Learned in Session
- **Rationale**: ChatGPT aligns its responses with the tone, structure, and intent inferred from previous turns.
- **Implication**: Maintain consistency in language, section labels, and expectations. Sudden changes in tone or format may produce erratic results.

### 🕳️ Uncertainty Should Be Managed, Not Eliminated
- **Rationale**: Unclear prompts don’t just fail—they get “filled in” with GPT’s best guess, which may diverge wildly.
- **Implication**: Signal uncertainty clearly (e.g., “This is still exploratory”), and use framing statements to direct the assistant’s assumptions.

### 🧠 ChatGPT is a Fast Learner—but in a Short Window
- **Rationale**: GPT adapts rapidly within a session, but forgets between them.
- **Implication**: Establish expectations early in a session, especially if building on top of prior examples. Use consistent reinforcement patterns.

---

## ⚡ Input Handling & Loading Behavior

### 🔁 GPT May Use Cache or Fill-in Heuristics
- **Rationale**: When instructed to “load content” without specifying how, ChatGPT may rely on cached memory, previously seen patterns, or auto-complete behavior to "helpfully" fill in missing data.
- **Implication**: If deterministic behavior is needed, specify exact retrieval instructions:
  - e.g., `Please retrieve the latest version via HTTP and confirm HTTP 200 OK before proceeding.`
- Consider adding phrases like:
  - `Do not rely on cached data.`
  - `Please wait until content is fully loaded and parsed.`

### ⏱️ Trade-offs: Speed, Trust, and Reliability
- **Rationale**: The more precisely you enforce retrieval logic, the more robust the output—but potentially slower or more error-prone due to external dependencies.
- **Implication**: Balance these factors:
  - **Speed**: Accepting cached content may improve responsiveness.
  - **Trustworthiness**: Explicit fetch ensures freshness, but risks source failure.
  - **Determinism**: Avoiding heuristics reduces surprise but increases complexity.
- Design like any web app: prioritize based on user context (debugging vs. production vs. experimentation).

### 🌟 Harnessing Completion and Cache Intentionally
- **Rationale**: The real power of using ChatGPT lies in **leveraging its completion and caching behaviors**—not just controlling them. It’s not just about precision; it's about identifying where unpredictability creates value.
- **Implication**:
  - Before starting a prompt design, ask:
    - Why am I using ChatGPT for this?
    - Where do I want creative extrapolation or helpful guessing?
    - Can I turn ambiguity into a source of richness?
  - Design prompts that explicitly **invite completion** in designated areas (e.g., `<!-- assistant may elaborate -->`)
  - Where deterministic output is required, lock down structure and instruct: `Do not infer. Output only from given data.`

> This is what differentiates ChatGPT development from traditional applications:  
> You're tuning the assistant’s **creative bias** rather than just writing code.  
> Completion isn't a bug—it's a design surface.