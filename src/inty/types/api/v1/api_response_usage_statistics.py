# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["APIResponseUsageStatistics", "Data", "DataUsageHistory"]


class DataUsageHistory(BaseModel):
    id: str

    created_at: datetime

    usage_date: datetime
    """使用日期"""

    usage_type: str
    """使用类型"""

    user_id: str

    extra_data: Optional[Dict[str, object]] = None
    """额外元数据"""

    subscription_id: Optional[str] = None

    usage_count: Optional[int] = None
    """使用次数"""


class Data(BaseModel):
    agent_count: Optional[int] = None
    """创建的 Agent 数量"""

    agent_limit: Optional[int] = None
    """Agent 创建限制"""

    chat_24h_count: Optional[int] = None
    """24 小时内聊天次数（免费用户）"""

    chat_24h_limit: Optional[int] = None
    """24 小时内聊天次数限制（免费用户）"""

    today_chat_count: Optional[int] = None
    """今日聊天次数"""

    today_limit: Optional[int] = None
    """今日限制"""

    total_chat_count: Optional[int] = None
    """总聊天次数（免费用户）"""

    total_chat_limit: Optional[int] = None
    """总聊天次数限制（免费用户）"""

    usage_history: Optional[List[DataUsageHistory]] = None
    """使用历史"""


class APIResponseUsageStatistics(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """使用统计响应"""

    message: Optional[str] = None
