# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["ModelConfig"]


class ModelConfig(BaseModel):
    api_key: Optional[str] = None

    base_url: Optional[str] = None

    frequency_penalty: Optional[float] = None
    """Frequency penalty"""

    max_tokens: Optional[int] = None
    """Maximum tokens in response"""

    model: Optional[str] = None

    presence_penalty: Optional[float] = None
    """Presence penalty"""

    temperature: Optional[float] = None
    """Temperature for response generation"""

    top_k: Optional[int] = None
    """Top-k sampling parameter"""

    top_p: Optional[float] = None
    """Top-p sampling parameter"""
