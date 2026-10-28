from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraint_violation import ConstraintViolation
from ...models.error import Error
from ...models.user import User
from ...models.user_user_activation import UserUserActivation
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: UserUserActivation,
    accept: Union[Unset, str] = "application/json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/activation",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConstraintViolation, Error, User]]:
    if response.status_code == 204:
        response_204 = User.from_dict(response.json())

        return response_204

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 410:
        response_410 = cast(Any, None)
        return response_410

    if response.status_code == 422:
        response_422 = ConstraintViolation.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ConstraintViolation, Error, User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserActivation,
    accept: Union[Unset, str] = "application/json",
) -> Response[Union[Any, ConstraintViolation, Error, User]]:
    """Activate a user

     This endpoint activates the user account using the token sent by email.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (UserUserActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstraintViolation, Error, User]]
    """

    kwargs = _get_kwargs(
        body=body,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserActivation,
    accept: Union[Unset, str] = "application/json",
) -> Optional[Union[Any, ConstraintViolation, Error, User]]:
    """Activate a user

     This endpoint activates the user account using the token sent by email.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (UserUserActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstraintViolation, Error, User]
    """

    return sync_detailed(
        client=client,
        body=body,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserActivation,
    accept: Union[Unset, str] = "application/json",
) -> Response[Union[Any, ConstraintViolation, Error, User]]:
    """Activate a user

     This endpoint activates the user account using the token sent by email.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (UserUserActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstraintViolation, Error, User]]
    """

    kwargs = _get_kwargs(
        body=body,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserActivation,
    accept: Union[Unset, str] = "application/json",
) -> Optional[Union[Any, ConstraintViolation, Error, User]]:
    """Activate a user

     This endpoint activates the user account using the token sent by email.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (UserUserActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstraintViolation, Error, User]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept=accept,
        )
    ).parsed
