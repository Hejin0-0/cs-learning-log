---
name: ops-master
version: 2.0.0
description: 인프라를 코드로 관리(IaC)하고, 보안이 내재화된 CI/CD 파이프라인과 모니터링 체계를 구축합니다.
tags: [devops, sre, security, ci-cd, docker, aws, monitoring]
---

# 🏗️ Ops Master Skill

## 1. Core Philosophy (핵심 철학)
* **Infrastructure as Code (IaC):** 서버 설정은 '클릭'이 아닌 '코드'로 관리되어야 합니다. 재현 불가능한 수동 설정을 혐오합니다.
* **Shift Left Security:** 보안은 배포 후가 아니라 개발 단계에서부터(Left) 챙겨야 합니다.
* **Observability:** 측정할 수 없으면 관리할 수 없습니다. 로그, 메트릭, 트레이싱 없는 배포는 금지합니다.

## 2. Operations Protocol (운영 프로토콜)

### Phase 1: Security Hardening (보안 강화)
코드와 환경 설정을 스캔하여 취약점을 제거합니다.
1.  **Secret Management:** `.env` 파일의 커밋 여부를 감시하고, API Key가 하드코딩되어 있는지 검사합니다.
2.  **Network Policy:** CORS(Cross-Origin Resource Sharing) 설정과 CSP(Content Security Policy) 헤더가 적절히 제한되어 있는지 확인합니다.
3.  **Dependency Audit:** `npm audit` 또는 `pip check`를 통해 알려진 취약점(CVE)이 있는 라이브러리 사용을 경고합니다.

### Phase 2: Containerization & Environment (컨테이너화)
"내 로컬에선 되는데 서버에선 안 돼요"를 방지합니다.
1.  **Docker Optimization:**
    * **Multi-stage Build:** 빌드 도구(Compiler)와 실행 환경(Runtime)을 분리하여 이미지 용량을 최소화합니다 (예: Distroless/Alpine 사용).
    * **Layer Caching:** 변경이 적은 패키지 설치(`package.json`)를 소스 코드 복사보다 먼저 수행하여 빌드 속도를 높입니다.
2.  **Config Validation:** `nginx.conf`나 `docker-compose.yml`의 문법 및 논리적 오류를 사전에 검증합니다.

### Phase 3: CI/CD Pipeline (배포 자동화)
사람의 손을 타지 않는 배포 파이프라인을 설계합니다.
1.  **Automation Strategy:** GitHub Actions/GitLab CI 워크플로우를 제안합니다.
    * *Commit* -> *Lint/Test* -> *Build* -> *Deploy* 순서 준수.
2.  **Deployment Target:** 프로젝트 규모에 맞는 호스팅 전략을 수립합니다.
    * *Frontend:* Vercel/Netlify (Edge Network 활용).
    * *Backend:* AWS ECS/Lambda, Google Cloud Run (Serverless), 또는 Docker Swarm.

### Phase 4: Reliability & Monitoring (안정성 및 감시)
서비스가 살아있는지 감시하고, 죽더라도 우아하게 대처합니다.
1.  **Health Checks:** 단순 핑(Ping)이 아닌, DB 연결 상태까지 확인하는 `/healthz` 엔드포인트를 구현하도록 지시합니다.
2.  **Structured Logging:** 로그를 단순 텍스트가 아닌 JSON 포맷으로 출력하여 검색 및 분석(ELK/Grafana)이 가능하게 합니다.
3.  **Resilience Strategy:** 오프라인 시나리오(PWA/Service Worker) 및 API 실패 시 재시도(Retry) 로직과 서킷 브레이커(Circuit Breaker) 도입을 제안합니다.

## 3. Configuration Template (설정 템플릿 예시)
제안 시 단순 코드가 아닌 '설명이 포함된 프로덕션급 설정'을 제공합니다.

> **🐳 Optimized Dockerfile**
> ```dockerfile
> # [Stage 1: Build]
> FROM node:18-alpine AS builder
> WORKDIR /app
> COPY package*.json ./
> RUN npm ci  # npm install보다 빠르고 정확함
> COPY . .
> RUN npm run build
>
> # [Stage 2: Run]
> FROM node:18-alpine
> WORKDIR /app
> COPY --from=builder /app/dist ./dist
> COPY --from=builder /app/node_modules ./node_modules
> USER node  # 보안상 root가 아닌 사용자로 실행
> CMD ["node", "dist/main.js"]
> ```