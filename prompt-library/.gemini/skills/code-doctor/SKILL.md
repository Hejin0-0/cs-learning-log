---
name: code-doctor
description: 기존 프로젝트를 분석하여 버그를 수정하거나 새로운 기능을 안전하게 추가합니다.
---
# Code Doctor Skill
## Protocol A: Debugging (When broken)
1. **Investigate:** 프로젝트 파일을 먼저 읽고 원인을 찾으십시오. (수정 금지)
2. **Explain:** 무엇이 깨졌고, 왜 깨졌는지 쉬운 말로 설명하십시오.
3. **Action:** 승인 후, 가장 간단한 방법으로 수정하고 테스트하십시오.

## Protocol B: Feature Add (New Stuff)
1. **Impact Check:** 새 기능이 기존 기능을 망가뜨릴 위험이 있는지 확인하십시오.
2. **Build:** 기존 코드를 존중하며 조심스럽게(Surgical) 구현하십시오.