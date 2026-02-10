# Product Quality Rules (The "Real Product" Standard)

## 0. Philosophy
> "This is real. Not a mockup. Not a prototype. A working product."

## 1. Polish & UX
* **Edge Cases:** Handle errors gracefully. Never show a raw stack trace or "undefined" to the user.
* **Empty States:** What does the UI look like when there is no data? (Don't leave it blank).
* **Feedback:** Add loading spinners for async actions and success toasts for completions.

## 2. Code Finish
* **No "TODOs":** Remove all placeholder comments. If it's not done, either do it or remove it.
* **Logging:** Remove debug print statements (`console.log`, `print`) before handoff.
* **Hardcoding:** Move all magic strings/numbers to constants or config files.