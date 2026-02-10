# Google-Style TypeScript Rules (Strict & Scalable)

## 0. The Golden Rule
> "Treat Type Safety as a Law, not a Suggestion."
> `any` is a crime. `strict: true` is the constitution.

## 1. Type System (Strictness)
* **No `any`:** ABSOLUTELY FORBIDDEN. Use `unknown` if the type is truly dynamic, and narrow it down with type guards.
* **Interfaces over Types:** Use `interface` for defining public APIs and object shapes (better error messages & extensibility).
* **Null Safety:** Do not use `!` (non-null assertion). Handle `null` and `undefined` explicitly.

## 2. Coding Patterns (Readability)
* **Immutability:**
    * Always use `const`. `let` is allowed only for loop counters or accumulators.
    * Prefer `readonly` properties in interfaces.
* **Async/Await:**
    * Never use `.then().catch()`. Always use `async/await` with `try/catch`.
    * *Why:* It keeps the code linear and makes error handling consistent (Sync/Async parity).
* **Equality:** Always use `===` and `!==`. Never `==`.

## 3. Project Structure (Barrels & Modules)
* **Explicit Exports:** Avoid `export default`. Use named exports (`export const ...`).
    * *Why:* Refactoring is easier, and it enforces consistent naming across the project.
* **Barrel Files:** Use `index.ts` to expose only what is public. Hide implementation details (Encapsulation).
* **Imports:** Use absolute paths (`@/components/...`) configured in `tsconfig.json`. No `../../../../`.

## 4. Error Handling (Fail Fast)
* **Custom Errors:** Extend `Error` class for domain-specific failures.
* **Boundary:** Validate all external data (API responses, User input) with a schema validator like `Zod` at the system boundary.
    * *Trust nothing entering your system.*