# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1.subscription import AdminProcessRefundResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdmin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_process_refund(self, client: Inty) -> None:
        admin = client.api.v1.subscription.admin.process_refund(
            subscription_id="subscription_id",
        )
        assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_process_refund_with_all_params(self, client: Inty) -> None:
        admin = client.api.v1.subscription.admin.process_refund(
            subscription_id="subscription_id",
            reason="reason",
            refund_amount=0,
        )
        assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_process_refund(self, client: Inty) -> None:
        response = client.api.v1.subscription.admin.with_raw_response.process_refund(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = response.parse()
        assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_process_refund(self, client: Inty) -> None:
        with client.api.v1.subscription.admin.with_streaming_response.process_refund(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = response.parse()
            assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdmin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_process_refund(self, async_client: AsyncInty) -> None:
        admin = await async_client.api.v1.subscription.admin.process_refund(
            subscription_id="subscription_id",
        )
        assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_process_refund_with_all_params(self, async_client: AsyncInty) -> None:
        admin = await async_client.api.v1.subscription.admin.process_refund(
            subscription_id="subscription_id",
            reason="reason",
            refund_amount=0,
        )
        assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_process_refund(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.admin.with_raw_response.process_refund(
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        admin = await response.parse()
        assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_process_refund(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.admin.with_streaming_response.process_refund(
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            admin = await response.parse()
            assert_matches_type(AdminProcessRefundResponse, admin, path=["response"])

        assert cast(Any, response.is_closed) is True
