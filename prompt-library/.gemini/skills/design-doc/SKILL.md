---
name: design-doc
description: Writes a Google-style Engineering Design Doc. Use for "Architecture", "System Design", "Tech Spec", or "How to build this?".
inputs:
  - feature_scope: "(Required) What specific feature or system are we designing?"
outputs:
  - design_doc: "A markdown file with Context, Design, and Trade-offs."
---

# Design Doc Protocol

## 1. Context & Scope
* **Goals:** What are the success metrics? (e.g., Latency < 200ms).
* **Non-Goals:** What are we explicitly NOT doing? (Scope creeping prevention).

## 2. Detailed Design
* **API Spec:** Define endpoints, inputs, and outputs (JSON schema).
* **Data Model:** ERD or Schema definitions.
* **Flow:** Text-based Sequence Diagram (Mermaid syntax preferred).

## 3. Trade-offs (Crucial)
* List at least 2 options (e.g., SQL vs NoSQL).
* Explain **Why** the chosen solution is better for *this* specific case.