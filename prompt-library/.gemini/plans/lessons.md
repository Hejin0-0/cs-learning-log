# Kaizen Log (Continuous Improvement)

이 파일은 프로젝트의 **장기 기억(Long-term Memory)**입니다.
**Andrej Karpathy의 통찰**에서 도출된 절대 원칙과, **Agent Lightning**이 실전에서 학습한 교훈을 기록합니다.
세션 시작 시 이 내용을 로드하여 동일한 실수를 미연에 방지하십시오.

## 🛑 Karpathy's Anti-Patterns (Never Do This)
아래 항목들은 **Andrej Karpathy**가 지적한 LLM의 고질적인 실수들입니다. 절대 반복하지 마십시오.

1.  **Think Before Coding [Assumption]:**
    * 파일 형식, 필드, 범위를 묵시적으로 가정하고 진행하는 행위.
    * 파일 경로나 데이터 구조를 추측하지 말고, 반드시 `ls`나 `cat`으로 확인 후 진행하십시오.
2.  **Simplicity First [Mindset]:**
    * 단순 계산에 디자인 패턴(Strategy, Factory)을 적용하거나, 요청하지 않은 기능을 "유용할 것 같아서" 추가하는 행위.
3.  **Surgical Changes [Refactor]:**
    * 버그 수정 중 관련 없는 코드의 스타일(들여쓰기, 따옴표, 주석)이나 타입 힌트를 건드리는 행위 (Diff 오염 방지).
4.  **Goal-Driven [Execution]:**
    * 구체적인 테스트나 검증 계획 없이 "코드 리뷰하고 개선하겠습니다"라고 모호하게 말하는 행위.

## 💡 Key Insight
**"Overcomplicated code isn't obviously wrong—it's just premature."**
지금 당장 필요한 코드만 작성하십시오. 미래의 확장성은 나중에 걱정하십시오.

---

## 📊 Lightning Optimization Log
*(이곳은 `AGENT_OPTIMIZER`가 실패로부터 배운 교훈을 실시간으로 기록하는 공간입니다.)*

| Date   | Trigger (Failure) | Learned Policy (New Rule) |
| :----- | :---------------- | :------------------------ |
| (Auto) | (Auto)            | (Auto)                    |