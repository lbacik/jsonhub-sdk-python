from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.oauth_2_token_body_type_1_grant_type import Oauth2TokenBodyType1GrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2TokenBodyType1")


@_attrs_define
class Oauth2TokenBodyType1:
    """
    Attributes:
        grant_type (Oauth2TokenBodyType1GrantType):  Example: refresh_token.
        refresh_token (str):
        client_id (str):
        scope (Union[Unset, str]): Optional subset of the original grant.
    """

    grant_type: Oauth2TokenBodyType1GrantType
    refresh_token: str
    client_id: str
    scope: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        refresh_token = self.refresh_token

        client_id = self.client_id

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "refresh_token": refresh_token,
                "client_id": client_id,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = Oauth2TokenBodyType1GrantType(d.pop("grant_type"))

        refresh_token = d.pop("refresh_token")

        client_id = d.pop("client_id")

        scope = d.pop("scope", UNSET)

        oauth_2_token_body_type_1 = cls(
            grant_type=grant_type,
            refresh_token=refresh_token,
            client_id=client_id,
            scope=scope,
        )

        oauth_2_token_body_type_1.additional_properties = d
        return oauth_2_token_body_type_1

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
