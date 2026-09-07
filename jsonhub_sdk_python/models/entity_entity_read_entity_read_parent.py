from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition_entity_read_entity_read_parent import DefinitionEntityReadEntityReadParent
    from ..models.entity_entity_read_entity_read_parent_data import EntityEntityReadEntityReadParentData


T = TypeVar("T", bound="EntityEntityReadEntityReadParent")


@_attrs_define
class EntityEntityReadEntityReadParent:
    """
    Attributes:
        id (Union[None, UUID, Unset]):
        slug (Union[None, Unset, str]):
        data (Union[Unset, EntityEntityReadEntityReadParentData]):
        definition (Union['DefinitionEntityReadEntityReadParent', None, Unset]):
        parent (Union[None, Unset, str]):
        private (Union[Unset, bool]):  Default: False.
        is_owned_by_current_user (Union[Unset, bool]):  Default: False.
    """

    id: Union[None, UUID, Unset] = UNSET
    slug: Union[None, Unset, str] = UNSET
    data: Union[Unset, "EntityEntityReadEntityReadParentData"] = UNSET
    definition: Union["DefinitionEntityReadEntityReadParent", None, Unset] = UNSET
    parent: Union[None, Unset, str] = UNSET
    private: Union[Unset, bool] = False
    is_owned_by_current_user: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.definition_entity_read_entity_read_parent import DefinitionEntityReadEntityReadParent

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

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        definition: Union[None, Unset, dict[str, Any]]
        if isinstance(self.definition, Unset):
            definition = UNSET
        elif isinstance(self.definition, DefinitionEntityReadEntityReadParent):
            definition = self.definition.to_dict()
        else:
            definition = self.definition

        parent: Union[None, Unset, str]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        private = self.private

        is_owned_by_current_user = self.is_owned_by_current_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        if is_owned_by_current_user is not UNSET:
            field_dict["isOwnedByCurrentUser"] = is_owned_by_current_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition_entity_read_entity_read_parent import DefinitionEntityReadEntityReadParent
        from ..models.entity_entity_read_entity_read_parent_data import EntityEntityReadEntityReadParentData

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

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        _data = d.pop("data", UNSET)
        data: Union[Unset, EntityEntityReadEntityReadParentData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EntityEntityReadEntityReadParentData.from_dict(_data)

        def _parse_definition(data: object) -> Union["DefinitionEntityReadEntityReadParent", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                definition_type_0 = DefinitionEntityReadEntityReadParent.from_dict(data)

                return definition_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DefinitionEntityReadEntityReadParent", None, Unset], data)

        definition = _parse_definition(d.pop("definition", UNSET))

        def _parse_parent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        private = d.pop("private", UNSET)

        is_owned_by_current_user = d.pop("isOwnedByCurrentUser", UNSET)

        entity_entity_read_entity_read_parent = cls(
            id=id,
            slug=slug,
            data=data,
            definition=definition,
            parent=parent,
            private=private,
            is_owned_by_current_user=is_owned_by_current_user,
        )

        entity_entity_read_entity_read_parent.additional_properties = d
        return entity_entity_read_entity_read_parent

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
