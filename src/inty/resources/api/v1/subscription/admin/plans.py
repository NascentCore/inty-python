# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.api.v1.subscription.admin import SubscriptionPlanType, plan_list_params, plan_create_params
from ......types.api.v1.subscription.admin.plan_list_response import PlanListResponse
from ......types.api.v1.subscription.admin.plan_create_response import PlanCreateResponse
from ......types.api.v1.subscription.admin.subscription_plan_type import SubscriptionPlanType

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return PlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return PlansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        google_play_product_id: str,
        name: str,
        plan_type: SubscriptionPlanType,
        price: float,
        agent_creation_limit: int | NotGiven = NOT_GIVEN,
        background_generation_limit_per_day: int | NotGiven = NOT_GIVEN,
        chat_limit_per_day: int | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        discount_rate: float | NotGiven = NOT_GIVEN,
        features: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        sort_order: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanCreateResponse:
        """
        创建订阅计划（管理员接口）

        Args:
          google_play_product_id: Google Play 产品 ID

          name: 计划名称

          plan_type: 计划类型

          price: 价格

          agent_creation_limit: Agent 创建数量限制

          background_generation_limit_per_day: 每日背景图生成次数限制，-1 为无限制

          chat_limit_per_day: 每日聊天次数限制，-1 为无限制

          currency: 货币

          description: 计划描述

          discount_rate: 价格折扣率，范围 0-1，1 表示无折扣

          features: 功能权益配置

          is_active: 是否激活

          sort_order: 排序顺序

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/subscription/admin/plans",
            body=maybe_transform(
                {
                    "google_play_product_id": google_play_product_id,
                    "name": name,
                    "plan_type": plan_type,
                    "price": price,
                    "agent_creation_limit": agent_creation_limit,
                    "background_generation_limit_per_day": background_generation_limit_per_day,
                    "chat_limit_per_day": chat_limit_per_day,
                    "currency": currency,
                    "description": description,
                    "discount_rate": discount_rate,
                    "features": features,
                    "is_active": is_active,
                    "sort_order": sort_order,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanCreateResponse,
        )

    def list(
        self,
        *,
        include_inactive: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanListResponse:
        """
        获取所有订阅计划（管理员接口）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/subscription/admin/plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_inactive": include_inactive}, plan_list_params.PlanListParams),
            ),
            cast_to=PlanListResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncPlansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        google_play_product_id: str,
        name: str,
        plan_type: SubscriptionPlanType,
        price: float,
        agent_creation_limit: int | NotGiven = NOT_GIVEN,
        background_generation_limit_per_day: int | NotGiven = NOT_GIVEN,
        chat_limit_per_day: int | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        discount_rate: float | NotGiven = NOT_GIVEN,
        features: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        sort_order: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanCreateResponse:
        """
        创建订阅计划（管理员接口）

        Args:
          google_play_product_id: Google Play 产品 ID

          name: 计划名称

          plan_type: 计划类型

          price: 价格

          agent_creation_limit: Agent 创建数量限制

          background_generation_limit_per_day: 每日背景图生成次数限制，-1 为无限制

          chat_limit_per_day: 每日聊天次数限制，-1 为无限制

          currency: 货币

          description: 计划描述

          discount_rate: 价格折扣率，范围 0-1，1 表示无折扣

          features: 功能权益配置

          is_active: 是否激活

          sort_order: 排序顺序

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/subscription/admin/plans",
            body=await async_maybe_transform(
                {
                    "google_play_product_id": google_play_product_id,
                    "name": name,
                    "plan_type": plan_type,
                    "price": price,
                    "agent_creation_limit": agent_creation_limit,
                    "background_generation_limit_per_day": background_generation_limit_per_day,
                    "chat_limit_per_day": chat_limit_per_day,
                    "currency": currency,
                    "description": description,
                    "discount_rate": discount_rate,
                    "features": features,
                    "is_active": is_active,
                    "sort_order": sort_order,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanCreateResponse,
        )

    async def list(
        self,
        *,
        include_inactive: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlanListResponse:
        """
        获取所有订阅计划（管理员接口）

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/subscription/admin/plans",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_inactive": include_inactive}, plan_list_params.PlanListParams
                ),
            ),
            cast_to=PlanListResponse,
        )


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_raw_response_wrapper(
            plans.create,
        )
        self.list = to_raw_response_wrapper(
            plans.list,
        )


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_raw_response_wrapper(
            plans.create,
        )
        self.list = async_to_raw_response_wrapper(
            plans.list,
        )


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_streamed_response_wrapper(
            plans.create,
        )
        self.list = to_streamed_response_wrapper(
            plans.list,
        )


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_streamed_response_wrapper(
            plans.create,
        )
        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
