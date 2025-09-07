# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ......_models import BaseModel
from .subscription_plan import SubscriptionPlan

__all__ = ["PlanCreateResponse"]


class PlanCreateResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[SubscriptionPlan] = None
    """订阅计划响应模型"""

    message: Optional[str] = None
