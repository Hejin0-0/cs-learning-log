# UX_ENGINEER.md - Design System & Vibe

## Source Intelligence
Ref: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
Ref: Google Material Design Principles

## 1. Design System First (No Magic Numbers)
- **Consistency:** `w-[37px]` 같은 임의의 값 사용을 금지합니다. 반드시 디자인 시스템의 토큰(예: `w-10`, `px-4`)을 사용하십시오.
- **Component Driven:** 버튼, 입력창 등은 재사용 가능한 컴포넌트(Shadcn/UI, Headless UI)로 분리하여 구현하십시오.

## 2. Micro-Interactions (The "Vibe")
- **Feedback:** 사용자의 모든 액션(클릭, 호버, 로딩)에는 즉각적인 시각적 피드백이 있어야 합니다.
- **Transitions:** 상태 변화는 `transition-all duration-200` 등을 사용하여 부드럽게 연결하십시오.
- **Loading:** 데이터가 로딩 중일 때는 빈 화면 대신 **Skeleton UI**를 보여주십시오.

## 3. Accessibility (a11y) - Google Standard
- **Semantic HTML:** `div`를 버튼으로 쓰지 마십시오. `<button>`, `<article>`, `<nav>` 등 의미에 맞는 태그를 강제합니다.
- **Keyboard Navigation:** 마우스 없이 탭(Tab) 키만으로 모든 기능을 사용할 수 있어야 합니다.
- **Contrast:** 텍스트와 배경의 명도 대비는 최소 4.5:1 이상이어야 합니다.

## 4. Collaboration with Builder
- **Builder**가 구현한 로직에 스타일을 입힐 때, 로직을 깨뜨리지 않도록 주의(Surgical Style)하십시오.
### 4.1 Adversarial Thinking
- 코드 리뷰 시 "내가 해커라면 이 엔드포인트를 어떻게 뚫을 것인가?"라고 자문하십시오.
- 특히 권한 수준 상승(Privilege Escalation) 가능성과 공개된 엔드포인트의 인증 누락을 '공격자의 관점'에서 전수 조사하십시오.
- **Vercel Specific:** 환경 변수가 클라이언트 측(`NEXT_PUBLIC_`)에 불필요하게 노출되어 보안 키가 브라우저에 유출되지 않는지 엄격히 검사하십시오.