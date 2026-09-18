from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraint_violation import ConstraintViolation
from ...models.entity_entity_create import EntityEntityCreate
from ...models.entity_jsonhal_entity_read_entity_read_parent import EntityJsonhalEntityReadEntityReadParent
from ...models.error import Error
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: EntityEntityCreate,
    accept: Union[Unset, str] = "application/hal+json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/entities",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]:
    if response.status_code == 201:
        response_201 = EntityJsonhalEntityReadEntityReadParent.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = ConstraintViolation.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EntityEntityCreate,
    accept: Union[Unset, str] = "application/hal+json",
) -> Response[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]:
    """Creates a entity resource.

     Creates a entity resource.

    Args:
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (EntityEntityCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]
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
    body: EntityEntityCreate,
    accept: Union[Unset, str] = "application/hal+json",
) -> Optional[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]:
    """Creates a entity resource.

     Creates a entity resource.

    Args:
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (EntityEntityCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: EntityEntityCreate,
    accept: Union[Unset, str] = "application/hal+json",
) -> Response[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]:
    """Creates a entity resource.

     Creates a entity resource.

    Args:
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (EntityEntityCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]
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
    body: EntityEntityCreate,
    accept: Union[Unset, str] = "application/hal+json",
) -> Optional[Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]]:
    """Creates a entity resource.

     Creates a entity resource.

    Args:
        accept (Union[Unset, str]):  Default: 'application/hal+json'.
        body (EntityEntityCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConstraintViolation, EntityJsonhalEntityReadEntityReadParent, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            accept=accept,
        )
    ).parsed
