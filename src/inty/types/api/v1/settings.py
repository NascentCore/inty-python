# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Settings"]


class Settings(BaseModel):
    id: str

    created_at: datetime

    user_id: str

    language: Optional[str] = None

    updated_at: Optional[datetime] = None

    voice_enabled: Optional[bool] = None
