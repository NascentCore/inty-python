# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr
from .agent_visibility import AgentVisibility
from .model_config_param import ModelConfigParam
from .agent_meta_data_param import AgentMetaDataParam

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    gender: Required[str]

    name: Required[str]

    alternate_greetings: Optional[SequenceNotStr[str]]

    avatar: Optional[str]

    background: Optional[str]

    background_images: Optional[SequenceNotStr[str]]

    category: Optional[str]

    character_book: Optional[Dict[str, object]]

    character_card_spec: Optional[str]

    character_version: Optional[str]

    creator_notes: Optional[str]
    """创作者备注"""

    extensions: Optional[Dict[str, object]]

    intro: Optional[str]

    llm_config: Optional[ModelConfigParam]
    """AI 模型配置"""

    main_prompt: Optional[str]
    """主提示词 - 作为第一个 system message，覆盖全局默认主提示词"""

    message_example: Optional[str]
    """对话示例"""

    meta_data: Optional[AgentMetaDataParam]
    """Agent 元数据模型"""

    mode_prompt: Optional[str]
    """模式提示词 - 放在角色卡提示词后面，覆盖全局默认模式提示词"""

    opening: Optional[str]

    opening_audio_url: Optional[str]

    personality: Optional[str]
    """角色性格特点 (推荐)"""

    photos: Optional[SequenceNotStr[str]]

    post_history_instructions: Optional[str]

    prompt: Optional[str]
    """已废弃 - 请使用 personality 字段代替"""

    request_id: Optional[str]

    scenario: Optional[str]
    """背景设定 (推荐)"""

    settings: Optional[Dict[str, object]]

    tags: Optional[SequenceNotStr[str]]

    visibility: AgentVisibility
    """AI 角色可见性"""

    voice_id: Optional[str]
