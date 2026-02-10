---
name: product-maker
description: Converts abstract ideas into concrete product specifications. Use when the user says "I have an idea", "Make an app", or needs a quick MVP plan.
inputs:
  - raw_idea: "(Required) The user's initial vague idea or requirement."
  - target_audience: "(Optional) Who is the app for?"
outputs:
  - project_brief: "A structured PROJECT_BRIEF.md file."
---

# Product Maker Protocol

## 1. Discovery Phase
* **Clarify:** Ask 3 "Killer Questions" to define the scope if the idea is too vague.
* **Core Value:** Define the "One Thing" this product solves perfectly.

## 2. Planning Phase
* **User Stories:** Write 3-5 key stories: "As a [User], I want [Action], so that [Benefit]."
* **Tech Stack:** Recommend the simplest, most robust stack (e.g., Vite + Firebase for web).
* **Data Model:** Roughly sketch the core entities (User, Post, etc.).

## 3. Output (The Blueprint)
Generate a `PROJECT_BRIEF.md` containing:
1.  **Vision Statement**
2.  **Core Features (MVP Scope)**
3.  **Tech Stack Recommendation**
4.  **Rough Database Schema**