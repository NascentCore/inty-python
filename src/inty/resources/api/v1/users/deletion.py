# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.users.deletion_check_eligibility_response import DeletionCheckEligibilityResponse

__all__ = ["DeletionResource", "AsyncDeletionResource"]


class DeletionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeletionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return DeletionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeletionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return DeletionResourceWithStreamingResponse(self)

    def check_eligibility(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletionCheckEligibilityResponse:
        """检查用户是否可以删除账户"""
        return self._get(
            "/api/v1/users/deletion/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletionCheckEligibilityResponse,
        )


class AsyncDeletionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeletionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeletionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeletionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return AsyncDeletionResourceWithStreamingResponse(self)

    async def check_eligibility(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeletionCheckEligibilityResponse:
        """检查用户是否可以删除账户"""
        return await self._get(
            "/api/v1/users/deletion/check",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletionCheckEligibilityResponse,
        )


class DeletionResourceWithRawResponse:
    def __init__(self, deletion: DeletionResource) -> None:
        self._deletion = deletion

        self.check_eligibility = to_raw_response_wrapper(
            deletion.check_eligibility,
        )


class AsyncDeletionResourceWithRawResponse:
    def __init__(self, deletion: AsyncDeletionResource) -> None:
        self._deletion = deletion

        self.check_eligibility = async_to_raw_response_wrapper(
            deletion.check_eligibility,
        )


class DeletionResourceWithStreamingResponse:
    def __init__(self, deletion: DeletionResource) -> None:
        self._deletion = deletion

        self.check_eligibility = to_streamed_response_wrapper(
            deletion.check_eligibility,
        )


class AsyncDeletionResourceWithStreamingResponse:
    def __init__(self, deletion: AsyncDeletionResource) -> None:
        self._deletion = deletion

        self.check_eligibility = async_to_streamed_response_wrapper(
            deletion.check_eligibility,
        )
