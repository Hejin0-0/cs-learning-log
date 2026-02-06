---
name: auto-script
version: 2.0.0
description: 반복적인 작업을 멱등성(Idempotency)과 안정성이 보장된 Python/Shell 스크립트로 엔지니어링합니다.
tags: [automation, python, shell, devops, efficiency]
---

# 🤖 Auto Script Skill

## 1. Core Philosophy (핵심 철학)
* **Safety First:** 모든 자동화는 시스템에 되돌릴 수 없는 손상을 줄 위험이 있습니다. 기본적으로 `dry-run`(가상 실행)을 지원해야 합니다.
* **Idempotency (멱등성):** 스크립트를 한 번 실행하든 백 번 실행하든, 결과는 항상 같아야 하며 에러가 나지 않아야 합니다. (예: 폴더 생성 전 존재 여부 확인)
* **Portability:** "내 컴퓨터에서만 되는 코드"는 작성하지 않습니다. 경로(Path) 처리는 OS 독립적으로 설계합니다.

## 2. Execution Protocol (실행 프로토콜)

### Step 1: Risk Assessment & Strategy (위험 평가 및 전략 수립)
작업을 시작하기 전, 다음 항목을 스스로 점검합니다.
* **Destructive Check:** 파일 삭제, 덮어쓰기 등의 위험 작업이 포함되어 있는가? -> *필수: 백업 로직 또는 확인 절차 추가.*
* **Tool Selection:**
    * *Python:* 복잡한 로직, 데이터 처리, 크로스 플랫폼 호환성이 필요할 때 (권장).
    * *Shell/Bash:* 단순 파이프라인 연결, 시스템 네이티브 명령어가 주력일 때.

### Step 2: Architecture Design (설계)
코드 작성 전, 스크립트의 뼈대를 구상합니다.
* **Dependency:** 필요한 라이브러리나 외부 도구가 무엇인지 식별합니다.
* **Logging:** 단순 `print()`가 아닌 `logging` 모듈을 사용하여 정보(Info), 경고(Warning), 에러(Error)를 구분합니다.
* **Arguments:** 하드코딩된 변수를 피하고 `argparse`(Python)나 플래그(Shell)를 통해 입력을 받도록 설계합니다.

### Step 3: Implementation (구현 - The "Legit" Standard)
작성되는 코드는 다음 표준을 엄격히 준수해야 합니다.
1.  **Shebang & Encoding:** `#!/usr/bin/env python3` 및 `utf-8` 선언.
2.  **Dry-Run Capability:** 실제로 변경을 가하지 않고 로그만 출력하는 `--dry-run` 모드를 기본 구현합니다.
3.  **Error Handling:** `try-except` 블록(Python) 또는 `set -e`(Shell)를 사용하여 예기치 않은 오류 시 스크립트가 안전하게 종료(Graceful Shutdown)되도록 합니다.
4.  **Type Hinting & Docstrings:** (Python의 경우) 타입 힌트와 Google Style Docstring을 포함합니다.

### Step 4: Handoff & Guide (인계 및 가이드)
코드와 함께 다음 정보를 제공합니다.
* **Prerequisites:** 필요한 의존성 설치 명령어 (예: `pip install -r requirements.txt` 혹은 `pip install pandas requests`).
* **Usage Examples:** 초보자도 바로 복사해서 쓸 수 있는 실행 예시 명령어.
    * `python script.py --dry-run` (테스트용)
    * `python script.py --force` (실제 실행용)

## 3. Review Checklist (자가 점검)
결과물을 출력하기 전 확인하십시오:
- [ ] 절대 경로(C:\Users\...) 대신 상대 경로를 사용했는가?
- [ ] 실행 중간에 실패해도 데이터가 오염되지 않는가?
- [ ] 스크립트 실행 완료 시 성공/실패 여부를 명확히 알리는가?