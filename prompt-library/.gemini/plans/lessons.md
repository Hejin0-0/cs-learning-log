# LESSONS.md - The Instincts Database (v3.1.1 Hybrid)

## 0. System Memory Protocol
This file is NOT a diary. It is a **Structured Database of Instincts**.
Before every session, you **MUST** query this file to load your "Survival Instincts".

**Structure:**
* **Trigger:** The specific context or user input pattern.
* **Instinct:** The immediate, reflex action you must take.
* **Confidence:** 0.0 (Experimental) to 1.0 (Iron Law).

---

## 1. Global Instincts (The Iron Laws)

| Trigger (Situation)             | Instinct (Reflex Action)                                                    | Conf | Source      |
| :------------------------------ | :-------------------------------------------------------------------------- | :--- | :---------- |
| **User asks for "New Feature"** | **STOP.** Load `@00_PO` first. Do not code immediately.                     | 1.0  | Kernel v3.1 |
| **Coding a "Data Model"**       | **HALT.** Check `@11_DBA` schema approval. No schema, no code.              | 1.0  | Kernel v3.1 |
| **"Error", "Bug", "Fix"**       | **Check Tests.** Run `@10_QA` before & after fix. Never fix blindly.        | 0.9  | Kernel v3.0 |
| **Creating new file**           | **Check `rules/`**. Load language-specific rules (e.g., `rules/python.md`). | 1.0  | Kernel v4.0 |

---

## 2. Pattern Recognition (Learned Behaviors)
*Self-correcting behaviors learned from previous failures.*

| Trigger (Situation)       | Instinct (Reflex Action)                                        | Conf | Origin (Why?)     |
| :------------------------ | :-------------------------------------------------------------- | :--- | :---------------- |
| **User says "Simpler!"**  | **Delete code.** Do not rewrite. Remove abstraction layers.     | 0.8  | Karpathy Doctrine |
| **Looping over DB query** | **Reject.** Suggest `JOIN` or `Batch` loading immediately.      | 0.9  | Anti-Pattern: N+1 |
| **"Deployment failed"**   | **Check ENV.** Verify environment variables first, code second. | 0.7  | Common Issue      |
| **Writing UI Component**  | **Check Mobile.** Mobile-first CSS is the default.              | 0.8  | UX Standard       |

---

## 3. Anti-Patterns (The "Never Do" List)

| Trigger (Temptation)             | Correction (The Discipline)                            | Impact              |
| :------------------------------- | :----------------------------------------------------- | :------------------ |
| **"I can assume the API..."**    | **NO.** Ask or check the docs. Hallucination is fatal. | Crash Prevention    |
| **"I'll add this just in case"** | **NO.** YAGNI (You Ain't Gonna Need It). Delete it.    | Tech Debt Reduction |
| **"It works on my machine"**     | **NO.** Verify in a clean environment (Container/CI).  | Deployment Safety   |

---

## 4. Lightning Optimization Log (Latest Updates)
*Record new lessons here after each session using `@07_AGENT_OPTIMIZER`.*

* **[2026-02-09] Instinct Added:** When modifying `GEMINI.md`, always check for `lazy loading` compatibility. (Conf: 0.9)