from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2RegisterResponse201")


@_attrs_define
class Oauth2RegisterResponse201:
    """
    Attributes:
        client_id (Union[Unset, str]):  Example: jh_client_id.
        client_secret (Union[Unset, str]): Only returned for confidential clients.
        redirect_uris (Union[Unset, list[str]]):
        grant_types (Union[Unset, list[str]]):  Example: ['authorization_code'].
        response_types (Union[Unset, list[str]]):  Example: ['code'].
        scope (Union[Unset, str]):  Example: mcp jsonhub:entities:write.
        token_endpoint_auth_method (Union[Unset, str]):  Example: none.
    """

    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    redirect_uris: Union[Unset, list[str]] = UNSET
    grant_types: Union[Unset, list[str]] = UNSET
    response_types: Union[Unset, list[str]] = UNSET
    scope: Union[Unset, str] = UNSET
    token_endpoint_auth_method: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        redirect_uris: Union[Unset, list[str]] = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris

        grant_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.grant_types, Unset):
            grant_types = self.grant_types

        response_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.response_types, Unset):
            response_types = self.response_types

        scope = self.scope

        token_endpoint_auth_method = self.token_endpoint_auth_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris
        if grant_types is not UNSET:
            field_dict["grant_types"] = grant_types
        if response_types is not UNSET:
            field_dict["response_types"] = response_types
        if scope is not UNSET:
            field_dict["scope"] = scope
        if token_endpoint_auth_method is not UNSET:
            field_dict["token_endpoint_auth_method"] = token_endpoint_auth_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        redirect_uris = cast(list[str], d.pop("redirect_uris", UNSET))

        grant_types = cast(list[str], d.pop("grant_types", UNSET))

        response_types = cast(list[str], d.pop("response_types", UNSET))

        scope = d.pop("scope", UNSET)

        token_endpoint_auth_method = d.pop("token_endpoint_auth_method", UNSET)

        oauth_2_register_response_201 = cls(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uris=redirect_uris,
            grant_types=grant_types,
            response_types=response_types,
            scope=scope,
            token_endpoint_auth_method=token_endpoint_auth_method,
        )

        oauth_2_register_response_201.additional_properties = d
        return oauth_2_register_response_201

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
