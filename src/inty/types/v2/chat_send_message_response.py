# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["ChatSendMessageResponse", "Data", "DataChoice", "DataChoiceMessage", "DataUsage"]


class DataChoiceMessage(BaseModel):
    content: str

    role: str

    id: Optional[int] = None

    audio_url: Optional[str] = None

    meta_data: Optional[Dict[str, object]] = None

    timestamp: Optional[str] = None


class DataChoice(BaseModel):
    finish_reason: str

    index: int

    message: DataChoiceMessage
    """Chat message model for OpenAI-style responses"""


class DataUsage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int


class Data(BaseModel):
    id: str

    choices: List[DataChoice]

    created: int

    model: str

    usage: DataUsage
    """Token usage model for OpenAI-style responses"""


class ChatSendMessageResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """OpenAI-style chat completion response model"""

    message: Optional[str] = None
