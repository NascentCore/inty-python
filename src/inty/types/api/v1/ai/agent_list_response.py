# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .agent import Agent
from ....._models import BaseModel

__all__ = ["AgentListResponse"]


class AgentListResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[Agent]] = None

    message: Optional[str] = None
