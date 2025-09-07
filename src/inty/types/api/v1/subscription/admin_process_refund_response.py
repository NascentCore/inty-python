# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["AdminProcessRefundResponse", "Data"]


class Data(BaseModel):
    message: str
    """处理消息"""

    refund_amount: float
    """退款金额"""

    subscription_id: str
    """订阅 ID"""

    success: bool
    """是否成功"""

    refunded_at: Optional[datetime] = None
    """退款时间"""


class AdminProcessRefundResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """退款响应"""

    message: Optional[str] = None
