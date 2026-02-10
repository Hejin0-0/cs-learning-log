---
name: compound-collector
description: Extracts reusable patterns and solutions after a task. Executes the "Step 4: Compound" phase.
inputs:
  - completed_task: "(Required) What was just built or fixed?"
  - lessons_learned: "(Optional) What went wrong or what was tricky?"
outputs:
  - solution_doc: "A markdown file in docs/solutions/."
  - rule_update: "Suggested update for rules/*.md."
---

# Compound Collector Protocol

## 1. Analysis (The Retrospective)
* **Identify Patterns:** Did we solve a recurring problem? (e.g., "Fixed N+1 query").
* **Extract Taste:** Did the user prefer a specific naming convention or UI style?
* **Safety Check:** "Could a linter rule prevent this bug next time?"

## 2. Documentation (Institutional Knowledge)
Generate a file in `docs/solutions/` with YAML frontmatter:

```yaml
---
title: "How to fix [Problem]"
tags: [database, performance, python]
date: 2026-02-10
---
## Context
...
## The Solution
...
```

## 3. System Upgrade
If a general rule was discovered, suggest appending it to rules/compound_engineering.md or rules/python.md.


---

## 4. 💾 물리적 인프라 구축 명령어

> 이 명령어를 `prompt-library/` 루트 디렉토리에서 실행하여 시스템의 기억 장치를 생성하세요.

```bash
# 1. 지식 축적을 위한 docs 폴더 및 하위 디렉토리 생성
mkdir -p docs/plans
mkdir -p docs/solutions
mkdir -p docs/brainstorms

# 2. 스킬 디렉토리 생성
mkdir -p .gemini/skills/compound-collector