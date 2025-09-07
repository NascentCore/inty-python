# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .device import (
    DeviceResource,
    AsyncDeviceResource,
    DeviceResourceWithRawResponse,
    AsyncDeviceResourceWithRawResponse,
    DeviceResourceWithStreamingResponse,
    AsyncDeviceResourceWithStreamingResponse,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from .deletion import (
    DeletionResource,
    AsyncDeletionResource,
    DeletionResourceWithRawResponse,
    AsyncDeletionResourceWithRawResponse,
    DeletionResourceWithStreamingResponse,
    AsyncDeletionResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1 import user_delete_account_params
from .....types.api.v1.user_delete_account_response import UserDeleteAccountResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def device(self) -> DeviceResource:
        return DeviceResource(self._client)

    @cached_property
    def deletion(self) -> DeletionResource:
        return DeletionResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def delete_account(
        self,
        *,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteAccountResponse:
        """
        删除用户账户

        Args:
          reason: 删除原因

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/users/delete-account",
            body=maybe_transform({"reason": reason}, user_delete_account_params.UserDeleteAccountParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteAccountResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def device(self) -> AsyncDeviceResource:
        return AsyncDeviceResource(self._client)

    @cached_property
    def deletion(self) -> AsyncDeletionResource:
        return AsyncDeletionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inty-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def delete_account(
        self,
        *,
        reason: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserDeleteAccountResponse:
        """
        删除用户账户

        Args:
          reason: 删除原因

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/users/delete-account",
            body=await async_maybe_transform({"reason": reason}, user_delete_account_params.UserDeleteAccountParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteAccountResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete_account = to_raw_response_wrapper(
            users.delete_account,
        )

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._users.profile)

    @cached_property
    def device(self) -> DeviceResourceWithRawResponse:
        return DeviceResourceWithRawResponse(self._users.device)

    @cached_property
    def deletion(self) -> DeletionResourceWithRawResponse:
        return DeletionResourceWithRawResponse(self._users.deletion)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete_account = async_to_raw_response_wrapper(
            users.delete_account,
        )

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._users.profile)

    @cached_property
    def device(self) -> AsyncDeviceResourceWithRawResponse:
        return AsyncDeviceResourceWithRawResponse(self._users.device)

    @cached_property
    def deletion(self) -> AsyncDeletionResourceWithRawResponse:
        return AsyncDeletionResourceWithRawResponse(self._users.deletion)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete_account = to_streamed_response_wrapper(
            users.delete_account,
        )

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._users.profile)

    @cached_property
    def device(self) -> DeviceResourceWithStreamingResponse:
        return DeviceResourceWithStreamingResponse(self._users.device)

    @cached_property
    def deletion(self) -> DeletionResourceWithStreamingResponse:
        return DeletionResourceWithStreamingResponse(self._users.deletion)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete_account = async_to_streamed_response_wrapper(
            users.delete_account,
        )

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._users.profile)

    @cached_property
    def device(self) -> AsyncDeviceResourceWithStreamingResponse:
        return AsyncDeviceResourceWithStreamingResponse(self._users.device)

    @cached_property
    def deletion(self) -> AsyncDeletionResourceWithStreamingResponse:
        return AsyncDeletionResourceWithStreamingResponse(self._users.deletion)
