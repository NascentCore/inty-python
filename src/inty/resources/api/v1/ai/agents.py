# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
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
from .....types.api.v1.ai import (
    AgentVisibility,
    agent_list_params,
    agent_create_params,
    agent_search_params,
    agent_update_params,
    agent_following_params,
    agent_recommend_params,
)
from .....types.api.v1.ai.agent import Agent
from .....types.api.v1.api_response_dict import APIResponseDict
from .....types.api.v1.ai.agent_visibility import AgentVisibility
from .....types.api.v1.ai.api_response_agent import APIResponseAgent
from .....types.api.v1.ai.model_config_param import ModelConfigParam
from .....types.api.v1.ai.agent_list_response import AgentListResponse
from .....types.api.v1.ai.api_response_pagination_data_agent import APIResponsePaginationDataAgent

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        gender: str,
        name: str,
        alternate_greetings: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        background: Optional[str] | NotGiven = NOT_GIVEN,
        background_images: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        category: Optional[str] | NotGiven = NOT_GIVEN,
        character_book: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        character_card_spec: Optional[str] | NotGiven = NOT_GIVEN,
        character_version: Optional[str] | NotGiven = NOT_GIVEN,
        creator_notes: Optional[str] | NotGiven = NOT_GIVEN,
        extensions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        intro: Optional[str] | NotGiven = NOT_GIVEN,
        llm_config: Optional[ModelConfigParam] | NotGiven = NOT_GIVEN,
        main_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        message_example: Optional[str] | NotGiven = NOT_GIVEN,
        mode_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        opening: Optional[str] | NotGiven = NOT_GIVEN,
        personality: Optional[str] | NotGiven = NOT_GIVEN,
        photos: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        post_history_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        prompt: Optional[str] | NotGiven = NOT_GIVEN,
        scenario: Optional[str] | NotGiven = NOT_GIVEN,
        settings: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        tags: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        visibility: AgentVisibility | NotGiven = NOT_GIVEN,
        voice_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseAgent:
        """
        Create new AI agent, used by app and inty-eval

        Args:
          creator_notes: 创作者备注

          llm_config: AI 模型配置

          main_prompt: 主提示词 - 作为第一个 system message，覆盖全局默认主提示词

          message_example: 对话示例

          mode_prompt: 模式提示词 - 放在角色卡提示词后面，覆盖全局默认模式提示词

          personality: 角色性格特点 (推荐)

          prompt: 已废弃 - 请使用 personality 字段代替

          scenario: 背景设定 (推荐)

          visibility: AI 角色可见性

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/ai/agents",
            body=maybe_transform(
                {
                    "gender": gender,
                    "name": name,
                    "alternate_greetings": alternate_greetings,
                    "avatar": avatar,
                    "background": background,
                    "background_images": background_images,
                    "category": category,
                    "character_book": character_book,
                    "character_card_spec": character_card_spec,
                    "character_version": character_version,
                    "creator_notes": creator_notes,
                    "extensions": extensions,
                    "intro": intro,
                    "llm_config": llm_config,
                    "main_prompt": main_prompt,
                    "message_example": message_example,
                    "mode_prompt": mode_prompt,
                    "opening": opening,
                    "personality": personality,
                    "photos": photos,
                    "post_history_instructions": post_history_instructions,
                    "prompt": prompt,
                    "scenario": scenario,
                    "settings": settings,
                    "tags": tags,
                    "visibility": visibility,
                    "voice_id": voice_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseAgent,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Get public agent by ID, include pre-generated agents and user-created public
        agents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/api/v1/ai/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def update(
        self,
        agent_id: str,
        *,
        alternate_greetings: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        background: Optional[str] | NotGiven = NOT_GIVEN,
        background_images: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        category: Optional[str] | NotGiven = NOT_GIVEN,
        character_book: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        character_card_spec: Optional[str] | NotGiven = NOT_GIVEN,
        character_version: Optional[str] | NotGiven = NOT_GIVEN,
        creator_notes: Optional[str] | NotGiven = NOT_GIVEN,
        extensions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        gender: Optional[str] | NotGiven = NOT_GIVEN,
        intro: Optional[str] | NotGiven = NOT_GIVEN,
        llm_config: Optional[ModelConfigParam] | NotGiven = NOT_GIVEN,
        main_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        message_example: Optional[str] | NotGiven = NOT_GIVEN,
        mode_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        opening: Optional[str] | NotGiven = NOT_GIVEN,
        personality: Optional[str] | NotGiven = NOT_GIVEN,
        photos: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        post_history_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        prompt: Optional[str] | NotGiven = NOT_GIVEN,
        scenario: Optional[str] | NotGiven = NOT_GIVEN,
        settings: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        tags: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        visibility: Optional[AgentVisibility] | NotGiven = NOT_GIVEN,
        voice_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Update AI agent

        Args:
          llm_config: AI 模型配置

          prompt: 已废弃 - 请使用 personality 字段代替

          visibility: AI 角色可见性

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._put(
            f"/api/v1/ai/agents/{agent_id}",
            body=maybe_transform(
                {
                    "alternate_greetings": alternate_greetings,
                    "avatar": avatar,
                    "background": background,
                    "background_images": background_images,
                    "category": category,
                    "character_book": character_book,
                    "character_card_spec": character_card_spec,
                    "character_version": character_version,
                    "creator_notes": creator_notes,
                    "extensions": extensions,
                    "gender": gender,
                    "intro": intro,
                    "llm_config": llm_config,
                    "main_prompt": main_prompt,
                    "message_example": message_example,
                    "mode_prompt": mode_prompt,
                    "name": name,
                    "opening": opening,
                    "personality": personality,
                    "photos": photos,
                    "post_history_instructions": post_history_instructions,
                    "prompt": prompt,
                    "scenario": scenario,
                    "settings": settings,
                    "tags": tags,
                    "visibility": visibility,
                    "voice_id": voice_id,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """
        This endpoint is used by an registered user to list their created AI characters
        (agents as a misnomer)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/ai/agents/me",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseAgent:
        """
        Delete AI agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/api/v1/ai/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseAgent,
        )

    def follow_agent(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseDict:
        """
        Follow AI agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/api/v1/ai/agents/{agent_id}/follow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDict,
        )

    def following(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponsePaginationDataAgent:
        """
        Get current user's followed AI agents list

        Args:
          page: Page number, starting from 1

          page_size: Items per page, maximum 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/ai/agents/following",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    agent_following_params.AgentFollowingParams,
                ),
            ),
            cast_to=APIResponsePaginationDataAgent,
        )

    def recommend(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort: Literal["created_asc", "created_desc", "random"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponsePaginationDataAgent:
        """
        Get recommended AI agents list (public and approved agents)

        Sorting options:

        - created_desc: Most recent first (default)
        - created_asc: Oldest first
        - random: Random order

        Args:
          page: Page number, starting from 1

          page_size: Items per page, maximum 100

          sort: Sort order: created_asc, created_desc, random

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/ai/agents/recommend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    agent_recommend_params.AgentRecommendParams,
                ),
            ),
            cast_to=APIResponsePaginationDataAgent,
        )

    def search(
        self,
        *,
        q: str,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponsePaginationDataAgent:
        """
        Search public AI agents Support fuzzy search by name, description, category

        Args:
          q: Search keyword

          page: Page number, starting from 1

          page_size: Items per page, maximum 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/ai/agents/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "page": page,
                        "page_size": page_size,
                    },
                    agent_search_params.AgentSearchParams,
                ),
            ),
            cast_to=APIResponsePaginationDataAgent,
        )

    def unfollow_agent(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseDict:
        """
        Unfollow AI agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._delete(
            f"/api/v1/ai/agents/{agent_id}/follow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDict,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        gender: str,
        name: str,
        alternate_greetings: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        background: Optional[str] | NotGiven = NOT_GIVEN,
        background_images: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        category: Optional[str] | NotGiven = NOT_GIVEN,
        character_book: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        character_card_spec: Optional[str] | NotGiven = NOT_GIVEN,
        character_version: Optional[str] | NotGiven = NOT_GIVEN,
        creator_notes: Optional[str] | NotGiven = NOT_GIVEN,
        extensions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        intro: Optional[str] | NotGiven = NOT_GIVEN,
        llm_config: Optional[ModelConfigParam] | NotGiven = NOT_GIVEN,
        main_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        message_example: Optional[str] | NotGiven = NOT_GIVEN,
        mode_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        opening: Optional[str] | NotGiven = NOT_GIVEN,
        personality: Optional[str] | NotGiven = NOT_GIVEN,
        photos: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        post_history_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        prompt: Optional[str] | NotGiven = NOT_GIVEN,
        scenario: Optional[str] | NotGiven = NOT_GIVEN,
        settings: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        tags: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        visibility: AgentVisibility | NotGiven = NOT_GIVEN,
        voice_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseAgent:
        """
        Create new AI agent, used by app and inty-eval

        Args:
          creator_notes: 创作者备注

          llm_config: AI 模型配置

          main_prompt: 主提示词 - 作为第一个 system message，覆盖全局默认主提示词

          message_example: 对话示例

          mode_prompt: 模式提示词 - 放在角色卡提示词后面，覆盖全局默认模式提示词

          personality: 角色性格特点 (推荐)

          prompt: 已废弃 - 请使用 personality 字段代替

          scenario: 背景设定 (推荐)

          visibility: AI 角色可见性

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/ai/agents",
            body=await async_maybe_transform(
                {
                    "gender": gender,
                    "name": name,
                    "alternate_greetings": alternate_greetings,
                    "avatar": avatar,
                    "background": background,
                    "background_images": background_images,
                    "category": category,
                    "character_book": character_book,
                    "character_card_spec": character_card_spec,
                    "character_version": character_version,
                    "creator_notes": creator_notes,
                    "extensions": extensions,
                    "intro": intro,
                    "llm_config": llm_config,
                    "main_prompt": main_prompt,
                    "message_example": message_example,
                    "mode_prompt": mode_prompt,
                    "opening": opening,
                    "personality": personality,
                    "photos": photos,
                    "post_history_instructions": post_history_instructions,
                    "prompt": prompt,
                    "scenario": scenario,
                    "settings": settings,
                    "tags": tags,
                    "visibility": visibility,
                    "voice_id": voice_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseAgent,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Get public agent by ID, include pre-generated agents and user-created public
        agents

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/api/v1/ai/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def update(
        self,
        agent_id: str,
        *,
        alternate_greetings: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        avatar: Optional[str] | NotGiven = NOT_GIVEN,
        background: Optional[str] | NotGiven = NOT_GIVEN,
        background_images: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        category: Optional[str] | NotGiven = NOT_GIVEN,
        character_book: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        character_card_spec: Optional[str] | NotGiven = NOT_GIVEN,
        character_version: Optional[str] | NotGiven = NOT_GIVEN,
        creator_notes: Optional[str] | NotGiven = NOT_GIVEN,
        extensions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        gender: Optional[str] | NotGiven = NOT_GIVEN,
        intro: Optional[str] | NotGiven = NOT_GIVEN,
        llm_config: Optional[ModelConfigParam] | NotGiven = NOT_GIVEN,
        main_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        message_example: Optional[str] | NotGiven = NOT_GIVEN,
        mode_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        opening: Optional[str] | NotGiven = NOT_GIVEN,
        personality: Optional[str] | NotGiven = NOT_GIVEN,
        photos: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        post_history_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        prompt: Optional[str] | NotGiven = NOT_GIVEN,
        scenario: Optional[str] | NotGiven = NOT_GIVEN,
        settings: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        tags: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        visibility: Optional[AgentVisibility] | NotGiven = NOT_GIVEN,
        voice_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """
        Update AI agent

        Args:
          llm_config: AI 模型配置

          prompt: 已废弃 - 请使用 personality 字段代替

          visibility: AI 角色可见性

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._put(
            f"/api/v1/ai/agents/{agent_id}",
            body=await async_maybe_transform(
                {
                    "alternate_greetings": alternate_greetings,
                    "avatar": avatar,
                    "background": background,
                    "background_images": background_images,
                    "category": category,
                    "character_book": character_book,
                    "character_card_spec": character_card_spec,
                    "character_version": character_version,
                    "creator_notes": creator_notes,
                    "extensions": extensions,
                    "gender": gender,
                    "intro": intro,
                    "llm_config": llm_config,
                    "main_prompt": main_prompt,
                    "message_example": message_example,
                    "mode_prompt": mode_prompt,
                    "name": name,
                    "opening": opening,
                    "personality": personality,
                    "photos": photos,
                    "post_history_instructions": post_history_instructions,
                    "prompt": prompt,
                    "scenario": scenario,
                    "settings": settings,
                    "tags": tags,
                    "visibility": visibility,
                    "voice_id": voice_id,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """
        This endpoint is used by an registered user to list their created AI characters
        (agents as a misnomer)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/ai/agents/me",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseAgent:
        """
        Delete AI agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/api/v1/ai/agents/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseAgent,
        )

    async def follow_agent(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseDict:
        """
        Follow AI agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/api/v1/ai/agents/{agent_id}/follow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDict,
        )

    async def following(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponsePaginationDataAgent:
        """
        Get current user's followed AI agents list

        Args:
          page: Page number, starting from 1

          page_size: Items per page, maximum 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/ai/agents/following",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    agent_following_params.AgentFollowingParams,
                ),
            ),
            cast_to=APIResponsePaginationDataAgent,
        )

    async def recommend(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        sort: Literal["created_asc", "created_desc", "random"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponsePaginationDataAgent:
        """
        Get recommended AI agents list (public and approved agents)

        Sorting options:

        - created_desc: Most recent first (default)
        - created_asc: Oldest first
        - random: Random order

        Args:
          page: Page number, starting from 1

          page_size: Items per page, maximum 100

          sort: Sort order: created_asc, created_desc, random

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/ai/agents/recommend",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    agent_recommend_params.AgentRecommendParams,
                ),
            ),
            cast_to=APIResponsePaginationDataAgent,
        )

    async def search(
        self,
        *,
        q: str,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponsePaginationDataAgent:
        """
        Search public AI agents Support fuzzy search by name, description, category

        Args:
          q: Search keyword

          page: Page number, starting from 1

          page_size: Items per page, maximum 100

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/ai/agents/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "page": page,
                        "page_size": page_size,
                    },
                    agent_search_params.AgentSearchParams,
                ),
            ),
            cast_to=APIResponsePaginationDataAgent,
        )

    async def unfollow_agent(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseDict:
        """
        Unfollow AI agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._delete(
            f"/api/v1/ai/agents/{agent_id}/follow",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseDict,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.follow_agent = to_raw_response_wrapper(
            agents.follow_agent,
        )
        self.following = to_raw_response_wrapper(
            agents.following,
        )
        self.recommend = to_raw_response_wrapper(
            agents.recommend,
        )
        self.search = to_raw_response_wrapper(
            agents.search,
        )
        self.unfollow_agent = to_raw_response_wrapper(
            agents.unfollow_agent,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.follow_agent = async_to_raw_response_wrapper(
            agents.follow_agent,
        )
        self.following = async_to_raw_response_wrapper(
            agents.following,
        )
        self.recommend = async_to_raw_response_wrapper(
            agents.recommend,
        )
        self.search = async_to_raw_response_wrapper(
            agents.search,
        )
        self.unfollow_agent = async_to_raw_response_wrapper(
            agents.unfollow_agent,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.follow_agent = to_streamed_response_wrapper(
            agents.follow_agent,
        )
        self.following = to_streamed_response_wrapper(
            agents.following,
        )
        self.recommend = to_streamed_response_wrapper(
            agents.recommend,
        )
        self.search = to_streamed_response_wrapper(
            agents.search,
        )
        self.unfollow_agent = to_streamed_response_wrapper(
            agents.unfollow_agent,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.follow_agent = async_to_streamed_response_wrapper(
            agents.follow_agent,
        )
        self.following = async_to_streamed_response_wrapper(
            agents.following,
        )
        self.recommend = async_to_streamed_response_wrapper(
            agents.recommend,
        )
        self.search = async_to_streamed_response_wrapper(
            agents.search,
        )
        self.unfollow_agent = async_to_streamed_response_wrapper(
            agents.unfollow_agent,
        )
