# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateCompletionParams", "Message"]


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    language: str

    model: str

    stream: bool


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
