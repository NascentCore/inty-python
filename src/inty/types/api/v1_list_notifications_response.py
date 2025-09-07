# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["V1ListNotificationsResponse", "Data", "DataItem"]


class DataItem(BaseModel):
    id: str

    content: Optional[str] = None

    created_at: datetime

    image_urls: Optional[List[str]] = None

    is_read: bool

    link_urls: Optional[List[str]] = None

    read_at: Optional[datetime] = None

    template_id: Optional[int] = None

    title: Optional[str] = None

    type: int


class Data(BaseModel):
    items: Optional[List[DataItem]] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class V1ListNotificationsResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """Specific model for a paginated list of notification items."""

    message: Optional[str] = None
