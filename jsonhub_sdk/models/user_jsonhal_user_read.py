from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_jsonhal_user_read_links import UserJsonhalUserReadLinks


T = TypeVar("T", bound="UserJsonhalUserRead")


@_attrs_define
class UserJsonhalUserRead:
    """Create user

    Attributes:
        id (UUID):
        email (Union[None, str]):
        field_links (Union[Unset, UserJsonhalUserReadLinks]):
    """

    id: UUID
    email: Union[None, str]
    field_links: Union[Unset, "UserJsonhalUserReadLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email: Union[None, str]
        email = self.email

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
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_jsonhal_user_read_links import UserJsonhalUserReadLinks

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, UserJsonhalUserReadLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UserJsonhalUserReadLinks.from_dict(_field_links)

        user_jsonhal_user_read = cls(
            id=id,
            email=email,
            field_links=field_links,
        )

        user_jsonhal_user_read.additional_properties = d
        return user_jsonhal_user_read

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
