# Qtec DevOps Task

## API Endpoints

- **GET /status** → Returns app status and number of handled POST requests
- **POST /data** → Accepts JSON payload and stores it in-memory

Example POST:

```bash
curl -X POST http://localhost:5000/data -H "Content-Type: application/json" -d '{"name":"test"}'
```

## Scaling Strategy for ~100 req/sec
- Use threaded=True in Flask to handle multiple requests concurrently.
- Deploy using Kubernetes with replicas >= 3 and Horizontal Pod Autoscaler.
- Use LoadBalancer/Ingress to distribute traffic.
- For production, replace in-memory store with a persistent DB to avoid data loss.

---

# 5️⃣ How to Run Locally

```bash
docker build -t abrahimcse/qtec-devops-task:latest .
docker run -p 5000:5000 abrahimcse/qtec-devops-task:latest
```
Test in browser or curl:

```bash
curl http://localhost:5000/status
curl -X POST http://localhost:5000/data -H "Content-Type: application/json" -d '{"key":"value"}'
```
## 📌 Next Steps for GitHub Actions + ArgoCD:

1. Push this repo to GitHub
2. GitHub Actions will build Docker image and push to DockerHub
3. K8s manifest repo will be updated with new image tag
4. ArgoCD will sync and deploy the app automatically
5. Set replicas=3 in K8s deployment to handle ~100 req/sec