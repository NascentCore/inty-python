# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .chats.chat_settings import ChatSettings

__all__ = ["Chat"]


class Chat(BaseModel):
    id: str

    agent_id: str

    created_at: datetime

    user_id: str

    agent_avatar: Optional[str] = None

    agent_background: Optional[str] = None

    agent_intro: Optional[str] = None

    agent_is_deleted: Optional[bool] = None

    agent_name: Optional[str] = None

    agent_opening: Optional[str] = None

    agent_opening_audio_url: Optional[str] = None

    last_message: Optional[str] = None

    last_message_time: Optional[datetime] = None

    settings: Optional[ChatSettings] = None
    """聊天设置"""

    updated_at: Optional[datetime] = None
