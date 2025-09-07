# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .agent import Agent
from ....._models import BaseModel

__all__ = ["APIResponsePaginationDataAgent", "Data"]


class Data(BaseModel):
    list: Optional[List[Agent]] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    total: Optional[int] = None

    total_pages: Optional[int] = None


class APIResponsePaginationDataAgent(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None

    message: Optional[str] = None
