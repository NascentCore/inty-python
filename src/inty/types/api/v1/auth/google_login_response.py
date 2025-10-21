# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel
from ..users.gender import Gender

__all__ = ["GoogleLoginResponse", "Data", "DataUser"]


class DataUser(BaseModel):
    id: str

    auth_type: Literal["PHONE", "GOOGLE", "GUEST"]
    """认证类型"""

    avatar: str

    email: str

    is_new_user: bool

    nickname: str

    age_group: Optional[str] = None

    description: Optional[str] = None

    gender: Optional[Gender] = None
    """性别"""

    phone: Optional[str] = None

    system_language: Optional[str] = None


class Data(BaseModel):
    token: str

    user: DataUser
    """登录用户响应"""


class GoogleLoginResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """登录响应"""

    message: Optional[str] = None
