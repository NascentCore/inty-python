# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import UserDeleteAccountResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_account(self, client: Inty) -> None:
        user = client.api.v1.users.delete_account()
        assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_account_with_all_params(self, client: Inty) -> None:
        user = client.api.v1.users.delete_account(
            reason="隐私关注",
            request_id="request_id",
        )
        assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_account(self, client: Inty) -> None:
        response = client.api.v1.users.with_raw_response.delete_account()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_account(self, client: Inty) -> None:
        with client.api.v1.users.with_streaming_response.delete_account() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_account(self, async_client: AsyncInty) -> None:
        user = await async_client.api.v1.users.delete_account()
        assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_account_with_all_params(self, async_client: AsyncInty) -> None:
        user = await async_client.api.v1.users.delete_account(
            reason="隐私关注",
            request_id="request_id",
        )
        assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_account(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.users.with_raw_response.delete_account()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_account(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.users.with_streaming_response.delete_account() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteAccountResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
