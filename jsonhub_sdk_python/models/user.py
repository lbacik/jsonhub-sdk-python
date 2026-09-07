from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        email (Union[None, str]):
        id (Union[None, UUID, Unset]):
        password (Union[None, Unset, str]):
        old_password (Union[None, Unset, str]):
        token (Union[None, Unset, str]):
        reset_password_link (Union[None, Unset, str]):
        activation_url (Union[None, Unset, str]):
    """

    email: Union[None, str]
    id: Union[None, UUID, Unset] = UNSET
    password: Union[None, Unset, str] = UNSET
    old_password: Union[None, Unset, str] = UNSET
    token: Union[None, Unset, str] = UNSET
    reset_password_link: Union[None, Unset, str] = UNSET
    activation_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[None, str]
        email = self.email

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        token: Union[None, Unset, str]
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        reset_password_link: Union[None, Unset, str]
        if isinstance(self.reset_password_link, Unset):
            reset_password_link = UNSET
        else:
            reset_password_link = self.reset_password_link

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
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if password is not UNSET:
            field_dict["password"] = password
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password
        if token is not UNSET:
            field_dict["token"] = token
        if reset_password_link is not UNSET:
            field_dict["resetPasswordLink"] = reset_password_link
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

        def _parse_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        token = _parse_token(d.pop("token", UNSET))

        def _parse_reset_password_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reset_password_link = _parse_reset_password_link(d.pop("resetPasswordLink", UNSET))

        def _parse_activation_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        activation_url = _parse_activation_url(d.pop("activationUrl", UNSET))

        user = cls(
            email=email,
            id=id,
            password=password,
            old_password=old_password,
            token=token,
            reset_password_link=reset_password_link,
            activation_url=activation_url,
        )

        user.additional_properties = d
        return user

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
