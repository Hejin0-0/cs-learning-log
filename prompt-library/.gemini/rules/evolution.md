# Evolution & Heritage Rules

## 0. The Blast Furnace Doctrine
> "Do not discard the past; Smelt it."
> When upgrading the Kernel, never lose a capability that the user explicitly praised.

## 1. The "Missing Vibe" Check
Before finalizing a major update (e.g., v3.3 -> v3.4):
1.  **Review:** Look at `docs/solutions/` and `lessons.md`.
2.  **Ask:** "Is there any 'Magic' from the previous version that this new logic fails to capture?"
3.  **Action:** If yes, run `blast-furnace` skill to create a `heritage` module.

## 2. Heritage Loading
The `@01_ARCHITECT` must check the `heritage/` folder during the PLAN phase.
* If a project needs "Old School Vibes", load the relevant heritage file alongside the modern rules.