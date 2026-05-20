from fastapi import APIRouter

from config import settings
from schemas.base import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        version=settings.app_version,
        app_name=settings.app_name,
    )
