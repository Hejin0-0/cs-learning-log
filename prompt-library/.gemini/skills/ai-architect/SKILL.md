---
name: ai-architect
description: Designs AI/LLM systems including RAG pipelines, Agent workflows, and Evaluation strategies. Use for "Design RAG", "Build Chatbot", or "AI System Architecture".
inputs:
  - use_case: "(Required) What is the AI solving? (e.g., Q&A over PDF)"
  - scale: "(Optional) Prototype or Production?"
outputs:
  - architecture_doc: "Component stack (Model, Vector DB, Orchestrator) and Data Flow."
---

# AI Architecture Protocol

## 1. Strategy Selection
* **Simple Q&A:** Direct Prompting or simple RAG.
* **Complex Reasoning:** Agentic Workflow (ReAct Pattern).
* **Domain Specific:** RAG vs Finetuning (Rule of thumb: RAG for knowledge, Finetuning for style/format).

## 2. Component Stack
* **LLM:** Choose model size based on complexity (Gemini Flash vs Pro).
* **Memory:** Vector DB (Pinecone/Chroma) vs Keyword Search.
* **Orchestrator:** LangChain vs Native Code (Start simple).

## 3. Evaluation Plan
* How will we measure success? (e.g., "Correctness on 50 golden questions").
* Define the "AI Judge" criteria.