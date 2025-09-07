# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1.users import DeletionCheckEligibilityResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeletion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_eligibility(self, client: Inty) -> None:
        deletion = client.api.v1.users.deletion.check_eligibility()
        assert_matches_type(DeletionCheckEligibilityResponse, deletion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_eligibility(self, client: Inty) -> None:
        response = client.api.v1.users.deletion.with_raw_response.check_eligibility()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deletion = response.parse()
        assert_matches_type(DeletionCheckEligibilityResponse, deletion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_eligibility(self, client: Inty) -> None:
        with client.api.v1.users.deletion.with_streaming_response.check_eligibility() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deletion = response.parse()
            assert_matches_type(DeletionCheckEligibilityResponse, deletion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeletion:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_eligibility(self, async_client: AsyncInty) -> None:
        deletion = await async_client.api.v1.users.deletion.check_eligibility()
        assert_matches_type(DeletionCheckEligibilityResponse, deletion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_eligibility(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.users.deletion.with_raw_response.check_eligibility()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deletion = await response.parse()
        assert_matches_type(DeletionCheckEligibilityResponse, deletion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_eligibility(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.users.deletion.with_streaming_response.check_eligibility() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deletion = await response.parse()
            assert_matches_type(DeletionCheckEligibilityResponse, deletion, path=["response"])

        assert cast(Any, response.is_closed) is True
