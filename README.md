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

## Phase 2 - Kubernetes Deployment

This phase focused on deploying the application to Kubernetes using declarative manifests and environment overlays.

### Objective
Run the application in a local Kubernetes cluster with production-minded workload definitions, stable service discovery, health probes, and resource controls.

### What was built
- A local Kubernetes cluster using kind
- A dedicated namespace for the application
- A ConfigMap for runtime configuration
- A Deployment with two replicas
- Liveness and readiness probes
- CPU and memory requests/limits
- A ClusterIP Service for internal access
- A Kustomize base and dev overlay for declarative configuration management

### Why this matters
Kubernetes is not just about running containers. It is about declaring how workloads should run, recover, and be exposed. This phase introduced the core runtime objects that production teams rely on for scheduling, resiliency, and service discovery.

### Production-minded decisions
- Used a Deployment for controlled replica management
- Added health probes so Kubernetes can detect unhealthy or unready Pods
- Added resource requests and limits to support predictable scheduling and later cost analysis
- Used a Service instead of direct Pod access to provide a stable endpoint
- Structured manifests with Kustomize to prepare for GitOps in the next phase

### Validation
- Created a local kind cluster
- Loaded the locally built container image into the cluster
- Applied the manifests with Kustomize
- Verified the rollout completed successfully
- Confirmed the application responded through the Kubernetes Service via port-forwarding


## Phase 3 - GitOps with Argo CD

This phase introduced GitOps-based deployment management using Argo CD.

### Objective
Move from manual Kubernetes deployment to a Git-driven reconciliation model where the cluster continuously converges toward the desired state stored in Git.

### What was built
- Argo CD installed into the Kubernetes cluster
- Local Argo CD UI and CLI access via port-forwarding
- A declarative Argo CD `Application` manifest stored in the repository
- Automated sync configuration for Git-driven deployment updates
- Self-heal configuration to correct live drift from desired state

### Why this matters
GitOps improves deployment consistency by making Git the source of truth for cluster state. Instead of applying changes manually, engineers update version-controlled manifests and let Argo CD reconcile the cluster automatically.

### Production-minded decisions
- Defined the Argo CD application declaratively rather than relying only on UI clicks
- Enabled automated sync so changes in Git trigger reconciliation
- Enabled pruning to remove obsolete resources safely
- Enabled self-heal so Argo CD can restore live state when manual drift is introduced
- Kept the application source path aligned with the existing Kustomize overlay structure

### Validation
- Installed and accessed Argo CD locally
- Logged into the UI and CLI successfully
- Created an Argo CD application targeting the `k8s/overlays/dev` path
- Verified the application reached a `Synced` and `Healthy` state
- Demonstrated GitOps by changing the desired replica count in Git and observing the cluster reconcile
- Demonstrated self-healing by manually scaling the deployment and confirming Argo CD restored the Git-defined state


