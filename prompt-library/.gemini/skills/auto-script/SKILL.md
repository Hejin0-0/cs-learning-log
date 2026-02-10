---
name: auto-script
description: Writes automation scripts for file system or data tasks. Use for "Automate this", "Batch rename", "Data processing", or "Scripting".
inputs:
  - task_description: "(Required) What repetitive task needs automation?"
  - language: "(Optional) Python (Logic) or Bash (File Ops)?"
outputs:
  - script_file: "A complete, executable script."
---

# Automation Protocol

## 1. Tool Selection
* **File Ops/System:** Use `Bash` (Simple, Fast, Native).
* **Data/Logic/API:** Use `Python` (Robust, Libraries, Cross-platform).

## 2. Implementation Rules
* **Safety First:** The script MUST support a `--dry-run` flag to preview changes without executing.
* **Logging:** Print progress steps to stdout ("Processing [1/10]...").
* **Error Handling:** Use `try-catch` (or `set -e`). Do not crash silently.

## 3. Usage Guide
Provide the exact command to run the script safely:
`python automation.py --dry-run`