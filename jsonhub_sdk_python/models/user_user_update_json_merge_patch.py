from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUserUpdateJsonMergePatch")


@_attrs_define
class UserUserUpdateJsonMergePatch:
    """Change user password

    Attributes:
        password (Union[None, Unset, str]):
        old_password (Union[None, Unset, str]):
    """

    password: Union[None, Unset, str] = UNSET
    old_password: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        old_password: Union[None, Unset, str]
        if isinstance(self.old_password, Unset):
            old_password = UNSET
        else:
            old_password = self.old_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_old_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        old_password = _parse_old_password(d.pop("oldPassword", UNSET))

        user_user_update_json_merge_patch = cls(
            password=password,
            old_password=old_password,
        )

        user_user_update_json_merge_patch.additional_properties = d
        return user_user_update_json_merge_patch

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
