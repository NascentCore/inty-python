# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TextToSpeechListVoicesParams"]


class TextToSpeechListVoicesParams(TypedDict, total=False):
    category: Optional[str]
    """音色分类过滤 (如: premade, cloned)"""

    page_size: Optional[int]
    """每页返回结果数，默认 10，最大 100"""

    search: Optional[str]
    """搜索音色名称关键词"""

    voice_type: Optional[str]
    """音色类型过滤 (如: personal, community)"""
