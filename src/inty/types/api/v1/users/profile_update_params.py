# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .gender import Gender

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    age_group: Optional[str]

    avatar: Optional[str]

    description: Optional[str]

    email: Optional[str]

    gender: Optional[Gender]
    """性别"""

    nickname: Optional[str]

    phone: Optional[str]

    system_language: Optional[str]
