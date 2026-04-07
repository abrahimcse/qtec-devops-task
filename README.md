# Qtec DevOps Engineer Practical Task

## Objective

Design and deploy a production-style system demonstrating:

* Containerization
* CI/CD automation
* Traffic management
* Observability

The system exposes:

* **GET API** → `/status`
* **POST API** → `/data`

---

## System Architecture

```
User → Nginx → Kubernetes Service (NodePort) → Pods (Flask App)
                         ↑
                      ArgoCD (GitOps)
                         ↑
                  GitHub Repository
                         ↑
                GitHub Actions (CI/CD)
```

---

## 1. Application (Python Flask API)

### API Endpoints

* **GET /status**

  * Returns application status and number of handled requests

* **POST /data**

  * Accepts JSON payload and stores it in-memory

### Example

```bash
curl -X POST http://localhost:5000/data \
-H "Content-Type: application/json" \
-d '{"name":"test"}'
```

---

## 🐳 2. Containerization (Docker)

* Base Image: `python:3.11-slim`
* Dependencies managed via `requirements.txt`
* Lightweight and production-ready setup

### Run Locally

```bash
docker build -t abrahimcse/qtec-devops-task:latest .
docker run -p 5000:5000 abrahimcse/qtec-devops-task:latest
```

---

## 3. Kubernetes Deployment

* Deployment with **3 replicas**
* Service type: **NodePort (30001)**

### Features:

* Rolling updates
* Self-healing pods
* Load balancing across replicas

---

## 4. Reverse Proxy (Nginx)

* Used to route external traffic
* Provides clean access without exposing NodePort

### Routes:

* `/` → index.html
* `/status` → API
* `/data` → API

---

## 5. CI/CD Pipeline

### Tools:

* GitHub Actions
* ArgoCD (GitOps)

### Flow:

1. Code pushed to GitHub
2. GitHub Actions:

   * Build Docker image
   * Tag with commit SHA
   * Push to Docker Hub
3. ArgoCD:

   * Monitors GitOps repository
   * Automatically deploys to Kubernetes

---

## GitOps Repository

Separate repository used for Kubernetes manifests:

👉 https://github.com/abrahimcse/qtec-devops-app-deploy

---

## Zero-Downtime Deployment

Achieved using:

* Kubernetes **Rolling Update strategy**
* Multiple replicas (3 pods)
* Readiness & liveness probes

➡️ New pods become ready before old ones are terminated
➡️ No downtime during deployment

---

## 6. Monitoring & Logging

### Tools Used:

* **Prometheus** → Metrics collection
* **Grafana** → Visualization dashboards

### Monitoring Features:

* Application metrics
* Pod & node health
* API health via `/status`

### Logs:

* Application logs (Flask)
* Kubernetes logs (`kubectl logs`)
* ArgoCD logs
* Nginx access & error logs

---

## Performance (~100 Requests/sec)

System handles ~100 req/sec using:

* Multiple pod replicas
* Kubernetes load balancing
* Nginx reverse proxy
* Lightweight Flask API

### Scaling Strategy:

* Use `threaded=True` for concurrency (Flask)
* Horizontal scaling via Kubernetes replicas
* Can integrate **Horizontal Pod Autoscaler (HPA)**

```bash
kubectl scale deployment qtec-devops-task --replicas=5
```

---

## Deployment Environment

* Deployed on **Virtual Machine (VM)**

### Reason:

* Office AWS account not used for personal tasks
* Cloud knowledge available but not used here

➡️ This system can be deployed to:

* AWS
* GCP
* DigitalOcean

---

## Infrastructure as Code (IaC)

* Terraform **not used in this task**
* But experienced in:

  * Infrastructure provisioning
  * Networking setup
  * Automation of cloud resources

---

## Security Practices

* No hardcoded credentials
* Environment-based configuration
* Minimal base image
* Container isolation

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

## Screenshots

### 🔹 Application Running

*(Add screenshot here)*

### 🔹 Kubernetes Pods

[*()*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/app-pod.png)

### 🔹 ArgoCD

[*(ArgoCD)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/ArgoCD.png)

### 🔹 API Response

* Status API:
  [*(Status)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/status-api.png)

* Data API:
  [*(Data)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/data-api.png)

### 🔹 Docker Hub

[*(Docker Registry)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/Dockerhub.png)

### 🔹 Nginx Reverse Proxy

*(Add screenshot here)*

### 🔹 Monitoring (Grafana)

[*(Grafana)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/grafana.png)

### 🔹 Application Logs

[*(Logs)*](https://github.com/abrahimcse/qtec-devops-task/blob/main/images/apps-log.png)

---

## Summary

This project demonstrates:

* End-to-end DevOps workflow
* GitOps-based deployment
* Kubernetes orchestration
* Reverse proxy setup
* Monitoring with Prometheus & Grafana

---

## Conclusion

The system is:

* Scalable
* Highly available
* Production-ready (basic level)

✔ Successfully fulfills all task requirements
✔ Demonstrates real-world DevOps practices

---
