# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionVerifyParams"]


class SubscriptionVerifyParams(TypedDict, total=False):
    product_id: Required[str]
    """产品 ID"""

    purchase_token: Required[str]
    """购买令牌"""

    order_id: Optional[str]
    """订单 ID"""
