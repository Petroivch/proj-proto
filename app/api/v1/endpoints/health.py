"""Health endpoint."""

from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthRead

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthRead)
async def health_check() -> HealthRead:
    """Return application health information."""

    return HealthRead(
        status="ok",
        app=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )
