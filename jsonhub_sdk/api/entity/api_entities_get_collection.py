from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_entities_get_collection_response_200 import ApiEntitiesGetCollectionResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    qid: Union[Unset, str] = UNSET,
    private: Union[Unset, bool] = UNSET,
    owned: Union[Unset, bool] = UNSET,
    root: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    properties: Union[Unset, list[str]] = UNSET,
    definition: Union[Unset, str] = UNSET,
    parent: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = "application/hal+json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    params: dict[str, Any] = {}

    params["qid"] = qid

    params["private"] = private

    params["owned"] = owned

    params["root"] = root

    params["page"] = page

    params["limit"] = limit

    json_properties: Union[Unset, list[str]] = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties

    params["properties[]"] = json_properties

    params["definition"] = definition

    params["parent"] = parent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/entities",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiEntitiesGetCollectionResponse200]:
    if response.status_code == 200:
        response_200 = ApiEntitiesGetCollectionResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiEntitiesGetCollectionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    qid: Union[Unset, str] = UNSET,
    private: Union[Unset, bool] = UNSET,
    owned: Union[Unset, bool] = UNSET,
    root: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    properties: Union[Unset, list[str]] = UNSET,
    definition: Union[Unset, str] = UNSET,
    parent: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = "application/hal+json",
) -> Response[ApiEntitiesGetCollectionResponse200]:
    """Retrieves the collection of entity resources.

     Results are ordered deterministically, oldest first.

    Args:
        qid (Union[Unset, str]):
        private (Union[Unset, bool]):
        owned (Union[Unset, bool]):
        root (Union[Unset, bool]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 10.
        properties (Union[Unset, list[str]]):
        definition (Union[Unset, str]):
        parent (Union[Unset, str]):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEntitiesGetCollectionResponse200]
    """

    kwargs = _get_kwargs(
        qid=qid,
        private=private,
        owned=owned,
        root=root,
        page=page,
        limit=limit,
        properties=properties,
        definition=definition,
        parent=parent,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    qid: Union[Unset, str] = UNSET,
    private: Union[Unset, bool] = UNSET,
    owned: Union[Unset, bool] = UNSET,
    root: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    properties: Union[Unset, list[str]] = UNSET,
    definition: Union[Unset, str] = UNSET,
    parent: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = "application/hal+json",
) -> Optional[ApiEntitiesGetCollectionResponse200]:
    """Retrieves the collection of entity resources.

     Results are ordered deterministically, oldest first.

    Args:
        qid (Union[Unset, str]):
        private (Union[Unset, bool]):
        owned (Union[Unset, bool]):
        root (Union[Unset, bool]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 10.
        properties (Union[Unset, list[str]]):
        definition (Union[Unset, str]):
        parent (Union[Unset, str]):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEntitiesGetCollectionResponse200
    """

    return sync_detailed(
        client=client,
        qid=qid,
        private=private,
        owned=owned,
        root=root,
        page=page,
        limit=limit,
        properties=properties,
        definition=definition,
        parent=parent,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    qid: Union[Unset, str] = UNSET,
    private: Union[Unset, bool] = UNSET,
    owned: Union[Unset, bool] = UNSET,
    root: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    properties: Union[Unset, list[str]] = UNSET,
    definition: Union[Unset, str] = UNSET,
    parent: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = "application/hal+json",
) -> Response[ApiEntitiesGetCollectionResponse200]:
    """Retrieves the collection of entity resources.

     Results are ordered deterministically, oldest first.

    Args:
        qid (Union[Unset, str]):
        private (Union[Unset, bool]):
        owned (Union[Unset, bool]):
        root (Union[Unset, bool]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 10.
        properties (Union[Unset, list[str]]):
        definition (Union[Unset, str]):
        parent (Union[Unset, str]):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiEntitiesGetCollectionResponse200]
    """

    kwargs = _get_kwargs(
        qid=qid,
        private=private,
        owned=owned,
        root=root,
        page=page,
        limit=limit,
        properties=properties,
        definition=definition,
        parent=parent,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    qid: Union[Unset, str] = UNSET,
    private: Union[Unset, bool] = UNSET,
    owned: Union[Unset, bool] = UNSET,
    root: Union[Unset, bool] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 10,
    properties: Union[Unset, list[str]] = UNSET,
    definition: Union[Unset, str] = UNSET,
    parent: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = "application/hal+json",
) -> Optional[ApiEntitiesGetCollectionResponse200]:
    """Retrieves the collection of entity resources.

     Results are ordered deterministically, oldest first.

    Args:
        qid (Union[Unset, str]):
        private (Union[Unset, bool]):
        owned (Union[Unset, bool]):
        root (Union[Unset, bool]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 10.
        properties (Union[Unset, list[str]]):
        definition (Union[Unset, str]):
        parent (Union[Unset, str]):
        accept (Union[Unset, str]):  Default: 'application/hal+json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiEntitiesGetCollectionResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            qid=qid,
            private=private,
            owned=owned,
            root=root,
            page=page,
            limit=limit,
            properties=properties,
            definition=definition,
            parent=parent,
            accept=accept,
        )
    ).parsed
