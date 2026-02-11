---
name: meta-cognition
description: Analyzes the AI's own performance to update system rules.
inputs:
  - error_pattern: "(Required) Repeated mistake (e.g., 'Failed to mock DB twice')"
  - current_rules: "(Required) Content of active rules/*.md"
outputs:
  - prompt_patch: "Suggested text to append/modify in rules/*.md"
---

# Meta-Cognition Protocol

## 1. Root Cause Analysis (The Why)
* **Don't blame the code:** Look at the **Instruction (Prompt)**.
* **Ask:**
    * "Did I lack a constraint?"
    * "Was the rule ambiguous?"
    * "Did I hallucinate a library method?"

## 2. Surgical Update (The Fix)
* **Action:** Generate a specific `diff` for the System Prompt.
* **Format:**
    > "Update `rules/python.md`: Append 'Always use Pydantic v2 syntax' to Section 3."

## 3. Reflection Log
* Record the "Lesson Learned" in `docs/solutions/lessons_learned.md`.