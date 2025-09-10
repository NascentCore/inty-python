# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ....._models import BaseModel
from .chat_settings import ChatSettings
from ..api_response_dict import APIResponseDict

__all__ = ["AgentUpdateChatSettingsResponse", "APIResponseChatSettings"]


class APIResponseChatSettings(BaseModel):
    code: Optional[int] = None

    data: Optional[ChatSettings] = None
    """聊天设置"""

    message: Optional[str] = None


AgentUpdateChatSettingsResponse: TypeAlias = Union[APIResponseChatSettings, APIResponseDict]
