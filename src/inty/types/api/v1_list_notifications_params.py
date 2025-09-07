# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["V1ListNotificationsParams"]


class V1ListNotificationsParams(TypedDict, total=False):
    is_read: Optional[bool]
    """是否已读，不传则查询全部"""

    page: int

    page_size: int
