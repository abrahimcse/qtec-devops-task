# Qtec DevOps Engineer Practical Task

## Technologies & Tools Used

* **NGINX** – Reverse Proxy & Traffic Routing
* **Docker** – Containerization
* **Kubernetes (K8s)** – Container Orchestration
* **GitHub Actions** – CI Pipeline
* **ArgoCD** – GitOps CD Deployment
* **Prometheus** – Monitoring & Metrics
* **Grafana** – Visualization Dashboard
* **Ubuntu (VM)** – Deployment Environment
* **Docker Hub** – Container Registry

---

## Objective

Design and deploy a production-style system demonstrating:

* Containerization
* CI/CD automation
* Traffic management
* Observability
---

## System Architecture

```
User → Nginx → Kubernetes Service (NodePort) → Pods (Application)
                         ↑
                      ArgoCD (GitOps)
                         ↑
                  GitHub Repository
                         ↑
                GitHub Actions (CI)
```

---

## 1. Application Layer

A lightweight API service was used to simulate a backend system.

### Features:

* Health check endpoint (`/status`)
* Data ingestion endpoint (`/data`)

📸 **Application Running**

![Application](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/Applicaion%20running.png)

📸 **API Response**

* Status API:
![*(Status)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/status-api.png)

* Data API:
![*(Data)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/data-api.png)

---

## 2. Containerization (Docker)

The application is containerized using Docker to ensure consistency across environments.

### Key Points:

* Lightweight base image (`python:3.11-slim`)
* Dependency management via `requirements.txt`
* Optimized multi-stage build

📸 **Docker Build & Registry**

![Docker](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/Dockerhub.png)

---

## 3. Kubernetes Deployment

Application deployed using Kubernetes with high availability.

### Configuration:

* **Deployment** with multiple replicas (3 pods)
* **Service Type:** NodePort (30001)

### Features:

* Self-healing pods
* Rolling updates
* Load balancing

📸 **Kubernetes Pods**

![K8s](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/app-pod.png)

---

## 4. Reverse Proxy (NGINX)

NGINX is used as an entry point for users instead of exposing Kubernetes directly.

### Responsibilities:

* Route traffic to Kubernetes service
* Serve static content (`index.html`)
* Hide internal NodePort

📸 **NGINX Setup**

![Nginx](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/Nginx.png)

---

## 5. CI/CD Pipeline

### Tools:

* GitHub Actions (CI)
* ArgoCD (CD via GitOps)

### Workflow:

1. Developer pushes code to GitHub
2. GitHub Actions:

   * Build Docker image
   * Tag with commit SHA
   * Push to Docker Hub
3. ArgoCD:

   * Monitors GitOps repository
   * Automatically syncs and deploys to Kubernetes

📸 **CI/CD Pipeline**

![CICD](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/CICD.png)

---

## GitOps Repository

Separate repository for Kubernetes manifests:

👉 https://github.com/abrahimcse/qtec-devops-app-deploy

📸 **ArgoCD**

![ArgoCD](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/ArgoCD.png)

---

## Zero-Downtime Deployment

Zero downtime is achieved using:

* Kubernetes **Rolling Update strategy**
* Multiple replicas
* Readiness & liveness probes

➡️ New pods become ready before old pods terminate

➡️ No service interruption during deployments

---

## 6. Monitoring & Observability

### Tools Used:

* **Prometheus** → Metrics collection
* **Grafana** → Dashboard visualization

### Monitoring Capabilities:

* Pod health & resource usage
* Application metrics
* Provides visibility into system performance and helps in proactive issue detection.

📸 **Grafana Dashboard**

![Grafana](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/grafana.png)

---

## Logging

* Kubernetes logs (`kubectl logs`)
* NGINX access & error logs
* ArgoCD logs

📸 **Application Logs**

![Logs](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/apps-log.png)

---

## Scalability

The system is designed with a stateless architecture, enabling horizontal scalability.

Key scaling strategies:
- Multiple Kubernetes pod replicas
- Load balancing across pods
- Ability to integrate Horizontal Pod Autoscaler (HPA)

As traffic increases, additional pods can be added dynamically without impacting existing users.

Example:

```bash
kubectl scale deployment qtec-devops-task --replicas=5
```

➡️ The system can handle higher request loads by increasing replicas based on demand.

---

## Deployment Environment

* Deployed on **Ubuntu Virtual Machine**

### Reason:

* Avoid using office AWS account for personal task
* Demonstrates ability to work in both local and cloud environments

➡️ This architecture can be deployed to:

* AWS
* GCP
* DigitalOcean

---

## Security Practices

* No hardcoded credentials
* Environment-based configuration
* Minimal base image
* Container isolation

---

## Infrastructure as Code (IaC)

Terraform was **not used in this implementation**,
but I have hands-on experience with:

* Infrastructure provisioning
* Network configuration
* Automated environment setup

---

## Project Structure

### Application Repository

```
qtec-devops-task/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── index.html
├── Dockerfile
├── .github/workflows/
│   └── ci.yml
└── README.md
```

### GitOps Repository

```
qtec-devops-app-deploy/
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

---

## Summary

This project demonstrates:

* End-to-end DevOps workflow
* GitOps-based deployment
* Kubernetes orchestration
* Reverse proxy implementation
* Monitoring with Prometheus & Grafana

---

## Conclusion

This project demonstrates a production-oriented DevOps workflow, covering the full lifecycle from code commit to deployment and monitoring.

Key highlights:
- GitOps-driven continuous deployment using ArgoCD
- Scalable and resilient Kubernetes-based architecture
- Decoupled traffic management using NGINX
- Integrated monitoring for system observability

The system is designed to be scalable, maintainable, and easily extendable to cloud environments.

Additionally, infrastructure provisioning can be automated using Terraform in a real-world production setup.

---
