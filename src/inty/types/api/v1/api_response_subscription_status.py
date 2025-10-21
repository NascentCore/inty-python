# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel
from .user_subscription import UserSubscription
from .subscription.admin.subscription_plan import SubscriptionPlan

__all__ = ["APIResponseSubscriptionStatus", "Data", "DataFeatureList"]


class DataFeatureList(BaseModel):
    description: str
    """权益描述"""

    icon: str
    """权益图标"""

    key: str
    """权益 key"""

    name: str
    """权益名称"""

    order: int
    """排序顺序"""

    type: str
    """权益类型：real/fake"""

    enabled: Optional[bool] = None
    """是否启用"""


class Data(BaseModel):
    is_subscribed: bool
    """是否订阅"""

    subscription_status: str
    """订阅详细状态：subscribed/subscribed_expiring/unsubscribed"""

    agent_creation_24h_limit: Optional[int] = None
    """24 小时内 Agent 创建数量限制"""

    agent_creation_limit: Optional[int] = None
    """Agent 创建数量限制（已废弃，使用 agent_creation_24h_limit）"""

    background_generation_limit_per_day: Optional[int] = None
    """每日背景图生成次数限制（已废弃，使用 image_gen_24h_limit）"""

    chat_24h_limit: Optional[int] = None
    """24 小时内聊天次数限制（免费用户）"""

    chat_limit_per_day: Optional[int] = None
    """每日聊天次数限制"""

    feature_list: Optional[List[DataFeatureList]] = None
    """权益功能列表"""

    features: Optional[Dict[str, object]] = None
    """功能权益"""

    guest_chat_24h_limit: Optional[int] = None
    """24 小时内聊天次数限制（游客用户）"""

    guest_voice_24h_limit: Optional[int] = None
    """24 小时内语音生成次数限制（游客用户）"""

    has_ever_subscribed: Optional[bool] = None
    """是否曾经有过订阅记录"""

    image_gen_24h_limit: Optional[int] = None
    """24 小时内图片生成次数限制"""

    plan: Optional[SubscriptionPlan] = None
    """订阅计划响应模型"""

    remaining_days: Optional[int] = None
    """剩余天数"""

    subscription: Optional[UserSubscription] = None
    """用户订阅响应模型"""

    total_chat_limit: Optional[int] = None
    """总聊天次数限制（免费用户）"""

    voice_24h_limit: Optional[int] = None
    """24 小时内语音生成次数限制"""

    will_auto_renew: Optional[bool] = None
    """是否会自动续费"""


class APIResponseSubscriptionStatus(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """订阅状态响应"""

    message: Optional[str] = None
