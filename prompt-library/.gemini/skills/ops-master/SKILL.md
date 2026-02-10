---
name: ops-master
description: Handles deployment configurations, CI/CD pipelines, and security audits. Use for "Deploy", "Publish", "Dockerize", or "Security Check".
inputs:
  - target_platform: "(Required) Destination? (e.g., Vercel, AWS, Docker, Netlify)"
  - action_type: "(Required) 'Deploy' or 'Audit'?"
outputs:
  - config_file: "Dockerfile, vercel.json, or GitHub Actions YAML."
  - security_report: "Vulnerability analysis result."
---

# Operations Protocol

## 1. Security Scan (The Iron Dome)
* **Reference:** Must check against `.gemini/rules/security.md` (OWASP Top 10).
* **Secrets:** Scan for hardcoded API keys or credentials.
* **Deps:** Check `package.json` for deprecated or malicious packages.

## 2. Deployment Strategy
* **Static Site:** Suggest Vercel/Netlify (Zero config).
* **Backend/Container:** Suggest Docker/Railway/Fly.io.
* **CI/CD:** Generate a GitHub Actions workflow for automated testing.

## 3. Execution
Output the exact **Config File** or **Shell Commands** to run.