# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AuthCreateGuestParams"]


class AuthCreateGuestParams(TypedDict, total=False):
    age_group: Optional[str]

    device_id: Optional[str]

    system_language: Optional[str]
