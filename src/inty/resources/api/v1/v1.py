# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast

import httpx

from .ai.ai import (
    AIResource,
    AsyncAIResource,
    AIResourceWithRawResponse,
    AsyncAIResourceWithRawResponse,
    AIResourceWithStreamingResponse,
    AsyncAIResourceWithStreamingResponse,
)
from .report import (
    ReportResource,
    AsyncReportResource,
    ReportResourceWithRawResponse,
    AsyncReportResourceWithRawResponse,
    ReportResourceWithStreamingResponse,
    AsyncReportResourceWithStreamingResponse,
)
from .version import (
    VersionResource,
    AsyncVersionResource,
    VersionResourceWithRawResponse,
    AsyncVersionResourceWithRawResponse,
    VersionResourceWithStreamingResponse,
    AsyncVersionResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .auth.auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .chats.chats import (
    ChatsResource,
    AsyncChatsResource,
    ChatsResourceWithRawResponse,
    AsyncChatsResourceWithRawResponse,
    ChatsResourceWithStreamingResponse,
    AsyncChatsResourceWithStreamingResponse,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.api import v1_upload_image_params, v1_list_notifications_params
from .text_to_speech import (
    TextToSpeechResource,
    AsyncTextToSpeechResource,
    TextToSpeechResourceWithRawResponse,
    AsyncTextToSpeechResourceWithRawResponse,
    TextToSpeechResourceWithStreamingResponse,
    AsyncTextToSpeechResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .subscription.subscription import (
    SubscriptionResource,
    AsyncSubscriptionResource,
    SubscriptionResourceWithRawResponse,
    AsyncSubscriptionResourceWithRawResponse,
    SubscriptionResourceWithStreamingResponse,
    AsyncSubscriptionResourceWithStreamingResponse,
)
from ....types.api.v1.api_response_dict import APIResponseDict
from ....types.api.v1_list_notifications_response import V1ListNotificationsResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def report(self) -> ReportResource:
        return ReportResource(self._client)

    @cached_property
    def ai(self) -> AIResource:
        return AIResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def subscription(self) -> SubscriptionResource:
        return SubscriptionResource(self._client)

    @cached_property
    def version(self) -> VersionResource:
        return VersionResource(self._client)

    @cached_property
    def chats(self) -> ChatsResource:
        return ChatsResource(self._client)

    @cached_property
    def text_to_speech(self) -> TextToSpeechResource:
        return TextToSpeechResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def list_notifications(
        self,
        *,
        is_read: Optional[bool] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListNotificationsResponse:
        """
        分页查询用户的消息列表；返回用户收到的通知。

        Args:
          is_read: 是否已读，不传则查询全部

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/notifications/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "is_read": is_read,
                        "page": page,
                        "page_size": page_size,
                    },
                    v1_list_notifications_params.V1ListNotificationsParams,
                ),
            ),
            cast_to=V1ListNotificationsResponse,
        )

    def upload_image(
        self,
        *,
        file: FileTypes,
        cropping_avatar: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseDict:
        """
        Upload image file with validation, compression, and GCS storage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "cropping_avatar": cropping_avatar,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/images",
            body=maybe_transform(body, v1_upload_image_params.V1UploadImageParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDict,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def report(self) -> AsyncReportResource:
        return AsyncReportResource(self._client)

    @cached_property
    def ai(self) -> AsyncAIResource:
        return AsyncAIResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        return AsyncSubscriptionResource(self._client)

    @cached_property
    def version(self) -> AsyncVersionResource:
        return AsyncVersionResource(self._client)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        return AsyncChatsResource(self._client)

    @cached_property
    def text_to_speech(self) -> AsyncTextToSpeechResource:
        return AsyncTextToSpeechResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def list_notifications(
        self,
        *,
        is_read: Optional[bool] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1ListNotificationsResponse:
        """
        分页查询用户的消息列表；返回用户收到的通知。

        Args:
          is_read: 是否已读，不传则查询全部

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/notifications/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "is_read": is_read,
                        "page": page,
                        "page_size": page_size,
                    },
                    v1_list_notifications_params.V1ListNotificationsParams,
                ),
            ),
            cast_to=V1ListNotificationsResponse,
        )

    async def upload_image(
        self,
        *,
        file: FileTypes,
        cropping_avatar: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseDict:
        """
        Upload image file with validation, compression, and GCS storage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "cropping_avatar": cropping_avatar,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/images",
            body=await async_maybe_transform(body, v1_upload_image_params.V1UploadImageParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDict,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.list_notifications = to_raw_response_wrapper(
            v1.list_notifications,
        )
        self.upload_image = to_raw_response_wrapper(
            v1.upload_image,
        )

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._v1.auth)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._v1.users)

    @cached_property
    def report(self) -> ReportResourceWithRawResponse:
        return ReportResourceWithRawResponse(self._v1.report)

    @cached_property
    def ai(self) -> AIResourceWithRawResponse:
        return AIResourceWithRawResponse(self._v1.ai)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._v1.settings)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithRawResponse:
        return SubscriptionResourceWithRawResponse(self._v1.subscription)

    @cached_property
    def version(self) -> VersionResourceWithRawResponse:
        return VersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def chats(self) -> ChatsResourceWithRawResponse:
        return ChatsResourceWithRawResponse(self._v1.chats)

    @cached_property
    def text_to_speech(self) -> TextToSpeechResourceWithRawResponse:
        return TextToSpeechResourceWithRawResponse(self._v1.text_to_speech)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.list_notifications = async_to_raw_response_wrapper(
            v1.list_notifications,
        )
        self.upload_image = async_to_raw_response_wrapper(
            v1.upload_image,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._v1.auth)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._v1.users)

    @cached_property
    def report(self) -> AsyncReportResourceWithRawResponse:
        return AsyncReportResourceWithRawResponse(self._v1.report)

    @cached_property
    def ai(self) -> AsyncAIResourceWithRawResponse:
        return AsyncAIResourceWithRawResponse(self._v1.ai)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._v1.settings)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithRawResponse:
        return AsyncSubscriptionResourceWithRawResponse(self._v1.subscription)

    @cached_property
    def version(self) -> AsyncVersionResourceWithRawResponse:
        return AsyncVersionResourceWithRawResponse(self._v1.version)

    @cached_property
    def chats(self) -> AsyncChatsResourceWithRawResponse:
        return AsyncChatsResourceWithRawResponse(self._v1.chats)

    @cached_property
    def text_to_speech(self) -> AsyncTextToSpeechResourceWithRawResponse:
        return AsyncTextToSpeechResourceWithRawResponse(self._v1.text_to_speech)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.list_notifications = to_streamed_response_wrapper(
            v1.list_notifications,
        )
        self.upload_image = to_streamed_response_wrapper(
            v1.upload_image,
        )

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._v1.auth)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._v1.users)

    @cached_property
    def report(self) -> ReportResourceWithStreamingResponse:
        return ReportResourceWithStreamingResponse(self._v1.report)

    @cached_property
    def ai(self) -> AIResourceWithStreamingResponse:
        return AIResourceWithStreamingResponse(self._v1.ai)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._v1.settings)

    @cached_property
    def subscription(self) -> SubscriptionResourceWithStreamingResponse:
        return SubscriptionResourceWithStreamingResponse(self._v1.subscription)

    @cached_property
    def version(self) -> VersionResourceWithStreamingResponse:
        return VersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def chats(self) -> ChatsResourceWithStreamingResponse:
        return ChatsResourceWithStreamingResponse(self._v1.chats)

    @cached_property
    def text_to_speech(self) -> TextToSpeechResourceWithStreamingResponse:
        return TextToSpeechResourceWithStreamingResponse(self._v1.text_to_speech)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.list_notifications = async_to_streamed_response_wrapper(
            v1.list_notifications,
        )
        self.upload_image = async_to_streamed_response_wrapper(
            v1.upload_image,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._v1.auth)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._v1.users)

    @cached_property
    def report(self) -> AsyncReportResourceWithStreamingResponse:
        return AsyncReportResourceWithStreamingResponse(self._v1.report)

    @cached_property
    def ai(self) -> AsyncAIResourceWithStreamingResponse:
        return AsyncAIResourceWithStreamingResponse(self._v1.ai)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._v1.settings)

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        return AsyncSubscriptionResourceWithStreamingResponse(self._v1.subscription)

    @cached_property
    def version(self) -> AsyncVersionResourceWithStreamingResponse:
        return AsyncVersionResourceWithStreamingResponse(self._v1.version)

    @cached_property
    def chats(self) -> AsyncChatsResourceWithStreamingResponse:
        return AsyncChatsResourceWithStreamingResponse(self._v1.chats)

    @cached_property
    def text_to_speech(self) -> AsyncTextToSpeechResourceWithStreamingResponse:
        return AsyncTextToSpeechResourceWithStreamingResponse(self._v1.text_to_speech)
