from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oauth_2_revoke_body import Oauth2RevokeBody
from ...models.oauth_2_revoke_response_200 import Oauth2RevokeResponse200
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: Oauth2RevokeBody,
    accept: Union[Unset, str] = "application/json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oauth2/revoke",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Oauth2RevokeResponse200]:
    if response.status_code == 200:
        response_200 = Oauth2RevokeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Oauth2RevokeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2RevokeBody,
    accept: Union[Unset, str] = "application/json",
) -> Response[Oauth2RevokeResponse200]:
    """Revoke OAuth consent

     Revokes the matching consent grant when the token can be validated. Already-issued short-lived JWTs
    remain valid until expiry.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RevokeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Oauth2RevokeResponse200]
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
    body: Oauth2RevokeBody,
    accept: Union[Unset, str] = "application/json",
) -> Optional[Oauth2RevokeResponse200]:
    """Revoke OAuth consent

     Revokes the matching consent grant when the token can be validated. Already-issued short-lived JWTs
    remain valid until expiry.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RevokeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Oauth2RevokeResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2RevokeBody,
    accept: Union[Unset, str] = "application/json",
) -> Response[Oauth2RevokeResponse200]:
    """Revoke OAuth consent

     Revokes the matching consent grant when the token can be validated. Already-issued short-lived JWTs
    remain valid until expiry.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RevokeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Oauth2RevokeResponse200]
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
    body: Oauth2RevokeBody,
    accept: Union[Unset, str] = "application/json",
) -> Optional[Oauth2RevokeResponse200]:
    """Revoke OAuth consent

     Revokes the matching consent grant when the token can be validated. Already-issued short-lived JWTs
    remain valid until expiry.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RevokeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Oauth2RevokeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept=accept,
        )
    ).parsed
