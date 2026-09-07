from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraint_violation import ConstraintViolation
from ...models.error import Error
from ...models.user_jsonhal_user_empty import UserJsonhalUserEmpty
from ...models.user_user_update_json_merge_patch import UserUserUpdateJsonMergePatch
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UserUserUpdateJsonMergePatch,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/users/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]:
    if response.status_code == 200:
        response_200 = UserJsonhalUserEmpty.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ConstraintViolation.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserUpdateJsonMergePatch,
) -> Response[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]:
    """Updates the user resource.

     Updates the user resource.

    Args:
        id (str):
        body (UserUserUpdateJsonMergePatch): Change user password

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserUpdateJsonMergePatch,
) -> Optional[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]:
    """Updates the user resource.

     Updates the user resource.

    Args:
        id (str):
        body (UserUserUpdateJsonMergePatch): Change user password

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, Error, UserJsonhalUserEmpty]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserUpdateJsonMergePatch,
) -> Response[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]:
    """Updates the user resource.

     Updates the user resource.

    Args:
        id (str):
        body (UserUserUpdateJsonMergePatch): Change user password

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserUserUpdateJsonMergePatch,
) -> Optional[Union[ConstraintViolation, Error, UserJsonhalUserEmpty]]:
    """Updates the user resource.

     Updates the user resource.

    Args:
        id (str):
        body (UserUserUpdateJsonMergePatch): Change user password

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, Error, UserJsonhalUserEmpty]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
