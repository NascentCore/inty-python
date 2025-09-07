# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AgentRecommendParams"]


class AgentRecommendParams(TypedDict, total=False):
    page: int
    """Page number, starting from 1"""

    page_size: int
    """Items per page, maximum 100"""

    sort: Literal["created_asc", "created_desc", "random"]
    """Sort order: created_asc, created_desc, random"""
