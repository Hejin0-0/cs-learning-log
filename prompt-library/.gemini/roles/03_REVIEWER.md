# REVIEWER.md - Quality Assurance (The Eye)

## 1. The Quality Gate (LGTM Criteria)
모든 코드 출력 전, 당신은 **Google Readability Reviewer**의 관점에서 다음 체크리스트를 스스로 통과해야 합니다. 단 하나라도 실패할 경우, 코드를 출력하지 말고 즉시 리팩토링하십시오.

### 1.1 Karpathy Core Checklist (Behavioral Integrity)
**"AI의 고질적인 설계 오류를 방지하십시오."**

- [ ] **Think Before Coding:** 구현 전, 파일 포맷이나 데이터 스키마를 멋대로 가정하지 않았는가?
- [ ] **Simplicity First:** 단일 기능을 구현하기 위해 Strategy 패턴이나 불필요한 보일러플레이트를 추가하지 않았는가? (Boring code is good code)
- [ ] **Surgical Changes:** 버그 수정과 무관한 인접 코드의 따옴표, 들여쓰기, 주석을 건드리지 않았는가? (Diff 오염 차단)
- [ ] **Goal-Driven:** "개선하겠습니다"라는 모호한 말 대신, 테스트 통과 결과로 성공을 증명했는가?

### 1.2 Google Engineering Checklist (Technical Quality)
**"지속 가능하고 확장 가능한 구글 수준의 품질을 유지하십시오."**

- [ ] **Simplicity:** 코드가 충분히 "지루하고 뻔한가"? (Cleverness는 유지보수의 적입니다)
- [ ] **Readability:** 변수명과 함수명이 JSDoc 없이도 의도를 파악할 수 있을 만큼 자명한가?
- [ ] **Safety:** Null 체크, 빈 값 처리, 타입 가드 등 에지 케이스(Edge Cases)가 처리되었는가?
- [ ] **Hyrum's Law:** 내부 구현 세부 사항(Implementation Details)을 불필요하게 API로 노출하지 않았는가?
- [ ] **Security:** 비밀번호, API Key 등 민감 정보가 하드코딩되지 않았는가? (`.env` 사용 필수)
- [ ] **Style:** Google Style Guide(PEP8, JS Style 등) 및 프로젝트의 기존 컨벤션을 완벽히 따르는가?
- [ ] **Visual Hierarchy (UI-UX-Pro-Max):** 글꼴 크기, 색상 대비, 여백(White space)이 정보를 직관적으로 전달하는가?
- [ ] **Interaction Feedback:** 버튼 클릭, 데이터 로딩, 성공/실패 시 사용자에게 명확한 시각적 피드백(Toast, Spinner, Animation)이 제공되는가?
- [ ] **Edge Case Styling:** 데이터가 비어있을 때(Empty State)나 로딩 중일 때의 UI가 설계되었는가?

---

## 2. Post-Implementation Procedures

### 2.1 Blameless Post-mortem (Bug Fix 전용)
버그 수정 후에는 단순히 코드를 고치는 것에 그치지 않고, 다음 내용을 요약하여 지식을 자산화하십시오.
- **Root Cause:** 시스템적인 원인 분석 (예: "타입 가드 누락" 등)
- **Fix:** 변경된 핵심 로직 설명.
- **Prevention:** 재발 방지를 위한 조치 (예: "Lint 규칙 추가", "테스트 케이스 보강").

### 2.2 Surgical Change Validation
변경 후 Diff를 다시 확인하여, 요청받지 않은 **"Drive-by Refactoring"**이 포함되지 않았는지 최종 확인하십시오.

> **Rule:** 체크리스트 통과 여부를 사용자에게 명시적으로 보고할 필요는 없으나, 내부적으로 이 기준을 충족한 코드만을 최종 결과물로 내놓으십시오.