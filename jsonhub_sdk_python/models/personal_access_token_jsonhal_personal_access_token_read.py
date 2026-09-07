import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.personal_access_token_jsonhal_personal_access_token_read_links import (
        PersonalAccessTokenJsonhalPersonalAccessTokenReadLinks,
    )


T = TypeVar("T", bound="PersonalAccessTokenJsonhalPersonalAccessTokenRead")


@_attrs_define
class PersonalAccessTokenJsonhalPersonalAccessTokenRead:
    """
    Attributes:
        id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):
        token_preview (Union[None, Unset, str]):
        expires_at (Union[None, Unset, datetime.datetime]):
        created_at (Union[None, Unset, datetime.datetime]):
        field_links (Union[Unset, PersonalAccessTokenJsonhalPersonalAccessTokenReadLinks]):
    """

    id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    token_preview: Union[None, Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "PersonalAccessTokenJsonhalPersonalAccessTokenReadLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        token_preview: Union[None, Unset, str]
        if isinstance(self.token_preview, Unset):
            token_preview = UNSET
        else:
            token_preview = self.token_preview

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if token_preview is not UNSET:
            field_dict["tokenPreview"] = token_preview
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.personal_access_token_jsonhal_personal_access_token_read_links import (
            PersonalAccessTokenJsonhalPersonalAccessTokenReadLinks,
        )

        d = dict(src_dict)

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_token_preview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        token_preview = _parse_token_preview(d.pop("tokenPreview", UNSET))

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

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, PersonalAccessTokenJsonhalPersonalAccessTokenReadLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PersonalAccessTokenJsonhalPersonalAccessTokenReadLinks.from_dict(_field_links)

        personal_access_token_jsonhal_personal_access_token_read = cls(
            id=id,
            name=name,
            token_preview=token_preview,
            expires_at=expires_at,
            created_at=created_at,
            field_links=field_links,
        )

        personal_access_token_jsonhal_personal_access_token_read.additional_properties = d
        return personal_access_token_jsonhal_personal_access_token_read

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
