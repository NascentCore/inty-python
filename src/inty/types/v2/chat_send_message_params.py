# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatSendMessageParams", "Message"]


class ChatSendMessageParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    language: str

    model: str

    request_id: Optional[str]

    stream: bool


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
