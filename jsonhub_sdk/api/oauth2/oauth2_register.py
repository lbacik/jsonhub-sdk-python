from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oauth_2_register_body import Oauth2RegisterBody
from ...models.oauth_2_register_response_201 import Oauth2RegisterResponse201
from ...models.oauth_2_register_response_400 import Oauth2RegisterResponse400
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: Oauth2RegisterBody,
    accept: Union[Unset, str] = "application/json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/oauth2/register",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]:
    if response.status_code == 201:
        response_201 = Oauth2RegisterResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Oauth2RegisterResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2RegisterBody,
    accept: Union[Unset, str] = "application/json",
) -> Response[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]:
    """Register OAuth client

     Controlled Dynamic Client Registration. Redirect URIs must be HTTPS, except HTTP localhost/127.0.0.1
    for development.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RegisterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]
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
    body: Oauth2RegisterBody,
    accept: Union[Unset, str] = "application/json",
) -> Optional[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]:
    """Register OAuth client

     Controlled Dynamic Client Registration. Redirect URIs must be HTTPS, except HTTP localhost/127.0.0.1
    for development.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RegisterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]
    """

    return sync_detailed(
        client=client,
        body=body,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Oauth2RegisterBody,
    accept: Union[Unset, str] = "application/json",
) -> Response[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]:
    """Register OAuth client

     Controlled Dynamic Client Registration. Redirect URIs must be HTTPS, except HTTP localhost/127.0.0.1
    for development.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RegisterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]
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
    body: Oauth2RegisterBody,
    accept: Union[Unset, str] = "application/json",
) -> Optional[Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]]:
    """Register OAuth client

     Controlled Dynamic Client Registration. Redirect URIs must be HTTPS, except HTTP localhost/127.0.0.1
    for development.

    Args:
        accept (Union[Unset, str]):  Default: 'application/json'.
        body (Oauth2RegisterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Oauth2RegisterResponse201, Oauth2RegisterResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept=accept,
        )
    ).parsed
