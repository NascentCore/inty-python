# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1.users import APIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register(self, client: Inty) -> None:
        device = client.api.v1.users.device.register(
            token="token",
        )
        assert_matches_type(APIResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: Inty) -> None:
        response = client.api.v1.users.device.with_raw_response.register(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(APIResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: Inty) -> None:
        with client.api.v1.users.device.with_streaming_response.register(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(APIResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDevice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncInty) -> None:
        device = await async_client.api.v1.users.device.register(
            token="token",
        )
        assert_matches_type(APIResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.users.device.with_raw_response.register(
            token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(APIResponse, device, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.users.device.with_streaming_response.register(
            token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(APIResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True
