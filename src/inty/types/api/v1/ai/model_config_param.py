# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ModelConfigParam"]


class ModelConfigParam(TypedDict, total=False):
    api_key: Optional[str]

    base_url: Optional[str]

    frequency_penalty: Optional[float]
    """Frequency penalty"""

    max_tokens: Optional[int]
    """Maximum tokens in response"""

    model: Optional[str]

    presence_penalty: Optional[float]
    """Presence penalty"""

    temperature: Optional[float]
    """Temperature for response generation"""

    top_k: Optional[int]
    """Top-k sampling parameter"""

    top_p: Optional[float]
    """Top-p sampling parameter"""
