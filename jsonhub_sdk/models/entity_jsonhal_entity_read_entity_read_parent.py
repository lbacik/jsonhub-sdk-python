from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition_entity_read_entity_read_parent import DefinitionEntityReadEntityReadParent
    from ..models.entity_entity_read_entity_read_parent_data import EntityEntityReadEntityReadParentData
    from ..models.entity_jsonhal_entity_read_entity_read_parent_links import (
        EntityJsonhalEntityReadEntityReadParentLinks,
    )


T = TypeVar("T", bound="EntityJsonhalEntityReadEntityReadParent")


@_attrs_define
class EntityJsonhalEntityReadEntityReadParent:
    """
    Attributes:
        id (UUID):
        definition (Union['DefinitionEntityReadEntityReadParent', None]):
        is_owned_by_current_user (bool):  Default: False.
        slug (Union[None, Unset, str]):
        data (Union[Unset, EntityEntityReadEntityReadParentData]):
        parent (Union[None, Unset, str]):
        private (Union[Unset, bool]):  Default: False.
        field_links (Union[Unset, EntityJsonhalEntityReadEntityReadParentLinks]):
    """

    id: UUID
    definition: Union["DefinitionEntityReadEntityReadParent", None]
    is_owned_by_current_user: bool = False
    slug: Union[None, Unset, str] = UNSET
    data: Union[Unset, "EntityEntityReadEntityReadParentData"] = UNSET
    parent: Union[None, Unset, str] = UNSET
    private: Union[Unset, bool] = False
    field_links: Union[Unset, "EntityJsonhalEntityReadEntityReadParentLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.definition_entity_read_entity_read_parent import DefinitionEntityReadEntityReadParent

        id = str(self.id)

        definition: Union[None, dict[str, Any]]
        if isinstance(self.definition, DefinitionEntityReadEntityReadParent):
            definition = self.definition.to_dict()
        else:
            definition = self.definition

        is_owned_by_current_user = self.is_owned_by_current_user

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        parent: Union[None, Unset, str]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        private = self.private

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "definition": definition,
                "isOwnedByCurrentUser": is_owned_by_current_user,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if data is not UNSET:
            field_dict["data"] = data
        if parent is not UNSET:
            field_dict["parent"] = parent
        if private is not UNSET:
            field_dict["private"] = private
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition_entity_read_entity_read_parent import DefinitionEntityReadEntityReadParent
        from ..models.entity_entity_read_entity_read_parent_data import EntityEntityReadEntityReadParentData
        from ..models.entity_jsonhal_entity_read_entity_read_parent_links import (
            EntityJsonhalEntityReadEntityReadParentLinks,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_definition(data: object) -> Union["DefinitionEntityReadEntityReadParent", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                definition_type_0 = DefinitionEntityReadEntityReadParent.from_dict(data)

                return definition_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DefinitionEntityReadEntityReadParent", None], data)

        definition = _parse_definition(d.pop("definition"))

        is_owned_by_current_user = d.pop("isOwnedByCurrentUser")

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

        def _parse_parent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        private = d.pop("private", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, EntityJsonhalEntityReadEntityReadParentLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = EntityJsonhalEntityReadEntityReadParentLinks.from_dict(_field_links)

        entity_jsonhal_entity_read_entity_read_parent = cls(
            id=id,
            definition=definition,
            is_owned_by_current_user=is_owned_by_current_user,
            slug=slug,
            data=data,
            parent=parent,
            private=private,
            field_links=field_links,
        )

        entity_jsonhal_entity_read_entity_read_parent.additional_properties = d
        return entity_jsonhal_entity_read_entity_read_parent

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
