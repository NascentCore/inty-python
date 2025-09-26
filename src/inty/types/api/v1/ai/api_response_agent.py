# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .agent import Agent
from ....._models import BaseModel

__all__ = ["APIResponseAgent"]


class APIResponseAgent(BaseModel):
    code: Optional[int] = None

    data: Optional[Agent] = None
    """AI 角色，在 sqlalchemy 模型基础上添加额外多表查询来的数据"""

    message: Optional[str] = None
