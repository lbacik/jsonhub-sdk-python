from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition_definition_write_json_merge_patch_json_schema import (
        DefinitionDefinitionWriteJsonMergePatchJsonSchema,
    )


T = TypeVar("T", bound="DefinitionDefinitionWriteJsonMergePatch")


@_attrs_define
class DefinitionDefinitionWriteJsonMergePatch:
    """
    Attributes:
        slug (Union[None, Unset, str]):
        json_schema (Union[Unset, DefinitionDefinitionWriteJsonMergePatchJsonSchema]):
        parent_entity (Union[None, Unset, str]):  Example: https://example.com/.
    """

    slug: Union[None, Unset, str] = UNSET
    json_schema: Union[Unset, "DefinitionDefinitionWriteJsonMergePatchJsonSchema"] = UNSET
    parent_entity: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        json_schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.json_schema, Unset):
            json_schema = self.json_schema.to_dict()

        parent_entity: Union[None, Unset, str]
        if isinstance(self.parent_entity, Unset):
            parent_entity = UNSET
        else:
            parent_entity = self.parent_entity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if json_schema is not UNSET:
            field_dict["jsonSchema"] = json_schema
        if parent_entity is not UNSET:
            field_dict["parentEntity"] = parent_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition_definition_write_json_merge_patch_json_schema import (
            DefinitionDefinitionWriteJsonMergePatchJsonSchema,
        )

        d = dict(src_dict)

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _json_schema = d.pop("jsonSchema", UNSET)
        json_schema: Union[Unset, DefinitionDefinitionWriteJsonMergePatchJsonSchema]
        if isinstance(_json_schema, Unset):
            json_schema = UNSET
        else:
            json_schema = DefinitionDefinitionWriteJsonMergePatchJsonSchema.from_dict(_json_schema)

        def _parse_parent_entity(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_entity = _parse_parent_entity(d.pop("parentEntity", UNSET))

        definition_definition_write_json_merge_patch = cls(
            slug=slug,
            json_schema=json_schema,
            parent_entity=parent_entity,
        )

        definition_definition_write_json_merge_patch.additional_properties = d
        return definition_definition_write_json_merge_patch

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
