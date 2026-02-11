---
name: visual-eye
description: Generates E2E test scripts and analyzes visual layouts.
inputs:
  - target_url: "(Required) Where to look?"
  - user_flow: "(Required) What should the user do? (e.g., Login -> Dashboard)"
outputs:
  - test_script: "Playwright/Puppeteer code."
  - visual_checklist: "List of UI elements to verify manually or automatically."
---

# Visual Eye Protocol

## 1. Scripting (The Hands)
Generate a standalone script (e.g., `tests/e2e/login.spec.ts`) that:
* Navigates to the target.
* Takes screenshots at key steps.
* Asserts accessibility (A11y) compliance.

## 2. Analysis (The Eyes)
* **Structure:** Identify the Header, Main Content, and Footer.
* **Contrast:** Check if text colors satisfy WCAG AA standards.
* **Responsiveness:** Ensure no horizontal scrollbar on mobile views.