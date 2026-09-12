import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.personal_access_token_jsonhal_personal_access_token_read_personal_access_token_create_read_links import (
        PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateReadLinks,
    )


T = TypeVar("T", bound="PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateRead")


@_attrs_define
class PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateRead:
    """
    Attributes:
        id (UUID):
        token_preview (str):
        token (str):
        created_at (datetime.datetime):
        name (Union[None, Unset, str]):
        expires_at (Union[None, Unset, datetime.datetime]):
        field_links (Union[Unset, PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateReadLinks]):
    """

    id: UUID
    token_preview: str
    token: str
    created_at: datetime.datetime
    name: Union[None, Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateReadLinks"] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        token_preview = self.token_preview

        token = self.token

        created_at = self.created_at.isoformat()

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tokenPreview": token_preview,
                "token": token,
                "createdAt": created_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personal_access_token_jsonhal_personal_access_token_read_personal_access_token_create_read_links import (
            PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateReadLinks,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        token_preview = d.pop("tokenPreview")

        token = d.pop("token")

        created_at = isoparse(d.pop("createdAt"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateReadLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PersonalAccessTokenJsonhalPersonalAccessTokenReadPersonalAccessTokenCreateReadLinks.from_dict(
                _field_links
            )

        personal_access_token_jsonhal_personal_access_token_read_personal_access_token_create_read = cls(
            id=id,
            token_preview=token_preview,
            token=token,
            created_at=created_at,
            name=name,
            expires_at=expires_at,
            field_links=field_links,
        )

        personal_access_token_jsonhal_personal_access_token_read_personal_access_token_create_read.additional_properties = d
        return personal_access_token_jsonhal_personal_access_token_read_personal_access_token_create_read

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
