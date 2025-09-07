# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .gender import Gender
from ....._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str

    auth_type: str

    created_at: datetime

    is_active: bool

    readable_id: str

    age_group: Optional[str] = None

    avatar: Optional[str] = None

    connector_count: Optional[int] = None

    description: Optional[str] = None

    email: Optional[str] = None

    followers_count: Optional[int] = None

    gender: Optional[Gender] = None
    """性别"""

    is_superuser: Optional[bool] = None

    nickname: Optional[str] = None

    phone: Optional[str] = None

    public_agents_count: Optional[int] = None

    system_language: Optional[str] = None

    total_public_agents_follows: Optional[int] = None

    updated_at: Optional[datetime] = None
