# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import APIResponseDict
from inty.types.api.v1.users import APIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inty) -> None:
        report = client.api.v1.report.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
        )
        assert_matches_type(APIResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inty) -> None:
        report = client.api.v1.report.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
            description="description",
            image_urls=["string"],
        )
        assert_matches_type(APIResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inty) -> None:
        response = client.api.v1.report.with_raw_response.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(APIResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inty) -> None:
        with client.api.v1.report.with_streaming_response.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(APIResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_image(self, client: Inty) -> None:
        report = client.api.v1.report.upload_image(
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseDict, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_image(self, client: Inty) -> None:
        response = client.api.v1.report.with_raw_response.upload_image(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(APIResponseDict, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_image(self, client: Inty) -> None:
        with client.api.v1.report.with_streaming_response.upload_image(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(APIResponseDict, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInty) -> None:
        report = await async_client.api.v1.report.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
        )
        assert_matches_type(APIResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInty) -> None:
        report = await async_client.api.v1.report.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
            description="description",
            image_urls=["string"],
        )
        assert_matches_type(APIResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.report.with_raw_response.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(APIResponse, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.report.with_streaming_response.create(
            reason_ids=[0],
            target_id="target_id",
            target_type="USER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(APIResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_image(self, async_client: AsyncInty) -> None:
        report = await async_client.api.v1.report.upload_image(
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseDict, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_image(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.report.with_raw_response.upload_image(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(APIResponseDict, report, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_image(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.report.with_streaming_response.upload_image(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(APIResponseDict, report, path=["response"])

        assert cast(Any, response.is_closed) is True
