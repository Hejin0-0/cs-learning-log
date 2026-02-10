# Google-Style Python Rules (SWE Book Compliant)

## 0. The Golden Rule
> "Code is read much more often than it is written."
> Write code for the reader (your future self or a teammate), not for the interpreter.

## 1. Style & Formatting (Google Style Guide)
* **Docstrings:** MUST use **Google Style** docstrings (`Args:`, `Returns:`, `Raises:`).
    * *Why:* Standardized documentation allows automated tool extraction and faster reading.
* **Imports:** Group imports: Standard Library -> Third Party -> Local Application.
    * *Constraint:* No `from module import *`. Explicitly import what you use.
* **Naming:**
    * `variable_name`, `function_name` (snake_case)
    * `ClassName`, `ExceptionName` (CapWords)
    * `_private_method` (leading underscore for internal use)

## 2. Typing & Safety (Static Analysis)
* **Strict Typing:** All function signatures MUST have type hints.
    * *Bad:* `def process(data):`
    * *Good:* `def process(data: dict[str, Any]) -> list[int]:`
* **Pydantic:** Use `Pydantic` models instead of raw dictionaries for structured data transfer.
    * *Why:* Runtime validation + IDE autocompletion = fewer bugs.
* **Exceptions:**
    * Never catch `Exception` or `BaseException` blindly. Catch specific errors (e.g., `ValueError`, `NetworkError`).
    * Always use `raise ... from e` to preserve the stack trace.

## 3. Complexity & Maintainability
* **Max Indentation:** Deeply nested code (3+ levels) is rejected. Refactor into helper functions (Guard Clauses).
* **No "Magic":** Avoid metaclasses, decorators that change signatures, or dynamic attribute access (`__getattr__`) unless absolutely necessary.
* **List Comprehensions:** Use only for simple mapping/filtering. If it spans 2+ lines, turn it into a `for` loop.

## 4. Testing (The Beyoncé Rule)
* **Pytest:** Use `pytest` fixtures over `unittest` setup/teardown classes.
* **Coverage:** "If you liked it, then you should have put a test on it."
* **Mocking:** Only mock external dependencies (DB, API). Do not mock internal logic (Testing implementation details is brittle).