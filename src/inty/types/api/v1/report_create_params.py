# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ReportCreateParams"]


class ReportCreateParams(TypedDict, total=False):
    reason_ids: Required[Iterable[int]]

    target_id: Required[str]

    target_type: Required[Literal["USER", "AGENT"]]

    description: Optional[str]

    image_urls: Optional[SequenceNotStr[str]]
