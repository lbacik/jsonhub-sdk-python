from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_jsonhal_links import UserJsonhalLinks


T = TypeVar("T", bound="UserJsonhal")


@_attrs_define
class UserJsonhal:
    """
    Attributes:
        id (UUID):
        email (Union[None, str]):
        password (Union[None, Unset, str]):
        old_password (Union[None, Unset, str]):
        token (Union[None, Unset, str]):
        field_links (Union[Unset, UserJsonhalLinks]):
    """

    id: UUID
    email: Union[None, str]
    password: Union[None, Unset, str] = UNSET
    old_password: Union[None, Unset, str] = UNSET
    token: Union[None, Unset, str] = UNSET
    field_links: Union[Unset, "UserJsonhalLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email: Union[None, str]
        email = self.email

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

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password
        if token is not UNSET:
            field_dict["token"] = token
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_jsonhal_links import UserJsonhalLinks

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

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

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, UserJsonhalLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UserJsonhalLinks.from_dict(_field_links)

        user_jsonhal = cls(
            id=id,
            email=email,
            password=password,
            old_password=old_password,
            token=token,
            field_links=field_links,
        )

        user_jsonhal.additional_properties = d
        return user_jsonhal

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
