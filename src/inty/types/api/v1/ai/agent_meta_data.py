# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["AgentMetaData"]


class AgentMetaData(BaseModel):
    comment: Optional[str] = None
    """Agent 备注信息"""

    score: Optional[int] = None
    """Agent 评分"""
