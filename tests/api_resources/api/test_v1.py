# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api import V1ListNotificationsResponse
from inty.types.api.v1 import APIResponseDict

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_notifications(self, client: Inty) -> None:
        v1 = client.api.v1.list_notifications()
        assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_notifications_with_all_params(self, client: Inty) -> None:
        v1 = client.api.v1.list_notifications(
            is_read=True,
            page=0,
            page_size=0,
        )
        assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_notifications(self, client: Inty) -> None:
        response = client.api.v1.with_raw_response.list_notifications()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_notifications(self, client: Inty) -> None:
        with client.api.v1.with_streaming_response.list_notifications() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_image(self, client: Inty) -> None:
        v1 = client.api.v1.upload_image(
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseDict, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_image_with_all_params(self, client: Inty) -> None:
        v1 = client.api.v1.upload_image(
            file=b"raw file contents",
            cropping_avatar=True,
        )
        assert_matches_type(APIResponseDict, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_image(self, client: Inty) -> None:
        response = client.api.v1.with_raw_response.upload_image(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(APIResponseDict, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_image(self, client: Inty) -> None:
        with client.api.v1.with_streaming_response.upload_image(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(APIResponseDict, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_notifications(self, async_client: AsyncInty) -> None:
        v1 = await async_client.api.v1.list_notifications()
        assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_notifications_with_all_params(self, async_client: AsyncInty) -> None:
        v1 = await async_client.api.v1.list_notifications(
            is_read=True,
            page=0,
            page_size=0,
        )
        assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_notifications(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.with_raw_response.list_notifications()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_notifications(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.with_streaming_response.list_notifications() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ListNotificationsResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_image(self, async_client: AsyncInty) -> None:
        v1 = await async_client.api.v1.upload_image(
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseDict, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_image_with_all_params(self, async_client: AsyncInty) -> None:
        v1 = await async_client.api.v1.upload_image(
            file=b"raw file contents",
            cropping_avatar=True,
        )
        assert_matches_type(APIResponseDict, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_image(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.with_raw_response.upload_image(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(APIResponseDict, v1, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_image(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.with_streaming_response.upload_image(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(APIResponseDict, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
