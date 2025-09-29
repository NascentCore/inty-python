# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AdminProcessRefundParams"]


class AdminProcessRefundParams(TypedDict, total=False):
    subscription_id: Required[str]
    """订阅 ID"""

    reason: str
    """退款原因"""

    refund_amount: Optional[float]
    """退款金额，不填写则退全款"""

    request_id: Optional[str]
