# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    language: Optional[str]

    request_id: Optional[str]

    voice_enabled: Optional[bool]
