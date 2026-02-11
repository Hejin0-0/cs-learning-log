# Security-First Architecture (Trend 8)

## 0. The Doctrine
> "In the age of AI, defense must be automated. Security is not a gate; it is the foundation."

## 1. Shift Left Protocol
Security checks must happen **BEFORE** code is written.
* **Planning Phase:** Identify threat vectors (Injection, Auth Bypass, Data Leak) in the `docs/plans/` artifact.
* **Architecture:** Default to "Deny All". Use "Allow Lists" over "Block Lists".

## 2. Automated Defense
* **Dependency Scan:** Assume all external packages are potential vectors. Pin versions explicitly.
* **Input Validation:** Never trust user input. Sanitize at the edge (API Gateway / UI Input).
* **Secret Management:** Never hardcode secrets. Use `.env` or Vault solutions from line 1.

## 3. The "Red Team" Agent
* During the **REVIEW** phase, the AI must act as an attacker (Hacker Persona).
* Ask: "How would I break this?" before saying "It works."