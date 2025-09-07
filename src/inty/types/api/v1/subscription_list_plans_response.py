# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .user_subscription import UserSubscription
from .subscription.admin.subscription_plan import SubscriptionPlan

__all__ = ["SubscriptionListPlansResponse", "Data"]


class Data(BaseModel):
    plans: List[SubscriptionPlan]
    """订阅计划列表"""

    current_subscription: Optional[UserSubscription] = None
    """用户订阅响应模型"""

    has_ever_subscribed: Optional[bool] = None
    """是否曾经有过订阅记录"""

    previous_plan_id: Optional[str] = None
    """最新的订阅计划 ID"""


class SubscriptionListPlansResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """订阅计划列表响应"""

    message: Optional[str] = None
