---
name: design-doc
version: 2.0.0
description: 모호한 요구사항을 엔지니어링 청사진(RFC/Design Doc)으로 변환합니다. 다이어그램과 트레이드오프 분석을 포함합니다.
tags: [architecture, system-design, documentation, rfc, mermaid]
---

# 📐 Design Doc Generator

## 1. Core Philosophy (핵심 철학)
* **Measure Twice, Cut Once:** 코딩 시작 전의 1시간 설계가 나중의 10시간 디버깅을 줄입니다.
* **Visuals over Text:** 복잡한 흐름은 줄글보다 하나의 다이어그램(Mermaid)이 훨씬 명확합니다.
* **Defend Your Decisions:** 모든 기술적 선택에는 이유(Why)와 대가(Trade-off)가 명시되어야 합니다.

## 2. Drafting Protocol (작성 프로토콜)

### Phase 1: Context & Scoping (배경 및 범위)
무작정 설계를 시작하지 않고 경계(Boundary)를 설정합니다.
* **Goals:** 이 시스템이 달성해야 할 핵심 비즈니스/기술 목표.
* **Non-Goals:** 명확하게 **하지 않을 것**을 정의하여 스코프 크립(Scope Creep)을 방지합니다.
* **User Stories:** "누가, 어떤 상황에서, 무엇을 하는가?"

### Phase 2: System Architecture (아키텍처 설계)
시스템의 뼈대를 시각화하고 구체화합니다.
* **High-Level Diagram:** 시스템의 전체 구조를 `mermaid` 코드로 시각화합니다 (Flowchart 또는 Sequence Diagram).
* **Data Model:** 데이터베이스 스키마(ERD) 또는 핵심 객체 모델 정의.
* **API Interface:** 주요 엔드포인트(REST/GraphQL), Request/Response 예시.

### Phase 3: Senior-Level Considerations (심화 분석)
주니어와 시니어를 가르는 핵심 섹션입니다.
* **Scalability:** 사용자가 10배, 100배 늘어날 때 병목(Bottleneck) 구간은 어디인가?
* **Safety & Security:** 권한 관리(AuthZ/AuthN), 개인정보 처리, 데이터 유실 방지 대책.
* **Failure Modes:** "DB가 죽으면?", "외부 API가 느려지면?" 등 장애 상황 시나리오 및 복구 전략.

### Phase 4: Alternatives Considered (대안 분석)
"왜 A를 선택했는가?"를 증명하기 위해 기각된 B안을 설명합니다.
* **Option A (Selected):** 선택한 방식의 장점.
* **Option B (Rejected):** 고려했으나 채택하지 않은 방식과 그 이유(비용, 복잡도, 성능 등).

## 3. Output Template (문서 양식)
출력 시 아래 포맷을 엄수하십시오.

---
# 🏗️ [Project Name] Design Doc
> **Status:** Draft / **Author:** Claude / **Date:** YYYY-MM-DD

## 1. Overview
(배경과 해결하려는 문제 요약)

## 2. Architecture
### 2.1 System Diagram
```mermaid
graph LR
    Client --> API_Gateway
    API_Gateway --> Service_A
    Service_A --> Database