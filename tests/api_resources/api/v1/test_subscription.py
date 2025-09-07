# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1 import (
    APIResponseUsageStatistics,
    SubscriptionVerifyResponse,
    SubscriptionWebhookResponse,
    APIResponseSubscriptionStatus,
    SubscriptionListPlansResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Inty) -> None:
        subscription = client.api.v1.subscription.get_status()
        assert_matches_type(APIResponseSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Inty) -> None:
        response = client.api.v1.subscription.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(APIResponseSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Inty) -> None:
        with client.api.v1.subscription.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(APIResponseSubscriptionStatus, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_usage(self, client: Inty) -> None:
        subscription = client.api.v1.subscription.get_usage()
        assert_matches_type(APIResponseUsageStatistics, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_usage(self, client: Inty) -> None:
        response = client.api.v1.subscription.with_raw_response.get_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(APIResponseUsageStatistics, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_usage(self, client: Inty) -> None:
        with client.api.v1.subscription.with_streaming_response.get_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(APIResponseUsageStatistics, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_plans(self, client: Inty) -> None:
        subscription = client.api.v1.subscription.list_plans()
        assert_matches_type(SubscriptionListPlansResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_plans(self, client: Inty) -> None:
        response = client.api.v1.subscription.with_raw_response.list_plans()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionListPlansResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_plans(self, client: Inty) -> None:
        with client.api.v1.subscription.with_streaming_response.list_plans() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionListPlansResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify(self, client: Inty) -> None:
        subscription = client.api.v1.subscription.verify(
            product_id="product_id",
            purchase_token="purchase_token",
        )
        assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify_with_all_params(self, client: Inty) -> None:
        subscription = client.api.v1.subscription.verify(
            product_id="product_id",
            purchase_token="purchase_token",
            order_id="order_id",
        )
        assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Inty) -> None:
        response = client.api.v1.subscription.with_raw_response.verify(
            product_id="product_id",
            purchase_token="purchase_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Inty) -> None:
        with client.api.v1.subscription.with_streaming_response.verify(
            product_id="product_id",
            purchase_token="purchase_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_webhook(self, client: Inty) -> None:
        subscription = client.api.v1.subscription.webhook()
        assert_matches_type(SubscriptionWebhookResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_webhook(self, client: Inty) -> None:
        response = client.api.v1.subscription.with_raw_response.webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionWebhookResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_webhook(self, client: Inty) -> None:
        with client.api.v1.subscription.with_streaming_response.webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionWebhookResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscription:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncInty) -> None:
        subscription = await async_client.api.v1.subscription.get_status()
        assert_matches_type(APIResponseSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(APIResponseSubscriptionStatus, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(APIResponseSubscriptionStatus, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_usage(self, async_client: AsyncInty) -> None:
        subscription = await async_client.api.v1.subscription.get_usage()
        assert_matches_type(APIResponseUsageStatistics, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.with_raw_response.get_usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(APIResponseUsageStatistics, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.with_streaming_response.get_usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(APIResponseUsageStatistics, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_plans(self, async_client: AsyncInty) -> None:
        subscription = await async_client.api.v1.subscription.list_plans()
        assert_matches_type(SubscriptionListPlansResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_plans(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.with_raw_response.list_plans()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionListPlansResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_plans(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.with_streaming_response.list_plans() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionListPlansResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncInty) -> None:
        subscription = await async_client.api.v1.subscription.verify(
            product_id="product_id",
            purchase_token="purchase_token",
        )
        assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncInty) -> None:
        subscription = await async_client.api.v1.subscription.verify(
            product_id="product_id",
            purchase_token="purchase_token",
            order_id="order_id",
        )
        assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.with_raw_response.verify(
            product_id="product_id",
            purchase_token="purchase_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.with_streaming_response.verify(
            product_id="product_id",
            purchase_token="purchase_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionVerifyResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_webhook(self, async_client: AsyncInty) -> None:
        subscription = await async_client.api.v1.subscription.webhook()
        assert_matches_type(SubscriptionWebhookResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_webhook(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.with_raw_response.webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionWebhookResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_webhook(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.with_streaming_response.webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionWebhookResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
