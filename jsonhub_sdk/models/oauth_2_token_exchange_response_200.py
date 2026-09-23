from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2TokenExchangeResponse200")


@_attrs_define
class Oauth2TokenExchangeResponse200:
    """
    Attributes:
        access_token (Union[Unset, str]):
        token_type (Union[Unset, str]):  Example: Bearer.
        expires_in (Union[Unset, int]):  Example: 300.
        scope (Union[Unset, str]):  Example: jsonhub:entities:write jsonhub:definitions:write.
        refresh_token (Union[Unset, str]): Present when offline_access was granted.
        issued_token_type (Union[Unset, str]):  Example: urn:ietf:params:oauth:token-type:access_token.
    """

    access_token: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    scope: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    issued_token_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type

        expires_in = self.expires_in

        scope = self.scope

        refresh_token = self.refresh_token

        issued_token_type = self.issued_token_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if scope is not UNSET:
            field_dict["scope"] = scope
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if issued_token_type is not UNSET:
            field_dict["issued_token_type"] = issued_token_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        token_type = d.pop("token_type", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        scope = d.pop("scope", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        issued_token_type = d.pop("issued_token_type", UNSET)

        oauth_2_token_exchange_response_200 = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            scope=scope,
            refresh_token=refresh_token,
            issued_token_type=issued_token_type,
        )

        oauth_2_token_exchange_response_200.additional_properties = d
        return oauth_2_token_exchange_response_200

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
