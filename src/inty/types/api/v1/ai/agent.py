# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ....._models import BaseModel
from ..users.user import User
from .model_config import ModelConfig
from .agent_visibility import AgentVisibility

__all__ = ["Agent", "AvatarSize", "BackgroundSize", "MetaData"]


class AvatarSize(BaseModel):
    height: int

    width: int


class BackgroundSize(BaseModel):
    height: int

    width: int


class MetaData(BaseModel):
    comment: Optional[str] = None
    """Agent 备注信息"""

    score: Optional[int] = None
    """Agent 评分"""


class Agent(BaseModel):
    id: str

    created_at: int

    gender: str

    name: str

    readable_id: str

    status: Literal["PENDING", "APPROVED", "REJECTED"]
    """AI 角色状态"""

    alternate_greetings: Optional[List[str]] = None

    avatar: Optional[str] = None

    avatar_size: Optional[AvatarSize] = None
    """Image size"""

    background: Optional[str] = None

    background_images: Optional[List[str]] = None

    background_size: Optional[BackgroundSize] = None
    """Image size"""

    category: Optional[str] = None

    character_book: Optional[Dict[str, object]] = None

    character_card_spec: Optional[str] = None

    character_version: Optional[str] = None

    connector_count: Optional[int] = None

    creator: Optional[User] = None
    """返回给客户端的用户信息"""

    creator_id: Optional[str] = None

    creator_notes: Optional[str] = None
    """创作者备注"""

    deleted_at: Optional[int] = None

    extensions: Optional[Dict[str, object]] = None

    follower_count: Optional[int] = None

    intro: Optional[str] = None

    is_followed: Optional[bool] = None

    llm_config: Optional[ModelConfig] = None
    """AI 模型配置"""

    main_prompt: Optional[str] = None
    """主提示词 - 作为第一个 system message，覆盖全局默认主提示词"""

    message_example: Optional[str] = None
    """对话示例"""

    meta_data: Optional[MetaData] = None
    """Agent 元数据模型"""

    mode_prompt: Optional[str] = None
    """模式提示词 - 放在角色卡提示词后面，覆盖全局默认模式提示词"""

    opening: Optional[str] = None

    opening_audio_url: Optional[str] = None

    personality: Optional[str] = None
    """角色性格特点 (推荐)"""

    photos: Optional[List[str]] = None

    post_history_instructions: Optional[str] = None

    prompt: Optional[str] = None
    """已废弃 - 请使用 personality 字段代替"""

    scenario: Optional[str] = None
    """背景设定 (推荐)"""

    settings: Optional[Dict[str, object]] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[int] = None

    user: Optional[str] = None

    visibility: Optional[AgentVisibility] = None
    """AI 角色可见性"""

    voice_id: Optional[str] = None
