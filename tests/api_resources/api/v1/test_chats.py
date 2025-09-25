# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import (
    Chat,
    APIResponseDict,
    ChatListResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inty) -> None:
        chat = client.api.v1.chats.create(
            agent_id="agent_id",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inty) -> None:
        response = client.api.v1.chats.with_raw_response.create(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inty) -> None:
        with client.api.v1.chats.with_streaming_response.create(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inty) -> None:
        chat = client.api.v1.chats.list()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inty) -> None:
        chat = client.api.v1.chats.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inty) -> None:
        response = client.api.v1.chats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inty) -> None:
        with client.api.v1.chats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inty) -> None:
        chat = client.api.v1.chats.delete(
            "chat_id",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inty) -> None:
        response = client.api.v1.chats.with_raw_response.delete(
            "chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inty) -> None:
        with client.api.v1.chats.with_streaming_response.delete(
            "chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.api.v1.chats.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: Inty) -> None:
        chat = client.api.v1.chats.create_completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(APIResponseDict, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: Inty) -> None:
        chat = client.api.v1.chats.create_completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            language="language",
            model="model",
            stream=True,
        )
        assert_matches_type(APIResponseDict, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: Inty) -> None:
        response = client.api.v1.chats.with_raw_response.create_completion(
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
        assert_matches_type(APIResponseDict, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: Inty) -> None:
        with client.api.v1.chats.with_streaming_response.create_completion(
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
            assert_matches_type(APIResponseDict, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_completion(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.api.v1.chats.with_raw_response.create_completion(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_voice(self, client: Inty) -> None:
        with pytest.warns(DeprecationWarning):
            chat = client.api.v1.chats.retrieve_voice(
                "voice_id",
            )

        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_voice(self, client: Inty) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.api.v1.chats.with_raw_response.retrieve_voice(
                "voice_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_voice(self, client: Inty) -> None:
        with pytest.warns(DeprecationWarning):
            with client.api.v1.chats.with_streaming_response.retrieve_voice(
                "voice_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                chat = response.parse()
                assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_voice(self, client: Inty) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `voice_id` but received ''"):
                client.api.v1.chats.with_raw_response.retrieve_voice(
                    "",
                )


class TestAsyncChats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInty) -> None:
        chat = await async_client.api.v1.chats.create(
            agent_id="agent_id",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.chats.with_raw_response.create(
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.chats.with_streaming_response.create(
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInty) -> None:
        chat = await async_client.api.v1.chats.list()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInty) -> None:
        chat = await async_client.api.v1.chats.list(
            limit=0,
            skip=0,
        )
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.chats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.chats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInty) -> None:
        chat = await async_client.api.v1.chats.delete(
            "chat_id",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.chats.with_raw_response.delete(
            "chat_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.chats.with_streaming_response.delete(
            "chat_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncInty) -> None:
        chat = await async_client.api.v1.chats.create_completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(APIResponseDict, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncInty) -> None:
        chat = await async_client.api.v1.chats.create_completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            language="language",
            model="model",
            stream=True,
        )
        assert_matches_type(APIResponseDict, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.chats.with_raw_response.create_completion(
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
        assert_matches_type(APIResponseDict, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.chats.with_streaming_response.create_completion(
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
            assert_matches_type(APIResponseDict, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_completion(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.api.v1.chats.with_raw_response.create_completion(
                agent_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_voice(self, async_client: AsyncInty) -> None:
        with pytest.warns(DeprecationWarning):
            chat = await async_client.api.v1.chats.retrieve_voice(
                "voice_id",
            )

        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_voice(self, async_client: AsyncInty) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.api.v1.chats.with_raw_response.retrieve_voice(
                "voice_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_voice(self, async_client: AsyncInty) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.api.v1.chats.with_streaming_response.retrieve_voice(
                "voice_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                chat = await response.parse()
                assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_voice(self, async_client: AsyncInty) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `voice_id` but received ''"):
                await async_client.api.v1.chats.with_raw_response.retrieve_voice(
                    "",
                )
