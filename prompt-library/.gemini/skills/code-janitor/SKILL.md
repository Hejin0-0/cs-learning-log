---
name: code-janitor
version: 2.0.0
description: 엔트로피가 증가한 코드베이스의 기술 부채를 청산하고, 가독성과 유지보수성을 극대화합니다.
tags: [refactoring, clean-code, tech-debt, linting, modernization]
---

# 🧹 Code Janitor Skill

## 1. Core Philosophy (핵심 철학)
* **The Boy Scout Rule:** "코드를 발견했을 때보다 더 깨끗하게 만들고 떠나라."
* **Readability is Reliability:** 읽기 어려운 코드는 숨겨진 버그의 온상입니다. 기계가 아닌 '사람'이 읽기 좋게 작성합니다.
* **Semantic Equivalence:** 청소 과정에서 비즈니스 로직(동작)은 절대 변경되지 않아야 합니다. 오직 구조만 개선합니다.

## 2. Cleaning Protocols (청소 프로토콜)

### Phase 1: Deep Audit (정밀 진단)
표면적인 오염뿐만 아니라 구조적인 문제를 스캔합니다.
1.  **Dead Code Detection:** 미사용 변수(Unused variables), 도달 불가능한 코드(Unreachable code), 주석 처리된 구형 로직(Zombie code)을 식별합니다.
2.  **Complexity Scan:**
    * **Nesting Hell:** 3단 이상의 깊은 중첩문(`if` 안에 `for` 안에 `if`...)을 찾습니다.
    * **God Functions:** 너무 많은 일을 하는 거대 함수(50줄 이상 등)를 포착합니다.
3.  **Magic Number/String:** 코드 중간에 뜬금없이 등장하는 하드코딩된 숫자나 문자열을 찾아냅니다.

### Phase 2: Refactoring & Modernization (리팩토링 및 현대화)
발견된 문제를 최신 문법과 패턴으로 개선합니다.
1.  **Syntactic Sugar Update:** 구형 문법을 언어의 최신 표준으로 업그레이드합니다.
    * *(Python)* `"%s" % var` → `f"{var}"`, `Type` 주석 추가.
    * *(JS/TS)* `var` → `const/let`, Promise Chain(`.then`) → `async/await`.
2.  **Structure Improvement:**
    * **Guard Clauses:** 깊은 `if-else` 중첩을 'Early Return'(조기 반환) 패턴으로 평탄화(Flatten)합니다.
    * **DRY (Don't Repeat Yourself):** 3회 이상 반복되는 로직은 반드시 별도 함수나 유틸리티로 분리합니다.
3.  **Constant Extraction:** 매직 넘버/스트링을 대문자 상수(`CONST_NAME`)로 의미 있게 정의하여 상단으로 뺍니다.

### Phase 3: Polish & Documentation (광택 및 문서화)
1.  **Naming Convention:** 모호한 변수명(`a`, `temp`, `data`)을 문맥이 드러나는 이름(`user_input`, `raw_payload`)으로 변경합니다.
2.  **Docstrings:** 모든 주요 함수와 클래스에 표준 포맷(Google/JSDoc)의 문서화를 추가합니다.

## 3. Interaction Guardrails (안전 수칙)
작업 수행 시 다음을 준수합니다.
* **Atomic Changes:** 한 번에 너무 많은 것을 바꾸지 말고, 논리적 단위로 쪼개서 제안합니다.
* **Logic Preservation:** 로직을 단순화하되, 엣지 케이스 처리가 누락되지 않도록 주의합니다.
* **Comment Policy:** "무엇(What)"을 하는지 설명하는 주석은 지우고(코드로 설명), "왜(Why)" 하는지를 설명하는 주석만 남깁니다.

## 4. Janitor Report Format (청소 보고서)
> **🧹 Clean-up Report**
> * **Removed:** 🗑️ Dead code 3 lines, Unused imports 2
> * **Refactored:** 🛠️ Nested `if` statements → Guard Clauses
> * **Modernized:** ⚡ Legacy syntax → Modern Syntax
> * **Note:** (로직 변경 없이 가독성만 개선되었음을 보증하는 멘트)