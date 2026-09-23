from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraint_violation import ConstraintViolation
from ...models.definition_definition_write_json_merge_patch import DefinitionDefinitionWriteJsonMergePatch
from ...models.definition_jsonhal_definition_read import DefinitionJsonhalDefinitionRead
from ...models.error import Error
from ...types import Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: DefinitionDefinitionWriteJsonMergePatch,
    accept: Union[Unset, str] = "application/hal+json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/definitions/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]:
    if response.status_code == 200:
        response_200 = DefinitionJsonhalDefinitionRead.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = ConstraintViolation.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]:
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
    body: DefinitionDefinitionWriteJsonMergePatch,
    accept: Union[Unset, str] = "application/hal+json",
) -> Response[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]:
    """Updates the definition resource.

     Updates the definition resource.

    Args:
        id (str):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (DefinitionDefinitionWriteJsonMergePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DefinitionDefinitionWriteJsonMergePatch,
    accept: Union[Unset, str] = "application/hal+json",
) -> Optional[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]:
    """Updates the definition resource.

     Updates the definition resource.

    Args:
        id (str):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (DefinitionDefinitionWriteJsonMergePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DefinitionDefinitionWriteJsonMergePatch,
    accept: Union[Unset, str] = "application/hal+json",
) -> Response[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]:
    """Updates the definition resource.

     Updates the definition resource.

    Args:
        id (str):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (DefinitionDefinitionWriteJsonMergePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DefinitionDefinitionWriteJsonMergePatch,
    accept: Union[Unset, str] = "application/hal+json",
) -> Optional[Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]]:
    """Updates the definition resource.

     Updates the definition resource.

    Args:
        id (str):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (DefinitionDefinitionWriteJsonMergePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConstraintViolation, DefinitionJsonhalDefinitionRead, Error]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            accept=accept,
        )
    ).parsed
