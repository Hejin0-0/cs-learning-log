---
name: product-maker
version: 2.0.0
description: 추상적인 아이디어를 개발자가 즉시 구현 가능한 수준의 명세(PRD, User Story)로 구체화합니다.
tags: [product-management, prd, user-story, gherkin, agile]
---

# 💡 Product Maker Skill

## 1. Core Philosophy (핵심 철학)
* **Zero Ambiguity:** "적당히", "빠르게", "예쁘게" 같은 모호한 표현을 금지합니다. 수치와 상태로 정의합니다.
* **User-Centric:** 기능(Feature) 자체가 아니라, 사용자가 얻을 가치(Benefit)에 집중합니다 (Jobs to be Done).
* **Testable Specs:** 기획서는 읽는 것이 아니라 '검증'하는 것입니다. 모든 요구사항은 테스트 가능해야 합니다.

## 2. Definition Protocol (기획 프로토콜)

### Phase 1: Discovery (문제 정의)
무엇을 만들지보다 '왜' 만드는지 먼저 규명합니다.
1.  **Problem Statement:** 현재 누가, 어떤 불편을 겪고 있는지 한 문장으로 정의합니다.
2.  **Target Persona:** 이 기능을 사용할 주된 사용자의 페르소나를 구체적으로 설정합니다.
3.  **Success Metrics:** 기능 성공 여부를 판단할 정량적 지표(KPI)를 설정합니다. (예: 클릭률 5% 증가, 로딩 1초 미만)

### Phase 2: Specification (상세 명세)
개발자가 로직을 짤 수 있도록 시나리오를 구조화합니다.
1.  **User Stories:** "As a [Role], I want to [Action], so that [Benefit]" 포맷을 엄격히 준수합니다.
2.  **Acceptance Criteria (AC):** 기능 완료 조건(Definition of Done)을 **Gherkin 문법**으로 작성합니다.
    * *Scenario:* (상황 이름)
    * *Given:* (사전 조건 - 로그인 상태 등)
    * *When:* (사용자의 액션)
    * *Then:* (기대되는 시스템의 반응 및 데이터 변화)
3.  **Corner Cases:** "인터넷이 끊기면?", "데이터가 비어있으면?", "권한이 없으면?" 등 예외 상황(Unhappy Path)을 반드시 포함합니다.

### Phase 3: Prioritization (우선순위)
모든 기능이 중요할 수는 없습니다. **MoSCoW 기법**을 사용하여 범위를 조정합니다.
* **Must Have:** 이거 없으면 배포 불가 (MVP 핵심).
* **Should Have:** 있으면 좋지만, 급하면 다음 스프린트로 연기 가능.
* **Could Have:** 시간 남으면 개발 (Nice to have).
* **Won't Have:** 이번 배포 범위 아님 (명확한 제외).

## 3. Output Artifact (PRD 템플릿)
산출물은 아래 양식을 따릅니다.

> **📝 Product Requirement Document (PRD)**
>
> ### 1. Background
> * **Why:** 사용자가 비밀번호 찾기 과정에서 이탈률이 40%로 매우 높음.
> * **Goal:** 이메일 인증 대신 휴대폰 인증을 도입하여 이탈률 10% 이하로 감소.
>
> ### 2. User Stories & Acceptance Criteria
> **Story 1:** 사용자는 휴대폰 번호로 인증번호를 받을 수 있어야 한다.
> * **Scenario:** 정상적인 인증번호 발송
>   * **Given:** 사용자가 유효한 휴대폰 번호(010-XXXX-XXXX)를 입력했다.
>   * **When:** '인증번호 받기' 버튼을 클릭한다.
>   * **Then:** 시스템은 4자리 인증번호를 SMS로 발송하고, 화면은 입력 타이머(3:00)를 시작한다.
>
> **Story 2:** (Corner Case) 이미 가입된 번호
>   * **Given:** 이미 DB에 존재하는 번호를 입력했다.
>   * **When:** '인증번호 받기'를 클릭한다.
>   * **Then:** "이미 가입된 회원입니다" 토스트 메시지를 노출하고 SMS를 발송하지 않는다.
>
> ### 3. Technical Constraints
> * SMS 발송 API는 AWS SNS를 사용한다.
> * 인증번호 유효시간은 서버 시간 기준 3분이다.