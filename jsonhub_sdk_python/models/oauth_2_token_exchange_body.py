from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.oauth_2_token_exchange_body_audience import Oauth2TokenExchangeBodyAudience
from ..types import UNSET, Unset

T = TypeVar("T", bound="Oauth2TokenExchangeBody")


@_attrs_define
class Oauth2TokenExchangeBody:
    """
    Attributes:
        grant_type (str):  Example: urn:ietf:params:oauth:grant-type:token-exchange.
        client_id (str):
        subject_token (str):
        subject_token_type (str):  Example: urn:ietf:params:oauth:token-type:access_token.
        audience (Oauth2TokenExchangeBodyAudience):  Example: jsonhub-api.
        client_secret (Union[Unset, str]):
        subject_audience (Union[Unset, str]):  Example: idea-forge-mcp.
    """

    grant_type: str
    client_id: str
    subject_token: str
    subject_token_type: str
    audience: Oauth2TokenExchangeBodyAudience
    client_secret: Union[Unset, str] = UNSET
    subject_audience: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type

        client_id = self.client_id

        subject_token = self.subject_token

        subject_token_type = self.subject_token_type

        audience = self.audience.value

        client_secret = self.client_secret

        subject_audience = self.subject_audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "client_id": client_id,
                "subject_token": subject_token,
                "subject_token_type": subject_token_type,
                "audience": audience,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if subject_audience is not UNSET:
            field_dict["subject_audience"] = subject_audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = d.pop("grant_type")

        client_id = d.pop("client_id")

        subject_token = d.pop("subject_token")

        subject_token_type = d.pop("subject_token_type")

        audience = Oauth2TokenExchangeBodyAudience(d.pop("audience"))

        client_secret = d.pop("client_secret", UNSET)

        subject_audience = d.pop("subject_audience", UNSET)

        oauth_2_token_exchange_body = cls(
            grant_type=grant_type,
            client_id=client_id,
            subject_token=subject_token,
            subject_token_type=subject_token_type,
            audience=audience,
            client_secret=client_secret,
            subject_audience=subject_audience,
        )

        oauth_2_token_exchange_body.additional_properties = d
        return oauth_2_token_exchange_body

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
