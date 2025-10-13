# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import chat_send_message_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.chat_send_message_response import ChatSendMessageResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def send_message(
        self,
        agent_id: str,
        *,
        messages: Iterable[chat_send_message_params.Message],
        language: str | Omit = omit,
        model: str | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSendMessageResponse:
        """
        可以处理包括图片在内的各种消息类型，媒体类型应该先上传，然后将 URL 作为索引发送
        到此 API

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/api/v2/chat/completions/{agent_id}",
            body=maybe_transform(
                {
                    "messages": messages,
                    "language": language,
                    "model": model,
                    "request_id": request_id,
                    "stream": stream,
                },
                chat_send_message_params.ChatSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSendMessageResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def send_message(
        self,
        agent_id: str,
        *,
        messages: Iterable[chat_send_message_params.Message],
        language: str | Omit = omit,
        model: str | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSendMessageResponse:
        """
        可以处理包括图片在内的各种消息类型，媒体类型应该先上传，然后将 URL 作为索引发送
        到此 API

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/api/v2/chat/completions/{agent_id}",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "language": language,
                    "model": model,
                    "request_id": request_id,
                    "stream": stream,
                },
                chat_send_message_params.ChatSendMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSendMessageResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.send_message = to_raw_response_wrapper(
            chat.send_message,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.send_message = async_to_raw_response_wrapper(
            chat.send_message,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.send_message = to_streamed_response_wrapper(
            chat.send_message,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.send_message = async_to_streamed_response_wrapper(
            chat.send_message,
        )
