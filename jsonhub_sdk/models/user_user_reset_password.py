from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserUserResetPassword")


@_attrs_define
class UserUserResetPassword:
    """
    Attributes:
        password (Union[None, str]):
        token (Union[None, str]):
    """

    password: Union[None, str]
    token: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password: Union[None, str]
        password = self.password

        token: Union[None, str]
        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop("password"))

        def _parse_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        token = _parse_token(d.pop("token"))

        user_user_reset_password = cls(
            password=password,
            token=token,
        )

        user_user_reset_password.additional_properties = d
        return user_user_reset_password

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
