# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .user_subscription import UserSubscription

__all__ = ["SubscriptionVerifyResponse", "Data"]


class Data(BaseModel):
    is_verified: bool
    """是否有效"""

    message: str
    """验证消息"""

    error_code: Optional[str] = None
    """错误代码"""

    subscription: Optional[UserSubscription] = None
    """用户订阅响应模型"""


class SubscriptionVerifyResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """购买验证响应"""

    message: Optional[str] = None
