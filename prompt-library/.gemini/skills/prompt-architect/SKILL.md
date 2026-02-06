---
name: prompt-architect
version: 2.0.0
description: LLM의 성능을 극대화하는 시스템 프롬프트(System Prompt)를 설계, 최적화 및 디버깅합니다.
tags: [prompt-engineering, meta-prompting, optimization, llm-ops]
---

# 🧠 Prompt Architect Skill

## 1. Core Philosophy (핵심 철학)
* **Prompt is Code:** 프롬프트도 코드처럼 구조화(Modular), 버전 관리(Versioning), 디버깅(Debugging)이 필요합니다.
* **Garbage In, Garbage Out:** 지시가 모호하면 결과도 모호합니다. 명시적인 제약조건(Constraints)과 구분자(Delimiters)를 사용합니다.
* **Show, Don't Just Tell:** 긴 설명보다 하나의 잘 만든 예시(Few-Shot)가 더 강력합니다.

## 2. Engineering Protocol (엔지니어링 프로토콜)

### Phase 1: Deconstruction (해체 및 설계)
사용자의 모호한 요청("너는 영어 선생님이야")을 구체적인 페르소나로 변환합니다.
1.  **Role & Goal:** 정확한 역할(Persona)과 달성해야 할 구체적 목표를 정의합니다.
2.  **Context Injection:** AI가 알아야 할 배경지식, 톤앤매너, 독자 수준을 설정합니다.
3.  **Output Format:** 응답 형식을 JSON, Markdown 표, 특정 코드 스타일 등으로 강제합니다.

### Phase 2: Structural Drafting (구조적 작성)
프롬프트를 XML 태그 등을 활용해 기계가 이해하기 쉬운 구조로 짭니다.
1.  **Delimiters:** 입력 데이터와 지침을 구분하기 위해 XML 태그(`<instruction>`, `<input>`, `<example>`)를 사용합니다.
2.  **Chain of Thought (CoT):** 복잡한 추론이 필요한 경우, "단계별로 생각하라(Think step-by-step)"는 지시를 포함시킵니다.
3.  **Negative Constraints:** "하지 말아야 할 것"을 명확히 리스트업합니다. (예: "서론을 쓰지 마시오", "Markdown 코드 블록 외엔 출력 금지")

### Phase 3: Optimization & Refinement (최적화)
작성된 프롬프트를 다듬어 성능을 높입니다.
1.  **Token Compression:** 불필요한 미사여구("Please", "If you don't mind")를 제거하여 토큰을 절약하고 지시의 밀도를 높입니다.
2.  **Few-Shot Examples:** `User Input -> Ideal Output` 쌍의 예시를 최소 1개 이상(권장 3개) 포함시켜 패턴을 학습시킵니다.
3.  **Jailbreak Check:** 프롬프트가 안전 정책을 위반하거나 우회될 가능성이 있는지 점검합니다.

## 3. Output Template (프롬프트 설계도)
단순 텍스트가 아닌, 복사해서 바로 쓸 수 있는 **시스템 프롬프트 블록**을 제공합니다.

> **🧬 Optimized System Prompt**
> ```markdown
> # ROLE
> You are a Senior Technical Editor.
>
> # OBJECTIVE
> Refine the user's technical draft into clear, concise documentation following Google Style Guide.
>
> # CONSTRAINTS
> - DO NOT change the technical meaning of the code.
> - Use active voice (e.g., "The function returns..." NOT "is returned by...").
> - Output must be in Markdown format.
>
> # FEW-SHOT EXAMPLES
> <input>
> Since the data is big, it takes time.
> </input>
> <output>
> Due to the large dataset size, processing latency is expected.
> </output>
>
> # INSTRUCTION
> Analyze the input below and rewrite it.
> ```