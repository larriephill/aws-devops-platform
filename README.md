# AWS DevOps Platform

This is an automated deployment platform that uses Kubernetes as the runtime layer, Argo CD for GitOps-based deployment control, Prometheus and Grafana for metrics and visibility, OpenTelemetry for telemetry generation, and CAST AI for workload efficiency and cost monitoring.

This platform does more than ship a container to a Kubernetes cluster, rather it is designed for Git to control application deployment,  application health is measurable, behaviour is observable, and infrastructure usage can be reviewed on Cast AI's dashboard where cost is visible. The main deliverable is a reliable delivery of FastAPI app from code to runtime.

The platform solves a common problem: applications are often easy to run once, but much harder to deploy consistently, monitor properly, recover safely, and operate efficiently over time. I addressed that by building a delivery platform that packages the app with Docker, deploys it to Kubernetes with health checks, service discovery, and environment-based configuration, then using Argo CD to continuously reconcile the cluster to the desired state stored in Git. Prometheus and Grafana provide runtime visibility, OpenTelemetry strengthens the observability model, and CAST AI adds efficiency and cost insight so operational decisions are based on evidence.

The result is a system  that makes deployments safer, changes easier to manage, and the platform operations more reliable.



## Platform Workflow
The platform consists of 5 connected layers that move the application from a packaged artifact to managed, observable and cost-aware runtime.
Docker creates a consistent container image, kubernetes runs and exposes it, Kustomize structures it for different environments, Argo CD keeps the cluster aligned with Git, and Prometheus, Grafana, and CAST AI provides visibility for monitoring behavior and efficiency



1. **Application and Container runtime**
   - Docker packages the FASTAPI app with health, readiness and metrics endpoints, into a consistent runtime artifact.
   - Outcome: the same workload can run locally, in CI, and in Kubernetes without drift.

2. **Kubernetes application layer**
   - Deployments, Services, ConfigMaps, probes, and resource settings define how the workload runs.
   - Outcome: the app can start predictably, recover from failure, and expose stable service access.

3. **Environment structure**
   - Kustomize base and overlays separate shared app configuration from environment-specific settings.
   - Outcome: the same application can be deployed to different environments in a controlled and repeatable way.

4. **GitOps control plane**
   - Argo CD watches the Git repository and reconciles the cluster to the desired state.
   - Outcome: deployments become version-controlled, repeatable, and resistant to manual drift.

5. **Observability and efficiency**
   - Prometheus collects metrics, Grafana visualises runtime behaviour, and CAST AI adds cost and efficency visibility for resource usage.
   - Outcome: the platform is easier to monitor, troubleshoot, and optimize for cost and reliability.


## Architecture
Git-driven platform architecture showing how Docker, Kubernetes, Kustomize, Argo CD, Prometheus, Grafana, OpenTelemetry, and CAST AI work together to deliver, observe, and optimise the application.

## Achieved outcomes

- The containerised FastAPI application was built and verified through its core endpoints: /, /healthz, /readyz, and /metrics
- The application was deployed successfully to Kubernetes with environment-based configuration and defined resource controls
- The deployment structure was organised with Kustomize so the same workload could be managed cleanly across environments
- GitOps was implemented with Argo CD, with automated sync and self-heal confirming that Git controlled the deployed state
- Application and platform behaviour were validated through Prometheus metrics and Grafana dashboards
- Cost visibility and workload efficiency were made visible through the CAST AI dashboard



## Repository areas

- `app/` - application code and instrumentation
- `k8s/base/` - shared Kubernetes runtime definition
- `k8s/overlays/dev/` - environment-specific deployment settings
- `argocd/apps/` - GitOps application definition

## Conclusion
This project brings delivery control, runtime reliability, observability, and cost awareness into one platform workflow. Instead of treating deployment, monitoring, and efficiency as separate tasks, it connects them into a system that is easier to operate, easier to trust, and easier to evolve.

