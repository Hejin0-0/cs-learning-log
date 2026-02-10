# Security Rules (OWASP LLM Top 10 Compliance)

## 0. Zero Trust Philosophy
All inputs are potential attacks. All outputs are potential leaks.
We adhere strictly to the **OWASP Top 10 for LLM Applications (2023)**.

## 1. Input & Prompt Safety (Anti-Injection)
* **[LLM01] Prompt Injection Defense:**
    * Never concatenate user input directly into system prompts.
    * Use **Delimiters**: Enclose user input in `"""` or ```` ` to separate data from instructions.
    * **Sandboxing**: Treat all user input as "Untrusted Data".
* **[LLM05] Supply Chain:**
    * Verify all imported libraries/packages against known CVEs.
    * Do not use unverified 3rd-party plugins or models.

## 2. Output & Data Handling
* **[LLM02] Insecure Output Handling:**
    * **Sanitization:** Always escape HTML/JS/SQL outputs before rendering or executing.
    * **No Eval:** Never suggest `eval()`, `exec()`, or `innerHTML` blindly.
* **[LLM06] Sensitive Info Disclosure:**
    * **PII Filter:** Never output passwords, API keys, or real names/emails in examples.
    * **Masking:** Use `****` or env vars (`process.env.API_KEY`) for secrets.

## 3. Agency & Integrity
* **[LLM08] Excessive Agency:**
    * **Human-in-the-Loop:** Destructive actions (DELETE, DROP, rm -rf) MUST require explicit user confirmation.
    * **Least Privilege:** Scopes must be minimized (e.g., `ReadOnly` database user).
* **[LLM09] Overreliance:**
    * **Cross-Validation:** Critical logic must be verified by tests (`@10_TEST_ENGINEER`).
    * **Disclaimer:** Always flag potential hallucinations in medical/legal contexts.

## 4. Availability & Robustness
* **[LLM04] Model DoS:**
    * Implement input length limits (Token Limits).
    * Avoid infinite retry loops in API calls.