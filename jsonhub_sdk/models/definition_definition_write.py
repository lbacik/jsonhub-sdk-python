from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition_definition_write_json_schema import DefinitionDefinitionWriteJsonSchema


T = TypeVar("T", bound="DefinitionDefinitionWrite")


@_attrs_define
class DefinitionDefinitionWrite:
    """
    Attributes:
        json_schema (DefinitionDefinitionWriteJsonSchema):
        slug (Union[None, Unset, str]):
        parent_entity (Union[None, Unset, str]):  Example: https://example.com/.
    """

    json_schema: "DefinitionDefinitionWriteJsonSchema"
    slug: Union[None, Unset, str] = UNSET
    parent_entity: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_schema = self.json_schema.to_dict()

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        parent_entity: Union[None, Unset, str]
        if isinstance(self.parent_entity, Unset):
            parent_entity = UNSET
        else:
            parent_entity = self.parent_entity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonSchema": json_schema,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if parent_entity is not UNSET:
            field_dict["parentEntity"] = parent_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition_definition_write_json_schema import DefinitionDefinitionWriteJsonSchema

        d = dict(src_dict)
        json_schema = DefinitionDefinitionWriteJsonSchema.from_dict(d.pop("jsonSchema"))

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_parent_entity(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_entity = _parse_parent_entity(d.pop("parentEntity", UNSET))

        definition_definition_write = cls(
            json_schema=json_schema,
            slug=slug,
            parent_entity=parent_entity,
        )

        definition_definition_write.additional_properties = d
        return definition_definition_write

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
