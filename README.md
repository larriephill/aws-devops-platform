# AWS DevOps Platform

This project is a production-style DevOps / SRE platform built around a small FastAPI application running on Kubernetes. The goal was not just to deploy an app, but to solve the operational problems that appear after deployment: manual infrastructure changes, configuration drift, poor visibility, difficult rollback paths, and weak cost awareness.

The FastAPI service was designed to be operationally ready from the start. It exposes application, health, readiness, and metrics endpoints so the workload can be monitored, probed, and managed properly in Kubernetes. Docker packages the app into a consistent runtime artifact, while Kubernetes provides the runtime layer through Deployments, Services, probes, and resource controls.

Argo CD sits at the center of the deployment model. Instead of treating deployment as a one-time pipeline action, Argo CD continuously reconciles the cluster against the desired state stored in Git. This prevents manual drift from becoming permanent, makes rollback easier because the trusted version lives in Git, and improves auditability because changes can be traced through commits rather than relying on ad-hoc edits in the cluster. In practical terms, Git becomes the source of truth and the cluster is kept aligned with it over time.

The monitoring stack adds the evidence needed to operate the platform properly. Prometheus collects application metrics, Grafana visualises runtime behaviour, OpenTelemetry adds telemetry generation and trace collection, and CAST AI provides workload efficiency and cost visibility. Together, these tools make it easier to troubleshoot issues, validate behaviour after changes, and make resource decisions based on real data rather than assumptions.

The result is a system  that makes deployments safer, changes easier to manage, and the platform operations more reliable.

## Architecture
Git-driven platform architecture showing how Docker, Kubernetes, Kustomize, Argo CD, Prometheus, Grafana, OpenTelemetry, and CAST AI work together to deliver, observe, and optimise the application.
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/5ffa3986-55d2-470c-8075-52ba8397b8b7" />



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
   - Outcome: the platform is easier to monitor, troubleshoot, and optimize for cost and reliability

## Achieved outcomes

- The containerised FastAPI application was built and verified through its core endpoints: /, /healthz, /readyz, and /metrics

<img width="1883" height="630" alt="Screenshot 2026-04-03 100704" src="https://github.com/user-attachments/assets/8a2b432a-c711-4430-b094-1a67dce39135" />

- The application was deployed successfully to Kubernetes with environment-based configuration and defined resource controls
  
- The deployment structure was organised with Kustomize so the same workload could be managed cleanly across environments
  
<img width="1717" height="465" alt="image" src="https://github.com/user-attachments/assets/e6740a9d-99d3-4d42-8423-92c9ec1ee1f9" />

- GitOps was implemented with Argo CD, with automated sync and self-heal confirming that Git controlled the deployed state
  
<img width="1918" height="901" alt="Screenshot 2026-04-03 110716" src="https://github.com/user-attachments/assets/6a3be5a2-ba03-46f1-9e6a-f17bc36e53af" />

<img width="1450" height="454" alt="Screenshot 2026-04-03 100157" src="https://github.com/user-attachments/assets/55d9f070-a9a8-4820-9fd3-e3f54920f81c" />

- Application and platform behaviour were validated through Prometheus metrics and Grafana dashboards

<img width="1913" height="987" alt="Screenshot 2026-04-04 123518" src="https://github.com/user-attachments/assets/5e4c57d5-54d9-4a63-86e4-9d6b5a8a2e9c" />

- Cost visibility and workload efficiency were made visible through the CAST AI dashboard
  
<img width="1909" height="978" alt="Screenshot 2026-04-04 133730" src="https://github.com/user-attachments/assets/35500b20-59ae-44a4-895e-0de329929d75" />

## Repository areas

- `app/` - application code and instrumentation
- `k8s/base/` - shared Kubernetes runtime definition
- `k8s/overlays/dev/` - environment-specific deployment settings
- `argocd/apps/` - GitOps application definition


## Conclusion

This project brings together deployment control, runtime reliability, observability, and cost awareness into one platform workflow. FastAPI provides an application that is operationally ready for Kubernetes, while Argo CD changes the CD model from a one-time deployment into continuous reconciliation from Git. That means manual drift is easier to prevent, rollback is clearer, and the deployed state is easier to trust.

On top of that, the monitoring and optimisation stack provides the visibility needed to operate the platform well. Prometheus and Grafana make application behaviour measurable, OpenTelemetry strengthens the observability model, and CAST AI adds efficiency and cost insight. The result is a platform that is easier to troubleshoot, easier to audit, and easier to operate safely over time.
