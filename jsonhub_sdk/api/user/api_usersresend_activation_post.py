from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraint_violation import ConstraintViolation
from ...models.error import Error
from ...models.user_jsonhal import UserJsonhal
from ...models.user_user_resend_activation import UserUserResendActivation
from ...types import Response


def _get_kwargs(
    *,
    body: UserUserResendActivation,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/resend-activation",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConstraintViolation, Error, UserJsonhal]]:
    if response.status_code == 204:
        response_204 = UserJsonhal.from_dict(response.json())

        return response_204

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
) -> Response[Union[ConstraintViolation, Error, UserJsonhal]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserResendActivation,
) -> Response[Union[ConstraintViolation, Error, UserJsonhal]]:
    """Resend activation email

     This endpoint resends the activation email to the user.

    Args:
        body (UserUserResendActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, Error, UserJsonhal]]
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
    body: UserUserResendActivation,
) -> Optional[Union[ConstraintViolation, Error, UserJsonhal]]:
    """Resend activation email

     This endpoint resends the activation email to the user.

    Args:
        body (UserUserResendActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, Error, UserJsonhal]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserResendActivation,
) -> Response[Union[ConstraintViolation, Error, UserJsonhal]]:
    """Resend activation email

     This endpoint resends the activation email to the user.

    Args:
        body (UserUserResendActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, Error, UserJsonhal]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserResendActivation,
) -> Optional[Union[ConstraintViolation, Error, UserJsonhal]]:
    """Resend activation email

     This endpoint resends the activation email to the user.

    Args:
        body (UserUserResendActivation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, Error, UserJsonhal]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
