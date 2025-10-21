# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .agent import Agent
from ....._models import BaseModel

__all__ = ["AgentCreateResponse", "Data"]

Data: TypeAlias = Union[Agent, Dict[str, object], None]


class AgentCreateResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """AI 角色，在 sqlalchemy 模型基础上添加额外多表查询来的数据"""

    message: Optional[str] = None
