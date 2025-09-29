# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AgentMetaDataParam"]


class AgentMetaDataParam(TypedDict, total=False):
    comment: Optional[str]
    """Agent 备注信息"""

    score: Optional[int]
    """Agent 评分"""
