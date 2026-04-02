# Production-Ready AWS Platform

A production-style DevOps/SRE project demonstrating containerisation, Kubernetes deployment, GitOps delivery, observability, and cost optimisation.

## Technology Stack
- Python / FastAPI
- Docker
- Kubernetes
- GitHub Actions
- Argo CD
- Prometheus
- Grafana
- OpenTelemetry
- CAST AI

## Repository Structure
## Phase 1 - Foundation
## Screenshots

### Application endpoints
- `/` returns service metadata and runtime status
- `/healthz` provides a basic liveness-style health response
- `/readyz` provides a readiness-style response
- `/metrics` exposes Prometheus-compatible metrics



### Container build
The application was packaged into a Docker image to provide a consistent runtime across local development, CI, and later Kubernetes deployment.

## Phase 1 - Foundation

This phase focused on building the application and container foundation for the platform.

### Objective
Create a small production-minded service that can be packaged consistently, configured through environment variables, and extended later for Kubernetes, GitOps, observability, and cost optimisation.

### What was built
- A small HTTP application for platform testing
- Health and readiness endpoints
- A Prometheus-compatible metrics endpoint
- Environment-based configuration
- Structured application logging
- A Docker image for repeatable local execution

### Why this matters
Before introducing Kubernetes or GitOps, the workload itself must be operationally sound. This means predictable startup behaviour, externalised configuration, health visibility, and basic telemetry support.

### Application endpoints
- `/` returns service metadata and runtime status
- `/healthz` provides a liveness-style health response
- `/readyz` provides a readiness-style response
- `/metrics` exposes Prometheus-compatible metrics

### Production-minded decisions
- Kept the service intentionally small to focus on platform engineering concerns
- Designed the app to expose health and metrics from the start
- Structured the repo for future Kubernetes, GitOps, and observability phases
- Packaged the application as a container to ensure environment consistency

### Validation
- Built the container image locally
- Ran the service in Docker
- Verified root, health, readiness, and metrics endpoints
- Confirmed the project structure was ready for the next platform phases


