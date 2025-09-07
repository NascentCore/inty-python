# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ......_models import BaseModel
from .subscription_plan import SubscriptionPlan

__all__ = ["PlanListResponse"]


class PlanListResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[List[SubscriptionPlan]] = None

    message: Optional[str] = None
