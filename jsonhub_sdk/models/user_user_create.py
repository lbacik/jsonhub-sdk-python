from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUserCreate")


@_attrs_define
class UserUserCreate:
    """Create user

    Attributes:
        email (Union[None, str]):
        password (Union[None, str]):
        activation_url (Union[None, Unset, str]):
    """

    email: Union[None, str]
    password: Union[None, str]
    activation_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[None, str]
        email = self.email

        password: Union[None, str]
        password = self.password

        activation_url: Union[None, Unset, str]
        if isinstance(self.activation_url, Unset):
            activation_url = UNSET
        else:
            activation_url = self.activation_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
            }
        )
        if activation_url is not UNSET:
            field_dict["activationUrl"] = activation_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop("password"))

        def _parse_activation_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activation_url = _parse_activation_url(d.pop("activationUrl", UNSET))

        user_user_create = cls(
            email=email,
            password=password,
            activation_url=activation_url,
        )

        user_user_create.additional_properties = d
        return user_user_create

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
