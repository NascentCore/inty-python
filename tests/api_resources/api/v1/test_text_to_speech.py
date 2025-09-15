# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import TextToSpeechListVoicesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTextToSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_speech(self, client: Inty) -> None:
        text_to_speech = client.api.v1.text_to_speech.generate_speech(
            "message_id",
        )
        assert_matches_type(object, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_speech(self, client: Inty) -> None:
        response = client.api.v1.text_to_speech.with_raw_response.generate_speech(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(object, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_speech(self, client: Inty) -> None:
        with client.api.v1.text_to_speech.with_streaming_response.generate_speech(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(object, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_generate_speech(self, client: Inty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.api.v1.text_to_speech.with_raw_response.generate_speech(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_voices(self, client: Inty) -> None:
        text_to_speech = client.api.v1.text_to_speech.list_voices()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_voices_with_all_params(self, client: Inty) -> None:
        text_to_speech = client.api.v1.text_to_speech.list_voices(
            category="category",
            page_size=1,
            search="search",
            voice_type="voice_type",
        )
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_voices(self, client: Inty) -> None:
        response = client.api.v1.text_to_speech.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = response.parse()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_voices(self, client: Inty) -> None:
        with client.api.v1.text_to_speech.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = response.parse()
            assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTextToSpeech:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_speech(self, async_client: AsyncInty) -> None:
        text_to_speech = await async_client.api.v1.text_to_speech.generate_speech(
            "message_id",
        )
        assert_matches_type(object, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_speech(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.text_to_speech.with_raw_response.generate_speech(
            "message_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(object, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_speech(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.text_to_speech.with_streaming_response.generate_speech(
            "message_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(object, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_generate_speech(self, async_client: AsyncInty) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.api.v1.text_to_speech.with_raw_response.generate_speech(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_voices(self, async_client: AsyncInty) -> None:
        text_to_speech = await async_client.api.v1.text_to_speech.list_voices()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_voices_with_all_params(self, async_client: AsyncInty) -> None:
        text_to_speech = await async_client.api.v1.text_to_speech.list_voices(
            category="category",
            page_size=1,
            search="search",
            voice_type="voice_type",
        )
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_voices(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.text_to_speech.with_raw_response.list_voices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        text_to_speech = await response.parse()
        assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_voices(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.text_to_speech.with_streaming_response.list_voices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            text_to_speech = await response.parse()
            assert_matches_type(TextToSpeechListVoicesResponse, text_to_speech, path=["response"])

        assert cast(Any, response.is_closed) is True
