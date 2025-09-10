# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from ....._types import SequenceNotStr
from .agent_visibility import AgentVisibility
from .model_config_param import ModelConfigParam

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    alternate_greetings: Optional[SequenceNotStr[str]]

    avatar: Optional[str]

    background: Optional[str]

    background_images: Optional[SequenceNotStr[str]]

    category: Optional[str]

    character_book: Optional[Dict[str, object]]

    character_card_spec: Optional[str]

    character_version: Optional[str]

    creator_notes: Optional[str]

    extensions: Optional[Dict[str, object]]

    gender: Optional[str]

    intro: Optional[str]

    llm_config: Optional[ModelConfigParam]
    """AI 模型配置"""

    main_prompt: Optional[str]

    message_example: Optional[str]

    mode_prompt: Optional[str]

    name: Optional[str]

    opening: Optional[str]

    opening_audio_url: Optional[str]

    personality: Optional[str]

    photos: Optional[SequenceNotStr[str]]

    post_history_instructions: Optional[str]

    prompt: Optional[str]
    """已废弃 - 请使用 personality 字段代替"""

    scenario: Optional[str]

    settings: Optional[Dict[str, object]]

    tags: Optional[SequenceNotStr[str]]

    visibility: Optional[AgentVisibility]
    """AI 角色可见性"""

    voice_id: Optional[str]
