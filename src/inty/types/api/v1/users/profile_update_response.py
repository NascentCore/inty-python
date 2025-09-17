# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .user import User
from ....._models import BaseModel

__all__ = ["ProfileUpdateResponse"]


class ProfileUpdateResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[User] = None
    """返回给客户端的用户信息"""

    message: Optional[str] = None
