# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["UserDeleteAccountResponse", "Data"]


class Data(BaseModel):
    message: str
    """删除结果消息"""

    success: bool
    """是否删除成功"""

    user_id: str
    """用户 ID"""

    anonymized_fields: Optional[List[str]] = None
    """已匿名化的字段列表"""

    deletion_log_id: Optional[str] = None
    """删除日志 ID"""


class UserDeleteAccountResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """账户删除响应"""

    message: Optional[str] = None
