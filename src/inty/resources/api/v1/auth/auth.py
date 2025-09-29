# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .google import (
    GoogleResource,
    AsyncGoogleResource,
    GoogleResourceWithRawResponse,
    AsyncGoogleResourceWithRawResponse,
    GoogleResourceWithStreamingResponse,
    AsyncGoogleResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.api.v1 import auth_create_guest_params
from .....types.api.v1.auth_create_guest_response import AuthCreateGuestResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def google(self) -> GoogleResource:
        return GoogleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def create_guest(
        self,
        *,
        age_group: Optional[str] | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        system_language: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthCreateGuestResponse:
        """
        创建游客账号

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/auth/guest",
            body=maybe_transform(
                {
                    "age_group": age_group,
                    "device_id": device_id,
                    "request_id": request_id,
                    "system_language": system_language,
                },
                auth_create_guest_params.AuthCreateGuestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthCreateGuestResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def google(self) -> AsyncGoogleResource:
        return AsyncGoogleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def create_guest(
        self,
        *,
        age_group: Optional[str] | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        request_id: Optional[str] | Omit = omit,
        system_language: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthCreateGuestResponse:
        """
        创建游客账号

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/auth/guest",
            body=await async_maybe_transform(
                {
                    "age_group": age_group,
                    "device_id": device_id,
                    "request_id": request_id,
                    "system_language": system_language,
                },
                auth_create_guest_params.AuthCreateGuestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthCreateGuestResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.create_guest = to_raw_response_wrapper(
            auth.create_guest,
        )

    @cached_property
    def google(self) -> GoogleResourceWithRawResponse:
        return GoogleResourceWithRawResponse(self._auth.google)


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.create_guest = async_to_raw_response_wrapper(
            auth.create_guest,
        )

    @cached_property
    def google(self) -> AsyncGoogleResourceWithRawResponse:
        return AsyncGoogleResourceWithRawResponse(self._auth.google)


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.create_guest = to_streamed_response_wrapper(
            auth.create_guest,
        )

    @cached_property
    def google(self) -> GoogleResourceWithStreamingResponse:
        return GoogleResourceWithStreamingResponse(self._auth.google)


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.create_guest = async_to_streamed_response_wrapper(
            auth.create_guest,
        )

    @cached_property
    def google(self) -> AsyncGoogleResourceWithStreamingResponse:
        return AsyncGoogleResourceWithStreamingResponse(self._auth.google)
