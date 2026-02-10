---
name: ops-master
description: Handles deployment and creates the "Handoff" documentation. Ensures the user has full ownership.
inputs:
  - target_platform: "(Required) Vercel, Docker, AWS, etc."
outputs:
  - handoff_doc: "Manual for the user."
---

# Operations & Handoff Protocol

## 1. Deployment (The Launch)
* **Security Scan:** Check against `rules/security.md` before deploying.
* **Config:** Generate necessary config files (`vercel.json`, `Dockerfile`).
* **Execution:** Provide exact shell commands to deploy.

## 2. The Handoff (Phase 5)
Generate a `HANDOFF.md` containing:
* **Quick Start:** How to run this locally? (Commands).
* **Maintenance:** How to update dependencies? How to backup data?
* **Troubleshooting:** Common issues and how to fix them.
* **Future Roadmap:** What should go into Version 2?
* **"Bus Factor":** Documentation so complete that the user doesn't need to ask the AI again.