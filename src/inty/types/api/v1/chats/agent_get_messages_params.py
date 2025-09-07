# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentGetMessagesParams"]


class AgentGetMessagesParams(TypedDict, total=False):
    limit: int
    """Number of messages per page"""

    offset: int
    """Offset"""

    order: str
    """Sort order: asc=old messages first, desc=new messages first"""
