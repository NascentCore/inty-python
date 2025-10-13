# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1.users import ProfileMeResponse, ProfileUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Inty) -> None:
        profile = client.api.v1.users.profile.update()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inty) -> None:
        profile = client.api.v1.users.profile.update(
            age_group="age_group",
            avatar="avatar",
            description="description",
            email="email",
            gender="MALE",
            nickname="nickname",
            phone="phone",
            request_id="request_id",
            system_language="system_language",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inty) -> None:
        response = client.api.v1.users.profile.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inty) -> None:
        with client.api.v1.users.profile.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_me(self, client: Inty) -> None:
        profile = client.api.v1.users.profile.me()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_me(self, client: Inty) -> None:
        response = client.api.v1.users.profile.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_me(self, client: Inty) -> None:
        with client.api.v1.users.profile.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileMeResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInty) -> None:
        profile = await async_client.api.v1.users.profile.update()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInty) -> None:
        profile = await async_client.api.v1.users.profile.update(
            age_group="age_group",
            avatar="avatar",
            description="description",
            email="email",
            gender="MALE",
            nickname="nickname",
            phone="phone",
            request_id="request_id",
            system_language="system_language",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.users.profile.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.users.profile.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_me(self, async_client: AsyncInty) -> None:
        profile = await async_client.api.v1.users.profile.me()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_me(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.users.profile.with_raw_response.me()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileMeResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_me(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.users.profile.with_streaming_response.me() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileMeResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
