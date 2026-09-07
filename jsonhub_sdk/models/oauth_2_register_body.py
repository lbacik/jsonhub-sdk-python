from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.oauth_2_register_body_token_endpoint_auth_method import Oauth2RegisterBodyTokenEndpointAuthMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2RegisterBody")


@_attrs_define
class Oauth2RegisterBody:
    """
    Attributes:
        redirect_uris (list[str]):  Example: ['https://chat.openai.com/aip/g-abc/oauth/callback'].
        client_name (Union[Unset, str]):  Example: ChatGPT Idea Forge MCP.
        grant_types (Union[Unset, list[str]]):  Example: ['authorization_code'].
        response_types (Union[Unset, list[str]]):  Example: ['code'].
        scope (Union[Unset, str]):  Example: idea-forge-mcp.
        token_endpoint_auth_method (Union[Unset, Oauth2RegisterBodyTokenEndpointAuthMethod]):  Example: none.
    """

    redirect_uris: list[str]
    client_name: Union[Unset, str] = UNSET
    grant_types: Union[Unset, list[str]] = UNSET
    response_types: Union[Unset, list[str]] = UNSET
    scope: Union[Unset, str] = UNSET
    token_endpoint_auth_method: Union[Unset, Oauth2RegisterBodyTokenEndpointAuthMethod] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redirect_uris = self.redirect_uris

        client_name = self.client_name

        grant_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.grant_types, Unset):
            grant_types = self.grant_types

        response_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.response_types, Unset):
            response_types = self.response_types

        scope = self.scope

        token_endpoint_auth_method: Union[Unset, str] = UNSET
        if not isinstance(self.token_endpoint_auth_method, Unset):
            token_endpoint_auth_method = self.token_endpoint_auth_method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redirect_uris": redirect_uris,
            }
        )
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
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
        redirect_uris = cast(list[str], d.pop("redirect_uris"))

        client_name = d.pop("client_name", UNSET)

        grant_types = cast(list[str], d.pop("grant_types", UNSET))

        response_types = cast(list[str], d.pop("response_types", UNSET))

        scope = d.pop("scope", UNSET)

        _token_endpoint_auth_method = d.pop("token_endpoint_auth_method", UNSET)
        token_endpoint_auth_method: Union[Unset, Oauth2RegisterBodyTokenEndpointAuthMethod]
        if isinstance(_token_endpoint_auth_method, Unset):
            token_endpoint_auth_method = UNSET
        else:
            token_endpoint_auth_method = Oauth2RegisterBodyTokenEndpointAuthMethod(_token_endpoint_auth_method)

        oauth_2_register_body = cls(
            redirect_uris=redirect_uris,
            client_name=client_name,
            grant_types=grant_types,
            response_types=response_types,
            scope=scope,
            token_endpoint_auth_method=token_endpoint_auth_method,
        )

        oauth_2_register_body.additional_properties = d
        return oauth_2_register_body

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
