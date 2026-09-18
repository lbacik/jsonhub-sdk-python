from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oauth_2_jwks_response_200 import Oauth2JwksResponse200
from ...types import Response, Unset


def _get_kwargs(
    *,
    accept: Union[Unset, str] = "application/json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth2/jwks",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Oauth2JwksResponse200]:
    if response.status_code == 200:
        response_200 = Oauth2JwksResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Oauth2JwksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    accept: Union[Unset, str] = "application/json",
) -> Response[Oauth2JwksResponse200]:
    """Get OAuth signing keys

     Publishes public RSA keys for local JWT validation by MCP and other resource servers.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Oauth2JwksResponse200]
    """

    kwargs = _get_kwargs(
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    accept: Union[Unset, str] = "application/json",
) -> Optional[Oauth2JwksResponse200]:
    """Get OAuth signing keys

     Publishes public RSA keys for local JWT validation by MCP and other resource servers.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Oauth2JwksResponse200
    """

    return sync_detailed(
        client=client,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    accept: Union[Unset, str] = "application/json",
) -> Response[Oauth2JwksResponse200]:
    """Get OAuth signing keys

     Publishes public RSA keys for local JWT validation by MCP and other resource servers.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Oauth2JwksResponse200]
    """

    kwargs = _get_kwargs(
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    accept: Union[Unset, str] = "application/json",
) -> Optional[Oauth2JwksResponse200]:
    """Get OAuth signing keys

     Publishes public RSA keys for local JWT validation by MCP and other resource servers.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Oauth2JwksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            accept=accept,
        )
    ).parsed
