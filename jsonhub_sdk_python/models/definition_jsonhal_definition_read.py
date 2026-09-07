from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition_definition_read_json_schema import DefinitionDefinitionReadJsonSchema
    from ..models.definition_jsonhal_definition_read_links import DefinitionJsonhalDefinitionReadLinks
    from ..models.entity_definition_read import EntityDefinitionRead


T = TypeVar("T", bound="DefinitionJsonhalDefinitionRead")


@_attrs_define
class DefinitionJsonhalDefinitionRead:
    """
    Attributes:
        json_schema (DefinitionDefinitionReadJsonSchema):
        id (Union[None, UUID, Unset]):
        slug (Union[None, Unset, str]):
        parent_entity (Union['EntityDefinitionRead', None, Unset]):
        is_owned_by_current_user (Union[Unset, bool]):  Default: False.
        field_links (Union[Unset, DefinitionJsonhalDefinitionReadLinks]):
    """

    json_schema: "DefinitionDefinitionReadJsonSchema"
    id: Union[None, UUID, Unset] = UNSET
    slug: Union[None, Unset, str] = UNSET
    parent_entity: Union["EntityDefinitionRead", None, Unset] = UNSET
    is_owned_by_current_user: Union[Unset, bool] = False
    field_links: Union[Unset, "DefinitionJsonhalDefinitionReadLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_definition_read import EntityDefinitionRead

        json_schema = self.json_schema.to_dict()

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        parent_entity: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent_entity, Unset):
            parent_entity = UNSET
        elif isinstance(self.parent_entity, EntityDefinitionRead):
            parent_entity = self.parent_entity.to_dict()
        else:
            parent_entity = self.parent_entity

        is_owned_by_current_user = self.is_owned_by_current_user

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonSchema": json_schema,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if parent_entity is not UNSET:
            field_dict["parentEntity"] = parent_entity
        if is_owned_by_current_user is not UNSET:
            field_dict["isOwnedByCurrentUser"] = is_owned_by_current_user
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition_definition_read_json_schema import DefinitionDefinitionReadJsonSchema
        from ..models.definition_jsonhal_definition_read_links import DefinitionJsonhalDefinitionReadLinks
        from ..models.entity_definition_read import EntityDefinitionRead

        d = dict(src_dict)
        json_schema = DefinitionDefinitionReadJsonSchema.from_dict(d.pop("jsonSchema"))

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

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_parent_entity(data: object) -> Union["EntityDefinitionRead", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_entity_type_0 = EntityDefinitionRead.from_dict(data)

                return parent_entity_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EntityDefinitionRead", None, Unset], data)

        parent_entity = _parse_parent_entity(d.pop("parentEntity", UNSET))

        is_owned_by_current_user = d.pop("isOwnedByCurrentUser", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, DefinitionJsonhalDefinitionReadLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = DefinitionJsonhalDefinitionReadLinks.from_dict(_field_links)

        definition_jsonhal_definition_read = cls(
            json_schema=json_schema,
            id=id,
            slug=slug,
            parent_entity=parent_entity,
            is_owned_by_current_user=is_owned_by_current_user,
            field_links=field_links,
        )

        definition_jsonhal_definition_read.additional_properties = d
        return definition_jsonhal_definition_read

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
