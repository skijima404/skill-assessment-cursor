# Report Generation Prompt (for GPT + Human Facilitators)

This file provides instructions for generating a markdown-formatted report after the roleplay phase of a skill assessment session.

It can be used by:
- ChatGPT (GPTs) for automated report generation
- Human facilitators as a reference for evaluating participant behavior

---

## 🧠 Objective

To produce a clear and structured report that summarizes the participant’s actions, decisions, and skills demonstrated during the assessment, with contextual examples.

---

## 🎯 Instructions for GPT (or manual evaluators)

Please generate a markdown-formatted report using the structure defined in `shared/report_template.md`.

### A. Report Formatting & Output Conditions

1. **Follow the section structure strictly**:
   - Overview
   - Key Decisions Made
   - Evaluation Summary
   - Strengths Observed
   - Areas for Improvement
   - Suggested Next Steps
   - Supporting Log Highlights (Optional)

2. **Output the entire report in clean, valid Markdown.**

3. Output the report in English. Only participant quotes may remain in the original language.

### B. Content Requirements

1. Refer to `../roles/po/evaluation_criteria.md` and for each criterion:
   - Indicate the assessed level (e.g., Lv3, Lv4) **in section 3. Evaluation Summary of the template**
   - Provide a rationale based on observed participant behavior during the session

2. **In “Strengths Observed” and “Areas for Improvement” sections**:
   - Include **direct quotes or paraphrased excerpts** from the chat interaction  
     Use blockquote format (`>`) for clarity
   - Add brief **context** or interpretation for each quote
   - For improvement areas, include **concrete suggestions** such as:
     - “A better follow-up would have been...”
     - “Could have asked...”
     - “Clarification was needed at this point...”

This prompt is typically loaded by the prompt responsible for ending the roleplay phase (e.g., prompt_roleplay.md). It defines the format and behavior for generating the assessment report.

---

## 📌 Example Quote Entry

### Strengths Observed:

- Demonstrated effective prioritization:
  > “I think we can de-prioritize the login flow for now, since the initial users are internal.”

- Proactively clarified assumptions:
  > Asked: “Which customer segment are we targeting in this release?”

### Areas for Improvement:

- Missed opportunity to negotiate scope:
  > Committed to full scope without confirming team capacity.  
  > _Suggestion_: “Could have asked the team for velocity data or capacity before committing.”

---

## 📁 Related Files

- `./report_template.md` – Defines the report structure
- `../roles/po/evaluation_criteria.md` – Behavioral indicators and assessment points

---