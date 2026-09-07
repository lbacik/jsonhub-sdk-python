from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2RevokeBody")


@_attrs_define
class Oauth2RevokeBody:
    """
    Attributes:
        token (str):
        client_id (str):
        client_secret (Union[Unset, str]):
        audience (Union[Unset, str]):  Example: idea-forge-mcp.
    """

    token: str
    client_id: str
    client_secret: Union[Unset, str] = UNSET
    audience: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        client_id = self.client_id

        client_secret = self.client_secret

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "client_id": client_id,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret", UNSET)

        audience = d.pop("audience", UNSET)

        oauth_2_revoke_body = cls(
            token=token,
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
        )

        oauth_2_revoke_body.additional_properties = d
        return oauth_2_revoke_body

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
