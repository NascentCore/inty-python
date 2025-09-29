# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .subscription_plan_type import SubscriptionPlanType

__all__ = ["PlanCreateParams"]


class PlanCreateParams(TypedDict, total=False):
    google_play_product_id: Required[str]
    """Google Play 产品 ID"""

    name: Required[str]
    """计划名称"""

    plan_type: Required[SubscriptionPlanType]
    """计划类型"""

    price: Required[float]
    """价格"""

    agent_creation_limit: int
    """Agent 创建数量限制"""

    background_generation_limit_per_day: int
    """每日背景图生成次数限制，-1 为无限制"""

    chat_limit_per_day: int
    """每日聊天次数限制，-1 为无限制"""

    currency: str
    """货币"""

    description: Optional[str]
    """计划描述"""

    discount_rate: float
    """价格折扣率，范围 0-1，1 表示无折扣"""

    features: Optional[Dict[str, object]]
    """功能权益配置"""

    is_active: bool
    """是否激活"""

    request_id: Optional[str]

    sort_order: int
    """排序顺序"""
