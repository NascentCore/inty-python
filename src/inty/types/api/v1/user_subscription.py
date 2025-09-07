# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .subscription.admin.subscription_plan import SubscriptionPlan

__all__ = ["UserSubscription"]


class UserSubscription(BaseModel):
    id: str

    created_at: datetime

    plan_id: str
    """订阅计划 ID"""

    user_id: str

    auto_renew: Optional[bool] = None
    """是否自动续费"""

    end_date: Optional[datetime] = None
    """结束时间"""

    extra_data: Optional[Dict[str, object]] = None
    """额外元数据"""

    google_play_order_id: Optional[str] = None
    """Google Play 订单 ID"""

    google_play_purchase_token: Optional[str] = None
    """Google Play 购买令牌"""

    google_play_subscription_id: Optional[str] = None
    """Google Play 订阅 ID"""

    plan: Optional[SubscriptionPlan] = None
    """订阅计划响应模型"""

    start_date: Optional[datetime] = None
    """开始时间"""

    status: Optional[Literal["ACTIVE", "EXPIRED", "CANCELLED", "PENDING", "REFUNDED", "GRACE_PERIOD", "PAUSED"]] = None
    """订阅状态"""

    trial_end_date: Optional[datetime] = None
    """试用结束时间"""

    updated_at: Optional[datetime] = None
