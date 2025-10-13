# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.v2 import ChatSendMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message(self, client: Inty) -> None:
        chat = client.v2.chat.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message_with_all_params(self, client: Inty) -> None:
        chat = client.v2.chat.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            language="language",
            model="model",
            request_id="request_id",
            stream=True,
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: Inty) -> None:
        response = client.v2.chat.with_raw_response.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: Inty) -> None:
        with client.v2.chat.with_streaming_response.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_message(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.v2.chat.with_raw_response.send_message(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncInty) -> None:
        chat = await async_client.v2.chat.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message_with_all_params(self, async_client: AsyncInty) -> None:
        chat = await async_client.v2.chat.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            language="language",
            model="model",
            request_id="request_id",
            stream=True,
        )
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncInty) -> None:
        response = await async_client.v2.chat.with_raw_response.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncInty) -> None:
        async with async_client.v2.chat.with_streaming_response.send_message(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatSendMessageResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_message(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.v2.chat.with_raw_response.send_message(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )
