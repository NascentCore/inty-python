# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentFollowingParams"]


class AgentFollowingParams(TypedDict, total=False):
    page: int
    """Page number, starting from 1"""

    page_size: int
    """Items per page, maximum 100"""
