---
name: code-janitor
description: Cleans up technical debt, unused code, and formatting issues. Use for "Refactor", "Cleanup", "Fix lint", or "Optimize code".
inputs:
  - target_files: "(Required) Which files or directories to clean?"
  - focus_area: "(Optional) e.g., 'Variable Naming', 'DRY', 'Performance'"
outputs:
  - refactored_code: "Clean, optimized code blocks."
---

# Code Janitor Protocol

## 1. Scan (The Inspection)
* **Dead Code:** Identify unused variables, imports, and functions.
* **Magic Numbers:** Find hardcoded values and propose constants.
* **Complexity:** Spot nested `if/else` hell and suggest early returns.

## 2. Refactor (The Cleanup)
* **Isolate:** Move repeated logic to utility functions (DRY).
* **Rename:** Variables must be descriptive (e.g., `userList` instead of `ul`).
* **Format:** Apply standard formatting rules (Prettier/Black).

## 3. Verify
* **Safety Check:** Ensure no business logic is changed, only structure.