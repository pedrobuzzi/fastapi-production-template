# 🚀 FastAPI Production Starter

**Production-ready FastAPI starter to kickstart backend services with CI/CD, observability, and Cloud Run deploy.**

This project is designed to help you bootstrap new FastAPI services using a clean architecture, Prometheus metrics, health checks, GitHub Actions for CI/CD, and test automation — perfect for personal projects or production microservices.

---

## 🔧 Features

- ✅ **Modular architecture** with organized app structure
- 🔁 **CI/CD pipeline** via GitHub Actions
- 📈 **Prometheus metrics** available at `/metrics`
- ❤️ **Healthcheck endpoint** at `/healthz`
- 🧪 **Unit tests** with `pytest`
- 🧹 **Makefile** for common development commands
- 📄 **OpenAPI docs** at `/docs`


---

## ⚙️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Prometheus FastAPI Instrumentator](https://github.com/trallard/prometheus-fastapi-instrumentator)
- [GitHub Actions](https://docs.github.com/actions)
- [Google Cloud Run](https://cloud.google.com/run)
- [Pytest](https://docs.pytest.org/en/stable/)

---

## 🛠 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/fastapi-cloudrun-starter.git
cd fastapi-cloudrun-starter

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
make install

# Run the API
make run
```

---

## 🚀 Deployment (Google Cloud Run)

This project uses **GitHub Actions** to automatically build and deploy the API to **Google Cloud Run** on every push to the `main` branch.

### 🔐 Required GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions → New repository secret, and add the following:

| Name               | Description                                           |
|--------------------|-------------------------------------------------------|
| `GCP_PROJECT_ID`    | Your Google Cloud project ID                         |
| `GCP_REGION`        | Deployment region (e.g. `us-central1`)               |
| `CLOUD_RUN_SERVICE` | Name of the Cloud Run service (e.g. `task-api`)      |
| `GCP_SA_KEY`        | Contents of the service account key JSON             |

### ⚙️ Service Account Permissions

Make sure the service account has these roles:
- `Cloud Run Admin`
- `Storage Admin`
- `Artifact Registry Reader`
- `Service Account User`

### 📦 GitHub Actions Workflow

The workflow file is located at:
`.github/workflows/deploy.yml`
It builds the Docker image, pushes it to Google Artifact Registry, and deploys it to Google Cloud Run.
### 🌐 Accessing the API
After deployment, you can access the API at:
```
https://YOUR_CLOUD_RUN_SERVICE-REGION.a.run.app
```

---

## Future Enhancements

- [ ] Authentication
- [ ] Rate limiting
- [ ] Caching
- [ ] Database integration
- [ ] Logging
- [ ] Monitoring and alerting
- [ ] Environment variable management
- [ ] API versioning
- [ ] Dockerfile for local development
- [ ] Dockerfile for production
- [ ] Docker Compose for local development
- [ ] Long running tasks
- [ ] Scheduled tasks
- [ ] Deploy API to AWS Lambda