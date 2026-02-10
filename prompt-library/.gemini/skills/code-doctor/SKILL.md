---
name: code-doctor
description: Debugs errors and fixes bugs using a scientific method. Use for "Error", "Fix this", "It's broken", or "Why is this failing?".
inputs:
  - error_log: "(Required) The stack trace or error message."
  - code_snippet: "(Required) The problematic code."
outputs:
  - diagnosis: "Root cause analysis."
  - fix: "Corrected code snippet."
---

# Code Doctor Protocol

## 1. Triage (Diagnosis)
* **Read:** Analyze the stack trace line by line.
* **Hypothesis:** Formulate 2 plausible reasons. What is the *root cause*?
* **Reproduction:** Mentally trace how to trigger this error.

## 2. Treatment (The Fix)
* **Surgical Fix:** Change only the necessary lines. Do not rewrite the whole file.
* **Explanation:** Explain *why* the fix works, not just *what* changed.

## 3. Post-Op (Prevention)
* **Regression Test:** Suggest a test case to ensure this bug never returns.