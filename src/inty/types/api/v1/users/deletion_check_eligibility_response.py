# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["DeletionCheckEligibilityResponse", "Data"]


class Data(BaseModel):
    can_delete: bool
    """是否可以删除"""

    active_subscription: Optional[bool] = None
    """是否有活跃订阅"""

    error_message: Optional[str] = None
    """错误信息"""


class DeletionCheckEligibilityResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """删除检查响应"""

    message: Optional[str] = None
