# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

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
from .....types.api.v1.users import Gender, profile_update_params
from .....types.api.v1.users.gender import Gender
from .....types.api.v1.users.profile_update_response import ProfileUpdateResponse
from .....types.api.v1.users.profile_retrieve_response import ProfileRetrieveResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return ProfileResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """Get current user profile."""
        return self._get(
            "/api/v1/users/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def update(
        self,
        *,
        age_group: Optional[str] | Omit = omit,
        avatar: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        gender: Optional[Gender] | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        system_language: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Update current user profile.

        Args:
          gender: 性别

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/users/profile",
            body=maybe_transform(
                {
                    "age_group": age_group,
                    "avatar": avatar,
                    "description": description,
                    "email": email,
                    "gender": gender,
                    "nickname": nickname,
                    "phone": phone,
                    "system_language": system_language,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NascentCore/inty-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NascentCore/inty-python#with_streaming_response
        """
        return AsyncProfileResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """Get current user profile."""
        return await self._get(
            "/api/v1/users/profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def update(
        self,
        *,
        age_group: Optional[str] | Omit = omit,
        avatar: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        gender: Optional[Gender] | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        system_language: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """
        Update current user profile.

        Args:
          gender: 性别

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/users/profile",
            body=await async_maybe_transform(
                {
                    "age_group": age_group,
                    "avatar": avatar,
                    "description": description,
                    "email": email,
                    "gender": gender,
                    "nickname": nickname,
                    "phone": phone,
                    "system_language": system_language,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profile.update,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_raw_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profile.update,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.retrieve = to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profile.update,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.retrieve = async_to_streamed_response_wrapper(
            profile.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profile.update,
        )
