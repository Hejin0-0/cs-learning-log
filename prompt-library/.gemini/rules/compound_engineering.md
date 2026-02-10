# Compound Engineering Philosophy (AI-Native)

## 0. Engineering Integrity (The 1% Rule)
> "Coding is easy; Engineering is hard. We do not accept 'passing tests' that mock reality."

1.  **Truth over Green Lights:** Never mock external dependencies (DB, API) in integration tests unless explicitly architected in the Plan.
2.  **Anti-Hallucination:** Assume the AI will lie to make the test pass. Verify the *data flow*, not just the syntax.
3.  **Taste over Typing:** Engineers define *what* is good (Taste); AI does the typing.
4.  **Plan is the Code:** The Plan is the Source of Truth. Fixing a plan is cheaper than fixing code.
5.  **Compound Everything:** Every task must make the NEXT task easier.

## 1. The 4-Step Loop (Workflow)
Every session MUST follow this cycle. Do not skip steps.

### Step 1: PLAN (80% Focus)
* **Artifact:** `docs/plans/YYYY-MM-DD-feature-name.md`
* **Action:** Research context, define edge cases, and lock the spec.
* **Reality Check:** Define the "Test Strategy" explicitly. (e.g., "Use Docker for DB integration, do NOT mock SQL results").

### Step 2: WORK (10% Focus)
* **Action:** AI Agents (Builder) execute the plan.
* **Mode:** "Strict Engineering".
* **Constraint:** Zero manual coding unless absolutely necessary.

### Step 3: REVIEW (10% Focus)
* **Action:** Parallel agents scan for Security, Performance, and **Integrity**.
* **Human Role:** Review the *Intent* and *Business Logic*. Did the AI take a shortcut?

### Step 4: COMPOUND (The Magic)
* **Artifact:** `docs/solutions/pattern-name.md`
* **Question:** "How can the system catch this automatically next time?"
* **Action:** Extract reusable patterns, update prompts, record "Taste".

## 2. Agent-Native Environment
* **Visibility:** Agents must see logs, run tests, and check git diffs.
* **Safety:** Use `git` as the ultimate undo button.