from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oauth_2_authorize_code_challenge_method import Oauth2AuthorizeCodeChallengeMethod
from ...models.oauth_2_authorize_response_type import Oauth2AuthorizeResponseType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    response_type: Oauth2AuthorizeResponseType,
    client_id: str,
    redirect_uri: str,
    scope: str,
    state: str,
    code_challenge: str,
    code_challenge_method: Oauth2AuthorizeCodeChallengeMethod,
    resource: Union[Unset, str] = UNSET,
    audience: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_response_type = response_type.value
    params["response_type"] = json_response_type

    params["client_id"] = client_id

    params["redirect_uri"] = redirect_uri

    params["scope"] = scope

    params["state"] = state

    params["code_challenge"] = code_challenge

    json_code_challenge_method = code_challenge_method.value
    params["code_challenge_method"] = json_code_challenge_method

    params["resource"] = resource

    params["audience"] = audience

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/oauth2/authorize",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 302:
        return None

    if response.status_code == 400:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    response_type: Oauth2AuthorizeResponseType,
    client_id: str,
    redirect_uri: str,
    scope: str,
    state: str,
    code_challenge: str,
    code_challenge_method: Oauth2AuthorizeCodeChallengeMethod,
    resource: Union[Unset, str] = UNSET,
    audience: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Start OAuth authorization

     Browser endpoint for Authorization Code with PKCE. Requires a JsonHub session and consent before
    issuing an authorization code.

    Args:
        response_type (Oauth2AuthorizeResponseType):  Example: code.
        client_id (str):  Example: jh_client_id.
        redirect_uri (str):  Example: https://chat.openai.com/aip/g-abc/oauth/callback.
        scope (str):  Example: idea-forge-mcp.
        state (str):  Example: client-csrf-state.
        code_challenge (str):
        code_challenge_method (Oauth2AuthorizeCodeChallengeMethod):  Example: S256.
        resource (Union[Unset, str]):  Example: idea-forge-mcp.
        audience (Union[Unset, str]):  Example: idea-forge-mcp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        resource=resource,
        audience=audience,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    response_type: Oauth2AuthorizeResponseType,
    client_id: str,
    redirect_uri: str,
    scope: str,
    state: str,
    code_challenge: str,
    code_challenge_method: Oauth2AuthorizeCodeChallengeMethod,
    resource: Union[Unset, str] = UNSET,
    audience: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Start OAuth authorization

     Browser endpoint for Authorization Code with PKCE. Requires a JsonHub session and consent before
    issuing an authorization code.

    Args:
        response_type (Oauth2AuthorizeResponseType):  Example: code.
        client_id (str):  Example: jh_client_id.
        redirect_uri (str):  Example: https://chat.openai.com/aip/g-abc/oauth/callback.
        scope (str):  Example: idea-forge-mcp.
        state (str):  Example: client-csrf-state.
        code_challenge (str):
        code_challenge_method (Oauth2AuthorizeCodeChallengeMethod):  Example: S256.
        resource (Union[Unset, str]):  Example: idea-forge-mcp.
        audience (Union[Unset, str]):  Example: idea-forge-mcp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope,
        state=state,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        resource=resource,
        audience=audience,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
