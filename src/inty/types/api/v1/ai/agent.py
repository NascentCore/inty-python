# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ....._models import BaseModel
from ..users.user import User
from .model_config import ModelConfig
from .agent_visibility import AgentVisibility

__all__ = ["Agent"]


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

    background: Optional[str] = None

    background_images: Optional[List[str]] = None

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

    mode_prompt: Optional[str] = None
    """模式提示词 - 放在角色卡提示词后面，覆盖全局默认模式提示词"""

    opening: Optional[str] = None

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

    visibility: Optional[AgentVisibility] = None
    """AI 角色可见性"""

    voice_id: Optional[str] = None
