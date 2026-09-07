from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oauth_2_token_exchange_body import Oauth2TokenExchangeBody
from ...models.oauth_2_token_exchange_response_200 import Oauth2TokenExchangeResponse200
from ...models.oauth_2_token_exchange_response_400 import Oauth2TokenExchangeResponse400
from ...models.oauth_2_token_exchange_response_401 import Oauth2TokenExchangeResponse401
from ...models.oauth_2_token_exchange_response_403 import Oauth2TokenExchangeResponse403
from ...types import Response


def _get_kwargs(
    *,
    body: Oauth2TokenExchangeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oauth2/token-exchange",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Oauth2TokenExchangeResponse200,
        Oauth2TokenExchangeResponse400,
        Oauth2TokenExchangeResponse401,
        Oauth2TokenExchangeResponse403,
    ]
]:
    if response.status_code == 200:
        response_200 = Oauth2TokenExchangeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Oauth2TokenExchangeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Oauth2TokenExchangeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Oauth2TokenExchangeResponse403.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Oauth2TokenExchangeResponse200,
        Oauth2TokenExchangeResponse400,
        Oauth2TokenExchangeResponse401,
        Oauth2TokenExchangeResponse403,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2TokenExchangeBody,
) -> Response[
    Union[
        Oauth2TokenExchangeResponse200,
        Oauth2TokenExchangeResponse400,
        Oauth2TokenExchangeResponse401,
        Oauth2TokenExchangeResponse403,
    ]
]:
    """Exchange MCP token for JsonHub API token

     OAuth 2.0 Token Exchange style endpoint. The MCP backend authenticates as a confidential client and
    exchanges an MCP-audience subject token for a short-lived downstream token with aud=jsonhub-api.

    Args:
        body (Oauth2TokenExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Oauth2TokenExchangeResponse200, Oauth2TokenExchangeResponse400, Oauth2TokenExchangeResponse401, Oauth2TokenExchangeResponse403]]
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
    body: Oauth2TokenExchangeBody,
) -> Optional[
    Union[
        Oauth2TokenExchangeResponse200,
        Oauth2TokenExchangeResponse400,
        Oauth2TokenExchangeResponse401,
        Oauth2TokenExchangeResponse403,
    ]
]:
    """Exchange MCP token for JsonHub API token

     OAuth 2.0 Token Exchange style endpoint. The MCP backend authenticates as a confidential client and
    exchanges an MCP-audience subject token for a short-lived downstream token with aud=jsonhub-api.

    Args:
        body (Oauth2TokenExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Oauth2TokenExchangeResponse200, Oauth2TokenExchangeResponse400, Oauth2TokenExchangeResponse401, Oauth2TokenExchangeResponse403]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2TokenExchangeBody,
) -> Response[
    Union[
        Oauth2TokenExchangeResponse200,
        Oauth2TokenExchangeResponse400,
        Oauth2TokenExchangeResponse401,
        Oauth2TokenExchangeResponse403,
    ]
]:
    """Exchange MCP token for JsonHub API token

     OAuth 2.0 Token Exchange style endpoint. The MCP backend authenticates as a confidential client and
    exchanges an MCP-audience subject token for a short-lived downstream token with aud=jsonhub-api.

    Args:
        body (Oauth2TokenExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Oauth2TokenExchangeResponse200, Oauth2TokenExchangeResponse400, Oauth2TokenExchangeResponse401, Oauth2TokenExchangeResponse403]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2TokenExchangeBody,
) -> Optional[
    Union[
        Oauth2TokenExchangeResponse200,
        Oauth2TokenExchangeResponse400,
        Oauth2TokenExchangeResponse401,
        Oauth2TokenExchangeResponse403,
    ]
]:
    """Exchange MCP token for JsonHub API token

     OAuth 2.0 Token Exchange style endpoint. The MCP backend authenticates as a confidential client and
    exchanges an MCP-audience subject token for a short-lived downstream token with aud=jsonhub-api.

    Args:
        body (Oauth2TokenExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Oauth2TokenExchangeResponse200, Oauth2TokenExchangeResponse400, Oauth2TokenExchangeResponse401, Oauth2TokenExchangeResponse403]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
