# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ......_models import BaseModel
from .subscription_plan_type import SubscriptionPlanType

__all__ = ["SubscriptionPlan"]


class SubscriptionPlan(BaseModel):
    id: str

    created_at: datetime

    google_play_product_id: str
    """Google Play 产品 ID"""

    name: str
    """计划名称"""

    plan_type: SubscriptionPlanType
    """计划类型"""

    price: float
    """价格"""

    agent_creation_limit: Optional[int] = None
    """Agent 创建数量限制"""

    background_generation_limit_per_day: Optional[int] = None
    """每日背景图生成次数限制，-1 为无限制"""

    chat_limit_per_day: Optional[int] = None
    """每日聊天次数限制，-1 为无限制"""

    currency: Optional[str] = None
    """货币"""

    description: Optional[str] = None
    """计划描述"""

    discount_rate: Optional[float] = None
    """价格折扣率，范围 0-1，1 表示无折扣"""

    features: Optional[Dict[str, object]] = None
    """功能权益配置"""

    is_active: Optional[bool] = None
    """是否激活"""

    sort_order: Optional[int] = None
    """排序顺序"""

    updated_at: Optional[datetime] = None
