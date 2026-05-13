"""Health-check schemas."""

from app.schemas.base import ORMBaseModel


class HealthRead(ORMBaseModel):
    """Health-check response."""

    status: str
    app: str
    version: str
    environment: str
