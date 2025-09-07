# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["VersionCheckResponse", "Data"]


class Data(BaseModel):
    current_version: str
    """当前客户端版本"""

    download_url: str
    """下载链接"""

    force_update: bool
    """是否强制更新"""

    latest_version: str
    """最新可用版本"""

    message: str
    """状态消息"""

    minimum_version: str
    """最低支持版本"""

    update_required: bool
    """是否需要更新"""

    changelog: Optional[str] = None
    """更新日志"""

    error: Optional[str] = None
    """错误信息"""

    latest_version_code: Optional[int] = None
    """最新版本代码"""


class VersionCheckResponse(BaseModel):
    code: Optional[int] = None

    data: Optional[Data] = None
    """版本检查响应模型"""

    message: Optional[str] = None
