# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .admin.admin import (
    AdminResource,
    AsyncAdminResource,
    AdminResourceWithRawResponse,
    AsyncAdminResourceWithRawResponse,
    AdminResourceWithStreamingResponse,
    AsyncAdminResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1 import subscription_verify_params
from .....types.api.v1.subscription_verify_response import SubscriptionVerifyResponse
from .....types.api.v1.api_response_usage_statistics import APIResponseUsageStatistics
from .....types.api.v1.subscription_webhook_response import SubscriptionWebhookResponse
from .....types.api.v1.api_response_subscription_status import APIResponseSubscriptionStatus
from .....types.api.v1.subscription_list_plans_response import SubscriptionListPlansResponse

__all__ = ["SubscriptionResource", "AsyncSubscriptionResource"]


class SubscriptionResource(SyncAPIResource):
    @cached_property
    def admin(self) -> AdminResource:
        return AdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return SubscriptionResourceWithStreamingResponse(self)

    def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseSubscriptionStatus:
        """获取用户订阅状态"""
        return self._get(
            "/api/v1/subscription/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseSubscriptionStatus,
        )

    def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseUsageStatistics:
        """获取用户使用统计"""
        return self._get(
            "/api/v1/subscription/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseUsageStatistics,
        )

    def list_plans(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionListPlansResponse:
        """现有订阅计划、用户订阅的内容、以及其他与用户订阅状态相关的信息"""
        return self._get(
            "/api/v1/subscription/plans",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListPlansResponse,
        )

    def verify(
        self,
        *,
        product_id: str,
        purchase_token: str,
        order_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionVerifyResponse:
        """
        Used by app to prove user has purchased a subscription

        Args:
          product_id: 产品 ID

          purchase_token: 购买令牌

          order_id: 订单 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/subscription/verify",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "purchase_token": purchase_token,
                    "order_id": order_id,
                },
                subscription_verify_params.SubscriptionVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionVerifyResponse,
        )

    def webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionWebhookResponse:
        """Google Play Developer Notifications webhook 处理订阅状态变化通知"""
        return self._post(
            "/api/v1/subscription/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionWebhookResponse,
        )


class AsyncSubscriptionResource(AsyncAPIResource):
    @cached_property
    def admin(self) -> AsyncAdminResource:
        return AsyncAdminResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return AsyncSubscriptionResourceWithStreamingResponse(self)

    async def get_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseSubscriptionStatus:
        """获取用户订阅状态"""
        return await self._get(
            "/api/v1/subscription/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseSubscriptionStatus,
        )

    async def get_usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponseUsageStatistics:
        """获取用户使用统计"""
        return await self._get(
            "/api/v1/subscription/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseUsageStatistics,
        )

    async def list_plans(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionListPlansResponse:
        """现有订阅计划、用户订阅的内容、以及其他与用户订阅状态相关的信息"""
        return await self._get(
            "/api/v1/subscription/plans",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListPlansResponse,
        )

    async def verify(
        self,
        *,
        product_id: str,
        purchase_token: str,
        order_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionVerifyResponse:
        """
        Used by app to prove user has purchased a subscription

        Args:
          product_id: 产品 ID

          purchase_token: 购买令牌

          order_id: 订单 ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/subscription/verify",
            body=await async_maybe_transform(
                {
                    "product_id": product_id,
                    "purchase_token": purchase_token,
                    "order_id": order_id,
                },
                subscription_verify_params.SubscriptionVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionVerifyResponse,
        )

    async def webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionWebhookResponse:
        """Google Play Developer Notifications webhook 处理订阅状态变化通知"""
        return await self._post(
            "/api/v1/subscription/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionWebhookResponse,
        )


class SubscriptionResourceWithRawResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.get_status = to_raw_response_wrapper(
            subscription.get_status,
        )
        self.get_usage = to_raw_response_wrapper(
            subscription.get_usage,
        )
        self.list_plans = to_raw_response_wrapper(
            subscription.list_plans,
        )
        self.verify = to_raw_response_wrapper(
            subscription.verify,
        )
        self.webhook = to_raw_response_wrapper(
            subscription.webhook,
        )

    @cached_property
    def admin(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self._subscription.admin)


class AsyncSubscriptionResourceWithRawResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.get_status = async_to_raw_response_wrapper(
            subscription.get_status,
        )
        self.get_usage = async_to_raw_response_wrapper(
            subscription.get_usage,
        )
        self.list_plans = async_to_raw_response_wrapper(
            subscription.list_plans,
        )
        self.verify = async_to_raw_response_wrapper(
            subscription.verify,
        )
        self.webhook = async_to_raw_response_wrapper(
            subscription.webhook,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self._subscription.admin)


class SubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.get_status = to_streamed_response_wrapper(
            subscription.get_status,
        )
        self.get_usage = to_streamed_response_wrapper(
            subscription.get_usage,
        )
        self.list_plans = to_streamed_response_wrapper(
            subscription.list_plans,
        )
        self.verify = to_streamed_response_wrapper(
            subscription.verify,
        )
        self.webhook = to_streamed_response_wrapper(
            subscription.webhook,
        )

    @cached_property
    def admin(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self._subscription.admin)


class AsyncSubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.get_status = async_to_streamed_response_wrapper(
            subscription.get_status,
        )
        self.get_usage = async_to_streamed_response_wrapper(
            subscription.get_usage,
        )
        self.list_plans = async_to_streamed_response_wrapper(
            subscription.list_plans,
        )
        self.verify = async_to_streamed_response_wrapper(
            subscription.verify,
        )
        self.webhook = async_to_streamed_response_wrapper(
            subscription.webhook,
        )

    @cached_property
    def admin(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self._subscription.admin)
