# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inty import Inty, AsyncInty
from tests.utils import assert_matches_type
from inty.types.api.v1.subscription.admin import (
    PlanListResponse,
    PlanCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inty) -> None:
        plan = client.api.v1.subscription.admin.plans.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
        )
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inty) -> None:
        plan = client.api.v1.subscription.admin.plans.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
            agent_creation_limit=0,
            background_generation_limit_per_day=0,
            chat_limit_per_day=0,
            currency="currency",
            description="description",
            discount_rate=0,
            features={"foo": "bar"},
            is_active=True,
            sort_order=0,
        )
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inty) -> None:
        response = client.api.v1.subscription.admin.plans.with_raw_response.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inty) -> None:
        with client.api.v1.subscription.admin.plans.with_streaming_response.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanCreateResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inty) -> None:
        plan = client.api.v1.subscription.admin.plans.list()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inty) -> None:
        plan = client.api.v1.subscription.admin.plans.list(
            include_inactive=True,
        )
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inty) -> None:
        response = client.api.v1.subscription.admin.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inty) -> None:
        with client.api.v1.subscription.admin.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanListResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInty) -> None:
        plan = await async_client.api.v1.subscription.admin.plans.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
        )
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInty) -> None:
        plan = await async_client.api.v1.subscription.admin.plans.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
            agent_creation_limit=0,
            background_generation_limit_per_day=0,
            chat_limit_per_day=0,
            currency="currency",
            description="description",
            discount_rate=0,
            features={"foo": "bar"},
            is_active=True,
            sort_order=0,
        )
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.admin.plans.with_raw_response.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.admin.plans.with_streaming_response.create(
            google_play_product_id="google_play_product_id",
            name="name",
            plan_type="MONTHLY",
            price=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanCreateResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInty) -> None:
        plan = await async_client.api.v1.subscription.admin.plans.list()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInty) -> None:
        plan = await async_client.api.v1.subscription.admin.plans.list(
            include_inactive=True,
        )
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInty) -> None:
        response = await async_client.api.v1.subscription.admin.plans.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanListResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInty) -> None:
        async with async_client.api.v1.subscription.admin.plans.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanListResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True
