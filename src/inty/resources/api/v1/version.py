# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.api.v1.version_check_response import VersionCheckResponse

__all__ = ["VersionResource", "AsyncVersionResource"]


class VersionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return VersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return VersionResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        app_version_code: int,
        app_version_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCheckResponse:
        """
        检查应用版本更新

        通过 HTTP 头传递版本信息：

        - appVersionCode: 应用版本代码（必填，整数）
        - appVersionName: 应用版本名称（可选，字符串）

        Args:
          app_version_code: 应用版本代码

          app_version_name: 应用版本名称（可选）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "appVersionCode": str(app_version_code),
                    "appVersionName": app_version_name,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/api/v1/version/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionCheckResponse,
        )


class AsyncVersionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncVersionResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        app_version_code: int,
        app_version_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCheckResponse:
        """
        检查应用版本更新

        通过 HTTP 头传递版本信息：

        - appVersionCode: 应用版本代码（必填，整数）
        - appVersionName: 应用版本名称（可选，字符串）

        Args:
          app_version_code: 应用版本代码

          app_version_name: 应用版本名称（可选）

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "appVersionCode": str(app_version_code),
                    "appVersionName": app_version_name,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/api/v1/version/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionCheckResponse,
        )


class VersionResourceWithRawResponse:
    def __init__(self, version: VersionResource) -> None:
        self._version = version

        self.check = to_raw_response_wrapper(
            version.check,
        )


class AsyncVersionResourceWithRawResponse:
    def __init__(self, version: AsyncVersionResource) -> None:
        self._version = version

        self.check = async_to_raw_response_wrapper(
            version.check,
        )


class VersionResourceWithStreamingResponse:
    def __init__(self, version: VersionResource) -> None:
        self._version = version

        self.check = to_streamed_response_wrapper(
            version.check,
        )


class AsyncVersionResourceWithStreamingResponse:
    def __init__(self, version: AsyncVersionResource) -> None:
        self._version = version

        self.check = async_to_streamed_response_wrapper(
            version.check,
        )
