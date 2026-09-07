from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_entity_create_data import EntityEntityCreateData


T = TypeVar("T", bound="EntityEntityCreate")


@_attrs_define
class EntityEntityCreate:
    """
    Attributes:
        slug (Union[None, Unset, str]):
        data (Union[Unset, EntityEntityCreateData]):
        definition (Union[None, Unset, str]):  Example: https://example.com/.
        parent (Union[None, Unset, str]):
        private (Union[Unset, bool]):  Default: False.
    """

    slug: Union[None, Unset, str] = UNSET
    data: Union[Unset, "EntityEntityCreateData"] = UNSET
    definition: Union[None, Unset, str] = UNSET
    parent: Union[None, Unset, str] = UNSET
    private: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        definition: Union[None, Unset, str]
        if isinstance(self.definition, Unset):
            definition = UNSET
        else:
            definition = self.definition

        parent: Union[None, Unset, str]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        private = self.private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if data is not UNSET:
            field_dict["data"] = data
        if definition is not UNSET:
            field_dict["definition"] = definition
        if parent is not UNSET:
            field_dict["parent"] = parent
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_entity_create_data import EntityEntityCreateData

        d = dict(src_dict)

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityEntityCreateData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EntityEntityCreateData.from_dict(_data)

        def _parse_definition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        definition = _parse_definition(d.pop("definition", UNSET))

        def _parse_parent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        private = d.pop("private", UNSET)

        entity_entity_create = cls(
            slug=slug,
            data=data,
            definition=definition,
            parent=parent,
            private=private,
        )

        entity_entity_create.additional_properties = d
        return entity_entity_create

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
