# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AuthCreateGuestResponse", "Data"]


class Data(BaseModel):
    token: str

    guest_id: str

    is_new_guest: bool


class AuthCreateGuestResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """游客响应"""

    message: Optional[str] = None
