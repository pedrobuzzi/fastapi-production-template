from fastapi import FastAPI
from app.api import routes as task_routes
from app.health import router as health_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Task API",
    version="1.0.0",
    description="A production-ready FastAPI sample for Cloud Run portfolio",
)

# Routes
app.include_router(task_routes.router)
app.include_router(health_router)

# Metrics
Instrumentator().instrument(app).expose(app)
