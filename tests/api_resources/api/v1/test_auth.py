# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import AuthCreateGuestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_guest(self, client: Inty) -> None:
        auth = client.api.v1.auth.create_guest()
        assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_guest_with_all_params(self, client: Inty) -> None:
        auth = client.api.v1.auth.create_guest(
            age_group="age_group",
            device_id="device_id",
            request_id="request_id",
            system_language="system_language",
        )
        assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_guest(self, client: Inty) -> None:
        response = client.api.v1.auth.with_raw_response.create_guest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_guest(self, client: Inty) -> None:
        with client.api.v1.auth.with_streaming_response.create_guest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_guest(self, async_client: AsyncInty) -> None:
        auth = await async_client.api.v1.auth.create_guest()
        assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_guest_with_all_params(self, async_client: AsyncInty) -> None:
        auth = await async_client.api.v1.auth.create_guest(
            age_group="age_group",
            device_id="device_id",
            request_id="request_id",
            system_language="system_language",
        )
        assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_guest(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.auth.with_raw_response.create_guest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_guest(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.auth.with_streaming_response.create_guest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthCreateGuestResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
