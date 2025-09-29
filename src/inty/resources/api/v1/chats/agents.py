# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.chats import (
    agent_get_messages_params,
    agent_update_settings_params,
    agent_generate_message_voice_params,
)
from .....types.api.v1.chats.chat_settings import ChatSettings
from .....types.api.v1.chats.agent_update_settings_response import AgentUpdateSettingsResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def generate_message_voice(
        self,
        message_id: str,
        *,
        agent_id: str,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generate voice for a message

        Args:
          language: 语言代码

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            f"/api/v1/chats/agents/{agent_id}/messages/{message_id}/voice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"language": language}, agent_generate_message_voice_params.AgentGenerateMessageVoiceParams
                ),
            ),
            cast_to=object,
        )

    def get_messages(
        self,
        agent_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get only chat message records by Agent ID (lighter interface)

        Args:
          limit: Number of messages per page

          offset: Offset

          order: Sort order: asc=old messages first, desc=new messages first

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/api/v1/chats/agents/{agent_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                    },
                    agent_get_messages_params.AgentGetMessagesParams,
                ),
            ),
            cast_to=object,
        )

    def get_settings(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSettings:
        """
        [Deprecated, use /chats/{chat_id}/settings instead] Get chat settings by Agent
        ID, bause we only support 1 chat per agent, so we do not use chat_id to get
        settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/api/v1/chats/agents/{agent_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSettings,
        )

    def update_settings(
        self,
        agent_id: str,
        *,
        language: Optional[str] | Omit = omit,
        premium_mode: Optional[bool] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        style_prompt: Optional[str] | Omit = omit,
        voice_enabled: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateSettingsResponse:
        """
        We do not use chat_id to get settings, because we only support 1 chat per
        agent.TODO: We should switch to /chats/{chat_id}/settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return cast(
            AgentUpdateSettingsResponse,
            self._put(
                f"/api/v1/chats/agents/{agent_id}/settings",
                body=maybe_transform(
                    {
                        "language": language,
                        "premium_mode": premium_mode,
                        "request_id": request_id,
                        "style_prompt": style_prompt,
                        "voice_enabled": voice_enabled,
                    },
                    agent_update_settings_params.AgentUpdateSettingsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AgentUpdateSettingsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def generate_message_voice(
        self,
        message_id: str,
        *,
        agent_id: str,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Generate voice for a message

        Args:
          language: 语言代码

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            f"/api/v1/chats/agents/{agent_id}/messages/{message_id}/voice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, agent_generate_message_voice_params.AgentGenerateMessageVoiceParams
                ),
            ),
            cast_to=object,
        )

    async def get_messages(
        self,
        agent_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Get only chat message records by Agent ID (lighter interface)

        Args:
          limit: Number of messages per page

          offset: Offset

          order: Sort order: asc=old messages first, desc=new messages first

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/api/v1/chats/agents/{agent_id}/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                    },
                    agent_get_messages_params.AgentGetMessagesParams,
                ),
            ),
            cast_to=object,
        )

    async def get_settings(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatSettings:
        """
        [Deprecated, use /chats/{chat_id}/settings instead] Get chat settings by Agent
        ID, bause we only support 1 chat per agent, so we do not use chat_id to get
        settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/api/v1/chats/agents/{agent_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatSettings,
        )

    async def update_settings(
        self,
        agent_id: str,
        *,
        language: Optional[str] | Omit = omit,
        premium_mode: Optional[bool] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        style_prompt: Optional[str] | Omit = omit,
        voice_enabled: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdateSettingsResponse:
        """
        We do not use chat_id to get settings, because we only support 1 chat per
        agent.TODO: We should switch to /chats/{chat_id}/settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return cast(
            AgentUpdateSettingsResponse,
            await self._put(
                f"/api/v1/chats/agents/{agent_id}/settings",
                body=await async_maybe_transform(
                    {
                        "language": language,
                        "premium_mode": premium_mode,
                        "request_id": request_id,
                        "style_prompt": style_prompt,
                        "voice_enabled": voice_enabled,
                    },
                    agent_update_settings_params.AgentUpdateSettingsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AgentUpdateSettingsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.generate_message_voice = to_raw_response_wrapper(
            agents.generate_message_voice,
        )
        self.get_messages = to_raw_response_wrapper(
            agents.get_messages,
        )
        self.get_settings = to_raw_response_wrapper(
            agents.get_settings,
        )
        self.update_settings = to_raw_response_wrapper(
            agents.update_settings,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.generate_message_voice = async_to_raw_response_wrapper(
            agents.generate_message_voice,
        )
        self.get_messages = async_to_raw_response_wrapper(
            agents.get_messages,
        )
        self.get_settings = async_to_raw_response_wrapper(
            agents.get_settings,
        )
        self.update_settings = async_to_raw_response_wrapper(
            agents.update_settings,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.generate_message_voice = to_streamed_response_wrapper(
            agents.generate_message_voice,
        )
        self.get_messages = to_streamed_response_wrapper(
            agents.get_messages,
        )
        self.get_settings = to_streamed_response_wrapper(
            agents.get_settings,
        )
        self.update_settings = to_streamed_response_wrapper(
            agents.update_settings,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.generate_message_voice = async_to_streamed_response_wrapper(
            agents.generate_message_voice,
        )
        self.get_messages = async_to_streamed_response_wrapper(
            agents.get_messages,
        )
        self.get_settings = async_to_streamed_response_wrapper(
            agents.get_settings,
        )
        self.update_settings = async_to_streamed_response_wrapper(
            agents.update_settings,
        )
