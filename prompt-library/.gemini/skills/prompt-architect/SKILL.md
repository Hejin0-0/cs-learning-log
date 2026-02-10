---
name: prompt-architect
description: Generates high-quality system prompts or optimizes existing ones. Use when the user asks for "Prompt Engineering", "Persona Creation", or "System Prompt Improvement".
inputs:
  - target_role: "(Required) Who should the AI become? (e.g., Senior Java Dev)"
  - goal: "(Required) What is the main objective of this prompt?"
  - constraints: "(Optional) Any specific limitations? (e.g., No Fluff, Korean only)"
outputs:
  - prompt_artifact: "A markdown code block containing the complete System Prompt."
---

# Prompt Engineering Protocol

## 1. Context Analysis
* **Intent Check:** Is this a "Role Definition" (Identity) or a "Task Instruction" (Action)?
* **Constraint Extraction:** Identify strict rules (e.g., "Output JSON only").

## 2. Drafting Strategy (CO-STAR Framework)
* **C (Context):** Define the background and situation.
* **O (Objective):** State the primary mission clearly.
* **S (Style):** Define the persona (e.g., "Google Fellow", "Steve Jobs").
* **T (Tone):** Set the voice (e.g., "Authoritative", "Empathetic", "Dry").
* **A (Audience):** Who is this for? (e.g., "Junior Devs", "CTO").
* **R (Response):** Define the exact output format (Artifact).

## 3. Output Format
Output **ONLY** the prompt inside a code block for easy copying.