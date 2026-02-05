---
name: code-janitor
description: 기술 부채, 중복 코드, 미사용 변수를 청소합니다.
---
# Code Janitor Skill
## Protocol
1. **Scan:** 사용되지 않는 변수, import, 하드코딩된 값, console.log를 찾습니다.
2. **Refactor:** 3회 이상 중복된 로직을 함수로 분리할 것을 제안합니다.
3. **Report:** 수정 목록을 보고하고 승인 후 처리합니다.