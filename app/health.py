from fastapi import APIRouter


router = APIRouter()


@router.get("/healthz", tags=["infra"])
def health_check():
    return {"status": "ok"}
