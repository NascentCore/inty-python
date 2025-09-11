# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_message_voice(self, client: Inty) -> None:
        agent = client.api.v1.chats.agents.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_message_voice_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.chats.agents.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
            language="language",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_message_voice(self, client: Inty) -> None:
        response = client.api.v1.chats.agents.with_raw_response.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_message_voice(self, client: Inty) -> None:
        with client.api.v1.chats.agents.with_streaming_response.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_message_voice(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.chats.agents.with_raw_response.generate_message_voice(
                message_id="message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.chats.agents.with_raw_response.generate_message_voice(
                message_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_messages(self, client: Inty) -> None:
        agent = client.api.v1.chats.agents.get_messages(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_messages_with_all_params(self, client: Inty) -> None:
        agent = client.api.v1.chats.agents.get_messages(
            agent_id="agent_id",
            limit=1,
            offset=0,
            order="desc",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_messages(self, client: Inty) -> None:
        response = client.api.v1.chats.agents.with_raw_response.get_messages(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_messages(self, client: Inty) -> None:
        with client.api.v1.chats.agents.with_streaming_response.get_messages(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_messages(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.chats.agents.with_raw_response.get_messages(
                agent_id="",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_message_voice(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.chats.agents.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_message_voice_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.chats.agents.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
            language="language",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_message_voice(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.chats.agents.with_raw_response.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_message_voice(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.chats.agents.with_streaming_response.generate_message_voice(
            message_id="message_id",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_message_voice(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.chats.agents.with_raw_response.generate_message_voice(
                message_id="message_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.chats.agents.with_raw_response.generate_message_voice(
                message_id="",
                agent_id="agent_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_messages(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.chats.agents.get_messages(
            agent_id="agent_id",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_messages_with_all_params(self, async_client: AsyncInty) -> None:
        agent = await async_client.api.v1.chats.agents.get_messages(
            agent_id="agent_id",
            limit=1,
            offset=0,
            order="desc",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_messages(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.chats.agents.with_raw_response.get_messages(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_messages(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.chats.agents.with_streaming_response.get_messages(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_messages(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.chats.agents.with_raw_response.get_messages(
                agent_id="",
            )
