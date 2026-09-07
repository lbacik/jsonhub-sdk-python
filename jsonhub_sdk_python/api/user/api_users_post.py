from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraint_violation import ConstraintViolation
from ...models.error import Error
from ...models.user_jsonhal_user_read import UserJsonhalUserRead
from ...models.user_user_create import UserUserCreate
from ...types import Response


def _get_kwargs(
    *,
    body: UserUserCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConstraintViolation, Error, UserJsonhalUserRead]]:
    if response.status_code == 201:
        response_201 = UserJsonhalUserRead.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = ConstraintViolation.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConstraintViolation, Error, UserJsonhalUserRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserCreate,
) -> Response[Union[ConstraintViolation, Error, UserJsonhalUserRead]]:
    """Creates a user resource.

     Creates a user resource.

    Args:
        body (UserUserCreate): Create user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, Error, UserJsonhalUserRead]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserCreate,
) -> Optional[Union[ConstraintViolation, Error, UserJsonhalUserRead]]:
    """Creates a user resource.

     Creates a user resource.

    Args:
        body (UserUserCreate): Create user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, Error, UserJsonhalUserRead]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserCreate,
) -> Response[Union[ConstraintViolation, Error, UserJsonhalUserRead]]:
    """Creates a user resource.

     Creates a user resource.

    Args:
        body (UserUserCreate): Create user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, Error, UserJsonhalUserRead]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserCreate,
) -> Optional[Union[ConstraintViolation, Error, UserJsonhalUserRead]]:
    """Creates a user resource.

     Creates a user resource.

    Args:
        body (UserUserCreate): Create user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, Error, UserJsonhalUserRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
