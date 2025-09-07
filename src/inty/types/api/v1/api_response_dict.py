# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["APIResponseDict"]


class APIResponseDict(BaseModel):
    code: Optional[int] = None

    data: Optional[Dict[str, object]] = None

    message: Optional[str] = None
