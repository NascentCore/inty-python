# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import APIResponseDict
from inty.types.api.v1.ai import (
    Agent,
    APIResponseAgent,
    AgentListResponse,
    AgentCreateResponse,
    APIResponsePaginationDataAgent,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.create(
            gender="gender",
            name="name",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.create(
            gender="gender",
            name="name",
            alternate_greetings=["string"],
            avatar="avatar",
            background="background",
            background_images=["string"],
            category="category",
            character_book={"foo": "bar"},
            character_card_spec="character_card_spec",
            character_version="character_version",
            creator_notes="creator_notes",
            extensions={"foo": "bar"},
            intro="intro",
            llm_config={
                "api_key": "api_key",
                "base_url": "base_url",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "model": "model",
                "presence_penalty": -2,
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            main_prompt="main_prompt",
            message_example="message_example",
            meta_data={
                "comment": "comment",
                "score": 0,
            },
            mode_prompt="mode_prompt",
            opening="opening",
            opening_audio_url="opening_audio_url",
            personality="personality",
            photos=["string"],
            post_history_instructions="post_history_instructions",
            prompt="prompt",
            request_id="request_id",
            scenario="scenario",
            settings={"foo": "bar"},
            tags=["string"],
            visibility="PUBLIC",
            voice_id="voice_id",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.create(
            gender="gender",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.create(
            gender="gender",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.retrieve(
            "agent_id",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.ai.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.update(
            agent_id="agent_id",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.update(
            agent_id="agent_id",
            alternate_greetings=["string"],
            avatar="avatar",
            background="background",
            background_images=["string"],
            category="category",
            character_book={"foo": "bar"},
            character_card_spec="character_card_spec",
            character_version="character_version",
            creator_notes="creator_notes",
            extensions={"foo": "bar"},
            gender="gender",
            intro="intro",
            llm_config={
                "api_key": "api_key",
                "base_url": "base_url",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "model": "model",
                "presence_penalty": -2,
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            main_prompt="main_prompt",
            message_example="message_example",
            meta_data={
                "comment": "comment",
                "score": 0,
            },
            mode_prompt="mode_prompt",
            name="name",
            opening="opening",
            opening_audio_url="opening_audio_url",
            personality="personality",
            photos=["string"],
            post_history_instructions="post_history_instructions",
            prompt="prompt",
            request_id="request_id",
            scenario="scenario",
            settings={"foo": "bar"},
            tags=["string"],
            visibility="PUBLIC",
            voice_id="voice_id",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.update(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.update(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.ai.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.delete(
            "agent_id",
        )
        assert_matches_type(APIResponseAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(APIResponseAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(APIResponseAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.ai.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_follow_agent(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.follow_agent(
            "agent_id",
        )
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_follow_agent(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.follow_agent(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_follow_agent(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.follow_agent(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(APIResponseDict, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_follow_agent(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.ai.agents.with_raw_response.follow_agent(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_following(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.following()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_following_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.following(
            page=1,
            page_size=1,
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_following(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.following()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_following(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.following() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_recommend(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.recommend()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_recommend_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.recommend(
            page=1,
            page_size=1,
            sort="created_asc",
            sort_seed="sort_seed",
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_recommend(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.recommend()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_recommend(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.recommend() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.search(
            q="q",
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.search(
            q="q",
            page=1,
            page_size=1,
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unfollow_agent(self, client: Inty) -> None:
        agent = client.api.v1.ai.agents.unfollow_agent(
            "agent_id",
        )
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unfollow_agent(self, client: Inty) -> None:
        response = client.api.v1.ai.agents.with_raw_response.unfollow_agent(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unfollow_agent(self, client: Inty) -> None:
        with client.api.v1.ai.agents.with_streaming_response.unfollow_agent(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(APIResponseDict, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unfollow_agent(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.ai.agents.with_raw_response.unfollow_agent(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.create(
            gender="gender",
            name="name",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.create(
            gender="gender",
            name="name",
            alternate_greetings=["string"],
            avatar="avatar",
            background="background",
            background_images=["string"],
            category="category",
            character_book={"foo": "bar"},
            character_card_spec="character_card_spec",
            character_version="character_version",
            creator_notes="creator_notes",
            extensions={"foo": "bar"},
            intro="intro",
            llm_config={
                "api_key": "api_key",
                "base_url": "base_url",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "model": "model",
                "presence_penalty": -2,
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            main_prompt="main_prompt",
            message_example="message_example",
            meta_data={
                "comment": "comment",
                "score": 0,
            },
            mode_prompt="mode_prompt",
            opening="opening",
            opening_audio_url="opening_audio_url",
            personality="personality",
            photos=["string"],
            post_history_instructions="post_history_instructions",
            prompt="prompt",
            request_id="request_id",
            scenario="scenario",
            settings={"foo": "bar"},
            tags=["string"],
            visibility="PUBLIC",
            voice_id="voice_id",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.create(
            gender="gender",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.create(
            gender="gender",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.retrieve(
            "agent_id",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.retrieve(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.retrieve(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.ai.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.update(
            agent_id="agent_id",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.update(
            agent_id="agent_id",
            alternate_greetings=["string"],
            avatar="avatar",
            background="background",
            background_images=["string"],
            category="category",
            character_book={"foo": "bar"},
            character_card_spec="character_card_spec",
            character_version="character_version",
            creator_notes="creator_notes",
            extensions={"foo": "bar"},
            gender="gender",
            intro="intro",
            llm_config={
                "api_key": "api_key",
                "base_url": "base_url",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "model": "model",
                "presence_penalty": -2,
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            main_prompt="main_prompt",
            message_example="message_example",
            meta_data={
                "comment": "comment",
                "score": 0,
            },
            mode_prompt="mode_prompt",
            name="name",
            opening="opening",
            opening_audio_url="opening_audio_url",
            personality="personality",
            photos=["string"],
            post_history_instructions="post_history_instructions",
            prompt="prompt",
            request_id="request_id",
            scenario="scenario",
            settings={"foo": "bar"},
            tags=["string"],
            visibility="PUBLIC",
            voice_id="voice_id",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.update(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.update(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.ai.agents.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.delete(
            "agent_id",
        )
        assert_matches_type(APIResponseAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(APIResponseAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(APIResponseAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.ai.agents.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_follow_agent(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.follow_agent(
            "agent_id",
        )
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_follow_agent(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.follow_agent(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_follow_agent(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.follow_agent(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(APIResponseDict, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_follow_agent(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.ai.agents.with_raw_response.follow_agent(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_following(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.following()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_following_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.following(
            page=1,
            page_size=1,
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_following(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.following()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_following(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.following() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_recommend(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.recommend()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_recommend_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.recommend(
            page=1,
            page_size=1,
            sort="created_asc",
            sort_seed="sort_seed",
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_recommend(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.recommend()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_recommend(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.recommend() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.search(
            q="q",
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.search(
            q="q",
            page=1,
            page_size=1,
        )
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(APIResponsePaginationDataAgent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unfollow_agent(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.ai.agents.unfollow_agent(
            "agent_id",
        )
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unfollow_agent(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.ai.agents.with_raw_response.unfollow_agent(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(APIResponseDict, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unfollow_agent(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.ai.agents.with_streaming_response.unfollow_agent(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(APIResponseDict, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unfollow_agent(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.ai.agents.with_raw_response.unfollow_agent(
                "",
            )
