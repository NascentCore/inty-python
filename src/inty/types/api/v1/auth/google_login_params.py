# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..users.gender import Gender

__all__ = ["GoogleLoginParams", "UserInfo"]


class GoogleLoginParams(TypedDict, total=False):
    id_token: Required[str]

    user_info: Optional[UserInfo]
    """用户信息"""


class UserInfo(TypedDict, total=False):
    age_group: Required[str]

    gender: Required[Gender]
    """性别"""

    system_language: Required[str]
