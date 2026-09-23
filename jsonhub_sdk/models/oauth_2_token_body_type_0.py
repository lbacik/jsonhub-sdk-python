from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.oauth_2_token_body_type_0_grant_type import Oauth2TokenBodyType0GrantType

T = TypeVar("T", bound="Oauth2TokenBodyType0")


@_attrs_define
class Oauth2TokenBodyType0:
    """
    Attributes:
        grant_type (Oauth2TokenBodyType0GrantType):  Example: authorization_code.
        code (str):
        redirect_uri (str):
        client_id (str):
        code_verifier (str):
    """

    grant_type: Oauth2TokenBodyType0GrantType
    code: str
    redirect_uri: str
    client_id: str
    code_verifier: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        code = self.code

        redirect_uri = self.redirect_uri

        client_id = self.client_id

        code_verifier = self.code_verifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": redirect_uri,
                "client_id": client_id,
                "code_verifier": code_verifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = Oauth2TokenBodyType0GrantType(d.pop("grant_type"))

        code = d.pop("code")

        redirect_uri = d.pop("redirect_uri")

        client_id = d.pop("client_id")

        code_verifier = d.pop("code_verifier")

        oauth_2_token_body_type_0 = cls(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            code_verifier=code_verifier,
        )

        oauth_2_token_body_type_0.additional_properties = d
        return oauth_2_token_body_type_0

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
