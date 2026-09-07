from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserUserSendResetPassword")


@_attrs_define
class UserUserSendResetPassword:
    """
    Attributes:
        email (Union[None, str]):
        reset_password_link (Union[None, str]):
    """

    email: Union[None, str]
    reset_password_link: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[None, str]
        email = self.email

        reset_password_link: Union[None, str]
        reset_password_link = self.reset_password_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "resetPasswordLink": reset_password_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        def _parse_reset_password_link(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reset_password_link = _parse_reset_password_link(d.pop("resetPasswordLink"))

        user_user_send_reset_password = cls(
            email=email,
            reset_password_link=reset_password_link,
        )

        user_user_send_reset_password.additional_properties = d
        return user_user_send_reset_password

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
